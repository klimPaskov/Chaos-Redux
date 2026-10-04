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

## D7. Base-game decision files are a visible compatibility exclusion

Decision: native `cost =` decisions in base-game decision files that Chaos Redux does not override keep their normal price during Black Friday.
Registry row BF-NAT-001 records them as `compatibility_exclusion_visible_note` with strategy D, and Chaos Redux-owned native costs, including the overridden `formable_nation_decisions.txt`, are BF-NAT-017 price-table rows.
The report event `chaosx.nr26.2.d` and the Event Details premise `black_friday.event_detail.premise` both end with the line "Base-game national decisions keep their normal price."

Basis: installed `documentation/modifiers_documentation.md` has no decision-cost modifier, so a base-game decision price can change only by overriding its whole file.
The native inventory counts about 2,150 numeric nonzero base-game native costs across 86 owner files.
Chaos Redux overrides only `formable_nation_decisions.txt` among base-game decision files; full overrides of the rest would freeze their content against base-game patches and DLC updates.
Spec Part 4 requires a visible compatibility note for any limitation that remains, so the note is shown in the two places a player reads about the sale.
The matching Event Details wording for the catalog is recorded in `catalog_changes_pending.md`; the workbook and CSV exports are not edited.

Disposition: implemented.

## D8. Black Friday joins the default-enabled event list

Decision: `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt` lists `constant:black_friday_event.id`, so `initialize_default_disabled_events_for_rework_queue` no longer disables Event 26 in a new campaign.
The catalog status stays `Needs Testing` until live verification, as queued in `catalog_changes_pending.md`.

Basis: a permanently disabled event gives players nothing, and the items the lead named as the enabling gate have landed: the Friday anchor (D1), the country-level leader discounts (D2), the trade-upkeep exclusion (D3), the sale price table (D4), the inactive-owner native conversion (D5), engine-priced achievement credit (D6), and the base-game compatibility note (D7).
Remaining owner custom costs no longer block enabling.
Under the spec Part 4 Future coverage rule each owner registers its own voluntary costs, so every unconverted owner carries an explicit per-owner disposition in the registry (`owner adoption pending` for active workstreams, queued conversion tranches for inactive owners) instead of holding the whole event back.
Until an owner adopts the sale, its custom costs charge their ordinary price, which is a missing discount rather than a wrong charge.

Disposition: implemented.
Live confirmation that a new campaign starts with Black Friday enabled is `needs_live_game`.

## D9. Simple custom costs get a lightweight sale API

Decision: an immediate custom cost in one native resource adopts the sale through `black_friday_simple_cost_quote` and `black_friday_simple_cost_is_affordable` (scripted triggers), `black_friday_simple_cost_pay` (scripted effect), and `GetBlackFridaySimpleCostLine` / `GetBlackFridaySimpleCostAmount` (scripted localisation).
The caller supplies only the ordinary amount and the resource kind; the API derives the sale mask and achievement family from the kind, prices the cost with `black_friday_quote_custom_cost`, checks it with `universal_cost_component_is_affordable`, pays it with `universal_cost_pay_component`, and credits the family during a valid natural sale.
A payment in a resource other than political power also counts as the achievement's non-political payment.
There is no receipt or refund path, and the receipt framework stays in use only for refundable, delayed, or multi-resource atomic transactions.
During an active sale a cost that cannot be priced is blocked rather than charged at an unchecked price, matching the existing CBRN external-aid owner (`black_friday_quote_cbrn_external_aid_pp_fee`).
The display is recomputed inside an owner `defined_text`, matching the South Africa purchase text, because a `custom_cost_text` cannot rely on an earlier evaluation of `custom_cost_trigger`.

Basis: the existing owner adapters run to roughly 100 to 200 lines per decision, while most of the roughly 2,300 unadapted custom-cost declarations are plain immediate payments; the task directive favours playable coverage over verification machinery.
No AI weight, MTTH, or random weight changes, so no probability comparison is required.

Contract and conversion example: `common/scripted_effects/026_black_friday_simple_cost_api.md`, indexed in `chaosx_dynamic_effects.md` as `black_friday_simple_costs`.

Disposition: implemented (source).
Live display and payment through a converted owner decision are `needs_live_game`.

## D10. Refunds of a price-table cost return the price that was charged

Decision: a decision whose native cost reads the sale price table refunds the price it actually charged, not the ordinary constant.
Timed decisions that refund on cancellation record the charged price when taken and refund that record: the four Zombie cure tiers (`zombie_cure_tier_<N>_paid_pp`) and the Anti-Zombie League formation (`anti_zombie_league_paid_pp`); the record is cleared on cancellation and on normal completion.
Same-tick refunds read the current table price: the Event 015 auxiliary-contract failure branches refund `global.black_friday_price_utopia_manifesto_decision_cost_pp_large`.

