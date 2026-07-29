# Event 006 League Expulsion Decision Audit and Patch Handoff

Date: 2026-07-22
Scope: Event 006 league expulsion acceptance gap only (DM-60).

## Result

Implemented the bounded, charter-governed patron-client expulsion action. It deliberately recognizes only the already-recorded patron-client breach; it does not infer any other breach from wars, claims, or diplomatic disagreements.

## Changed files and identifiers

| File | Identifiers / change |
| --- | --- |
| `common/decisions/006_independence_wave_decisions.txt` | Adds targeted decision `independence_wave_call_charter_expulsion_vote` (DM-60); captured members cannot begin or complete ordinary league actions while the enforcement window is open. |
| `common/scripted_triggers/006_independence_wave_decision_triggers.txt` | Adds `is_independence_wave_charter_compliant_member`, `is_independence_wave_charter_expulsion_authority`, and `is_valid_independence_wave_charter_expulsion_target`; DM-60 counts as an active league crisis. |
| `common/scripted_effects/006_independence_wave_decision_effects.txt` | Adds `independence_wave_decision_resolve_charter_expulsion_vote` and `independence_wave_decision_fail_charter_expulsion_vote`; clears `independence_wave_last_charter_expulsion_vote_date` during decision cleanup. |
| `common/scripted_effects/006_independence_wave_effects.txt` | Preserves a captured member in the league ledger solely for enforcement, adds `independence_wave_expel_league_member`, and retains the existing discredited-member idea lifecycle. |
| `common/scripted_effects/006_independence_wave_achievement_effects.txt` | Adds `independence_wave_achievement_record_member_expulsion`, the missing writer for `independence_wave_achievement_member_expulsion_during_term`. |
| `common/script_constants/006_independence_wave_decision_constants.txt` | Adds named DM-60 duration, cooldown, member minimum, success losses, and failure losses. |
| `localisation/english/006_independence_wave_decisions_l_english.yml` | Adds DM-60 name, description, cost, start, success, and failure text. |
| `docs/events/006_independence_wave/overview.md` | Documents the captured-member enforcement window and its bounded outcome. |
| `docs/achievements/006_independence_wave/achievements.md` | Records the completed-expulsion disqualifier and its validation coverage. |

## Before and after behavior

Before this patch, choosing the patron-client route immediately removed a league member, leaving no charter enforcement, no time or resource commitment, no explicit grounds, no league fracture transaction, and no writer for the leadership-term expulsion disqualifier.

After this patch, the patron-client route removes founder status but holds an existing league member in the aligned ledger as a non-compliant, non-operational enforcement target. The current recognized leader can spend the existing strategic palette and one civilian factory commitment to open a 120-day targeted vote, provided the anti-puppetry charter is active, at least four members are present, and no other league crisis is running. Completion revalidates authority and the target before removing every aligned membership row, applies named five-value losses, lowers patron capture, starts a league-crisis evaluation, and records the achievement disqualifier. Cancellation or invalidation spends the committed resources, applies the smaller named failure losses, and cannot remove a stale target.

## Decision category lifecycle

