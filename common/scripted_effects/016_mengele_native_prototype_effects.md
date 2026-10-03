# Event016 exact native Prototype core

Disposition: helper definitions implemented under the parent's explicit new-file-only delegation of 2026-10-03.
External integration remains accepted and queued with the parent.
The accepted selection/provenance design is recorded in `docs/specs/016_brilliant_scientist_specs/specs/016_native_prototype_ownership_amendment_2026-10-03.md`.
Native start/cancel synchronization, selection persistence through native cancellation, and delayed-output isolation after same-project release/reselection remain unresolved.
This layer cannot satisfy or waive those stronger lifecycle requirements.

## Scope and exact source map

All effects and triggers execute in the owning country scope.
The temporary inputs are unscoped engine temporaries and must never be qualified with `ROOT.` or `PREV.`.
No event target or persistent numeric project pointer is needed for these three static identities.

| Source constant | Code | Exact native ID | Private family | Durable index | Fresh wrapper |
| --- | --- | --- | --- | --- | --- |
| `mengele_event016_native_prototype_source.cloning` | 1 | `sp_brilliant_scientist_cloning` | Cloning, ID 8 | 7 | `brilliant_scientist_mengele_native_output_cloning` |
| `mengele_event016_native_prototype_source.flying_bomb` | 2 | `sp_rockets_flying_bomb` | Rocketry, ID 4 | 3 | `brilliant_scientist_mengele_native_output_rocketry_flying_bomb` |
| `mengele_event016_native_prototype_source.jet_engine` | 3 | `sp_air_jet_engine` | Rocketry, ID 4 | 3 | `brilliant_scientist_mengele_native_output_rocketry_air_jet_engine` |

Every source-taking transaction rejects none, fractional codes, and unsupported codes before receipt initialization or index preparation.
It replaces inherited private family/stage/index selectors with its exact mapping before using the existing stage core.
Cloning selection and one Rocketry selection may coexist.
Either opposite Rocketry selection blocks fresh selection and settlement for the other alternative.

## Metadata and durable state

The new constants file contains only stable metadata codes.
It adds no gameplay tuning table, price, duration, threshold, or AI factor.
The existing `brilliant_scientist_event.project_family_count` supplies the fifteen-slot schema, and the existing family/stage constants retain their identities.

| Category | Values |
| --- | --- |
| `mengele_event016_native_prototype_source` | none 0, cloning 1, flying_bomb 2, jet_engine 3 |
| `mengele_event016_native_prototype_mode` | none 0, fresh_output 1, adopted_completed 2 |
| `mengele_event016_native_prototype_result` | none 0, selected 1, fresh_settled 2, adopted_settled 3, released 4, blocked 5 |

The country arrays `mengele_event016_native_prototype_source_entries` and `mengele_event016_native_prototype_mode_entries` use family ID minus one.
The initializer extends each array independently with its none code until it has at least fifteen slots.
It never truncates an oversized array, clears history, or repairs contradictory existing metadata by guessing.
Only indices 7 and 3 are written on a successful changed private Prototype output.
The other families' surviving values are preserved.
These arrays store the source and mode of the family's accepted Prototype receipt, while per-source observed flags preserve exact output observations independently.

For each suffix `cloning`, `flying_bomb`, and `jet_engine`, the country flags are:

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
| `brilliant_scientist_mengele_select_native_prototype` | Exact source, strict provider, Theory, incomplete private Prototype, empty matching paid receipt, no conflicting family selection, exact native availability or completed query. A matching held selection is allowed only when that exact native source is completed. | Returns selected and writes one selection flag for an incomplete native source, clearing its retired intent. A completed exact source, including a matching selected job, instead returns adopted_settled through the adoption core. No debit or timer. | Three instant exact-source choices in the existing Biological/Conventional Programs categories. |
| `brilliant_scientist_mengele_settle_fresh_native_prototype` | Exact source and matching synchronous temporary output witness, matching selection, strict provider, Theory, incomplete private Prototype, empty paid receipt. | Returns fresh_settled only after the existing output core changes the private Prototype, records exact source/fresh_output, and consumes only the matching selection. Otherwise blocked. A conflicting output retires that output source. | Internal call from the three literal native output wrappers only. |
| `brilliant_scientist_mengele_adopt_exact_completed_native_prototype` | Exact source, exact completed query, strict provider, Theory, incomplete private Prototype, empty paid receipt, no opposite Rocketry selection. | Returns adopted_settled after a changed private Prototype, records exact source/adopted_completed, and consumes a matching selection if held. Retired completed sources are permitted explicitly. No native output replay or observed flag fabrication. | Explicit completed-source choice and parent-owned historical reconciliation after its automatic-adoption gate passes. |
| `brilliant_scientist_mengele_release_native_prototype_selection` | Exact source, matching selection, empty matching family paid receipt, and that exact project not being researched. Provider validity and incomplete private Prototype are not required. | Returns released, clears only the matching selection, and retires that source. An active native query or funded family stage returns blocked, preserving selection and receipt. No native cancellation or refund. | Three parent-owned release controls. |
| `brilliant_scientist_mengele_cleanup_native_prototype_selections` | No selector required, original owning country. | Returns released if any selection was cleared, otherwise none. Clears all held selections and retires their exact ownership, even if native research is active. Preserves observed flags, paid receipts, durable history, and native research. | Existing provider-loss and terminal cleanup boundaries in the original country scope. |
| `brilliant_scientist_mengele_initialize_native_prototype_provenance` | No selector required. | Append-only independent array extension. Does not alter the dedicated result or clear selectors. | Called internally before accepted settlement and available to the parent for bounded schema initialization. |
| `brilliant_scientist_mengele_clear_native_prototype_selector` | No input. | Resets private source, witness, mode, family, stage, index, authorization, and the existing later-stage source selector through the existing cleanup helper. Preserves the dedicated result, durable arrays, and flags. | Transaction epilogues and parent cleanup after a read-only automatic-adoption probe that makes no effect call. |

