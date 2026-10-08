# Current inventory reconciliation, 8 October 2026

Disposition: implemented documentation integrity refresh, subject to parent review.
The parent authorized this refresh after the ALL20 freeze of 146 accepted Markdown candidates on 2026-10-08.
The user authorization and review boundary are recorded in [the pass brief](../brief.md).
The parent separately confirmed that Event 070 has a current checkout inventory despite its DELIVERY_MANIFEST filename and authorized the current inventory columns for Events 038 and 048.
No design acceptance, gameplay implementation status, balance target, source specification, shared registry, skill, navigation index, asset, workbook, catalog export, staging or commit was changed.

## Source-of-truth map

| Surface | Authority and disposition |
| --- | --- |
| Accepted candidate bytes | Parent-owned accepted_groups.json in the external task directory records 20 accepted groups, their exact acceptance bases and 146 before/after file hashes. The current accepted hashes were verified and remain unchanged. |
| Current inventories below | Implemented integrity refresh under the parent freeze instruction. Hashes and counts establish document identity, not approval or engine behavior. |
| Original archives, reading ledgers, briefs and dated QA records | Retained historical evidence. The 161 historical or unchanged ledger/receipt records checked against the task baseline remain byte-identical. |
| Event 098 mixed manifest | Only current_repository_inventory changed. The raw prefix containing the original delivery receipt is byte-identical. Original reading counts, files entries, dates and PASS/CLOSED results are unchanged. |
| Event 099 mixed inventory | Only current files-row fields and the root evidence-scope note changed. original_bytes, original_sha256, arithmetic and current_checks remain unchanged. The note identifies those check sections as original import-review evidence, not a rerun. |
| Event 025 mixed checksum ledger | Only the accepted specs/007_world_reactions_and_event_connections.md checksum and package_manifest.md checksum changed. The manifest current as-of date changed. Every unrelated pending checksum row remains byte-identical to the immediate before-copy. |
| Events 085 and 087 | Current files rows and inventory_updated changed. Original design_word_count/markdown_word_count, planning figures, checks and validation results remain historical delivery evidence as inventory_scope declares. |

## Exact changed files and byte identities

All 34 modified repository inventory files are listed below.
Every inventory was copied byte-for-byte into inventory_before before any repository write, with its SHA-256 recorded.
The matching inventory_after bytes and row/scalar changes are recorded in inventory_changes.json.

