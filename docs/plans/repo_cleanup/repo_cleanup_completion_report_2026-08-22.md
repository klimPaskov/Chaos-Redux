# Chaos Redux Repository Cleanup Completion Report — 2026-08-22

## Executive disposition

This report reconciles the bounded cleanup evidence for shared systems and event-specific surfaces for Events 1–20 as of 2026-08-22.

The safe cleanup tranche is complete: high-confidence stale localisation, selector, helper, inert-bookkeeping, documentation-path, evidence-link, and explicitly unreferenced runtime-copy defects were corrected, while the repository cleanup map, baselines, migration queue, spreadsheet alignment, docs/assets inventory, and Git-storage record were preserved.

This is not a claim that every event, country package, focus tree, asset package, GUI, probability surface, or design migration is complete.

Events 21+ event-specific implementations remain out of scope; only shared registration, catalog, settings, scenario, localisation, and helper references were inspected or mentioned where needed to verify the bounded Events 1–20 cleanup.

The cleanup-owned implementation evidence is the following commit set: `b638e743a`, `29abd27ea`, `72ae50791`, `9de7d2293`, `1ade302fb`, `3ba28a960`, `4c3c8f1db`, `393135c5c`, `da05faa36`, `7a5754cd1`, `b6f61028f`, `886f50d80`, `fd0089b06`, `9954f2e32`, `949594883`, `adcbbc25a`, `5b5302cae`, `49dad024c`, `e77ae8965`, `f1a1d56d3`, `eec9f7692`, `e3eb929f3`, `2f529cc54`, `775099cbf`, `15de66457`, `0587e680c`, `5e907da0a`, and `9e77bf976`. Report-only reconciliation commits are not enumerated recursively. Only the storage-report portion of mixed commit `15de66457` belongs to this cleanup ledger; unrelated Event 014 edits in that commit are excluded.

The additional cleanup documentation commits `49dad024c` and `e77ae8965` are included: historical Event 017 and Event 020 helper observations now carry explicit supersession notes, and the bounded Event 013–020 report distinguishes preserved historical evidence from current ownership.

Commit `f1a1d56d3` reconciles durable README navigation, fixes the cleanup-goal prompt path, normalises the known hard-wrapped historical interface audit, and records the filesystem-wide README inventory and link validation.

## Systems inspected

The source-of-truth map is: accepted design specifications under `docs/specs/<event>_<slug>_specs/`; current implementation descriptions under `docs/events/<event>/overview.md`; working plans and subagent handoffs under `docs/plans/`; current scripts, localisation, interface, assets, and workbook as implementation evidence; and the cleanup reports as bounded audit evidence rather than approval to redesign.

The inspected shared surfaces were event registration and settings selectors, Event Log and Event Details localisation, scripted localisation, scripted effects and triggers, on-action bookkeeping, repeatable-event recovery comments, decision and mission references, focus and country package references, super-event and asset provenance references, event-catalog workbook/export alignment, and Git object/LFS storage.

The required repository instructions, the [`chaos-redux-subagents` skill](../../../.agents/skills/chaos-redux-subagents/SKILL.md), the cleanup master prompt, the cleanup goal prompt, all cleanup handoffs and reports, the relevant offline Paradox wiki pages, and the relevant vanilla documentation were read before reconciliation.

Exact commit paths were inspected with Git, then compared against current source scans and the current worktree so unrelated concurrent changes were not attributed to cleanup.

The primary evidence bundles are [`events_001_010_cleanup_audit_2026-08-22.md`](subagent_handoffs/events_001_010_cleanup_audit_2026-08-22.md), [`events_011_020_cleanup_audit_2026-08-22.md`](subagent_handoffs/events_011_020_cleanup_audit_2026-08-22.md), [`repo_map_2026-08-22.md`](subagent_handoffs/repo_map_2026-08-22.md), [`shared_helper_architecture_baseline_2026-08-22.md`](subagent_handoffs/shared_helper_architecture_baseline_2026-08-22.md), [`shared_system_migration_plan_2026-08-22.md`](shared_system_migration_plan_2026-08-22.md), and the historical [`documentation_cleanup_2026-07-29.md`](subagent_handoffs/documentation_cleanup_2026-07-29.md).

## Event-specific surfaces inspected for Events 1–20

