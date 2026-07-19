# Event 006 country registry API

The authoritative package ledger is
[`006_candidate_country_registry.csv`](../specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv).
Every row is documented there by `package_id`, resolved/provisional tag,
`baseline_anchor_state_names` (location), and `region_overlay`, together with
tag policy, pool disposition, and reservation group. This field guide defines
the runtime API and the provenance rules around that ledger.

Current anchors, hosts, compact territory, and map-binding status live in
[`006_current_installed_map_package_bindings.csv`](../plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv).
Tag reuse, intentional sharing, overlays, and collision decisions live in
[`006_tag_collision_and_reuse_audit.md`](../specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md).

## Registry shape

- 206 package rows.
- 102 rows reserve a new Event 006 X tag.
- 91 rows reuse a registered tag; CHU is intentionally shared by IW-043 and
  IW-046, and BIA is intentionally shared by IW-096 and IW-107.
- 13 rows are overlays with no `resolved_tag`; they are never selectable
  carriers. The 193 tagged rows resolve to 191 unique tags.
- The static country-group category is
  `independence_wave_country_groups` in
  `common/script_constants/006_independence_wave_country_registry_constants.txt`.
  It exposes `all_resolved_carrier_tags`, `event6_owned_new_tags`,
  `registered_reuse_tags`, 14 region arrays, and the Africa overlap arrays.

Region arrays (the counts below are unique resolved tags, so overlay rows are
excluded) are:

| Region key | CSV region | Tags |
| --- | --- | ---: |
| `northern_and_western_europe` | Northern and Western Europe | 11 |
| `mediterranean_and_iberia` | Mediterranean and Iberia | 9 |
| `balkans_and_danube` | Balkans and Danube | 9 |
| `eastern_europe_and_former_imperial_russia` | Eastern Europe and western former imperial Russia | 9 |
| `volga_urals_siberia_far_east` | Volga, Urals, Siberia, and Far East | 14 |
| `caucasus_anatolia_mesopotamia` | Caucasus, Anatolia, and Mesopotamia | 14 |
| `levant_and_arabia` | Levant and Arabia | 10 |
| `north_africa_and_sahara` | North Africa and Sahara | 9 |
| `west_and_central_africa` | West and Central Africa | 11 |
| `east_africa_horn_great_lakes` | East Africa, Horn, and Great Lakes | 13 |
| `southern_africa_and_indian_ocean` | Southern Africa and Indian Ocean | 12 |
| `south_asia_and_himalaya` | South Asia and Himalaya | 17 |
| `southeast_asia_east_asia_oceania` | Southeast Asia, East Asia, and Oceania | 29 |
| `americas_and_caribbean` | Americas and Caribbean | 24 |

## Static groups versus collections

The named collections in
`common/collections/006_independence_wave_country_collections.txt` use the
same country-group arrays. Collections are an active runtime view: a dormant
tag that is not currently instantiated contributes no country scope. Use the
static arrays (or the exact registry scripted triggers) for dormant reservation
and availability checks, and use collections for operations over countries
that currently exist. Neither view grants gameplay content by tag alone.

A future event can take a regional active-country view with a normal
collection input, for example:

```txt
input = constant:independence_wave_country_groups.west_and_central_africa
```

When it needs a dormant carrier, it must select the documented package row,
reserve that exact tag and its states, prove the tag is not living or reserved,
then record its own origin before loading its own content. It must not call an
Event 006 setup, focus, AI, decision, or formable dispatcher merely because the
carrier appears in an Independence Wave group.

Africa exposes three overlap views:

- `africa_overlap_tags`: all 12 compatible registry-carrier overlaps,
  including COG's overlay-only IW-101 identity and the MAD carrier shared by
  the Event 006 Madagascar restoration and Event 012 Merina package.
- `africa_overlap_non_overlay_tags`: the 11 non-overlay carriers, including
  dormant/unbound DYX (IW-103), DZX (IW-104), and EMX (IW-117).
- `africa_overlap_current_map_bound_tags`: the eight carriers with legal
  current-map bindings (DOX, DSX, SOK, DUX, UGA, HAR, EQX, MAD). This group
  proves map feasibility only; each package still needs its own content-
  readiness gate before Event 006 may select it.

## Event 012 identity boundaries

Event 012 compatible carrier reuse is explicit and canonical:

| Africa package | Carrier | Event 006 row | Notes |
| --- | --- | --- | --- |
| Asante | DOX | IW-093 | direct overlap |
| Oyo | DSX | IW-097 | direct overlap |
| Sokoto | SOK | IW-098 | registered reuse |
| Kanem-Bornu | DUX | IW-099 | direct overlap |
| Kongo | COG | IW-101 | overlay-only; not an Event 006 selectable carrier |
| Luba | DYX | IW-103 | dormant/unbound overlap |
| Lunda | DZX | IW-104 | dormant/unbound overlap |
| Buganda | UGA | IW-108 | registered reuse |
| Harar | HAR | IW-113 | registered reuse |
| Kilwa | EMX | IW-117 | dormant/unbound overlap |
| Zulu | EQX | IW-121 | direct overlap |
| Merina | MAD | IW-130 | registered reuse |

Manden (MLI), Aksum (TIG), Nubia (SUD), and Great Zimbabwe (ZIM) remain on
their existing vanilla carriers. They have no compatible Event 006 identity
row; the registry deliberately does not mislabel them as overlaps or reject
them. TIG remains an Event 006 carrier for Tigray, but Event 012's Aksum
package is a separate identity and therefore requires Event 012 provenance.

`CHU` and `BIA` are shared carriers, not duplicate tag definitions. Package
dispatch must resolve the package ID and anchor/location row before loading any
content; never infer package identity from the tag alone.

## Provenance and loading contract

`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`
provides exact membership, Event 006 origin, Soviet origin, and safe Africa
origin predicates. Event 006 content continues to require its own package and
origin markers. Event 012 writes only `africa_priority_origin_*` and Africa
package flags; it never calls the Event 006 origin effect.

`africa_priority_member_ensure_focus_tree_loaded` now loads the Africa tree only
for a validated Event 012 package whose current tree is `generic_focus`. An
existing meaningful tree is preserved and the package runs additively (ideas,
decisions, forces, and AI remain available). Event 006 and Soviet origins are
fail-closed before any focus-tree operation. A carrier with an unrecognised or
missing focus tree is preserved rather than overwritten; this is intentional
until a supported no-tree predicate is available.

The two wrappers in
`common/scripted_effects/006_independence_wave_country_registry_effects.txt`
only record/clear Event 006's existing origin markers. They create no tags,
event targets, advisors, or assets. Existing Event 006 setup event targets and
cleanup chain remain the owner of short-lived scope pointers and global target
cleanup.

## Assets and future work

This registry adds no player-facing icons, portraits, flags, advisor assets, or
new country definitions. Existing package assets remain owned by their event
and package files. If a future package gains a visual identity, register the
sprite and localisation in that package's asset handoff rather than extending
this registry API.

Future work may bind the three dormant African overlap rows and expose a
supported no-tree check, but such work must update the CSV binding map and the
current-map-bound group together.