| File | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| [docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md) | `76849b0d3b8dcae52d7d06cdbfbfc71c68bb45c21a63f1a8740dfd788ae443dc` | `4a0cb184706d7cbb056ac36f07de01b48e7b415783d9a70ee671b02a792c1d0c` |
| [docs/specs/018_resources_found_specs/manifest.md](../../../../../docs/specs/018_resources_found_specs/manifest.md) | `a2d944146b63627c763fa5f1adb8e9e4c9cd9421f1a6df57a9714c65c450e9dc` | `0ca254304f3bd2c27b4f633d46e1b26140db6e040ac7378fa9dbb2c8f618ec46` |
| [docs/specs/025_alien_technology_in_antarctica_specs/package_manifest.md](../../../../../docs/specs/025_alien_technology_in_antarctica_specs/package_manifest.md) | `03c30cdb9d8195665d24a9844dd00d5aa5cab79761da253a3b945ad184526f5f` | `42d7d975edf942a0f3146928bba7e184be512f2c07994f80e5e7e2506d43594a` |
| [docs/specs/025_alien_technology_in_antarctica_specs/package_checksums.sha256](../../../../../docs/specs/025_alien_technology_in_antarctica_specs/package_checksums.sha256) | `9974a2553eed18d121642d1688402d6d766471f7b35ca17b7f438ca30aaa3f21` | `f4298fdfd49fbc0172b214997b681bc0addd7920efc9696dc4e7a203a2cdb663` |
| [docs/specs/030_time_traveler_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/030_time_traveler_specs/PACKAGE_MANIFEST.md) | `e5a067a8c7a9c62eeed58c7f0e0e70be2996d7baf0a8f10e48953f5fea11fdf0` | `7ca2aed1f420efa1c4431df95da71ba1a1fec737324c1eb2e847bf5c9d81ad32` |
| [docs/specs/031_random_terror_specs/031_random_terror_manifest.json](../../../../../docs/specs/031_random_terror_specs/031_random_terror_manifest.json) | `0ddaf7fb666ebf4c262fe87c7c7f18a6df301a729a0bf08112dc7fada7f8e287` | `5d6b1852b0f7d1fb25c85b26efed6cf6a0c358595e69aa619cae2097544d3d53` |
| [docs/specs/032_missiles_specs/032_missiles_package_manifest.md](../../../../../docs/specs/032_missiles_specs/032_missiles_package_manifest.md) | `d741bfa0b8e25135ad88385fbe7e974191d250c6abb66b4deb6143c28e9d30ea` | `6185fd5a96639433e694439a82a887acd155ccfc683eee40abb1291733068217` |
| [docs/specs/034_industrial_boom_specs/034_industrial_boom_package_manifest.md](../../../../../docs/specs/034_industrial_boom_specs/034_industrial_boom_package_manifest.md) | `a99338c8e02f5c3e7f5f79f29b33c5c70663f5fb47093c9a1af4c786f637cea8` | `564e6be2d21d236e385ae832476d5d9dd0a4847f30f8e3f984914a11497c9f83` |
| [docs/specs/035_great_depression_specs/035_great_depression_package_manifest.md](../../../../../docs/specs/035_great_depression_specs/035_great_depression_package_manifest.md) | `10a2924249dccf775116b4e237d57c60363e26ca28b9069408efa672b6e1f989` | `a7eb1e0fc554396c8221b368d4eb77d77ca282483ae05e45b4a2c73a50a6677a` |
| [docs/specs/036_chemical_and_biological_weapons_convention_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/036_chemical_and_biological_weapons_convention_specs/PACKAGE_MANIFEST.md) | `2f04db74a798a12865181ba74711f9d63abf1716b6003d80461e3eca835c1727` | `44bd46b56a829aae75d90cdb287d9695dbc55045e6f72f52a74a8a01e4edb685` |
| [docs/specs/037_mysterious_people_specs/quality/037_mysterious_people_package_manifest.md](../../../../../docs/specs/037_mysterious_people_specs/quality/037_mysterious_people_package_manifest.md) | `f41ee001a4add5cf70812bea24647e2e117b432230a1d6db59d3d3251ec947ef` | `61c46f4edaf5f5b6eb72b5f8bb40223f12776bfa1d706f8646d3685df5e7dff2` |
| [docs/specs/038_malta_crusaders_specs/validation/package_inventory.csv](../../../../../docs/specs/038_malta_crusaders_specs/validation/package_inventory.csv) | `361b59889c704db9ee9b3f545fcc12c55ed8be83a1dfc722405021f736f346ed` | `251376e9561e26e2aaa07d8ac50256ce78583b80af98e754bbfce5bb8202e714` |
| [docs/specs/041_disease_in_divisions_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/041_disease_in_divisions_specs/PACKAGE_MANIFEST.md) | `8209cfc64347f494b53c37f8207762e52051a5c1e1555e19b7208b60310f45e5` | `31b9d9994eacce10b8e876c26c517811a6f23ceeb660a96f507f50f097753982` |
| [docs/specs/048_old_great_bulgaria_specs/quality/package_file_manifest.csv](../../../../../docs/specs/048_old_great_bulgaria_specs/quality/package_file_manifest.csv) | `8fda3ae34fe187583ecc0d2517861a13c6bbbe78f1a52f01f66a5fabf4372044` | `22fbff9dc87033c6c88ed2a0bc2fb39a9307455bd7b53d1a853118950e8e76c1` |
| [docs/specs/049_doomsday_specs/quality/049_doomsday_package_manifest.md](../../../../../docs/specs/049_doomsday_specs/quality/049_doomsday_package_manifest.md) | `18a5f1159f5471f4397f406f7234bbcd734681d8031bc9272b5c8f7ada99111e` | `54f5f63cb8b360a6ef810d8f8afd43d89a1759162b4aebce283b19631af47302` |
| [docs/specs/050_the_great_embargo_specs/quality/050_package_manifest.md](../../../../../docs/specs/050_the_great_embargo_specs/quality/050_package_manifest.md) | `4da9d0649641f368bfbe5744642342e32a350a12e649f32bfb1f9b5ea1361415` | `5dbf816b1855cc9d3d508d7a41dda5c4003d67f4a89da6c49a035a66b1a85f9a` |
| [docs/specs/051_heat_wave_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/051_heat_wave_specs/PACKAGE_MANIFEST.md) | `c990cd1f72c7744aebf0d35143663112b78db1f820a6f6a003a562a270c54855` | `065038c2bcad4abbdc0662cce554086697c9d6bd299c72e32c5348dde0b64a86` |
| [docs/specs/052_intel_leaked_specs/manifest.md](../../../../../docs/specs/052_intel_leaked_specs/manifest.md) | `e80e5b2136686608d81776f183376199bccab547f0ec9a28db15a52db2b1014d` | `d319de0cf7e7e81731550a90115a950b5ce8a0b5c2cb02395908a8e8d406ffd0` |
| [docs/specs/058_random_buildings_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/058_random_buildings_specs/PACKAGE_MANIFEST.md) | `f03f53a13aff263a8a5616918ae3daa9b2d65d3827d8aac9143198aba708ebde` | `e0819ce2be35c93cd2e2733706750661a9319dbc56af262b378fac81c137f079` |
| [docs/specs/062_allies_backstab_specs/PACKAGE_MANIFEST.md](../../../../../docs/specs/062_allies_backstab_specs/PACKAGE_MANIFEST.md) | `34ecbcf0435755540659233a6a1df3b217dcbfb4e95aa995ddc3a7219e3e3306` | `394c3570316c704bef01536a404d707721e41d9a6dc669738d4d05d21cc02dc6` |
| [docs/specs/064_border_fortifications_specs/manifest.md](../../../../../docs/specs/064_border_fortifications_specs/manifest.md) | `911c72da0eb912e7f78b23536c5479405e70f16bdce385b9cb0f6beb31f9f33a` | `0d1ba686cd8bf317c797af981ddff458c25e5ea614685d5be37b13aa65c612a4` |
| [docs/specs/066_abundance_specs/MANIFEST.md](../../../../../docs/specs/066_abundance_specs/MANIFEST.md) | `502f27a8dc24a6c7976737cd92ac931bb8c1739f8853a38c77e654af582649e4` | `dc00e8ec2066fde7d0e8a74fc236b20ddb3182692412bb135e3b8c7ea1d5b2af` |
| [docs/specs/069_boxer_rebellion_specs/package_manifest.json](../../../../../docs/specs/069_boxer_rebellion_specs/package_manifest.json) | `a61b9163e77c098ff2b3bed272372916b0df62316bda96c22b333734542d8794` | `d2e446e6f493c88e4905e31137356e49fb45bc50f935e4cce71c94d8a291f5ae` |
| [docs/specs/070_cookie_click_specs/DELIVERY_MANIFEST.json](../../../../../docs/specs/070_cookie_click_specs/DELIVERY_MANIFEST.json) | `0727d912833d33599e2a79ac9959a32419f6ae08c7931bfe8cc7959967f6239e` | `89a3e9e4a328cc4f43d50857984f29099b1024a765e4fcfe0714e26040a7d669` |
| [docs/specs/071_persia_specs/071_persia_package_manifest.json](../../../../../docs/specs/071_persia_specs/071_persia_package_manifest.json) | `8adfb4863a54dc5a8e12d1bd5c83a7b1e0c8763fcd871d8ac68925feb7296b15` | `2838fb45692cbd7261900393dd8394eb9e23c2c8de4e5fe1ec9e6d2596e14139` |
| [docs/specs/072_ireland_reclaims_north_specs/PACKAGE_MANIFEST.json](../../../../../docs/specs/072_ireland_reclaims_north_specs/PACKAGE_MANIFEST.json) | `040c057c78af823b49d6d96da9b72dcda64be7938c227319984908b4233d61eb` | `59859abd2f6cb008e1efd9211f734656fd3d116d07b8cf5f546ed452401cf6ed` |
| [docs/specs/081_british_tax_specs/PACKAGE_MANIFEST.json](../../../../../docs/specs/081_british_tax_specs/PACKAGE_MANIFEST.json) | `66a016c52b5db6a57c81eb3fcf2e7e5dcf02be46046130da30bba1fa27bbf838` | `d2ec8518b5d56335c6af9533e14ba2f552b590d1023ef3097fefac750e74119c` |
| [docs/specs/084_the_peace_movement_specs/package_manifest.json](../../../../../docs/specs/084_the_peace_movement_specs/package_manifest.json) | `2970791b4f4434afa824b734251a7327c46c059b6c31c0047e39a62e9e022ae2` | `ea8c3c2dd893734b32b3e5d83010515609b4cb5a6cf074b10b643776debd1358` |
| [docs/specs/085_ten_plagues_of_egypt_specs/package_manifest.json](../../../../../docs/specs/085_ten_plagues_of_egypt_specs/package_manifest.json) | `2a0f748a31265b821102efff0902981350a6bb7e0c2b3afdd5d68e6608060c01` | `8a354b2daa405bd5c8b4a078e51505846c34760da88c17257276e71c71462941` |
| [docs/specs/087_military_madness_specs/087_military_madness_package_manifest.json](../../../../../docs/specs/087_military_madness_specs/087_military_madness_package_manifest.json) | `14c9230e0428e9af6bdc8f77ad886bcb2963d303ddcac5ac23c607b6a967d217` | `1b61c6069a82a59bc8021c06059dd5fea409170ff700641a0d25e3c40abd1e9b` |
| [docs/specs/093_treaty_of_tordesillas_restoration_specs/093_treaty_of_tordesillas_restoration_package_inventory.json](../../../../../docs/specs/093_treaty_of_tordesillas_restoration_specs/093_treaty_of_tordesillas_restoration_package_inventory.json) | `0140070848c4daa4e11122ac76dd224bc36e6f8fb3ae46e668a5d38477f79808` | `6e6f00c78199224f8a595c4e0e736e6b0106ef4ef153df966822a915b8526522` |
| [docs/specs/095_occupation_revolt_specs/095_occupation_revolt_package_manifest.json](../../../../../docs/specs/095_occupation_revolt_specs/095_occupation_revolt_package_manifest.json) | `74193a0202a385bf1be198816fae71d7cc2f46d8ec43a682bcc9e1c94649e7df` | `e3cb6a4f40a0cca1c4c77116e757d2b2a2fc603f0521c31143a7d91083a5bd6b` |
| [docs/specs/098_new_ore_specs/098_new_ore_package_manifest.json](../../../../../docs/specs/098_new_ore_specs/098_new_ore_package_manifest.json) | `458975829deb1620c0a00bae1afc25ffa9b35fde5919d4b3e9d957f5613cfe35` | `127d9ba6e9a8f63f94dd6dd3fc5784facbc0c15a69f225556e3d17a26513246e` |
| [docs/plans/099_sandstorm_plans/099_import_inventory_2026-10-08.json](../../../../../docs/plans/099_sandstorm_plans/099_import_inventory_2026-10-08.json) | `a2dba7d879e88c13d9da6691c572d2c215dc4ed9d885eab6fd09f02c8350feac` | `e00ff7fe91e680ecb82e3d00eb61e483aaf786da7a88612565b8e9474b8e5d8b` |

