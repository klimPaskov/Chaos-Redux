# Event 026 — Black Friday

## Current status

Event 26 preserves `chaosx.nr26.1` as the canonical actorless entry and remains classified as Minor Fire-Once. It is on the default-enabled event list (`event_log_event_is_reworked_default_enabled`), so a new campaign starts with it enabled (agent decision D8). Owner custom costs that have not adopted the sale yet charge their ordinary price and carry per-owner dispositions in the cost registry; live acceptance evidence is still pending, and the catalog status stays Needs Testing.

## Gameplay contract

Black Friday is eligible at Gathering Storm and 200 Chaos. Automatic selection reserves it globally, rejects the reserved event from later candidate evaluation without mutating its stored weight, resolves the active selection timer without recording history, and waits for the first Friday at or above 200 Chaos.

Friday activation records one event, applies minor pacing and one dynamic major gain, broadcasts one report to each human player, and snapshots the sale rate. The baseline is 50 percent off, and Evolution I is 75 percent off when enabled at 600 Chaos or higher. Later Chaos changes and Evolution toggles do not mutate the snapshot. The sale expires on the next daily tick.

The shared Friday helper uses the absolute `global.num_days` day index with a seven-day cycle and remainder six (`friday_remainder` in `common/script_constants/026_black_friday_constants.txt`). `global.num_days` counts days since the start of year 0 in the engine's 365-day calendar: the offline wiki's Data structures page gives 706640 for 1 January 1936, and a save dated 1936.1.3 stores 706642 for a variable set from `global.num_days`. 3 January 1936 was a Friday and 706642 % 7 = 6, so the sale can open on 3 January 1936, 10 January 1936, and every seven days after. The engine calendar has no leap days, so after each skipped 29 February the in-game Friday drifts one weekday from the real calendar; the seven-day rhythm is kept as the in-game week rather than corrected.

Disable clears only a pending reservation. Re-enabling does not restore a canceled reservation. A Friday activation reached from the reservation path does not recalculate the timer that was already resolved at selection, and the reservation's natural-selection provenance persists until activation or cancellation. Manual launches keep the ordinary reservation and Friday rules, while Force Trigger Mode bypasses those gates; both settings paths preserve an already-running timer and disqualify the natural-sale achievement. Terminal cleanup removes pending or active Event 26 state without leaving a permanent sale.

## Runtime ownership

`events/026_black_friday.txt` owns the canonical entry and the player-facing report event. `common/scripted_effects/026_black_friday_effects.txt` owns lifecycle state, Friday arithmetic, pacing, activation, expiry, status refresh, event-log integration, and achievement receipts.

The implementation uses the existing bounded global event-system daily pulse and the existing country status refresh hook. It does not add a new country-wide daily scan.

## Cost contract and completion gate

The reusable framework is implemented in `common/scripted_effects/chaosx_universal_cost_effects.txt`, `common/scripted_triggers/chaosx_universal_cost_triggers.txt`, `common/script_constants/chaosx_universal_cost_constants.txt`, and the corresponding Markdown references.

The effect quotation and custom-cost trigger share `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt` as their exact producer.
It multiplies represented source ratios in integer limbs and quantizes once, without an overflowing scalar numerator or a truncated composed-ratio cache.
Native execution, duplicate-preserving token iteration, and consumer performance remain acceptance gates in the [exact implementation handoff](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_exact_quote_implementation.md).

Black Friday multiplies the ordinary current payable cost after ordinary modifiers and before final quantization. One quote is shared by display, affordability, payment, receipt, and refund. Positive values round upward to at least one registered quantum, zero remains zero, and rewards, penalties, casualties, upkeep, time, cooldowns, and non-cost requirements remain outside the source.

The 39 Vanilla `cat_*_cost_factor` technology fields, factory-conversion cost factors, and `refit_ic_cost` are audited exclusions rather than sale modifiers: they alter research, construction, or production time instead of charging an atomic voluntary payment. Doctrine XP costs and designer XP payments remain in scope through their distinct payable-cost modifiers.

Native decision costs have no engine modifier, so Chaos Redux decisions read their political power price from the sale price table in `common/scripted_effects/026_black_friday_price_table_effects.txt`. Each registered ordinary amount has one global price, `global.black_friday_price_<key>`, that equals the ordinary amount outside a sale and the rounded-up sale price, at least 1, while a sale is active, so the engine's display, affordability, debit, and AI evaluation read one value. The 15 owner files without an active engineer, including the overridden base-game `formable_nation_decisions.txt`, read the table; active workstream owners adopt it in their own files. Base-game decision files that Chaos Redux does not override keep their normal price, and the report event and Event Details tell the player so (agent decisions D4, D5, and D7 in `docs/plans/026_black_friday_plans/agent_decisions_2026-10-04.md`).

