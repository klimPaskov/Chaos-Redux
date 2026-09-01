# Event 23 AI/probability baseline audit

Status: BLOCKED — read-only source baseline completed, but current HOI4 MCP engine evidence is unavailable.

Audit date: 2026-09-01.

Surface: `sov_nuclear_bombs` / `chaosx.nr23.1`, including decision and mission AI scores, event `ai_chance`, evolution MTTH, target-aware selection, test outcome weighting, retaliation, first-use, stand-down, and collapse/breakaway recovery.

No gameplay files were edited. The worktree already reports `events/023_soviet_nukes.txt` as modified; that change was preserved and not overwritten.

## Executive result

The source review found 67 decision `ai_will_do` blocks, 11 non-selectable mission `ai_will_do` blocks, one six-option weighted response event, deterministic one-option events, four evolution MTTH entries, and one three-outcome test `random_list`.

The mandatory opening call to `hoi4.probability_inspect` was attempted for `decision_ai_will_do` on `common/decisions/023_sov_nuclear_bombs_decisions.txt`, with `refresh = true`, and failed with the exact error `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`.

Retries for the event-option, MTTH, mission, and random-list adapters returned `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`. The structural `hoi4.event_inspect` route was also present in the tool inventory but returned `TypeError: tools.mcp__hoi4_agent_tools__hoi4_event_inspect is not a function`.

Consequently, no current `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `event_inspect`, or `event_render` result exists. There is no current MCP artifact URI, analyzer revision, scenario hash, analysis id, or rendered evidence path. Every named scenario below is therefore unresolved for engine probability or timing, and no exact selection probability, rank, dominance, starvation, repetition rate, or timing quantile is claimed.

## Source and evidence ledger

Primary source files reviewed:

- `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_probability_scenarios.md`.
- `events/023_soviet_nukes.txt`.
- `common/decisions/023_sov_nuclear_bombs_decisions.txt`.
- `common/mtth/023_sov_nuclear_bombs_mtth.txt`.
- `common/script_constants/023_sov_nuclear_bombs_constants.txt`.
- `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`.
- `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`.
- `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`.
- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`.
- `common/on_actions/023_sov_nuclear_bombs_on_actions.txt`.
- `common/decisions/categories/023_sov_nuclear_bombs_categories.txt`.
- `common/scripted_effects/023_sov_nuclear_bombs_cxt_test_effects.txt`.

The local scenario-spec SHA-256 is `B2DC932928C132FE7F16F78A51F44F4A1B45DCA8FEF34FE73E052CEFC92B9D65`.

The local source snapshot hashes below are provenance only; they are not MCP revisions.

| Source | SHA-256 |
|---|---|
| `events/023_soviet_nukes.txt` | `E85B213B11803FA8E66FA08703D54D392F8685CDE55C26A09BE8EB96665E5F6D` |
| `common/decisions/023_sov_nuclear_bombs_decisions.txt` | `A55734B754151D63367B3598A06358DA5FA19F41404DCD7D84C48E0C540B83CC` |
| `common/mtth/023_sov_nuclear_bombs_mtth.txt` | `DCB60B1AE6F08C09B0E3D22E9E2442432EB424E3ED2BB103517F0DF3BBD1DE09` |
| `common/script_constants/023_sov_nuclear_bombs_constants.txt` | `6553FD5A328CA207C7FB4919D7D71819556DEA81407E0F9A4DECFC7E0B42A95C` |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | `421176854980E6E9FEDC391E7FF8EAD02F494E996049F3AF1233A0050484626A` |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | `AC6BC65BB433D5DC41D93FA0B6E54A12D5759ECE203858816323F22160EF8603` |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `614659E8087246B20A4EEEB5385AC476C10902112FDEBD6D561F334B20FBAC1B` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `D9CCBD5712AACA8F8586CC5C283ADAA3BC245AC10F05FF9AF597F9A0B7EDDC1B` |
| `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` | `8A510105C5F1038785CD56AE7524973BE76ACFBFAB7C09A3A0D1AEC59808228A` |

