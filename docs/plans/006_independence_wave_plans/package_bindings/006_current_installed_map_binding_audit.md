# Event 006 current-installed-map binding audit

## Status and authority

This is the authoritative planning audit for binding all 206 accepted Event 006 package rows to the currently installed Hearts of Iron IV map. The later vanilla-identity reconciliation separates 193 selectable release packages from 13 non-selectable route overlays; it does not erase the geographic evidence recorded here.

The machine-readable source of truth for each package is:

- `006_current_installed_map_package_bindings.csv` — one row for every package from `IW-001` through `IW-206`;
- `006_current_map_state_collisions.csv` — every state claimed by more than one bound package;
- `006_current_map_reservation_groups.csv` — all 111 accepted reservation groups, their bound and unbound members, current state claims, and cross-group collisions.

No fallback or generic binding was used. A package is unbound where the installed map does not provide the exact accepted geography, the accepted research requires a more specific community or institution, or the public-baseline state points at a broad or stale current state.

## Installed map snapshot

The audit used the locally installed build on 2026-07-14:

| Evidence | Result |
| --- | --- |
| Vanilla state history | 1,081 state files in `history/states/` |
| State ID range | 1 through 1081 |
| State names | `localisation/english/state_names_l_english.yml` |
| Installed executable timestamp | 2026-07-07 11:43:13 UTC |
| Chaos Redux state overrides | `history/states/` exists but contains zero files |
| Chaos Redux root map override | none |
| `replace_path` for `history/states` or `map` | none |

Initial owner and capital annotations come from the installed vanilla state and country histories. They are static 1936 evidence only. The release planner must recalculate ownership, capital protection, and host remnants at runtime.

## Required references consulted

The offline wiki snapshot was used, not the live Paradox wiki. The core pages were re-read together with the map-specific pages:

- Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions;
- Event modding, Decision modding, Idea modding, AI modding;
- Map modding, State modding, Country creation.

The installed official documentation was checked for the release and state-transfer behavior:

- `documentation/effects_documentation.md`: `release`, `release_autonomy`, `transfer_state`, `set_state_owner`, `set_state_controller`, `add_state_core`, `remove_state_core`;
- `documentation/triggers_documentation.md`: `owns_state`, `controls_state`, `is_core_of`, `country_exists`, `has_full_control_of_state`.

Vanilla precedents included `common/decisions/BALTIC.txt` for scoped `release` and `common/decisions/CHL.txt` for scoped `transfer_state` followed by state-core handling.

The Event 006 candidate registry, package research resolution, sensitive-package restrictions, tag audit, state-anchor registry, core specification, and host-survival rules were read together. The installed map and the accepted names/requirements take precedence over the public 763-state numeric baseline.

## Result summary

| Result | Count |
| --- | ---: |
| Packages audited | 206 |
| Geographically bound rows in the original map audit | 149 |
| Geographically unbound rows in the original map audit | 57 |
| Selectable bound release packages | 138 |
| Selectable unbound release packages | 55 |
| Non-selectable vanilla route overlays | 13 |
| Distinct installed states referenced | 205 |
| `ready_automatic` | 8 |
| `ready_if_tag_not_living` | 44 |
| `ready_unique_state_confirmed` | 51 |
| `ready_high_chaos` | 23 |
| `route_only_bound` | 7 |
| `scenario_only_bound` | 1 |
| `specific_variant_only_bound` | 4 |
| Automatic or high-chaos packages disabled for no unique current state | 27 |
| Specific-community packages left unbound | 26 |
| Scenario packages left unbound | 2 |
| `overlay_nonselectable` | 13 |
| Reservation groups | 111 |
| State collision rows | 14 |
| Cross-group automatic blockers | 1 |
| Cross-group route exclusions required | 1 |

## Binding semantics

