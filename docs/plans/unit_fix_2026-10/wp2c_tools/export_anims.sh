#!/bin/bash
# export_anims.sh <job> <family> <stem> <prefix> <blend> <out_rel> <loops_csv> <installed_mesh_rel_to_repo> <tag> [windows_json] [nonhum_csv]
cd "<mod root>"
J=$1; F=$2; S=$3; P=$4; B=$5; O=$6; L=$7; M=$8; T=$9; W=${10:-"{}"}; N=${11:-""}
mkdir -p docs/assets/$F/models_3d/$J/$O
cp "$M" docs/assets/$F/models_3d/$J/$O/$S.mesh
python .tmp/unitfix2/make_policy2.py $J $F blender/checkpoints/$B $P "$L" "$W" "$N" > /dev/null
python .tmp/wp2b/export_model.py $J blender/checkpoints/$B $S $P $O --skip-mesh --proof-tag=$T > .tmp/unitfix2/exportA_$J.log 2>&1
echo EXPORT_DONE >> .tmp/unitfix2/exportA_$J.log
