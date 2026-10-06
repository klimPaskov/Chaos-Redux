# Event 013 - Natural Disasters

This overview retains package implementation and audit records. The [documentation review](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_events_011_013_014_documentation.md) separates their historical claims from the source checks and unresolved acceptance or validation in this cleanup.

Event 013 is a repeatable, non-terminal disaster system rooted at `chaosx.nr13.1`. It presents physical disasters in named states, applies population and building losses, leaves state-scoped aftermath work, and reports resolved consequences after each sequence's scheduled physical jobs drain, with a one-day serialized delivery delay. A single accepted Event 013 call owns one sequence and at most one Event 013 history row even when that sequence produces many delayed impacts, aggregate reports, news items, follow-ups, and reassessments.

The 2026-10-05 release disposition records the parent-accepted G2/G4 design: one aggregate report per recipient and sequence, one eligible world-news event per sequence, actual consequence accounting, and no second popup for later player-driven recovery outcomes. Source evidence and validation limits are recorded in the [release handoff](../../plans/013_natural_disasters_plans/2026-10-05_report_news_implementation_handoff.md). The supplemental report event `chaosx.nr13.100` remains inside Event 013 and does not receive a separate event-log identity or catalog row.

The implementation follows the Event 013 source design. Event 046 is an inactive unknown placeholder, Event 099 is a narrow compatibility bridge into Event 013's dust-and-sandstorm family rather than a second sandstorm engine, and Event 051 remains the separate Heat Wave event. Event 013 heat cannot target a country carrying the Event 051 heat-wave idea, and Event 051 clears Event 013 heat aftermath before applying its own effect.

## Runtime flow

1. The random-event dispatcher fires Event 013 against an eligible state controlled by the firing country. Natural Disasters clusters, Disaster Barrage scenarios, and other events call `call_natural_disaster` from country scope with their own documented target mode.
2. The public API validates the caller, family, target mode, severity, presentation policies, scaling overrides, heat exclusion, and abnormal-family access.
3. The resolver selects an exact country, state, or strategic region. Canonical Event 013 calls reroll evolution-valid families against the firing country's controlled states, while reusable random-valid calls may select another country. Both paths use the bounded target-attempt table before rejecting, then provisionally allocate a global sequence id. A no-target rejection rolls that allocation back.
4. Every primary impact receives a distinct future date. Random Event 013 and cluster seasons always give the first impact a state-specific warning on the preceding day, while later warnings and reusable external calls retain family and exposure chance. As soon as a target is accepted, its controller receives an available forecast decision naming the disaster, state, severity, hazard class, and scheduled date. Acknowledging it clears only that forecast alert. Warning, impact, follow-up, and recovery-reassessment jobs remain in the affected state's current-controller queue; report and eligible news consequences accumulate separately by sequence.
5. `chaosx.nr13.2` processes one due job. Impact resolution applies Deaths-system population loss, family-specific building damage, state disruption, regional spread when appropriate, aftermath-card state, factual consequence receipts, and follow-up scheduling. When the sequence's scheduled warning, impact, and follow-up jobs drain, the report finalizer routes one aggregate to each eligible recipient and dispatches at most one world-news event after rechecking family cooldowns.
6. Rescue, stabilization, and reconstruction missions advance the state card. Full recovery closes the card. Partial or failed work prolongs cleanup and may strengthen delayed chains.
7. Sequence-aware ledgers finalize report and news delivery only after that sequence's counted physical jobs have drained; later recovery outcomes still change the card, map, and history but cannot reopen a sent recipient report.

Delayed subevents are never scheduled on the call date. A global reservation ledger prevents two jobs in the same sequence from sharing a due date.

## Public disaster-call API

`call_natural_disaster` is defined in `common/scripted_effects/chaosx_dynamic_effects.txt`. Its gateway contract and a minimal example are documented in `common/scripted_effects/chaosx_dynamic_effects.md` under `call_natural_disaster`; the target and policy summary follows here. The Event 013 runtime implementation and private helpers remain in `common/scripted_effects/013_natural_disasters_effects.txt`.

The caller may provide:

- a specific family, one of the family groups, or the evolution-aware random family pool.
- a random valid target, selected country, selected state, selected strategic region, coast, nearby enemy, dense state, or caller-provided target mode.
- local, severe, regional, catastrophic, or abnormal severity.
- single, local-season, regional, barrage, or moving-corridor sequence mode and an optional exact primary-impact count.
- none, meaningful, first-family, major-only, or always-news policy.
- affected-country, caller, or global report policy.
- aftermath and follow-up policy.
- separate death, building-damage, warning-chance, supply-disruption, and recovery-burden multipliers.
- scenario type and intensity for Disaster Barrage calls.
- explicit caller-cost, cooldown, and target-legitimacy proof flags for deity or hostile-actor calls.
- Event 013, scenario, or no-history ownership.

