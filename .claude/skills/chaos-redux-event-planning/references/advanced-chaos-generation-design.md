# Chaos generation and feedback standards

Read the relevant complete section before specifying an event that can materially change global Chaos.

## Chaos generation and feedback standard

Chaos is a measure of global instability, abnormality, and breakdown. It is not a moral score. A beneficial but impossible incident can raise Chaos because the world has become stranger and less predictable, while successful containment can lower Chaos because a destabilizing force has actually been pushed back.

Events must be active sources of Chaos, not only consumers of the current Chaos tier. The intended campaign loop is that higher Chaos makes events more severe and strange, then successful strange movements, concrete consequences produced by evolved behavior, failed containment, special Chaos countries, and other abnormal outcomes can push the Chaos Meter higher again. This feedback loop should be strong enough to matter without letting one repeatable action farm the campaign from calm conditions to World Collapse.

A genuinely strange, anomalous, violent, reality-breaking, extremist, supernatural, or system-disrupting event should normally create at least one positive Chaos source when its first meaningful manifestation occurs. Do not add Chaos merely because the random-event picker selected an event. The incident itself must have changed the world in a destabilizing or abnormal way.

Ordinary beneficial development should not raise Chaos just because it makes a country stronger. A factory program, normal military reform, ordinary election victory, or routine research success is not a Chaos source unless the event gives that success a wider destabilizing, anomalous, or threatening meaning.

### Required Chaos impact map

Every event that can materially destabilize the campaign must include a Chaos impact map in its specification. The coding agent should never have to invent the event's Chaos feedback during implementation.

Use a table or equivalent structured section with at least these fields:

| Milestone or outcome | Why global Chaos changes | Direction | Starting magnitude or band | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | --- | --- | --- | --- | --- |

Map the event from first manifestation through later success, spread, evolution-enabled consequences, containment, defeat, and aftermath. A large event may need many rows. A small event may need only a few.

If a genuinely strange or destabilizing event has no positive Chaos source, the spec must explain why. Do not omit Chaos simply because the event already uses Chaos as an evolution gate.

### Chaos source families to inspect

Actively look for Chaos sources in these event outcomes when they fit the event:

- first public or material manifestation of a strange incident
- an event-created movement reaching a meaningful support, organization, territorial, or institutional threshold. Peaceful success can still raise Chaos when it proves that the event-created movement has become a real new political or social force
- a movement winning a revolt, coup, election crisis, government struggle, or other route that materially expands the event's power or destabilizes the country or world
- creation, release, transformation, or public recognition of a special Chaos country
- a special Chaos country gaining meaningful territory, population, industry, subjects, allies, faction members, strategic capitals, or regional reach
- an abnormal actor defeating a major enemy, containment coalition, anti-event league, or other force that was holding it back
- a dangerous focus-route, decision-route, project, doctrine, technology, unit family, weapon, supernatural power, or special capability becoming operational
- spread into a new state group, strategic region, country, sea route, continent, or other meaningful geographic layer
- failed containment, missed crisis objectives, broken quarantine, collapsed negotiations, radicalization, mutiny, mass defection, or another event-specific failure
- a concrete consequence caused or intensified by an evolution, such as a new outbreak, spawned actor, territorial breakthrough, government transformation, destructive incident, capability actually entering use, or another material escalation
- a normal country adopting, sponsoring, weaponizing, legitimizing, or exporting an event-created abnormal system
- a new event-created faction, league, cult, military order, machine network, plague realm, supernatural authority, or other power structure reaching a meaningful milestone
- an event-to-event interaction or cluster combination creating a new level of instability beyond the ordinary effects of its member events
- a super-event-level reveal, irreversible transformation, or global escalation milestone
- progress toward an event-owned terminal state when that progress represents a real new loss of world order rather than a hidden bookkeeping threshold

Do not treat this list as a requirement to add every source to every event. Use the sources that represent real changes in the event's power, reach, or abnormality.

Evolution status is never itself a real change for Chaos accounting. Eligibility, MTTH completion, stage activation, evolution logging, unlocking a branch, or incrementing an evolution variable must have zero direct Chaos effect unless the same operation also causes a separate concrete outcome.

### Special Chaos country power growth

When an event creates or manages a country that counts as a special Chaos actor, its growth should feed the Chaos Meter through meaningful milestones. Do not let a supernatural, extremist, plague, death-state, machine, cannibal, anomalous, or other event-created Chaos country become a continental power while the meter reacts only to its initial creation.

Useful power milestones include:

- creation or transformation into the Chaos identity
- first durable territorial gain
- capture of an important capital, refuge, holy site, laboratory, industrial center, or event-specific strategic objective
- control of a meaningful territorial, population, industrial, or military band
- first subject, protectorate, faction partner, converted government, or foreign client
- first expansion into another region or continent
- defeat of a major opponent or organized containment bloc
- completion of a route that unlocks a much stronger army, special unit family, weapon, power, technology, or recruitment system
- transition from a local actor into a regional, continental, or global threat

Use thresholds and one-shot milestones. Do not award Chaos for every factory built, every division spawned, every daily population change, or every single state tick when several changes are part of one continuous expansion.

### Source sizing and scaling

Use the existing shared Chaos sources as calibration. Event-specific additions should normally use several readable milestones instead of one huge opening jump. Suggested starting bands are:

