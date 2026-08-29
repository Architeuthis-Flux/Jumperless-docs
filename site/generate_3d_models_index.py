"""
Generate docs/assets/3Dstands/index.json listing every 3D model in that folder.

The stl-viewer web component fetches this manifest so any model dropped into
docs/assets/3Dstands/ shows up automatically (no code edits). Files that share
a base name are grouped into one model with multiple download formats, e.g.
JumperlessStandProbeHolder.stl + .step + .3mf -> one entry, three downloads.

Runs during the MkDocs build (on_post_build) so it regenerates whenever a model
is added, removed, or renamed. URLs are site-root-relative so the same manifest
works locally (mkdocs serve) and in production.

Usage:
  python docs/generate_3d_models_index.py [models_dir] [output_path]
  Or let MkDocs run it via the on_post_build hook.
"""

import json
import os
import re
import sys

# Formats that can be previewed in the viewer, plus CAD/source-only downloads.
PREVIEW_EXTS = ("stl", "3mf", "obj", "ply", "gltf", "glb")
DOWNLOAD_EXTS = PREVIEW_EXTS + ("step", "stp")

# Base names (without extension) to keep in the folder but hide from the viewer.
EXCLUDE = frozenset({
    "JumperlessAndProbe",  # kept for reuse elsewhere, not a printable stand
})


def _prettify(base):
    """JumperlessStandProbeHolder -> 'Jumperless Stand Probe Holder'."""
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", base)   # split camelCase
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", s)     # split ABCd -> AB Cd
    s = s.replace("_", " ").replace("-", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s or base


def build_models(models_dir, base_url=""):
    """Group model files by base name into {label, files:{ext:url}} entries."""
    base_url = base_url.rstrip("/")
    groups = {}
    order = []
    for fn in sorted(os.listdir(models_dir), reverse=True):
        path = os.path.join(models_dir, fn)
        if not os.path.isfile(path):
            continue
        base, ext = os.path.splitext(fn)
        ext = ext.lstrip(".").lower()
        if ext not in DOWNLOAD_EXTS or base in EXCLUDE:
            continue
        if base not in groups:
            groups[base] = {}
            order.append(base)
        groups[base][ext] = f"{base_url}/assets/3Dstands/{fn}"

    models = []
    for base in order:
        label = _prettify(base)
        # Drop the shared "Jumperless Stand" prefix so buttons stay short.
        label = re.sub(r"^Jumperless Stand\s*", "", label).strip() or label
        models.append({"label": label, "files": groups[base]})
    return models


def generate_index(models_dir, output_path, base_url=""):
    models = build_models(models_dir, base_url)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"models": models}, f, indent=2)
    return len(models)


def on_post_build(config):
    """MkDocs hook: write assets/3Dstands/index.json into the built site."""
    site_dir = config["site_dir"]
    docs_dir = config["docs_dir"]

    models_dir = os.path.join(docs_dir, "assets", "3Dstands")
    output_path = os.path.join(site_dir, "assets", "3Dstands", "index.json")

    if not os.path.isdir(models_dir):
        print("⚠ No docs/assets/3Dstands directory, skipping 3D models index")
        return

    n = generate_index(models_dir, output_path)
    print(f"✓ Generated 3D models index: {output_path} ({n} models)")


if __name__ == "__main__":
    this_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(this_dir, "assets", "3Dstands")
    output = sys.argv[2] if len(sys.argv) > 2 else os.path.join(models_dir, "index.json")
    if not os.path.isdir(models_dir):
        print("Models directory not found:", models_dir, file=sys.stderr)
        sys.exit(1)
    n = generate_index(models_dir, output)
    print(f"Wrote {output} ({n} models)")
