# Event 015 Utopia Manifesto Decision/Mission Audit And Small Patch

Date: 2026-07-02
Agent role: decision and mission subagent
Scope: Event 015 `utopia_manifesto` decisions, missions, costs, target validity, scripted GUI parity, focus unlock integration, cleanup, and localisation/tooltips.

## Files Changed

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-02_decision_mission_audit_small_patch.md`

## Changed IDs

- `decision_utopia_household_census`

## Patch Summary

### Medium - Patched

`decision_utopia_household_census` ignored the existing focus unlock marker.

- Before: the decision appeared as soon as `utopia_manifesto_has_ledger = yes` was true, even though the focus `utopia_household_census` sets `utopia_manifesto_household_census_ready`.
- After: the decision is visible only after the ledger exists and `utopia_manifesto_household_census_ready` is set.
- Reason: this aligns the opening trunk with the rest of the Event 015 decision category, where focus progress stages decision clutter and unlocks concrete ledger work.

## Severity-Sorted Findings

### Critical

None found in the current Event 015 decision/mission surface.

### High

None left open from this pass. Earlier risks about global event targets and stale project counters appear stale in the current files: arbitration, marked district, and League aid now use per-country arrays, and `utopia_manifesto_cleanup_project_state` decrements active project counters before clearing active state flags.

### Medium

1. Patched: household census decision was not gated by the focus-set readiness flag.
   - Files/ids: `common/decisions/015_utopia_manifesto_decisions.txt`, `decision_utopia_household_census`, `common/national_focus/015_utopia_manifesto_focus_tree.txt`, `utopia_household_census`.
   - Risk before patch: early category clutter and an opening ledger action available before the focus intended to prepare it.
   - Resolution: added `has_country_flag = utopia_manifesto_household_census_ready` to the decision `visible` block.

### Low / Monitoring

1. Mission blocks still include `visible = { has_country_flag = ... }`. Per the decision wiki, `visible` does not control mission display the way it controls normal decisions. This is not currently harmful because the missions are explicitly activated, have active-flag `activation`, and use impossible `available` blocks so success/failure resolves through timeout handlers.
2. `decision_utopia_storehouse_audit`, `decision_utopia_collect_petitions`, and `decision_utopia_recognize_friend` use no direct material cost. They are not political-power stores and are constrained by cooldown, focus, ledger, or target gates, so I did not patch them.
3. League aid requires the initial material spend and reserve availability at timeout. Current mission description explains the reserve requirement, so this is a deliberate objective rather than a hidden extra spend.

## Decision Category Lifecycle Notes

- `utopia_manifesto_ledger_category` appears only for countries with `utopia_manifesto_has_ledger = yes` and hosts the ledger scripted GUI.
- `visible_when_empty = yes` is appropriate here because the category is also the ledger display surface, not only a list of decisions.
- Decisions are staged by completed focuses, route flags, ledger bands, active project caps, and active mission flags.
- Needful Land and Marked Bounds decisions block concurrent arbitration and marked survey missions.
- Rejection cleanup clears relationship arrays, mission target arrays, and active mission flags.

## Mission Quality Notes

| Mission | Owner | Category | Region/target | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mission_utopia_harvest_rotation` | ROOT | `utopia_manifesto_ledger_category` | country economy | active flag, ledger open, reserves and core control checked at timeout | `@utopia_harvest_rotation_days` / 110 | Surplus and vocation gains | Need rises and Consent falls | low, active flag blocks repeat |
| `mission_utopia_household_guard` | ROOT | ledger | defensive pressure route | active flag, Overreach safe, war or nearby pressure at timeout | `@utopia_guard_mission_days` / 120 | Consent and defensive record | Foreign Suspicion | low, active flag blocks repeat |
| `mission_utopia_boundary_arbitration` | ROOT and target | ledger / Needful Land | neighbor state array | Need proof, safe target, valid target-owned state, Overreach/Suspicion checks | `@utopia_arbitration_days` / 150 | compensated or guarantee-backed claim, no core | refusal, Need/Suspicion/Overreach pressure, possible outside guarantee | low, one arbitration or marked survey at a time |
| `mission_utopia_marked_district_survey` | ROOT and target | ledger / Marked Bounds | neighbor state array | hard clause open, safe state still owned and controlled by target | `@utopia_marked_survey_days` / 120 | risky claim and forced-settlement risk, no core | Need/Suspicion pressure | low, one arbitration or marked survey at a time |
| `mission_utopia_league_aid_corridor` | ROOT and target | ledger / League | friend, League, or faction target | valid target and reserve convoys, trains, support equipment at timeout | `@utopia_league_aid_days` / 150 | aid delivery, League member progress, confidence | Suspicion and confidence loss | low, active flag and target array clear on resolution |
| `mission_utopia_renunciation_vote` | ROOT | ledger / Marked Bounds exit | home politics | Overreach high and stability cost at start, Consent/Overreach checked at timeout | `@utopia_renunciation_vote_days` / 120 | hard clause renounced and Overreach reduced | Need rises and Consent falls | low, active flag blocks repeat |

