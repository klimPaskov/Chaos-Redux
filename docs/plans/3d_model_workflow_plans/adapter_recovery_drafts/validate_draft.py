from pathlib import Path
import ast
import importlib.util
import unittest

root=Path(__file__).resolve().parent
repo=root.parents[3]
source=(repo/'.tools/3d_pipeline/tests/test_manual_creature_rig_contract.py').read_text()
source=source.replace('PATH=Path(__file__).parents[1]/"adapter/manual_creature_rig.py"','PATH=Path(__file__).parent/"manual_creature_rig.py"')
namespace={'__file__':str(root/'validate_draft.py'),'__name__':'draft_contracts'}
exec(compile(source,'draft_original_contracts','exec'),namespace)
suite=unittest.defaultTestLoader.loadTestsFromTestCase(namespace['ManualRigContracts'])
result=unittest.TextTestRunner(verbosity=2).run(suite)
module=namespace['module']
import struct
header=bytearray(128); header[:4]=b'DDS '
for offset,value in ((4,124),(12,128),(16,128),(20,512),(28,1),(76,32),(80,0x41),(88,32),(92,0x00ff0000),(96,0x0000ff00),(100,0x000000ff),(104,0xff000000)):
    struct.pack_into('<I',header,offset,value)
assert module.validate_component_dds(header,128+128*128*4)==(128,128)
for offset,value in ((104,0),(16,2048),(20,511)):
    wrong=bytearray(header); struct.pack_into('<I',wrong,offset,value)
    try: module.validate_component_dds(wrong,128+128*128*4)
    except ValueError: pass
    else: raise AssertionError((offset,value))
try: module.validate_component_dds(header,128+128*128*4-1)
except ValueError: pass
else: raise AssertionError('Truncated DDS accepted')
row={'name':'body','min':[-1,-1,-1],'max':[1,1,1],'bones':['root'],'rigid':True,'mesh_names':['body_mesh']}
module.validate_regions([row],{'root'})
for invalid in ([],['body_mesh','body_mesh'],['missing name'],None):
    try: module.validate_regions([dict(row,mesh_names=invalid)],{'root'})
    except ValueError: pass
    else: raise AssertionError(invalid)
for file in ('blender_worker.py','chaosx_blender_hoi4_mcp.py','manual_creature_rig.py'):
    ast.parse((root/file).read_text())
mcp=(root/'chaosx_blender_hoi4_mcp.py').read_text()
assert mcp.index('def chaosx_blender_hoi4_repair_explicit_mesh_winding(')<mcp.index('def main()')
assert mcp.index('def chaosx_blender_hoi4_ground_existing_action(')<mcp.index('def main()')
print('Draft source and new region rejection checks passed; no Blender execution or shared writes.')
raise SystemExit(0 if result.wasSuccessful() else 1)
