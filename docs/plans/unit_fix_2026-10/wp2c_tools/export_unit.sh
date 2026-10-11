#!/bin/bash
# export_unit.sh <job> <blend> <out_rel> <tag> [windows_json]
cd "<mod root>"
J=$1; B=$2; O=$3; T=$4; W=${5:-"{}"}
python .tmp/wp2b/make_policy.py $J blender/checkpoints/$B $J "idle,move,defend,retreat,training" "$W" move > /dev/null
python .tmp/wp2b/export_model.py $J blender/checkpoints/$B $J $J $O --proof-tag=$T > .tmp/unitfix2/export_$J.log 2>&1
echo EXPORT_DONE >> .tmp/unitfix2/export_$J.log