Basis: during a sale the engine debits the table price, so refunding the ordinary constant would pay out more than was charged and let a player profit by taking and cancelling a decision during the sale.
A scan of every add_political_power in the converted decisions found these refunds; the other matches are rewards with their own amounts (Holy Realm audits, the Greenland payment to Denmark, the Kuzbass tender) and stay outside the sale, as D5 records for rewards.

Two uncommitted refunds of the same kind belong to other threads' unfinished work and are left untouched: the Mengele import-subjects stale-completion refunds in `germany_mengele_decisions.txt` and the Soviet collapse aftermath invalid-target refunds in `005_soviet_collapse_effects.txt`.
Both must refund the charged table price when that work lands, as recorded in `owner_adoption_requests.md`.

Disposition: implemented (source) for the committed refunds; the two uncommitted refunds are `owner adoption pending`.

## D11. Constant-amount owner custom costs read the sale price table

Decision: an owner custom cost whose ordinary amount is a script constant registers that constant in the sale price table, and its `custom_cost_trigger`, payment, and cost text all read the same `global.black_friday_price_<group>_<key>`.
The price table quote takes an optional step (`black_friday_price_quantum`), so stability and war support round up to their 0.01 fixed-point quantum instead of a whole point.
Payment stays in the owner's own effect, which keeps the owner's equipment types and family rules, and the owner calls `black_friday_credit_sale_purchase` (new shared helper, also used by the simple API) once per action with one primary family.
Variable-amount custom costs use the simple API (D9).

Basis: the lead's tranche 1 acceptance asks that display, affordability, and payment share one quote, that multi-resource actions credit one primary family, and that equipment payments keep the owner's model and family rules.
The table gives one engine-read value for all three, exactly as D4 does for native costs.
For Event 015, whose 92 cost texts print fixed numbers next to resource icons, the table lets each text read the live price in place (`[?global.<key>|0]`), where the simple API would need an owner `defined_text` wrapper per text.
The simple API's shared payment would also have narrowed Event 015's archetype payments (`motorized_equipment`, `train_equipment`, `convoy_1`) to single models, which the stopped thread's inspection of the prefire domestic-shore purchase specifically ruled out.

Event 015 application (tranche 1): 28 `utopia_manifesto_decision_cost` amounts and the three Penal Works material amounts are registered (`price_table_version` 2).
Apart from the exceptions below, every custom cost of the 101 Event 015 custom-cost decisions reads the table in its trigger, its payment temps, the seven evolution-policy profile triggers, and the policy payment effect, and 279 cost and effect texts show the table price.
`utopia_manifesto_pay_prepared_decision_cost` credits one family per action: equipment first, then trains, convoys, manpower, army experience, command power, stability, and war support, and any of these counts as a non-political payment.
Kept at the ordinary amount, with reasons:
- the support equipment shipped by Send Surplus Abroad and Pool Reconstruction Brigades, because it is delivered to the recipient and a discount would create equipment;
- the district founding reserve thresholds, which are requirements rather than payments;
- the Auxiliary Contract's custom costs, because its support requirement is a combined total with the state-scaled formation cost that is refreshed outside the sale, so converting only part would make the shown price, the requirement, and the payment disagree (its native political power already reads the table);
- the state-scaled military and institutional growth costs, which are variable amounts recomputed by `utopia_manifesto_refresh_dynamic_costs` and remain queued for the simple API.

Disposition: implemented (source) for the constant-amount Event 015 custom costs; the Auxiliary Contract and growth costs are `accepted and queued` under tranche 1.
Live display and payment at 50 and 75 percent are `needs_live_game`.

## D12. Event 013 Natural Disasters reads the sale price table

