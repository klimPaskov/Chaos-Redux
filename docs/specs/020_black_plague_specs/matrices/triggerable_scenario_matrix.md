# Black Plague Triggerable Scenario Matrix

All names are working labels. Final IDs and sort values must be checked against the live scenario registry.

## Scenario registry row

| Field | Planned value |
| --- | --- |
| Scenario ID | `SCN-012` |
| Working name | Black Plague Unbound |
| Type | fixed profile, Instant Plague Kingdoms |
| Intensity control | Low, Medium, High, Maximum |
| Direct launch | yes, except impossible setup or active world end |
| Forced event state | Event 20 plus Evolutions I through IV |
| Immediate actors | several Rat Nations and one separate Rat King |
| World end | not launched |
| Repeat launch | blocked after success |
| Achievement handling | permanent scenario shortcut disqualifier |

## Intensity targets

| Intensity | Eligible continents targeted | Established plague states | Independent Rat Nations | Rat King states | Chaos floor | Rat opening strength |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Low | 3 | 12 to 18 | 2 to 3 | 1 to 2 | 400 | young but viable broods and royal core |
| Medium | 4 | 24 to 36 | 4 to 6 | 2 to 4 | 600 | established regional rat armies |
| High | 5 or all when fewer exist | 45 to 65 | 7 to 10 | 4 to 6 | 800 | strong multi-front rat war |
| Maximum | every eligible inhabited continent | 75 to 110 | 10 to 16, tag capped | 7 to 10 | 999 | near-world-collapse armies under performance caps |

## Seed-state mix

| State role | Low | Medium | High | Maximum |
| --- | --- | --- | --- | --- |
| Anchor | Severe Crisis, rare Collapsed | Severe or Collapsed | Collapsed favored in rat basins | Collapsed favored in rat and royal basins |
| Inner ring | mostly Infected | Infected and Severe | Severe weighted | Severe and Collapsed weighted |
| Outer ring | Threatened and known Incubating | Threatened and Incubating | broad threatened transport ring | broad global transport and port ring |
| Rat Infestation | high in rat basins | high in rat basins and selected cities | high in many cities, ports, and depots | widespread in infected transport and urban states |
| Opening deaths | small bounded pass | moderate severe-state pass | substantial collapsed-state pass | severe but nonterminal pass |

## Bootstrap sequence matrix

| Order | System | Required result | Duplicate protection |
| ---: | --- | --- | --- |
| 1 | scenario state | bootstrap and permanent launched flag set | launch gate blocks prior success |
| 2 | Event 20 | registered and marked fired | reuse existing event history |
| 3 | continents and states | distributed anchor basins selected | existing infected states count toward target |
| 4 | disease values | status and seven Black Plague state values initialized | one registry entry per state |
| 5 | Evolution I | stronger strain active and logged | skip record when already present |
| 6 | Evolution II | overseas spread active and logged | skip record when already present |
| 7 | Rat Nations | missing independent broods created | existing valid broods count toward target |
| 8 | Evolution III | logged with first brood actor | one row only |
| 9 | Rat King | separate Royal Basin and country created | preserve existing King when present |
| 10 | Evolution IV | logged with Rat King actor | one row only |
| 11 | global systems | Chaos floor, world threat, pulses, Deaths, air cleanliness | shared helpers and one opening death pass |
| 12 | UI | disease board and full mapmode rebuild | one batch refresh after setup |
| 13 | cleanup | temporary arrays, reservations, bypasses cleared | permanent scenario flag retained |

## Black Plague-specific decisions initialized by scenario

These appear as separate decision entries inside the general disease category.

| Decision family | Immediate scenario use |
| --- | --- |
| Clean the City of Rats | reduces urban Rat Infestation, spread, mortality, and rat-emergence pressure |
| Seal Granaries, Markets, and Warehouses | slows infestation growth and transport contamination at economic cost |
| Clear Sewers and Burrow Shafts | reduces infestation, burrow strength, and resurgence risk |
| Flea, Shelter, and Bedding Control | reduces mortality and local transmission while consuming medical and civilian capacity |
| Purge Vermin from Rail Yards and Docks | reduces rail, port, and Evolution II spread at throughput cost |
| Demolish Infested Blocks | emergency overreaction that sharply lowers local infestation but causes displacement and heavy economic damage |
| Purge the Warrens after Liberation | removes rat-control remnants from retaken states and prevents resurgence |

## Mapmode contract

| State condition | Shared contamination-map appearance |
| --- | --- |
| Threatened only | existing amber warning colour |
| Known Incubating | charcoal to authorized viewer, becoming black when established display threshold is reached |
| Infected | black base fill with infected outline or icon |
| Severe Crisis | black base fill with stronger severe outline or pattern |
| Collapsed | black base fill with broken crisis edge |
| Contained | black base fill with blue containment outline |
| Recovery | black base fill with green recovery outline |
| Rat-Controlled | black base fill with rat-control accent |
| Weaponized provenance | black base fill with weaponized border or symbol |
| Cured | black fill removed after cleanup, monitored status shown separately |

## Validation matrix

| Case | Required result |
| --- | --- |
| Low launch on ordinary map | three continents, two or more broods, one King, no world end |
| Maximum launch | every eligible continent, capped actors and units, Chaos no higher than 999 from bootstrap |
| Event 20 already active | existing progress retained, missing states and actors added, no duplicate history |
| Rat Nations already active | existing broods count toward target, no duplicated tags or units |
| Rat King already active | existing King retained, no duplicate Evolution IV row |
| small or altered map | targets scale down after minimum validity, no invalid state or capital |
| mapmode | every established Black Plague state is black immediately after launch |
| decisions | Black Plague-specific rows appear in shared category, no dedicated category exists |
| repeat launch | launch disabled with clear reason |
| save and reload | scenario state, actors, mapmode, decisions, and pulses remain valid |
