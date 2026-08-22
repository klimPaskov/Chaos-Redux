# Famine and migration decision and mission audit handoff

Status: decision-owned source is implemented and structurally audited. The work remains uncommitted as requested. Localisation, assets, workbook, shared GUI, event pool, and owner systems were not edited.

## Changed files

- `common/decisions/categories/famine_migration_categories.txt` contains the ordinary `chaosx_famine_migration_category` declaration only.
- `common/decisions/famine_migration_decisions.txt` contains the matching top-level category block, three missions, and all 26 accepted decision-map IDs.
- `common/script_constants/famine_migration_constants.txt` contains decision timing, threshold, AI, and outcome tuning used by the decision source. This file is shared with the architect-owned contracts and must be reviewed together at merge time.
- This handoff is the required documentation output. No commit was created.

## IDs and matrix coverage

The source covers all 26 CSV working IDs: `fm_release_reserves`, `fm_emergency_imports`, `fm_repair_relief_route`, `fm_escorted_relief_convoy`, `fm_emergency_airlift`, `fm_invite_relief`, `fm_famine_evacuation`, `fm_requisition_safer_state`, `fm_conceal_crisis`, `fm_maintain_extraction`, `fm_prepare_evacuation`, `fm_evacuate_vulnerable`, `fm_evacuate_workers`, `fm_open_departure_routes`, `fm_restrict_departure`, `fm_negotiate_corridor`, `fm_open_reception`, `fm_controlled_medical_reception`, `fm_distribute_arrivals`, `fm_transit_only`, `fm_close_border`, `fm_enforce_closure`, `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation`.

The category lifecycle is campaign-hidden, evidence-derived emerging, active management, resolution, and dormant retirement. Emerging visibility requires sustained food exposure/incidents or a large flight/trapped cohort and has no bare first-registration flag alternative. Active transitions clear emerging, resolution transitions clear active, and integration retires to dormant only when reception load and owned food/displacement registries are empty. The category uses `GFX_fm_cat_displacement`, `GFX_fm_pic_displacement`, and the central category priority constant.

The normal decision surface uses state targets and map highlights. It exposes the accepted action families rather than a new scripted GUI. The source has three non-selectable active missions: `fm_mission_secure_relief_route`, `fm_mission_hold_humanitarian_corridor`, and `fm_mission_prevent_reception_collapse`.

## Costs, formulas, and cooldowns

Decision durations, re-enable timers, mission timeouts, category priority, reveal thresholds, route shares, forced-return hazard shares, relief fractions, AI weights, and stability or war-support outcomes are centralized under `famine_migration_decision_timing`, `famine_migration_decision_threshold`, `famine_migration_decision_ai`, and `famine_migration_decision_outcome` in `common/script_constants/famine_migration_constants.txt`.

Every visible decision has at most four spendable cost families. Political power is paired with equipment, fuel, aircraft experience, or policy-specific material where appropriate. Existing cost localisation uses texticon-backed keys owned by the localisation worker. The airlift requirement now has a custom trigger tooltip for the aircraft commitment; representative target, effect, and transfer custom tooltips are wired in the decision source.

Normal relief uses bounded fractions of current food pressure. Border closure registers only the selected persisted cohort and applies `resolved_amount * trapped_cohort_share`; it does not mark a broad percentage of every owned state as trapped. Closure then applies shared famine pressure, stability/war-support consequences, the trapped modifier path, and relief-obstruction condemnation after a proven result. Enforcement owns coercive movement, the forced-displacement death reason, violent-pushback condemnation, and its achievement evidence.

Forced-return route deaths are population-scaled. The requested cohort slice is `resolved_amount * transfer_share`, the route-death share starts at the centralized base share, adds destination-origin food, persecution, bombing, contamination, and unsafe-route factors, and is clamped to the centralized maximum before the exact transfer. There is no fixed route-death total.

## Exact transfer call sites and ledger use

