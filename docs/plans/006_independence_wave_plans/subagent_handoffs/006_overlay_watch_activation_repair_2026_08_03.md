# Event 006 overlay watch activation repair

Date: 2026-08-03.

Scope: source-level repair for the IW-022 Dalmatia, IW-025 Vojvodina, and IW-035 Livonia overlay watch missions.

## Finding

Each overlay already defined a paid `start_*watch_mission` scripted effect and an `activation = { always = no }` mission block, but no decision called the start effect. The follow-on watch mission therefore could not set its running flag or activate, leaving the watch-completion gate ahead of the municipal or federal settlement decisions unreachable.

## Repair

Each overlay now has a visible, repeatable mobilisation decision after its preparatory coastal, mounted-reserve, or coastal-watch action:

- `independence_wave_iw022_mobilize_adriatic_watch`
- `independence_wave_iw025_mobilize_border_watch`
- `independence_wave_iw035_mobilize_livonian_watch`

The decisions require the existing anchor-control trigger and the existing command-power, manpower, infantry-equipment, and support-equipment guard-cost trigger. Their complete effects call the existing start effect, which pays the cost once, clears stale interruption state, marks the watch running, resets the hold ledger, and activates the corresponding mission. AI is disabled when no qualifying garrison is present and receives the existing peacetime multiplier. No free formations, state transfer, tag creation, or silent resource subtraction was added.

## Files

- `common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt`
- `common/decisions/006_independence_wave_iw025_vojvodina_decisions.txt`
- `common/decisions/006_independence_wave_iw035_livonia_decisions.txt`
- `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml`
- `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml`
- `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`

The existing scripted effects, triggers, constants, ideas, and mission definitions remain the owners of the costs, objective checks, lifecycle values, timeout, cancellation, and cleanup behavior.

Watch-success legitimacy is centralized per overlay so each existing two-branch settlement map remains reachable after the documented action chain: IW-022 uses `27` (`32 + 10 - 4 + 27 = 65`), IW-025 uses `34` (`28 + 8 - 5 + 34 = 65`), and IW-035 uses `32` (`30 + 8 - 5 + 32 = 65`). These are the minimum threshold-closing values and add no free reward or hidden action.

## Validation boundary

Static source inspection confirms each new decision's name, localisation keys, existing cost trigger, anchor trigger, complete-effect caller, and AI constants. The three localisation files retain UTF-8 with BOM. The source blocks were checked for balanced braces and no unsupported literal `<=` or `>=` operators. No Hearts of Iron IV process, live save, or runtime mission observation was performed.

The read-only `hoi4.probability_inspect` decision adapter also scanned the three updated decision files with validation passed, zero unresolved diagnostics, and five discovered weighted candidates in each pool. Artifact receipts are `probability-inspect-47bcb9351b23.json` (IW-022), `probability-inspect-86e1afb6388a.json` (IW-025), and `probability-inspect-47e74fbb8001.json` (IW-035). The pools remain incomplete for runtime evaluation because the required world-state inputs were not supplied.

This repair closes the source-level activation gap only. It does not promote any overlay to a complete Event 006 country package, prove route reachability in a live session, or alter the whole-event **HOLD / PARTIAL** disposition.
