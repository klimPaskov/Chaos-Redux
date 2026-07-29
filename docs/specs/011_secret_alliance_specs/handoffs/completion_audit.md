# Event 011 Secret Alliance completion audit state

## Status and boundary

The original version of this file audited the planning package before implementation. That planning verdict remains valid as historical source-design evidence, but its statements that gameplay, assets, audio, localisation, scenario registration, and workbook work had not started are superseded.

The final engine-compatible gameplay commit is `407b9a05eb7024dd1728c4092fba2f1162efde9c`, atop high-impact balance freeze `1c87d9235319781c871c2948813ab55693eb8618`. It also sits on lifecycle closure `a1f47c0c`, callback isolation `7563648f`, and wording/catalog reconciliation `97a2da80`. DM-15 through DM-20 and CA-01 through CA-13 are resolved, the decision specialist returned CLEAN, and the localisation/workbook audit returned FINAL CLEAN. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this source-package handoff does not replace it.

## Immutable audit hashes

| Surface | SHA-256 prefix |
| --- | --- |
| Decisions | `B22CC92A` |
| Script constants | `2A635EE5` |
| Scripted effects | `10B03E94` |
| Scripted triggers | `A228DC3B` |
| Ideas | `D9C0C4D8` |
| MTTH | `8CE980BF` |
| Scripted localisation | `51F25FE3` |
| Events | `02046301` |
| Event 011 localisation | `6A42CEFE` |
| Achievement localisation | `6EE16E2B` |
| Scripted GUI | `C07907E2` |

## Source-design coverage

The accepted five-part specification remains the historical source of design intent. The implementation covers the three-minor concealed opening, factionless preference, no initial target war, invitations, six operation families, Evolution I through III, major sponsorship, investigation and preparedness, exact border actions, public faction formation, hostile-war force call, state-driven reveal routes, direct scenario launch, role AI, faction settlement, assets, animation, audio, and six achievements.

The accepted later SCN-009 design supersedes the early no-manual-scenario direction. New countries, focus trees, formables, and a world-end branch remain deliberate exclusions because Event 011 is a procedural faction event involving existing countries. They are not implementation omissions.

## Decision and mission remediation

| Finding | Resolution preserved at final freeze `1c87d923` |
| --- | --- |
| DM-15, pre-war callbacks could settle before the public offensive | Public-war pulses and terminal evaluation require `secret_alliance_public_war_started`; the flag is set only after a leader or valid anchor is actually at war and is cleared during cleanup. |
| DM-16, Evolution III removed missions without lifecycle cleanup | Phase transition calls the exact investigation, crossing, and border-conflict cleanup before removing missions, so slots, targets, verification state, and controls cannot remain hidden and active. |
| DM-17, prepared border pair was not bound to its suspect | The pair stores suspect, attacker state, and defender state; currentness checks ownership, control, passability, adjacency, selection, and conflict state. Scripted-GUI select and clear actions refresh the pair and are blocked during an unresolved conflict. |
| DM-18, Defecting Envoy could launch without an objective | Availability requires a valid owned-and-controlled coastal objective. Resources and the investigation slot are not consumed until that state exists. |
| DM-19, revealed costs stopped refreshing | Dynamic costs refresh at reveal, public-war pulses, and relevant lifecycle paths before target-AI action selection. Display, affordability, and payment retain one shared value source. |
| DM-20, direct AI protections lacked exact states | AI protection selectors save valid industrial, border, stockpile, port or airfield, and continuity states before invoking the same project helpers. No valid state means no payment or project flag. |

The direct target-AI controller is the unique execution owner for eight protection projects, Turn Member, and three wartime actions. Their engine `ai_will_do` weights are blocked. The controller records successful action ownership and applies target-owned cooldowns of 120 days for protection, 180 days for Turn Member, and 120 days for wartime action. Cleanup resets both cooldown families and saved AI targets.

## Completion-audit remediation