Each of the following calls `famine_migration_transfer_civilians_exact = yes` exactly once and consumes the returned ledger values: `fm_famine_evacuation`, `fm_evacuate_vulnerable`, `fm_evacuate_workers`, `fm_distribute_arrivals`, `fm_transit_only`, `fm_enforce_closure`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation`.

The ordinary evacuation consumers select an adjacent safe destination, debit source flight pressure by `famine_migration_transfer_actual_origin_debit`, record the cohort with `famine_migration_transfer_survivor_credit`, and add only actual survivor credit to destination reception load. Distribution is a state-to-state inland movement and transit is a confirmed onward movement; neither is a reception-load-only substitute. Return decisions resolve the persisted cohort origin through `famine_migration_resolve_cohort_origin`, fail closed without a valid stored origin, and never select a random neighbor as a return target.

All movement routes use food, route, persecution, bombing, contamination, controller, border-policy, reception, and actor proof where the route family requires it. Actual route deaths are consumed from the exact-transfer return and never credited as survivors. Forced-return and closure effects call the parent condemnation adapters only after a valid exact transaction. Selected cohort pointers and temporary route proofs are cleared on successful movement or cancellation; close/enforce policy-selection flags are cleared on cancellation.

## Achievement evidence wiring

Completed escorted convoy and airlift relief can record blockade relief after pressure is actually reduced. Corridor negotiation records a proven gate crisis and corridor start after the trapped-population transaction, while the corridor mission records completion only on mission success. Controlled medical reception records medical reception only after the reception-capacity contract returns success, and the reception mission records safe reception only when overload is absent. Exact movement destinations record arrival and gate protection only after actual transfer, and integration records a durable outcome only inside the empty-load/no-active-registry retirement proof. Voluntary return records return evidence after a valid exact transfer; extraction suspension/recovery evidence is tied to completed relief; forced return and violent pushback evidence are tied to completed exact transactions.

## AI pools and scenario mapping

The source exposes the 26 decision candidates to the `decision_ai_will_do` adapter and the three mission candidates to the `mission_ai_will_do` adapter. AI bases and factors are all `constant:famine_migration_decision_ai.*`; no decision source `base =` or `factor =` contains an uncentralized numeric tuning value. State and country validity conditions are shared with the player path, including persisted cohort ambiguity guards and route safety checks.

The required later read-only compare scenarios are `prob_famine_relief_dense`, `prob_famine_relief_blocked_island`, `prob_soviet_extraction`, `prob_humanitarian_border`, `prob_capacity_exhausted_border`, `prob_outbreak_reception`, `prob_nuclear_evacuation`, `prob_genocide_escape`, `prob_authoritarian_pushback`, `prob_destination_selection_internal`, `prob_destination_selection_persecution`, `prob_corridor_acceptance`, `prob_forced_return`, `prob_integration`, `prob_opposition_channel`, `prob_disaster_flight`, `prob_bombing_exodus`, `prob_requisition_donor`, `prob_relief_donor`, and `prob_cleanup`.

## MCP evidence

- Probability source discovery after the final decision edits: `PROBABILITY_SOURCE_DISCOVERED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/824fbca7673608e8cb019c3b25d4101d8497c6109d0f66246bfd20785efd8189/537a4970ef837d99c949ab697a3506b9d027bff51f3c72d3fb6d2d2e0c543f87/probability-inspect-59e1d1ff03fa.json`.
- Full 26-candidate mission adapter inspection: `PROBABILITY_SOURCE_INSPECTED`, pool complete, 26 candidates, 11 required inputs, and zero unresolved inspection inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a28ec3ffb8aa662c465a7809c7071fb7092d51b23072f98ac803bb13f5bad6a0/bdeb5bb1af068d14c46484a06891e739af6e78431be2c2621f7f9c588b06a689/probability-inspect-59e1d1ff03fa.json`.
- A one-scenario, 26-candidate probability evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with 84 explicit unresolved or bounded analysis items and six informational modifier-coverage diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/496de96540b12819ebf9549276020d70a9882fd0cedf45b4f67f86b0072fd816/2124c32d3494a1df30398a6af7954b5992ca6e669b3b1adde30a6fdf33fcc821/probability-045ca8617df41e84a8cc1d5f.json`.
- The required 20-scenario evaluation was attempted with the documented object-shaped `scenarioSet` and timed out after 180 seconds. The exact blocker is `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: timed out awaiting tools/call after 180s`; this is not treated as a completed 20-scenario balance audit.
- The mandatory ordinary decision GUI inspection used `decision_view` with scenario `famine_migration_category` and returned `GUI_INSPECTED`, but the shared graph was dominated by unrelated repository-wide diagnostics and truncation. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0d7834193c9556b79c25cb981271f1d5befb263e03f14d42f0cc0a53d0c5af1/3e8da763443f484744b96d84323d26da9646ba10694c0f8c357f0fa07f01b7a1/gui-inspect.4ba915d232717fac.json`.
- The corresponding read-only GUI render returned `GUI_RENDERED` with a linked `decision_view-full.svg` artifact. No GUI rewrite was requested or performed because the category deliberately uses the ordinary decision surface.

## Audit findings and remaining risks

Severity high: third-country resettlement currently calls the regular destination-bind contract after the exact movement. The architect contract accepts only `active` rows, while a persisted inbound cohort is normally `destination_bound`; the forced bind contract is intentionally coercive and must not be substituted for safe resettlement. This requires an architect-side safe rebind/update contract before the resettlement path can be considered fully engine-proven.

Severity high: full 20-scenario probability evaluation and before/after comparison remain blocked by the MCP timeout and the absence of an owner-approved pre-patch baseline artifact. The one-scenario partial result is evidence of source discovery and modifier parsing, not a balance acceptance claim.

Severity medium: route selection in ordinary movement actions is fail-closed through the exact transfer contract, but several `event_target:famine_migration_route_destination` post-processing blocks rely on the selected route existing in the same effect chain. The regular target lifetime prevents cross-chain persistence, but a focused runtime lint should verify missing-target handling after route loss.

Severity medium: the ordinary decision category still relies on shared vanilla decision rendering for its values and action density. No new GUI was added, so the one-primary/two-supporting-value presentation must be checked by the parent against final localisation and the shared decision window.

Severity medium: mission timing and rewards are centralized, but the three missions use shared country/state activation rather than a named regional object. Parent review should confirm that the selected-state activation is sufficient for the intended region semantics.

No world-wide daily, weekly, or monthly scan, event ID, event pacing hook, shared scripted GUI, or population-creation fallback was added. Live gameplay validation remains intentionally skipped because the repository instructions assign live consumer testing to the user.

## Validation performed

The decision source has equal braces (`1230` opening and `1230` closing), the category has equal braces (`25` and `25`), the top-level category root is `chaosx_famine_migration_category`, and all 26 decision IDs plus three mission IDs are present. There are nine exact-transfer call sites and no country-scope use of the state-only displacement flag. A numeric audit found only file-scoped `@` cost/resource definitions in the decision source; AI bases and factors are constant-backed. The final source includes four prepared custom tooltip consumers and the delivered action icon family, category icon, and category picture.

Skipped meaningful validation: in-game execution, live save testing, and a completed 20-scenario probability compare remain pending the parent/user workflow and the recorded MCP blocker. No localisation or asset source was modified by this subagent.
