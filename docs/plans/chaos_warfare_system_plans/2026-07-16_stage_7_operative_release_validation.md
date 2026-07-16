# Stage 7 Operative-Release Validation Handoff

Status: bounded tranche accepted. Stage 7 and the full CBRN goal remain incomplete.

This handoff records source-proven behavior, current-version engine limits, and the scenario audit for ordinary biological intelligence operations. It does not claim runtime behavior the engine documentation does not expose.

## Implemented surface

- `common/operations/chaosx_bioweapon_operations.txt`: four native ordinary-agent operations and the preserved weaponized-zombie operation
- `common/scripted_triggers/biological_operation_triggers.txt`: preparation, exact-state, AI-profile, native-scope, and capture validation
- `common/scripted_effects/biological_operation_effects.txt`: outcome weights, lifecycle dispatch, attempt history, doctrine refund, and capture consequences
- `common/on_actions/chaosx_on_actions_biological_operations.txt`: exact `on_operative_captured` adapter with no periodic iteration
- `common/scripted_triggers/biological_lifecycle_triggers.txt`: route-specific native-operation debit authority
- `common/scripted_effects/biological_lifecycle_effects.txt`: ordinary lifecycle dispatch, incubation, detection, spread, deaths, evidence, Condemnation, and cleanup
- `common/script_constants/biowarfare_constants.txt`: outcome, doctrine, capture, state-profile, and AI tuning
- `localisation/english/chaosx_operations_l_english.yml`: final ordinary-operation and preserved zombie text

No interface, sprite, DDS, PNG, or raid-icon file is modified by this tranche. The operations reuse `GFX_operations_plant_bioweapon`, `GFX_operations_plant_bioweapon_map`, and the existing biological operation phase sprites. Files under `gfx/interface/military_raids/` remain untouched.

## Operation contract

| Agent | Operation | Days | Network | Operatives | Native non-refundable cost | Exact eligible-state evidence |
| --- | --- | ---: | ---: | ---: | --- | --- |
| Anthrax | `operation_plant_anthrax_outbreak` | 120 | 40 | 2 | 20 Anthrax payload, 50 support equipment | airfield, naval base, supply node, industry, or `biowarfare_facility` |
| Plague | `operation_plant_plague_outbreak` | 150 | 50 | 2 | 25 Plague payload, 60 support equipment | capital, dense city, high population, supply node, or high infrastructure |
| Tularemia | `operation_plant_tularemia_outbreak` | 105 | 40 | 2 | 20 Tularemia payload, 50 support equipment | actual state division or supply node |
| Smallpox | `operation_plant_smallpox_outbreak` | 210 | 60 | 3 | 15 Smallpox payload, 75 support equipment | capital, dense city, or high population |

Each exact payload archetype maps to one current model in `common/units/equipment/bioweapons.txt`. All four ordinary operations use `return_on_complete = no` and omit `operation_cost`, so their authored equipment bill is not modified or refunded by operation modifiers.

## Scenario audit

