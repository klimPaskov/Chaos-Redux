# WP6 Humanoid rig reworks - Audio delivery and held-source needs

This package has 36 unique active mod sound paths: 18 are installed and 18 are held. Consumer counts are path-scoped; a shared pool path appears once per relevant package report.

## Installed file facts

The final install has 18 unique path(s) for this package, by file role: loop 2, shot 13, step 3. Each installed row maps to the authoritative install manifest and has an actual-workspace hash match. The global 135-file set is provenance-eligible and decodes as PCM signed 16-bit, 44.1 kHz mono.

The installed derivative SHA is the one listed in the install manifest; the before SHA matches the captured baseline. Mastering is file-level evidence only and does not establish soundeffect state, role, repetition, contact timing, or live-game suitability.

## Held active paths

This package has 18 held path(s): 10 have a blocking provenance row, 7 lack a final per-file provenance row, and 1 are marked provenance-eligible but are absent from the final install. All held bytes match the original baseline SHA-256.

### `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_idle_vocal.wav`
Consumers: cannibal_march_predation_column / cannibal_march_predation_column_idle_vocal_sfx / cannibal_march_predation_column_idle_vocal_source, cannibal_march_predation_column / cannibal_march_predation_column_idle_vocal.wav.
Before/current SHA-256: `36d1ff4f8629100ce3fc91d742810d3d5c41e29457c6546688946b03b8bf7242` / `36d1ff4f8629100ce3fc91d742810d3d5c41e29457c6546688946b03b8bf7242`; unchanged: `true`; bytes: 88,316.
Review status: `eligible`; unit `cannibal_march_predation_column`; role `loop`; master batch `needs_review`; original archive state `archival_gap`.
Recorded source: Male Grunt/Yelling Sounds; creator HaelDB; license CC0 option published on the asset page; URL https://opengameart.org/content/male-gruntyelling-sounds; original SHA `not recorded`; original path `not recorded`.
Existing references: `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/manifest.json:169` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: owner decision on this eligible mapping because the active runtime path is not in the final install list; do not infer that a candidate should replace the held file.

