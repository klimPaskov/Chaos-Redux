# Event Chaos Levels

## Purpose

Every registered normal Chaos Redux event has a minimum global Chaos tier for automatic selection.

The requirement is an event property and does not replace its enabled state, normal availability trigger, fire-once or repeatable state, weight, cap, recovery state, or cluster membership.

Event Chaos Levels remain independent from the Dynamic Severity-Aware Cluster Overhaul.

## Levels

The player-facing levels use the existing six Chaos tiers.

| Chaos level | Existing tier ID | Tier name |
| --- | --- | --- |
| 1 | chaos_meter_tier_id.tier_0 | Calm World |
| 2 | chaos_meter_tier_id.tier_1 | Gathering Storm |
| 3 | chaos_meter_tier_id.tier_2 | Rising Chaos |
| 4 | chaos_meter_tier_id.tier_3 | Chaos Tier |
| 5 | chaos_meter_tier_id.tier_4 | Totalen Chaos |
| 6 | chaos_meter_tier_id.tier_final | World Collapse |

The registry stores the existing zero-based tier IDs and presents them as one-based Chaos levels.

## Registry and lookup

initialize_event_chaos_level_registry rebuilds the registered event-tier entries in the same order as the normal event registry.

Every registered event receives an aligned entry.

An event without a specific assignment receives Calm World through chaos_meter_tier_id.tier_0.

get_event_required_chaos_level resolves the registered tier for the current event, and event_required_chaos_level_is_met compares it with the existing global chaos_tier state.

## Automatic selection

The shared active-pool evaluator resolves the event requirement before a candidate contributes selectable weight.

An automatic candidate remains eligible only when its event toggle, normal event trigger and target requirements, fire history, weight state, Event Chaos Level, and every other existing selection rule permit firing.

When the current tier is below the requirement, the event contributes no selectable weight without writing zero into the stored event weight.

Repeatable recovery skips the locked event, so its stored weight, maximum cap, and recovery position remain unchanged until the required tier returns.

Major-event growth skips a locked major through the same active-pool eligibility helper.

The lock does not mark the event fired, change its cap, advance the event timer, or add major-event weight.

Crossing the threshold makes the event eligible on the next normal evaluation, and falling below it restores the temporary lock without erasing persistent event state.

## Relationship to event clusters

The ordinary event-system eligibility check is authoritative before cluster lookup for an automatic trigger.

A selected trigger rejected by the ordinary event system does not roll its cluster and continues through ordinary standalone handling.

Cluster logic can narrow eligibility after the ordinary event-system check, but it cannot bypass the event's Event Chaos Level, target requirements, fire history, or other event-system fireability rule.

Cluster member severity adds a separate member floor.

| Member severity | Cluster floor |
| --- | --- |
| Low | T0 Calm World |
| Medium | T1 Gathering Storm |
| High | T2 Rising Chaos |
| Severe | T3 Chaos Tier |

The effective member minimum is the greater of the severity floor and the declared member minimum.

High and Severe non-trigger rows require another base-eligible member after the first eligibility pass.

Trigger rows and sole configured members are exempt from that support requirement.

Two-pass base eligibility avoids circular support between high-severity rows.

The cluster member floor does not alter the event's registered Event Chaos Level or its existing automatic selection assignment.

The cluster-facing severity corrections are Fury as Medium, Tensions Rising as Low, and Black Plague as Severe.

Event 9, White Peace, requires Gathering Storm even though the Peace cluster unlocks at Calm World.

The Peace cluster cannot enter automatically through White Peace during Calm World because the event-system requirement is not met.

## Manual triggering

Normal manual event firing from Settings, the Event Details trigger button, and the Events-tab bulk trigger respects the event Chaos Level in addition to existing manual readiness checks.

Force Trigger Mode may bypass the event Chaos-level requirement together with the other restrictions that it already bypasses.

Manual cluster forcing may bypass cluster-specific gates and the automatic activation roll, but it cannot fire a trigger or member rejected by the equivalent event-system force context.

Triggerable scenarios remain separate from normal event eligibility and do not read the event Chaos-level gate.

## Event Details and Events tab

Event Details shows the exact numeric Chaos level with its existing tier colour, while an Events-tab row shows Chaos lvl and the number beside Weight.

The Events tab keeps the enabled checkbox independent from Chaos availability.

When the current tier is too low, the row shows N/A instead of selectable weight and its hover tooltip reports the required tier name in red.

Other automatic-pool gates use the same hover line to report their first unmet requirement.

The Events-tab filter cycles through the event-state and event-type filters only.

By Chaos Level remains an Events-tab sort mode.

The rebuilt Events view carries the event Chaos tier in an aligned array, so sorting cannot associate one event with another event's requirement.

Cluster details separately show each member's severity floor, declared minimum, effective minimum, ordinary event-system availability, and starting activation chance.

## Event 1-20 assignments

| Event ID | Event | Chaos level |
| --- | --- | --- |
| 1 | Communist Insurgency | 1, Calm World |
| 2 | Zombie Outbreak | 1, Calm World |
| 3 | The Holy Realm | 1, Calm World |
| 4 | Random War | 1, Calm World |
| 5 | Soviet Union Collapse | 1, Calm World |
| 6 | Independence Wave | 1, Calm World |
| 7 | Fury | 1, Calm World |
| 8 | Tensions Rising | 1, Calm World |
| 9 | White Peace | 2, Gathering Storm |
| 10 | Death | 1, Calm World |
| 11 | Secret Alliance | 1, Calm World |
| 12 | Africa | 1, Calm World |
| 13 | Natural Disasters | 1, Calm World |
| 14 | Cannibalism | 1, Calm World |
| 15 | Utopia Manifesto | 1, Calm World |
| 16 | Brilliant Scientist | 1, Calm World |
| 17 | Random Faction | 1, Calm World |
| 18 | Resources Found | 1, Calm World |
| 19 | Infantry Spawn | 1, Calm World |
| 20 | Black Plague | 1, Calm World |

The table is unchanged by cluster member severity.

## Pacing and history

Event Chaos Level gating happens during ordinary event selection and does not count as a cluster activation.

A successful fixed-member cluster activation applies one cluster pacing and cooldown update regardless of member count. Random Stuff is attempted after ordinary minor pacing and therefore applies no second aggregate pacing update; its selected events still obey their independent Event Chaos Levels.

A valid failed cluster activation roll does not apply cluster pacing or a cluster cooldown update and returns to ordinary standalone handling.

Historical cluster rows preserve their original tier, activation chance, member severity, effective minimum, status, and reason snapshots.

Historical values are never recomputed from the current Chaos tier.

## Icons and assets

No new icon or bitmap asset is required.

The feature reuses the existing Event Details window, Events-tab rows, Clusters tab, Settings controls, checkboxes, buttons, fonts, and Chaos tier colours.

No new sprite registration or GFX entry is required.

## Artifact references

The Event Chaos Level implementation is documented through the shared selection, settings, Event Logs, and cluster artifacts listed in event_clusters.md.

The event catalog workbook schema and formula prose remain unchanged.

The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

The shared GUI routes render successfully without a selected Random Stuff runtime state, so this document does not claim full engine or branch-specific visual evidence.

## Future extensions

Assign higher event Chaos Levels only through an accepted event-specific design decision that preserves the independent event property.

Add a compact locked-reason icon only if future Event Details metadata can no longer present the tier status clearly.
