# Event 026 — Black Friday

## Current status

Event 26 preserves `chaosx.nr26.1` as the canonical actorless entry and remains classified as Minor Fire-Once.
It remains default-disabled until the complete cost registry, implementation surfaces, and required acceptance gates are finished.
Unadapted owner costs, native composition and quantization, exact inaccessible-surface proof, and live acceptance remain unresolved.
The catalog status must remain Needs Testing until live validation passes.

## Gameplay contract

Black Friday is eligible at Gathering Storm and 200 Chaos. Automatic selection reserves it globally, rejects the reserved event from later candidate evaluation without mutating its stored weight, resolves the active selection timer without recording history, and waits for the first Friday at or above 200 Chaos.

Friday activation records one event, applies minor pacing and one dynamic major gain, broadcasts one report to each human player, and snapshots the sale rate. The baseline is 50 percent off, and Evolution I is 75 percent off when enabled at 600 Chaos or higher. Later Chaos changes and Evolution toggles do not mutate the snapshot. The sale expires on the next daily tick.

The shared Friday helper uses the absolute `global.num_days` day index with a seven-day cycle and remainder six (`friday_remainder` in `common/script_constants/026_black_friday_constants.txt`). `global.num_days` counts days since the start of year 0 in the engine's 365-day calendar: the offline wiki's Data structures page gives 706640 for 1 January 1936, and a save dated 1936.1.3 stores 706642 for a variable set from `global.num_days`. 3 January 1936 was a Friday and 706642 % 7 = 6, so the sale can open on 3 January 1936, 10 January 1936, and every seven days after. The engine calendar has no leap days, so after each skipped 29 February the in-game Friday drifts one weekday from the real calendar; the seven-day rhythm is kept as the in-game week rather than corrected.

Disable clears only a pending reservation. Re-enabling does not restore a canceled reservation. A Friday activation reached from the reservation path does not recalculate the timer that was already resolved at selection, and the reservation's natural-selection provenance persists until activation or cancellation. Manual launches keep the ordinary reservation and Friday rules, while Force Trigger Mode bypasses those gates; both settings paths preserve an already-running timer and disqualify the natural-sale achievement. Terminal cleanup removes pending or active Event 26 state without leaving a permanent sale.

## Runtime ownership

`events/026_black_friday.txt` owns the canonical entry and the player-facing report event. `common/scripted_effects/026_black_friday_effects.txt` owns lifecycle state, Friday arithmetic, pacing, activation, expiry, status refresh, event-log integration, and achievement receipts. `common/scripted_effects/026_black_friday_native_sale_effects.txt` owns the per-country native sale values read by the `black_friday_native_sale` dynamic modifier in `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt`, and `common/peace_conference/cost_modifiers/026_black_friday_peace_cost_modifiers.txt` owns the peace conference discount.

The implementation uses the existing bounded global event-system daily pulse and the existing country status refresh hook. It does not add a new country-wide daily scan.

## Cost contract and completion gate

The reusable framework is implemented in `common/scripted_effects/chaosx_universal_cost_effects.txt`, `common/scripted_triggers/chaosx_universal_cost_triggers.txt`, `common/script_constants/chaosx_universal_cost_constants.txt`, and the corresponding Markdown references.

The effect quotation and custom-cost trigger share `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt` as their exact producer.
It multiplies represented source ratios in integer limbs and quantizes once, without an overflowing scalar numerator or a truncated composed-ratio cache.
Native execution, duplicate-preserving token iteration, and consumer performance remain acceptance gates in the [exact implementation handoff](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_exact_quote_implementation.md).

Black Friday multiplies the ordinary current payable cost after ordinary modifiers and before final quantization. One quote is shared by display, affordability, payment, receipt, and refund. Positive values round upward to at least one registered quantum, zero remains zero, and rewards, penalties, casualties, upkeep, time, cooldowns, and non-cost requirements remain outside the source.

