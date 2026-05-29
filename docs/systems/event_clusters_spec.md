# Chaos Redux Event Cluster System Prompt

Implement an event cluster system for Chaos Redux.

Follow `AGENTS.md`, the `chaos-redux-events` skill, and the relevant event-system, UI, localisation, documentation, and spreadsheet rules. Do not use fallback behavior, simplified versions, or placeholder logic. Keep iterating until the event cluster system is fully implemented and wired into the existing Chaos Redux event framework.

## Goal

Add event clusters as a new layer above individual random events.

An event cluster represents a linked group of events that can fire together as one broader incident, cascade, crisis, or thematic sequence.

Instead of always firing a single selected event, the event system should sometimes fire a cluster. When a cluster fires, all events inside that cluster are treated as fired for weighting purposes, and the player should be able to inspect the cluster through the event log and settings UI.

Clusters should make Chaos Redux feel more connected. Related events should be able to arrive as a combined wave rather than always appearing as isolated events.

## 1. Core concept

A cluster is a hidden grouping of existing events.

If an event belongs to a cluster, then when that event would be selected, there should be a chance that the whole cluster fires instead of only that one event.

The cluster should not replace the normal event system. It should sit on top of it.

Basic behavior:

- event selection works normally first
- if the selected event belongs to one or more clusters, the system checks whether a cluster should fire
- if the cluster roll fails, the original event fires normally
- if the cluster roll succeeds, the cluster fires instead
- the triggering event is processed as part of the cluster unless it has become invalid before firing
- the cluster checks each member event's own eligibility before processing it
- the cluster may skip optional member events based on chaos tier, validity, cooldown, and participation chance
- firing or processing a member event updates that event's weight as if it had individually fired

## 2. Cluster chance, member chance, and chaos scaling

There are two different chances:

1. **Cluster roll chance**: the chance that the selected event turns into a cluster firing instead of firing alone.
2. **Member participation chance**: the chance that an eligible optional member event fires when the cluster fires.

Cluster roll chance should start low and increase as the Chaos Meter rises.

Design intent:

- Calm World: clusters that are not unlocked show 0% roll chance
- Gathering Storm: clusters are possible but uncommon
- Rising Chaos: clusters become noticeable
- Chaos Tier: clusters become a real risk
- Totalen Chaos: clusters become much more likely
- World Collapse: same as in totalen chaos

Member participation chance is controlled per event inside the cluster.

Rules:

- required member events fire when valid
- optional member events roll separately when the cluster fires
- more dangerous optional events should usually have lower participation chance than safer events
- eligible optional member events should not be weighted so low that they almost never appear
- default minimum participation chance for an eligible optional member event should be 50%, unless a cluster definition gives a clear reason to block or gate it
- the event that caused the cluster roll should be treated as required for that firing, unless it becomes invalid during cluster setup

Use existing Chaos Redux chaos tier logic where appropriate. Values can be tuned, but the distinction between cluster roll chance and member participation chance must remain clear.

## 3. Event weight and pacing behavior when a cluster fires

When a cluster fires, every member event inside the cluster should update its own fired state and post-fire availability as though that event had fired normally.

The cluster itself, not each child member, should update global pacing. A fired cluster counts as one event for timer compression and major-event weight growth/reset behavior, no matter how many member events fire inside it.

Required behavior:

### Fire-once events

If a fire-once event is inside a fired cluster, its weight should go to `0` permanently, just as if it had fired by itself.

It should not be able to fire again later.

### Repeatable events

If a repeatable event is inside a fired cluster, it should apply its own repeatable-event fired behavior.

It should still be able to recover weight later, but only up to the reduced cap that would normally apply after firing.

### Major events

If major events are allowed inside clusters, define the rules clearly.

Preferred behavior:

- major events should only be placed in clusters intentionally
- major-event cluster behavior must respect existing major event reset rules once at the cluster level