External review and isolation artifacts are under `C:\Users\klimp\AppData\Local\Temp\chaos-redux-specs-audit-20261008-qgzbgbrz`.

- `inventory_changes.json`: changed paths, before/after byte counts and SHA-256 values, raw copy paths, updated source rows and scalar edits.
- `inventory_before_sha256.json`, `inventory_before/` and `inventory_after/`: exact hashes and raw copies outside the repository.
- `inventory_reconciliation.patch`: reviewable delta relative to the immediate shared-checkout before-copies.
- `inventory_validation.json`: executed checks, including all 161 preserved record paths and hashes.

## Dispositions, retained evidence and open work

| Document group or issue | Disposition and basis |
| --- | --- |
| The 34 current inventories above | Implemented documentation refresh after parent acceptance/freeze. Current fields were refreshed for 50 source rows; membership and ordering are unchanged. |
| 070 DELIVERY_MANIFEST.json | Current files section confirmed by inventory_scope and parent authorization. Original date, purpose and historical source receipts are unchanged. |
| 038 validation/package_inventory.csv | Implemented current path/bytes/lines/words/sha256 row refresh. Current scope is established by validation/package_validation.md and the October 7 audit handoff. |
| 048 quality/package_file_manifest.csv | Implemented current path/bytes/sha256 row refresh. Current scope is stated in its README and October 7 audit handoff. |
| 011, 012, 020, 043–046, 057, 074, 090, 097, warfare and famine original package receipts | Left unchanged as historical provenance. Current-sounding filenames do not override their recorded historical receipt scopes. Source-reading and original delivery ledgers remain original evidence. |
| Existing package navigation/indexes | Left unchanged. Accepted edits retain original paths and introduce no package membership change; current inventory paths all resolve. |
| Existing plans, addenda, prior handoffs and native proof gates | Dispositions unchanged. This task neither chooses design alternatives nor executes implementation or engine checks. Parent acceptance is limited to the exact accepted candidate claims. |
| Event 091 | Excluded from import. No Event 091 file was read, installed or modified for this task. |