Owner custom costs with a constant ordinary amount register that constant in the same table and read the global in their `custom_cost_trigger`, payment, and cost text (D11); a sale price never exceeds the ordinary price. Event 015 Utopia Manifesto (D11), Event 013 Natural Disasters (D12), Event 020 Black Plague's fixed amounts (D13), the genocide crisis decisions (D16), Event 010 Death (D17), Event 019 Infantry Spawn's fixed amounts (D18), and Event 005 Soviet Collapse (D21, including foreign aid tier surcharges that add up to the checked tier price) are converted this way; Event 020's population-scaled response quotes, Event 015's growth costs (D15), Event 019's formation requests (D18), Event 011's cached response costs (D19), and Event 018's project estimates (D20) apply the ratio the table holds, recorded in `global.black_friday_price_table_ratio`, and are refreshed through `black_friday_price_table_refresh_owner_quotes` when the sale starts and ends. Variable custom costs use the simple custom-cost API in `common/scripted_effects/026_black_friday_simple_cost_api.md` (D9). Each converted owner credits one achievement family per paid action through `black_friday_credit_sale_purchase`.

The completion-gating registry is `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`. Its exact custom declaration inventory is `event26_cost_surface_custom_inventory.md`, its native decision declaration inventory is `event26_cost_surface_native_inventory.md`, and its exact installed design-modifier inventory is `event26_design_modifier_inventory.md`. The earlier 104-component adapter inventory includes retired Japan chemical and biological attack decisions and is historical evidence, not current native-raid payment coverage. Other bounded source adapters and remaining owner-controlled custom surfaces still need their individual completion evidence. Flat MIO assignment and policy, operation, equipment-upgrade, guarantee, license-purchase, special-project, leader/tactic, assignable-trait, and factory-commitment costs remain engine-inaccessible or owner-bound registry rows with their own dispositions.

## Presentation and assets

The report event uses `GFX_report_event_026_black_friday` and `gfx/event_pictures/026_black_friday/black_friday_report.dds`. The sale idea uses `GFX_idea_026_black_friday_sale`, and the achievement uses the normal, grey, and not-eligible sprites registered in `interface/026_black_friday.gfx`.

The shared Events list and Event Details framework provide the truthful disabled, eligible, reserved, active, fired, evolution, premise, source, actorless-history, and debug mappings. The achievement key is `026_black_friday_five_departments`.

The Evolution I threshold and discount, and the achievement's five-family target, are displayed through `common/scripted_localisation/026_black_friday_scripted_localisation.txt` from the same script constants used by their conditions. The [binding handoff](../plans/026_black_friday_plans/subagent_handoffs/event026_constant_text_binding.md) records the vanilla precedent and the still-partial event render.

For that achievement, an ordinary paid purchase must commit during a naturally selected sale. A discounted native Japan chemical or biological raid prepared during the sale contributes the equipment family only when a successful accepted release resolves, even after expiry. The outcome marker, native reservation, human-country eligibility, and sale sequence are checked without a synthetic purchase receipt. Failed or canceled raids do not credit a family. Existing family progress remains until the delayed outcome; ordinary post-expiry purchases remain ineligible.

Purchases the engine prices through the sale ideas also count toward the achievement. Activation snapshots each eligible human country's law in every law category, its filled political advisor slots, its filled theorist, chief, and high command slots, its army, navy, and air experience, and its command power. At expiry, before the sale source clears, a changed law credits the laws family, more advisors credit personnel, more senior staff credit officer corps, and a net experience or command power decrease credits that family and counts as the payment in a resource other than political power. The law ids live in the `black_friday_engine_law` constant table, and the comparison is `black_friday_engine_purchase_credit` (agent decision D6).

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

The required offline source, wiki, vanilla documentation, asset, localisation, spreadsheet, event-inspection, and probability-inspection reviews are recorded under `docs/plans/026_black_friday_plans/`. The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; its Event 26 premise and evolution cells match the current game text, and it has no achievement field to update for this rule. Its existing CSV exports remain unchanged. The Event 26 row remains `Needs Testing` until live validation passes.

Part 8 acceptance status is recorded in `docs/plans/026_black_friday_plans/event26_part8_acceptance.md`. No HOI4 process was launched by the coding agent, and no live or multiplayer evidence is claimed.

## Future extension

Once the registry is closed, additional temporary cost sources can register through the same priority and family-mask contract without changing Event 26 lifecycle state. Further sale evolutions should add only registered ratios and corresponding preview, log, and acceptance rows.
