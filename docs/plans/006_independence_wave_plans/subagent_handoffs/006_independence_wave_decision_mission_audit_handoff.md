# Event 006 Decision and Mission Audit Handoff

## Scope

Audited the Event 006 decision, mission, formation-ledger, trigger, effect, constant, idea, focus-unlock, localisation, and event-doc surfaces named by the parent prompt.

Read before patching:

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding
- Vanilla documentation in `~/projects/Hearts of Iron IV/documentation/`
- Vanilla decision and mission examples in `~/projects/Hearts of Iron IV/common/decisions/`

No web lookup was used.

## Files Changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_decision_mission_audit_handoff.md`

## IDs Audited

Decision categories:

- `independence_wave_host_aftermath_category`
- `independence_wave_committee_survival_category`
- `independence_wave_new_states_congress_category`
- `independence_wave_formation_ledger_category`

Decisions and missions:

- `independence_wave_recognize_the_loss`
- `independence_wave_invite_observers`
- `independence_wave_hold_capital_ministry`
- `independence_wave_request_recognition`
- `independence_wave_form_local_defense_brigades`
- `independence_wave_seize_depot_inventory`
- `independence_wave_send_delegates_to_congress`
- `independence_wave_prepare_regional_compact`
- `independence_wave_proclaim_regional_compact`
- `independence_wave_integrate_compact_ministries`

Related helpers:

- `is_independence_wave_release`
- `is_independence_wave_host_aftermath_active`
- `is_independence_wave_breakaway_aftermath_active`
- `can_independence_wave_host_take_capital_mission`
- `can_independence_wave_committee_request_recognition`
- `can_independence_wave_prepare_regional_compact`
- `can_independence_wave_proclaim_regional_compact`
- `has_independence_wave_regional_compact_failure`
- `independence_wave_form_regional_compact`
- `independence_wave_finish_regional_compact_integration`

## Issue List

1. **High: failed missions could repeat their penalty.** `independence_wave_hold_capital_ministry` and `independence_wave_integrate_compact_ministries` used mission `available` as the failure condition, which is correct for HOI4 mission semantics, but neither mission blocked reactivation after failure. A host without capital control or a broken compact could repeatedly take stability, pressure, or anger penalties.
2. **High: `independence_wave_form_local_defense_brigades` was an equipment/manpower farm.** The decision could repeat and granted command power, equipment, and militia strength for a political-power cost and a manpower availability check. It did not consume manpower or set a completion flag.
3. **Medium: regional compact state requirement was stricter than the constant name implied.** `num_of_controlled_states > compact_required_states` with `compact_required_states = 2` required three controlled states. The formation text and failure check imply a two-state minimum.
4. **Medium: formation-ledger requirement text exposed implementation-shaped gates.** `can_independence_wave_prepare_regional_compact` and `can_independence_wave_proclaim_regional_compact` were called directly from `available`, making the ledger harder to read than a named proof requirement.
5. **Medium: most visible costs are still political-power anchored.** The patch adds a manpower commitment to brigades, but recognition, observers, congress, compact preparation, and compact proclamation still primarily use PP.
6. **Medium: category lifecycle is mostly flag-open and timed-recent based.** Categories have opening gates, but not full per-crisis cleanup for external annexation, host collapse, compact failure recovery, or congress collapse.
7. **Low: Event 006 resolver and formation ledger remain ordinary-first placeholders.** This audit did not implement the full candidate ladder, patron ledger, dossier board, border commission, or package-specific formables.

## Decision Category Lifecycle Notes

