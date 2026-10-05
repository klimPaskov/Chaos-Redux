# Mechanics guide refresh handoff, 2026-10-03

## Scope and result

`CHAOS_REDUX_MECHANICS.md` was reconciled with the current game files, `docs/systems/`, and the export CSVs under `docs/spreadsheets/`.
Only `CHAOS_REDUX_MECHANICS.md` and this handoff were edited.
Nothing was committed.
The guide was last committed on 2026-09-06 and had 855 lines; it now has about 1,016 lines.
Disposition of this refresh: implemented in the guide, validated by source reading only.
No in-game validation was performed, and the user performs live-game validation.

Source priority applied: game files under `common/`, `events/`, `interface/`, and `localisation/english/`, then `docs/systems/`, then the export CSVs.
Where a `docs/systems/` page contradicted current game files, the game files won and the page is listed under unresolved items below.

## Corrections to existing claims

Line numbers in the guide refer to the file after this refresh.

| # | Claim | Old text | New text | Source evidence |
| --- | --- | --- | --- | --- |
| 1 | Harder Crises for Players is a setting | Misc settings: "choose whether Harder Crises for Players is enabled" and "enabled by default" | The guide now says player countries face harder crises and that no setting switches this off (guide lines 61-62; the Miscellaneous section no longer mentions it) | `common/scripted_effects/chaosx_settings_effects.txt:3721-3730` sets the flag unconditionally; no GUI control exists in `interface/chaosx.gui` or `localisation/english/chaosx_gui_l_english.yml`; commit `c180c6ed4` "Remove harder player crises setting" (2026-06-04) |
| 2 | Air Winter stage names | "Clear, Dimming, Crop Shock, Hard Freeze, Black Harvest, Ash Winter, Terminal Winter" | Seven stages Open Sky, Dim Frost, Failed Season, Infrastructure Winter, Black Winter, Dead Sky, Fallout Night; state conditions named Dim Frost, Crop Shock, Hard Freeze, Black Harvest, Ash Winter, Terminal Winter | `localisation/english/chaosx_map_modes_l_english.yml:95-101`, `localisation/english/fallout_consolidated_l_english.yml:157-169`, `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:354-379`, `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt:20-120` |
| 3 | Air Cleanliness sources | "Chemical contamination, disease outbreaks, nuclear fallout, wildfire smoke, and volcanic ash" | Adds asteroid dust and acid rain | `common/script_constants/chaos_meter_constants.txt:667-679` (`air_contamination_source`) |
| 4 | Migration border policies | "open humanitarian reception and controlled entry to transit-only access, quarantine, or border closure"; "forced return" | Humanitarian Entry, Controlled Entry, Transit Only, Controlled Medical Entry, Closed Border, Violent Enforcement, Forced Return | `localisation/english/migration_l_english.yml:12-19` |
| 5 | Event list filters and sorting | "filter ... by enabled state, event type, or minimum Chaos tier"; sort by "number, occurrence count, or likelihood" | Filter by enabled state or event type; sort by event number, times fired, weight, or required Chaos level | `localisation/english/chaosx_gui_l_english.yml:530-550` |
| 6 | Autonomous robot manpower | "50 manpower per battalion" | "They need no human manpower." Width 2, 50 robots, 10 support equipment unchanged | `common/units/016_brilliant_scientist_project_forces.txt:51` (`ROBOT_MANPOWER = 0`), `:165-181`; width macro `:64`, equipment macros `:59`, `:63` |
| 7 | Camps window name and tabs | "Repression and Camps System" with Summary, Territories, Sites, Authority, Records | **Camp Administration** window with Administration, Locations, Records tabs, opened by Open Administration | `localisation/english/camp_administration_ui_l_english.yml:2-9`, `interface/camp_repression_ledger.gui:11-21`, `common/scripted_guis/camp_repression_ledger_scripted_gui.txt:3-14`; the old tab names in `localisation/english/camp_repression_ui_l_english.yml:7-12` have no consumer in `interface/` or `common/` |
| 8 | Camps starting networks | "Some countries begin with established repression networks" | Germany, Japan, and the Soviet Union begin with low-intensity networks | `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md` Overview (docs only; not independently confirmed in script) |
| 9 | Chaos Warfare establishment | "100 Army Experience", "90-day establishment mission", required 500 gas masks, 50 decontamination, 100 support equipment, deployed HQ Section and Detachment, failure leaves offensive options closed | Adoption costs 100 Army Experience and establishes command immediately; no mission, deadline, or equipment requirement | `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt:1-12` and `:40`, `common/script_constants/cbrn_doctrine_constants.txt:55-60`; no establishment decision exists in `common/decisions/cbrn_doctrine_decisions.txt` (only 4 decisions: cleanup and 3 policies) |
| 10 | Chemical Readiness | "measures how prepared the national program is, from 0 to 100. Training alone cannot replace equipment..." | Plain-language operational status in Program Management; hidden 0-100 readiness derived from masks, kits, filters, training | `localisation/english/cbrn_simplification_l_english.yml` (status keys), `common/script_constants/cbrn_doctrine_constants.txt:110-120` (`cbrn_readiness_status`) |
| 11 | Institutional milestones | Four milestones described as proofs involving a completed protective headquarters order and weapons stocks | Milestones are recognized automatically from mastery levels and protection research | `common/scripted_triggers/cbrn_doctrine_triggers.txt:281-305` |
| 12 | Use policies | Five (Defensive Preparation, Retaliation Authority, Limited Battlefield Authority, Strategic Release Authority, Unrestricted Chaos Warfare) with 90-day reassessment | Three: Retaliation Only, Battlefield Authorization, Unrestricted Authorization; 5 Command Power and 90-day reassessment each | `common/decisions/cbrn_doctrine_decisions.txt:60-131`, `common/script_constants/cbrn_doctrine_constants.txt:94-97,178`, `localisation/english/cbrn_simplification_l_english.yml` |
| 13 | Mastery tracks | "Hazard Assault Training" temporary program; "some specialist equipment requires a separate commission" | Rewards are granted automatically; no training or commission order | `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md` (Doctrine-only technologies); no such decision in `common/decisions/cbrn_doctrine_decisions.txt` |
| 14 | Officer corps | Unnamed "controlled retaliation, broader contamination, extreme offensive power"; "Chemical Operations Commanders help prepare HQ orders more quickly" | Names the three army postures, three division postures, academy, earned commander trait, and three High Command offices | `localisation/english/cbrn_doctrine_l_english.yml`, `localisation/english/chaosx_ideas_l_english.yml:203-217`, `docs/systems/cbrn_warfare/cbrn_commander_progression.md` |
| 15 | Army headquarters | "Six specialist headquarters companies" with protective posture, decontamination corridor, medical response, infection cordon | Three HQ sections and five orders with preparation and duration (1-3/28, 3-7/28, 2-7/30, 1/14, 2-5/60 days); force bands 100 and 200 battalions | `common/units/cbrn_hq_support.txt:52,115,174`, `localisation/english/cbrn_hq_l_english.yml:2-36` |
| 16 | Protection programs | "National programs build reserves, issue military masks, distribute civilian protection, replace filters" as player decisions | Issue, filters, and civilian distribution run in an automatic cycle about every 30 days; decisions are the Program Management and Civil Defence cards | `common/decisions/cbrn_protection_decisions.txt:35-490`, `docs/systems/cbrn_warfare/cbrn_simplification.md` (maintenance cycle paragraphs) |
| 17 | Decontamination | "assignments cost masks, decontamination equipment, support supplies, transport, fuel, and political and command resources" | 4 Command Power, 40 decontamination equipment, 300 fuel; masks, support equipment, trucks held in stock; one national assignment per 28 days | `common/script_constants/cbrn_doctrine_constants.txt:81-104`, `localisation/english/cbrn_doctrine_l_english.yml:30-31`, `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md` (28 days) |
| 18 | Chemical raids | "Chemical air and rocket raids"; "Chemical tank detachments and projector units" | Ground raids (cylinder release, projector barrage, artillery fire plan, light/medium/heavy armored delivery) and air raids with equipment reserved at preparation; named support companies | `docs/systems/cbrn_warfare/cbrn_native_raid_migration.md`, `common/raids/cbrn_chemical_land_raids.txt`, `common/raids/cbrn_chemical_air_raids.txt`, `localisation/english/chaosx_units_l_english.yml:102-132` |
| 19 | Chemical doomsday | "A fascist country close to capitulation can gain a last-resort decision" | Last-resort native raid: fascist government at war, surrender progress above threshold, Unrestricted Authorization, one stockpile each of four agents | `common/scripted_triggers/cbrn_chemical_doomsday_triggers.txt:32-52`, `common/raids/cbrn_doomsday_raids.txt:1-100` |
| 20 | Biological delivery | "Special strike missions require suitable aircraft and weapons" | Native raids: strategic, battlefield, sabotage, recovery; battlefield raids need Pathogen Handling Protocols, readiness, authority | `docs/systems/cbrn_warfare/biological_warfare/biowarfare_system.md` Delivery, `docs/systems/cbrn_warfare/cbrn_native_raid_migration.md` |
| 21 | Biological doomsday | "A last-resort biological release consumes the country's stockpile" | Adds Unrestricted Authorization, near-capitulation or world-end condition, and one stockpile of each of four agents | `docs/systems/cbrn_warfare/biological_warfare/biological_doomsday_release.md` Purpose |
| 22 | Military industrial organizations | Six generic functions | Three shared organizations plus national and fictional organizations and industrial concerns | `docs/systems/cbrn_warfare/cbrn_designers.md` "Current accepted and source-backed contract"; `common/military_industrial_organization/organizations/` |
| 23 | Capitulation Chaos | not listed | +1, or +3 for a major power (hardcoded 3 for major) | `common/scripted_effects/chaos_meter_effects.txt:6317-6327` |
| 24 | Chaos sources table | 9 rows | Adds subject independence, subject annexation, faction creation, coups, capitulation and restoration, exile and reinstatement, joining allies, major-power guarantee and war goal expiry; nuclear tests, accidents, demonstrations | `common/script_constants/chaos_meter_constants.txt:228-330`, `common/scripted_effects/chaos_meter_effects.txt:5799-6365`. Civil-war and call-allies deltas exist but their hooks are commented out (`:6108-6112`, `:6275`), so they were left out |
| 25 | Death Chaos weight | "Every million recorded deaths adds 1 Chaos" | Adds that a few causes count at a reduced weight | `common/script_constants/chaos_meter_constants.txt:303-318` (`chaos_meter_deaths` weights 0.10 and 0.20) |
| 26 | Scenarios | "Each entry offers a type selection and a four-level intensity slider" | "Most entries"; adds shortcut, confirmation, name list of 15 catalog scenarios plus Fallout | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:80-208` (16 registered ids), `localisation/english/chaosx_gui_l_english.yml:63-175` |
| 27 | Settings structure | Subsections "Event System Settings", "Timer and Country Settings", "Chaos Meter Configuration", "Advanced Settings", "Miscellaneous Settings" | One subsection per window section with the exact names (Trigger Events, Timer System, Tag Management, Chaos Meter, Advanced Settings, Miscellaneous, Reset All Settings, Scenarios); timer limits 5 and 999 days; Disable World End; Timer Modifier meaning | `localisation/english/chaosx_gui_l_english.yml:18-39`, `:919-972`, `:1038-1092` |
| 28 | Chaos Meter window | no opening instruction | Click the top-bar meter or press Ctrl+Shift+M | `interface/chaosx.gui:328`, `localisation/english/chaosx_chaos_meter_l_english.yml:4` |
| 29 | Event Logs | no opening instruction | Ctrl+Shift+E, Ctrl+E for Events tab | `interface/chaosx.gui:14,64,381` |
| 30 | Condemnation responses | not described | Compliance, defiance, and evasion decision families; cost scales with Condemnation | `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` lines 405-470 |
| 31 | Clusters | not described | 19 clusters named | `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (rows 1-19) |
| 32 | Achievements | no count | "More than 370" (377 `possible` blocks) | `common/achievements/chaos_redux_achievements.txt` |