- `fixed_anchor_compact`: `anchor_state_ids` is mandatory. `compact_state_ids` is the normal defensible package. `extended_state_ids` is optional and must be trimmed first.
- `choose_one_ordered`: listed IDs are ordered alternatives, not a cumulative grant.
- `choose_one_host_safe`: test each listed alternative independently and use only a state that passes capital and remnant protection.
- `choose_one_host_branch`: select one branch-compatible state; never grant both cross-border alternatives automatically.
- `unbound`: the package has no authoritative current-map state and is not selectable.
- `overlay_carrier_route`: the row documents territory associated with an exact vanilla route or carrier. It is not a release candidate and reserves no country or state in the Event 6 allocator.

Every anchor is contained in its compact set. No compact state is duplicated in an extended set. Extended territory is never an entitlement.

## Direct old-to-current rebindings

These 26 packages no longer use their public-baseline anchor:

| Package | Public baseline | Current anchor | Current compact |
| --- | --- | --- | --- |
| IW-047 Mari El | 256 | 833 | 833 |
| IW-055 Nenets state | 579 | 825 | 825 |
| IW-060 Kurdistan | 421 | 1001 | 1001 |
| IW-064 Circassia | 234 | 827 | 827 |
| IW-065 Chechnya | 232 | 821 | 821 |
| IW-078 Oman Imamate | 294 | 1015 | 1015 |
| IW-089 Darfur | 549 | 767 | 767\|887 |
| IW-095 Dahomey | 556 | 776 | 776 |
| IW-098 Sokoto | 558 | 902 | 902 |
| IW-099 Kanem-Bornu | 558 | 901 | 901 |
| IW-100 Hausa Federation | 558 | 902 | 902 |
| IW-101 Kongo | 538 | 295 | 295 |
| IW-106 Aro Confederacy | 558 | 900 | 900 |
| IW-107 Biafran regional state | 558 | 900 | 900 |
| IW-114 Afar state | 268 | 908 | 908 |
| IW-135 Sikh state | 440 | 986 | 986 |
| IW-150 Aceh | 672 | 1050 | 1050 |
| IW-151 Minangkabau | 672 | 1048 | 1048 |
| IW-152 Riau | 672 | 1049 | 1049 |
| IW-155 Bali | 667 | 1052 | 1052 |
| IW-159 Shan federation | 640 | 999 | 999\|993 |
| IW-161 Mon state | 288 | 994 | 994 |
| IW-162 Kachin state | 640 | 998 | 998 |
| IW-164 Arakan or Rakhine | 288 | 997 | 997 |
| IW-167 Champa restoration | 671 | 286 | 286 |
| IW-204 Araucania and Patagonia restoration | 512\|507 | 950 | 950 |

Twenty-two packages with no public-baseline ID receive an exact current-map binding:

`IW-011=337`, `IW-031=802`, `IW-054=569`, `IW-066=232`, `IW-067=354`, `IW-068=354`, `IW-069=345`, `IW-076=659`, `IW-083=290`, `IW-091=775`, `IW-110=768`, `IW-111=769`, `IW-113=835`, `IW-119=842`, `IW-121=719`, `IW-126=981`, `IW-142=982`, `IW-143=982`, `IW-147=990`, `IW-148=985`, `IW-158=724`, and `IW-197=950`.

Important current split expansions are recorded exactly in the CSV. They include Scotland, Flanders/Antwerp, the Basque package, the Danube borderlands, Karelia, Hejaz, Cyrenaica and Tripolitania, Punjab, Balochistan, Pashtunistan, Kashmir, Lan Xang, Hawaii, Samoa, Quebec, and Newfoundland.

Notable stale baseline findings include:

- state 123 is South-West England, not a unique Cornwall state;
- the Basque anchor is current state 792 País Vasco, not baseline Navarra 172;
- state 232 is current Dagestan, while Chechnya-Ingushetia is 821;
- the dedicated Kurdistan anchor is 1001 rather than broad Ilam 421;
- state 556 is Bamako, while Dahomey is 776;
- the Baloch map is split among 444, 988, and 1012; baseline 445 is Sibi;
- Sumatra and Burma now have dedicated regional splits;
- Quebec's populated compact is anchored on 468 and the 860–863 splits, with 466 only optional;
- current state 496 is Minas Gerais, so the public-baseline Amazonian “Pará” entry cannot be reused.

