# Package Manifest

> Documentation reconciliation, 2026-08-02: this manifest retains the original planning-package inventory and integrity snapshot. The current static runtime facts below supersede the former blanket "not implemented in this environment" line; the integrity table is historical until the package is regenerated. See `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-02_event20_documentation_reconciliation_handoff.md` for the evidence and remaining blockers.

## Package summary

- Event: 20 Black Plague
- Source specification folder: `docs/specs/020_black_plague_specs/`
- Files excluding this manifest: **44**
- Total words excluding this manifest: **67,242**
- Total bytes excluding this manifest: **440,452**
- Goal prompt length: **3,998 characters before its final newline**
- Planning status: revised complete design handoff with current static-runtime reconciliation
- Incorporated corrections: instant triggerable scenario, Black Plague-specific decisions inside the shared disease category, and black mapmode fill for established Black Plague states
- Runtime identity: exactly two Rat tags, reusable `RTA` and separate `RTX`; no additional Rat country tags are permitted
- Focus surfaces: 52 RTA focus nodes and 71 RTX focus nodes are the current documented runtime counts, confirmed by the source files and the 2026-08-05 national focus inspections
- Native last-response missions: `Hold the Line` and `Secure the Refuge` use native `activate_mission` and `days_mission_timeout` declarations
- Promoted visual/audio evidence: the dedicated weapon-delivery icon, source-frame Rat King portrait, source-frame Royal Burrows seal, Severe/Collapsed crisis seal pair, Rat King terminal-readiness seal pair, and three 44.1 kHz Event 020 WAVs are wired or registered in their owning runtime surfaces
- Model boundary: one shared rat ground-unit model/entity package is promoted for the six locked RTA/RTX unit consumers, with no per-subtype or separate Rat King model; sound-definition wiring, counter review, and live consumer validation remain open
- In-game validation: not run in this documentation pass; live playback, scenario, mission, balance, and release-attribution checks remain parent/user-owned

## Contents

### root

- `README.md`: 343 words, 2,847 bytes, package overview, correction summary, and reading order

### focus_graphs

- `focus_graphs/crisis_board_state_flow.md`: 127 words, 1,049 bytes, disease state and response flow diagram
- `focus_graphs/rat_brood_tree_architecture.md`: 257 words, 1,662 bytes, base Rat Nation focus architecture diagram
- `focus_graphs/rat_king_tree_architecture.md`: 320 words, 2,149 bytes, Rat King focus architecture diagram

### matrices

- `matrices/achievement_matrix.md`: 972 words, 6,308 bytes
- `matrices/ai_strategy_matrix.md`: 1,524 words, 9,121 bytes
- `matrices/asset_inventory.md`: 2,036 words, 11,986 bytes
- `matrices/catalog_update_draft.md`: 627 words, 3,727 bytes
- `matrices/country_package_matrix.md`: 1,138 words, 7,260 bytes
- `matrices/decision_mission_matrix.md`: 2,579 words, 15,657 bytes
- `matrices/disease_state_matrix.md`: 770 words, 4,824 bytes
- `matrices/event_chain_map.md`: 916 words, 5,438 bytes
- `matrices/evolution_matrix.md`: 741 words, 4,225 bytes
- `matrices/focus_tree_route_architecture.md`: 823 words, 5,062 bytes
- `matrices/implementation_acceptance_checklist.md`: 1,285 words, 7,442 bytes
- `matrices/state_selection_and_spread_model.md`: 1,061 words, 6,598 bytes
- `matrices/triggerable_scenario_matrix.md`: 1,169 words, 6,355 bytes, scenario registration, intensity, bootstrap, and validation matrix
- `matrices/tuning_and_balance_targets.md`: 1,538 words, 8,839 bytes

### prompts

