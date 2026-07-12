# Event 018 documentation curator handoff

Date: 2026-07-12  
Mode: documentation-only reconciliation  
Gameplay, localisation, assets, workbook, and Git commit: unchanged by this curation pass

## Result

The Event 018 documentation set is reconciled to the implemented and audited state. Accepted implementation changes are represented in the source specification package, the improvement loop is closed, the acceptance proof boundary is explicit, asset and audio wiring are documented as complete, and stale planning-stage claims have a current disposition without deleting their historical evidence.

The acceptance matrix contains 363 checked requirements out of 363. Fresh event-completion, selected-field UI and localisation, and asset and audio audits returned PASS after every finding was repaired and re-read. No RF item, required route, mapped surface, AI behavior, asset, text key, workbook field, plan disposition, or acceptance scenario remains unresolved.

## Current source-of-truth map

| Surface | Current source of truth | Status |
| --- | --- | --- |
| Accepted design | `docs/specs/018_resources_found_specs/` | Current. Parts 4 through 7 and the tuning matrix contain the accepted RF design promotions. |
| Implementation behavior | `docs/events/018_resources_found.md`, `018_resources_found_cave_country.md`, and `018_resources_found_helper_contracts.md` | Current. These describe the implemented field, cave-country, terminal, and helper lifecycles. |
| Definition-based acceptance | `018_static_acceptance_report.md` and `docs/specs/018_resources_found_specs/matrices/acceptance_criteria.md` | Current. Live engine execution was waived and is not claimed. |
| Fresh closure audits | `subagent_handoffs/final_event_completion_reaudit_handoff.md`, `ui_localisation_reaudit_handoff.md`, and `asset_audio_reaudit_handoff.md` | Current. All three strict verdicts are PASS. |
| Improvement-loop disposition | `improvement_loop_closure_handoff.md` and the closure table at the top of `018_resources_found_implementation_depth_addendum.md` | Current. RF-018-01 through RF-018-08 are closed. |
| Visual and audio package | `docs/assets/018_resources_found/manifest.md` and `audio_manifest.md` | Current. Runtime files, registrations, provenance, and handoffs are complete. |
| Static icon provenance | `docs/assets/018_resources_found/icon_generation_provenance_ledger.md` | Current. All 150 generated focus, idea/state, decision, and category assets have exact source, processed, runtime, use, prompt-family, and registration records. |
| Super-event research | `docs/super_events/018_resources_found_super_event_research.md` | Current. The final text, sourced quotations, licensed music, rights, hashes, live slots, and rejected candidates are reconciled in one authority. |
| Achievements | `docs/achievements/018_resources_found_achievements.md` | Current. Fifteen achievements and their evidence, disqualifiers, and three-state icon contract are documented. |
| Workbook alignment | `subagent_handoffs/spreadsheet_doc_worker_handoff.md` | Current. Event row, four evolution fields, world-end field, cluster, severity, and implementation status match the accepted in-game wording. |

## Promoted into the source specifications

| Item | Promotion |
| --- | --- |
| RF-018-01 | Part 4 and `matrices/tuning_and_balance_framework.md` record the accepted `6 + floor(score / 5)` opening-strength equation, 6 through 30 clamp, mandatory-package resource floor, score bands, and deterministic profiles. |
| RF-018-02 | Part 5 records the visible controlled-denial contract, delay on every attempt while prepared, interrupted-attempt persistence, one-time three-capacity subtraction, zero clamp, and consumption on successful activation. |
| RF-018-03 | Part 6 records cumulative Stone, Burrow, Scree, and adaptation spirits together with their map, spawn, objective, and AI consumers. |
| RF-018-04 | Part 4 records one shared Event Details chronology row per event-wide evolution tier while later fields retain their own physical progression. |
| RF-018-05 | Part 7 records the exact regional/global defeat classifier, incompatible-world-end guard, one-time reconstruction offer, and join, lead, or refuse lifecycle. |
| RF-018-06 through RF-018-08 | These are implementation and alignment closures. Their final wording, asset, documentation, and workbook facts are recorded in the focused handoffs and current implementation docs. They did not require a new source-design route. |

The spec README now points to the completed independent planner result. The planning-stage improvement review remains in the package as history, with a current-disposition note above its original record. The acceptance matrix now explains exactly what a checked item proves.

## Acceptance reconciliation

- 363 of 363 checkboxes are checked.
- Checked items are supported by current deterministic definitions, exact fixtures, focused static audits, registered runtime assets, documentation, or workbook evidence.
- The user explicitly waived launching Hearts of Iron IV. Checked engine-facing scenarios do not claim observed live gameplay, combat, campaign AI, GUI scale, music playback, or achievement unlocks.
- PG-01 through PG-06 are accepted under that static and definition-based proof boundary.
- The final event-completion auditor compared the latest implementation to the full package and returned PASS. The selected-field UI and localisation and asset and audio re-audits also returned PASS.
- The completion re-audit's 362-of-363 sentence records the snapshot immediately before the auditor authorized the parent to close its own checkbox. This reconciliation records the completed parent action and regenerated package manifest. The PASS verdict itself remains current.

## Superseded and historical records

The following files remain preserved for traceability. Their stale status claims are superseded as listed here.

