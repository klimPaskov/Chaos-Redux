# Event 018 Resources Found Specification, Part 1

## Core event and baseline discovery

All names in this file are working labels for design structure. They are not final localisation.

## Event identity

Event 018 remains a **Minor Repeatable** event in the **Economy (pos)** cluster. Its cluster member severity is **Medium**. The ordinary event is a major economic opportunity rather than a disguised punishment. A country discovers that one valid state contains far more of one normal strategic resource than existing surveys indicated. The first visible consequence is a large deposit, new investment demand, and foreign trade interest.

The event can become dangerous through repeated development and its evolution tracks. The ordinary discovery should still feel desirable after the player knows that deeper branches exist. The event fails if the correct strategy is always to reject the deposit immediately. Safe exploitation, regulated growth, foreign partnership, national development, strategic militarisation, suspension, and closure must each be viable in different campaign situations.

The event’s central promise is a resource field that remembers what the world has done to it. It records what was found, who owns the state, who holds the contracts, how deeply the field was excavated, how many people were exposed, how much foreign pressure accumulated, and whether the underground was disturbed. Repeated firings should strengthen this persistent story instead of creating unrelated bonuses with no history.

## Player experience

The event should create the following sequence in ordinary play:

1. A survey, test shaft, drilling team, mine office, refinery crew, or local authority identifies an unexpectedly rich deposit.
2. The owner receives an immediate resource increase and a discovery popup focused on the state, the resource, and the people making the find usable.
3. A compact management category opens for that field. The player can appraise, develop, connect, regulate, concession, guard, suspend, or close the site.
4. Foreign countries react according to their need for the resource, access to the owner, proximity, rivalry, and war situation.
5. Repeated discoveries can enrich the same field, add another resource type to it, or create a new field elsewhere when no current site is the better target.
6. The field can mature into a stable economic asset, become a diplomatic prize, or enter an evolved excavation crisis.
7. The player can still decide that the deposit is too costly. Closing it removes only resources created by Event 018 and ends the site’s active chain.

This baseline must work as a complete event even when every evolution is disabled. It needs useful decisions, foreign reactions, ownership transfer behavior, event log detail, and a clean ending without relying on monsters.

## Discovery target selection

### Eligible owner

A discovery owner must be a living country that controls at least one valid state and can meaningfully use or trade strategic resources. The ordinary selection should favor countries participating in the active event system, but it should not require the selected country to be at peace or to be a major power.

Countries that cannot support the baseline economy should be excluded. This includes actual nonhuman countries whose economy does not use ordinary resources, terminal world-end actors, countries with no valid controlled state, and temporary administrative tags that the shared country classification marks as unsuitable for normal economic events.

### Eligible state

A valid state should satisfy all of the following design rules:

- It is owned and controlled by the selected country at discovery time.
- It is not impassable.
- It is not already reserved by an incompatible terminal mechanic.
- It can legally hold strategic resource additions.
- It has enough local population or industrial presence to support a survey and labor story, unless the selected discovery skin is an oil field, remote mine, or geological basin that justifies a sparse state.
- It is not the excluded starting state of an active cave country.
- It is not already closed by Event 018 unless a separate rediscovery rule deliberately reopens it, which the baseline design does not require.

State selection should be weighted rather than uniform. The weights should make the result feel plausible without becoming predictable.

Positive factors can include:

- existing infrastructure
- an existing resource of any type
- coastal access for oil or export-oriented discoveries
- mountains or hills for mineral discoveries
- plains and desert basins for oil or chromium-style geological skins
- existing civilian industry that can organize a development program
- a rail connection or nearby supply route
- an existing active Event 018 field that is eligible for enrichment

Negative factors can include:

- active combat
- severe devastation
- extremely low population where the selected presentation would make no sense
- no practical connection to the owner’s economy
- an unresolved state-level disaster that would make the discovery unreadable
- a recent field closure

The event must not hard-lock each resource type to one terrain. The resource is completely random. Terrain and geography control presentation weighting, not the actual random resource pool.

### Existing-field preference

When the event repeats, it should decide whether to enrich an existing active field or create a new one.

An existing field becomes more likely when:

- the owner is actively investing in it
- the field has strong transport and administration
- the owner chose deeper appraisal or surveying
- an evolution allows compound discoveries
- the field is already internationally important
- the state has not reached the event’s practical concentration cap

A new field becomes more likely when:

- the owner has no active field
- existing fields are suspended or under closure
- another country was selected
- the current field is already at its concentration cap
- the repeatable roll should distribute economic opportunity across the world

