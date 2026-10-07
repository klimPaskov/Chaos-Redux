# 13. Shared Systems and the Chaos Impact Map

## Event ownership

Event 085 owns the global sequence, plague forecasts, Divine Wrath, its conduct decisions, Passover preparation, firstborn vulnerability records, event-specific manifestations, and recurrence eligibility.
It owns neither the world's generic disease simulation nor a replacement famine or migration framework.

A connection must state which owner accepts the cause, which owner changes the world, and which receipt proves the result.
A shared system's implementation ledger is not evidence that every desired Event 085 adapter already exists.

## Population and Deaths

Use `apply_exact_state_civilian_population_loss` for a direct event-owned civilian loss.
The documented helper is state-scoped, accepts an exact requested amount and protected remaining population, can log the actual result to Deaths, reconciles unintended recruitable-manpower credit, and clears its public inputs.

The caller supplies all contract fields, including a valid logging country, reason, and explicit supplied-proof flag.
It reads `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`.
A helper call that already logs the actual loss must not be followed by a second `chaos_meter_register_deaths` call for the same people.

Population cannot increase recruitable manpower as a side effect of civilian death.
No temporary manpower subtraction may be mistaken for actual civilian mortality.
A missing or invalid transaction remains a failed operation, not a narrated success.

The shared Deaths ledger is the sole public casualty total.
Add one localized Ten Plagues reason for direct anomaly deaths if the current reason registry and UI permit the required extension.
Do not invent a numeric reason constant before inspecting that registry.
Natural-disaster, outbreak, famine, route, and military causes retain their owners' reason classes.

Event episode, cycle, phase, and source correlation identify relevant receipts across these reasons.
An event summary can aggregate that filtered view without debiting population or maintaining an independently authoritative total.

| Cause | Population-changing owner | Deaths treatment |
| --- | --- | --- |
| Direct event-owned unsafe-water or Darkness accident loss | Exact population helper called by 085 | Actual applied amount, direct plague reason |
| Infectious consequences of early infestations and Boils | Existing disease/outbreak owner | Owner's actual outbreak cause |
| Hunger after livestock, crop, or transport loss | Famine | Existing famine cause |
| Hail, causal fire, and physical disaster aftermath | Natural Disasters | Existing disaster cause |
| Route deaths during Exodus or evacuation | Exact transfer under Migration | Route/forced-displacement cause as applicable |
| Death of the Firstborn | Exact population helper called by 085 | Direct plague reason, tenth-phase correlation |
| Actual formation casualties | Military casualty owner | No duplicate civilian transaction |

## Famine

Famine owns Food Security, Food Reserves, Relief Access, severe-stage exposure, relief, and mortality.
Those remain Famine's values and decisions; they do not become additional Event 085 meters.

Livestock and locust phases send proven loss of productive food capacity or remaining crops.
Blood and Flies can send proven damage to safe food or water-dependent services.
Hail sends actual crop and transport destruction.
Darkness sends a relevant service interruption only when its facts meet the receiving contract.

The event must not set a private famine stage or subtract an invented percentage of Food Security.
The owner receives the defined state, actor, source, component or amount, generation, revision, and proof.
An unsupported connection remains an explicit adapter requirement.

The current owner uses sustained exposure and separate recovery confirmation.
Its documented severe-stage windows make the interval from livestock loss through locust devastation important.
Do not shorten the sequence so far that genuine famine never develops and then compensate with a duplicate flat famine death effect.

Ending a plague clears only its live pressure contribution.
Destroyed productive capacity and valid famine aftermath do not disappear.
A state that has not been evaluated is not automatically safe for reception or food imports.

## Migration

Migration owns exact movements, cohorts, custody, routes, trapped populations, reception, and return.
Its positive safety and availability contracts must be used instead of reading private flags.

Firstborn survivors and Passover coverage need a narrow population-metadata extension.
That extension must conserve the metadata when people depart, die en route, arrive, split, settle, or return.
The reviewed material does not prove that this extension currently exists.

Famine-driven flight uses its existing source request and Migration acceptance path.
Event-specific Exodus pressure uses the appropriate event adapter only after the people and cause are proven.
Neither path invents a revived Event 149 Immigrations event, a new flat population drain, or a second pacing pulse.

A receiving population can strain food and services.
Migration supplies the actual receiving or trapped population through its typed projection; Famine computes food consequences.
Event 085 does not turn a generic refugee flag into a guessed famine pulse.

## Disease

Use the existing non-weapon disease/outbreak owner for infectious consequences and Boils.
Event 085 supplies a fictional syndrome context, actual exposure, impaired services, preparedness, and its bounded episode allowance.
The owner retains outbreak state, progression, treatment, containment, and mortality.