Reference baseline consulted: the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI modding, plus the installed vanilla documentation for script concepts/constants, effects, triggers, modifiers, and random lists. No web wiki source was used.

Historical artifacts retained in the existing Event 23 audit handoff are not current named-scenario results, but may help restore the MCP route:

- Decision inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90e02e69c58d07ce8cf97542cd359b19018a086af773a454734b5a04fac1ac34/1f9027965e4e8b64c92aefa941396fa2db3eff5fbaabde3b46877e7a35089d79/probability-inspect-2b9fe4347f0de43a69e631e6f078d9c9da338cab118d8c69417693fd18153756.json`.
- Mission inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9de8210df2e4c2432a19766a2b497dc59d86d9760247cbb6004140ec802ff0a6/34919803aae0c985291e142d8be106bacf81c9f8d75a724e006dd358f90e5df1/probability-inspect-2b9fe4347f0de43a69e631e6f078d9c9da338cab118d8c69417693fd18153756.json`.
- Prior mission evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e848b5e91afbb3a58539a9bfafbf0486c6cb94fac365849969322e9dd7dcd02/c46bbdbf9804f7bbf69a760c8dd1a59dc251d8e7fa484de3b05b9b1fd10c712b/probability-abfe517d072cb595106aa9f7.json`.
- Prior random-list inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e644c1417e0ac2347ff2b24a024dfff568e4fa2c5ec4fed4b69aeccc947ae66/0f550e7930ceb8eac8d2b07695cc402f10a7717b8d2bfd6f7532443dda74a7b9/probability-inspect-73fde4afb0c2c0.json`.
- Prior event traces: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b703f8a53e6742eb441fa0c51c01a065a674b3b990b53d72fbaa2e05b098207/43c3178c1d6882371248e8f884b46d0b65c8d1eb2a1eb2552c3ff384dfdd0ec7/event-trace-7994e7bb6ce7.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8b1fce8f299971f460fa5c23f9afdcf49a67d48af9ffb860e06a660ba6a3b8f/43a0e5d695c14f48658f763e91dc2598f8c2ce1877e199a35adbace2cc6ffdde/event-trace-7994e7bb6ce7.json`.

## Current weighted surfaces

### Decision `ai_will_do`

These are score formulas, not click probabilities. The target-bearing decisions have country-level scores and no target-specific score or factor.

```text
sov_nuclear_bombs_custody_party: doctrine; communism x1.25
sov_nuclear_bombs_custody_military: doctrine; wartime x ai.wartime_factor
sov_nuclear_bombs_custody_scientific_safety: doctrine; democratic x1.50; test_failure x1.40
sov_nuclear_bombs_custody_dispersed_commands: doctrine; war x1.20; capital_threat x1.20
sov_nuclear_bombs_operational_command: command; wartime x ai.wartime_factor; non-Evolution-I x0
sov_nuclear_bombs_collapse_command: collapse; war x1.40
sov_nuclear_bombs_audit_stockpile: 1.20; integrity<70 x2
sov_nuclear_bombs_harden_storage_site: 1.00; war x1.80
sov_nuclear_bombs_disperse_reserve_package: 0.90; war x1.60
sov_nuclear_bombs_centralize_release_authority: 0.70; ultimatum_response_window x1.60
sov_nuclear_bombs_delegate_emergency_retaliation: 0.70; capital_threat x1.60
sov_nuclear_bombs_expand_fissile_production: 1.10; reactor_entitlement x1.80
sov_nuclear_bombs_assemble_device_batch: 0.80; readiness<50 x1.50
sov_nuclear_bombs_prepare_delivery_crews: 1.20; command_exercise_incomplete x2
sov_nuclear_bombs_conduct_command_exercise: 1.00; war x1.50
sov_nuclear_bombs_install_stronger_authentication: 0.90; integrity<70 x1.60
sov_nuclear_bombs_survey_remote_test_state: 1.30; test_failure x1.40
sov_nuclear_bombs_prepare_instrumented_proof_test: 1.50; scientific_safety x1.40
sov_nuclear_bombs_prepare_concealed_field_test: 1.00; not public_arsenal_confirmed x1.40
sov_nuclear_bombs_prepare_public_test: ai.demonstration (0.80); confirmed_enemy_nuclear_use x1.40
sov_nuclear_bombs_strengthen_test_evacuation: 1.10
sov_nuclear_bombs_cancel_prepared_test: 0.20; integrity<25 x2
sov_nuclear_bombs_investigate_test_failure: 1.60
sov_nuclear_bombs_select_coercion_target: 1.00; war x1.30
sov_nuclear_bombs_close_coercion_target: 0.05
sov_nuclear_bombs_send_private_signal: 1.20; not public_arsenal_confirmed x1.40
sov_nuclear_bombs_issue_public_ultimatum: 1.10; public_arsenal_confirmed x1.30
sov_nuclear_bombs_stage_wartime_demonstration: 0.80; ultimatum_response_window x1.50
sov_nuclear_bombs_prepare_limited_strike: 0.60; war x1.50
sov_nuclear_bombs_accept_partial_settlement: 0.90
sov_nuclear_bombs_adjust_demand: 0.40; demand>maximum x1.40
sov_nuclear_bombs_raise_demand: 0.15
sov_nuclear_bombs_back_down: 0.25; credibility<10 x2.50
sov_nuclear_bombs_complete_technical_certification: 1.00
sov_nuclear_bombs_overrule_safety_veto: 0.10; severe_first_use_gate x ai.severe_loss_factor (1.50)
sov_nuclear_bombs_give_final_authorization: 0.10; can_authorize_first_use x ai.severe_loss_factor; non-Evolution-III x0
sov_nuclear_bombs_hold_strike: 0.40
sov_nuclear_bombs_redirect_strike_state: 0.20
sov_nuclear_bombs_reduce_to_remote_demonstration: 0.70
sov_nuclear_bombs_abort_and_recover_device: 0.30
sov_nuclear_bombs_establish_emergency_hotline: ai.moratorium (0.90); confirmed_enemy_use x2
sov_nuclear_bombs_propose_reciprocal_standdown: 1.10; confirmed_enemy_use x ai.restraint_factor (1.35)
sov_nuclear_bombs_limit_retaliation_profile: 1.20
sov_nuclear_bombs_preserve_reserve: 1.00
sov_nuclear_bombs_select_retaliation_target: 1.30
sov_nuclear_bombs_authorize_retaliation: 0.30; confirmed_enemy_nuclear_use x1.60
sov_nuclear_bombs_suspend_release_orders: 1.00
sov_nuclear_bombs_enter_atomic_moratorium: ai.moratorium (0.90); confirmed_use x ai.restraint_factor (1.35)
sov_nuclear_bombs_select_disputed_depot: 1.50
sov_nuclear_bombs_recall_devices: 1.10
sov_nuclear_bombs_secure_rail_corridor: 0.90; war x1.60
sov_nuclear_bombs_negotiate_joint_custody: 1.00
sov_nuclear_bombs_conduct_recovery_raid: 0.20; breakaway_operationalization_imminent x1.80
sov_nuclear_bombs_disable_devices: 1.40; breakaway_operationalization_imminent x2
sov_nuclear_bombs_destroy_compromised_site: 0.30
sov_nuclear_bombs_restore_the_ledger: 1.00
sov_nuclear_bombs_seal_reserve_batch: 1.30
sov_nuclear_bombs_select_dismantlement_site: 0.70
sov_nuclear_bombs_dismantle_batch: 0.70; scientific_safety x1.70
sov_nuclear_bombs_invite_observers: 0.80
sov_nuclear_bombs_record_reciprocal_restraint: ai.restraint_factor (1.35)
sov_nuclear_bombs_reactivate_arsenal: 0.20; serious_crisis x2
sov_nuclear_bombs_breakaway_secure_custody: 1.30
sov_nuclear_bombs_breakaway_attempt_technical_access: 0.40; atomic/nukes tech required by availability
sov_nuclear_bombs_breakaway_form_command: 0.25
sov_nuclear_bombs_breakaway_integrate_delivery: 0.10; local delivery capability required by availability
sov_nuclear_bombs_breakaway_request_return: 1.00
```

Target-bearing decisions with no target-aware score are `operational_command`, `collapse_command`, `harden_storage_site`, `disperse_reserve_package`, `expand_fissile_production`, `survey_remote_test_state`, `select_coercion_target`, `redirect_strike_state`, `select_retaliation_target`, `select_disputed_depot`, `select_dismantlement_site`, and `breakaway_request_return`.

### Mission `ai_will_do`

All 11 missions use `selectable_mission = no` and an impossible `available` trigger (`always = no`). Their scores are activation/timeout bookkeeping scores, not player click probabilities.

```text
sov_nuclear_bombs_device_assembly_mission: 0.80; timeout 120 days
sov_nuclear_bombs_delivery_crews_mission: 0.70; timeout 90 days
sov_nuclear_bombs_command_exercise_mission: 0.60; timeout 60 days
sov_nuclear_bombs_proof_test_mission: ai.demonstration (0.80); timeout 120 days
sov_nuclear_bombs_ultimatum_response_mission: 1.00; timeout 14 days
sov_nuclear_bombs_strike_preparation_mission: 0.40; timeout 7 days
sov_nuclear_bombs_retaliation_window_mission: 0.60; timeout 30 days
sov_nuclear_bombs_rail_corridor_security_mission: 0.70; timeout 120 days
sov_nuclear_bombs_breakaway_operationalization_mission: 0.20; timeout 180 days
sov_nuclear_bombs_joint_custody_transfer_mission: 0.70; timeout 120 days
sov_nuclear_bombs_dismantlement_inspection_mission: 0.80; timeout 180 days
```

The breakaway operationalization mission is the weakest mission score and its visibility/activation path does not itself prove actor validity, crisis state, or complete local delivery capability. The source effect and runtime fail-closed checks remain the controlling safety boundary; the current MCP route could not test timeout timing or repeated activation.

### Event `ai_chance`

The response event `chaosx.nr23.120` has six positive options with static bases: `.120.a` accepted 35, `.120.b` partial 25, `.120.c` delayed 20, `.120.d` refused 20, `.120.e` exposed 10, and `.120.f` foreign support 10.

The option triggers overlap. For example, a valid non-war target can satisfy delayed, refusal, and foreign-support options when it is also in a faction. None of these bases incorporates target strength, losses, credibility, prior threats, guarantee/support, intelligence, or delivery feasibility. The listed values are not normalized probabilities and were not engine-evaluated.

The single-option events `.2`, `.100`, `.101`, `.102`, `.106`, `.110`, `.140`, `.150`, `.160`, `.161`, and `.162`/`.170` use `ai_chance = { base = 100 }` on their only option where present. Hidden timing/root events have no option race.

### Evolution MTTH and fixed random pool

`common/mtth/023_sov_nuclear_bombs_mtth.txt` currently defines these bases and factors:

| MTTH entry | Base | Current factors |
|---|---:|---|
| `sov_nuclear_bombs_evolution_i_interval` | `evolution_i_days` = 180 | public acceleration 0.75; serious crisis 0.65; integrity below 40 delay 1.35; moratorium delay 1.50 |
| `sov_nuclear_bombs_evolution_ii_interval` | `evolution_ii_days` = 240 | breakaway 0.75; war 0.85; public acceleration 0.75; integrity below 40 delay 1.35; moratorium delay 1.50 |
| `sov_nuclear_bombs_evolution_iii_interval` | `evolution_iii_days` = 300 | major exchange 0.60; confirmed enemy use/serious crisis 0.65; war 0.85; integrity below 40 delay 1.35; moratorium delay 1.50 |
| `sov_nuclear_bombs_evolution_iv_interval` | `evolution_iv_days` = 360 | collapse 0.70; major exchange 0.60; confirmed enemy use 0.65; reciprocal restraint 1.25; centralized authority 1.10; integrity below 40 delay 1.35; moratorium delay 1.50 |

The test resolution in `sov_nuclear_bombs_resolve_test` uses one static pool: success `constant:tuning.test_success_weight` = 70, failure `constant:tuning.test_failure_weight` = 20, and accident `constant:tuning.test_accident_weight` = 10. There are no source modifiers for site quality, command weakness, readiness, integrity, safety doctrine, preparation quality, observation, or public knowledge.

## Named scenario matrix

For every row, the declared scenario inputs came from the probability-scenario specification, but the adapter never accepted the scenario. `Pool incomplete` means that the engine candidate set, hidden state, and external modifiers were not returned by MCP; it does not mean that every source trigger is absent. `Source-only` is not an engine result.

### Evolution timing and gates

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_EVO1_HIDDEN_NORMAL` | Evolution I gate is actor-valid, stage inactive, log enabled, and chaos ≥400; base is 180 days, while the scenario describes a 120-day center. | Unresolved MTTH; source/spec center mismatch. Pool is singleton timing, but hidden state and schedule trace are unavailable. |
| `P23_EVO1_PUBLIC_ACCELERATED` | Public arsenal confirmation applies the 0.75 MTTH factor to the 180-day base. | Unresolved MTTH; no exact acceleration or same-day exclusion proved. |
| `P23_EVO1_MORATORIUM_DELAYED` | Moratorium applies only a 1.50 delay factor; `event_can_enable_evolution_i` has no explicit moratorium exclusion. | Unresolved MTTH; source can activate after a delayed pulse instead of safely skipping. |
| `P23_EVO2_BREAKAWAY_ACCELERATED` | Evolution II requires Evolution I active and chaos ≥600; breakaway and war factors are present. | Unresolved MTTH; breakaway timing and state transition are not engine-verified. |
| `P23_EVO2_NO_TARGET_NORMAL` | Evolution II does not require a coercion or strike target; target decisions are separately trigger-gated. | Unresolved; targetless progression is source-possible and target starvation cannot be measured. |
| `P23_EVO3_NO_NUCLEAR_RIVAL_BLOCKED` | Evolution III requires chaos ≥800 plus `event_evolution_iii_world_gate`; that gate requires another nuclear major or an opened/exchange/use flag. | Source-blocked as named; MCP could not prove the blocked trace. |
| `P23_EVO3_MAJOR_RIVAL_NORMAL` | Two nuclear majors alone do not open the current world gate; stable peace with no use/exchange flag remains blocked. The scenario expects eligibility from the rival count. | Unresolved with source/spec gate mismatch. |
| `P23_EVO3_ENEMY_USE_ACCELERATED` | Soviet-owner nuclear-use on-action sets `evolution_iii_world_gate_opened` and major exchange; MTTH has 0.60 exchange and 0.65 serious-crisis factors. | Unresolved MTTH; source supports acceleration but no timing distribution is available. |
| `P23_EVO4_GATE_BLOCKED` | Evolution IV requires chaos ≥1000 plus another nuclear major and `event_evolution_iv_world_gate`; no exchange/use/open flag leaves it closed. | Source-blocked as named; MCP could not prove the blocked trace. |
| `P23_EVO4_COLLAPSE_ACCELERATED` | Collapse factor 0.70 exists, but the world gate does not accept launch-prep verification alone; it requires exchange, confirmed use during war, or the already-open memory flag. | Unresolved with source/spec gate mismatch; launch-prep-only route can remain blocked. |

