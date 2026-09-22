# Event 080: Research, source coverage, and limitations

## Status

This package is a detailed source-spec proposal and implementation handoff. It is not implemented event code, a tested mod build, an approved GUI, completed artwork, or an independent completion audit. Its balance figures and expanded content are proposed design choices unless explicitly fixed by the user's brief.

All **42 supplied text files** were read in full, including all twenty extracted subagent definitions. The text corpus totals **1,202,682 bytes and 14,072 lines**. The nested `subagents.zip` was extracted and its twenty text files were included in that reading. Temporary output truncations in supplied-file reads were repaired by further reads. The SHA-256 ledger identifies the exact read versions.

**Not every externally referenced must-read file was available or fully read.** In particular, the archive did not include the offline wiki, installed vanilla documentation and game files, the actual canonical visual reference images and processing templates, the dedicated MTTH skill referenced by the planning workflow, the authoritative catalog workbook, or the original route DDS/source geometry. Only the repository files and ranges listed below were inspected outside the archive. The complete shared population-custody and fire implementation contracts were not inspected.

**No provided subagent was run.** Their definitions were read, but no callable `collaboration.spawn_agent` or HOI4 MCP tool surface was available here. Connector discovery and a plugin search did not provide that capability. Configuration entries on the user's machine are not evidence of tool execution in this session. No probability MCP audit, GUI inspect/render, technology graph audit, asset conversion, or live game playtest was performed.

The specifications were not intentionally shortened into a rough idea sheet. They include full voyage behaviour, 60 passenger and host situations, resource choices, outcomes, evolutions, achievements, Chaos ownership, visuals, and specialist prompts. Unresolved data and engine contracts are reported as blockers instead of being replaced with invented state IDs, API names, or claims of successful validation.

## Authority

[S00] The user's current Airship brief is authoritative for identity, route length, timing, controller-based hosting, Condition, real deaths, direct foreign-controller war, evolutions, and presentation. It overrides conflicting old catalog and runtime behaviour.

[S01] The uploaded source archive is `all-project-sources(20260921-145728).zip`. Its text files establish the planning workflow and shared system contracts available during this task. The CSV files are snapshots. They are not proof that the authoritative workbook was edited.

[S02] Repository evidence was pinned to `klimPaskov/Chaos-Redux` at `879b3007d3b6bf75c726c11635473fccda45c569`. No claim is made that this is the latest repository commit or that it matches the user's current installed build.

## Supplied-file reading manifest

Every row below was read in full. A separate JSON ledger retains each full SHA-256 digest and the completed chunk list.

