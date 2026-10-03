# Event 35 cost contract repair

## Disposition and acceptance basis

Implemented source repair within the user's Event 35 goal, which explicitly requires dynamic costs, a four-type cost cap, tooltips, and cleanup.
Native render and executed gameplay validation remain unverified.

## Changes

`localisation/english/035_great_depression_l_english.yml` has 22 shortened inline normal/blocked rows across eleven cost families, plus all seventeen `great_depression_cost_*_tooltip` keys with complete dynamic quoted amounts.
The eleven shortened families are emergency relief, center protection, center reopen, center restructure, public works, strategic rescue, finance/trade, state planning, contagion, social response, and global reconstruction.
Every fourth value remains in the matching hover tooltip.
Civilian-capacity tooltips identify the capacity as committed rather than destroyed or permanently spent.
The nine War Support occurrences in center abandonment, austerity, and market clearing now use the installed `GFX_war_support_icon` sprite.

`common/scripted_localisation/035_great_depression_cost_localisation.txt` supplies nine resource-specific quote selectors shared by all 51 normal, blocked, and tooltip rows.
Each selector checks that its quote exists and applies the same inclusive resource predicate used by the corresponding cost-family affordability checks.
Each resource is colored independently, with the eighteen `great_depression_quote_*_available` and `great_depression_quote_*_blocked` keys keeping texticons, values, and formatting in YAML.
The selectors are `GetGreatDepressionCostPoliticalPower`, `GetGreatDepressionCostManpower`, `GetGreatDepressionCostFuel`, `GetGreatDepressionCostTrains`, `GetGreatDepressionCostConvoys`, `GetGreatDepressionCostSupportEquipment`, `GetGreatDepressionCostCivilian`, `GetGreatDepressionCostStability`, and `GetGreatDepressionCostWarSupport`.
Stability and War Support percentages use two decimal places to retain fractional quotes.

`common/scripted_effects/035_great_depression_effects.txt` adds the omitted Public Works family to the civilian-capacity payment branch in `great_depression_pay_action_cost`.
The payment branch freezes `great_depression_cost_civilian` into the hidden `great_depression_committed_civilian` snapshot, and `great_depression_clear_dynamic_state` clears that snapshot after removing both commitment modifiers.

`common/dynamic_modifiers/035_great_depression_dynamic_modifiers.txt` makes both existing civilian-commitment variants read the frozen snapshot.
The former one/two-factory tiers contradicted quotes that can round to zero or three under the configured 0.35 to 2.50 cost-factor range.
The existing remove-before-add behavior still prevents modifier stacking.

`docs/events/035_great_depression.md` documents the compact display, complete hover quote, frozen commitment, and cleanup.

No AI weight, target weighting, probability modifier, or cooldown was edited.

## Task-specific source review

Public Works now has four payment components in the dispatcher, matching manpower, fuel, trains, and civilian capacity in its affordability predicate.
The commitment branch captures the quote before installing its modifier, and both variants read only that captured value rather than the subsequently refreshed quote.
All seventeen cost tooltips retain their mapped one to four quote values, and no inline normal or blocked cost row exceeds three values.
All nine resource-icon tokens used in these cost strings resolve to installed vanilla or Chaos Redux sprite definitions.
All 51 cost rows resolve their quote selectors, and all eighteen selector output keys exist.
These are source checks, not observed engine transactions.

## References

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 285 to 340, explains custom cost keys, `_blocked` and `_tooltip` lookup, manual payment, and the fixed AI hint.
Its SHA-256 is `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
Installed `common/decisions/_documentation.md`, lines 1 to 30, defines visibility and availability evaluation, with SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.
Installed `common/decisions/AUS.txt`, lines 982 to 996, supplies a custom-cost precedent, with SHA-256 `619F5E7D922C7900C2CFE31B54DC37D32B7583DEDAE9F33336A430D753362EF0`.
Offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`, lines 112 to 173, defines variable-backed dynamic modifiers and scope behavior, with SHA-256 `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F`.
Installed `documentation/effects_documentation.md`, lines 1153 to 1173, defines `add_dynamic_modifier`, with revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed `documentation/modifiers_documentation.md`, lines 2202 to 2205, defines integer `civilian_factory_use`, with SHA-256 `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E`.
Installed `interface/topbar.gfx`, lines 256 to 259, defines the War Support sprite, and `interface/texticons.gfx` plus mod `interface/chaosx_texticons.gfx` define the other resource icons.
Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 655 to 696, defines current-scope scripted localisation and first-matching-text selection.
Its SHA-256 is `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`.
Installed `common/scripted_localisation/00_scripted_localisation.txt`, lines 1 to 36, supplies the documented selector schema and a vanilla fallback precedent.
Its SHA-256 is `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587`.

## Route failures and remaining gaps

The connected reference-context and reference-search routes returned cited sources, but the relevant reference-read calls lost their handles without final results, so the pertinent sections were read locally.
The October isolated decision/mission auditor `01a10016-3f6e-7081-bf33-07870de20f0d` terminated with `workspace routing discovery timed out` before returning an audit.
The bounded map lookup for states 1 and 64 and the focused event trace lost their handles without final artifacts.
The current native decision inspection requires explicit scenarios, and its declared insufficient-PP fixture has not produced a retrievable final result.
No live-game result or native decision-row render is claimed.
Mixed affordability colors are implemented in source through the nine resource quote selectors, but native rendering of the mixed state remains unverified.
The missing ordinary availability predicates were subsequently repaired and committed as `37c6b472a9cb44c54fcea9214309fdf87facf00d`.
All 89 paid entries share their affordability predicate between availability and custom-cost display.
The native same-scenario comparison remains unresolved after domain timeouts.
This source repair does not close the full Event 35 goal.
