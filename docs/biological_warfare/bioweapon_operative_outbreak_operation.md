# Biological Operative-Release Operations

This subsystem provides four ordinary, state-targeted biological intelligence operations and keeps the weaponized-zombie operation separate. Ordinary releases use the shared biological lifecycle, so an operation establishes a hidden seed rather than applying a direct contamination modifier.

## Player flow

1. Complete the special project for Anthrax, Plague, Tularemia, or Smallpox delivery.
2. Establish the required intelligence network in an eligible target country.
3. Select an exact controlled state whose profile matches the chosen agent.
4. Assign the required operatives, agent payload, and support equipment.
5. Complete five stages: secure sample and transport, infiltrate, establish a release condition, release or abort, and exfiltrate into attribution and containment resolution.
6. The native equipment cost commits the payload and support equipment to launch the operation. `return_on_complete = no` prevents their return at completion.
7. A limited or full release enters the ordinary biological lifecycle in the exact selected state. An abort or lost target context creates no outbreak.
8. If an assigned operative is captured, the exact current operation, employer, target country, and selected state determine whether the capture confirms a live seeded outbreak or exposes an attempt with no proven release.

## Ordinary operations

| Operation | Preparation | Network | Operatives | Native equipment debit | Eligible state profile |
| --- | ---: | ---: | ---: | --- | --- |
| `operation_plant_anthrax_outbreak` | 120 days | 40 | 2 | 20 Anthrax payload, 50 support equipment | Airfield, naval base, supply node, industry, or laboratory state |
| `operation_plant_plague_outbreak` | 150 days | 50 | 2 | 25 Plague payload, 60 support equipment | Dense population or transport center |
| `operation_plant_tularemia_outbreak` | 105 days | 40 | 2 | 20 Tularemia payload, 50 support equipment | State with an actual troop presence or supply node |
| `operation_plant_smallpox_outbreak` | 210 days | 60 | 3 | 15 Smallpox payload, 75 support equipment | Major population or strategic center |

Each ordinary operation requires its exact payload model in stock before preparation. The native operation cost uses the matching archetype because that is the operation schema accepted by the engine; each archetype has one mapped model. Ordinary operations have no operation-cost modifier. The engine does not expose the runtime amount charged from an operation equipment block, so the lifecycle deliberately leaves its numeric payload fields at zero for this route instead of inventing a debit amount or proof.

Weaponized zombies continue to use `operation_plant_weaponized_zombie_outbreak`, their own payload, target trigger, resolver, outcome, and country-developed infectiousness value. They do not enter the ordinary-agent lifecycle.

## Outcome and lifecycle contract

The ordinary resolver calculates abort, partial-release, and full-release weights from mission preparation, network strength, agent infectiousness, and bounded Chaos Warfare doctrine escalation. Readiness controls the physical weaponization multiplier. Attribution-control capacity changes concealment during later detection but never lowers evidence already created by an operation or capture.

Every partial or full release calls `bio_lifecycle_dispatch_seed` with:

- the exact selected state, actor, and victim
- one of the four ordinary agents
- route `operative_release`
- deliberate-source and use-history proofs
- the operative-release route whose native operation definition owns the physical equipment cost
- partial or success result
- weaponization and concealment values

The shared lifecycle owns incubation, detection, spread, deaths, contamination, medical saturation, evidence, attribution, Condemnation, history, and cleanup. The operation does not apply a separate outbreak effect.

An abort records the attempt without creating an outbreak; the native committed equipment is not returned. If the selected state is no longer controlled by the target when the native outcome resolves, validation fails closed before any state dereference: no replacement state is selected and no outbreak is created.

## Captured operatives

`on_operative_captured` is scoped to the captured character. The capture adapter accepts only the four ordinary operation ids and reads the engine-provided `operation_country`, positive `operation_state`, and `operative_leader_operation` values. Every callback represents an actual captured operative and is processed immediately; it does not depend on operation-completion ordering.

If a matching live lifecycle episode exists in that exact state, capture immediately raises evidence to the confirmed-operative floor, confirms attribution, records public history, and adds the outbreak coverup component to Condemnation once. Otherwise capture records a confirmed biological attempt and public coverup Condemnation without writing weapon-use, treaty-breach, contamination, outbreak, death, or medical-saturation history. A capture before a later release is therefore an attempt at the time it occurs; the later release must establish its own evidence through the lifecycle.