| Historical record | Superseding disposition |
| --- | --- |
| `018_repo_explorer_map.md` | Its preimplementation status and open architecture questions are superseded by the implemented event docs, focused audits, static acceptance report, and improvement-loop closure. It remains the location and precedent map used during implementation. |
| `research/improvement_loop_review.md` | Its statement that no independent planner interface was available is a planning-stage fact only. The later independent planner returned `improvement_loop_closure_handoff.md` and closed RF-018-01 through RF-018-08. |
| `subagent_handoffs/scripted_system_architect_handoff.md` | A supersession note now marks its `/ 4` opening-strength formula and parent-integration warnings obsolete. The `/ 5` formula, mandatory-package floor, later integration, and current evidence are linked without erasing the early API record. |
| `subagent_handoffs/errorlog_acceptance_audit_handoff.md` | A supersession note now marks its acceptance-open verdict and latent defects as an older read-only snapshot. The log remains negative loader evidence only. Current acceptance is in `018_static_acceptance_report.md`. |
| `subagent_handoffs/event_chain_worker_handoff.md` | The event chain remains valid evidence. Its parent-owned decision, asset, presentation, achievement, workbook, and manifest dependencies were completed by later tranches and audits. |
| `subagent_handoffs/focus_tree_auditor_handoff.md` | Its gameplay and 65-focus audit remains valid. Its then-pending idea/state GFX dependency is closed by the country-package audit and consolidated asset manifest. |
| `subagent_handoffs/localisation_auditor_handoff.md` | Its earlier spoiler-masking evidence remains valid. Its 123-rendered and 132-total decision inventory and 1,517-key count are superseded by the fresh UI and localisation re-audit after the final two visible mission mappings and localisation repairs. The current inventory is 125 rendered decisions and missions, nine hidden clocks, and 1,569 unique dedicated Event 018 localisation keys. |
| `subagent_handoffs/final_event_completion_audit_handoff.md` | Its strict FAIL verdict and 34-second audio table are preserved as the pre-repair checkpoint. The fresh `final_event_completion_reaudit_handoff.md`, final audio manifests, and repaired implementation supersede that verdict and those cue lengths. |
| Generated art, GUI animation, achievement icon, super-event text, and super-event audio handoffs | Their production evidence remains valid. Their parent-wiring checklists are closed by the consolidated asset manifest, audio live-wiring map, current GFX/audio registries, and static acceptance report. |
| Original implementation snapshot inside `018_resources_found_implementation_depth_addendum.md` | Preserved as the reason for RF-018-01 through RF-018-08. The closure table at the top and `improvement_loop_closure_handoff.md` are the current disposition. |

## Rejected optional depth

The following ideas remain explicitly rejected for this completion pass:

- Evolution V
- a second cave country
- a commodity exchange or abstract resource currency
- a normal cave production economy
- a fourth doctrine
- hidden retaliation after successful full closure
- breadth-only incident or art expansion

These are optional extensions outside the accepted design. None is queued, omitted from a required route, or allowed to block completion.

## Asset and audio closure

The consolidated asset manifest states that the visual and audio package is complete and wired. Its current inventory includes 10 report images, 6 news images, 3 super-event images, the Oth-Kesh portrait and flag packages, 65 focus icons, 36 unique idea/state icons, 39 decision-family icons mapped across 125 visible decisions and missions, 5 category icons, 5 category pictures, 15 complete achievement triplets, and the selected-field UI package with five real-frame animation families and required static fallbacks. The provenance ledger records 150 unique generated static icons and category assets with one-to-one source, processed, runtime, and registration evidence.

The audio manifest states complete integration for visible slots 82 through 84 and audio IDs 54 through 56. It records unique 115-second, 110-second, and 109-second 44.1 kHz OGG cues, three WAV mirrors, source and recording rights, hashes, loudness, music helpers, sound wrappers, base sounds, music localisation, HTML catalogue entries, and playback selectors. No superseded 49, 50, or 51 Event 018 path remains.

The manifests do not claim in-engine playback or UI-scale observation. Those checks were waived and remain correctly disclosed as unperformed rather than converted into false live evidence.

## Queued and unresolved work

### Queued

- None. The plan-scoped Git commit is the parent handoff action after this documentation reconciliation, not queued Event 018 content.

### Unresolved

- No RF-018-01 through RF-018-08 item is unresolved.
- No accepted design promotion is unresolved.
- No asset, audio, localisation, workbook, documentation, or improvement-loop blocker is unresolved.
- No required surface, AI behavior, text key, plan disposition, or definition-based acceptance scenario is unresolved.
- Live engine scenarios were waived. They are not claimed and are not blockers under the accepted proof boundary.

## Files changed by this curation pass

- `docs/specs/018_resources_found_specs/README.md`
- `docs/specs/018_resources_found_specs/research/improvement_loop_review.md`
- `docs/specs/018_resources_found_specs/matrices/acceptance_criteria.md`
- `docs/specs/018_resources_found_specs/manifest.md`
- `docs/plans/018_resources_found_plans/018_static_acceptance_report.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/scripted_system_architect_handoff.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/errorlog_acceptance_audit_handoff.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/final_event_completion_reaudit_handoff.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/ui_localisation_reaudit_handoff.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/asset_audio_reaudit_handoff.md`
- `docs/assets/018_resources_found/icon_generation_provenance_ledger.md`
- `docs/super_events/018_resources_found_super_event_research.md`
- `docs/plans/018_resources_found_plans/documentation_curator_handoff.md`

## Simplifications, omissions, fallbacks, and blockers

No documentation simplification, source-design omission, fallback, or hidden blocker was introduced. Historical records were retained and labeled through current-disposition notes or this ledger. No gameplay, localisation, asset, workbook, or Git change was made by this documentation-only reconciliation.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-super-events`
- `chaos-redux-improvement-loop`

No skill was created or modified.
