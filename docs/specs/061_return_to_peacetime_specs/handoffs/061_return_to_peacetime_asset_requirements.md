# Event 061 asset requirements

## Production rule

This is the asset inventory for Return to Peacetime.

Exact dimensions, alpha rules, final paths, and sprite definitions must follow inspected installed vanilla and current Chaos Redux consumer precedents.

The four report images use the `210x176` target when the local report-event precedent confirms it.

All visible art is static.

Final art must be processed through `chaos-redux-event-assets` with source preservation, manifest, PNG preview, DDS conversion, GFX handoff, and in-game crop validation.

## Style family

- grounded 1930s to 1940s industrial and administrative imagery
- anonymous global subjects
- clear small-size silhouettes
- painted strategy-game finish for event images
- coherent metal, paper, factory, rail, uniform, and civic-construction motifs
- no readable generated text
- no dominant national flag
- no named real person
- no modern equipment
- no fake interface controls inside category art

## Report and category art

| Asset ID | Working file slug | Consumer | Source mode | Visual direction |
| --- | --- | --- | --- | --- |
| `61_report_baseline` | `return_to_peacetime_report` | baseline national report | generated | arms factory being retooled toward civilian machinery, workers active, returning personnel secondary |
| `61_report_evo1` | `swords_into_ploughshares_report` | Evolution I warning or result | generated | depot sorting and dismantling rifles, vehicle parts, crates, and machine tools for reconstruction |
| `61_report_evo2` | `great_demobilization_report` | Evolution II warning or result | generated | railway or demobilization center with soldiers returning equipment and receiving papers |
| `61_report_evo3` | `permanent_peace_report` | Evolution III settlement or result | generated | closed arsenal and quiet barracks with civilian construction beyond, restrained vulnerability |
| `61_category_picture` | `return_to_rearmament_category_picture` | decision category | generated | factory divided by military tooling and civilian production, no fake controls |

## Category and normal rearmament icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_icon_category` | `return_to_rearmament_category` | category | gear divided between rifle silhouette and civilian tool |
| `61_icon_contracts` | `restart_arms_contracts` | decision | signed procurement folder, gear, and factory stamp without text |
| `61_icon_arsenal_state` | `reopen_state_arms_plants` | targeted state decision | factory doors opening around machine tooling |
| `61_icon_general_staff` | `reconstitute_general_staff` | decision | staff map, dividers, and officer cap |
| `61_icon_public_defence` | `make_case_for_defence` | decision | public rostrum, shield, and mobilization poster shape without text |
| `61_icon_economy_law` | `restore_mobilisation_law` | decision | factory gear moving upward through legal document bands |
| `61_icon_conscription` | `restore_conscription` | decision | service registry cards and uniform insignia |
| `61_icon_emergency_rearm` | `emergency_rearmament` | decision | alarm bell over rushed factory tooling |
| `61_icon_permanent_conversion` | `make_conversion_permanent` | decision | rifle line sealed behind a civilian gear |
| `61_icon_national_program` | `national_rearmament_program` | mission or decision | coordinated factory, staff, and law symbols in one structured seal |
| `61_icon_defence_ministry` | `reestablish_defence_ministry` | extreme-law recovery | government building with shield and planning papers |
| `61_icon_national_arsenal` | `reopen_national_arsenal` | extreme-law recovery | locked arsenal reopening around one machine tool |
| `61_icon_service_registry` | `restore_service_registry` | extreme-law recovery | registry book, identification cards, and simple service badge |
| `61_icon_emergency_defence` | `emergency_national_defence` | extreme-law recovery | shield raised in front of a dark border and hurried factory |

## Evolution I icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_icon_protect_army` | `protect_army_stores` | decision | protected rifle, shell, and supply crate |
| `61_icon_protect_mobile` | `protect_mobile_reserves` | decision | protected track, wheel, and armoured silhouette |
| `61_icon_protect_air` | `protect_air_reserves` | decision | protected aircraft silhouette inside depot roof |
| `61_icon_protect_logistics` | `protect_logistics_reserves` | decision | shield over locomotive and convoy bow |
| `61_icon_central_reconstruction` | `central_reconstruction` | disposition | recovered metal entering public construction gear |
| `61_icon_civilian_auctions` | `civilian_auctions` | disposition | auction hammer beside vehicle part and tool crate, no currency text |