| Supplied file | Lines | Bytes | SHA-256 prefix |
|---|---:|---:|---|
| `AGENTS.md` | 431 | 44442 | `ba5f6799c692f461e392` |
| `CHAOS_REDUX_MECHANICS.md` | 855 | 41848 | `e3f21aca358f84d08522` |
| `README.md` | 42 | 2857 | `9f713e2dcaf1e0fad5b0` |
| `chaos-redux-3d-model-pipeline.md` | 477 | 96728 | `45ffc273c4df5ec479c8` |
| `chaos-redux-comfyui.md` | 21 | 2456 | `125daa4e66957fcf02f5` |
| `chaos-redux-debug-playtest.md` | 698 | 34086 | `9c6e27b8a86fd27422d8` |
| `chaos-redux-decisions-missions.md` | 1022 | 64394 | `bd92b691ec78d81db2fe` |
| `chaos-redux-event-assets.md` | 1004 | 109712 | `6766e846130e22a1ac0c` |
| `chaos-redux-event-planning.md` | 2297 | 197109 | `4a1a0a46ffe4145d61fe` |
| `chaos-redux-events.md` | 833 | 80791 | `42b1c53c5996f8bb4954` |
| `chaos-redux-focus-trees.md` | 1505 | 98951 | `74805c1f8522ee863091` |
| `chaos-redux-frame-animation.md` | 501 | 28266 | `86469ff50f33ead0690d` |
| `chaos-redux-improvement-loop.md` | 289 | 28515 | `ca2b6a001f691f2b2478` |
| `chaos-redux-scripted-gui.md` | 130 | 23695 | `f85f0a0888b25d14ca6d` |
| `chaos-redux-subagents.md` | 366 | 41493 | `68e6b1d4878e4c87981c` |
| `chaos-redux-super-events.md` | 787 | 33489 | `001a899b4b19ccf6bdf1` |
| `chaos_redux_clusters_catalog.csv` | 20 | 5362 | `689fe07883da14abe2ce` |
| `chaos_redux_events_catalog.csv` | 294 | 65053 | `e2e457ba96ae89b316aa` |
| `chaos_redux_scenarios_catalog.csv` | 120 | 16848 | `8b944de19817b3887eac` |
| `chaosx_dynamic_effects.md` | 328 | 19635 | `73b2740ebfb891c6772d` |
| `chaosx_dynamic_triggers.md` | 61 | 3991 | `6792ee030cb6b658698e` |
| `config.toml` | 192 | 11714 | `24bcac71960d42d2958f` |
| `subagents/chaosx_3d_model_pipeline.toml` | 197 | 27552 | `f0036ce6d12b60c01c3b` |
| `subagents/chaosx_ai_probability_auditor.toml` | 66 | 6414 | `1c3c202e7f15d310cbe2` |
| `subagents/chaosx_asset_source_researcher.toml` | 58 | 3024 | `f652dfac61f3e41decbd` |
| `subagents/chaosx_country_package_auditor.toml` | 87 | 8099 | `d1c6e194082366b51431` |
| `subagents/chaosx_decision_mission_auditor.toml` | 100 | 8994 | `1b1f9e50909d54daf2a1` |
| `subagents/chaosx_documentation_curator.toml` | 134 | 11319 | `e881bcc4303dac392904` |
| `subagents/chaosx_event_completion_auditor.toml` | 66 | 4141 | `38180484672c2cb363b4` |
| `subagents/chaosx_event_ui_worker.toml` | 90 | 10136 | `56a254896faf78e4c6ca` |
| `subagents/chaosx_focus_tree_auditor.toml` | 80 | 4480 | `88149cedcf2de42a2b82` |
| `subagents/chaosx_generated_event_art.toml` | 72 | 3930 | `d056a89535a8740cd6da` |
| `subagents/chaosx_icon_artist.toml` | 117 | 10096 | `df0345a30665c2197b77` |
| `subagents/chaosx_improvement_loop_planner.toml` | 61 | 7229 | `c8bcb04ac81e33dac597` |
| `subagents/chaosx_localisation_auditor.toml` | 111 | 9782 | `8d588111bb27da851af9` |
| `subagents/chaosx_portrait_creator.toml` | 20 | 2049 | `ea2ae603081f64afa82f` |
| `subagents/chaosx_repo_explorer.toml` | 235 | 13488 | `276acf0305e8b2a1a9c2` |
| `subagents/chaosx_scripted_system_architect.toml` | 74 | 5388 | `7c845c07d54d3c19533e` |
| `subagents/chaosx_skill_maintainer.toml` | 45 | 3258 | `232a9a008c076c9baf38` |
| `subagents/chaosx_spreadsheet_doc_worker.toml` | 59 | 4605 | `896cb63222484317280d` |
| `subagents/chaosx_super_event_audio_researcher.toml` | 65 | 3342 | `c0e7e0c422f158e566e2` |
| `subagents/chaosx_super_event_text_researcher.toml` | 62 | 3921 | `c918dae02f2b1127f711` |

## Repository reading extent

| Reference | Path | Extent and evidence used |
|---|---|---|
| R01 | `events/080_airship.txt` | Full returned file read. Confirms legacy opening and ending rewards, host messages, delayed crash report, and war inside a later US event option |
| R02 | `common/decisions/080_airship_decisions.txt` | Full returned file read. Confirms one-day mission, completion at 120, broad flag refresh, paid crash controls, nuclear shortcut, and fixed manpower loss |
| R03 | `common/scripted_guis/080_airship_scripted_guis.txt` | Full returned file read. Confirms decision-category GUI, window name, and dynamic trail sprite selection |
| R04 | `common/scripted_triggers/080_airship_triggers.txt` | Returned main content plus overlapping tail ranges read. Confirms numeric branches 0 through 121 and final region 117. It does not provide exact state bindings |
| R05 | `common/on_actions/080_airship_on_actions.txt` | Large returned excerpt and lines 240 through file end read. The initial full fetch was truncated. This report conservatively treats the file as inspected in substantial ranges, not as a certified complete external-file read |
| R06 | `common/scripted_effects/080_airship_effects.txt` | Lines 1 through 130 read. Confirms broad owner-based host selection and the index-1 region-array discrepancy. The rest was not fully read |
| R07 | `interface/chaosx_decisions.gfx` | Search excerpts only. Confirms the `GFX_airship_trail_120` declaration and its event-owned DDS path. Full file and image contents not inspected |
| R08 | `interface/chaosx_decisions.gui` | Search excerpt only. Identifies the existing Airship container. Full hierarchy and runtime rendering not inspected |
| R09 | `common/decisions/categories/080_airship_categories.txt` | Search excerpt only. Identifies the event category surface |
| R10 | `localisation/english/080_airship_l_english.yml` | Search excerpt only. Identifies existing English localisation and legacy welcome wording |
| R11 | `docs/events/013_natural_disasters/overview.md` | Lines 1 through 130 read. Confirms public gateway ownership, future-date jobs, selected-target proofs, wildfire family, existing-card merging, control transfer, and actual Deaths ownership. Full enum tables and runtime implementation not read |
| R12 | `docs/specs/famine_and_migration_system_specs/` and related handoff matches | Search excerpts only. These identify relevant migration and transit work but do not prove a complete implemented reusable passenger-custody API |