Selected-country and selected-state calls use regular event targets named `natural_disaster_call_target_country` and `natural_disaster_call_target_state`. The caller must set the matching `natural_disaster_call_target_country_supplied` or `natural_disaster_call_target_state_supplied` proof to `1` immediately after saving that target. Caller-provided targeting can supply either or both proved pairs. Outputs identify acceptance or rejection, the rejection reason, allocated sequence id, scheduled and skipped primary counts, first resolved family, and proved first resolved state and country targets. The resolved-target proof values must be checked because regular event targets can outlive one request inside the same effect chain. A caller that reads an output after `call_natural_disaster` returns must initialize that temporary in its own effect context before the call; the outer disaster controller owns its nested outputs but cannot establish their lifetime in a previously uninitialized caller. The canonical `.1` initializes its acceptance result before calling. Random-family calls use weighted opening draws and then a complete group-preserving family pass, so compatible selected-country, state, and region requests do not fail merely because replacement draws missed the valid family. Invalid enums, conflicting specific family selectors, missing or stale targets, physically incompatible states, invalid scaling, unauthorized abnormal bypasses, and unproven hostile calls fail closed and queue nothing. Public inputs are reset after every call so one external event cannot leak arguments into the next, and a no-eligible-target result preserves the last accepted sequence state.

Direct ashfall, lahar, and tsunami calls must also supply a proved physical origin state together with a compatible origin family and origin medium. Those public calls cannot invent a volcanic or offshore cause from the destination alone. Internal causal continuation follows a separate authority path: it is validated against the owning card and sequence, retains the originating physical context, and may retain scenario evolution authority for the continuation. The scalar, target, origin, and authority contract remains centralized in this overview beside the Event 013 owner implementation. The public gateway itself remains in `common/scripted_effects/chaosx_dynamic_effects.txt`.

When an explicit selected-state or caller-provided impact reaches a state with an open card, the new impact merges into that card instead of disappearing. Losses and burden accumulate, completed response work remains credited, and the latest sequence becomes the card owner. Random target selection still avoids open cards. State-control changes use a narrow on-action path that removes every former-country mission and pointer, closes any in-transit foreign-relief target, migrates every aligned delayed-job row without changing its reserved due date, and transfers the live card, abnormal-map entry, phase capacity, and chain objective to the valid country that owns or controls the state. Controller-only occupations remain actionable under the controller. The unresolved-territory card is reserved for a state without a valid responsible country.

Affected-country and delayed-batch policies retain each consequence's original controller while that country survives, then use a surviving current controller or owner as fallback. Ordinary territorial transfers move physical jobs and live state work without taking a frozen report away from a surviving recipient. An annexed recipient's unseen per-state report rows migrate to the new controller, with a one-day dispatch delay allowing same-day callbacks to merge their rows. An already-open summary stays frozen; if its country is annexed, that shown summary closes while the unseen queue is preserved for migration. Caller policy also informs any distinct caller, global policy sends one aggregate to every existing country, and the legacy silent policy retains its controller report while suppressing additional distribution. These reports do not replace the historical Event 013 actor. News policy is independent and chooses the highest-severity family that remains eligible when the sequence flushes.

The reusable API owns disaster logic. External callers do not copy Deaths registration, damage, report, aftermath, or follow-up code.

### Event-owned internal helpers

Event 013 internal effects remain in `common/scripted_effects/013_natural_disasters_effects.txt` and are not part of the cross-system dynamic-effect registry.

- `natural_disaster_resolve_ordinary_family` resolves the ordinary family for a validated request.
- `natural_disaster_register_relief_recipient_country` and `natural_disaster_unregister_relief_recipient_country_if_inactive` maintain the bounded relief-recipient registry.
- `natural_disaster_transfer_pending_jobs_for_state` moves the complete aligned delayed-job rows when responsibility for an affected state changes.
- `natural_disaster_append_abnormal_history_record` and `natural_disaster_update_abnormal_history_record` own the abnormal-path history ledger.
- `natural_disaster_rebuild_abnormal_gui_view` projects that ledger into the Event 013 abnormal-disaster view.

External events call only `call_natural_disaster`. They do not call these internal helpers directly.

## Disaster families

The engine defines 25 families:

- earthquake.
- flood.
- tropical cyclone.
- extreme wind.
- tornado outbreak.
- thunderstorm.
- hailstorm.
- blizzard.
- cold wave.
- heat wave.
- drought.
- dust and sandstorm.
- wildfire.
- dry mass movement.
- wet mass movement.
- volcanic eruption.
- ashfall.
- lahar.
- tsunami.
- storm surge.
- meteor impact.
- meteor shower.
- whole-earth rupture.
- massive eruption.
- moving storm corridor.

Each family profile selects its lethality, priority building types, transport/industry/port/air/resource exposure, default follow-up route, batch report prose, news event, warning action, AI target priorities, and aftermath text. The 25 news events remain family-specific; the single supplemental country event presents mixed families and affected states from stored consequence rows.

Random targeting uses a distinct physical-eligibility trigger and fit profile for every family. Coastal families require a coast. Volcanic eruption, massive eruption, ashfall origin, and lahar origin are restricted by a curated 175-state Holocene-volcano registry derived from the Smithsonian Global Volcanism Program and mapped to the vanilla state raster. Massive eruptions use a narrower 92-state high-consequence subset, and lahars use a 103-state water-and-relief subset. Heat, cold, drought, wildfire, dust, tropical-cyclone, storm-surge, tsunami-basin, slope-failure, and moving-path families likewise fail closed outside their climate, basin, coast, relief, or exposure registry. In particular, all named Siberian strategic regions are cold-valid and heat-invalid. Eligibility is rechecked when a delayed impact matures and again for every neighboring spread, repeat, corridor segment, and chained target, so control changes or an invalid route cannot bypass geography.

After eligibility passes, family-specific weights rank valid states by the exposure HOI4 can represent: population density, agricultural state category, infrastructure and rail, supply nodes, ports and dockyards, air bases, radar and anti-air, industry, resources, capital status, prior disaster history, and wartime logistics. The physical registries are documented in `common/scripted_triggers/013_natural_disasters_geography_triggers.txt` and `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-11_event013_physical_geography_data_handoff.md`. Weights never substitute for a failed physical gate.

Geological disasters at regional severity or above can produce a delayed tsunami risk on a coast. Earthquakes otherwise favor aftershocks, volcanic eruptions favor lahars, and meteor impacts favor displacement pressure. The tsunami-prevention action can cancel a queued second wave before its job matures.

## Evolution behavior

### Baseline

Baseline random seasons draw earthquake, flood, extreme wind, thunderstorm, hailstorm, cold wave, heat wave, wildfire, and dry mass movement. They use local or severe impacts with distinct state targets and one aggregate sequence report per recipient, cause family-specific disruption and measured building damage where a building is present, and pass population losses to the shared Deaths system as the natural-disaster cause.

### Wider Disaster Seasons

This first evolution unlocks at Gathering Storm. It expands sequence length and adds tropical cyclone, blizzard, drought, dust and sandstorm, wet mass movement, volcanic eruption, and storm surge to the random pool. More warning and aftermath cards can compete for the fixed mission slots, making prioritization important even before regional spread is common.

### Regional Cascades

This second evolution unlocks at Rising Chaos. It adds tornado outbreak, ashfall, lahar, and tsunami to the normal random pool. It raises deaths, building damage, state-modifier duration, neighboring-state damage, supply disruption, famine, disease, refugee pressure, and recovery-score penalties. Regional and catastrophic impacts apply weaker but still persistent cards to neighboring valid states, whose consequences join the same sequence report for each eligible recipient alongside their own recovery work.

### Abnormal Paths

This third evolution unlocks at Chaos. It opens abnormal meteor showers, whole-earth rupture, massive eruption, moving storm and tornado corridors, multi-coast tsunami paths, and related severe chains. These can devastate several states or regions while remaining non-terminal. Automatic abnormal families observe a global cooldown. The manual Maximum Disaster Barrage may bypass that cooldown only for its call and does not record a natural third-evolution milestone.

## Damage, Deaths, and disruption

Population loss scales from state population, family lethality, severity, evolution, caller overrides, preparation, resilience, and a capped physical-vulnerability profile. Named candidates cover dense settlement, weak infrastructure, exposed coasts, strategic transport, air assets, agricultural districts, dry fuel, slopes and valleys, volcanic proximity, wartime logistics, unresolved devastation, failed warning, and repeated abnormal impacts. Each applicable candidate contributes its script-constant multiplier, the combined contribution is capped, and the highest-priority observed cause is persisted as the card's casualty-driver summary. The resulting deaths are removed from the state and registered through cause id 14 in the Deaths system.

`natural_disaster_last_deaths` remains the latest-impact value used by spike checks and impact-specific outcomes. Sequence reports store the actual returned death delta at each application and aggregate unique consequence receipts, while `natural_disaster_total_deaths` remains the card-level running total for live cards and abnormal history.

