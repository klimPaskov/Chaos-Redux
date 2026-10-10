#!/bin/bash
# refix.sh <job> <prefix> <out_rel> <cfg_json> [stagger] : actions (Lab) -> policy -> full export to a new out dir
cd "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
job=$1; prefix=$2; out=$3; cfg=$4; stagger=$5
L=.tmp/wp3_zombies/refix_$job.log
{
echo "== actions"; python .tmp/wp3_zombies/run_lab.py .tmp/wp3_zombies/actions_model.py "$cfg" | tr -d '\n ' | head -c 3500; echo
echo "== policy"; python .tmp/wp3_zombies/make_policy.py $job blender/checkpoints/wp3_02_actions.blend $prefix $stagger
echo "== export"; python .tmp/wp3_zombies/export_model.py $job blender/checkpoints/wp3_02_actions.blend $prefix $prefix $out --proof-tag=_$(date +%H%M%S) 2>&1 | cut -c1-260
echo DONE
} > $L 2>&1
