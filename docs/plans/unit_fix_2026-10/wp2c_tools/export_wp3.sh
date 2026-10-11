#!/bin/bash
# export_wp3.sh <job> <blend> <out_rel> <tag>
cd "<mod root>"
J=$1; B=$2; O=$3; T=$4
python .tmp/wp3_zombies/make_policy.py $J blender/checkpoints/$B chaosx_$J stagger_move > /dev/null
python .tmp/wp3_zombies/export_model.py $J blender/checkpoints/$B chaosx_$J chaosx_$J $O --proof-tag=$T > .tmp/unitfix2/export_$J.log 2>&1
echo EXPORT_DONE >> .tmp/unitfix2/export_$J.log
