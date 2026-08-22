# Event 016 D’Rhondan portrait package handoff

Date: 2026-08-21.

Owner: `/root/dhr_portraits`.

Status: fictional native-ImageGen portrait package complete through processing, DDS conversion, portrait-specific GFX registration, deterministic visual/round-trip evidence, and parent review of all full portraits and role cards.

## Scope and source state

This package covers the exact twelve fictional D’Rhondan identities locked by the Event 016 alien addendum: three regime leaders, five civilian advisors, one high-command figure, and three commanders. Every subject is a bald muted-green alien with large intelligent black eyes, but the faces, ages, silhouettes, attire, palette, and role cues are individually generated and visually distinct.

The source mode is `fictional_high_chaos` through native ImageGen. No Internet identity source, archival placeholder, real-person likeness, Kruger art, RunPod job, or user-supplied grounded replacement is involved. Therefore the replacement state is `not_applicable_fictional_native_imagegen` rather than `replacement_pending`.

The parent country/runtime owner must use the exact IDs and tokens below; the earlier provisional names such as `DHR_vael_ix` and `DHR_talor_vesh` are not approved roster identifiers.

## Stable IDs, sprite tokens, and runtime paths

All full portraits are `156x210` and are registered in `interface/016_dhrondan_portraits.gfx`. Role cards are canonical `65x67` dossier-card compositions and are also registered in that file.