## Packages disabled for no unique current state

These 27 automatic or high-chaos candidates are excluded from selection:

`IW-003 Cornwall`; `IW-032 Slavonia`; `IW-049 Mordovia`; `IW-061 Luristan`; `IW-063 Bakhtiari`; `IW-075 Jabal Shammar`; `IW-084 Kabylia`; `IW-087 Fezzan`; `IW-090 Wadai`; `IW-094 Fante`; `IW-096 Benin Kingdom`; `IW-103 Luba`; `IW-104 Lunda`; `IW-109 Bunyoro`; `IW-112 Ankole`; `IW-117 Kilwa restoration`; `IW-122 Ndebele`; `IW-123 Xhosa`; `IW-124 Basotho`; `IW-125 Eswatini`; `IW-165 Wa state`; `IW-176 Tonga`; `IW-181 Acadia`; `IW-186 Cherokee state`; `IW-188 Lakota state`; `IW-189 Dine state`; `IW-194 Miskito state`.

`IW-102 Kuba` and `IW-105 Loango` retain their no-unique-state geographic findings, but they are no longer selectable candidates: they are additive `COG` cosmetic-route overlays. The complete overlay set is `IW-005`, `IW-022`, `IW-025`, `IW-035`, `IW-059`, `IW-085`, `IW-101`, `IW-102`, `IW-105`, `IW-156`, `IW-196`, `IW-197`, and `IW-204`.

These 26 specific-community packages remain deliberately unbound until their accepted named community, district, institution, or member package exists:

`IW-056`, `IW-079`, `IW-080`, `IW-088`, `IW-092`, `IW-118`, `IW-120`, `IW-127`, `IW-128`, `IW-129`, `IW-146`, `IW-153`, `IW-157`, `IW-160`, `IW-163`, `IW-168`, `IW-174`, `IW-178`, `IW-187`, `IW-190`, `IW-191`, `IW-195`, `IW-199`, `IW-202`, `IW-205`, `IW-206`.

The two unbound scenario packages are `IW-077 Mahra` and `IW-116 Zanzibar`.

Four restricted packages have exact geography but remain non-automatic: `IW-055 Nenets state` on 825, `IW-091 Toubou state` on 775, `IW-172 Ainu state` on 536, and `IW-193 Zapotec-Mixtec Oaxaca federation` on 476. The binding does not relax their accepted institution, community, or negotiated-compact restrictions.

## Reservation and state collisions

All same-group overlaps are valid only under the accepted maximum-one reservation rule:

| State | Packages | Resolution |
| --- | --- | --- |
| 42 Moselland | IW-008 Rhineland / IW-010 Saar | same group; Rhineland extension trims before Saar anchor |
| 249 Kazan | IW-043 Volga Bulgaria / IW-044 Tatarstan | same group; choose at most one |
| 256 Chuvashia | IW-043 Volga Bulgaria / IW-046 Chuvashia | same group; choose at most one |
| 425 Mysore | IW-141 Mysore / IW-144 Dravidian federation | route cannot bypass the group |
| 427 Hyderabad | IW-140 Hyderabad / IW-144 Dravidian federation | route cannot bypass the group |
| 432 Assam | IW-145 Assam / IW-149 Himalayan confederation | route cannot bypass the group |
| 764 West Banat | IW-024 Banat / IW-025 Vojvodina | both are extensions; trim before anchors |
| 900 Benue | IW-106 Aro / IW-107 Biafran regional state | choose at most one |
| 902 Sokoto | IW-098 Sokoto / IW-100 Hausa Federation | route cannot bypass the group |
| 950 Araucanía | IW-197 Mapuche / IW-204 restoration | choose at most one |
| 982 Madras States | IW-142 Travancore / IW-143 Tamil state | choose at most one |
| 986 East Punjab | IW-134 Punjab / IW-135 Sikh state | choose at most one |

