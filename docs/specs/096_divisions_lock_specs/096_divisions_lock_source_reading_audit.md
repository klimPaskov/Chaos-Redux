# Event 096 Divisions Lock source-reading audit

## 1. Gate disposition and evidence boundaries

The complete supplied-source reading gate passed before substantive Event 096 planning and repository research.
The parent personally read and processed all reading pages `001` through `069`, including the complete shared blocks and every differing older and newer source block.
This semantic completion is recorded in `source_gate/parent_progress.json` and the final `GATE COMPLETE` entry in `source_gate/parent_instruction_notes.txt`.
The progress ledger contains exactly pages 1 through 69, has no next page, and records the gate as passed for all supplied decoded source contents.

An independently instantiated `chaosx_documentation_curator` performed the bounded structural coverage audit.
That audit directly compared original archive payloads, extracted copies, manifest aliases, chapter source-line content, and reading-page character ranges.
Its mechanical issue list is empty in `source_gate/coverage_audit_data.json`.
Structural reconstruction alone was not treated as semantic reading completion.
The initial curator report correctly left the gate pending while the parent continued its actual reads.
This appendix records the later completed reading state alongside the independent structural findings.

The appendix documents the source set and evidence used for this task.
It does not provide gameplay design, implementation validation, live-game evidence, or an assertion that every file in an external repository was read.
Its inventories identify sources without reproducing their entire contents in the final specification pack.

## 2. Coverage totals

| Measure | Verified total |
| --- | ---: |
| Supplied top-level sources | 26 |
| Top-level standalone text sources | 23 |
| Top-level archives | 3 |
| Archive instances after recursive nested coverage | 5 |
| Archive member records | 111 |
| Text member copies inside archives | 109 |
| Nested archive member records | 2 |
| Total physical text copies | 132 |
| Distinct raw-byte text groups | 90 |
| Source families and complete reading chapters | 49 |
| Families with two source versions | 41 |
| Families with one source version | 8 |
| Role-definition families | 20 |
| Skill families | 19 |
| Reading pages personally processed by the parent | 69 |
| Source lines across all physical text copies | 43,859 |
| Source lines across distinct raw-byte groups | 29,787 |
| Source payload lines displayed in the multiversion stream | 16,384 |
| Shared source payload lines displayed once for both versions | 13,403 |
| Separate payload lines, including single-version chapters | 2,981 |
| Reading-stream characters, including framing | 1,630,686 |

The counts distinguish physical copies, raw-byte groups, and logical source families.
A byte-identical physical duplicate remains inventoried even when the parent reads its verified canonical content once.
A family with different earlier and newer bytes retains both source identities and the complete text of both versions.

## 3. All supplied top-level sources

Every top-level item resolves to a fully read text source or to an archive whose required contents were extracted and fully read.
The filenames below are the actual supplied-copy names, including numeric prefixes and catalog suffixes.
They are not substituted repository filenames.
The `S` identifiers refer to the independently checked groups in `source_gate/manifest.json`.

