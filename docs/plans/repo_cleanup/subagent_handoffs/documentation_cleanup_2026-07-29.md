# Chaos Redux documentation cleanup handoff

Date: 2026-07-29

Agent: `chaosx_documentation_curator`

Mode: documentation-only reconciliation in the shared dirty worktree; no commit created.

## Scope and authority

This pass covered the shared event-system documentation and the event-owned docs, specifications, plans, prompts, and handoff surfaces for Events 001 through 020. Event 021 and later were inspected only when a shared registration, settings, Event Log, or helper reference was relevant. Gameplay, localisation, GUI, GFX, binary assets, and the event catalog workbook were not edited.

The accepted source-design areas remain `docs/specs/<event>_*_specs/`. Current implementation-facing event records remain `docs/events/<event>/overview.md`. Plan folders and subagent handoffs remain evidence and working material with the dispositions below. The current filesystem and scripts were used only as evidence of documented ownership or path validity.

## Current source-of-truth map

| Event | Accepted design source | Current implementation or status authority | Current disposition |
| --- | --- | --- | --- |
| 001 Communist Insurgency | `docs/specs/001_communism_spread_specs/` | `docs/events/001_communism_spread/overview.md` | Current implementation record; no whole-event completion claim was introduced by this pass. |
| 002 Zombie Outbreak | `docs/specs/002_zombie_special_project_specs/` | `docs/events/002_zombie_outbreak/overview.md` | Canonical event record; stale main-file paths were corrected to the current tree. |
| 003 Holy Realm | `docs/specs/003_holy_realm_specs/003_holy_realm_buddhahood_specs/` for the accepted Buddhahood and Final Silence package; top-level `003_holy_realm_spec.md` retained as legacy provenance | `docs/events/003_holy_realm/overview.md` | Current route is documented; the package relationship is now explicit rather than unresolved. |
| 004 Random War | `docs/specs/004_random_war_specs/` | `docs/events/004_random_war/overview.md` | Current implementation record; no event-specific plan folder requiring promotion was found. |
| 005 Soviet Collapse | `docs/specs/005_soviet_collapse_specs/` | `docs/events/005_soviet_collapse/overview.md` and `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md` | Current accepted implementation map; older audits remain historical unless the source map supersedes them. |
| 006 Independence Wave | `docs/specs/006_independence_wave_specs/` | `docs/events/006_independence_wave/overview.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event_completion_audit_v33_2026_07_29.md` | Shared core milestone closed, but whole event remains `HOLD / PARTIAL` with country-package, focus, formable, provenance, and reachability boundaries. |
| 007 Fury | `docs/specs/007_fury_specs/` | `docs/events/007_fury/overview.md` and `docs/plans/007_fury_plans/007_fury_followup_addendum_after_partial_implementation.md` | Implementation surface and bounded follow-up are documented; this pass does not promote the event to a new whole-event completion state. |
| 008 Tensions Rising | `docs/specs/008_tensions_rising_specs/` | `docs/events/008_tensions_rising/overview.md` | Current implementation record; the planning-era `To Be Reworked` label is explicitly historical. |
| 009 White Peace | `docs/specs/009_white_peace_specs/` | `docs/events/009_white_peace/overview.md` | Current implementation record; no contradictory status surface was found in scope. |
| 010 Death | `docs/specs/010_death_specs/` | `docs/events/010_death/overview.md` and `docs/plans/010_death_plans/subagent_handoffs/event_completion_audit_latest_handoff.md` | Broadly implemented with no known static blocker in the latest handoff; live Event Details, scenario, world-end, and achievement validation remain useful and are not claimed here. |
| 011 Secret Alliance | `docs/specs/011_secret_alliance_specs/` | `docs/events/011_secret_alliance/overview.md` and its completion audit | Completion and balance freeze are already reconciled; no patch was needed. |
| 012 Africa | `docs/specs/012_africa_specs/` | `docs/events/012_africa/overview.md` and `docs/plans/012_africa_plans/documentation_cleanup_handoff.md` | Release candidate, not whole-event complete; current asset, runtime, language, carrier, world-package, and owner decisions remain explicit. |
| 013 Natural Disasters | `docs/specs/013_natural_disasters_specs/` | `docs/events/013_natural_disasters/overview.md` and current Event 013 completion evidence | Fresh implementation record; Event 046 remains inert and Event 099 remains a narrow bridge. Historical preimplementation maps are not current status. |
| 014 Cannibalism | `docs/specs/014_cannibalism_specs/` | `docs/events/014_cannibalism/overview.md` and its current re-audit references | Current implementation and audit record; the plan-side legacy helper removals are already documented. |
| 015 Utopia Manifesto | `docs/specs/015_utopia_manifesto_specs/` | `docs/events/015_utopia_manifesto/overview.md` and its frozen whole-event audit | Complete against the cited frozen static snapshot; no patch was needed. |
| 016 Brilliant Scientist | `docs/specs/016_brilliant_scientist_specs/` for design; `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` for current runtime | `docs/events/016_brilliant_scientist/overview.md` | Default-enabled core runtime is accepted; whole-event completion is not claimed because deferred flavor, report/news, 3D, and live-consumer work remain. Historical default-disabled wording is labeled as a snapshot. |
| 017 Random Faction | `docs/specs/017_random_faction_specs/` | `docs/events/017_random_faction/overview.md` and `docs/plans/017_random_faction_plans/subagent_handoffs/017_random_faction_event_completion_audit_handoff.md` | Static implementation and completion audit are PASS; catalog `Needs Testing` remains the user-owned live-validation boundary. |
| 018 Resources Found | `docs/specs/018_resources_found_specs/` | `docs/events/018_resources_found/overview.md`, `docs/plans/018_resources_found_plans/documentation_curator_handoff.md`, and the static acceptance report | Baseline and required static package are reconciled; live engine execution was waived and is not claimed. |
| 019 Infantry Spawn | `docs/specs/019_infantry_spawn_specs/` | `docs/events/019_infantry_spawn/overview.md` and `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md` | Final whole-event audit is PASS with no closure gate in the current record; older asset findings are retained as superseded evidence. |
| 020 Black Plague | `docs/specs/020_black_plague_specs/` | `docs/events/020_black_plague/overview.md` and `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md` | Core-stabilization tranche is source-complete for its declared mechanics, but shared completion remains partial because the Diseases cluster, public terminal world-end row, and paid Rat absorption payoff remain open; narrative expansion, bespoke 3D, presentation, extra scenarios, and live validation are also deferred. |