The event should support several active fields globally. A country can own more than one, but the user interface must keep the current field selected and avoid presenting every field’s actions at once.

## Resource selection and amount

### Resource pool

The discovered resource is selected from the full standard strategic-resource pool used by Hearts of Iron IV. The pool includes oil, aluminium, rubber, tungsten, steel, and chromium. No normal resource type is excluded merely because it is geographically unusual. The event premise is that previous surveys were wrong.

The selection should be truly random at the final roll. Context can influence the descriptive skin, appraisal method, and foreign reactions, but it must not silently replace the requested random resource rule with terrain-determined selection.

### Baseline deposit

The baseline discovery should add a large deposit centered around **100 units of production** of the selected resource. The practical design band is roughly 80 to 120 before scaling. A clean default target is 100.

The amount may vary through dynamic factors:

- ordinary first discovery stays near the baseline
- high chaos can increase variance
- superior survey preparation can increase the confirmed amount
- poor infrastructure can leave part of the deposit unexploited until development
- repeated discovery in the same field can add another full deposit
- the same resource can be rolled more than once and stack
- pre-fire evolved openings can add several independent deposit rolls

The event must record every Event 018 addition by resource type. It cannot rely on reading the state’s total resource value later, because the state may already have vanilla resources, other mod resources, or gains from other events. Closure and ownership transfer need the exact Event 018 contribution.

### Confirmed reserve and developed yield

The initial popup represents a confirmed reserve. The field’s management system distinguishes the reserve from the portion that the owner has made usable.

A simple baseline can place most of the 100 units directly on the state so the event delivers the promised immediate result. Development then adds temporary output efficiency, infrastructure, trade access, or a second tranche of event-owned resources. The player should not receive a popup promising 100 and then see only a token amount.

The design should keep two readable concepts:

- **Confirmed Reserve** is the total Event 018 resource addition known in the state.
- **Developed Yield** is how much of that reserve the owner can exploit efficiently through roads, shafts, wells, pumping, sorting, refining, and administration.

Confirmed Reserve is mostly geological. Developed Yield is political and industrial. Closing the site removes the Event 018 reserve itself. Suspending the site keeps the reserve but suppresses development benefits and disturbance growth.

## The discovery popup

The first popup should identify:

- the owning country
- the selected state
- the selected resource
- the approximate scale of the find
- the discovery method appropriate to the resource and region
- the immediate economic interest
- the first public choice about administration

The text direction should remain practical and optimistic. Workers, surveyors, drilling crews, geologists, local officials, or railway engineers should be the viewpoint. Do not mention hidden monsters, future world-end mechanics, subterranean disturbance, or an ominous warning label.

The popup option family should represent administrative posture rather than a one-time accept or reject switch.

### State-led development posture

The owner places the field under a national authority, mining office, petroleum board, wartime ministry, or public works administration. This posture favors national control, direct investment, local infrastructure, and stronger resistance to foreign pressure. It requires more domestic civilian capacity and administrative effort.

### Licensed private development posture

The owner grants domestic firms broad rights to open the field. This posture develops quickly, uses less direct state capacity, and increases commercial activity. It also raises labor pressure, smuggling risk, and difficulty of enforcing later closure.

### Foreign concession posture

The owner invites a foreign consortium or a selected strategic partner. This posture accelerates extraction, supplies machinery, creates trade ties, and can improve relations. It also transfers influence, creates compensation claims, and makes later nationalization or closure diplomatically costly.

### Cautious appraisal posture

The owner confirms the discovery but limits early excavation. This posture gives a smaller immediate development benefit, improves safety, reduces foreign pressure, and preserves the option to close cleanly. It is attractive for weak countries, countries already fighting a large war, and players who value low risk.

These are posture directions, not final option labels. The implementation can use one opening option followed by decisions if four popup options would create clutter. The player must still choose a posture early enough that the field develops a distinct identity.

## Persistent field identity

Each active field needs a persistent record tied to its state. That record should survive:

- repeatable discoveries
- changes of owner
- changes of controller
- temporary occupation
- concession agreements
- demilitarization
- suspension
- partial development
- evolution changes

The record ends when:

- the field is permanently closed and all Event 018 resources are removed
- the state becomes the starting state of the cave country and the field is converted into the cave origin package
- the world-end branch replaces the ordinary field rules
- the state becomes invalid through an engine-level change that requires explicit cleanup

The field identity should have a stable sequence or field number for history and debugging. Player-facing text should prioritize the state name and resource composition instead of exposing internal numbering.

## Baseline stages

Baseline stages are ordinary lifecycle states. They are not logged as evolutions.

### Stage 1: Discovery

