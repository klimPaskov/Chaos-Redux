# Event 101 Tasks: Project Source coverage appendix

## 1. Verified result and scope

**The mandatory Project Source gate passed with no missing content groups and no unresolved verification issues.** The independent verification completed on **9 October 2026 at 19:25:29 UTC**. This appendix records that completed gate for the Event 101 Tasks specification package. It was assembled from the existing inventory, four reader ledgers, and saved verification report. Creating this appendix did not restart the gate or reread the source collection.

The reading was distributed among four actual collaborators. Each distinct content version was read completely by its attributed reader. Additional paths with identical content received complete coverage through direct comparison of their entire original byte arrays with the read representative. The tables below distinguish the representative from those identical copies.

| Measure | Verified total |
| --- | --- |
| Distinct content groups | 91 |
| Supplied and extracted text paths | 133 |
| Additional identical text copies | 42 |
| Bytes across distinct representatives | 2,601,810 |
| Bytes across all text paths, including identical copies | 3,804,492 |
| Counted complete semantic reading chunks | 199 |
| Archives, including nested archives | 5 |
| Archive member entries | 111 |
| Top-level supplied inputs | 27 |
| Missing groups | 0 |
| Unresolved verification issues | 0 |

The 111 archive member entries comprise 109 text entries and two nested ZIP entries. The 27 top-level inputs comprise 24 text files and three ZIP files. The 109 extracted text paths plus the 24 top-level text paths account for all 133 text paths. Archive containers are accounted for separately and do not inflate the text-group count.

## 2. Distributed reader attribution

| Reader | Actual collaborator | Groups | Text paths | Chunks | Representative bytes |
| --- | --- | --- | --- | --- | --- |
| Root | `/root` | 8 | 9 | 41 | 806,858 |
| Gameplay reader | `/root/source_gameplay` | 20 | 27 | 59 | 736,340 |
| Assets reader | `/root/source_assets` | 10 | 17 | 32 | 484,055 |
| Agents reader | `/root/source_agents` | 53 | 80 | 67 | 574,557 |
| Total | Four actual collaborators | 91 | 133 | 199 | 2,601,810 |

The counted attribution uses one complete primary reading record per group. Supplemental protocol readings and additional rereads do not increase these totals. The root collaborator is attributed only to its eight primary groups. Groups G26, G29, and G32 were explicitly transferred unread by the assets reader and then fully read by root. Their coverage belongs to root in every table below.

## 3. Source identity, reading method, and range conventions

Readers processed the complete representative text through bounded tool outputs and recorded successful reading ranges. The independent aggregation then checked the complete original bytes of every supplied or extracted text path against its representative. It also checked each representative against the inventory byte count, line count, and SHA-256. A hash was an inventory integrity check, not a substitute for direct byte comparison or semantic reading.

For archives, every recorded member name was checked against the ZIP member list. Each member was decompressed and its complete resulting bytes were compared directly with the extracted file. Every text member was mapped to a covered content group. Both nested ZIP members were linked to their separately inventoried and fully accounted-for archives.

For the gameplay, assets, and agents readers, reading intervals use original bytes with a zero-based inclusive start and exclusive end. Their line intervals use one-based inclusive endpoints. The verification checked exact line-to-byte boundaries, contiguous coverage, and reconstruction of the original complete byte sequence. Root used Unicode character intervals. Its saved payloads were compared with the corresponding complete source text under the actual newline convention of each group, then mapped back to original byte boundaries.

Notation in this appendix is `B[start,end)` for original bytes, `C[start,end)` for Unicode characters, and `Lfirst–last` for inclusive line numbers. Every group covers the whole source from original byte zero through its stated byte length. Root character counts and original byte counts differ where UTF-8 uses multiple bytes per character or newline normalization removes carriage returns.

| Root group | Complete displayed character coverage | Complete original byte coverage | Verified newline basis |
| --- | --- | --- | --- |
| G06 | `C[0,197107)` | `B[0,197109)` | Original characters preserved. Raw and normalized text are identical. |
| G22 | `C[0,12712)` | `B[0,12728)` | Original characters preserved. Raw and normalized text are identical. |
| G24 | `C[0,55501)` | `B[0,55586)` | Original characters preserved. Raw and normalized text are identical. |
| G26 | `C[0,115625)` | `B[0,116242)` | Universal newline normalization. CRLF and CR become LF. |
| G29 | `C[0,116310)` | `B[0,117335)` | Universal newline normalization. CRLF and CR become LF. |
| G30 | `C[0,200866)` | `B[0,200868)` | Original newline characters preserved, including CRLF. |
| G32 | `C[0,97974)` | `B[0,99463)` | Universal newline normalization. CRLF and CR become LF. |
| G90 | `C[0,7527)` | `B[0,7527)` | Original characters preserved. Raw and normalized text are identical. |

The original-byte reconstruction for normalized root chunks used the observed source newline map. It did not assume that normalized text alone can recover the original distinction between LF and CRLF. Group G30 was verified using preserved newline characters, correcting the initial general description that all root chunks used universal newline normalization.

### Repaired clipped outputs

| Reader | Affected material | Repair and final status |
| --- | --- | --- |
| Root | G30, current supplied event-planning source | An earlier combined display of characters 0:44000 clipped. The two final 22000-character chunks were reread separately. Root explicitly attested that all final chunks were semantically read and untruncated. |
| Assets reader | G33, current supplied frame-animation source | An earlier display clipped. Both final chunks were reread completely. The final ledger marks both chunks as reread after clipping and untruncated. |
| Gameplay reader | Initial inventory metadata display | A broad metadata output clipped. All assigned inventory group records were displayed separately without clipping. No source-content reading range was affected. |

The 199 counted records refer to the successful complete readings. Failed or clipped attempts do not receive additional reading credit. Gameplay, assets, and agents final chunk records explicitly record no truncation. Root completeness and lack of final truncation are supported by its direct attestation and the exact payload coverage checks.

### Version labels

