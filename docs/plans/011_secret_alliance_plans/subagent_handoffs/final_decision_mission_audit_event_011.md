# Event 011 Final Decision and Mission Audit Handoff

Result: PASS after local patch.

Audit date: 2026-07-01

Scope audited:
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_decisions_missions_ui.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_map.md`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_guis/011_secret_alliance_scripted_gui.txt`
- `interface/011_secret_alliance_dossier.gui`
- `docs/events/011_secret_alliance.md`

References used:
- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding
- Vanilla docs under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`
- Vanilla decision and scripted GUI precedents under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`

## Changed Files

- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/final_decision_mission_audit_event_011.md`

The Event 011 gameplay files are currently untracked in git, so this patch sits on top of parent-owned Event 011 work. No unrelated Event 014 files were touched.

## Changed Identifiers

Effects:
- `secret_alliance_decision_counter_ultimatum`
- `secret_alliance_reveal_pact_by_war` call path, via `secret_alliance_decision_counter_ultimatum`
- `secret_alliance_start_prefire_evolution_iii_delay`
- `secret_alliance_emit_reveal_super_event`
- `secret_alliance_unlock_evolution_ii`
- `secret_alliance_decision_shield_factories`
- `secret_alliance_decision_strike_first`
- `secret_alliance_clear_current_member_state`
- `secret_alliance_cleanup_after_resolution`

Decisions:
- All 17 decisions using `secret_alliance_pp_low_cost_text`, `secret_alliance_pp_medium_cost_text`, or `secret_alliance_pp_high_cost_text`

Local file constants added:
- `@secret_alliance_three_knocks_window_days`
- `@secret_alliance_factory_shield_days`
- `@secret_alliance_counter_protocol_window_days`
- `@secret_alliance_super_event_visible_days`
- `@secret_alliance_pp_low_ai_hint`
- `@secret_alliance_pp_medium_ai_hint`
- `@secret_alliance_pp_high_ai_hint`

## Before and After Behavior

Before:
- `secret_alliance_open_public_pact_crisis` correctly opened the public crisis without immediate faction formation or war.
- `secret_alliance_decision_strike_first` declared war directly and then called `secret_alliance_reveal_pact_by_war`.
- `secret_alliance_decision_counter_ultimatum` could cross the Evolution III readiness threshold, but only formed or announced the pact. It did not set `secret_alliance_war_reveal_member`, did not call `secret_alliance_reveal_pact_by_war`, and therefore did not join live pact members to war through the formal reveal helper.
- Several timed flags used temporary variables directly in `days =`, which repo guidance treats as unsafe for this engine surface.
- Patron event target cleanup checked `secret_alliance_role_patron` after clearing that same flag.
- Resolution cleanup cleared mission flags but did not immediately remove active Event 011 missions.
- Custom PP costs subtracted PP correctly in effects, but AI did not receive `ai_hint_pp_cost` for PP budgeting.

After:
- Public crisis still does not immediately form the faction or start war.
- Final counter-ultimatum pressure now prepares the public leader, has the public leader declare war on the target when no target-member war exists, saves that leader as `secret_alliance_war_reveal_member`, and calls `secret_alliance_reveal_pact_by_war`.
- If the public leader is already at war with the target, final counter-ultimatum pressure saves that leader as `secret_alliance_war_reveal_member` and calls the same war reveal helper.
- War reveal remains centralized in `secret_alliance_reveal_pact_by_war`, which confirms live members, forms or reuses the public leader faction, emits the reveal super-event, and joins live members through `secret_alliance_pull_live_members_into_reveal_war`.
- Static timed flags now use file-scoped `@` constants. The dynamic Evolution III prefire delay uses `meta_effect` to inject the computed day count.
- Patron global event target cleanup runs before the patron role flag is cleared.
- Resolution cleanup immediately removes the four Event 011 active missions.
- Every PP custom-cost decision now has a matching `ai_hint_pp_cost`.

## Issue List

High severity, patched:
- Final counter-ultimatum pressure did not enter the formal war reveal path. This broke the required design fact that formal reveal joins live members to war only on target-member war or final counter-ultimatum pressure. Patched in `secret_alliance_decision_counter_ultimatum`.

Medium severity, patched:
- Timed flag durations used variables directly in `days =` in several effects. Patched with file constants and one `meta_effect` for dynamic duration injection.
- Patron cleanup could leave `secret_alliance_major_patron` as a stale global event target because it cleared `secret_alliance_role_patron` before checking it. Patched.
- Resolution cleanup depended on mission cancel triggers instead of immediately removing active missions. Patched.

Low severity, patched:
- PP custom costs lacked AI PP budget hints. Patched with `ai_hint_pp_cost` entries.

Remaining low risk:
- `secret_alliance_form_anti_target_faction` creates the named Anti-[target] Pact when the public leader is not already in a faction. If the public leader already leads a faction, the helper reuses the existing faction and marks a block flag. This matches `docs/events/011_secret_alliance.md`, which says the war reveal "forms or reuses the public leader's faction", but it is a caveat if the strict design intent is always a freshly named faction.

## Decision Category Lifecycle Notes

- `secret_alliance_dossier_category` is visible only while `secret_alliance_target_has_active_pact = yes`.
- The category is separately registered in `common/decisions/categories/011_secret_alliance_categories.txt` with `visible_when_empty = yes`, dossier icon art, and the scripted GUI attachment.
- Dormant, investigation, protection, diplomacy, border, exposure, public crisis, and war decision families are phase-gated by active pact, public reveal, war reveal, known member, neighboring member, and Evolution III checks.
- Public crisis is opened by `secret_alliance_open_public_pact_crisis` and remains non-war until strike-first, target-member war reveal, or patched final counter-ultimatum pressure.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_rail_guard_mission` | Target country | Protection | Target home rail/junction surface | `secret_alliance_rail_guard_active` from `secret_alliance_guard_rail_nodes` | 70 days | `secret_alliance_secure_guarded_junctions` removes mission and resolves rail guard | `secret_alliance_timeout_rail_guard` boosts pact readiness and suspicion | Low. Flag and mission removal gate duplicates. |
| `secret_alliance_customs_corridor_mission` | Target country | Border/corridor | Neighboring live member frontier | Neighboring live member plus `secret_alliance_customs_corridor_active` | 60 days | `secret_alliance_close_customs_corridor` removes mission and resolves corridor | `secret_alliance_timeout_customs_corridor` increases readiness/suspicion | Low. Active flag blocks duplicate starts. |
| `secret_alliance_false_leak_mission` | Target country | Counter-intelligence | Dossier/intelligence surface | `secret_alliance_false_leak_active` from false leak decision | 45 days | `secret_alliance_exploit_false_leak` removes mission and resolves leak | `secret_alliance_timeout_false_leak` strengthens pact cohesion/readiness | Low. Active flag blocks duplicate starts. |
| `secret_alliance_protocol_deadline_mission` | Target country | Exposure/deadline | Public protocol pressure | `secret_alliance_protocol_deadline_active`, created by protocol deadline effect | 180 days | `secret_alliance_disrupt_protocol_deadline` removes mission and weakens pact readiness | `secret_alliance_resolve_protocol_deadline` opens public crisis on timeout | Low. Active mission and active flag checks prevent repeat activation. |