| No. | Supplied top-level path | Type | Reading-stream association |
| --- | --- | --- | --- |
| 01 | `project_sources/01-subagents.zip` | Archive | Recursive member coverage below |
| 02 | `project_sources/02-chaos-redux-improvement-loop.md` | Standalone text | `S021` in `chaos-redux-improvement-loop.md` |
| 03 | `project_sources/03-chaos-redux-comfyui.md` | Standalone text | `S022` in `chaos-redux-comfyui.md` |
| 04 | `project_sources/04-chaos-redux-decisions-missions.md` | Standalone text | `S023` in `chaos-redux-decisions-missions.md` |
| 05 | `project_sources/05-AGENTS.md` | Standalone text | `S024` in `AGENTS.md` |
| 06 | `project_sources/06-chaos-redux-subagents.md` | Standalone text | `S025` in `chaos-redux-subagents.md` |
| 07 | `project_sources/07-chaos-redux-3d-model-pipeline.md` | Standalone text | `S026` in `chaos-redux-3d-model-pipeline.md` |
| 08 | `project_sources/08-chaos-redux-event-planning.md` | Standalone text | `S027` in `chaos-redux-event-planning.md` |
| 09 | `project_sources/09-chaos-redux-event-assets.md` | Standalone text | `S028` in `chaos-redux-event-assets.md` |
| 10 | `project_sources/10-chaos-redux-events.md` | Standalone text | `S029` in `chaos-redux-events.md` |
| 11 | `project_sources/11-chaosx_dynamic_effects.md` | Standalone text | `S030` in `chaosx_dynamic_effects.md` |
| 12 | `project_sources/12-chaos-redux-scripted-gui.md` | Standalone text | `S031` in `chaos-redux-scripted-gui.md` |
| 13 | `project_sources/13-chaos-redux-frame-animation.md` | Standalone text | `S032` in `chaos-redux-frame-animation.md` |
| 14 | `project_sources/14-chaos-redux-focus-trees.md` | Standalone text | `S033` in `chaos-redux-focus-trees.md` |
| 15 | `project_sources/15-chaos-redux-debug-playtest.md` | Standalone text | `S034` in `chaos-redux-debug-playtest.md` |
| 16 | `project_sources/16-chaos-redux-super-events.md` | Standalone text | `S035` in `chaos-redux-super-events.md` |
| 17 | `project_sources/17-chaos_redux_clusters_catalog-5-.csv` | Standalone text | `S036` in `chaos_redux_clusters_catalog.csv` |
| 18 | `project_sources/18-chaos_redux_scenarios_catalog-5-.csv` | Standalone text | `S037` in `chaos_redux_scenarios_catalog.csv` |
| 19 | `project_sources/19-chaos_redux_events_catalog-5-.csv` | Standalone text | `S038` in `chaos_redux_events_catalog.csv` |
| 20 | `project_sources/20-config.toml` | Standalone text | `S039` in `config.toml` |
| 21 | `project_sources/21-README.md` | Standalone text | `S040` in `README.md` |
| 22 | `project_sources/22-chaosx_dynamic_triggers.md` | Standalone text | `S041` in `chaosx_dynamic_triggers.md` |
| 23 | `project_sources/23-CHAOS_REDUX_MECHANICS.md` | Standalone text | `S042` in `CHAOS_REDUX_MECHANICS.md` |
| 24 | `project_sources/24-all-project-sources.zip` | Archive | Recursive member coverage below |
| 25 | `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | Standalone text | `S043` in `CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` |
| 26 | `upload/all-project-sources(20261008-064315).zip` | Archive | Recursive member coverage below |

## 4. Recursive archive coverage

The audit opened each original top-level archive and enumerated its actual member records.
For nested archives, it opened the nested payload directly from the original parent archive bytes and compared that payload with the extracted nested archive.
It then checked every recursively extracted member against the corresponding original archive payload using direct byte equality.
A listing was not counted as reading completion.
The parent's subsequent full reading of the represented member contents completed the archive reading requirement.

| Archive instance | Origin | Members | Text copies | Nested ZIP members |
| --- | --- | ---: | ---: | ---: |
| `project_sources/01-subagents.zip` | Standalone supplied role archive | 20 | 20 | 0 |
| `project_sources/24-all-project-sources.zip` | Earlier supplied project bundle | 23 | 22 | 1 |
| `project_sources/24-all-project-sources.zip` → `subagents.zip` | Nested role archive from the earlier bundle | 20 | 20 | 0 |
| `upload/all-project-sources(20261008-064315).zip` | Newer uploaded project bundle | 28 | 27 | 1 |
| `upload/all-project-sources(20261008-064315).zip` → `subagents.zip` | Nested role archive from the newer bundle | 20 | 20 | 0 |

All five inventories match the manifest exactly, including archive chains, member order, member names, and uncompressed byte sizes.
The extracted nested archives are at `source_gate/extracted/project_sources/24-all-project-sources/subagents.zip` and `source_gate/extracted/upload/all-project-sources(20261008-064315)/subagents.zip`.
All 109 non-archive member copies decode as UTF-8 text.
The archive inventories contain no directory entries, unclassified binary members, unsafe extraction paths, repeated exact member names, or case-insensitive member-name collisions.

The older standalone role archive and the older nested role archive contain exact duplicate copies of their 20 definitions.
Those copies were not assumed equivalent merely because their basenames match.
Their original bytes were compared directly before being associated with shared canonical groups.
The newer role archive remains separately represented wherever its bytes differ.

## 5. Complete family, role, and skill reading ledger

All 49 families below were fully processed by the parent through the indicated page spans.
The page spans locate each complete family in the reading stream.
The `Full` state means all represented versions, not a selected version or only relevant excerpts.
Every one of the 20 role definitions and every one of the 19 supplied skills is explicitly listed.
A skill being read does not imply that its subject requires a new gameplay system in this event.
A role definition being read does not imply that the role was spawned.

| Chapter | Source family | Kind | Original-content group identifiers | Reading pages | Parent reading |
| --- | --- | --- | --- | --- | --- |
| 01 | `CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | Protocol, guidance, registry, or configuration | `S043` | 001 | Full |
| 02 | `AGENTS.md` | Protocol, guidance, registry, or configuration | `S024`, `S044` | 001 to 004 | Full |
| 03 | `chaos-redux-subagents.md` | Skill | `S025`, `S062` | 004 to 006 | Full |
| 04 | `chaosx_3d_model_pipeline.toml` | Role definition | `S001`, `S071` | 006 to 008 | Full |
| 05 | `chaosx_ai_probability_auditor.toml` | Role definition | `S002`, `S072` | 008 | Full |
| 06 | `chaosx_asset_source_researcher.toml` | Role definition | `S003`, `S073` | 008 | Full |
| 07 | `chaosx_country_package_auditor.toml` | Role definition | `S004`, `S074` | 008 to 009 | Full |
| 08 | `chaosx_decision_mission_auditor.toml` | Role definition | `S005`, `S075` | 009 | Full |
| 09 | `chaosx_documentation_curator.toml` | Role definition | `S006`, `S076` | 009 to 010 | Full |
| 10 | `chaosx_event_completion_auditor.toml` | Role definition | `S007`, `S077` | 010 | Full |
| 11 | `chaosx_event_ui_worker.toml` | Role definition | `S008`, `S078` | 010 | Full |
| 12 | `chaosx_focus_tree_auditor.toml` | Role definition | `S009`, `S079` | 010 to 011 | Full |
| 13 | `chaosx_generated_event_art.toml` | Role definition | `S010`, `S080` | 011 | Full |
| 14 | `chaosx_icon_artist.toml` | Role definition | `S011`, `S081` | 011 | Full |
| 15 | `chaosx_improvement_loop_planner.toml` | Role definition | `S012`, `S082` | 011 to 012 | Full |
| 16 | `chaosx_localisation_auditor.toml` | Role definition | `S013`, `S083` | 012 | Full |
| 17 | `chaosx_portrait_creator.toml` | Role definition | `S014`, `S084` | 012 | Full |
| 18 | `chaosx_repo_explorer.toml` | Role definition | `S015`, `S085` | 012 to 013 | Full |
| 19 | `chaosx_scripted_system_architect.toml` | Role definition | `S016`, `S086` | 013 | Full |
| 20 | `chaosx_skill_maintainer.toml` | Role definition | `S017`, `S087` | 013 | Full |
| 21 | `chaosx_spreadsheet_doc_worker.toml` | Role definition | `S018`, `S088` | 013 to 014 | Full |
| 22 | `chaosx_super_event_audio_researcher.toml` | Role definition | `S019`, `S089` | 014 | Full |
| 23 | `chaosx_super_event_text_researcher.toml` | Role definition | `S020`, `S090` | 014 | Full |
| 24 | `chaos-redux-event-planning.md` | Skill | `S027`, `S051` | 014 to 023 | Full |
| 25 | `chaos-redux-events.md` | Skill | `S029`, `S052` | 023 to 027 | Full |
| 26 | `CHAOS_REDUX_MECHANICS.md` | Protocol, guidance, registry, or configuration | `S042`, `S045` | 027 to 031 | Full |
| 27 | `chaos-redux-decisions-missions.md` | Skill | `S023`, `S049` | 031 to 034 | Full |
| 28 | `chaosx_dynamic_effects.md` | Protocol, guidance, registry, or configuration | `S030`, `S068` | 034 to 036 | Full |
| 29 | `chaosx_dynamic_triggers.md` | Protocol, guidance, registry, or configuration | `S041`, `S069` | 036 | Full |
| 30 | `README.md` | Protocol, guidance, registry, or configuration | `S040`, `S046` | 036 to 037 | Full |
| 31 | `chaos-redux-3d-model-pipeline.md` | Skill | `S026`, `S047` | 037 to 044 | Full |
| 32 | `chaos-redux-comfyui.md` | Skill | `S022` | 044 | Full |
| 33 | `chaos-redux-debug-playtest.md` | Skill | `S034`, `S048` | 044 to 046 | Full |
| 34 | `chaos-redux-event-assets.md` | Skill | `S028`, `S050` | 046 to 052 | Full |
| 35 | `chaos-redux-focus-trees.md` | Skill | `S033`, `S053` | 052 to 056 | Full |
| 36 | `chaos-redux-frame-animation.md` | Skill | `S032`, `S054` | 056 to 058 | Full |
| 37 | `chaos-redux-improvement-loop.md` | Skill | `S021`, `S055` | 058 to 059 | Full |
| 38 | `chaos-redux-mtth.md` | Skill | `S056` | 059 | Full |
| 39 | `chaos-redux-native-raids.md` | Skill | `S057` | 059 | Full |
| 40 | `chaos-redux-save-inspection.md` | Skill | `S058` | 059 to 060 | Full |
| 41 | `chaos-redux-scripted-gui.md` | Skill | `S031`, `S059` | 060 to 061 | Full |
| 42 | `chaos-redux-shared-git-commit.md` | Skill | `S060` | 061 | Full |
| 43 | `chaos-redux-state-ledgers.md` | Skill | `S061` | 061 to 062 | Full |
| 44 | `chaos-redux-super-events.md` | Skill | `S035`, `S063` | 062 to 063 | Full |
| 45 | `chaos-redux-xlsx.md` | Skill | `S064` | 063 | Full |
| 46 | `chaos_redux_clusters_catalog.csv` | Catalog | `S036`, `S065` | 064 | Full |
| 47 | `chaos_redux_events_catalog.csv` | Catalog | `S038`, `S066` | 064 to 067 | Full |
| 48 | `chaos_redux_scenarios_catalog.csv` | Catalog | `S037`, `S067` | 067 to 068 | Full |
| 49 | `config.toml` | Protocol, guidance, registry, or configuration | `S039`, `S070` | 068 to 069 | Full |

