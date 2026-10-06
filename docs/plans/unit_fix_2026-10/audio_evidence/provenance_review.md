# Existing audio batch provenance review

The JSON covers all 189 existing runtime WAV inputs. Each row records its source path and captured runtime hash, eligibility, exact source title/creator/license/page where proven, original SHA/path when an existing receipt joins it to the runtime derivative, cited package documents with line spans, and exact blockers.

Result: 137 eligible and 52 held. Runtime inputs match the captured allowlist SHA for 189/189 files. Initial master_batch.json records 168 staged and 21 non-staged; staged output hashes verified 168/168 files. Processing holds are separate from license eligibility.

Missing untouched originals are archival gaps when existing per-file source attribution and the current derivative binding are explicit. Same-filename-only evidence is not accepted. The allowlist and master batch are cited only for current bytes/status, never as originating license evidence.

## Held entries

- autonomous_robot: 1 files: autonomous_robot_idle_loop.wav.
- cannibal_feast_guard: 1 files: cannibal_feast_guard_training.wav.
- cannibal_siege_eaters: 1 files: cannibal_siege_eaters_training.wav.
- chaos_assault_battalion: 9 files: chaos_assault_battalion_attack_gas.wav, chaos_assault_battalion_death_01.wav, chaos_assault_battalion_death_02.wav, chaos_assault_battalion_death_03.wav, chaos_assault_battalion_idle_breath.wav, chaos_assault_battalion_move_step_01.wav, chaos_assault_battalion_move_step_02.wav, chaos_assault_battalion_move_step_03.wav, chaos_assault_battalion_move_step_04.wav.
- chaosx_demonic_zombies: 2 files: zombie_idle_moan_01.wav, zombie_idle_moan_03.wav.
- chaosx_gorilla_heavy_infantry: 6 files: chaosx_gorilla_heavy_infantry_attack.wav, chaosx_gorilla_heavy_infantry_death.wav, chaosx_gorilla_heavy_infantry_idle.wav, chaosx_gorilla_heavy_infantry_move.wav, chaosx_gorilla_heavy_infantry_recovery.wav, chaosx_gorilla_heavy_infantry_select.wav.
- chaosx_pan_sappers: 3 files: chaosx_pan_sappers_construction.wav, chaosx_pan_sappers_move.wav, chaosx_pan_sappers_sabotage.wav.
- chaosx_riverborn: 6 files: chaosx_riverborn_attack.wav, chaosx_riverborn_death.wav, chaosx_riverborn_idle.wav, chaosx_riverborn_move.wav, chaosx_riverborn_select.wav, chaosx_riverborn_water_transition.wav.
- chaosx_stone_cohorts: 6 files: chaosx_stone_cohorts_attack.wav, chaosx_stone_cohorts_collapse_recovery.wav, chaosx_stone_cohorts_death.wav, chaosx_stone_cohorts_idle.wav, chaosx_stone_cohorts_move.wav, chaosx_stone_cohorts_select.wav.
- chaosx_temporal_guard: 9 files: chaosx_temporal_guard_acknowledgement.wav, chaosx_temporal_guard_attack_contact.wav, chaosx_temporal_guard_death.wav, chaosx_temporal_guard_footstep_a.wav, chaosx_temporal_guard_footstep_b.wav, chaosx_temporal_guard_idle_clock.wav, chaosx_temporal_guard_impact.wav, chaosx_temporal_guard_selection.wav, chaosx_temporal_guard_temporal_special.wav.
- clone_infantry: 7 files: clone_infantry_attack_voice_01.wav, clone_infantry_casing_01.wav, clone_infantry_death_01.wav, clone_infantry_rifle_01.wav, clone_infantry_step_left_01.wav, clone_infantry_step_right_01.wav, clone_infantry_wounded_01.wav.
- portal_raider: 1 files: portal_raider_electrical_pulse.wav.

Per-file blockers and source candidates are in provenance_review.json. Ineligible rows do not claim an original SHA or path where the current source chain is unproven.

## Evidence

Each per-file row includes the existing attribution/source document and line span. No source files were downloaded or edited during this review.
