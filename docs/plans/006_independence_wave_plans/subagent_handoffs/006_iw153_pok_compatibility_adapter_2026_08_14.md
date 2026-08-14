# IW-153 POK compatibility adapter handoff

## Disposition

Implemented a bounded, package-local, source-backed compatibility boundary for IW-153. IW-153 remains a `specific_community_variant_only` and unbound package. The adapter is dormant unless a living registered `POK` carrier has the active Event 006 origin, exact package id `iw_153`, and a future named-community selection marker.

No central adapter, content attestation, preflight, Join, dispatcher, event, decision, focus, force, asset, localization, country-history, or vanilla-file entry was added or changed. No tag, Dayak identity, leader, flag art, route, or generic current-map selection was invented.

## Files changed

| File | Identifiers | Scope and side effects |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt` | `is_independence_wave_iw_153_pok_compatibility_context`; `has_independence_wave_iw_153_pok_character_surface`; `has_independence_wave_iw_153_pok_core_surface`; `has_independence_wave_iw_153_pok_releasable_surface`; `has_independence_wave_iw_153_pok_compatibility_contract` | Country-scope, read-only predicates. Every predicate inherits `original_tag = POK`, active Event 006 origin, `independence_wave_package_id = iw_153`, and `independence_wave_iw_153_named_community_selected`. The strict contract additionally checks the vanilla character, both POK core states, Indonesia’s releasable array, and capital state 334. |
| `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt` | `independence_wave_iw_153_pok_compatibility_clear_named_selection`; `independence_wave_cleanup_iw_153_pok_compatibility` | Country-scope cleanup wrappers. They only clear the future selection marker and only after the complete context gate passes. They do not set the marker or alter any vanilla surface. |

## Vanilla preservation evidence and invariants

- `common/country_tags/00_countries.txt` registers `POK` as `countries/Pontianak.txt`; no replacement country definition or tag alias was added.
- `history/countries/POK - Pontianak.txt` keeps capital state `334` and `recruit_character = INS_syarif_muhammad_alkadrie`; the strict contract reads the character and capital without changing either.
- `history/states/334-Kalimantan Barat.txt` and `history/states/1022 - Interior Borneo.txt` both contain `add_core_of = POK`; the strict contract reads both cores and contains no core effect.
- `history/countries/INS - Indonesia.txt` contains `add_to_array = { INS_releasables = POK }`; the strict contract reads `INS_releasables` from `INS` and never adds, removes, or rewrites array members.
- `common/scripted_effects/INS_scripted_effects.txt` owns vanilla `indonesia_transfer_POK`. The adapter never calls, overrides, or duplicates it, and it never uses `set_nationality`, `remove_country_leader_role`, or another character-transfer effect.
- The adapter contains no history writer, `add_core_of`, `remove_core_of`, `recruit_character`, `set_nationality`, `add_to_array`, `remove_from_array`, tag, cosmetic identity, flag asset, or route effect.
- Cleanup only clears `independence_wave_iw_153_named_community_selected`, which is a reserved future selector marker. It never clears the Event 006 origin or package id, and it is inert when any required gate is missing.

## Future call-site and identity boundary

The future named-community owner must set `independence_wave_iw_153_named_community_selected` only after selecting a precise Dayak polity or river-region federation and supplying defensible identity, territory, institutional leader, and symbol sources. This adapter does not choose or name that community, does not make state 334 an automatic binding, and does not provide a generic Dayak route. The package remains unavailable to automatic selection while the accepted row is unbound.

If a future route invokes `indonesia_transfer_POK`, it must invoke the untouched vanilla effect in its existing context. The strict character predicate is a pre-transfer source witness; after vanilla transfer changes the character nationality/role, callers must not treat the adapter as permission to reimplement or reverse that behavior.

## Validation

- Read-only source validation completed against the offline Paradox wiki pages for data structures, triggers, effects, modifiers, localization, scopes, on actions, event/decision/idea/AI modding, and country creation.
- Read-only vanilla documentation consulted for script constants, effects, triggers, `is_core_of`, `has_character`, `is_in_array`, origin flags, and event-target/array behavior.
- Source evidence rechecked in the installed vanilla POK country history, state 334 and state 1022 files, Indonesia history, `INS.txt`, and `INS_scripted_effects.txt`.
- Static syntax hygiene run on the two new script files: balanced braces, tab indentation for script blocks, no unsupported `<=` or `>=`, and no unary variable negation. The new effect file contains no dynamic or weighted logic.
- No HOI4 MCP event/focus/map/GUI/probability inspection was run because these files add no linked event, focus, map, GUI, or weighted surface and no central call site was requested. No live game or save/load claim is made.

## Blockers and follow-up

The named Dayak community/institution, exact territory/host-remnant contract, period-valid male leader, and attested symbol/flag remain unresolved research gates. Runtime integration, central admission, force/idea/focus/decision/localization/assets, and live validation remain intentionally out of scope and must not be inferred from these dormant helpers. Any future implementation must preserve the vanilla POK/Indonesia surfaces listed above and obtain parent approval before adding callers or central entries.