Resolved documentation contradictions: current-versus-original scope for Event 070 and the two package-local CSV inventories; Event 099 stored current_checks could imply a new run and now has an explicit import-review scope note.
No unresolved inventory ownership conflict remains.
No documentation was merged, superseded, deleted or duplicated.
No stale production prompt or historical instruction was executed.
No resume packet is needed for this bounded integrity task.

## Meaningful validation and limits

The final parent link-only correction in Event 031 changed the missile reference from `#site-capture` to the existing `#capture` heading.
The affected Event 031 current row and byte totals were refreshed against the updated accepted ledger; all original inventory_before snapshots were retained.

- Verified all 20 accepted groups and all 146 current accepted Markdown SHA-256 values before and after the integrity refresh.
- Verified existence of all 1,090 listed paths and actual SHA-256 plus applicable byte/line/word/character fields for 1,081 text rows; no path or field mismatch remains.
- Refreshed applicable current totals and Event 037's sorted concatenated-byte checksum using current listed files. No acceptance, scenario, tuning, source-reading or historical test figures were recalculated.
- Verified 161 historical or unchanged ledger/receipt records against the task baseline, including source-reading ledgers and original archive manifests.
- Confirmed Event 098's exact original raw-prefix preservation, Event 099 original metadata/check preservation, Event 025 unrelated row preservation, and Events 085/087 original figure preservation.
- Preserved table/list structure, original ordering, JSON formatting, BOM treatment and line endings. Events 014 and 030 retain their declared LF-count-plus-one convention; other physical-line inventories retain their established convention.
- No accidental Markdown hard wrap was introduced. Canonical prose was not reformatted. The handoff uses one sentence per physical prose line and deliberate table/list structure.

Nine binary inventory rows were retained and their paths checked, but their bytes were not inspected under the assigned scope.
Gameplay, weighted logic, GUI, focus, event, technology, map, asset, engine, workbook and original import arithmetic checks were not rerun because this task changes documentation integrity fields only.
No MCP service health or standalone viewer availability claim is made.
Existing historical results remain limited to their own dates and scopes.

The parent must review the exact inventory delta against the immediate before-copies and isolate the two changed Event 025 checksum rows from pre-existing pending edits when committing.
There is no implementation simplification in this integrity refresh; binary validation and gameplay completion remain outside this task.
Skill used: [chaos-redux-subagents](../../../../../.agents/skills/chaos-redux-subagents/SKILL.md).
