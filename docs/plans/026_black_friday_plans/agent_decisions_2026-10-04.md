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

Current disposition: superseded by the original user completion gate, restored on 2026-10-07.
The user requires all cost rows, assets, localisation, logs, docs, audits, catalog fields, and tests to be complete before re-enabling Event 26.
The remaining owner, native-composition, exact inaccessible-surface, final-registry, and live acceptance gaps do not meet that condition.
The historical reasoning below is retained as provenance and does not authorize current enablement or partial universal coverage.

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

## D26. Paid event options in owners queued to Event 26 follow the purchase rule

Decision: every option with a negative resource effect in the inactive owners' events is classified by one rule. A purchase is an option where the player pays to obtain the option's outcome; it pays the registered table price, shows that amount in its option tooltip, and credits one achievement family in a `hidden_effect`. A refusal penalty or a consequence is `not_a_purchase_cost` and keeps its ordinary amount.
A scan of `001`, `003`, `022`, `043`, `048`, `049`, `053`, `063`, `068`, `069`, `071`, `072`, `073`, `076`, `078`, `080`, `081`, `086`, `091`, `092`, and `093` finds 40 such options (the Event 043 manpower loss sits in its `immediate` block, not an option). Five are purchases:
- `chaosx.nr1.2.b` Deploy security detachments: 10 Command Power from `global.black_friday_price_cp_10`.
- `chaosx.nr1.8.a` Launch emergency intervention now: 25 Command Power from `global.black_friday_price_cp_25`.
- `chaosx.nr3.21.c` Remove the Arhat quietly: 25 Political Power from `global.black_friday_price_pp_25`. The payment left the hidden block so the tooltip shows it, and `chaosx_nr3_21_c_tt` no longer repeats "spends Political Power".
- `chaosx.nr53.1.a` Pay him: 200 Political Power from `global.black_friday_price_pp_200`.
- `chaosx.nr78.2.b` Just end them: 100 Political Power from `global.black_friday_price_pp_100`.

