# Event 58: Integration, presentation, and balance

## Result accounting

The resolver keeps a temporary transaction ledger long enough to support reports, event logs, achievements, and owner callbacks.

The transaction records:

- frozen world-state count
- active evolution layers
- successful baseline placements
- successful Evolution I placements
- successful Evolution II packages
- provinces changed by multi-province packages
- successful Evolution III placements
- exhausted states by layer
- invalid provider and failed callback counts for debug evidence
- result counts by stable display family
- rare and exceptional recipient locations
- per-human-country summaries for states owned and controlled at transaction start

Only evolution milestones, achievement progress, owner-system state, and other facts that remain useful after the report should persist.

The event should not retain a permanent per-state history of every ordinary infrastructure or air-base level. That would enlarge saves without creating player value.

## Human player report

Every human player receives one report event through the project's global multiplayer event-copy pattern.

The report uses the player's country at the start of the transaction. A tag switch after the transaction starts cannot redirect the result summary or achievement credit.

The main text establishes the world event. A concise dynamic result block summarizes the player's territory.

The result block should normally show:

- total state-level construction received
- total province packages received
- any exceptional structure placed in player territory
- whether some states had no available room

It can identify a small number of notable rare structures by state name. It should not print a complete state ledger, a row of internal counters, raw risk bands, registry IDs, or exact random weights.

A player with no controlled land can still receive the world report without a fabricated national result.

## Event log

Random Buildings receives one normal Event History row per firing.

The event has no single responsible country. Its default actor should use the project's global or actorless presentation. The country whose timer selected the event must not supply a flag.

The history detail should retain a compact outcome summary:

- world states processed
- total results by active layer
- total exhausted states by layer
- number of exceptional structures
- Chaos tier at firing

The history detail should not preserve every ordinary state result.

The event must appear in the Events catalog view with:

- ID `58`
- Random Buildings name mapping
- Minor Repeatable type
- Chaos level `1`
- live weight and fired count
- enabled state
- Positive Economy cluster membership

The event should remain disabled by default until the rework is implemented, wired, audited, and ready for normal selection. The implementation pass that makes it ready should add ID `58` to the reworked-event default allowlist.

## Event Details

Event Details describes the premise and omits the building table and exact probabilities.

The premise direction should cover:

- structures appearing across every region
- independent local outcomes
- ordinary construction at low Chaos
- increasingly unusual state, province, and exceptional construction at higher Chaos

Evolution previews should explain the visible change in scope:

- Evolution I expands the state-building pool and adds another state-level result
- Evolution II spreads construction across borders, coasts, railways, ports, and supply nodes
- Evolution III creates a limited number of exceptional structures in valid locations

The detail text must not expose internal registry fields, fallback order, owner callbacks, probability bands, debug reasons, or future secret providers.

## Evolution log coverage

Each evolution uses the shared evolution log with Event ID `58`.

The log should show the first successful activation date, tier, and stage. It does not need a country actor because the layer is global.

Evolution I, II, and III need distinct display identities. Their Event Details previews are catalog entries, while the Evolutions tab and History-related view are actual logged milestones.

Disabled evolutions do not place construction, record an evolution entry, set a recorded flag, award an evolution achievement condition, or contribute the layer's Event 58 Chaos milestone.

## Localisation direction

Final player-facing text should use concrete construction imagery and simple language.

### Root event

The description should show cranes, poured concrete, rail work, factory machinery, military installations, or other visible construction appearing in places that did not commission it. It should emphasize that each region received something different.

The cause remains unknown. The text should not build mystery through a staged contrast between witnesses and officials. It should describe what people can see.

### Option

The acknowledgement should use dry bewilderment, restrained sarcasm, or administrative resignation. It should remain short enough for the report-event button.

### Evolution I

The direction is specialized and advanced construction appearing among ordinary development. Avoid a technology list in the prose.

### Evolution II

The direction is construction spreading through the physical landscape, including borders, coasts, rail corridors, ports, and supply routes.

### Evolution III

The direction is a small number of enormous or highly restricted structures appearing at sites that can support them. Avoid calling the layer apocalyptic or world-ending.

