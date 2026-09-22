# Sources and reading register

## Scope of the claim

All 42 supplied text files were read in full, including all 20 supplied subagent definitions.
The remaining-content reading pass omitted only exact text already read elsewhere and was traversed completely.
That pass was not a summary of unread sections.
The SHA-256 manifest identifies each source and the uploaded archive.

The separate requirement to read every externally referenced must-read file could not be completed.
The local installed game, every linked offline-wiki article, the full repository, the asset reference library, and some referenced shared implementation files were not available or were not read in full.
Those gaps remain explicit below.
No independent subagent was executed and no live HOI4 or HOI4 MCP validation was performed.

The user brief in this conversation is authoritative for the new Event 074 design.
The supplied project rules govern its packaging and integration.
Repository excerpts establish limited existing-code facts and must not be promoted into evidence that a new engine behavior is tested.

## Supplied source inventory

| Source | Bytes | Reading status |
| --- | ---: | --- |
| `chaos-redux-subagents.md` | 41,493 | Fully read |
| `chaos-redux-event-planning.md` | 197,109 | Fully read |
| `chaos-redux-3d-model-pipeline.md` | 96,728 | Fully read |
| `chaos-redux-events.md` | 80,791 | Fully read |
| `chaos-redux-decisions-missions.md` | 64,394 | Fully read |
| `chaos-redux-event-assets.md` | 109,712 | Fully read |
| `chaos-redux-improvement-loop.md` | 28,515 | Fully read |
| `chaos-redux-comfyui.md` | 2,456 | Fully read |
| `chaos-redux-debug-playtest.md` | 34,086 | Fully read |
| `chaos-redux-scripted-gui.md` | 23,695 | Fully read |
| `chaos-redux-super-events.md` | 33,489 | Fully read |
| `chaos-redux-focus-trees.md` | 98,951 | Fully read |
| `chaos-redux-frame-animation.md` | 28,266 | Fully read |
| `chaosx_dynamic_effects.md` | 19,635 | Fully read |
| `chaos_redux_clusters_catalog.csv` | 5,362 | Fully read |
| `chaos_redux_events_catalog.csv` | 65,053 | Fully read |
| `chaos_redux_scenarios_catalog.csv` | 16,848 | Fully read |
| `CHAOS_REDUX_MECHANICS.md` | 41,848 | Fully read |
| `README.md` | 2,857 | Fully read |
| `config.toml` | 11,714 | Fully read |
| `chaosx_dynamic_triggers.md` | 3,991 | Fully read |
| `AGENTS.md` | 44,442 | Fully read |
| `subagents.zip/chaosx_3d_model_pipeline.toml` | 27,552 | Fully read |
| `subagents.zip/chaosx_ai_probability_auditor.toml` | 6,414 | Fully read |
| `subagents.zip/chaosx_asset_source_researcher.toml` | 3,024 | Fully read |
| `subagents.zip/chaosx_country_package_auditor.toml` | 8,099 | Fully read |
| `subagents.zip/chaosx_decision_mission_auditor.toml` | 8,994 | Fully read |
| `subagents.zip/chaosx_documentation_curator.toml` | 11,319 | Fully read |
| `subagents.zip/chaosx_event_completion_auditor.toml` | 4,141 | Fully read |
| `subagents.zip/chaosx_event_ui_worker.toml` | 10,136 | Fully read |
| `subagents.zip/chaosx_focus_tree_auditor.toml` | 4,480 | Fully read |
| `subagents.zip/chaosx_generated_event_art.toml` | 3,930 | Fully read |
| `subagents.zip/chaosx_icon_artist.toml` | 10,096 | Fully read |
| `subagents.zip/chaosx_improvement_loop_planner.toml` | 7,229 | Fully read |
| `subagents.zip/chaosx_localisation_auditor.toml` | 9,782 | Fully read |
| `subagents.zip/chaosx_portrait_creator.toml` | 2,049 | Fully read |
| `subagents.zip/chaosx_repo_explorer.toml` | 13,488 | Fully read |
| `subagents.zip/chaosx_scripted_system_architect.toml` | 5,388 | Fully read |
| `subagents.zip/chaosx_skill_maintainer.toml` | 3,258 | Fully read |
| `subagents.zip/chaosx_spreadsheet_doc_worker.toml` | 4,605 | Fully read |
| `subagents.zip/chaosx_super_event_audio_researcher.toml` | 3,342 | Fully read |
| `subagents.zip/chaosx_super_event_text_researcher.toml` | 3,921 | Fully read |

The manifest includes only source names, sizes, hashes, and reading status.
It does not redistribute the supplied configuration contents or the nested source archive.

## Additional repository sources read in full

Repository: `klimPaskov/Chaos-Redux`.
Search results referenced commit `879b3007d3b6bf75c726c11635473fccda45c569`.
The existing event was fetched from the default branch and is identified below by its observed blob SHA.
Do not assume the repository remains at that snapshot when implementation starts.

### R01. Existing Event 074

Path: `events/074_japan_california.txt`.
Observed blob SHA: `0aec45e87e66eab74057c2bc1fc66f0f5115a3aa`.
Read in full.

