# Event016 exact native Prototype core

Disposition: Cloning/Rocketry helper definitions and the bounded Electronics extension are implemented under the parent's explicit file-ownership delegations of 2026-10-03.
The Cloning/Rocketry integrated checkpoint is recorded in `docs/events/016_brilliant_scientist/systems/native_prototype_ownership.md`.
Electronics decision, presentation, localisation, CXT, native project output, and stage-dispatcher integration are present in the shared source and remain parent-owned for final review.
This document records source implementation, not accepted engine evidence.
The accepted selection/provenance design is recorded in `docs/specs/016_brilliant_scientist_specs/specs/016_native_prototype_ownership_amendment_2026-10-03.md`.
Native start/cancel synchronization, selection persistence through native cancellation, and delayed-output isolation after same-project release/reselection remain unresolved.
This layer cannot satisfy or waive those stronger lifecycle requirements.

## Scope and exact source map

All effects and triggers execute in the owning country scope.
The temporary inputs are unscoped engine temporaries and must never be qualified with `ROOT.` or `PREV.`.
No event target or persistent numeric project pointer is needed for these four static identities.

| Source constant | Code | Exact native ID | Private family | Durable index | Fresh wrapper |
| --- | --- | --- | --- | --- | --- |
| `mengele_event016_native_prototype_source.cloning` | 1 | `sp_brilliant_scientist_cloning` | Cloning, ID 8 | 7 | `brilliant_scientist_mengele_native_output_cloning` |
| `mengele_event016_native_prototype_source.flying_bomb` | 2 | `sp_rockets_flying_bomb` | Rocketry, ID 4 | 3 | `brilliant_scientist_mengele_native_output_rocketry_flying_bomb` |
| `mengele_event016_native_prototype_source.jet_engine` | 3 | `sp_air_jet_engine` | Rocketry, ID 4 | 3 | `brilliant_scientist_mengele_native_output_rocketry_air_jet_engine` |
| `mengele_event016_native_prototype_source.electronics_radar` | 4 | `sp_air_radar` | Electronics, ID 2 | 1 | `brilliant_scientist_mengele_native_output_electronics_radar` |

Every source-taking transaction rejects none, fractional codes, and unsupported codes before receipt initialization or index preparation.
It replaces inherited private family/stage/index selectors with its exact mapping before using the existing stage core.
Cloning, Electronics, and one Rocketry selection may coexist.
Either opposite Rocketry selection blocks fresh selection and settlement for the other alternative.

## Metadata and durable state

The new constants file contains only stable metadata codes.
It adds no gameplay tuning table, price, duration, threshold, or AI factor.
The existing `brilliant_scientist_event.project_family_count` supplies the fifteen-slot schema, and the existing family/stage constants retain their identities.

| Category | Values |
| --- | --- |
| `mengele_event016_native_prototype_source` | none 0, cloning 1, flying_bomb 2, jet_engine 3, electronics_radar 4 |
| `mengele_event016_native_prototype_mode` | none 0, fresh_output 1, adopted_completed 2 |
| `mengele_event016_native_prototype_result` | none 0, selected 1, fresh_settled 2, adopted_settled 3, released 4, blocked 5 |

The country arrays `mengele_event016_native_prototype_source_entries` and `mengele_event016_native_prototype_mode_entries` use family ID minus one.
The initializer extends each array independently with its none code until it has at least fifteen slots.
It never truncates an oversized array, clears history, or repairs contradictory existing metadata by guessing.
Only indices 7, 3, and 1 are written on a successful changed private Prototype output.
The other families' surviving values are preserved.
These arrays store the source and mode of the family's accepted Prototype receipt, while per-source observed flags preserve exact output observations independently.

For each suffix `cloning`, `flying_bomb`, `jet_engine`, and `electronics_radar`, the country flags are:

| Flag pattern | Meaning and lifetime |
| --- | --- |
| `mengele_event016_native_selected_<suffix>` | Exact provider authorization for future output. Selection sets it, matching successful settlement consumes it, and release/cleanup clears it. It proves no native start or payment. |
| `mengele_event016_native_observed_<suffix>` | That literal output wrapper executed. It is set even when the country lacks private eligibility and is preserved by release and cleanup. Adoption never fabricates it. |
| `mengele_event016_native_retired_<suffix>` | Ownership was released, cleaned up, or rejected because an opposite Rocketry source was selected at output. Automatic adoption rejects this disposition. Explicit fresh reselection clears the matching retired intent. Explicit completed adoption may accept it and preserves the historical retired flag. |

A blocked output with no matching selection still records observation.
A conflicting Rocketry output also retires that output's source, retaining the other alternative's pending selection.
Missing provider, Theory, or empty paid receipt does not consume a held selection.
Cancellation/resume semantics for that retained selection remain unresolved and must not be presented as fulfilled engine synchronization.

## Public effect map

In this table, `source` means the caller-set temporary `mengele_event016_native_prototype_source`.
The dedicated temporary `mengele_event016_native_prototype_result` is the only request-result contract.
It survives selector cleanup.
The default source is none and source-taking requests return blocked when the input is unsupported.

