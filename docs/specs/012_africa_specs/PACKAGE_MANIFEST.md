# Event 12 Africa expanded package manifest

> Manifest provenance notice, 2026-08-10: this manifest is the frozen 2026-07-10 specification-package inventory and its byte counts and hashes are not the current runtime ledger. Use `docs/events/012_africa/overview.md`, the authoritative asset matrix, and `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` for reconciled implementation status. The manifest remains a design-package integrity record and has not been silently regenerated during this documentation-only pass.

> Current reconciliation pointer, 2026-08-11: the source-completion certification records 44/44 achievements, 64/64 AI profiles, 102/102 actions with six deliberate runtime gates, 16 implemented conditional priority packages, 16 matching implemented polity rows, 199 queued controlled-pool candidates, and 239 visual dispositions. See `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_current_source_certification_2026-08-11.md` and `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_documentation_reconcile_2026-08-11.md` for current evidence boundaries.

## Package identity

- Event ID: `12`
- Event slug: `africa`
- Edition: expanded second edition
- Package date: `2026-07-10`
- Deliverable type: planning and specification package
- Gameplay implementation included: no

## Coverage counts

- `012_africa_host_country_playbook_matrix.csv`: 51 data rows
- `012_africa_focus_route_payoff_matrix.csv`: 78 data rows
- `012_africa_priority_member_package_matrix.csv`: 16 data rows
- `012_africa_polity_catalog.csv`: 215 data rows
- `012_africa_decision_mission_matrix.csv`: 102 data rows
- `012_africa_achievement_matrix.csv`: 44 data rows
- `012_africa_ai_route_matrix.csv`: 64 data rows
- `012_africa_asset_animation_matrix.csv`: 239 data rows
- specification parts: 9
- diagrams: 5
- research notes: 3
- bounded prompts: 6
- goal prompt character count: 3,998

## Validation recorded

- all eight CSV matrices parse successfully
- every CSV cell is populated
- primary keys are unique in seven matrices
- the focus route matrix has unique `route` plus `focus_group` pairs
- package-relative Markdown references resolve to existing files
- the goal prompt remains within the required 3,500 to 4,000 character range
- no em dash or semicolon character remains in package prose
- the original source-reading record and revision review are included

## Inventory

The manifest excludes its own hash. Paths are relative to `012_africa_specs/`.

