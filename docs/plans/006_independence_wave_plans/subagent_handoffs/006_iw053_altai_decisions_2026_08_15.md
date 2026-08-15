# IW-053 ALT decision category and project handoff — 2026-08-15

## Disposition

The package-local ALT decision category, founding mission, and ten serialized project decisions are implemented in the two owned decision files. The source remains fail-closed behind the ALT package and identity-rights contract; no central admission, attestation, Join, shared-constant, focus, localization, asset, or vanilla file was changed by this handoff.

The source is structurally complete for the requested decision surface, but runtime admission remains blocked by the parent-owned IW-053 identity, flag, portrait, Event 005 collision, force-contract, and typed probability gates documented by the package audit handoffs.

## Changed files

- `common/decisions/categories/006_independence_wave_altai_categories.txt` adds the package-local `independence_wave_altai_mountain_compact_category` category and repeats the ALT identity-rights gate in its visibility block.
- `common/decisions/006_independence_wave_altai_decisions.txt` defines the founding mission and ten ALT project decisions listed below.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw053_altai_decisions_2026_08_15.md` records this implementation, validation, and blockers.

No other files were edited in this decision tranche.

## Exact decision identifiers

| Surface | Identifier |
| --- | --- |
| Category | `independence_wave_altai_mountain_compact_category` |
| Founding mission | `independence_wave_altai_hold_mountain_council` |
| Project 1 | `independence_wave_altai_secure_oyrot_depots` |
| Project 2 | `independence_wave_altai_integrate_mountain_guards` |
| Project 3 | `independence_wave_altai_register_communities` |
| Project 4 | `independence_wave_altai_settle_former_host_ledgers` |
| Project 5 | `independence_wave_altai_ratify_constitutional_autonomy` |
| Project 6 | `independence_wave_altai_adopt_traditional_compact` |
| Project 7 | `independence_wave_altai_convene_socialist_councils` |
| Project 8 | `independence_wave_altai_establish_emergency_command` |
| Project 9 | `independence_wave_altai_codify_durable_sovereignty` |
| Project 10 | `independence_wave_altai_open_frontier_network` |

The ten project IDs exactly match `has_independence_wave_altai_active_package_project` in `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt`.

## Before and after behavior

Before this tranche, the ALT package had no owned category or project decision surface available for the package-local setup contract.

After this tranche, the category is visible only for the exact ALT package with the IW-053 setup flag and identity-rights clearance. The founding mission activates only through `is_independence_wave_exact_package_iw_053_runtime_ready`, with the state-654 Oyrot anchor, state-654 capital, valid former-host target, complete setup, and current force generation all present. The mission has a founding-crisis timeout, success resolution, failure effect, anchor/capital cancellation, and force-generation cancellation.

The ten projects are mutually serialized through `has_independence_wave_altai_active_package_project`, use `is_independence_wave_altai_project_ready`, require the state-654 anchor and state-654 capital in each `available` block, expose shared cost text, charge the shared Event 006 payment effect on selection, and resolve through the exact ALT effect helpers already provided by the package effects file.

Every timed project cancels when the ALT package or route prerequisite is withdrawn, the compact has failed, state 654 or the capital is lost, or the force-package generation no longer matches. Cancellation applies the package-local one-time failure effect while preserving the existing cleanup and idempotence guard in `independence_wave_altai_apply_project_failure`.

## Decision category lifecycle notes

The category is fail-closed on `is_independence_wave_altai_package`, `has_independence_wave_altai_identity_rights_clearance`, and `independence_wave_iw_053_setup_complete`. It does not add central dispatch or admission authority.

The founding mission uses `available = { always = no }` as an activation-backed mission, matching the accepted YAK/BYA package pattern. Its activation also calls `is_independence_wave_exact_package_iw_053_runtime_ready`, so the former-host pointer is validated against the complete ALT setup contract before the mission is created. It times out at `constant:independence_wave_altai_duration.founding_crisis` and marks the compact crisis failed on timeout or non-success cancellation.

The mission resolves successfully only when both ALT compact ledgers are stable, a route government is installed, state 654 remains owned and controlled, and the capital remains state 654 and controlled by ALT. All other package, anchor, capital, and generation losses use the failure branch.

## Mission quality notes

| Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ALT / IW-053 | `independence_wave_altai_mountain_compact_category` | State 654 Oyrot Region with ALT capital at 654 and a valid former-host variable | Exact ALT package, identity-rights clearance, IW-053 setup, state-654 ownership/control, state-654 capital, former-host variable, unresolved compact crisis | `constant:independence_wave_altai_duration.founding_crisis` | Stable Council Cohesion and Mountain Guard Readiness, one installed route government, state 654 retained, capital still 654 | Set `independence_wave_altai_compact_crisis_failed` and call `independence_wave_altai_apply_project_failure` once | No repeatable success path; mission activation and crisis flags prevent duplicate founding resolution |

The mission does not itself spend resources. The ten projects carry the material costs and the one-active-project lock, so the mission cannot become a passive political-power exchange.

## Project parity, costs, and durations

All ten projects have `visible`, `available`, `custom_cost_trigger`, `custom_cost_text`, `days_remove`, `complete_effect`, `remove_effect`, `cancel_trigger`, `cancel_effect`, and `ai_will_do` blocks.

| Project | Cost family | Duration | Completion helper |
| --- | --- | --- | --- |
| `independence_wave_altai_secure_oyrot_depots` | ALT administration light | `constant:independence_wave_decision_duration.short` | `independence_wave_altai_focus_secure_oyrot_depots` |
| `independence_wave_altai_integrate_mountain_guards` | Shared security standard | `constant:independence_wave_decision_duration.standard` | `independence_wave_altai_focus_integrate_mountain_guards` |
| `independence_wave_altai_register_communities` | ALT administration standard | `constant:independence_wave_decision_duration.standard` | `independence_wave_altai_focus_register_altai_communities` |
| `independence_wave_altai_settle_former_host_ledgers` | Shared diplomatic standard | `constant:independence_wave_decision_duration.long` | `independence_wave_altai_focus_settle_former_host_ledgers` |
| `independence_wave_altai_ratify_constitutional_autonomy` | ALT administration light | `constant:independence_wave_decision_duration.short` | `independence_wave_install_altai_constitutional_government` plus administrative progress |
| `independence_wave_altai_adopt_traditional_compact` | Shared diplomatic standard | `constant:independence_wave_decision_duration.long` | `independence_wave_install_altai_traditional_government` plus diplomatic progress |
| `independence_wave_altai_convene_socialist_councils` | ALT administration light | `constant:independence_wave_decision_duration.short` | `independence_wave_install_altai_socialist_government` plus administrative progress |
| `independence_wave_altai_establish_emergency_command` | Shared security major | `constant:independence_wave_decision_duration.standard` | `independence_wave_install_altai_emergency_government` plus security progress |
| `independence_wave_altai_codify_durable_sovereignty` | ALT strategic | `constant:independence_wave_decision_duration.strategic` | Durable-sovereignty flag plus major settlement |
| `independence_wave_altai_open_frontier_network` | Shared diplomatic standard | `constant:independence_wave_decision_duration.long` | `independence_wave_altai_focus_open_altai_frontier_network_corridor` |

The decision-local civilian factory burden uses `@CR_SC_INDEPENDENCE_WAVE_ALT_CIVILIAN_FACTORY_USE = 1` only where the existing ALT cost palette requires a factory modifier. The payment and affordability helpers remain shared or ALT-specific as already defined in the package contract; no new magic cost values were introduced here.

## AI validity and route locks

The project AI uses the shared `independence_wave_decision_ai` constants with urgent weights for the founding mission and emergency command, high weights for core recovery and route installation, standard weights for diplomatic and network work, and war multipliers on guard and emergency projects. These are willingness scores, not claimed click probabilities.

The four government projects are mutually exclusive through their route triggers and `has_independence_wave_altai_route_government`. Durable sovereignty requires a resolved founding crisis, stable ledgers, a completed founding settlement, and an installed route. The frontier network requires the founding settlement, resolved crisis, Network membership, League route availability, stable ledgers, and an unopened corridor flag.

The former-host project has both peaceful-living-host and local-unsettled-host paths. Peaceful settlement requires the host not to be at war with ALT. The local fallback requires the exact ALT depots-secured and unsettled-host gates. A host-war cancellation may still resolve locally through the package helper only when the fallback gate is valid.

No route in this tranche creates a war goal, annexes territory, grants cores, creates a free unit loop, or bypasses the package's host and state gates.

## Localisation and tooltip coverage

No localization file was edited by this tranche. The concurrent ALT localization handoff `006_iw053_altai_localisation_2026_08_15.md` records the category, mission, ten project names/descriptions, twelve effect/failure tooltip keys, and shared cost-key coverage.

Static comparison of the final decision source against `localisation/english/006_independence_wave_altai_l_english.yml` and the shared Event 006 decision localization found no missing `name`, `desc`, `custom_effect_tooltip`, or `custom_cost_text` key for the owned decision surface.

No dedicated scripted GUI is introduced or owned by these decisions, so the mandatory `hoi4.gui_inspect` and `hoi4.gui_render` route is not applicable to this ordinary decision category. The installed MCP has no read-only decision-category rendering route; visual text overflow remains parent/user-owned and unverified.

## Cleanup and exploit-risk notes

`independence_wave_altai_begin_project` clears the one-time failure guard when a new project begins. `independence_wave_altai_apply_project_failure` applies the shared country deltas and ALT ledger losses only once per active project or failure path.

The active-project trigger lists all ten project IDs, so a second paid project cannot start while one is running. Completion flags, route-government flags, durable-sovereignty state, and the network-corridor flag prevent repeat success rewards. The project cost is charged in `complete_effect` before the timed effect resolves, while cancellation and timeout use the package-local failure helper rather than refunding a spent cost.

Generation-safe cancellation is present in all eleven `cancel_trigger` blocks, including the founding mission and all ten projects, through `NOT = { has_independence_wave_force_package_for_current_generation = yes }`. State-654 ownership/control and state-654 capital gates are present in the category lifecycle, mission activation/success, and every project `available` block.

## Issue list sorted by severity

1. **Blocking runtime admission:** ALT identity-rights clearance is intentionally unset until the parent accepts the exact released identity, portraits, and flag/symbol provenance. The category and all decisions fail closed without `independence_wave_iw_053_identity_rights_cleared`.
2. **Blocking runtime admission:** Existing IW-053 package audits retain unresolved Event 005 Soviet-origin collision/protected-remnant semantics. Central dispatch, attestation, preflight, scenario, and Join were not widened here.
3. **Blocking package setup:** The accepted IW-053 force mapping records military tradition 61, while the shared p61 constant currently exposes 57. The ALT package trigger/effect contract remains parent-owned and no shared-constant change was made.
4. **Unresolved AI balance evidence:** The mandatory custom `chaosx_ai_probability_auditor` route was not available in this subagent context. Direct HOI4 MCP inspection and evaluation were run, but the empty fixture cannot establish valid campaign ranking, dominance, starvation, or timing.
5. **Visual evidence limitation:** The installed MCP exposes no decision-category inspect/render route, and no dedicated scripted GUI exists in this scope. Decision text overflow remains unverified.

## Probability and static validation

The required first weighted-surface call was run against `common/decisions/006_independence_wave_altai_decisions.txt` with adapter `mission_ai_will_do` and the eleven-candidate pool consisting of the founding mission plus all ten projects.

The final `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = true`, 11 candidates, 16 required inputs, 0 unresolved inspect items, and 0 available candidates in the empty MCP fixture. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3102639cb0e6e25efe236c132209001ea80b4d829606cc3a7ff9156e6ec21612/8abe27197891049c3423c6ba0282246ded8f467d74eec235c6e3bebf9c38efcf/probability-inspect-d1de3befb888.json`.

