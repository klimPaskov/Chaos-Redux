# Event 006 country API and regional carrier map

This document is the implementation-facing reference for reusing Independence Wave carriers in later events. The accepted registry remains `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`; the runtime collections and constants below are the stable lookup surfaces. The documented X-tag to identity mapping is kept in `common/country_tags/006_independence_wave_countries.txt`, while registered-carrier rows remain keyed by the CSV's exact package ID and resolved tag.

## Runtime collections

Use the named collections in `common/collections/chaosx_country_collections.txt` when a later event needs a country scope. These collections are active views over the declared static arrays, so a dormant reservation is absent until the tag exists in the current game.

| Collection | Contents | Intended consumer |
| --- | --- | --- |
| `collection:chaosx_country_independence_wave` | Every resolved Event 006 carrier, including registered vanilla-tag reuse and Event 006-owned `X` tags | Generic Event 006-aware systems that still apply origin and readiness gates |
| `collection:chaosx_country_independence_wave_owned` | The 102 Event 006-owned `X` tags | New-country release, tag collision, and custom-history consumers |
| `collection:chaosx_country_independence_wave_registered` | Registered vanilla carriers reused by Event 006 | Additive overlays that must preserve vanilla history and identity |
| `collection:chaosx_country_independence_wave_selectable_bound` | Current-map-bound selectable carrier tags | Automatic and scenario candidate views after package readiness is checked |
| `collection:chaosx_country_independence_wave_selectable_unbound` | Selectable rows without a current-map binding | Scenario or later researched-release work; never silently substitute a nearby anchor |
| `collection:chaosx_country_independence_wave_overlay_routes` | All thirteen route-only overlay carriers | Living-country overlays; these rows are never standalone release candidates |
| `collection:chaosx_country_africa` | Africa-priority carrier pool | Event 012 and later Africa crisis consumers |
| `collection:chaosx_country_africa_overlap` | The twelve direct Event 006/Event 012 identity overlaps, including overlay-only COG | Africa identity selection before its own origin gate is applied |
| `collection:chaosx_country_africa_overlap_non_overlay` | African overlaps that can be country packages rather than route-only overlays | Africa package selection after the overlay exclusion is proven |
| `collection:chaosx_country_africa_current_map_bound` | African overlap carriers with a current-map anchor | Africa release planning after map and readiness checks |
| `collection:chaosx_country_soviet_collapse` | Soviet Collapse carriers | Event 005-only consumers; never infer Event 006 content from membership |

Region collections are exposed as `collection:chaosx_country_region_*` in the same file. The fourteen region arrays are `northern_and_western_europe`, `mediterranean_and_iberia`, `balkans_and_danube`, `eastern_europe_and_former_imperial_russia`, `volga_urals_siberia_far_east`, `caucasus_anatolia_mesopotamia`, `levant_and_arabia`, `north_africa_and_sahara`, `west_and_central_africa`, `east_africa_horn_great_lakes`, `southern_africa_and_indian_ocean`, `south_asia_and_himalaya`, `southeast_asia_east_asia_oceania`, and `americas_and_caribbean`.

## Tag provenance and country identity

The registry has 206 package rows: 102 Event 006-owned `X` tags, 91 rows that intentionally reuse registered vanilla tags, and 13 overlay-only rows with no standalone country tag. The 91 reuse rows resolve to 89 unique carriers because CHU and BIA each serve two mutually exclusive package identities. Use the exact package ID and reservation group when a carrier is shared; a tag alone never selects content.

Every new Event 006 country, formable, and cosmetic tag ends in `X`. Reused carriers retain their vanilla history, flag, meaningful focus tree, and real identity. A later event may add its own origin-gated package to a reused carrier only after it proves that the current country is not living under a protected origin, does not own a meaningful incompatible tree, and has a unique anchor and reservation receipt.

The inert reservations in `common/countries/006_independence_wave_unresearched_reservations.txt` are parser-safe declarations only. They intentionally have no history or country localisation and must remain outside every content-ready gate until the accepted research dossier names the community, territory, symbol, leader path, and public identity.

## Origin and focus dispatch

Collection membership is not permission to mutate a country. Event 006 consumers require `is_independence_wave_registry_event6_origin = yes` or the exact Event 006 package gate. Soviet Collapse consumers require `is_independence_wave_registry_soviet_origin = yes`. Africa consumers require `is_independence_wave_registry_africa_origin = yes`, which explicitly rejects both live Event 006 and Soviet origins.

Focus content follows the creating event. Every admitted Event 006-owned tag uses the one generic `independence_wave_focus_tree` only after the frozen release transaction and package attestation. Registered carriers keep their meaningful vanilla tree and receive a reviewed additive overlay using the same generic Event 006 route/effect contract. The common final validator is fail-closed when a package has neither the generic tree nor a registered owning-tree carrier; do not set an overlay flag and assume the engine will inject a shared focus by itself. See [generic focus tree](systems/generic_focus_tree.md) for the lane and assignment matrix.

For Africa, call `africa_priority_member_register_from_origin` after the Africa package has recorded its own origin and exact package ID. `africa_priority_member_ensure_focus_tree_loaded` then loads `africa_priority_member_focus_tree` only when the carrier is on its generic or Event 006-owned safe path. If Event 006 or Soviet Collapse still owns the active origin or a meaningful focus tree, the loader records `africa_priority_member_focus_tree_overlay_skipped` and preserves the existing surface. This is the intended handoff for Asante (`DOX`), Oyo (`DSX`), Sokoto (`SOK`), Kanem-Bornu (`DUX`), Kongo (`COG` cosmetic overlay), Luba (`DYX`), Lunda (`DZX`), Buganda (`UGA`), Harar (`HAR`), Kilwa (`EMX`), Zulu (`EQX`), and Merina (`MAD`).

The Africa priority-member identity helper also consumes the intersection of `collection:chaosx_country_independence_wave_owned` and `collection:chaosx_country_africa_overlap_non_overlay`. This keeps the public API live for Event 006-owned African carriers without broadening the focus loader to registered vanilla carriers. Origin, package, map, and meaningful-tree gates remain mandatory; collection membership never grants admission or permits a tree overwrite.

## Safe reuse sequence

1. Resolve the desired identity through the registry CSV and the appropriate `chaosx_country_*` collection.
2. Check the exact origin predicate and package ID; never select by `original_tag` alone when a carrier is shared.
3. Reserve the country tag, reservation group, unique anchor, and one surviving host state before any territory transfer.
4. Apply the later event's package only after its own history, territory, symbols, leaders, forces, ideas, AI, focus or overlay contract, and cleanup proof pass.
5. Preserve a living carrier's existing history and meaningful tree; use the reviewed additive adapter or leave the package fail-closed.
6. Clear the later event's origin, ledgers, decisions, ideas, and focus flags through its own cleanup effect without clearing another event's origin markers.

The allocator and collision audits remain authoritative for availability. A collection is a lookup surface, not a readiness shortcut, and no later event should create a second tag when one of these carriers is the accepted identity.