| Character ID | Name and class | Stable full sprite and path | Stable role sprite and path | Route palette or role cue | Review state |
|---|---|---|---|---|---|
| `DHR_emperor_vael_ix` | Emperor Vael IX, regime leader | `GFX_portrait_DHR_emperor_vael_ix`; `gfx/leaders/DHR/leader_dhr_emperor_vael_ix.dds` | — | Imperial brass and deep crimson robes, warm imperial background | `parent_approved` |
| `DHR_first_calculant_sera_qel` | First Calculant Sera Qel, regime leader | `GFX_portrait_DHR_first_calculant_sera_qel`; `gfx/leaders/DHR/leader_dhr_first_calculant_sera_qel.dds` | — | Cold teal and geometric blue mantle, technocratic precision | `parent_approved` |
| `DHR_speaker_ilyr_ren` | Speaker Ilyr Ren, regime leader | `GFX_portrait_DHR_speaker_ilyr_ren`; `gfx/leaders/DHR/leader_dhr_speaker_ilyr_ren.dds` | — | Parchment blue and civic cream robes, assembly calm | `parent_approved` |
| `DHR_archivist_thaal_ven` | Archivist Thaal Ven, advisor | `GFX_portrait_DHR_archivist_thaal_ven`; `gfx/leaders/DHR/leader_dhr_archivist_thaal_ven.dds` | `GFX_portrait_DHR_advisor_archivist_thaal_ven`; `gfx/interface/ideas/016_dhrondan/advisor_dhr_archivist_thaal_ven.dds` | Umber/parchment robes and blank data tablet | `parent_approved` |
| `DHR_logistics_oracle_nym_vor` | Logistics Oracle Nym Vor, advisor | `GFX_portrait_DHR_logistics_oracle_nym_vor`; `gfx/leaders/DHR/leader_dhr_logistics_oracle_nym_vor.dds` | `GFX_portrait_DHR_advisor_logistics_oracle_nym_vor`; `gfx/interface/ideas/016_dhrondan/advisor_dhr_logistics_oracle_nym_vor.dds` | Navy/oxidized-amber harness and blank cargo discs | `parent_approved` |
| `DHR_harmonic_envoy_rae_syl` | Harmonic Envoy Rae Syl, advisor | `GFX_portrait_DHR_harmonic_envoy_rae_syl`; `gfx/leaders/DHR/leader_dhr_harmonic_envoy_rae_syl.dds` | `GFX_portrait_DHR_advisor_harmonic_envoy_rae_syl`; `gfx/interface/ideas/016_dhrondan/advisor_dhr_harmonic_envoy_rae_syl.dds` | Indigo/copper/lilac robes and resonance plates | `parent_approved` |
| `DHR_war_calculant_orr_kesh` | War Calculant Orr Kesh, high command | `GFX_portrait_DHR_war_calculant_orr_kesh`; `gfx/leaders/DHR/leader_dhr_war_calculant_orr_kesh.dds` | `GFX_portrait_DHR_high_command_war_calculant_orr_kesh`; `gfx/interface/ideas/016_dhrondan/high_command_dhr_war_calculant_orr_kesh.dds` | Basalt/ochre armored mantle and cheek ridges | `parent_approved` |
| `DHR_genetic_steward_vel_ara` | Genetic Steward Vel Ara, advisor | `GFX_portrait_DHR_genetic_steward_vel_ara`; `gfx/leaders/DHR/leader_dhr_genetic_steward_vel_ara.dds` | `GFX_portrait_DHR_advisor_genetic_steward_vel_ara`; `gfx/interface/ideas/016_dhrondan/advisor_dhr_genetic_steward_vel_ara.dds` | Bone/sea-glass/violet robes and sealed ampoules | `parent_approved` |
| `DHR_shadow_listener_thel_ior` | Shadow Listener Thel Ior, advisor | `GFX_portrait_DHR_shadow_listener_thel_ior`; `gfx/leaders/DHR/leader_dhr_shadow_listener_thel_ior.dds` | `GFX_portrait_DHR_advisor_shadow_listener_thel_ior`; `gfx/interface/ideas/016_dhrondan/advisor_dhr_shadow_listener_thel_ior.dds` | Charcoal/deep-plum robes and blank receiver | `parent_approved` |
| `DHR_field_vector_kaal_dren` | Field Vector Kaal Dren, commander | `GFX_portrait_DHR_field_vector_kaal_dren`; `gfx/leaders/DHR/leader_dhr_field_vector_kaal_dren.dds` | `GFX_portrait_DHR_commander_field_vector_kaal_dren`; `gfx/interface/ideas/016_dhrondan/commander_dhr_field_vector_kaal_dren.dds` | Field green/cobalt/ochre expedition mantle and route slates | `parent_approved` |
| `DHR_enclave_guardian_syr_vek` | Enclave Guardian Syr Vek, commander | `GFX_portrait_DHR_enclave_guardian_syr_vek`; `gfx/leaders/DHR/leader_dhr_enclave_guardian_syr_vek.dds` | `GFX_portrait_DHR_commander_enclave_guardian_syr_vek`; `gfx/interface/ideas/016_dhrondan/commander_dhr_enclave_guardian_syr_vek.dds` | Forest/maroon/dull-silver armor and shield collar | `parent_approved` |
| `DHR_orbital_liaison_omn_tal` | Orbital Liaison Omn Tal, commander | `GFX_portrait_DHR_orbital_liaison_omn_tal`; `gfx/leaders/DHR/leader_dhr_orbital_liaison_omn_tal.dds` | `GFX_portrait_DHR_commander_orbital_liaison_omn_tal`; `gfx/interface/ideas/016_dhrondan/commander_dhr_orbital_liaison_omn_tal.dds` | Cobalt/silver/violet robes, navigation ring, orbital arcs | `parent_approved` |

The gameplay owner should reference the full sprite token for character portrait fields and the class-specific role token for advisor/high-command/commander UI fields. The portrait worker owns all binary assets and `interface/016_dhrondan_portraits.gfx`; no gameplay definitions, country setup, traits, history, localisation, events, focuses, decisions, shared portrait files, or catalog files were edited.

## Native ImageGen result lineage and exact prompts

The complete prompt text is retained in `docs/assets/016_brilliant_scientist/dhrondan_portraits/prompts/dhrondan_imagegen_prompts.md`. Each section records the exact native ImageGen result path and the copied workspace source path. The prompt set consistently requests a fictional HOI4-style painted portrait, bald muted-green alien, large intelligent black eyes, centered head and shoulders, role-specific attire and palette, no text, no insignia, no watermark, no human face, no copied artwork, and no gore.

