# Event 097 Collaboration: Source Inventory

Disposition: implementation evidence for the planning pass. This record states what the planning agent read and how. It does not establish design approval.

## Uploaded package

Archive `dae90af9-all-project-sources.zip`, sha256 `0f13352a0bbf4c657fcb82ac6ec549a1ac208f2624b23489c25dc9bd85105d3e`. It held 27 files, including `subagents.zip` with 20 role definitions.

Reading status for every uploaded file is full unless stated otherwise.

- Skill files `chaos-redux-*.md` (19 files): read in full. The planning, events, decision, assets, and focus-tree skills were read in sequential chunks that cover every line. Two files contain lines longer than 2,000 characters (`chaos-redux-3d-model-pipeline.md` line 155, `chaos-redux-subagents.md` lines 177 and 179). The tails of those lines were read separately so no text was skipped.
- `AGENTS.md`: the repository copy was read in full and the uploaded copy was compared with it line by line. The uploaded copy adds the 1,000-iteration loop limit and the variable-scope note.
- `CHAOS_REDUX_MECHANICS.md`, `README.md`, `config.toml`, `chaosx_dynamic_effects.md`, `chaosx_dynamic_triggers.md`: read in full.
- `chaos_redux_events_catalog.csv` and `chaos_redux_clusters_catalog.csv`: read in full.
- `chaos_redux_scenarios_catalog.csv`: first read with every line cut at 400 characters. The cut tails of the twelve longer lines were read later in the same session, so the whole file has now been read.
- Subagent role definitions (20 TOML files): read in full except the `model` lines, which were skipped because model selection belongs to the runtime.

## Repository sources read directly by the planning agent

- `AGENTS.md`, `events/097_collaboration.txt`, `events/095_occupation_revolt.txt`
- `docs/specs/052_intel_leaked_specs/README.md`, part 1, part 5, and the first 250 lines of part 6, used as the package format reference and for the reserved Event 097 hook
- `docs/specs/README.md` and `docs/plans/README.md` headers
- `common/scripted_effects/chaos_meter_effects.txt`, the tier update effect
- `docs/spreadsheets/chaos_redux_events_catalog.csv` row 97 and `chaos_redux_clusters_catalog.csv`
- Offline wiki snapshot `paradox_wiki/`: collaboration entries in Effects, Triggers, Data structures, Defines, List of modifiers, and On actions, read as targeted sections rather than whole pages

## Repository sources read by subagents

- `chaosx_repo_explorer`: see `subagent_handoffs/097_repo_explorer_handoff.md`, section Scope read. It covers event registration, clusters, evolution logging, the Chaos Meter, on-actions, occupation, autonomy and ideologies, Fallout collaboration handling, achievements, super-event slots, decision categories, and AI strategy.
- `chaosx_scripted_system_architect`: see `097_collaboration_scripted_architecture_plan.md`.
- `chaosx_decision_mission_auditor` and `chaosx_ai_probability_auditor`: see their handoffs in `subagent_handoffs/`.

## Sources that could not be read

- Vanilla Hearts of Iron IV files and the vanilla `documentation` folder are not present in this Linux container.
- Approved reference mods (Kaiserreich and the other two workshop ids) are not present.
- The HOI4 MCP server failed to connect, so no MCP inspection exists.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is a Git LFS pointer in this checkout. Only the CSV exports were readable.
- The Paradox wiki on the web was not used, as the repository rules require.

## Uploaded file hashes

