# Event 35 Chaos impact map

## Core rule

Event 35 changes global Chaos only when a concrete outcome occurs. Eligibility, evolution availability, evolution activation, ordinary phase movement, Severity drift, decision clicks, modifier refreshes, and threshold display changes add zero Chaos.

Generic Chaos sources keep ownership of wars, annexations, ideology changes, deaths, contamination, nuclear use, bombing, and other shared outcomes. Event 35 must not count them again.

## Provisional working outcome table

| Outcome ID | Concrete outcome | Working Chaos change | Receipt scope | Duplicate exclusions |
| --- | --- | ---: | --- | --- |
| `GD-CHAOS-01` | Independent Event 35 opens | `0` | None | Random event selection already represents the incident |
| `GD-CHAOS-02` | Event 34 collapse starts Event 35 | `0` | None | Consequence of the existing Event 34 pacing event |
| `GD-CHAOS-03` | Contagion converts another country into full Event 35 | `+2` | Source-target conversion receipt | No second charge for same target episode |
| `GD-CHAOS-04` | One national crisis remains at Economic Paralysis for a sustained proof period | `+1` to `+2` provisional | One per Event 35 episode | Severity reaching 100 without proof gives zero |
| `GD-CHAOS-05` | A durable national strike or factory-occupation outcome changes government policy or recovery control | `+2` to `+3` provisional | One per incident family and episode | Routine protests and repeated reports give zero |
| `GD-CHAOS-06` | Crisis causes a coup or durable emergency government | `+3` | One per political outcome | Do not duplicate ideology-change Chaos when already recorded |
| `GD-CHAOS-07` | Baseline National Breakdown or Evolution II causes separatist rupture or civil conflict | `+3` to `+5` | One per rupture | Do not duplicate generic war, release, or annexation changes |
| `GD-CHAOS-08` | Evolution III worldwide wave commits | `+20` working target | One per global episode | Evolution activation before the global transaction gives zero |
| `GD-CHAOS-09` | Strong national recovery reverses Event 35-owned paralysis | Up to `-2` | One per recovered episode | Cannot remove more than that episode recorded |
| `GD-CHAOS-10` | Coordinated international recovery ends the worldwide state | Up to `-10` | One per global episode | Cannot remove other systems' Chaos |

Every amount in this table is provisional. Final values require implementation-stage balance work, review against the shared Chaos Meter, and probability evidence. The outcome and receipt contracts are binding, while the exact numbers are tuning targets.

## Evolution treatment

| Evolution state | Chaos at availability | Chaos at activation | Later concrete outcomes |
| --- | ---: | ---: | --- |
| Financial Contagion | `0` | `0` | Secondary full conversion can add guarded Chaos |
| Social Collapse | `0` | `0` | Major organized outcomes can add guarded Chaos |
| The Second Great Depression | `0` | `0` before commit | One worldwide wave can add one global amount |

## Event 34 inheritance

No Event 35 opening Chaos is added after an Event 34 collapse. Event 34 owns the collapse outcome and its own concrete Chaos milestones. Event 35 can later add Chaos for new Event 35-owned consequences, such as a secondary contagion conversion or social rupture.

## Economic Paralysis proof

Severity `100` alone is a state value. It becomes a Chaos outcome only after:

- The crisis remains at maximum for a sustained proof period long enough to represent national paralysis. A short external spike does not qualify.
- One maximum-emergency receipt exists.
- The episode has not already recorded the paralysis milestone.
- The effect is not a one-day temporary spike from an external source.

## Social Collapse exclusions

Event 35 can add Chaos for the specific economic crisis outcome only when it creates a durable national political or institutional rupture. It should not add a second generic amount for:

- War beginning.
- Country release.
- Annexation.
- Ideology change.
- Deaths.
- State damage.

The shared systems remain authoritative for those results.

A single outcome transaction should decide whether Event 35 adds a distinct causal amount and then allow generic systems to record their own separate facts without double counting the same meaning.

## Recovery subtraction

Event 35 recovery can remove only Event 35-owned Chaos that remains attributed to the episode.

The episode records:

- Chaos added by paralysis.
- Chaos added by social outcomes.
- Chaos already reversed.

The global episode records:

- Worldwide-wave Chaos.
- Event 35 global recovery subtraction.

Recovery never reduces generic war, death, contamination, condemnation, or another event's Chaos.

## History requirements

Every non-zero Event 35 Chaos entry records:

- Event ID 35.
- National or global episode ID.
- Affected country when applicable.
- Source country for contagion when applicable.
- Outcome family.
- Exact amount.
- One-shot receipt.
- Date.

## Exploit protection

- Crossing a threshold repeatedly cannot farm Chaos.
- Reloading cannot replay a receipt.
- Transferring a center cannot recreate an outcome.
- Several contagion sources converting one country produce one conversion amount.
- Civil conflict adds Event 35 causal Chaos once.
- Global recovery subtracts once.
- A repeat national crisis receives a new episode and new bounded receipts only after the safeguard.

## Implementation validation

Required checks:

- Evolution activation adds zero.
- Event 34 handoff adds zero Event 35 opening Chaos.
- Independent opening adds zero.
- Secondary conversion adds once.
- Sustained paralysis adds once.
- Repeated social incidents do not spam.
- Generic war and death changes remain separate.
- Recovery cannot reduce more than Event 35 recorded.
- Chaos History shows correct country, source, cause, and amount.