| Path | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `README.md` | 7,644 | 130 | `c1d7c2dce640d4362f24dc595332acd1de3004574e810622a0a97282bfb18ab0` |
| `diagrams/012_africa_evolution_and_world_order_state_machine.md` | 3,051 | 56 | `a18437c3f03b29106f770bfb55500962b76ea1960cfe3437471a53071e55f7e6` |
| `diagrams/012_africa_focus_route_interaction_map.md` | 3,070 | 134 | `5872a6660cf07aaaed4576a3cf3dffb6493d987043748bdbce568d9119c67e3e` |
| `diagrams/012_africa_host_overlay_selection_flow.md` | 2,608 | 68 | `664f1901f6a10ebbd510ecc98f7031464241f9e0b43fe07eacc9503c43836612` |
| `diagrams/012_africa_member_relationship_state_machine.md` | 2,960 | 63 | `b9cbe46cdc09f991a42b9c083e557f12f63bced34cba53b3b9f2829c34d8a0bb` |
| `diagrams/012_africa_system_architecture.md` | 2,804 | 77 | `8b2e104b17c2c6c5a05ec491508bb5929caf3626e811a34de04eabadbc572af4` |
| `handoffs/012_africa_expansion_revision_and_anti_bloat_review.md` | 7,243 | 133 | `48f6cd09c498be6c1727537ffb6c34acb889b763f03a8f02bdb125147cbaade8` |
| `handoffs/012_africa_implementation_acceptance_and_catalog_reconciliation.md` | 10,662 | 201 | `0afd629a1a2eb9c57a9ec726181494aa855154101f3a31c33b8348e7715ae353` |
| `handoffs/012_africa_improvement_loop_closure_review.md` | 5,359 | 89 | `86afd66960d5081ca84334da6fe30e36e4993dca357e11325a4f6b9def889984` |
| `handoffs/012_africa_source_of_truth_and_reading_record.md` | 8,143 | 90 | `89585f44f0403bf57ab243e5f3cd30cc79c348a2f002f63ad739ac8cb4a58cce` |
| `matrices/012_africa_achievement_matrix.csv` | 25,844 | 45 | `1448c2cdb4364ab57390aacc7cbf63c9580c0a11c92d45ba9f289ff246facb6a` |
| `matrices/012_africa_achievement_matrix_notes.md` | 4,659 | 74 | `0391d9678c15eeadc466321769e246ceba2cf7f1c9d434d3fa3b3c24953ff508` |
| `matrices/012_africa_ai_route_matrix.csv` | 51,968 | 65 | `9c4dbdeeadf4fab5c58db965d172db8c9259f4edb49e09c80f0fcaccfc5926e0` |
| `matrices/012_africa_ai_route_matrix_notes.md` | 6,348 | 118 | `1c433796bcf30025d07507ecc61026ae446468b582031b0fa0897de2c7db8742` |
| `matrices/012_africa_asset_animation_matrix.csv` | 160,659 | 240 | `be4d1f293339d1c324e93cd6fe669e31db6a1eba9a34fb8dd3445aac580ef417` |
| `matrices/012_africa_asset_animation_matrix_notes.md` | 6,672 | 136 | `81031c3acd528f36c921bdf36cef792eab672076ea02995d4eb988722018d719` |
| `matrices/012_africa_decision_mission_matrix.csv` | 61,162 | 103 | `f0415263e8cab0a1e5f3737f20f8796c729309b6bc74e973439b3bf19b14cf72` |
| `matrices/012_africa_decision_mission_matrix_notes.md` | 7,869 | 120 | `279eb3b409ee1e5239358de3599660123e4a0ad8c9aa653998807971d922cf78` |
| `matrices/012_africa_focus_route_payoff_matrix.csv` | 39,200 | 79 | `71efd06ac497c1b539ff463af345b72847c1e5d5a639a2b0a4fad9c868b43090` |
| `matrices/012_africa_focus_route_payoff_matrix_notes.md` | 1,856 | 42 | `93055f5afd4c7d3e923b34506e3a32edea594d665de5503ada9ba5c0917c7082` |
| `matrices/012_africa_host_country_playbook_matrix.csv` | 37,396 | 52 | `7a35aab6895b4ab7ed755b202816d3ca2f9d17de2741eadf1a97f8efe0d33d62` |
| `matrices/012_africa_host_country_playbook_matrix_notes.md` | 1,827 | 28 | `623a299339f09437e17b34e5662dde45d9f48edee2a55bcc4ad82e5b156b623c` |
| `matrices/012_africa_polity_catalog.csv` | 49,310 | 216 | `0bae6b3777635db38b4a9728f7817e31c99f7139e9d93b3c81aaee941602f77d` |
| `matrices/012_africa_polity_catalog_notes.md` | 6,303 | 215 | `a8894fa18ad41c609b301a96f0b89039d4b7a611024d5821a00953d610883dac` |
| `matrices/012_africa_priority_member_package_matrix.csv` | 16,959 | 17 | `6074e8aca4000ea9f92c1080c27502105eae4422fd819ecc01ca6f6bfc07e20a` |
| `matrices/012_africa_priority_member_package_matrix_notes.md` | 1,854 | 32 | `a9f8671e36142412bd5be245f7365ac65c04583e30ce63f76349464cceaeb3e7` |
| `prompts/africa_achievement_prompt.md` | 4,717 | 64 | `6c09e6341a583d0e58fae49c6b30b8ae7f46ef86dd3da8c12a2e055a37fcb29b` |
| `prompts/africa_asset_prompt.md` | 7,469 | 134 | `ed53fd78e05e2c08df55d02eba38a2c83e5f7fd82f35d1563f8f73ba82d3e894` |
| `prompts/africa_coding_agent_prompt.md` | 6,004 | 64 | `7a494f24beda2bc1c83da19a02b9a5a26fa36b448b8104e26d52cca7102a5b70` |
| `prompts/africa_decision_mission_prompt.md` | 5,257 | 99 | `5269a7f568f27e0f98db450a37e2c72bb63598e98dc0ca117f49cd84a6063639` |
| `prompts/africa_goal_prompt.md` | 3,998 | 25 | `fe5b6cbc47494aac9bf69e03a53856111cdf2667b6397228b601f2664f03584a` |
| `prompts/africa_super_event_prompt.md` | 6,417 | 105 | `9daa8a8a4eabbc12a0894aac5c4a324ca741a0d3e94542d8832a3b8e30485bb5` |
| `research/012_africa_historical_research_and_bibliography.md` | 17,975 | 406 | `ef99cda60ff76ff0e3dc2a744c5db927e99b97c73cae81acf02483643b9ba564` |
| `research/012_africa_host_country_research_addendum.md` | 20,889 | 340 | `917078f0fea29b2f36018ed566a36c0d79c7249f259e503a5bc3a600149e48e5` |
| `research/012_africa_language_names_and_sensitivity_protocol.md` | 7,458 | 220 | `a252dd21f3a921e0ab915b338e5b83752f3a382680e89cfe59e023042c384f13` |
| `specs/012_africa_spec_part_1_core_progression.md` | 31,612 | 532 | `8c293e8351cdfe2b40cdf19b990fc66f692078215bff591e77d1cd5202047523` |
| `specs/012_africa_spec_part_2_charter_league_integration.md` | 30,885 | 817 | `a25078ff69c8e708cb4849083c097b84ec1f52c812897c4ad748f357d74f32db` |
| `specs/012_africa_spec_part_3_focus_tree_architecture.md` | 37,391 | 977 | `444a91fdfc8873bd87d7cf5020825eed71d7f9d47d43db6ed7d28905b8f8d245` |
| `specs/012_africa_spec_part_4_country_packages_formables.md` | 34,608 | 897 | `f2ac337a235b967898661cd0a98091330144790959785061a3da84e2f0664606` |
| `specs/012_africa_spec_part_5_high_chaos_world_order.md` | 28,790 | 823 | `7d989e184db2e0dc6be8b021c3f651b9a9c9e772dab2a238e3c423801829b626` |
| `specs/012_africa_spec_part_6_presentation_achievements_assets.md` | 26,848 | 802 | `20b2c04844ff01bfc6785daca91b661d14f71e2f4d994e0348a73e538df9bba8` |
| `specs/012_africa_spec_part_7_host_country_playbooks.md` | 102,235 | 1,176 | `5aaeaa13cdf311bff7a08f0fe87c1751594d4af7c8173f3305692298ded7b00d` |
| `specs/012_africa_spec_part_8_focus_route_deepening.md` | 58,862 | 1,166 | `86a57c1a4e2f547d0539309cff94bc4dfb154c223e329ed706884ce0ebca9fd1` |
| `specs/012_africa_spec_part_9_priority_member_country_packages.md` | 46,071 | 783 | `c6be5db0a7fd84b8564f0267dd2905c432213a17c91afa73f86f3e15708d877a` |

## Integrity note

The external ZIP hash is written beside the final archive. Rebuild the manifest after any file changes and rebuild the archive after any manifest change.
