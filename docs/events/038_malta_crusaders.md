# Event 38: Malta Crusaders

Source design: `docs/specs/038_malta_crusaders_specs/`. This page describes what the repository implements. The design decisions accepted by the release-pass parent on 11 October 2026 are recorded in the spec README.

## What the event is

The Order of Saint John rises as a crusader state. Malta is released at once together with Jerusalem, a Holy Land corridor, a maritime bridge and one island foothold, and the governments that lost them are at war with Malta from the first day. The campaign is a management loop of three readouts (Command Standing, Order Cohesion, Sacred Legitimacy) over a council of military orders, a set of logistics and campaign actions, and a recovery route (the Eleventh Crusade) for the case that the expedition collapses.

- Entry event `chaosx.nr38.1`, Minor Fire-Once, Chaos level 1, member of the Formables cluster (cluster id 6) as an optional High member that is eligible from tier 0.
- Enabled by default through `event_log_event_is_reworked_default_enabled`.
- Event Details text key `malta_crusaders.event_details.description`.
- Catalog note: the spreadsheet row for Event 38 and the Formables cluster membership are not edited here. The spreadsheet worker updates the workbook and runs `python .tools/export_event_catalog_csv.py`.

## Phase status

| Phase | Content | State |
| --- | --- | --- |
| 1 | Opening release transaction, Malta package, Crusade Council values and header, baseline decisions and missions, failure comeback, reactions, reports, news, event log, cluster, constants, baseline achievements | implemented, never run in game |
| 2 | Focus tree, principalities and governance | see the phase 2 section when present |
| 3 | Evolutions I to III | see the phase 3 section when present |

## Deferred by decision

These parts of the spec are intentionally outside the release pass. The scripts do not contain stubs for them.

| Part | Reason |
| --- | --- |
| Custom unit families, counters, audio, animation (spec 05 and 17) | They need the 3D model pipeline. Malta uses the ordinary infantry, cavalry, artillery and engineer sub-units under the template names Fortress Commandery, Armored Knight Banner, Mounted Crusader Column, Crossbow Levy, Siege Host, Holy Land Guard and Crusader Engineers. A later pass swaps a family by changing `malta_create_templates` and the template tables only. |
| Hidden Teutonic Order and Atlantis betrayal (spec 10 and 11) | Deferred to a later pass. No script, loc or public text mentions them. |
| Holy World terminal and the Believers vs Nonbelievers scenario (spec 12 and 13) | Deferred to a later pass. The event has no world-end row yet. |
| Super-event quotes and audio (spec 18) | The spec forbids invented quotes. No super-event is wired. |
| The Crusade Council window | Needs a reference image and the event UI worker. The header text of the council category carries the three readouts. |

## Event map

| Event | Role |
| --- | --- |
| `.1` | hidden entry, runs the opening transaction and sends the opening messages |
| `.2` | Malta: the crusade is underway, and the choice of the first command |
| `.3` | response event of every displaced owner |
| `.4` | appeal from Malta to Catholic governments (bounded recipients) |
| `.5` | weekly pulse of the actor (hidden) |
| `.6` | report to neighbouring governments (bounded recipients) |
| `.7` | world news |
| `.8` | an order's demand, with the three answers |
| `.9` | an incident in the council |
| `.10` | a demand that was not answered by its deadline |
| `.14` `.15` `.16` | Eleventh Crusade opens, succeeds, and the island settlement |
| `.20` | arbitration of Jerusalem |
| `.21` | a charter for one order |
| `.30` `.31` | ultimatum received by the target, and the answer reported to Malta |

## Opening transaction

The opening is one transaction in three steps and fails closed. The detailed reject codes are in the header of `common/scripted_effects/038_malta_crusaders_setup_effects.txt`.

1. Freeze (`malta_prepare_opening_transaction`). The pre-fire hook runs it before the Event History row is written. It reads the live map and writes the proposed states, the owners those states have now and the displaced top owners to private arrays. It changes nothing on the map. A blocked opening leaves the fire-once state unconsumed and the Events list shows N/A with the Malta reason.
2. Validate (`malta_validate_opening_transaction`). Every frozen state must still pass the target trigger at commit.
3. Commit (`malta_commit_opening_transaction`). The states move to Malta, ownership is proven for every state, then the package and the wars are applied. A failed proof restores every state to its recorded owner and leaves no package, flag or war behind.

### Malta identity

The actor is the vanilla tag `MLT` with the existing cosmetic tag `CRU` (Malta Crusader State). A live Malta is transformed. A dead Malta is revived by the first state transfer and receives the package. A Malta that is a subject, has capitulated, is a special actor or already carries the origin proof makes the opening unavailable. Collision scan: no other tag is created. `CRU` is the only cosmetic tag (`common/countries/cosmetic.txt`, flag files `gfx/flags/CRU.tga` and the medium and small variants). Origin proof is the country flag `malta_origin` with `malta_origin_event_038`, the transaction id in `malta_release_transaction_id` and the package level in `malta_package_level`. A human player who controls Malta before the event keeps control, the package is applied to that actor.

### Exact state registry

