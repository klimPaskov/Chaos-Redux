# 13. Shared Systems and the Chaos Impact Map

## What Event 085 owns

Event 085 owns the global sequence and calendar, warnings, Divine Wrath and its conduct actions, Passover status, remaining firstborn shares, plague-specific effects, Exodus requests and recurrence.
It owns no famine, migration, disease or disaster framework of its own; it sends causes to those owners and reads their results.

## Deaths and population

| Cause | Owner that changes population | Deaths reason |
| --- | --- | --- |
| Direct Blood and Darkness losses, Death of the Firstborn | Event 085 through `apply_exact_state_civilian_population_loss` | A new Ten Plagues reason, added to the Deaths reason registry |
| Outbreak deaths from Frogs, Lice, Flies and Boils | Biological outbreak owner | Owner's outbreak reason |
| Hunger after Blood, Flies, Livestock, Hail and Locusts | Famine | `From famine` |
| Hail and Fire impact | Natural Disasters | Disaster reason |
| Exodus and evacuation route deaths | Migration's exact transfer | Migration's route reason |
| Soldier deaths | Military casualty owner | No civilian transaction |

The exact helper is state-scoped, takes the requested amount and a protected floor, logs the applied loss to Deaths once and prevents civilian deaths from creating manpower.
Never call `chaos_meter_register_deaths` again for people the helper already logged.
The shared Deaths ledger is the only public casualty total; Event 085 reports filter it by episode and phase.

## Famine

Famine owns Food Security, Food Reserves, Relief Access, stages and famine mortality.
Event 085 sends each affected state a food shock and a production or transport context through Famine's adapter, following the Hunger Lines scenario adapter precedent (`famine_hunger_lines_scenario`):

| Phase | Famine input |
| --- | --- |
| Blood | Small food shock (contaminated water and kitchens) |
| Flies | Moderate food shock, larger where earlier sanitation failed |
| Livestock | Strong production context |
| Hail and Fire | Food shock for destroyed harvest, transport context for rail damage |
| Locusts | Food shock for the remaining harvest only |

Each input is reduced by the state's completed protective objective and scaled by Wrath.
Contexts last for the phase plus a recovery tail so a real famine can develop; destroyed capacity does not vanish when the phase ends.
Event 085 never sets a famine stage or deaths directly, and Famine's stage timing is why Livestock sits at day 75 and Locusts at day 140.

## Migration

Migration owns movement, cohorts, routes, trapped people, reception and return.
Event 085 sends Exodus flight requests through Migration's incident adapter (Part 10) and links to Migration's own actions.
It reads only state population and location for Passover; no metadata travels with people.
Event 149 Immigrations is retired and is not revived.

## Disease

The biological outbreak owner in the CBRN lifecycle owns outbreak state, spread, treatment, containment and mortality, and Event 020's exposure adapter is the closest precedent for an external caller.
Event 085 supplies a fictional, non-weapon syndrome context, the exposed states, impaired services, completed care and its mortality allowance (Part 15).
The syndrome creates no weapon, research, stockpile, doctrine or Condemnation.

A non-weapon outbreak entry has not been verified and is an implementation gate.
If the owner cannot accept it, the alternative needs the user's decision (README open question 2); a flat national penalty or an outbreak started through private flags fails this specification.

## Natural Disasters

Only the public `call_natural_disaster` gateway is used, with selected-state targets, supplied proof and no Event 013 history row.
Natural Disasters owns impact scheduling, physical damage, disaster mortality, reports and aftermath.
The composite Hail and Fire contract is described in [Part 6](085_ten_plagues_of_egypt_spec_part_06_hail_fire_and_locusts.md).
No volcanic, tsunami or other origin is invented to obtain a damage effect.

## Other systems

| System | Connection |
| --- | --- |
| Condemnation | A recorded incident of violence against civilians during the episode raises Wrath (Part 2); Event 085 never creates Condemnation itself |
| Camps and repression | Camp abuse reaches Wrath only through its Condemnation record; reception camps follow the camp system |
| World threat | `world_threat_source_ten_plagues` while The Plagues Without End is active (Part 9) |
| Doctor Wu | Clinical care during Boils (Part 5) |
| War | Competes for the same trucks, fuel and output used for protection; war itself never adds Wrath |
| Air Cleanliness, Winter, Fallout | Not touched; darkness and insects do not imply atmospheric contamination |

Other crop- or transport-damaging events worsen an existing food problem only through what remains.
No technology, doctrine, country, formable, focus tree or 3D unit is added.

## Chaos impact map

These are non-death contributions; real deaths add Chaos through the Deaths system.

| Event | Chaos | Guard |
| --- | ---: | --- |
| First global Blood of an episode | +20 | Once per episode |
| First Hail and Fire impact of an episode | +10 | Once per episode |
| First Darkness onset of an episode | +20 | Once per episode |
| Entry into The Plagues Without End | +20 | Once, after all terminal gates pass |
| Each renewed cycle's first Blood at a new recurrence step | +5 | At most +20 across the episode |
| Verified escape from the endless branch | −20 | Once; earlier death-derived Chaos stays |
| Phase reports, recognition, Harden or Heed choices, Evolution activation, migration, relief, cleanup, save/load | 0 | Never a new manifestation |

A first cycle adds at most +50 before deaths; world-end entry and recurrence add at most +40 more.
Where a shared owner already records Chaos for the same physical incident, the Event 085 entry is suppressed.
Failed preparation adds Wrath or exposure, never a separate Chaos charge.

## Sparse progression

One global coordinator owns the episode and phase deadlines.
State and country work queues hold only due impacts, objectives and callbacks.
A bounded onset census at each phase opening is permitted because the event is global; no new permanent daily, weekly or monthly world scan is added.
Control changes and owner results update affected records through callbacks.
Cleanup removes only Event 085's own records and never another owner's active crisis.
