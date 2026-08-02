# The Door List chain proof record

This record is the static proof companion to
`FALLOUT_DOOR_LIST_IMPLEMENTATION_HANDOFF.md`. It records what can be proven
from source and what still needs the engine-sensitive review gate.

## Pair selection

The candidate producer scans every owned state in stable id order. The
destination requires a current Fallout identity row, a durable survival row,
a produced Air Winter snapshot, shelter of at least thirty-five, and more
than one hundred people. The source requires the same identity and snapshot
receipts, at least 25,000 people, and exposure at least fifteen points above
the selected destination. The source and destination ids must differ and both
must remain owned by the requesting country.

## Frozen arithmetic

The base cohort is the rounded source population multiplied by `0.004`, capped
at 20,000. Receiving capacity is the rounded destination population multiplied
by destination shelter and divided by 1,000. Arrival pressure is the rounded
base cohort multiplied by 1,000 and divided by destination population, clamped
to 0 through 100.

Viability uses the reviewed weights in
`fallout_event_230_viability`. Families require food and filters. Specialists
require medicine and destination supply. The lottery requires recognition and
cohesion. Refusal grades the scrap, cohesion, recognition, supply, and source
exposure score into orderly, fractured, or violent outcomes.

## Scheduler sequence

The opening consumes one ordinary scheduler receipt only after a delayed result
row is reserved. The result row stores the opening token, branch, mode, target,
cleanup token, generation, and frozen ledgers. The delayed result consumes its
own issued receipt before applying the population and state effects. A second
delayed row is then reserved for the callback. The callback consumes its issued
receipt before applying its small institution-memory effects. The cleanup event
releases the callback receipt and then the result receipt, preserving durable
state memories and clearing the live registry flags.

## Static checks recorded

- Event ids `230` through `242` are unique in the Fallout event file.
- Braces are balanced in the new effects, triggers, scripted localisation,
  interface, and event surfaces.
- The dedicated Door List report DDS exists at
  `gfx/event_pictures/fallout/report_event_fallout_door_list.dds` and
  is registered as `GFX_report_event_fallout_door_list`.
- Every `chaosx.fallout.230` through `242` title, description, option, and
  tooltip reference has a localisation key.
- Every Door List Event Log payload has a scripted localisation selector and a
  concrete detail string.
- The new surfaces contain no Zombie ids, files, assets, audio, sprites, or
  paths.
- The new player-facing text contains no em dash or semicolon.

## Limits of this proof

This is a source and static contract proof. HOI4 was not run. It does not prove
the engine-native host identity, full-screen input block, save recovery, or the
two-state cross-effect pointer behavior. Those remain explicit blockers in the
Fallout release gate and are not replaced with a fallback.
