# BOOM integrations, balance, and acceptance

## Shared population and Deaths integration

Every civilian casualty transaction uses the shared exact state civilian population loss path. Event 47 needs its own Deaths reason so country and cause summaries can identify deaths from BOOM without treating them as nuclear deaths.

The Event 47 incident total is the sum of the actual applied values returned by the shared transaction. Requested deaths, pre-clamp estimates, and report text never become the authoritative total.

A disabled Deaths display or history surface must not make the blast harmless when the shared settings contract still permits population loss. In that state, Event 47 uses the supported unlogged population-removal path and keeps only the minimum internal receipt needed to prevent duplicate application.

Military deaths use the shared military casualty path only when the implementation can read an exact observed loss. Civilian and military values remain separate.

## Chaos impact map

Event 47 creates large Chaos pressure through the shared Deaths system. It does not add a flat event-owned Chaos award for the same deaths.

| Milestone or outcome | Chaos handling | Reason | Repeat guard | Shared overlap |
| --- | --- | --- | --- | --- |
| Baseline civilian deaths | Shared Deaths conversion only | The population transaction already measures the real consequence | One receipt per incident and state | Do not add Event 47 Chaos for the same deaths |
| Exact military deaths | Shared military Deaths conversion only | Exact personnel loss is already a shared source | One observed casualty receipt | Do not estimate or duplicate |
| Building and supply destruction | No direct Chaos | The event's main measurable global source is mortality | No extra source | Later wars, famine, and other systems can add their own ordinary changes |
| Bigger BOOM activation | Zero | Evolution state is capability, not an incident | One evolution record | No Chaos for unlock or log |
| Multi-strike activation | Zero | Evolution state is capability, not an incident | One evolution record | No Chaos for unlock or log |
| Two or three simultaneous blasts | Shared Deaths conversion for each affected state | Every blast creates real casualties | Strongest-zone receipt per state | No cluster or event bonus for the same mortality |
| Global soundwave | Zero | Presentation does not change world systems | One report per country and incident | No stability or tension effect |
| Later recovery | No Event 47 refund | The event creates no persistent source that can be contained | Not applicable | Reconstruction, peace, migration, and famine use their own systems |

This narrow map prevents a repeatable mass-casualty event from farming the Chaos Meter through duplicate rewards. A stronger evolved incident still raises more Chaos because it kills more people through the shared threshold.

## Nuclear, condemnation, and atmosphere isolation

The implementation must prove that an Event 47 firing leaves these values unchanged except where another independent world event changes them during the same test:

- nuclear stockpile
- nuclear-use count
- nuclear attacker and victim history
- nuclear condemnation source
- total public condemnation
- fallout intensity
- fallout duration
- Air Cleanliness source ledger
- Air Cleanliness current value
- nuclear retaliation or war state
- nuclear achievements and mission progress

The map effect should be isolated through presentation code. No nuclear gameplay callback is allowed as a convenience.

## Famine, migration, and supply consequences

BOOM does not call a special famine or migration transaction during the blast. The event has already removed the dead through one exact population transaction.

The ordinary famine and migration systems may react later to:

- destroyed railways and supply links
- damaged ports
- destroyed civilian industry
- loss of local population
- active war or occupation
- blocked relief routes
- displaced survivors

Those systems retain their own proof, timing, destination, route, and mortality rules. They must not debit the blast victims again.

No universal refugee event is forced. A heavily damaged state can produce displacement only when the shared migration system's normal evidence supports it.

## Building and infrastructure integration

The blast package should cover every valid state-owned building family that can be damaged safely. The final implementation audit must compare the package against the installed game's current state building definitions and Chaos Redux additions.

The audit should classify each building family as:

- affected at the infrastructure and supply profile
- affected at the industry profile
- affected at the base profile
- affected at the defense profile
- excluded because damage is meaningless or unsafe
- blocked pending an engine-supported route

A building family must not disappear from the design because the implementation started from a short remembered list.

## Force integration

The force effect is limited to units present in the final affected-state ledger at the moment the blast begins.

The implementation should snapshot unit targets before strength damage starts when iterating and mutating the same collection can skip later units. A unit is processed once even when its state appears through several blast paths.

Division deletion is not a normal baseline effect. The high strength-loss bands can destroy very weak formations through ordinary engine behavior. The event should not force-delete every unit in an epicenter because that can erase special divisions, expeditionary forces, volunteers, and other structures without accurate casualty accounting.

## AI behavior

There is no AI choice at the incident opening. AI countries receive the same target rules and damage as human countries.

AI behavior is limited to ordinary reactions after the blast:

- repair damaged infrastructure and supply links according to normal strategic need
- replace or reorganize weakened divisions
- respond to famine or migration through the shared systems when those systems activate
- rebuild damaged airbases, ports, industry, and defenses according to current war needs

Event 47 should not add a special permanent AI strategy. The event ends before such a strategy would have a clear lifecycle.

