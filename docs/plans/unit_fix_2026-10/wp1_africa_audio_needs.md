# WP1 Africa Strange Forces (012) - Audio delivery and held-source needs

The original held-path audit below is the shared-delivery baseline before the WP1 repair pass.
Current replacements and source hashes for forest idle, plague hoof steps, Pan death and stone recovery are recorded in `wp1_sound_attribution.md` and `wp1_evidence/audio_install/manifest.json`.
The final table at the end records remaining needs; baseline current-byte statements do not apply to those three replaced canonical WAVs or nine added variants.

This package has 43 unique active mod sound paths: 13 are installed and 30 are held. Consumer counts are path-scoped; a shared pool path appears once per relevant package report.

## Installed file facts

The final install has 13 unique path(s) for this package, by file role: loop 2, shot 9, step 2. Each installed row maps to the authoritative install manifest and has an actual-workspace hash match. The global 135-file set is provenance-eligible and decodes as PCM signed 16-bit, 44.1 kHz mono.

The installed derivative SHA is the one listed in the install manifest; the before SHA matches the captured baseline. Mastering is file-level evidence only and does not establish soundeffect state, role, repetition, contact timing, or live-game suitability.

## Held active paths

This package has 30 held path(s): 21 have a blocking provenance row, 9 lack a final per-file provenance row, and 0 are marked provenance-eligible but are absent from the final install. All held bytes match the original baseline SHA-256.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_attack.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_attack_sfx / chaosx_gorilla_heavy_infantry_attack_sound, gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_attack.wav.
Before/current SHA-256: `8680b07b4846a4f12379339fcbe2e65d535283bc519571a2ec87b3bba97c5cd7` / `8680b07b4846a4f12379339fcbe2e65d535283bc519571a2ec87b3bba97c5cd7`; unchanged: `true`; bytes: 124,100.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:40` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_death.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_death_sfx / chaosx_gorilla_heavy_infantry_death_sound, gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_death.wav.
Before/current SHA-256: `44008b58d83f26c3632299d501a3a801295573acc375bf7015d615529ae885c5` / `44008b58d83f26c3632299d501a3a801295573acc375bf7015d615529ae885c5`; unchanged: `true`; bytes: 194,084.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:42` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_idle.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_idle_sfx / chaosx_gorilla_heavy_infantry_idle_sound, gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_idle.wav.
Before/current SHA-256: `94936e5e92a20769409488ed4397df787c43e8443c364932c22cf2252c40f3c5` / `94936e5e92a20769409488ed4397df787c43e8443c364932c22cf2252c40f3c5`; unchanged: `true`; bytes: 176,444.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `loop`; master batch `needs_review`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:38` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_move.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_move_sfx / chaosx_gorilla_heavy_infantry_move_sound, gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_move.wav.
Before/current SHA-256: `560ee95a4e1746972cd2c2b8662a90afb866631ae775fa655a3da60cc407d26e` / `560ee95a4e1746972cd2c2b8662a90afb866631ae775fa655a3da60cc407d26e`; unchanged: `true`; bytes: 105,884.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:39` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_recovery.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_recovery_sfx / chaosx_gorilla_heavy_infantry_recovery_sound, gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_recovery.wav.
Before/current SHA-256: `5d1766c861562d487c80586784d29b2ed42ef84194dabe1e292245bb2e9da929` / `5d1766c861562d487c80586784d29b2ed42ef84194dabe1e292245bb2e9da929`; unchanged: `true`; bytes: 132,344.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:41` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_select.wav`
Consumers: gorilla_heavy_infantry / chaosx_gorilla_heavy_infantry_select.wav.
Before/current SHA-256: `b96fb073c3b1478e5bfcea0d2d51c47d4e8061788aa5db8446189526603ff577` / `b96fb073c3b1478e5bfcea0d2d51c47d4e8061788aa5db8446189526603ff577`; unchanged: `true`; bytes: 158,804.
Review status: `blocked`; unit `chaosx_gorilla_heavy_infantry`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Pant-hoot call / Metal Clanging Noises; creator Ambiguous between Pawel Fedurek et al. and Camshaft64; license Ambiguous: CC BY 4.0 or CC BY-SA 4.0; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Two licensed source families are listed, but neither is assigned to this individual runtime file.
Existing references: `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_integration.md:43` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_death.wav`
Consumers: oracle_recon / chaosx_oracle_recon_death_sfx / chaosx_oracle_recon_death_sound, oracle_recon / chaosx_oracle_recon_death.wav.
Before/current SHA-256: `184cb87973ec4933bdb6e4341b13a4f9823c8193c8a08bb32a904692537e2256` / `184cb87973ec4933bdb6e4341b13a4f9823c8193c8a08bb32a904692537e2256`; unchanged: `true`; bytes: 388,172.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_idle.wav`
Consumers: oracle_recon / chaosx_oracle_recon_idle_sfx / chaosx_oracle_recon_idle_sound, oracle_recon / chaosx_oracle_recon_idle.wav.
Before/current SHA-256: `3146df216da596c84fc09781f6e2153e0b83f04a7c2d5df532776ca1d3b82cfe` / `3146df216da596c84fc09781f6e2153e0b83f04a7c2d5df532776ca1d3b82cfe`; unchanged: `true`; bytes: 388,172.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_move.wav`
Consumers: oracle_recon / chaosx_oracle_recon_move_sfx / chaosx_oracle_recon_move_sound, oracle_recon / chaosx_oracle_recon_move.wav.
Before/current SHA-256: `4303c5996978f64bee3f1c8c281756308a61a0f8c21632ffb970d22fc9ba7e04` / `4303c5996978f64bee3f1c8c281756308a61a0f8c21632ffb970d22fc9ba7e04`; unchanged: `true`; bytes: 264,692.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_observation.wav`
Consumers: oracle_recon / chaosx_oracle_recon_observation_sfx / chaosx_oracle_recon_observation_sound, oracle_recon / chaosx_oracle_recon_observation.wav.
Before/current SHA-256: `73e91a619f21b9e7449705a504410b6b4f6c58625c6a8538e2a7848c710737e8` / `73e91a619f21b9e7449705a504410b6b4f6c58625c6a8538e2a7848c710737e8`; unchanged: `true`; bytes: 317,612.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_recon.wav`
Consumers: oracle_recon / chaosx_oracle_recon_recon_sfx / chaosx_oracle_recon_recon_sound, oracle_recon / chaosx_oracle_recon_recon.wav.
Before/current SHA-256: `c236fff9d51ade19f6918604344a96cd0dca2d8ba08c9a1e13138b78d0df01af` / `c236fff9d51ade19f6918604344a96cd0dca2d8ba08c9a1e13138b78d0df01af`; unchanged: `true`; bytes: 317,612.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/oracle_recon/chaosx_oracle_recon_select.wav`
Consumers: oracle_recon / chaosx_oracle_recon_select.wav.
Before/current SHA-256: `c72d9378d85733091fb48478e99b68fbb7cf1cb2b064f1e6749e6bdcab41d229` / `c72d9378d85733091fb48478e99b68fbb7cf1cb2b064f1e6749e6bdcab41d229`; unchanged: `true`; bytes: 317,612.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_construction.wav`
Consumers: pan_sappers / chaosx_pan_sappers_construction_sfx / chaosx_pan_sappers_construction_sound, pan_sappers / chaosx_pan_sappers_construction.wav.
Before/current SHA-256: `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` / `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a`; unchanged: `true`; bytes: 264,692.
Review status: `blocked`; unit `chaosx_pan_sappers`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Shovel Sound; creator themightyglider; derived from RavenWolfProds; license CC0; URL https://opengameart.org/content/shovel-sound; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-derived candidate hash for this role.
Existing references: `docs/assets/012_africa/models_3d/pan_sappers/audio/finalize_20260912/sound_design_handoff.md:61` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_death.wav`
Consumers: pan_sappers / chaosx_pan_sappers_death_sfx / chaosx_pan_sappers_death_sound, pan_sappers / chaosx_pan_sappers_death.wav.
Before/current SHA-256: `511cbb615ccb75c0180b4d9f859f6c157748bd5f3e83b767b9ff2dade9e04ad2` / `511cbb615ccb75c0180b4d9f859f6c157748bd5f3e83b767b9ff2dade9e04ad2`; unchanged: `true`; bytes: 385,292.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_idle.wav`
Consumers: pan_sappers / chaosx_pan_sappers_idle_sfx / chaosx_pan_sappers_idle_sound, pan_sappers / chaosx_pan_sappers_idle.wav.
Before/current SHA-256: `78deabbc26b553fcc9b5d15ec0a61427908bafd3a5bed9c02edd3b831cbfd697` / `78deabbc26b553fcc9b5d15ec0a61427908bafd3a5bed9c02edd3b831cbfd697`; unchanged: `true`; bytes: 352,892.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_move.wav`
Consumers: pan_sappers / chaosx_pan_sappers_move_sfx / chaosx_pan_sappers_move_sound, pan_sappers / chaosx_pan_sappers_move.wav.
Before/current SHA-256: `4a4f7fe38ef2bf21d1aa480bc7a5682834b780054b42c5acb9be50c940148e8d` / `4a4f7fe38ef2bf21d1aa480bc7a5682834b780054b42c5acb9be50c940148e8d`; unchanged: `true`; bytes: 211,772.
Review status: `blocked`; unit `chaosx_pan_sappers`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Horse gallop on different surfaces; creator congusbongus; source by D4XX; license CC0 source; archive compilation CC BY 4.0; URL https://opengameart.org/content/horse-gallop-on-different-surfaces; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-derived candidate hash for this role.
Existing references: `docs/assets/012_africa/models_3d/pan_sappers/audio/finalize_20260912/sound_design_handoff.md:26` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_sabotage.wav`
Consumers: pan_sappers / chaosx_pan_sappers_sabotage_sfx / chaosx_pan_sappers_sabotage_sound, pan_sappers / chaosx_pan_sappers_sabotage.wav.
Before/current SHA-256: `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` / `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b`; unchanged: `true`; bytes: 248,204.
Review status: `blocked`; unit `chaosx_pan_sappers`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Fantasy Accessory SFX Library glass vial; creator Vehicle; license CC0; URL https://opengameart.org/content/fantasy-accessory-sfx-library; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-derived candidate hash for this role.
Existing references: `docs/assets/012_africa/models_3d/pan_sappers/audio/finalize_20260912/sound_design_handoff.md:62` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_select.wav`
Consumers: pan_sappers / chaosx_pan_sappers_select.wav.
Before/current SHA-256: `ff66173a723b36b8e6e80550c040f4841bef491d8e49662c597485f0ccac1a19` / `ff66173a723b36b8e6e80550c040f4841bef491d8e49662c597485f0ccac1a19`; unchanged: `true`; bytes: 264,692.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/012_africa/units/riverborn/chaosx_riverborn_attack.wav`
Consumers: riverborn / chaosx_riverborn_attack_sfx / chaosx_riverborn_attack_sound, riverborn / chaosx_riverborn_attack.wav.
Before/current SHA-256: `26ffe43934ac355da6df6887968b061ad54bef41a80bbe7d2bc69f506351d994` / `26ffe43934ac355da6df6887968b061ad54bef41a80bbe7d2bc69f506351d994`; unchanged: `true`; bytes: 264,400.
Review status: `blocked`; unit `chaosx_riverborn`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:29` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/riverborn/chaosx_riverborn_death.wav`
Consumers: riverborn / chaosx_riverborn_death_sfx / chaosx_riverborn_death_sound, riverborn / chaosx_riverborn_death.wav.
Before/current SHA-256: `ebc3839c560129e25fd2bfe8a763ed5bf0e4a2de53ecd4a09ec10b4230b6af33` / `ebc3839c560129e25fd2bfe8a763ed5bf0e4a2de53ecd4a09ec10b4230b6af33`; unchanged: `true`; bytes: 388,172.
Review status: `blocked`; unit `chaosx_riverborn`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:26` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/riverborn/chaosx_riverborn_idle.wav`
Consumers: riverborn / chaosx_riverborn_idle_sfx / chaosx_riverborn_idle_sound, riverborn / chaosx_riverborn_idle.wav.
Before/current SHA-256: `8ecdf4c1e95588304f4070ae07c5f8481a95c75891f6f199cd1ecf0b2a9d2474` / `8ecdf4c1e95588304f4070ae07c5f8481a95c75891f6f199cd1ecf0b2a9d2474`; unchanged: `true`; bytes: 441,092.
Review status: `blocked`; unit `chaosx_riverborn`; role `loop`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:21` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/riverborn/chaosx_riverborn_move.wav`
Consumers: riverborn / chaosx_riverborn_move_sfx / chaosx_riverborn_move_sound, riverborn / chaosx_riverborn_move.wav.
Before/current SHA-256: `146de88d1393c83c9b92b9de29ad29c2e4e8f23613c3e4eed778211b25fec75f` / `146de88d1393c83c9b92b9de29ad29c2e4e8f23613c3e4eed778211b25fec75f`; unchanged: `true`; bytes: 282,332.
Review status: `blocked`; unit `chaosx_riverborn`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:22` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/riverborn/chaosx_riverborn_select.wav`
Consumers: riverborn / chaosx_riverborn_select.wav.
Before/current SHA-256: `5e923a7c38e2dee453f1f174301109e70d65d17df23f48b0fed63b295ee42b6a` / `5e923a7c38e2dee453f1f174301109e70d65d17df23f48b0fed63b295ee42b6a`; unchanged: `true`; bytes: 315,956.
Review status: `blocked`; unit `chaosx_riverborn`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:20` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/riverborn/chaosx_riverborn_water_transition.wav`
Consumers: riverborn / chaosx_riverborn_water_transition_sfx / chaosx_riverborn_water_transition_sound, riverborn / chaosx_riverborn_water_transition.wav.
Before/current SHA-256: `739e9720bc812c573aed579f7db5687b9d92496175cbfe67e70b64a7274878fa` / `739e9720bc812c573aed579f7db5687b9d92496175cbfe67e70b64a7274878fa`; unchanged: `true`; bytes: 352,892.
Review status: `blocked`; unit `chaosx_riverborn`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: Current runtime bytes are not joined to the source-backed cue outputs; the handoff states there is no source-to-runtime synchronization claim.
Existing references: `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/sound_design_handoff.md:25` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
Candidate sources recorded in review (not approved for this exact runtime file): Flowing-water-100019 by Fg2, Public domain, https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg; Ducks landing in water by U.S. Fish and Wildlife Service, Public domain, https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg; Bamboo-stick swishes by qubodup, CC0, https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes; Medieval weapon impacts by Ben Jaszczak / Brian Nelson, Still North Media, CC0, https://opengameart.org/node/146863.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_attack.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_attack_sfx / chaosx_stone_cohorts_attack_sound, stone_cohorts / chaosx_stone_cohorts_attack.wav.
Before/current SHA-256: `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` / `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b`; unchanged: `true`; bytes: 248,204.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Metal Clanging Noises; creator Camshaft64; license CC BY-SA 4.0; URL https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:9` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_collapse_recovery.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_collapse_recovery_sfx / chaosx_stone_cohorts_collapse_recovery_sound, stone_cohorts / chaosx_stone_cohorts_collapse_recovery.wav.
Before/current SHA-256: `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` / `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a`; unchanged: `true`; bytes: 264,692.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: Metal Clanging Noises; creator Camshaft64; license CC BY-SA 4.0; URL https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:10` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_death.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_death_sfx / chaosx_stone_cohorts_death_sound, stone_cohorts / chaosx_stone_cohorts_death.wav.
Before/current SHA-256: `7ffbe2820f00621a1db3743edc6518b7f71f65da8b2e19906ea5e7f504c1d842` / `7ffbe2820f00621a1db3743edc6518b7f71f65da8b2e19906ea5e7f504c1d842`; unchanged: `true`; bytes: 388,172.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: WWS Quern-stones; creator Work With Sounds / recordist Monika Widzicka; license CC BY 4.0; URL https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:11` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_idle.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_idle_sfx / chaosx_stone_cohorts_idle_sound, stone_cohorts / chaosx_stone_cohorts_idle.wav.
Before/current SHA-256: `729f14dede6b178678544bbd880a5c71498393f034c1c6684ef3c778cb5d4e49` / `729f14dede6b178678544bbd880a5c71498393f034c1c6684ef3c778cb5d4e49`; unchanged: `true`; bytes: 388,172.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `loop`; master batch `needs_review`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: WWS Quern-stones; creator Work With Sounds / recordist Monika Widzicka; license CC BY 4.0; URL https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:7` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_move.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_move_sfx / chaosx_stone_cohorts_move_sound, stone_cohorts / chaosx_stone_cohorts_move.wav.
Before/current SHA-256: `9ecc737021ea144c452786879909f98ab422d62d6312468a8c8ab7401b810743` / `9ecc737021ea144c452786879909f98ab422d62d6312468a8c8ab7401b810743`; unchanged: `true`; bytes: 282,332.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `step`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: WWS Quern-stones; creator Work With Sounds / recordist Monika Widzicka; license CC BY 4.0; URL https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:8` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_select.wav`
Consumers: stone_cohorts / chaosx_stone_cohorts_select.wav.
Before/current SHA-256: `9e57db53e3f6b73f099d72c54f2d461207765941ccfc76b840d85668023251eb` / `9e57db53e3f6b73f099d72c54f2d461207765941ccfc76b840d85668023251eb`; unchanged: `true`; bytes: 247,052.
Review status: `blocked`; unit `chaosx_stone_cohorts`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: WWS Quern-stones; creator Work With Sounds / recordist Monika Widzicka; license CC BY 4.0; URL https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg; original SHA `not recorded`; original path `not recorded`.
Held reason: Current input SHA differs from the selected source-to-cue output SHA for this role.
Existing references: `docs/assets/012_africa/models_3d/stone_cohorts/audio/finalize_20260912/ATTRIBUTION.md:6` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

## Other staged recovery outputs

2 staged output(s) match this package but are absent from the final install manifest:

- `chaosx_gorilla_heavy_infantry` / `chaosx_gorilla_heavy_infantry_idle_sfx` (loop): output SHA `ace79183ba21a2c563b7cfa9ecf1d400de6193087957580b85ff9e1219872add`; staging path `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\unit_fix_2026-10\audio_evidence\recovery2_evidence\staged\a048.wav`. Candidate status is staged only.
- `chaosx_stone_cohorts` / `chaosx_stone_cohorts_idle_sfx` (loop): output SHA `5c3b427d2ddf411e9daa7130fc73022e0528b034a94ac4161ae7413cd447ac34`; staging path `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\unit_fix_2026-10\audio_evidence\recovery2_evidence\staged\a071.wav`. Candidate status is staged only.

## Recording requirements from the user-authored plan

The following brief is transcribed from section 2 of `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` (SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`). It records the requested role, timing/length, and source-license choices. It is a production brief, not approval for an existing candidate or runtime file.

