# Soviet Collapse Focus Active Audit and Small Patch Handoff

Date: 2026-05-29

Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Write scope used:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

No localisation, decisions, scripted effects, scripted triggers, events, flags, or constants were edited.

The worktree was already dirty before this pass, including the four focus files and Soviet Collapse localisation. I did not revert or normalize unrelated existing edits.

## Route Coverage Table

| Required route or identity | Implemented focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine compact republic routes | `soviet_collapse_ukraine_focus_tree` with democratic, socialist, directory, League, foreign/protectorate, black-banner, bread-state, and expansion branches | Needs parent layout pass | Mechanically connected, but route locks and crosslinks are visually busy. No safe full coordinate pass was attempted here. |
| Belarus compact rail/forest/corridor routes | `soviet_collapse_belarus_focus_tree` rail timetable, corridor, national council, socialist, military transit, foreign corridor, forest-state branches | Patched partially | Early branch cluster was spread out. Later forest/route convergence remains dense. |
| CFR civilian construction successor | `CFR_soviet_collapse_focus_tree` public works, housing, cities-first, rails-first, factories-first, contracts, concrete-republic/endgame | Patched | Added direct map construction to several construction-themed focuses so the route visibly builds, not only calls helper effects. |
| Railway successor rail/supply hub identity | `PRA_soviet_collapse_focus_tree` and rail-themed custom branches | Mostly covered | Existing rewards include railways, supply nodes, rail authority hooks, decisions, and aggression. No patch made. |
| DSC zombie-like dead army | `DSC_soviet_collapse_focus_tree` roll-call, revenant staff, dead-regiment columns, dead-army endgame | Patched | Added controlled-state cores on hardline claimed roads and raised SOV aggression values in the extreme route. |
| Factory states focused on factory type | `CFR_soviet_collapse_focus_tree`, `MFR_soviet_collapse_focus_tree`, `OGB_soviet_collapse_focus_tree` | Patched for CFR/MFR | CFR now directly adds civilian factories/infrastructure/rail/supply. MFR now directly adds arms factories on arsenal focuses. OGB remains more restoration/Volga than factory-specific. |
| Naval northern directorate | `ARD_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `NLC_soviet_collapse_focus_tree` | Covered with risks | Existing branches have navy, convoy, dockyard, coastal defense, and port logic. Some still use small convoy rewards and should get a later pass. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` ancient focus trees | Covered but shallow | Compact, claim-heavy, and readable. They mostly stop at claims, not staged cores or formable depth. |

## High-Priority Fixes Applied

### `common/national_focus/005_soviet_collapse_factory_successors.txt`

Changed focus ids:
- `CFR_the_trust_office_takes_the_seal`
- `CFR_emergency_cement_accounts`
- `CFR_rails_first`
- `CFR_factories_first`
- `CFR_the_first_new_district`
- `MFR_foundry_line_holds`
- `MFR_the_arsenal_state`

Before:
- CFR construction route mostly applied custom helper effects and offsite/state variables, with little direct map-visible construction.
- MFR arsenal spine had scripted reward hooks but weak direct arms-factory payoff on the factory route.

After:
- CFR adds direct construction on core controlled states:
  - civilian factory on `CFR_the_trust_office_takes_the_seal`
  - infrastructure on `CFR_emergency_cement_accounts`
  - rail and supply hub on `CFR_rails_first`
  - civilian factory on `CFR_factories_first`
  - civilian factory on `CFR_the_first_new_district`
- MFR adds direct arms factories on:
  - `MFR_foundry_line_holds`
  - `MFR_the_arsenal_state`

### `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Changed focus ids:
- `DSC_claim_the_soldiers_road`
- `DSC_armies_that_do_not_demobilize`
- `DSC_congress_of_the_dead_army`

Before:
- DSC hardline route claimed states and had final SOV war/AI pressure, but did not core the controlled claimed roads.
- Final SOV conquer/antagonize strategies were present at `200`.

After:
- `DSC_claim_the_soldiers_road` adds a core on state `240` if DSC controls it and it is not already a core.
- `DSC_armies_that_do_not_demobilize` adds a core on state `228` under the same controlled-state guard.
- `DSC_congress_of_the_dead_army` SOV conquer/antagonize hidden AI strategies increased from `200` to `250`.

### `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus ids:
- `blr_soviet_collapse_the_rail_map_on_the_wall`
- `blr_soviet_collapse_forest_committees_report_in`
- `blr_soviet_collapse_first_corridor_guard`
- `blr_soviet_collapse_which_road_is_belarus`
- `blr_soviet_collapse_evacuation_choice`
- `blr_soviet_collapse_western_corridor_switchmen`
- `blr_soviet_collapse_eastern_line_watch`
- `blr_soviet_collapse_depot_cars_without_labels`
- `blr_soviet_collapse_forest_defense_staff`

Before:
- Belarus' opening rows were cramped, especially the rail/corridor/forest setup and row-3 follow-up cluster.

After:
- Early Belarus branches are more separated:
  - rail at `x = 10, y = 1`
  - first corridor guard at `x = 16, y = 1`
  - forest committees at `x = 22, y = 1`
  - statehood convergence moved to `x = 16, y = 2`
  - row-3 rail/corridor/forest follow-ups spread across `x = 8/12/16/20/28`.

## Missing or Simplified Content