| Effect | Inputs and defaults | Outputs and side effects | Parent call site |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_select_native_prototype` | Exact source, strict provider, Theory, incomplete private Prototype, empty matching paid receipt, no conflicting family selection, exact native availability or completed query. A matching held selection is allowed only when that exact native source is completed. | Returns selected and writes one selection flag for an incomplete native source, clearing its retired intent. A completed exact source, including a matching selected job, instead returns adopted_settled through the adoption core. No debit or timer. | Four instant exact-source choices in the existing Biological/Conventional Programs categories. |
| `brilliant_scientist_mengele_settle_fresh_native_prototype` | Exact source and matching synchronous temporary output witness, matching selection, strict provider, Theory, incomplete private Prototype, empty paid receipt. | Returns fresh_settled only after the existing output core changes the private Prototype, records exact source/fresh_output, and consumes only the matching selection. Otherwise blocked. A conflicting output retires that output source. | Internal call from the four literal native output wrappers only. |
| `brilliant_scientist_mengele_adopt_exact_completed_native_prototype` | Exact source, exact completed query, strict provider, Theory, incomplete private Prototype, empty paid receipt, no opposite Rocketry selection. | Returns adopted_settled after a changed private Prototype, records exact source/adopted_completed, and consumes a matching selection if held. Retired completed sources are permitted explicitly. No native output replay or observed flag fabrication. | Explicit completed-source choice and parent-owned historical reconciliation after its automatic-adoption gate passes. |
| `brilliant_scientist_mengele_release_native_prototype_selection` | Exact source, matching selection, empty matching family paid receipt, and that exact project not being researched. Provider validity and incomplete private Prototype are not required. | Returns released, clears only the matching selection, and retires that source. An active native query or funded family stage returns blocked, preserving selection and receipt. No native cancellation or refund. | Four parent-owned release controls. |
| `brilliant_scientist_mengele_cleanup_native_prototype_selections` | No selector required, original owning country. | Returns released if any selection was cleared, otherwise none. Clears all held selections and retires their exact ownership, even if native research is active. Preserves observed flags, paid receipts, durable history, and native research. | Existing provider-loss and terminal cleanup boundaries in the original country scope. |
| `brilliant_scientist_mengele_initialize_native_prototype_provenance` | No selector required. | Append-only independent array extension. Does not alter the dedicated result or clear selectors. | Called internally before accepted settlement and available to the parent for bounded schema initialization. |
| `brilliant_scientist_mengele_clear_native_prototype_selector` | No input. | Resets private source, witness, mode, family, stage, index, authorization, and the existing later-stage source selector through the existing cleanup helper. Preserves the dedicated result, durable arrays, and flags. | Transaction epilogues and parent cleanup after a read-only automatic-adoption probe that makes no effect call. |

The four public literal output wrappers set their literal source and witness, mark their exact observed flag, attempt fresh settlement, and clear selectors.
They return fresh_settled or blocked through the dedicated result.
Their intended call sites are each exact project's existing `project_output.country_effects` block, which the installed documentation defines as country scope with FROM as the project.
Calling a wrapper elsewhere violates its synchronous output contract.
The temporary witness prevents accidental reliance on an observed flag or inherited selector, and does not provide immutable engine callback-generation authentication.
Scripted `complete_special_project` can also reach this output boundary, so fresh_output is not independent proof of native payment.

## Read-only trigger map

Use the eight literal UI wrappers directly with `= yes` without pre-setting any temporary selector.
They perform no temporary or persistent writes.
Use hidden internal conditions and parent-owned custom trigger tooltips/localisation when presenting their technical flags to players.

| Trigger | Literal behavior |
| --- | --- |
| `brilliant_scientist_mengele_can_select_native_cloning` | Strict private Cloning gates, either no own selection or exact custom completion, and either the exact custom completion or the existing `brilliant_scientist_can_research_mengele_cloning_prototype` availability gate. A selected completed custom job can enter adoption. The legacy `sp_mengele_cloning` completion/shared latch never substitutes. |
| `brilliant_scientist_mengele_can_select_native_flying_bomb` | Strict private Rocketry gates, no opposite Jet Engine selection, either no own selection or exact Flying Bomb completion, and either exact Flying Bomb completion or `has_tech = experimental_rockets`. |
| `brilliant_scientist_mengele_can_select_native_electronics_radar` | Strict private Electronics gates, either no own selection or exact radar completion, and either exact `sp_air_radar` completion or both `has_dlc = "Gotterdammerung"` and `has_tech = electronic_mechanical_engineering`. A held completed source can enter adoption. |
| `brilliant_scientist_mengele_can_select_native_jet_engine` | Strict private Rocketry gates, no opposite Flying Bomb selection, either no own selection or exact Jet Engine completion, and either exact Jet Engine completion or the installed vanilla prerequisite branches. With By Blood Alone, engines_2 and an improved small/medium airframe are required. Otherwise fighter2 or tactical_bomber2 is required. |
| `brilliant_scientist_mengele_can_release_native_cloning` | Matching Cloning selection, existing Cloning decision receipt empty, and custom Cloning not being researched. No provider or incomplete private Prototype requirement. |
| `brilliant_scientist_mengele_can_release_native_flying_bomb` | Matching Flying Bomb selection, existing Rocketry decision receipt empty, and Flying Bomb not being researched. No provider or incomplete private Prototype requirement. |
| `brilliant_scientist_mengele_can_release_native_electronics_radar` | Matching radar selection, existing Electronics decision receipt empty, and exact `sp_air_radar` not being researched. No provider or incomplete private Prototype requirement. |
| `brilliant_scientist_mengele_can_release_native_jet_engine` | Matching Jet Engine selection, existing Rocketry decision receipt empty, and Jet Engine not being researched. No provider or incomplete private Prototype requirement. |

The literal `brilliant_scientist_mengele_native_cloning_private_gate`, `_native_rocketry_private_gate`, and `_native_electronics_private_gate` reuse the existing strict provider and exact Prototype predecessor conditions.
They delegate receipt checks to `brilliant_scientist_mengele_cloning_decision_receipt_is_empty`, `brilliant_scientist_mengele_rocketry_decision_receipt_is_empty`, and `brilliant_scientist_mengele_electronics_decision_receipt_is_empty`, which own literal family indexing and the no-initialization-marker alternative.
The same existing family predicates also gate release, so the effect atomically checks the UI's no-funded-stage condition without adding provider or private Prototype restrictions.
The effect core additionally initializes the existing receipt schema and rechecks the original selector-based predicates before settlement.
If those existing predicates or family IDs change, update the literal wrappers and rerun their parity scenarios together.

`brilliant_scientist_mengele_can_auto_adopt_exact_completed_native_prototype` is a read-only parent scanning guard that reads the exact temporary source but needs no temporary family/stage/index.
For Cloning it requires private eligibility, exact custom completion, and no retired Cloning ownership.
For Electronics it requires private eligibility, exact radar completion, and no retired radar ownership.
For Rocketry it requires private eligibility, exactly one completed alternative, no opposite Rocketry selection, and neither Rocketry source retired.
A matching selection may be reconciled as adopted_completed from its exact completed query, and is never relabeled as fresh_output by scanning.
The parent automatic driver uses this guard only for unselected historical sources and sends selected sources through explicit exact adoption.
Rejecting either Rocketry retirement prevents an automatic scan from switching a released/rejected ownership to its alternative.
Both completed Rocketry alternatives always require explicit source acceptance, even if one has a retired disposition.
There is no automatic scanning effect or hook in these files.

Other generic trigger helpers dispatch exact source identity, completion, selection conflict/matching, release, and the fresh output witness.
`brilliant_scientist_mengele_native_prototype_private_gate` reads the prepared family/stage and delegates to the existing strict provider/predecessor/empty-receipt core.
These internal generic predicates do not replace the literal UI wrappers.

| Internal read-only trigger | Inputs and result |
| --- | --- |
| `brilliant_scientist_mengele_native_prototype_source_is_supported` | Temporary source only. True for exactly the four supported enum values, false for none or malformed input. |
| `brilliant_scientist_mengele_native_cloning_private_gate` | Country lifecycle, exact Cloning Theory/Prototype flags, and literal family receipt slot. No temporary input. |
| `brilliant_scientist_mengele_native_rocketry_private_gate` | Country lifecycle, exact Rocketry Theory/Prototype flags, and literal family receipt slot. No temporary input. |
| `brilliant_scientist_mengele_native_electronics_private_gate` | Country lifecycle, exact Electronics Theory/Prototype flags, and existing literal Electronics receipt predicate. No temporary input or writes. |
| `brilliant_scientist_mengele_native_jet_engine_technology_gate` | Country DLC and learned vanilla prerequisite technologies. No temporary input or learned-technology write. |
| `brilliant_scientist_mengele_native_prototype_can_be_selected` | Temporary exact source. Dispatches to its literal selection availability wrapper. None/unsupported fails. |
| `brilliant_scientist_mengele_native_prototype_exact_source_is_completed` | Temporary exact source. Queries only that literal native project. None/unsupported fails. |
| `brilliant_scientist_mengele_native_prototype_selection_conflicts` | Temporary exact source. True only for a Rocketry source with its opposite selection held. Cloning/Electronics/none/unsupported has no opposite-source conflict, and callers independently validate supported source. |
| `brilliant_scientist_mengele_native_prototype_selection_matches` | Temporary exact source. Requires its selection and absence of an opposite Rocketry selection. None/unsupported fails. |
| `brilliant_scientist_mengele_native_prototype_output_witness_matches` | Temporary exact source and output_source witness. Requires a supported source and equal witness. An observed flag alone does not supply it. |
| `brilliant_scientist_mengele_native_prototype_private_gate` | Supported source plus prepared private family/stage. Uses the original strict provider, predecessor, and empty receipt predicates. Intended for mapped effect transactions only. |
| `brilliant_scientist_mengele_native_prototype_can_be_released` | Temporary exact source. Dispatches to its literal selected/not-researched release wrapper. None/unsupported fails. |

`brilliant_scientist_mengele_native_cloning_fresh_receipt_is_present` is the read-only bridge proof requested by the parent.
Both provenance arrays must have at least eight entries, using the existing Cloning family ID as the size requirement, before slot 7 is read.
The literal 7 is the existing static enumeration mapping of Cloning family ID 8 minus one, consistent with the existing Cloning decision receipt predicate, rather than a gameplay tuning value.
No existing reusable zero-based Cloning index constant was found.
The local references document temporary-variable arithmetic in triggers, but temporary values are unscoped and introduce writes into this otherwise pure proof.
Keeping the literal schema mapping avoids that scratch-state side effect and avoids assuming unsupported constant-token substitution inside an array index.
The source must equal cloning and the mode must equal fresh_output.
Adopted history, absent/short arrays, another source, or a none/unknown mode never supplies this proof.
The trigger writes nothing and depends on no temporary selector or country completion bit.
The parent bridge retains its own strict provider, Theory, and private Prototype checks around this durable receipt proof.

## Internal effect contracts

The internal helpers execute only from their documented callers and leave selector cleanup to the public transaction.

| Helper | Inputs, outputs, and defaults | Side effects and callers |
| --- | --- | --- |
| `brilliant_scientist_mengele_prepare_native_prototype_request` | Exact source, defaults to none. Maps supported source to private family/Prototype/index. Unsupported input resets private mapping to none/zero without preparing an index. | Temporary mapping only, called by selection and both settlement cores. |
| `brilliant_scientist_mengele_consume_native_prototype_selection` | Exact source, unsupported input does nothing. | Clears only that source's static selection flag. Called by successful provenance recording and release. |
| `brilliant_scientist_mengele_retire_native_prototype_source` | Exact source, unsupported input does nothing. | Sets only that source's retired flag. Called by guarded release and conflicting fresh output. |
| `brilliant_scientist_mengele_record_native_prototype_provenance` | Supported prepared source/mode/index with initialized arrays, immediately after `mengele_event016_project_output_applied = 1`. No defaults. | Writes the two mapped durable values and consumes only matching selection. Called only by successful fresh/adopted settlement. Never call directly from UI or generic scanning. |

The existing stage initializer may append its own receipt schema and initialize its existing private Singularity component registry.
The existing Prototype output core writes private completion flags and its dynamic modifier, updates availability through its existing reconciliation helper, and clears output authorization.
Its availability reconciliation can query native completion after output application.
Those queries are not used to authorize fresh settlement or classify its source/mode.
This implementation adds no paid receipt clearing, debit, technology grant, public Kruger selector, Capacity, or project-history write.
The existing output core remains the owner of its existing availability side effects.

## Usage and integrated call sites

Selection effect for an incomplete or already-completed Flying Bomb source:

```txt
set_temp_variable = { mengele_event016_native_prototype_source = constant:mengele_event016_native_prototype_source.flying_bomb }
brilliant_scientist_mengele_select_native_prototype = yes
```

Read-only UI availability:

```txt
brilliant_scientist_mengele_can_select_native_flying_bomb = yes
```

Guarded parent historical adoption of a named source:

```txt
set_temp_variable = { mengele_event016_native_prototype_source = constant:mengele_event016_native_prototype_source.cloning }
if = {
	limit = { brilliant_scientist_mengele_can_auto_adopt_exact_completed_native_prototype = yes }
	brilliant_scientist_mengele_adopt_exact_completed_native_prototype = yes
}
brilliant_scientist_mengele_clear_native_prototype_selector = yes
```

1. The four exact country-output hooks are wired to their literal wrappers in the existing native projects.
The Cloning hook preserves its original CBRN/legacy consumer and immediate operational bridge, and the two Rocketry hooks preserve native payloads.
The radar hook in `common/special_projects/projects/radar_projects.txt` calls the exact wrapper before the existing radar-output marker and original radio_detection grant.
This preserves native technology/module/facility output ownership and lets fresh output precede the completed bit.
2. The parent stage dispatcher excludes Cloning, Rocketry, and Electronics from the generic fresh recorder, sync path, and reused-completion scan.
The Electronics Prototype output leaves its family/stage/index intact until this core writes provenance.
The literal Electronics wrapper owns fresh retry after durable settlement; neither generic settlement core retries radar.
3. `common/decisions/016_mengele_native_prototype_selection_decisions.txt` contains four instant choices and four release controls under the existing categories.
Electronics uses `mengele_event016_native_select_electronics_radar` and `mengele_event016_native_release_electronics_radar`, existing `GFX_decision_brilliant_scientist_project_electronics_guidance_prototype`, and parent-owned hidden presentation, custom requirements, localisation, and AI.
Fresh radar selection requires G?tterd?mmerung plus electronic_mechanical_engineering; exact completed adoption remains available without DLC or that technology, retaining the same private gate.
4. `brilliant_scientist_mengele_try_adopt_exact_native_prototype` in the parent selection-decision effects maps Electronics to exact source 4.
It accepts a matching held selection or the non-retired automatic-adoption gate, then retries radar only after adopted_settled.
The parent selection-feedback adapter also retries after an explicitly selected completed Electronics source has settled as adopted.
The enclosing after-Theory effect routes Electronics through this driver and restores its outer family/stage/index, output, authorization, availability, gap, and component context.
5. The Cloning bridge uses exact completion or `brilliant_scientist_mengele_native_cloning_fresh_receipt_is_present` inside its original private grant gates.
The project hook grants from proven fresh history before its original CBRN consumer; adopted bridge history still uses exact native completion.
This tranche changes no Cloning/Rocketry bridge or native payload.
6. Existing provider/terminal cleanup calls the shared native selection cleanup in the original owner scope.
Its Electronics extension retires only current held selection, preserving durable observation/provenance, paid receipt, and native research.
`common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt` adds player-triggered observation of radar's three flags and index 1 source/mode; it creates no selection, completion, grant, or timer.
7. Final decision/weighted-action evidence, broader fifteen-family coverage, native cancellation, and same-project generations remain parent-owned and unresolved.
The temporary-output caller-storage rule below remains required at every result-consuming boundary; an integrated call site alone does not prove conservative lifetime safety.

No new icon or model is required by the core.
The exact existing native consumers use `GFX_sp_brilliant_scientist_cloning`, `GFX_sp_rockets_flying_bomb`, `GFX_sp_air_jet_engine`, and radar's installed `GFX_sp_nuclear_radar`.
Parent decision controls reuse the existing family Prototype icons without introducing an art package or changing any approved model.


## Electronics output ordering and caller-owned storage

`brilliant_scientist_mengele_native_output_electronics_radar` takes no source input, assigns source code 4 and its matching synchronous witness, and always writes `mengele_event016_native_observed_electronics_radar`.
Observation includes missing provider/Theory, stale or absent selection, repeated output, and an active paid Electronics family receipt.
Fresh authorization uses matching selection and the provider/Theory/incomplete-Prototype/empty-receipt gate, without a country completed query.
Only a changed private Prototype records exact source/fresh_output at index 1 and consumes matching selection.

After that durable success, the literal wrapper calls `brilliant_scientist_mengele_settle_native_electronics_deployment_from_radar`.
The existing helper owns the separate radar-output-seen plus radio_detection pair, Deployment predecessor, empty paid receipt, later-stage provenance, and operational package.
It can clear private family/stage/index selectors and change general stage-output results.
The wrapper explicitly restores the dedicated result to fresh_settled after the retry, whether Deployment succeeds or remains blocked, and clears its selectors.
Neither generic settlement core invokes radar retry.
The integrated parent selection-feedback and after-Theory adoption drivers retry only after adopted_settled, once adopted provenance and matching consumption exist.

For every supported source, each generic selection, fresh-output, and explicit-adoption transaction initializes its own family/stage/index/project_output_applied/stage_package_applied storage before nested mapping/output calls.
Family and stage start at none; index and the two output slots start at zero.
These five slots belong to the consuming transaction frame and are internal outputs, not additional public caller inputs.
The repeated initializers deliberately remain in those three frames; moving their first creation into a shared helper would recreate the lifetime defect.
This related correctness fix preserves persistent receipts, flags, source/mode meaning, costs, and native authority while making Cloning/Rocketry work under conservative helper-return cleanup.
The literal wrapper initializes its own forwarded scratch before nested calls: native_prototype_result = none, project_family/requested_stage = none, project_index/project_output_applied/stage_package_applied = zero.
Its two literal source/witness assignments also provide storage for nested inputs.
An outer caller consuming the dedicated result must initialize `mengele_event016_native_prototype_result = constant:mengele_event016_native_prototype_result.none` before invoking this wrapper.
The public source-taking contract remains the exact source temporary, plus the synchronous witness for fresh settlement.
A public caller consuming the dedicated native result initializes native_prototype_result to result.none before the call; it does not supply the five internal mapping/output slots.
If a caller intentionally consumes another forwarded temporary after the API returns, it must independently own that storage, and enclosing Theory transactions still snapshot and restore their own context.
Cloning and Rocketry literal wrappers do not consume the nested dedicated result locally; they forward it into outer caller-owned storage.
The Electronics literal wrapper does consume it for retry and therefore initializes its own result slot.
The parent feedback selection/release adapters, after-Theory caller, provider-cleanup caller, and original Cloning country-output boundary initialize each consumed native result before their helper call.
Temporaries are unscoped; never qualify them with ROOT or PREV.
The wrapper clears inherited selector context; enclosing transactions snapshot and restore their own context.

Exact radar output call, in the existing project_output.country_effects COUNTRY boundary:

```txt
set_temp_variable = { mengele_event016_native_prototype_result = constant:mengele_event016_native_prototype_result.none }
brilliant_scientist_mengele_native_output_electronics_radar = yes
```

Selection or explicit completed adoption:

```txt
set_temp_variable = { mengele_event016_native_prototype_result = constant:mengele_event016_native_prototype_result.none }
set_temp_variable = { mengele_event016_native_prototype_source = constant:mengele_event016_native_prototype_source.electronics_radar }
brilliant_scientist_mengele_select_native_prototype = yes
```

The parent preserves original radar technology/module/facility outputs and uses the existing Electronics Prototype decision icon.
The core creates no paid receipt, resource debit, timer, native start/cancel action, technology, project, event target, artwork, entity, or animation.
Cleanup retires held radar selection and preserves observation, accepted history, paid receipt, and native research.
Native cancellation and same-project generation requirements remain unresolved.

## Validation and limits

The prior Cloning/Rocketry implementation handoff records local bounded reference spans/hashes, its source behavior matrix, and 568 source-contract cases executed at that checkpoint.
The additional boundary cases cover completed selected jobs re-entering selection for adoption, opposite Rocketry exclusion, release checks for every funded stage across provider/private Prototype states, and parity with the parent selection/release visible gates.
These include 256 fresh bridge proof combinations covering absent/short/aligned arrays, every supported source code, and fresh/adopted/unknown mode values.
The driver uses explicit provider/query inputs and stubs engine availability reconciliation and dynamic modifier behavior.
It does not execute HOI4, prove callback order, establish native payment, verify native cancellation, or prove delayed-generation isolation.
The HOI4 event/reference requests exposed in the session returned no result before the bounded orchestration was cancelled.
These earlier deadline results are route-specific evidence limits; they are not a claim of global service outage.
Later parent and localisation handoffs record successful narrow reference search/context/source lookup results separately.
No source scenario is engine acceptance evidence.

Future work is the remaining parent-owned integration and engine proof above.
No substitute start/cancel callback, polling loop, native effect mirror, replacement timer, or silent fallback is proposed.

The Electronics extension's handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_electronics_core_2026-10-03.md`.
The final driver passes 6,590 source-contract cases.
It records 869 Electronics source scenarios, 960 flat-model Cloning/Rocketry parity cases against immutable a23ea17, 660 conservative Electronics cases, 184 parent Electronics integration cases, 2,880 conservative Cloning/Rocketry cases, 240 parent feedback cases, 788 Cloning history/bridge cases, and nine old-core lifetime regressions.
The actual source driver and its source hashes are retained there.
Provider validity, native queries, engine availability reconciliation/dynamic modifier refresh, technology-package grants, and the full custom operational bridge payload remain declared model inputs or stubs.
The Cloning bridge eligibility gate is evaluated from actual source, including its durable fresh receipt proof before exact native completed-bit visibility.
All nine negative regression cases reproduce blocked selection/output/adoption on a23ea17 with conservative helper-return cleanup and pass on the corrected core.
Flat-model parity treats absent and explicitly initialized zero scratch slots as the same value while separately comparing every persistent receipt/flag, output modifier, dedicated result, and other temporary value.
MCP reference and event inspection deadlines, render/compare results, and schema errors are recorded in that handoff.
No source result proves native clock/payment, callback timing, cancellation, live technology consumption, or callback-generation isolation.