## Claims verified unchanged

Timer ranges and acceleration table (`common/script_constants/event_system_constants.txt:7-70`, `common/scripted_effects/chaosx_logic_effects.txt:222-495`), tier multipliers 1.0, 0.8, 0.7, 0.6, 0.5, 0.5, Chaos tier ranges (`chaos_meter_constants.txt:12-21`), the nine Chaos source rows already in the guide, the nuclear ladder 10/5/3/2/1, military buildup 100 and 100, air recovery rates and thresholds (`chaos_meter_constants.txt:637-665`), treaty project numbers (`fallout_consolidated_constants.txt:86-90`, decision file `fallout_consolidated_decisions.txt:34-221`), Condemnation tiers (`condemnation_sanctions_constants.txt:111-118`), famine stages (`famine_l_english.yml:15-19`), the five map modes (`chaosx_map_modes_l_english.yml`), the three-crisis cap (`individual_crisis_targeting_constants.txt`), default weight 1,000 and recovery 20 and cap factor 0.5 (`event_system_constants.txt`), robot width 2 and 50 and 10, and the Help window tabs.

## Unresolved items

| Item | Disposition | Reason |
| --- | --- | --- |
| Tier 4 name in the Chaos Meter top bar and window is "Total Chaos" | `unresolved` | `localisation/english/chaosx_chaos_meter_l_english.yml:12` says "Total Chaos"; the event requirement text and Event Logs use "Totalen Chaos" (`chaosx_gui_l_english.yml:380,852`). The guide uses "Totalen Chaos" as instructed. The settings tier tooltip at `chaosx_gui_l_english.yml:1046-1047` also calls it "Critical (800)". The localisation owner should choose one name. |
| SCN-014 Assassin Network in the scenario catalog | `unresolved` | `chaos_redux_scenarios_catalog.csv` lists it, but `triggerable_scenarios_initialize_registry` (`chaosx_triggerable_scenarios_effects.txt:80-208`) does not register it and the launcher shows id #014 for Fallout (`chaosx_gui_l_english.yml:74`). The guide lists 15 catalog scenarios plus Fallout and omits Assassin Network. The catalog owner and event owner must decide whether the scenario or the catalog row is current. `docs/systems/event_system/triggerable_scenarios.md` already records identity conflicts for SCN-014 to SCN-016. |
| Whether Fallout should be described as a scenario | `unresolved` | It is a registered, player-visible launcher entry but the docs call it a consequence outside the catalog. The guide mentions it as a single setup. |
| `docs/systems/chaosx_settings/settings_miscellaneous_menu.md` still documents a Harder Crises for Players checkbox | `unresolved` (documentation out of scope for this task) | Contradicts current source; see correction 1. |
| `docs/systems/shared_autonomous_robot_system.md` line 15 says robots use 50 manpower | `unresolved` (documentation out of scope) | Source sets manpower to 0; see correction 6. The guide follows source. |
| `docs/systems/air_cleanliness/winter.md` phase table uses "Dimming" and "Clear" | `unresolved` (documentation out of scope) | Player-facing names differ; see correction 2. |
| Count of historical CBRN scientists (67 in `cbrn_historical_scientists.md`) | `unresolved` | Not verified against script, so the guide says "historical chemical and biological scientists" without a number. |
| Which Army Headquarters feature or DLC the HQ sections need | `unresolved` | `chaos_warfare_doctrine.md` says the surface is DLC-owned but does not name it; the guide does not name it. |
| Camp starting networks (correction 8) | `unresolved` | Supported by documentation only. The condition for each country was not traced in script. |
| Per-country details overlay in the Deaths tab | `unresolved` | `docs/systems/chaos_meter/README.md` records conflicting records. The guide says only that country values show causes on hover, which matches `chaos_meter_popup_window.md`. |
| Live behavior of every item | `unresolved` | All claims come from source and localisation reading. No game session, MCP render, or save inspection was used. `hoi4.reference_*` and GUI inspection tools were not run because this task edits prose only. |

