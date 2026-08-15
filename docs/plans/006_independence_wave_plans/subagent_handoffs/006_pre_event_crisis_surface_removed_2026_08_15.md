# Event 006 pre-event crisis surface removal

Date: 2026-08-15

## Disposition

The pre-event Independence Wave pressure surface is retired. Before the public Event 006 report fires, the player receives no Independence Wave decision category, mission, pressure label, or crisis cost.

## Source changes

- Deleted `common/decisions/006_independence_wave_crisis_decisions.txt`.
- Deleted `common/decisions/categories/006_independence_wave_crisis_categories.txt`.
- Hard-disabled `can_independence_wave_open_crisis` in `common/scripted_triggers/006_independence_wave_crisis_triggers.txt` with `always = no`.
- Removed the retired crisis category, mission, and pre-wave cost localisation keys from `localisation/english/006_independence_wave_decisions_l_english.yml`.
- Neutralized the obsolete pre-wave wording in `localisation/english/006_independence_wave_super_event_l_english.yml`.
- Updated `docs/events/006_independence_wave/overview.md` to make the public report the first player-facing entry point.
- Updated the decision-category inventories so they no longer claim the retired category exists.
- Updated `.tools/audit_event6_allocator.py` to assert the retired surface remains absent and the trigger remains hard-disabled.

## Behavior

Pressure, resistance, stability, and host state conditions no longer create a decision category or selectable mission. The legacy crisis scripted effects and event callback remain inert compatibility code for old references. They have no live decision caller after the source deletion.

The normal Event 006 planner and public report path are unchanged. Central adapter, attestation, scenario preflight, Join, package counts, and the 40/32/29/161 authority boundary are unchanged.

## Evidence

- Source search finds no live `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, or `independence_wave_cost_pre_wave_crisis` consumer.
- The allocator audit now checks that the retired decision and category files are absent and that `can_independence_wave_open_crisis` contains `always = no`.
- The event surface remains subject to the existing MCP `EVENT_INSPECTED_PARTIAL` limitation recorded in the current Event 006 completion handoffs. No new event or GUI surface was introduced by this narrow change.

## Remaining limitations

Historical plans and handoffs still describe the former crisis mission as dated implementation evidence. They are not current runtime authority. The legacy crisis effect and event files were deliberately retained to avoid breaking unrelated old scripted references, but no player-facing pre-event path remains.
