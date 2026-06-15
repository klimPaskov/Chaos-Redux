# Event 010 Death Decision/Mission Audit Handoff

Audit date: 2026-06-15

Scope: Event 010 `Death`, root `chaosx.nr10.1`, country `DTH`, no cluster, triggerable scenario `SCN-006`. Audited:

- `common/decisions/categories/010_death_categories.txt`
- `common/decisions/010_death_decisions.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `localisation/english/010_death_l_english.yml`
- Supporting references in `events/010_death.txt`, `common/on_actions/chaosx_on_actions.txt`, `common/script_constants/010_death_constants.txt`, `docs/events/010_death.md`, and relevant Event 010 specs/plans.

No gameplay files were edited. This is an audit-only handoff.

## Required References Consulted

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs and precedents:
  - `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - Vanilla decision examples for custom costs, state-targeted decisions, missions, and AI weights.

## Issue List

### High

1. **Custom cost localisation is incomplete for every Death custom cost.**
   - Files/ids: `common/decisions/010_death_decisions.txt` `death_*_cost_text`; `localisation/english/010_death_l_english.yml`.
   - Evidence: all 14 `custom_cost_text` keys have base localisation only. None define the expected `_blocked` or `_tooltip` variants.
   - Impact: blocked decisions can show missing localisation or unclear cost state. The base strings also use prose such as `Costs Command Power...` instead of icon-first exact values.
   - Recommended fix: add icon-first `key`, `key_blocked`, and `key_tooltip` entries for all 14 custom costs, using the values from `common/script_constants/010_death_constants.txt`.

2. **Several post-reveal decisions remain available after Death is defeated.**
   - Files/ids: `death_recognize_death_war`, `death_call_living_conference`, `death_join_living_compact`, `death_joint_coastal_patrol_plan`, `death_authorize_wasteland_entry_gear`, `death_share_wasteland_entry_gear`, `death_keep_port_lit`.
   - Evidence: `death_finish_defeat` clears `death_active` and `death_world_end_started`, but does not clear `death_publicly_revealed`, `death_living_compact_formed`, compact member/invite flags, or reveal/compact event targets. Many decision `visible` blocks do not exclude `death_defeated`.
   - Impact: obsolete war, compact, coastal patrol, and gear actions can remain visible in a post-defeat world. Some post-defeat wasteland work is legitimate, but the category does not separate aftermath actions from active-containment actions.
   - Recommended fix: add `NOT = { has_global_flag = death_defeated }` to active-containment decisions and keep only recaptured-wasteland aftermath decisions visible after defeat.

3. **Any Living Compact member can launch a compact-wide war declaration for free.**
   - Files/ids: `death_compact_war_declaration`, `death_decision_compact_war_declaration_effect`.
   - Evidence: visible requires only compact membership, not compact leadership; there is no custom cost or cohesion cost; effect loops all eligible compact members into war.
   - Impact: a minor member or AI member can force all eligible compact members into the Death war. This may be intended as emergency coordination, but it bypasses leader ownership, cost, and consent.
   - Recommended fix: restrict to `death_living_compact_leader` or add a compact-cohesion/command cost and much stricter AI weights.

4. **Reconsumed recaptured wastelands can retain the recaptured dynamic modifier.**
   - Files/ids: `death_apply_active_wasteland_state`, `death_apply_recaptured_wasteland_state`.
   - Evidence: recapture removes `death_active_wasteland_state`, but reactivation only clears the `death_recaptured_wasteland` flag and adds `death_active_wasteland_state`; it does not remove `death_recaptured_wasteland_state`.
   - Impact: a state reconsumed by Death can stack active and recaptured wasteland modifiers, corrupting state penalties and player-facing state tooltip state.
   - Recommended fix: add `remove_dynamic_modifier = { modifier = death_recaptured_wasteland_state }` inside `death_apply_active_wasteland_state`.

### Medium

5. **The implementation has no actual mission blocks.**
   - Files/ids: `common/decisions/010_death_decisions.txt`.
   - Evidence: no `activation`, `timeout_effect`, `selectable_mission`, or mission-style entries exist.
   - Impact: map objectives are all click decisions. There are no timed hold-line, secure-port, recapture-foothold, or outpost-construction missions with success/failure/partial-success behavior, despite the decision prompt asking for goal-style missions.
   - Recommended fix: add at least one bounded goal-style mission family for Last Shores foothold recapture or recaptured-wasteland outpost construction, with active caps and cleanup.

6. **Recognize the Death War charges war support without gating war support.**
   - Files/ids: `can_pay_death_recognize_war_cost`, `death_pay_recognize_war_cost`, `death_recognize_war_cost_text`.
   - Evidence: cost text says war support is spent and `death_pay_recognize_war_cost` applies `add_war_support = -0.03`, but `can_pay_death_recognize_war_cost` only checks command power.
   - Impact: the decision can be taken even when the country cannot meaningfully pay the listed war support sacrifice.
   - Recommended fix: add a war-support gate constant or remove war support from the listed/spent cost.