Do not let clusters bypass major-event pacing or multiply major-event pacing by member count.

## 4. Repeatable clusters

Clusters themselves can be either one-time or repeatable.

A repeatable cluster should be able to fire more than once if at least some of its events are repeatable or otherwise still valid.

Rules for repeatable clusters:

- repeatable clusters can fire again after cooldown or weight recovery
- they should not endlessly spam
- they should respect event weight state for member events
- if all member events are unavailable, the cluster should not fire
- if only some member events remain valid, the cluster can either fire only valid members or be blocked, depending on the cluster definition

Make the system flexible enough to support both one-time clusters and repeatable clusters.

## 5. Cluster membership rules

Create a clear way to define which events belong to a cluster.

A cluster should have:

- a stable cluster ID
- player-facing name
- short description
- member event IDs
- cluster type, such as one-time or repeatable
- base cluster roll chance or chance profile
- chaos scaling behavior
- optional cooldown or gating rules
- optional cluster-specific trigger rules
- optional event ordering rules

Each member event should be able to define:

- member event ID
- whether it is required or optional when the cluster fires
- member participation chance if optional
- minimum chaos tier to appear inside the cluster
- danger level, such as low, medium, high, or severe
- cluster order, usually from least dangerous to most dangerous
- optional member-specific trigger rules
- skip behavior if the event is unavailable, exhausted, disabled, or blocked by its own chaos requirement

Cluster unlock and member event eligibility are separate.

A cluster can become available at one chaos tier while some member events only become eligible later. If a member event requires a higher chaos tier than the current world state, it should be skipped for that cluster firing unless the cluster definition explicitly says otherwise.

The system should be easy to extend with new clusters later.

Do not hardcode everything in one-off logic that only works for the first cluster.

## 6. Cluster firing behavior

When a cluster fires, it should not feel like a random technical dump of events.

Decide how the player experiences it.

Preferred behavior:

- show a cluster-facing popup or log entry first
- then fire or queue member events in a controlled order
- order member events from least dangerous to more dangerous unless the cluster defines a stronger narrative order
- roll optional member events before presentation so the cluster log can show what happened and what was skipped
- avoid overwhelming the player with too many popups at once
- keep the cluster readable in logs
- make sure event details remain accessible for each member event

If a cluster contains many events, consider pacing or grouping the presentation so it does not become annoying.

The system should preserve the identity of individual events while making the cluster feel like one connected incident.

## 7. Event log integration

Add event clusters to the event logs.

The event log UI should support a clusters view.

This clusters view should show the registered cluster catalogue. Fired cluster rows belong in History.

The clusters view should be switchable from the existing event log interface.

The cluster entries should be clickable.

Clicking a cluster log entry should open a cluster details window.

## 8. Cluster details window

The cluster details window should show:

- cluster name
- cluster description
- whether it is one-time or repeatable
- chaos tier at time of firing
- date fired
- actor or affected country if relevant
- list of member events
- which member events fired or were processed
- any member events skipped and why, if relevant
- summary of cluster consequences

The list of member events should appear as log-style entries.

Each member event entry should be clickable.

Clicking a member event inside the cluster details window should open the normal event details window for that event.

This means the player can inspect the cluster first, then drill down into each event.

The cluster can be triggerable, just like with normal events.

## 9. Settings UI integration

Add cluster controls to the settings UI under the cluster heading.

The cluster settings content should mirror the existing trigger-events content where appropriate.

The player should be able to trigger clusters by ID.

Required behavior:

- show a cluster trigger section
- allow entering or selecting a cluster ID
- allow manually triggering that cluster
- show clear tooltip text
- make errors or invalid IDs understandable
- keep the UI consistent with existing manual event-trigger controls

This should be useful for testing, debugging, sandbox play, and showcase use.

Do not load cluster content in a confusing or unrelated settings panel. Keep it under the correct cluster heading.

## 10. Event log and settings naming

Use clear wording.

Suggested terms:

