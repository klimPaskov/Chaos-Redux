# Event 037 specification package manifest

## Package identity

| Field | Value |
| --- | --- |
| Event | `037 Mysterious People` |
| Intended repository path | `docs/specs/037_mysterious_people_specs/` |
| Package filename | `037_mysterious_people_specs.zip` |
| Files listed below | `23` |
| Listed source bytes | `204,764` |
| Aggregate ordered-content digest | `99cb3a1ec4912c88aedd94325ad8deb104441823398d84c8c82e25b62005f355` |

This manifest excludes its own file from the checksum table so that the recorded hashes remain stable.

## File inventory

| Relative path | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `README.md` | 5,182 | 67 | `e117f8bc8734d1f047b9b643306859ff5f6dbc5e3c7db2fb776ea8ba3966b083` |
| `diagrams/037_mysterious_people_system_flow.md` | 3,702 | 107 | `9eb0756df47691d8a335090bf4f00875b36266390ec2c65c3ec06281ad828796` |
| `handoffs/037_mysterious_people_catalog_and_cluster_alignment.md` | 3,958 | 108 | `2ca5dcd10748e40ddce165f604b0ac4f944a56cf6b1881daf07012b500ee78bd` |
| `handoffs/037_mysterious_people_subagent_routing.md` | 4,983 | 143 | `71558a9ce9f6f2925c3b8a42d74a29f8fe54e1198d6b512a198fd43061437811` |
| `prompts/037_mysterious_people_achievement_prompt.md` | 4,666 | 101 | `40b62b25b0911e3fe85029e8ff670222a5ce89863d5dd2bb281207c5935e00e6` |
| `prompts/037_mysterious_people_asset_prompt.md` | 6,028 | 155 | `e0cc7b75c606721eb704318593d7c62f1afbb67bc7149c0151b22b98534c2482` |
| `prompts/037_mysterious_people_coding_prompt.md` | 7,940 | 132 | `476ef8b001d88156739d2112915185da28c8fbf62c9a52facc6799488eebd143` |
| `prompts/037_mysterious_people_decision_mission_prompt.md` | 5,532 | 146 | `b9e7e3ce1c3b193fdfc94ed28169fbd7ad6d4e8e38050980034a32fc19851cef` |
| `prompts/037_mysterious_people_goal_prompt.md` | 4,000 | 27 | `324d2538c59a4fbdbea9b13a31a2d5eaad01ef54837597743467a9973ace68fd` |
| `prompts/037_mysterious_people_population_ledger_and_adapters_prompt.md` | 5,142 | 88 | `e4df7020cb7801fa0255977c01fb06f19a1f90d794fdfd9246b37e9775c99487` |
| `quality/037_mysterious_people_acceptance_criteria.md` | 15,670 | 298 | `b45df01fe57b813af67f40d0dc89d44945cf500d435a85491f49240bf11ace29` |
| `quality/037_mysterious_people_balance_matrix.md` | 10,681 | 269 | `8a9faeba513343bd063d08465255e57e0f915bd31c51af87358c201837a47d2a` |
| `quality/037_mysterious_people_parent_improvement_review.md` | 6,074 | 130 | `a9f3ab13aac8ebf9876be72ce27d0817fc9b76ad7486e60f4e18c07e4702c047` |
| `quality/037_mysterious_people_probability_scenarios.md` | 11,092 | 165 | `8c606ca7b0a9b4888e469f7b439ef7618a9ee9ee5e490e1f45f11af9cf678ba3` |
| `quality/037_mysterious_people_source_reading_manifest.md` | 6,337 | 93 | `829009647f9ee1b23a0aa8d0c690cc8e1e16699c1bd87a7d49e076a77488b1e2` |
| `research/037_mysterious_people_research_boundary.md` | 1,893 | 41 | `8a6103393f336da01193e454fd047eda7741413ad7725367e777a2c38675c83b` |
| `specs/037_mysterious_people_spec_part_1_core.md` | 14,229 | 219 | `a69674b251158f08e21a9caebe6dfea1399b69022030070004a037a99611eb14` |
| `specs/037_mysterious_people_spec_part_2_population_and_ledger.md` | 14,952 | 298 | `85b902758a0b3718739c81005d35fa93f6c319b970b9469e5cd501cbdc506eac` |
| `specs/037_mysterious_people_spec_part_3_pressure_and_evolutions.md` | 13,850 | 262 | `552d1e5261b2fffd031805470812904e7dd4d22e8db37db15741212ae35800d1` |
| `specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md` | 16,489 | 457 | `95c629fd64480a361b981b3da9d96c35c04504d9c6c57762b7265e63617c8627` |
| `specs/037_mysterious_people_spec_part_5_events_flavour_and_reactions.md` | 21,242 | 724 | `fc8b9ec8f34cd1cc682c00f844d66c86fabd6b4acc7c72db9eec4ee898a437c9` |
| `specs/037_mysterious_people_spec_part_6_system_connections.md` | 10,525 | 199 | `3360121524f0cb7de60fab911cffdc7b6d4d82d0136d4a8e328dd2f18f712275` |
| `specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md` | 10,597 | 243 | `dbb1ce6730cffc944b7d42230bcef469a5af09061f4a470f1b198ad50c6e2f22` |

## Package checks

- Every required sequential spec part is present.
- Asset, achievement, decision and mission, population-ledger, coding, and goal prompts are present.
- The goal prompt is exactly `4,000` characters including its final newline.
- No temporary continuation prompt is present.
- No generated Markdown file contains an em dash or semicolon.
- The ZIP is built with the repository path prefix `docs/specs/037_mysterious_people_specs/`.
- The source-reading manifest records every uploaded file and every subagent archive member.