### Test outcomes and target choice

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_TEST_PROOF_SECURE` | Static outcome pool is 70/20/10 with no secure-site or high-readiness modifier. | Source-only score observation; outcome probability and repetition unresolved. |
| `P23_TEST_CONCEALED_WEAK_COMMAND` | The same 70/20/10 pool is used despite the scenario expecting lower success and higher accident/observation risk. | Unresolved with missing sensitivity; source has no command-weakness weighting. |
| `P23_TEST_PUBLIC_PREPARED` | The same pool is used; public knowledge and foreign reaction are handled elsewhere, not in the outcome weights. | Unresolved with missing preparation/observation weighting. |
| `P23_TARGET_WARTIME_REAL_DISPUTE` | Target triggers can reject invalid/distant/faction cases, but target-bearing decisions have no per-target rank for the valid core/logistics target. | Unresolved target pool; no proof that the intended target wins or that invalid candidates normalize to zero. |
| `P23_TARGET_BREAKAWAY_CUSTODY` | Breakaway custody, core ownership, and protected-major conditions are trigger inputs only; no target score ranks return, joint custody, or protected targets. | Unresolved target pool; missing custody/route/value scoring. |
| `P23_TARGET_RANDOM_WEAK_MINOR` | No target score uses size or strategic value, and weak neutral validity is not represented as a score penalty. | Unresolved; positive or selectable invalid target risk cannot be quantified. |

### Coercion demand and response

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_COERCE_ISOLATED_LOSING_MINOR` | `.120` remains 35/25/20/20/10/10; losing position and credibility do not modify acceptance or partial settlement. | Unresolved event-option pool; intended full/partial dominance is not proved. |
| `P23_COERCE_PROTECTED_STABLE_MINOR` | Foreign-support response only requires faction membership; guarantee, stability, outside support, and exposure risk do not change bases. | Unresolved with unsafe static response weighting risk. |
| `P23_COERCE_UNTESTED_SECRET` | No public-knowledge or untested-secret modifier exists in `.120` `ai_chance`. | Unresolved; expected doubt/delay behavior is not source-weighted. |
| `P23_COERCE_EMPTY_THREATS` | Previous backdowns/credibility do not alter `.120` option bases; the back-down decision has a separate credibility factor. | Unresolved; refusal does not adapt in the event option race. |