Engine-priced purchases (laws, advisors and military staff, designers, officer corps spirits, doctrines, equipment, module, and unit designs, command abilities, medals, commander recruitment and appointment as advisor, embargoes, and subject annexation) are discounted by one country dynamic modifier, `black_friday_native_sale`, with 580 cost keys. HOI4 adds every contribution to a modifier key into one total, so a flat -50% would add to a country's own discounts: an ordinary -25% plus the sale would leave 25% of the price instead of 37.5%, and an ordinary -50% would make the purchase free. Each key's value is therefore a per-country variable, set when the sale starts and whenever the country's status refreshes, to (payment ratio - 1) x max(0, 1 + ordinary), where ordinary is the key's current total (`modifier@<key>`) without the sale's own value. The engine then charges base x payment ratio x (1 + ordinary): a 150 Political Power advisor with an ordinary -25% costs 56 at 50% off and 28 at 75% off, a +25% surcharge leaves 62.5% of the base price at 50% off, and an ordinary -100% stays free. The two sale ideas carry no modifiers; they show the sale in the national spirits with one line naming what it discounts.

Each purchase is priced by exactly one carried key. Where a second key can price the same purchase (the army, navy, and air advisor ledger factors beside the slot factors, `military_leader_cost_factor` beside the army and navy leader factors, the officer corps slot groups beside their category type, and the 114 concrete equipment type design keys beside their archetype key), the second key carries no sale value, and its most negative ordinary value (never above zero) joins the carrier's ordinary factor. Under unchanged ordinary factors the linked-key treatment computes a conservative contribution. Exact native composition and cost changes during the sale remain unresolved under D42. Political advisors read only the army ledger, the one ledger vanilla gives them.

Leader promotions keep their normal price: unit-leader traits such as `politically_connected` add to `promote_cost_factor` at leader scope, which a country value cannot offset, so a sale on it could make a promotion free. License fees keep their normal price because the licensee pays them while the license is active, which is upkeep. Peace conference demands to take states or puppet a country are discounted by two `peace_action_modifiers` entries whose `cost_multiplier` is the sale's payment ratio; the installed peace conference documentation multiplies all active cost modifiers, so the discount applies to the price the other modifiers produce (agent decisions D36 and D37).

The 39 Vanilla `cat_*_cost_factor` technology fields, factory-conversion cost factors, and `refit_ic_cost` are audited exclusions rather than sale modifiers: they alter research, construction, or production time instead of charging an atomic voluntary payment. Doctrine XP costs and designer XP payments remain in scope through their distinct payable-cost modifiers.

Native decision costs have no engine modifier, so Chaos Redux decisions read their political power price from the sale price table in `common/scripted_effects/026_black_friday_price_table_effects.txt`. Each registered ordinary amount has one global price, `global.black_friday_price_<key>`, that equals the ordinary amount outside a sale and the rounded-up sale price, at least 1, while a sale is active, so the engine's display, affordability, debit, and AI evaluation read one value. The 15 owner files without an active engineer, including the overridden base-game `formable_nation_decisions.txt`, read the table; active workstream owners adopt it in their own files. Base-game decision files that Chaos Redux does not override keep their normal price (agent decisions D4, D5, and D7 in `docs/plans/026_black_friday_plans/agent_decisions_2026-10-04.md`). Taking a converted decision during a valid natural sale credits Political Power toward the achievement through `black_friday_credit_political_power_purchase`, unless its own payment already credits a material family (D27). The report event and the Event Details premise end with one sentence naming every purchase the sale cannot change: base-game national decisions, guarantees, intelligence operations, license purchases, military-industrial organizations, equipment upgrades, leader promotions, leader traits, preferred tactics, and special projects (D24, D36).

Owner custom costs with a constant ordinary amount register that constant in the same table and read the global in their `custom_cost_trigger`, payment, and cost text (D11); a sale price never exceeds the ordinary price. Event 015 Utopia Manifesto (D11), Event 013 Natural Disasters (D12), Event 020 Black Plague's fixed amounts (D13), the genocide crisis decisions (D16), Event 010 Death (D17), Event 019 Infantry Spawn's fixed amounts (D18) and its family management and own family providers (D30), and Event 005 Soviet Collapse (D21, including foreign aid tier surcharges that add up to the checked tier price) are converted this way; Event 020's population-scaled response quotes, Event 015's growth costs (D15), Event 019's formation requests (D18), Event 011's cached response costs (D19), and Event 018's project estimates (D20) apply the ratio the table holds, recorded in `global.black_friday_price_table_ratio`, and are refreshed through `black_friday_price_table_refresh_owner_quotes` when the sale starts and ends. Variable custom costs use the simple custom-cost API in `common/scripted_effects/026_black_friday_simple_cost_api.md` (D9). Each converted owner credits one achievement family per paid action through `black_friday_credit_sale_purchase`.