Building damage is distributed among the family's primary, secondary, and tertiary building types, then extended to transport, ports, airfields, industry, and resources where the family profile calls for them. The player-facing Damage line deliberately combines the family's impact signature with its primary damage profile instead of repeating those two closely related fields as separate rows. State disruption is stored in `natural_disaster_state_disruption`. Regional spillover uses `natural_disaster_neighbor_disruption`. Supply, supply impact, movement, attrition, repair, and resource penalties persist until recovery or expiry.

## Warnings and aftermath

The `Disaster Warnings and Aftermath` category is visible from the first accepted forecast through cleanup. Its state-targeted entries expose the affected state, family and broad hazard group, cumulative known deaths, strongest casualty driver, damage, disruption, warning result, recovery need, follow-up route, foreign-relief state, current phase, and relevant date. Warning and pending-impact cards show the scheduled impact date. Recovery cards show the next reassessment only after that value exists. Other states show a field-assessment message rather than formatting an unset date. The category's large cosmetic is selected dynamically from the highest-priority live state: abnormal cards outrank ordinary cards, active warnings outrank recovery work, and the stored family drives one mutually exclusive triggered-picture entry. All 25 families resolve to one of the existing disaster-specific cosmetic images. The overview appears only when relief remains visible without a live display state, and foreign relief uses the famine-and-displacement cosmetic. The separate `Foreign Relief` category is staged as well: inbound aid keeps it visible, while outbound aid requires a payable variant and a matching registered recipient card, so it does not open as an empty donor shell.

Warning actions are family-specific. Every one of the 25 families has three mutually exclusive preparations, for 75 named actions. The catalogue covers rail stand-downs, rolling-stock movement, port closures, shelter belts, lightning patrols, aircraft protection, fuel corridors, heated shelters, water points, firebreaks, slope watches, valley evacuation, exclusion zones, machinery covers, lahar and tsunami sirens, storm-surge road defenses, crater evacuation, lights-out sheltering, food corridors, and path rerouting. The chosen protection is persisted and appears on the aftermath card and abnormal map. Costs use manpower, support equipment, trucks, trains or convoys, fuel, Stability, Command Power, and civilian-factory capacity according to the preparation; holding exactly the displayed physical cost is sufficient.

After impact, missions advance through:

- early rescue, with three base slots and a fourth reinforced slot.
- middle stabilization, with two base slots and a third reinforced slot.
- late reconstruction, with two base slots and a third reinforced slot.
- one active chain-prevention mission.
- one active inbound-relief mission.
- one active outbound-relief operation per donor.

Capacity responds to country weakness, major-power resources, war, Evolution II pressure, active-card burden, incoming relief, and Maximum Barrage mobilization while remaining within the 4/3/3 hard caps. Each refill scores eligible states by severity, population, capital status, strategic transport, industry, coast, and chain risk, so the most exposed open card receives the next slot. Mission outcomes are full success, partial success, or failure. Partial reconstruction closes only after a cleanup reassessment and leaves a weaker recovery-strain modifier. Terminal failure strengthens disruption and schedules a family-conditioned follow-up or political shock, produces another affected-country report, and can disqualify response achievements. The failure guard resets for every new card, so repeated disasters in the same state retain the full failure contract. Closing a card releases ordinary and special mission slots in the same effect chain, clears temporary family pressure, removes heat overlap, updates the recovery catalogue, and refreshes the category.

The seven playable follow-up objectives are separate tsunami, disease, famine, wildfire-spread, supply-collapse, lahar, and aftershock missions. The queue draws an arrival inside the accepted family band, records the reserved due date, and gives the matching objective a deadline one day earlier. Tsunami evacuation uses trucks, convoys, manpower, and fuel. Disease prevention uses medical stores and vehicles. Famine prevention opens a train or convoy food corridor. Wildfire work funds firebreak patrols. Supply prevention holds a transport route. Lahar work clears valleys by road and rail. And aftershock work inspects priority structures. Full work cancels the chain. Partial work applies chain-specific human, material, and disruption multipliers before impact. Failure strengthens those same components before deaths and damage are calculated. Refugee and political chains remain visible consequences but do not consume the single objective slot, while a refugee-derived disease chain receives its own timed disease mission.