There are eight single-version families: the source-reading protocol, comfyui, MTTH, native raids, save inspection, shared git commit, state ledgers, and xlsx.
The earlier comfyui source remains in the stream despite its absence from the newer bundle.
The six skills introduced only in the newer bundle remain represented in full.
All 41 two-version families preserve both their earlier and newer content.

## 6. Exact-byte grouping and decoded-text sharing

### 6.1 Original byte identity

The audit independently enumerated all 132 physical text-copy paths from the actual standalone sources and recursively opened archives.
That path set equals the manifest alias set exactly, with no missing, additional, or multiply declared alias.
For each alias, actual original bytes were compared directly with its declared canonical group bytes.
The audit independently recomputed 90 distinct groups using actual content equality.
No hash-only equivalence assumption was used to establish duplicate identity.
All 90 source identifiers are unique, and all recorded byte sizes and source-line counts match their originals.

The complete physical text copies contain 3,796,965 bytes.
The 90 distinct raw-byte groups contain 2,594,283 bytes.
Repeated names across archive instances are retained as separate provenance paths even when their content belongs to the same exact-byte group.
Family assignment was independently checked after accounting for the supplied top-level numeric prefixes and the `-5-` catalog suffixes.
The resulting family membership matches `source_gate/chapters.json` exactly.
No cross-family merge or source-name collision was found.

