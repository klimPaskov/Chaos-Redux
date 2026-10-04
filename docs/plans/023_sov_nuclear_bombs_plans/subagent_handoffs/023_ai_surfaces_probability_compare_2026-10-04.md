# Event 23 AI surfaces, probability baseline and compare request, 2026-10-04

Owner: the Event 23 implementing engineer (takeover round 1).
Disposition: `blocked` for the MCP baseline and compare; source-level eligibility evidence is recorded below and is not a substitute for the MCP compare.
No numeric weight, MTTH entry or evolution timing (bases 120/120/180/90) changed.

## MCP route attempt

`hoi4_probability_inspect` with `adapter = decision_ai_will_do` and `source = { path = common/decisions/023_sov_nuclear_bombs_decisions.txt }` returned `INTERNAL_ERROR` with `artifactCount = 0`, once with an eight-decision candidate pool and once without one.
No `refresh`, helper expansion, state-flow or repository-wide query was used, and the route was not retried in a loop.
The required `probability_evaluate`, `probability_sweep` and `probability_compare` passes for the `P23_NAV_*` and `P23_FIRST_USE_*` scenarios therefore remain `blocked` on this server error.

## Before and after sources

Before sources were frozen before any AI-surface edit, after the adoption commit `aa1435e5c`.

| Surface | Before path | Before SHA-256 | After |
| --- | --- | --- | --- |
| Decisions | `probability_source_snapshots/ai_surfaces_before_2026-10-04/before_decisions.txt` | `daac795660d061cbbd60ca806a46e9ddc41089231c2c5c3fd202da7dd52999e9` | `common/decisions/023_sov_nuclear_bombs_decisions.txt`, `58677de0c4b48ec7fae3ed7b2739034340585b626384b595498ce317a7c51a30` |
| Event triggers | `.../before_event_triggers.txt` | `f75165c7bacb545caf57f88074d02acc1727fa781c6f02697445e3fa3abed83a` | `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, `d2a8960e4e7a3516199e11d7a611d9fa0e04f5e65da05db2c23a630624b5e60f` |
| Vanilla nuclear raids | `.../before_vanilla_nuclear_raids.txt` | `966408c81eba9f5928ed352d5f95f6648977b23a8e12ce9aa2cd2cdbca76256f` | `common/raids/nuclear_raids.txt`, `796ff56da41dee1d1cd6b8edfd397d56cad7a44cbb0af3f8efc6fa47ff9d2f78` |
| Constants | `.../before_constants.txt` | `5bcf3f563b9abeec59c8a93a73fa1f89a7af3fb1ef9b9d4b9d7fde90b40e54fc` | `common/script_constants/023_sov_nuclear_bombs_constants.txt`, `5c1416b067b9e363485d3585c5ae544edcce11de50ff9ebec82d4b516dbfc07b` |

After commits: `ff4adef81` (raid AI gate), `7bbd68da1` (router), `e7afe3f4f` (first-use route and final-authorization guard), `29d7fef8c` (assembly ceiling), `d47e5ab5d` (map-only presentation), `daaa5d402` (delivery preflight).

## Changed AI eligibility surfaces

| Surface | Before | After |
| --- | --- | --- |
| Six vanilla nuclear raid types, `ai_will_do` | Vanilla weight for every country | First modifier `factor = 0` under `sov_nuclear_bombs_native_raid_ai_restrained` (AI SOV with Event 23 active) |
| `sov_nuclear_bombs_operational_command` | AI could buy the board (factor 0 only before Evolution I) | Hidden from the AI (`is_ai = no`) |
| `sov_nuclear_bombs_give_final_authorization` | `factor = 0` below Evolution III | `factor = 0` only for a staged nuclear-major target without the staged first-use gate |
| `sov_nuclear_bombs_assemble_device_batch` | Any production-phase window | `factor = 0` without a replacement deficit |
| `sov_nuclear_bombs_survey_remote_test_state` | Any valid test site | `factor = 0` for a site that cannot host a test now |
| `sov_nuclear_bombs_harden_storage_site` | Any valid hardening site | `factor = 0` for an empty depot |
| `sov_nuclear_bombs_select_coercion_target` | Any valid coercion state | `factor = 0` for the counterpart already coerced at the current stage |
| `sov_nuclear_bombs_select_retaliation_target` pool | Confirmed exchange only | Also the Evolution IV first-use pool, empty without every severe condition |
| `sov_nuclear_bombs_prepare_limited_strike` | Coercion dossier only | Also the marked nuclear-major state under the prospective gate |
| Phase navigation | Only evolution and attack writes moved the AI | Deterministic router (no weighted pool; not a `probability_sequence` subject without a declared model) |

## Source-level scenario outcomes

These are deterministic reads of the after source, not probability results.

| Scenario | Expected after-source result |
| --- | --- |
| `P23_NAV_BASELINE_ALL_DOCTRINES_VALID` | Custody duty (audit, hardening of a held depot) then idle custody; no production or coercion entry without Evolution I or II; no `.100` purchase |
| `P23_NAV_NORMAL_PRODUCTION_TO_PROOF` | Evolution I review enters production while crews, exercise or authentication are missing; then test once per stage when a ready site exists |
| `P23_NAV_IDLE_NO_PURPOSE` | Router writes nothing new; assembly weight 0 without a deficit; test purpose spent for the stage |
| `P23_NAV_EVOLUTION_DURING_TEST_POSTSTAGE` | Evolution grants and logs once; the phase write becomes a review that holds while the test is prepared |
| `P23_NAV_NATIVE_PENDING_PROTECTED` | Protected predicate holds the board; no pointer clearing |
| `P23_NAV_IV_MAJOR_HIGH_CHAOS_INVALID`, `P23_FIRST_USE_HIGH_CHAOS_EVO4_ABSENT` | Prospective gate false without Evolution IV, so the selector pool and preparation are empty at 1100 Chaos |
| `P23_NAV_IV_MAJOR_WINNING_INVALID` | Prospective gate false without the severe loss, capital, front, reserve and enemy-preparation flags |
| `P23_NAV_IV_MAJOR_PROSPECTIVE_VALID` | Router enters 6, selector offers lower-consequence enemy-major states, preparation stages once and enters 5, final authorization keeps base 0.10 x 1.50 |
| `P23_NAV_II_MINOR_PREPARATION_VALID` | Final authorization keeps base 0.10 for a prepared nonnuclear minor at Evolution II (previously 0) |
| Native raid, AI SOV with Event 23 active | All six raid types weigh 0; human SOV and other countries unchanged |

## Parent follow-up

Rerun `probability_inspect`, `probability_evaluate` and `probability_compare` with the before paths above once the server's `decision_ai_will_do` adapter stops returning `INTERNAL_ERROR`.

## Review additions (decision R4)

The reviewer retried `hoi4_probability_inspect` once (`adapter = decision_ai_will_do`, `source = { path = common/decisions/023_sov_nuclear_bombs_decisions.txt }`, a two-decision candidate pool) and it again returned `INTERNAL_ERROR` with `artifactCount = 0`; the compare stays `blocked`.
The before source for these surfaces is the same frozen `before_decisions.txt`; none of them changed between that snapshot and the review.

| Surface | Before | After |
| --- | --- | --- |
| `sov_nuclear_bombs_enter_atomic_moratorium` | Base 0.90 whenever visible in custody | `factor = 0` without `sov_nuclear_bombs_event_ai_has_restraint_reason` |
| `sov_nuclear_bombs_disperse_reserve_package` | Base 0.90 on every custody visit | `factor = 0` once `sov_nuclear_bombs_ai_dispersal_stage` reaches the attained stage |
| `sov_nuclear_bombs_select_retaliation_target` | Any state in the pool | `factor = 0` for a state outside `sov_nuclear_bombs_event_state_has_delivery_access` |

| Scenario | Expected after-source result |
| --- | --- |
| `P23_NAV_BASELINE_ALL_DOCTRINES_VALID` | Moratorium weight 0 at the opening unless the opening already made the arsenal public or a crisis is recorded |
| `P23_NAV_IDLE_NO_PURPOSE` | Idle custody: one dispersal per stage, no moratorium without a restraint reason |
| `P23_NAV_IV_MAJOR_PROSPECTIVE_VALID` | Selector weight only on reachable lower-consequence states |

## Review additions, second pass (decision R6)

One narrow `hoi4_probability_inspect` call (`adapter = decision_ai_will_do`, `source = { path = common/decisions/023_sov_nuclear_bombs_decisions.txt }`, `candidatePool = ["sov_nuclear_bombs_select_coercion_target"]`) again returned `INTERNAL_ERROR` with `artifactCount = 0`; it was not retried and the compare stays `blocked`.
The before source for this surface is `HEAD` `ab3470be58d3231e495e305dbe5f308a66f88005` (`common/decisions/023_sov_nuclear_bombs_decisions.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`), readable with `git show`.

| Surface | Before | After |
| --- | --- | --- |
| `sov_nuclear_bombs_select_coercion_target` | `factor = 0` only for the state whose controller is the last coerced government at the current stage | `factor = 0` unless the dossier's government (non-Soviet controller, otherwise owner) is an independent minor at war with the Union, absent from the stage list `sov_nuclear_bombs_ai_coerced_target_ids`, and not the counterpart of a verified settlement |
| Router coercion purpose | An enemy minor other than the last coerced government | An enemy minor absent from the stage list, through the same country predicate |

| Scenario | Expected after-source result |
| --- | --- |
| `P23_NAV_COERCION_TWO_MINORS_ONE_STAGE` | One dossier against each enemy minor, then no coercion purpose and zero selection weight until the next attained stage |
| `P23_NAV_COERCION_NEW_STAGE` | The stage list empties on the first dossier of the new stage; every enemy minor except a verified settlement counterpart is eligible again |
| `P23_NAV_COERCION_NONWAR_COUNTERPART` | Zero selection weight for a state whose dossier would name a government not at war with the Union |

## Review additions, third pass (decisions R8 and R9)

One narrow `hoi4_probability_inspect` call (`adapter = decision_ai_will_do`, `source = { path = common/decisions/023_sov_nuclear_bombs_decisions.txt }`, `candidatePool = ["sov_nuclear_bombs_audit_stockpile"]`) again returned `INTERNAL_ERROR` with `artifactCount = 0`; it was not retried and the compare stays `blocked`.
The before source for these surfaces is `HEAD` `1cebd5393e82e8661fab4d92e35c5807d8b15cdc` (`common/decisions/023_sov_nuclear_bombs_decisions.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`), readable with `git show`.

| Surface | Before | After |
| --- | --- | --- |
| `sov_nuclear_bombs_audit_stockpile` | Base 1.20, x2.00 below 70 integrity, on every visible custody visit | `factor = 0` after the first audit unless `sov_nuclear_bombs_native_custody_reconciles` holds |
| Router custody duty, dispute row | A national custody dispute after a full audit interval | The same, only while `sov_nuclear_bombs_native_custody_reconciles` holds |
| Router first-use candidate | Any lower-consequence state of an enemy nuclear major | The same, only for a state inside `sov_nuclear_bombs_event_state_has_delivery_access` with the Soviet actor as launcher |

| Scenario | Expected after-source result |
| --- | --- |
| `P23_NAV_AUDIT_DISPUTE_UNRESOLVABLE` | After the first audit, zero audit weight and no custody duty while the native stockpile stays below operational, assigned and reserved custody |
| `P23_NAV_AUDIT_DISPUTE_RESOLVABLE` | Once the stockpile covers custody again, the router's custody row applies after the audit interval and the audit keeps base 1.20 |
| `P23_NAV_IV_MAJOR_PROSPECTIVE_UNREACHABLE` | Every candidate state is beyond the delivery ceiling: no row 5, the router continues to rows 6 to 11 |
| `P23_NAV_IV_MAJOR_PROSPECTIVE_VALID` | Unchanged: a reachable candidate enters phase 6 at once |

## Round 2 additions (decisions R2-1, R2-3, R2-7 and R2-8)

This round made two narrow inspect attempts, one per new surface family, both without `refresh` and without repository-wide or helper-expansion queries, and neither was retried:

- `adapter = event_mean_time_to_happen`, `source = { path = common/mtth/023_sov_nuclear_bombs_mtth.txt }`, `candidatePool = ["sov_nuclear_bombs_evolution_iv_interval"]`: `INTERNAL_ERROR`, `artifactCount = 0`.
- `adapter = ai_strategy_factor`, `source = { path = common/ai_strategy/023_sov_nuclear_bombs_ai_strategy.txt }`, `candidatePool` holding the plan id before its rename to `sov_nuclear_bombs_ai_delivery_bombers`: `INTERNAL_ERROR`, `artifactCount = 0`.

The lead's earlier attempt this round (`decision_ai_will_do`, the decisions file, `candidatePool = ["sov_nuclear_bombs_disable_devices"]`) failed the same way, so evaluate and compare were not run and the disposition stays `blocked`.
The rows below are the source-level expectations for the named scenarios; they are not compare evidence.
Before sources: `probability_source_snapshots/ai_surfaces_before_round2_2026-10-04/` (constants, decisions, event effects, event triggers, MTTH and on_actions from `b6d4c6e45`); the AI strategy is new, and its before state is the installed vanilla Soviet plan (`SOV_unit_production`: strategic bomber unit ratio 0, production factor -20; `SOV_bomber_production`: one strategic bomber line above 30 military factories).

| Surface | Before | After |
| --- | --- | --- |
| Severe first-use gate inputs (R2-1) | `sov_nuclear_bombs_strategic_losses`, `capital_threat_active`, `front_collapsed` and `reserve_exhausted` never written, so the gate never held | Written weekly at war by `sov_nuclear_bombs_assess_strategic_losses`; numeric weights unchanged |
| `sov_nuclear_bombs_conduct_recovery_raid` and `sov_nuclear_bombs_disable_devices` imminence factors (R2-3) | x1.80 and x2.00 on a flag nothing set | The same factors on `sov_nuclear_bombs_event_selected_breakaway_operationalization_is_imminent` |
| Evolution III interval (R2-7) | 180 days, factors for exchange, enemy use, war, low integrity, moratorium | Adds x0.80 for a threatened capital |
| Evolution IV interval (R2-7) | 90 days, factors for collapse, exchange, enemy use, restraint, centralized authority, low integrity, moratorium | Adds x0.80 threatened capital, x0.80 front in full collapse, x0.85 critical strategic losses |
| Soviet AI strategic bomber demand (R2-8) | Vanilla values only | +3 unit weight, +20 production factor, one minimum line while the deployed force is at or below the delivery floor |

| Scenario | Expected after-source result |
| --- | --- |
| `P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION` | Reachable: technical access done and command formation running for the selected depot doubles the disablement weight and raises the raid's; "Destroy a Compromised Site" becomes available when recovery is impossible |
| `P23_EVO3_MAJOR_RIVAL_NORMAL` | Unchanged at 180 days: at peace the war assessment clears the capital threat; a wartime threat to the capital gives 144 days |
| `P23_EVO4_COLLAPSE_ACCELERATED` | Before: 90 days, since no factor read the war situation; after: about 58 days with the threatened capital and the front in full collapse, about 49 when the losses are also critical; it still records once |
| `P23_EVO4_GATE_BLOCKED` | Unchanged: timing never bypasses the stage gate |
| `P23_FIRST_USE_TIER_1000_SEVERE_RARE` | The gate can now hold when all five war inputs and the delivery, command and enemy-use requirements are met; first use stays limited to that case |
