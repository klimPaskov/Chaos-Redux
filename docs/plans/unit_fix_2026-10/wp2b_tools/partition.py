import sys, hashlib, json
from pathlib import Path
MOD=Path(r"<mod root>")
sys.path.insert(0,str(MOD/'.tools/3d_pipeline/review'))
import provider_intake as pi
job,src,dst=sys.argv[1:4]
J=pi.job_root(job)
d=hashlib.sha256((J/src).read_bytes()).hexdigest().upper()
r=pi.adapter("partition_skeletal_mesh_export_batches",{"job_id":job,"blend_rel":src,"expected_source_sha256":d,"checkpoint_rel":dst,"target_armature_name":"Armature.001","target_mesh_names":["char1.001"]})
print(json.dumps({k:r.get(k) for k in ('status','mesh_streams','batches','checkpoint','geometry') if k in r},indent=1,default=str)[:2500])