## Evolution II icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_icon_cadres` | `retain_essential_cadres` | decision | small officer cadre around training manual |
| `61_icon_border_formations` | `mark_border_formations_essential` | targeted decision | guarded border post with division marker |
| `61_icon_accelerate_demob` | `accelerate_mustering_out` | decision | uniform and rifle handed toward civilian suitcase |

## Evolution III icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_icon_settlement` | `national_defence_settlement` | mission | scales balancing civic building and shield |
| `61_icon_voluntary_peace` | `voluntary_permanent_peace` | decision | open civic gates with a stored rifle behind them |
| `61_icon_extreme_recovery` | `extreme_law_recovery` | category phase or mission | broken shield being rebuilt beside one factory gear |

## Idea icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_idea_reconversion` | `industrial_reconversion_shock` | staged national spirit | factory line with mismatched military and civilian tooling |
| `61_idea_materials` | `reconstruction_materials` | timed national spirit | steel beams, machine tools, and construction crane hook |
| `61_idea_veterans` | `veteran_reintegration` | timed national spirit | uniform coat beside work clothes, gear, and railway ticket |
| `61_idea_dividend` | `peace_dividend` | law-linked national spirit | civic construction rising from a closed arsenal ledger |
| `61_idea_improvised` | `improvised_rearmament` | emergency aftermath | rushed assembly line, crooked gear, and warning lamp |

## Law icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_law_peacetime_economy` | `peacetime_economy` | economy law | large civilian gear covering a dormant military factory |
| `61_law_no_army` | `no_army` | conscription law | empty barracks gate with stored rifle crossed out by a legal seal, no text |

The law icons should share framing and lighting while remaining distinct.

## Achievement icons

| Asset ID | Working file slug | Consumer | Icon concept |
| --- | --- | --- | --- |
| `61_achievement_arsenal_reborn` | `achievement_arsenal_reborn` | achievement | closed arsenal doors forced open around a growing gear and rifle silhouette |
| `61_achievement_swords_ploughshares_swords` | `achievement_swords_ploughshares_swords` | achievement | plough blade reshaped into bayonet around a factory gear |
| `61_achievement_arsenal_sleeps` | `achievement_arsenal_sleeps` | achievement | padlocked arsenal beneath laurel, idle smokestacks, distant border marker |

## Consumer and path handoff fields

Each final asset row must record:

- asset ID
- source mode
- source file
- prompt or source URL
- rights and provenance when sourced
- reference folder and exact inspected consumer
- native source dimensions
- processed PNG dimensions
- alpha mode
- final PNG path
- final DDS path
- proposed sprite name
- target `.gfx` file
- target event, decision, idea, law, or achievement consumer
- review result at actual in-game size
- status and blocker

## Audit requirements

Reject any package with:

- missing asset rows
- one file duplicated under several unrelated names
- wrong consumer dimensions
- uncropped contact-sheet labels
- opaque squares behind transparent icons
- alpha halos
- clipped silhouettes
- modern machinery or clothing
- readable generated text
- category picture controls that do not work
- report images dominated by a real national flag
- inconsistent law icon framing
- achievement icons unreadable at actual size

## Minimum planned total

| Family | Count |
| --- | ---: |
| Report images | 4 |
| Category picture | 1 |
| Category icon | 1 |
| Normal rearmament and recovery icons | 13 |
| Evolution I icons | 6 |
| Evolution II icons | 3 |
| Evolution III icons | 3 |
| Idea icons | 5 |
| Law icons | 2 |
| Achievement icons | 3 |
| Total | 41 |

The final consumer audit can add assets. It should not silently remove distinct required concepts.
