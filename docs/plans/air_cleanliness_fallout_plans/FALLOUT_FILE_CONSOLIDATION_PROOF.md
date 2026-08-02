# Fallout runtime file consolidation proof

## Scope

The merge snapshot was taken on 2026-08-02. It covers 718 source files and produces 20 loader files.
Events remain in `events/fallout_world_end_events.txt`, with the Air Treaty namespace folded into that canonical event file.
The event catalog workbook and all three exported catalog snapshots have no rows whose identifier begins with `FALLOUT`.
Fallout is not registered as an ordinary event log entry or ordinary super-event.

## Preserved invariants

- Source blocks were appended in lexical filename order, matching the directory ordering used before consolidation.
- No source block was transformed except for removing repeated `l_english:` headers in the one localisation output.
- Explicit namespaces remain present, including `chaosx.fallout` and `chaosx_air_treaty`.
- Localisation output has one UTF-8 BOM and one `l_english:` header.
- Existing asset references were copied unchanged. No asset was moved out of `gfx/event_pictures/fallout`.
- Shared files containing non-Fallout systems were not folded into these outputs.

## Source-to-destination ledger

- `common/ai_strategy_plans/fallout_consolidated_ai.txt` receives 2 sources, 232 source lines, and has SHA-256 `20bdfe16633d09f230be6928055ab43b3c1f383a53afc93dec0923d21d54bb62`.
- `common/characters/fallout_consolidated_characters.txt` receives 1 sources, 10 source lines, and has SHA-256 `8ffba1ddaffab4cd1d7813eeddbd3d5369a9e7f379e7a1ac49ed83745b3ad88e`.
- `common/countries/fallout_consolidated_countries.txt` receives 1 sources, 20 source lines, and has SHA-256 `35e4022fabb582228853564bc2571a0b54fc902425607b70fe49f9400d90729b`.
- `common/country_leader/fallout_consolidated_leader_traits.txt` receives 1 sources, 50 source lines, and has SHA-256 `f9c03c9f40e8af8f9bf67e638efae4b1b95d593e009f4be19693db9c918a6b12`.
- `common/decisions/fallout_consolidated_decisions.txt` receives 5 sources, 2,455 source lines, and has SHA-256 `270afb1966dfe4004632143fb975beb948ce55ace69fc13ceb69e8c75b013644`.
- `common/decisions/categories/fallout_consolidated_categories.txt` receives 3 sources, 39 source lines, and has SHA-256 `dc47805ec03a3d3dcf96c4ee1a0f6ffface4f3c09ebeefb301a5c6db96f9f8b2`.
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt` receives 106 sources, 5,844 source lines, and has SHA-256 `6ffe5436c13501f2e521cd9aee393482d919bb276395b2032e4d67ed46e1314a`.
- `common/ideas/fallout_consolidated_ideas.txt` receives 2 sources, 264 source lines, and has SHA-256 `ffb681a1f5518f66f8c13244f3f3ff21c8f6fae9bcd922ea791e554f5adb9853`.
- `common/national_focus/fallout_consolidated_focus.txt` receives 2 sources, 957 source lines, and has SHA-256 `1b88435818a891b288d7f978e8be08cec2254a185d74b69a8055e6480d7e1a89`.
- `common/on_actions/fallout_consolidated_on_actions.txt` receives 3 sources, 182 source lines, and has SHA-256 `ba2c3c6bcb5e49dd9654eae6f4ff1f24c28c587a456b980101fea31d747a2b82`.
- `common/opinion_modifiers/fallout_consolidated_opinion_modifiers.txt` receives 27 sources, 1,119 source lines, and has SHA-256 `55b11a277888f2f6bc209879a9331763a461fde2d520a7c3c4b3868af9ef00f5`.
- `common/script_constants/fallout_consolidated_constants.txt` receives 99 sources, 41,400 source lines, and has SHA-256 `6b205f265767ab2c6048e2e7baae542de80ca714c1b9d158985388b8424562c5`.
- `common/scripted_effects/fallout_consolidated_effects.txt` receives 123 sources, 127,677 source lines, and has SHA-256 `e355f543f8d526d65b8c9e4befc9b2663bc9e589768aacc1a7d4ff3ffdc44a18`.
- `common/scripted_guis/fallout_consolidated_scripted_gui.txt` receives 2 sources, 44 source lines, and has SHA-256 `f2b490c04576434a208fc8d37c73a05c5aa5f895a950a7feafb453dec6208097`.
- `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt` receives 106 sources, 3,397 source lines, and has SHA-256 `4dd6b0b57eeb3b94d83294331afba6431190e89a96cb75476f7c4223118ed6d7`.
- `common/scripted_triggers/fallout_consolidated_triggers.txt` receives 114 sources, 33,103 source lines, and has SHA-256 `c7f5b20f2a1760e4af5988df64d7d8add88391cde061adfddeb13866bc617403`.
- `interface/fallout_consolidated.gfx` receives 4 sources, 1,089 source lines, and has SHA-256 `aa6e775f81fe08db315898e88bf4abb0c2fe7876c645c73a08944ebfa4a293c3`.
- `interface/fallout_consolidated.gui` receives 2 sources, 47 source lines, and has SHA-256 `48a033ac8bf21733de9a0ff0e508a8863638c034486b133a6de9ac5fbc8bff92`.
- `localisation/english/fallout_consolidated_l_english.yml` receives 113 sources, 8,185 source lines, and has SHA-256 `9719c34afb50e530e95ea835d5d7f700b58d1d5af01b78eac8b30c9ccec32423`.
- `events/fallout_world_end_events.txt` receives 2 sources, 23,389 source lines, and has SHA-256 `3eb1229a5f5ca64f79448479a735b084a73d8e08c6cc5dc6c7ea3e6485f25ff3`.

## Review checks

The post-merge audit checks for stale owned source files, duplicate localisation keys, duplicate Fallout event ids, repeated localisation headers, stale source filename references in runtime files, and nested Fallout event-picture directories.
A live HOI4 run is intentionally not part of this change. The user will perform consumer validation.

## Offline Event Inspector evidence

The read-only Event Inspector lint query targeted `chaosx.fallout.1051` after consolidation with `refresh = true`, helper expansion disabled, depth `1`, eight nodes, and twelve edges.
The returned status was `ok` with code `EVENT_INSPECTED_PARTIAL`, `blockers: []`, `blockingDiagnostics: 0`, `skippedSources: 0`, `events: 9430`, `options: 14539`, `entries: 1042`, `terminals: 7597`, and `edges: 36650`.
The authoritative report is [event-lint-ba0787a23907.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/563b69ddf173875b3028a7ba24cf028697ed7d95c944ab85ccd851bcfd835611/18d0554dd09925d7a1dc799ca94eccd275d79f178aedaf9a67983f7a8920d877/event-lint-ba0787a23907.json).
The workspace-wide helper and lifecycle projection remains partial by tool design, so this is static parser evidence and not a live campaign claim.

## Deliberate boundaries

Documentation and art packages remain split so each reviewed tranche retains its source prompt, manifest, proof packet, and asset provenance.
The shared Events Log scripted-localisation router and shared candidate producer remain in their existing files because they also serve non-Fallout or cross-chain consumers.
