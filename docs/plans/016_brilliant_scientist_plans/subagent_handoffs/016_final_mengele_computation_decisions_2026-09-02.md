# Event 016 Mengele Computation decision handoff

Status: bounded decision slice implemented for parent review on 2026-09-02.

This handoff covers only the four provider decisions, their fixed-stage triggers, their localisation, and the required standard decision-view evidence.

No commit, configuration change, stage operation, game launch, log request, live QA claim, model work, or asset generation was performed.

## Changed files and entry points

| File | Change | Entry points |
| --- | --- | --- |
| `common/decisions/016_mengele_computation_stage_decisions.txt` | Added one existing-category block with exactly four timed provider decisions and file-scoped civilian-factory modifier constants. | `mengele_event016_computation_theory`, `mengele_event016_computation_prototype`, `mengele_event016_computation_deployment`, `mengele_event016_computation_weaponization` under `mengele_clone_army_category`. |
| `common/scripted_triggers/016_mengele_computation_decision_triggers.txt` | Added fixed-stage visibility, native-route, affordability, receipt-match, and cancellation triggers with no temporary-variable writes. | `brilliant_scientist_mengele_computation_*_decision_visible`, `*_decision_requirements`, `*_decision_can_pay`, `*_decision_receipt_matches`, and `*_decision_cancel_trigger`. |
| `localisation/english/016_mengele_computation_l_english.yml` | Added names, descriptions, icon-first cost rows, one shared affordability tooltip, requirement tooltips, start/cancel tooltips, and settlement effect text. | All decision and tooltip keys referenced by the new decision file. The file is UTF-8 with BOM. |

## Decision contract

| Decision | Visibility and predecessor | Duration | Civilian factories | Political power | Support equipment | Fuel |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `mengele_event016_computation_theory` | Valid provider, empty Computation receipt, no Theory completion. | 120 days | 1 | 45 | 80 | 0 |
| `mengele_event016_computation_prototype` | Valid provider, Theory completion, empty Computation receipt, no native Computation Prototype completion, and native presentation unavailable. | 180 days | 2 | 68 | 200 | 100 |
| `mengele_event016_computation_deployment` | Valid provider, provider Prototype completion, empty Computation receipt, and no Deployment completion. | 270 days | 3 | 90 | 600 | 500 |
| `mengele_event016_computation_weaponization` | Valid provider, provider Deployment completion, empty Computation receipt, and no Weaponization completion. | 360 days | 5 | 135 | 1200 | 1500 |

The three direct provider payment axes are debited and stored by `brilliant_scientist_mengele_begin_project_stage` and are never duplicated with a native `cost` field.

The civilian-factory quote is reserved by each decision's `modifier = { civilian_factory_use = ... }` and is released by native timed-decision cancellation or removal.

The shared Event 016 stage cost and duration constants remain authoritative for Theory, Deployment, and Weaponization.

The bounded Prototype quote comes from `constant:mengele_event016_project_stage` and is not duplicated in a new tuning file.

