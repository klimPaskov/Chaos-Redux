# Event005 Focus Tree Current Audit Handoff - 2026-06-04

## Scope

Audit role: Chaos Redux focus-tree auditor subagent for Event005 Soviet Collapse.

Reviewed focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No flag assets, `.tga` files, flag `.gfx` files, sprite flag wiring, interface files, or `gfx/flags/` files were edited.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_current_audit_ukr_blr_patch.md`

## Focus IDs Patched

- `ukr_soviet_collapse_first_republican_line`
  - Moved from `x = 26` to `x = 23`.
  - Reduces an early one-row pathline from `ukr_soviet_collapse_count_the_depot_keys`.

- `ukr_soviet_collapse_question_of_statehood`
  - Added `soviet_collapse_apply_focus_legal_recognition = yes`.
  - Connects the statehood fork to the parent focus-depth/recognition/recovery helper instead of leaving it as only a flag plus small stability.

- `ukr_soviet_collapse_war_without_a_declaration`
  - Moved from `x = 28` to `x = 25`.
  - Keeps the wartime branch near the adjusted republican-line parent.

- `ukr_soviet_collapse_foreign_courts_notice_kyiv`
  - Moved from `x = 22` to `x = 20`.
  - Shortens the statehood-to-diplomacy pathline.

- `ukr_soviet_collapse_open_the_liaison_offices`
  - Moved from `x = 27` to `x = 25`.
  - Keeps the diplomacy lane aligned with the adjusted foreign-courts focus.

- `ukr_soviet_collapse_british_caution`
  - Moved from `x = 31` to `x = 28`.
  - Reduces the short wide line out of `ukr_soviet_collapse_foreign_courts_notice_kyiv`.

- `ukr_soviet_collapse_protectorate_debate`
  - Moved from `x = 22` to `x = 21`.
  - Slightly shortens the pathline from the statehood fork while leaving route gating unchanged.

- `blr_soviet_collapse_forest_committees_report_in`
  - Moved from `x = 22` to `x = 20`.
  - Added `soviet_collapse_apply_focus_security_supply_plan = yes`.
  - Gives the early forest branch a connected security/depot depth helper rather than only manpower and institution variable gain.

- `blr_soviet_collapse_railway_neutrality`
  - Moved from `x = 12` to `x = 14`.
  - Shortens the one-row recognition-to-neutrality line without changing the rail-war mutual exclusion.

- `blr_soviet_collapse_the_corridor_everyone_wants`
  - Moved from `x = 5` to `x = 7`.
  - Reduces the opening Minsk-to-corridor pathline spread.

- `blr_soviet_collapse_armored_train_workshops`
  - Moved from `x = 5` to `x = 11`.
  - Re-centers a multi-prerequisite rail/military node between rail, Brest, League, and swamp parents.

- `blr_soviet_collapse_the_league_depot_at_minsk`
  - Moved from `x = 17` to `x = 15`.
  - Keeps the League depot closer to the adjusted armored-train workshop and Minsk-supply parents.

## Audit Findings

- Structural parse across the four focus files found `1,698` focus blocks in `41` focus trees.
- No duplicate focus IDs were found in the four files.
- No missing prerequisite focus targets were found.
- No missing mutual-exclusion focus targets were found.
- No asymmetric mutual exclusions were found.
- No raw `add_ideas` calls were found in any of the four focus files.
- The parent depth helpers are present inside existing focus helper effects, especially `soviet_collapse_advance_legal_focus_depth`, `soviet_collapse_advance_socialist_focus_depth`, `soviet_collapse_advance_military_focus_depth`, `soviet_collapse_advance_depot_focus_depth`, and `soviet_collapse_advance_league_focus_depth`.
- The focus files now call many helper wrappers that route into those depth helpers, including legal recognition, military consolidation, depot/supply control, League preparation/logistics/security, foreign recognition/supply/security, lawful supply, republican compact, chaos legitimacy/supply/assault, and several custom/factory successor helpers.
- The four files still contain many direct construction/stat/equipment rewards. Many are paired with helper effects, but a full reward-quality pass is still needed to decide which direct rewards are intentional map payoff and which are old shallow filler.

## Remaining Layout Risks

After the bounded patch, the parser still flags these Ukraine/Belarus wide short links:

- `ukr_soviet_collapse_romanian_grain_and_river_bargain` from `ukr_soviet_collapse_romanian_port_route`.
- `ukr_soviet_collapse_dead_fields_living_columns` from `ukr_soviet_collapse_carpathian_security_belt`.
- `blr_soviet_collapse_guide_companies` from `blr_soviet_collapse_council_bargains_with_forests`.
- `blr_soviet_collapse_minsk_supplies_the_front` from `blr_soviet_collapse_baltic_wire_rooms`.
- `blr_soviet_collapse_the_forest_state_rumor` from `blr_soviet_collapse_forest_ammunition_hides`.
- `blr_soviet_collapse_armored_train_workshops` from `blr_soviet_collapse_swamp_roads_closed`.

I did not patch those because they are multi-prerequisite or late-branch connections where fixing the line cleanly would likely require a broader branch layout pass.

## Remaining Full-Rework Gaps

- Ukraine is deeper than a linear ladder, but the visible layout still reads like several stretched lanes stitched together. The foreign/Black Sea/protectorate/right-side expansion family and bread/high-chaos endgame need a deliberate layout pass, not more isolated coordinate nudges.
- Belarus still has a crowded rail/forest/corridor midgame. The branch is mechanically more connected than a pure reward ladder, but several convergence focuses pull from far-apart lanes and should be redesigned as cleaner visual gateways.
- The custom splinter file still relies on many repeated identity helpers. The helper system now contains milestone logic, but the actual trees still need route-by-route review for whether each chaos country has bespoke payoffs instead of template rhythm.
- CFR/MFR/OGB and ancient restorations have more bespoke helpers than the oldest templates, but their remaining direct construction/equipment rewards should be audited against mechanic variables, decisions, League hooks, foreign pressure, and Soviet objective pressure before claiming the reward-spam complaint is fully resolved.
- This audit did not redesign whole trees, add new route families, or rewrite late-game payoff structure.

## Validation Run

- Brace balance check on all four focus files:
  - `005_soviet_collapse_republics.txt`: final balance `0`, minimum balance `0`.
  - `005_soviet_collapse_custom_splinters.txt`: final balance `0`, minimum balance `0`.
  - `005_soviet_collapse_factory_successors.txt`: final balance `0`, minimum balance `0`.
  - `005_soviet_collapse_ancient_restorations.txt`: final balance `0`, minimum balance `0`.
- Structural parser:
  - Total focuses: `1,698`.
  - Focus trees: `41`.
  - Duplicate focus IDs: none.
  - Missing prerequisites: none.
  - Missing mutual-exclusion targets: none.
  - Asymmetric mutual exclusions: none.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - No matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_current_audit_ukr_blr_patch.md`
  - Passed with no output.
- Flag-related diff/status check:
  - `git diff --name-only -- gfx/flags`
  - `git status --short -- gfx/flags`
  - `git diff --name-only -- ':(glob)**/*.tga' ':(glob)**/*flag*.gfx'`
  - `git status --short -- ':(glob)**/*.tga' ':(glob)**/*flag*.gfx'`
  - All produced no output.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