| Event-specific change | Starting Chaos band | Typical use |
| --- | ---: | --- |
| Local strange manifestation | `+2` | First meaningful appearance, small abnormal incident, first durable local success |
| Regional escalation | `+3` to `+5` | Movement breakthrough, new Chaos polity, failed containment, spread into another region |
| National or systemic power gain | `+10` to `+15` | Government capture, major Chaos-country growth, dangerous capability entering use, major consequence produced by evolved behavior |
| Major international or global escalation | `+20` to `+50` | Cross-continental spread, major-power collapse into the event, global reveal, near-terminal breakthrough |

These are planning anchors, not universal constants. Scale with the event's footprint, severity, actor strength, geographic reach, rarity, and existing generic Chaos consequences. Keep authored values easy to tune and use dynamic factors when the same milestone can occur at very different scales.

Current Chaos can influence an event-specific gain when it genuinely changes the severity of the outcome, but do not strongly multiply every gain by the current Chaos value. The event system already accelerates and evolves at higher Chaos, so aggressive direct multiplication can create an uncontrolled feedback spiral.

Do not use a giant event-specific Chaos grant merely to force the meter over `1000`. World-end readiness should emerge from accumulated campaign consequences and the owning terminal route's real prerequisites.

### Shared-source overlap and abnormal significance

The shared Chaos Meter already reacts to wars, annexations, puppeting, faction changes, ideology changes, nuclear use, world tension, military buildup, deaths, air contamination, and other global systems. Event planning must account for those existing sources.

Do not duplicate the same fact twice. If an event kills civilians and the Deaths system already converts those deaths into Chaos, do not add another event-specific gain whose only reason is the same deaths. If contamination already raises Chaos, do not repeat the contamination value as a separate event bonus.

An event-specific premium is valid when the same action has additional abnormal significance that the generic source does not measure. For example, annexation already has a generic Chaos effect. A supernatural Chaos country taking its first major capital can also receive a separate event-specific milestone because the abnormal actor itself has crossed a new power threshold. Those are two different causes and should be documented as such in the Chaos impact map.

Cluster incidents should follow the same rule. Member events keep their distinct Chaos sources, while a separate cluster-level Chaos source should exist only when the combined incident creates an additional destabilizing condition that the members do not already represent.

### Repetition, cooldowns, and anti-farming

Repeatable sources need explicit protection against farming. Use one or more of these patterns:

- one-time milestone flags
- first-time-per-region or first-time-per-continent rewards
- power-band thresholds
- cooldowns
- diminishing returns for repeated ordinary incidents
- stronger rewards only when a repeated event reaches a genuinely new severity or footprint
- caps on one event family's direct contribution over a short period

A repeatable event can still keep raising Chaos when each firing creates a real new crisis. Repetition alone should not be enough.

Do not require recurring whole-world scans merely to discover that a Chaos actor became stronger. Prefer event-owned actions, state-control changes, focus or decision completions, evolution-owned incidents that actually change the world, war outcomes, and bounded milestone checks that already occur when the relevant state changes.

### Evolutions and triggerable scenarios

Reaching, unlocking, activating, logging, or advancing an evolution must not add Chaos by itself. Evolution state only changes what the event is capable of doing. Chaos changes when an evolution causes a concrete world consequence, such as spread, conquest, a spawned actor, government capture, a destructive incident, failed containment, or a dangerous capability actually being used or becoming materially present. Attach the Chaos source to that consequence and guard it there.

If an evolution activates and only unlocks future focuses, decisions, AI behavior, incidents, or capabilities, Chaos remains unchanged until one of those unlocked paths produces a mapped destabilizing outcome. If the evolution activation event itself simultaneously causes a real world change, attribute Chaos to that real change, not to the abstract evolution stage.

A pre-fire evolved opening receives no extra Chaos merely for starting at a higher evolution stage. Its stronger opening can generate Chaos through the concrete incidents and outcomes that actually occur during that opening.

Triggerable scenarios already create instant Chaos from their setup controls. The spec should define how scenario type and intensity affect that initial amount when relevant. After setup, the resulting event actors and mechanics should continue to use the same normal Chaos impact map as automatic play. Manual launch must not suppress later movement victories, Chaos-country power milestones, evolution-enabled consequences, or containment reversals.

### Containment, defeat, and Chaos reduction

Events can lower Chaos when the player or AI materially reverses an event-created source of instability. Useful negative sources include:

- destroying or dissolving a special Chaos country
- defeating an event-created movement after it had established real power
- curing, sealing, banishing, dismantling, or permanently containing an abnormal system
- retaking a major event-specific objective from a Chaos actor
- breaking an event-created faction, cult, network, or weapon program that had become a major source of instability
- completing a durable peace or restoration outcome that actually reverses the event's destabilizing state

Do not automatically refund every point previously added. Deaths, destruction, contamination, political fragmentation, and other lasting consequences may remain. A containment reduction should represent the instability that has genuinely been removed.

### Handoff and completion requirements

The coding-agent prompt must require implementation of the complete Chaos impact map, including positive sources, negative sources, dynamic scaling, repeat guards, shared-source overlap, evolution-enabled consequence sources, and special Chaos-country power milestones.

The goal prompt must treat Chaos-source coverage as a pass or fail requirement for destabilizing events. A completed event should be able to show where its Chaos comes from across the full lifecycle, not only at the opening popup.