The three public literal output wrappers set their literal source and witness, mark their exact observed flag, attempt fresh settlement, and clear selectors.
They return fresh_settled or blocked through the dedicated result.
Their intended call sites are each exact project's existing `project_output.country_effects` block, which the installed documentation defines as country scope with FROM as the project.
Calling a wrapper elsewhere violates its synchronous output contract.
The temporary witness prevents accidental reliance on an observed flag or inherited selector, and does not provide immutable engine callback-generation authentication.
Scripted `complete_special_project` can also reach this output boundary, so fresh_output is not independent proof of native payment.

## Read-only trigger map

Use the six literal UI wrappers directly with `= yes` without pre-setting any temporary selector.
They perform no temporary or persistent writes.
Use hidden internal conditions and parent-owned custom trigger tooltips/localisation when presenting their technical flags to players.

| Trigger | Literal behavior |
| --- | --- |
| `brilliant_scientist_mengele_can_select_native_cloning` | Strict private Cloning gates, either no own selection or exact custom completion, and either the exact custom completion or the existing `brilliant_scientist_can_research_mengele_cloning_prototype` availability gate. A selected completed custom job can enter adoption. The legacy `sp_mengele_cloning` completion/shared latch never substitutes. |
| `brilliant_scientist_mengele_can_select_native_flying_bomb` | Strict private Rocketry gates, no opposite Jet Engine selection, either no own selection or exact Flying Bomb completion, and either exact Flying Bomb completion or `has_tech = experimental_rockets`. |
| `brilliant_scientist_mengele_can_select_native_jet_engine` | Strict private Rocketry gates, no opposite Flying Bomb selection, either no own selection or exact Jet Engine completion, and either exact Jet Engine completion or the installed vanilla prerequisite branches. With By Blood Alone, engines_2 and an improved small/medium airframe are required. Otherwise fighter2 or tactical_bomber2 is required. |
| `brilliant_scientist_mengele_can_release_native_cloning` | Matching Cloning selection, existing Cloning decision receipt empty, and custom Cloning not being researched. No provider or incomplete private Prototype requirement. |
| `brilliant_scientist_mengele_can_release_native_flying_bomb` | Matching Flying Bomb selection, existing Rocketry decision receipt empty, and Flying Bomb not being researched. No provider or incomplete private Prototype requirement. |
| `brilliant_scientist_mengele_can_release_native_jet_engine` | Matching Jet Engine selection, existing Rocketry decision receipt empty, and Jet Engine not being researched. No provider or incomplete private Prototype requirement. |

The literal `brilliant_scientist_mengele_native_cloning_private_gate` and `_native_rocketry_private_gate` reuse the existing strict provider and exact Prototype predecessor conditions.
They delegate receipt checks to `brilliant_scientist_mengele_cloning_decision_receipt_is_empty` and `brilliant_scientist_mengele_rocketry_decision_receipt_is_empty`, which own literal family indexing and the no-initialization-marker alternative.
The same existing family predicates also gate release, so the effect atomically checks the UI's no-funded-stage condition without adding provider or private Prototype restrictions.
The effect core additionally initializes the existing receipt schema and rechecks the original selector-based predicates before settlement.
If those existing predicates or family IDs change, update the literal wrappers and rerun their parity scenarios together.