Foreign relief has neighboring convoy, port lifeline, engineer-column, and medical-column variants. All four draw affected countries from `global.natural_disaster_relief_recipient_countries`, a bounded country ledger updated only when an actionable recovery card opens, closes, or changes controller. Neighbor convoys can reach non-enemy neighbors, faction members, subjects, and same-continent recipients when the donor is a major. Port lifelines require a coastal recovery card and a faction, subject, or positive-opinion relationship. Positive opinion is the engine-supported cooperation gate used for Part 10's trade-partner direction, not a claim that an active resource trade is detected. Engineer columns from industrial majors or faction leaders can reach any non-enemy recipient whose card reports damaged transport or industry. Medical columns can reach non-enemy neighbors directly and faction, subject, or positive-opinion partners at longer range, while major or humanitarian-aligned donor eligibility remains in the resource gate. Each outbound package costs two physical stockpiles and 1% Stability, then reserves the donor's dispatch slot for 45 days; minimum War Support is an eligibility threshold. The recipient receives a targeted relief mission and, on arrival, temporary dependency pressure plus a gratitude opinion modifier. Each selected card records the visible lifecycle as no relief, pledged, route secured, arrived, misdirected, refused, or withdrawn. Abnormal history snapshots the same state. AI chooses actions from family, capital, population, transport, industry, war, chain, and severity priorities.

### Gods of Africa neighbor-relief adapter

`natural_disaster_offer_neighbor_relief_for_gods_of_africa` is an Event 013 scripted effect called in the African donor's country scope. The Event 012 caller supplies the regular country event target `gods_of_africa_protected_participant` and independently owns the Gods participant, generation, reliability, defiance, and focus-unlock gates. The adapter reads that one target, verifies that the recipient is in Event 013's bounded relief ledger, distinct from the donor, not at war with it, connected by the neighbor, faction, subject, or major same-continent route, in open aftermath, without inbound relief, and controlling a selectable live recovery card. It applies the existing `natural_disaster_can_offer_neighbor_relief` donor gate for minimum Stability and War Support, the dispatch lock, manpower, and convoys.

The adapter seeds the neighbor-convoy variant and unrestricted recovery phase, then calls `natural_disaster_select_priority_open_card`. Only a successful selection pays through `natural_disaster_pay_neighbor_relief`. The selected state receives the existing pledged status and physical route from `natural_disaster_set_inbound_relief_route_from_state`, and its controller receives the inbound state pointer, donor pointer, variant flag, and `natural_disaster_inbound_relief_mission`. A failed gate or empty selector leaves those effects unapplied and charges nothing. No constants or costs are introduced by the adapter; the targeted choice retains its AI weights and listed price while its visible wording reflects its full foreign-recipient scope.

Foreign-relief actions recheck donor affordability and the recipient card before payment. Inbound routing requires its recorded recovery card to remain selectable and exactly one recorded train or convoy route, together with manpower, Stability, and War Support; a stale card, conflicting route flags, or short stock fails before any partial payment. Outbound port, engineer, and medical dispatch selects an actionable recipient card again at completion, and reports an unserviceable forced dispatch without charging. Outbound packages use two physical stockpiles and Stability, then reserve the donor's relief dispatch slot for 45 days; War Support is an eligibility threshold and the timed lock adds no production penalty. Live mission outcomes and cost-boundary behavior remain unverified in game.

Neighbor relief displays manpower, convoys, and Stability; the outbound dispatch lock is described in the cost tooltip. The full `natural_disaster_can_offer_neighbor_relief` gate also checks recipient eligibility, minimum Stability and War Support, and the active dispatch lock. Its completion path selects a valid card before charging.

On success, the donor carries the hidden `natural_disaster_gods_of_africa_neighbor_relief_offered` flag for the Event 012 caller to check immediately after the effect returns, while the selected recipient carries `natural_disaster_gods_of_africa_neighbor_relief_active` to bind terminal cleanup to this bridge. The adapter clears an earlier donor receipt at entry. Event 013 clears both flags through `natural_disaster_clear_gods_of_africa_neighbor_relief_receipt` when the recipient refuses or the inbound mission completes, expires, cancels, or loses its selected state during a control transfer. The regular participant and priority-state event targets last only for the originating effect chain. Event 013's mission and abnormal-history cleanup remains independent, and this bridge does not cancel a disaster or alter its outcome.

## Black Friday prices

