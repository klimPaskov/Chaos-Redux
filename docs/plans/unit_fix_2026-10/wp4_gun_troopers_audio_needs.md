# WP4 Gun troopers - Audio delivery and held-source needs

This package has 38 unique active mod sound paths: 26 are installed and 12 are held. Consumer counts are path-scoped; a shared pool path appears once per relevant package report.

## Installed file facts

The final install has 26 unique path(s) for this package, by file role: loop 2, shot 16, step 8. Each installed row maps to the authoritative install manifest and has an actual-workspace hash match. The global 135-file set is provenance-eligible and decodes as PCM signed 16-bit, 44.1 kHz mono.

The installed derivative SHA is the one listed in the install manifest; the before SHA matches the captured baseline. Mastering is file-level evidence only and does not establish soundeffect state, role, repetition, contact timing, or live-game suitability.

## Held active paths

This package has 12 held path(s): 9 have a blocking provenance row, 3 lack a final per-file provenance row, and 0 are marked provenance-eligible but are absent from the final install. All held bytes match the original baseline SHA-256.

### `sound/portal_raider/portal_raider_electrical_pulse.wav`
Consumers: portal_raider / portal_raider_idle_electrical / portal_raider_electrical_pulse, portal_raider / portal_raider_electrical_pulse.wav.
Before/current SHA-256: `7698f5cf9fcab36cbb9dcef988cb6bdd5bf7255d0ef4e82f8ffa5f012c7c1d1f` / `7698f5cf9fcab36cbb9dcef988cb6bdd5bf7255d0ef4e82f8ffa5f012c7c1d1f`; unchanged: `true`; bytes: 88,244.
Review status: `blocked`; unit `portal_raider`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Force Field Electric Hum; creator Hansjörg Malthaner (Varkalandar); license CC BY 4.0; URL https://opengameart.org/content/force-field-electric-hum; original SHA `not recorded`; original path `not recorded`.
Held reason: Captured current input SHA 7698f5cf9fcab36cbb9dcef988cb6bdd5bf7255d0ef4e82f8ffa5f012c7c1d1f does not match any source-bound derived SHA in the Portal Raider audio manifest; the idle-electrical candidate hash is feb5eaf7d0d2d74e5637289a4dc264252f2a47a83a479ce2ea7c701c73e898cc.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-09-08_portal_runtime_integration.md:56` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only); `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/audio/audio_manifest.md:16` (candidate original/derived SHA; current runtime input mismatch).
Candidate sources recorded in review (not approved for this exact runtime file): Force Field Electric Hum by creator text contains a replacement character in provenance_review.json, CC BY 4.0, https://opengameart.org/content/force-field-electric-hum.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.
Before-commit rollback: candidate SHA `2707e90c02ffa2bbb2649cc4c062f69252bce77b19290960be51c9754fc45e60` was reverted because Final source-bound provenance contradiction; original runtime cue retained before commit; current bytes retain the baseline SHA.

### `sound/shared_clone_system/clone_infantry/clone_infantry_attack_voice_01.wav`
Consumers: clone_infantry / clone_infantry_attack_voice / clone_infantry_attack_voice_source, clone_infantry / clone_infantry_attack_voice_01.wav.
Before/current SHA-256: `7d2b088e00fa2010b0c0efe00a73933fe8ec5bddcde71bef92f102932a5b224b` / `7d2b088e00fa2010b0c0efe00a73933fe8ec5bddcde71bef92f102932a5b224b`; unchanged: `true`; bytes: 33,712.
Review status: `blocked`; unit `clone_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:144` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_casing_01.wav`
Consumers: clone_infantry / clone_infantry_rifle_cartridge / clone_infantry_cartridge_source, clone_infantry / clone_infantry_casing_01.wav.
Before/current SHA-256: `389bf2808c4398bf5b5ee93b462905d8d4460df6501c3c1732e588fa4ad22ea6` / `389bf2808c4398bf5b5ee93b462905d8d4460df6501c3c1732e588fa4ad22ea6`; unchanged: `true`; bytes: 87,928.
Review status: `blocked`; unit `clone_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:146` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_death_01.wav`
Consumers: clone_infantry / clone_infantry_death / clone_infantry_death_source, clone_infantry / clone_infantry_death_01.wav.
Before/current SHA-256: `2302251f6bd604ab16d46446ac9556689951c827d980ce20868bddb37e3e7da9` / `2302251f6bd604ab16d46446ac9556689951c827d980ce20868bddb37e3e7da9`; unchanged: `true`; bytes: 122,412.
Review status: `blocked`; unit `clone_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:148` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_rifle_01.wav`
Consumers: clone_infantry / clone_infantry_rifle_attack / clone_infantry_rifle_source, clone_infantry / clone_infantry_rifle_01.wav.
Before/current SHA-256: `a2c95706a790f48a318cc2301cf5b776433aba28815072d3f437e5a59478cd7c` / `a2c95706a790f48a318cc2301cf5b776433aba28815072d3f437e5a59478cd7c`; unchanged: `true`; bytes: 79,576.
Review status: `blocked`; unit `clone_infantry`; role `shot`; master batch `needs_review`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.; The rifle source review rejects this inherited WAV as simulated Audacity/popped-balloon shots; there is no licensed recording source.
Existing references: `docs/assets/shared_clone_system/models_3d/clone_infantry/attempts/20260906_weaponfree_blender/audio_source_review.md:24` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_step_left_01.wav`
Consumers: clone_infantry / clone_infantry_step_left / clone_infantry_step_left_source, clone_infantry / clone_infantry_step_left_01.wav.
Before/current SHA-256: `77abdb9056f7d9539ca5bc00f64781220093444770efba07f4f338825917cc1c` / `77abdb9056f7d9539ca5bc00f64781220093444770efba07f4f338825917cc1c`; unchanged: `true`; bytes: 23,040.
Review status: `blocked`; unit `clone_infantry`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:142` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_step_right_01.wav`
Consumers: clone_infantry / clone_infantry_step_right / clone_infantry_step_right_source, clone_infantry / clone_infantry_step_right_01.wav.
Before/current SHA-256: `10e99be91b24a7ad8c67b205cc16e39eee8d4a11df043c55b95be6c687fe59a0` / `10e99be91b24a7ad8c67b205cc16e39eee8d4a11df043c55b95be6c687fe59a0`; unchanged: `true`; bytes: 29,302.
Review status: `blocked`; unit `clone_infantry`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:143` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_clone_system/clone_infantry/clone_infantry_wounded_01.wav`
Consumers: clone_infantry / clone_infantry_wounded / clone_infantry_wounded_source, clone_infantry / clone_infantry_wounded_01.wav.
Before/current SHA-256: `89f0a1b92c4cb19796e4ce40c68f89d420f858853a053cd095abca724f46f85d` / `89f0a1b92c4cb19796e4ce40c68f89d420f858853a053cd095abca724f46f85d`; unchanged: `true`; bytes: 60,966.
Review status: `blocked`; unit `clone_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime SHA differs from the selected licensed candidate SHA.
Existing references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_weaponfree_closure_2026-09-12.md:147` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/shared_robot_system/autonomous_robot/autonomous_robot_casings_02.wav`
Consumers: autonomous_robot / autonomous_robot_casings_sfx / autonomous_robot_casings_02_source, autonomous_robot / autonomous_robot_casings_02.wav.
Before/current SHA-256: `4e8100ed6d9eb7f342c0cb562dee238c46b43b6d7c62edac9babd5fdf2734660` / `4e8100ed6d9eb7f342c0cb562dee238c46b43b6d7c62edac9babd5fdf2734660`; unchanged: `true`; bytes: 76,812.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/shared_robot_system/autonomous_robot/autonomous_robot_casings_03.wav`
Consumers: autonomous_robot / autonomous_robot_casings_sfx / autonomous_robot_casings_03_source, autonomous_robot / autonomous_robot_casings_03.wav.
Before/current SHA-256: `cff2b4187900a653ef72ab8d8d14526e1f0bb4f316abf827dc1b46f1d5f27296` / `cff2b4187900a653ef72ab8d8d14526e1f0bb4f316abf827dc1b46f1d5f27296`; unchanged: `true`; bytes: 52,116.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/shared_robot_system/autonomous_robot/autonomous_robot_casings_04.wav`
Consumers: autonomous_robot / autonomous_robot_casings_sfx / autonomous_robot_casings_04_source, autonomous_robot / autonomous_robot_casings_04.wav.
Before/current SHA-256: `6a648a5a8b30acda221e565b21a88816b0815375ea427d784c542e9cf9ae7ef2` / `6a648a5a8b30acda221e565b21a88816b0815375ea427d784c542e9cf9ae7ef2`; unchanged: `true`; bytes: 58,114.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/shared_robot_system/autonomous_robot/autonomous_robot_idle_loop.wav`
Consumers: autonomous_robot / autonomous_robot_idle_sfx / autonomous_robot_idle_source, autonomous_robot / autonomous_robot_idle_loop.wav.
Before/current SHA-256: `e256cf3ef13a6d5c45eeebe5955167e02e89208fce2c53fab130c36236af9700` / `e256cf3ef13a6d5c45eeebe5955167e02e89208fce2c53fab130c36236af9700`; unchanged: `true`; bytes: 352,878.
Review status: `blocked`; unit `autonomous_robot`; role `loop`; master batch `needs_review`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current idle-loop bytes do not match a source-bound candidate; current per-file source URL/license/creator mapping is absent.
Existing references: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/source_ledger.md:12` (source creator/license and original-hash records); `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/source_plan.md:11` (source pages, direct URLs, creator and license for retained original sources); `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/polish_20260927/README.md:13` (per-file source, creator, license, and source pages); `docs/assets/shared_robot_system/models_3d/autonomous_robot/attempts/20260906_weaponfree_blender/evidence/finalize_20260912/release_evidence_manifest.json:287` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

