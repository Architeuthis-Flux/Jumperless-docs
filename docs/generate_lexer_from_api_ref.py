"""
Regenerate JUMPERLESS_FUNCTIONS in docs/lexers/jumperless_lexer.py from:
1) C source of truth: modjumperless.c jumperless_module_globals_table + module_stubs.c
2) MicroPython API reference (09.5-micropythonAPIreference.md)
3) jumperless_module.py re-exports (functions + aliases)
Run from repo root or docs/: python docs/generate_lexer_from_api_ref.py
Set JUMPERLESS_MOD_C to path to modjumperless.c if not using default.
Set JUMPERLESS_MODULE_PY to path to jumperless_module.py if not using default.
"""
from pathlib import Path
import os
import re

# Paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_DIR = SCRIPT_DIR
API_REF_MD = DOCS_DIR / "09.5-micropythonAPIreference.md"
LEXER_PY = DOCS_DIR / "lexers" / "jumperless_lexer.py"

# Optional: modjumperless.c (JumperlOS) - source of truth for exported symbols
def _mod_c_candidates():
    env_path = os.environ.get("JUMPERLESS_MOD_C", "").strip()
    base = SCRIPT_DIR.parent.parent
    parent = base.parent
    candidates = []
    if env_path:
        candidates.append(Path(env_path))
    candidates.extend([
        parent / "JumperlOS" / "modules" / "jumperless" / "modjumperless.c",
        base / "JumperlOS" / "modules" / "jumperless" / "modjumperless.c",
    ])
    for p in candidates:
        if p and p.is_file():
            return p
    return None

def _stubs_candidates():
    mod_path = _mod_c_candidates()
    if mod_path:
        stubs = mod_path.parent / "module_stubs.c"
        if stubs.is_file():
            return stubs
    return None

# Optional: jumperless_module.py (JumperlOS) for aliases + all re-exports
def _module_candidates():
    env_path = os.environ.get("JUMPERLESS_MODULE_PY", "").strip()
    base = SCRIPT_DIR.parent.parent
    candidates = []
    if env_path:
        candidates.append(Path(env_path))
    parent = base.parent
    candidates.extend([
        parent / "JumperlOS" / "scripts" / "jumperless_module.py",
        base / "JumperlOS" / "scripts" / "jumperless_module.py",
        base / "jumperless_module.py",
        SCRIPT_DIR / "scripts" / "jumperless_module.py",
    ])
    for p in candidates:
        if p and p.is_file():
            return p
    return None

HEADING_RE = re.compile(r'^### `([^`]+)`\s*$', re.MULTILINE)
NATIVE_RE = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*_native\.', re.MULTILINE)
# C: MP_QSTR_(name) on a line that has MP_ROM_PTR (function/object entry in globals table)
C_QSTR_PTR_RE = re.compile(r'MP_QSTR_([a-zA-Z0-9_]+).*?MP_ROM_PTR', re.DOTALL)
# module_stubs.c: MP_QSTR_<name> in forced qstrs array
STUBS_QSTR_RE = re.compile(r'MP_QSTR_([a-zA-Z0-9_]+)')


def extract_function_names_from_api_ref(content: str) -> list[str]:
    names = []
    for m in HEADING_RE.finditer(content):
        heading = m.group(1)
        name = heading.split("(")[0].strip().lower().replace("-", "_")
        names.append(name)
    return names


def extract_names_from_module(content: str) -> list[str]:
    """All names re-exported as name = _native.xxx. Exclude constants (all-uppercase)."""
    names = []
    for m in NATIVE_RE.finditer(content):
        name = m.group(1)
        if name.startswith("_"):
            continue
        if name.replace("_", "").isupper():
            continue
        names.append(name)
    return names


def _is_function_like(name: str) -> bool:
    """True if name is a function/callable (not constant, not dunder)."""
    if name.startswith("__") and name.endswith("__"):
        return False
    if name.replace("_", "").isupper():
        return False
    return True


