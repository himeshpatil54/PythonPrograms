"""
_import_helper.py  —  shared utility for Test_Code test files.

Because the Code/ filenames start with digits (e.g. 01_even_odd.py),
they cannot be imported with a plain 'import' statement.
This helper uses importlib to load any file by its absolute path and
return the resulting module object.
"""
import importlib.util
import os
import sys


def load_module(relative_path):
    """
    Load a Python source file by its path relative to the repository root
    and return it as a module.

    Usage inside a test file (which is run from the repo root):
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from Test_Code._import_helper import load_module
        mod = load_module("Code/01_even_odd.py")
        is_even = mod.is_even
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    abs_path = os.path.join(repo_root, relative_path.replace("/", os.sep))
    module_name = os.path.splitext(os.path.basename(abs_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, abs_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
