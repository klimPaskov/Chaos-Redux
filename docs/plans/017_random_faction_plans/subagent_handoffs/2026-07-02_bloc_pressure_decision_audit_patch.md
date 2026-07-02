# Event 17 Bloc Pressure Decision Audit and Patch Handoff

Date: 2026-07-02
Agent role: `chaosx_decision_mission_auditor` style audit, patch-capable scope
Scope: Event 17 Random faction Bloc Pressure decision surface only

## Files Changed

- `common/decisions/017_random_faction_decisions.txt`
- `common/scripted_triggers/017_random_faction_triggers.txt`
- `common/scripted_effects/017_random_faction_effects.txt`
- `localisation/english/017_join_faction_l_english.yml`
- `docs/events/017_random_faction.md`

## Changed IDs

Decisions and missions:

- `random_faction_stabilize_alignment`
- `random_faction_request_liaison`
- `random_faction_quiet_opposition`
- `random_faction_convene_neutrality_council`
- `random_faction_reinforce_border_posts`
- `random_faction_invite_observers`
- `random_faction_publish_neutrality`
- `random_faction_offer_staff_mission`
- `random_faction_radio_networks`
- `random_faction_guarantee_corridor`
- `random_faction_guarantee_corridor_mission`
- `random_faction_demand_commitment`

Scripted triggers and effects:

- `random_faction_border_posts_objective_secured`
- `random_faction_corridor_objective_secured`
- `can_pay_random_faction_quiet_opposition_cost`
- `can_pay_random_faction_neutrality_council_cost`
- `can_pay_random_faction_staff_mission_cost`
- `random_faction_decision_quiet_opposition`
- `random_faction_decision_convene_neutrality_council`
- `random_faction_decision_offer_staff_mission`
- `random_faction_decision_guarantee_corridor`
- `random_faction_cancel_corridor_mission`
- `random_faction_corridor_success`
- `random_faction_corridor_failure`

Localisation keys:

- `random_faction_*_available_tt` for patched cost and target checks
- `random_faction_*_cost_text`, `_blocked`, and `_tooltip` for all patched costs
- `random_faction_border_posts_objective_tt`
- `random_faction_corridor_objective_tt`

## Issue List Sorted by Severity

High, patched: `random_faction_reinforce_border_posts` was a passive wait mission. It succeeded on timeout and only failed when the capital was lost, the country joined a faction, or capitulation happened. The matrix requires a real border or capital unit objective.

High, patched: `random_faction_guarantee_corridor_mission` was also passive. It succeeded on timeout and failed only when the leader became invalid. The matrix requires route or supply plausibility.

High, patched: several visible costs did not match their gates or actual spending effects. The worst mismatches were staff mission, liaison, invite observers, neutrality council, radio networks, corridor, commitment, and quiet opposition.

Medium, patched: targeted decisions relied on daily `target_trigger` filtering, but their `available` blocks only checked costs. Same-day invalid `FROM` scopes could still pass the visible button state.

Medium, patched: PP-spending custom-cost decisions lacked `ai_hint_pp_cost`, so AI would not budget for the custom PP cost as documented by vanilla decision docs.

Medium, remaining: the corridor target is tracked by a simple `random_faction_corridor_guaranteed` flag, not a per-leader or per-target mapping. This is acceptable for the small patch, but it can cross-talk if multiple leaders run corridor missions at the same time.

Low, remaining: the category header remains static localisation, not the dynamic status header requested by the spec.

Low, remaining: decision costs are centralized constants, but they are not dynamically scaled by size or distance.

## Before and After Behavior

Before:

- Border posts rewarded waiting out 120 days rather than placing troops.
- Corridor guarantees rewarded waiting out 90 days rather than maintaining a plausible route.
- UI costs described old PP, XP, support equipment, convoy, and command values that did not match script.
- Staff mission charged Command Power and Army XP despite the matrix asking for support equipment and command resources.
- Neutrality council displayed Command Power but did not charge it.
- Quiet Opposition displayed stability and war support strain but gave stability instead.
- AI PP budgeting did not know about custom PP costs.

After:

- Border posts complete successfully only when the pressured neutral controls its capital, has infantry equipment reserves, and has divisions in the capital or a border state. Timeout is failure.
- Corridor guarantee completes successfully only while the faction leader remains valid, retains enough convoys, and has a valid guaranteed pressure target. Timeout is failure.
- Targeted decisions revalidate `FROM` in `available` before the click.
- Staff mission now spends Command Power and support equipment.
- Neutrality council now spends Political Power, Command Power, and stability.
- Quiet Opposition now spends Political Power, infantry equipment, stability, and wartime war support.
- Cost localisation and blocked cost text match the constants and effects.
- PP custom-cost decisions now include `ai_hint_pp_cost`.