Two overlaps cross accepted reservation-group boundaries. Their runtime resolutions are implemented without changing the accepted groups:

1. **State 354 Trabzon.** `IW-067 Lazistan` uses `RG-LAZISTAN`; `IW-068 Pontus` uses `RG-PONTUS`. The Region 06 readiness layer applies an explicit state-354 mutex in addition to the shared per-state reservation check.
2. **State 441 Kashmir.** `IW-139 Kashmir` is in `RG-NORTHWEST-SOUTH-ASIA`; route-only `IW-149 Himalayan confederation` is in `RG-NORTHEAST-HIMALAYA`. Both readiness triggers use the shared per-state reservation check, so an explicit route caller cannot reserve the already committed Kashmir state.

## Host-survival and protected-capital findings

The CSV records initial owner, owner capital, and a package-specific implication for every bound state. The following packages touch a 1936 protected capital or present a 1936 erasure risk:

| Package | Initial finding | Required behavior |
| --- | --- | --- |
| IW-005 Flanders | BEL capital is state 6 | skip while capital protection applies |
| IW-012 Icelandic emergency republic | ICE capital and sole state is 100 | inactive while ICE lives; reject any later sole-state host |
| IW-059 Mesopotamia | IRQ capital is 291 | skip while capital protection applies |
| IW-074 Najd | SAU capital is 292 | route-only; do not take protected capital |
| IW-081 Lebanon | LEB capital and sole state is 553 | inactive while LEB lives; reject a sole-state host |
| IW-082 Palestine | PAL capital and sole state is 454 | inactive while PAL lives; reject a sole-state host |
| IW-114 Afar state | AFA capital and sole state is 908 | reject while the current host would disappear |
| IW-169 East Turkestan | SIK capital is 617 | skip while capital protection applies |
| IW-198 Aymara state | BOL capital is 302 | skip while capital protection applies |
| IW-200 Guarani state | PAR capital is 301; alternative 688 is initially safe | evaluate alternatives independently; prefer 688 in the installed start |
| IW-201 Muisca restoration | COL capital is 306 | skip while capital protection applies |

This is not a static allow-list. At selection time:

1. reserve the host's protected state before package selection;
2. reject a protected capital when a safe package or safe alternative exists;
3. require every affected owner to retain at least one owned state;
4. trim extended territory, then compact territory, before losing the anchor;
5. reject the package if the anchor itself would destroy the host.

## Optional map-tool result

The optional HOI4 map inspection tool was attempted. It returned `MAP_MODEL_BUDGET_BLOCKED`: 500,208 domain records exceeded its 500,000-record ceiling. This is not treated as evidence and did not trigger a fallback binding. The audit instead uses the authoritative installed state histories, state-name localisation, country histories, registered tag cores, and verified victory-point locations.

## Validation and implementation gates

The final artifacts independently confirm:

- exactly 206 unique package IDs with no gaps;
- 149 geographically bound and 57 geographically unbound rows in the original map audit;
- 138 selectable bound packages, 55 selectable unbound packages, and 13 non-selectable overlays after vanilla-identity reconciliation;
- 205 distinct referenced current states, all present in the installed state history;
- every bound anchor is in its compact set and no compact/extended overlap exists;
- all 111 reservation groups cover all 206 packages exactly once;
- 14 collision rows recomputed exactly from the package CSV;
- no empty readiness verdict or binding reason.

The Trabzon mutex and Kashmir per-state route exclusion are implemented. The 55 selectable unbound packages must remain unavailable until an accepted spec change or a future installed-map state supplies exact geography. The 13 overlays activate only through their vanilla carriers and never enter this allocator. Do not substitute a nearby broad state.
