# Event005 Special Focus Audit Handoff - 2026-06-04

## Scope

Audit role: Chaos Redux focus-tree audit subagent for Event005 Soviet Collapse.

Allowed focus files reviewed and patched:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No flag assets, gfx files, interface files, or `common/national_focus/005_soviet_collapse_republics.txt` were edited.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_special_focus_audit_handoff.md`

## Focus IDs Patched

- `PRA_armored_train_schools`
  - Added `pra_raise_mobile_supply_yards` unlock tooltip, train equipment, and a core-state supply node plus railway construction.
  - Keeps the existing armored-train tech and rail guard column reward, but makes the focus visibly railway/logistics oriented.

- `PRA_claim_the_branch_lines`
  - Added train equipment and core-state railway/infrastructure construction.
  - Expanded search filters to include `FOCUS_FILTER_ARMY_XP` alongside industry because the focus leads into the junction-column military route.

- `PRA_seize_the_junction_cities`
  - Added industry and annexation filters to match expansion/claim behavior.
  - Added manpower, train equipment, and a core-state supply node plus railway construction before the existing expansion-claim and rail-guard effects.

- `MFR_armored_train_workshops`
  - Added train equipment and core-state railway plus supply-node construction.
  - Keeps the existing MFR rail authority helper and makes the focus produce an immediate map/logistics consequence.

- `MFR_gates_sirens_rifles`
  - Added core-state bunker and anti-air construction.
  - This turns the factory guard/security reward into visible worksite-defense infrastructure instead of only helper/stat output.

- `MFR_every_border_needs_guns`
  - Added core-state bunker and anti-air construction.
  - The focus now matches its border-defense premise with immediate map consequences.

- `KZR_caspian_patrol_letters`
  - Added industry search filter, convoys, and coastal dockyard/naval-base construction.
  - The Caspian/naval focus now has port and shipping payoff instead of only naval XP and recognition variables.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Passed with no output.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - No matches.
- Brace balance check on the three touched focus files:
  - `005_soviet_collapse_custom_splinters.txt`: final balance `0`, minimum balance `0`.
  - `005_soviet_collapse_factory_successors.txt`: final balance `0`, minimum balance `0`.
  - `005_soviet_collapse_ancient_restorations.txt`: final balance `0`, minimum balance `0`.
- Tree-local layout scan for focuses on the same row between mutually exclusive siblings:
  - `005_soviet_collapse_custom_splinters.txt`: `0`.
  - `005_soviet_collapse_factory_successors.txt`: `0`.
  - `005_soviet_collapse_ancient_restorations.txt`: `0`.

## Remaining Issues

- The three files still contain many focus rewards that route through existing helper effects. Some helpers are already deep, but a full audit would need helper-by-helper review to distinguish real mechanics from tooltip-heavy or variable-only rewards.
- `005_soviet_collapse_custom_splinters.txt` is large enough that more bounded passes are still warranted for death-state, religious, naval, and high-chaos splinter payoffs.
- `005_soviet_collapse_factory_successors.txt` still has several MFR/CFR/OGB focuses whose identity depends mostly on helper calls. The next broad pass should inspect helper outputs before adding more direct construction, to avoid double-paying.
- `005_soviet_collapse_ancient_restorations.txt` has stronger expansion payoffs than before this audit, but SOG/KHW/ALN still deserve a separate route-by-route audit for late branch aggression and map consequences.

Further broad rework is still needed. This handoff is a bounded safe tranche, not a completion claim for every special focus tree in Event005.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
