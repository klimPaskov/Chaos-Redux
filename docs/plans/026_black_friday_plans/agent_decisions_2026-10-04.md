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