The owner receives the deposit and the initial popup. The management category opens. Foreign countries begin calculating interest. The field has low Excavation Depth and low Foreign Pressure unless the opening posture creates immediate involvement.

The player’s first tasks are to choose administration, commission a fuller survey, and decide whether transport or security comes first.

### Stage 2: Appraisal

The owner confirms reserve quality, maps the field, identifies access routes, and learns whether the deposit is concentrated or spread across the state. Appraisal can reveal a second lode, a deeper seam, a connected oil structure, or poor-quality material that requires more processing.

Appraisal is active play. It can require civilian factory commitment, construction time, trains, trucks, fuel, engineering capacity, or temporary production disruption. A successful appraisal improves development options and reduces the chance of wasteful investment. Aggressive appraisal increases Excavation Depth faster.

### Stage 3: Development

The owner opens shafts, wells, processing facilities, depots, roads, rail spurs, and company housing. The state begins generating stronger economic value. Local employment rises. Trade partners can sign contracts. Smuggling and espionage become possible.

Development is where the field becomes strategically visible. A country that refuses all development still keeps the discovered deposit, but it does not gain the full trade, construction, or industrial advantages.

### Stage 4: Rush

A rush begins when the owner, companies, or foreign partners push extraction faster than administration and safety can keep pace. The rush is not automatically supernatural. It represents labor shortages, inflated prices, transport congestion, corruption, dangerous shifts, theft, and political pressure.

The player can embrace the rush, regulate it, or end it. Embracing it gives a strong short-term yield. Regulation costs equipment and industry but improves safety and long-term value. Ending it reduces output temporarily and can anger concession holders.

### Stage 5: Mature field

A mature field has completed its main infrastructure and settled into one of several stable forms:

- nationally controlled strategic field
- regulated commercial field
- foreign concession zone
- internationally supervised field
- militarized wartime field
- suspended reserve

A mature field still reacts to repeated discoveries, wars, occupation, evolution changes, and trade shocks. It is not a permanent passive modifier with no further decisions.

### Stage 6: Closure

Closure is a deliberate project, not a single cheap button. It removes the Event 018 resource additions, ends development benefits, terminates active decisions, settles or breaks contracts, moves workers, and seals or dismantles the site.

Baseline closure can be motivated by exhausted administration, military danger, foreign pressure, environmental damage, or player preference. It should be expensive enough that the player does not use closure to erase every minor inconvenience, but it must remain attainable.

Closure before Evolution II is mostly an economic decision. Closure during Evolution II or III becomes a safety and survival project with stronger requirements.

## Baseline management values

The field uses four visible values before the supernatural layer is public.

### Developed Yield

Developed Yield measures extraction capacity, transport, processing, and administrative control. It rises through infrastructure, machinery, labor organization, foreign investment, and technical programs. It falls through occupation, sabotage, suspension, strikes, severe accidents, and closure.

High Developed Yield increases economic benefit and makes the field more attractive to foreign powers. It can also increase Excavation Depth when the owner pursues deeper seams.

### Excavation Depth

Excavation Depth measures how aggressively the owner is extending shafts, wells, galleries, tunnels, and survey works. It is a visible industrial measure. It does not initially claim that anything supernatural exists.

Depth rises through deep survey, maximum extraction, repeated deposit rolls, military exploitation, and unsafe night shifts. It falls slowly through suspension and substantially through sealing work. High depth unlocks richer development and increases evolution exposure.

### Workforce Safety

Workforce Safety measures ventilation, medical supervision, supports, equipment quality, shift length, evacuation planning, and regulatory authority. High safety reduces ordinary accidents and later population loss. Low safety accelerates the rush and lowers costs, but creates visible casualties and instability.

Safety should be capable of real improvement. The event must not punish the player identically after they invest heavily in protection.

### Foreign Pressure

Foreign Pressure measures contract demands, espionage, diplomatic bargaining, smuggling, military attention, and border tension generated by the field. It rises when the resource is scarce, the owner is weak, concessions overlap, nearby rivals have claims, or the world is at war.

Foreign Pressure falls through stable contracts, adequate exports, national deterrence, neutral administration, demilitarization, successful counterintelligence, and reduced strategic need.

These values need consistent color identities and integer-style display. The user interface should also show plain-language bands such as Low, Managed, High, and Critical.

## Economic outcomes

The field’s baseline benefits should be meaningful and layered.

### Direct resource production

The state gains the event-owned resource deposit. This is the primary reward and must remain visible on the map.

### Local development

