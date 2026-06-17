# Event 012 Africa Focus Tree Audit and Patch Handoff

Date: 2026-06-16

Role: Chaos Redux focus tree subagent. Scope was audit plus safe small patches only.

Parent follow-up, 2026-06-17: the Federal Congress finding below has been narrowed. The main tree now includes `AFR_charter_assembly_votes`, `AFR_regional_autonomy_statutes`, `AFR_federal_high_court`, `AFR_continental_citizenship`, and `AFR_congress_of_capitals` after `AFR_federal_charter_path`. `AFR_federal_charter_path` applies `africa_federal_charter_spirit`; Integrated Regions now requires the federal payoff `AFR_congress_of_capitals` on the federal route rather than the route lock alone; and `common/decisions/012_africa_decisions.txt` adds targeted Federal Member Vote, Autonomy Statute, and High Court Case decisions with equipment or manpower costs.

Parent follow-up, 2026-06-17: the sponsor/world-end finding below has also been narrowed. The main tree now continues after `AFR_africa_is_one` through `AFR_continental_export_office`, four charter-staff focuses, `AFR_congress_of_continents`, `AFR_unifier_proof_ledger`, `AFR_last_borders_are_administrative`, `AFR_one_charter_above_nations`, and `AFR_the_world_is_one`. The matching decisions now require the relevant focus flags; `AFR_congress_of_continents` requires all four staff focuses and all four sponsored charters; the final decision prepares `africa_world_is_one_gate_prepared`; and only the terminal focus calls `africa_mark_world_is_one_gate_ready`. A parent layout check counts 108 main-tree focuses, no missing focus references, no unresolved focus icons, and no duplicate coordinates. This does not complete the full tree spec: route families, subject trees, sponsor-country surfaces, and scenario validation still need further depth.

## Files Changed

- `common/national_focus/012_africa_focus.txt`
- `localisation/english/012_african_union_l_english.yml`

Files audited but not edited:

- `common/national_focus/012_africa_authority_focus.txt`

## High-Priority Fixes Applied

1. `AFR_continent_sponsor_office`
   - Before: required both `AFR_integrated_regions` and `AFR_autonomous_regions` through separate prerequisite blocks.
   - Problem: those focuses are locked behind mutually exclusive parent focuses, `AFR_federal_charter_path` and `AFR_sovereign_seats_path`, making the sponsor branch and final `AFR_africa_is_one` path impossible through normal focus play.
   - After: uses one prerequisite block with both focus ids, making the endpoint an OR while still requiring `AFR_continental_register`.

2. Naval focus filters
   - Changed `FOCUS_FILTER_NAVY` to vanilla-supported `FOCUS_FILTER_NAVY_XP`.
   - Changed focus ids:
     - `AFR_swahili_monsoon_ledgers`
     - `AFR_island_diwan_office`
     - `AFR_coralline_port_charters`
     - `AFR_court_of_thunder_and_tides`

3. `AFR_the_charter_mandate_desc`
   - Before: described values as things "the player can read and move."
   - After: in-world wording about legitimacy, authority, defense, aid, and integration obligations.

## Focus IDs Audited

Audited 80 focus ids across:

