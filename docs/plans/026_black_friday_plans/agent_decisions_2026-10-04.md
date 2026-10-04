# Event 26 agent decisions, 2026-10-04

These decisions were taken by the implementing agent under the user's standing grant of design authority, following the lead's recommended options for the Round 1 remaining-work list.
Each entry records the decision, its basis, and its disposition.

## D1. Friday anchor

Decision: the in-game Friday is the seven-day cycle where `global.num_days % 7 = 6`, so 3 January 1936 is the first Friday.
`friday_remainder` changes from 2 to 6 in `common/script_constants/026_black_friday_constants.txt`.

Basis: the offline wiki Data structures page (line 1470) gives `num_days` as days since the start of year 0, with 706640 on 1 January 1936.
The save `qa_cxt_base.hoi4` dated 1936.1.3 stores `great_depression_recent_major_industrial_state_loss_day=706642`, which `common/scripted_effects/035_great_depression_external_adapters.txt:160` sets from `global.num_days`.
706642 % 7 = 6, and 3 January 1936 was a Friday.
The former remainder 2 opened the sale on 6 January 1936 and every seven days after, which are Mondays.

The engine calendar has 365 days in every year, so the seven-day cycle drifts one real weekday after each skipped 29 February.
That drift is accepted as the in-game week and documented rather than corrected, because a leap-day correction would need a real calendar the engine does not keep.

Disposition: implemented.
Live date progression remains a `needs_live_game` acceptance item.

## D2. Unit-leader cost factors move to the country sale ideas

Decision: `army_leader_cost_factor`, `navy_leader_cost_factor`, and `promote_cost_factor` are carried by `black_friday_sale` (-0.5) and `black_friday_sale_evolution_i` (-0.75) beside the existing `unit_leader_as_advisor_cp_cost_factor`.
The leader-scoped dynamic modifiers `black_friday_native_leader_sale` and `black_friday_native_leader_sale_evolution_i`, the `every_unit_leader` loops in activation and expiry, `black_friday_refresh_created_unit_leader`, and `common/on_actions/026_black_friday_on_actions.txt` (the `on_unit_leader_created` hook) are removed.

Basis: vanilla applies these factors in country ideas (`common/ideas/army_spirits.txt:87`, `:121`, `:290`; `common/ideas/SOV.txt:304`, `:1210`; `common/ideas/british_raj.txt:365`).
The `unit_leader` category in `documentation/modifiers_documentation.md` is a display grouping, not the payer scope.
A modifier on an existing leader cannot discount recruiting a new one, so the old placement missed the main purchase and ran a leader loop on every country at activation and expiry for no benefit.

Deviation from the lead's acceptance text: `military_leader_cost_factor` is not carried.
The offline wiki Modifiers page describes it as the cost to recruit any unit leader, and `army_leader_cost_factor` and `navy_leader_cost_factor` as the land and naval cost.
Carrying all three would apply the sale twice to every recruit (to zero if the engine adds factors, or to a quarter if it multiplies them), while the army and navy factors alone discount each recruit exactly once.

Disposition: implemented.
The live check that recruiting a general costs half during the sale is `needs_live_game`.

## D3. Trade upkeep factors leave the sale

Decision: `trade_cost_for_target_factor` and `overlord_trade_cost_factor` are removed from both sale ideas; `embargo_cost_factor` stays.

Basis: the two trade factors change the civilian factories committed to ongoing trade deals.
That is passive upkeep, which spec Part 4 excludes from the sale, rather than a one-time voluntary purchase.
Peace-conference, annex, and puppet factors stay because they price a voluntary one-off commitment.
Registry row BF-NAT-010 records trade upkeep as `not_a_purchase_cost`.

Disposition: implemented.
