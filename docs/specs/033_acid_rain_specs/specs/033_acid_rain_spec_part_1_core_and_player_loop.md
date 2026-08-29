# Event 033 Acid Rain, Part 1, core and player loop

## Catalog contract

| Field | Value |
| --- | --- |
| Event ID | `33` |
| Name | Acid Rain |
| Type | Major |
| Status | To Be Reworked |
| Chaos level | 2 |
| Earliest ordinary eligibility | Gathering Storm |
| Cluster | Natural Disasters |
| Cluster danger | Severe |
| Fire identity | One accepted Major firing per campaign |

The event is valid only after the world reaches Chaos level 2. Its evolutions use later Chaos thresholds and remain separate from the event-level gate.

## Premise

An anomalous atmospheric system produces lethal acid rain and corrosive aerosol. Its source is unresolved and may be supernatural, Chaos-driven, or physically inexplicable. The first front forms over one valid world region and immediately begins affecting a moving connected footprint of states. The anomaly can cross regions, revisit old routes, split into several fronts, and later become a worldwide layer.

The rain directly kills exposed civilians, poisons water and food, and destroys transport, medical, and industrial systems. Its lethality is part of the event premise. Final text should preserve uncertainty about the origin without softening the visible human cost.

## Design goals

1. Make a Major event that remains active long enough for planning and adaptation without relying on a fixed expiry date.
2. Give every country useful preparation time, including countries outside the current route.
3. Make state population, local vulnerability, storm intensity, exposure time, and preparation matter.
4. Make the storm move through real state footprints instead of coloring a whole region as one boolean.
5. Preserve complete world coverage as a hard precondition for ordinary dissipation.
6. Keep the runtime bounded through event-owned registries and scheduled pulses.
7. Integrate with Deaths, Air Cleanliness, CBRN civilian protection, Humanitarian pressure, event history, evolutions, achievements, and the Natural Disasters cluster.
8. Give the global phase a guaranteed endpoint after a substantial minimum duration.

## Non-negotiable rules

- Event 33 is a Major event and is not repeatable.
- Event 33 has Chaos level 2.
- The formation uses super-event treatment.
- Every existing country receives the Acid Rain decision category at formation.
- The category remains available until national cleanup has finished or the event has fully closed.
- Every frozen valid state must be touched before ordinary dissipation becomes possible.
- The event can revisit regions and states.
- The event contribution to Air Contamination cannot exceed `1500 bp`, equal to 15 percentage points.
- The event cannot increase global Air Contamination above `5000 bp`, equal to 50 percent.
- Preparations reduce deaths and damage but do not reduce atmospheric contamination additions.
- Every positive mortality pulse removes real civilian population from the affected state through `apply_exact_state_civilian_population_loss`.
- The actual applied population loss returned by that helper is the sole authoritative death amount for Event 33 counters, reports, achievements, and Deaths registration.
- `local_manpower`, recruitable-population modifiers, generic manpower loss, unit attrition, and counter-only changes cannot satisfy the mortality requirement.
- Evolution availability does not create Chaos.
- A cleanup guarantee prevents an endless storm after coverage is complete.

## Player-facing loop

### Observe

The player opens the Acid Rain category and its map window to see current front footprints, warning regions, movement windows, severe cells, world coverage, Event 33 casualties, Event 33 contamination additions, and national Preparedness.

### Prepare

The country improves four preparedness components through repeatable national projects:

- shelter network
- protected water and food
- medical and protective capacity
- transport and infrastructure resilience

Each component has four tiers. The category shows one project per component and changes its cost, duration, and result from the current tier. The player never sees sixteen separate project buttons.

### React

When a front is approaching or active, the category replaces broad project emphasis with urgent measures. The country can activate shelter protocols, secure water and food distribution, surge medical response, reroute transport, or evacuate a forecast severe zone. Only relevant actions appear.

### Endure

An active state takes an opening population-loss and damage shock once per exposure episode. It then takes a smaller three-day sustained population-loss pulse while it remains under the footprint. Each pulse reduces the state's real civilian population by its exact applied deaths. Severe cells and the global transition create their own episode receipts.

### Recover

When rain leaves a state, acute exposure ends and environmental aftermath remains. The country can restore transport, clean water and soil, repair exposed industry, and close its emergency apparatus. Recovery actions lower aftermath tiers and shorten penalties.

## Event phases

| Phase | Purpose | Exit condition |
| --- | --- | --- |
| Formation | Register states and countries, show super-event, create category, choose first front | First footprint and timers are valid |
| Regional movement | One front drifts through states and changes regions | Evolution transition, full coverage, or event termination |
| Severe-cell escalation | Local severe cells exist inside ordinary front footprints | Cell expires, front leaves, or later evolution replaces front model |
| Multiple-front phase | Two or three independent fronts move at once | Global transition, full coverage and dissipation, or termination |
| Global-layer phase | Every valid state is exposed, with local superstorms | Minimum duration and later dissipation check succeed |
| Dissipation | Stop new exposure, clear front state, report end | No active acute states remain |
| Recovery tail | Countries finish remaining local aftermath work | All event-owned national recovery state is closed |

Formation and regional movement exist in every ordinary firing. Later phases depend on enabled evolutions and Chaos progression.

## Two active player values

### World Coverage

World Coverage is the number of frozen valid states touched at least once divided by the frozen eligible-state count. It is global, exact, persistent, and cannot decrease.

### Preparedness

Preparedness is a national value from 0 to 100. It is calculated from the four component tiers:

- shelter network, 30 percent weight
- protected water and food, 25 percent weight
- medical and protective capacity, 25 percent weight
- transport and infrastructure resilience, 20 percent weight

Each component tier contributes one quarter of its component weight. The display rounds only after the exact component result is calculated.

Casualties and Event 33 contamination are read-only counters. Front intensity is qualitative on each front card. These do not become extra managed values.

## Ordinary success and failure

The event does not have one binary national victory condition. A country performs well when it prepares before arrival, limits deaths, keeps supply routes working, prevents severe-cell spikes, and clears aftermath quickly. It performs poorly when it ignores warnings, loses transport capacity, accepts repeated unprotected exposure, or leaves high-tier aftermath unresolved.

The global system succeeds when every valid state is touched, the later dissipation process resolves, all acute state modifiers are removed, and retained contamination and aftermath remain connected to their normal recovery systems.

## Event endpoint

Complete coverage only unlocks dissipation checks. It does not end the event on the same day. Baseline and multiple-front phases wait at least 14 days after the final newly touched state. They then use a rising chance ladder with a guaranteed last check. The global phase has its own minimum duration and rising check ladder.

Dissipation stops new front creation and acute pulses. It does not erase deaths, event history, permanent achievement facts, Event 33 lifetime contamination additions, or contamination already present in the Air Cleanliness system.

## Direct Chaos outcomes

The shared Deaths and Air Cleanliness systems already add their ordinary Chaos changes. Event 33 uses one-time direct changes only for discrete abnormal outcomes:

| Outcome | Direct Chaos |
| --- | --- |
| Hyperacid system forms | `+5` |
| First successful cross-region movement | `+5` |
| First severe cell that crosses its impact threshold | `+5` |
| Stable second front forms | `+10` |
| Third simultaneous front forms for the first time | `+5` |
| Global atmospheric layer begins | `+15` |
| Final dissipation | `-5`, or `-10` if the global layer occurred |

Each outcome has one permanent receipt. Evolution activation alone gives no Chaos. A severe cell that forms but causes no qualifying impact gives no direct Chaos.