The Stability and War Support losses next to these payments (1% and 3% Stability in Event 001, 20% War Support in Event 078) are the domestic consequences of a crackdown or an aggressive war, as D21 treats coercion Stability losses, and keep their amounts.
The other 35 options are refusal penalties (refusing a demand, a claim, a sale, or a peace) or consequences (a disaster, a lost battle, a ceded state, a submitted tax, a policy's own unrest), each recorded as `not_a_purchase_cost` with its reason in the registry's BF-EVO rows.
Command Power literals register as `cp_10` and `cp_25` in `black_friday_price_table`, so the table reads by resource name, and `price_table_version` goes from 9 to 10.
Political Power options credit through the new `black_friday_credit_political_power_purchase`, which item D27's decisions also use; Command Power options credit the Command Power family inline, as the Event 011 options do (D19).

Basis: lead decision (3) for round 2 and the Event 011 precedent (D19); spec Part 4 lists paid event options as a purchase family, and the README completion rule needs a disposition for every discovered surface.
No option gains a trigger and no AI chance changes, so availability and AI behaviour are unchanged.

Disposition: implemented (source). The option tooltip amount and the sale debit are `needs_live_game`.

## D27. Native price-table decisions credit Political Power when taken

Decision: every decision whose native `cost` reads `global.black_friday_price_*` counts as a Political Power purchase toward the achievement (registry BF-NAT-017).
`black_friday_credit_political_power_purchase` (in `026_black_friday_effects.txt`) sets the family to Political Power and the non-political input to zero, then calls `black_friday_credit_sale_purchase`, so it credits once during a valid natural sale and does nothing otherwise; AI, forced, manual, and debug sales stay excluded by that effect's trigger.
Of the 399 converted decisions in the 15 owner files, 272 call it from a `hidden_effect` at the start of `complete_effect`, which runs when the decision is taken (23 of them, the European Union expansion decisions and the Zombie containment measures and their revocations, had no `complete_effect` and get one holding only that call).
The other 127 already credit one family through their own payment and are left as they are, so no decision credits twice: 87 Event 015 decisions through `utopia_manifesto_pay_prepared_decision_cost`, 15 Event 015 evolution decisions through `utopia_manifesto_start_prepared_evolution_policy_action`, two through the Utopia growth payments alone, 14 genocide crisis decisions (D16), and nine Event 005 Kuznetsk and UWR decisions.
`utopia_manifesto_pay_prepared_decision_cost` credited nothing when a decision paid no material cost; every caller also pays a Political Power table price, so it now falls back to the Political Power family.
The four Zombie cure tiers and the Anti-Zombie League formation, which refund their charged price when cancelled (D10), call the new `black_friday_withdraw_political_power_purchase` in that refund, so a cancelled purchase in the same sale is not counted.

Basis: lead decision (2) for round 2. The installed `documentation/` and vanilla `common/on_actions` have no decision-taken hook, and a political power snapshot would also count law and advisor spending that D6 already credits to their own families. A source scan of the scripted effects each decision calls, including transaction-based credit, confirms that none of the 272 decisions credits another family.
No availability, cost, or AI weight changes.

Disposition: implemented (source). The in-game credit check is `needs_live_game`.

## D28. The consumed arms and aid corridor surcharges of Event 005 foreign aid take the sale price (addendum to D21)

Decision: D21 kept the arms shipment and the aid corridor trains at their ordinary amounts because the recipient receives them. That holds for the base shipment only: the recipient receives `armaments_target_infantry_equipment` and `armaments_target_support_equipment` (equal to the base 1000 and 100) and `intelligence_trains` (equal to the base 4), while the regional and major surcharges (500 or 1000 infantry equipment, 50 or 100 support equipment, 2 or 4 trains) are consumed and never delivered.
The six surcharges now read the price table: each `global.black_friday_price_soviet_collapse_foreign_intervention_<action>_<tier>_<resource>_extra_spend` holds the negated sale price of the surcharge, and each tier global (`..._armaments_regional_infantry_equipment`, `..._armaments_major_support_equipment`, `..._aid_corridor_regional_trains`, and the others) holds the ordinary base plus that price.
`can_pay_soviet_collapse_foreign_armaments_cost` and `can_pay_soviet_collapse_foreign_aid_corridor_cost` compare the regional and major tiers against the tier globals with the inclusive check D21 uses, `soviet_collapse_apply_foreign_armaments_aid` and `soviet_collapse_apply_foreign_aid_corridor` pay the base constant plus the surcharge global, and the regional and major texts behind `GetSovietCollapseForeignAidArmamentsInfantryCost`, `...ArmamentsSupportCost`, and `...CorridorTrainCost` print the tier globals, so the shown, checked, and paid totals agree.
At 100, 50, and 25 percent a regional infantry shipment costs 1500, 1250, and 1125; a major one 2000, 1500, and 1250; a regional support shipment 150, 125, and 113; a major one 200, 150, and 125; regional corridor trains 6, 5, and 5; major corridor trains 8, 6, and 5. Each surcharge rounds up with a one-unit minimum.
A regional or major arms shipment credits the equipment family; a base-tier shipment pays only delivered goods, so it credits nothing. The aid corridor decisions already credit the convoy family.
The volunteers and military construction surcharges already read the table from D21, so no other consumed surcharge keeps an ordinary price. `price_table_version` goes from 10 to 11.

Basis: D11's transfer rule covers goods the recipient receives one for one, and the round 1 review recorded the undiscounted surcharges as a known limit. Base-tier checks keep their ordinary form, and no AI weight changes.

Disposition: implemented (source). Live display, affordability, and payment for a regional and a major target during a sale are `needs_live_game`.

## D29. Coverage dispositions for owners the registry missed

Decision:
- `039_murder_mystery_decisions.txt` (42 custom costs; active owner) and `006_independence_wave_foreign_reaction_decisions.txt` (one custom cost at line 30) are `owner adoption pending`, with their line lists in `owner_adoption_requests.md` and rows in the registry's owner table.
- Events 001, 007, and 017 and the Germany Mengele decisions are converted: a rescan finds that every custom-cost decision there reads the sale through its bounded adapter (BF-COM, BF-FUR, BF-RF, BF-MEN), the Mengele native costs read the table (D5) and credit Political Power (D27), and their paid event options are BF-EVO rows (D26).
- Event 019 family-management providers: `chaos_unit_family_provider_511` (Event 002), `_512` and `_513` (Event 012), `_514` (Event 010), `_518` (Event 018), `_520` (Event 020), `_521` (CBRN), `_523` (Event 014), and `_524` (Event 039) only report whether the family can spawn or be sustained and charge nothing, so they are `not_a_purchase_cost`. The Event 016 providers `_504` to `_510` and `_522` pay real costs and stay Event 016 `owner adoption pending`. Event 019's own zombie, ghost, and golem providers `_501` to `_503` pay ordinary constants and are accepted and queued with the Event 26 engineer.
- The Part 8 record's conclusion and the registry's freeze rule no longer say Event 26 must stay disabled or wait to be re-enabled.

Basis: the README completion rule requires a disposition for every discovered purchase surface. The lead's round 2 list named the Event 012, 014, 039, and CBRN providers as payers, but their `_event19_pay_management_action` bodies contain no payment, so they join the no-op group; only Event 016 and Event 019's own providers pay.
No gameplay file changes.

Disposition: implemented (documentation). Providers `_501` to `_503` are accepted and queued: they need the price table in their payment, their checks in `019_infantry_spawn_derivative_package_triggers.txt`, and the management cost text.

## D30. Event 019 family management and its own family providers charge the sale price

Decision: the generic family management actions and Event 019's own zombie, ghost, and golem family providers (`chaos_unit_family_provider_501` to `_503`) read the price table (`price_table_version` 12).

- `black_friday_price_table_refresh_entries` registers the 12 `infantry_spawn_family_management_cost` amounts (cantonment, liaison, restricted deployment, containment, and dispersal) and the 14 provider amounts: zombie training and sustainment (`event19_zombie_family`), ghost manifestation and sustainment (`event19_ghost_family`), and golem binding and sustainment (`event19_golem_family`), each as `global.black_friday_price_<group>_<key>`.
- `infantry_spawn_pay_generic_family_management_cost`, the six `infantry_spawn_can_*_selected_family_*` triggers, the provider `_evaluate_management`, `_pay_management_action`, and `_refund_management_action` effects, the derivative `can_authorize`, `can_manifest`, `can_bind`, and `can_pay_family_sustainment` triggers, and every cost, blocked, and tooltip text read the same globals, with the inclusive temp-variable check D18 uses. The dispersal refund on a failed demobilization start and every provider refund return the global they charged in the same effect chain.
- The six management decisions wrap their availability trigger in a `custom_trigger_tooltip` (`infantry_spawn_open_selected_family_cantonment_requirements_tt` and its five siblings), so the requirement line names the requirement instead of raw variable names; `custom_cost_trigger` still blocks them.
- Credit runs once, after a successful payment and never on a refund: `infantry_spawn_credit_generic_family_management_purchase` credits equipment for cantonment, containment, and dispersal (only when the demobilization starts), command power for the liaison, and army experience for restricted deployment; `infantry_spawn_credit_family_provider_purchase` credits equipment for the zombie and golem providers and command power for the ghost provider, at the muster board's train or spawn commit, the selected family's sustainment, and the derivative authorize, manifest, and sustainment payments. Other providers charge nothing or keep their owner's price, so they credit nothing.
- Defect found and fixed with it: `infantry_spawn_publish_registered_family_custom_equipment_tokens` walks the whole registry through `infantry_spawn_current_registry_provider_id`, and the resource snapshots call it between a family's registry lookup and its provider payment, so the muster board request and the derivative manifestation dispatched payment and refund to the last registered provider instead of the selected one. The walk now restores the caller's provider id, and each payment dispatch records the provider it charged in `infantry_spawn_paid_family_provider_id`, which the provider credit reads.

Basis: D29 accepted and queued providers `_501` to `_503` with the Event 26 engineer, Event 019 has no active engineer, and the lead adopted the stopped thread's uncommitted D30 hunks for this round after checking that every new global is registered and every new text key exists. D11 (one global for display, check, and payment), D10 (refunds return the charged price), and D18 (Event 019's inclusive check) apply unchanged. The family request overhead is zero, so it is not a payment. No AI weight, availability rule, or chance changes.