## Shared-system source-of-truth map

| Shared surface | Current authority | Boundary |
| --- | --- | --- |
| Random-event settings and manual firing | `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_guis/chaosx_scripted_gui_settings.txt`, and the event-system skill contract | Preserve automatic, manual, Event Details, cluster, FIFO, settings-gate, and `last_fired` behavior. |
| Random-event preparation and accounting | `common/scripted_effects/chaosx_logic_effects.txt` plus event-owned preparation helpers | Event-specific candidate logic stays event-owned; shared selection, accounting, and callback contracts require an inventory before any future move. |
| Event Log history, Event Details, evolutions, and clusters | `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, and `docs/systems/event_system/events_log_evolutions_and_clusters.md` | Parallel arrays, exact sequence binding, secondary actors, evolution previews, cluster rows, and rebuild entry points are current contracts. |
| World threat and shared cause records | `docs/systems/world_threat_mechanic.md` and current shared scripted effects | The current source flags and consumer mappings were retained; this pass did not change mechanics or claims. |
| GUI event-target conventions | `common/scripted_guis/chaosx_scripted_gui_settings.txt`, `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, and interface consumers | Existing `event_target:` patterns are valid and intentionally untouched. |

## Plan and handoff disposition ledger

| Package or document | Disposition | Reason and next owner |
| --- | --- | --- |
| Event 001 and Event 004 plan absence | Left unchanged | Their current event overviews are the available implementation records; no missing accepted plan was invented. Parent decides if a future bounded plan is needed. |
| Event 002 overview main-file list | Implemented documentation correction | Replaced deleted aggregate paths with `events/002_zombie_outbreak.txt`, the two Event 002 scripted helpers, `002_zombie_constants.txt`, the actual localisation file, and `docs/systems/event_system/events_log_evolutions_and_clusters.md`. |
| Event 003 top-level and nested specs | Promoted disposition note | Nested Buddhahood package is accepted current design; top-level spec remains legacy provenance. No source package was deleted. |
| Event 006 plan and audit family | Queued/HOLD/PARTIAL | Current overview and v33 handoff remain authoritative; unresolved package, focus, formable, provenance, and reachability work remains parent-owned. |
| Event 007 follow-up addendum | Implemented or explicitly bounded plan, retained | The addendum records implemented phases and remaining audit gates; this cleanup does not claim a new completion verdict. |
| Event 008 planning spec status | Historical status note added | The active `To Be Reworked` wording is now explicitly a planning-era snapshot while the event overview is current. |
| Event 010 plans and old audits | Retained with current pointer | Latest static audit is the current baseline; older blocker lists remain traceability and are not a request to restore the old event. |
| Event 012 plans and handoffs | Release-candidate disposition retained | Existing Event 012 cleanup handoff already reconciles stale asset wording and keeps open owner decisions visible. |
| Event 016 source map and package README | Historical snapshot reconciled | Current core-runtime handoff now controls default-enabled core status; old default-disabled and placeholder paragraphs remain historical. |
| Event 017 spec README and handoffs | Implemented/current pointer added | Completion audit is PASS; catalog `Needs Testing` is retained as live validation rather than a missing-content claim. |
| Event 018 spec README and closure handoffs | Static closure pointer added | Existing documentation curator handoff and static acceptance report remain current; no live-engine claim was added. |
| Event 019 older specialist audits | Superseded evidence, retained | Final completion audit and current overview control status; older asset-policy findings remain historical records. |
| Event 020 spec README and rat absorption follow-up | Core tranche pointer and partial shared-status note added; follow-up retained | `2026-07-29_event20_core_readiness_report.md` controls current core scope and explicitly leaves the Diseases cluster, public terminal row, and Rat absorption payoff open. The newly present `rat_absorption_follow_up.md` remains the accepted queued follow-up; the forbidden duplicate filename was not recreated. |
| Shared ownership separation | Deferred plan created at `docs/plans/event_system_plans/ownership_separation_migration.md` | Concentration is documented as a future architecture candidate only. No helper, array, ID, context, or GUI contract was moved. |

