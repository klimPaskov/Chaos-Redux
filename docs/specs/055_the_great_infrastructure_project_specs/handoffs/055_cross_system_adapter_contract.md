# Event 55 Cross-System Adapter Contract

## Rule

Event 55 publishes project facts and consumes owner-published facts. It does not read or mutate another system's primary ledger.

Every adapter should carry a version, request or project generation, source owner, target scope proof, result, and rejection reason.

## Event 18 to Event 55

Input facts:

- resource state
- resource family
- owner
- discovery generation
- safety or closure status

Event 55 result:

- Resource Corridor proposal created
- proposal rejected with reason
- existing corridor proposal refreshed

Event 55 must not change the deposit's danger or closure state.

## Event 55 to Famine

Published facts:

- route origin and destination
- route states
- route mode
- operational status
- relief priority
- port status
- partner access
- capacity class

Famine decides Relief Access, reserve movement, mortality, and crisis stage.

## Event 55 to Migration

Published facts:

- safe route endpoints
- route capacity
- fixed-link or port availability
- operational and security status
- partner access

Migration decides cohort movement, trapped populations, destination validity, reception, settlement, and route deaths.

## Great Embargo to Event 55

Consumed facts:

- embargo target
- participant restriction
- current generation or active proof
- relevant trade or cooperation block

Event 55 result:

- international benefit reduced or suspended
- procurement pressure
- partner contribution suspended
- alternative or domestic route proposal

Event 55 does not remove the embargo.

## Natural Disaster and damage adapters

Consumed facts:

- affected state or node
- disaster or damage generation
- physical building damage
- current owner and controller

Event 55 result:

- route status refresh
- repair or reroute action
- no duplicate building or population damage

## Failure behavior

Missing generation, missing scope, stale project, invalid owner, or incomplete route proof returns a rejected result and performs no mutation.
