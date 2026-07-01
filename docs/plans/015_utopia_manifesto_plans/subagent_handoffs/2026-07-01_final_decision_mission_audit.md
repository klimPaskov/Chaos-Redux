# Event 015 Utopia Manifesto Final Decision/Mission/Scripted GUI Audit

Date: 2026-07-01
Agent role: decision and mission subagent
Scope: `utopia_manifesto` decisions, missions, scripted effects/triggers, scripted GUI, ledger GUI, and related localisation.

## Verdict

Pass after local patches. The Event 015 decision, mission, timed-project, and scripted GUI surfaces are clean enough for completion from a decision/mission perspective, subject to the parent reviewing the wider dirty/untracked Event 015 batch before staging.

No broad mechanic handoff was needed. No fallback or simplification was used.

## Files Changed

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `interface/015_utopia_manifesto_ledger.gui`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_decision_mission_audit.md`

## Patched Findings

High: Needful Land arbitration and marked district survey could be opened concurrently.

- Before: `decision_utopia_boundary_arbitration` and `decision_utopia_mark_needed_district` each blocked their own active flag but did not block the other mission family. Scripted start effects also did not exclude states already flagged by the other family.
- After: both decision visible gates block the other active mission flag. `utopia_manifesto_start_boundary_arbitration_mission` and `utopia_manifesto_start_marked_district_survey_mission` now also exclude states flagged by the other mission.
- Changed ids: `decision_utopia_boundary_arbitration`, `decision_utopia_mark_needed_district`, `utopia_manifesto_start_boundary_arbitration_mission`, `utopia_manifesto_start_marked_district_survey_mission`.

High: Timed storehouse/integration projects could complete after target state control was lost.

- Before: `utopia_manifesto_complete_storehouse_project` always added the local storehouse flag/building/compliance rewards. `utopia_manifesto_complete_integration_project` always marked integration complete and could add a core if ledger/compliance gates passed, even if ROOT no longer controlled the state when the timer expired.
- After: both completion effects first clear the active project flag, then only apply rewards, integration completion, and core grants when `is_controlled_by = ROOT` still holds. Lost-control completions only decrement the corresponding active project counter.
- Changed ids: `utopia_manifesto_complete_storehouse_project`, `utopia_manifesto_complete_integration_project`.

Medium: Several custom costs could spend stability or war support without a matching centralized affordability trigger or clear tooltip.

- Before: open stores, just-cause review, marked district survey, and League storehouse aid had mixed raw checks or partial checks. League aid spent war support but did not require enough war support in the helper or describe it consistently.
- After: added constants and helper triggers for the missing affordability gates, then wired the decisions and localisation to those helpers.
- Changed constants: `utopia_manifesto_decision_fixed.open_stores_stability_requirement`, `utopia_manifesto_decision_fixed.just_cause_war_support_requirement`, `utopia_manifesto_decision_fixed.marked_bounds_stability_requirement`, `utopia_manifesto_decision_fixed.aid_war_support_requirement`.
- Changed triggers: `utopia_manifesto_can_pay_open_stores`, `utopia_manifesto_can_pay_just_cause_review`, `utopia_manifesto_can_pay_marked_district_survey`, `utopia_manifesto_can_pay_foreign_aid`.
- Changed decisions: `decision_utopia_open_stores`, `decision_utopia_just_cause_review`, `decision_utopia_mark_needed_district`, `decision_utopia_storehouse_aid`.
- Changed localisation: `utopia_open_stores_available_tt`, `utopia_just_cause_review_available_tt`, `utopia_just_cause_review_cost_text`, `utopia_just_cause_review_cost_text_blocked`, `utopia_just_cause_review_cost_text_tooltip`, `utopia_mark_needed_district_available_tt`, `utopia_mark_needed_district_cost_text_tooltip`, `decision_utopia_storehouse_aid_desc`, `utopia_storehouse_aid_cost_text`, `utopia_storehouse_aid_cost_text_blocked`, `utopia_storehouse_aid_cost_text_tooltip`, `utopia_storehouse_aid_available_tt`.

Medium: Ledger scripted GUI buttons had text but no player-facing hover explanation.

- Before: refresh, petitions, audit, and renunciation buttons exposed only short button text.
- After: added `pdx_tooltip` wiring and localisation for all four buttons.
- Changed GUI elements/localisation: `utopia_manifesto_ledger_button_refresh_tt`, `utopia_manifesto_ledger_button_petitions_tt`, `utopia_manifesto_ledger_button_audit_tt`, `utopia_manifesto_ledger_button_renounce_tt`.

## Lifecycle Notes

- Category lifecycle is coherent. `utopia_manifesto_ledger_category` is tied to the ledger route flag and the scripted GUI category. Rejection cleanup clears active mission flags and arrays, closing stale mission surfaces.
- No political power stores were found in the audited Event 015 decision/effect/trigger/scripted GUI/localisation files.
- No global event target storage remains in the audited Event 015 files. Boundary arbitration, marked district survey, and League aid use per-ROOT arrays and clear them during mission cleanup.
- State-targeted timed projects now fail closed on state control loss at completion. The current patch avoids free buildings, integration flags, and cores outside ROOT control while preserving existing timers and counter cleanup.

## Mission Quality Notes

| Mission | Owner/category | Region/target | Requirement | Duration | Success | Failure/timeout | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mission_utopia_harvest_rotation` | ROOT / `utopia_manifesto_ledger_category` | Domestic ledger economy | Ledger active and harvest route open | Existing constant duration | Surplus and vocation gains | Need/consent pressure on timeout | Low |
| `mission_utopia_household_guard` | ROOT / ledger category | Coast/shore defense surface | Household guard and valid security route | Existing constant duration | Defensive confidence and guard payoff | Suspicion/pressure on timeout | Low |
| `mission_utopia_boundary_arbitration` | ROOT / ledger category | Neighbor state array | Needful Land route, valid neighbor, no concurrent marked survey | Existing constant duration | Compensated settlement, charter/guarantee path, claim only | Public refusal/suspicion/overreach and possible outside guarantees | Low after patch |
| `mission_utopia_marked_district_survey` | ROOT / ledger category | Marked district state | Marked Bounds route, valid state, no concurrent arbitration | Existing constant duration | Claim/forced settlement risk, no instant core | Need/suspicion/pressure | Low after patch |
| `mission_utopia_league_aid_corridor` | ROOT / ledger category | Valid League/faction/neighbor target array | Foreign aid route and aid cost helper | Existing constant duration | Aid corridor confidence/member payoff | Suspicion/confidence loss | Low |
| `mission_utopia_renunciation_vote` | ROOT / ledger category | National vote | Overreach pressure and stability route gate | Existing constant duration | Marked Bounds renunciation cleanup | Consent/need pressure | Low |

