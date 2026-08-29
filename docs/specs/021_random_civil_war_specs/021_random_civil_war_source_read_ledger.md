# Event 021 Source Read Ledger

## Reading statement

Every project source file supplied directly for this task was opened and read in full before the specification package was finalized.

This includes:

- repository rules
- the complete mechanics guide
- every supplied skill Markdown file
- dynamic trigger and effect registries
- the current Codex configuration
- all three catalog CSV exports
- every custom subagent TOML file inside `subagents.zip`

The prior July 25 Event 021 package was also reviewed through the user's File Library. Its compiled master specification, README, manifest, coding prompt, goal prompt, and source ledger were available as file-search references. Those File Library items were not mounted as local byte files, so local hashes are not claimed for them.

## Directly supplied files

| File | Lines | Bytes | SHA-256 | Read status |
| --- | ---: | ---: | --- | --- |
| `AGENTS(7).md` | 404 | 38,674 | `6a98c2676c0130bc78e843eb7cf485fd86f04696c03a9225034f2008f3915704` | Complete |
| `CHAOS_REDUX_MECHANICS(7).md` | 1091 | 57,858 | `615d1293862582fc458acf6440e2d2f7dd738793fc0f11aac6c5c471528cdfc4` | Complete |
| `chaos-redux-comfyui(2).md` | 16 | 2,123 | `128acd133fedc56b14612eed163de11d7261dac887f11eacf4c8b695dae97fa0` | Complete |
| `chaos-redux-events(8).md` | 761 | 67,981 | `fbbc00b27aeefa915ec6f5a032a08fbbc076146855f68922609cfe7652e57c0f` | Complete |
| `chaos-redux-event-assets(7).md` | 1457 | 111,377 | `5c73bdf087be2ca087aab8e856c14c4d60f473c57c8ec3878e155eabf42a2fdd` | Complete |
| `chaos-redux-debug-playtest(2).md` | 666 | 30,145 | `ec9d66e433e9d964a2561844aa45281342842b973e059a09fab18f2107283a43` | Complete |
| `chaos-redux-3d-model-pipeline(3).md` | 303 | 43,678 | `5ac9915cf30fbde15687eb9c30ca8b8be0d24a5801b72019efceb5766b5f6296` | Complete |
| `chaos-redux-event-planning(20260813-152954).md` | 2116 | 174,584 | `1f8108878ed76d5dc4fd649e69208f0912924acf9351f5dde2cefa7f3c494886` | Complete |
| `chaos-redux-super-events(7).md` | 793 | 33,028 | `d7afffcf25b70333fd50aaef1f72378c1c270b8057269597f085c96204e01607` | Complete |
| `chaos-redux-improvement-loop(8).md` | 287 | 27,425 | `fdd2f3526a0fb4d051dd135a403de99dc402f5df82788c01eedabe44156f96f9` | Complete |
| `chaos-redux-frame-animation(8).md` | 488 | 25,386 | `71b9b82c067fb6162d52eff233d8e60f49ece8c6fdec043c5e1de8127b7b769d` | Complete |
| `chaos-redux-subagents(8).md` | 351 | 32,913 | `7062f5a36f9dd7f7844b38374a3339308799441380c6d48d3250c8e989204bb7` | Complete |
| `chaos-redux-focus-trees(3).md` | 1503 | 98,154 | `51f741f8abde30c7772be46072fa4530361dcf4fc348da97b69c86206761789b` | Complete |
| `chaos-redux-decisions-missions(3).md` | 1158 | 72,964 | `8bf185927863c2da3781aabc31f4df6a373d30a8c497bc21121cd4c3c3cbdbc4` | Complete |
| `chaosx_dynamic_triggers.md` | 87 | 4,690 | `08142b36d735c9994daca01a1fce8296998c530fab8d3e2fd4ffdf4a45a26a37` | Complete |
| `chaosx_dynamic_effects.md` | 537 | 31,440 | `c44d28801253892b9d141097ba31c0705a3f5b07da46ac163be66998b58f11b7` | Complete |
| `config.toml` | 179 | 10,887 | `8579f09a550ad451e56e6bee51fa39eb559f67849a9c6249c66ef37f8c67c139` | Complete |
| `chaos_redux_events_catalog(3).csv` | 329 | 55,685 | `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db` | Complete |
| `chaos_redux_clusters_catalog(3).csv` | 14 | 2,586 | `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299` | Complete |
| `chaos_redux_scenarios_catalog(3).csv` | 48 | 10,807 | `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760` | Complete |
| `subagents.zip` | n/a | 56,708 | `6e6f029b37107cc9ab5a27e8b2e874980cc3ab3e515ea1022de0a930b4bcd05f` | Complete |

## Custom subagent files extracted from `subagents.zip`