| Scenario | Source-proven result |
| --- | --- |
| Missing project, operational readiness, policy authority, network, exact payload, support equipment, or eligible state | Native visibility, availability, requirements, and scripted preparation gates reject the operation. |
| Selected state remains controlled and valid | ROOT, FROM, and FROM.FROM are saved only after the vanilla-aligned control check; agent profile and lifecycle eligibility are then revalidated. |
| Selected state changes controller before outcome | The resolver fails closed before dereferencing a replacement state; equipment is not returned and no seed is created. |
| Abort outcome | Attempt history is recorded; no outbreak, completed-use, treaty-breach, contamination, death, or medical-saturation record is created. |
| Partial release | The exact selected state enters `operative_release` incubation with the partial-result multiplier. |
| Full release | The exact selected state enters `operative_release` incubation with the full-result multiplier. |
| Weak or defensive AI profile | The route gate can reduce weight to zero; a defensive profile multiplies otherwise valid weight by `0.20`. |
| Retaliatory AI | Retaliation authorization or prior target biological use increases willingness while all player-equivalent gates remain required. |
| Radical, high-chaos, or desperate AI | First-use, unrestricted-use, surrender, and doctrine factors increase willingness only after route and policy authorization. |
| Agent-specific target country | AI rewards countries with high-value agent-specific evidence and halves weight for countries that contain only a minimally eligible state. |
| Theater Contamination doctrine | Release success increases and 2 Command Power is returned once after operation resolution; physical cost and consequence records are unchanged. |
| Terminal Hazard doctrine | Release success and physical potency increase, 4 Command Power is returned once, and only later Condemnation calculation may be reduced. |
| Operative captured with a matching live episode | Exact operation token, employer, victim, state, agent, route, source, and actor/victim episode records raise evidence to the confirmed-operative floor and release confirmed attribution. |
| Operative captured without a matching live episode | The actual capture records a confirmed attempt, public coverup Condemnation, and domestic war-support cost without completed-use history. |
| Capture occurs before a later release | The capture records the no-release attempt supported at that moment. A later release must establish evidence through its own lifecycle. |
| Multiple actual capture callbacks | Each callback increments the exact captured-operative ledger and is separately consequential. A seeded episode's public coverup and confirmed Condemnation remain protected by lifecycle one-shot flags; no synthetic callback or inferred operation count is created. |
| Zombie operation | `operation_plant_weaponized_zombie_outbreak` retains its separate project, payload, target trigger, resolver, consequences, localisation, and sprites. |

## Engine limits and unresolved runtime evidence

- Native operations expose an authored equipment cost and `return_on_complete`, but no script-readable runtime debit amount. The implementation records no fabricated amount or proof; numeric lifecycle payload history remains zero for `operative_release`.
- Native operation AI can weight a target country but provides no field for ranking the eventual selected state. Agent-specific country profiles are used; no state estimator is retained.
- Current-version trigger documentation exposes no exact state-scope frontline predicate. Tularemia uses actual troop presence or a supply node and does not treat airfields, factories, or ports as frontline evidence.
- `on_operative_captured` documents character ROOT/FROM and the operation character accessors, but it exposes no unique operation-instance id. Actual capture callbacks cannot be deduplicated by operation without inventing identity.
- The engine owns model selection within an equipment archetype and cancellation timing. Source inspection proves one current model per ordinary payload archetype and `return_on_complete = no`; it does not expose a runtime transaction record to script.
- The local HOI4 inspection service could not provide an operation artifact because its storage quota returned `ARTIFACT_STORAGE_LIMIT`. This is recorded as unavailable evidence, not a passing validation result.
- The bounded completion-auditor run was rejected by the platform safety filter before it could inspect the tranche. This is unavailable audit evidence, not a passing result; full Stage 7 and package completion audits remain required.
- The post-fix scripted-system architect recheck was also rejected by the platform safety filter before source inspection. The repaired invariants were therefore rechecked against current source locally, and the specialist recheck remains unavailable evidence rather than a pass.

## Specialist re-audit follow-up

- The scripted-system architect found that a Command Power refund could execute after invalid native operation scopes. The refund now occurs only inside the validated ROOT/FROM/FROM.FROM branch and only after a resolved operation outcome.
- The architect also found that the capture history looked operation-idempotent despite the engine exposing no operation-instance id. The ledger now records exact captured operatives. Every real `on_operative_captured` callback is independently consequential, while episode-level attribution and cover-up consequences remain one-shot through the matching lifecycle episode flags.

## No-fallback statement

No inferred launch state, replacement target, timer, periodic country scan, continuous-air proxy, payload estimator, operation-instance proxy, designer substitute, placeholder art, resized cross-type asset, or compatibility wrapper is used. Unsupported native behavior is disclosed above and left unsupported rather than approximated.

## Remaining Stage 7 work

Battlefield dissemination, food/water/medical sabotage, laboratory accidents, captured-facility release, doomsday release, full countermeasure and treatment routes, remaining assets and localisation, package scenarios, improvement-loop review, and Stage 7 completion audits remain active in the parent plan.
