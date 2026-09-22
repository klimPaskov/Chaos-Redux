# Event 026 Black Friday

## Status

Event 26 is the actorless global Black Friday sale and keeps `chaosx.nr26.1` as its canonical entry event.

The event is classified as Minor Fire-Once, remains disabled in the default event allowlist during implementation, and must not be re-enabled until the cost registry, audits, and live acceptance evidence are complete.

## Player-facing behavior

Black Friday becomes eligible at Gathering Storm and 200 Chaos.

When the event system selects it, the event is reserved globally and removed from further selection without recording history, firing pacing, or creating an event-log row.

The reservation waits for the first in-game Friday at or above 200 Chaos, and a Friday reservation may activate on that same day. The reservation records whether it came from natural selection so a delayed Friday activation preserves achievement eligibility across save/reload and transient dispatch cleanup.

Activation records exactly one minor fire, applies the normal minor pacing and one dynamic major gain, broadcasts one report event to every human player, and snapshots the sale rate for the day.

The baseline sale rate is 50 percent off, while Evolution I uses 75 percent off when the activation Chaos value is at least 600 and the evolution is enabled.

The snapshot does not change when Chaos changes later, and the sale expires on the next daily tick.

The entry event is hidden and actorless, while the report event supplies the player-facing title, premise, price-sheet text, and report art.

## Runtime lifecycle

`common/scripted_effects/026_black_friday_effects.txt` owns initialization, Friday calculation, reservation, activation, expiry, disable cancellation, terminal cleanup, history integration, human status markers, and the achievement ledger.

The lifecycle uses the existing bounded global event-system pulse in `common/on_actions/chaosx_on_actions_chaos_meter.txt` and does not introduce a new country-wide daily scan.

The existing country on-action only refreshes the active human player's marker and sale source so tag changes and joining players receive the current state without changing global lifecycle state.

The central Chaos change hook can activate an already-reserved Friday after a later Chaos increase without recalculating a timer or creating a second history row.

Disable cancellation clears a reservation without history, while terminal cleanup cancels a reservation or expires an active sale and removes only the Black Friday source state.

Manual launches retain the ordinary reservation and Friday rules, while Force Trigger Mode may bypass the 200-Chaos and Friday gates. Both settings paths preserve a running timer and disqualify the natural-sale achievement.

## Cost contract

The reusable framework lives in `common/scripted_effects/chaosx_universal_cost_effects.txt`, `common/scripted_triggers/chaosx_universal_cost_triggers.txt`, `common/script_constants/chaosx_universal_cost_constants.txt`, and `docs/systems/universal_cost_modifier.md`.

Owners provide the ordinary current payable value after their ordinary modifiers, select a registered source by family mask and priority, quote the discounted value with fixed-point ratios, round positive values upward to the registered quantum, and use the same quote for affordability, payment, display, and refund.

Zero remains zero, negative values remain unchanged, and every positive value retains at least one registered quantum.

The framework contains native resource payment and refund adapters for political power, command power, manpower, fuel, infantry equipment, support equipment, motorized equipment, trains, convoys, Army Experience, Navy Experience, Air Experience, Stability, and War Support, plus an owner-adapter contract for commitments and custom currencies.

The Event 26 country ideas provide native country-level factor modifiers for the verified national, law, personnel, officer, doctrine, conversion, embargo, license-equipment, refit, and trade-cost fields. Flat one-time fields for equipment upgrades, guarantees, license purchases, and other absolute engine costs are explicitly absent because the installed schema does not interpret them as relative discounts.

The installed schema exposes intelligence-operation fields as flat absolute values rather than relative factors, so operation payment remains an explicit engine-inaccessible registry row until an exact confirmation adapter or complete static variants exist.

The earlier 104-component adapter inventory is a historical source checkpoint covering Communist-spread, Fury, medical capacity, civilian shelter, Mengele, D'Rhondan, Random Faction, Africa Elephant, and retired Japan chemical and biological decision payments. The Japan attack decisions were replaced by native chemical and biological raids with engine-reserved equipment and native Command Power prices; the old Japan registry rows do not prove current shared-quote payment, receipt, refund, or achievement coverage. Other bounded adapters retain their individual source claims, subject to current owner review. The final registry must still close every other custom cost owner and every engine-inaccessible field listed in `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md` before the event can be enabled.

## Achievement

Japan's native campaign raids have sale-priced variants, but the engine reservation occurs before a multi-day preparation resolves. A Black Friday achievement credit at reservation time has no documented callback proof, so these raids are not counted as verified achievement transactions in this document. The removed Japan attack decisions and their former registry rows are historical evidence only.

`026_black_friday_five_departments` uses the shared transaction receipt and final registry family IDs.

It requires five distinct qualifying families in one natural human-controlled sale, including an institutional family, a material or commitment family, and a non-political-power family.

AI, free, refunded, repeated-family, manual, forced, and post-expiry transactions do not count.

## Assets and interface wiring

The report sprite is `GFX_report_event_026_black_friday` from `gfx/event_pictures/026_black_friday/black_friday_report.dds` and `interface/026_black_friday.gfx`.

The active and Evolution I ideas both use `GFX_idea_026_black_friday_sale` from `gfx/interface/ideas/026_black_friday/black_friday_sale.dds`; the sale ratio is carried by the idea definition rather than a second sprite.

The achievement uses `GFX_achievement_026_black_friday_five_departments`, `GFX_achievement_026_black_friday_five_departments_grey`, and `GFX_achievement_026_black_friday_five_departments_not_eligible`.

The complete source-to-runtime visual audit, including the exact Vanilla consumers, DDS checks, deterministic achievement-triplet repair record, and scope exclusions, is maintained in `docs/plans/026_black_friday_plans/event26_asset_audit.md`.

The shared event list and Event Details framework map ID 26 to the Black Friday name, premise, status line, source line, evolution preview, actorless history row, and debug selector mappings.

## CXT setup contract

`common/scripted_effects/026_black_friday_cxt_test_effects.txt` registers the modifier-free hidden carrier `chaosx_cxt_extension_event026_black_friday` through the dynamic extension contract.

The bounded startup and `on_daily_CXT` hooks initialize and synchronize the carrier for the existing test country without adding a world-wide scan.

## Required acceptance coverage

The Part 8 scenarios cover disabled state, below-threshold selection, reservation, Friday activation, same-day expiry, 50 percent and 75 percent snapshots, timer preservation, save and reload, tag changes, joining players, disable and re-enable, manual and forced launches, terminal cleanup, multiplayer history, and quote/payment/refund boundaries.

The cost registry is the completion gate for the remaining Part 8 purchase scenarios and must be updated after the final implementation commit.

## Future depth

After the universal registry is closed, the sale can be extended with additional source priorities for other time-limited economic events without changing the transaction contract.

Further evolution tiers should add only new registered ratios and preview/log text, while preserving the same snapshot, refund, and family-ledger rules.

The event can also expose a small audit view of the active source and receipt ledger if a future specification introduces a dedicated event-owned GUI.