- Main Africa tree: `AFR_the_charter_mandate` through `AFR_africa_is_one`.
- Regional authority companion tree: `AFR_AUTH_charter_seat` through `AFR_AUTH_charter_future`.
- High-chaos actor companion tree: `AFR_BEST_bestiary_seat` through `AFR_BEST_world_witness`.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening statebuilding and Charter trunk | `AFR_the_charter_mandate`, `AFR_continental_congress`, `AFR_charter_courts` | Partial | Functional opener exists, but it is much smaller than the spec's opening survival/state-building trunk. |
| Federal Congress | `AFR_federal_charter_path`, `AFR_charter_assembly_votes`, `AFR_regional_autonomy_statutes`, `AFR_federal_high_court`, `AFR_continental_citizenship`, `AFR_congress_of_capitals`, `AFR_integrated_regions` | Partial | Parent follow-up adds the court/citizenship/capital congress spine and target decisions, but the route still needs richer failure states, route-specific advisors, and scenario validation. |
| People's Liberation Front | `AFR_liberation_war_office`, `AFR_liberation_columns` | Simplified | Exists as support/military lane, not as a mutually exclusive political route. |
| Continental General Staff | `AFR_charter_general_staff`, `AFR_scramble_reverse_claims` | Simplified | Staff support exists, but no full military-state political route or failure path. |
| Crown Congress and Old Thrones | Archive/old-seat lanes only | Missing as route | Old-seat content exists, but there is no distinct Crown Congress route family. |
| Green Covenant / high-chaos myth | `AFR_high_chaos_door`, `AFR_no_seats_for_caricature`, `AFR_first_nonhuman_envoys`, `AFR_world_root_mandate` | Partial | High-chaos branch is present and gated, but not a full Green Covenant political route. |
| Industry / continental economy | `AFR_industrial_convergence`, `AFR_lake_and_rail_agreements`, `AFR_mandate_foundries`, regional infrastructure lane focuses | Partial | Rewards are geographically flavored but still often broad `random/every_owned_state` construction. |
| Military / liberation armies | `AFR_liberation_war_office`, `AFR_charter_general_staff`, `AFR_liberation_columns`, `AFR_regional_guard_schools` | Partial | Adds manpower/equipment/XP, but lacks route-specific templates, elephant corps, and deeper force-growth logic. |
| Diplomacy / Charter League | `AFR_continental_congress`, `AFR_charter_courts`, `AFR_regional_authority_charters` | Partial | Focus hooks exist; decision/faction depth is outside this focused audit. |
| Expansion and integration | `AFR_scramble_reverse_claims`, `AFR_foreign_holder_case_files`, `AFR_scramble_counter_dockets`, `AFR_integrated_regions`, `AFR_autonomous_regions` | Partial | No instant annexation seen in these focus rewards, but region-by-region postwar settlement is not fully represented in the tree. |
| Diaspora return | `AFR_return_offices`, `AFR_afro_american_delegations`, `AFR_caribbean_atlantic_networks`, `AFR_exile_professors_engineers`, `AFR_returnee_settlement_councils`, `AFR_citizenship_without_erasure`, `AFR_diaspora_guard_cadres`, `AFR_pan_atlantic_congress` | Present, partial depth | Parent follow-up adds the branch; it still needs deeper route-specific consequences and scenario validation. |
| Regional authority branches | `AFR_AUTH_*` companion tree plus `AFR_regional_authority_charters` | Partial | Companion tree is present but shallow. |
| Authority Atlas / Archive of Old Seats | `AFR_authority_atlas`, `AFR_archive_of_old_seats`, `AFR_authority_register`, macro-region dossier lanes, settlement fork | Present, partial depth | Accepted addendum focus clusters are represented, but many rewards are still flags/value deltas rather than full mission/decision consequences. |
| High-chaos Bestiary actors | `AFR_BEST_*` companion tree and main Bestiary branch | Present, partial depth | Safety framing exists; package-specific gameplay remains mostly outside focus files. |
| Post-unification / sponsor / world-end | `AFR_continent_sponsor_office`, `AFR_africa_is_one`, `AFR_continental_export_office`, `AFR_middle_east_charter_staff`, `AFR_asia_charter_liaison_columns`, `AFR_europe_charter_observers`, `AFR_south_atlantic_return_mandate`, `AFR_congress_of_continents`, `AFR_unifier_proof_ledger`, `AFR_last_borders_are_administrative`, `AFR_one_charter_above_nations`, `AFR_the_world_is_one` | Present, partial depth | Parent follow-up adds a real post-unification sequence and focus-gates the matching decisions. Sponsor-country packages, terminal scenario validation, and variant super-event choices remain open. |
| RSA civil-war subtree | `AFR_rsa_congress_underground`, `AFR_rsa_mine_and_port_strikes`, `AFR_rsa_defecting_units`, `AFR_rsa_allied_pressure`, `AFR_rsa_pretoria_test`, `AFR_rsa_victory_settlement` | Present, partial depth | Parent follow-up adds the subtree; civil-war scenario balance and Allied peace validation remain open. |

## Missing or Simplified Content

- Main tree has 108 focuses; the spec expects roughly 120-180 for a complete full shared tree, plus deeper RSA/high-chaos/post-unification depth.
- Diaspora return branch exists, but still needs deeper route-specific consequences and validation beyond the current focus and decision hooks.
- Crown Congress route exists as a distinct route family, but it still needs richer failure states, advisors, and scenario validation.
- People's Liberation Front and General Staff now exist as political route families, but still need deeper route-specific consequences and scenario validation.
- RSA civil-war subtree exists, but Allied peace, pressure, and Pretoria objective behavior still need scenario validation.
- Sponsor/world-end content now has a real focus sequence, but sponsor-country packages, terminal scenario validation, and variant super-event choices remain open.
- Many macro-region Archive lane rewards are value deltas, flags, or broad state construction rather than package-specific missions, advisors, state targets, or settlement consequences.
- Several broad construction rewards use `random_owned_controlled_state` or `every_owned_state` over African states. This is not a syntax error, but it is less geographically specific than the spec asks.