Disposition: implemented (source). Live display, affordability, payment, refund, and credit during a sale are `needs_live_game`.

## D31. Requirement checks follow the price they guard

Decision:
- `decision_utopia_attach_penal_works_to_district` (Event 015) checks its manpower, infantry equipment, and support equipment in `available` against `global.black_friday_price_utopia_manifesto_penal_method_{manpower,infantry_equipment,support_equipment}_cost` with the inclusive temp-variable check its `custom_cost_trigger` already uses, so a country that can pay the sale price is no longer refused by the full-price check. The Common Reserve floor (`reserve_start_floor`) stays.
- `black_plague_shared_armored_clearance` (Event 020) keeps its ordinary 250 infantry equipment check (`constant:black_plague_shared_cost.country_infantry_equipment`). That equipment is an on-hand requirement the action never spends (its cost tooltip says so, and the begin effect pays only the scaled support, truck, and fuel bundle), and D13 keeps on-hand requirements at their ordinary amounts. The defect was the tooltip, which printed the sale price of the Royal Node strike's infantry payment (`GetBlackPlague020SharedCostCountryInfantryEquipmentQuote`); `black_plague_shared_armored_clearance_cost_tooltip` now prints the ordinary constant, so the shown and checked requirement agree in and out of a sale.

Basis: lead decision (4) for round 2 (a requirement that checks the full price of a payment charged at the sale price is a defect under the README completion rule) and D13. The lead's list asked for the armored clearance check to read the sale-price global on the premise that the action pays that equipment; a source read shows it does not, so lowering the requirement would discount a non-purchase. Changing the tooltip instead satisfies the same acceptance scan: no availability, target, or cost check in the converted owners compares against an ordinary constant for a payment charged at the sale price.
A rescan of `005`, `010`, `011`, `013`, `015`, `018`, `019`, `020`, the genocide crisis, and Mengele files for checks against the 756 owner constants the price table registers finds 43 lines. Apart from the two above and the Event 015 Fund appeals option (D33), they are rewards (the Event 005 factory milestone Command Power grants), transfers (Event 005 base arms, Event 015 shipped aid, the reconstruction brigade's delivered support equipment, and the Auxiliary Contract's delivered trucks), pressure calculations (Event 015 calling and trade pressure), or mission objective checks (Event 011 manhunt).
No availability rule outside these two lines and no AI weight changes.

