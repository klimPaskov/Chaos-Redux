# IW-047 Mari El decision and mission handoff

Date: 2026-08-14

Owner: `/root/iw045_decisions`

## Superseded source-status note (2026-08-14)

This decisions handoff predates the landed MEL package effects, focus hooks, AI source, and localisation. Statements below that describe those surfaces as absent or undefined are historical at handoff time. The package remains package-local and central attestation, normal/scenario preflight, and deterministic Join remain fail-closed.

## Scope and changed files

This handoff covers only the IW-047/MEL decision category and its package-local mission/project surface.

- `common/decisions/categories/006_independence_wave_mari_categories.txt`
- `common/decisions/006_independence_wave_mari_decisions.txt`

Central attestation, Join, package dispatch, focus files, localisation, assets, and other country packages were not edited.

## Canonical identifiers

The category is `independence_wave_mari_forest_compact_category`.

The founding mission is `independence_wave_mel_hold_forest_congress`.

The ten serialized projects are `independence_wave_mel_secure_forest_depots`, `independence_wave_mel_integrate_woodland_guards`, `independence_wave_mel_register_mari_communities`, `independence_wave_mel_settle_former_host_ledgers`, `independence_wave_mel_ratify_constitutional_autonomy`, `independence_wave_mel_adopt_forest_land_compact`, `independence_wave_mel_convene_woodland_councils`, `independence_wave_mel_establish_forest_emergency_command`, `independence_wave_mel_codify_durable_sovereignty`, and `independence_wave_mel_open_volga_finnic_corridor`.

The package gate is `is_independence_wave_mari_package` with the accepted alias `is_independence_wave_mel_package`.

The setup flag is `independence_wave_iw_047_setup_complete`, the anchor is state 833, and the crisis flags are `independence_wave_mel_compact_crisis_resolved` and `independence_wave_mel_compact_crisis_failed`.

## Lifecycle and race safety

The category is visible only for the exact MEL package and setup flag, so it does not widen central admission.

The founding mission has a package-specific 420-day timeout, is not player-available, and activates only with the exact package, setup, current force-package generation, and neither crisis terminal flag.

The mission cancels on package loss, force-package generation rollover, anchor or capital control loss, or the stable-ledger plus route-government plus anchor-control success condition.

Mission timeout and non-success cancellation set the failed crisis flag and call the package failure helper; the success cancellation sets the resolved crisis flag without applying failure.

Every project requires `is_independence_wave_mel_project_ready`, which includes the exact package, setup, current force-package generation, and failed-crisis exclusion.

Every project also requires the capital to remain controlled and the package active-project trigger to be false, preventing concurrent project completion or free reward loops.

Every project cancel trigger independently checks package loss, generation rollover, failed crisis, and capital loss, then calls the idempotent package failure helper while the package still exists.

## Costs and requirements

Administration-light projects use `can_pay_independence_wave_mel_administration_light_cost` and `independence_wave_decision_pay_administration_light`.

Administration-standard projects use `can_pay_independence_wave_mel_administration_standard_cost` and `independence_wave_decision_pay_administration_standard`.

Diplomatic projects use the shared `can_pay_independence_wave_diplomatic_standard_cost` and `independence_wave_decision_pay_diplomatic_standard` convoy-or-train commitment.

Woodland guard integration uses the shared security-standard manpower, army-experience, infantry-equipment, and support-equipment cost.

Forest emergency command uses the shared security-major material commitment.

Durable sovereignty uses the MEL strategic gate plus the shared strategic stability, war-support, command-power, and convoy-or-train commitment.

All player-facing cost rows use the existing generic Event 006 cost localisation keys rather than package-specific magic numbers.

## Host and route behavior

Former-host settlement is visible after the package is ready when a living former host exists or when secured forest depots expose the local fallback ledger path.

The live-host path requires the former host to be at peace with MEL; a war transition cancels the project and the fallback path is idempotent through the package focus helper.

