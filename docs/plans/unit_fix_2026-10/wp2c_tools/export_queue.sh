#!/bin/bash
cd "<mod root>"
for u in "$@"; do
  mkdir -p docs/assets/012_africa/models_3d/$u/export/wp1c
  cp gfx/models/units/012_africa_$u/chaosx_$u.mesh docs/assets/012_africa/models_3d/$u/export/wp1c/chaosx_$u.mesh
  python .tmp/unitfix2/make_policy2.py $u 012_africa blender/checkpoints/wp1c_02_doctor.blend chaosx_$u "idle,move,attack,defend,support_attack,retreat,training" "{}" move > /dev/null
  python .tmp/wp2b/export_model.py $u blender/checkpoints/wp1c_02_doctor.blend chaosx_$u chaosx_$u export/wp1c --skip-mesh --proof-tag=_a > .tmp/unitfix2/exportA_$u.log 2>&1
  echo EXPORT_DONE >> .tmp/unitfix2/exportA_$u.log
done