Disposition: implemented (source). The requirement line during a sale is `needs_live_game`.

## D32. The D26 purchase rule covers the converted owners' own events and actions; Event 019's incident options, combat trials, and claimant guard rally charge the sale price

Decision: D26's rule (an action that pays to obtain its outcome is a purchase; a refusal penalty or a consequence is not) applies to the events and remaining paid actions of the owners already converted to the price table, which the D26 scan did not reach. For Event 019 (`price_table_version` 13):
- The eight paid incident options `chaosx.nr19.301.a`, `302.b`, `303.c`, `308.a`, `309.a`, `310.a`, `311.b`, and `312.b` settle an incident on better terms by paying infantry, support, or motorized equipment or Army Experience, so they are purchases. `infantry_spawn_incident.{infantry,support,motorized}_equipment_cost` and `army_experience_cost` register as `global.black_friday_price_infantry_spawn_incident_<key>`, and the option triggers, the payments in the incident choice effects, `infantry_spawn_deferred_incident_choice_check_affordability`, and the option tooltips read them with the inclusive `check_variable` form. A choice deferred by a running scenario transaction rechecks and pays the price current when it resolves, and a choice that cannot pay then is not executed, so it pays and credits nothing. Each paid choice credits one family through `infantry_spawn_credit_incident_purchase` after paying: equipment, or Army Experience for `312.b`, which pays only Army Experience.
- The four achievement combat trials (One-Battalion, Combined-Arms, Borrowed Future, Babel) pay Army Experience and Command Power to stage the trial, so they are purchases. The eight `infantry_spawn_achievement_combat_trial_cost` amounts register as `global.black_friday_price_infantry_spawn_achievement_combat_trial_cost_<key>`, and the cost triggers, the cost set that the start effect checks and debits, and the cost texts read them. The trial credits Army Experience once its border war has started and the cost is debited; a trial that fails to start charges nothing and credits nothing.
- The derivative claimant guard rally pays Army Experience to raise a formation, so it is a purchase. It quotes `constant:infantry_spawn_claimant_cost.another_formation_army_experience` under its own key, `global.black_friday_price_infantry_spawn_derivative_claimant_guard_army_experience`, which its trigger, payment, requirement line, and cost texts read; the claimant's own demand for another formation keeps reading the constant at full price (D18). The rally pays only after the formation materializes and credits Army Experience there.