Every material cost of a warning, rescue, stabilization, chain-prevention, reconstruction, inbound-route, and foreign-relief action reads the Black Friday sale price table (Event 026).
The ordinary amounts stay in `natural_disaster_cost` and `natural_disaster_warning_cost`; each one is registered in `common/scripted_effects/026_black_friday_price_table_effects.txt` as `global.black_friday_price_natural_disaster_cost_<key>` or `global.black_friday_price_natural_disaster_warning_cost_<severity>_<resource>`.
Outside a sale each global equals the ordinary constant, and during a sale it holds the rounded-up sale price.
The affordability triggers, the payment effects and inline decision payments, and the cost texts all read that one global, so the shown price, the requirement, and the debit agree.
Material, Fuel and Command Power checks compare directly against the actual quote through `NOT` with a strict `<` comparison.
They do not subtract a unit from the fee, so fractional stocks cannot slip below the payment.
Stability payments compare against the exact positive quoted or constant-derived debit through `NOT = { has_stability < nd_cost_gate }`, with no epsilon gap.
The civilian-factory requirement of warning actions keeps its fixed `natural_disaster_warning_cost_gate` floor, because it is a capacity requirement rather than a payment.
The shared price table retains historical recovery Stability quote fields, but Event 013 rescue, stabilization and reconstruction no longer check or debit those prices.
Warning, chain-prevention and outbound-aid Stability deductions follow their quoted contracts. Recovery missions commit civilian production while active instead of charging a second Stability fee. Inbound routing spends manpower and its selected physical route, commits civilian production during delivery, and then carries the 365-day dependency at +2% consumer-goods factor and -0.10 daily political power. After successful delivery, it adds one slot to each rescue and stabilization capacity for 90 days and applies the selected aid effect. Outbound relief requires minimum War Support and reserves the donor's dispatch slot for 45 days without deducting War Support.
A paid action credits one Black Friday achievement family through `natural_disaster_credit_black_friday_purchase`: equipment when it pays support equipment or trucks, otherwise its trains or convoys.

## Abnormal disaster path map

`common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`, and `interface/013_natural_disasters.gfx` define the Evolution III/manual-abnormal map. Normal disasters remain in the aftermath category.

The active map combines every abnormal sequence visible to the current controller and first selects the highest-priority sequence by imminent impact, active warning, scheduled warning, chain risk, unresolved severity, and next due date. Within that selected sequence, up to five cards are rebuilt in ascending physical segment/arrival order so the path reads chronologically. Path-segment index breaks equal-urgency ties when choosing the sequence. Event Details opens a global Evolution III history view that remains available after cleanup and before the first abnormal path, where it shows a dormant monitor instead of disabling the button. Selecting a card shows the exact state, family, broad hazard group, severity, cumulative deaths, casualty driver, warning result, card phase, damage, foreign-relief state, follow-up, scheduled impact date and next reassessment. Six selectable milestones explain warning, schedule, impact, report, follow-up, and reassessment state, while the return control opens the selected controlled state's live aftermath work. Foreign and archived records remain read-only.

Abnormal history uses an aligned global record ledger rather than reading the affected state's current disaster variables. A state/sequence pair owns one record index. Live warning, impact, and recovery changes refresh only that matching row, while cleanup freezes its final status. Family group, cumulative deaths, casualty driver, and foreign-relief state have dedicated aligned snapshot arrays, so a later ordinary disaster cannot rewrite those fields or the archived family, severity, dates, recovery result, and path layer. If another abnormal sequence later crosses the same state, it appends a separate record, so both cards can appear together in history. Each country rebuild copies the selected records into aligned local view arrays with a globally unique rebuild pass, preventing one observer's sort markers from hiding records for another observer. The dormant view and every selected-row GUI trigger are guarded against missing array entries.

The live layers are rupture wave, meteor fall, eruption plume, tsunami train, and storm corridor. Their art is authored against the same five normalized segment anchors, so the selected sequence's segment index, state name, strategic region, next date, and warning state describe where its family-specific motion sheet is going next. Warning and impact card rims, the next-hit marker, and path layers use horizontal DDS frame sheets. Every animated sprite has an explicit static DDS fallback controlled by the Motion / Static button. GIFs exist only as review previews and are not referenced by gameplay.

The direct GUI geometry is kept explicit for interaction QA: the centered shell is 1080x744, the authored panel uses scale 1.43, disaster cards use 232x102 hit boxes, route markers use 64x64, sequence controls use 86x28, milestone controls use 48x48, path controls use 80x28, footer controls use 123x36, and the close control uses 32x33. These dimensions match the corrected source hitboxes and keep adjacent controls separated in the reviewed 1280x720, 1920x1080, and 2560x1440 layouts.

The selected-record panel keeps its severity, hazard, path, state, death, warning, disruption, relief, damage, recovery, and follow-up facts in a compact eleven-line summary so long state and damage values do not push recovery controls out of bounds. The path queue uses deliberate line breaks for ordered states, and the legend has room for all of its marker and timeline lines. The standard aftermath category uses mutually exclusive family pictures with a shared 114x101 frame, so a live family card remains identifiable at every supported UI scale.

## Super-events

Six researched, non-terminal super-event packages are reserved for rare abnormal milestones:

These packages feed the shared, general super-event presentation. They are not part of the Event 013 aftermath or abnormal-map UI surfaces.