### `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_selection.wav`
Consumers: cannibal_siege_eaters / cannibal_siege_eaters_selection.wav.
Before/current SHA-256: `0387847775c01825059f3fc3cbc4b650fb89140df85a08b6864240f8d3ba7e3f` / `0387847775c01825059f3fc3cbc4b650fb89140df85a08b6864240f8d3ba7e3f`; unchanged: `true`; bytes: 88,316.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_training.wav`
Consumers: cannibal_siege_eaters / cannibal_siege_eaters_training_sfx / cannibal_siege_eaters_training_source, cannibal_siege_eaters / cannibal_siege_eaters_training.wav.
Before/current SHA-256: `2fb04bfa3652e87056631845766fa3d5fc11808df4834c8c48102a38b0655290` / `2fb04bfa3652e87056631845766fa3d5fc11808df4834c8c48102a38b0655290`; unchanged: `true`; bytes: 289,604.
Review status: `blocked`; unit `cannibal_siege_eaters`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: No source member/license is assigned to this runtime training cue in the per-file row or Event 014 role mapping.
Existing references: `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json:2136` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_attack_gas.wav`
Consumers: chaos_battalion / chaos_assault_battalion_attack / chaos_assault_battalion_attack_source, chaos_battalion / chaos_assault_battalion_attack_gas.wav.
Before/current SHA-256: `979c4d512d7e17a79a3a3451613adf5cd801402e89da56098e7e1dbb31cf4741` / `979c4d512d7e17a79a3a3451613adf5cd801402e89da56098e7e1dbb31cf4741`; unchanged: `true`; bytes: 352,892.
Review status: `blocked`; unit `chaos_assault_battalion`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:38` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_death_01.wav`
Consumers: chaos_battalion / chaos_assault_battalion_death / chaos_assault_battalion_death_01, chaos_battalion / chaos_assault_battalion_death_01.wav.
Before/current SHA-256: `885bbe5f4ca50e1ae68942792f7b4ca1bab4ca3970110dad1045ff4832c513ff` / `885bbe5f4ca50e1ae68942792f7b4ca1bab4ca3970110dad1045ff4832c513ff`; unchanged: `true`; bytes: 647,420.
Review status: `blocked`; unit `chaos_assault_battalion`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:46` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_death_02.wav`
Consumers: chaos_battalion / chaos_assault_battalion_death / chaos_assault_battalion_death_02, chaos_battalion / chaos_assault_battalion_death_02.wav.
Before/current SHA-256: `892edda65d26fe7d9e48493cd4df0ffc43b956d47649fa90255b6ea2b0f81ca2` / `892edda65d26fe7d9e48493cd4df0ffc43b956d47649fa90255b6ea2b0f81ca2`; unchanged: `true`; bytes: 716,780.
Review status: `blocked`; unit `chaos_assault_battalion`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:47` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_death_03.wav`
Consumers: chaos_battalion / chaos_assault_battalion_death / chaos_assault_battalion_death_03, chaos_battalion / chaos_assault_battalion_death_03.wav.
Before/current SHA-256: `188d02cde5ed11e3ddbd92b959a608826d90a57ba409e4136b5100c01e40959b` / `188d02cde5ed11e3ddbd92b959a608826d90a57ba409e4136b5100c01e40959b`; unchanged: `true`; bytes: 531,828.
Review status: `blocked`; unit `chaos_assault_battalion`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:48` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_idle_breath.wav`
Consumers: chaos_battalion / chaos_assault_battalion_idle / chaos_assault_battalion_idle_source, chaos_battalion / chaos_assault_battalion_idle_breath.wav.
Before/current SHA-256: `222debcb8972edaed5b4b34a620714065cb003836c3fa9fcfce935fb18746b9f` / `222debcb8972edaed5b4b34a620714065cb003836c3fa9fcfce935fb18746b9f`; unchanged: `true`; bytes: 1,103,276.
Review status: `blocked`; unit `chaos_assault_battalion`; role `loop`; master batch `unresolved`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:35` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_move_step_01.wav`
Consumers: chaos_battalion / chaos_assault_battalion_move / chaos_assault_battalion_move_step_01, chaos_battalion / chaos_assault_battalion_move_step_01.wav.
Before/current SHA-256: `b47341232e4d9ea281d6bd896567a45d3dbe655d1c2bf97faea3acf64c9159d2` / `b47341232e4d9ea281d6bd896567a45d3dbe655d1c2bf97faea3acf64c9159d2`; unchanged: `true`; bytes: 43,680.
Review status: `blocked`; unit `chaos_assault_battalion`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:42` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_move_step_02.wav`
Consumers: chaos_battalion / chaos_assault_battalion_move / chaos_assault_battalion_move_step_02, chaos_battalion / chaos_assault_battalion_move_step_02.wav.
Before/current SHA-256: `9771ca8d3e5936b79d1c76020fcc757b2dcc2fde333b2a64a26287e6e91ddbd7` / `9771ca8d3e5936b79d1c76020fcc757b2dcc2fde333b2a64a26287e6e91ddbd7`; unchanged: `true`; bytes: 43,680.
Review status: `blocked`; unit `chaos_assault_battalion`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:43` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_move_step_03.wav`
Consumers: chaos_battalion / chaos_assault_battalion_move / chaos_assault_battalion_move_step_03, chaos_battalion / chaos_assault_battalion_move_step_03.wav.
Before/current SHA-256: `913169a436ef7d6ab4edb3f8e335aeca716259b1f9b8ca672d8d757fe8d65f34` / `913169a436ef7d6ab4edb3f8e335aeca716259b1f9b8ca672d8d757fe8d65f34`; unchanged: `true`; bytes: 46,428.
Review status: `blocked`; unit `chaos_assault_battalion`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:44` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/chaos_warfare/chaos_assault_battalion/chaos_assault_battalion_move_step_04.wav`
Consumers: chaos_battalion / chaos_assault_battalion_move / chaos_assault_battalion_move_step_04, chaos_battalion / chaos_assault_battalion_move_step_04.wav.
Before/current SHA-256: `389a2a1c2e2c300dac1ec69ac68b46a9ec7a1a2da94ab08fd4335b9f9c8a0742` / `389a2a1c2e2c300dac1ec69ac68b46a9ec7a1a2da94ab08fd4335b9f9c8a0742`; unchanged: `true`; bytes: 43,680.
Review status: `blocked`; unit `chaos_assault_battalion`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes do not match recovery-candidate derived hashes; the handoff says candidates were not copied to runtime.
Existing references: `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sound_handoff.md:45` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/units/death_ghost_hosts/death_ghost_attack.wav`
Consumers: death_hollow_ghost_host / death_ghost_attack / death_ghost_attack_source, death_hollow_ghost_host / death_ghost_attack.wav.
Before/current SHA-256: `187a0375dd1bee80227204aaf1b9e1588b2140d255c1235e057c9520edf280c7` / `187a0375dd1bee80227204aaf1b9e1588b2140d255c1235e057c9520edf280c7`; unchanged: `true`; bytes: 132,378.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/units/death_ghost_hosts/death_ghost_death.wav`
Consumers: death_hollow_ghost_host / death_ghost_death / death_ghost_death_source, death_hollow_ghost_host / death_ghost_death.wav.
Before/current SHA-256: `8a13837e9e370397a1d6be233c2534bc8449f296bedd9aac42fe004647ba1c01` / `8a13837e9e370397a1d6be233c2534bc8449f296bedd9aac42fe004647ba1c01`; unchanged: `true`; bytes: 123,558.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/units/death_ghost_hosts/death_ghost_idle.wav`
Consumers: death_hollow_ghost_host / death_ghost_idle / death_ghost_idle_source, death_hollow_ghost_host / death_ghost_idle.wav.
Before/current SHA-256: `1c3b6090126c8fd38344f19df7965b3524a68db83715483fc5ea0254f405d6d6` / `1c3b6090126c8fd38344f19df7965b3524a68db83715483fc5ea0254f405d6d6`; unchanged: `true`; bytes: 705,678.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/units/death_ghost_hosts/death_ghost_impact.wav`
Consumers: death_hollow_ghost_host / death_ghost_impact / death_ghost_impact_source, death_hollow_ghost_host / death_ghost_impact.wav.
Before/current SHA-256: `28f84fc78d7fa3aab8f40835cff40cbfc5c6eeb8b6d92c1f5f35f3002927e3ed` / `28f84fc78d7fa3aab8f40835cff40cbfc5c6eeb8b6d92c1f5f35f3002927e3ed`; unchanged: `true`; bytes: 161,358.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/units/death_ghost_hosts/death_ghost_movement.wav`
Consumers: death_hollow_ghost_host / death_ghost_movement / death_ghost_movement_source, death_hollow_ghost_host / death_ghost_movement.wav.
Before/current SHA-256: `c07b37020170e49d9423b5fd11dba79dea5a97b78ac86bcbfb4d29f9ffe2030b` / `c07b37020170e49d9423b5fd11dba79dea5a97b78ac86bcbfb4d29f9ffe2030b`; unchanged: `true`; bytes: 264,678.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/units/death_ghost_hosts/death_ghost_selection.wav`
Consumers: death_hollow_ghost_host / death_ghost_selection.wav.
Before/current SHA-256: `428e0ca931d7d9a6f7ec5948b2e4ebd5681459180301586d6fbe91fb187db132` / `428e0ca931d7d9a6f7ec5948b2e4ebd5681459180301586d6fbe91fb187db132`; unchanged: `true`; bytes: 226,382.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