### 6.2 Complete shared and differing source blocks

The reading edition displays a verified equal run in full once and explicitly associates it with the line ranges of both source versions.
It displays every differing run separately in full for its own source version.
This is content sharing after exact comparison, not a summary, preview, selective excerpt, or deletion of surrounding context.
A removed older paragraph remains available in its older-version block.
An inserted newer paragraph remains available in its newer-version block.
Blank lines, indentation, spaces, punctuation, code, tables, and CSV contents remain represented in their original decoded line strings.

The audit parsed all chapter framing and source-range labels.
Every shared block equals the corresponding original line strings in both versions.
Every separate block equals the corresponding original line strings in its named version.
For each of the 90 groups, the represented line numbers equal the ordered complete sequence from line 1 through that source's final line, exactly once.
The 583 shared blocks cover 13,403 lines that belong to both represented versions.
There are 1,531 separately labelled blocks, and the complete separately displayed content, including single-version chapters, contributes 2,981 lines.
Together these represent all 29,787 distinct-group source lines while displaying 16,384 source payload lines.
No source context was omitted by the sharing method.

### 6.3 Encoding qualification

The reading stream is lossless for decoded source-line content.
It is not a raw-byte-identical transcription of every original file.
The reading edition normalizes CRLF endings to LF and removes the UTF-8 BOM from catalog text.
CRLF occurs in 64 distinct raw-byte groups and 94 physical text copies.
A UTF-8 BOM occurs in six distinct groups and nine physical copies.
There are no bare CR endings.
The sole source without a final newline is `S043`, the source-reading protocol, and its single-source chapter preserves that absence.

Original BOM and newline bytes remain intact in the original sources and extracted copies, whose byte equality was separately verified.
The gate completion claim concerns all supplied decoded contents, with original encoding bytes preserved and audited separately.
The appendix therefore does not describe the displayed reading edition as byte-identical to every source.

## 7. Page reconstruction and recovery of incomplete output

