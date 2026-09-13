# Africa Elephant Black Friday Adapter Handoff

Status: source-bounded and live-blocked after parent integration; this handoff does not claim universal cost coverage or approve enabling Event 26.

Scope audited: `africa_elephant_open_logistics_contract` and its `africa_elephant_logistics_mission` lifecycle in `common/decisions/012_africa_elephant_operations_decisions.txt`, `common/scripted_effects/012_africa_elephant_operation_effects.txt`, and `common/scripted_triggers/012_africa_elephant_operation_triggers.txt`.

## Parent integration supersession

The parent integrated the bounded five-component adapter after this audit. The former P0 findings below are retained as audit history and are resolved in the current source as follows.

- The shared trigger-readable cache now includes the fuel family in `common/scripted_effects/chaosx_universal_cost_effects.txt`, and `black_friday_quote_custom_cost` reads the fuel ratio in `common/scripted_triggers/026_black_friday_triggers.txt`.
- The active owner path quotes and preflights command power, elephant equipment, motorized equipment, train equipment, and fuel. Native components use the shared payment helper; `chaosx_elephant_equipment_1` uses an explicit owner debit and refund acknowledgement.
- `africa_elephant_open_logistics_contract` now exposes the shared dynamic five-component cost text in `localisation/english/012_africa_elephant_operations_l_english.yml`, with active, blocked, tooltip, and texticon forms.
- The source contract is recorded in the Event 26 registry as `BF-AFR-001` through `BF-AFR-005`, for five logical components. The owner keeps the original route, target, mission, timing, AI, and ordinary inactive behavior.

The integrated source has not received live HOI4 tooltip, payment, refund, save/reload, multiplayer, or calendar validation. Event 26 remains default-disabled. The remaining semantic risks are the atomicity of the temporary `africa_elephant_logistics_materials_already_paid` guard if an owner chain were interrupted between payment and mission start, and the inactive-path behavior if a sale expires between decision evaluation and confirmation; neither is claimed live-proven.

## Original audit findings (pre-integration record)

- P0 (resolved by parent): the pre-integration trigger/cache contract had no `fuel` family branch. The current source adds the fuel cache and trigger branch described above.
- P0 (resolved by parent): `chaosx_elephant_equipment_1` lacked a native payment branch. The current owner adapter performs the explicit debit, records the actual amount, and acknowledges an external refund before the shared refund state is marked.
- P0 (resolved by parent): the original fixed cost text had no quote-backed icon-first active/blocked/tooltip forms. The current owner localisation supplies the dynamic five-component text surface.
- P1 (resolved by parent): the five distinct spendable types are retained and shown as one shared custom-cost contract; no component was silently dropped.
- P2: The shared decision-category GUI evidence is incomplete. `hoi4.gui_inspect` and `hoi4.gui_render` returned an offline/approximated representation with `GUI_WINDOW_MISSING`, unresolved-reference diagnostics, truncated source/validation diagnostics, `GUI_STATE_COVERAGE_MISSING`, and one missing fidelity component. This is the shared `decision_category_window`, not a dedicated Event 26 scripted GUI, so no event UI worker handoff was appropriate.

## Existing decision and lifecycle

- `africa_elephant_open_logistics_contract` at `common/decisions/012_africa_elephant_operations_decisions.txt:51-90` preserves operation visibility, DLC/route gates, `state_target = any_controlled_state`, `FROM` formation and supply-node checks, the ordinary custom-cost trigger, the 12 command-power cost, and the existing AI modifiers.
- `africa_elephant_begin_logistics_contract` at `common/scripted_effects/012_africa_elephant_operation_effects.txt:110-148` saves `FROM` as the global `africa_elephant_logistics_state` target, seals the generation, completion day, four ordinary commitment variables, and 181-day timeout, then debits 30 elephant equipment, 8 motorized equipment, 1 train, and 300 fuel, sets the active flag, and activates the mission.
- `africa_elephant_clear_logistics_contract` at `common/scripted_effects/012_africa_elephant_operation_effects.txt:150-163` clears the active flag, all sealed commitment/timing variables, and the saved state target.
- `africa_elephant_logistics_mission` at `common/decisions/012_africa_elephant_operations_decisions.txt:125-160` belongs to the current host, requires the intact contract and completion day, cancels on host/contract loss, completes through `africa_elephant_complete_logistics_contract`, and fails through `africa_elephant_fail_logistics_contract` on cancellation or timeout.
- Completion at `common/scripted_effects/012_africa_elephant_operation_effects.txt:165-175` records the existing elephant-supply achievement, sets the completed flag, and clears the contract. Failure at `:184-218` records the existing formation-destroyed or supply-failed result and clears the contract. The current ordinary commitment intentionally has no refund path.

