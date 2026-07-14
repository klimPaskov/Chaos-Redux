# CBRN chemical payload and consequence core

## Purpose

This system provides the shared logistics and consequence contract used by every chemical delivery method. A route cannot create disruption, deaths, contamination, medical saturation, evidence, attribution, or Condemnation unless it first identifies an exact target state, validates an unlocked agent, and removes the required real payload equipment.

Doctrine may reduce the Condemnation impact of an accepted action. That reduction applies only to Condemnation. It does not reduce payload expenditure, protection failure, disruption, deaths, contamination, medical saturation, mask loss, evidence, attribution, confirmed-use history, treaty response, or first-exposure adaptation. Confirmed strategic and mass-casualty actions retain public-harm floors after doctrine is applied.

The current implementation establishes the shared core. Ground operations, explicit air raids, biological actions, and nerve-agent suppression are separate delivery adapters and remain pending until their exact route gates are implemented and validated.

## Source-of-truth map

| Surface | Implementation |
| --- | --- |
| Shared delivery and consequence tuning | `common/script_constants/cbrn_chemical_delivery_constants.txt` |
| Strategic, shell, and air payload equipment | `common/units/equipment/cbrn_payload_equipment.txt` |
| Payload route, profile, technology, and stock validation | `common/scripted_triggers/cbrn_payload_triggers.txt` |
| Profile changes, conversion, debit proof, and legacy migration | `common/scripted_effects/cbrn_payload_effects.txt` |
| Exposure calculation contract | `common/scripted_effects/cbrn_exposure_effects.txt` |
| Exact-state consequence dispatch | `common/scripted_effects/cbrn_consequence_effects.txt` |
| Military and civilian protection resolution | `common/scripted_effects/cbrn_protection_effects.txt` |
| Targeted contamination, medical, and evidence recovery | `events/cbrn_chemical_delivery_events.txt` |
| Sanctions stock detection and destruction | `common/scripted_triggers/condemnation_sanctions_triggers.txt` and `common/scripted_effects/condemnation_response_effects.txt` |
| Equipment and adaptation sprites | `interface/cbrn_chemical_delivery.gfx` |
| Player-facing equipment and adaptation text | `localisation/english/cbrn_chemical_delivery_l_english.yml` |

## Payload equipment

### Strategic agent lots

The national stockpile keeps nine exact models:

- chlorine;
- phosgene;
- mustard;
- lewisite;
- tabun;
- sarin;
- soman;
- malodor agent; and
- behavioral agent.

They share the `chemical_agent_payload` archetype so offensive support formations can receive a real standing payload load without nine duplicate subunits. Scripted operations still debit the exact selected model, so having one agent cannot pay for another.

Build cost, resources, and reliability differ by model. Reliability represents storage and handling integrity rather than battlefield potency. These values are gameplay abstractions with low historical confidence: one lot covers bulk agent, sealing, transfer equipment, filling records, transport preparation, and quality control rather than a fixed historical mass.

### Filled shell lots

`chemical_artillery_ammunition` is the archetype and `chemical_shell_lot_1` is its producible model. Shell lots inherit the persistent `cbrn_shell_filling_agent` profile. The profile must match the action's exact agent before an artillery fire plan may debit the stock.

Changing the shell profile takes 21 days and discards 25 percent of already filled stock. Converting selected strategic-agent stock to shell lots has class-specific recovery:

| Agent class | Output retained |
| --- | ---: |
| Choking | 85.0% |
| Blister | 80.0% |
| Nerve | 72.5% |
| Incapacitating | 85.0% |

### Prepared air payload lots

`chemical_air_payload` is the archetype. Prepared stock is kept in four class-specific models: choking, blister, nerve, and incapacitating. The persistent `cbrn_air_payload_agent` still records the exact agent. Both the exact profile and matching class stock are required for an air action.