- slot 67, `NO FIRM GROUND`, whole-earth rupture.
- slot 68, `ASH AT NOON`, massive eruption.
- slot 69, `THE BURNING FIRMAMENT`, meteor shower.
- slot 70, `THE FRETFUL ELEMENTS`, moving storm corridor.
- slot 71, `OLD STORIES CEASE TO BE INCREDIBLE`, first natural abnormal age.
- slot 72, `BELOW THE STONE`, delayed multi-coast tsunami chain.

The final quote, cultural-reference, image, and audio source decisions are recorded in:

- `docs/super_events/013_natural_disasters/archive/text_research.md`.
- `docs/super_events/013_natural_disasters/archive/audio_research.md`.
- `docs/super_events/013_natural_disasters/research_addendum.md`.
- `docs/super_events/013_natural_disasters/audio_production.md`.

Each slot has its own image sprite, audio id 37-42, music track, short sound variant, localisation, once-only gate, and same-sequence suppression.

## Achievements

The Event 013 achievement set is defined in `common/achievements/chaos_redux_achievements.txt` and uses sequence-bound ledgers rather than button counts:

- `All Clear, All Accounted For`: close every tracked card from a severe season without a failed deadline or abandonment.
- `The Tide Stops Here`: prevent a delayed geological tsunami before arrival or a major second death spike.
- `The Trains Came Through`: recover every tracked regional transport card without losing the capital supply route.
- `Bread Beneath the Ash`: recover every major ashfall state before famine matures.
- `No World Weather Office`: receive affected-country reports from four normal family groups without global-announcer policy.
- `Keep the Runways Lit`: endure a full meteor-shower sequence while the controlled capital, supply route, and airfield network remain operational.
- `Brace the Broken Earth`: recover the required whole-earth rupture regions before a major aftershock or delayed tsunami matures.
- `All Sirens at Once`: survive Maximum Disaster Barrage, preserve the capital route and a port or rail corridor, and close the required recovery cards before its deadline.
- `Every Cot Accounted For`: complete protection work for severe refugee pressure without the death, camp-disease, or border-camp failure gates.
- `An Atlas Bound in Dust`: fully reconstruct at least one card from every normal disaster family group.

