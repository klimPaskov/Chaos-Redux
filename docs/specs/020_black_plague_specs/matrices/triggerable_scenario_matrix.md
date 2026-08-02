# Black Plague Triggerable Scenario Matrix

The live implementation uses `SCN-012` and the two-tag correction below is authoritative.

> Runtime reconciliation, 2026-08-02: the historical repeat-blocked rows are superseded for live behavior. A repeat SCN-012 signal is an idempotent reconciliation-only path that preserves existing disease ledgers, actors, intensity, and history while rebuilding counts, shared threat, board, and mapmode; terminal or otherwise unavailable worlds still fail closed. The current intensity postcondition also reconciles live RTA/RTX division counters before top-up and verifies both selected floors before marking launch success. A failed postcondition clears temporary reservations and remains retryable; it does not claim atomic inverse rollback of every prior mutation.

## Scenario registry row

| Field | Planned value |
| --- | --- |
| Scenario ID | `SCN-012` |
| Working name | Black Plague Unbound |
| Type | fixed profile, Instant Plague Kingdoms |
| Intensity control | Low, Medium, High, Maximum |
| Direct launch | yes, except impossible setup or active world end |
| Forced event state | Event 20 plus Evolutions I through IV |
| Immediate actors | one reusable `RTA` Rat Nation carrier with internal brood basins and one separate `RTX` Rat King |
| World end | not launched |
| Repeat launch | reconciliation-only after success; terminal or unavailable worlds remain blocked |
| Achievement handling | permanent scenario shortcut disqualifier |

## Intensity targets

| Intensity | Eligible continents targeted | Established plague states | Internal `RTA` brood coverage | Rat King states | Chaos floor | Rat opening strength |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Low | 3 | 12 to 18 | 1 `RTA` carrier with several internal broods | 1 to 2 | 400 | young but viable broods and royal core |
| Medium | 4 | 24 to 36 | 1 `RTA` carrier with several internal broods | 2 to 4 | 600 | established regional rat armies |
| High | 5 or all when fewer exist | 45 to 65 | 1 `RTA` carrier with many internal broods | 4 to 6 | 800 | strong multi-front rat war |
| Maximum | every eligible inhabited continent | 75 to 110 | 1 `RTA` carrier with capped internal broods | 7 to 10 | 999 | near-world-collapse armies under performance caps |

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
| 1 | scenario state | bootstrap and permanent launched flag set | successful repeat signals enter reconciliation-only mode; terminal gate blocks |
| 2 | Event 20 | registered and marked fired | reuse existing event history |
| 3 | continents and states | distributed anchor basins selected | existing infected states count toward target |
| 4 | disease values | status and seven Black Plague state values initialized | one registry entry per state |
| 5 | Evolution I | stronger strain active and logged | skip record when already present |
| 6 | Evolution II | overseas spread active and logged | skip record when already present |
| 7 | Rat Nation carrier | missing internal broods and state markers created inside `RTA` | existing valid `RTA` brood markers count toward target; live division counters reconcile before top-up; no new rat tag |
| 8 | Evolution III | logged with first brood actor | one row only |
| 9 | Rat King | separate Royal Basin and country created | preserve existing King when present; reconcile the selected RTX division floor before postcondition success |
| 10 | Evolution IV | logged with Rat King actor | one row only |
| 11 | global systems | Chaos floor, world threat, pulses, Deaths, air cleanliness | shared helpers, one opening death pass, and one saved scheduler anchor that queues the first `.900` callback |
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
| Strike the Royal Node | earned military strike after Evolution IV; success delays a royal pulse, while counterfire raises Dominion, Hunger, and terminal preparation |
| Strike the Crown | earned Royal Basin assault after sufficient successful node strikes; route-specific consequences apply and the operation never cures the plague |
| Seal Royal Burrows | post-defeat state operation against former Royal Nodes or the Royal Basin; lowers infestation and raises containment over 180 days with fixed material and command costs |

Royal King Hunger crises are country events rather than ordinary disease phases. The Absolute Crown, Council of Burrows, and Black-Breath Hierophancy each expose a distinct crisis choice and feed their route policy consumers.

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
| Event 20 already active | existing progress retained, unestablished candidates added without reseeding established states, missing actors added, no duplicate history |
| Rat Nation already active | existing `RTA` brood markers count toward target, no duplicated tag or units |
| Rat King already active | existing King retained, no duplicate Evolution IV row |
| small or altered map | targets scale down after minimum validity, no invalid state or capital |
| mapmode | every established Black Plague state is black immediately after launch |
| decisions | Black Plague-specific rows appear in shared category, no dedicated category exists |
| repeat launch | reconciliation-only idempotent path with clear terminal/unavailable reason when blocked |
| save and reload | scenario state, actors, mapmode, decisions, and pulses remain valid |
