# Event 013 - Natural Disasters

Event 013 is a repeatable, non-terminal disaster system rooted at `chaosx.nr13.1`. It presents physical disasters in named states, applies population and building losses, schedules delayed affected-country reports, and leaves state-scoped aftermath work behind. A single accepted Event 013 call owns one sequence and at most one Event 013 history row even when that sequence produces many delayed impacts, reports, news items, follow-ups, and reassessments.

The implementation is a fresh source design. Event 046 is an inactive unknown placeholder, Event 099 is an inactive placeholder rather than a second sandstorm engine, and Event 051 remains the separate Heat Wave event. Event 013 heat cannot target a country carrying the Event 051 heat-wave idea, and Event 051 clears Event 013 heat aftermath before applying its own effect.

## Runtime flow

1. The random-event dispatcher, Natural Disasters cluster, Disaster Barrage scenario, or another event calls `call_natural_disaster` from country scope.
2. The public API validates the caller, family, target mode, severity, presentation policies, scaling overrides, heat exclusion, and abnormal-family access.
3. The resolver selects an exact country, state, or strategic region and provisionally allocates a global sequence id; a no-target rejection rolls that allocation back.
4. Every primary impact receives a distinct future date. The warning job, impact job, controller report, optional news item, family follow-up, and recovery reassessments are stored in the affected state's current controller queue.
5. `chaosx.nr13.2` processes one due job. Impact resolution applies Deaths-system population loss, family-specific building damage, state disruption, regional spread when appropriate, aftermath-card state, report/news routing, and follow-up scheduling.
6. Rescue, stabilization, and reconstruction missions advance the state card. Full recovery closes the card; partial or failed work prolongs cleanup and may strengthen delayed chains.
7. Sequence-aware ledgers close achievement and history predicates only after that exact sequence has no queued jobs left in the affected country.

Delayed subevents are never scheduled on the call date. A global reservation ledger prevents two jobs in the same sequence from sharing a due date.

## Public disaster-call API

`call_natural_disaster` is defined in `common/scripted_effects/chaosx_dynamic_effects.txt`; its full contract and example are documented in `common/scripted_effects/chaosx_dynamic_effects.md`.

The caller may provide:

- a specific family, one of the family groups, or the evolution-aware random family pool;
- a random valid target, selected country, selected state, selected strategic region, coast, nearby enemy, dense state, or caller-provided target mode;
- local, severe, regional, catastrophic, or abnormal severity;
- single, local-season, regional, barrage, or moving-corridor sequence mode and an optional exact primary-impact count;
- none, meaningful, first-family, major-only, or always-news policy;
- affected-country, caller, or global report policy;
- aftermath and follow-up policy;
- separate death, building-damage, warning-chance, supply-disruption, and recovery-burden multipliers;
- scenario type and intensity for Disaster Barrage calls;
- explicit caller-cost, cooldown, and target-legitimacy proof flags for deity or hostile-actor calls;
- Event 013, scenario, or no-history ownership.

Selected-country and selected-state calls use regular event targets named `natural_disaster_call_target_country` and `natural_disaster_call_target_state`. The caller must set the matching `natural_disaster_call_target_country_supplied` or `natural_disaster_call_target_state_supplied` proof to `1` immediately after saving that target; caller-provided targeting can supply either or both proved pairs. The outputs identify acceptance or rejection, the rejection reason, allocated sequence id, and primary jobs queued. Invalid enums, conflicting specific family selectors, missing or stale targets, invalid scaling, unauthorized abnormal bypasses, and unproven hostile calls fail closed and queue nothing. Public inputs are reset after every call so one external event cannot leak arguments into the next, and a no-eligible-target result preserves the last accepted sequence state.

When an explicit selected-state or caller-provided impact reaches a state with an open card, the new impact merges into that card instead of disappearing. Losses and burden accumulate, completed response work remains credited, and the latest sequence becomes the card owner. Random target selection still avoids open cards. State-control changes use a narrow on-action path that removes every former-country mission and pointer, closes any in-transit foreign-relief target, migrates every aligned delayed-job row without changing its reserved due date, and transfers the live card, abnormal-map entry, phase capacity, and chain objective to the valid country that owns or controls the state. Controller-only occupations remain actionable under the controller; the unresolved-territory card is reserved for a state without a valid responsible country.