### Tooltips and summaries

Tooltips can state exact player-country counts and named notable states. They should lead with the result, then explain any exhausted-state reason concisely.

Do not expose raw Clausewitz triggers, internal provider IDs, debug labels, or long candidate lists.

## Visual direction

Random Buildings needs one generated report-event image.

The image should show a 1936 to 1945 period landscape undergoing several kinds of construction at once. A useful composition can include railway workers, cranes, concrete defenses, a radar mast, an airfield edge, and a factory skyline. One coherent place is stronger than a collage of unrelated panels.

The image should feel like a period press photograph or documentary still. It should avoid modern cranes, safety equipment, vehicles, road markings, glass towers, readable signs, map overlays, blueprints covering the frame, or a generic conference room.

The final report image follows the project's report-event processing, sprite registration, manifest, and DDS rules.

The achievement set needs three original completed icons and their required grey and not-eligible variants. Building and facility providers keep their own building icons, map entities, and other assets. Event 58 does not duplicate them.

## Balance purpose

One building per state is already a major permanent world grant. Balance should come from composition, capacity, rarity, and repeatable-event pacing. Keep the core promise intact.

The baseline should produce a broad but controlled development wave. Infrastructure, air support, detection, state defense, and fuel storage should dominate. Factories and dockyards should remain a minority.

Evolution I adds volume first and unusual structures second. Most states still receive an ordinary second building. Advanced and rare entries remain visible at world scale without filling every country with reactors or severe institutions.

Evolution II is powerful because one state result can affect several provinces. One fort level per relevant province is sufficient for one firing. Railway, port, and supply packages should not include free equipment or broad national modifiers.

Evolution III uses a strict world budget and owner uniqueness. It must remain the smallest layer by count.

## Expected world impact

Probability audits should check the actual installed state count and candidate pool, but the intended effect of one baseline firing is:

- most states gain transport, air, detection, defense, or storage capacity
- a smaller group gain civilian, military, naval, or synthetic industry
- a very small group gain restricted special structures

At `200+`, the total number of state-building changes nearly doubles, but unusual buildings remain a small part of the added layer.

At `400+`, province packages become the main source of map-visible strategic change.

At `600+`, only a limited exceptional set appears worldwide.

## Anti-snowball safeguards

The event affects every country, so it does not directly target the strongest power. Large countries gain more total construction because they own more states. This is inherent in the premise and should not be hidden.

The design limits snowballing through:

- independent state rolls with no economy-scaled country grants
- factory and dockyard minority weights
- normal building caps and slots
- no free equipment, manpower, research, projects, or production lines
- rare-band protection
- low exceptional budget
- repeatable weight-cap reduction after every firing
- increasing saturation on later firings
- no country choice that lets a player optimize every result

Do not add a compensating penalty to large countries. That would change the event from random world construction into a balance correction system.

## Exploit safeguards

Implementation must prevent:

- reloading a player-facing option to roll construction again
- firing the hidden resolver separately from the registered event transaction
- achievement credit from force-trigger or debug routes
- repeated owner callback registration for one placed special structure
- factory placement without a free slot
- province package duplication inside one state
- exceptional budget reuse after a failed placement
- one exceptional location receiving several structures in the same firing
- a camp or facility being registered twice
- higher-risk fallback when safer bands are empty
- a disabled evolution setting its recorded flag
- a zero-result transaction consuming repeatable weight
- stale human-country summaries after tag switching

## Special-country integration

Random Buildings affects states held by special Chaos actors unless an individual provider excludes them.

The shared country classifiers should be used narrowly:

- `uses_normal_civilian_systems` can gate civilian-only structures
- `is_actual_nonhuman_country` can help an owner block incompatible institutions
- `is_special_chaos_country` can support a provider's special routing or responsibility rule

The event must not create another private copy of these shared classifiers.

A special country can still receive infrastructure, air bases, state anti-air, radar, fuel storage, military industry, forts, railways, or other valid structures.

## Camp and repression integration

Camp buildings are real camp-system instances.

The camp owner decides:

