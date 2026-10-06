"""Read the installed io_pdx_mesh binary parser without importing Blender.

No bytes are rewritten. The report records the exact parser source hash.
"""
import hashlib
import importlib
import json
from pathlib import Path
import sys
import types

PIPELINE = Path(__file__).resolve().parents[1]


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def parser():
    config = json.loads((PIPELINE / 'config/blender_hoi4_adapter.json').read_text(encoding='utf-8'))
    root = Path(config['io_pdx_mesh_root'])
    name = '_chaosx_readonly_pdx'
    if name not in sys.modules:
        package = types.ModuleType(name)
        package.__path__ = [str(root)]
        sys.modules[name] = package
    module = importlib.import_module(name + '.pdx_data')
    return module, {'path': str(root / 'pdx_data.py'), 'sha256': sha256(root / 'pdx_data.py')}


def read(path):
    module, evidence = parser()
    return module.read_meshfile(str(Path(path).resolve())), evidence
