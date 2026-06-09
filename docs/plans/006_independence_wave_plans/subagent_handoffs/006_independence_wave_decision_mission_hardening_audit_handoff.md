# Event 006 Decision and Mission Hardening Audit Handoff

Date: 2026-05-29
Owner: chaosx_decision_mission_auditor
Scope: Independence Wave package/ledger hardening tranche after parent edits.

## Skills and References Used

- Used `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`.
- Read `AGENTS.md`.
- Consulted offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Consulted vanilla documentation in `~/projects/Hearts of Iron IV/documentation/`, especially effects, triggers, localisation objects/formatters, script concepts, and script constants.
- Checked vanilla targeted and state-targeted decision precedents in `~/projects/Hearts of Iron IV/common/decisions/KOR.txt` and `~/projects/Hearts of Iron IV/common/decisions/AFG.txt`.

## Files Changed

- `common/decisions/006_independence_wave_decisions.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_decision_mission_hardening_audit_handoff.md`

No commits were made.

## Changed IDs

- `independence_wave_hold_capital_ministry`

## Patch Summary

Before:

- `independence_wave_hold_capital_ministry` activation excluded only `independence_wave_capital_ministry_failed`.
- After the timeout success set `independence_wave_capital_ministry_secured`, the mission could still satisfy its activation gate. Because its `available` block becomes true once the secured flag makes `can_independence_wave_host_take_capital_mission` false, a reactivated mission could immediately run the failure effect and mark the capital ministry failed after it had already been secured.

After:

- `independence_wave_hold_capital_ministry` activation also excludes `independence_wave_capital_ministry_secured`.
- The host capital mission closes cleanly after either success or failure and cannot re-arm into a contradictory failure.

This is local to one mission lifecycle gate and does not change balance, costs, targets, host release logic, or Event 005 content.

## Issue List

1. High, patched: `independence_wave_hold_capital_ministry` could reactivate after successful timeout and then immediately fire the failure effect. Fixed by adding the secured-flag activation guard.
2. Medium, not patched: Border Commission targeting is currently built from `is_core_of = ROOT` instead of named state groups or package-specific border definitions. This is safe from free transfer/coring, but it is broader and less package-aware than the improvement addendum asks for.
3. Medium, not patched: Border Commission costs are mostly political-power `cost = constant:*` with pressure/legitimacy changes in effects. The tranche has cooldowns and flags, but survey, parish petition, arbitration, and observer freeze would be stronger with equipment, command power, legitimacy, or local-support style requirements in later hardening.
4. Medium, not patched: `can_independence_wave_secure_compact_charter` accepts any one of member quorum, anti-puppet clause, or legitimacy. `independence_wave_proclaim_regional_compact` still blocks single-country formation, but the charter mission can mark the charter secured from one proof vector alone.
5. Low, not patched: `independence_wave_finish_regional_compact_integration` grants cores on every owned controlled state. This is outside the Border Commission and does not transfer states, but it should be revisited once package-specific proof and integration rules exist.

## Decision Category Lifecycle Notes

