# Doctor Wu Stage 3 source-reading report

## Supplied-source gate

The complete source gate passed before feature repository inspection, Part 7 authoring, or the cumulative package update. This task used a fresh pass over the current supplied sources. Earlier Stage 1 and Stage 2 reading claims were not substituted for reading.

The pass covered 69 distinct supplied text byte-identities, totaling 1,712,705 bytes and 21,214 physical lines. They comprise the 42 text files extracted from the source archive, the source protocol, the original Doctor Wu brief, 23 other unique Stage 2 files, and two unique Stage 1 files. The Stage 2 package contains 24 files, with its original-brief copy byte-identical to the separately supplied brief. The two additional Stage 1 identities are its README and specification index. All other supplied duplicate copies were compared before being treated as aliases of fully read text.

The 42 archive files include 22 root text, configuration, skill, and catalogue files and all twenty nested specialist definitions. Both supplied ZIP containers were inventoried and safely extracted without running their configuration or scripts. The nineteen files left unread in Stage 1 were included in the complete fresh pass. The separately supplied source protocol was read in full.

Complete current-task visible source text supplied the fully available opening ranges. The remaining text was displayed and processed in 124 bounded chunks. Truncated attempts were recovered through smaller ranges. The original archive-reading inventory's initial unreviewed discovery states have not been copied into the current completion ledger.

The [source inventory](2026-09-25_stage_3_source_inventory.json) records every source identity, byte count, physical line count, completed range, reading segment, and duplicate comparison. Hashes establish file identity. They do not independently prove reading or understanding. Physical file lines and the Files viewer's displayed line numbering can differ by one around trailing newlines.

## Current repository reference

The live GitHub branch query returned master at `5212636eef9f9607691ddc1348bddade1bafe0dd`, committed on 24 September 2026 at 19:29:51 UTC. All feature reads in this pass were pinned to that revision. The connector returned source text and Git blob identities. No local raw repository checkout was obtained.

Fourteen owner-source files were fully read. The two Kruger maps that remained incomplete at Stage 2 are now included in the completed full-text set. Their references to other documents do not imply that every linked file or all forty-four historical Kruger specification files was also read.

| Fully read file | Git blob | Completed source ranges | Finding and limit |
| --- | --- | --- | --- |
| `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md` | `badba01a1c31061e488493d04009d2e956987bf5` | 1-40, 41-80, 81-160, 161-end | Completed historical map, current amendment and authority order. Old completion and asset claims are not current acceptance. |
| `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` | `265b9454e398c7129ec3ade9f9d64ca4489adc55` | 1-35, 36-85, 86-155, 156-185, 186-225, 226-270, 271-end | Completed runtime handoff. Historical provider counts and model dispositions require their current owners, not blind reuse. |
| `common/units/equipment/clone_equipment.txt` | `6c5e2edf11f2262b8adb8b9c00b9243d9b5e1bb9` | full file | Legacy physical archetype and concrete model. Build cost 12, steel 1, rubber 2. No finite birth or settlement interface. |
| `common/dynamic_modifiers/clone_system_dynamic_modifiers.txt` | `5880e9c4f4f5d25abf033de52d136d6c84e3987c` | full file | Recurring weekly manpower reads the stockpile-derived variable. |
| `common/technologies/clone_technologies.txt` | `bc2f649512a552c1999fb9c9e3025374c2582086` | full file | Grant-only legacy access and separate Mengele refinement technologies. |
| `common/scripted_effects/clone_system_effects.txt` | `ec9187aa65eaaa63b1b48d9fcbc2c5b6047bc375` | full file | Legacy access opens manufacture and recruitment. Refinement selectors exclude competing legacy refinements. Reserve refresh does not consume stock. |
| `common/script_constants/clone_system_constants.txt` | `087bc788662901e1981596c85792b25c1f93a73a` | full file | Ten weekly manpower per stock item and the ten-battalion legacy template contract. |
| `docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md` | `a4b780c7e94899c98f606fec7bbff26dbb72a052` | full file | Provider-neutral ownership, legacy capture and transfer, model limits, and conditional permission for causally distinct future archetypes. |
| `common/scripted_effects/016_clone_maturation_effects.txt` | `0aaf60de99887ebb2058c2fc8633f909b4d2ac3e` | 1-end | KRG receipt is retired before refund or physical output. Native decision owns factory reservation. No direct manpower reward. |
| `common/scripted_effects/016_clone_maturation_effects.md` | `cd6c2f185d5e6c96fdff69f84f4e17a68ec67c27` | full file | Current KRG paid cycle, exact cancellation and single-active-receipt assumptions, and validation limits. |
| `common/units/clone_infantry.txt` | `1ad77d24526649f5a58e2b518bf22021d05ee069` | full file | Legacy battalions use 1,000 manpower, 90 rifles, one legacy cohort, width 2, organisation 70, and strength 20. |
| `docs/plans/germany_mengele_path_plans/mengele_cloning_special_project.md` | `c0e257d7c6fb53b36e438e3b2a18a797e7fcc458` | full file | Mengele-owned project and facility production remain separate. This reference does not prove all current Mengele runtime callers. |
| `common/special_projects/projects/mengele_cloning_projects.txt` | `8329c01b6be366e46ac9d4eea99ed24857320607` | Full file | Current native owner gate and completion, with neutral custom-technology provenance. |
| `common/scripted_effects/cbrn_special_project_effects.txt` | `4aaecd17b826693f7815db5f0b2c2bd16e4e3193` | 1–end | Neutral clone discovery completion grants the legacy custom package without Event 016 story history. |