- `Event Clusters`
- `Clusters`
- `Cluster Log`
- `Cluster Details`
- `Trigger Cluster by ID`
- `Members`
- `Cluster Fired`
- `Repeatable Cluster`
- `One-Time Cluster`

Avoid wording that makes clusters sound like world-end scenarios or triggerable scenarios. These are part of the random event ecosystem, not separate manual gameplay scenarios by default.

## 11. Balance and pacing expectations

Clusters should add tension and connectedness without breaking the existing event pacing.

Design expectations:

- low base cluster roll chance
- chaos-scaled cluster chance increase
- member events keep their own eligibility rules
- cluster unlock does not automatically unlock every member event
- optional members use participation chance, not guaranteed firing
- more dangerous optional members usually have lower chance and later order
- eligible optional members should normally have at least 50% participation chance
- cooldowns where needed
- respect member event weights
- no free bypass of fire-once limits
- no unlimited repeatable spam
- cluster firing should feel special
- clusters should not replace normal single-event firing

If a cluster fires, it should feel like related events are converging without dumping every possible member event into the player at once.

## 12. Documentation

Update the relevant documentation.

The docs should explain:

- what event clusters are
- how cluster roll chance works
- how member participation chance works
- how chaos scaling affects clusters
- how member event danger, ordering, and eligibility work
- how member events are handled
- how fire-once and repeatable member events update their weights
- how repeatable clusters work
- how cluster logs work
- how the cluster details window works
- how manual cluster triggering works
- how future clusters should be added

If the existing event system docs or mechanics guide describes random event selection, update it so clusters are included. Update the CHAOS_REDUX_MECHANICS.md specifically.

## 13. Spreadsheet updates

Update the event catalog or related spreadsheet structure if relevant.

Add enough information so event clusters can be tracked.

Possible spreadsheet fields:

- cluster ID
- cluster name
- member event IDs
- cluster type
- base cluster roll chance profile
- chaos scaling profile
- repeatable or one-time
- member required or optional status
- member participation chance
- member minimum chaos tier inside the cluster
- member danger level
- member cluster order
- description
- notes

Do not let the spreadsheet fall out of sync with the implemented cluster system.

## 14. Localisation and tooltips

Add clear localisation for all new UI and log text.

Tooltips should explain:

- what event clusters are
- why a cluster can fire instead of a single event
- how chaos affects cluster roll chance
- how optional member participation works
- why some cluster members may be skipped until higher chaos
- how member events are handled
- how repeatable clusters differ from one-time clusters
- how to trigger a cluster by ID from settings

Keep player-facing text concise but understandable.

## 15. Extensibility requirements

The system should be built so new clusters can be added later without rewriting the framework.

Future cluster creation should only require defining the cluster data, member events, localisation, and any special gating.

Avoid one-off hardcoding that only works for the first cluster.

## 16. Final validation

Before finishing, verify that:

- events can belong to clusters
- a selected event can roll into a cluster instead of firing alone
- base cluster roll chance is low
- cluster chance increases with chaos tier
- optional member participation chance works
- cluster unlock and member minimum chaos tier are handled separately
- more dangerous events usually fire later in the cluster order
- eligible optional members normally have at least 50% participation chance
- fire-once member events are permanently removed after cluster firing
- repeatable member events apply their own repeatable weight reduction and recovery rules
- repeatable clusters can fire more than once when valid
- invalid or exhausted clusters do not fire
- cluster firing counts once for major-event pacing
- event logs have a cluster view
- cluster log entries are clickable
- cluster details window shows member events
- member events in the cluster details window are clickable
- clicking member events opens the normal event details window
- settings UI has a cluster heading with trigger-by-ID content
- manual cluster triggering works
- invalid manual cluster IDs are handled clearly
- localisation and tooltips are updated
- documentation is updated
- spreadsheet or catalog tracking is updated where relevant
- no placeholder, fallback, or simplified behavior remains