## Icon Coverage Table

| Icon area | Status | Notes |
| --- | --- | --- |
| Event-specific focus icons | Covered | All referenced `GFX_goal_africa_*` focus icons resolve in `interface/012_africa.gfx`. |
| Vanilla/generic focus icons | Covered | All generic icon references resolve against local or vanilla interface sprite definitions. |
| Missing icon references | None found | Structural check found no unresolved focus icon sprite names. |
| Repeated icon risk | Present | `GFX_goal_generic_construct_infrastructure` is used by 12 focuses, `GFX_goal_africa_high_chaos_bestiary` by 8, `GFX_goal_generic_improve_relations` by 6, and `GFX_focus_research` by 5. This is not broken, but the tree would benefit from more route-specific icons. |
| Changed icon ids | None | No icon id changes were made. |

## Localisation and Reward Mismatches

- Missing focus localisation: none found for the 80 audited focus ids and their `_desc` keys.
- Changed key: `AFR_the_charter_mandate_desc`.
- Remaining mismatch risk: several focus descriptions promise missions, offices, or route systems whose focus rewards only set a flag/value delta. This is acceptable for scaffolding but incomplete against the spec unless the decision layer fully consumes those flags.

## AI Behavior Gaps

- Only 37 of 80 audited focuses have direct `ai_will_do` blocks.
- AI weights are mostly generic constants such as `constant:africa_ai.normal`, `preferred`, `strong`, or `low`.
- Route-aware behavior from `012_africa_ai_strategy_matrix.md` is only partially represented in focus files.
- No focus-level AI differentiation was found for full Federal vs revolutionary vs military vs crown vs high-chaos route selection beyond simple weights and route gates.
- High-chaos focuses are weighted low, which is safe, but package-specific AI restraint mostly depends on decisions/effects outside this focused patch.

## Validation Run

Meaningful task-specific checks run:

- Parsed both focus files and found 80 focus ids, no duplicate focus ids, and no missing prerequisite, mutual-exclusion, or relative-position focus references.
- Checked focus localisation coverage for every audited focus id and `_desc`: no missing keys.
- Checked icon sprite coverage against local `interface/*.gfx` plus vanilla interface definitions: no missing sprite names.
- Verified no remaining `FOCUS_FILTER_NAVY` tokens in the scoped focus files after replacing them with `FOCUS_FILTER_NAVY_XP`.
- Verified unsupported comparison-operator tokens were absent from the scoped focus files.
- Verified brace depth returns to zero in both scoped focus files.
- Verified `localisation/english/012_african_union_l_english.yml` still has UTF-8 BOM after the localisation edit.

Skipped validation:

- No full game load was run.
- I did not validate decision/event/effect runtime semantics outside the scoped focus-tree audit.
- I did not patch broader route depth gaps because the task explicitly limited this pass to small safe patches.

## Remaining Route Risks

- Final `AFR_africa_is_one` still depends on decision/effect-set flags such as `africa_continent_sponsor_ready`, `africa_minimum_historical_dossiers_ready`, `africa_minimum_high_chaos_packages_ready`, regional authority count, and living-core count. Those are outside the focus-only patch and should be validated with the decision/effect systems.
- The tree is much deeper than a stub, but it remains incomplete against the full Event 012 focus spec because several required route families are missing or compressed.
- The accepted addendum's Archive/Authority Atlas lane is represented, but broad playable consequences must be verified in `common/decisions/012_africa_decisions.txt`, `common/scripted_effects/012_africa_effects.txt`, and related triggers before claiming implementation completion.

## Plan Handoff

No new improvement plan was written. The existing accepted addendum remains the correct broad-depth plan:

- `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`

## Parent Follow-Up: 2026-06-17 Federal Audit Fixes

The read-only focus audit findings were folded into the parent patch. `AFR_federal_charter_path` now has route-root `ai_will_do` weighting, `AFR_congress_of_capitals` no longer repeats the already-implied `AFR_federal_high_court` prerequisite, and `africa_ratify_regional_autonomy_statute` mirrors the other federal targeted decisions with `NOT = { tag = ROOT }`. The federal custom cost localisation now includes the PP decision cost alongside manpower or support-equipment costs.

Remaining federal-route gap: distinct federal focus/idea art is still queued as an asset and visual-identity issue rather than a syntax or route blocker.
