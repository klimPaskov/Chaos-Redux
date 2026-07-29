# Spec 69: Work for Rations

Work for Rations is the first-year Food Compact labor crisis. It is a post-consequence Fallout-owned country event chain, not the Fallout consequence itself and not an ordinary world-end scenario. A food compact government must decide how to keep a native owned harvest state staffed while Air Winter reduces the available labor pool.

## Identity

| Surface | Value |
| --- | --- |
| Candidate | `670` |
| Human opening | `chaosx.fallout.670` |
| Hidden AI opening | `chaosx.fallout.671` |
| Human delayed result | `chaosx.fallout.672` |
| Hidden AI delayed result | `chaosx.fallout.673` |
| Human callback | `chaosx.fallout.674` |
| Hidden AI callback | `chaosx.fallout.675` |
| Cleanup | `chaosx.fallout.676` |
| Transaction | `710067` |
| Scheduler route | `7167` |
| Event Log history | `9173` |

All rows are dormant until the Fallout scheduler activation and runtime delivery contracts are approved. The chain does not add a Fallout consequence Event Log row, evolution, public scenario entry, or ordinary super-event registration. Its later survival-history payload is ordinary post-consequence content and remains separate from the transition itself.

## Admission

The opening requires a current-generation Fallout country with the Food Compact archetype, a live country survival resource row, a current owned and controlled state, and the first post-consequence year after the opening season. The state must have a current Air Winter record, surviving population, harvestable food reserve, non-terminal supply access, moderate exposure, moderate disease pressure, and enough adaptation to make a labor policy meaningful. The state selector must use the lowest eligible native state in a deterministic order and must preserve that state in the opening receipt. The producer refuses to issue a row after the maximum safe first-year issue day so the scheduler's authored delivery delay cannot move the opening outside the first year.

The country gate rejects stale generation, stale owner or controller, an existing Work for Rations memory, an existing chain reservation, a missing resource row, and any branch set whose costs cannot be paid. The producer and opening both prove that at least one complete branch cost is affordable, so a human receipt cannot create an empty choice window. It must not require a coastal state, naval base, lock, lake, port, or other Great Lakes-specific surface.

## Choices

The four player and hidden-AI-parity branches are:

1. Universal Duty assigns every able household a harvest rotation. It costs Food, Fuel, Scrap, and Recognition, improves immediate labor availability and Supply Access, and increases Exposure if the rotation outlasts the weather window.
2. Paid Labor protects a smaller skilled workforce with ration and command credits. It costs Food, Fuel, and Command Power, improves Production and Cohesion, and leaves the wider labor pool underfed if the ledger is exhausted.
3. Refugee Work Program offers admission and supervised field work to displaced families. It costs Food, Shelter Capacity, Medicine, and Recognition, improves refugee integration and Food, and creates a durable owner-state memory for every resolved outcome while the selected state and owner remain current. The result and callback preserve whether the route succeeded, held partially, or failed.
4. Mechanized Harvest diverts Power and Support Equipment to reduce human exposure. It costs Fuel, Scrap, Power, and Support Equipment, improves production resilience, and adds a bounded maintenance burden only when the frozen state Adaptation is below the low-adaptation threshold.

The opening records one branch and pays its costs exactly once. Option tooltips expose the current costs and the branch-specific effects. Unaffordable options are hidden from the player and receive an invalid hidden-AI score.

## Delayed result and callback

The result resolves after 35 days from the same country, generation, state, controller, branch, and transaction receipt. Its deterministic grade uses the pretransition food reserve, live Supply Access, pretransition Adaptation and Reclamation, inverse pretransition Exposure, and inverse Disease Pressure. Success, partial, and failure are authored separately for each branch. Failure applies a bounded state population loss through the Deaths system with the `fallout_aftermath` cause and never applies a variable-only casualty shortcut.

The result commits branch memory, labor availability, food production, power use, cohesion, refugee integration, and state recovery ledgers. Every resolved Refugee Work Program outcome records a durable owner-state host memory with the current controller, Fallout generation, and branch outcome. It schedules a 270-day harvest review callback with an authenticated ticket. The callback rechecks the same target, current Air Winter record, branch, generation, and Refugee owner-state memory before writing its delayed harvest result. It has success, partial, and failure outcomes, a second bounded Deaths loss on failure, and a final labor-rights memory.

Human and hidden-AI results use the same effect path after mode-specific event delivery. Hidden AI scores all affordable branches from the food, supply, adaptation, exposure, disease, refugee-pressure, and power ledgers. Government archetypes add authored weights, and low supply adds shelter pressure. Fixed branch order resolves ties. Result and callback effects are deterministic and idempotent.

## Cleanup and reset

Cleanup releases the result and callback tickets, clears only this chain's temporary variables, releases the committed state row, and preserves the durable branch and cause memories. A failed opening receipt is terminalized with one cancellation memory before the chain is discarded. Generation-reset cancellation and automatic branch refunds remain outside this dormant tranche and are not claimed by its runtime proof.

## Assets and localisation

The chain needs a dedicated fictional Fallout report image showing a Food Compact harvest crew, ration ledgers, field shelter, and winter machinery under ash-dark light. The source, processed PNG, DDS, sprite registration, hash manifest, and prompt record belong under `docs/assets/670_work_for_rations/`. The event picture sprite must be `GFX_report_event_fallout_work_for_rations` in `interface/fallout_world_end.gfx`.

Visible event titles, descriptions, option labels, tooltips, result text, callback text, Event Log name, Event Log detail, and cancellation wording must use concrete Food Compact and regional language. Working labels are not final localisation.

## Engine-sensitive boundary

Static source inspection can prove identity, target receipt checks, delayed timing declarations, hidden-AI parity, Deaths effect calls, and cleanup ordering. Runtime event delivery, host authority, save recovery, multiplayer input handling, Event Log rendering, and the scheduler caller remain unproven until the user validates them in HOI4. This tranche must remain dormant while those surfaces are unobserved.