- `independence_wave_host_aftermath_category`: Opens from `independence_wave_host_aftermath_open`; host capital mission now has terminal success and failure guards.
- `independence_wave_committee_survival_category`: Uses one-time flags for recognition, brigades, and depot seizure; no repeat reward loop found in the audited tranche.
- `independence_wave_new_states_congress_category`: Anti-puppet clause is one-time by flag and route/petition-gated.
- `independence_wave_formation_ledger_category`: Ledger opens by flag, compact petition starts the charter mission, proclamation requires charter and compact proof, integration has success/failure terminal flags, and recovery clears failed integration for another attempt.
- `independence_wave_border_commission_category`: Opens through route/focus gates, requires a filed survey for state-targeted actions, applies a shared cooldown, and uses state flags to prevent repeated identical target actions.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_hold_capital_ministry` | Recent host | Host aftermath | Host capital ministry state | Keep an owned capital controlled for the full timer | 90 days | Timeout sets `independence_wave_capital_ministry_secured`, stability gain, anger relief | `available` becomes true when capital condition fails; sets failed flag, stability loss, anger gain | Fixed; terminal success now blocks reactivation |
| `independence_wave_compact_charter_window` | Compact founder | Formation Ledger | Compact member/charter proof | Wait through the charter window; timeout checks charter proof | 120 days | Timeout runs `independence_wave_secure_compact_charter` when gate passes | Timeout runs `independence_wave_fail_compact_charter` otherwise | Low; `available = { always = no }` is intentional for timeout-only resolution |
| `independence_wave_integrate_compact_ministries` | Formed compact | Formation Ledger | Compact-owned map and member state | Avoid subject status, low controlled-state count, or member shortfall | 120 days | Timeout integrates ministries and cores owned controlled states | `available` true on failure condition; discredits compact | Low for duplicate mission, medium for broad coring design risk |

## Cost and Requirement Clarity Notes

- Long formation requirements for preparation and proclamation use custom trigger tooltips.
- Normal `cost = constant:*` costs are engine-collected political power costs; no custom cost text is currently needed for those simple costs.
- Border Commission player text clearly says claims, arbitration, protected transfer petitions, ultimatums, and observer freezes do not immediately transfer districts.
- Further hardening should vary non-political costs for Border Commission actions once package-specific state groups and local support exist.

## AI Validity and Route-Lock Notes

- AI-usable decisions in the audited tranche have `ai_will_do`.
- Country-targeted compact decisions use `target_array` plus `FROM` as country; state-targeted border decisions use `FROM` as state.
- Compact invite/arbitration reject dead, self, war, and invalid member targets through target triggers.
- Border Commission route locks exist for civic, officer, national directorate, patron, and focus-based openings.
- Remaining route risk: protected transfer cannot yet check actual patron identity or target protector because that patron ledger is not implemented in this tranche.

## Localisation and Tooltip Gaps

- Localisation file keeps UTF-8 BOM.
- No `:0` localisation keys were found in `localisation/english/006_independence_wave_l_english.yml`.
- All 22 decision/mission IDs in `common/decisions/006_independence_wave_decisions.txt` have name and `_desc` keys.
- Border target labels use `[FROM.GetName]`, which is appropriate for state-targeted decisions.
- No missing player-facing keys found for the audited decisions.

## Cleanup and Exploit-Risk Notes

- Border Commission actions add claims/state flags/cooldowns/pressure variables. They do not call `transfer_state_to`, do not add cores, and do not erase hosts.
- Border target helper excludes capital states and owner state counts below the host survival floor.
- The shared border cooldown and state flags reduce repeated target spam.
- Parish claims increment `independence_wave_open_border_dispute_count`; arbitration, protected transfer, ultimatum, and freeze do not currently increment that count. This may be intentional if only filed claims count as open disputes, but it should be clarified before achievements or treaty settlement counters depend on it.
- No Event 005 decision/package content was added or modified.

## Validation Run

- `rg -n "<=|>=" common/decisions/006_independence_wave_decisions.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/script_constants/006_independence_wave_constants.txt localisation/english/006_independence_wave_l_english.yml`
  - No unsupported operators found.
- `rg -n "^[^#\\n]*:0\\s*\\\"" localisation/english/006_independence_wave_l_english.yml`
  - No `:0` localisation keys found.
- Python brace-balance check over the audited decision, trigger, effect, and constant files.
  - All reported `brace_balance=0` and `premature_closes=0`.
- Python localisation audit for decision IDs.
  - 22 decision/mission IDs found; no missing name keys; no missing `_desc` keys.
- Python BOM check.
  - `localisation/english/006_independence_wave_l_english.yml` starts with UTF-8 BOM.

## Skipped Validation

- No live HOI4 launch or in-game scenario validation was performed; subagent scope is file audit and narrow patch.
- No full Clausewitz parser is present in the repository; validation used targeted static checks and manual review against wiki/vanilla references.
- No broader Event 006 release resolver audit was performed beyond the allowed files.

## Remaining Recommended Fixes

1. Parent should decide whether Border Commission targets must move from generic `ROOT` core states to package-specific state groups before this tranche is treated as complete.
2. Add varied non-political costs to Border Commission decisions when local support, equipment, command power, or legitimacy requirements are available.
3. Clarify whether charter success should require member quorum plus one proof vector, or whether the current OR proof model is intended.
4. Revisit `independence_wave_finish_regional_compact_integration` once package-specific integration proof exists, because broad owned-state coring is safe from host transfer but may be too generous for later formable depth.