## Decision Category Lifecycle Notes

The category visibility trigger is scoped and safe for current use:

- newly aligned minors use `random_faction_newly_aligned_minor_decisions_visible`
- pressured neutrals use `random_faction_pressured_neutral_decisions_visible`
- faction leaders use `random_faction_faction_leader_decisions_visible`

Cleanup exists through `random_faction_clear_current_country_pressure` and active mission cancellation. The patch strengthened mission cleanup for corridor target flags, but the corridor cleanup is broad because no per-leader target map exists.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `random_faction_reinforce_border_posts` | pressured neutral | `random_faction_bloc_pressure_category` | dynamic capital or border state | control capital, keep infantry reserve, station divisions in capital or a border state | 120 days | resilience gain, stability gain, achievement check | neutrality exhaustion and pressure gain | low, one flag-gated mission |
| `random_faction_guarantee_corridor_mission` | faction leader | `random_faction_bloc_pressure_category` | dynamic pressure target | valid leader state, convoy reserve, valid guaranteed pressure target | 90 days | target pressure reduction and resilience gain | target pressure gain and leader stability strain | medium, target flag is not leader-specific |

## Cost and Requirement Clarity Notes

Patched costs now match implementation:

- Stabilize Alignment: 45 PP, 60 support equipment
- Request Liaison: 15 CP, 60 support equipment
- Quiet Opposition: 25 PP, 450 infantry equipment, stability, wartime war support
- Neutrality Council: 45 PP, 15 CP, stability
- Invite Observers: 15 CP, 15 convoys
- Publish Neutrality: 25 PP, stability
- Offer Staff Mission: 30 CP, 120 support equipment
- Radio Networks: 25 PP, 120 support equipment
- Guarantee Corridor: 15 CP, 450 infantry equipment, 15 convoys
- Demand Commitment: 70 PP, 30 CP

## AI Validity and Route-Lock Notes

AI can use meaningful actions because every decision already had nonzero `ai_will_do` for AI and zeroed human-only modifiers. The patch added `ai_hint_pp_cost` to PP custom-cost decisions. Targeted actions now repeat their target validity in `available`, reducing invalid same-day clicks and AI evaluations.

## Localisation and Tooltip Gaps

Patched:

- cost text values
- blocked cost text values
- custom objective tooltips for both missions
- duplicate objective localisation keys introduced during patch were removed

Remaining:

- category description is still a broad static summary rather than a dynamic status header with current faction, pressure source, or resilience.

## Cleanup and Exploit-Risk Notes

Patched:

- missions no longer create free success by waiting.
- corridor success and failure now clear `random_faction_corridor_guaranteed`.
- border and corridor missions now fail on timeout instead of rewarding passive survival.

Remaining:

- corridor guarantee needs a future per-leader target record if multiple leaders can run corridors at once.
- no exact supply-state check is used. The border mission approximates supplied defense through infantry reserve plus actual division placement.
- no selected-target UI is implemented for human faction leaders, so a large target array can still clutter the category in a broad pressure cascade.

## Validation Run

- Verified all 11 matrix decision ids are present in `common/decisions/017_random_faction_decisions.txt`.
- Verified brace balance on the touched decision, trigger, effect, constants, and category scripts.
- Verified no duplicate localisation keys remain in `localisation/english/017_join_faction_l_english.yml`.
- Verified the localisation file still begins with UTF-8 BOM bytes `EF BB BF`.
- Verified no unsupported `<=` or `>=` operators were introduced in the touched Event 17 files.
- Verified new objective trigger and tooltip references resolve by text search.

## Skipped Meaningful Validation

- No live HOI4 launch was run from this subagent context.
- No in-game decision UI screenshot was captured.
- No parser-level HOI4 error log validation was run.

## Concrete Recommended Fixes Remaining

- Add a per-leader corridor target helper or target-scoped flag if the parent wants simultaneous corridor missions from multiple faction leaders.
- Add dynamic category header localisation for current faction, pressure source, and resilience.
- Add selected-target browsing if human faction leaders see too many pressured targets during Evolution III.
- Consider dynamic cost scaling by country size, distance, war state, or convoy route once the broader system is being tuned.