Each cost row contains no more than four distinct cost or reservation types and uses `£civ_factory`, `£pol_power`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon` where applicable.

Theory omits a zero-valued fuel icon from its visible cost row while its affordability trigger still represents the exact zero-fuel quote.

## Before and after behavior

Before this slice, the existing `mengele_clone_army_category` had no provider-owned Computation Theory, Prototype fallback, Deployment, or Weaponization rows.

After this slice, the category exposes only the current Computation stage and keeps later stages hidden until their exact provider predecessor flag exists.

Theory, Deployment, and Weaponization are provider decisions in both DLC states.

Prototype is provider-owned only when `brilliant_scientist_mengele_computation_native_prototype_presentation_available` is false.

The native presentation trigger requires `has_dlc = "Gotterdammerung"`, the existing `brilliant_scientist_can_research_mengele_computation_prototype` gate, and no completed native Computational Engine project.

This DLC condition is based on the vanilla special-project files and documentation, while the mod's Computational Engine definition itself has an empty `allowed` block.

If the parent confirms that the mod intentionally exposes this native object without Götterdämmerung, the Prototype native-route trigger needs a parent-approved adjustment before live acceptance.

## Lifecycle and callback safety

Every `complete_effect`, `cancel_effect`, and `remove_effect` sets `mengele_event016_project_family = computation` and an exact literal `mengele_event016_requested_stage` before calling the corresponding private helper.

The begin helper owns provider validation, predecessor validation, direct affordability, the private receipt initialization, one-time direct debit, and receipt storage.

The cancel helper owns exact receipt matching, snapshot-before-clear ordering, one-time political-power/support-equipment/fuel refund, and selector cleanup.

The finish helper owns exact receipt matching, snapshot-before-clear ordering, provider output dispatch, fallback refund when output cannot be applied, and selector cleanup.

`cancel_if_not_visible = no` is explicit on all four decisions, so hiding a row after its receipt is created cannot self-cancel its timer.

Each cancellation trigger requires either the strict provider lifecycle gate to remain valid or the exact family-stage receipt to remain present.

The active receipt is private Computation array index `^0`; no global concurrency flag, active-family field, or generated callback token is introduced.

The fixed-stage triggers do not set temporary selectors in trigger context, so a wrong-stage callback cannot borrow a dynamically populated selector.

Repeated starts, wrong-stage callbacks, invalid-provider settlement, and post-cancel callbacks fail closed at the helper receipt gate.

## Audit findings by severity

### High

1. Native Prototype presentation eligibility remains an integration assumption until the parent verifies the engine's Götterdämmerung route against the mod's custom special-project object.

2. Native Prototype completion cannot settle the provider receipt until the parent-owned native bridge calls `brilliant_scientist_mengele_record_native_project_prototype` from the exact Computational Engine `project_output` branch.

### Medium

3. The parent-owned native Computational Engine reward branch still has the previously identified incident or reward integration risk and was not edited in this bounded slice.

4. The standard `countrydecisionview` production evidence reports inherited layout defects, including clipping and non-positive sizes, and this slice does not own the shared GUI source.

5. New decision AI rows have no historical candidate baseline because the parent froze `absent HEAD5f31c83` after MCP `SOURCE_NOT_FOUND` for this new source.

### Low

6. The existing category contains other Mengele actions, but the four new rows are stage-gated and at most one of these Computation rows is visible at a time.

## Decision-category lifecycle notes

The new rows use the existing category and existing family-stage sprites, so no category or GUI registration is required.

The stage rows are visible without direct-resource gating so missing inputs remain visible in the cost row.

The active row becomes hidden after start because the receipt is no longer empty, but its timer remains active because `cancel_if_not_visible = no`.

Completion clears the active receipt before applying the stage output, and cancellation clears it before refunding direct costs.

Parent lifecycle hooks must continue to call the same cancel helper for program rejection, closure, expiry, defeat, victory, annexation, civil war, death, and terminal cleanup.

## Cognitive-load notes

The slice adds four primary actions to an existing category, but stage ordering limits the visible Computation choice to the current stage rather than a wall of parallel rows.

There are no missions or new public meters in this slice.

The visible values are the stage name, timer, civilian-factory reservation, political-power quote, support-equipment quote, and fuel quote.

Each visible value has a direct player response: satisfy the displayed inputs, commit the listed factories, wait for the timer, or cancel to recover the direct payment.

The descriptions explain the stage consequence without exposing receipt-array implementation details.

The generic category remains outside this write scope and should be checked by the parent if unrelated Mengele actions make the full category exceed the accepted density target.

## Mission quality notes

Not applicable because this slice adds timed decisions, not missions or active mission objectives.

## Cost and requirement clarity notes

Native CIC availability uses `NOT = { num_of_civilian_factories_available_for_projects < quote }`, so an exact factory balance passes.

Political power uses the inclusive `greater_than_or_equals` comparison.

Support equipment and fuel use the strict-less-than rejection form, so exact balances pass.

The `custom_cost_trigger` and `available` affordability tooltip use the same fixed-stage affordability trigger.

The shared affordability tooltip is positive and icon-first: `Available capacity and stores cover the displayed £civ_factory £pol_power £support_equipment_text_icon £GFX_fuel_texticon commitments.`

The decision file has no native `cost` field and no direct `add_political_power` payment, leaving all three direct debits to the begin helper.

All spendable cost strings are icon-first and contain no literal resource labels or padded prose.

## AI validity and route locks

Every row reuses `constant:brilliant_scientist_project_board.ai_high` with the existing `brilliant_scientist_project_ai.preferred_factor` wartime modifier.

The Directorate low-capacity cautious modifier is intentionally omitted because `brilliant_scientist_has_low_project_capacity` reads the uninitialized shared Directorate meter for these private Mengele rows.

The rows require the strict Mengele provider gate, which rejects missing, defeated, rejected, closed, expired, recently expired, incident, current-host, and terminal states through the worker-owned trigger.

Prototype additionally rejects the native route when the native presentation is available and rejects an already completed native project to prevent duplicate provider settlement.

The parent froze the absent baseline at `HEAD5f31c83` with MCP `SOURCE_NOT_FOUND` and fixture `E016_MENGELE_COMPUTATION_STAGE_INCIDENT_BASELINE_2026_09_02.scenarios.json` SHA `9a6548a0`.

No timing probability, click probability, or weighted balance claim is made for these brand-new rows.

The parent must route the mandatory `chaosx_ai_probability_auditor` post-wire comparison through `hoi4.probability_compare` using the same named scenarios before changing any of these reused AI weights.

## Localisation and tooltip gaps

All decision names and descriptions, four cost rows, one shared affordability tooltip, four requirement tooltips, start and cancel tooltips, and four settlement effect tooltips are present in `016_mengele_computation_l_english.yml`.

The localisation file was normalized to UTF-8 with BOM.

No raw dynamic value dump or literal resource-name cost string was added.

The existing category name and icon are reused and are not duplicated.

## Cleanup and exploit-risk notes

The private receipt is idempotent because begin requires an empty index-0 slot and cancel or finish requires the exact active stage.

Refunds snapshot and clear the receipt before returning direct resources, preventing repeated callback refunds.

Civilian factories are released by the decision lifecycle and never refunded through `add_factories`.

Provider invalidation cancels unresolved work through the exact callback selector and leaves durable learned outputs to the parent-owned cleanup contract.

No free-unit loop, equipment farming loop, war-goal spam, core spam, global active flag, or cooldown bypass is introduced.

## Validation and evidence

Static review found exactly four decision definitions under the existing category, balanced braces at depth zero in both new script files, and matching localisation for every referenced decision, cost, requirement, cancellation, and effect key.

The required read-only `hoi4.gui_inspect` pass used `windowName = countrydecisionview`, scenario `event016_directorate_compact_current`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The final post-localisation inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f51c3293c2e1b731b611fb28115203c63ea5c4bd157a90115101b21ac36d566/cf6ffd442f7104e969533c12139db7fb62f13e0d493df4310c5857a14651218f/gui-inspect.83b6c5241caca767.json`.

