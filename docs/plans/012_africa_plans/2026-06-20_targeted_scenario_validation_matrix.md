# Event 012 Africa SCN-008 Validation Matrix

Date: 2026-06-21

Scope: static/script reconciliation for the current `SCN-008` triggerable scenario plus the separate normal-route World Is One gate. This matrix replaces the older 2026-06-20 matrix that described retired manual scenario types.

This is not a full Event 012 completion claim and does not replace live in-game scenario testing.

## Current Manual Scenario Shape

`SCN-008` is the shared triggerable scenario window entry for Event 012 Africa. It has two live type options:

| Manual type | Static implementation status | Script evidence | Required live proof |
| --- | --- | --- | --- |
| `Africa Is One` | Static coverage present, live proof pending | `triggerable_scenario_africa_type.africa_is_one`; `africa_apply_triggerable_africa_is_one_opening`; `africa_apply_triggerable_continental_pole_opening`; `africa_apply_triggerable_continental_pole_validation_gates`; `africa_triggerable_scenario_seed_first_authority`; `africa_triggerable_scenario_seed_extra_authorities`; `africa_start_triggerable_unifying_wars`. | Launch at Low, Medium, High, and Maximum. Confirm selected host or WAC scenario exception, Africa identity/focus loading, Charter League, paper claims, living-core counters, regional authorities, Authority Atlas, sponsor/proof-ledger surfaces, visible value movement, unification wars, AI posture, and cleanup. |
| `World Is One` | Static coverage present as direct manual terminal setup, live proof pending | `triggerable_scenario_africa_type.world_is_one`; `africa_apply_triggerable_world_is_one_opening`; `africa_spawn_triggerable_external_continent_unifiers`; `africa_start_triggerable_world_is_one_terminal_wars`; `africa_force_triggerable_world_is_one_terminal`. | Launch at Low, Medium, High, and Maximum. Confirm the Africa Is One opening still occurs, external continent-unifier actors receive intensity-scaled support, terminal wars start, World Is One flags are set intentionally by the scenario helper, accepted super-event/audio slots fire, and compatibility with an existing world-end state behaves as documented. |

## Retired Manual-Type Mapping

The older manual scenario profiles are no longer `SCN-008` type options. They remain validation topics for Event 012 proper or for ordinary-route proof, not scenario-window selectors.

| Former matrix row | Current disposition | Validation still required |
| --- | --- | --- |
| Ordinary unifier / Standard Unifier | Folded into `Africa Is One` host selection and normal Event 012 entry behavior. | Live host-selection proof for a valid African-capital country, paper claims, Charter League creation, and staged integration. |
| Weak or small unifier / Fragile Unifier | No longer a manual scenario type. Weak-host behavior must be validated through normal Event 012 selection or a future dedicated validation setup. | Record selected-host strength and integration pace in live validation rather than relying on the retired fragile type. |
| RSA in Allies / RSA Civil War | No longer a manual scenario type. The RSA civil-war branch remains part of Event 012 proper. | Live SAF-in-Allies validation: continental side, emergency decisions, victory detection, and Allied peace after continental victory. |
| African ally under attack | No longer a manual scenario type. Charter aid, member confidence, protected-member aid, and external-holder defense remain decision-system validation targets. | Live aid/corridor/member-confidence proof under a real member war and cleanup after victory or capitulation. |
| High-chaos Green Covenant | No longer a manual scenario type. High-chaos Bestiary and Authority Atlas routes remain normal-route validation targets. | Live Bestiary package unlocks, nonhuman classification, package actions, containment, warnings, and no human-polity recast. |
| Full Africa unification / Continental Pole | Folded into the strong `Africa Is One` scenario opening for manual launch, but not proof of normal integration mechanics. | Live normal integration proof for state control, living cores, regional authorities, resistance cleanup, and Africa Is One route completion. |
| Cross-continent union | No longer a manual scenario type. The scenario may seed terminal support through `World Is One`, but dynamic union and sponsor routes remain normal-route validation targets. | Live sponsor charters, dynamic union naming, proof missions, route-specific costs, and stale proof-failure behavior. |
| World Is One gate | Split into direct manual terminal setup for `SCN-008 World Is One` and strict normal-route gate proof. | Validate manual direct terminal behavior separately from ordinary proof/certification/preparation/final-focus sequencing. |

