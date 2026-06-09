# Event005 Parent Focus Layout And Reward Tranche

## Scope

Parent patch for the active Soviet Collapse focus-tree cleanup goal.

Touched files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_blr_focus_l_english.yml`
- `localisation/english/005_soviet_collapse_kaz_focus_l_english.yml`

No flag, sprite, image, or asset files were touched.

## Focus ids changed

- `ukr_soviet_collapse_free_soil_compromise`
- `ukr_soviet_collapse_german_liaison_question`
- `ukr_soviet_collapse_open_the_liaison_offices`
- `blr_soviet_collapse_the_green_rail_pact`
- `blr_soviet_collapse_the_green_border`
- `kaz_soviet_collapse_the_resource_towns_demand_seats`
- `kaz_soviet_collapse_call_the_steppe_congress`
- `kaz_soviet_collapse_karaganda_coal_accounting`
- `kaz_soviet_collapse_emergency_oil_boards`
- `kaz_soviet_collapse_army_of_the_open_horizon`
- `kaz_soviet_collapse_uzbek_supply_delegates`
- `kaz_soviet_collapse_local_notable_compacts`
- `kaz_soviet_collapse_steppe_land_statutes`
- `kaz_soviet_collapse_planned_economy_without_center`
- `kaz_soviet_collapse_red_nomad_committees`
- `kaz_soviet_collapse_the_steppe_keeps_many_memories`

## Behavior changes

- Ukraine's Free Soil Compromise was moved off the military route row and no longer rewards only the generic chaos-legitimacy helper. It now directly raises rural Rada strength, institutions, local authority, resilience, and opens Black Soil committee enforcement when the Black Banner compact is active.
- Belarus's Green Rail Pact was moved away from the adjacent League and Green Border focuses. Its reward now uses the existing Minsk League depot package instead of a generic security-supply helper, tying the focus to trains, depot control, League support, a supply hub, local industry, and League unit deployment decisions.
- Kazakhstan's tight same-row rows around the Steppe Congress, resource, oil, military, and far-right political/economy branches were spaced to a two-column rhythm where possible.
- Kazakhstan's Resource Towns focus no longer uses a generic lawful-supply helper. It now directly grants political reserves, resource security, resource authority, republican institutions, resilience, and a civilian factory in a controlled core state.
- After the `chaosx_focus_tree_auditor` subagent returned a layout-only patch, the parent resolved newly exposed Ukraine row collisions around the German liaison, arsenal, and liaison-office nodes.

## Related subagent handoff

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_event005_focus_tree_audit_priority_layout_patch.md`

## Localisation keys added

- `ukr_soviet_collapse_free_soil_compromise_mechanics_tt`
- `blr_soviet_collapse_green_rail_pact_mechanics_tt`
- `kaz_soviet_collapse_resource_towns_demand_seats_mechanics_tt`

## Validation

- Focused parser check: `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, and `soviet_collapse_kazakhstan_focus_tree` now report `duplicate_coords 0` and `close_pairs 0` for same-row focus coordinates at distance 0 or 1.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_l_english.yml localisation/english/005_soviet_collapse_blr_focus_l_english.yml localisation/english/005_soviet_collapse_kaz_focus_l_english.yml` passed.
- Brace balance on `common/national_focus/005_soviet_collapse_republics.txt`: final depth 0, minimum depth 0.
- Localisation BOM check passed for all three touched localisation files.

## Remaining gaps

- This is a bounded tranche, not a full completion of the Event005 focus-tree goal.
- Current parent scan still shows broad generic helper repetition across all focus trees; the direct repeated `add_ideas` issue is not present in the current focus files, but many focuses still rely on high-frequency generic helper effects.
- A full route-depth pass is still needed for all minor/custom/ancient trees, especially to turn generic helper reward ladders into branch-specific mechanics, wars, claims, cores, units, decisions, and AI behavior.