| Event | Current disposition and cleanup evidence |
|---|---|
| 001 Communism Spread | No high-confidence event-source defect was found in the bounded audit; eight shared option confirmations were normalised to `PDXO_OK`, and the shared Event Details premise/catalog text was corrected. Event inspection was partial and event rendering timed out. |
| 002 Zombie Special Project | The base zombie package and runtime registration are current; seven specialised model packages remain blocked or incomplete, and the dynamically live provider adapters were retained. No speculative package deletion or redesign was made. |
| 003 Holy Realm | Current Fallout ownership and terminal-route documentation was reconciled; four unreferenced Holy Realm helpers and three unconsumed Final Silence triggerable-scenario localisation keys were removed, while compatibility callbacks and archived assets were retained. The Event 003 audit remained partial because render and some MCP routes timed out. |
| 004 Random War | No high-confidence cleanup defect was found; no source or layout change was justified. |
| 005 Soviet Collapse | The runtime package was treated as functionally mature; four explicitly unreferenced runtime leader DDS copies were removed, while the durable archive manifest and documentation assets were retained. |
| 006 Independence Wave | The bounded cleanup corrected evidence links and normalised the evolution-incident localisation file; the wider package remains HOLD/PARTIAL because portraits, rights, focus, probability, audio, and package-admission evidence are incomplete or blocked. |
| 007 Fury | No safe source cleanup was found; the repeatable recovery comments now describe the configured recovery rate and one recovery step without changing behavior. The option-999/option-1 probability candidate remains deferred. |
| 008 Tensions Rising | No high-confidence source defect was found; no speculative focus, country, or GUI change was made. |
| 009 White Peace | Source and catalog evidence remain aligned; the shared White Peace Event Details premise was corrected. No broader design change was made. |
| 010 Death | Ghost-host assets are wired, but shared DTH dashboard reuse remains blocked; the shared Death Event Details premise was corrected and no cleanup-owned GUI layout rewrite was made. |
| 011 Secret Alliance | The implementation is materially present, but a broader docs/assets archive is absent; the stale `event_011_unavailable` Event Details key was removed from active localisation and retained only in historical evidence. |
| 012 Africa | The package is a release candidate with intentional dormant packages; the catalog detail was aligned to current player-facing wording. No dormant package was deleted. |
| 013 Natural Disasters | The Event Log settings and last-event selectors now map Event 013 to `chaosx.event_name.13`; the bounded static audit is extensive, while asset archiving and catalog-status promotion remain unresolved. |
| 014 Cannibalism | Gameplay evidence is current for the bounded audit; the world-threat documentation path was corrected to `014_cannibalism_effects.txt`, while historical/source-comment occurrences of the former path remain flagged rather than globally rewritten. |
| 015 Utopia Manifesto | The implementation documentation is current for the bounded audit, but the broader manifest/assets workspace is absent; no unrelated asset or gameplay change was made. |
| 016 Brilliant Scientist | The core package is accepted but the whole event remains partial; two implementation-jargon localisation strings were rewritten as player-facing text, and reserved helper/package disposition remains open. |
| 017 Random Faction | Static evidence is positive, but the catalog still says `Needs Testing`, which is a live-validation boundary; historical helper observations now carry explicit supersession notes. |
| 018 Resources Found | Static implementation evidence is positive, but probability and 3D visual proof remain open; one tooltip was rewritten in player-facing language and the catalog remains `Needs Testing`. |
| 019 Infantry Spawn | The bounded static audit is final and the catalog detail is aligned; provider odds and the broader asset workspace remain unresolved, so no balance or provider redesign was made. |
| 020 Black Plague | The bounded cleanup removed dead evolution effects, eligibility triggers, and response-target wrappers; the active scheduler and current evolution owners remain. The wider event is partial because probability comparison, 3D evidence, and asset provenance remain open. |

The event audits report partial or timed-out MCP evidence where applicable; none of those timeouts are presented as passing validation.

## Events 21+ shared-system references inspected/touched

No Events 21+ event-specific implementation was inspected or changed as a cleanup task.

Only shared references that could affect the Events 1–20 boundary were eligible for mention, including registration/catalog/settings/localisation/helper references; no Event 21+ gameplay, GUI, focus, country, asset, or balance claim is made.

Cleanup-owned Events 21+ edits are limited to shared catalog and navigation infrastructure: the authoritative workbook and exported Events CSV classify the 81 post-20 IDs with an actual `chaosx.nr<ID>.1` root as `To Be Reworked` and the 65 unregistered IDs as `Unavailable`; the event skill records that root-definition status contract; and the shared [`docs/specs/README.md`](../../specs/README.md) navigation table preserves design-package discoverability while explicitly withholding current implementation-status claims. These edits changed catalog metadata and workflow guidance only, not Event 21+ gameplay, registration, enablement, GUI, assets, or balance.

## Files changed grouped by gameplay/localisation/docs/assets/storage/spreadsheet

### Gameplay and script files

The cleanup-owned gameplay/script paths were [`events/001_communism_spread.txt`](../../../events/001_communism_spread.txt), [`common/on_actions/chaosx_on_actions_system.txt`](../../../common/on_actions/chaosx_on_actions_system.txt), [`common/scripted_localisation/chaosx_scripted_localisation_settings.txt`](../../../common/scripted_localisation/chaosx_scripted_localisation_settings.txt), [`common/scripted_effects/003_holy_realm_effects.txt`](../../../common/scripted_effects/003_holy_realm_effects.txt), [`common/scripted_effects/020_black_plague_rat_effects.txt`](../../../common/scripted_effects/020_black_plague_rat_effects.txt), [`common/scripted_triggers/020_black_plague_rat_triggers.txt`](../../../common/scripted_triggers/020_black_plague_rat_triggers.txt), [`common/scripted_triggers/020_black_plague_response_triggers.txt`](../../../common/scripted_triggers/020_black_plague_response_triggers.txt), and [`common/scripted_effects/chaosx_logic_effects.txt`](../../../common/scripted_effects/chaosx_logic_effects.txt).

The only event-file change was standardising eight Event 001 confirmation options; the repeatable-recovery edit in `chaosx_logic_effects.txt` changed comments only.

No focus, decision, mission, country, map, technology, AI-strategy, on-action iteration, GUI layout, or new gameplay system was added.

### Localisation files

