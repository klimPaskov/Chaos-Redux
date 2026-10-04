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

## D14. Rat Nation and Rat King meters stay outside the sale

Decision: the 36 custom-cost decisions in `common/decisions/020_black_plague_rat_decisions.txt` keep their ordinary amounts; registry disposition `not_a_purchase_cost`.
They spend the event actors' own pacing meters (Brood Mass, Dominion, Sentience, Cohesion, Hunger, and the division-cap reserve), not a stockpile or national resource.

Basis:
- Both actors are special chaos countries (`is_special_chaos_country` lists `black_plague_rat_country` and `black_plague_rat_king_country`) and are never human-played or eligible for the Black Friday achievement.
- The rat meters pace a deliberately bounded escalation: the owner's decision file states that rat armies grow only through scripted capped pulses, and the Dominion, Sentience, Cohesion, and division-cap spends gate the Crown-the-Continent and terminal takeover route. Spec Part 4's qualifying test excludes a reduction that bypasses a non-cost requirement, and Part 5 forbids the sale from making otherwise invalid escalation affordable.
- Several actions are one-for-one meter conversions (Hold a Hunger Court turns Hunger into Cohesion, Convene the Council turns Cohesion into Sentience); discounting the paid side would mint meter value and change the action's identity, which Part 4's qualifying test also excludes.

The human counter-actions against the rats (Royal Node strike, Crown Strike, Royal Burrow sealing, armored clearance, the last-response missions) are purchases and read the sale price (D13).

Disposition: `not_a_purchase_cost`, recorded in the registry. This closes the Event 020 tranche 1 surface.

## D15. Event 015 growth costs and the Auxiliary Contract follow the sale

Decision: the two Event 015 surfaces that D11 queued now charge the Black Friday price.

- State-scaled military and institutional growth: `utopia_manifesto_refresh_dynamic_costs` applies the ratio the Black Friday price table holds (`global.black_friday_price_table_ratio`) to its seven base costs through `black_friday_price_table_quote` before the foundation, network, capstone, and current-tier copies are made, so every tier, the affordability triggers, the payment, and the focus and decision cost rows read one sale-priced cache. Payment already refreshes the cache at click or completion time; `black_friday_price_table_refresh_owner_quotes` also refreshes every accepted country through `utopia_manifesto_refresh_dynamic_costs_for_sale`, which keeps the stored growth tier, when the sale starts and ends.
- Auxiliary Contract: the consumed convoys read `global.black_friday_price_utopia_manifesto_decision_cost_convoys_medium` in the trigger, the payment, and both cost texts. The support equipment and trucks delivered to the contracting neighbour keep their ordinary amounts under D11's transfer rule. The combined Support Equipment requirement is now consistent during a sale, because it is computed from the sale-priced foundation formation plus the ordinary delivery, which removes the reason D11 held the contract back.
- Each paid formation or institutional batch credits the equipment family (`black_friday_credit_sale_purchase`); the Auxiliary Contract's package payment already credits through `utopia_manifesto_pay_prepared_decision_cost`, in the same family.

Basis: the lead's tranche 1 acceptance (one quote for display, affordability, and payment) and the cached-quote pattern accepted for Event 020 in D13. The one `every_country` pass runs only at sale start and end and is limited to countries that accepted the manifesto.
No AI weight changes.

Disposition: implemented (source). Tranche 1 is complete with D12 to D15.
Live checks that a focus-completion formation and an institutional batch charge the sale price, and that the Auxiliary Contract shows and charges the sale convoy price, are `needs_live_game`.

## D16. Genocide crisis payments read the sale price table