Decision: every Event 013 material cost (manpower, support equipment, trucks, trains, convoys, fuel, and command power) of the 75 warning actions, the rescue, stabilization, chain-prevention, and reconstruction actions, the inbound relief route, and the four foreign relief offers reads the sale price table.
The 35 `natural_disaster_cost` amounts and the 35 material amounts of `natural_disaster_warning_cost` (five severities by seven resources) are registered as `global.black_friday_price_natural_disaster_cost_<key>` and `global.black_friday_price_natural_disaster_warning_cost_<severity>_<resource>` (`price_table_version` 3).
The affordability triggers, the payment effects and inline decision payments, and the cost texts read the same global, so the shown price, the requirement, and the debit agree.
Affordability keeps Event 013's inclusive strict-`>` floor: each check copies the price into `nd_cost_gate`, subtracts `natural_disaster_cost_gate.unit_step`, and compares, which is the vanilla form in `common/decisions/INS.txt` (`subtract_from_temp_variable` then `has_manpower > var`).
The per-cost floor constants that this replaces are removed from `natural_disaster_cost_gate`, `natural_disaster_warning_cost_gate`, and `natural_disaster_cost_gate_fixed`, so no stale ordinary floor remains to drift from the price.
The stabilization (1.5%) and reconstruction (2%) Stability losses are registered as positive amounts with the shared 1% Stability step, so they fall to 1% during a sale; their checks subtract `natural_disaster_cost_gate_fixed.stability_step` and their tooltips show the live percentage.
Warning (0.25% to 1%), rescue (1%), and relief (1%) Stability and War Support losses are at or below one 1% step, so under the shared rounding rule their sale price equals the ordinary loss; they are not registered and keep their fixed text.
The warning civilian-factory requirement stays at its gate, because it is a capacity requirement and the burden it adds is a timed modifier, not a payment.
Each paid action credits one achievement family through the new owner helper `natural_disaster_credit_black_friday_purchase`: equipment when the action pays support equipment or trucks (every warning profile except the coastal one, every rescue, stabilization, chain, and reconstruction action, and the neighbor, engineer, and medical relief offers), convoys for the coastal warning profile and the port lifeline, and the route's trains or convoys for the inbound relief route.
Foreign relief equipment is consumed by the donor rather than delivered as stock to the recipient, so discounting it creates no equipment.

The shared quote `black_friday_price_table_quote` now caps a sale price at the ordinary price.
Before the cap, an ordinary price smaller than one rounding step would have been raised to one full step, for example a 0.25% Stability loss to 1%.

Basis: the lead's tranche 1 acceptance (display, affordability, and payment share one quote; one primary family per multi-resource action; equipment payments keep the owner's model; penalties stay excluded), and the D11 price-table pattern for constant-amount owner costs.
The inbound relief mission's timeout Stability and War Support loss is a penalty and stays excluded.
No AI weight changes: the owner's `ai_will_do` blocks still read the same affordability triggers.

Disposition: implemented (source).
Live display and payment of an Event 013 action at 50 and 75 percent are `needs_live_game`.

## D13. Event 020 Black Plague human response costs read the sale price

Decision: every Event 020 response project, shared disease action, national programme, last-response mission, and weaponization payment that a country pays charges the Black Friday price.
Two mechanisms, chosen by how the owner prices the action:

- Population-scaled state quotes stay in Event 020's quote cache. `black_plague_refresh_current_state_response_quotes` applies the ratio the Black Friday price table currently holds (`global.black_friday_price_table_ratio`, recorded by `black_friday_price_table_refresh_entries`) to the components each project spends, with the same rounding rule as the table (`black_friday_price_table_quote`: rounded up, at least one unit, never above the ordinary quote). The ratio is part of the cache key, and `black_friday_price_table_refresh_owner_quotes` (called by the table's apply and restore) refreshes every registered response state and every selected board state through `black_plague_refresh_response_quotes_for_sale`, so the quotes change on the sale's first and last day instead of at the next weekly pulse.
- Fixed amounts (60 owner constants across `black_plague_response_cost_*`, `black_plague_medical_reserve*`, `black_plague_shared_cost`, `black_plague_shared_result`, `black_plague_last_response`, and `black_plague_weaponization_program`) are registered in the price table (`price_table_version` 4) and read in their triggers, payments, and `Get...Quote` cost texts. Negative Stability and War Support loss constants are stored as positive amounts and negated at payment and display. The shared state actions' three population bands pay the registered band amount, which equals the band's scaled standard bundle rounded up outside a sale.

What a project only requires on hand keeps its ordinary amount: personnel, trucks, convoys, and Medical Reserve that are checked but not consumed, the armored clearance infantry requirement, and the last-response Stability and War Support floors.
Civilian-factory commitments are static decision modifiers and keep their size, as the CBRN procurement exception (BF-CBRN-013) already records.
Each paid action credits one achievement family through `black_plague_credit_black_friday_purchase`: equipment for every action that spends support or infantry equipment, trains for the transport purge, and fuel for quarantine.
No Event 020 payment is refunded, so no paid-amount record is needed.

Basis: the lead's tranche 1 acceptance, spec Part 4 (equipment, fuel, Command Power, Stability, War Support, and custom mechanic currencies such as Medical Reserve are purchase families), and the D11 price-table pattern.
The quote cache is the owner's existing single source for display, affordability, and payment, so applying the sale inside it keeps the three in agreement without a second quote path.
AI weights are unchanged; AI affordability reads the same quotes and triggers.

Disposition: implemented (source) for the response, shared, last-response, and weaponization surfaces.
The Rat Nation and Rat King meter decisions are the remaining Event 020 tranche 1 surface.
Live display and payment of a response project, a shared band action, and a last-response mission during a sale are `needs_live_game`.
