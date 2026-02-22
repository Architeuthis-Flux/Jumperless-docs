"""
Generate docs/scripts/index.json from all .py files in docs/scripts/.

Used by JumperIDE to list scripts (name, description, url). Run during MkDocs
build so the index is regenerated whenever scripts are added or changed.

Usage:
  python docs/generate_scripts_index.py [docs_dir] [output_path] [base_url]
  Or let MkDocs run it via the on_post_build hook.
"""

import json
import os
import re
import sys

# Files to exclude from the index (utilities, incomplete, etc.)
EXCLUDE = frozenset({
    "fuck.py",
    "listFiles.py",
    "viperide_reinit.py",
})


def _filename_to_name(basename):
    """Turn script filename into display name: overlay_probe_move -> Overlay Probe Move."""
    name = os.path.splitext(basename)[0]
    return name.replace("_", " ").strip().title() or basename


def _extract_from_py(content, filename):
    """
    Extract script name and description from .py file content.
    Supports:
      - Docstring: first line = name, second line or rest = description
      - First # comment block = description; name from filename
      - # script-name: ... and # script-description: ... override
    """
    name = None
    description = None
    lines = content.splitlines()

    # Override lines
    for line in lines[:30]:
        s = line.strip()
        if s.startswith("# script-name:"):
            name = s.split(":", 1)[1].strip()
        elif s.startswith("# script-description:"):
            description = s.split(":", 1)[1].strip()

    if name is not None and description is not None:
        return (name, description)

    # Docstring
    if content.lstrip().startswith('"""'):
        match = re.match(r'\s*"""\s*(.*?)(?:"""|\n)', content, re.DOTALL)
        if match:
            block = match.group(1).strip()
            parts = [p.strip() for p in block.split("\n", 1)]
            if not name and parts:
                name = parts[0].strip('"\'')
            if not description and len(parts) > 1:
                description = parts[1].split("\n")[0].strip()[:200]
            elif not description and len(parts) == 1 and len(parts[0]) > 60:
                description = parts[0][:200]
    elif content.lstrip().startswith("'''"):
        match = re.match(r"\s*'''\s*(.*?)(?:'''|\n)", content, re.DOTALL)
        if match:
            block = match.group(1).strip()
            parts = [p.strip() for p in block.split("\n", 1)]
            if not name and parts:
                name = parts[0].strip('"\'')
            if not description and len(parts) > 1:
                description = parts[1].split("\n")[0].strip()[:200]
            elif not description and len(parts) == 1 and len(parts[0]) > 60:
                description = parts[0][:200]

    # First # comment (not script-name/script-description)
    if not description:
        for line in lines[:15]:
            line = line.strip()
            if line.startswith("#") and "script-" not in line:
                desc = line.lstrip("#").strip()
                if desc and len(desc) > 2:
                    description = desc[:200]
                    break

    if not name:
        name = _filename_to_name(filename)
    if not description:
        description = ""

    return (name, description)


def build_scripts_index(scripts_dir, base_url):
    """Scan scripts_dir for .py files and return list of {name, description, url}."""
    base_url = base_url.rstrip("/")
    entries = []
    if not os.path.isdir(scripts_dir):
        return entries

    for fn in sorted(os.listdir(scripts_dir)):
        if not fn.endswith(".py") or fn in EXCLUDE:
            continue
        path = os.path.join(scripts_dir, fn)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception:
            content = ""
        name, description = _extract_from_py(content, fn)
        url = f"{base_url}/scripts/{fn}"
        entries.append({"name": name, "description": description, "url": url})

    return entries


def generate_index(scripts_dir, output_path, base_url="https://docs.jumperless.org"):
    """Write index.json to output_path."""
    entries = build_scripts_index(scripts_dir, base_url)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"scripts": entries}, f, indent=2)
    return len(entries)


def on_post_build(config):
    """
    MkDocs hook: after site is built, generate scripts/index.json in the site
    so JumperIDE can load the script list. Regenerates when files are added.
    """
    site_dir = config["site_dir"]
    docs_dir = config["docs_dir"]
    site_url = config.get("site_url", "https://docs.jumperless.org").rstrip("/")

    scripts_dir = os.path.join(docs_dir, "scripts")
    output_path = os.path.join(site_dir, "scripts", "index.json")

    if not os.path.isdir(scripts_dir):
        print("⚠ No docs/scripts directory, skipping scripts index")
        return

    n = generate_index(scripts_dir, output_path, site_url)
    print(f"✓ Generated scripts index: {output_path} ({n} scripts)")


if __name__ == "__main__":
    this_dir = os.path.dirname(os.path.abspath(__file__))
    # Default: docs_dir is the folder containing this script (docs/)
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else this_dir
    scripts_dir = os.path.join(docs_dir, "scripts")
    output = sys.argv[2] if len(sys.argv) > 2 else os.path.join(scripts_dir, "index.json")
    base_url = sys.argv[3] if len(sys.argv) > 3 else "https://docs.jumperless.org"

    if not os.path.isdir(scripts_dir):
        scripts_dir = os.path.join(this_dir, "scripts")
    if not os.path.isdir(scripts_dir):
        print("Scripts directory not found:", scripts_dir, file=sys.stderr)
        sys.exit(1)

    n = generate_index(scripts_dir, output, base_url)
    print(f"Wrote {output} ({n} scripts)")
