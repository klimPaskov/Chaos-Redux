# Commissioning System Prompt: Event 056 The Navy

Implement the Event 56 recipient, package-allocation, port-selection, commissioning, and bounded cohort systems according to:

- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_1_core.md`
- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_2_eligibility_and_commissioning.md`
- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_3_fleet_package_catalog.md`
- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_4_repeats_and_evolutions.md`
- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_6_chaos_balance_and_performance.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and the shared dynamic helper registries. Use `chaosx_scripted_system_architect` for the event-owned reusable logic. Inspect the actual repository, offline wiki, vanilla documentation, vanilla naval precedents, existing Chaos Redux event patterns, ship definitions, DLC gates, and event-log framework before implementation.

## Recipient contract

Build the eligible recipient set once during the firing. Process each country once. A country requires direct owned and controlled usable coast, legal ordinary naval participation under its owner system, and a valid existing or emergency commissioning location.

Evaluate majors, minors, subjects, civil-war sides, island countries, governments in exile, capitulated enclaves, special Chaos countries, coast-without-port cases, and landlocked countries exactly as the spec defines them.

Do not add a daily, weekly, or monthly whole-world scan. Delayed work belongs only to recipients with phased or emergency commissioning.

## Package contract

Roll one primary identity independently for every recipient. The identity roll must not consider doctrine, ideology, enemy composition, faction role, current production, or strategic usefulness.

Implement all legal baseline identities and their composition contracts. Use an internal hull-equivalent value plus a direct entity-count limit. Protect a defining minimum for every delivered package. Build the entire world allocation before commissioning so processing order cannot starve later countries.

Use recipient receipt count for local repeat scale. Preserve the first, second, third, and fourth-or-later shape from the spec. Cosmetic and ideology changes cannot reset it.

Do not grant research. Use legal existing or controlled event designs. Owner-registered experimental content must fail closed when incomplete, unavailable, disabled, or incompatible.

## Port contract

Select one to three commissioning ports after package identity and scale are known. Score direct ownership, control, naval base capacity, land supply, repair capacity, active combat, hostile air and naval exposure, home-area relevance, and nearby air capacity.

Create only the minimum emergency naval facility for a coast-without-port recipient. Use a short delayed delivery. If the original delayed port is lost, reselect once. Deliver or cancel once.

Never place ships in enemy ports, inland states, invalid sea regions, or uncontrolled colonial facilities.

## Commissioning choices

Give every eligible human recipient one personal report and one legal choice set. AI recipients use the same outcomes through hidden handling.

Full Commissioning delivers all legal ships and support once.

Phased Commissioning delivers the urgent first tranche and reserves heavy or carrier content for one bounded follow-up. Store an explicit delivery or cancellation proof.

Break Up the Package appears only when actual convertible value exists. Preserve the defining core, remove real package hull value, and return a deliberately lossy mix of convoys, fuel, repair support, and limited naval experience. Prevent conversion of the whole fleet and prevent repeat profit loops.

Do not build a permanent decision category or custom scripted GUI. The personal report and ordinary naval interface are the accepted surfaces.

## Support contract

Scale convoys, fuel, aircraft, repair support, and emergency port assistance from package identity and delivered value. Protect minimum carrier air and screening support. Do not grant endless fuel or support above practical storage.

Use existing admirals. Do not generate named commanders for every country. A bounded temporary naval-staff effect is acceptable only when an existing supported pattern needs it.

## Cohort contract

Create bounded origin memory that supports:

- receipt count and package identity history
- delayed delivery proof
- Break Up disqualifiers
- surviving granted-value checks
- direct participation by defining ships
- achievement region and deadline proof

Do not create an unlimited per-ship narrative ledger or a permanent per-battle history. Reuse one origin system for the event and achievements.

## AI contract

Package identity remains random. Commissioning choice and later use are strategy-aware.

Implement the scenario ordering in `quality/ai_probability_scenario_matrix.md`. Invalid choices must be absent. Organize safe task forces by identity. Add bounded naval strategy reactions for missions, reserves, repair, fuel, aircraft support, and production without forcing suicidal deployment.

Run the required baseline audit and post-change comparison through `chaosx_ai_probability_auditor` using the same named scenarios.

## Chaos and evolution contract

Implement only the one-time concrete milestones in the spec. Evolution activation gives zero Chaos. Do not add Chaos per ship, country, aircraft, convoy, battle, blockade, or repeat.

Evolution I changes future scale and skew. Evolution II accepts owner-registered experimental assets. Evolution III enables coherent impossible hybrids. No evolution grants ships retroactively.

All evolution toggle combinations must preserve a complete baseline event.

## Handoff and evidence

Document:

- recipient rules and skip reasons
- package identities and legal pool rules
- hull-equivalent mapping and world allocation targets
- port selection and emergency facility behavior
- commissioning outcomes
- repeat scale
- cohort storage and cleanup
- AI scenarios and probability evidence
- owner registration contract for experimental assets
- task-specific validation and remaining blockers

Do not use a fallback that changes the event promise. If a naval effect, ship-design route, cohort proof, or owner API cannot be implemented cleanly, report the exact limitation and its design consequence before claiming completion.
