# Event 011 documentation state

## Current source-of-truth map

| Area | Current source |
| --- | --- |
| Historical source design | `docs/specs/011_secret_alliance_specs/specs/` parts 1-5 |
| Design matrices | `docs/specs/011_secret_alliance_specs/matrices/` |
| Final engine-compatible gameplay | Event 011 gameplay files at `407b9a05eb7024dd1728c4092fba2f1162efde9c` |
| High-impact balance implementation | Event 011 tuning at `1c87d9235319781c871c2948813ab55693eb8618` |
| Lifecycle, callback, wording, and catalog lineage | Commits `a1f47c0c`, `7563648f`, and `97a2da80` beneath the final freeze |
| Mechanic overview | `docs/events/011_secret_alliance.md` |
| Improvement-loop closure | `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_resolution.md` |
| Holistic completion verdict | `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md` |
| Source-package audit chronology | `docs/specs/011_secret_alliance_specs/handoffs/completion_audit.md` |
| Decision and mission audit chronology | `docs/plans/011_secret_alliance_plans/subagent_handoffs/decision_mission_audit.md` plus the final independent rescan recorded in the completion audit |
| Super-event implementation | `docs/super_events/011_secret_alliance_super_event_research.md` |
| Asset and animation evidence | `docs/assets/011_secret_alliance/asset_register.md`, `manifest.md`, `manifest_icons_ui_animation.md`, and `notes/validation.md` |
| Audio rights and conversion | `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md` and `docs/super_events/super_event_audio_packages.md` |
| Achievements | `docs/achievements/011_secret_alliance_achievements.md` and live definitions |
| Scenario | `docs/systems/triggerable_scenarios.md`, spec part 4, and live SCN-009 registration |
| Workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and `handoffs/spreadsheet_handoff.md` |

## Historical design disposition

The five-part specification and matrices remain the accepted source design. Planning-era implementation prompts, asset requests, spreadsheet directions, and completion statements are historical handoffs. They are retained for chronology but do not override verified gameplay behavior at `407b9a05` or the balance values frozen at `1c87d923`.

Early working labels are no longer current localisation authority. Stable identifiers and final player-facing wording are defined by the immutable event, scripted-localisation, Event 011 localisation, achievement localisation, scenario localisation, and super-event localisation files. The early no-manual-scenario direction is superseded by accepted SCN-009.

## Immutable implementation markers

| Surface | SHA-256 prefix |
| --- | --- |
| Decisions | `B22CC92A` |
| Constants | `2A635EE5` |
| Effects | `10B03E94` |
| Triggers | `A228DC3B` |
| Ideas | `D9C0C4D8` |
| MTTH | `8CE980BF` |
| Scripted localisation | `51F25FE3` |
| Events | `02046301` |
| Event 011 localisation | `6A42CEFE` |
| Achievement localisation | `6EE16E2B` |
| Scripted GUI | `C07907E2` |

## Current lifecycle notes

- Automatic Event Log evolution and reveal history is stored on the normal target only. Scenario, forced, debug, and AI-test origins do not create that history.
- Pending invitation, sponsor, `.4`, and `.5` content is bound to its exact target and phase. Counted `.50` delayed-call and `.51` through `.53` commitment callbacks plus pending `.190`, `.201`, and `.202` state must drain before automatic or scenario relaunch. Annexation releases a delayed-call owner's pending slot.
- Super-event slot `73` reads durable route, target, leader, member count, and faction-name grammar snapshots for 14 days. `.202` closes the context on day 15.
- The direct AI controller owns eight protections, Turn Member, and three wartime actions with exact state selection and 120/180/120-day cooldowns.
- Live family caps are two investigations, one protection, one diplomacy, one offensive action, one border action, and one emergency commitment. Retained counterintelligence is capped at 730 days.
- Scripted-GUI suspect selection refreshes the exact suspect-bound border pair and is locked while a conflict is unresolved.
- DM-15 through DM-20 and CA-01 through CA-13 are resolved at the immutable freeze.

## Plan disposition

| Planning item | Current disposition |
| --- | --- |
| Main five-part spec | Historical source design, implemented and retained |
| Historical research | Supporting source evidence |
| Super-event text research | Promoted; older Luke and Hamlet candidate superseded |
| Improvement-loop addendum | Accepted and fully disposed through the resolution record |
| High-impact balance plan | Implemented and frozen at `1c87d923` |
| Focus-tree expansion | Rejected as bloat |
| New country package | Rejected as contrary to procedural design |
| Formable | Rejected as unrelated |
| World-end branch | Not part of Event 011 |
| Triggerable scenario | Implemented as SCN-009 with five compositions and four intensities |
| Evolution III animation | Implemented with eight authored frames and a static fallback |
| Additional animated UI | Rejected as readability cost |

## Evidence status

- Final workbook SHA-256 is `597E71A1307958135BA1B34A8E60741320CD9E2753FA2EBDDBC1ED83403E1D59`; Event 011 and SCN-009 status cells are `Implemented`, and no formula error cells or formula error tokens remain.
- Audio ID `43` uses `Revelation`; final OGG and WAV duration is `86.101746` seconds at 44.1 kHz. Composition and federal-government recording rights are documented separately.
- The asset validator covers 57 runtime DDS targets, eight source and processed animation frames, one static fallback, and six achievement triplets.

## Resume note

The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this documentation-state map does not replace it. No accepted plan remains queued. No in-engine playtest is claimed by this scoped documentation record.