7. **PP custom-cost decisions lack `ai_hint_pp_cost`.**
   - Files/ids: `death_check_telegraph_office`, `death_call_living_conference`, `death_join_living_compact`.
   - Evidence: vanilla Decision modding docs note that AI will not save PP for custom costs unless `ai_hint_pp_cost` is provided.
   - Impact: AI may only take these decisions opportunistically and may fail to plan for compact formation/joining.
   - Recommended fix: add fixed `ai_hint_pp_cost` values matching the PP costs.

8. **Dead-Zone Outpost achievement timing is looser than the player-facing text.**
   - Files/ids: `death_build_dead_zone_outpost`, `death_apply_dead_zone_outpost_to_target`, `death_check_names_do_not_come_back_achievement`, `death_the_names_do_not_come_back` achievement text.
   - Evidence: outposts increment `death_dead_zone_outposts_completed` before defeat; the achievement check can later validate that pre-defeat count when `death_mark_public_defeat_achievements` runs.
   - Impact: text says outposts are completed after Death is defeated, but implementation can count pre-defeat outposts.
   - Recommended fix: either gate outpost construction behind `death_defeated` for achievement-counting purposes or track post-defeat outposts separately.

9. **State-targeted decision tooltips do not name the selected state.**
   - Files/ids: `death_strengthen_quarantine_line_tt`, `death_keep_port_lit_tt`, `death_survey_the_wasteland_tt`, `death_build_dead_zone_outpost_tt`.
   - Evidence: descriptions say "selected border state" or "selected recaptured wasteland" but do not use `[FROM.GetName]`.
   - Impact: the map state is visible, but the tooltip is less clear than the targeted-decision surface allows.
   - Recommended fix: update target tooltips to name `[FROM.GetName]` where the decision is state-targeted.

10. **Category-level lifecycle is too broad after reveal.**
    - Files/ids: `death_country_containment_category`, `death_containment_decisions_visible`.
    - Evidence: category remains visible from `death_publicly_revealed`, compact flags, or any border with active wasteland. It has no phase distinction for pre-reveal coastal watch, active war containment, world-end, and aftermath.
    - Impact: the category can drift into a mixed active/aftermath panel and show stale compact actions beside valid wasteland aftermath actions.
    - Recommended fix: split visibility helpers into active containment, Last Shores, and aftermath helper triggers.

### Low

11. **Indentation is inconsistent in two decision blocks.**
    - Files/ids: `death_recognize_death_war`, `death_keep_port_lit`.
    - Evidence: nested `visible`/`available` blocks are over-indented compared with surrounding decisions.
    - Impact: readability only; no syntax impact.
    - Recommended fix: normalize indentation during the next gameplay patch.

12. **Some static numbers remain in helper logic.**
    - Files/ids: `death_mark_world_end_foothold_created`.
    - Evidence: `value = 5` is used for the Six Continents achievement readiness despite constants existing for most Death tuning.
    - Impact: tuning is less centralized.
    - Recommended fix: add a `death_world_end.six_continents_ready_threshold` or achievement-specific constant.

## Decision Category Lifecycle Notes

- `death_missing_island_category` is well-bounded to report recipients before public reveal. It hides after `death_publicly_revealed`.
- `death_country_containment_category` is useful but too broad. It covers active war, compact coordination, pre-reveal coastal watch, world-end response, and recaptured wasteland aftermath in one category.
- Dark Methods and Black Oath are correctly hidden/queued. `docs/events/010_death.md` and the source-processing notes explicitly state they are not exposed because their mechanics are not implemented.
- After defeat, Death-specific active containment decisions need to close while recaptured-wasteland aftermath remains available.

## Mission Quality Notes

No actual Death missions are implemented.

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| None found | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

Decision substitutes currently cover:

- Missing Island report response decisions.
- Living Compact formation/joining/war call.
- State-targeted quarantine lines, coastal watch, wasteland surveys, and dead-zone outposts.

Recommended mission candidates:

- Last Shores foothold recapture mission with timeout and failure escalation.
- Hold a quarantine-line state adjacent to active wasteland for a fixed duration.
- Post-defeat dead-zone outpost goal that auto-completes when enough recaptured wasteland states have outposts.

## Cost And Requirement Clarity Notes

- Costs are materially varied and thematic: command power, PP, fuel, convoys, trains, support equipment, motorized equipment, infantry equipment, army XP, and war support.
- The actual cost payment helpers subtract the listed resources via hidden effects.
- Custom-cost localisation is the main failure: missing `_blocked`/`_tooltip` variants and no icon-first exact values.
- Requirements involving state targets should use `[FROM.GetName]` in tooltips.
- Several availability checks are hidden, so blocked players may see only vague cost text rather than the precise missing item.

## AI Validity And Route-Lock Notes