The registry is `common/scripted_triggers/038_malta_crusaders_map_triggers.txt`. Every id was read from the installed `history/states` files (the mod has no state overrides) and the map inspector confirmed all of them.

| Role | State | 1936 owner | Used in |
| --- | --- | --- | --- |
| heartland | 116 Malta | ENG | opening |
| Holy Land command (Jerusalem) | 454 Israel | PAL | opening |
| Holy Land corridor | 455 Jordan | JOR | opening (only with 454) |
| maritime bridge | 183 Cyprus | ENG | opening |
| island foothold, in priority order | 164 Dodecanese (ITA), 187 Aegean Islands (GRE), 182 Crete (GRE) | | opening (one foothold, two with Evolution II) |
| Levantine frontier | 553 Lebanon, 677 Aleppo, 799 Hatay | LEB, SYR, SYR | regional crusades |
| Anatolian march | 342 Antalya, 344 Adana, 345 Mersin | TUR | regional crusades |
| Greek mainland | 47, 186, 185, 731, 184 | GRE | regional crusades |
| North African coast | 661 Tripolitania, 663 Cyrenaica | ITA | regional crusades only |

The two North African states are wasteland without an installed naval base, so they never enter an opening package. Diyarbekir, Sinai and Cairo of the old stub are outside the registry. An opening state needs a valid owner (not capitulated, not special, not nonhuman) and must not be wasteland. At most four displaced top owners are allowed. A foothold is skipped when its owner would be the fifth.

### What the package does

- Capital Malta, cosmetic identity CRU, a Crusade Council government with Grand Master Ludovico Chigi Albani della Rovere (portrait `GFX_portrait_CRU_crusader`, an archival source placeholder, HOI4-style final pending) and five institutional officers named by office.
- Three national spirits (Fortress Without a Hinterland, The Orders Recalled, An Army Out of Time), limited conscription, early mobilization and limited exports.
- A 1936 baseline technology set, not a copy of the previous controller.
- Grants scaled by the package level and the footprint: political power, command power, army experience, rifles, support equipment, convoys, trains and fuel.
- Instant buildings: a workshop and a dockyard in Malta, a workshop and a road level in Palestine, a road level in Jordan, and with Evolution I a workshop in the bridge state.
- Forces: seven division templates and a one-time opening force. With package level 0 the force is 3 Armored Knight Banners, 2 Mounted Columns, 2 Crossbow Levies, 1 Siege Host, 1 Fortress Commandery and one Holy Land Guard per held state. Each level adds one banner of each line family and two guards. Evolution I adds a second Siege Host.
- Wars: one war per displaced top owner, with a claim on every registry state the owner still holds so `take_claimed_state` has a goal. An owner that holds no registry state gets a war without items.

## The Crusade Council

Three public readouts, shown in the header of the council category. Supply is read from the normal supply interface. Nothing else is persistent and visible.

| Readout | Form | Source |
| --- | --- | --- |
| Command Standing | five steps | computed by `malta_refresh_standing` from four anchors |
| Order Cohesion | 0 to 100 | moved by demands, incidents, Joint Command and settlements |
| Sacred Legitimacy | 0 to 100 | moved by arbitration, missions, reactions and settlements |

Anchors: Malta held; Jerusalem held for 30 days; at least one bridge state held (the sea road is not checked for blockade); a Holy Land state held (the port). Fewer than two anchors is Fractured, two Disputed, three Functional, four Functional until they have been held for 120 days, then Recognized. Supreme needs a completed settlement and no open demand (the flag is set by the settlement routes of phase 2 and by the Fortress Malta settlement). A suppressed incident or a returned state lowers the step by one for 90 days. The step is recomputed by the weekly pulse, by every state control change of a registry state and when an incident or a demand is resolved.

### Orders, demands and incidents

Six orders: Hospitallers, Templar Revival, Naval Orders, Teutonic Chapter, Order of Saint Lazarus and Siege Brotherhoods. The first three hold seats at the opening, Evolution I seats all six. Each order keeps an influence step and a grievance from 0 to 3. A filled seat applies a small idea.

A demand states the order and one of four requests (treasury, command, levy, headquarters in a named state), has a 45-day deadline and is answered by Grant, Offer half or Refuse. Cohesion moves by constants. An unanswered demand counts as a refusal. The cadence is an MTTH (base 195 days, longer when United, shorter in Open Rivalry, never under 60) and the first demand waits 90 days. An incident opens when an order's grievance reaches 3 or Cohesion falls below 30, with three answers (concede, arbitrate, suppress). Three incidents of one order within 365 days suspend its seat for 180 days.

## Decisions and missions

Four categories: The Crusade Council, Mediterranean Campaigns, The Banners and The Eleventh Crusade.