Every report policy queues a delayed family report for the affected state's current controller, including external calls and occupied states. Caller policy also informs the caller, global policy delivers the family report to every country, delayed-batch policy keeps the controller report in the sequence queue, and silent policy suppresses only additional distribution. News policy is independent and controls the rarer world-facing news event.

The reusable API owns disaster logic. External callers do not copy Deaths registration, damage, report, aftermath, or follow-up code.

## Disaster families

The engine defines 25 families:

- earthquake;
- flood;
- tropical cyclone;
- extreme wind;
- tornado outbreak;
- thunderstorm;
- hailstorm;
- blizzard;
- cold wave;
- heat wave;
- drought;
- dust and sandstorm;
- wildfire;
- dry mass movement;
- wet mass movement;
- volcanic eruption;
- ashfall;
- lahar;
- tsunami;
- storm surge;
- meteor impact;
- meteor shower;
- whole-earth rupture;
- massive eruption;
- moving storm corridor.

Each family profile selects its lethality, priority building types, transport/industry/port/air/resource exposure, default follow-up route, report event, news event, warning action, AI target priorities, and aftermath text. Reports are separate event definitions rather than one generic popup with substituted place names.

Random targeting uses a distinct fit profile for every family. Coastal families require a coast. Other families weight the physical and logistical exposure that the HOI4 state model can actually expose: population density, agricultural state category, infrastructure and rail, supply nodes, ports and dockyards, air bases/radar/anti-air, industry, resources, capital status, previous dry/wet/volcanic disaster history, and wartime logistics. HOI4 exposes no stable state-level desert, slope, river-valley, or volcanic-arc trigger to this script, so dust, mass-movement, and volcanic families use those documented infrastructure, agriculture, resource, coast, and disaster-history proxies rather than silently treating all inhabited land as equivalent.

Geological disasters at regional severity or above can produce a delayed tsunami risk on a coast. Earthquakes otherwise favor aftershocks, volcanic eruptions favor lahars, and meteor impacts favor displacement pressure. The tsunami-prevention action can cancel a queued second wave before its job matures.

## Evolution behavior

### Baseline

Baseline random seasons draw earthquake, flood, extreme wind, thunderstorm, hailstorm, cold wave, heat wave, wildfire, and dry mass movement. They use local or severe impacts with distinct state targets and delayed reports, cause meaningful damage to infrastructure, supply, industry, ports, airfields, or resources according to family identity, and pass population losses to the shared Deaths system as the natural-disaster cause.

### Evolution I - Wider Disaster Seasons

Evolution I expands sequence length and adds tropical cyclone, blizzard, drought, dust and sandstorm, wet mass movement, volcanic eruption, and storm surge to the random pool. More warning and aftermath cards can compete for the fixed mission slots, making prioritization important even before regional spread is common.

### Evolution II - Regional Cascades

Evolution II adds tornado outbreak, ashfall, lahar, and tsunami to the normal random pool. It raises deaths, building damage, state-modifier duration, neighboring-state damage, supply disruption, famine, disease, refugee pressure, and recovery-score penalties. Regional and catastrophic impacts apply weaker but still persistent cards to neighboring valid states, including their own controller reports and recovery work.

### Evolution III - Abnormal Paths

Evolution III opens abnormal meteor showers, whole-earth rupture, massive eruption, moving storm and tornado corridors, multi-coast tsunami paths, and related severe chains. These can devastate several states or regions while remaining non-terminal. Automatic abnormal families observe a global cooldown; the manual Maximum Disaster Barrage may bypass that cooldown only for its call and does not record a natural Evolution III milestone.

## Damage, Deaths, and disruption

Population loss scales from state population, family lethality, severity, evolution, caller overrides, vulnerability, preparation, and resilience. The resulting deaths are removed from the state and registered through cause id 14 in the Deaths system.

Building damage is distributed among the family's primary, secondary, and tertiary building types, then extended to transport, ports, airfields, industry, and resources where the family profile calls for them. State disruption is stored in `natural_disaster_state_disruption`; regional spillover uses `natural_disaster_neighbor_disruption`. Supply, supply impact, movement, attrition, repair, and resource penalties persist until recovery or expiry.

## Warnings and aftermath

