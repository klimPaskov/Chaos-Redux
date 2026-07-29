# Event 006 shared dynamic-systems closure

Date: 2026-07-29

Scope: shared Event 006 decisions, missions, decision triggers/effects, rival-bloc triggers/effects, ideas, and directly used Event 006 constants.

## Static-evidence conclusion

The shared country values, former-host, patron, Network, League, and rival-bloc systems are source-complete for the user's static-evidence acceptance decision.

Each has an initializer, a player-facing or gameplay reader, bounded writers, central thresholds, a recompute or clamp path, and origin-generation cleanup.

No source-only blocker remains in the owned surfaces after the narrow cost-contract fix below.

This is not a claim of live balance or UI-runtime proof; the parent explicitly excluded live/in-game evidence from this closure.

## Patch applied

Changed file:

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`

Changed identifier:

- `can_pay_independence_wave_security_standard_cost`

Before: the availability/custom-cost predicate required Command Power, while `independence_wave_decision_pay_security_standard` did not spend Command Power and `independence_wave_cost_security_standard` did not disclose it.

After: the predicate requires only the manpower, Army Experience, infantry equipment, and support equipment that the payment effect removes and localisation describes.

Affected call sites: `independence_wave_integrate_militias`, `independence_wave_form_border_guards`, `independence_wave_sponsor_coup`, `independence_wave_integrate_settled_regions`, and `independence_wave_integrate_formable_region`.

## Shared-system crosswalk

| System | Initialization and visible reader | Gameplay writers, costs, timing, and AI | Thresholds, lifecycle, clamp/recompute, and generation cleanup |
| --- | --- | --- | --- |
| Active origin/country | `independence_wave_prepare_country_origin` records the generation, former host, baseline values, route state, and Network standing. Categories read `is_independence_wave_active_country`; the founding category exposes `independence_wave_status_scripted_gui`. | Focuses use `independence_wave_focus_apply_value_bundle`; evolutions use their named country-value effects; decisions and missions use `independence_wave_decision_apply_country_deltas`. Decision durations/cooldowns/AI bases are centralised in `006_independence_wave_decision_constants.txt`. | `independence_wave_refresh_country_state` calls `independence_wave_clamp_country_values`, phase refresh, patron refresh, idea refresh, GUI-frame refresh, and achievement refresh. `independence_wave_end_active_origin` calls shared decision and rival cleanup before reset. |
| Legitimacy | Initialised in `independence_wave_prepare_country_origin`; read by phase triggers and government/formable availability. | Written by focus/evolution bundles and the shared decision-delta helper, including mission success/failure. No direct political-power store exists in the owned decision surfaces. | Bands `provisional`, `established`, `entrenched`, and `foundational` are in `006_independence_wave_mechanics_constants.txt`; government/identity ideas are refreshed by `independence_wave_refresh_government_idea` and `independence_wave_refresh_identity_idea`; country clamp and origin reset apply. |
| Recognition | Initialised with the origin; read by `is_independence_wave_recognized_or_later`, recognition/patron/Network/formable categories, and diplomacy target gates. | Written by focus/evolution bundles, recognition decisions, former-host outcomes, patrons, and Network/League actions through the same country-delta helper. | Observed/de-facto/treaty/entrenched bands are central constants; `independence_wave_refresh_recognition_idea`, country clamp, and origin reset apply. |
| Capacity | Initialised from territory and archetype adjustments; read by provisional/regional-power gates, treasury/public-works availability, and formable integration. | Written by focus/evolution bundles, country decisions/missions, territory actions, and formation completion through the shared helper. | Functioning/institutional/capable/mature bands and phase gates are central constants; `independence_wave_refresh_command_idea`, country clamp, and reset apply. |
| Security | Initialised from force, territory, and archetype adjustments; read by security missions, border operations, severe-instability checks, and regional-power gates. | Written by focus/evolution bundles and security mission success/failure. Standard security costs now exactly match payment and localisation. The only `create_unit` path is the emergency-formations helper, gated by `independence_wave_force_package_applied` and `independence_wave_emergency_units_raised`, then removed by decision cleanup. | Guarded/organised/prepared/formidable bands are central constants; `independence_wave_refresh_command_idea`, country clamp, and reset apply. No free-unit repeat loop was found. |
| Instability | Initialised from territory/archetype and force start; read by `has_independence_wave_severe_instability`, action availability, and the status GUI. | Written by focus/evolution bundles plus explicit mission success/failure and settlement/patron/League outcomes via the shared helper. | Strained/volatile/severe/critical bands are central constants; `independence_wave_refresh_instability_idea`, country clamp, and reset apply. |
| Former host | `independence_wave_prepare_country_origin` saves `independence_wave_former_host` and starts the eight host-relation values. Host categories and `is_independence_wave_former_host_target` only expose valid, living host relations. | Host, property, citizenship, claims, autonomy, forced-recognition, and reclamation decisions use `independence_wave_decision_apply_host_deltas`; target checks reject invalid/dead hosts and unsafe war states. | Host values are clamped by `independence_wave_clamp_host_relation_values`; ledger alignment uses `independence_wave_sync_former_host_ledger`. `independence_wave_cleanup_former_host_relationship` and `independence_wave_handle_former_host_death` remove stale state before origin reset. |
| Patron ledger | Empty ledger starts in `independence_wave_prepare_country_origin`; patron category and strongest-patron idea read current valid rows. | Patron decisions register/reduce channels through `independence_wave_decision_register_targeted_patron_channel`, `independence_wave_decision_reduce_targeted_patron_influence`, and patron-effects ledger helpers; resource costs are custom-cost predicates paired with named payment effects. | Rows clamp through `independence_wave_clamp_patron_row`, stale/dead rows are pruned by `independence_wave_prune_patron_ledger`, strongest patron refreshes the idea, and `independence_wave_clear_patron_ledger` is called for reset. |
| Network | Origin sets `independence_wave_network_standing` to `independence_wave_network.standing_start`; Network category and rival eligibility require Network membership/standing. | Network-recognition/cadre/reserve/arbitration actions, focus/evolution calls, and League transitions use `independence_wave_change_network_standing` and member-registration helpers. Targeted actions validate living countries, routes, memberships, and target loss. | Standing clamps in `independence_wave_change_network_standing`; member arrays reconcile through `independence_wave_reconcile_network_registry`; League transitions deliberately unregister/re-register members. Origin termination invokes `independence_wave_reconcile_registries` before reset. |
| League | `independence_wave_initialize_league_values` creates global cohesion and other public League values when a League is formed; League category reads member/founder/phase flags and a valid leader target. | Congress, pillar, leadership, expulsion, charter, rival pressure, focus, and evolution effects call `independence_wave_decision_apply_league_deltas` or `independence_wave_change_league_values`; the actions carry central durations, cooldowns, target checks, and AI weights. | `independence_wave_clamp_league_values`, founder/member reconciliation, confidence recalculation, phase flags, split/reform/dissolve transitions, and member unregister helpers cover the lifecycle. Origin cleanup removes the departing country and reconciles the registry. |
| Rival bloc | `independence_wave_rival_bloc_initialize_runtime` establishes runtime state only on an eligible Network split. Rival actions read contract generation, member arrays, leader, Network standing, and exclusion from the main League. | Invite/accept/decline, reserve, host coordination, patron balancing, leadership challenge, and leave-contract actions have resource payment effects, deadlines/cooldowns where applicable, AI blocks, and target/route checks in `006_independence_wave_rival_bloc_triggers.txt`. | `independence_wave_rival_bloc_reconcile_registry` removes stale/dead/reused rows and selects a leader. `independence_wave_rival_bloc_cleanup_for_origin`, `independence_wave_rival_bloc_dissolve_contract`, and reunification remove pending invitations, targets, flags, arrays, and contract values. |

## Mission and decision quality notes

- Base shared file: 17 mission timeouts and 17 timeout effects. Every owned mission has a cancellation path appropriate to origin loss, route loss, target loss, or failure state. `independence_wave_cleanup_decision_layer` removes all 17 base missions and active/cooldown treasury work during origin teardown.
- Rival file: three missions, each with a timeout effect; invitation response clears its pending target/activation on deadline, while reserve and leadership actions cancel on membership/route loss. Rival cleanup handles the remaining contract state.
- The owned categories are action/milestone surfaces rather than passive political-power stores. A scoped search found no political-power operation in the base/rival decision or effect files.
- Costs and durations use the shared Event 006 decision and rival-bloc script constants. The standard-security mismatch was the only concrete cost contract defect found and is patched above.
- Target and route validity are checked by `is_valid_independence_wave_patron_target`, `is_valid_independence_wave_network_target`, `is_independence_wave_former_host_target`, League membership/array checks, and rival contract-generation checks. No dead-target or closed-route action remained in the reviewed surfaces.
- All reviewed player-facing complex requirements use custom-cost or custom-trigger text. No new localisation was required by the predicate-only correction because it removes an undisclosed requirement.

## Static validation and artifacts

- Confirmed the fixed standard-security predicate, the named payment effect, and the cost localisation describe the same four resource types at all five shared call sites.
- Confirmed the shared five country values have central clamp/recompute paths and that the decision layer removes its owned active missions, flags, targets, timed states, and emergency formations on origin end.
- Probability source inspection, with no invented world-state inputs:
  - Base decision AI: 10 candidates, 51 required scenario inputs, incomplete pool. [Artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a46390ead28e27f3e8c6438d98b7ad9ccb1649408af3da82e5a6615a716f5057/34dc661966c709df868d48c9676a7c753d7607d3f6e2dd0a765d48c92768e895/probability-inspect-c573b604d014.json)
  - Base mission AI: 54 candidates, 33 required scenario inputs, incomplete pool. [Artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10250a9845dc6db5958bcb7789e41cfc3701db97d087bbc43c754bfb04e626cb/ab194517c4b05944f713741e8247b48db3ba1e72cdf27d3e32a926fa3b7ae78f/probability-inspect-c573b604d014.json)
  - Rival decision AI: two candidates, six required scenario inputs, incomplete pool. [Artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2df4f248b46e07fda068c018362e7c48001f239aac851da18f372ae17aff7ca8/904a68b818779d3f31bc13da73db08087f3fb91d602c13d7e2c48c548fe86d5c/probability-inspect-02eae392529a.json)
  - Rival mission AI: seven candidates, ten required scenario inputs, incomplete pool. [Artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8854af85bd2e094d4bcd7aeaf36dd3ea2a3e81b2471b3d9464cdf5871000192/aaf072766eaec36d09960c7b8db1fb96125defada9094742dfd1628882a0acd5/probability-inspect-02eae392529a.json)
- Read-only GUI inspection of `independence_wave_status_window` completed for `event006_belgium_static`; its source graph includes unrelated mod-wide GUI diagnostics, so it is retained only as fidelity evidence and not used to declare a decision-system failure. The inspector reported 426 modelled, 54 approximated, one missing, four unsupported, and 12 unresolved elements, none isolated to this decision audit. [Artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/631cb0c4e153cf3e6f18eb60762cec4b4c4db6708372ab01189e95d0ce79fc41/ac5679f747cca488ce3b3e3d30d0bd24192736aa8fdde78889264c8c65709959/gui-inspect.9bcf44d028051884.json)

## Remaining uncertainty

- Exact comparative AI probabilities were not evaluated because the MCP discovery correctly requires a declared candidate pool and 6-51 scenario inputs. This is a validation limitation, not a source blocker; no synthetic world state was introduced.
- The GUI artifact cannot isolate its one missing and unresolved elements from the repository-wide diagnostic set. No GUI source is owned by this task, and no GUI rewrite was made.
- Live/in-game evidence was intentionally skipped under the user's acceptance decision.

## Handoff

The parent can treat the shared dynamic systems as closed under static evidence and can use the crosswalk above for package-level consumers.

No commit was created.