Direct `hoi4.probability_evaluate` against named scenario set `E6_IW053_ALT_PACKAGE_EMPTY_FIXTURE_2026_08_15` and scenario `ALT_EMPTY_PACKAGE_FIXTURE` returned `PROBABILITY_ANALYZED_PARTIAL` for all 11 candidates with 146 unresolved or bounded items. The adapter reported all candidates never eligible in the empty state, which is an expected fixture result rather than proof of dead source. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46a2dd8be9ba041eae961aee357fae8e4223a0c617e4855baac95c30685272e5/0fd17f5f73dc0eb7953cd31f5cc35d4cc43e01e61dfe5a17f9e868c64e09bd13/probability-eefa221bbd7b1ea8d422f2cc.json`.

The required sweep attempt used the same source, candidate pool, named scenario, and `has_war` path with rank-reversal and pairwise analysis requested. It returned the exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` because every sweep path needs a declared scenario range, numeric alternatives, or numeric state value. No sweep balance claim is made.

Static reference checks found all ten project IDs in both the decision source and ALT active-project trigger, all decision effect calls defined in the ALT or shared scripted-effects files, all player-facing names/descriptions/tooltips/cost keys localized, 14 explicit state-654 capital gates, 14 explicit state-654 ownership/control gates, 11 generation cancellation guards, 11 cancellation blocks, and balanced braces.

