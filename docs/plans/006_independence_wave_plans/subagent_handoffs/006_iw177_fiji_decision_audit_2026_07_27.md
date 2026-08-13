# IW-177 Fiji founding-congress decision and mission audit

## Scope and status

This audit covers only the IW-177 Fiji founding-congress category, its six timed paid decisions, its founding mission, the FIJ-specific lifecycle cleanup, and the immediate shared helpers they call.

The FIJ decision and mission tranche is audit-complete after one narrow FIJ-local duration correction.

This is not a completion claim for Event 006 or any other Pacific package.

## Sources consulted

The required offline wiki references were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

The decision-specific engine behaviour was checked against `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

Vanilla decision precedents reviewed were `common/decisions/AST.txt` for mission structure and `common/decisions/WTT_border_conflicts.txt` for timeout and cancellation handling.

The `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-focus-trees` skills were applied.

## Issue list, ordered by severity

### High, fixed: the decision-only route could not beat the founding-mission deadline

Fiji starts at 31 congress pressure and needs 62 to stabilize its congress.

The shortest legal decision-only route is Convene the Constituent Congress for 65 days, Register the Communal Veto for 50 days, Charter the Coastal Guard for 65 days, and either Open the Labor and Shipping Board or Settle the Colonial Accounts for 65 days.

That route takes 245 sequential days because the active-project trigger permits only one FIJ project at a time.

The previous shared founding-mission timeout was 240 days, so uninterrupted decision play failed before a valid pressure threshold could be reached.

`independence_wave_fij_hold_constituent_congress_together` now uses the FIJ-specific 250-day constant, which leaves a five-day completion window without changing shared Pacific mission timings, costs, rewards, or route requirements.

### Low, retained: the decision-only completion window is deliberately narrow

The corrected decision-only route has five days of slack, so losing capital control, running out of a paid resource, or intentionally cancelling a project remains consequential rather than recoverable by a free retry loop.

This is appropriate for the active crisis mission, but its exact live timing remains a user-owned in-game validation item because agents do not launch Hearts of Iron IV.

### Informational: generic cost copy is text-first rather than icon-first

All FIJ cost text resolves and matches its actual deductions, but the shared Event 006 custom-cost localisation spells out resources rather than presenting an icon-first compact cost line.

This is outside the FIJ-local patch surface and does not hide a cost or make a requirement ambiguous.

## Decision category lifecycle

`independence_wave_fij_founding_congress_category` is visible only while the FIJ package predicate is true.

The founding mission activates after `independence_wave_iw_177_setup_complete` and remains non-selectable through `available = { always = no }`.

The mission resolves when `has_stable_independence_wave_fij_congress` becomes true, fails on timeout or lost capital control while the package exists, and disappears if the package no longer exists.

The six decisions use completion flags for one-time visibility and `has_independence_wave_fij_active_project` to prevent concurrent construction of pressure.

Each decision has a cancellation path and applies the Pacific project-failure pressure loss if it is interrupted while the FIJ package still exists.

`independence_wave_cleanup_iw_177_fiji` removes the mission and all six decisions, clears FIJ ledger variables and completion flags, removes package ideas, resets the focus tree where appropriate, and retires the package chair.

The parent-added cleanup of `independence_wave_fij_founding_crisis_resolved` and `independence_wave_fij_founding_crisis_failed` was reviewed and is necessary and sufficient for a fresh FIJ package repeat-run.

No FIJ decision in this tranche saves an event target, so there is no decision-owned event-target cleanup obligation.

## Mission quality

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_fij_hold_constituent_congress_together` | FIJ | `independence_wave_fij_founding_congress_category` | Fiji | FIJ package, IW-177 setup, and neither resolved nor failed flag | 250 days | Stable FIJ congress sets the resolved flag through `cancel_effect` | Timeout or capital loss sets the failed flag and applies the project-failure pressure loss | None, because resolution or failure blocks reactivation and cleanup clears both terminal flags only when the package is retired |

The mission is correctly marked `is_good = no` and its timeout uses a player-facing failure tooltip before applying the state change.

## Decision costs, requirements, and effects

| Decision | Paid cost and duration | Route requirement and cancellation | Completion result |
| --- | --- | --- | --- |
| `independence_wave_fij_convene_constituent_congress` | Administration standard, 65 days, plus one temporary civilian-factory use | FIJ package, controlled capital, and no FIJ project | Pays command power and manpower, then sets the congress flag and adds standard pressure |
| `independence_wave_fij_register_communal_veto` | Administration light, 50 days | Convened congress, controlled capital, and no FIJ project | Pays command power and manpower, then registers the charter and improves the ledger |
| `independence_wave_fij_open_labor_shipping_board` | Diplomatic light, 65 days | Registered communal charter, controlled capital, and no FIJ project | Pays command power and either convoy or train capacity, then raises pressure and shipping access |
| `independence_wave_fij_settle_colonial_accounts` | Diplomatic light, 65 days | Living former host and no FIJ project | Pays command power and either convoy or train capacity, then applies the safe bilateral former-host settlement |
| `independence_wave_fij_charter_coastal_guard` | Security standard, 65 days | Convened congress, controlled capital, and no FIJ project | Pays manpower, Army Experience, infantry equipment, and support equipment, then raises pressure and defense readiness |
| `independence_wave_fij_ratify_island_compact` | Pacific island strategic, 90 days | Coastal guard, labor board, stable congress, recognized-or-later state, and no FIJ project | Pays stability, war support, command power, manpower, and convoys, then finalizes the compact and its major settlement |