The cleanup-owned localisation paths were [`localisation/english/chaosx_gui_l_english.yml`](../../../localisation/english/chaosx_gui_l_english.yml), [`localisation/english/condemnation_sanctions_l_english.yml`](../../../localisation/english/condemnation_sanctions_l_english.yml), [`localisation/english/fallout_consolidated_l_english.yml`](../../../localisation/english/fallout_consolidated_l_english.yml), [`localisation/english/006_independence_wave_evolution_incidents_l_english.yml`](../../../localisation/english/006_independence_wave_evolution_incidents_l_english.yml), [`localisation/english/016_brilliant_scientist_foreign_l_english.yml`](../../../localisation/english/016_brilliant_scientist_foreign_l_english.yml), and [`localisation/english/018_resources_found_decisions_l_english.yml`](../../../localisation/english/018_resources_found_decisions_l_english.yml).

### Documentation files

Cleanup-created evidence includes [`event_003_006_bounded_cleanup_2026-08-22.md`](event_003_006_bounded_cleanup_2026-08-22.md), [`event_013_020_bounded_cleanup_2026-08-22.md`](event_013_020_bounded_cleanup_2026-08-22.md), [`shared_system_migration_plan_2026-08-22.md`](shared_system_migration_plan_2026-08-22.md), [`git_storage_cleanup_2026-08-22.md`](git_storage_cleanup_2026-08-22.md), and the cleanup handoffs listed in the evidence section.

Cleanup-owned documentation edits also touched [`docs/events/003_holy_realm/overview.md`](../../events/003_holy_realm/overview.md), [`docs/systems/world_threat_mechanic.md`](../../systems/world_threat_mechanic.md), five Event 006 handoffs under [`docs/plans/006_independence_wave_plans/subagent_handoffs/`](../006_independence_wave_plans/subagent_handoffs/), [`docs/plans/017_random_faction_plans/repo_explorer_report.md`](../017_random_faction_plans/repo_explorer_report.md), and [`docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-24_rat_system_country_package_audit.md`](../020_black_plague_plans/subagent_handoffs/2026-07-24_rat_system_country_package_audit.md).

README management is recorded in [`docs_readme_management_2026-08-22.md`](subagent_handoffs/docs_readme_management_2026-08-22.md) and commit `f1a1d56d3`.

The README tranche modified `docs/README.md`, `docs/plans/README.md`, `docs/specs/README.md`, `docs/systems/README.md`, `docs/super_events/README.md`, `docs/specs/condemnation_system_specs/README.md`, `docs/specs/006_independence_wave_specs/README.md`, and `docs/specs/019_infantry_spawn_specs/README.md`; it created `docs/formables/README.md`, `docs/spreadsheets/README.md`, and `docs/testing/README.md`.

It also corrected `chaos_redux_repo_cleanup_goal_prompt.md` and normalised the known hard-wrapped historical `interface_audit_2026-07-22.md` without changing its findings.

### Assets

No asset was created, converted, rewired, or visually redesigned by cleanup.

Four explicitly unreferenced Event 005 runtime DDS copies were deleted: `gfx/leaders/005_soviet_collapse/LID_leader.dds`, `RCD_leader.dds`, `RLD_leader.dds`, and `TRS_leader.dds`.

The durable archive manifest at [`docs/assets/portraits/005_soviet_collapse/user_supplied_runtime_2026-08-21/manifest.md`](../../assets/portraits/005_soviet_collapse/user_supplied_runtime_2026-08-21/manifest.md) records the retained provenance and absence of active consumers.

### Storage

The physical `.git` and Git LFS cleanup is documented in [`git_storage_cleanup_2026-08-22.md`](git_storage_cleanup_2026-08-22.md); it changed repository storage rather than tracked source files.

### Spreadsheet

The first bounded spreadsheet tranche aligned Event Details rows 001, 002, 007, 009, 010, 012, and 019. Event 016 required no prose correction because the existing D’Rhondan detail already matched the current wording.