The `Disaster Warnings and Aftermath` category is visible from the first warning through cleanup. Its state-targeted entries expose the affected state, family, damage type, disruption, recovery need, follow-up route, current phase, and next reassessment.

Warning actions are family-specific. Every one of the 25 families has three mutually exclusive preparations, for 75 named actions. The catalogue covers rail stand-downs, rolling-stock movement, port closures, shelter belts, lightning patrols, aircraft protection, fuel corridors, heated shelters, water points, firebreaks, slope watches, valley evacuation, exclusion zones, machinery covers, lahar and tsunami sirens, storm-surge road defenses, crater evacuation, lights-out sheltering, food corridors, and path rerouting. The chosen protection is persisted and appears on the aftermath card and abnormal map. Costs draw from manpower, support equipment, trucks, trains or convoys, fuel, stability, and war support as appropriate, and holding exactly the displayed physical cost is sufficient.

After impact, missions advance through:

- early rescue, with three base slots and a fourth reinforced slot;
- middle stabilization, with two base slots and a third reinforced slot;
- late reconstruction, with two base slots and a third reinforced slot;
- one active chain-prevention mission;
- one active inbound-relief mission;
- one active outbound-relief operation per donor.

Capacity responds to country weakness, major-power resources, war, Evolution II pressure, active-card burden, incoming relief, and Maximum Barrage mobilization while remaining within the 4/3/3 hard caps. Each refill scores eligible states by severity, population, capital status, strategic transport, industry, coast, and chain risk, so the most exposed open card receives the next slot. Mission outcomes are full success, partial success, or failure. Partial reconstruction closes only after a cleanup reassessment and leaves a weaker recovery-strain modifier. Terminal failure strengthens disruption and schedules a family-conditioned follow-up or political shock, produces another affected-country report, and can disqualify response achievements. The failure guard resets for every new card, so repeated disasters in the same state retain the full failure contract. Closing a card releases ordinary and special mission slots in the same effect chain, clears temporary family pressure, removes heat overlap, updates the recovery catalogue, and refreshes the category.

The seven playable follow-up objectives are separate tsunami, disease, famine, wildfire-spread, supply-collapse, lahar, and aftershock missions. The queue draws an arrival inside the accepted family band, records the reserved due date, and gives the matching objective a deadline one day earlier. Tsunami evacuation uses trucks, convoys, manpower, and fuel; disease prevention uses medical stores and vehicles; famine prevention opens a train or convoy food corridor; wildfire work funds firebreak patrols; supply prevention holds a transport route; lahar work clears valleys by road and rail; and aftershock work inspects priority structures. Full work cancels the chain. Partial work applies chain-specific human, material, and disruption multipliers before impact. Failure strengthens those same components before deaths and damage are calculated. Refugee and political chains remain visible consequences but do not consume the single objective slot, while a refugee-derived disease chain receives its own timed disease mission.

Foreign relief has neighboring convoy, port lifeline, engineer-column, and medical-column variants. The donor pays physical equipment, transport, fuel, stability, and war-support costs and receives a temporary outbound burden. The recipient receives a targeted relief mission and, on arrival, temporary dependency pressure plus a gratitude opinion modifier. Neighbor medical aid rejects enemies and requires a faction, subject, or positive-opinion relationship; humanitarian government direction increases AI interest without bypassing that legitimacy gate. AI chooses actions from family, capital, population, transport, industry, war, chain, and severity priorities.

## Abnormal disaster path map

`common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`, and `interface/013_natural_disasters.gfx` define the Evolution III/manual-abnormal map. Normal disasters remain in the aftermath category.

The active map combines every abnormal sequence visible to the current controller and rebuilds up to five cards by urgency: imminent impact, active warning, scheduled warning, chain risk, unresolved severity, and next due date. The top card selects the active physical layer; path-segment index breaks equal-urgency ties. Event Details opens a global Evolution III history view that remains available after cleanup and before the first abnormal path, where it shows a dormant monitor instead of disabling the button. Selecting a card shows the exact state, family, severity, warning result, card phase, damage, follow-up, scheduled impact date, next reassessment, and sequence id.