Every actual page file was compared directly with the exact chapter character slices recorded in `source_gate/pages.json`.
The declared page ranges are contiguous and reconstruct each chapter completely.
Concatenating all 69 page files equals concatenating all 49 reading chapters exactly.
All declared character counts match, with no unlisted or missing chapter or page files.
This structural proof establishes page completeness and provenance independently of the parent's reading ledger.

The parent recorded all incomplete or truncated source-output attempts as not counted toward completion and recovered them before passing the gate.
The ledger specifically records initial oversized output attempts that were later fully recovered and the first page `031` response, which was context-truncated and subsequently reread in full.
Pages `033`, `039`, `059`, and `064` were processed through complete split reads.
The final ledger covers every page from `001` through `069` and records that every older and newer block was read and processed before substantive design or repository research.
No truncated source-output attempt was accepted as a complete source read.

Pages `006`, `011`, `033`, `039`, `059`, and `064` contain exactly 24,000 characters.
All other pages contain fewer than 24,000 characters.
The page size is not itself a claim about whether a tool output was truncated.
The parent's completion record establishes the actual reading state, and the independent audit establishes exact page content and coverage.

The curator personally read the four bounded role and protocol inputs assigned for its audit in chunks below 24,000 characters.
Those inputs were the curator role definition, the multiversion AGENTS chapter, the multiversion subagent-routing chapter, and the supplied source-reading protocol.
The curator mechanically compared the remaining source content for coverage and did not substitute its audit for the parent's personal full reads.

## 8. Authority and supplemental research disclosures

Full reading does not automatically make every catalog entry, old plan, runtime instruction, or historical implementation statement an accepted current design decision.
Explicit current user instructions retain priority over older supplied descriptions.
For this package, the current user brief governs the Peace High membership and the four evolution thresholds of 200, 400, 600, and 800.
The `To Be Reworked` status is retained.
This is a provenance and instruction-priority disclosure, not an additional gameplay proposal.
The package's separate design documents own how the user's brief is developed.

After the supplied-source gate passed, the parent reports supplemental targeted remote repository research and use of offline reference snapshots.
This later investigation is distinct from the complete supplied-source pass.
It does not replace any provided source, change the verified provided-source inventory, or imply that the entire external repository was read.
Exact external files, passages, revisions, and remaining uncertainties belong to the research evidence in the relevant package documents.
The curator did not independently perform or certify that external research.

Installed vanilla documentation is unavailable in the current research environment.
No HOI4 tool names are exposed in the current environment, and this source-reading audit includes no HOI4 MCP inspection, render, comparison, probability, source-lookup, or live engine evidence.
No live-game validation was performed by this audit.
These limits do not retroactively fail the completed supplied-source gate because the inaccessible supporting material was not part of the supplied source set.
They remain relevant limits on later feasibility and implementation validation.

Separate MCP and Subagent Usage Maps are owned by the parent.
They describe required later work and must not be interpreted as proof that every listed tool was called or every listed role was spawned during source reading.
The actual curator delegation reported here was bounded to source coverage and this appendix.

## 9. Evidence index and conclusion

| Evidence record | What it establishes | What it does not establish |
| --- | --- | --- |
| `source_gate/manifest.json` | Original source identities, aliases, sizes, line counts, archive inventories, and nested provenance | Semantic reading by itself |
| `source_gate/chapters.json` | Complete family membership and chapter identities | Acceptance of a design claim |
| `source_gate/pages.json` | Exact page-to-chapter character ranges | Actual processing of tool output |
| `source_gate/parent_progress.json` | Parent completion of all 69 pages, recovered incomplete calls, and semantic processing state | Byte equality without the independent comparisons |
| `source_gate/parent_instruction_notes.txt` | Reading checkpoints and the final completed-gate record | Full external-repository reading |
| `source_gate/coverage_audit_data.json` | Independent structural totals and an empty mechanical issue list | Runtime or implementation validation |
| `source_gate/coverage_audit.md` | Curator's earlier mechanical audit, including the then-pending semantic gate | The later reading state without the parent completion ledger |
| Supplied originals and extracted copies | Complete original bytes retained for direct verification | Automatic correctness or current acceptance of their content |

The supplied-source gate is complete on the combined basis of the parent's full semantic reading and the curator's independent exact coverage verification.
All 26 top-level sources, five recursive archive instances, 132 text copies, 90 raw-byte groups, 49 families, 20 role definitions, and 19 skills are accounted for.
No archive-member, source-copy, source-version, source-line, chapter, or page omission remains in the supplied-source coverage audit.
Encoding normalization and later external research limits remain explicitly disclosed.