## Cost And Requirement Clarity

- No Event 015 political-power store or flat political-power exchange was found.
- Concrete costs are present across command power, support equipment, trains, convoys, manpower, infantry equipment, motorized equipment, Army XP, stability, war support, compliance, resistance, state control, target safety, and timed missions.
- Custom costs have matching scripted effect spends in `common/scripted_effects/015_utopia_manifesto_effects.txt`.
- Needful Land claims require Need proof and a successful timed arbitration or marked survey. Claims do not grant instant cores.
- Cores are only granted through `utopia_manifesto_complete_integration_project` after local preparation, compliance, stable Consent, safe Overreach, and current ROOT control.

## AI Validity And Route-Lock Notes

- Targeted AI paths use target triggers that block dead, invalid, capitulated, major, at-war, non-neighbor, or stronger ordinary Needful Land targets.
- AI decision weights are present for every normal decision family. Claim decisions include zero-weight or low-weight route safety checks.
- Scripted GUI is human-only, but its actions mirror normal decisions/effects, giving AI equivalent access through the decision category.
- Focus integration is present for all audited decision unlocks. The patched census gate now uses the existing `utopia_manifesto_household_census_ready` focus flag.

## Localisation And Tooltip Gaps

- No missing localisation key was found for audited decision names, mission names, cost text, or custom trigger/effect tooltips.
- Mission descriptions now carry the timeout objective text because mission `available` is intentionally impossible until timeout.
- No localisation file was changed in this pass.

## Cleanup And Exploit-Risk Notes

- Per-country arrays are used and cleared for boundary arbitration, marked district surveys, and League aid.
- Active project counters decrement on normal completion and in `utopia_manifesto_cleanup_project_state`.
- No war-goal spam was found in Event 015 decisions. Claims are delayed to mission resolution and state flags prevent repeat claim marking.
- Free-unit surfaces are capped by scripted unit-family counters and costed decisions/focus calls. No repeatable uncapped unit decision loop was found in this pass.
- No stale broad cleanup hook was added. A broad all-country/on-action cleanup would exceed this subagent scope.

## Concrete Recommended Fixes

- Completed: gate `decision_utopia_household_census` behind `utopia_manifesto_household_census_ready`.
- No further small local fix is recommended from this pass.
- No broad improvement-loop plan was written because no broad decision/mission redesign gap was found.

## Validation

Meaningful validation run:

- Confirmed `utopia_household_census` sets `utopia_manifesto_household_census_ready`, and `decision_utopia_household_census` now checks it.
- Rechecked Event 015 decision/effect/trigger/scripted GUI files for political-power stores, global event targets, war goals, claim/core effects, mission timeout blocks, target arrays, and custom costs.
- Rechecked touched and adjacent script/gui brace counts after the patch:
  - `common/decisions/015_utopia_manifesto_decisions.txt`: 356 open / 356 close
  - `common/scripted_effects/015_utopia_manifesto_effects.txt`: 1010 open / 1010 close
  - `common/scripted_triggers/015_utopia_manifesto_triggers.txt`: 259 open / 259 close
  - `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`: 26 open / 26 close
  - `interface/015_utopia_manifesto_ledger.gui`: 44 open / 44 close

Skipped:

- No live HOI4 launch or in-game click-through was run from this subagent.
- No full repository parse was attempted because the worktree has extensive unrelated dirty and untracked files outside Event 015.

## Remaining Risks

- Wider Event 015 focus, asset, achievement, country package, spreadsheet, and super-event completion surfaces were not re-audited beyond the decision/focus unlock touchpoints needed for this task.
- The current worktree contains many unrelated dirty files. Parent should review and stage only this Event 015 decision patch plus this handoff if accepting the change.

## Skills Used

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-focus-trees` for the narrow focus unlock check

No skills were created or updated.
