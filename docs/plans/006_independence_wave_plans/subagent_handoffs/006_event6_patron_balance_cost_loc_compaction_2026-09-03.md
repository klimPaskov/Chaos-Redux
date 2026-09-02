# Event 006 Patron Balance cost localisation compaction

## Result and ownership

The player-facing Patron Balance cost text was compacted in `localisation/english/006_independence_wave_decisions_l_english.yml`.
No decision triggers, payment effects, constants, visibility gates, scripted localisation, GUI files, or spreadsheet files were changed.
The edit is limited to the normal and blocked variants of `independence_wave_cost_patron_balance`; the existing tooltip alias remains unchanged.
No files were staged or committed by the localisation pass.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or updated.

## Changed keys

`independence_wave_cost_patron_balance` now reads:

`Every use: [diplomatic standard command power] · [diplomatic standard transport]`

`After the first: + [administration light command power] · [administration light manpower]`

`independence_wave_cost_patron_balance_blocked` carries the same two-row structure with the existing red blocked palette.
The dynamic transport selector and all constant tokens were preserved.

## Semantic alignment

`independence_wave_balance_patrons` always pays `independence_wave_decision_pay_diplomatic_standard`.
When `independence_wave_patron_balance_count` is above the minimum, completion additionally pays `independence_wave_decision_pay_administration_light`, which consumes the light command-power and manpower amounts shown on the second row.
The compact wording therefore removes the duplicated standard row while still identifying the recurring standard payment and the later staged surcharge.
The decision's current affordability predicates and payment effects were not altered.

## Validation and remaining scope

The edited localisation file retains its UTF-8 BOM and the tooltip alias resolves to the compact normal string.
Run the focused Event 006 allocator and GUI matrix validators after the parent integrates this isolated localisation change.
This handoff does not claim live HOI4 popup rendering, save/load, or full localisation review for all Event 006 keys.