## Contradictions found and disposition

| Contradiction | Evidence | Disposition |
| --- | --- | --- |
| Event 002 overview listed deleted aggregate scripts and an old docs path. | `docs/events/002_zombie_outbreak/overview.md` versus the current `events/`, `common/scripted_effects/`, `common/scripted_triggers/`, `common/script_constants/`, and `localisation/english/` files. | Resolved by path-only documentation patch. |
| Event 003 README said the legacy and Buddhahood packages had no final relationship. | `docs/specs/003_holy_realm_specs/README.md` versus the nested Buddhahood package and current overview. | Resolved by marking the nested package current and the top-level spec legacy provenance. |
| Event 008 spec said `To Be Reworked` while the event overview describes the live runtime. | `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_spec.md` and `docs/events/008_tensions_rising/overview.md`. | Resolved by a historical-status notice; the original design body was not rewritten. |
| Event 010 package and catalog research retain planning-stage status language while the current overview and latest audit describe Death as implemented. | `docs/specs/010_death_specs/README.md`, `docs/specs/010_death_specs/research/010_death_source_processing_notes.md`, and `docs/plans/010_death_plans/subagent_handoffs/event_completion_audit_latest_handoff.md`. | README now points to the current baseline. Individual catalog/research wording remains historical and should be updated only through the workbook/documentation owner when exact current wording is available. |
| Event 012 README calls the package planning-only while the current event is a release candidate. | `docs/specs/012_africa_specs/README.md` and `docs/events/012_africa/overview.md`. | Resolved by a current RC pointer; open RC decisions remain visible. |
| Event 016 README and source-map body said default-disabled placeholder while the core-runtime handoff and overview say default-enabled core runtime. | `docs/specs/016_brilliant_scientist_specs/README.md`, `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`, and `016_core_runtime_handoff_map.md`. | Resolved by current-runtime pointers and historical-snapshot wording; deferred whole-event surfaces remain open. |
| Event 017 README said no gameplay files were edited and planning only while the current overview and completion audit are PASS. | `docs/specs/017_random_faction_specs/README.md` and the current Event 017 handoffs. | Resolved by moving the statement into a historical planning-intake note. |
| Event 018 README presents a source-design handoff without pointing to the implemented static closure. | `docs/specs/018_resources_found_specs/README.md` and the current documentation curator handoff. | Resolved by a static-closure pointer; live execution remains waived. |
| Event 020 README said the package did not claim gameplay code while the core-readiness report documents a source-complete stabilization tranche. | `docs/specs/020_black_plague_specs/README.md` and `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`. | Resolved by separating full-design provenance from the core tranche and deferred content. |
| Event 020 overview implied that the stabilization tranche left no active shared references unresolved while the current readiness report records missing cluster and public world-end registry rows and an unresolved Rat absorption payoff. | `docs/events/020_black_plague/overview.md` and `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`. | Resolved by making the shared-completion boundary explicit in the overview and spec README; gameplay registry work remains parent-owned. |
| Event 006 contains many package-level passes alongside a whole-event `HOLD / PARTIAL` status. | `docs/events/006_independence_wave/overview.md` and its v33 completion handoff. | Not a contradiction after scope separation; package passes do not promote the whole event. Parent must keep the HOLD boundary. |
| Older Event 019 asset audits report open source-policy issues while the final whole-event audit reports PASS. | `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_asset_army_independent_audit_2026_07_16.md` versus `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md` and the current overview. | Current final audit supersedes the older checkpoint; both remain preserved. |