Constitutional autonomy, forest-land compact, woodland councils, and forest emergency command are mutually serialized by the route-government gate and each requires its matching route trigger.

Durable sovereignty requires stable ledgers, completed founding settlement, resolved crisis, an installed route government, and current state control.

The Volga-Finnic corridor requires stable ledgers, completed founding settlement, resolved crisis, network membership, league-route availability, current state control, and the diplomatic standard cost.

## AI and probability evidence

Decision AI bases are shared Event 006 high, standard, and urgent constants, with wartime doubling on woodland guards and forest emergency command and a host-threat modifier on settlement.

The mandatory `mission_ai_will_do` probability inspection returned `PROBABILITY_SOURCE_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2389ed24d881a0540a93a30d2e0e0dc75c0ab15b8fe09e7bf8ee6b92beb0af1/f1841d6f174d27a5cd10632940a63139dce8e0e7caf375bb5aff7167ac986ac71a/probability-inspect-fe28dbeb18d6.json` (source hash `fe28dbeb18d645410397c80926c8d4d620d3072d856ba0b6749bf03b1c9b7fe5`, 11 candidates, zero available candidates, incomplete pool).

The `decision_ai_will_do` request was correctly redirected by the MCP to the mission adapter because the source contains no decision adapter candidates; its discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f00866e88b0f0bad15931a0bc19be89c13108dc05ee893f1c2f21acf37976b2/76243d27f330ac65dfea5a8b99236ef610f591835c75bb5aff7167ac986ac71a/probability-inspect-fe28dbeb18d6.json`.

No quantitative AI ranking or balance claim is made because the adapter reported no available scenario surface; the current MEL strategy source exists, but `ai_strategy_factor` reports `no_weighted_surfaces` and the named evaluation reports `PROBABILITY_SURFACE_EMPTY`.

## Historical localisation and integration blockers at handoff time

Historical at handoff time: the generic cost keys were present, but MEL names, descriptions, effect tooltips, and failure text were not yet present in the localisation tree. The MEL localisation tranche has since landed; remaining localisation risk is limited to final player-facing review.

Historical at handoff time: no MEL package effect file was present in `common/scripted_effects/`, so the decision source intentionally referenced the documented expected helper IDs `independence_wave_mel_begin_project`, `independence_wave_mel_apply_project_failure`, `independence_wave_mel_focus_secure_forest_depots`, `independence_wave_mel_focus_integrate_woodland_guards`, `independence_wave_mel_focus_register_mari_communities`, `independence_wave_mel_focus_settle_former_host_ledgers`, `independence_wave_mel_focus_open_ural_network_corridor`, `independence_wave_install_mel_constitutional_government`, `independence_wave_install_mel_forest_land_government`, `independence_wave_install_mel_woodland_council_government`, `independence_wave_install_mel_forest_emergency_government`, `independence_wave_mel_apply_administrative_progress`, `independence_wave_mel_apply_diplomatic_progress`, `independence_wave_mel_apply_security_progress`, and `independence_wave_mel_apply_major_settlement`.

Historical at handoff time: the core agent needed to define or alias those helpers. The package-local effects and focus-hook tranches now define them; this handoff still does not widen the decision surface with central admission or guessed central helpers.

## Validation

Brace counts are balanced for both touched script files (`2/2` for the category and `253/253` for decisions).

The ten project IDs match the ten `has_decision` entries in `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt`; the founding mission is intentionally not part of the active-project trigger.

Static scans found no stale IW-044, Tatarstan, river-compact, `<=`, or `>=` references in the MEL decision source.

No commit or staging was performed.

## Remaining work

Keep the package-local effects, focus hooks, and localisation aligned while resolving the 256-versus-833 map/FORM-12/13 contract, blocked flag and portrait gates, and incomplete probability evidence.

Parent review is required before claiming complete in-game integration because this handoff deliberately leaves central admission and unresolved package-local effect/localisation dependencies untouched.