- site type
- active or dormant state
- responsible actor
- population processing
- evidence
- discovery
- condemnation
- death registration
- inspection
- capture
- reform
- dismantling
- cleanup

Event 58 contributes only placement provenance and its own result reporting. It does not call population-loss effects, condemnation effects, or camp-processing loops directly.

Concentration camps belong to the baseline restricted band. Extermination camps and gulag networks belong to Evolution I only when their owner explicitly registers them there.

## Scientific and facility integration

Reactors, heavy-water sites, civilian nuclear buildings, rocket sites, special-project facilities, and research structures remain owner-controlled.

Random Buildings does not grant a technology merely because it places a building. It does not count Gift from Scientists, Brilliant Scientist, Alien Technology in Antarctica, or another source event as fired.

An owner can require a compatible technology, provide an anomalous no-tech initialization, or disable Event 58 access entirely.

## Natural disaster and damage integration

Event 58 creates buildings at full normal condition unless the owner entry defines another normal initial state.

Natural disasters, bombing, demolition, state transfer, wasteland conversion, and other systems can later damage or remove them through their normal rules.

The event does not protect its buildings from future damage and does not automatically rebuild an Event 58 structure that is destroyed.

## Infrastructure-project interaction

Event 55, The Great Infrastructure Project, and Event 58 can affect some of the same physical systems.

Random Buildings remains random and immediate. It does not open project decisions or count a Great Infrastructure Project as completed.

A railway, port, dam, bridge, tunnel, corridor, or other structure owned by Event 55 can join Event 58 only through an explicit provider entry that defines whether a random completed instance makes sense.

## Gift from Scientists interaction

Event 54 can grant technology. Event 58 can grant a building.

Neither event marks the other as fired. A technology granted by Event 54 can make a provider valid on a later Event 58 firing. A building granted by Event 58 does not automatically grant its normal research prerequisite.

## Future building integration rules

A future building owner chooses the lowest layer where the structure remains safe and understandable.

### Baseline ordinary state construction

Use for common permanent state development with simple placement and no rare owner lifecycle.

### Evolution I expanded state construction

Use for advanced, unusual, restricted, or powerful state structures that should remain uncommon.

### Evolution II provincial construction

Use for buildings or compound packages whose meaning depends on exact province geography, adjacency, coastline, rail, or supply.

### Evolution III exceptional construction

Use for scarce, unique, landmark, facility, dam, or site-specific structures with narrow locations and complete owner lifecycle.

The owner must provide the adapter, display family, probability band, validity, capacity, placement, initialization, uniqueness, and cleanup ownership.

Adding a new provider should not require rewriting the Event 58 root event. A genuinely new selection model can justify a registry extension, but one event's private lifecycle does not belong in the shared selector.

## Documentation and catalog alignment

Implementation must create or update the Event 58 documentation under the current `docs/events/` convention and keep it aligned with the accepted spec.

The authoritative event catalog workbook must replace the stale ID `58` entry with Random Buildings and fill:

- name
- premise details
- Evolution I details
- Evolution II details
- Evolution III details
- Minor Repeatable type
- Chaos level `1`
- Cluster ID `7`
- Medium member severity
- final implementation status supported by evidence

The Positive Economy cluster row must add member ID `58` and update its player-facing details to cover random worldwide construction without removing Event 18.

After the workbook is saved, the exporter must regenerate all three CSV snapshots. The CSV files must not be edited directly.

## Completion evidence direction

A complete implementation needs evidence for:

- event registration and repeatable behavior
- global transaction membership
- every evolution layer
- risk-band fallback
- building caps and shared slots
- special owner callbacks
- province geography
- railway and supply graph safety
- exceptional allocation and uniqueness
- multiplayer reports
- event logs and Event Details
- evolution toggles
- Chaos milestones and no double counting
- Positive Economy cluster behavior
- achievements
- assets
- localisation
- docs and workbook alignment
- probability before-and-after comparison
- event-chain MCP inspection and comparison
- final completion audit

The implementation report must list any unsupported provider, map operation, building type, DLC path, or owner callback. It cannot silently substitute another reward.