Current-version script exposes no operation-instance identifier that can deduplicate multiple captured operatives belonging to one operation. The persistent counter therefore records actual captured operatives rather than inferred operation attempts, and each real capture is consequential. No synthetic callback is created. There is no timer, guessed target, inferred state, replacement state, country scan, or fallback capture path.

## Doctrine and AI

Chaos Warfare doctrine can increase release success, weapon potency, outbreak harm, spread, duration, medical saturation, and route willingness. Theater Contamination refunds 2 Command Power and Terminal Hazard refunds 4 Command Power once after an operation resolves. Doctrine can reduce the Condemnation calculation after the physical and evidentiary records are fixed. It cannot reduce or erase the native equipment cost, evidence, attribution, deaths, contamination, medical saturation, use history, attempt history, domestic war-support penalty, or capture record.

AI uses the same country, policy, readiness, payload, network, and state-profile gates as the player. Ordinary first use is restricted to retaliation, a qualified radical/high-chaos profile, or desperation. Defensive profiles reduce willingness. Agent-specific country checks reward capitals, dense populations, major depots, ports, laboratories, industry, or combined troop-and-supply concentrations and penalize countries that contain only a minimally eligible state. Domestic biological-safety preparation increases willingness; neutral targeting is restricted to the extreme route. An unrestricted actor under formal censure receives a continuation preference only when a current enemy has crossed the exact near-victory surrender threshold. An actor at its own near-capitulation threshold stops selecting all four ordinary-agent operations; an explicitly authorized doomsday route leaves the separate doomsday decision as the only biological release choice during collapse. Weaponized-zombie operation AI remains separate and is not changed by this rule. The native operation AI interface cannot rank the eventual selected state inside a valid target country, and no estimator substitutes for that missing hook.

## Current-version engine limits

- Operation equipment is a native launch cost and can be made non-refundable, but script cannot read the runtime amount actually charged. No numeric lifecycle debit is fabricated.
- Operation AI can weight a target country that contains suitable states but cannot assign a score to the eventual selected state.
- Capture exposes operation country, state, and token, but no unique operation-instance id. Actual capture callbacks are processed independently.
- The documented trigger set exposes no exact state-scope frontline predicate. Tularemia uses only verified troop-presence and supply-node evidence; unrelated buildings are not substitutes.

## Script ownership

- Operation definitions and native costs: `common/operations/chaosx_bioweapon_operations.txt`
- Route triggers and exact state selectors: `common/scripted_triggers/biological_operation_triggers.txt`
- Outcome, lifecycle dispatch, and capture consequences: `common/scripted_effects/biological_operation_effects.txt`
- Capture hook: `common/on_actions/chaosx_on_actions_biological_operations.txt`
- Shared ordinary-agent lifecycle: `common/scripted_effects/biological_lifecycle_effects.txt`
- Central tuning: `common/script_constants/biowarfare_constants.txt`
- Player text: `localisation/english/chaosx_operations_l_english.yml`

The operation effects and triggers are biological-subsystem helpers. They are intentionally not documented in the shared dynamic effect or trigger registries.

## Assets

No new visual asset is required for this tranche. All five operations reuse the established Chaos Redux biological-operation art without modifying it:

- `GFX_operations_plant_bioweapon`
- `GFX_operations_plant_bioweapon_map`
- `GFX_phase_bioweapon_plant_reservoir` and its small sprite
- `GFX_phase_bioweapon_seed_medical_chain` and its small sprite
- `GFX_phase_bioweapon_contaminate_transport_hub` and its small sprite

The sprite declarations remain in `interface/chaosx_operations.gfx`. Their DDS files remain under `gfx/interface/operations/chaosx_bioweapon/`. Existing raid icons under `gfx/interface/military_raids/` are unrelated and remain untouched.

## Future plans

The accepted Stage 7 work still requires the battlefield dissemination, food/water/medical sabotage, laboratory accident, captured-facility, doomsday, countermeasure, treatment, scenario, and completion-audit tranches. Those routes must use exact route evidence and the shared biological lifecycle; none may substitute a periodic country scan or inferred target.
