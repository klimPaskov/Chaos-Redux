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

## D4. Chaos Redux native decisions use a global sale price table

Decision: each registered ordinary political power price has one global variable, `global.black_friday_price_<key>`.
`black_friday_price_table_initialize` builds the table at ordinary prices from `on_startup` and, once per `price_table_version`, from `black_friday_initialize_runtime`.
`black_friday_activate_sale` sets every price to `ceil(ordinary x payment ratio / 10000)` with a minimum of 1, and `black_friday_expire_sale` (also reached from terminal cleanup) restores the ordinary price.
Zero prices stay zero.
Decisions read the price through `cost = global.black_friday_price_<key>`.
Literal ordinary amounts are registered as `black_friday_price_pp_<N>` from the `black_friday_price_table` constant group; owner-constant prices keep the owner's constant as their source and are registered as `black_friday_price_<group>_<key>`.

Basis: installed `documentation/modifiers_documentation.md` has no decision-cost modifier.
The offline wiki Decision modding page (Decision cost, line 286) states that `cost` accepts a variable, and the Data structures page (line 549) documents `cost = var_name?100`.
Vanilla uses `cost = TUR_etatism_cost_penalty_var?50` and `cost = var:AST_call_on_fascists_cost` (`common/decisions/AST.txt:2481`).
Kaiserreich uses a global variable directly: `cost = global.UPC_coalition_cost_var` (`common/decisions/UPC decisions (Federalist China).txt:981`, set in `common/scripted_effects/UPC effects (Federalist China).txt:1655`).
That production precedent for the `global.` form is why the inactive-owner conversion proceeds without waiting for the live probe; the CXT probe decision `chaosx_test_country_event026_price_probe_decision` (100, 50, and 25 political power) remains the live confirmation.
If the probe shows the global form misbehaving, the fallback is the vanilla-proven country form `cost = black_friday_price_<key>?<ordinary>` written on every country by the same apply and restore effects.
This is spec Part 4 strategy C (conditional data) with a single engine-computed price.

Placement: the table and its registered entries live in `common/scripted_effects/026_black_friday_price_table_effects.txt` rather than in the 4,800-line lifecycle file, so the entry list stays reviewable; the lifecycle file only calls initialize, apply, and restore.
The `on_startup` build matters because an unset price variable reads as zero, which would make a converted decision free before the first daily pulse.

Disposition: implemented (source).
Live display and debit at 100/50/25 percent are `needs_live_game` through the CXT probe.

## D5. Inactive-owner native costs convert now, on the Kaiserreich precedent

Decision: every positive decision-level `cost = N` or `cost = constant:K` in the 15 inactive owner files named in the lead's list (including the vanilla-override `formable_nation_decisions.txt`) reads its registered price-table key; 399 lines changed, 25 zero costs untouched.
The conversion was not held for the live probe because Kaiserreich ships the identical `cost = global.<variable>` form (D4); the probe stays the live confirmation, and D4 records the fallback form.
Lines were converted only at decision depth (direct children of a decision block), so nested `cost =` fields inside effects such as advisor creation cannot pick up a sale price.
In the three owner files that carry another thread's uncommitted work (`germany_mengele_decisions.txt`, `genocide_crisis_decisions.txt`, `005_soviet_collapse_decisions.txt`), only the converted cost lines were committed and the other hunks were left uncommitted and untouched.
Rewards stay outside the sale: the Greenland purchase still pays Denmark its full ordinary 250 political power while the buyer pays the sale price.

Disposition: implemented (source).

## D6. Engine-priced purchases credit the Five Departments achievement

Decision: law changes, advisor and staff hires, and experience or command power spending count toward `026_black_friday_five_departments`.
At activation, inside the existing activation country loop, each human country that holds a valid natural sale (`black_friday_achievement_is_valid_sale`) snapshots its economy, trade, and mobilization law ids, its filled political advisor slots, its filled theorist, chief, and high command slots, and its army, navy, and air experience and command power (`black_friday_engine_purchase_snapshot`).
At expiry, before the sale source clears and while the sale is still active, one bounded `every_country` loop limited to `is_ai = no` runs `black_friday_engine_purchase_credit`.
A changed law credits `laws`, more political advisors credit `personnel`, more theorist, chief, or high command holders credit `officer_corps`, and a net decrease of an experience pool or of command power credits the matching `army_experience`, `navy_experience`, `air_experience`, or `command_power` family.
Credit goes through `black_friday_add_committed_achievement_family`, so a later refund of an owner receipt in the same family cannot remove it.
An experience or command power credit also sets `black_friday_achievement_engine_non_political_payment`, which the completion check accepts as the payment in a resource other than political power.
The snapshot is cleared after the comparison.

Basis: the achievement description names institutional purchases, and the registry maps law changes to `laws` (BF-NAT-003), advisors to `personnel` (BF-NAT-002), senior staff to `officer_corps` (BF-NAT-004), and doctrine, design, and spirit spending to the experience families (BF-NAT-005, BF-NAT-007).
The engine prices these through the sale ideas and exposes no law-change, hire, or spend hook, so a before-and-after comparison over the one-day sale is the only source-side signal.
Law ids come from the new `black_friday_engine_law` constant table, built from the vanilla `economy`, `trade_laws`, and `mobilization_laws` categories in `common/ideas/_economic.txt`, `_manpower.txt`, and `spain_republic.txt`; Chaos Redux defines no laws of its own.
Slot counts use `amount_taken_ideas` (installed `documentation/triggers_documentation.md`, vanilla `common/characters/ENG.txt:918`) through `meta_trigger`, bounded by `engine_slot_count_limit`.
All disqualifiers stay in force: forced, manual, debug, AI, and already-awarded progress fail `black_friday_achievement_is_valid_sale`.
No recurring scan is added; the expiry loop runs once per sale.

Accepted limits: a law, slot, or resource change made by a focus or event on the sale day also counts; replacing an advisor without filling a new slot is not detected; spending smaller than the same day's experience or command power gain is not detected.

Disposition: implemented (source).
Live confirmation that a law change, an advisor hire, and an experience spend during a natural sale are credited is `needs_live_game`.