## Other staged recovery outputs

2 staged output(s) match this package but are absent from the final install manifest:

- `clone_infantry` / `clone_infantry_rifle_attack` (shot): output SHA `87d9889982b863d316bcbe09de2f85619b34618045408dc29a9b45728e6201b7`; staging path `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\unit_fix_2026-10\audio_evidence\recovery2_evidence\staged\a175.wav`. Candidate status is staged only.
- `autonomous_robot` / `autonomous_robot_idle_sfx` (loop): output SHA `a74767ef5d1c5984e53d306e70b5446b39ceb736fb1fadc083a63162eed9b132`; staging path `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\unit_fix_2026-10\audio_evidence\recovery2_evidence\staged\a182.wav`. Candidate status is staged only.

## Recording requirements from the user-authored plan

The following brief is transcribed from section 2 of `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` (SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`). It records the requested role, timing/length, and source-license choices. It is a production brief, not approval for an existing candidate or runtime file.

- `alien_infantry`: replace the one-shot vehicle hum with a 3-4 s seamless loop (loop = yes, equal head/tail RMS) cut from a CC0 creature-breath or suit-hum recording (Ogrebane CC0 pack or Freesound CC0), or remove the idle cue; impact gets a 5 ms fade-in and -6 dBFS normalisation; layer the archived CC0 Kenney sci-fi laser chirp (`evidence/audio/original/source_search_20260905`) over the noise burst.
- `autonomous_robot`: either trim `autonomous_robot_mg_report.wav` to a dry <= 0.15 s transient (40 ms fade-out) for the per-shot events, or replace the 22 events with one 2.6 s burst fired at 0.667 s per gun (vanilla infantry_mg_attack pattern) built from the same recorded report source; 5-10 ms fade-ins on casings_01..04, 40 ms fade-outs on hydraulic_release and gun_heave; raise idle_loop ~6 dB.
- `assassin_cadre`: define `chaosx_assassin_cadre_attack` (3-shot 0.3 s burst assembled at 10 Hz from the sourced `docs/assets/039_murder_mystery/audio/source/gunshot_sounds/sounds/cz.wav`, volume 0.2, falloff_100, max_audible 4) with one event per burst at 0.6667/2.0/3.3333; `chaosx_assassin_cadre_death` (0.8-1.2 s trimmed take from `death_pain_grunts.wav`, volume ~0.3, falloff_100, is3d) at 0.3 s in death; optional sourced footsteps from `footstep_01-06.wav`; all in `sound/039_murder_mystery_units_sound.asset`.
- `master_assassin`: inherits the cadre definitions.
- `mechanized_assassin`: define `chaosx_mechanized_assassin_destroyed` (sourced `mechanical_explosion_44100.wav` trimmed to ~2 s, volume ~0.5, falloff_100) at 0.1 s in death, and optionally `chaosx_mechanized_assassin_engine` (sourced `engine_heavy_loop_0.wav`, volume 0.2, loop = yes) on idle; keep vanilla `mechanized_units_mg_fire`.
- `shadow_company`: inherits the cadre definitions; no separate files unless an alias is chosen.
- `silent_guard`: define `chaosx_silent_guard_attack` (3-shot burst from cz.wav, volume 0.2, falloff_100) and `chaosx_silent_guard_death` (trimmed death_pain_grunts take at 0.3 s) in the 039 sound asset and reference them from the entity.
- `clone_infantry`: `clone_infantry_rifle_01.wav` cut to one report (~0.45 s, 120 ms fade-out, peak -3 dBFS, onset at sample 0, 0.17 s lead trimmed); shout re-trimmed from the source with full decay (~0.8 s, 30 ms fade-out, -3 dBFS); 10-20 ms fades on wounded and death; add the body-impact candidate from `audio/sound_design_handoff.md` on the death landing; all existing CC0/attributed sources.
- `portal_raider`: set `portal_raider_idle_electrical` loop = yes (trigger_once kept) and rebuild the 1 s file as a seamless loop (crossfade last 100 ms into the head, equal head/tail RMS); extend the ray cue to ~0.6 s with a 60 ms fade-out from the archived laser source and raise its volume to 0.75; normalise steps to -6 dBFS with 5 ms fades; layer a short recorded human grunt (CC0 pain-grunt pack) over `portal_raider_death_01`.

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