- Ukraine still needs a dedicated layout pass. Main risk ids: `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_protectorate_debate`, `ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_the_commander_or_the_cabinet`, `ukr_soviet_collapse_black_sea_port_ledgers`, and downstream row-7/row-9 crosslinks.
- Belarus late forest/green-state area remains dense after the early layout cleanup. Main risk ids: `blr_soviet_collapse_partisans_or_army`, `blr_soviet_collapse_regular_forest_brigades`, `blr_soviet_collapse_decentralized_detachments`, `blr_soviet_collapse_the_forest_general_staff`, `blr_soviet_collapse_the_forest_state_rumor`, `blr_soviet_collapse_a_forest_that_can_govern`.
- Ancient restoration trees are compact but still mostly claim/payoff trees. Follow-up should consider staged integration/core mechanics for `KZR_khazar_charter`, `SOG_sogdian_charter`, `KHW_khwarezmian_charter`, `ALN_alan_charter` and their expansion endgames.
- Several 18-focus high-chaos trees are mechanically stronger than pure reward ladders, but their compactness comes with shallow route choice. Broad route-family expansion was out of scope.

## Icon Coverage Table

| Changed id | Icon id | Status |
| --- | --- | --- |
| `CFR_the_trust_office_takes_the_seal` | `GFX_focus_CFR_cement_allocation_boards` | Existing reference, unchanged |
| `CFR_emergency_cement_accounts` | `GFX_focus_CFR_emergency_cement_imports` | Existing reference, unchanged |
| `CFR_rails_first` | `GFX_focus_CFR_bridge_permit_ministries` | Existing reference, unchanged |
| `CFR_factories_first` | `GFX_focus_CFR_civilian_hegemony_project` | Existing reference, unchanged |
| `CFR_the_first_new_district` | `GFX_focus_CFR_the_permit_state` | Existing reference, unchanged |
| `MFR_foundry_line_holds` | `GFX_focus_MFR_foundry_line_holds` | Existing reference, unchanged |
| `MFR_the_arsenal_state` | `GFX_focus_MFR_the_arsenal_state` | Existing reference, unchanged |
| `DSC_claim_the_soldiers_road` | `GFX_focus_DSC_claim_the_soldiers_road` | Existing reference, unchanged |
| `DSC_armies_that_do_not_demobilize` | `GFX_focus_DSC_armies_that_do_not_demobilize` | Existing reference, unchanged |
| `DSC_congress_of_the_dead_army` | `GFX_focus_DSC_congress_of_the_dead_army` | Existing reference, unchanged |
| Belarus changed layout ids | Existing `GFX_blr_soviet_collapse_*` icons | Existing references, unchanged |

No icon ids were renamed.

## Localisation and Reward Mismatches

- No localisation keys were changed.
- No focus ids were renamed.
- No new player-facing text was added.
- CFR focus names/descriptions already imply construction; the patch brings rewards closer to the text by adding visible construction.
- MFR focus names/descriptions already imply arsenal output; the patch brings rewards closer to the text by adding direct arms factories.
- DSC focus names/descriptions already imply undead/old-front territorial claims; the patch brings rewards closer to that by adding controlled-state cores on hardline roads.

## AI Behavior Gaps

- Existing mutual exclusion reciprocity checked cleanly.
- CFR/MFR/DSC patched rewards did not require new `ai_will_do` blocks because those focuses already had state-aware or route-aware weights.
- Ukraine route-lock AI remains uneven. Some route choices use simple base weights and should get cleaner route-specific modifiers during the layout pass.
- Belarus early AI is serviceable, but several downstream focuses still use flat `base` weights.
- Ancient restorations have many simple AI weights and should be given stronger route-aware conquest/settlement behavior if expanded.

## Validation Run

Commands run:
- `rg -n "add_ideas\\s*=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Result: no matches.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Result: no matches.
- Python duplicate-id and mutual-exclusion reciprocal audit over the four scoped focus files.
  - Result: `duplicate focus ids: none; mutual exclusivity reciprocal errors: none`.
- `rg -n "FOCUS_FILTER_ARMY(\\s|})" ...`
  - Result: no matches in the four scoped files.
- Tiny/equipment-only heuristic audit over the four scoped files.
  - Result: no remaining equipment-only hits after counting scripted hooks, buildings, claims, cores, war goals, custom tooltips, and mechanics.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Result: clean.

Skipped validation:
- No in-game load or Clausewitz parser run was available in this subagent pass.
- No localisation validation was required because no localisation was changed.
- No decision/scripted-effect validation was run because decisions and scripted helpers were explicitly out of write scope.

## Remaining Route Risks

- Ukraine remains the highest priority parent follow-up for layout. It is mechanically rich but visually crowded, and a safe fix should be a coordinate-only pass that respects every existing prerequisite and mutual exclusion.
- Belarus is improved at the opening but still needs a second pass for the late forest/green-state branch.
- CFR and MFR now have visible direct factory rewards, but their helper effects still carry most of the mechanical depth. Parent should verify live balance after helper effects resolve.
- DSC controlled-state core additions are intentionally guarded by control and existing-core checks. If the intended design is unconditional cores, that requires broader balance approval.

## Plan Handoff

No separate improvement plan was written. The remaining Ukraine/Belarus layout work is specific enough for the parent or another focus-tree subagent to patch directly inside the existing focus file.