| Row | What it does |
| --- | --- |
| Grant, Offer half, Refuse | the three answers to a demand, one compromise per order until it is granted in full |
| Convene Joint Command | usually a better-planned army for four months, a failed conference exposes the rivalry |
| Arbitrate the Custody of Jerusalem | opens event `.20`, once, five outcomes |
| Seize an Order Treasury | funds and rifles now, a rift later, once |
| Escort the Sea Road | opens the sea road mission |
| Repair the Holy Land Rail | 150-day project that opens the corridor mission |
| Fortify a Port | state-targeted project, one per state, Malta opens the harbour mission |
| Open the Emergency Air Bridge | temporary supply relief when the sea road is cut |
| Issue a Crusader Ultimatum, Launch a Regional Crusade | aimed at the owner of registry states, one regional crusade at a time |
| Direct commandery, grant to an order, return under treaty | settlement of held states |
| Raise a banner (knights, mounted, crossbow, siege, engineers) | training time, a cap that grows with the footprint |
| Eleventh Crusade rows | evacuate, fortify Malta, volunteers, rebuild transports, choose a landing, launch, restore the Holy Land command, accept Fortress Malta |

Missions: Hold the Four Anchors, Keep the Sea Road Open, Guard the Jordan Corridor, Protect the Grand Harbour, The Evacuation, Gather the Landing Force and Hold the New Foothold. Each has success and failure outcomes.

### Merged or missing register rows

- Select Regional Objective is the target list of Issue a Crusader Ultimatum and Launch a Regional Crusade.
- The Port Project mission is the timer of Fortify a Port.
- Convert Captured Equipment, Request Foreign Equipment, Call Foreign Chapters, Request Papal Blessing, Seek Temporary Refuge, the principality, relic and Holy World rows and the order dominance and confederation rows belong to later phases or to parts deferred above.

### The Eleventh Crusade

A sustained loss opens the recovery: no Holy Land state for 60 days, or no expedition state at all, while Malta is held. Phase 1 (survivors): evacuate and fortify Malta. Phase 2 (rebuild): volunteers, transports and workshops, a gathering mission, the choice of a landing. The landing spawns a bounded force on the chosen coast and opens a mission to hold it. A failed landing raises the costs by a quarter of the base, and after three failures only the Fortress Malta settlement remains. Restoring the Holy Land command needs Jerusalem held for 60 days.

## AI

Decisions use the MTTH entries of `common/mtth/038_malta_crusaders_mtth.txt`. Survival rows (escort, air bridge, rail, harbour, recovery) outrank banners and expansion. Target rows add inline factors for the target (major powers, divisions, adjacent islands and Levant). Demand and incident options use the same scores as the decisions. The calculation was done by hand from the script. No MCP probability run was made.

## Interactions

- Event log: default actor Malta, Event Details text, N/A reason `malta_crusaders_target` in the Events list and in the cluster detail view.
- Formables cluster: optional High member from tier 0, row id 6002.
- Event 40: Jordan and the Levantine states can be targets of both events. Event 40 handles a target that lost its states through its own watchdog. No adapter exists.
- Event 6 and Soviet collapse carriers are not used in phase 1. The principality carrier plan belongs to phase 2.

## Achievements

`chaos_redux_038_deus_vult_logistically`, `chaos_redux_038_the_eleventh_time_is_the_charm` and `chaos_redux_038_malta_stands_alone`. All are `is_ai = no`, outside Force Trigger Mode, and set by flags in the weekly pulse. The remaining achievements of the spec need the focus tree, the principalities or the hidden routes.

## Icons and assets

All icons are vanilla stand-ins. No asset was created.

| Surface | Sprite | File |
| --- | --- | --- |
| spirits | `generic_fortify_the_borders`, `generic_supply_lines`, `generic_neglected_military`, `BEL_european_crusade`, `SPA_crusade_against_democracy`, `generic_army_war_college` and others | vanilla `GFX_idea_*` |
| decisions | vanilla `GFX_decision_generic_*` icons | vanilla |
| categories | `GFX_decision_category_generic_*` | vanilla |
| events and news | `GFX_news_crusaders` | existing mod sprite |
| leader | `GFX_portrait_CRU_crusader` | `interface/chaosx_characters.gfx`, placeholder from the Library of Congress archive, HOI4-style final pending from the user |

Assets still needed: Malta flags for each political form and the Holy See, the Kingdom of God and the cosmetic identities of phase 2 (`gfx/flags/`, three sizes each), achievement art (`gfx/achievements/chaos_redux_038_*.dds`), idea icons for the spirits and seats, decision icons, event report pictures for the opening, the Eleventh Crusade and the council scenes, portraits of the officers (`chaosx_portrait_creator`), the custom unit families with counters, audio and animation, and the Crusade Council window with its reference image.

## Limitations

- Nothing was run in the game. All checks are source review and static scans.
- The sea road anchor does not test for blockade, only for the held bridge state.
- Fortify a Port adds a building slot, a road level and a dockyard. Naval base level and coastal forts are province buildings and need exact provinces.
- The opening wars of owners that hold no registry state have no war goal items.
- No ship, aircraft or transport plane is created. Convoys come from the stockpile.
- Cosmetic CRU keeps its existing colour.

## Open tuning notes and future work

- Calibrate the opening force and the grants with live play, especially the British war that follows from Cyprus and Malta.
- A second demand family for relics and principalities arrives with the later phases.
- The order seats could show influence through a window instead of the header.