| Finding | Resolution preserved at final freeze `1c87d923` |
| --- | --- |
| CA-01, reveal leader could be a planned exiter | Route-aware leader validity excludes turned, delayed, or fractured planned exiters while preserving precedence: designated first major, strongest major, strongest founder, then hostile-war anchor. |
| CA-02, wartime fracture was not a true exit | A fracture performs white peace, faction removal, active-member removal, and counted outcome state. Survivor and postwar-bloc logic excludes the exiter. |
| CA-03, border transaction identity and mission state were incomplete | Exact suspect and state identity, rail and unit gates, payment order, GUI reconciliation, reinforced-patrol mission state, and unresolved-conflict selection locks are aligned. |
| CA-04, the same member could be turned repeatedly | Turn eligibility and execution reject an already turned member. |
| CA-05, preemption could erase planned member outcomes | Planned preemption honors turned, delayed, and fractured outcomes; hostile-war reveal alone force-calls every valid active member. |
| CA-06, fractured reveal lacked explicit presentation wording | `super_event_73_desc_fractured` is an explicit route package distinct from hostile, controlled, player-forced, and weakened text. |
| CA-07, invitation and sponsor state could outlive cleanup | Pending flags, saved recipients, watchdog cleanup, and notification scopes are reconciled and cleared across accept, refuse, invalidation, timeout, and runtime cleanup. |
| CA-08, delayed `.4` and `.5` could display stale content | Each delayed visible event requires the exact fixed target and its current evolution phase before display. |
| CA-09, nonstandard origins could earn normal achievements | Forced, debug, AI-test, and scenario origins carry explicit disqualifying origin state and cannot earn normal-route achievements. |
| CA-10, Event Log history was not origin safe | Automatic Evolution II and reveal set durable target-owned history flags. Event Log names and details use actor-aware history helpers. Scenario and forced origins do not manufacture automatic-run evolution history. |
| CA-11, news and super-event text depended on live runtime scopes | Reveal copies route, target, leader, member count, and faction-name grammar into durable presentation state. All five route packages use presentation scopes and `GetSecretAlliancePresentationFactionName`; no generic route fallback exists. |
| CA-12, Sponsor Accountability used permanent history | The action uses a per-run Event 011 flag that cleanup resets. |
| CA-13, delayed callbacks could contaminate a later run | `.50` delayed member calls and `.51` through `.53` commitment releases use counted pending state; `.190`, `.201`, and `.202` own explicit pending flags and saved callback targets. Automatic and scenario relaunches require every family to drain. Annexation releases an annexed delayed-call owner's pending count. |

## Reveal presentation contract

Slot `73` and audio ID `43` open only after the public transaction has selected and snapshotted its route, target, leader, member count, and faction-name grammar. The slot remains visible for 14 days. Hidden `.202` clears the slot, audio identity, route snapshot, presentation targets, and grammar flag on day 15. Invalid-country lifecycle handling closes the same context early. The presentation context intentionally survives ordinary Event 011 runtime cleanup so settlement cannot erase or rename text while the slot is visible. Relaunch remains blocked until this context and counted `.50` through `.53` callbacks have also drained.

## Content and evidence status

| Surface | Current evidence |
| --- | --- |
| Event and evolutions | Entry `chaosx.nr11.1`, dynamic roster and sponsors, six operation families, rare assassination attempt `.21`, controlled, forced, fractured, and weakened Evolution III outcomes, and hostile-war convergence are implemented. |
| Counterplay | Source-aware Evidence, maintained Preparedness, exact state protections, seven investigation missions, exact border pair, a 65 percent preemption gate with 15/10/6 percent Evidence-scaled strain, and factual nonfarmable Resolve are implemented. One protection and one emergency commitment may be active at once. |
| AI | Role-aware `front_unit_request`, full-array suspect selection, shared direct-action helpers, explicit ownership, exact state selectors, and 120/180/120-day cooldowns are implemented. Dynamic political actions reserve 170 PP for the rounded 168 PP mixed-profile maximum at scale 2.2425. |
| Event Log | Automatic-only coordinated and public-reveal history uses durable target-owned actor flags. |
| Super-event | Five route packages, stable presentation faction helper, 14-day slot, day-15 cleanup, image, audio, quote, and remark are wired. |
| Audio | `Revelation`, audio ID `43`, exact final WAV and WAV duration `86.101746` seconds at 44.1 kHz. The 1901 composition and 1992 United States Marine Band federal-government recording have separate public-domain evidence. |
| Assets and animation | 57 runtime DDS targets, 38 transparent assets, 17 unique decision sources, seven idea sources, eight authored confrontation-emblem source frames, eight processed frames, one still fallback, and six achievement triplets passed the package validator. |
| Achievements | Six contracts use durable origin, evidence, reveal, capital, fracture, roster, and outcome facts. Every tooltip requires the player not to capitulate, relevant forced/debug disqualifiers are disclosed, and Two Giants uses in-world reveal wording. |
| Scenario | SCN-009 has five AI-only compositions and Low, Medium, High, and Maximum intensities with safe-pool and outcome snapshots. |
| Balance | High-impact freeze `1c87d923` uses long 90/120/180-day diplomacy, offensive, and emergency commitments, exact 150/135/190/150/190/100/140-day mission timeouts, no repeat-use cost multiplier, and a 730-day retained-counterintelligence ceiling. |
| Workbook | SHA-256 `597E71A1307958135BA1B34A8E60741320CD9E2753FA2EBDDBC1ED83403E1D59`; `Events!M12` and `Scenarios!F9` are `Implemented`; no formula error cells or formula error tokens. |

## Simplifications, omissions, and blockers

No accepted Event 011 route, evolution, scenario type, scenario intensity, achievement, animation fallback, visual package, or audio package is omitted. No gameplay fallback or substitute is documented.

The audit evidence is static and source based. It is not an in-engine playtest. The holistic verdict is maintained in the final completion-audit handoff rather than this historical source-package record.

## Current verdict

**Immutable implementation evidence reconciled.**

DM-15 through DM-20 and CA-01 through CA-13 remain closed through engine-compatible gameplay commit `407b9a05`, atop balance freeze `1c87d923`, and the wording/workbook audit is FINAL CLEAN. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`.