| Decision | Owner / category | Region / target | Requirement | Duration and cost | Success | Failure / cleanup | Duplicate protection |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_call_charter_expulsion_vote` | Current Event 006 league leader; `independence_wave_league_category` | Capital state of a captured league member | Active origin, exact current-leader target, formal/durable/reformed phase, anti-puppetry charter, aligned ledger, at least four members, valid non-self client target, no active league crisis | `independence_wave_decision_duration.charter_expulsion_vote` (120 days); existing strategic command power, stability, war-support, train-or-convoy cost and civilian-factory commitment | Removes the target with `independence_wave_unregister_league_member`, keeps Event 006 origin/network membership, applies existing discredited-member idea lifecycle, reduces named league values, evaluates crisis, sets leadership-term disqualifier | Authority or target invalidation cancels; no stale target is removed; failure loses the committed resources and applies named cohesion/confidence losses; end-of-origin cleanup clears the recorded vote date | DM-60 is included in `has_independence_wave_active_league_crisis`; a 365-day re-enable cooldown follows each completed selection |

This task adds a targeted timed decision, not a mission. No decision-owned scripted GUI is involved; therefore no GUI inspection/render artifact applies.

## Audit findings, sorted by severity

| Severity | Finding | Disposition |
| --- | --- | --- |
| High | A captured member had no bounded expulsion transaction and the leadership-term expulsion disqualifier had no writer. | Resolved by DM-60 and `independence_wave_achievement_record_member_expulsion`. |
| High | Immediate removal on patron-client selection made a later targeted, charter-governed response impossible. | Resolved: existing members remain as non-compliant ledger targets until DM-60 resolves; new client routes still cannot register through the normal member helper. |
| Medium | A captured member could have completed a league action started before capture. | Resolved for contribution, recognition, arbitration, rescue, leadership challenge, and the two radical league missions by the compliant-member gate or cancellation checks. |
| Medium | The current written system has factual state only for the patron-client breach. | Intentionally unresolved: annexation, arbitration refusal, abandoned rescue, repeated violations, sponsored coups, and unauthorized wars need individual factual transaction writers before they can be valid targets. |
| Low | The specification permits a rival bloc outcome, but this architecture has no safe rival-bloc transaction. | Deliberately not implemented; DM-60 uses the existing discredited-member outcome and does not create a rival bloc. |

## Cost, requirement, AI, and route-lock notes

- DM-60 reuses the strategic cost predicate and payment effect rather than exchanging only political power: the existing palette supplies command attention, stability, war support, and train-or-convoy expenditure, with a temporary civilian-factory commitment.
- Conditions are encapsulated in named scripted triggers. Player text names the current leader, anti-puppetry charter, targeted patron-client ground, and dynamic four-member minimum rather than exposing raw trigger blocks.
- AI starts at the existing very-low base, increases for a valid captured target and durable cohesion, and decreases for the radical route. The target trigger prevents dead, inactive, self, non-member, and non-client targets.
- A captured actor is excluded from ordinary league actions during enforcement. In-flight recognition, arbitration, and rescue actions cancel if either participating member locks the client route. A captured leader also loses DM-60 authority.

## Localisation and cleanup notes

- All six player-facing DM-60 localisation keys are in the Event 006 decision localisation file, which retains UTF-8 BOM encoding.
- Resolution saves the state target's owner only as a regular event target and revalidates it inside the same effect chain; no global target needs clearing.
- The expulsion reuses `independence_wave_league_member_discredited` and the existing idea lifecycle instead of creating unconsumed state. Existing origin cleanup clears the flag and its ideas; decision-layer cleanup clears the DM-60 timestamp.

## Meaningful validation

- Read the required offline Paradox wiki core pages plus Decision Modding, and the vanilla decision and script-constant documentation before the patch; followed the existing Event 006 target and league-ledger precedents.
- Traced the full source path from patron-client selection through member registry reconciliation, DM-60 start/cancel/remove effects, membership unregister, idea refresh, achievement writer, and end-of-origin cleanup.
- Checked every added identifier has a definition and a consumer across `common`, `localisation`, and `docs`; confirmed the DM-60 localisation file begins with UTF-8 BOM.
- Ran `git diff --check` on the nine owned implementation/documentation files with no diff diagnostics.

Skipped meaningful validation: no HOI4 scripted-GUI surface exists for this decision, and no local engine parser or live scenario runner is available in this bounded subtask. Parent integration should exercise one successful vote, one authority-loss cancellation, and one target-invalidated cancellation in the Event 006 league scenario.

## Remaining issues and expansion handoff

DM-60 is complete only for the patron-client fact already written by Event 006. Expanding the target pool requires a separate broad mechanism plan for each accepted ground, including an objective writer, target visibility, resolution semantics, cleanup, AI incentives, and balance review. A rival-bloc branch likewise needs a dedicated safe transaction design; it was not approximated here.
