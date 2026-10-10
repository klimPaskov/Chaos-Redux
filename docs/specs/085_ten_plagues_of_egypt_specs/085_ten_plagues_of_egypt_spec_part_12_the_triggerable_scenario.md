# 12. Triggerable Scenario: The Ten Plagues

## Identity

The Ten Plagues reserves `SCN-032`, raw integer `32`, for Event 085 in the [shared identifier registry](../shared_identifier_registry.md) and its [machine-readable counterpart](../shared_identifier_registry.json).
The user's 7 October 2026 allocation instruction approves the identity only; the profiles below are proposed design and runtime registration is not done.

## Starting the catastrophe

The manual scenario starts Event 085 at once through the shared scenario interface, using the same episode, participation, order, warnings, population rules and owners as a natural firing.
It needs no country target; Egypt receives its scenes when the map has Egyptian territory, and their absence does not block launch.

Every profile starts with Water into Blood at launch.
A manual launch marks natural fire-once eligibility as used if it was unused and never rearms it.
No profile fabricates earlier plagues, earlier deaths, an observed Passover or a completed cycle; profiles change only how dangerous the new sequence is.

## Intensity profiles

| Profile | Starting Wrath | Capability | Pre-tenth intensity | Tenth-plague intensity | Footprint | Schedule |
| --- | ---: | --- | ---: | ---: | --- | --- |
| Low | 25 | Baseline | 1.00 | 1.00 | One quarter of eligible states | 168 days |
| Medium | 50 | Evolution I overlap | 1.50 | 1.10 | One half | 128 days |
| High | 75 | Evolution II and Exodus | 2.00 | 1.25 | Every valid populated state | 128 days |
| Maximum | 90 | Evolution III recurrence and Exodus | 2.50 | 1.50 | Every valid populated state | 128 days |

Darkness lasts 72 hours and warnings keep their full length at every profile.
A profile grants event-local capabilities only; it does not change global Chaos or grant other events' Evolutions.
If a natural Evolution later gives a stronger value, the stronger value applies; identical capabilities never multiply (a High launch that later gains natural Evolution II stays at 2.00).
Recurrence multiplies the profile intensity as in Part 9.

## What Maximum means

Maximum starts near world-end conditions but does not start with the world-end proven.
The terminal gates in Part 9 still apply: a full sequence, Chaos strictly above 1000, global Wrath at least 75 and branches enabled.
Launched at low Chaos, Maximum is a severe finite crisis, and the scenario description says so.
It never raises Chaos to satisfy its own branch.
Its renewal follows the same proposal as natural Evolution III (README open question 1).

## Existing crises

A second launch while an episode is active, including a mourning intermission before a scheduled renewal, is unavailable.
An incompatible shared terminal state blocks launch with the conflict named.
Other crises are not a reason to block launch; Famine, Migration, disease and Natural Disasters activity continue alongside.

Countries created later join the current phase with their territory's records, as in Part 1, and never receive a private preparation window that moves the global deadline.

## Presentation

The scenario card states starting Wrath, overlap, reach, the fixed order, real population consequences and terminal gating without internal multipliers.
Maximum warns that the whole sequence must be survived and that the final night is not the only killer.
Low warns that careful preparation reduces harm but does not make the campaign bloodless.
No separate launcher GUI is justified.

## Achievement and restart integrity

Each achievement states whether a manual launch qualifies (Part 18).
A Maximum achievement records the profile at launch.
Debug resets, forced phase skips, administrative population restoration and duplicate-launch manipulation invalidate survival achievements for that episode; ordinary save and load does not.
A new launch after a closed episode is a new episode and reuses each state's remaining firstborn share (Part 8).
Testing controls belong to the debug and CXT infrastructure, not the production scenario.