### Limited use and strike profiles

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_LIMITED_USE_BREAKAWAY_SEVERE` | Limited targets are Evolution II gated and generic delivery-route gated; `prepare_limited_strike` is 0.60 with war x1.50. | Unresolved score race; no target severity or breakaway custody rank. |
| `P23_LIMITED_USE_BREAKAWAY_SETTLEMENT` | Partial settlement is a flat 0.90 and target selection has no settlement/custody factor. | Unresolved; settlement versus escalation dominance is not engine-verified. |
| `P23_LIMITED_USE_MINOR_NO_DISPUTE` | Minor target validity is checked, but there is no target-value or retaliation-risk score. | Unresolved target-aware weighting. |
| `P23_PROFILE_VALID_MILITARY` | Military profile is constrained by runtime target and delivery checks, but AI scores do not choose among target profiles. | Unresolved; profile selection is not a probability-proportional race. |
| `P23_PROFILE_RETALIATION_LIMITED` | Retaliation authorization is 0.30 with confirmed-use x1.60; target choice is a flat 1.30. | Unresolved; limited retaliation preference is not target-scored. |
| `P23_PROFILE_RETALIATION_COUNTERVALUE` | Major target validity and exchange gate exist in triggers, but the AI score does not distinguish countervalue from military targets. | Unresolved; consequence ordering and safety are not proved. |

### First use, retaliation, and stand-down

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_FIRST_USE_TIER_800_BLOCKED` | First-use authorization is Evolution IV and chaos ≥1000 gated; tier 800 is below the source gate. | Source-blocked as named; MCP trace unavailable. |
| `P23_FIRST_USE_TIER_1000_STABLE_BLOCKED` | Severe first use additionally requires war, strategic losses ≥3, capital threat, front collapse, exhausted reserve, verified route, readiness ≥75, integrity ≥20, and a nuclear-major action target. | Source-blocked unless all hidden gate inputs are supplied; no probability result. |
| `P23_FIRST_USE_TIER_1000_SEVERE_RARE` | The scenario declares severe loss, capital threat, launch preparation, high readiness/integrity, and no stand-down, but does not explicitly declare all severe-gate flags. | Unresolved with incomplete fixture and source gate mismatch. |
| `P23_FIRST_USE_STANDDOWN_BLOCKED` | Moratorium and suspended orders block final authorization, but the full competing score pool was not engine-resolved. | Unresolved; source gates support blocking but no score-race result. |
| `P23_FIRST_USE_INVALID_TARGET_BLOCKED` | Generic action target validity and major-target triggers fail closed, but target-specific route/range and normalized candidate behavior were not inspected by MCP. | Unresolved fail-closed trace; no exact probability. |
| `P23_RETAL_CONFIRMED_USE` | Confirmed-use on-action opens major exchange; retaliation target is flat 1.30 and authorization is 0.30 with a 1.60 confirmed-use factor. | Unresolved score/timing; stale-target timeout safety remains a source concern. |
| `P23_RETAL_FALSE_WARNING` | Confirmed-use modifier is absent in a false-warning case, but no MCP comparison of hold, stand-down, and authorization was possible. | Unresolved. |
| `P23_RETAL_BROKEN_COMMAND` | Runtime rejects missing context, capability, stockpile, reservation, target, route, or terminal state; AI command-integrity sensitivity is not scored directly. | Unresolved; runtime fail-closed is source-only. |
| `P23_STANDDOWN_PRE_DETONATION` | Moratorium is 0.90 with restraint x1.35 when confirmed use is present; other hold/abort scores remain positive. | Unresolved score race. |
| `P23_STANDDOWN_AFTER_LIMITED_EXCHANGE` | No target/profile-aware stand-down score is present; event state and competing action pool were not engine-resolved. | Unresolved. |
| `P23_STANDDOWN_AFTER_COUNTERVALUE` | No countervalue-specific restraint factor is present in the AI scores. | Unresolved with missing consequence sensitivity. |