## Skipped meaningful validation

- A true `chaosx_ai_probability_auditor` audit and before/after `hoi4.probability_compare` were skipped because the custom auditor route and an approved pre-change source snapshot were unavailable. The direct MCP receipts above are evidence of source discovery and bounded empty-fixture behavior only.
- A typed multi-scenario probability evaluation and sweep were skipped because no parent-approved ALT runtime fixture can truthfully satisfy the still-blocked identity, host, force-contract, and central-admission gates.
- Live HOI4 execution and save-state validation were not attempted because they belong to the parent/user workflow.

## Recommended parent follow-up

1. Keep the package fail-closed until identity-rights, exact opening identity, flag/symbol, portrait, Event 005 collision, and force tradition gates are accepted.
2. After those gates are resolved, supply typed ALT probability fixtures covering fragile ledgers, host war, route locks, emergency route, network readiness, durable sovereignty, state-654 control, capital control, cost affordability, and active-project state.
3. Rerun the same eleven-candidate inspect/evaluate/sweep pool through `chaosx_ai_probability_auditor`, then compare any AI changes with a real pre-change source revision.
4. Preserve the category and decision files as package-local and add central dispatch/attestation/Join entries only through the separately owned parent admission plan.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was introduced in the owned decision files. The remaining omissions are intentional parent-owned admission and evidence gates, not substitutes for the requested category, mission, project, cost, duration, route, cleanup, or cancellation behavior.