- `prompts/black_plague_achievement_prompt.md`: 531 words, 3,639 bytes
- `prompts/black_plague_asset_prompt.md`: 1,792 words, 12,106 bytes
- `prompts/black_plague_coding_prompt.md`: 1,854 words, 13,647 bytes
- `prompts/black_plague_decision_mission_prompt.md`: 970 words, 6,861 bytes
- `prompts/black_plague_goal_prompt.md`: 557 words, 3,999 bytes, compact implementation goal prompt within the required character range
- `prompts/black_plague_super_event_prompt.md`: 770 words, 5,242 bytes

### research

- `research/bibliography.md`: 302 words, 3,003 bytes
- `research/plague_history_and_science_notes.md`: 1,160 words, 8,894 bytes
- `research/rat_king_folklore_notes.md`: 394 words, 2,520 bytes
- `research/source_read_ledger.md`: 834 words, 6,890 bytes, complete supplied-source read ledger and disclosure
- `research/super_event_text_and_audio_research.md`: 740 words, 5,057 bytes

### review

- `review/completion_audit.md`: 1,355 words, 8,151 bytes, requirement-by-requirement design completion audit
- `review/improvement_loop_review.md`: 679 words, 4,957 bytes
- `review/limitations_and_blockers.md`: 608 words, 4,155 bytes
- `review/manual_role_reviews.md`: 929 words, 6,576 bytes
- `review/package_validation.md`: 391 words, 2,713 bytes, final artifact validation record
- `review/source_of_truth_and_plan_disposition.md`: 494 words, 3,130 bytes

### specs

- `specs/020_black_plague_spec_part_1_core_crisis.md`: 3,471 words, 22,893 bytes
- `specs/020_black_plague_spec_part_2_crisis_board_and_containment.md`: 4,505 words, 30,703 bytes
- `specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md`: 3,941 words, 26,552 bytes
- `specs/020_black_plague_spec_part_4_evolutions_and_rat_emergence.md`: 3,392 words, 21,693 bytes
- `specs/020_black_plague_spec_part_5_rat_nations.md`: 4,562 words, 29,680 bytes
- `specs/020_black_plague_spec_part_6_rat_king.md`: 3,904 words, 25,825 bytes
- `specs/020_black_plague_spec_part_7_world_end_and_aftermath.md`: 3,109 words, 20,321 bytes
- `specs/020_black_plague_spec_part_8_ai_balance_assets_and_acceptance.md`: 3,639 words, 24,300 bytes
- `specs/020_black_plague_spec_part_9_triggerable_scenario.md`: 4,133 words, 26,396 bytes, instant multi-continent disease, Rat Nation, and Rat King scenario design

## Integrity table

