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