Paid event options in owners without an active engineer follow the same table (D26): an option that buys its outcome pays the registered price, shows it in the option tooltip, and credits one achievement family, while refusal penalties and consequences keep their ordinary amounts. The five purchases are Deploy security detachments and Launch emergency intervention now (Event 001), Remove the Arhat quietly (Event 003), Pay him (Event 053), and Just end them (Event 078); the registry lists the other 35 options with their reasons. The same rule covers the converted owners' own events and actions (D32): Event 019's eight paid incident options, its four achievement combat trials, and its derivative claimant guard rally charge the sale price. Event 015's Fund appeals option charges the sale price as well (D33), while Event 077's equipment gift to another country stays a transfer at its full amount.

The completion-gating registry is `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`. Its exact custom declaration inventory is `event26_cost_surface_custom_inventory.md`, its native decision declaration inventory is `event26_cost_surface_native_inventory.md`, and its exact installed design-modifier inventory is `event26_design_modifier_inventory.md`. The earlier 104-component adapter inventory classified Japan chemical and biological decision payments as retired; that classification is historical. The Japanese chemical direct decision is restored in the current source alongside native raids, and its custom quote/debit/refund path requires separate source review rather than relying on native-raid payment evidence. Other bounded source adapters and remaining owner-controlled custom surfaces still need their individual completion evidence. Flat MIO assignment and policy, operation, equipment-upgrade, guarantee, license-purchase, special-project, leader/tactic, assignable-trait, and factory-commitment costs remain engine-inaccessible or owner-bound registry rows with their own dispositions.

## Presentation and assets

The report event uses `GFX_report_event_026_black_friday` and `gfx/event_pictures/026_black_friday/black_friday_report.dds`. The sale idea uses `GFX_idea_026_black_friday_sale`, and the achievement uses the normal, grey, and not-eligible sprites registered in `interface/026_black_friday.gfx`.

The shared Events list and Event Details framework provide the truthful disabled, eligible, reserved, active, fired, evolution, premise, source, actorless-history, and debug mappings. The achievement key is `026_black_friday_five_departments`.

The Evolution I threshold and discount, and the achievement's five-family target, are displayed through `common/scripted_localisation/026_black_friday_scripted_localisation.txt` from the same script constants used by their conditions. The [binding handoff](../plans/026_black_friday_plans/subagent_handoffs/event026_constant_text_binding.md) records the vanilla precedent and the still-partial event render.

13 October 2026 direct Japan restoration: the historical campaign decision, custom quote and refund helpers are active again alongside the native raid route. The decision uses the current universal-cost source and keeps the selected-agent cylinder and Command Power charges; this source restoration has not established live sale display, multiplayer payment, save/reload, or refund behavior.

For that achievement, an ordinary paid purchase must commit during a naturally selected sale. A discounted native Japan chemical or biological raid prepared during the sale contributes the equipment family only when a successful accepted release resolves, even after expiry. The outcome marker, native reservation, human-country eligibility, and sale sequence are checked without a synthetic purchase receipt. Failed or canceled raids do not credit a family. Existing family progress remains until the delayed outcome; ordinary post-expiry purchases remain ineligible.

Purchases the engine prices through the native sale modifier use bounded achievement inference. Activation snapshots each eligible human country's law in every law category, its filled political advisor slots, its filled theorist, chief, and high command slots, its Political Power, its army, navy, and air experience, and its Command Power. At expiry, before the sale source clears, a changed law or increased advisor count requires a net Political Power decrease before it credits laws or personnel. Increased senior staff requires a net Political Power or Command Power decrease before it credits officer corps. A net experience or command power decrease credits that family and counts as payment in a resource other than Political Power. Free changes alone do not earn institutional credit. Unrelated losses can still coincide with changes, and gains can mask real spending, so these readings are not individual purchase proof. The law ids live in the `black_friday_engine_law` constant table, and the comparison is `black_friday_engine_purchase_credit` (agent decision D6).

Timed CBRN Protective Aid reserves its full physical respirator shipment and discounts only the voluntary Political Power service fee. Its payer-scoped receipt and saved sale sequence permit PP-family credit after a proven delivery, including completion after expiry; cancellation retains the spent fee but earns no family. The PP-only proof validates the settled Black Friday component and actual payment, and does not satisfy the achievement's separate non-political-payment requirement. The native two-factory commitment still lacks sale coverage, as recorded in the [aid contract](../plans/026_black_friday_plans/2026-10-03_cbrn_protective_aid_pp_adapter.md).