Every custom cost has a matching `complete_effect` deduction helper, so the display-only custom-cost text is not mistaken for payment.

The diplomatic helper takes the convoy branch only with more than the required convoy reserve and otherwise spends trains, which matches its availability trigger and avoids a zero-resource completion path.

The FIJ ledger and congress-pressure helpers clamp their variables, so repeated deltas cannot exceed their intended bounds.

The former-host settlement changes bilateral ledger values only and creates no state transfer, core, claim, or war-goal effect.

The colonial-accounts decision intentionally does not require a controlled capital because it is an external bilateral settlement, while loss of the former host invalidates and cancels the project safely.

## AI, focus integration, and route locks

The six decisions have non-zero FIJ AI weights using existing urgent, high, or low constants.

The final compact has a guarded severe-host-threat multiplier and still requires stable congress and recognition, so it cannot bypass the route gates.

All decisions are self-scoped, and the only external target is protected by `has_independence_wave_living_former_host` in both visibility and cancellation logic.

The FIJ focus branch uses the same one-time effect helpers and blocks a focus while its corresponding decision is active, so focus and decision completion cannot grant the same settlement twice.

The focus tree was inspected only to confirm decision integration and was not modified by this audit.

## Localisation and tooltip notes

The category, mission, all six decisions, their descriptions, completion tooltips, and each custom-cost string have matching English localisation keys.

The mission failure and decision completion effects expose player-facing tooltips rather than raw trigger blocks.

No scripted GUI is owned by this category, so no GUI inspection or render artifact applies.

## Cleanup and exploit-risk notes

Cancelled projects keep their already-paid cost, do not set a completion flag, and apply a pressure loss, so cancellation cannot farm resources, units, equipment, claims, cores, or war goals.

Completed decision effects set one-time FIJ flags and are internally guarded by the same flags, preventing duplicate ledger rewards through focus or decision repetition.

Mission terminal flags are now cleared by FIJ package cleanup, preventing either a stale resolved flag or a stale failure flag from suppressing the mission after a legitimate fresh package setup.

No free-resource loop, unit loop, equipment loop, war-goal spam, core spam, or cooldown bypass was found in the FIJ tranche.

## Changes made

- `common/script_constants/006_independence_wave_pacific_constants.txt`
  - Added `independence_wave_pacific_duration.fij_founding_mission_days = 250`.
- `common/decisions/006_independence_wave_pacific_decisions.txt`
  - Changed `independence_wave_fij_hold_constituent_congress_together` to use the FIJ-specific duration constant.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fiji_decision_audit_2026_07_27.md`
  - Recorded this audit and narrow fix.

Before the change, the FIJ mission used the shared 240-day timer and the legal decision-only route needed at least 245 days.

After the change, only the FIJ mission uses the 250-day timer and all other Pacific founding missions retain the shared 240-day constant.

## Meaningful validation

- Traced each FIJ decision from availability and custom-cost trigger to its matching payment helper, completion effect, cancellation effect, and one-time completion flag.
- Calculated the shortest legal decision-only pressure route as 65 + 50 + 65 + 65 = 245 days and verified that it reaches the stability threshold from Fiji's starting pressure.
- Confirmed that `fij_founding_mission_days` has exactly one consumer, the FIJ mission, while HBX, Hawaii, and Micronesia continue to use `founding_mission_days`.
- Traced the parent-added resolved and failed mission flags through `independence_wave_cleanup_iw_177_fiji` and confirmed both are cleared with the mission, decisions, ledger variables, and FIJ route flags.
- Confirmed the English localisation references for the category, mission, six decisions, their effect tooltips, and all four cost families.

The weighted-logic MCP evaluation was skipped because the available selector did not expose an accepted decision-source schema for this local file, while every FIJ `ai_will_do` block is a direct constant score with at most one fixed threat modifier and was manually source-reviewed.

No Hearts of Iron IV session was launched, in accordance with repository policy.

## Remaining risks and recommended follow-up

The corrected decision-only deadline has only five days of slack, so live user validation should observe the mission's daily cancellation timing around the fourth decision completion.

No FIJ-local follow-up patch is required unless that live timing proves materially different from the documented mission semantics.

The shared text-first custom-cost presentation can be considered by the Event 006 owner as a separate visual-localisation pass, but it is not a functional FIJ blocker.

No broader decision system or plan addendum was created.