The inspect result was `GUI_INSPECTED` with source revision `83b6c5241caca7671296e53e1253d011c85b84e00cb01e3a264ae7b386daa27c`, complete graph coverage, and no blocking diagnostics.

The required read-only `hoi4.gui_render` pass covered normal, locked, warning, and long-text states at 1366x768 and 1920x1080.

The final production render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf551d536d5f323e23809df0f5530c6e66fe7983b7cd75e14d4bec5fd0e44e19/91eeb26ed849363bba962143d42d1ede5169805807dbd2e776ebcee97695a736/countrydecisionview-full.svg`, with PNG companion `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/c54fa26528ae90e1b4ce860829210ce828e7a22339406d900b50b2402bde23c5/countrydecisionview-full.png`.

The render result was `GUI_RENDERED` with no blocking diagnostics, source revision `83b6c5241caca7671296e53e1253d011c85b84e00cb01e3a264ae7b386daa27c`, and `changedPixels = 0`, `changedRatio = 0` across the two requested resolutions.

The production evidence reports `GUI_ACCIDENTAL_CLIPPING` for `countrydecisionview`, `GUI_INVALID_SIZE` for `production_header_bg`, `decisionview_title`, `close_button`, and `decision_grid_container`, and `GUI_SPRITE_RENDER_PARTIAL` for `buttonstate_nodowneffect`.

The render also reports missing shared state-matrix coverage for hover, selected, disabled, active, completed, list, minimum-value, maximum-value, and missing-localisation states.

Those are real shared standard-view findings in the production evidence, not renderer differences, but patching `interface/countrydecisionview.gui` is outside this decision-slice ownership and would require a parent or GUI-owner change.

The probability compare was not run by this subagent because the parent froze the new-source baseline as absent and no weighted patch was applied here.

Decision-specific MCP inspect or lint is not exposed by the installed HOI4 server, so source checks and the mandatory standard GUI evidence are the meaningful validation available in this scope.

## Parent wiring checklist

1. Keep the new decision and trigger files loaded without editing the worker-owned stage helpers or constants.

2. Add the exact native Computational Engine output bridge to `brilliant_scientist_mengele_record_native_project_prototype` and ensure native completion precedes provider Prototype visibility.

3. Reconcile the native presentation flag with the DLC decision confirmed by engine or parent integration evidence.

4. Route parent lifecycle cancellation through the exact literal Computation stage wrappers so index 0 is refunded once.

5. Run `chaosx_ai_probability_auditor` with the frozen absent baseline and the named incident fixture, then perform the mandatory post-wire probability comparison before any AI-weight change.

6. Review the inherited shared `countrydecisionview` production warnings with the owner responsible for the standard decision GUI.

## Remaining issues and simplifications

No mechanic simplification was made inside this bounded four-decision slice.

The cautious AI modifier is an intentional parent-approved omission because its shared Directorate capacity meter is uninitialized for these private rows; the approved base and wartime preference remain active.

Native Prototype DLC eligibility, native bridge integration, parent lifecycle wiring, shared GUI warnings, and post-wire probability comparison remain parent-owned acceptance items.