The five existing South Africa purchases use one owner bundle with eleven resource components, fresh cost text, preflight checks, actual-paid receipts, and outcome-gated settlement.
Their [owner contract and component ledger](../systems/africa_rsa_purchase_transactions.md) retain the original routes, targets, limits, cooldowns, and AI weights.
All five use Political Power as the primary achievement family, and their flags do not establish an institutional-law purchase.
Native execution, UI expansion, probability comparison, and save/reload evidence remain pending.

The [existing-owner caller migration](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_existing_owner_caller_integration.md) establishes consumed temporary output storage in 16 further source files.
Its 454 known-call inventory and 17 actual-fragment scenarios remain bounded source evidence.
The [Condemnation provider correction](../plans/026_black_friday_plans/2026-10-03_condemnation_provider_lifetime_fix.md) restores ordinary score-scaled prices before any future sale adapter, and does not discount ongoing inspection burden.
The source purchase registry remains incomplete.

Ordinary achievement calls prove source 26, recorded positive prices, an explicit logical family and primary-cost basis, matching caller amounts, and the required unrefunded receipt state.
Immediate credit requires settlement, while refundable pending rows earn no family until their valid confirmation.
The [receipt proof contract](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_achievement_receipt_proof_repair.md) preserves the accepted delayed PP and native Japan raid exceptions without inferring a family from the currency.
Untyped existing receipt rows retain their payment, refundability, pending state, and earned progress, but cannot acquire missing family proof by inference.
The full family and native purchase registry remains a separate completion gate.

## Validation record

The required offline source, wiki, vanilla documentation, asset, localisation, spreadsheet, event-inspection, and probability-inspection reviews are recorded under `docs/plans/026_black_friday_plans/`. The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Current premise and evolution wording is queued for the workbook owner in `docs/plans/026_black_friday_plans/catalog_changes_pending.md`, so alignment is not claimed. This pass edits neither the workbook nor its exported CSVs. The Event 26 row remains `Needs Testing` until the required acceptance is established.

Part 8 acceptance status is recorded in `docs/plans/026_black_friday_plans/event26_part8_acceptance.md`. No HOI4 process was launched by the coding agent, and no live or multiplayer evidence is claimed.

## Takeover review on 6 October 2026

Caller-owned temporary storage preserves native linked-factor compensation, law and slot readings, and simple custom-cost API results. The source regressions and design decisions are recorded in `docs/plans/026_black_friday_plans/agent_decisions_2026-10-05.md`.

A rejected manual or forced entry sends one captured-reason report, `chaosx.nr26.3`, at most once per human country. Repeated requests do not duplicate it. The ordinary chain sends one activation report. The notice reuses `GFX_report_event_026_black_friday` and changes neither the history nor the sale.

Exact native pricing remains incomplete. Some appointments with overlapping discounts receive smaller savings under D36, which the report and sale tooltip disclose. The stored contribution can also become stale if another cost modifier changes during the sale: adding an ordinary -25% factor after a 75% contribution was calculated can produce a zero multiplier before an explicit refresh. The source regression retains that counterexample as a completion blocker. No whole-world recurring refresh or engine behavior is inferred as a remedy.

## Implementation acceptance gate

Black Friday remains default-disabled until every requested cost row, asset, localisation surface, log, document, audit, catalog field, and test is complete.
The October 4 D8 enablement is superseded by the original user goal and the October 7 continuation correction.
The source framework and bounded adapters are implemented, but the complete final-commit semantic registry, exact inaccessible-surface evidence, native composition and minimum-payment proof, multiplayer and persistence acceptance, and live Part 8 scenarios remain unresolved.
The catalog must remain `Needs Testing` until live validation passes.

## Future extension

A later native cost key enters the sale by adding it to `black_friday_native_sale` and to the store and clear lists in `026_black_friday_native_sale_effects.txt`; a key that shares its purchase with a carried key joins that carrier's linked ordinary instead of carrying a second sale value.

Once the registry is closed, additional temporary cost sources can register through the same priority and family-mask contract without changing Event 26 lifecycle state. Further sale evolutions should add only registered ratios and corresponding preview, log, and acceptance rows.
