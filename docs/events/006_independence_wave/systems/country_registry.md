# Event 006 country registry API

The authoritative package ledger is [`006_candidate_country_registry.csv`](../../../specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv).
Every row is documented there by `package_id`, resolved/provisional tag, `baseline_anchor_state_names` (location), and `region_overlay`, together with tag policy, pool disposition, and reservation group.
This field guide defines the runtime API and the provenance rules around that ledger.

Current anchors, hosts, compact territory, and map-binding status live in [`006_current_installed_map_package_bindings.csv`](../../../plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv).
Tag reuse, intentional sharing, overlays, and collision decisions live in [`006_tag_collision_and_reuse_audit.md`](../../../specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md).

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
`common/collections/chaosx_country_collections.txt` use the
same country-group arrays. Collections are an active runtime view: a dormant
tag that is not currently instantiated contributes no country scope. Use the
static arrays (or the exact registry scripted triggers) for dormant reservation
and availability checks, and use collections for operations over countries
that currently exist. Neither view grants gameplay content by tag alone.

## Reusable `chaosx_country_*` API

The public cross-event API is in
`common/collections/chaosx_country_collections.txt`. The `chaosx_country_*`
prefix is a collection namespace, not a country tag: HOI4 country identifiers
are fixed three-character tokens and cannot be renamed to a long string such
as `chaosx_country`. The API therefore keeps the actual carrier tag stable and
gives every later event a discoverable collection name.

| API collection | Contents | Intended consumers |
| --- | --- | --- |
| `chaosx_country_all` | Every country declared by Chaos Redux | Fallout rebuilds, crisis release helpers, and generic carrier lookup |
| `chaosx_country_independence_wave` | All 191 resolved Event 006 carriers, including registered reuse | Any event that wants a researched independence identity |
| `chaosx_country_independence_wave_owned` | The 102 Event 006-owned X tags | New-country admission and dormant reservation checks |
| `chaosx_country_independence_wave_registered` | Registered vanilla carriers reused by the ledger | Overlay and existing-country content loaders |
| `chaosx_country_africa` | The four African Event 006 region arrays (45 carriers) | Event 012 and later African regional crises |
| `chaosx_country_africa_overlap` | The 12 Africa/Event 006 identity overlaps | Direct Africa package reuse decisions |
| `chaosx_country_soviet_collapse` | The 34 Event 005 successor carriers | Soviet Collapse follow-up systems and later Eurasian crises |
| `chaosx_country_region_*` | The 14 documented Event 006 regions | Regional overlays, patrons, and formable routing |

Use a collection as an active scope input, for example:

```txt
every_collection_element = {
	input = collection:chaosx_country_africa
	limit = { exists = yes }
	# Prove this event's package, origin, anchor, and content readiness here.
	# Load the event-specific overlay only after those checks pass.
}
```

The collection does not create a country, transfer ownership, or select an
Event 006 focus tree by itself. A caller records its own origin and applies
its own history, territory, forces, diplomacy, and focus overlay. Shared tags
such as CHU and BIA still require package-id and anchor resolution before any
content is loaded.

The current collision proof is generated by
`.tools/audit_chaosx_country_tags.py`. It scans vanilla, sibling local mods,
and Workshop `common/country_tags` definitions, ignores event/localisation
mentions, and explicitly excludes the Random Events Mod. The 28 July 2026
run protects 102 Event 006 tags plus 34 Soviet Collapse carriers and reports
zero external country-definition collisions. Its reviewed Soviet remap is
`ALA -> AAX`, `ALN -> ABX`, `BAC -> ADX`, `BSC -> AEX`, `KHW -> ANX`, `KRS -> AOX`, and
`KZR -> INX`; a companion extended-surface rescan also retired `OGB -> IJX`,
`RMC -> IKX`, `TSC -> ILX`, `APX -> INX`, and `MRC -> IMX`. All replacements are
X-suffixed and remain available to later API consumers.

A future event can take a regional active-country view with a normal
collection input, for example:

```txt
input = collection:chaosx_country_region_west_and_central_africa
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

`africa_priority_member_ensure_focus_tree_loaded` loads the Africa tree for a validated Event 012 package on a generic carrier or an approved Event 006 carrier only when the protected Event 006 origin and full Event 006 tree are absent.

An active `independence_wave_active_origin`, an active `independence_wave_focus_tree`, or a Soviet origin records `africa_priority_member_focus_tree_overlay_skipped` and leaves the meaningful tree untouched.

Event 012 ideas, decisions, forces, and AI still apply additively while the focus overlay is skipped.

The Event 006 end-of-origin and generation-reset helpers retry the overlay only after clearing the protected origin receipt; the existing DOX/SOK cleanup calls remain guarded while Event 006 owns its tree.

An approved Event 006 carrier with no active meaningful tree remains eligible for the Africa tree, while an unrecognised or missing tree on any other carrier is preserved rather than overwritten; this is intentional until a supported no-tree predicate is available.

The two wrappers in
`common/scripted_effects/006_independence_wave_country_registry_effects.txt`
only record/clear Event 006's existing origin markers. They create no tags,
event targets, advisors, or assets. Existing Event 006 setup event targets and
cleanup chain remain the owner of short-lived scope pointers and global target
cleanup.

## Country-history ownership

Every new Chaos Redux carrier may use a normal country-history filename in the
form `TAG - Country Name.txt`. Static setup that is native to that new country
in every origin may live in its history file. The current 85 registered new-tag
history files use their documented country names rather than the generic
`Event 006 Country Shell` suffix.

Existing vanilla and previously registered carriers keep their original
history files unchanged. Event 006, Event 012, and other creating events apply
their own setup additively after recording provenance. A shared carrier never
loads another event's history or package simply because it appears in a
regional registry group.

## Assets and future work

This registry adds no player-facing icons, portraits, flags, advisor assets, or
new country definitions. Existing package assets remain owned by their event
and package files. If a future package gains a visual identity, register the
sprite and localisation in that package's asset handoff rather than extending
this registry API.

Future work may bind the three dormant African overlap rows and expose a
supported no-tree check, but such work must update the CSV binding map and the
current-map-bound group together.