## Image placeholders

All 27 original placeholders are still present and unchanged.
Two of them describe targets that no longer exist, so a corrected placeholder follows each:

- Line 548: "In-game Miscellaneous settings with audio and crisis-difficulty controls." The crisis-difficulty control does not exist. The corrected line 549 asks for the audio volume and Disable Fallout controls. The orchestrator should drop line 548 or capture the same screenshot as line 549.
- Line 736: "In-game Repression and Camps System with an affected territory and site details visible." That window is now called Camp Administration. The corrected line 737 asks for its Locations tab. The orchestrator should drop line 736 or reuse the line 737 capture.

Lines in the final file (generated with `grep -n "IMAGE PLACEHOLDER"`):

| Line | Subject | Status |
| ---: | --- | --- |
| 116 | Event countdown beside Chaos tier | original |
| 151 | Super-event announcement | original |
| 178 | Chaos Meter window, five tabs | original |
| 268 | Air Cleanliness tab, source details | original |
| 290 | Air Winter map | original |
| 304 | Treaty decisions | original |
| 340 | Condemnation country details | original |
| 350 | Deaths tab | original |
| 385 | Famine map and relief decision | original |
| 416 | Migration map | original |
| 417 | Reception decisions | original |
| 437 | World-end details | original |
| 471 | Events tab with detail window | original |
| 491 | Cluster detail window | original |
| 512 | Event settings, Force Trigger Mode | original |
| 548 | Miscellaneous settings, crisis-difficulty (stale) | original, stale |
| 549 | Miscellaneous settings, audio and Disable Fallout | new |
| 591 | Scenario controls | original |
| 629 | Special projects screen (chemical and biological project lineup, one project's requirements and prototype reward choices) | new |
| 648 | Chemical raid selection | original |
| 668 | Contaminated state with protection and cleanup | original |
| 694 | Outbreak map | original |
| 703 | Outbreak-response decisions | original |
| 736 | Repression and Camps System (stale) | original, stale |
| 737 | Camp Administration, Locations tab | new |
| 738 | Camp Administration, Administration tab | new |
| 847 | Chaos Warfare doctrine, four tracks | original |
| 848 | Chaos Warfare use-policy decisions, three choices with cost and reassessment period | new |
| 883 | Headquarters order | original |
| 905 | Civilian protection and cleanup decision | original |
| 953 | Autonomous robot battalion | original |
| 963 | Custom battalions in division designer or unit list | new |
| 984 | Map-mode buttons and tooltip | original |
| 994 | Achievements list | new |
| 1003 | Help window, five tabs | new |

(Line numbers were taken after the final edit; re-run the grep before capturing because later edits shift them.)

## Markdown prose check

No prose sentence is split across lines.
A scripted check found only list items and one list continuation that end without punctuation, and these are deliberate structures.

## Remaining risks

- The guide now describes systems from source and localisation that the user has not seen in a live game. Camp Administration, the Chaos Warfare policy cards, the five HQ orders, and the native raid planner are the largest new descriptions.
- Several other numbers come from `docs/systems/` pages rather than direct script reads: the Condemnation compliance, defiance, and evasion families, Camp Administration behavior, and the biological and chemical raid routes. They matched the localisation and decision files I opened but were not traced end to end.
- `docs/systems/` contains pages that still contradict current source (listed above) and will mislead the next curator unless they are corrected.