## Normal-Route World Is One Gate

The ordinary focus/decision path must still prove all continent-unifier prerequisites before terminal World Is One begins.

| Gate | Static status | Evidence | Required live proof |
| --- | --- | --- | --- |
| External proof routes | Static coverage present, live proof pending | `has_africa_*_unifier_proof_route_ready`; route-specific proof decisions and missions; proof flags for Middle East, Asia, Europe, and South Atlantic. | Complete each proof mission and verify costs, active flags, success/failure, and no stale timer increments the proof ledger after route invalidation. |
| Certification | Static gate strong, live proof pending | `can_africa_certify_continent_unifiers_for_world_is_one` requires chaos tier 5, Africa Is One, super-event fired, continental pole, external readiness, proof readiness, register/dossier/case/high-chaos/regional package/living-core/Bestiary requirements. | Confirm certification is blocked until every listed prerequisite is present and does not self-certify from manual scenario state during ordinary play. |
| Gate preparation | Static gate strong, live proof pending | `can_africa_prepare_world_is_one_gate`; `africa_prepare_world_is_one_gate` spends political power, convoys, trains, support equipment, manpower, command power, and army experience before setting the prepared marker. | Confirm the preparation decision revalidates costs and prerequisites at click time and fails closed if any route requirement drops. |
| Final focus | Static gate strong, live proof pending | `AFR_the_world_is_one` is available only through `can_africa_start_world_is_one_gate` and calls `africa_mark_world_is_one_gate_ready`. | Confirm terminal flags are absent before `AFR_the_world_is_one`, then present only after the focus completes in the ordinary route. |

## Exploit Checks

| Risk | Static finding | Remaining live check |
| --- | --- | --- |
| Manual `World Is One` confused with ordinary route proof | `SCN-008 World Is One` directly sets proof/certification/prepared/terminal flags through scenario-only helpers. Ordinary-route gates still use separate triggers and final focus logic. | Record manual scenario and ordinary route separately in validation notes so the direct manual terminal path is not used as proof that the normal route gates are complete. |
| Manual `Africa Is One` becomes instant-core shortcut | Scenario grants strong Africa and validation counters, but the Event 012 integration/living-core systems remain separate surfaces for normal-route proof. | Confirm scenario paper claims, cores, living-core counters, resistance state, and integration decisions are readable and do not silently bypass the normal route where not intended. |
| Type cycling exposes removed options | Script constants and localisation expose only `Africa Is One` and `World Is One`. | Confirm the scenario UI cycles only the two live types with readable descriptions and intensity text. |
| Existing world-end state compatibility | Launch gate intentionally permits SCN-008 even if Event 012 already fired or another world-end branch is active. | Launch under an existing world-end flag and confirm no incompatible cleanup, missing actor target, N/A text, or duplicate terminal event state. |
| External-unifier support imbalance | External support scales through `africa_apply_triggerable_external_unifier_scaled_support`. | Compare Low, Medium, High, and Maximum support values and resulting wars; confirm Maximum is severe but not broken by missing equipment, manpower, or target setup. |
| Cleanup/stale targets | Scenario cleanup and runtime context helpers exist, but direct terminal setup touches global flags, event targets, external actors, wars, and super-event state. | Confirm cleanup behavior after scenario victory/defeat, tag destruction, capitulation, and repeated opening attempts where the UI allows launch. |

## Validation Status

Static/script reconciliation for current `SCN-008` is now aligned with the two live manual types. Live proof remains queued:

- `Africa Is One` at Low, Medium, High, and Maximum intensity.
- `World Is One` at Low, Medium, High, and Maximum intensity.
- Separate ordinary-route World Is One proof through sponsor charters, proof missions, certification, preparation, and `AFR_the_world_is_one`.
- Scenario-pressure checks for living cores, dossier/case/retry slots, resistance watches, Bestiary actions, sponsor proofs, RSA peace, GUI buttons, AI posture, and stale targets.