Abnormal history uses an aligned global record ledger rather than reading the affected state's current disaster variables. A state/sequence pair owns one record index; live warning, impact, and recovery changes refresh only that matching row, while cleanup freezes its final status. A later ordinary disaster cannot rewrite the archived family, severity, dates, deaths, recovery result, or path layer. If another abnormal sequence later crosses the same state, it appends a separate record, so both cards can appear together in history. Each country rebuild copies the selected records into aligned local view arrays with a globally unique rebuild pass, preventing one observer's sort markers from hiding records for another observer. The dormant view and every selected-row GUI trigger are guarded against missing array entries.

The live layers are rupture wave, meteor fall, eruption plume, tsunami train, and storm corridor. Warning and impact card rims, the next-hit marker, and path layers use horizontal DDS frame sheets. Every animated sprite has an explicit static DDS fallback controlled by the Motion / Static button. GIFs exist only as review previews in the asset package and are not referenced by gameplay.

## Super-events

Six researched, non-terminal super-event packages are reserved for rare abnormal milestones:

- slot 67, `NO FIRM GROUND`, whole-earth rupture;
- slot 68, `ASH AT NOON`, massive eruption;
- slot 69, `THE BURNING FIRMAMENT`, meteor shower;
- slot 70, `THE FRETFUL ELEMENTS`, moving storm corridor;
- slot 71, `OLD STORIES CEASE TO BE INCREDIBLE`, first natural abnormal age;
- slot 72, `BELOW THE STONE`, delayed multi-coast tsunami chain.

The final quote, cultural-reference, image, and audio source decisions are recorded in:

- `docs/super_events/013_natural_disasters_super_event_text_research.md`;
- `docs/super_events/013_natural_disasters_super_event_audio_research.md`;
- `docs/super_events/013_natural_disasters_super_event_research_addendum.md`;
- `docs/assets/013_natural_disasters/audio_manifest.md`.

Each slot has its own image sprite, audio id 37-42, music track, short sound variant, localisation, once-only gate, and same-sequence suppression.

## Achievements

The Event 013 achievement set is defined in `common/achievements/chaos_redux_achievements.txt` and uses sequence-bound ledgers rather than button counts:

- `All Clear, All Accounted For`: close every tracked card from a severe season without a failed deadline or abandonment;
- `The Tide Stops Here`: prevent a delayed geological tsunami before arrival or a major second death spike;
- `The Trains Came Through`: recover every tracked regional transport card without losing the capital supply route;
- `Bread Beneath the Ash`: recover every major ashfall state before famine matures;
- `No World Weather Office`: receive affected-country reports from four normal family groups without global-announcer policy;
- `Keep the Runways Lit`: endure a full meteor-shower sequence while the controlled capital, supply route, and airfield network remain operational;
- `Brace the Broken Earth`: recover the required whole-earth rupture regions before a major aftershock or delayed tsunami matures;
- `All Sirens at Once`: survive Maximum Disaster Barrage, preserve the capital route and a port or rail corridor, and close the required recovery cards before its deadline;
- `Every Cot Accounted For`: complete protection work for severe refugee pressure without the death, camp-disease, or border-camp failure gates;
- `An Atlas Bound in Dust`: fully reconstruct at least one card from every normal disaster family group.

Complete, grey, and not-eligible icon triplets live under `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.

## Cluster and scenario integration

Natural Disasters is repeatable cluster id 5. It contains five logical Event 013 season slots: one required local season, an optional early repeat, an Evolution I varied repeat, an Evolution II regional repeat, and an Evolution III abnormal repeat. All five dispatch the public API and each accepted season owns its own Event 013 history row. Events 046, 051, and 099 are not cluster members.

SCN-007 `Disaster Barrage` calls the same API once from the selected country. Its type choices are Random Barrage, Geological Crisis, Weather Crisis, Skyfall Crisis, and Full Catalogue. Low, Medium, High, and Maximum scale sequence length, severity, aftermath policy, delay pressure, and abnormal access. Maximum is non-terminal and opens the abnormal map without setting `world_end`.

## Gameplay and presentation files

- events: `events/013_natural_disasters.txt`;
- constants: `common/script_constants/013_natural_disasters_constants.txt`;
- effects and triggers: `common/scripted_effects/013_natural_disasters_effects.txt`, `common/scripted_triggers/013_natural_disasters_triggers.txt`;
- state modifiers: `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt`;
- decisions and categories: `common/decisions/013_natural_disasters_decisions.txt`, `common/decisions/categories/013_natural_disasters_categories.txt`;
- ideas and opinion modifiers: `common/ideas/013_natural_disasters_ideas.txt`, `common/opinion_modifiers/013_natural_disasters_opinion_modifiers.txt`;
- on-action hook: `common/on_actions/013_natural_disasters_on_actions.txt`;
- scripted GUI: `common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`;
- sprites: `interface/013_natural_disasters.gfx`, `interface/chaosx_super_events.gfx`, `interface/chaosx_achievements.gfx`;
- localisation: `localisation/english/013_natural_disasters_l_english.yml` and the shared event-log, scenario, achievement, Deaths, and music localisation files;
- scripted localisation: `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt` and shared Event Details selectors;
- catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`;
- asset manifest and wiring map: `docs/assets/013_natural_disasters/manifest.md`, `docs/assets/013_natural_disasters/gfx_handoff.md`.

