# Event 006 IW-022 — Dalmatia vanilla-route overlay adapter

## Status

`PARTIAL` — bounded source implementation is present, but the adapter is not admitted as a complete Event 006 country package or as proof that the full route-overlay matrix is complete.

## Source contract

IW-022 observes the vanilla Yugoslav route that creates a dynamic country from `CRO`, assigns the cosmetic carrier `dalmatia`, and transfers the Dalmatian anchor state in `common/national_focus/yugoslavia.txt` (the `create_dynamic_country` block around lines 817–825). The implementation does not register a tag, create history, transfer a state, change autonomy, overwrite the vanilla Yugoslav focus tree, or create a flag, portrait, or advisor asset. Vanilla dynamic-country carriers are constrained to the `D01`–`D50` range, so the adapter uses those narrow daily hooks and an exact identity trigger instead of a world iteration.

## Files added

- `common/script_constants/006_independence_wave_iw022_dalmatia_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt`
- `common/ideas/006_independence_wave_iw022_dalmatia_ideas.txt`
- `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt` (the shared D01-D50 table also invokes the IW-025 Vojvodina refresh, avoiding duplicate on-action keys)
- `common/decisions/categories/006_independence_wave_iw022_dalmatia_categories.txt`
- `common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt`
- `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml`

## Implemented surface

The exact CRO-origin carrier receives three visible values — Port Coordination, Coastal Security, and Municipal Legitimacy — with centralized caps, gains, losses, and AI weights. Five actions spend concrete command power, manpower, trains, infantry equipment, support equipment, and army experience: port ledgers, Adriatic coastwatch, an expiring garrison/watch mission, a municipal charter, and a coastal security compact. Four lifecycle ideas expose contested administration, port authority, municipal charter, and coastal security states. Territorial checks cover the vanilla Dalmatian anchor and the optional Adriatic access state. The watch mission has explicit availability, timeout, cancellation, failure, completion, AI, and objective effects. The adapter records a narrow overlay-active flag plus the anchor/package profile for future shared systems.

## Preservation and safety

The route is additive and only activates while `is_dynamic_country = yes`, `original_tag = CRO`, and `has_cosmetic_tag = dalmatia` are all true. On route loss it removes its ideas, clears its values and mission flags, and pauses the watch state. No country creation, state assignment, autonomy rewrite, free-unit loop, or unconditional Event 006 focus-tree load is performed.

## Validation evidence

- New script blocks and localisation were checked for balanced braces/quotes; the localisation file is UTF-8 with BOM.
- The touched scripts contain no unsupported literal `<=` or `>=` operators.
- `hoi4.probability_inspect` read the decision source with the `decision_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED` with validation passed, four discovered weighted candidates, and no unresolved source diagnostics. The same read with `mission_ai_will_do` found one weighted mission candidate with no unresolved source diagnostics. Both pools are not complete for runtime evaluation because the required scenario inputs were not supplied.
- No HOI4 process was launched. No live save/load, runtime, AI, or scenario evidence is claimed.

## Remaining acceptance work

This bounded adapter does not yet provide a safe way to insert the shared Event 006 focus framework into a meaningful living YUG tree. Network, patron, league, formable, host-survival, save/load cleanup, and live carrier evidence remain open. The overall route-overlay acceptance item therefore remains unchecked; eleven other exact vanilla route-overlay adapters are still absent, and the Event 006 completion audit remains `HOLD/PARTIAL`.

## 2026-08-03 source continuation

The previously orphaned paid `independence_wave_iw022_dalmatia_start_watch_mission` effect now has the explicit `independence_wave_iw022_mobilize_adriatic_watch` decision caller with anchor and material-cost gates, matching the existing overlay mission pattern. The watch-success legitimacy writer now uses the centralized `watch_legitimacy_gain = 27`, which closes the municipal and coastal-security settlement threshold after the documented ledger and coastwatch chain (`32 + 10 - 4 + 27 = 65`). This does not promote the overlay to a complete Event 006 package and does not resolve the existing route-loss pause, focus, network, league, formable, source, or runtime boundaries.
