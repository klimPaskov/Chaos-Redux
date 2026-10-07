# Event 83 source read ledger

## Supplied archive

All 42 supplied text files were read completely before authoring the source specification. Long inputs were read in bounded chunks, and truncated supplied-file windows were revisited. The nested ZIP contains 20 profiles, which were extracted and read as text. Archive containers are not counted as additional text reads.

| Supplied text file | Bytes | SHA-256 | Read status |
| --- | ---: | --- | --- |
| `AGENTS.md` | 44,442 | `ba5f6799c692f461e3922e0a2e6687516bba210206c3758b07c37fce5cfb56d4` | Fully read |
| `CHAOS_REDUX_MECHANICS.md` | 41,848 | `e3f21aca358f84d085222272bccd1d2896b4c0ef4bb418de079f882975e35da1` | Fully read |
| `README.md` | 2,857 | `9f713e2dcaf1e0fad5b070b8a921b23a648a1a01583e4f698cdd50e8e66bce74` | Fully read |
| `chaos-redux-3d-model-pipeline.md` | 96,728 | `45ffc273c4df5ec479c83f193815d2c9ffd6092e18cec54242544c08684442f7` | Fully read |
| `chaos-redux-comfyui.md` | 2,456 | `125daa4e66957fcf02f5cd91e3a0a17f4a99395ad0f40c7ae376b4b59393b303` | Fully read |
| `chaos-redux-debug-playtest.md` | 34,086 | `9c6e27b8a86fd27422d8b2ec5302ac6fa7c64d89a564dbbda71db238190e3549` | Fully read |
| `chaos-redux-decisions-missions.md` | 64,394 | `bd92b691ec78d81db2fe9c19f5574e21969dfa951ef08dbb9dc80085cc2034d9` | Fully read |
| `chaos-redux-event-assets.md` | 109,712 | `6766e846130e22a1ac0cea89e32bb0fca9495828216a130c1a882e1544212bfd` | Fully read |
| `chaos-redux-event-planning.md` | 197,109 | `4a1a0a46ffe4145d61fe0992ad7eb82650c386af028b21a1dbd10a6e227881cb` | Fully read |
| `chaos-redux-events.md` | 80,791 | `42b1c53c5996f8bb495426b9ebdc6854cdd4309744feddb26df781a0692dd036` | Fully read |
| `chaos-redux-focus-trees.md` | 98,951 | `74805c1f8522ee8630912fd8946c6d547fd43d61e4a907fc71ba08a803253d3f` | Fully read |
| `chaos-redux-frame-animation.md` | 28,266 | `86469ff50f33ead0690d3709b0523de1992f01a29713b801a6dd08c27b1be870` | Fully read |
| `chaos-redux-improvement-loop.md` | 28,515 | `ca2b6a001f691f2b247823b5b9914a3d04076dff429aa85bc035aa34f6124d73` | Fully read |
| `chaos-redux-scripted-gui.md` | 23,695 | `f85f0a0888b25d14ca6d6b6535ea8b578542e19dac1f5fbd3d9113e51a525b93` | Fully read |
| `chaos-redux-subagents.md` | 41,493 | `68e6b1d4878e4c87981c9e58cebb1182052555d9313d60748fd573f01ad8223e` | Fully read |
| `chaos-redux-super-events.md` | 33,489 | `001a899b4b19ccf6bdf15a82bd446eae0e290c5f64caec5762883af25976924e` | Fully read |
| `chaos_redux_clusters_catalog.csv` | 5,362 | `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2` | Fully read |
| `chaos_redux_events_catalog.csv` | 65,053 | `e2e457ba96ae89b316aa01248eebe41d9aacbafc590f4940b56a55133fcd35c6` | Fully read |
| `chaos_redux_scenarios_catalog.csv` | 16,848 | `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7` | Fully read |
| `chaosx_dynamic_effects.md` | 19,635 | `73b2740ebfb891c6772de72d456dd1805f5bd3921f61ff60c0df38c6f2c45030` | Fully read |
| `chaosx_dynamic_triggers.md` | 3,991 | `6792ee030cb6b658698e92f188f4980e05553f80ba3de8b9260d3cf47fab4843` | Fully read |
| `config.toml` | 11,714 | `24bcac71960d42d2958fc98b49fd38a5244b0946bf80cf3ddb879a633c269427` | Fully read |
| `subagents/chaosx_3d_model_pipeline.toml` | 27,552 | `f0036ce6d12b60c01c3b1042ddee59bbefad13f8267625efcfd9569ac42d226d` | Fully read |
| `subagents/chaosx_ai_probability_auditor.toml` | 6,414 | `1c3c202e7f15d310cbe2879f3d6f088e2c2fe71806bb33f13bd276c173d184b2` | Fully read |
| `subagents/chaosx_asset_source_researcher.toml` | 3,024 | `f652dfac61f3e41decbdcbb48765b281f7ac7bc0eb7803aa2a89d94c6ccdea7b` | Fully read |
| `subagents/chaosx_country_package_auditor.toml` | 8,099 | `d1c6e194082366b514310f76d4c8e7e81679fc81d2be6d23bb59fc16a0ce4bd0` | Fully read |
| `subagents/chaosx_decision_mission_auditor.toml` | 8,994 | `1b1f9e50909d54daf2a11d255873b7382f970871543d751d924d94b015265a32` | Fully read |
| `subagents/chaosx_documentation_curator.toml` | 11,319 | `e881bcc4303dac392904464c7bdce47a11d2210f6f794842f56245579c048008` | Fully read |
| `subagents/chaosx_event_completion_auditor.toml` | 4,141 | `38180484672c2cb363b40cbdd712ef9dbdd1df9cda9acbc534223ab42fb22990` | Fully read |
| `subagents/chaosx_event_ui_worker.toml` | 10,136 | `56a254896faf78e4c6ca5aa6398fa5ac6b7106ec6bdc6f0efe767acfa879032c` | Fully read |
| `subagents/chaosx_focus_tree_auditor.toml` | 4,480 | `88149cedcf2de42a2b824635133d083dac4ab9e911de4d91174b727919bb7aac` | Fully read |
| `subagents/chaosx_generated_event_art.toml` | 3,930 | `d056a89535a8740cd6dac3d61cea5f5a73fe9ef6e4d9a87406a86aedc851a38d` | Fully read |
| `subagents/chaosx_icon_artist.toml` | 10,096 | `df0345a30665c2197b77e5a9df72fd12d545086de3010358077fbe4bf9799f2b` | Fully read |
| `subagents/chaosx_improvement_loop_planner.toml` | 7,229 | `c8bcb04ac81e33dac5975c7f3294383f730645b3a3fc3ef26b0c2eb1d79a86b8` | Fully read |
| `subagents/chaosx_localisation_auditor.toml` | 9,782 | `8d588111bb27da851af9d16b8c426d6e9b59e517444464225e0a3e91385a161b` | Fully read |
| `subagents/chaosx_portrait_creator.toml` | 2,049 | `ea2ae603081f64afa82f588bfc143b35f97ee8165f16cf0271784869c55086f8` | Fully read |
| `subagents/chaosx_repo_explorer.toml` | 13,488 | `276acf0305e8b2a1a9c2b6f60cc8153a9e5cd2d629dca85c592e834c9a65fd9a` | Fully read |
| `subagents/chaosx_scripted_system_architect.toml` | 5,388 | `7c845c07d54d3c19533ed24f6a68a9b77d9e90e056824bd87023916d9a8a89f2` | Fully read |
| `subagents/chaosx_skill_maintainer.toml` | 3,258 | `232a9a008c076c9baf38e10b412c8d1bbedfd108e209f33b514053f29b41d148` | Fully read |
| `subagents/chaosx_spreadsheet_doc_worker.toml` | 4,605 | `896cb63222484317280d31c340edfc282847774f8edab31a68d7fc2b8b0be33b` | Fully read |
| `subagents/chaosx_super_event_audio_researcher.toml` | 3,342 | `c0e7e0c422f158e566e2b8fa72de3da225ff626ef3fab06927281b9e33a458c3` | Fully read |
| `subagents/chaosx_super_event_text_researcher.toml` | 3,921 | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` | Fully read |

Total supplied text bytes: **1,202,682**.
Outer archive SHA-256: `658006c9a1fdde344db7a647a329c70478bb2dac564371c2eac4bc4cf01ee318`.

## External reads

| External material | Status in this session |
| --- | --- |
| Pinned Event 83 event file | Fully read |
| Pinned Event 83 English localisation | Fully read |
| Pinned shared cluster constants | Fully read |
| Pinned MTTH skill | Fully read |
| Repository offline Effects reference | Partially read, including focused agency and operative sections |
| Repository offline Modifiers reference | Partially read, including focused intelligence and operative sections |
| Repository offline wiki directory listing | Inspected listing, not a read of every listed file |
| Official 30 October 2019 intelligence-agency diary | Relevant diary section read, archive contains unrelated entries |
| GCHQ historical page | Relevant article read |
| CIA foreign-language history article | Fully read |
| Official La Résistance product pages | Product descriptions reviewed, not engine documentation |

## Required material not fully available or not read

| Required reference or capability | Reason and consequence |
| --- | --- |
| Installed game documentation and actual game-version identifiers | Installation unavailable, exact script adapters unverified |
| Vanilla agency-upgrade definitions and actual vanilla random-upgrade helper | Not supplied, exhaustive native pool and helper behavior unverified |
| Installed operative recruitment definitions, interface, and hooks | Not supplied, immediate batch recruitment remains a gate |
| Installed operation definitions, assignment values, and achievement callbacks | Not supplied, exact pursuit hooks remain a gate |
| Complete offline Effects and Modifiers files | Retrieved responses were oversized and only selected portions were read |
| Other linked offline wiki pages | Not exhaustively fetched or read |
| Current shared picker, cluster effects, history, settings, MTTH implementation, and achievement source files | Follow-up inspection targets, not claimed as fully read here |
| All accepted connected-event source packages | Supplied brief and catalog context available, complete Intel Leaked and Parliament of Fear implementations not read |
| Canonical source workbooks | CSV exports supplied, authoritative XLSX workbooks not supplied or edited |
| Vanilla visual reference library and matching contact sheets | Not supplied and not visually inspected |
| Current full local and Workshop mod load order | Unavailable, exhaustive third-party coverage cannot be claimed |
| Executable independent subagents and HOI4 MCP services | No usable tool route exposed, configuration declarations do not execute agents |
| Live in-game testing and screenshots | No engine execution or user-provided Event 83 live evidence in this task |

## Honest completion statement

Every supplied text file was fully read. Not every required external project or game reference was fully read. No independent subagents, HOI4 MCP audits, asset-generation workers, or live game tests were executed. The delivered files therefore separate authored design, inspected evidence, semantic tests, and unresolved implementation gates.
