# Event 006 FORM-05 convoy-only cost icon repair

## Scope

This tranche corrects the FORM-05 decision cost disclosures in `localisation/english/006_independence_wave_form05_l_english.yml`. It removes the unrelated `£GFX_train_texticon` token from the nine convoy-backed cost families and their nine blocked variants. No decision, trigger, effect, constant, icon definition, package gate, or admission rule changed.

## Source crosswalk

Every affected decision explicitly requires the FORM-05 convoy-capacity trigger in both `available` and `custom_cost_trigger` before it can start. The light delegation rows use `has_independence_wave_form05_light_convoy_capacity`; the standard shipping, opening, customs, proclamation, reopening, shipping-board, customs-clearinghouse, and first-board-reconvening rows use `has_independence_wave_form05_standard_convoy_capacity` directly or through their FORM-05 payment trigger. The shared payment effect retains its train fallback for other Event 006 callers, but that branch is unreachable for these FORM-05 decisions by design.

The repaired base keys are `independence_wave_form05_delegation_cost`, `independence_wave_form05_shipping_cost`, `independence_wave_form05_opening_cost`, `independence_wave_form05_customs_cost`, `independence_wave_form05_proclamation_cost`, `independence_wave_form05_reopening_cost`, `independence_wave_form05_shipping_board_cost`, `independence_wave_form05_customs_clearinghouse_cost`, and `independence_wave_form05_first_board_reconvening_cost`. Their matching `_blocked` keys were repaired in the same pass. Defense, capital, coastal-warning, and first-board-ratification costs do not use convoy transport and were left unchanged.

## Validation

- The localisation file retains its UTF-8 BOM.
- The eighteen repaired strings retain their existing command-power, manpower, stability, convoy, and civilian-factory values; only the train icon was removed.
- `£GFX_train_texticon` no longer occurs in the FORM-05 cost localisation.
- The Event 006 allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 static validators were rerun after the edit.

## Remaining scope

This closes only the FORM-05 transport-icon mismatch. Shared transport selectors and other package-owned cost strings remain separate follow-up surfaces; this repair does not change their dynamic payment behavior or the whole-event HOLD / PARTIAL status.