Basis: lead decisions (2) and (3) for round 2, D26, and D18. The installed effect documentation lists `army_experience` and `add_command_power` as plain value effects, and the existing Event 019 payments already pass temp variables to both. No option trigger is added or removed, and no AI chance or weight changes.

Disposition: implemented (source). Option tooltips, the deferred recheck, the trial and rally debits, and the credit during a sale are `needs_live_game`.

## D33. Event 015's Fund appeals option is a purchase; Event 077's equipment gift is a transfer

Decision:
- `chaosx.nr15.46.a` (Fund appeals and rewrite the conduct rules) pays Political Power to fund the appeals and lower the district's Resistance Target, so under D32 it is a purchase. Its option trigger checks `global.black_friday_price_utopia_manifesto_decision_cost_pp_medium` with an inclusive `greater_than_or_equals` instead of a strict check on the ordinary constant, its payment negates the same global, its option text prints `[?global.black_friday_price_utopia_manifesto_decision_cost_pp_medium|0]` instead of the fixed 40, and its `hidden_effect` calls `black_friday_credit_political_power_purchase` after paying. The inclusive check matches the decision costs D11 converted, so a country holding exactly the shown price can take the option.
- The five `chaosx.nr77.2` options (`.a`, `.b`, `.c`, `.e`, and `.f`; `.d` is the event description) send the chosen stockpile to the selected minor through `send_chosen_equipment`, which the minor receives one for one, so they are transfers under D11 and `not_a_purchase_cost` (registry BF-EVO-050 to BF-EVO-054).

Basis: lead decision (2) for round 2, D26, D11, and D32. A scan of the converted owners' events (`005`, `010`, `011`, `013`, `015`, `018`, `019`, `020`) for options that pay a registered owner constant or a negative literal amount found only Fund appeals and the Event 019 incident options (D32); after this change no option in those events reads a constant the price table registers. The AI chance of `chaosx.nr15.46.a` is unchanged.

Disposition: implemented (source). The option text amount and the sale debit are `needs_live_game`.

## D34. Refunded purchases earn no achievement credit

Decision:
- `infantry_spawn_derivative_rally_zombie_band` (Event 019) credits the equipment family only in the `infantry_spawn_derivative_materialization_succeeded` branch, after the band materializes. The rollback branch refunds the charged manpower and equipment and no longer keeps a credit for them.
- The three retired Mengele import decisions (`import_subjects_from_japanese_china`, `import_subjects_from_india`, and `import_subjects_from_africa`) no longer call `black_friday_credit_political_power_purchase`. They cannot be seen or taken (`allowed` and `visible` are `always = no`), and a stale completion refunds the charged price in the same `complete_effect`, so it buys nothing. D27's count of decisions that credit Political Power at the start of `complete_effect` is 269 after this change.

Basis: the spec's Part 5 achievement-farming rule (refunded transactions do not count) and D10 (refunds return the charged price). No payment, availability, or AI weight changes.

Disposition: implemented (source).