def extract_function_names_from_c(content: str) -> list[str]:
    """Parse jumperless_module_globals_table in modjumperless.c; return function-like names from PTR entries."""
    start_marker = "jumperless_module_globals_table[] = {"
    end_marker = "\n};\n\nstatic MP_DEFINE_CONST_DICT"
    start = content.find(start_marker)
    if start == -1:
        return []
    block_start = start + len(start_marker)
    end = content.find(end_marker, block_start)
    if end == -1:
        return []
    table_block = content[block_start:end]
    names = []
    for line in table_block.splitlines():
        if "MP_ROM_PTR" not in line:
            continue
        for m in C_QSTR_PTR_RE.finditer(line):
            name = m.group(1)
            if _is_function_like(name):
                names.append(name)
    return names


def extract_function_names_from_stubs(content: str) -> list[str]:
    """Parse _jl_forced_qstrs in module_stubs.c; return function-like names."""
    # Look for the array block
    start = content.find("_jl_forced_qstrs[] = {")
    if start == -1:
        return []
    block = content[start : start + 1024]
    names = []
    for m in STUBS_QSTR_RE.finditer(block):
        name = m.group(1)
        if _is_function_like(name):
            names.append(name)
    return names


def main() -> None:
    names_set = set()

    # 1) C source of truth: modjumperless.c globals table
    mod_c_path = _mod_c_candidates()
    if mod_c_path:
        try:
            c_content = mod_c_path.read_text(encoding="utf-8")
            names_set.update(extract_function_names_from_c(c_content))
        except Exception as e:
            print(f"[generate_lexer_from_api_ref] Could not read modjumperless.c: {e}")

    # 2) module_stubs.c forced qstrs (new symbols)
    stubs_path = _stubs_candidates()
    if stubs_path:
        try:
            stubs_content = stubs_path.read_text(encoding="utf-8")
            names_set.update(extract_function_names_from_stubs(stubs_content))
        except Exception as e:
            print(f"[generate_lexer_from_api_ref] Could not read module_stubs.c: {e}")

    # 3) API reference (docs)
    if API_REF_MD.exists():
        api_content = API_REF_MD.read_text(encoding="utf-8")
        names_set.update(extract_function_names_from_api_ref(api_content))
    else:
        print(f"[generate_lexer_from_api_ref] Not found: {API_REF_MD}")

    # 4) jumperless_module.py re-exports (aliases)
    module_path = _module_candidates()
    if module_path:
        try:
            module_content = module_path.read_text(encoding="utf-8")
            names_set.update(extract_names_from_module(module_content))
        except Exception as e:
            print(f"[generate_lexer_from_api_ref] Could not read module: {e}")
    elif os.environ.get("JUMPERLESS_MODULE_PY"):
        print(f"[generate_lexer_from_api_ref] Not found: {os.environ['JUMPERLESS_MODULE_PY']}")

    names = sorted(names_set)
    if not names:
        print("[generate_lexer_from_api_ref] No function names collected")
        return

    if not LEXER_PY.exists():
        print(f"[generate_lexer_from_api_ref] Not found: {LEXER_PY}")
        return

    lexer_content = LEXER_PY.read_text(encoding="utf-8")

    # Replace JUMPERLESS_FUNCTIONS = { ... } with generated set
    start_marker = "    JUMPERLESS_FUNCTIONS = {"
    end_marker = "    }\n\n    JUMPERLESS_CONSTANTS = {"

    start = lexer_content.find(start_marker)
    end = lexer_content.find(end_marker, start)
    if start == -1 or end == -1:
        print("[generate_lexer_from_api_ref] Could not find JUMPERLESS_FUNCTIONS block in lexer")
        return

    # Build new set as Python source (sorted, one per line, quoted)
    lines = ["    JUMPERLESS_FUNCTIONS = {"]
    for n in names:
        lines.append(f"        {repr(n)},")
    lines.append("    }")
    new_block = "\n".join(lines)

    before = lexer_content[:start]
    after = lexer_content[end : end + len(end_marker)] + lexer_content[end + len(end_marker) :]
    new_content = before + new_block + "\n\n    JUMPERLESS_CONSTANTS = {" + lexer_content[end + len(end_marker) :]

    LEXER_PY.write_text(new_content, encoding="utf-8")
    print(f"[generate_lexer_from_api_ref] Updated {LEXER_PY.name} with {len(names)} functions")


if __name__ == "__main__":
    main()