| Character ID | Native ImageGen result | Copied source | Prompt section and distinguishing instruction |
|---|---|---|---|
| `DHR_emperor_vael_ix` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-54695991-961e-49b4-b286-9b36c6d678af.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_emperor_vael_ix_source.png` | `## Emperor Vael IX`; about 70, narrow angular face, imperial brass/deep crimson robes |
| `DHR_first_calculant_sera_qel` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-71db0b9b-df86-47a4-8a75-105e78e8e9d4.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_first_calculant_sera_qel_source.png` | `## First Calculant Sera Qel`; about 38, triangular face, cold teal/blue geometric mantle |
| `DHR_speaker_ilyr_ren` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-45cafd87-2300-45e9-964d-3d9d1dafb30c.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_speaker_ilyr_ren_source.png` | `## Speaker Ilyr Ren`; about 55, broad oval face, parchment-blue civic robes |
| `DHR_archivist_thaal_ven` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-bfc904e9-3bc8-49be-b14b-63ff5b5cf122.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_archivist_thaal_ven_source.png` | `## Archivist Thaal Ven`; about 72, long narrow face, umber/parchment robes, blank tablet |
| `DHR_logistics_oracle_nym_vor` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-5906c973-af79-42a1-a2fc-2fb257c4c19e.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_logistics_oracle_nym_vor_source.png` | `## Logistics Oracle Nym Vor`; about 48, compact round face, navy/amber harness and cargo discs |
| `DHR_harmonic_envoy_rae_syl` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-31b25376-84a3-463e-ae7b-093cf63b84e5.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_harmonic_envoy_rae_syl_source.png` | `## Harmonic Envoy Rae Syl`; about 34, heart-shaped face, indigo/copper/lilac robes and resonance plates |
| `DHR_war_calculant_orr_kesh` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-c10cae43-f152-4aa7-9520-b9822a5fc0a2.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_war_calculant_orr_kesh_source.png` | `## War Calculant Orr Kesh`; about 59, square face, basalt/ochre armor and cheek ridges |
| `DHR_genetic_steward_vel_ara` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-b5fe5bf3-01b0-4016-94c9-049072cf6fe5.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_genetic_steward_vel_ara_source.png` | `## Genetic Steward Vel Ara`; about 46, long oval face, pale clinical robes and sealed ampoules |
| `DHR_shadow_listener_thel_ior` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-e3e4ead0-8fd5-4593-9c24-9079217187d9.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_shadow_listener_thel_ior_source.png` | `## Shadow Listener Thel Ior`; about 61, weathered narrow face, charcoal/plum robes and receiver |
| `DHR_field_vector_kaal_dren` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-263bb72f-fbe3-46f2-bdb8-2bae3394873e.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_field_vector_kaal_dren_source.png` | `## Field Vector Kaal Dren`; about 41, wedge face, field green/cobalt/ochre mantle and route slates |
| `DHR_enclave_guardian_syr_vek` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-d10d2043-2e35-4681-8e67-c4d06de33f45.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_enclave_guardian_syr_vek_source.png` | `## Enclave Guardian Syr Vek`; about 52, shield-shaped face, forest/maroon/silver armor |
| `DHR_orbital_liaison_omn_tal` | `C:\Users\klimp\.codex\generated_images\01a02436-6390-7f73-8cab-9894ec63e3f7\exec-3f7eb435-54a7-48a3-a88e-f49fcb19bb7d.png` | `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/DHR_orbital_liaison_omn_tal_source.png` | `## Orbital Liaison Omn Tal`; about 29, high narrow face, cobalt/silver/violet robes and orbital ring |

## Processing and compositor evidence

The source masters are archived in `docs/assets/016_brilliant_scientist/dhrondan_portraits/source_png/` with native dimensions around `1080x1454` to `1082x1456`. `process_dhrondan_portraits.py` center-cover crops each source to the exact `156:210` ratio and uses Pillow LANCZOS to produce opaque RGB `156x210` masters in `processed_png/`.

