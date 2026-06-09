# Event005 Urgent Playability Tranche Handoff

## Scope

Parent-agent urgent wrap-up pass for Soviet Collapse playability.

## Gameplay Fixes

- Existing countries freed by the collapse are no longer marked as `soviet_collapse_event_created_republic` by terminal, first-wave, progressive, or all-core release helpers.
- Newly released countries still receive `soviet_collapse_event_created_republic`, breakaway setup, and the custom Event005 focus tree.
- Terminal breakaway finalization now loads custom focus trees only for countries already marked as event-created.
- Existing Soviet subjects freed during terminal collapse receive breakaway setup without being given the custom Event005 focus tree.
- Kazakhstan first-wave special handling now initializes an already-existing Kazakhstan without assigning the event-created focus tree.
- Foreign patron intervention now requires a dynamic major through `is_major = yes`, excludes direct Soviet-war participants, excludes breakaway/event-created/high-chaos successor countries, and shuts off after Union Unmade or terminal collapse.
- Foreign patron category visibility and all foreign patron target-root triggers now require `is_soviet_collapse_foreign_patron_candidate = yes`, preventing released republics or stale menu flags from surfacing intervention decisions.

## Focus Layout Fixes

Coordinate-only cleanup in `common/national_focus/005_soviet_collapse_republics.txt` for the highest-priority visible clutter:

- Ukraine:
  - `ukr_soviet_collapse_free_soil_compromise` moved out from between mutually exclusive route locks.
  - `ukr_soviet_collapse_advisers_without_flags` moved away from `ukr_soviet_collapse_republican_deep_battle`.
- Belarus:
  - `blr_soviet_collapse_foreign_aid_through_brest` moved away from the state-route mutual-exclusion lane.
  - `blr_soviet_collapse_the_green_rail_pact` moved away from `blr_soviet_collapse_join_the_league_when_war_comes`.
- Kazakhstan:
  - Resource, Alash/socialist, and southern coordination nodes were moved to reduce same-row crowding and keep branches legible.

## Documentation Subagent

Documentation curator subagent `019e9880-6c69-7242-9f04-1e553e57f6ea` completed the broad Event005 documentation cleanup.

Changed docs:

- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`

## Validation

- Brace balance passed for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/decisions/categories/005_soviet_collapse_categories.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- `git diff --check` passed for touched gameplay and documentation files.
- Foreign patron target-root audit passed: no foreign patron target-root trigger with only the broad decision surface remains.
- `git status --short gfx/flags` returned no output; flags were not touched.

## Remaining Risks

- Focus reward diversity is improved in prior tranches but not proven complete across all 41 Event005 trees in this urgent pass.
- The Ukraine/Kazakhstan/Belarus coordinate pass fixes known audit hotspots, but a full visual in-game focus-tree screenshot audit remains recommended before final completion claims.
- No commit was made because the same Event005 files contain large pre-existing edits from earlier tranches; committing now would risk bundling unrelated work.