- Every decision has `ai_will_do`, and state-targeted decisions use `target_root_trigger`/`target_trigger`, matching the vanilla decision documentation.
- AI validity gaps:
  - PP custom-cost decisions lack `ai_hint_pp_cost`.
  - `death_compact_war_declaration` can be taken by any compact member and has high AI weight.
  - Active-containment decisions need defeat gates to prevent AI from using stale post-defeat actions.
- Targeted state decisions use `state_target = any_controlled_state`, which is preferable to scanning every state.
- No invalid dead-country target issue was found for most war decisions because `death_country_exists` and `can_declare_war_on` are checked. The post-defeat visibility gap remains because `DTH` can still exist with `death_country` flag.

## Localisation And Tooltip Gaps

- Missing cost variants:
  - `death_survey_boat_cost_text_blocked` / `_tooltip`
  - `death_telegraph_cost_text_blocked` / `_tooltip`
  - `death_quiet_quarantine_cost_text_blocked` / `_tooltip`
  - `death_recognize_war_cost_text_blocked` / `_tooltip`
  - `death_call_compact_cost_text_blocked` / `_tooltip`
  - `death_join_compact_cost_text_blocked` / `_tooltip`
  - `death_patrol_cost_text_blocked` / `_tooltip`
  - `death_wasteland_gear_cost_text_blocked` / `_tooltip`
  - `death_share_gear_cost_text_blocked` / `_tooltip`
  - `death_last_shores_response_cost_text_blocked` / `_tooltip`
  - `death_quarantine_line_cost_text_blocked` / `_tooltip`
  - `death_coastal_watch_cost_text_blocked` / `_tooltip`
  - `death_wasteland_survey_cost_text_blocked` / `_tooltip`
  - `death_dead_zone_outpost_cost_text_blocked` / `_tooltip`
- Tooltips are generally player-facing and not raw trigger dumps, but they are often broad effect summaries rather than exact requirements.
- Cost text should be changed from prose to icon-first values.

## Cleanup And Exploit-Risk Notes

- Recaptured wasteland reconsumption can leave a stale recaptured modifier unless `death_apply_active_wasteland_state` removes it.
- Defeat cleanup does not clear compact membership/invite state, compact leader event target, reveal state event target, or `death_publicly_revealed`.
- `world_end` is not cleared when Death is defeated after `world_end_death`; this may be intentional if terminal-state policy is global, but it conflicts with Black Tide Reversed-style recovery play and needs parent review.
- Compact-wide war call has no cost and no leader restriction.
- Dead-zone outposts can count before defeat toward an achievement whose text says post-defeat.
- No free equipment-farming loop was found in the audited decisions. Costs subtract equipment/fuel/XP/CP before rewards. Death ghost host spawning is outside the player decision layer and is not a decision exploit.

## Concrete Recommended Fixes

1. Add icon-first cost localisation variants in `localisation/english/010_death_l_english.yml` for all Death custom cost keys.
2. Add active/aftermath visibility helpers in `common/scripted_triggers/010_death_triggers.txt`, for example `death_active_containment_decisions_visible` and `death_aftermath_wasteland_decisions_visible`.
3. Add defeat gates to active containment decisions in `common/decisions/010_death_decisions.txt`.
4. Restrict `death_compact_war_declaration` to `death_living_compact_leader` or add a real compact cohesion/command cost and safer AI weights.
5. Add `ai_hint_pp_cost` to PP custom-cost decisions.
6. Gate or separately count post-defeat outposts for `death_the_names_do_not_come_back_ready`.
7. In `death_apply_active_wasteland_state`, remove `death_recaptured_wasteland_state` before applying the active modifier.
8. Add `[FROM.GetName]` to state-targeted decision tooltips in `localisation/english/010_death_l_english.yml`.
9. Decide whether Death defeat should clear `world_end` when `world_end_death` is the only terminal source. If yes, patch `death_finish_defeat`.
10. If missions are still required by the accepted design, add a bounded mission family instead of only click decisions.

## Changed Files

- `docs/plans/010_death_plans/subagent_handoffs/decision_mission_audit_handoff.md`

No gameplay, localisation, GUI, or asset files were edited.

## Validation Performed

- Confirmed offline wiki and vanilla decision documentation requirements for decision visibility, targeted decisions, custom costs, missions, and AI weights.
- Checked Death decision custom-cost keys against `localisation/english/010_death_l_english.yml`; all 14 are missing `_blocked` and `_tooltip` variants.
- Checked the audited Death decision/effect/trigger/localisation files for unsupported `<=` / `>=`; none were found.
- Searched the Death decision/effect/trigger files for mission-specific fields; no mission blocks were found.
- Reviewed `common/on_actions/chaosx_on_actions.txt` for Death recapture hook coverage; `death_on_state_control_changed` is wired from `on_state_control_changed`.

## Remaining Risks

- This audit did not run the game parser. Findings are based on static inspection, offline wiki/vanilla docs, and repo precedent.
- Broader Death event completion, country package, focus tree, super-event, and achievement wiring need their own audits.
- The repo worktree was already dirty with many Event 010 files untracked/modified before this handoff; this audit did not attempt to separate parent changes.

## Skills Used

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