Mission implementation notes:
- All active missions use `days_mission_timeout`.
- `available = { hidden_trigger = { always = no } }` prevents instant mission completion.
- Each active mission has a paired player disruption/completion decision and a distinct timeout effect.
- `visible` on missions is harmless but not relied on for mission lifecycle, because HOI4 mission visibility behavior is limited. Activation, active flags, cancel triggers, paired decisions, and cleanup carry the lifecycle.

## Cost and Requirement Clarity Notes

- Costs are varied across PP, command power, support equipment, infantry equipment, and paired mission completion costs.
- Actual custom costs are charged in `complete_effect` helpers, not only displayed through `custom_cost_text`.
- PP custom costs now include AI hints: 17 PP custom-cost decisions, 17 `ai_hint_pp_cost` entries.
- Factory shield uses support equipment and a timed shield flag, now with a safe local duration constant.
- Custom trigger tooltips hide long raw conditions for player-facing requirements.
- Explicit scanned tooltip, custom-cost, custom-effect-tooltip, and GUI text references are present in `localisation/english/011_secret_alliance_l_english.yml`. Localisation files were not edited per task instruction.

## AI Validity and Route-Lock Notes

- Targeted member decisions exist and are bounded to `global.secret_alliance_members`:
  - `secret_alliance_embassy_registry_sweep`
  - `secret_alliance_member_backchannel`
  - `secret_alliance_publish_member_dossier`
  - `secret_alliance_watch_suspect_frontier`
  - `secret_alliance_targeted_fracture_signatory`