## Recording need: march idle

The retained idle fails the measured head/tail RMS loop gate; bounded recorded-sample crossfades also failed (`recovery2_batch.json`: `recorded_loop_crossfade_could_not_meet_3db_gate`).
The installed idle action is 5.9 seconds, so a roughly six-second sustained breath/grunt recording is a concrete source brief for an audible continuous loop.
Check the already attributed Male Grunt/Yelling Sounds pack by HaelDB first, preserving its exact source-member and license evidence: https://opengameart.org/content/male-gruntyelling-sounds.
The existing evidence records a CC0 page option; its applicability to the selected member must be verified before production.
If no suitable archived recording exists, the orchestrator can source a recorded vocal bed under CC0 or attributable CC BY/CC BY-SA terms after obtaining sourcing permission.
The current cue stays in place until the authored state and accepted replacement are wired by its package owner.

## Recording requirements from the user-authored plan

The following brief is transcribed from section 2 of `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` (SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`). It records the requested role, timing/length, and source-license choices. It is a production brief, not approval for an existing candidate or runtime file.

- `cannibal_bone_guard`: from WP2's batch: selection trimmed to the voiced 1.2 s, impact at -3 dBFS, two footstep takes at -18 dB peak; death/idle/training already clean.
- `cannibal_march_predation_column`: from WP2's batch: death re-derived at -3 dBFS with a different grunt take than the scavenger, distinct movement/training takes (currently byte copies of feast_cohort files), footsteps at -18 dB peak, impact at -3 dBFS, training lead trimmed; the archers-shooting release sample is kept.
- `cannibal_siege_eaters`: from WP2's batch: impact limited to -3 dBFS, idle lead trimmed, footsteps at -18 dB peak, swish lengthened; events as above.
- `chaos_battalion`: install the reviewed PCM16 recovery set from `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/derived/` under the names in `chaos_assault_battalion_sound.asset` (idle breath -12 dBFS, DC-free; spray re-derived from the Soundkrampf source with onset/release and 40 ms fades at -6 dBFS; the 0.61 s support_attack_gas candidate on the 0.6333/1.6333 s events; steps at -6 dBFS with 10 ms fade-in / 60 ms release; death_01..03 lead silence <= 50 ms, tails trimmed, -6 dBFS); add the CC0 Body Fall candidate as a new cue on the 2.6333 s death landing; every file pcm_s16le 44.1 kHz mono.
- `death_hollow_ghost_host`: replace the Wilhelm scream with a sourced CC0 dissipating wail or reverse-reverb gasp (Freesound CC0 horror vocal, attributed; processing of a recording, not synthesis), 1.5-2.5 s, peak -6 dBFS, onset at 0.1 s and tail ending before the frame-139 impact; cut three 0.3-0.5 s drag/step whooshes from the movement source (onset at sample 0, 20/80 ms fades, -8 dBFS) for the three contact events instead of stacking the 3 s bed; trim the idle lead silence, lower to ~-30 dBFS RMS, defend event trigger_once or a 3 s excerpt; trim 0.40 s off the impact head; re-trim the selection cue; locate or re-source the missing `sound/handoff.md` licence table and re-verify every cue's licence before reinstalling.

No recording source was downloaded or created for this documentation update. Per-file source binding and licensing gaps listed above remain the audio install gate.
## Remaining runtime checks

The package definitions and actions remain unchanged. Final entity lint records current unresolved event-sample overlaps, cycle/state mismatches, missing contact evidence, and measured event/contact offsets as shown in the main package report. Successful PCM mastering does not clear those findings.

Source-tree audit reports 209 active cues, 173 single-sample cues, 52 duplicate groups, and 52 undeclared cross-unit duplicate groups. Source sharing, state/take choice, event timing, and player-facing role fit remain unaccepted.

No source downloads or new recordings were performed. Source URLs and license families above are copied only from existing per-file provenance/candidate records; an unapproved candidate is not treated as a license or runtime match.

## Evidence source hashes
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery_batch.json` - SHA-256 `148ffb5a39ce96a1ee6cd532b72dc5426ff5d3abbeccb4afe5a7eba734e533d8`.
- User-authored recording brief `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` - SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

- `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json` - SHA-256 `72054623f8c388f79f7a8a0c71881025add5efe505c5ae4317db1e3c5ba1ecb5`
- `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json` - SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`
- `docs/plans/unit_fix_2026-10/audio_evidence/provenance_review.json` - SHA-256 `bd4e36c9edbba24c926a2306efb4190541c3f6b90290e9f9a3a0c6111f74b577`
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json` - SHA-256 `e277faf5be6a49d26fd81bf305b0b873ada14e0ae3e36bb11e9f95ff78cf360a`
- `docs/plans/unit_fix_2026-10/audio_evidence/sound_tree_after.json` - SHA-256 `532aae613a6eaab88e21067aa75222fb8a8da8a77ed9d1792363b7cb8d7bb275`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json` - SHA-256 `6b87475048580ee78e33ccf052d1f67be5002099b3c5db17092dfb1baece633d`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/contact_peak_evidence.json` - SHA-256 `b6193d744c0b10f3d4c6bf464799934010ab07f6ed9991d04ac89bce68a96af8`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/entity_lint_after.json` - SHA-256 `a388fae714faf098968191b752e99193a82fdd37a28daf6bf6b6ca372dfe42bc`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/final_inventory.json` - SHA-256 `d1f72e1456c6a09cdce948df00590534414b91518c8241ec36ca3e11ccb6bb6b`
