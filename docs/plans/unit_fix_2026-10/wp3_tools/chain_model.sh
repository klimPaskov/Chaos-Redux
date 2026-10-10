#!/bin/bash
# chain_model.sh <job> <folder> <stem> <prefix> <tag> <actions_cfg_json> [stagger]
cd "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
job=$1; folder=$2; stem=$3; prefix=$4; tag=$5; cfg=$6; stagger=$7
L=.tmp/wp3_zombies/chain_$job.log
{
echo "== actions"; python .tmp/wp3_zombies/run_lab.py .tmp/wp3_zombies/actions_model.py "$cfg" | tr -d '\n ' | head -c 3000; echo
echo "== textures"; python .tmp/wp3_zombies/tex_deliver.py $job $stem $stem .tmp/wp3_zombies/fin_$job $tag 2>&1 | grep -E "^convert|^prepare|ERROR"
echo "== policy"; python .tmp/wp3_zombies/make_policy.py $job blender/checkpoints/wp3_02_actions.blend $prefix $stagger
echo "== export"; python .tmp/wp3_zombies/export_model.py $job blender/checkpoints/wp3_02_actions.blend $stem $prefix export/wp3 --proof-tag=_a 2>&1 | cut -c1-260
echo DONE
} > $L 2>&1