- Host aftermath opens through `independence_wave_mark_host_aftermath`, sets `independence_wave_host_aftermath_open`, and relies on timed `independence_wave_recent_host` for visibility. It does not yet clear all aftermath state through a settlement helper.
- Committee survival opens through `independence_wave_setup_released_country` and remains visible while `independence_wave_committee_survival_open` is set. It lacks annexation/capitulation cleanup.
- New States Congress opens from focus/effect state and is origin-gated. It is a first-pass category, not a full congress lifecycle with member count, collapse, patron takeover, or league formation cleanup.
- Formation Ledger opens from `independence_wave_reveal_the_formation_ledger` and currently supports only the regional compact route.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_hold_capital_ministry` | Host | Host aftermath | Host capital ministry state | Keep an owned capital state controlled by ROOT | 90 days | Sets `independence_wave_capital_ministry_secured`, lowers anger, small stability gain | Sets `independence_wave_capital_ministry_failed`, stability loss, anger gain | Low after patch; failure no longer reactivates |
| `independence_wave_integrate_compact_ministries` | Breakaway/compact founder | Formation Ledger | Controlled compact territory | Remain independent and keep at least two controlled states | 120 days | Calls `independence_wave_finish_regional_compact_integration` | Sets `independence_wave_regional_compact_integration_failed`, pressure gain | Low after patch; failure no longer reactivates |

Mission semantics were preserved intentionally: `available` is the auto-complete condition, so these positive hold missions use the bad state as `available`, `complete_effect` as failure, `timeout_effect` as success, and `is_good = yes` for correct failure tooltip framing.

## Patch Details

Before:

- Capital ministry failure could repeat while host aftermath stayed active.
- Compact integration failure could repeat while the compact remained formed but not integrated.
- Defense brigades could be repeatedly taken for command power, rifles, and militia strength.
- Compact proclamation required more controlled states than the apparent two-state minimum.
- Formation requirements were raw scripted-trigger gates.

After:

- `independence_wave_hold_capital_ministry` sets `independence_wave_capital_ministry_failed` and will not activate again after failure.
- `independence_wave_integrate_compact_ministries` checks `NOT = { has_country_flag = independence_wave_regional_compact_integration_failed }` in activation.
- `independence_wave_form_local_defense_brigades` sets `independence_wave_local_defense_brigades_formed`, consumes `constant:independence_wave_decision.brigade_manpower_spend`, and shows `independence_wave_form_local_defense_brigades_manpower_tt`.
- `can_independence_wave_proclaim_regional_compact` uses `compact_required_states_strict_floor = 1`, preserving strict `>` syntax while requiring at least two controlled states.
- Formation preparation and proclamation use custom trigger tooltips:
  - `independence_wave_prepare_regional_compact_requirements_tt`
  - `independence_wave_proclaim_regional_compact_requirements_tt`

## Cost and Requirement Clarity Notes

- Brigade manpower now has a visible custom effect tooltip and hidden manpower subtraction.
- Compact requirements are clearer, but still generic. Future work should name the state group or route identity when package-specific compact routes exist.
- Built-in decision `cost = constant:...` remains present across the file. No syntax evidence was found in this pass that it fails, but live parser validation is still needed because script constants are not supported in every field.
- Most costs need more variety in later passes: trains for rail/corridor work, convoys for port aid, command power for army orders, equipment for loyalists and brigades, and legitimacy/cohesion costs for congress actions.

## AI Validity and Route-Lock Notes

- Current AI weights avoid the worst invalid route choices and react to government, stability, war, congress delegates, and patron-cabinet route.
- Formation AI is now less likely to hit misleading requirements because the two-state floor matches the failure semantics.
- AI still lacks target validation for patrons, neighboring hosts, border claims, and league membership. Those systems are not implemented yet.
- Event 006 origin gates are present and explicitly block Event 005/Soviet Collapse origin flags in `is_independence_wave_release`.

## Localisation and Tooltip Gaps

- Added localisation keys are present and the file remains UTF-8 BOM.
- No `:0` keys were found.
- Host and committee decision descriptions are readable, but many effects still rely on stock HOI4 effect output instead of short cost summaries.
- Future package-specific formation decisions need named state-group localisation, not generic “enough territory” wording.

## Cleanup and Exploit-Risk Notes

- Patched repeat-failure loops and brigade farming.
- `independence_wave_seize_depot_inventory` is already one-shot through `independence_wave_depot_inventory_seized`.
- `independence_wave_request_recognition` is already one-shot through recognition flags.
- Remaining cleanup risk: categories and flags do not yet have a broad crisis-resolution cleanup helper.
- Remaining exploit risk: focus rewards can still add free industry/equipment in a shared tree without package-specific scaling; outside this decision/mission patch scope.

## Validation Run

- `git diff --no-index --check /dev/null common/decisions/006_independence_wave_decisions.txt` produced no whitespace diagnostics. Exit code was `1` because the file is untracked and differs from `/dev/null`.
- `git diff --no-index --check /dev/null common/scripted_triggers/006_independence_wave_triggers.txt` produced no whitespace diagnostics. Exit code was `1` for the same no-index reason.
- `git diff --no-index --check /dev/null common/script_constants/006_independence_wave_constants.txt` produced no whitespace diagnostics. Exit code was `1` for the same no-index reason.
- `git diff --check -- localisation/english/006_independence_wave_l_english.yml` passed.
- Brace count across Event 006 decision/category/trigger/effect/constant/idea/focus/event files: `open=614 close=614 delta=0`.
- Unsupported operator scan for `<=` and `>=` across Event 006 script files: no matches.
- Localisation `:0` scan: no matches.
- Localisation BOM check with `xxd -p -l 3`: `efbbbf`.
- New localisation key scan confirmed the three new tooltip keys are referenced and defined.

## Skipped Validation

- No live-game parser or scenario run was performed.
- No full HOI4 launch validation was performed.
- No spreadsheet/catalog validation was performed because this audit only patched the current decision/mission/formable-ledger surface.

## Remaining Recommended Fixes

- Add a narrow crisis-resolution cleanup helper for Event 006 host aftermath, committee survival, congress, and formation-ledger flags.
- Replace more PP-only costs with action-specific costs as the mechanics deepen.
- Give the Formation Ledger package-specific named state groups and post-formation missions before adding larger formables.
- Add patron, border commission, and congress target checks before any targeted foreign or border decision is introduced.
- Continue the full resolver work: reserved host-state scoring, batch-level state-removal validation, package ladder, and actual release-count shrinkage.
