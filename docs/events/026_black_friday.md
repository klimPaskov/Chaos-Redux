# Event 026 — Black Friday

## Current status

Event 26 preserves `chaosx.nr26.1` as the canonical actorless entry and remains classified as Minor Fire-Once. The default allowlist keeps it disabled until the universal cost registry, owner adapters, engine-inaccessible dispositions, and live acceptance evidence are complete.

## Gameplay contract

Black Friday is eligible at Gathering Storm and 200 Chaos. Automatic selection reserves it globally, rejects the reserved event from later candidate evaluation without mutating its stored weight, resolves the active selection timer without recording history, and waits for the first Friday at or above 200 Chaos.

Friday activation records one event, applies minor pacing and one dynamic major gain, broadcasts one report to each human player, and snapshots the sale rate. The baseline is 50 percent off, and Evolution I is 75 percent off when enabled at 600 Chaos or higher. Later Chaos changes and Evolution toggles do not mutate the snapshot. The sale expires on the next daily tick.

The shared Friday helper uses the absolute `global.num_days` day index with a seven-day cycle and remainder two. The project date contract records 17 June 1938 as day 898 from 1 January 1936; 3 January 1936, day 898, and 1 September 1939 all resolve to remainder two and are Fridays. Installed Vanilla exposes no weekday predicate or Friday-index precedent, so the source anchor is documented while the live acceptance row remains open.

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

The completion-gating registry is `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`. Its exact custom declaration inventory is `event26_cost_surface_custom_inventory.md`, its native decision declaration inventory is `event26_cost_surface_native_inventory.md`, and its exact installed design-modifier inventory is `event26_design_modifier_inventory.md`. The earlier 104-component adapter inventory includes retired Japan chemical and biological attack decisions and is historical evidence, not current native-raid payment coverage. Other bounded source adapters and remaining owner-controlled custom surfaces still need their individual completion evidence. Flat MIO assignment and policy, operation, equipment-upgrade, guarantee, license-purchase, special-project, leader/tactic, assignable-trait, and factory-commitment costs remain engine-inaccessible or owner-bound registry rows, so the event remains disabled.

## Presentation and assets

The report event uses `GFX_report_event_026_black_friday` and `gfx/event_pictures/026_black_friday/black_friday_report.dds`. The sale idea uses `GFX_idea_026_black_friday_sale`, and the achievement uses the normal, grey, and not-eligible sprites registered in `interface/026_black_friday.gfx`.

The shared Events list and Event Details framework provide the truthful disabled, eligible, reserved, active, fired, evolution, premise, source, actorless-history, and debug mappings. The achievement key is `026_black_friday_five_departments`.

The Evolution I threshold and discount, and the achievement's five-family target, are displayed through `common/scripted_localisation/026_black_friday_scripted_localisation.txt` from the same script constants used by their conditions. The [binding handoff](../plans/026_black_friday_plans/subagent_handoffs/event026_constant_text_binding.md) records the vanilla precedent and the still-partial event render.

For that achievement, an ordinary paid purchase must commit during a naturally selected sale. A discounted native Japan chemical or biological raid prepared during the sale contributes the equipment family only when a successful accepted release resolves, even after expiry. The outcome marker, native reservation, human-country eligibility, and sale sequence are checked without a synthetic purchase receipt. Failed or canceled raids do not credit a family. Existing family progress remains until the delayed outcome; ordinary post-expiry purchases remain ineligible.

Timed CBRN Protective Aid reserves its full physical respirator shipment and discounts only the voluntary Political Power service fee. Its payer-scoped receipt and saved sale sequence permit PP-family credit after a proven delivery, including completion after expiry; cancellation retains the spent fee but earns no family. The PP-only proof validates the settled Black Friday component and actual payment, and does not satisfy the achievement's separate non-political-payment requirement. The native two-factory commitment still lacks sale coverage, as recorded in the [aid contract](../plans/026_black_friday_plans/2026-10-03_cbrn_protective_aid_pp_adapter.md).

The five existing South Africa purchases use one owner bundle with eleven resource components, fresh cost text, preflight checks, actual-paid receipts, and outcome-gated settlement.
Their [owner contract and component ledger](../systems/africa_rsa_purchase_transactions.md) retain the original routes, targets, limits, cooldowns, and AI weights.
All five use Political Power as the primary achievement family, and their flags do not establish an institutional-law purchase.
Native execution, UI expansion, probability comparison, and save/reload evidence remain pending.

The [existing-owner caller migration](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_existing_owner_caller_integration.md) establishes consumed temporary output storage in 16 further source files.
Its 454 known-call inventory and 17 actual-fragment scenarios remain bounded source evidence.
The [Condemnation provider correction](../plans/026_black_friday_plans/2026-10-03_condemnation_provider_lifetime_fix.md) restores ordinary score-scaled prices before any future sale adapter, and does not discount ongoing inspection burden.
The source purchase registry remains incomplete.

## Validation record

The required offline source, wiki, vanilla documentation, asset, localisation, spreadsheet, event-inspection, and probability-inspection reviews are recorded under `docs/plans/026_black_friday_plans/`. The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; its Event 26 premise and evolution cells match the current game text, and it has no achievement field to update for this rule. Its existing CSV exports remain unchanged. The Event 26 row remains `Needs Testing` until live validation passes.

Part 8 acceptance status is recorded in `docs/plans/026_black_friday_plans/event26_part8_acceptance.md`. No HOI4 process was launched by the coding agent, and no live or multiplayer evidence is claimed.

## Future extension

Once the registry is closed, additional temporary cost sources can register through the same priority and family-mask contract without changing Event 26 lifecycle state. Further sale evolutions should add only registered ratios and corresponding preview, log, and acceptance rows.