The repository resources were obtained through the connected GitHub tools. They were not downloaded as a complete repository checkout. No source code or workbook was edited as part of this planning task.

## Traceability of the main corrections

| Finding | Evidence | Design response |
|---|---|---|
| Stale Major and war-goal catalog description | Supplied event catalog, row 80, compared with S00 | Minor Fire-Once and immediate declaration are authoritative |
| Daily route timing and early completion | R02 compared with R04 and S00 | 121 transitions at two days each, including the final return |
| Broad owner-based host flags | R06 and R05 compared with S00 | Exact actual position and live state controller |
| Existing dynamic map | R03, R07, R08 | Preserve event-owned map and route art, validate rather than replace it |
| Popup-dependent retaliation | R01 | Immediate crash-resolution declaration, reports afterwards |
| Nuclear and manpower shortcuts | R02, R05 | Actual crash damage and shared exact population/Deaths ownership |
| Per-country and additive risk inflation | R05 | One bounded ship exposure per flight window |
| Public wildfire ownership and delayed jobs | R11 and supplied dynamic-effect registry | Separate immediate impact from subsequent owner-managed fire |
| Shared civilian and nonhuman classification | Supplied dynamic-trigger registry | Adapt civilian flavour without inventing event-local classifications |
| Missing original stop and state map | R04 provides only region predicates, original art unavailable | Preserve the crosswalk and block exact binding completion until verified |

## Historical research and asset research leads

The event is fictional. The passenger counts, refits, Flying City, reward figures, and unconditional American retaliation are design inventions. They are not presented as the history or engineering capability of an actual airship. No historical round-the-world route was substituted for the project's authoritative route.

The following external sources were located during research. They are useful leads for the later asset and super-event researchers. No redistribution permission is implied by their inclusion.

| Source | URL | Inspection and permitted use here |
|---|---|---|
| US Naval History and Heritage Command, USS Akron photography | `https://www.history.navy.mil/content/history/museums/nmusn/explore/photography/aircraft-us/aircraft-usn-a/uss-akron-zrs-4.html` | Official archival search result located. Full page access failed. Treat as a source lead, not a reviewed image set |
| US Naval History and Heritage Command, Akron ship history | `https://www.history.navy.mil/research/histories/ship-histories/danfs/a/akron.html` | Official history located through search. Full page access failed. No quotation or final audio choice drawn from it |
| Zeppelin Museum, American rigid airship USS Akron | `https://www.zeppelin-museum.de/en/digital-offers/the-american-rigid-airship-uss-akron` | Opened museum page with headings and image references. Useful institutional reference lead, not a fully reviewed engineering source |
| Airships.net, Graf Zeppelin | `https://www.airships.net/lz127-graf-zeppelin/` | Historical specialist search result located, including a manifest reference. Research lead only |
| Airships.net, Hindenburg disaster | `https://www.airships.net/hindenburg/disaster/` | Search material reviewed for passenger and rescue context. Not used to assert new engineering conclusions or license archival media |
| British Pathe, archival Hindenburg footage | `https://www.youtube.com/watch?v=CgWHbpMVQ1U` | Archive search lead. Footage, recording rights, and reuse permissions not reviewed |

No final super-event quotation, slogan, lyric, cultural remark, or audio recording was selected. The dedicated prompt preserves these as research gates. Actual historical images, their native files, licensing, and reference comparisons still need the asset workflow.

## Release blockers to close

| Gate | What is missing | Required owner |
|---|---|---|
| G01 | Exact original state, water, stop, coordinate, and final-frame binding for the route | Repository explorer and event UI owner |
| G02 | Approved persistent travel-custody population contract and complete Deaths attribution | Shared population, migration, and Deaths owners |
| G03 | Verified urban and industrial fire coverage where wildfire eligibility does not apply | Disaster or existing fire-system owner |
| G04 | Proven immediate war against exact allied or subject controllers under native restrictions | Main implementation agent and runtime reviewer |
| G05 | Verified nearby-unit damage and casualty reconciliation | Main implementation agent and shared casualty owner |
| G06 | Exact technology targets and modifier support for rewards and trials | Technology graph review |
| G07 | Actual canonical asset references, templates, original map files, and finished processed art | Asset specialists and UI owner |
| G08 | Dedicated MTTH rules and full probability/AI sequence evidence | Probability auditor |
| G09 | Researched final super-event text and licensed audio | Super-event text and audio researchers |
| G10 | Authoritative workbook update, independent completion review, and applicable live evidence | Workbook owner, completion auditor, and user-authorised playtest workflow |

These gates are not evidence that the requested design should be reduced. They identify the precise source and implementation work that remains before anyone can claim the event has been completed.