This package specifies no real pathogen, engineering procedure, delivery method, or biological weapon capability.
Boils does not grant biological weapons, research, stockpiles, or a doctrine unlock.
An epidemic is not automatically a weapons attack.

An exact peaceful Event 085 disease adapter was not verified.
It must be identified or added with the owner before implementation can be called complete.
Starting an arbitrary named outbreak through private flags, or replacing it with a flat national penalty, fails the specification.

## Natural Disasters

Only the public `call_natural_disaster` gateway is an external interface.
It accepts documented family, target, severity, presentation, and caller-proof inputs.
It owns accepted impact scheduling, physical damage, disaster mortality, reports, and aftermath.

Event 085 calls with no separate Event 013 history ownership for the same plague episode.
Its own global stage owns narrative progression, while the disaster call owns the physical impact receipt.
Reports may be distributed without inserting another independently paced random event.

An explicit selected state needs the documented saved target and supplied proof.
A stale saved target without the proof is not accepted.
The caller checks acceptance and valid output-target proofs.

A composite Hail and Fire episode with one combined mortality budget and coherent preparation remains a required owner-level contract to verify or extend.
Two unrelated full-strength disaster calls are not an adequate substitute.
No volcanic, tsunami, or other origin is invented to obtain a convenient damage effect.

## Other systems and events

War can compete for the same trucks, fuel, trains, convoys, equipment, and labor used for protection.
War itself does not automatically add Wrath.
A maximum-production policy becomes relevant when the government knowingly rejects or diverts a concrete civilian obligation.

Condemnation can receive an actual deliberate abuse incident through its existing owner.
It does not increase simply because a government adopts a different explanation of the plagues.
Deaths and diplomatic blame must not be duplicated across these systems.

Other crop-destroying or transport-damaging events can worsen an already proven food problem.
Only remaining physical resources are available to be damaged again.
An overlapping disaster cannot erase completed protection without a new actual loss.

Darkness does not call Winter, nuclear winter, or Air Cleanliness merely because their visuals are dark.
Insects and red water likewise do not imply a global atmospheric contamination event.
Existing contamination matters only where a proven owner fact affects the exposed population.

No technology, doctrine, country tag, formable, focus tree, or 3D unit system is added by this specification.
An implementation discovery that genuinely requires one must be proposed and routed through its skill rather than quietly expanding scope.

## Explicit Chaos impact map

The following values are proposed non-death anomaly contributions.
They are separate from the shared Deaths contribution and do not multiply with the number of countries, states, reports, or acknowledgements.

| Proven event | Direct Chaos change | Guard |
| --- | ---: | --- |
| First global Blood manifestation in a new accepted episode | +20 | Once per episode, only after manifestation is accepted |
| First actual Hail and Fire impact of the episode | +10 | Once per episode, regardless of the number of state impacts |
| First global Darkness onset of the episode | +20 | Once per episode |
| Ordinary intermediate phase report or recognition of the pattern | 0 | Presentation is not another manifestation source |
| A country's Harden or Heed choice | 0 directly | Changes Wrath; later actual consequences retain their owners |
| Evolution activation alone | 0 | Activation is not a concrete consequence |
| First entry into The Plagues Without End | +20 | Once, after all terminal gates pass |
| A newly stronger renewed-cycle manifestation | +5 | Once per new recurrence rung; at most +20 across the episode |
| Verified full-cycle escape from the endless branch | −20 | Once; does not erase earlier Deaths-derived Chaos |
| Successful migration or delivery alone | 0 directly | No generic movement reward or penalty added |
| Cleanup, report acknowledgement, save/load, or country transfer | 0 | Never treated as a new event |

Real deaths contribute through the shared Deaths system's established scale.
Event 085 does not add the same casualty contribution itself.
Likewise, concrete shared-system Chaos already attributed to the same physical incident must suppress a duplicate anomaly entry where their contracts overlap.

The first-cycle anomaly contributions total at most +50 before deaths.
World-end entry and stronger recurrence can add at most another +40 before the once-only escape reduction.
These bounds describe this map, not the world's total Chaos from unrelated events.

Failed preparation raises Wrath or leaves exposure unprotected.
It does not add a second arbitrary failure Chaos charge on top of every consequent death.
The shared Chaos impact record must make every source, zero-source, reversal, and guard auditable.

## Sparse progression

One global coordinator owns the episode and fixed phase deadlines.
Registered state and country work queues own only their due impacts, preparations, and result callbacks.
A bounded global onset or phase census is permitted by the explicitly global event.
A new permanent whole-world daily, weekly, or monthly scan is not.

Control changes, population transfers, and owner receipts update affected records through exact callbacks.
Save/load preserves episode and cycle identity.
Cleanup removes only this event's registered work and never sweeps away another owner's active crisis.
