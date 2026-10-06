# Event 023 Decision and Mission Audit — 2026-10-06

Scope: read-only adversarial review of the Event 023 decision and mission closure work, including both new projects, retaliation access, costs, project locks, AI routing, action density, and the inherited custom-cost rows aligned in this finish.

Status: the new decision and mission paths pass the source-level audit after the parent’s fixes. I found no remaining local gameplay patch for this bounded pass. The required decision MCP inspection did not return, so scenario-derived engine findings remain blocked.

## Findings ordered by severity

1. **P2 — Native decision selection behavior remains unverified.** One `hoi4_decision_inspect` call for `sov_nuclear_bombs_service_arsenal` (`mode=inspect`, `refresh=false`, actor `SOV`, named over-capacity production scenario) returned no result within 45 seconds and produced no artifact. The local Decision modding page says `custom_cost_trigger` chooses the normal or `_blocked` cost key and payment must be manually debited; installed `_documentation.md` assigns decision availability to `available`. The vanilla `AFG_cross_border_target_state` precedent displays a `command_power > 24.9` custom-cost trigger, omits that condition from `available`, and debits 25 command power in `complete_effect`. These sources establish the Chaos Redux shared-gate contract and its broad application, but they do not prove whether the engine independently blocks an unaffordable click. No runtime exploit claim is made.

2. **No remaining source-level project-lock issue.** The parent’s `sov_nuclear_bombs_interrupt_work_after_enemy_strike` runs before strike handling continues, clears pending service/development flags, removes each mission, and restores the service-held Readiness once. The service description states that the withdrawn Readiness returns and that the strike interruption does not refund spent supplies. The target-selection and authorization gates therefore do not retain either new project lock after confirmed enemy use.

## Category lifecycle and action density

Event 023 keeps one shared `sov_nuclear_bombs_command_category`, visible for the active Soviet event or a breakaway custody crisis, with one static picture and phase-filtered ordinary decisions. The new command development appears in custody under the selected doctrine; service appears in production only when the intact arsenal exceeds upkeep capacity and its other requirements pass. Neither adds a category, tab, or scripted GUI.

Source visibility yields at most five ordinary category rows in custody: doctrine reform, stockpile audit, counterintelligence, centralize authority, and command development. Hardening and reserve dispersal remain map-only task families. Production has at most four ordinary rows: service, delivery crews, command exercise, and stronger authentication; reactor expansion and batch assembly remain map-only. This is a source inventory, not MCP-rendered or engine-confirmed row evidence.

The two new mission flags are both in `sov_nuclear_bombs_event_no_active_project`, so the new projects cannot overlap each other or another project protected by that helper. Their missions expose one in-progress project row at a time. No wall of text or unexplained number dump was introduced: the development decision has doctrine-specific names, durations, and effects, while the service tooltip displays intact warheads against upkeep capacity, controlled reactor count, and the temporary Readiness hold.

## Mission quality

| Mission | Owner and category | Region and requirement | Duration and success | Failure, cancellation, duplicate risk |
| --- | --- | --- | --- | --- |
| `sov_nuclear_bombs_command_development_mission` | SOV; shared `sov_nuclear_bombs_command_category` | No map region. Requires a settled doctrine, unfinished doctrine development, and no active project; the Party branch additionally requires a capital threat. | 90 days; completion applies the doctrine-specific command development, clears pending, and requests AI phase review. | No timeout failure state exists; timeout is the planned completion. Invalid actor cancellation and confirmed-strike preemption clear pending and remove the project without applying an unfinished development. Duplicate risk is low because each doctrine’s development flag suppresses repetition and the project gate is shared. |
| `sov_nuclear_bombs_service_arsenal_mission` | SOV; shared `sov_nuclear_bombs_command_category` | No map region. Requires Evolution I, intact inventory above maintenance capacity, Readiness at least the threshold, no moratorium, no active project, and no cooldown/stabilization flag. | 60 days; completion restores held Readiness, raises Integrity, and starts 180-day stabilization plus a 360-day cooldown. | There is no separate timeout failure; timeout is the planned completion. Invalid actor cancellation or confirmed-strike preemption restores only this service’s held Readiness and clears pending; spent logistics supplies are retained on strike preemption as stated in the decision text. Duplicate risk is low because of the shared project gate, timed protection, and cooldown. |

## Costs, requirements, AI, and cleanup

All 71 Event 023 decisions with `custom_cost_trigger` now repeat the exact named `sov_nuclear_bombs_can_pay_*` predicate in `available`; the 63-row manifest is `docs/plans/023_sov_nuclear_bombs_plans/cost_gate_alignment_20261006.json`. The other eight were already aligned, including both new decisions. Both decision-level `available` blocks enforce the relevant phase and matching affordability predicate. Before payment, development rechecks its development purpose and security affordability; service rechecks service eligibility and logistics affordability in its start helper.

The 14 state-targeted paid decisions were checked individually for scope placement: all 14 carry the affordability helper in the country-level `available` scope, none places that gate under `FROM`, and all 14 invoke the payment helper outside a `FROM` scope in `complete_effect`. The existing cost helpers debit the same actor country evaluated by their affordability helpers.

`develop_command` uses the security profile: political power, support equipment, and manpower, each with its matching texticon. `service_arsenal` uses the logistics profile: command power, train equipment, and fuel, each with its matching texticon. The service Readiness decrease is a temporary held value restored on completion, cancellation, or confirmed-strike preemption; counting that temporary state change still keeps the action at four distinct types. No new cost exceeds the four-type limit, and no hidden fifth payment was found in either project.

The doctrine development branch is included in AI custody duty only when the security profile is affordable. The service branch is included in AI production duty only when the logistics profile is affordable. Decision and mission weights remain assigned to the separate probability auditor; this report does not claim weighted comparison evidence.

Pending cleanup is idempotent: service restoration clears its receipt variable before any subsequent cleanup path can pay it twice, and confirmed-strike preemption removes the mission without invoking timeout/completion effects. Service cannot be spammed through a short cycle because cooldown starts on completion and lasts longer than stabilization. No free-reward, refund, or repeat loop was found in the bounded paths.

## Remaining blockers and validation limits

- The one narrow `hoi4_decision_inspect` attempt did not return within 45 seconds; no scenario, artifact, or engine-derived availability result is claimed, and it was not retried.
- No live game was launched. Live campaign and save behavior remain with the user.
- The separate probability auditor owns the required baseline and comparison for Event 023 decision/mission weights.
- No gameplay source was edited by this subagent. This handoff is the only file written for the bounded audit.

## Evidence references

- Repository and skill guidance: `AGENTS.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md` sections on custom-cost affordability, mission lifecycle, project capacity, and cleanup; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Prior audit: `C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\phase2_history\023.md`, which listed the doctrine-development and service-action gaps before this closure tranche.
- Decision source: `common/decisions/023_sov_nuclear_bombs_decisions.txt`; project guard: `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`; closure guards: `common/scripted_triggers/023_sov_nuclear_bombs_closure_triggers.txt`; project effects and preemption: `common/scripted_effects/023_sov_nuclear_bombs_closure_effects.txt`; confirmed-strike call site: `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`.
- Cost pair audit: `docs/plans/023_sov_nuclear_bombs_plans/cost_gate_alignment_20261006.json`; cost definitions: `common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt` and `common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt`.
- Player text: `localisation/english/023_soviet_nukes_l_english.yml`; maintenance quote: `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`.
- Offline syntax/behavior references read directly: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` custom-cost section; installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` availability section; vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AFG.txt`, decision `AFG_cross_border_target_state`; installed effects documentation `remove_mission` entry.