Changing the air profile takes 28 days and discards 20 percent of prepared stock. Converting strategic agent to air payload retains 82.5 percent. An aircraft module or idle chemical-capable aircraft never consumes this equipment and never proves release.

## Standing formation loads

The division layer carries real essential payload equipment:

| Formation | Standing payload |
| --- | ---: |
| Projector Battery | 60 strategic-agent lots |
| Chemical Ammunition Train | 120 filled shell lots |
| Light, Medium, or Heavy Armored Delivery Detachment | 60 strategic-agent lots |
| Nerve Suppression Detachment | 40 strategic-agent lots |

These standing needs produce native reinforcement-shortage scaling. They do not pay for an operation. A delivery adapter must also remove the route's national expenditure before exposure is calculated.

## Shared action order

Every chemical delivery adapter must use this order:

1. Call `cbrn_reset_action_context`.
2. Save the exact selected state as `cbrn_action_target_state` and set the target-state proof.
3. Set exact weapon class, agent, agent class, delivery route, severity, and any route-specific authorization proof.
4. Call `cbrn_set_default_payload_requirement_for_action` or supply an explicitly mapped requirement.
5. Call `cbrn_try_debit_action_payload`.
6. Continue only when `cbrn_action_payload_consumed_proof` confirms the exact equipment removal.
7. Resolve the target's military and civilian protection with `cbrn_resolve_action_target_protection`.
8. Resolve the route's verified conditions and set condition proof.
9. Call `cbrn_prepare_chemical_action_record`.
10. If accepted, immediately call `cbrn_dispatch_chemical_action_record` exactly once.
11. Clear route-specific locks and targets through the adapter's cleanup path.

The dispatcher refuses a rejected record, a missing target, a missing payload proof, a zero debit, or a second dispatch from the same context.

## Route expenditure

The default national operation costs are centrally tuned:

| Route | Payload units |
| --- | ---: |
| Cylinder release | 40 strategic-agent lots |
| Projector barrage | 70 strategic-agent lots |
| Artillery fire plan | 120 filled shell lots |
| Armored delivery | 80 strategic-agent lots |
| Chemical air raid | 120 prepared air payload lots |
| Strategic chemical raid | 240 prepared air payload lots |
| Covert operation | 20 strategic-agent lots |
| Nerve suppression | 40 strategic-agent lots |

The figures are gameplay tuning and do not claim a precise historical tonnage conversion.

## Consequence dispatch

An accepted record is applied to the selected state once.

### Units and friendly exposure

`damage_units` applies calculated organization and strength loss to hostile divisions in the state. Friendly and faction divisions receive a separate bounded loss derived from the action's friendly-exposure risk. The system does not estimate military dead from scripted strength damage; the game engine's casualty tracking remains authoritative.

### Civilian deaths and contamination

The exact civilian death fraction enters the shared state Deaths ledger once. The dispatcher then writes the CBRN contamination ledger and the legacy contamination dynamic modifier under a guard that suppresses the legacy helper's second death registration. Overlapping contamination extends the exact expiry, and an older cleanup event cannot erase a later exposure.

### Medical saturation and evidence

State medical saturation is clamped from 0 to 100 and recovers by 20 points every 30 days through state-targeted events. Evidence is clamped from 0 to 100 and decays by 20 points every 180 days. No daily, weekly, monthly, or other all-country pulse is added.

Persistent agents establish at least 45 evidence, confirmed strategic use at least 75, and mass-casualty use at least 90 before decay begins. Attribution is recalculated from the state evidence record. Confirmed use writes permanent country, victim, state, and world history flags even if the current evidence record later decays.

### First exposure

The first chemical exposure belongs to the defending country, not the attacker. It increases only the first affected action's bounded disruption and casualty outputs and applies a 14-day national adaptation penalty. Prior confirmed world use and high military or civilian protection reduce the surprise multipliers. The victim then receives permanent awareness, preventing repeated first-use shock.

### Condemnation and treaty response