Decision: the Command Power, Army Experience, and Political Power that 16 genocide crisis decisions pay in their `complete_effect` read the Black Friday price table.
The file-scoped `@GENOCIDE_*` amounts move to `genocide_decision_cost` script constants (`security_command_power`, `deportation_command_power`, `extermination_army_experience`, `extermination_command_power`, `rail_army_experience`, `records_command_power`, `gulag_command_power`, `gulag_army_experience`; the Gulag network's Political Power reuses the previously unused `build_gulag`), registered as `global.black_friday_price_genocide_decision_cost_<key>` (`price_table_version` 5).
Requirements compare inclusively against the current price (`NOT = { command_power < price }`), so holding exactly the shown amount is enough; the former strict `>` checks required one point more than the payment. Bare requirement lines are wrapped in `custom_trigger_tooltip` with the matching `genocide_requires_*_tt` text, which now shows the live price (three new keys: records, Gulag resources, Gulag Army Experience).
Each payment credits one achievement family (Army Experience before Command Power before Political Power).
The static `ai_hint_pp_cost` literals stay, because that field takes no variable.

Basis: these are immediate voluntary payments (spec Part 4: Command Power and Army Experience families) with constant amounts, the D11 pattern.
The three camp-system payments the decisions call (`camp_rework_germany_start_occupied_poland_expansion_mission_in_from`, `camp_occ_manual_transfer_can_pay` with its payment, and `camp_rework_consume_expansion_resources`) belong to the active Camps workstream and are listed for its adoption in `owner_adoption_requests.md`.
No AI weight changes.

Disposition: implemented (source); camp-system components `owner adoption pending`.

## D17. Event 010 Death human payments read the sale price table

Decision: the 84 `death_decision_cost` payments (Command Power, Political Power, Army Experience, fuel, manpower, support equipment, trucks, infantry equipment, trains, convoys, Stability, and War Support) of the survey, telegraph, quarantine, recognition, compact, patrol, wasteland gear, quarantine line, coastal watch, survey and outpost, Transit Custodianship and its maintenance, Last Shores, and Black Book actions read the Black Friday price table (`price_table_version` 6).
The owner keeps each payment as a negative `<cost>_spend` constant and an affordability floor `<cost>_gate`; the table registers the positive spend amount as `global.black_friday_price_death_decision_cost_<cost>` (Stability and War Support with their 1% step), the `can_pay_death_*` triggers compare inclusively against it, the `death_pay_*` effects pay its negation, and the 242 numbers in the cost texts read it (`|0`, or `|%0` for Stability and War Support).
Each paid action credits one achievement family through `black_friday_credit_sale_purchase` (equipment, then trains, convoys, manpower, Army Experience, Command Power, fuel, Stability, War Support, Political Power); a Political Power-only action is not a non-political payment.

Excluded, with reason (`not_a_purchase_cost`):
- Death's soul power (`can_pay_death_*_souls`): the meter of a special chaos actor (`is_death_country`) that paces its spread toward the world-end route, the same reasoning as D14.
- Custodial capacity (Sealed Exclusion, Memorial Stewardship, and the capacity part of Transit Custodianship): an earned policy budget from surveys, outposts, the Living Compact, and the Death war; discounting it would let a country hold policies its earned capacity does not cover, which spec Part 4's qualifying test excludes as bypassing a non-cost requirement.

Basis: immediate voluntary payments with constant amounts (spec Part 4 families), the D11 pattern; the Transit Custodianship maintenance is a player decision rather than passive upkeep, so it is a purchase.
No AI weight changes.

Disposition: implemented (source). Live display and payment during a sale are `needs_live_game`.

## D18. Event 019 Infantry Spawn charges the sale price

Decision: the Event 019 purchases read the Black Friday price (`price_table_version` 7).

- Scaled formation requests keep the owner's cached cost variables. `infantry_spawn_refresh_request_costs` applies the table ratio to the seven rounded field costs before the nine request modes copy and adjust them, so every mode, the `infantry_spawn_can_pay_*_request` triggers, the payment, and the Muster Board read the sale-priced cache. The request transaction refreshes before paying and its rollback refunds the paid temps, so a refund never returns more than was paid. `black_friday_price_table_refresh_owner_quotes` refreshes each `infantry_spawn_participant` when the sale starts and ends.
- Fixed costs move to the price table: the five `infantry_spawn_request_cost.base_*` amounts that management actions pay (the scaled request field costs still start from the ordinary constants, so the sale is applied once), the four prototype preservation amounts, the six claimant response amounts (Stability with its 1% step), 24 derivative decision amounts, and the two zombie rally band amounts. Triggers compare against the table price, payments subtract it, and the cost texts show it. The rail corridor and prototype fuel checks compare fuel against the table price instead of a fixed thousands value.
- Each paid action credits one achievement family; a committed request credits by the resources it actually paid.

Kept at ordinary amounts, with reason:
- Equipment that changes hands (zombie containment infantry equipment, the golem material agreement's coal golems and support equipment): D11 transfer rule. The golem agreement credits only its Political Power.
- Claimant demand acceptance: the amounts are the claimant's terms; lowering them would change what was demanded (spec Part 4 qualifying test, identity).
- Lot obligation settlement and standardization requisition tranches: they pay down a liability already incurred rather than buy a new action.
- Family management payments routed to unit family providers live in the provider owners' files and are listed for their adoption.

Basis: the D11 and D15 patterns (constant amounts in the table; cached scaled costs apply the table ratio in their refresh). No AI weight changes.

Disposition: implemented (source); provider family management `owner adoption pending`. Live request display and payment at 50 and 75 percent are `needs_live_game`.

## D19. Event 011 Secret Alliance charges the sale price

Decision: Secret Alliance purchases read the Black Friday price (`price_table_version` 8).

- The owner already caches every response cost on the country in `secret_alliance_refresh_dynamic_costs`. That refresh applies the table ratio after the country scale and rounding to the nine scaled material costs, the diplomacy Command Power, the four dossier Political Power costs (including the public war aims action, which pays the partial dossier amount), the investigation, diplomacy, and emergency Stability losses (1% step), and the preemption and border escalation War Support (1% step).
- Payments and affordability checks that read the ordinary constants directly now read the cached variables, so every shown, required, and paid amount comes from the same cache. The investigation Stability is cached as its two paid parts, and the displayed intermediary total is their sum.
- The nine paid event options read `global.black_friday_price_secret_alliance_decision_gate_<cost>` in their trigger and payment; their achievement credit runs in a `hidden_effect` so the option tooltip shows only the payment.
- `black_friday_price_table_refresh_owner_quotes` refreshes each country holding `secret_alliance_cost_scale` when the sale starts and ends.
- Each composite payment (investigation, protection, diplomacy, offensive, emergency, war), each dossier action, the border escalation, and each paid event option credits one achievement family; the preemptive strike credits through its emergency payment only.

Kept at ordinary values: the Stability and War Support floors (diplomacy, manhunt, rumor, preemption), the mission objective requirement checks, and the false-accusation Stability penalty.

Basis: the D15 cached-cost pattern and spec Part 4 (event options with payment and Stability or War Support payments are purchases; floors and penalties are not). No AI weight changes.

Disposition: implemented (source). Live display and payment during a sale are `needs_live_game`.

## D20. Event 018 Resources Found charges the sale price

Decision: `resources_found_prepare_decision_project`, the single calculator behind every Event 018 cost estimate and payment, applies the ratio the Black Friday price table holds to the eleven spent resources after country and field scaling and rounding. The estimates, the `resources_found_decision_has_*_inputs` affordability triggers, and `resources_found_pay_decision_project_cost` therefore show, require, and charge the same sale price.
The owner's estimate context, which already blocks priced projects when country scale, war, field, depth, risk, contract, or infrastructure changes, also records the table ratio, so estimates taken at another price are stale rather than wrong. `black_friday_price_table_refresh_owner_quotes` refreshes the estimates of every country with `resources_found_decision_cost_preview_ready` at sale start and end; the owner's refresh skips a busy project queue, which leaves priced projects blocked until the next refresh instead of charging a price that differs from the shown one.
Civilian and military factory amounts are availability checks and project burdens and keep their size. Each paid project credits one achievement family by its primary spent resource.

Basis: the D15 and D19 cached-cost pattern; the owner's fail-closed estimate context. No AI weight changes; no Event 018 payment is refunded.

Disposition: implemented (source). Live estimate refresh and payment during a sale are `needs_live_game`.

## D21. Event 005 Soviet Collapse charges the sale price

Decision: every Event 005 decision price reads the Black Friday price table (`price_table_version` 9).

- `black_friday_price_table_refresh_soviet_collapse_entries`, called from `black_friday_price_table_refresh_entries`, registers 190 positive amounts as `global.black_friday_price_soviet_collapse_<group>_<key>` and stores, for each `_spend` payment constant of that amount, its negation as `global.black_friday_price_soviet_collapse_<group>_<key>_spend`. The quote helper now also returns that negation (`black_friday_price_spend`), so each of the 288 payment lines in the effects and the 11 in the decisions only swaps the constant for the global.
- Foreign aid actions charge a base amount plus a regional or major surcharge. The 78 surcharge globals hold the base price minus the tier price, so the base payment plus the surcharge always equals the tier price that the `can_pay_*` trigger required; quoting each part separately could have charged more than the shown and checked price.
- The 270 resource comparisons in the `can_pay_*` triggers compare against the positive price with an inclusive check (`set_temp_variable` copy, then `NOT = { <resource> < copy }`), replacing the strict `>` checks and the one-below `_gate` constants, so holding exactly the shown amount is enough. The three operational-priority compromises charge the table price through their owner's own negation.
- Stability and War Support prices use the 1% step. Stability losses without a positive constant (breakaway mobilization and recognition, the press network tiers, emergency mobilization) are registered from their negative constants.
- Cost texts show the table price: 264 fixed numbers and 51 `[?constant:...]` values in the cost and blocked texts, the 117 foreign aid tier texts behind the `GetSovietCollapseForeign*Cost` getters, the regional faction display values set in `custom_cost_trigger`, and the League formation cost in the breakaway category description.
- 188 paid decisions credit one achievement family from a hidden block at the end of their completion effect, by the primary paid resource (equipment, trains, convoys, manpower, army experience, command power, fuel, Stability, War Support, then political power).
- The invalid-target refunds of the three UWR aftermath actions return the native price the decision charged (D10).

Kept at ordinary amounts, with reason:
- Arms shipments, aid corridor trains, the Ukrainian League arms quota equipment and trains, and the grain compact trains and convoys: the recipient receives them one for one (D11 transfer rule). Their political power still reads the table.
- Stability floors, division counts, and construction mandate and arsenal quota amounts: requirements or owner meters, not payments.
- The resources the Soviet objective missions consume on completion: mission objective completion, not a purchase (as in D19).
- The patronage, coercion, and client cabinet Stability losses: consequences of the action, not its price.

Side effects accepted: the custom splinter payoff effects and the Factory City Belt effect are also called by focuses, so a focus completed during a sale pays the sale price there as well; only decisions credit the achievement. Nine decisions show and check a cost but charge nothing (owner defect, listed in owner_adoption_requests.md); their check and text follow the sale price.

Basis: D11 (constant amounts in the table, one global for display, affordability, and payment) and D10 (refunds return the charged price). No AI weight changes.

Disposition: implemented (source). Live display, payment, and tier surcharges during a sale are `needs_live_game`.

## D22. The nine Event 005 decisions that never charged their shown cost now pay it

Decision: `soviet_collapse_write_restored_charter`, `fev_negotiate_japanese_liaison_officers`, `ijx_press_trade_city_claims`, `pra_raise_mobile_supply_yards`, `pra_drive_the_junction_columns`, `dsc_register_field_hospital_columns`, and `dsc_order_the_dead_army_forward` pay the medium splinter cost (Political Power, Command Power, and Army Experience) through the new `soviet_collapse_pay_custom_splinter_medium_cost`, and `pra_repair_the_branch_lines` and `dsc_mark_the_unfinished_front_roads` pay the low splinter cost's support equipment through `soviet_collapse_pay_custom_splinter_low_cost`.
Both effects read the Black Friday price table, so the charge equals the shown and checked price during a sale, and credit one achievement family (Army Experience for the medium cost, equipment for the low cost), as the sibling decisions do.

Basis: each decision shows `chaosx_sovcollapse_decision_blocked_custom_splinter_medium` or `_low` in its cost slot and requires it through `can_pay_soviet_collapse_custom_splinter_medium_cost`, `can_pay_soviet_collapse_returned_names_medium_cost`, or `can_pay_soviet_collapse_custom_splinter_low_cost`, and every other decision with the same cost text pays exactly these amounts through its reward effect (`soviet_collapse_apply_custom_splinter_mobilize_signature_forces`, `soviet_collapse_apply_custom_splinter_push_extreme_route`, `soviet_collapse_apply_returned_names_claim_pressure`, or `soviet_collapse_apply_custom_splinter_consolidate_claim`).
A cost a player is shown and must hold but never pays is a defect, not a balance choice, so the shown price is charged instead of leaving it for an owner request.
The low cost text's Stability figure is the `recognition_stability_floor` requirement rather than a payment, so only its support equipment is charged; the consolidate-claim siblings' extra 1% Stability belongs to their reward effect and is not added.
A scan of every Event 005 decision with a custom cost text, following its completion and removal effects through the scripted effects they call, finds no other decision without a payment.
No AI weight changes.

Disposition: implemented (source). Live payment of one medium and one low decision, at full price and during a sale, is `needs_live_game`.

## D23. Sale duration wording says the rest of the day

Decision: the sale report, the Event Details status line, the Evolution I body, and the cost-source line say the discount lasts "for the rest of the day" instead of "until the next daily tick".

Basis: the sale expires one day after activation (`active_duration_days`), and player-facing text describes the game, not its update loop.
The Evo I catalog cell carries the same sentence, so its new wording is queued in `catalog_changes_pending.md`.

Disposition: implemented.

## D24. Leader assignment, preferred tactics, and special projects keep their price, and the sale names every price it cannot change

Decision: BF-ABS-001 (`assign_army_leader_cp_cost`, `assign_navy_leader_cp_cost`, `choose_preferred_tactics_cost`) and BF-ABS-003 (special-project `breakthrough_cost`, `prototype_cost`, and `resource_cost` blocks) take strategy D and become `engine_inaccessible`; no flat sale modifier approximates them.
The report (`chaosx.nr26.2.d`) and the Event Details premise (`black_friday.event_detail.premise`) end with one sentence naming the purchases that keep their normal price: base-game national decisions, guarantees, intelligence operations, license purchases, military-industrial organizations, equipment upgrades, leader traits, preferred tactics, and special projects.
The report's flavour line and the premise say staff officers instead of intelligence officers, so neither implies that intelligence operations are discounted.

Basis:
- The installed modifier documentation lists the three leader and tactic fields as numbers with 0 decimal places, not factors.
- Vanilla has no base leader-assignment price: `common/defines/00_defines.lua` defines none, and the cost exists only when a modifier adds one, so a flat sale value would have nothing to halve.
- Preferred tactics cost the flat define `PREFERRED_TACTIC_COMMAND_POWER_COST = 20` (`00_defines.lua:928`), and vanilla stacks flat modifiers on it (`common/ideas/army_spirits.txt:919`, `choose_preferred_tactics_cost = -15`). A flat sale value cannot multiply the current price and can take a 5 Command Power tactic to zero, breaking the one-quantum minimum.
- Special projects define their costs as static blocks (`common/special_projects/special_projects_documentation.md`, `common/special_projects/projects/documentation.md`); the only special-project modifiers change speed and supply, which Part 4 excludes, and there is no generic start or confirmation hook.
- Spec Part 4 requires a player-facing note for every visible strategy D limitation. The note covers these rows and the rows that were already `engine_inaccessible` (BF-NAT-007, BF-NAT-014, BF-NAT-016, BF-ABS-002, BF-ABS-004 to BF-ABS-010), which closes registry sign-off question 9.

The catalog Details text is queued in `catalog_changes_pending.md`.
The registry's BF-ABS-001 and BF-ADP-001 compatibility-effect lines no longer say that Event 26 is disabled.

Disposition: implemented.

## D25. Requirement lines and cost slots show only what they check or charge

Decision:
- The seven Event 005 breakaway and internal-compact requirement tooltips (`soviet_collapse_mobilize_defense_units_req_tt`, `_seize_depots_req_tt`, `_coordinate_fronts_req_tt`, and the northern rail, Volga-Ural oilfield, Tuvan road, and common-front compact keys) print the price globals their wrapped `can_pay_soviet_collapse_breakaway_{mobilize,seize_depots,coordinate_fronts}_cost` triggers compare against; the 35% Stability floor stays a fixed figure (commit `e368476a0`).
- Establish Muster Districts, Appoint Integration Staff, and Reserve Rail Corridors (Event 019) no longer repeat their cost checks in `available`, so the requirement tooltip shows no raw variable names; `custom_cost_trigger` still blocks them (commit `ba23efb1b`).
- The Event 005 low splinter and returned-names cost texts (`chaosx_sovcollapse_decision_blocked_custom_splinter_low`, `chaosx_sovcollapse_decision_blocked_returned_names`) show only the support equipment price. The 28 low splinter decisions and the three returned-names decisions state their Stability floor in `available` through a `custom_trigger_tooltip` (`soviet_collapse_splinter_stability_floor_tt` above `recognition_stability_floor`, `soviet_collapse_returned_names_stability_floor_tt` above `good_stability`), and their `custom_cost_trigger` checks only the support equipment through the new `has_soviet_collapse_splinter_support_equipment_price`, so a Stability shortfall no longer turns the price red.

Basis: the README completion rule forbids a displayed price that differs from the checked and paid price, D22 already records that the Stability figure is a floor rather than a payment, and CLAUDE.md section 2 requires plain requirement lines without raw identifiers.
The hidden `can_pay_*` triggers stay in each `available` block, so every decision keeps every gate it had; availability and AI weights are unchanged.

Disposition: implemented (source). The red and green states of the new floor line are `needs_live_game`.