Investment can improve infrastructure, construction capacity, rail access, supply, and selected buildings in the field state. The exact package should depend on the resource and geography. An oil field may prioritize infrastructure, fuel handling, and export access. A mineral field may prioritize rail, processing, and industrial capacity. Rubber can use plantations, laboratories, collection networks, or synthetic processing depending on the presentation skin.

### National economic benefit

A developed field can give a temporary or staged national benefit tied to actual development. Appropriate effects include construction speed in the state, trade-deal opinion, reduced resource-to-market friction, civilian construction support, or a resource authority spirit with a lifecycle.

The event should not use a pile of tiny national modifiers. One or two staged institutions are better than many passive bonuses.

### Trade benefit

Contracts create political relations, access, and economic commitments. A foreign buyer should gain a reason to protect the route. The owner should gain a reason to maintain exports. Breaking the contract should matter.

### Local costs

Rapid development can strain housing, food, transport, policing, and public administration. These are not meant to erase the positive event. They create decisions and tradeoffs around the rush.

## Repeatable behavior

Each firing should choose one of three broad results after owner and state selection:

### New field discovery

A valid state with no active field receives a new deposit and begins the baseline chain.

### Existing field enrichment

An active field receives another independent random resource roll. If the result matches an existing event-owned resource, the amount stacks. If it differs, the field becomes multi-resource.

The owner receives a follow-up popup focused on the new geological result, revised transport demands, and foreign interest. The field should not replay the full first-discovery tutorial.

### Survey breakthrough

An actively appraised field receives a larger confirmed reserve, a development efficiency gain, or a special opportunity such as a deeper seam, offshore extension, connected basin, or secondary ore body. This result can be used when the state is near the practical resource concentration cap.

Repeatable firings must update event history and field detail. They should also increment the field’s discovery count. That count helps determine evolution preconditions and future opening strength.

## Occupation and ownership change

A resource field is attached to land, but contracts and institutions are attached to countries. The design needs clear separation.

### Temporary occupation

An occupier can exploit a limited share of the field, guard it, sabotage it, or prepare seizure. The legal owner retains its claims and contract history. Developed Yield may fall while the front disrupts infrastructure.

### State transfer in peace

The new owner inherits the Event 018 resource additions and the physical field. It does not automatically inherit every political benefit. Existing foreign concessions can continue, be renegotiated, or be expropriated. The former owner can retain compensation claims or receive a settlement.

### Border-war transfer

A border-war defeat transfers the field state only when the designed dispute flow reaches that outcome. The winner inherits the physical field, current damage, and foreign pressure. The loser receives an aftermath choice around recognition, compensation, sabotage, or escalation.

### Annexation or country removal

If the owner disappears, the current state owner receives the physical field. Global targets, contracts, selected-field records, and stale decisions must be cleaned up or reassigned.

## Clean endings

The baseline chain can end in several healthy states without evolutions.

### Stabilized national field

The owner has high safety, manageable depth, strong domestic administration, and low foreign pressure. The field remains a valuable state asset with occasional maintenance and trade events.

### Stable concession field

A foreign partner supplies machinery and buys output. The owner gains development and diplomacy, while accepting influence and compensation obligations.

### Neutral commission field

The field becomes supervised and partially demilitarized after a serious international dispute. It remains productive, but military use and unilateral contract changes are restricted.

### Strategic reserve

The owner suspends most extraction and preserves the deposit for later use. This reduces immediate benefit and foreign pressure while retaining the resources on the state at reduced development efficiency.

### Permanently closed field

The owner completes closure, removes Event 018 resource additions, resolves workers and contracts, and marks the state ineligible for ordinary Event 018 rediscovery. This ending must be mechanically clean and respected by every future evolution check.

## Event log and detail direction

The Events tab detail should describe an unexpectedly rich strategic-resource discovery that can become a center of development, trade, and foreign competition. It must not list exact modifiers or reveal the cave branch.

History entries should record the state, resource, owning country, and whether the firing created a new field or enriched an existing one.

The field detail view should show:

- current owner and controller
- state name
- discovered resource composition
- discovery count
- administration posture
- lifecycle stage
- Developed Yield band
- Excavation Depth band
- Workforce Safety band
- Foreign Pressure band
- active contracts or commission status
- current closure or suspension status

Evolution entries belong in the shared evolution log and are specified in Part 4. Ordinary baseline stages must not be logged as evolutions.

## Baseline acceptance standard

The baseline is complete only when a player can experience the entire discovery, appraisal, development, trade, rush, stabilization, suspension, ownership-transfer, and closure loop with evolutions disabled. The event must remain economically desirable, repeatable without duplication errors, readable in the event log, usable by AI, and capable of cleanly removing only its own state resource additions.