- `forest_giants`: idle = creaking wood and leaf rustle (CC0 forest creak recording) high-passed at 40 Hz with DC removed; attack = one heavy wood whoosh plus ground impact per blow at frames 48/76 (1.60/2.53 s), 3 variants (CC0 whoosh + CC0 heavy impact); death = trunk crack and crash (CC0 tree-fall recording); emergence = roots tearing and leaves; s16 through the mastering script.
- `gorilla_heavy_infantry`: replace attack.wav with one 0.4-0.6 s heavy iron-on-earth impact (3 variants) cut from a CC0 anvil/sledge-on-ground recording (Freesound CC0) at events frame 22 (0.73 s) and frame 101 (3.37 s); replace the chimp pant-hoot with a real gorilla chest-beat or bark (Wikimedia Commons or Freesound CC BY zoo recording, attributed); defend uses a leather/forearm thud from the same impact pack; move = two or three heavy footfalls with 60-200 Hz body (CC0 heavy-step pack); all through the mastering script.
- `oracle_recon`: trim recon.wav to a 20 ms lead-in and place one event at frame 63; idle = breathy chant/whisper in the 200 Hz-4 kHz band (CC0 or CC BY vocal ambience, sub layer only underneath); death = vocal gasp plus body fall (CC0); observation = short chant swell from the same vocal source; move = bare-foot steps, 2-3 variants (CC0); s16 through the mastering script.
- `pan_sappers`: sabotage = fuse hiss into a demolition blast (1.0-1.2 s, blast at ~0.15 s, 3 variants) from a CC0 fuse recording plus a CC0/PD explosion (Sonniss GDC or Freesound CC0) at the new throw frame; construction = tool clatter and wire tick (CC0 workshop pack); move = soft hoof-on-dirt steps (2-3 variants, CC0 goat/deer hoof recording); death = goat bleat (CC0 farm recording) layered with a body fall (bigsoundbank CC0 Body Fall) with a 10 ms fade-in; idle = breath and cloth rustle; everything s16 through the mastering script.
- `plague_carriers`: move = hoof-on-dirt steps, 4 variants (CC0 donkey/horse hoof recording); remove deploy_sfx from the attack state (keep it on deploy/support_attack); add a bray at frame 12 (0.40 s) from a CC0/CC BY donkey recording (Freesound or Wikimedia Commons, attributed); trim the idle and death silent tails; 2-3 variants per cue; format already s16.
- `riverborn`: layer a short spear whoosh (CC0 swish pack) and a wet thud (CC0 impact pack) under the existing splash with impacts at frames 54/68 (1.80/2.27 s), 3 variants; move = wet bare-foot steps, 2-3 variants (CC0 wet footstep recording); select gets a 5 ms fade-in; water hiss kept for idle and water_transition only; s16 through the mastering script.
- `stone_cohorts`: one 0.3-0.5 s stone-and-iron thrust impact (3 variants, CC0 rock-impact pack) at frames 30/61/89; death = grinding rock-fall cut from a PD/CC0 rockslide recording (not the forest giant's file); collapse_recovery = settling-stone rumble from the same source; keep the grinding idle/move; s16 through the mastering script.

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

## WP1 repair disposition and remaining recordings

The parent installed twelve source-derived WAVs: two forest idle beds, four plague hoof contacts, three Pan death takes and three stone-recovery takes.
Every installed file has source/member/cut/output hashes and fresh runtime-byte metrics in the audio install evidence.
The old forest attack, riverborn water impact/movement, Pan construction/sabotage, donkey voice, gorilla voice and other unresolved cues remain at their existing recordings.
The model and waveform review interfaces do not establish live listening; the orchestrator's role/transition/plant checks remain required.

| Unit | Delivered | Recording still needed and duration | License options / candidate sources |
|---|---|---|---|
| gorilla_heavy_infantry | Finite death blood burst; no sound source substitution. | Real gorilla bark/chest beat, about 0.5-1.5 s; three 0.4-0.6 s iron-on-earth blows; forearm/leather block thuds, about 0.2-0.4 s; two or three 0.2-0.4 s heavy footfalls with body energy. | CC0 or attributed CC BY zoo/field recordings; Wikimedia Commons gorilla calls, Freesound CC0 sledge/anvil/earth impacts. The archived chimp pant-hoot is the wrong species and metal-clanging lineage is unresolved. |
| pan_sappers | Three public-domain goat calls combined with the clean archived CC0 leonelmail dirt fall, preserving the intended landing phase. | Two or three goat/deer hoof-on-dirt steps, about 0.1-0.3 s; three fuse-hiss/demolition-blast cues, 1.0-1.2 s with blast near 0.15 s; workshop tool clatter and wire ticks, about 0.2-0.6 s; breath/cloth ambience suitable for idle. | CC0 farm/hoof and workshop recordings, or already attributed CC BY/CC BY-SA packs. Existing Shovel Sound supplies only one shovel contact; it is not a complete construction cue. The clipped remaxim/qubodup fall is rejected and is not used in the delivered takes. |
| stone_cohorts | Three CC BY 4.0 Work With Sounds / Monika Widzicka quern-stone grinding/settling takes. | Three 0.3-0.5 s stone-and-iron thrust impacts; a distinct 1-3 s rockslide/falling-stone death with appropriate settling detail. | CC0 rock-impact packs or PD/CC0 rockslide recordings. [WWS Quern-stones](https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg) covers grinding only; it does not supply a rockslide or thrust. |
| riverborn | Five archived CC0 bamboo swishes remain unwired candidates; finite death blood burst. | Three wet-thud impact takes, about 0.2-0.5 s, under the existing splash; two or three wet bare-foot steps, about 0.1-0.3 s; source/variation review for selection and water hiss. | CC0 wet impacts/footsteps or PD water recordings. [Bamboo swishes](https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes) supply air movement; the dry shaft contacts fail RMS gates, and the previously referenced water originals are absent. |
| forest_giants | Two distinct CC0 wood-creak loop beds, properly wired for continuous idle. | Three heavy wood-whoosh/ground blows, about 0.4-0.8 s; 1-3 s trunk-crack/tree crash; root-tear and leaf movement for emergence, about 0.5-1.5 s; distinct motion/selection/death role review. | CC0 field/Foley wood, earth-impact, tree-fall and roots/leaves recordings. [Wood Creak](https://freesound.org/people/claretcanelon/sounds/346140/) covers the delivered idle; the archived small-axe/dry-branch cuts are too light for the giant strike and remain candidates. |
| oracle_recon | Finite death blood burst; no source substitution. | Barefoot contacts, about 0.1-0.3 s; breathy chant/whisper bed and observation swell in 200 Hz-4 kHz, about 1-3 s; a gasp and role-matched body fall, about 0.3-1 s. | CC0 or attributed CC BY vocal ambience/footsteps. No exact eligible per-file source chain was found for the current cues; low-band existing recordings remain held. |
| plague_carriers | Four distinct CC0 outdoor ground/grass horse-hoof contacts; wrong attack deployment hiss removed. | Donkey bray, about 0.4-1 s, with two or three real takes; donkey-appropriate idle/death vocal and tail/variation review; selection/source binding review. | CC0 or attributed CC BY donkey field/zoo recordings from Freesound or Wikimedia Commons. [The archived horse collection](https://opengameart.org/content/horse-gallop-on-different-surfaces) supplies hoof contacts, not a bray; indoor/cartoon members were not selected. |

Selection is a separate engine consumer from entity-state idle.
No per-subunit selection voice is claimed from the new idle or movement pools; country/original-tag voice routing and mixed-infantry limitations remain open.
Every genuinely missing recording remains a need for the orchestrator to source with permission; none was downloaded by this pass.