## Cost And Requirement Clarity

- Costs are concrete and varied: equipment, support equipment, trains, convoys, command power, army/navy/air XP, manpower, stability, war support, compliance/state conditions, map targets, and route flags.
- The audited decisions do not use political power exchange loops.
- Newly centralized cost gates remove raw or hidden affordability mismatches for stability and war support spending.
- Player-facing cost text now matches the scripted cost surfaces for League aid and just-cause review.

## AI Validity And Route Locks

- Decision AI weights generally include zero-weight blocks for missing costs or unsafe route state. The marked district survey AI now also zeroes when the new affordability helper fails.
- Target triggers avoid dead or invalid targets in the audited Needful Land and aid surfaces: capitulated countries, invalid human/nonhuman route targets, war states, and already-selected state flags are blocked.
- Scripted GUI has `ai_enabled = no`, but its buttons mirror decision/effect functionality that the AI can reach through normal decisions. No separate scripted GUI AI path is required for this surface.

## Localisation And Tooltip Notes

- Ledger button tooltips are now wired and localized.
- Cost and availability tooltips now disclose stability/war support requirements that were previously implicit or incomplete.
- Mission timeout copy had already been expanded by the parent and remains consistent with the current success/failure semantics.

## Cleanup And Exploit Risk

- No instant free cores were found in Needful Land. Arbitration and marked district outcomes create claims/settlement pressure, while integration cores are gated behind timed administration, compliance, consent, overreach safety, and current ROOT control.
- No stale global target risk remains in audited files.
- Per-ROOT arrays for boundary arbitration, marked district survey, and League aid have cleanup hooks on mission resolution/rejection.
- Timed storehouse/integration projects no longer reward states that leave ROOT control before expiry.

## Validation

Meaningful checks run:

- `rg -n "political_power|add_political_power|save_global_event_target|clear_global_event_target|global_event_target" ...` over the audited Event 015 decision/effect/trigger/scripted GUI/interface/localisation files returned no matches.
- `rg -n "<=|>=" ...` over the same audited files returned no matches.
- Brace counts after patches:
  - `common/decisions/015_utopia_manifesto_decisions.txt`: 356 open / 356 close
  - `common/scripted_effects/015_utopia_manifesto_effects.txt`: 905 open / 905 close
  - `common/scripted_triggers/015_utopia_manifesto_triggers.txt`: 257 open / 257 close
  - `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`: 20 open / 20 close
  - `interface/015_utopia_manifesto_ledger.gui`: 36 open / 36 close
- Targeted ID checks confirmed new cost helpers/constants are called by decisions and that all four scripted GUI button tooltips have matching localisation.
- Offline wiki reference checked `Decision modding` timer semantics: `remove_effect` fires on timer expiry, while `cancel_trigger` ends a timer without `remove_effect`. This is why the state-control completion guard was patched.

Skipped:

- No live HOI4 launch or in-game click-through was run from this subagent.
- No full repository parse was attempted because the Event 015 batch and the wider worktree are dirty/untracked and the audit was scoped to decision/mission/scripted GUI surfaces.

## Remaining Risks

- The target Event 015 files are untracked in the current dirty worktree. Parent should review and stage only the intended Event 015 files.
- Broader non-decision systems, assets, focus integration, spreadsheet rows, and event completion are outside this final decision/mission/scripted GUI audit.

## Completion Status

Decision, mission, timed project, Needful Land claim/integration, scripted GUI button, cost/tooltip, AI route-lock, and cleanup surfaces are clean for completion from this subagent's scope after the patches above.