## D35. The Formation Ledger refreshes its family availability when a sale starts and ends

Decision: `black_friday_price_table_refresh_owner_quotes` rebuilds the Event 019 Formation Ledger view (`infantry_spawn_muster_board_refresh_if_open`) on each participant in Evolution IV, right after its request cost refresh.
The ledger caches each family's train, spawn, and sustainment availability (`infantry_spawn_muster_gui_family_can_train_entries`, `_can_spawn_entries`, and `_can_sustain_entries`) from the provider `_evaluate_management` effects, which compare the family prices since D30, and the "Meet the Family's Obligations" and anomalous request decisions read that cache.
Without the refresh, a sale left the cache at the old price until the next weekly Event 019 pulse: a family affordable only at the sale price stayed unavailable for up to a week, and after the sale a decision could stay clickable for a payment the provider then refused.

Basis: review of D30 for round 2. Event 019 already rebuilds the view inside `every_country` when it applies Evolution IV, and the rebuild keeps its own idle-transaction guard. Payments were never affected, because each provider re-evaluates the price at payment.
No price, payment, credit, or AI weight changes.

Disposition: implemented (source). The ledger's availability on the day a sale starts and ends is `needs_live_game`.

## D36. Native sale discounts multiply each country's current price

Decision:
- The native discounts move from fixed -0.5 and -0.75 values in the two sale ideas and two dynamic modifiers to one country dynamic modifier, `black_friday_native_sale` (`common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt`), whose 580 keys each read a country variable `black_friday_sale_<key>`.
- `black_friday_native_sale_apply` (`common/scripted_effects/026_black_friday_native_sale_effects.txt`) sets each variable to (payment ratio - 1) x max(0, 1 + ordinary), where ordinary is `modifier@<key>` minus the stored value when the modifier is already applied, adds the modifier when it is missing, and runs `force_update_dynamic_modifier`. `black_friday_refresh_active_cost_modifier` calls it for every country at activation and again on the report option, a tag switch, and enabling the event system for a country, so a repeated refresh never counts the sale twice. `black_friday_clear_active_status` runs `black_friday_native_sale_remove` on every possible country that received the sale, which removes the modifier and clears all 580 variables, including on a country that ceased to exist during the sale day.
- The two sale ideas keep no cost modifiers and stay the visible status marker, with one `custom_modifier_tooltip` (`black_friday_sale_native_tt`) naming what the sale discounts.
- One carrier per purchase: where two keys can price the same purchase, only one carries the sale, and the most negative ordinary value of the other (never above zero) joins the carrier's ordinary factor. The slot factors carry advisors and staff and read the ledger factors (`army_advisor_cost_factor`, `navy_advisor_cost_factor`, `air_advisor_cost_factor`): chiefs and designers read their fixed ledger from vanilla `common/idea_tags/00_idea.txt` `slot_ledgers`, high command and theorists read the most negative of the three, and political advisors read the army ledger only, because every vanilla political advisor with a ledger (ten characters in LAT, LIT, POL, PRC, and SIA) uses it. `army_leader_cost_factor` and `navy_leader_cost_factor` read `military_leader_cost_factor` (D2). The three officer corps category type factors carry the spirits and read their nine slot group factors, which vanilla never uses. The 81 equipment archetype design keys carry designs; the 114 concrete type keys ending in `_0` to `_5` are dropped, because vanilla's `dive_bombing_spirit` discounts CAS designs through the archetype key `small_plane_cas_airframe_design_cost_factor` (`common/ideas/air_spirits.txt:53`) and no vanilla file uses a concrete key.
- `promote_cost_factor` leaves the sale (strategy D). Vanilla unit-leader traits add to it at leader scope (`politically_connected`, -50%, `common/unit_leader/00_traits.txt:154-161`), which a country variable cannot read or offset, and a -50% sale on a promotion with base 40 (`common/defines/00_defines.lua:1146`) would make it free. Leader promotions join the keep-normal-price sentence in `chaosx.nr26.2.d`, `black_friday.event_detail.premise`, and the Details row in `catalog_changes_pending.md`.
- `annex_cost_factor` and `puppet_cost_factor` leave the sale. `common/peace_conference/cost_modifiers/026_black_friday_peace_cost_modifiers.txt` adds `black_friday_peace_sale` (`cost_multiplier` 0.5) and `black_friday_peace_sale_evolution_i` (0.25) for `take_states` and `puppet`, each enabled only while the sale is active at its ratio, in the vanilla `events_or_focuses` category.
- `black_friday_native_sale` is localised as "Black Friday", so cost tooltips that list modifier sources name the sale.