| Label used below | Supplied provenance | Meaning |
| --- | --- | --- |
| Current supplied archive | `upload/all-project-sources(20261009-191148).zip` | Extracted to `source_gate/current/`. This label distinguishes the supplied archive version. |
| Project archive version | `project_sources/24-all-project-sources.zip` | Extracted to `source_gate/project_archive/`. Its distinct source versions remain separate from current supplied versions. |
| Standalone project sources | `project_sources/02-*` through `project_sources/23-*` | Original top-level text inputs. Their archive counterparts are listed as identical copies only where complete bytes matched. |
| Standalone agent definitions | `project_sources/01-subagents.zip` | Extracted to `source_gate/standalone_subagents/`. Its 20 definitions match the corresponding project archive definitions byte for byte. |
| Project Source protocol | `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | Separate top-level protocol input, covered as G22. |
| Event 101 task brief | `upload/101 - Tasks(1).md` | Separate top-level event brief, covered as G90. |

Groups G50–G69 contain 20 current supplied agent-definition versions. Groups G70–G89 contain 20 distinct project archive versions with the same family of filenames. Each of those latter groups also includes its identical standalone archive copy. This accounts for **40 distinct agent-definition content groups and 60 agent-definition text paths**. The definitions were treated as supplied source text and fully read, regardless of whether a named project agent was available for execution.

## 4. Exhaustive content-group and text-path mapping

Every path in the following tables has complete content coverage. **R** identifies the semantically read representative. **C** identifies an additional supplied or extracted path whose entire bytes matched that representative. A group can contain multiple paths, but its content is counted once. Paths are relative provenance labels without the temporary workspace prefix.

### 4.1 Standalone and project archive source documents, G00–G21

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G00 | Gameplay reader | Complete<br>`L1–289`<br>`B[0,28515)`<br>2 chunks | **R** `project_sources/02-chaos-redux-improvement-loop.md`<br>**C** `source_gate/project_archive/chaos-redux-improvement-loop.md` |
| G01 | Assets reader | Complete<br>`L1–21`<br>`B[0,2456)`<br>1 chunk | **R** `project_sources/03-chaos-redux-comfyui.md`<br>**C** `source_gate/project_archive/chaos-redux-comfyui.md` |
| G02 | Gameplay reader | Complete<br>`L1–1022`<br>`B[0,64394)`<br>5 chunks | **R** `project_sources/04-chaos-redux-decisions-missions.md`<br>**C** `source_gate/project_archive/chaos-redux-decisions-missions.md` |
| G03 | Agents reader | Complete<br>`L1–431`<br>`B[0,44442)`<br>3 chunks | **R** `project_sources/05-AGENTS.md`<br>**C** `source_gate/project_archive/AGENTS.md` |
| G04 | Agents reader | Complete<br>`L1–366`<br>`B[0,41493)`<br>3 chunks | **R** `project_sources/06-chaos-redux-subagents.md`<br>**C** `source_gate/project_archive/chaos-redux-subagents.md` |
| G05 | Assets reader | Complete<br>`L1–477`<br>`B[0,96728)`<br>6 chunks | **R** `project_sources/07-chaos-redux-3d-model-pipeline.md`<br>**C** `source_gate/project_archive/chaos-redux-3d-model-pipeline.md` |
| G06 | Root | Complete<br>`L1–2297`<br>`B[0,197109)`<br>9 chunks | **R** `project_sources/08-chaos-redux-event-planning.md`<br>**C** `source_gate/project_archive/chaos-redux-event-planning.md` |
| G07 | Assets reader | Complete<br>`L1–1004`<br>`B[0,109712)`<br>7 chunks | **R** `project_sources/09-chaos-redux-event-assets.md`<br>**C** `source_gate/project_archive/chaos-redux-event-assets.md` |
| G08 | Gameplay reader | Complete<br>`L1–833`<br>`B[0,80791)`<br>6 chunks | **R** `project_sources/10-chaos-redux-events.md`<br>**C** `source_gate/project_archive/chaos-redux-events.md` |
| G09 | Gameplay reader | Complete<br>`L1–328`<br>`B[0,19635)`<br>2 chunks | **R** `project_sources/11-chaosx_dynamic_effects.md`<br>**C** `source_gate/project_archive/chaosx_dynamic_effects.md` |
| G10 | Assets reader | Complete<br>`L1–130`<br>`B[0,23695)`<br>2 chunks | **R** `project_sources/12-chaos-redux-scripted-gui.md`<br>**C** `source_gate/project_archive/chaos-redux-scripted-gui.md` |
| G11 | Assets reader | Complete<br>`L1–501`<br>`B[0,28266)`<br>2 chunks | **R** `project_sources/13-chaos-redux-frame-animation.md`<br>**C** `source_gate/project_archive/chaos-redux-frame-animation.md` |
| G12 | Assets reader | Complete<br>`L1–1505`<br>`B[0,98951)`<br>6 chunks | **R** `project_sources/14-chaos-redux-focus-trees.md`<br>**C** `source_gate/project_archive/chaos-redux-focus-trees.md` |
| G13 | Gameplay reader | Complete<br>`L1–698`<br>`B[0,34086)`<br>3 chunks | **R** `project_sources/15-chaos-redux-debug-playtest.md`<br>**C** `source_gate/project_archive/chaos-redux-debug-playtest.md` |
| G14 | Assets reader | Complete<br>`L1–787`<br>`B[0,33489)`<br>2 chunks | **R** `project_sources/16-chaos-redux-super-events.md`<br>**C** `source_gate/project_archive/chaos-redux-super-events.md` |
| G15 | Agents reader | Complete<br>`L1–20`<br>`B[0,5362)`<br>1 chunk | **R** `project_sources/17-chaos_redux_clusters_catalog-5-.csv`<br>**C** `source_gate/project_archive/chaos_redux_clusters_catalog.csv` |
| G16 | Agents reader | Complete<br>`L1–120`<br>`B[0,16848)`<br>2 chunks | **R** `project_sources/18-chaos_redux_scenarios_catalog-5-.csv`<br>**C** `source_gate/project_archive/chaos_redux_scenarios_catalog.csv` |
| G17 | Gameplay reader | Complete<br>`L1–294`<br>`B[0,65053)`<br>5 chunks | **R** `project_sources/19-chaos_redux_events_catalog-5-.csv`<br>**C** `source_gate/project_archive/chaos_redux_events_catalog.csv` |
| G18 | Agents reader | Complete<br>`L1–192`<br>`B[0,11714)`<br>1 chunk | **R** `project_sources/20-config.toml`<br>**C** `source_gate/project_archive/config.toml` |
| G19 | Agents reader | Complete<br>`L1–42`<br>`B[0,2857)`<br>1 chunk | **R** `project_sources/21-README.md`<br>**C** `source_gate/project_archive/README.md` |
| G20 | Agents reader | Complete<br>`L1–61`<br>`B[0,3991)`<br>1 chunk | **R** `project_sources/22-chaosx_dynamic_triggers.md`<br>**C** `source_gate/project_archive/chaosx_dynamic_triggers.md` |
| G21 | Gameplay reader | Complete<br>`L1–855`<br>`B[0,41848)`<br>3 chunks | **R** `project_sources/23-CHAOS_REDUX_MECHANICS.md`<br>**C** `source_gate/project_archive/CHAOS_REDUX_MECHANICS.md` |

### 4.2 Project Source protocol, G22

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G22 | Root | Complete<br>`L1–373`<br>`B[0,12728)`<br>1 chunk | **R** `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` |

### 4.3 Current supplied source documents and catalogs, G23–G49

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G23 | Agents reader | Complete<br>`L1–448`<br>`B[0,48552)`<br>4 chunks | **R** `source_gate/current/AGENTS.md` |
| G24 | Root | Complete<br>`L1–1023`<br>`B[0,55586)`<br>3 chunks | **R** `source_gate/current/CHAOS_REDUX_MECHANICS.md` |
| G25 | Agents reader | Complete<br>`L1–39`<br>`B[0,2650)`<br>1 chunk | **R** `source_gate/current/README.md` |
| G26 | Root | Complete<br>`L1–597`<br>`B[0,116242)`<br>6 chunks | **R** `source_gate/current/chaos-redux-3d-model-pipeline.md` |
| G27 | Gameplay reader | Complete<br>`L1–701`<br>`B[0,35963)`<br>3 chunks | **R** `source_gate/current/chaos-redux-debug-playtest.md` |
| G28 | Gameplay reader | Complete<br>`L1–1082`<br>`B[0,77650)`<br>5 chunks | **R** `source_gate/current/chaos-redux-decisions-missions.md` |
| G29 | Root | Complete<br>`L1–1038`<br>`B[0,117335)`<br>6 chunks | **R** `source_gate/current/chaos-redux-event-assets.md` |
| G30 | Root | Complete<br>`L1–2287`<br>`B[0,200868)`<br>10 chunks | **R** `source_gate/current/chaos-redux-event-planning.md` |
| G31 | Gameplay reader | Complete<br>`L1–971`<br>`B[0,100605)`<br>7 chunks | **R** `source_gate/current/chaos-redux-events.md` |
| G32 | Root | Complete<br>`L1–1489`<br>`B[0,99463)`<br>5 chunks | **R** `source_gate/current/chaos-redux-focus-trees.md` |
| G33 | Assets reader | Complete<br>`L1–501`<br>`B[0,29504)`<br>2 chunks | **R** `source_gate/current/chaos-redux-frame-animation.md` |
| G34 | Gameplay reader | Complete<br>`L1–287`<br>`B[0,28767)`<br>2 chunks | **R** `source_gate/current/chaos-redux-improvement-loop.md` |
| G35 | Gameplay reader | Complete<br>`L1–69`<br>`B[0,2383)`<br>1 chunk | **R** `source_gate/current/chaos-redux-mtth.md` |
| G36 | Gameplay reader | Complete<br>`L1–37`<br>`B[0,4821)`<br>1 chunk | **R** `source_gate/current/chaos-redux-native-raids.md` |
| G37 | Gameplay reader | Complete<br>`L1–93`<br>`B[0,8139)`<br>1 chunk | **R** `source_gate/current/chaos-redux-save-inspection.md` |
| G38 | Assets reader | Complete<br>`L1–145`<br>`B[0,28241)`<br>2 chunks | **R** `source_gate/current/chaos-redux-scripted-gui.md` |
| G39 | Gameplay reader | Complete<br>`L1–33`<br>`B[0,6515)`<br>1 chunk | **R** `source_gate/current/chaos-redux-shared-git-commit.md` |
| G40 | Gameplay reader | Complete<br>`L1–106`<br>`B[0,14609)`<br>1 chunk | **R** `source_gate/current/chaos-redux-state-ledgers.md` |
| G41 | Agents reader | Complete<br>`L1–425`<br>`B[0,55946)`<br>4 chunks | **R** `source_gate/current/chaos-redux-subagents.md` |
| G42 | Assets reader | Complete<br>`L1–771`<br>`B[0,33013)`<br>2 chunks | **R** `source_gate/current/chaos-redux-super-events.md` |
| G43 | Gameplay reader | Complete<br>`L1–75`<br>`B[0,5309)`<br>1 chunk | **R** `source_gate/current/chaos-redux-xlsx.md` |
| G44 | Agents reader | Complete<br>`L1–20`<br>`B[0,5232)`<br>1 chunk | **R** `source_gate/current/chaos_redux_clusters_catalog.csv` |
| G45 | Gameplay reader | Complete<br>`L1–288`<br>`B[0,63141)`<br>5 chunks | **R** `source_gate/current/chaos_redux_events_catalog.csv` |
| G46 | Agents reader | Complete<br>`L1–135`<br>`B[0,18229)`<br>2 chunks | **R** `source_gate/current/chaos_redux_scenarios_catalog.csv` |
| G47 | Gameplay reader | Complete<br>`L1–582`<br>`B[0,49370)`<br>4 chunks | **R** `source_gate/current/chaosx_dynamic_effects.md` |
| G48 | Gameplay reader | Complete<br>`L1–63`<br>`B[0,4746)`<br>1 chunk | **R** `source_gate/current/chaosx_dynamic_triggers.md` |
| G49 | Agents reader | Complete<br>`L1–224`<br>`B[0,12647)`<br>1 chunk | **R** `source_gate/current/config.toml` |

### 4.4 Current supplied agent definitions, G50–G69

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G50 | Agents reader | Complete<br>`L1–198`<br>`B[0,28417)`<br>2 chunks | **R** `source_gate/current/subagents_extracted/chaosx_3d_model_pipeline.toml` |
| G51 | Agents reader | Complete<br>`L1–66`<br>`B[0,6412)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_ai_probability_auditor.toml` |
| G52 | Agents reader | Complete<br>`L1–58`<br>`B[0,3019)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_asset_source_researcher.toml` |
| G53 | Agents reader | Complete<br>`L1–86`<br>`B[0,8021)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_country_package_auditor.toml` |
| G54 | Agents reader | Complete<br>`L1–100`<br>`B[0,8992)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_decision_mission_auditor.toml` |
| G55 | Agents reader | Complete<br>`L1–134`<br>`B[0,11319)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_documentation_curator.toml` |
| G56 | Agents reader | Complete<br>`L1–66`<br>`B[0,4141)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_event_completion_auditor.toml` |
| G57 | Agents reader | Complete<br>`L1–90`<br>`B[0,10134)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_event_ui_worker.toml` |
| G58 | Agents reader | Complete<br>`L1–80`<br>`B[0,4478)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_focus_tree_auditor.toml` |
| G59 | Agents reader | Complete<br>`L1–72`<br>`B[0,3925)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_generated_event_art.toml` |
| G60 | Agents reader | Complete<br>`L1–128`<br>`B[0,10864)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_icon_artist.toml` |
| G61 | Agents reader | Complete<br>`L1–61`<br>`B[0,7229)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_improvement_loop_planner.toml` |
| G62 | Agents reader | Complete<br>`L1–111`<br>`B[0,9782)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_localisation_auditor.toml` |
| G63 | Agents reader | Complete<br>`L1–22`<br>`B[0,2509)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_portrait_creator.toml` |
| G64 | Agents reader | Complete<br>`L1–235`<br>`B[0,13486)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_repo_explorer.toml` |
| G65 | Agents reader | Complete<br>`L1–74`<br>`B[0,5388)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_scripted_system_architect.toml` |
| G66 | Agents reader | Complete<br>`L1–45`<br>`B[0,3258)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_skill_maintainer.toml` |
| G67 | Agents reader | Complete<br>`L1–60`<br>`B[0,4714)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_spreadsheet_doc_worker.toml` |
| G68 | Agents reader | Complete<br>`L1–65`<br>`B[0,3340)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_super_event_audio_researcher.toml` |
| G69 | Agents reader | Complete<br>`L1–62`<br>`B[0,3919)`<br>1 chunk | **R** `source_gate/current/subagents_extracted/chaosx_super_event_text_researcher.toml` |

### 4.5 Project archive and standalone agent definitions, G70–G89

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G70 | Agents reader | Complete<br>`L1–197`<br>`B[0,27552)`<br>2 chunks | **R** `source_gate/project_archive/subagents_extracted/chaosx_3d_model_pipeline.toml`<br>**C** `source_gate/standalone_subagents/chaosx_3d_model_pipeline.toml` |
| G71 | Agents reader | Complete<br>`L1–66`<br>`B[0,6414)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_ai_probability_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_ai_probability_auditor.toml` |
| G72 | Agents reader | Complete<br>`L1–58`<br>`B[0,3024)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_asset_source_researcher.toml`<br>**C** `source_gate/standalone_subagents/chaosx_asset_source_researcher.toml` |
| G73 | Agents reader | Complete<br>`L1–87`<br>`B[0,8099)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_country_package_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_country_package_auditor.toml` |
| G74 | Agents reader | Complete<br>`L1–100`<br>`B[0,8994)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_decision_mission_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_decision_mission_auditor.toml` |
| G75 | Agents reader | Complete<br>`L1–134`<br>`B[0,11319)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_documentation_curator.toml`<br>**C** `source_gate/standalone_subagents/chaosx_documentation_curator.toml` |
| G76 | Agents reader | Complete<br>`L1–66`<br>`B[0,4141)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_event_completion_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_event_completion_auditor.toml` |
| G77 | Agents reader | Complete<br>`L1–90`<br>`B[0,10136)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_event_ui_worker.toml`<br>**C** `source_gate/standalone_subagents/chaosx_event_ui_worker.toml` |
| G78 | Agents reader | Complete<br>`L1–80`<br>`B[0,4480)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_focus_tree_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_focus_tree_auditor.toml` |
| G79 | Agents reader | Complete<br>`L1–72`<br>`B[0,3930)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_generated_event_art.toml`<br>**C** `source_gate/standalone_subagents/chaosx_generated_event_art.toml` |
| G80 | Agents reader | Complete<br>`L1–117`<br>`B[0,10096)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_icon_artist.toml`<br>**C** `source_gate/standalone_subagents/chaosx_icon_artist.toml` |
| G81 | Agents reader | Complete<br>`L1–61`<br>`B[0,7229)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_improvement_loop_planner.toml`<br>**C** `source_gate/standalone_subagents/chaosx_improvement_loop_planner.toml` |
| G82 | Agents reader | Complete<br>`L1–111`<br>`B[0,9782)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_localisation_auditor.toml`<br>**C** `source_gate/standalone_subagents/chaosx_localisation_auditor.toml` |
| G83 | Agents reader | Complete<br>`L1–20`<br>`B[0,2049)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_portrait_creator.toml`<br>**C** `source_gate/standalone_subagents/chaosx_portrait_creator.toml` |
| G84 | Agents reader | Complete<br>`L1–235`<br>`B[0,13488)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_repo_explorer.toml`<br>**C** `source_gate/standalone_subagents/chaosx_repo_explorer.toml` |
| G85 | Agents reader | Complete<br>`L1–74`<br>`B[0,5388)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_scripted_system_architect.toml`<br>**C** `source_gate/standalone_subagents/chaosx_scripted_system_architect.toml` |
| G86 | Agents reader | Complete<br>`L1–45`<br>`B[0,3258)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_skill_maintainer.toml`<br>**C** `source_gate/standalone_subagents/chaosx_skill_maintainer.toml` |
| G87 | Agents reader | Complete<br>`L1–59`<br>`B[0,4605)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_spreadsheet_doc_worker.toml`<br>**C** `source_gate/standalone_subagents/chaosx_spreadsheet_doc_worker.toml` |
| G88 | Agents reader | Complete<br>`L1–65`<br>`B[0,3342)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_super_event_audio_researcher.toml`<br>**C** `source_gate/standalone_subagents/chaosx_super_event_audio_researcher.toml` |
| G89 | Agents reader | Complete<br>`L1–62`<br>`B[0,3921)`<br>1 chunk | **R** `source_gate/project_archive/subagents_extracted/chaosx_super_event_text_researcher.toml`<br>**C** `source_gate/standalone_subagents/chaosx_super_event_text_researcher.toml` |

### 4.6 Event 101 task brief, G90

| Group | Attributed reader | Complete source coverage | All text paths in the group |
| --- | --- | --- | --- |
| G90 | Root | Complete<br>`L1–241`<br>`B[0,7527)`<br>1 chunk | **R** `upload/101 - Tasks(1).md` |

## 5. Exact successful reading intervals

This table preserves the successful chunk intervals for every group. Entries within a cell follow reading order and cover the complete group without gaps. For byte-based readers, each entry pairs the original byte interval with its inclusive line interval. For root, each entry pairs the displayed character interval with its verified original byte interval. The root newline conventions are listed in section 3.

| Group | Reader | Successful complete reading intervals |
| --- | --- | --- |
| G00 | Gameplay reader | `B[0,15883)` · `L1–190`<br>`B[15883,28515)` · `L191–289` |
| G01 | Assets reader | `B[0,2456)` · `L1–21` |
| G02 | Gameplay reader | `B[0,15966)` · `L1–321`<br>`B[15966,31740)` · `L322–612`<br>`B[31740,47675)` · `L613–805`<br>`B[47675,63638)` · `L806–1005`<br>`B[63638,64394)` · `L1006–1022` |
| G03 | Agents reader | `B[0,14717)` · `L1–119`<br>`B[14717,29648)` · `L120–309`<br>`B[29648,44442)` · `L310–431` |
| G04 | Agents reader | `B[0,14996)` · `L1–124`<br>`B[14996,29845)` · `L125–259`<br>`B[29845,41493)` · `L260–366` |
| G05 | Assets reader | `B[0,16938)` · `L1–86`<br>`B[16938,33929)` · `L87–193`<br>`B[33929,50641)` · `L194–259`<br>`B[50641,67005)` · `L260–337`<br>`B[67005,83437)` · `L338–425`<br>`B[83437,96728)` · `L426–477` |
| G06 | Root | `C[0,22000)` → `B[0,22002)`<br>`C[22000,44000)` → `B[22002,44002)`<br>`C[44000,66000)` → `B[44002,66002)`<br>`C[66000,88000)` → `B[66002,88002)`<br>`C[88000,110000)` → `B[88002,110002)`<br>`C[110000,132000)` → `B[110002,132002)`<br>`C[132000,154000)` → `B[132002,154002)`<br>`C[154000,176000)` → `B[154002,176002)`<br>`C[176000,197107)` → `B[176002,197109)` |
| G07 | Assets reader | `B[0,16887)` · `L1–201`<br>`B[16887,33835)` · `L202–324`<br>`B[33835,50800)` · `L325–497`<br>`B[50800,67580)` · `L498–631`<br>`B[67580,83970)` · `L632–766`<br>`B[83970,100883)` · `L767–917`<br>`B[100883,109712)` · `L918–1004` |
| G08 | Gameplay reader | `B[0,15914)` · `L1–127`<br>`B[15914,31829)` · `L128–275`<br>`B[31829,47497)` · `L276–450`<br>`B[47497,63479)` · `L451–624`<br>`B[63479,79412)` · `L625–826`<br>`B[79412,80791)` · `L827–833` |
| G09 | Gameplay reader | `B[0,15860)` · `L1–309`<br>`B[15860,19635)` · `L310–328` |
| G10 | Assets reader | `B[0,16801)` · `L1–99`<br>`B[16801,23695)` · `L100–130` |
| G11 | Assets reader | `B[0,16994)` · `L1–304`<br>`B[16994,28266)` · `L305–501` |
| G12 | Assets reader | `B[0,16996)` · `L1–287`<br>`B[16996,33979)` · `L288–514`<br>`B[33979,50968)` · `L515–772`<br>`B[50968,67902)` · `L773–1084`<br>`B[67902,84688)` · `L1085–1307`<br>`B[84688,98951)` · `L1308–1505` |
| G13 | Gameplay reader | `B[0,15944)` · `L1–279`<br>`B[15944,31944)` · `L280–632`<br>`B[31944,34086)` · `L633–698` |
| G14 | Assets reader | `B[0,16719)` · `L1–438`<br>`B[16719,33489)` · `L439–787` |
| G15 | Agents reader | `B[0,5362)` · `L1–20` |
| G16 | Agents reader | `B[0,14872)` · `L1–100`<br>`B[14872,16848)` · `L101–120` |
| G17 | Gameplay reader | `B[0,15667)` · `L1–56`<br>`B[15667,31292)` · `L57–129`<br>`B[31292,47266)` · `L130–167`<br>`B[47266,63188)` · `L168–280`<br>`B[63188,65053)` · `L281–294` |
| G18 | Agents reader | `B[0,11714)` · `L1–192` |
| G19 | Agents reader | `B[0,2857)` · `L1–42` |
| G20 | Agents reader | `B[0,3991)` · `L1–61` |
| G21 | Gameplay reader | `B[0,15943)` · `L1–338`<br>`B[15943,31929)` · `L339–671`<br>`B[31929,41848)` · `L672–855` |
| G22 | Root | `C[0,12712)` → `B[0,12728)` |
| G23 | Agents reader | `B[0,14995)` · `L1–123`<br>`B[14995,29963)` · `L124–239`<br>`B[29963,44353)` · `L240–408`<br>`B[44353,48552)` · `L409–448` |
| G24 | Root | `C[0,22000)` → `B[0,22077)`<br>`C[22000,44000)` → `B[22077,44077)`<br>`C[44000,55501)` → `B[44077,55586)` |
| G25 | Agents reader | `B[0,2650)` · `L1–39` |
| G26 | Root | `C[0,22000)` → `B[0,22128)`<br>`C[22000,44000)` → `B[22128,44259)`<br>`C[44000,66000)` → `B[44259,66391)`<br>`C[66000,88000)` → `B[66391,88483)`<br>`C[88000,110000)` → `B[88483,110592)`<br>`C[110000,115625)` → `B[110592,116242)` |
| G27 | Gameplay reader | `B[0,15856)` · `L1–267`<br>`B[15856,31848)` · `L268–598`<br>`B[31848,35963)` · `L599–701` |
| G28 | Gameplay reader | `B[0,15922)` · `L1–237`<br>`B[15922,31823)` · `L238–532`<br>`B[31823,47813)` · `L533–738`<br>`B[47813,63808)` · `L739–905`<br>`B[63808,77650)` · `L906–1082` |
| G29 | Root | `C[0,22000)` → `B[0,22230)`<br>`C[22000,44000)` → `B[22230,44404)`<br>`C[44000,66000)` → `B[44404,66617)`<br>`C[66000,88000)` → `B[66617,88785)`<br>`C[88000,110000)` → `B[88785,110962)`<br>`C[110000,116310)` → `B[110962,117335)` |
| G30 | Root | `C[0,22000)` → `B[0,22002)`<br>`C[22000,44000)` → `B[22002,44002)`<br>`C[44000,66000)` → `B[44002,66002)`<br>`C[66000,88000)` → `B[66002,88002)`<br>`C[88000,110000)` → `B[88002,110002)`<br>`C[110000,132000)` → `B[110002,132002)`<br>`C[132000,154000)` → `B[132002,154002)`<br>`C[154000,176000)` → `B[154002,176002)`<br>`C[176000,198000)` → `B[176002,198002)`<br>`C[198000,200866)` → `B[198002,200868)` |
| G31 | Gameplay reader | `B[0,15930)` · `L1–125`<br>`B[15930,31892)` · `L126–267`<br>`B[31892,47745)` · `L268–402`<br>`B[47745,63535)` · `L403–555`<br>`B[63535,79506)` · `L556–723`<br>`B[79506,95424)` · `L724–919`<br>`B[95424,100605)` · `L920–971` |
| G32 | Root | `C[0,22000)` → `B[0,22323)`<br>`C[22000,44000)` → `B[22323,44634)`<br>`C[44000,66000)` → `B[44634,67040)`<br>`C[66000,88000)` → `B[67040,89365)`<br>`C[88000,97974)` → `B[89365,99463)` |
| G33 | Assets reader | `B[0,16978)` · `L1–259`<br>`B[16978,29504)` · `L260–501` |
| G34 | Gameplay reader | `B[0,15917)` · `L1–188`<br>`B[15917,28767)` · `L189–287` |
| G35 | Gameplay reader | `B[0,2383)` · `L1–69` |
| G36 | Gameplay reader | `B[0,4821)` · `L1–37` |
| G37 | Gameplay reader | `B[0,8139)` · `L1–93` |
| G38 | Assets reader | `B[0,16885)` · `L1–84`<br>`B[16885,28241)` · `L85–145` |
| G39 | Gameplay reader | `B[0,6515)` · `L1–33` |
| G40 | Gameplay reader | `B[0,14609)` · `L1–106` |
| G41 | Agents reader | `B[0,14833)` · `L1–97`<br>`B[14833,29574)` · `L98–186`<br>`B[29574,44159)` · `L187–319`<br>`B[44159,55946)` · `L320–425` |
| G42 | Assets reader | `B[0,16970)` · `L1–435`<br>`B[16970,33013)` · `L436–771` |
| G43 | Gameplay reader | `B[0,5309)` · `L1–75` |
| G44 | Agents reader | `B[0,5232)` · `L1–20` |
| G45 | Gameplay reader | `B[0,15733)` · `L1–56`<br>`B[15733,31104)` · `L57–131`<br>`B[31104,47047)` · `L132–173`<br>`B[47047,62978)` · `L174–287`<br>`B[62978,63141)` · `L288–288` |
| G46 | Agents reader | `B[0,14934)` · `L1–103`<br>`B[14934,18229)` · `L104–135` |
| G47 | Gameplay reader | `B[0,15578)` · `L1–284`<br>`B[15578,31344)` · `L285–443`<br>`B[31344,47331)` · `L444–569`<br>`B[47331,49370)` · `L570–582` |
| G48 | Gameplay reader | `B[0,4746)` · `L1–63` |
| G49 | Agents reader | `B[0,12647)` · `L1–224` |
| G50 | Agents reader | `B[0,14749)` · `L1–102`<br>`B[14749,28417)` · `L103–198` |
| G51 | Agents reader | `B[0,6412)` · `L1–66` |
| G52 | Agents reader | `B[0,3019)` · `L1–58` |
| G53 | Agents reader | `B[0,8021)` · `L1–86` |
| G54 | Agents reader | `B[0,8992)` · `L1–100` |
| G55 | Agents reader | `B[0,11319)` · `L1–134` |
| G56 | Agents reader | `B[0,4141)` · `L1–66` |
| G57 | Agents reader | `B[0,10134)` · `L1–90` |
| G58 | Agents reader | `B[0,4478)` · `L1–80` |
| G59 | Agents reader | `B[0,3925)` · `L1–72` |
| G60 | Agents reader | `B[0,10864)` · `L1–128` |
| G61 | Agents reader | `B[0,7229)` · `L1–61` |
| G62 | Agents reader | `B[0,9782)` · `L1–111` |
| G63 | Agents reader | `B[0,2509)` · `L1–22` |
| G64 | Agents reader | `B[0,13486)` · `L1–235` |
| G65 | Agents reader | `B[0,5388)` · `L1–74` |
| G66 | Agents reader | `B[0,3258)` · `L1–45` |
| G67 | Agents reader | `B[0,4714)` · `L1–60` |
| G68 | Agents reader | `B[0,3340)` · `L1–65` |
| G69 | Agents reader | `B[0,3919)` · `L1–62` |
| G70 | Agents reader | `B[0,14777)` · `L1–102`<br>`B[14777,27552)` · `L103–197` |
| G71 | Agents reader | `B[0,6414)` · `L1–66` |
| G72 | Agents reader | `B[0,3024)` · `L1–58` |
| G73 | Agents reader | `B[0,8099)` · `L1–87` |
| G74 | Agents reader | `B[0,8994)` · `L1–100` |
| G75 | Agents reader | `B[0,11319)` · `L1–134` |
| G76 | Agents reader | `B[0,4141)` · `L1–66` |
| G77 | Agents reader | `B[0,10136)` · `L1–90` |
| G78 | Agents reader | `B[0,4480)` · `L1–80` |
| G79 | Agents reader | `B[0,3930)` · `L1–72` |
| G80 | Agents reader | `B[0,10096)` · `L1–117` |
| G81 | Agents reader | `B[0,7229)` · `L1–61` |
| G82 | Agents reader | `B[0,9782)` · `L1–111` |
| G83 | Agents reader | `B[0,2049)` · `L1–20` |
| G84 | Agents reader | `B[0,13488)` · `L1–235` |
| G85 | Agents reader | `B[0,5388)` · `L1–74` |
| G86 | Agents reader | `B[0,3258)` · `L1–45` |
| G87 | Agents reader | `B[0,4605)` · `L1–59` |
| G88 | Agents reader | `B[0,3342)` · `L1–65` |
| G89 | Agents reader | `B[0,3921)` · `L1–62` |
| G90 | Root | `C[0,7527)` → `B[0,7527)` |

## 6. Archive and member accounting

All five archives have the verified status **fully extracted and read**. This status combines complete member extraction and byte equality with complete semantic coverage of all contained text groups, including definitions inside the nested archives. The member tables list every archive entry and its destination group or nested archive.

| Archive | Supplied or nested ZIP path | ZIP bytes | Members | Text members | Nested ZIPs | Extraction destination |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | `upload/all-project-sources(20261009-191148).zip` | 478,938 | 28 | 27 | 1 | `source_gate/current/` |
| A2 | `source_gate/current/subagents.zip` | 62,900 | 20 | 20 | 0 | `source_gate/current/subagents_extracted/` |
| A3 | `project_sources/24-all-project-sources.zip` | 418,567 | 23 | 22 | 1 | `source_gate/project_archive/` |
| A4 | `source_gate/project_archive/subagents.zip` | 62,071 | 20 | 20 | 0 | `source_gate/project_archive/subagents_extracted/` |
| A5 | `project_sources/01-subagents.zip` | 62,071 | 20 | 20 | 0 | `source_gate/standalone_subagents/` |

### A1: `upload/all-project-sources(20261009-191148).zip`

Extraction destination: `source_gate/current/`. Every member below passed complete decompressed-byte comparison with its extracted file.

| Exact member name | Decompressed bytes | Coverage destination | Verified status |
| --- | --- | --- | --- |
| `AGENTS.md` | 48,552 | G23 | Complete text coverage |
| `CHAOS_REDUX_MECHANICS.md` | 55,586 | G24 | Complete text coverage |
| `README.md` | 2,650 | G25 | Complete text coverage |
| `chaos-redux-3d-model-pipeline.md` | 116,242 | G26 | Complete text coverage |
| `chaos-redux-debug-playtest.md` | 35,963 | G27 | Complete text coverage |
| `chaos-redux-decisions-missions.md` | 77,650 | G28 | Complete text coverage |
| `chaos-redux-event-assets.md` | 117,335 | G29 | Complete text coverage |
| `chaos-redux-event-planning.md` | 200,868 | G30 | Complete text coverage |
| `chaos-redux-events.md` | 100,605 | G31 | Complete text coverage |
| `chaos-redux-focus-trees.md` | 99,463 | G32 | Complete text coverage |
| `chaos-redux-frame-animation.md` | 29,504 | G33 | Complete text coverage |
| `chaos-redux-improvement-loop.md` | 28,767 | G34 | Complete text coverage |
| `chaos-redux-mtth.md` | 2,383 | G35 | Complete text coverage |
| `chaos-redux-native-raids.md` | 4,821 | G36 | Complete text coverage |
| `chaos-redux-save-inspection.md` | 8,139 | G37 | Complete text coverage |
| `chaos-redux-scripted-gui.md` | 28,241 | G38 | Complete text coverage |
| `chaos-redux-shared-git-commit.md` | 6,515 | G39 | Complete text coverage |
| `chaos-redux-state-ledgers.md` | 14,609 | G40 | Complete text coverage |
| `chaos-redux-subagents.md` | 55,946 | G41 | Complete text coverage |
| `chaos-redux-super-events.md` | 33,013 | G42 | Complete text coverage |
| `chaos-redux-xlsx.md` | 5,309 | G43 | Complete text coverage |
| `chaos_redux_clusters_catalog.csv` | 5,232 | G44 | Complete text coverage |
| `chaos_redux_events_catalog.csv` | 63,141 | G45 | Complete text coverage |
| `chaos_redux_scenarios_catalog.csv` | 18,229 | G46 | Complete text coverage |
| `chaosx_dynamic_effects.md` | 49,370 | G47 | Complete text coverage |
| `chaosx_dynamic_triggers.md` | 4,746 | G48 | Complete text coverage |
| `config.toml` | 12,647 | G49 | Complete text coverage |
| `subagents.zip` | 62,900 | A2 | Nested archive fully accounted for |

### A2: `source_gate/current/subagents.zip`

Extraction destination: `source_gate/current/subagents_extracted/`. Every member below passed complete decompressed-byte comparison with its extracted file.

| Exact member name | Decompressed bytes | Coverage destination | Verified status |
| --- | --- | --- | --- |
| `chaosx_3d_model_pipeline.toml` | 28,417 | G50 | Complete text coverage |
| `chaosx_ai_probability_auditor.toml` | 6,412 | G51 | Complete text coverage |
| `chaosx_asset_source_researcher.toml` | 3,019 | G52 | Complete text coverage |
| `chaosx_country_package_auditor.toml` | 8,021 | G53 | Complete text coverage |
| `chaosx_decision_mission_auditor.toml` | 8,992 | G54 | Complete text coverage |
| `chaosx_documentation_curator.toml` | 11,319 | G55 | Complete text coverage |
| `chaosx_event_completion_auditor.toml` | 4,141 | G56 | Complete text coverage |
| `chaosx_event_ui_worker.toml` | 10,134 | G57 | Complete text coverage |
| `chaosx_focus_tree_auditor.toml` | 4,478 | G58 | Complete text coverage |
| `chaosx_generated_event_art.toml` | 3,925 | G59 | Complete text coverage |
| `chaosx_icon_artist.toml` | 10,864 | G60 | Complete text coverage |
| `chaosx_improvement_loop_planner.toml` | 7,229 | G61 | Complete text coverage |
| `chaosx_localisation_auditor.toml` | 9,782 | G62 | Complete text coverage |
| `chaosx_portrait_creator.toml` | 2,509 | G63 | Complete text coverage |
| `chaosx_repo_explorer.toml` | 13,486 | G64 | Complete text coverage |
| `chaosx_scripted_system_architect.toml` | 5,388 | G65 | Complete text coverage |
| `chaosx_skill_maintainer.toml` | 3,258 | G66 | Complete text coverage |
| `chaosx_spreadsheet_doc_worker.toml` | 4,714 | G67 | Complete text coverage |
| `chaosx_super_event_audio_researcher.toml` | 3,340 | G68 | Complete text coverage |
| `chaosx_super_event_text_researcher.toml` | 3,919 | G69 | Complete text coverage |

### A3: `project_sources/24-all-project-sources.zip`

Extraction destination: `source_gate/project_archive/`. Every member below passed complete decompressed-byte comparison with its extracted file.

| Exact member name | Decompressed bytes | Coverage destination | Verified status |
| --- | --- | --- | --- |
| `chaos-redux-subagents.md` | 41,493 | G04 | Complete text coverage |
| `chaos-redux-event-planning.md` | 197,109 | G06 | Complete text coverage |
| `chaos-redux-3d-model-pipeline.md` | 96,728 | G05 | Complete text coverage |
| `chaos-redux-events.md` | 80,791 | G08 | Complete text coverage |
| `chaos-redux-decisions-missions.md` | 64,394 | G02 | Complete text coverage |
| `chaos-redux-event-assets.md` | 109,712 | G07 | Complete text coverage |
| `chaos-redux-improvement-loop.md` | 28,515 | G00 | Complete text coverage |
| `chaos-redux-comfyui.md` | 2,456 | G01 | Complete text coverage |
| `chaos-redux-debug-playtest.md` | 34,086 | G13 | Complete text coverage |
| `chaos-redux-scripted-gui.md` | 23,695 | G10 | Complete text coverage |
| `chaos-redux-super-events.md` | 33,489 | G14 | Complete text coverage |
| `chaos-redux-focus-trees.md` | 98,951 | G12 | Complete text coverage |
| `chaos-redux-frame-animation.md` | 28,266 | G11 | Complete text coverage |
| `chaosx_dynamic_effects.md` | 19,635 | G09 | Complete text coverage |
| `chaos_redux_clusters_catalog.csv` | 5,362 | G15 | Complete text coverage |
| `chaos_redux_events_catalog.csv` | 65,053 | G17 | Complete text coverage |
| `chaos_redux_scenarios_catalog.csv` | 16,848 | G16 | Complete text coverage |
| `CHAOS_REDUX_MECHANICS.md` | 41,848 | G21 | Complete text coverage |
| `README.md` | 2,857 | G19 | Complete text coverage |
| `config.toml` | 11,714 | G18 | Complete text coverage |
| `chaosx_dynamic_triggers.md` | 3,991 | G20 | Complete text coverage |
| `subagents.zip` | 62,071 | A4 | Nested archive fully accounted for |
| `AGENTS.md` | 44,442 | G03 | Complete text coverage |

### A4: `source_gate/project_archive/subagents.zip`

Extraction destination: `source_gate/project_archive/subagents_extracted/`. Every member below passed complete decompressed-byte comparison with its extracted file.

| Exact member name | Decompressed bytes | Coverage destination | Verified status |
| --- | --- | --- | --- |
| `chaosx_3d_model_pipeline.toml` | 27,552 | G70 | Complete text coverage |
| `chaosx_ai_probability_auditor.toml` | 6,414 | G71 | Complete text coverage |
| `chaosx_asset_source_researcher.toml` | 3,024 | G72 | Complete text coverage |
| `chaosx_country_package_auditor.toml` | 8,099 | G73 | Complete text coverage |
| `chaosx_decision_mission_auditor.toml` | 8,994 | G74 | Complete text coverage |
| `chaosx_documentation_curator.toml` | 11,319 | G75 | Complete text coverage |
| `chaosx_event_completion_auditor.toml` | 4,141 | G76 | Complete text coverage |
| `chaosx_event_ui_worker.toml` | 10,136 | G77 | Complete text coverage |
| `chaosx_focus_tree_auditor.toml` | 4,480 | G78 | Complete text coverage |
| `chaosx_generated_event_art.toml` | 3,930 | G79 | Complete text coverage |
| `chaosx_icon_artist.toml` | 10,096 | G80 | Complete text coverage |
| `chaosx_improvement_loop_planner.toml` | 7,229 | G81 | Complete text coverage |
| `chaosx_localisation_auditor.toml` | 9,782 | G82 | Complete text coverage |
| `chaosx_portrait_creator.toml` | 2,049 | G83 | Complete text coverage |
| `chaosx_repo_explorer.toml` | 13,488 | G84 | Complete text coverage |
| `chaosx_scripted_system_architect.toml` | 5,388 | G85 | Complete text coverage |
| `chaosx_skill_maintainer.toml` | 3,258 | G86 | Complete text coverage |
| `chaosx_spreadsheet_doc_worker.toml` | 4,605 | G87 | Complete text coverage |
| `chaosx_super_event_audio_researcher.toml` | 3,342 | G88 | Complete text coverage |
| `chaosx_super_event_text_researcher.toml` | 3,921 | G89 | Complete text coverage |

### A5: `project_sources/01-subagents.zip`

Extraction destination: `source_gate/standalone_subagents/`. Every member below passed complete decompressed-byte comparison with its extracted file.

| Exact member name | Decompressed bytes | Coverage destination | Verified status |
| --- | --- | --- | --- |
| `chaosx_3d_model_pipeline.toml` | 27,552 | G70 | Complete text coverage |
| `chaosx_ai_probability_auditor.toml` | 6,414 | G71 | Complete text coverage |
| `chaosx_asset_source_researcher.toml` | 3,024 | G72 | Complete text coverage |
| `chaosx_country_package_auditor.toml` | 8,099 | G73 | Complete text coverage |
| `chaosx_decision_mission_auditor.toml` | 8,994 | G74 | Complete text coverage |
| `chaosx_documentation_curator.toml` | 11,319 | G75 | Complete text coverage |
| `chaosx_event_completion_auditor.toml` | 4,141 | G76 | Complete text coverage |
| `chaosx_event_ui_worker.toml` | 10,136 | G77 | Complete text coverage |
| `chaosx_focus_tree_auditor.toml` | 4,480 | G78 | Complete text coverage |
| `chaosx_generated_event_art.toml` | 3,930 | G79 | Complete text coverage |
| `chaosx_icon_artist.toml` | 10,096 | G80 | Complete text coverage |
| `chaosx_improvement_loop_planner.toml` | 7,229 | G81 | Complete text coverage |
| `chaosx_localisation_auditor.toml` | 9,782 | G82 | Complete text coverage |
| `chaosx_portrait_creator.toml` | 2,049 | G83 | Complete text coverage |
| `chaosx_repo_explorer.toml` | 13,488 | G84 | Complete text coverage |
| `chaosx_scripted_system_architect.toml` | 5,388 | G85 | Complete text coverage |
| `chaosx_skill_maintainer.toml` | 3,258 | G86 | Complete text coverage |
| `chaosx_spreadsheet_doc_worker.toml` | 4,605 | G87 | Complete text coverage |
| `chaosx_super_event_audio_researcher.toml` | 3,342 | G88 | Complete text coverage |
| `chaosx_super_event_text_researcher.toml` | 3,921 | G89 | Complete text coverage |

## 7. All 27 top-level supplied inputs

These are the original inputs under `upload/` and `project_sources/`. Extracted files are accounted for separately in sections 4 and 6. Every top-level input is present in the source inventory or the archive inventory.

| Input | Exact top-level path | Type | Coverage destination | Verified status |
| --- | --- | --- | --- | --- |
| 1 | `upload/101 - Tasks(1).md` | source text | G90 | Complete text coverage |
| 2 | `upload/all-project-sources(20261009-191148).zip` | archive | A1 | Archive fully extracted and read |
| 3 | `project_sources/01-subagents.zip` | archive | A5 | Archive fully extracted and read |
| 4 | `project_sources/02-chaos-redux-improvement-loop.md` | source text | G00 | Complete text coverage |
| 5 | `project_sources/03-chaos-redux-comfyui.md` | source text | G01 | Complete text coverage |
| 6 | `project_sources/04-chaos-redux-decisions-missions.md` | source text | G02 | Complete text coverage |
| 7 | `project_sources/05-AGENTS.md` | source text | G03 | Complete text coverage |
| 8 | `project_sources/06-chaos-redux-subagents.md` | source text | G04 | Complete text coverage |
| 9 | `project_sources/07-chaos-redux-3d-model-pipeline.md` | source text | G05 | Complete text coverage |
| 10 | `project_sources/08-chaos-redux-event-planning.md` | source text | G06 | Complete text coverage |
| 11 | `project_sources/09-chaos-redux-event-assets.md` | source text | G07 | Complete text coverage |
| 12 | `project_sources/10-chaos-redux-events.md` | source text | G08 | Complete text coverage |
| 13 | `project_sources/11-chaosx_dynamic_effects.md` | source text | G09 | Complete text coverage |
| 14 | `project_sources/12-chaos-redux-scripted-gui.md` | source text | G10 | Complete text coverage |
| 15 | `project_sources/13-chaos-redux-frame-animation.md` | source text | G11 | Complete text coverage |
| 16 | `project_sources/14-chaos-redux-focus-trees.md` | source text | G12 | Complete text coverage |
| 17 | `project_sources/15-chaos-redux-debug-playtest.md` | source text | G13 | Complete text coverage |
| 18 | `project_sources/16-chaos-redux-super-events.md` | source text | G14 | Complete text coverage |
| 19 | `project_sources/17-chaos_redux_clusters_catalog-5-.csv` | source text | G15 | Complete text coverage |
| 20 | `project_sources/18-chaos_redux_scenarios_catalog-5-.csv` | source text | G16 | Complete text coverage |
| 21 | `project_sources/19-chaos_redux_events_catalog-5-.csv` | source text | G17 | Complete text coverage |
| 22 | `project_sources/20-config.toml` | source text | G18 | Complete text coverage |
| 23 | `project_sources/21-README.md` | source text | G19 | Complete text coverage |
| 24 | `project_sources/22-chaosx_dynamic_triggers.md` | source text | G20 | Complete text coverage |
| 25 | `project_sources/23-CHAOS_REDUX_MECHANICS.md` | source text | G21 | Complete text coverage |
| 26 | `project_sources/24-all-project-sources.zip` | archive | A3 | Archive fully extracted and read |
| 27 | `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | source text | G22 | Complete text coverage |