| File | Lines | Bytes | SHA-256 | Read status |
| --- | ---: | ---: | --- | --- |
| `chaosx_3d_model_pipeline.toml` | 181 | 19,388 | `7c2352911569cc0c1131b1679e5b6665e8c2b314edc42d05089a19fc813b9c0b` | Complete |
| `chaosx_ai_probability_auditor.toml` | 66 | 6,348 | `20336a1ec04210d7f468e364fa48ca59427a5fa1292e8765af9eb746a73e6856` | Complete |
| `chaosx_asset_source_researcher.toml` | 58 | 3,017 | `4db7e102822821201eb80055d45ad89272de7cdc4c6c695953d45854bd0e8df6` | Complete |
| `chaosx_country_package_auditor.toml` | 87 | 7,965 | `b140694067beb96d77ab31f6bf1eaa595eff02cf6ae83ce33e50e7ef2bedece4` | Complete |
| `chaosx_decision_mission_auditor.toml` | 85 | 5,713 | `0283283ae968c573d3ac0ee45bf654a4c15fd86bbc70b0592f9063b2503f8a16` | Complete |
| `chaosx_documentation_curator.toml` | 131 | 10,140 | `8aea5aad0f4c5350013377041e57029d3cd296774a6713977f2e34cccf533885` | Complete |
| `chaosx_event_completion_auditor.toml` | 66 | 4,118 | `fadb00b2634b66d3c150cdd872a3d4307d2e725811d00684c467d8057978a757` | Complete |
| `chaosx_event_ui_worker.toml` | 78 | 8,145 | `3f08c4655ad7da66d897de6301804d649f223215193f3e09d52c42a6a54256b9` | Complete |
| `chaosx_focus_tree_auditor.toml` | 80 | 4,499 | `83149977d6749cfe743d8ec4c2afa769a019dbfbbc8fd62390460b3629f444e3` | Complete |
| `chaosx_generated_event_art.toml` | 64 | 3,307 | `76e26422ac3e59c3fe43b5cc8fb969fc52973e22b241d4caa85aedc9dc80670a` | Complete |
| `chaosx_icon_artist.toml` | 90 | 6,610 | `61fa1d540d47a7571f8dff0636a43bfa7fda4f74b875662be307a88f9e8364e9` | Complete |
| `chaosx_improvement_loop_planner.toml` | 61 | 7,069 | `a90323b1cbbd664fa61e245186fe7dd912498018e07f3e2393e2641555fbd2bf` | Complete |
| `chaosx_localisation_auditor.toml` | 108 | 8,894 | `8133c2956a876475179383e5e6bff051776d0f4abbad797d88627846f932ca4d` | Complete |
| `chaosx_portrait_creator.toml` | 20 | 2,029 | `87b001c6fb5afc33267eb77a3187ff654dbf6b03ae5d669cb2d5182bf7ac2174` | Complete |
| `chaosx_repo_explorer.toml` | 234 | 12,690 | `3b7380b83e0dd6bba741b5c5cd5419e3e5bf22c284459d28d60706b246d964a1` | Complete |
| `chaosx_scripted_system_architect.toml` | 74 | 5,387 | `b2e012aaec78bc875ae27275eb03f86d425aa19ece182716d2570117ff56cacf` | Complete |
| `chaosx_skill_maintainer.toml` | 47 | 3,819 | `1c5efb578a007fc1e3e7f0561d7353876d73918be830f754870041f9d2f66ac2` | Complete |
| `chaosx_spreadsheet_doc_worker.toml` | 59 | 4,607 | `b34a6420591c90ba905cc793e36a531bb4c1e3484fa4684663eb49cac0e70832` | Complete |
| `chaosx_super_event_audio_researcher.toml` | 65 | 3,333 | `16df05752d0ebff6838e2580a35cfac30e781ab1eef3d16e8deec2835a5a2834` | Complete |
| `chaosx_super_event_text_researcher.toml` | 62 | 3,921 | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` | Complete |

## Catalog parsing

| Catalog | Data rows | Nonempty rows | Reading result |
| --- | ---: | ---: | --- |
| `chaos_redux_events_catalog(3).csv` | 182 | 182 | Complete |
| `chaos_redux_clusters_catalog(3).csv` | 13 | 13 | Complete |
| `chaos_redux_scenarios_catalog(3).csv` | 11 | 11 | Complete |

The catalogs are export snapshots. The authoritative event workbook was not supplied to the planning environment and was not edited.

## Important catalog findings

- Event 21 is listed as Random Civil War
- the event is a Minor Repeatable event
- the event remains To Be Reworked in the supplied export
- Cluster 1 is Wars
- the proposed Event 021 member severity is Medium
- the supplied scenario export ends at `SCN-013`
- `SCN-014` appears to be the next numerical slot, but the package does not reserve it
- the implementation agent must verify the live workbook and registry before assigning an ID

## Planning-environment sources that were unavailable

The following required implementation sources could not be read because they were not mounted or exposed:

- the live Chaos Redux repository
- the repository's offline Paradox wiki snapshot
- installed vanilla Hearts of Iron IV documentation
- installed vanilla game files
- approved Workshop reference mods
- other local mods
- current authoritative XLSX workbook
- live HOI4 MCP tools and schemas
- the custom Codex subagent runtime

The package does not pretend those sources were reviewed.

Their review is an implementation gate in Part 10 and in the coding prompt.

## Web research

External research was used only to strengthen the generic civil-war model.

The research note records:

- UCDP armed-conflict definitions
- Fearon and Laitin on insurgency and state capacity
- Cederman, Wimmer, and Min on exclusion and mobilization
- Salehyan and Gleditsch on cross-border diffusion and refugees
- Walter on recurrence
- Cunningham on multiple actors and duration
- Bakke, Cunningham, and Seymour on fragmentation
- SIPRI material on external support

Every source is linked and separated from project-derived design in `021_random_civil_war_research_notes.md`.

## Honesty statement

All directly supplied sources and all extracted subagent files were fully read.

The unavailable live repository, wiki, vanilla, Workshop, MCP, and subagent execution sources were not read or run. They remain explicit implementation requirements.