### Collapse and breakaway recovery

| Scenario | Source-side evidence | Result classification |
|---|---|---|
| `P23_COLLAPSE_RECALL_SECURE_ROUTE` | Recall is 1.10 and rail security is 0.90 with war x1.60; selected depot/route targets have no per-target score. | Unresolved target/timing race. |
| `P23_COLLAPSE_NEGOTIATE_STABLE_BREAKAWAY` | Joint custody is 1.00 and breakaway custody is 1.30; stability and custody value are not target factors. | Unresolved; no preference or starvation result. |
| `P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION` | Recovery raid is 0.20 with imminent x1.80; disable devices is 1.40 with imminent x2, but target ranking is flat. | Unresolved score race; unsafe repetition/dominance cannot be measured. |
| `P23_COLLAPSE_TINY_UNSTABLE_BREAKAWAY` | No size or stability modifier appears in breakaway target decisions or the operationalization mission score. | Unresolved with missing target-aware weighting. |
| `P23_COLLAPSE_OPERATIONAL_SUCCESS` | Breakaway operationalization has a 0.20 non-selectable mission score and activation gates for technical access/local delivery; no engine timing or repeat trace was available. | Unresolved mission timing and repetition. |

## Findings for the parent patch owner

1. **MCP blocker, critical.** Restore the callable `hoi4.probability_inspect` route before any balance patch, then rerun the same named scenario IDs. Until that happens, this handoff is not an engine baseline.