```text
0bef38348ee4388c70eac073ff855e25ebdabcfef4855ba14183ef9cc604e5a8  AGENTS.md
21f21df8bf621e4362f1e010d342f71df2a939c499bbfce89bc7772790411b56  CHAOS_REDUX_MECHANICS.md
9f713e2dcaf1e0fad5b070b8a921b23a648a1a01583e4f698cdd50e8e66bce74  README.md
1cc1ec0c64fd150c4a4066ca1694211c621b4cd5625bf2c6f13694b64782fae9  chaos-redux-3d-model-pipeline.md
ea26d70c3239138dce16d3a653e166701a6b7a99fcd0ed06332ad2c5785e626a  chaos-redux-debug-playtest.md
69c7710d7b4688e22b4ed9f04bfe3dded4a9cd5f936316d1d66bd0fda9b9e9d7  chaos-redux-decisions-missions.md
7a728ccbab2ccf3483b1932a99ba971622f5086767bd2cfa76c313a4ef02b279  chaos-redux-event-assets.md
798800daed7178a659c51811384f71f5f15d0c34fbf2c9443d03c596931f4a2a  chaos-redux-event-planning.md
9fb0b8d8b7a9eda49245922c6e483a711fbfa2e83ba425896d18d220e0ee2e1b  chaos-redux-events.md
201b6a026201bfc2e02e5d122a02d2bf3423ed463ec5041becb9d496cf7e4018  chaos-redux-focus-trees.md
57ab0788652c45c6b21b56d46d96bd5b0e1aa3456d826a6cc42ae89a12e712ab  chaos-redux-frame-animation.md
a875e05d1f4fa31d90ccc126ea61d9e391ee23af333521a818eafddf2eef50b7  chaos-redux-improvement-loop.md
8a58ec3b838fbc006af98a39f69f77d104e405588490384b81f53ea75bae2160  chaos-redux-mtth.md
601c90faca20b8166496a38153776facf37d5efb0224ad48fd8879de66b7534c  chaos-redux-native-raids.md
038224e26040889915458b6aa03039f2f34bd8e4c1e182dbe4ec8a3cded8f01e  chaos-redux-save-inspection.md
b8aa8fe124d15a5f7fddaa97d6193b2cc54d9dfba9bd1fdbbaab90d6a0184842  chaos-redux-scripted-gui.md
ce1cc18b7b2a522aa1d12d687c85247e2d4881d50593508f6a37b54bd34fd502  chaos-redux-shared-git-commit.md
208c7451f42c7f60fda71f8ed79a604f1469b819f2f17a4769d87016519e1646  chaos-redux-state-ledgers.md
06079fb7e7c01bf09a5fea1ffabdfbb73b99fcecddd28ef7720415fbbceeda61  chaos-redux-subagents.md
cb6fd9f8641c9115cc2ab6b357f53d7ef0b21a9348a227e0f1aab1586e5548bd  chaos-redux-super-events.md
0192ea7fabe323a73147af74928397c925546865f87387835968fba033dec739  chaosx_dynamic_effects.md
9e6db6f77e0b5fca50ed2b6840664fc5642bacdc754d68c42f0d3c4a5f5fe681  chaosx_dynamic_triggers.md
e5b47a6c9f0f4af495ffc16ce5ae3d8765af3bc16ca5e3418a81eac0c6501ff5  config.toml
276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a  chaos_redux_clusters_catalog.csv
465050976a1134e57945cec56e95232e6c54fa2a8b4c5a3b569b0d638230d2c0  chaos_redux_events_catalog.csv
cdc1c288a885d6b62225d7d84ed6af560f4267322d74a7a4cf4b28a7d16b124d  chaos_redux_scenarios_catalog.csv
89f68c42cc1385f7cfc40c14229462854754fa4d933a7de582002cd901e93b23  chaosx_3d_model_pipeline.toml
f30e9b61560f9e863013740946ebd53bbb1d4cb2fbb21d5d4903c86ce813acf6  chaosx_ai_probability_auditor.toml
02e9522da2f968bb1d1aedf6d5b3ceee13773c19c43a9b72ef1fc96f94ba922b  chaosx_asset_source_researcher.toml
a6a6a9e003c58af795a217ae8e5cf0096d1ec116b0ec5b3a25871e2526211b44  chaosx_country_package_auditor.toml
e70f478705aa61c145e4ed1776d5cedc78acf1b26182809ee3e1e1c557d5cc59  chaosx_decision_mission_auditor.toml
68aab4a71c00065ae88cff1417e2e2790da79d0c9a1390d132dec93942ffc49d  chaosx_documentation_curator.toml
277fa8ce183ecb1b586620be058e075860940863121e190b619be18e3eabde66  chaosx_event_completion_auditor.toml
a9f67e17c7ad6aeb31f4a1d7078ad50a2c7dffe52ba5fdc6d704f752aa932ef9  chaosx_event_ui_worker.toml
8905303df1fdc2c7ff002c8cfb53abf59e87259cef574c6935d4d85b36682847  chaosx_focus_tree_auditor.toml
adaac5d900e1e0b2d3a69c8746b85f0e5585faea7b011acd33bc51eb4ce4e66a  chaosx_generated_event_art.toml
2ae3cce3c2fe249a24cc91efcaccdbede8be8cac56bf7f9dd23a3a83657d9574  chaosx_icon_artist.toml
04b7bdbe8f0e4dc33f8b97d45fc4823a1b4684fe59896c0721297fa21a385fa5  chaosx_improvement_loop_planner.toml
cd66a77792965ec5c435e7b8892847000ff4da0c70816966b047f2f3514c2b9f  chaosx_localisation_auditor.toml
1d8e334d8535bc1f5a4722f0fa7877b641dff51a20e8269e891ae7694daf9145  chaosx_portrait_creator.toml
dfaaf09b1ae5d8b98684a6dfcac20bed03d03ae27f5e210abfe7b8659fbedb01  chaosx_repo_explorer.toml
d1f3face145ee254ce6b02d602778311c6183c53a9343df0ff18acc56d294289  chaosx_scripted_system_architect.toml
ee8785031aa9924bd0370043297af80c627d853f86bb05caf43527111913aa88  chaosx_skill_maintainer.toml
90e6f756d7d9547709e630e5071def8d4cc968b5070276ff8c795134b52801bc  chaosx_spreadsheet_doc_worker.toml
bf623c4ad7210badfe0f53d175e5c7ef8f73e27639501c4811e07bc12d0c0098  chaosx_super_event_audio_researcher.toml
f75fd8cd6aba92afe806f0687027d7f8a92f1574a07064698548b82c5ed1441a  chaosx_super_event_text_researcher.toml
```