## 8. Evidence limits and count interpretation

The semantic-reading evidence consists of the actual readers’ confirmations and their complete reading ledgers. The independent verifier did not claim that decompression, file iteration, hashing, or byte comparison amounted to semantic reading. It validated source identity, range completeness, archive membership, and the correspondence between supplied paths and those reading records.

The group count measures distinct original content versions. The path count includes exact copies. The archive-member count includes nested archive entries and repeated definitions present in separate supplied archives. The 199 chunk count includes only successful primary reading records. Supplemental reading does not add new content groups, paths, or counted chunks.

One supplemental protocol entry in the assets ledger lists lines 1–372 while recording all 12,728 bytes. The inventory, gameplay and agents protocol records, and canonical G22 coverage use 373 lines. The primary G22 record is fully covered and independently verified. The supplemental line-label discrepancy does not create a missing byte range and does not affect the counted coverage.

This appendix is a record of supplied-source reading and verification at the stated time. It does not establish the behavior of an implementation or constitute runtime or code validation. Subsequent source changes are outside this recorded snapshot. Independent repetition of the original-byte comparisons requires the original inputs and extracted contents. Independent review of displayed reading evidence also requires the internal ledgers and reading records. This appendix preserves the exhaustive path attribution, successful intervals, and verification result without embedding those original materials.