2. **Missing target-aware weighting, high.** Add or expose a target scorer for the 12 target-bearing decisions listed above. The scorer should use the complete eligible pool and consistently account for target validity, actual route/range, war relation, nuclear-major status, custody, strategic value, foreign support, target profile, and stale/terminal state. Do not normalize a pool until every candidate is present and invalid candidates are zero or excluded.

3. **Evolution III gate mismatch, high.** `event_evolution_iii_world_gate` does not open from two nuclear majors alone in the peaceful-rival scenario. Either the source gate or the scenario contract must be aligned, and the resulting transition must be re-evaluated with `P23_EVO3_MAJOR_RIVAL_NORMAL` and `P23_EVO3_ENEMY_USE_ACCELERATED`.

4. **Evolution IV gate mismatch, high.** `event_evolution_iv_world_gate` does not accept enemy launch-prep verification alone. Align `P23_EVO4_COLLAPSE_ACCELERATED` with the trigger, or add the intended launch-prep opening route and re-test the blocked and collapse cases.

5. **Moratorium is delay-only, high.** `event_can_enable_evolution_i` through `event_can_enable_evolution_iv` do not explicitly reject `atomic_moratorium`; the 1.50 MTTH factor cannot guarantee a safe skip. Decide whether moratorium is a hard gate or only a delay and scenario-test both pulse timing and recovery.

