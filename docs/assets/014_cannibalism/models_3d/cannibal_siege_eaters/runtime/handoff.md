# cannibal_siege_eaters v8 runtime handoff

Status: **blocked before Meshy task creation; do not wire a model**.

Consumer contract: `common/units/014_cannibalism_irregular_infantry.txt#cannibal_siege_eaters -> cannibal_siege_eaters_entity`.

Proposed parent-owned runtime root: `gfx/models/units/014_cannibalism/cannibal_siege_eaters/`.

The parent approved exact reference SHA-256 `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`. The locked Meshy 7 generation request returned HTTP 402 at a live balance of 25 before it created a task, and the post-check remained 25. The v8 lineage therefore has no provider task ID, geometry, rig, animations, Blender checkpoint, PDX export, or reimport proof. Historical provider and Blender artifacts in this package are rejected evidence only and must not be wired.

When sufficient credits are available, resume from `provider/requests/v8_001_meshy_image_to_3d.json`, then require accepted multi-view geometry before rig/animation spend. The eight bindings must use genuine Meshy motion: `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`. Final stable names are planned as `cannibal_siege_eaters_<role>` and require exported plus reimported `.anim` proof. Do not use the historical locally authored actions or semantic aliases.

Seven sourced PCM s16le 44100 Hz mono candidates are prepared under `audio/derived/`. Their source pages, licenses, source and derived hashes, transformations, proposed roles, and pending sync points are in `evidence/audio_sources/sound_design_v8.json`. Exact animation-frame bindings remain pending genuine provider actions. Proposed sound identifiers:

- `cannibal_siege_eaters_selection`
- `cannibal_siege_eaters_movement`
- `cannibal_siege_eaters_idle_vocal`
- `cannibal_siege_eaters_maul_swing`
- `cannibal_siege_eaters_heavy_impact`
- `cannibal_siege_eaters_training`
- `cannibal_siege_eaters_death`

The bespoke counter stays external and is consumed through `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md` using:

- `GFX_unit_cannibal_siege_eaters_icon_medium`
- `GFX_unit_cannibal_siege_eaters_icon_medium_white`
- `GFX_unit_cannibal_siege_eaters_icon_small`

Parent work after a complete model package: create the entity/GFX/action/sound definitions, copy approved final mesh/anim/DDS/audio files into the runtime root, bind exact sound frames from the action manifest, and perform live in-game consumer validation. No runtime, GFX, entity, asset, or sound-definition file has been edited here.
