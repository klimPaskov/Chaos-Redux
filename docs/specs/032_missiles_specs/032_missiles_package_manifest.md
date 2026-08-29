# Event 32 package manifest

## Package identity

- Event: `32`, Missiles
- Intended repository folder: `docs/specs/032_missiles_specs/`
- Package date: `2026-08-19`
- Markdown files excluding this manifest: `22`
- Total characters excluding this manifest: `291334`
- Total words excluding this manifest: `43466`
- Goal prompt characters: `3881`

## Source disclosure

All uploaded project Markdown files, all three uploaded catalog CSVs, `config.toml`, and all 20 TOML definitions extracted from `subagents.zip` were read in full before the design was finalized.

The connected Chaos Redux repository was inspected for the current Event 32 script, its localisation, the Event 16 reaction bridge, Event 23, Event 76, the raid documentation, and the scenario registry state.

The current chat runtime did not expose the project subagent runner, HOI4 MCP server, installed Windows vanilla game directory, or installed vanilla documentation directory. No independent subagent run, MCP graph proof, exact installed technology audit, or live-game test is claimed. These implementation gates are preserved in the coding prompt, acceptance criteria, and test matrix.

## Scope and completeness

No intentional design simplification or content truncation was used.

The following surfaces are absent by design and are not omissions:

- event-owned country packages
- focus trees
- portraits or flags
- dedicated scripted GUI
- frame-sheet animation
- custom 3D models
- super-events
- event-owned world-end branch

The improvement-loop closure explains why those additions would add maintenance cost without improving the accepted Event 32 play loop.

## Validation summary

The package passed these planning-artifact checks:

- every file listed in `README.md` exists
- every supplied baseline and evolution requirement has a traceability mapping
- the goal prompt is between 3500 and 4000 characters
- no Markdown code fence is left open
- every Markdown file ends with a newline
- no em dash or semicolon appears in package prose
- prohibited response templates and contrast phrases were not found
- no unfinished task marker or unresolved placeholder remains
- the package does not claim implementation or live testing

## File hashes

SHA-256 values cover the exact files placed in this package before ZIP creation. This manifest excludes its own hash.

| File | Bytes | Characters | SHA-256 |
| --- | ---: | ---: | --- |
| `032_missiles_acceptance_criteria.md` | 18711 | 18711 | `62db29dc7e33a32c95ac25e2c72d0dfa27792502b86b147d3f0f8892a2130f56` |
| `032_missiles_achievement_prompt.md` | 12390 | 12390 | `702f944a67ecdc2fa29a7b03afbb018bd98d3a53d6dbf63b26393ca5f6ba6bab` |
| `032_missiles_asset_prompt.md` | 8701 | 8701 | `6fcceff630189e685afe484e1f5d7480ac22ba4e946a9c5138062dd21999ed07` |
| `032_missiles_coding_prompt.md` | 7223 | 7223 | `8a975b3db6f62130575b88476600e7dd62e173e4e59b39b68bd636e27b24c947` |
| `032_missiles_decision_mission_prompt.md` | 8952 | 8952 | `9cca11cc3520f93c61d9c44f948920a35e282420a6e445052f0f4150d3e380fe` |
| `032_missiles_goal_prompt.md` | 3881 | 3881 | `cc9e482f36da8407c23e8f0dd92ba09bdcdc76d5b5dcff6f325076a77e142d78` |
| `032_missiles_improvement_loop_closure.md` | 5530 | 5530 | `9ef0d905b695ca5315adffc3866211be42c3fa52c9e4b7d54fd0868446209f05` |
| `032_missiles_probability_scenario_matrix.md` | 10613 | 10613 | `3e1d754eb5a3c9d4e0c72c2a7f0a253f38adae560ea2134578aaf76511e4e957` |
| `032_missiles_requirement_traceability.md` | 8995 | 8995 | `d35096f3c65a5b5aee3ad0e32efd5c0864c21b5cae8129f758d5e048c5964651` |
| `032_missiles_research_notes.md` | 4339 | 4339 | `8abd85f4a1ca031671e660ab036e38c3e2338e7788340c820d93c90ecbdae3de` |
| `032_missiles_source_review.md` | 7776 | 7776 | `bd3cb4ea4b91993fb5d1e236dd63242eeb0d1e89ee86b60b7da9d2ff5bb52eca` |
| `032_missiles_spec_part_1_core.md` | 13666 | 13666 | `43787b9f33a0d61ec4088a25e4b0777595f66cc9466f7f45183b46690490c659` |
| `032_missiles_spec_part_2_program_and_launch_sites.md` | 19279 | 19279 | `ead30740f2eb146ccd3768abc02e9be7bf8b5472a0ec059911b556582ce6562f` |
| `032_missiles_spec_part_3_operations_and_consequences.md` | 21569 | 21569 | `21a9e3fc1c75f359d85fb4cbefbaaaa425fd349aaf18005448e450da616a5545` |
| `032_missiles_spec_part_4_evolutions.md` | 35981 | 35981 | `cb6d46f480315d1e7f584ca65012f09a87e4db0682569cc87248b7c771a85704` |
| `032_missiles_spec_part_5_decisions_missions_and_scenario.md` | 23909 | 23909 | `e6be99c1612cd4cd693ba85f91733ecdb73b81efb6a08ae54b5a311b94f28fb0` |
| `032_missiles_spec_part_6_ai_and_probability.md` | 16147 | 16147 | `5a5667a4d84e261bd16ac54cb2f3b6027798df0a30cd39aa1f2864dce85b5304` |
| `032_missiles_spec_part_7_assets_text_and_achievements.md` | 15312 | 15311 | `f1b9c9c1e44a9a84fcde50e054660db058f68f9e5d5d1f01cff5ed3c498eb8e2` |
| `032_missiles_spec_part_8_implementation_contract.md` | 17542 | 17542 | `df0870503eabd9b6094b249e62f61fc9790302e699b2ff4eaa1a9716db217ffa` |
| `032_missiles_system_connections.md` | 12339 | 12339 | `7e2001b19e2450421383a676b81b07c6846ca708360c8ec9d44f1db260a114a9` |
| `032_missiles_test_matrix.md` | 13078 | 13078 | `a194165ece3ad5c5396216aca0607b9c455460d189f42cf7ff904a3d4ad203f3` |
| `README.md` | 5402 | 5402 | `86f782d0d4c8203131bca326f847b2833868ca79846de8d74254db3d5d74a9b0` |