## 9. Verification provenance

The appendix was generated from the following existing verification inputs. The inventory and all four reader ledgers still matched the recorded verification snapshots when the appendix was assembled. SHA-256 values identify the evidence snapshots and do not replace the complete-byte comparison method described above.

| Verification input | Bytes | SHA-256 |
| --- | --- | --- |
| `source_gate/inventory.json` | 46877 | `f78ab3579a350f85fb12c347e8df1b762be2fdb37bf712013e03099e12ee67fa` |
| `source_gate/readers/root_ledger.json` | 12865 | `f9a53b930d313ed97819239e1e3c396565d1f555e9659074e5a7701514188ad0` |
| `source_gate/readers/gameplay_ledger.json` | 40946 | `6da7633746c90c0c328c39afc7bd41b2d23ffb70752136f7139975907ad644d9` |
| `source_gate/readers/assets_ledger.json` | 28360 | `debd8dea2916b9b690218afd884bbfed2194e11cdc534c2de5d2a67315dd38db` |
| `source_gate/readers/agents_ledger.json` | 81610 | `bd75ebc7c8ca20d0cdc678de124ceedccf4274357eae24efd483a5d400968da5` |
| `source_gate/coverage_verification.json` | 238699 | `73186c2c5d4e77601d5a67889c789f0d5e791f051d1d0cfd465baaa827b0b577` |