`brilliant_scientist_mengele_can_auto_adopt_exact_completed_native_prototype` is a read-only parent scanning guard that reads the exact temporary source but needs no temporary family/stage/index.
For Cloning it requires private eligibility, exact custom completion, and no retired Cloning ownership.
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
| `brilliant_scientist_mengele_native_prototype_source_is_supported` | Temporary source only. True for exactly the three supported enum values, false for none or malformed input. |
| `brilliant_scientist_mengele_native_cloning_private_gate` | Country lifecycle, exact Cloning Theory/Prototype flags, and literal family receipt slot. No temporary input. |
| `brilliant_scientist_mengele_native_rocketry_private_gate` | Country lifecycle, exact Rocketry Theory/Prototype flags, and literal family receipt slot. No temporary input. |
| `brilliant_scientist_mengele_native_jet_engine_technology_gate` | Country DLC and learned vanilla prerequisite technologies. No temporary input or learned-technology write. |
| `brilliant_scientist_mengele_native_prototype_can_be_selected` | Temporary exact source. Dispatches to its literal selection availability wrapper. None/unsupported fails. |
| `brilliant_scientist_mengele_native_prototype_exact_source_is_completed` | Temporary exact source. Queries only that literal native project. None/unsupported fails. |
| `brilliant_scientist_mengele_native_prototype_selection_conflicts` | Temporary exact source. True only for a Rocketry source with its opposite selection held. Cloning/none/unsupported has no opposite-source conflict, and callers independently validate supported source. |
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

## Usage and parent migration

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

1. Wire the three existing exact country-output blocks to their literal wrappers once, preserving all existing native rewards and existing CBRN/legacy output consumers once per output.
Do not wire the legacy Cloning project to the accepted custom wrapper.
2. Route only Cloning and Rocketry away from the existing aggregate/family-level fresh completion recorder, so that old completion ORs cannot bypass this core's exact selection ownership.
Retain all other family callbacks unchanged.
3. Add three instant selection choices and mutually exclusive release controls in the existing categories, using the literal availability triggers and caller-set literal source codes.
The parent owns visible-state gates, localisation, icons, effect tooltips, and AI weights.
4. Integrate bounded historical scanning after Theory using the auto-adoption guard and explicit acceptance for retired sources or both completed Rocketry alternatives.
Save and restore the enclosing Theory transaction's selectors, output status, availability result, and related context using the existing adoption isolation pattern.
The new core intentionally clears selectors, and its dedicated result does not replace the outer Theory result.
5. On successful Cloning private Prototype receipt, preserve native custom operational access through the parent-owned bridge.
The parent will preserve the operational grant's existing gates and replace only its Cloning exact-completed condition with an OR of exact completed and `brilliant_scientist_mengele_native_cloning_fresh_receipt_is_present`.
The parent hook will invoke its idempotent operational grant immediately after fresh_settled, before the original CBRN consumer, so the proven fresh receipt can provide access before the country completed bit is visible.
Adopted history continues to require the exact completed query at that bridge condition.
No bridge change or operational grant is implemented by these new files.
6. Add selection cleanup to the existing original-owner provider/terminal boundaries, and retain the unresolved native cancellation/reselection proof requirements.
7. Complete parent-owned source/MCP scenarios, decision/probability review, and CXT cases before any integrated feature completion claim.

No new icon or model is required by the core.
The exact existing native consumers use `GFX_sp_brilliant_scientist_cloning`, `GFX_sp_rockets_flying_bomb`, and `GFX_sp_air_jet_engine`.
Parent decision controls reuse the existing family Prototype icons without introducing an art package or changing any approved model.

## Validation and limits

The implementation handoff records local bounded reference spans/hashes, the source behavior matrix, and 568 source-contract cases executed against these files and the existing private stage core.
The additional boundary cases cover completed selected jobs re-entering selection for adoption, opposite Rocketry exclusion, release checks for every funded stage across provider/private Prototype states, and parity with the parent selection/release visible gates.
These include 256 fresh bridge proof combinations covering absent/short/aligned arrays, every supported source code, and fresh/adopted/unknown mode values.
The driver uses explicit provider/query inputs and stubs engine availability reconciliation and dynamic modifier behavior.
It does not execute HOI4, prove callback order, establish native payment, verify native cancellation, or prove delayed-generation isolation.
The HOI4 event/reference requests exposed in the session returned no result before the bounded orchestration was cancelled.
Parent-owned MCP/domain evidence remains blocked until an actual successful route result is reviewed.
No source scenario is engine acceptance evidence.

Future work is the accepted external wiring and engine proof above.
No substitute start/cancel callback, polling loop, native effect mirror, replacement timer, or silent fallback is proposed.
