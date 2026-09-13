# Event 062 Chaos impact map

## Core rule

Event 62 does not add Chaos for being selected, for opening a crisis, or for activating an Evolution.

Wars, peace, annexation, puppeting, deaths, contamination, and ordinary faction changes already belong to shared systems. Event 62 records only a distinct structural consequence that those systems do not represent.

## Forced faction exit correction

The current mechanics guide assigns negative Chaos to a country leaving a faction. That default represents diplomatic de-escalation. An Event 62 expulsion is a hostile forced exit followed by war and must not reduce Chaos through that generic route.

Implementation must use an explicit source context around every Event 62 removal:

- ordinary voluntary faction exit keeps the shared negative Chaos rule
- Event 62 forced expulsion suppresses the negative faction-exit source
- Evolution II defection into the victim side suppresses the negative exit but still allows the later faction join source when a real new faction is formed
- neutral withdrawal during an active Event 62 fracture should normally suppress the negative exit because it is part of violent bloc collapse
- a later peaceful voluntary withdrawal outside the active generation uses ordinary shared behavior

The preferred solution is a shared Chaos Meter context that classifies the faction change before the owner hook records it. A compensating Event 62 award is acceptable only when the current architecture cannot suppress the incorrect negative source and the compensation exactly neutralizes the observed amount. It must not create a net bonus.

## Shared sources that remain active

| Outcome | Owner | Event 62 behavior |
| --- | --- | --- |
| war declaration | shared war Chaos source | use once per real war, no duplicate Event 62 award |
| peace | shared peace Chaos source | use ordinary source, no automatic extra Event 62 reduction |
| annexation | shared annexation source | use ordinary source |
| puppeting | shared puppeting source | use ordinary source |
| real faction formation or joining | shared faction-join source | use ordinary source after a genuine successor faction or readmission |
| military and civilian deaths | shared Deaths system | use ordinary death threshold |
| nuclear, chemical, biological, atrocity, and contamination outcomes | owning systems | Event 62 records context only |
| civil war | Random Civil War and shared war sources | Event 62 does not duplicate |

## Event-owned sources

### World-order fracture

A one-time `+5` Chaos source is recommended when the Evolution III super-event threshold is met.

Reason:

- the threshold proves simultaneous destruction of several large alliance structures
- individual wars do not fully represent the institutional world-order collapse
- it is fire-once per campaign

The implementation audit may reduce or omit this award if another shared system already records the exact simultaneous structural collapse.

### Formal settlement violation

A `+2` one-shot source is recommended when a country deliberately breaks an accepted Event 62 armistice, readmission guarantee, or recognized-separation settlement.

Required proof:

- the settlement was accepted and recorded
- the violating country was bound by the term
- a concrete hostile action broke it
- no other Event 62 settlement violation was recorded for that transaction

Generic renewed war still records its ordinary Chaos. The `+2` represents the distinct betrayal of a formal Event 62 settlement.

### Collective reconciliation

A bounded `-3` source may be used when one mediated settlement resolves at least two active Evolution III faction fractures, ends their Event 62 structural state, and creates a durable guarantee system.

This source is optional. Implementation must omit it when generic peace already represents the complete result or when the settlement merely pauses the wars.

## No Chaos sources

These actions always add zero Event 62 specific Chaos:

- event draw
- target selection
- victim scoring
- expulsion receipt
- public popup
- decision category opening
- cohesion gain or loss
- Evolution eligibility
- Evolution log entry
- equipment aid
- formation of temporary liaison
- defensive mission success
- failed offensive by itself
- ordinary settlement offer
- cleanup

## Anti-farming

Every Event 62 specific Chaos source requires:

- a stable generation ID
- a source receipt flag
- one application per allowed scope
- a recorded reason in Chaos History
- faction and country cooldown compatibility

The world-order source is once per campaign. The settlement-violation source is once per settlement and no more than once per generation. Collective reconciliation is once per qualifying mediated package.

A save and reload between trigger and effect cannot repeat the source.

## Chaos History text direction

History entries should name the concrete outcome:

- several major alliances fractured in one generation
- a named country broke a recorded alliance-crisis settlement
- a named mediator resolved several tracked alliance fractures

The text should not mention script flags, caps, compensation, or source suppression.

## Required implementation audit

Before final balance is accepted, inspect:

1. the actual faction-leave Chaos hook
2. the war-start source and whether one declaration can fire more than once
3. successor-faction join sources
4. peace and scripted white-peace sources
5. the Event 45 armistice-violation source to avoid double recording
6. cluster pacing and any cluster-level Chaos effect
7. save and reload behavior around delayed war launch

The completion report must show the observed Chaos delta for one baseline purge, one Evolution II split, one Evolution III super-event generation, one settlement, and one settlement violation.