## Duplicate or superseded document list

- The Event 003 top-level spec and nested Buddhahood package are intentionally both retained, with the top-level file now marked legacy provenance.
- Event 006 v28-v33 audits and older acceptance ledgers remain dated evidence; the current overview and v33 handoff control status.
- Event 012's older acceptance ledger and dated asset handoffs remain baseline evidence; the existing Event 012 documentation cleanup handoff controls current RC status.
- Event 013's preimplementation repository map is superseded for current status by the current overview and final completion evidence; its historical warnings remain useful for provenance.
- Event 016's 2026-07-14 source map body, historical asset manifests, and superseded planner or continuation prompts remain preserved; `016_core_runtime_handoff_map.md` controls current core status.
- Event 017's repository explorer report is a placeholder-baseline snapshot; the completion audit and current overview control current status.
- Event 018's early implementation and audit handoffs are superseded where the documentation curator handoff names fresh reaudits; no file was deleted.
- Event 019's older asset-policy audit and machine JSON are retained as historical or immutable evidence; the final completion audit controls approval status.
- Existing repo-cleanup handoffs remain separate ownership records and were not merged destructively into this file.

## Stale prompt or instruction list

- `docs/specs/016_brilliant_scientist_specs/prompts/016_brilliant_scientist_improvement_loop_planner_prompt.md` is explicitly superseded and must not be rerun without a new distinct gap.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_mandatory_continuation_prompt.md` is superseded by `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_resume_packet.md` and the current core-runtime map.
- Event 012's `prompts/africa_goal_prompt.md`, Event 007's coding and goal prompts, and Event 020's production prompts remain accepted design or routing instructions rather than current status reports; they were not rewritten to hide open work.
- Event 010 and Event 019 audit prompts remain historical process evidence where their handoffs already supersede a verdict; they should not be used as current completion status without the cited current handoff.

## Parent decisions recommended

1. Decide whether to start Phase 0 of the deferred shared ownership migration in `docs/plans/event_system_plans/ownership_separation_migration.md` after the current event-specific cleanup is stable.
2. Keep Event 006 at `HOLD / PARTIAL` until its current package, focus, formable, provenance, AI/source-proof, and reachability gates are resolved or consciously rejected.
3. Keep Event 012 at release candidate until the owner decisions in its existing cleanup handoff are resolved, especially carrier ownership, broader focus icon scope, world-package readiness, audio wiring, and native-language review.
4. Treat Event 016 as core-runtime accepted but whole-event incomplete until deferred presentation, flavor, 3D, and live-consumer surfaces receive their own bounded plans and evidence.
5. Treat Event 017 `Needs Testing`, Event 018 waived live execution, Event 019 static PASS, and Event 020's partial shared-completion boundary according to their current overviews rather than older planning files.
6. Use `chaosx_spreadsheet_doc_worker` for any Event 010 catalog wording reconciliation; this pass did not open or edit the workbook.
7. Decide whether Event 001's existing runtime picture set needs a future asset manifest reconciliation; this pass did not inspect binary assets and therefore makes no asset-completeness claim.
8. Keep the Event 020 rat-absorption follow-up queued under `docs/plans/020_black_plague_plans/rat_absorption_follow_up.md`, preserve the open Diseases cluster and public terminal-row registry gaps, and do not recreate the similarly named forbidden follow-up file.

## Cleanup actions performed

- Corrected Event 002 overview paths to current event, helper, constants, localisation, and shared Event Log files.
- Added explicit current-versus-legacy source disposition notes for Event 003.
- Labeled Event 008 planning status as historical without rewriting the accepted design body.
- Added current static or release-candidate pointers to the Event 010, 012, 016, 017, 018, and 020 README surfaces.
- Reconciled Event 020 overview and spec wording with the readiness report's partial shared-completion boundary and open registry/payoff gaps.
- Reconciled the Event 016 source-map implementation paragraph as a dated historical snapshot while preserving its evidence.
- Added the deferred shared ownership migration plan under `docs/plans/event_system_plans/`.
- Created this handoff as the current documentation ledger and resume packet for the parent.

No documentation file was deleted. No gameplay, localisation, GUI, GFX, binary asset, spreadsheet, or skill file was changed.

## Validation performed

- Checked every Event 002 path listed in the overview against the current filesystem before and after the correction; the old aggregate script and docs paths are no longer listed.
- Extracted 71 backticked `docs/` references from this handoff: 69 concrete paths resolve, while `docs/specs/<event>_*_specs/` and `docs/events/<event>/overview.md` are intentional ownership-pattern examples rather than literal filesystem paths.
- Used targeted `rg` scans for stale Event 008, 016, 017, 018, and 020 status phrases and manually confirmed that retained old wording is marked as historical or deferred rather than silently promoted.
- Confirmed the current Event 006, 012, 016, 017, 018, 019, and 020 status authorities from their event overviews and named handoffs.
- Confirmed the deferred ownership plan path exists under `docs/plans/event_system_plans/` and contains no gameplay edit instructions beyond future gated phases.
- Confirmed the Event Log GUI and shared docs continue to use the existing `event_target:` conventions; no migration or rename was applied.

Meaningful validation skipped: no HOI4 launch, parser/load run, live GUI interaction, binary-asset inspection, workbook readback, or gameplay scenario execution was performed because those surfaces are parent-owned or explicitly outside this documentation-only scope.

## Remaining risks

- Event-specific plan folders still contain many dated snapshots with contradictory historical counters; the current pointers above must be used until a future owner reconciles each package.
- Event 006 and Event 012 remain materially incomplete under their own current boundaries.
- Event 016 deferred content and Event 020 deferred content are intentionally not hidden by the current core-runtime notes.
- The shared ownership migration is only a proposal; moving helpers before a contract ledger would risk array alignment, Event 006 context, `last_fired`, sequence binding, or GUI target regressions.
- Current event overviews are documentation evidence, not proof of in-game execution; live validation boundaries remain as each event records them.

## Skills and references used

- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `AGENTS.md`
- Required offline wiki pages and relevant vanilla event, effects, triggers, script, and localisation documentation.

No skill was created or modified. No Git commit was created.