Basis: lead decision (b) for round 3 and the 2026-10-03 native composition audit. The offline wiki Modifiers page (line 57; reference search revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`) adds every contribution to a key into one total, and its Dynamic modifiers section (lines 108-122) documents variable values and `force_update_dynamic_modifier`; `documentation/dynamic_variables_documentation.md:496-498` documents `modifier@` as a country-scope modifier value. The spec Part 3 order (multiply the ordinary current cost) and the Part 9 hard blocker (a positive cost can become zero) require compensation: with the former flat factors, an ordinary -25% advisor paid 25% instead of 37.5% at baseline and nothing at 75% off, a +25% surcharge received less than half off, and slot plus ledger factors (both -0.5) could make military staff free. Wiki Modifiers lines 561-562 mark `annex_cost_factor` and `puppet_cost_factor` partially deprecated in favour of peace conference cost modifiers, which the installed `common/peace_conference/cost_modifiers/_documentation.md` multiplies together.
Worked checks: a 150 Political Power advisor with an ordinary -25% has ordinary factor 0.75, so it costs 150 x 0.75 x 0.5 = 56.25 (56) at 50% off and 28.125 (28) at 75% off; an ordinary +25% leaves 1.25 x 0.5 = 0.625 of base at 50% off; an ordinary -100% gives max(0, 0) = 0 and stays free.
Residual cases: when a linked key carries an ordinary discount, the carrier's purchases pay somewhat more than the exact sale price (for example, a democracy with `relief_of_command_spirit`, army advisors -50%, pays 75% of its political advisor price at baseline instead of 50%), never less and never nothing, whether the engine adds or multiplies the two keys. Whether the engine adds a duplicated equipment archetype's parent archetype key to the same design (for example `heavy_tank_chassis` for `heavy_tank_aa_chassis`), how module and equipment design factors combine, how the engine rounds native prices, and whether the designer factors also scale Arms Against Tyranny organization costs (`LEGACY_COST_FACTOR_SCALE` in `common/defines/00_defines.lua`) are `needs_live_game`.
Activation computes the 580 values once per existing country, a one-time pass of about 3,500 effect steps per country when the sale starts; no daily or weekly scan is added.
No AI weight, chance, or availability rule changes.

Disposition: implemented (source). Registry rows BF-NAT-002, 003, 004, 005, 010 (embargo), 013, 015, 018, 019, and 020 and BF-DES-001 to 003 move to implemented (source). Native prices, tooltips, and debits during a sale, the peace conference multiplier, and save and reload of the stored values are `needs_live_game`.

## D37. License fees leave the sale

Decision: `license_infantry_eq_cost_factor`, `license_artillery_eq_cost_factor`, `license_light_tank_eq_cost_factor`, and `license_anti_tank_eq_cost_factor` are not carried by any Black Friday idea or dynamic modifier. Registry row BF-NAT-011 becomes `not_a_purchase_cost`.

Basis: lead decision (c) for round 3. The installed license request text says the licensee pays the civilian factories "while the license is active" (`localisation/english/diplomacy_l_english.yml:376`), and `modifiers_l_english.yml:994-997` names these four fields "License purchase cost" for that fee. An ongoing factory commitment is passive upkeep under spec Part 4, the same reason D3 removed the trade upkeep factors. The report (`chaosx.nr26.2.d`) and Event Details premise (`black_friday.event_detail.premise`) already say license purchases keep their normal price, which is now true without a text change.

Disposition: implemented (source).