## Bounded owner reads

The following reads are useful current evidence but are not counted as full files. In particular, the transfer function was fully covered inside a larger effects file whose remaining text was not all read.

| File | Git blob | Completed source ranges | Finding and limit |
| --- | --- | --- | --- |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | `56ced7525bfceeaf9be4517c618fbb13a2ec8d8c` | 1-90, 280-435, 500-660, 800-1010, 2000-2090, 2700-2720, 2900-3430, 3500-3520 | The full transfer_kruger_atomically function is covered inside 2900-3430. One canonical Kruger is moved after validation and old-role removal. Other file sections and complete helper closure were not read. |
| `docs/events/016_brilliant_scientist/systems/projects.md` | `b0f3a86dc95f409d2aba69e2c76526c485155414` | 1-190 | Cloning project prerequisites, native/no-DLC stage ownership, and permanent learned knowledge. Remaining file not read in this task. |
| `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` | `dae1c879f433df35c3e44d4e1818d42addaa062a` | 1-105 | Binding legacy ten-weekly-manpower and KRG cycle clauses, API isolation, and native biological amendment. Later sections not reread in this task. |
| `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` | `120e7569306ef83fa3fc583e25b99f72ce11ea1e` | 80-end | Fourteen provider surfaces, exact fees and refunds, parent isolation, and limited natural-release substitute. Lines 1-79 not reread in this task. |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `8e68b44df308409d858ed4ecb9b3be669a998568` | 350–610 | Complete native cloning definition within a larger partially read project file. Neutral CBRN discovery is an additional visible and available route. |

The runtime-map request for lines 156–235 was truncated and was replaced by smaller reads covering the complete interval. The main-effects request for lines 3121–3360 was also truncated and was replaced by three complete smaller reads. Neither truncated response is counted as a completed range on its own. Search matches were discovery only. The truncated special-project directory response was used only to locate exact filenames and is not a complete inventory claim.

## Offline wiki consultations

The required eleven core offline wiki pages and four additional character, unit, equipment, and technology pages were consulted in bounded ranges. These are repository snapshot references, not current installed-vanilla proof or complete-page reads. No Paradox wiki website was substituted for the required offline source.

| Offline page | Source lines consulted |
| --- | --- |
| Data structures | 45-115 |
| Triggers | 60-115 |
| Effects | 70-115 |
| Modifiers | 50-115 |
| Localisation | 42-90 |
| Scopes | 23-78 |
| On actions | 29-65 |
| Event modding | 24-68 |
| Decision modding | 40-95 |
| Idea modding | 26-75 |
| AI modding | 24-75 |
| Character modding | 1-110 |
| Unit modding | 32-110 |
| Equipment modding | 1-115 |
| Technology modding | 55-120 |

## External references and execution not completed

Installed vanilla documentation, current Windows game files, actual character-instance and exact-formation consumers, native positive-population side effects, current catalogue workbook, and production visual references were not accessible as mounted inputs and were not inspected. Their gaps affect implementation evidence. They do not describe missing supplied Project Sources.

Native biological operations, Zombie Outbreak, Black Plague, the custom technology API, and CXT retain the detailed Stage 2 source findings already present in the cumulative package. Their complete external owner files were not all reread during Stage 3. Only the current bounded native-biological amendment and unit-family evidence listed above are fresh Stage 3 reads. The next part needs new current reads for the owners it extends.

Tool discovery found no usable project specialist spawn or HOI4 execution route. The exposed Codex runtime-inventory action required an unsupplied turn token, and none was invented. A plugin search for the requested route names returned no usable specialist or HOI4 execution interface. No specialist was spawned, and no HOI4 MCP, live-game, model-provider, image-generation, or audio-research workflow ran.

The local design fixtures, link checks, preservation comparisons, and ZIP checks are separately recorded in the [parent review](audits/2026-09-25_stage_3_parent_design_review.md). They are parent-authored document and arithmetic evidence, not independent audit, native-timer, or live-game validation.