The nine nonleader role cards use the canonical vanilla advisor template at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`. The measured opening is center `(24.76151027919129, 30.645146882359736)`, size `(30.477406015014285, 45.09450833210553)`, rotation `-4.76` degrees, alpha threshold `128`. `create_advisor_icon.py` was run for each card with portrait size `30.477406 45.094508`, offset `0 0`, rotation `-4.76`, a linked placement study, alignment preview, 4x review preview, and `sepia_strength 0.18`. Each compositor metadata file records zero opening gap, zero inner-edge gap, zero exterior alpha leak, no stretch, and under-frame bleed.

The compositor staged DDS files remain under `review/*_compositor.dds` as evidence. Final runtime DDS files were then converted through the required bundled converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` with `156x210` for full portraits and `65x67` for role cards. The runtime files are uncompressed BGRA, one-level DDS textures.

## Hash and dimension evidence

The complete machine-readable records are `metadata/portrait_manifest.json`, `metadata/process_manifest.json`, and `metadata/dds_validation.json`. The tables below include every source, processed full PNG, full runtime DDS, role-card preview PNG, and role-card runtime DDS hash.

### Full portrait source/process/runtime hashes

| ID | Source PNG SHA-256 | Processed `156x210` PNG SHA-256 | Full runtime DDS SHA-256 |
|---|---|---|---|
| `DHR_emperor_vael_ix` | `5612f97ad6643c4ccc509807866afb726f41fa999c594049cd1c8eea4992d730` | `41abcae3b06ac09111b1484998562a209fac3f5a98ccb4f363a0a7b2248f0fa7` | `93b6d271c935013a24ff77b7363095995c7f16e44058b653b37aa6c166b50aa2` |
| `DHR_first_calculant_sera_qel` | `42cc4f4d2f64102238fc1f23a2a2878b982ce9c7fb58024604b19d8c5ee400ad` | `1360c566d4006a38de4e4716da31ea0d54fdffdef32c985d34d946735a600975` | `0d8aa938232818c0a72fa2b91e7d3edb671a0ec486c6bbe6c135d0b2dba79ed7` |
| `DHR_speaker_ilyr_ren` | `4781dace30f5f435ff2e7587987cf759d30ced056fa36b18966303173344baf7` | `6a24ff5e2e45b40b48f237126b3ad1afc53f02c627b825a9c657be261ddee952` | `63623cbe5074580cda92229d280a7f5de9a3139d3e8d69a9ffc3bcc7b8b0e829` |
| `DHR_archivist_thaal_ven` | `f663c284e39895bee326be35e0a74e4a15045357f467fcfacd676cabc6592971` | `1f72e1dd7e890d102fc4d97bf7a052dbdd9cd5ea19efe70069d09b09d964e98a` | `a9de7cf7c4f814ea92bbcbc06431e3bb6d634a59d76c18b678598c8f1206b8c5` |
| `DHR_logistics_oracle_nym_vor` | `a6f6beb4c3789b72f8f2576370dd55eb1417f1f60f04dc074a4ffd45ef84aa04` | `85690cca85e7e06289816a563acdc68a761e88cf7655b02a255ebbfcbd1a7cdc` | `011d1587e0fd4e0843b2ea58150d01e4a8400403ef8b943fe63f765aa28c6d43` |
| `DHR_harmonic_envoy_rae_syl` | `3af4883ea8561ff4f6cb923b69a19063a48dc09a20495c42278e4b062971af16` | `ecf5a849b30b50dfa40245b4d22f570cb11b8474b9c020e1c41b3b85483c9989` | `df819dca0760652cb5897a14fa7f7419a25d05c25bb8804f2a82b05720119239` |
| `DHR_war_calculant_orr_kesh` | `c99f97580f6fcfed24a0a1edb6d560697df7a7897f53c69cf96d629008b1fafc` | `bc848bbfc123c8aafa2808db97f8f562bfa4d648422f4d9d0d4117a5f1cd3f6d` | `8672bcef8531f9ad67171b2f5b5739883041dea3f1c53e628479608ed2f036cb` |
| `DHR_genetic_steward_vel_ara` | `f459cf082e423d3361c27bafd596da1dca3737e10b06a7ce493edcc77896a4d1` | `64d443e7b69385396755aa4e15fdf6d6d0f18043fbba06dc6bd0318d636b4556` | `dc981c6286c9f70de09ac4b1dc3d5fba42760b548a36d862b19ebc28deaa95fa` |
| `DHR_shadow_listener_thel_ior` | `144c576cb32af686d52d2b6425561bbb34997eb4b5fb4ea3006a65694b613e10` | `933101a579404ad97cf2f5ba82c279102fab07e70c6dbab93974380021537710` | `2205e73b63b73317e7ea6b04050f6229d2df38fde791975a423aacc54465adb7` |
| `DHR_field_vector_kaal_dren` | `a5d62c3db070a589b7b05c029ab2ff157afb22c5704cd7c7621e99ddf9351eb9` | `b1adcbee8219ef33353ae25d60764cb76e23caf43940ceae03b548c5748f3822` | `6bb93f8a2001588690502f12e0d68c399a8ad9ee30bb3e3e80bbe1299debfee9` |
| `DHR_enclave_guardian_syr_vek` | `05595655beb49cab5720ef8e25196fd9ae505068ef7e29c03db243e14929a20c` | `20148b27f382ab14b44685f7e25740a2ed96e8124b7713533338b3c193a8170f` | `0f25207834f54712aa280e466e9e0be98b44c8f8f1d683f25930910c7b2492b1` |
| `DHR_orbital_liaison_omn_tal` | `d0f70f613ffe9db830e09d3927ca58e1cf9dcbd1e5a15e66a3b69cd469c92b6e` | `c18ef6d630ffd9dfa08e727d67ea5865480d6c0e0a06aceb3a71b9588af892d2` | `589bc912037016f59abf4e11378a0d57d106f691121a6d7ca6232753b6af12bd` |

Every full output is exactly `156x210`, opaque RGBA after decode with alpha range `[255, 255]`, and decoded pixel bytes match the processed PNG exactly.

### Role-card preview/runtime hashes

| ID | Role-card preview `65x67` PNG SHA-256 | Role-card runtime DDS SHA-256 |
|---|---|---|
| `DHR_archivist_thaal_ven` | `217ccf029f45ec68b076484015d33865d30a769a2fe0fba16dc9decf74af8370` | `0ac32ae6389e611ae3b2e3e29ec9c6d3844439f6c6758f37ff8a92e686bf3d48` |
| `DHR_logistics_oracle_nym_vor` | `63d9ad3a6a5ec2f46f28ef56f7a84f73cf186394dab76783d7fb4039ddd70d15` | `46bf7050825fef5474b9bb3321ec734c5b3d7a8a97b0feacda5dd343616cb337` |
| `DHR_harmonic_envoy_rae_syl` | `d1286a3ce528d855712b871e6b698c5710790d900abd75d6ac84b8f574fa61e1` | `77b85230403c231d19f8ea98c401304a4d296206a99ed8b36eed084afe9a76f4` |
| `DHR_war_calculant_orr_kesh` | `3f2b4dcef91e800b3f203e4a46ba1e703a3ee6d0fd21197915d4e9750cbfb8de` | `fdd333852d3bf8361df3d7d1d71d292bde4b929a0f199cbf50c9811dd8c648f8` |
| `DHR_genetic_steward_vel_ara` | `98fdf323c8fa302c533243e448e867158413a68b1899b592757d3dd818b3fa41` | `311ac5de75a65c8b61101ef0d1fdd4b4c6fab3ec9096abff46dd87f3b4aafc78` |
| `DHR_shadow_listener_thel_ior` | `589137ce91ed72615f7440f7bba16df42dd008fe8fb803abe70ec87f72784fc2` | `c6fceb1384be70902a71539bd2c1fed08bdb27f87cfabbc826db4379d3c80ff6` |
| `DHR_field_vector_kaal_dren` | `ca5401ad4cdc54c166f15d92f3597f7468580cc0efdbd2e507d129ef3c636b09` | `7fffac94ba9dfa538407446b072335d6740da3965afc7d44475b9e6df4b200fe` |
| `DHR_enclave_guardian_syr_vek` | `6a1d443160810af0816920581498220d2e321e03b9a6a8ec1a1af820fe5094da` | `3ded2669efb8fb608f43857c200376e772fc48c23d2d41895e42dde04a6b05a8` |
| `DHR_orbital_liaison_omn_tal` | `ed7e14649ac7e6117bc9d1e8c2a39bbed91690986413e98c8a230318937a5eb0` | `8c3e31050faf54ad8e5bab8319dd67888199a19eb9db67950cedc38c1a9dbb90` |

Every role-card output is exactly `65x67`, decodes with alpha range `[0, 255]`, preserves transparent template corners, and matches the compositor preview pixel-for-pixel after conversion. Each runtime DDS has the required uncompressed BGRA masks, DDS header size `124`, texture caps, one-level mip declaration, and expected byte length.

## Visual QA and evidence

The full-roster source contact sheet is `docs/assets/016_brilliant_scientist/dhrondan_portraits/review/dhrondan_source_contact_sheet.png`. The decoded full runtime contact sheet is `review/dhrondan_full_decoded_contact_sheet.png`. The decoded role-card contact sheet is `review/dhrondan_role_cards_decoded_contact_sheet.png`.

The parent agent visually approved the full decoded roster and role-card contact sheets. All twelve identities are distinct bald muted-green aliens with large black eyes, differentiated faces, ages, attire, palettes, and role cues. All nine role cards retain the inspected template tilt, scale, transparent corners, and clean paper/frame edges. No duplicated source or processed SHA-256 was found.

Placement evidence for every role card is retained as `review/dhr_<suffix>_placement_study.png`, with corresponding `alignment_8x.png` and `4x.png` previews. Per-card compositor metadata under `metadata/dhr_<suffix>_advisor.json` records the template hash, measured opening geometry, transform, alpha coverage, and staged compositor DDS hash.

The GFX audit found `21` unique sprite names and `21` unique texture paths in `interface/016_dhrondan_portraits.gfx`; every referenced runtime path exists and all twelve full plus nine role sprites match the manifest. No gameplay or country wiring was edited by this portrait worker, and no live HOI4 launch was performed.

## Changed files and reproducibility

Portrait-specific source and evidence are under `docs/assets/016_brilliant_scientist/dhrondan_portraits/`, including twelve native ImageGen sources, twelve processed full PNGs, nine compositor previews, nine placement/alignment/review sets, decoded DDS round trips, contact sheets, prompt lineage, process metadata, `portrait_manifest.json`, and `dds_validation.json`.

Runtime assets are twelve full DDS files under `gfx/leaders/DHR/` and nine role DDS files under `gfx/interface/ideas/016_dhrondan/`.

Portrait-specific wiring is `interface/016_dhrondan_portraits.gfx`.

This handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_portrait_package_handoff_2026-08-21.md`.

Re-run processing with `python -B docs/assets/016_brilliant_scientist/dhrondan_portraits/process_dhrondan_portraits.py`, then re-run DDS and contact-sheet validation with `python -B docs/assets/016_brilliant_scientist/dhrondan_portraits/validate_dhrondan_portraits.py`. Final DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; the source-to-runtime commands and exact file hashes are recorded in the JSON metadata and this handoff.

## Review state, simplifications, and blockers

No simplification, placeholder, grounded-source substitution, or unapproved fallback was used. Parent visual review is complete for all twelve full portraits and all nine role cards. User-owned in-game acceptance remains part of the overall package acceptance, but no portrait source-provenance or replacement review is required because the subjects are fictional native ImageGen creations.