It preserves the root `chaosx.nr74.1`, grants state 378 through `transfer_state_to = JAP`, defines a twelve-infantry-battalion template with support companies, and creates twelve divisions.
It sends report `chaosx.nr74.2` and news `chaosx.news.65`.
The report acknowledgement adds war support.
These are facts about the inspected old implementation, not the new specification.
The rework must replace ownership transfer with proven wartime-control behavior and make material effects independent of report acknowledgement.

Source: https://github.com/klimPaskov/Chaos-Redux/blob/master/events/074_japan_california.txt

### R02. Portal Raider API documentation

Path: `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`.
Pinned blob SHA: `4c6c0f302ce032e4f21e72f26dda7710a09f86a3`.
Read in full at the search-referenced commit.

The documented transaction uses a captured province, an actual created formation, a completion receipt and bounded beachhead registries.
The document warns that the known `teleport_armies` effect operates over a state with an owner filter, which can affect unrelated formations.
This is a repository design precedent and a warning against broad movement effects.
It does not prove that a defended multi-province Event 074 landing is already safe.

Source: https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/docs/events/016_brilliant_scientist/systems/portal_raider_api.md

### R03. MTTH skill

Path: `.agents/skills/chaos-redux-mtth/SKILL.md`.
Pinned blob SHA: `7d86c0fe166a23264fcb2a9f512994977f372a80`.
Read in full at the search-referenced commit.

This skill defines MTTH-backed values and requires the probability auditor's inspection, scenario evaluation, sweep, simulation and comparison workflow.
Its referenced `common/mtth/chaosx_mtth_variables.txt` was not read in full in this session.

Source: https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/.agents/skills/chaos-redux-mtth/SKILL.md

## Partial repository inspection

The offline `paradox_wiki` directory was listed.
Its full article collection was not read.
Keyword results exposed a `set_province_controller` entry in the Effects article and its use in Event 016, but those searches were excerpts.
Searches also exposed `local_supplies` and `local_supplies_for_controller` in famine, zombie, chemical, and death modifier files.
These excerpts identify candidate capability surfaces, not their verified numerical behavior or safe use in partially controlled states.

The Event 074 English localisation and shared news files were inspected through matching excerpts only.
The full dispatcher, shared event log, settings, cluster routing, native unit manifests, air variants, state histories, and achievement registry still require implementation-stage reading.

## Catalog snapshots and authority

The supplied `chaos_redux_events_catalog.csv` contains the older sparse Event 074 row.
The supplied cluster export does not establish the new Wars Medium assignment as implemented.
The present user brief explicitly sets Wars as the cluster and Medium as the member role.
No supplied CSV was changed in this session.

The editable source of truth for implementation is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
The CSV is an exported snapshot.
After the final player-facing wording and verified mechanics exist, the spreadsheet specialist must update the authoritative workbook and use `.tools/export_event_catalog_csv.py` to regenerate the export.
Do not write speculative final localisation or a completion status into the CSV directly.
The scenario catalog is background context and no new scenario is requested here.

## Limited external primary research

The National Park Service page for Rosie the Riveter/WWII Home Front was opened and read.
It describes Richmond, California's Kaiser shipyards and Liberty and Victory ship construction, which provide useful reference directions for port and industrial-home-front imagery.
That history supports visual research and does not establish that this fictional Japanese invasion was historically feasible.

Source: https://www.nps.gov/rori/learn/historyculture/index.htm
Page update shown: January 22, 2025.

The National Park Service Fort Mason page was also read.
Its harbor geography can inform research into Bay Area approaches.
The inspected page emphasizes earlier history and must not be cited for unverified WWII embarkation totals.

Source: https://www.nps.gov/goga/learn/historyculture/fort-mason.htm
Page update shown: July 10, 2019.

A surfaced Fort Stevens page concerned Washington, DC, not the Oregon coastal fort, and was excluded.
No quotation, song, historical speaker, or final super-event title was selected from these searches.
Fictional campaign artwork must not be labeled an authentic photograph of the event.

## External must-read and evidence gaps

| Missing or incomplete dependency | Required next action |
| --- | --- |
| Installed vanilla game, current map and supported DLC files | Read exact unit, equipment, province, state, building, air and AI consumers before implementation |
| Relevant full offline-wiki articles | Read complete Effects, AI modding, unit creation, supply, building, character and decision references that the chosen implementation actually uses |
| Shared repository dispatcher, event log, settings, clusters and catalog workbook | Inspect exact current APIs and update only through their owners |
| Native asset reference library and contact sheets | Read root indexes and each requested family before visual production |
| Executable subagent interface | Run the supplied roles with context-complete prompts and no inherited-context assumption |
| HOI4 event, map, technology and probability tools | Produce the specified inspection and comparison evidence where supported |
| Live HOI4 testing | Run or request the precise reproducible cases according to the debug-playtest skill and current user authority |
| Super-event text, quotation and audio rights | Complete specialist research and approval before final localisation and registration |

The specifications were not intentionally shortened into a quick-output outline.
They provide the full planned design and handoff while preserving unresolved technical and research gates.
Final localisation, final assets, working code and live tests were not produced because this is a plan-only package.
Unavailable references and independent reviews must remain visible in the implementation completion report.