Parent final reference evidence is retained in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_electronics_reference_results_2026-10-03.json`.
The complete exact-completion section was read successfully through two bounded MCP deliveries at installed triggers_documentation.md:6243-6250 and 6251-6257, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
The complete offline Decision modding timer section was read successfully at 337-356, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
The parent radar source lookups at 75 and 12 lines and four-node root event lint timed out after 600 seconds; the parent two-node event retry remained pending at final worker handoff.
Those results do not establish engine callback or cancellation behavior.

## Reused-source provenance: High Energy and Biological Weapons

High Energy reuses `sp_nuclear_reactor`, and Biological Weapons reuses `anthrax_bomb`, `plague_bomb`, `tularemia_bomb`, `smallpox_bomb`, `weaponize_the_zombies`, and `black_plague_weaponization_program`.
Countries can complete these outside the provider, so neither family has selection controls; settlement records the exact source and mode in `mengele_event016_native_prototype_source_entries` and `mengele_event016_native_prototype_mode_entries` instead.

| Effect | Scope and inputs | Output | Callers |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_settle_reused_native_prototype` | COUNTRY; temporary family (High Energy or Biological Weapons), source code, and mode | `mengele_event016_native_prototype_result`: `fresh_settled`, `adopted_settled`, or `blocked` | The three helpers below |
| `brilliant_scientist_mengele_native_completion_sp_nuclear_reactor` | COUNTRY; none | Same result; marks the reactor observed | `sp_nuclear_reactor` project output in the Event 016 `nuclear_projects.txt` mirror |
| `brilliant_scientist_mengele_observe_reused_biological_sources` | COUNTRY; none | Same result when a new agent settles | `brilliant_scientist_mengele_reconcile_reused_native_project_prototypes` from `on_project_completion` |
| `brilliant_scientist_mengele_adopt_reused_native_prototype` | COUNTRY; temporary family | Same result | `brilliant_scientist_mengele_adopt_completed_native_after_theory` |

Settlement requires the strict provider, the completed private Theory, an empty paid receipt (an active paid Prototype timer is never replaced), and the mapped completed source; the shared output core applies the Prototype once.
A source that completes after the Theory settles as `fresh_output`.
A source completed before the Theory is adopted as `adopted_completed` when the Theory settles; Biological Weapons adopts the first completed agent in the fixed order anthrax, plague, tularemia, smallpox, weaponized zombies, black plague.
The CBRN agent projects carry no Event 016 output hook, so the completing agent is identified as the mapped source that is completed but not yet observed; every agent is observed once through `mengele_event016_reused_source_observed_*` flags.
Source codes 5 to 11 in `mengele_event016_native_prototype_source` name the reactor and the six agents.

Limit: an agent completed while the provider was invalid and observed later after the Theory is recorded as fresh output; it is still the exact agent that completed.