Complete, grey, and not-eligible icon triplets live under `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.

## Cluster and scenario integration

Natural Disasters is repeatable cluster id 5. It contains five logical Event 013 season slots at Low, Low, Low, Low, and Medium severity. The first Low row is the required primary trigger row, while the other four rows retain independent eligibility, participation, ordering, runtime context, and history identity. Event 033 Acid Rain follows as the sixth optional Severe member and Event 051 Heat Wave follows as the seventh optional High member. A queue containing Acid Rain reserves its launch, and Event 33 resets major-event weights and the event timer only when it actually dispatches. Events 046 and 099 are not cluster members.

SCN-007 `Disaster Barrage` calls the same API once from the selected country. Its type choices are Random Barrage, Geological Crisis, Weather Crisis, Skyfall Crisis, and Full Catalogue. The launch control proves that the selected type has at least one compatible controlled state. Weighted misses then enter a complete type-preserving family pass. A same-chain rejection after confirmation opens an explicit Event 013 notice instead of silently scheduling nothing. The manual scenario carries a validated scenario-only evolution proof, so its selected intensity works before the corresponding natural evolution without unlocking or recording that evolution globally. Low, Medium, High, and Maximum scale sequence length, severity, aftermath policy, delay pressure, and abnormal access. Maximum alone opens abnormal families and the abnormal map. It remains non-terminal and never sets `world_end`.

## Gameplay and presentation files

- events: `events/013_natural_disasters.txt`.
- constants: `common/script_constants/013_natural_disasters_constants.txt`.
- effects and triggers: `common/scripted_effects/013_natural_disasters_effects.txt`, `common/scripted_triggers/013_natural_disasters_triggers.txt`.
- state modifiers: `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt`.
- decisions and categories: `common/decisions/013_natural_disasters_decisions.txt`, `common/decisions/categories/013_natural_disasters_categories.txt`.
- ideas and opinion modifiers: `common/ideas/013_natural_disasters_ideas.txt`, `common/opinion_modifiers/013_natural_disasters_opinion_modifiers.txt`.
- on-action hook: `common/on_actions/013_natural_disasters_on_actions.txt`.
- scripted GUI: `common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`.
- sprites: `interface/013_natural_disasters.gfx`, `interface/chaosx_super_events.gfx`, `interface/chaosx_achievements.gfx`.
- localisation: `localisation/english/013_natural_disasters_l_english.yml` and the shared event-log, scenario, achievement, Deaths, and music localisation files.
- scripted localisation: `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt` and shared Event Details selectors.
- catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- live asset registrations: `interface/013_natural_disasters.gfx`, `interface/chaosx_super_events.gfx`, and `interface/chaosx_achievements.gfx`.
- super-event audio provenance and uniqueness record: `docs/super_events/013_natural_disasters/audio_production.md`.

## Icon and sprite wiring

All Event 013 art uses stable sprite names. Runtime DDS files and registrations are the authoritative live wiring. The earlier retention record says `docs/assets/013_natural_disasters/` and its `manifest.md` preserved source, processed, provenance, prompt, and handoff material. That directory and manifest are absent in the reviewed worktree, and Git records deletion in `c008ec53f051add01f4c81ff8ce86b9fea668b1e`. The restoration claim and current archive availability remain unresolved. Runtime registrations are separate evidence and do not recover the missing source package.

Gameplay registrations are grouped as follows:

- aggregate country report: `GFX_report_event_nd_regional_aftermath`, reusing `gfx/event_pictures/013_natural_disasters/report_event_nd_regional_aftermath.dds` through `interface/013_natural_disasters.gfx`; the older family-report event definitions `.101–.125` are no longer used by normal dispatch.
- family news sprites `GFX_news_event_nd_*`: the same event-picture folder and GFX file.
- decision-category pictures `GFX_decision_cat_picture_nd_*`: `gfx/interface/decisions/013_natural_disasters/`, registered in the Event 013 GFX file.
- decision-category button icons `GFX_decision_category_nd_*`: the same decision folder and GFX file.
- response decision icons `GFX_decision_nd_*`: the same decision folder and GFX file.
- idea sprites `GFX_idea_013_disaster_aftermath`, `GFX_idea_013_refugee_pressure`, `GFX_idea_013_famine_pressure`, `GFX_idea_013_broken_infrastructure`, and `GFX_idea_013_disaster_recovery_mobilization`: `gfx/interface/ideas/013_natural_disasters/`.
- abnormal GUI statics `GFX_013_abnormal_disaster_panel`, `GFX_013_abnormal_disaster_panel_damaged`, `GFX_013_disaster_card_frame`, `GFX_013_map_marker_impact`, `GFX_013_map_marker_chain_risk`, `GFX_013_foreign_relief_badge`, `GFX_013_legend_report`, `GFX_013_legend_aftermath`, `GFX_013_legend_closed`, `GFX_013_legend_blocked`, `GFX_013_recovery_progress_frame`, and `GFX_013_recovery_progress_fill`: `interface/013_natural_disasters.gfx`.
- legend sprite sources are `gfx/interface/decisions/013_natural_disasters/decision_nd_observatory_watch.dds`, `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_aftermath.dds`, `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_recovery_mobilization.dds`, and `gfx/interface/decisions/013_natural_disasters/decision_nd_port_closure.dds` for report, aftermath, closed, and blocked states respectively.
- abnormal GUI animated/static pairs: `gfx/interface/animated/013_natural_disasters/`, registered in `interface/013_natural_disasters.gfx`.
- six super-event sprites `GFX_super_event_nd_*`: `gfx/super_events/013_natural_disasters/`, registered in `interface/chaosx_super_events.gfx`.
- ten achievement triplets: `gfx/achievements/`, registered in `interface/chaosx_achievements.gfx`.

## Balance notes

The numeric tuning source is `common/script_constants/013_natural_disasters_constants.txt`. Ordinary baseline disasters are intended to kill thousands to tens of thousands in exposed states. Regional Evolution II seasons can reach hundreds of thousands across multiple vulnerable states. Evolution III abnormal paths may produce multi-million aggregate loss when the family, state population, failed preparation, and failed recovery align.

The achievement thresholds deliberately require several recovered cards or operational routes. The major second-wave death spike is 100,000, the severe refugee death failure line is 50,000, the meteor-shower airfield network requires two controlled airfield states, whole-earth rupture recovery requires five cards, meteor survival requires four tracked hits, and Maximum Disaster Barrage requires ten fully reconstructed cards.

## Future plans

The retained proposals below have unresolved current acceptance and do not authorize implementation through this documentation cleanup.

- Add optional memorial and long-term rebuilding flavour after historically large but successfully closed disaster seasons without reopening gameplay cards.
- Expand regional target-fit data only when new state metadata can improve family selection without introducing world scans.
- Add any future abnormal visual family as a real source-frame package with its own static fallback and manifest entry.
- Keep Event 046 inactive, keep Event 051 separate, and keep Event 099's compatibility bridge routed through `call_natural_disaster` rather than restoring standalone sandstorm damage.
