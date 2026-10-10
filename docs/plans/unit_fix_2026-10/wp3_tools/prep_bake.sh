#!/bin/bash
# prep_bake.sh <job> <src_rel> <tex_dir_name> <extra_cfg_json_fragment>
cd "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
job=$1; src=$2; tex=$3; extra=$4
M="C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux"
python .tmp/wp3_zombies/run_lab.py .tmp/wp3_zombies/prep_uv.py "{\"job\":\"$job\",\"src\":\"$src\",\"out\":\"wp3_01_geom_uv.blend\",\"npz\":\"$M/.tmp/wp3_zombies/${job}_bake.npz\",\"boost\":{\"head\":1.5,\"l_hand\":1.3,\"r_hand\":1.3,\"tentacle\":1.4},\"min_comp\":120$extra}" > .tmp/wp3_zombies/run_$job.out 2>&1
python -c "
import json;d=json.load(open('.tmp/wp3_zombies/run_$job.out'));print('$job',d['settle'],d['topo'],d['uv']['islands'])"
(cd .tmp/wp3_zombies && python rebake.py ${job}_bake.npz "../../docs/assets/002_zombie_outbreak/models_3d/$job/provider/downloads/${tex}_textures" out_$job 1024 2 | tail -1 && python grade.py out_$job cfg_$job.json fin_$job | grep -E "spec_gate|\"p50\"" | head -3)
