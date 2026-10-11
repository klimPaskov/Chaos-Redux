import sys; sys.path.insert(0,r"<mod root>/.tools/3d_pipeline/review")
import importlib, lab_finalize, lab_actions; importlib.reload(lab_actions); importlib.reload(lab_finalize)
import json
J=r"<mod root>/docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/working/wp2b/blender/checkpoints/"
cfg={"blend":J+CFG['src'],"out":J+CFG['out'],"prefix":CFG['job'],"roles":["idle","move","attack","defend","support_attack","retreat","training","death"],"armature":"Armature.001","meshes":["char1.001"],"root":"Hips"}
p=J+"_finalize_cfg.json"; json.dump(cfg,open(p,"w"))
result=lab_finalize.run(p)