## Icon and sprite wiring

All Event 013 art uses stable sprite names. The exhaustive source, processed PNG, DDS, dimension, prompt, provenance, and contact-sheet ledger is `docs/assets/013_natural_disasters/manifest.md`.

Gameplay registrations are grouped as follows:

- family report sprites `GFX_report_event_nd_*`: `gfx/event_pictures/013_natural_disasters/`, registered in `interface/013_natural_disasters.gfx`;
- family news sprites `GFX_news_event_nd_*`: the same event-picture folder and GFX file;
- decision-category pictures `GFX_decision_cat_picture_nd_*`: `gfx/interface/decisions/013_natural_disasters/`, registered in the Event 013 GFX file;
- decision-category button icons `GFX_decision_category_nd_*`: the same decision folder and GFX file;
- response decision icons `GFX_decision_nd_*`: the same decision folder and GFX file;
- idea sprites `GFX_idea_013_disaster_aftermath`, `GFX_idea_013_refugee_pressure`, `GFX_idea_013_famine_pressure`, `GFX_idea_013_broken_infrastructure`, and `GFX_idea_013_disaster_recovery_mobilization`: `gfx/interface/ideas/013_natural_disasters/`;
- abnormal GUI statics `GFX_013_abnormal_disaster_panel`, `GFX_013_abnormal_disaster_panel_damaged`, `GFX_013_disaster_card_frame`, `GFX_013_map_marker_impact`, `GFX_013_map_marker_chain_risk`, `GFX_013_foreign_relief_badge`, `GFX_013_recovery_progress_frame`, and `GFX_013_recovery_progress_fill`: `gfx/interface/013_natural_disasters/`;
- abnormal GUI animated/static pairs: `gfx/interface/animated/013_natural_disasters/`, registered in `interface/013_natural_disasters.gfx`;
- six super-event sprites `GFX_super_event_nd_*`: `gfx/super_events/013_natural_disasters/`, registered in `interface/chaosx_super_events.gfx`;
- ten achievement triplets: `gfx/achievements/`, registered in `interface/chaosx_achievements.gfx`.

## Balance notes

The numeric tuning source is `common/script_constants/013_natural_disasters_constants.txt`. Ordinary baseline disasters are intended to kill thousands to tens of thousands in exposed states. Regional Evolution II seasons can reach hundreds of thousands across multiple vulnerable states. Evolution III abnormal paths may produce multi-million aggregate loss when the family, state population, failed preparation, and failed recovery align.

The achievement thresholds deliberately require several recovered cards or operational routes. The major second-wave death spike is 100,000, the severe refugee death failure line is 50,000, the meteor-shower airfield network requires two controlled airfield states, whole-earth rupture recovery requires five cards, meteor survival requires four tracked hits, and Maximum Disaster Barrage requires ten fully reconstructed cards.

## Future plans

- Add optional memorial and long-term rebuilding flavour after historically large but successfully closed disaster seasons without reopening gameplay cards.
- Expand regional target-fit data only when new state metadata can improve family selection without introducing world scans.
- Add any future abnormal visual family as a real source-frame package with its own static fallback and manifest entry.
- Keep Event 046 inactive, keep Event 051 separate, and route any future Event 099 bridge through `call_natural_disaster` rather than restoring standalone sandstorm damage.