| File | Bytes | Words | Lines | SHA-256 |
| --- | ---: | ---: | ---: | --- |
| `README.md` | 2,847 | 343 | 45 | `aa3fea88bf1013260dd801a2d18300e9e7b8fb40079b1bbd6561ea4290411562` |
| `focus_graphs/crisis_board_state_flow.md` | 1,049 | 127 | 27 | `4521833ef10c3671b6769a2ae4819ad1de916423ac53ef0109a29f21507dc733` |
| `focus_graphs/rat_brood_tree_architecture.md` | 1,662 | 257 | 67 | `55096750451241433bbc49bb8a1c6105bc7213efa1bce5d3a8cb6e4eeb44aaa5` |
| `focus_graphs/rat_king_tree_architecture.md` | 2,149 | 320 | 77 | `3145cf5ae242d82d14cf0f6dd3600c5efa1320e994995fe4dd80787b6dc5f0cd` |
| `matrices/achievement_matrix.md` | 6,308 | 972 | 33 | `bc16bef2e0f8b71d1403d6930d07d42a70085cccf58fa87e3c332448351e194e` |
| `matrices/ai_strategy_matrix.md` | 9,121 | 1,524 | 134 | `041fee44b953f6e492f429cac7f630d694f03232d6fa1a212f483bdf59eac11d` |
| `matrices/asset_inventory.md` | 11,986 | 2,036 | 239 | `fb10098bb172e40a4a33b99e23ec3472fba93214f43d3efe1932560bf600d72a` |
| `matrices/catalog_update_draft.md` | 3,727 | 627 | 50 | `b7c240da97a71aa1cc36c7947fec02f083bd7af27d4e6a5e29069b26893951ae` |
| `matrices/country_package_matrix.md` | 7,260 | 1,138 | 87 | `5a3ed33b2caf467265b6d59307f7449d0b6adf7153b02a1b3d3978a470e5021d` |
| `matrices/decision_mission_matrix.md` | 15,657 | 2,579 | 134 | `3e3e1bb34b88e933b040870542bcc7a3ec790ee87090b7c4a1be9996c36a868c` |
| `matrices/disease_state_matrix.md` | 4,824 | 770 | 42 | `297473b25fda6c4d0e01dab02499bec39ec90ad44cd5edd01624cb9bbd0ffc47` |
| `matrices/event_chain_map.md` | 5,438 | 916 | 83 | `125249c308851276866965e284022e2c8d2cfae68c87eb299cb940c3b40d7cf6` |
| `matrices/evolution_matrix.md` | 4,225 | 741 | 38 | `11e1299fe1aa63ca9af907e1456d908dce0369b2356d4e29757caf1372b65af4` |
| `matrices/focus_tree_route_architecture.md` | 5,062 | 823 | 61 | `eccd0b756bcd7d105efc315096ec1d15cc3757c0ea07d5d7a2dc21811f14528d` |
| `matrices/implementation_acceptance_checklist.md` | 7,442 | 1,285 | 152 | `e5bfc9cb46ce783c1d2e1e9858e67db8aa2f5c9cbcf7d1b2d4fb19428474f246` |
| `matrices/state_selection_and_spread_model.md` | 6,598 | 1,061 | 100 | `7b31cd9825b7f57b30a33e0472a92a106e288fa8ebbe2f2e5a7656f69de27482` |
| `matrices/triggerable_scenario_matrix.md` | 6,355 | 1,169 | 99 | `b851f7481c9db17077ee5ec660cb5aa31b13627f72e7f4bcc4c2834f879be7b7` |
| `matrices/tuning_and_balance_targets.md` | 8,839 | 1,538 | 160 | `db2442a47cbc5cbea51db63e5714356b1d2820dca65d11016d2d429a0b981576` |
| `prompts/black_plague_achievement_prompt.md` | 3,639 | 531 | 81 | `22baa4d754af07617173d48e1aa57dc856d6e8785d911967592aef0095c6fa8e` |
| `prompts/black_plague_asset_prompt.md` | 12,106 | 1,792 | 347 | `51e0428c57a4e7efd58159b84ffcdb571f995f2563c747f36b4192191324601f` |
| `prompts/black_plague_coding_prompt.md` | 13,647 | 1,854 | 147 | `81d14afac90895ee975a0ccc304208bf86e844b4cce463736e73b3e756b778be` |
| `prompts/black_plague_decision_mission_prompt.md` | 6,861 | 970 | 131 | `87943f8ee425654de593a552442827a0312f0fcba79087e8545d1887dc8193f5` |
| `prompts/black_plague_goal_prompt.md` | 3,999 | 557 | 19 | `02e74a4292aae350f99154c007c98b4c19ea3a8f6548201a52f9f5e73143e153` |
| `prompts/black_plague_super_event_prompt.md` | 5,242 | 770 | 96 | `3197bfad157519a9f8337afdf631cb0f7ce0c46bae3ab37f95b8526f649a0984` |
| `research/bibliography.md` | 3,003 | 302 | 41 | `ba912d3541827e6bd71c84435f3834f55620b7017bca1903dae23ec228fb284e` |
| `research/plague_history_and_science_notes.md` | 8,894 | 1,160 | 164 | `f42813cc8e79c03b375d2bbd79849b946a613c931c93efc42f6c4cffa9c25cfb` |
| `research/rat_king_folklore_notes.md` | 2,520 | 394 | 49 | `cb6a33941669d4fb599d896cb1a02f407778a5d5df0bf1416b52662f5f3f86fa` |
| `research/source_read_ledger.md` | 6,890 | 834 | 58 | `89a0e27ab48579669526fb75a5131b91e6418e479d2e20572d9192c7eb8cd6af` |
| `research/super_event_text_and_audio_research.md` | 5,057 | 740 | 111 | `83249ee51fa61f2414b69d36694f6b36fd55ebcd1271bdce69b4bb14eb2d167f` |
| `review/completion_audit.md` | 8,151 | 1,355 | 120 | `92fe73c8a3a79a18c9574e41735f129feb1496ee4d4ff776aef99dbab5a0a01f` |
| `review/improvement_loop_review.md` | 4,957 | 679 | 86 | `b7be46fc97c332e85275f2cd08bce0f539dfa754d61ee9a73e278ba22b911d61` |
| `review/limitations_and_blockers.md` | 4,155 | 608 | 63 | `24259710eea871a9e730e772931f899a03fe00c733ec176fae5ad4bde3f0e255` |
| `review/manual_role_reviews.md` | 6,576 | 929 | 135 | `1202534c19f77c373096caed8406dbdcc72473aad43c3654d02ef53ddd2716ef` |
| `review/package_validation.md` | 2,713 | 391 | 44 | `ce9a60dc3f92da610d97b706cc376999fec3222f437511a03221917c18d9fdcc` |
| `review/source_of_truth_and_plan_disposition.md` | 3,130 | 494 | 47 | `97c71d3cce33c79721bbcfcec1fcb3204fe27840048dd766606c90714f7f4803` |
| `specs/020_black_plague_spec_part_1_core_crisis.md` | 22,893 | 3,471 | 315 | `9c39200fcf72a164d0c713d1bf7bccaff4e9a58c2c1bae0636fe195c958e9606` |
| `specs/020_black_plague_spec_part_2_crisis_board_and_containment.md` | 30,703 | 4,505 | 818 | `9b2152a67ff55def6b05f5065b2ac40b98c59fbc3e87105f2e3669ea9ddf0ed6` |
| `specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md` | 26,552 | 3,941 | 589 | `7be9371ecddae47710afb61ddef08273efced5a300da3ec04ca629397caab290` |
| `specs/020_black_plague_spec_part_4_evolutions_and_rat_emergence.md` | 21,693 | 3,392 | 496 | `079bbedb44b28481bcbdf9f00c586f9876f5062693911b0dd0387451dbc0c599` |
| `specs/020_black_plague_spec_part_5_rat_nations.md` | 29,680 | 4,562 | 831 | `4b1d0ebb1e72a63b3861185672812882aa78daba3220db5dc6da641a8cd1897b` |
| `specs/020_black_plague_spec_part_6_rat_king.md` | 25,825 | 3,904 | 803 | `c95f54be57efee1e9129e1d8e723c187260d6168374cb42f3438128a81063895` |
| `specs/020_black_plague_spec_part_7_world_end_and_aftermath.md` | 20,321 | 3,109 | 547 | `0d0b58f323913e79833cc06c101b1a618d045cc0c52e245bf397a490b9b5fd26` |
| `specs/020_black_plague_spec_part_8_ai_balance_assets_and_acceptance.md` | 24,300 | 3,639 | 808 | `5d0515ae6385caa44550e052a800ef2e87aec9955a396c4f522e318446f5178d` |
| `specs/020_black_plague_spec_part_9_triggerable_scenario.md` | 26,396 | 4,133 | 485 | `711d7c97de91684d775a21e6b7534d0a132f375700ae38b244a704136f6016d1` |