6. **First-use fixture and veto scope, high.** `event_severe_first_use_gate` requires more inputs than the named severe scenario declares, and `sov_nuclear_bombs_overrule_safety_veto` remains positively weighted in any war when visible, with only a severe-gate boost. Make the scenario fixture complete and ensure the veto/final-authorization scores are profile-specific if strict first-use rarity is intended.

7. **Route and stale-target risk, high.** `event_has_delivery_route` checks a broad bomber/airbase capability rather than per-target reachability. Retaliation timeout execution also needs a fresh major-target, war, exchange, route, and terminal-state recheck before release; generic runtime fail-closed checks do not prove the full retaliation gate.

8. **Static response and test pools, medium.** The six `.120` response bases and the 70/20/10 test pool ignore the scenario inputs that are expected to change their outcomes. Add explicit factors or revise the scenario contract, then use `probability_sweep` for sensitivity and rank reversals.

9. **Mission semantics, medium.** Keep mission scores separate from click probability. Recheck every activation path, especially `sov_nuclear_bombs_breakaway_operationalization_mission`, for actor validity, crisis state, local capability, cleanup, timeout, and duplicate activation.

10. **External strategy factors unresolved.** No Event 23-specific `common/ai_strategy` source or `ai_strategy` reference was found in the reviewed surface. Confirm whether strategy factors are intentionally absent or supplied by a broader adapter/source; this could not be tested without MCP.

## Skipped analyses and remaining uncertainty

- `hoi4.probability_evaluate`: skipped after the required opening inspect failed; no named scenario was accepted by the engine adapter.
- `hoi4.probability_sweep`: skipped because the route was unavailable and no owner-approved tuning range was supplied.
- `hoi4.probability_compare`: skipped because this is a pre-patch audit and the route was unavailable; there is no before/after candidate.
- `hoi4.probability_render`: skipped because no current analysis id or result exists to render.
- `hoi4.probability_simulate`: skipped because no explicit uncertain-input distribution or seed contract was provided, and the route was unavailable.
- `hoi4.probability_sequence`: skipped because no complete custom pool manifest with cadence, state transitions, cooldown, recovery, cap, removal, reset, and terminal states was available to the adapter.
- `hoi4.event_inspect` and `hoi4.event_render`: skipped after the callable structural route failed with `TypeError: tools.mcp__hoi4_agent_tools__hoi4_event_inspect is not a function`.

The source review is complete for the listed weighted surfaces. Engine-backed timing, normalized event-option probabilities, decision/mission rank order, target choice, repetition, starvation, dominance, and snowball severity remain unresolved until the MCP tools are callable. No patch, comparison, or engine-completion claim is made.