The later catalog tranche expanded that work across Events 1–20: it synchronized 77 evolution descriptions and 12 public world-end descriptions, corrected the Event 3 and Event 5 workbook mismatches without changing the schema, aligned the five-value status legend, and regenerated all three export-only CSV files. The complete current catalog result is recorded under [Spreadsheet/catalog alignment](#spreadsheetcatalog-alignment).

## Helpers and triggers changed

Removed Event 003 helpers from [`common/scripted_effects/003_holy_realm_effects.txt`](../../../common/scripted_effects/003_holy_realm_effects.txt): `holy_realm_core_northern_indian_register_states`, `holy_realm_core_western_chinese_register_states`, `holy_realm_core_eastern_chinese_register_states`, and `holy_realm_prepare_final_silence`.

Removed Event 020 effects from [`common/scripted_effects/020_black_plague_rat_effects.txt`](../../../common/scripted_effects/020_black_plague_rat_effects.txt): `black_plague_rat_set_initial_evolution_ready_day`, `black_plague_rat_load_evolution_log_context`, and `black_plague_rat_record_current_evolution`.

Removed Event 020 evolution eligibility triggers from [`common/scripted_triggers/020_black_plague_rat_triggers.txt`](../../../common/scripted_triggers/020_black_plague_rat_triggers.txt): `black_plague_rat_evolution_i_is_eligible`, `black_plague_rat_evolution_ii_is_eligible`, `black_plague_rat_evolution_iii_is_eligible`, `black_plague_rat_evolution_iv_is_eligible`, and `black_plague_rat_evolution_v_is_eligible`.

Removed definition-only Event 020 country-target wrappers from [`common/scripted_triggers/020_black_plague_response_triggers.txt`](../../../common/scripted_triggers/020_black_plague_response_triggers.txt): `black_plague_country_has_clean_city_rats_target`, `black_plague_country_has_seal_food_stores_target`, `black_plague_country_has_clear_sewers_target`, `black_plague_country_has_flea_control_target`, `black_plague_country_has_transport_purge_target`, `black_plague_country_has_demolition_target`, `black_plague_country_has_emergency_hospital_target`, `black_plague_country_has_quarantine_target`, `black_plague_country_has_cordon_target`, `black_plague_country_has_treatment_target`, `black_plague_country_has_warren_purge_target`, `black_plague_country_has_countermeasure_target`, and `black_plague_country_has_doctor_wu_target`.

The current source scans found no live gameplay or meta-effect consumers for these removed names; remaining matches are historical handoffs and supersession notes, except for similarly named live capacity/state triggers that were not removed.

Removed the shared `modify_value_based_on_chaos_tier` effect and its matching API documentation after exact scans found no runtime, dynamic-name, scripted-localisation, GUI, GFX, documentation, or spreadsheet consumer.

Deleted the 28-key `005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml` duplicate after confirming every key exists in the canonical Event 5 localisation file. The canonical file supplies the current wording and was not edited by cleanup.

Two inert tag-switch bookkeeping blocks were removed from [`common/on_actions/chaosx_on_actions_system.txt`](../../../common/on_actions/chaosx_on_actions_system.txt), and the Event 013 selector branches were added to [`common/scripted_localisation/chaosx_scripted_localisation_settings.txt`](../../../common/scripted_localisation/chaosx_scripted_localisation_settings.txt).

No new helper or trigger was created.

## Constants changed

None.

No new script constant, file-scoped constant, tuning table, or balance value was introduced or changed.

## Overcomplicated code simplified

None beyond removing inert bookkeeping and unreferenced definitions.

The repeated Event Log helper pattern and shared dynamic-helper architecture were documented as candidates, but no broad abstraction was applied because ownership and runtime evidence were insufficient.

## Workflow patterns normalized

Event 001 confirmation options now use the shared `PDXO_OK` pattern.

Shared Event Details premise text now uses player-facing current-world language, and the Event 001, 002, 007, 009, 010, 012, and 019 catalog details follow that wording.

The Event 006 evolution-incident localisation file was column-aligned without changing keys or text.

The repeatable-event recovery comments now name the configured recovery rate and one recovery step rather than an obsolete fixed-multiple description.

Documentation links in the bounded Event 006 evidence were corrected to current paths, and retired helper references now carry explicit historical/supersession wording.

The shared dynamic-helper index now distinguishes helpers declared in `chaosx_dynamic_effects.txt` from cross-subsystem APIs and names the authoritative Event 006, Event 016, clone-system, Mengele-bridge, Event 019, and famine declaration owners.

## Code moved

None.

## New files created

Cleanup created documentation and handoff files only, including the bounded Event 003–006 and Event 013–020 plans, Event 001–010 and Event 011–020 audit reports, shared helper and migration baselines, decision/focus/country baselines, localisation and spreadsheet handoffs, repository map, docs/assets inventory, probability baseline, Git-storage report, README-management handoff, and the durable formables, spreadsheets, and testing README indexes.

No new gameplay script, localisation source file, interface file, GUI file, asset, spreadsheet, constant file, or generated MCP wrapper was created.

The sole remaining completion output is this report; the README-management handoff and its changes are already committed.

## Duplication removed

None as a broad refactoring category.

The cleanup removed duplicate/unused definition-only wrappers and inert assignments where current scans proved no consumers, but it did not merge shared systems or rewrite repeated Event Log logic.

## Dead code removed

The removed Event 003 and Event 020 helper families listed above were explicitly unreferenced or definition-only under the bounded source scan.

The two inert tag-switch bookkeeping assignments and four unreferenced Event 005 runtime DDS copies were removed.

The unconsumed Event 003 Final Silence triggerable-scenario localisation keys were removed from active localisation, with historical references retained in evidence.

The stale Event 011 unavailable Event Details key and the obsolete shared CBRN action Event Details key were removed from active localisation where current consumer scans supported removal.

The post-catalog closure removed superseded Event 1, Event 2, and Event 11 evolution-body wrappers and their private scripted-localisation methods, plus unused generic, locked, unrecorded, and Event 20 prefire body keys. Exact source, dynamic-localisation, GUI, GFX, documentation, and spreadsheet reference scans found no remaining live consumers.

## Dead code kept with reasons and dynamic-reference uncertainty

Compatibility callbacks, archived docs/assets, provider adapters, active scheduler/evolution owners, and current Black Plague capacity/state triggers were retained because their runtime or provenance role remains live or cannot be disproved by static references.

The reserved `clear_special_chaos_country_civilian_effects` hook was retained for its documented future cleanup contract. `damage_buildings_in_random_states` has no verified runtime caller but remains because the accepted Event 11 improvement addendum names it as a future sabotage implementation pattern.

Meta-effect provider families were retained because their dynamically constructed names are not safely discoverable by ordinary literal-reference scans.

Historical handoffs and audit observations were retained and marked superseded instead of deleted so provenance is not lost.

## Docs and localisation updates

The Event 003 overview now describes current Fallout ownership and treats Final Silence as retained cause memory/compatibility rather than a current independent public world-end route.

The world-threat documentation now points to `014_cannibalism_effects.txt`. A later exact repository scan found no remaining reference to the retired `014_cannibalism_logic_effects` filename after the isolated Event 014 source comment was corrected.

Two Event 016/018 implementation-jargon strings were rewritten in player-facing language.

Shared Event Details prose was corrected for communism, zombie outbreak, fury, white peace, and death, and the Event 011 unavailable key was removed.

Events 1–20 evolution descriptions and all public world-end descriptions were synchronized between the in-game Event Details selectors and the workbook. Mechanics-heavy, generic locked, and unrecorded placeholder bodies were replaced on the catalog description path while dynamic titles and gameplay logic were preserved.

The CBRN deaths display now uses integer formatting, the Fallout clean-certificate detail key was added, and unconsumed Event 003 Final Silence scenario strings were removed.

The localisation handoff records the focused read-only Event Details GUI inspection and its truncated global diagnostics; it does not claim a layout render passed.

## Spreadsheet/catalog alignment

The workbook is the authority and the CSV is export-only.

The exporter `python .tools/export_event_catalog_csv.py` completed after the workbook updates and produced 166 Event data rows with 14 columns, 14 Cluster rows with 7 columns, and 12 Scenario rows with 6 columns. Blank formatted rows below Event 166 remain empty and are not exported.

The workbook was reopened with its existing five sheets, dimensions, tables, validation, formatting, and formulas preserved, and the exported rows matched the workbook.

Current player-facing Event Details text was aligned for Events 001, 002, 007, 009, 010, 012, and 019. In addition, 77 Events 1–20 evolution cells and 12 public world-end entries now contain complete descriptions matching their in-game description keys rather than title-only text. Event 3's stale fifth evolution cell was cleared, and Event 5's additional `Fringe Breakaways` catalog row remains combined with Evo V because the approved workbook layout has no Evo VI column.

The workbook status validation now exposes exactly five values: `Playable`, `Partially Available`, `To Be Reworked`, `Unavailable`, and `Needs Testing`. No Event row is marked `Playable`; Events 1–20 are `Needs Testing`, post-20 IDs with an actual `chaosx.nr<ID>.1` root definition are `To Be Reworked`, and IDs without that root definition are `Unavailable`. A final root-definition scan corrected IDs 46, 99, and 100 from `Unavailable` to `To Be Reworked`. Event counts remain 20 `Needs Testing`, 81 `To Be Reworked`, 65 `Unavailable`, and zero `Playable`; the current Cluster sheet contains eight `Partially Available` and five `Unavailable` rows, while all eleven Scenario rows are `Needs Testing`.

## Skills used or updated

The [`chaos-redux-subagents` skill](../../../.agents/skills/chaos-redux-subagents/SKILL.md) was read and applied for ownership, evidence, audit, and handoff boundaries.

The `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-super-events`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-mtth`, and `xlsx` skills were used for their respective event/log/catalog, decision, super-event, focus, asset/provenance, timing, and workbook rules. The event skill's catalog status contract was updated to preserve the five-value status vocabulary and prevent events from defaulting to `Playable`.

The official `skill-creator` instructions were consulted to assess whether the cleanup revealed a reusable skill gap; no new skill or non-trivial skill update was justified.

The required offline Paradox wiki core pages and relevant vanilla documentation were consulted before repository inspection.

The cleanup evidence was reconciled from the event, decision/mission, focus, country, localisation, spreadsheet, asset, super-event, MTTH, improvement-loop, and storage handoffs produced through their respective project workflows.

No skill was created, and no central MCP skill or wrapper was created.

## Meaningful validation performed

Current source rescans found no live gameplay or meta-effect consumers for the removed Event 003/020 helper names; remaining occurrences are historical evidence and explicit supersession notes.

The Event 003 post-change partial lint reported zero blocking diagnostics in its retained artifact, and the Event 013 GUI inspection covered functional selectors without a layout rewrite.

Localisation and spreadsheet checks confirmed the changed keys, BOM/alignment requirements, workbook/export row agreement, and Event Details wording alignment.

The catalog synchronization resolved all 178 mapped evolution/world-end title and body keys, found no duplicate mapped body keys, and confirmed that each mapped key is consumed by its selector. Workbook validation confirmed the five exact status options, the Event-sheet 20/81/65/0 distribution, exact agreement with all 101 root event definitions, blank-ID row emptiness, 166 exported Event rows, and exact Legend agreement for status, Type, Member Severity, evolution, and World-End values and fills.

Read-only source-reference rescans covered stale Event Details keys, old triggerable-scenario keys, removed helper names, and the corrected cannibalism path.

The storage handoff recorded exact deletion counts, LFS verification, multi-pack-index/commit-graph refresh, and recovery boundaries; fresh checks also returned exit code 0 for `git fsck --connectivity-only --no-dangling` and `Git LFS fsck OK` for `git lfs fsck --objects`.

Event render attempts timed out after 180 seconds, several inspect traces were partial, GUI aggregate diagnostics were truncated, and weighted-logic pools/probability comparisons were incomplete or transport-closed; these are limitations, not passing validation.

No live game testing was performed; live game testing belongs to the user.

## Behavior changes

Event 013 settings and last-event selectors now display Event 013 correctly.

Shared Event Details and catalog premise text now describes the current player-facing event situations for the corrected event set.

Evolution and public world-end detail panels now show stable in-world descriptions that match the spreadsheet catalog instead of effect lists, generic lock text, or title-only spreadsheet entries. Event titles, dynamic title states, gameplay effects, balance, and GUI layout are unchanged.

The Event 001 confirmation buttons use the standard shared confirmation localisation.

The CBRN death count display is integer-formatted, and the Fallout clean-certificate detail is available through its new localisation key.

The removed dead/inert definitions have no intended behavior change, and the repeatable recovery edit is comment-only.

No balance change, probability target, new trigger, new gameplay helper, or code-move migration was implemented.

## Rejected candidates

Broad generic helper extraction, Event Log reset-helper consolidation, shared registry-constant conversion, Event 006 registry migration, Event 019 meta-provider API migration, scheduler ownership changes, and global event-target lifecycle changes were rejected for this safe tranche because exact runtime ownership and rollback evidence were not available.

The Event 020 weighted literals were not centralised because the required probability-compare route was unavailable or incomplete.

The old Event 020 absorption no-op observation was rejected as stale against current source ownership and was not treated as a defect.

The four empty `chaos_warfare_system_audit` directories were not deleted, and no top-level docs/assets workspace was deleted.

No interface layout or coordinate change was accepted, and no broad `on_daily`, `on_weekly`, or other whole-world iteration was introduced.

## Deferred migrations

The shared migration queue in [`shared_system_migration_plan_2026-08-22.md`](shared_system_migration_plan_2026-08-22.md) remains deferred pending exact engine semantics, focused MCP evidence, named probability scenarios, and parent approval.

Deferred items include shared event-name selector consolidation beyond the safe Event 013 branch, scheduler and registry ownership, Event 006 registration, Event 019 dynamic provider APIs, global event-target lifecycle cleanup, Event Log functional helper extraction, and risky helper/constant consolidation.

Deferred event/package work includes Event 002 specialised models, Event 006 package/portrait/rights/focus/probability/audio gates, Event 016 reserved helper and asset disposition, Event 017 live testing, Event 018 probability and 3D proof, Event 019 provider odds and assets, and Event 020 weighted and asset evidence.

History rewrite and large repack remain deferred; reachable 20.83 GiB pack history was intentionally retained.

## Remaining risks

There is no live game or new-save validation evidence, so runtime behaviour beyond static and MCP evidence remains a user-owned risk.

Event renders and several MCP inspections timed out or remained partial, and weighted-logic pools did not produce complete probability comparisons.

Events 006, 016, 018, and 020 retain package, provenance, probability, visual, or reserved-helper uncertainty, while Events 002, 010, 011, 013, 015, and 019 retain narrower asset/archive gaps.

Static absence of a helper name cannot disprove dynamic meta-effect, scripted localisation, or external/generated references; the retained helper list records that uncertainty.

The worktree contains substantial unrelated concurrent changes, including Event 014, Event 016, and Event 020 GUI/interface work; those changes are not cleanup evidence and must be reviewed separately.

## Docs/assets cleanup

The original docs/assets inventory counted 3,939 tracked paths, zero non-ignored untracked paths, and 16,774 ignored paths, with 2,544 modified tracked paths. The 2026-08-24 refresh found 23 physical top-level workspaces before empty-directory cleanup, 28,427 files, 56,979,143,899 bytes, 4,090 tracked paths, 2,568 modified tracked paths, and 24,341 ignored paths. The three additional active workspaces are Event 014, Event 019, and the famine-and-migration system.

No top-level docs/assets deletion was approved because remaining workspaces are active, blocked, recent, unresolved, or provenance-bearing.

The four empty `docs/assets/chaos_warfare_system_audit/` subdirectories and their empty parent were removed after exact path containment and zero-file checks. No asset, manifest, handoff, Git path, or recoverable content was deleted.

Contradictory optimistic and blocked package manifests were retained as provenance rather than merged or deleted.

The four Event 005 runtime DDS copies were the only cleanup-owned asset deletions, and their archive manifest remains durable.

README management under `f1a1d56d3` covered the 74 README files present in that snapshot. A current filesystem rescan covers 95 README files, including later active provenance packages, and reports zero broken local targets.

## .git/storage cleanup

The original stale-file cleanup and the 2026-08-24 follow-up removed 143 files totaling 444,747,725 bytes: 128 old `.git/objects/*/tmp_obj_*` files totaling 391,617,334 bytes and 15 allowlisted top-level scratch files totaling 53,130,391 bytes.

The cleanup did not use a recursive broad deletion and did not rewrite history.

Git LFS remote-verifying prune deleted 31,791 cached files reported as approximately 21 GB and retained 15,113 LFS files totaling 3,800,310,194 bytes afterward.

Six current object-temp files totaling 6.59 MiB, reflogs/logs, and `.git/lfs/tmp` contents were deliberately retained. No object-temp file older than 14 days remains.

The multi-pack index and commit graph were refreshed, `git gc --auto` was run, reachable 20.83 GiB pack history was retained, and history rewrite/large repack was deferred.

Current object inventory reports 243,103 in-pack objects across four packs, 20.84 GiB packed, six garbage files, and 6.59 MiB of retained recent garbage; the follow-up connectivity check is clean and the earlier Git LFS fsck remains recorded.

## GUI boundary

Functional Event Log, Event Details, selectors, registries, and scripted bindings were in scope; the Event 013 selector mapping was corrected and functionally inspected.

No cleanup-owned `interface/*.gui` layout, geometry, coordinate, hierarchy, or main-GUI rewrite occurred.

Shared Event Details localisation changes are content changes, not GUI layout changes.

Unrelated concurrent Event 014, Event 016, and Event 020 GUI/interface commits are explicitly excluded from this cleanup claim.

The timed-out or truncated GUI artifacts are recorded as limitations and do not establish a layout pass.

## Simplifications, omissions, and blockers

No unapproved fallback, placeholder gameplay implementation, balance shortcut, or design-changing substitute was introduced by cleanup.

The safe tranche intentionally omitted broad migrations, source abstractions, dynamic constant changes, probability tuning, layout changes, top-level docs/assets deletion, history rewriting, and live game testing.

Mandatory MCP routes were attempted for the supported in-scope surfaces; where routes timed out, were partial, or returned incomplete pools, static review was not treated as equivalent proof and risky candidates were deferred.

Repository-wide README management is current for the safe documentation boundary: the original 74-file inventory was reconciled, and a later 95-file filesystem rescan includes ignored active provenance READMEs and reports that all local README targets resolve.

The known accidental mid-sentence hard wrapping in the historical [`interface_audit_2026-07-22.md`](interface_audit_2026-07-22.md) was normalised without changing its findings.

The cleanup goal prompt now points to the current [`chaos_redux_repo_cleanup_master_prompt.md`](chaos_redux_repo_cleanup_master_prompt.md) filename.

The documentation audit also retains superseded Event 016 improvement-loop and mandatory-continuation prompts, while Event 012 and Event 007 goal/coding prompts remain design/routing material rather than current status authority.

## Source-of-truth and disposition ledger

The current source-of-truth map and historical contradiction handling are recorded in [`documentation_cleanup_2026-07-29.md`](subagent_handoffs/documentation_cleanup_2026-07-29.md) and [`repo_map_2026-08-22.md`](subagent_handoffs/repo_map_2026-08-22.md).

| Plan or handoff | Disposition |
|---|---|
| Events 001–010 cleanup audit | Bounded safe findings implemented; wider event statuses remain mixed, with render timeouts and live-validation gaps retained. |
| Events 011–020 cleanup audit | Bounded safe findings implemented; wider event statuses remain mixed, with probability, asset, and live-validation gaps retained. |
| Event 003–006 bounded cleanup plan | Bounded removals, evidence corrections, localisation cleanup, and archive cleanup implemented; Event 006 remains HOLD/PARTIAL. |
| Event 013–020 bounded cleanup plan | Event 013 selector and dead-helper cleanup plus Event 016/018 text fixes implemented; broader Event 013–020 work remains partial or deferred. |
| Shared helper architecture baseline | Recorded; no generic helper extraction approved. |
| Shared-system migration plan | Queued and deferred pending parent approval and stronger MCP/engine/probability evidence. |
| Decision/mission baseline | Read-only audit; candidates deferred, rejected, or blocked rather than blindly patched. |
| Focus baseline | Read-only audit; layout and AI candidates deferred. |
| Country-package baseline | Read-only audit; no safe country deletion or source change. |
| Localisation baseline and patch | Implemented and reconciled with active consumers. |
| Spreadsheet alignment and follow-up | Implemented through workbook edits and exporter output. |
| Events 1–20 catalog descriptions and status policy | Implemented through in-game selector/localisation synchronization, workbook updates, skill guidance, and regenerated exports. |
| Docs/assets inventory | Approved retention; no top-level deletion. |
| Git-storage cleanup report | Physical cleanup implemented and verified; history rewrite deferred. |
| Event 017 repo explorer report | Historical evidence retained with supersession notice from `49dad024c`. |
| Event 020 rat-system audit | Historical helper observations retained with supersession notice from `49dad024c`. |
| README management handoff | Implemented in `f1a1d56d3`; 74 README files were inventoried at that revision, three durable indexes were created, and a current 95-file rescan reports zero broken local targets. |

## Contradictions, duplicate documents, and stale instructions

The principal contradiction was historical Event 003/020 documentation describing helper families as current after their safe removal; `49dad024c` and `e77ae8965` now mark those observations as superseded while preserving the original audit evidence.

The Event 003 Final Silence documentation was reconciled to current Fallout ownership while retaining compatibility/cause-memory context.

The world-threat documentation path and the isolated Event 014 source comment are corrected. An exact current-repository scan found no remaining reference to the retired cannibalism filename.

Event 006 package manifests and handoffs contain both optimistic and blocked dispositions; the contradiction is preserved because it reflects provenance and unresolved admission gates, not a safe deletion candidate.

Events 017 and 018 have positive static evidence but remain `Needs Testing`; Event 018 still has open probability and 3D proof, so neither was silently promoted.

The Event 002 base package is current while specialised model packages remain blocked; no package-wide completion claim is made.

The shared helper baseline identifies possible orphaned helpers, but dynamic references and ownership are uncertain; no deletion was made.

Duplicate or superseded material was not deleted: historical Event 017 and Event 020 reports were annotated, Event 016 prompts remain marked superseded, and the 2026-07-29 documentation cleanup remains a historical map with current pointers.

Remaining prompt/instruction hazards are superseded Event 016 improvement-loop and continuation prompts plus older Event 012/Event 007 goal or coding prompts that must not be mistaken for current status authority; the cleanup-goal master-prompt path is corrected.

Recommended parent decisions are whether to schedule the shared migration phases, how to resolve Event 006 HOLD and Event 016/018/020 open gates, and when user-owned live validation can be recorded.

## Exact tracked path ledger

The cleanup owns 82 tracked paths when this completion report and the cleanup-plan README are included. This count excludes unrelated paths that happened to share a mixed commit.

Gameplay and script paths:

- `.agents/skills/chaos-redux-events/SKILL.md`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/scripted_effects/003_holy_realm_effects.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/scripted_effects/020_black_plague_rat_effects.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_triggers/020_black_plague_rat_triggers.txt`
- `common/scripted_triggers/020_black_plague_response_triggers.txt`
- `events/001_communism_spread.txt`

Localisation paths:

- `localisation/english/005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml` (deleted)
- `localisation/english/001_communism_spread_l_english.yml`
- `localisation/english/002_zombie_outbreak_l_english.yml`
- `localisation/english/006_independence_wave_evolution_incidents_l_english.yml`
- `localisation/english/011_secret_alliance_l_english.yml`
- `localisation/english/015_utopia_manifesto_evolutions_l_english.yml`
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml`
- `localisation/english/018_resources_found_system_l_english.yml`
- `localisation/english/018_resources_found_decisions_l_english.yml`
- `localisation/english/020_black_plague_evolutions_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/condemnation_sanctions_l_english.yml`
- `localisation/english/fallout_consolidated_l_english.yml`

Spreadsheet paths:

- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
- `docs/spreadsheets/chaos_redux_events_catalog.csv`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`

Deleted runtime asset paths:

- `gfx/leaders/005_soviet_collapse/LID_leader.dds`
- `gfx/leaders/005_soviet_collapse/RCD_leader.dds`
- `gfx/leaders/005_soviet_collapse/RLD_leader.dds`
- `gfx/leaders/005_soviet_collapse/TRS_leader.dds`

Documentation paths:

- `docs/README.md`
- `docs/events/003_holy_realm/overview.md`
- `docs/formables/README.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_fsm_micronesia_civic_source_clearance_2026_07_24.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw045_bashkiria_portrait_runtime_2026_08_14.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw048_udm_boris_berman_portrait_source_gate_2026_08_15.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw048_udm_boris_berman_portrait_source_search_followup_2026_08_15.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw053_altai_portrait_source_research_2026_08_15.md`
- `docs/plans/017_random_faction_plans/repo_explorer_report.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-24_rat_system_country_package_audit.md`
- `docs/plans/README.md`
- `docs/plans/repo_cleanup/chaos_redux_repo_cleanup_goal_prompt.md`
- `docs/plans/repo_cleanup/event_003_006_bounded_cleanup_2026-08-22.md`
- `docs/plans/repo_cleanup/event_013_020_bounded_cleanup_2026-08-22.md`
- `docs/plans/repo_cleanup/git_storage_cleanup_2026-08-22.md`
- `docs/plans/repo_cleanup/interface_audit_2026-07-22.md`
- `docs/plans/repo_cleanup/README.md`
- `docs/plans/repo_cleanup/repo_cleanup_completion_report_2026-08-22.md`
- `docs/plans/repo_cleanup/shared_system_migration_plan_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/ai_probability_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/country_cleanup_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/decision_cleanup_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/docs_assets_cleanup_inventory_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/docs_readme_management_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/events_001_010_cleanup_audit_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/events_011_020_cleanup_audit_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/events_1_20_catalog_description_sync.md`
- `docs/plans/repo_cleanup/subagent_handoffs/events_1_20_catalog_dead_localisation_cleanup.md`
- `docs/plans/repo_cleanup/subagent_handoffs/focus_cleanup_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/localisation_cleanup_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/localisation_cleanup_patch_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/repo_map_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/remaining_safe_cleanup_2026-08-24.md`
- `docs/plans/repo_cleanup/subagent_handoffs/shared_helper_architecture_baseline_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/spreadsheet_cleanup_alignment_2026-08-22.md`
- `docs/plans/repo_cleanup/subagent_handoffs/spreadsheet_cleanup_alignment_followup_2026-08-22.md`
- `docs/specs/006_independence_wave_specs/README.md`
- `docs/specs/019_infantry_spawn_specs/README.md`
- `docs/specs/README.md`
- `docs/specs/condemnation_system_specs/README.md`
- `docs/spreadsheets/README.md`
- `docs/super_events/README.md`
- `docs/systems/README.md`
- `docs/systems/event_system/events_log_evolutions_and_clusters.md`
- `docs/systems/event_system/events_log_world_end_scenarios.md`
- `docs/systems/world_threat_mechanic.md`
- `docs/testing/README.md`

Physical `.git` scratch and LFS cache deletions are not tracked paths; their exact categories, counts, and safety boundary are recorded in the Git-storage section and report.

## Current completion status

The dated cleanup commits and the post-catalog localisation closure implement the accepted bounded improvements, documentation navigation, catalog alignment, storage cleanup, and safe dead-code removals described above.

An unconditional current-repository completion claim is not made. Later concurrent Event 006, Event 014, Event 016, Event 019, Event 020, famine-system, asset, and documentation edits overlap audited surfaces; current MCP event, focus, GUI, and probability reruns timed out or remained incomplete.

Broad or design-changing migrations remain explicitly planned and deferred. This report is the durable handoff for cleanup-owned work and its current blockers, not proof that later concurrent work has completed every repository-wide validation gate.