## Cognitive-load and mission quality

- The category exposes three primary decisions and can expose two missions, so it is below the six-action and three-active-mission limits and does not need another tab or category.
- The four material values have clear mechanical significance in source: they are sealed commitments checked by `africa_elephant_logistics_material_contract_is_intact` at `common/scripted_triggers/012_africa_elephant_operation_triggers.txt:302-314`, while the completion witness is the selected depot, formation, and 180-day window. The player-facing cost sentence does not explain the quote state during Black Friday, does not use icons, and is longer prose than the UI should carry.
- The mission owner is the current host country, its category is the Africa Elephant Operations category, and its region is the saved `FROM` state target. Its requirements are an intact formation/roster, controlled supply node, intact sealed material contract, and elapsed completion day; its normal duration is 180 days with a 181-day timeout. Success, failure, cancellation, and cleanup are all present in the ordinary path.
- Duplicate mission risk is controlled by the active flag, generation match, contract-intact trigger, and saved target cleanup. A future adapter must keep sealed ordinary commitments separate from quoted/paid receipt values so it does not weaken the existing mission integrity test.

## Cost, requirement, AI, and route notes

- The ordinary inclusive affordability trigger is `africa_elephant_logistics_start_cost_is_paid` at `common/scripted_triggers/012_africa_elephant_operation_triggers.txt:326-331`: 30 `chaosx_elephant_equipment_1`, 8 `motorized_equipment`, 1 `train_equipment`, and 300 fuel. The ordinary decision also consumes 12 command power through its native `cost` field.
- The shared effect helper `universal_cost_quote_integer` supports fuel and deterministic upward quantization through the registered quantum, and the current owner adapter uses the shared native payment/credit helpers for fuel, motorized equipment, and trains. The remaining custom-equipment and live-engine risks are described in the parent integration section.
- AI is unchanged: the decision uses base `0.15`, zeroes after the elephant-supply achievement, and doubles during war; the mission uses base `0.15` and zeroes when the contract is not intact. No invalid target, dead-country target, closed route, or impossible state target was introduced or found in this owner surface. Since no AI weight was patched, no before/after probability comparison is claimed.

## Required follow-up, if the shared contract is extended

- The parent resolved the shared trigger/cache, custom-equipment, and dynamic-localisation prerequisites in the integrated source files listed above.
- The owner path quotes all five components, preflights them before debit, records actual paid values, settles on successful start, and refunds each paid component through the shared/native plus owner-specific path where cancellation handling calls the adapter.
- Preserve the existing command-power cost, route/target scopes, commitment variables, timing, mission effects, action limits, and ordinary inactive behavior. Do not call the Fury-only bundle helper for the custom elephant component and do not add a daily scan.

## Evidence and validation

- The pre-integration read-only source review confirmed there were no Event 26 or universal-cost identifiers in the three owner files; that finding is retained as historical provenance. The current parent-integrated source path was then reviewed across the decision, trigger, effect, localisation, registry, and handoff files.
- Required offline Paradox wiki pages and the relevant vanilla documentation for decisions, triggers, effects, scopes, localisation, GUI, and script constants were consulted before source review.
- GUI artifacts: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e68aab119248a46d6f1c60c3aa627d04c08e8e36bcf06d9fbe415f71821a7258/5f0818c8160de8158a1c0bce5b11b6370c70efd47c474cee5a9a091c4752110f/gui-inspect.0a4c98dde13bb7136d5ce2e504b34cf7c0e7c609631110a3bc08d62468717bc1.json`; render full view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87bbe82d9d756820/298e1f05689c80940735592547d99a007839bcfa21bcdf407dc356ce6870ed05/decision_category_window-full.png`; state matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9ef3d9afa016a15b8d46873c89c9177bc62c177aa6bb2b49c4606656a823334/be09208bd4564246f13ecef87f3143c1b856d2fc6aa187f59f10e15a2d861e22/decision_category_window-state-matrix.png`; layout `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7a5e83f29cd700d684e6e94d8f0dbd195c4826f93c283160843f1a59504f1c0/d54badda8533e1ee5e2b4196155621be54d2de3410c1f811d7ce1a60af6c30f0/decision_category_window-layout.json`.
- No live HOI4 session, payment/refund scenario, save-load check, multiplayer check, live tooltip check, or post-integration probability comparison was run. HOI4 was not launched, and no live or universal-coverage claim is made.

Remaining gap: the Africa Elephant adapter is source-bounded but live-blocked, and the wider Event 26 registry still lacks universal owner coverage and complete engine-inaccessible/static dispositions.