## Various Anomalies cluster role

Event 47 fits Various Anomalies because the blast has no known actor, cause, or ordinary weapon path.

Its proposed cluster role is optional Severe member.

When the cluster later receives a stable identity and runtime contract:

- independent Event 47 eligibility remains Chaos level 1
- the cluster's own unlock tier remains separate
- a cluster call starts one Event 47 incident
- Evolution II can make that one member incident contain several blasts
- the cluster records one member firing
- Event 47 updates its own repeatable cap, fired count, Event History, deaths, and evolution behavior
- global event pacing advances once for the whole cluster incident
- no extra cluster Chaos is added for Event 47 deaths

Cluster wiring must not be guessed while the catalog row has no stable ID. The accepted Event 47 spec can be implemented independently first.

## Repeatable-event balance

The repeatable weight and cap rules already reduce Event 47 frequency after each firing. The event therefore does not need a separate cooldown or permanent target immunity.

Balance should be reviewed against these risks:

### Small-state erasure

The 1,000 population floor prevents invalid zero-population states while retaining catastrophic mortality. The primary 25,000 population threshold keeps almost empty states out of the main pool.

### Major-state devastation

A dense industrial state can lose a large population and much of its infrastructure. This is intended. The event is rare after repeated firings because the repeatable cap falls.

### Multi-strike runaway damage

Evolution II limits one firing to two or three epicenters. It does not scale the count with the total number of countries or states.

### Overlap multiplication

The strongest-zone rule prevents additive mortality and duplicate building damage.

### Deaths and Chaos multiplication

Only exact shared Deaths conversions change Chaos. No event-owned duplicate is added.

### Report spam

One main report, bounded later-blast notices, and one soundwave acknowledgment per country keep the incident readable.

## Probability contracts

The weighted surfaces require explicit probability evidence.

### Primary target uniformity

Given a frozen pool of eligible states, each state must have equal primary selection probability unless the separation selector is choosing a later Evolution II target. Country size, major status, player control, and war status do not modify the first target.

### Evolution II count

At Chaos 800 to 899, a complete eligible pool should produce two blasts 75 percent of the time and three blasts 25 percent of the time.

At Chaos 900 and above, a complete eligible pool should produce two blasts 60 percent of the time and three blasts 40 percent of the time.

Pool shortage can lower the applied count. Probability evidence must distinguish the rolled count from the safely resolved count.

### Separation preference

The selector should prove that a higher separation tier dominates every lower tier while candidates exist. Different-continent candidates should not lose to same-region candidates because of enumeration order.

### Evolution pacing

Evolution MTTH analysis must separate pre-fire immediate activation from active-history pacing. It should test the named dynamic factors and verify that repeated checks do not create repeated evolution records.

## Performance and bounded work

Event 47 runs only when the event fires or an evolution check is already due through the event framework.

It does not add a daily, weekly, or monthly world scan.

The primary pool can be built through one bounded state selection pass at incident start. Evolution II uses bounded retries and a small number of selected targets. Blast ring construction follows adjacency from those selected states and does not scan the world for each ring.

Reports are routed through bounded country categories and should avoid repeated per-blast whole-world loops. One global soundwave delivery pass is enough for the incident.

## Save and cleanup rules

Active evolution state and repeatable-event weight persist through save and reload.

An incident should normally complete inside one immediate chain or same-day sequence. If delayed events are used for later epicenters, the incident stores:

- incident generation ID
- rolled epicenter count
- resolved epicenter count
- selected primary states
- frozen final affected-state ledger
- current blast index
- state transaction receipts
- report receipts

On completion or safe rejection, it clears every incident target and temporary variable. A stale delayed callback must fail closed when its generation ID no longer matches.

## Required acceptance scenarios

The full acceptance matrix is in `047_boom_acceptance_matrix.md`. The minimum pass set includes:

- peacetime baseline strike
- wartime baseline strike
- isolated island strike
- cross-border first ring
- actual nonhuman primary exclusion
- human special-country eligibility
- exact population and Deaths conservation
- population-floor clamp
- duplicate adjacency removal
- all installed building families classified
- state-local force damage
- no invented military casualties
- complete nuclear isolation
- complete condemnation and atmosphere isolation
- pre-fire Evolution I opening
- active-history Evolution I pacing
- Evolution II two and three blast probabilities
- broad separation and every fallback tier
- overlap strongest-zone behavior
- one camera move
- bounded multiplayer reports
- one history row and one pacing transaction
- later repeat strike on an earlier valid state
- save and reload persistence
- clean rejection when no valid state exists

## Completion boundary

The event is complete when its direct incident loop, exact population accounting, building coverage, force disruption, evolutions, reports, event-log surfaces, repeatable registration, asset, documentation, catalog row, AI recovery behavior, probability evidence, and acceptance tests agree.

A working mushroom cloud with approximate damage is not enough. A correct damage package with nuclear side effects is also not enough. Both the physical result and the isolation contract are required.