The dispatcher passes source, context, exact civilian deaths, contamination, attribution visibility, victim, and calculated Condemnation base to the shared Condemnation system. Integrated CBRN Command may reduce that base through its accepted doctrine ladder. Confirmed strategic and mass-casualty actions reapply their minimum public-harm floors afterward. Confirmed attribution also records treaty use and world confirmed-use history.

Compliance actions recognize strategic-agent lots, filled shells, prepared air payloads, and legacy cylinders. Monitored destruction removes the configured fraction of every recognized chemical stockpile family.

## Legacy migration

`cbrn_migrate_legacy_payload_stockpiles` is idempotent and converts legacy cylinders, malodor bombs, and behavioral bombs to their exact strategic-agent lots at the centralized recovery ratio. It also chooses an initial shell and air profile when none exists.

The migration helper is deliberately not called while legacy delivery consumers remain active. Until each old route is retired, doctrine reserves, AI readiness checks, and sanctions accept both old and new stock. Activating migration earlier would remove equipment still referenced by legacy mechanics.

## Engine boundaries

- Selected-state decisions and raids can preserve an exact target state and can contaminate it reliably.
- Current 1.19 documentation exposes `divisions_in_state` with a scoped state, so ground adapters can prove an exact mapped route formation in a friendly state adjacent to the selected enemy state.
- The available scopes do not prove that a particular active Army Headquarters commands that adjacent formation. Headquarters therefore remains the theater authorization and preparation layer; the adjacent formation remains the delivery proof. This distinction must remain visible in route documentation.
- No verified current-version hook proves eligible activity by an ordinary continuous air mission. The continuous-air route is rejected fail-closed. No aircraft-presence, mission-assignment, or idle-module estimator is retained.
- Current state-targeted decision scope exposes no verified live weather or state-terrain trigger. Ground condition handling remains unresolved until an accepted, disclosed model or a verified engine hook is selected. Density and fortification can be read from state structure, but they must not be described as terrain or weather.

## Assets

Final assets are independent type-specific images produced through the Chaos Redux asset workflow. Source PNGs, processed PNGs, DDS files, contact sheets, manifest entries, and the production handoff live under `docs/assets/chaos_warfare_system/stage_6_chemical_delivery/` and the mapped runtime directories.

Registered runtime sprite IDs:

- `GFX_archetype_chemical_agent_payload_medium`;
- one `GFX_<agent>_agent_lot_1_medium` sprite for each of the nine strategic models;
- `GFX_archetype_chemical_artillery_ammunition_medium`;
- `GFX_chemical_shell_lot_1_medium`;
- `GFX_archetype_chemical_air_payload_medium`;
- one medium sprite for each of the four air-payload classes; and
- `GFX_idea_cbrn_first_chemical_shock`.

Equipment DDS files live in `gfx/interface/technologies/stage_6_chemical_delivery/equipment/`. The first-exposure idea DDS lives in `gfx/interface/ideas/stage_6_chemical_delivery/`.

## Pending implementation and future depth

The following work is intentionally not represented as complete:

- exact-state cylinder, projector, artillery, and armored operations with route-specific formation proof, costs, preparation, cooldown, cleanup, and AI;
- an accepted and disclosed ground condition model or a newly verified live weather/terrain hook;
- explicit selected-state chemical air raids and their outcome bands;
- chemical aircraft modules and verified CAS/tactical eligibility;
- retirement of legacy route effects followed by activation of idempotent stock migration;
- biological-agent logistics, incubation, spread, detection, treatment, accidents, and containment;
- equipment-backed nerve-agent suppression with resistance trauma and severe consequence floors;
- mapped equipment designers, route-aware country AI profiles, achievements, final localisation, and specialist completion audits.

Possible later extensions, after the accepted package is complete, include richer depot-accident chains, captured-stock disposal, and state-specific handling infrastructure. They must reuse the exact payload and consequence contracts rather than creating parallel release paths.
