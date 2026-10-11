#!/bin/bash
# stage1.sh <job> <short> <cloth_target> <skin_target> [normal_strength]
cd "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
export LABPORT=${LABPORT:-9877}
job=$1; s=$2; M="C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
R=docs/assets/014_cannibalism/models_3d/$job
echo "== finalize $(date +%T)"
python .tmp/wp2b/run_lab.py .tmp/wp2b/finalize.py "{\"job\":\"$job\",\"src\":\"17_death_imported.blend\",\"out\":\"20_grounded.blend\"}" | head -c 600
echo "== partition $(date +%T)"
python .tmp/wp2b/partition.py $job blender/working/wp2b/blender/checkpoints/20_grounded.blend blender/working/wp2b/blender/checkpoints/21_export_batches.blend | tail -3
echo "== prep_uv $(date +%T)"
python .tmp/wp2b/run_lab.py .tmp/wp2b/prep_uv.py "{\"job\":\"$job\",\"src\":\"blender/working/wp2b/blender/checkpoints/21_export_batches.blend\",\"out\":\"wp2b_01_geom_uv.blend\",\"npz\":\"$M/.tmp/wp2b/${s}_bake.npz\",\"boost\":{\"head\":1.5,\"l_hand\":1.3,\"r_hand\":1.3},\"min_comp\":120}" > .tmp/wp2b/prep_$s.out 2>&1
python -c "
import json;d=json.load(open('.tmp/wp2b/prep_$s.out'));print(d['topo'],d['uv'])"
echo "== rebake $(date +%T)"
(cd .tmp/wp2b && python rebake.py ${s}_bake.npz "../../$R/provider/downloads/wp2b_body_v1_textures" out_$s 1024 2 | tail -1)
python .tmp/wp2b/auto_cfg.py .tmp/wp2b/out_$s .tmp/wp2b/cfg_$s.json $3 $4 $5
(cd .tmp/wp2b && python grade.py out_$s cfg_$s.json fin_$s | grep -E "spec_gate|normal_G|normal_A|\"p50\"" | head -5)
echo "== actions $(date +%T)"
python .tmp/wp2b/run_lab.py .tmp/wp2b/actions_model.py "{\"job\":\"$job\",\"prefix\":\"$job\",\"src\":\"wp2b_01_geom_uv.blend\",\"out\":\"wp2b_02_actions.blend\"}" | tr -d '\n ' | head -c 3500
echo; echo "== done $(date +%T)"