- Member target triggers require live, valid, known or neighboring pact members through `secret_alliance_known_member_target` and `secret_alliance_neighbor_member_target`.
- Target and member validity triggers exclude dead, capitulated, special, nonhuman, subject, existing-faction-with-target, and diplomacy-locked cases where relevant.
- Border decisions require a neighboring live member and do not expose impossible non-border routes.
- Scripted GUI has `ai_enabled = { always = no }` and no clickable gameplay buttons. AI interaction is through decisions and AI counterplay effects, not GUI clicks.

## Localisation and Tooltip Gaps

- No localisation files were edited.
- No missing explicit localisation keys were found in the scanned decision cost, available tooltip, effect tooltip, and dossier GUI text references.
- Dynamic faction naming still depends on the existing faction template and `secret_alliance_anti_target_pact` localisation outside this audit's localisation-edit scope.

## Cleanup and Exploit-Risk Notes

- Public crisis does not grant a free faction, free war, or immediate pact military join.
- Formal war reveal remains centralized and idempotent through `secret_alliance_war_revealed`.
- Strike-first directly declares war and uses the same war reveal helper.
- Final counter-ultimatum pressure now uses the same war reveal helper, avoiding a half-revealed faction state.
- Active mission completion decisions call `remove_mission` and clear active flags.
- Resolution cleanup now immediately removes all four active Event 011 missions.
- No free-unit loop, equipment farming loop, core spam, or repeat war-goal spam was found in the scoped decision/mission surface.

## Validation Run

Meaningful checks run:
- Checked offline wiki and vanilla documentation for decision custom costs, mission lifecycle, targeted decisions, scripted GUI context, event targets, scripted effects, triggers, and script constants.
- Confirmed `secret_alliance_open_public_pact_crisis` does not call faction formation, war declaration, or member war-join helpers.
- Confirmed `secret_alliance_reveal_pact_by_war` is the only helper that calls both `secret_alliance_form_anti_target_faction` and `secret_alliance_pull_live_members_into_reveal_war`.
- Confirmed both `secret_alliance_decision_counter_ultimatum` and `secret_alliance_decision_strike_first` now call `secret_alliance_reveal_pact_by_war`.
- Confirmed no remaining lines matching a direct `days = variable_name` pattern in the scoped decisions/effects files.
- Confirmed active mission IDs, paired completion/disruption decisions, activation calls, timeout effects, and cleanup removals are present.
- Confirmed explicit scanned localisation references resolve in `localisation/english/011_secret_alliance_l_english.yml`.
- Confirmed brace counts match on touched and directly audited script/GUI files.
- Confirmed PP custom-cost count and AI hint count match: 17 PP custom costs, 17 AI hints.

Skipped validation:
- No live HOI4 runtime load was run from this subagent pass.
- No localisation edits were made by instruction, so localisation auditor ownership remains intact.
- No git commit was made because the scoped Event 011 files are untracked parent work and the workspace contains unrelated Event 014 changes; committing would capture full parent-owned untracked files rather than only this audit patch.

## Remaining Issues

No blocking decision or mission issues remain in the audited scope.

The only remaining caveat is the faction reuse behavior noted above. It is consistent with `docs/events/011_secret_alliance.md`; do not patch it unless the parent decides the strict faction-name requirement overrides the current documentation.

No additional plan handoff was written beyond this audit handoff.
