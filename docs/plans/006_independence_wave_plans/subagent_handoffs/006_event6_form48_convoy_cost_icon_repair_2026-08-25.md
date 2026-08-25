# Event 006 FORM-48 convoy cost icon repair — 2026-08-25

## Scope

This bounded localisation repair corrects the four FORM-48 cost families that displayed a train icon beside a convoy amount even though their availability triggers and payment effects use convoys only.

## Changed keys

The following base and `_blocked` keys in `localisation/english/006_independence_wave_pacific_l_english.yml` now retain `£convoy_texticon` without `£GFX_train_texticon`:

- `independence_wave_form48_invitation_acceptance_cost`
- `independence_wave_form48_carrier_convoy_cost`
- `independence_wave_form48_carrier_procurement_cost`
- `independence_wave_form48_member_convoy_cost`

The matching `_tooltip` keys continue to alias the base strings. No amount, constant, trigger, payment helper, timer, AI weight, decision ID, category ID, or package gate changed.

## Preservation evidence

The FORM-48 trigger scan confirms the four cost triggers check convoy stockpiles for their transport input; the corresponding payment helpers subtract convoy stockpiles and retain their existing command-power, fuel, equipment, and civilian-factory inputs where applicable. No train branch is present in those trigger or payment paths.

The eight edited keys retain their pre-existing values after removing only the unrelated train-icon token. The localisation file retains its UTF-8 BOM and has no duplicate keys. Static `git diff --check` passed.

## Boundary

This is a player-facing localisation correction only. It does not claim live tooltip rendering, decision-engine inspection, or in-game validation. The broader Event 006 decision surface remains HOLD/PARTIAL for the gaps recorded in `006_event6_decision_mission_current_audit_2026-08-25.md`.
