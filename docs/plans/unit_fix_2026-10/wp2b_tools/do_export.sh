#!/bin/bash
# do_export.sh <job> <blend> <proof_tag> <looped_csv> <windows_json>
cd "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
J=$1
python .tmp/wp2b/make_policy.py $J blender/checkpoints/$2 $J $4 "$5" move > /dev/null
python .tmp/wp2b/export_model.py $J blender/checkpoints/$2 $J $J export/wp2b --proof-tag=$3 > .tmp/wp2b/export_$J.log 2>&1
cut -c1-420 .tmp/wp2b/export_$J.log | tail -11
