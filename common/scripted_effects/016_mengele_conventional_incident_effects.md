# Event 016 private conventional incident helpers

## Scope and acceptance

The parent approved private counterparts of the five existing conventional Event 016 family incidents on 2026-09-08.
The accepted identities, penalty constants, and response profiles are reused exactly, with private country-local flags and payment receipts.
One incident and one recovery can be active in each family, and independent families may coexist.
A later actual stage output can cause another incident after settlement.
There is no lifetime one-shot cap.
The parent owns all causal stage receipts, native risky-option receipts, rolls, callbacks, and final integration.
No real-world biomedical procedure is represented by this package.

## Family map and tuning

| Family token | Incident | Recovery | Profile | PP | Support equipment | Fuel | CIC | Days | Penalties |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `electronics` | Guidance Phantom | Purge the Guidance Network | technical | 35 | 300 | 500 | 2 | 60 | Air mission efficiency -10%, static AA hit chance -20% |
| `materials` | Catalytic Spill | Isolate the Catalytic Chain | industrial | 50 | 600 | 1500 | 3 | 90 | Factory output -10%, production efficiency growth -10% |
| `rocketry` | Test Stand Explosion | Secure the Propulsion Works | industrial | 50 | 600 | 1500 | 3 | 90 | Air mission efficiency -10%, fuel gain -10% |
| `high_energy` | Reactor Containment Crisis | Stabilize the Reactor Envelope | exotic | 75 | 1000 | 2500 | 4 | 150 | Stability -10%, special project speed -20% |
| `biomedical` | Clinical Contamination | Seal the Clinical Chain | biological | 60 | 800 | 750 | 3 | 120 | Weekly manpower -500, army organization -5% |

All costs and durations read `brilliant_scientist_project_board.response_<profile>_<resource>` in `common/script_constants/016_brilliant_scientist_project_constants.txt`.
Penalty keys exactly match the existing public-family entries in `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`.
There are no new global tuning categories.
The four file constants `@MENGELE_INCIDENT_<PROFILE>_CIC` mirror the shared 2/3/4/3 reservation values because the existing native decision modifier precedent uses literal file constants.
The regression checks that these mirrors remain equal.
No trucks, manpower payment, Exposure, public Capacity, or other cost is added.

## Public helper map

All APIs execute in country scope.
Replace `<family>` only with the five fixed family tokens above.

| Helper | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_record_<family>_incident` | Caller-authenticated actual output, existing temporary `mengele_event016_requested_stage` | Sets temporary `mengele_event016_conventional_incident_recorded` to 0 or 1, adds the private modifier, sets active/history flags, increments permanent incident count once | Deterministic dispatcher, parent weighted outcome or native risky option |
| `brilliant_scientist_mengele_record_requested_conventional_incident` | Existing `mengele_event016_project_family` and `mengele_event016_requested_stage`, both read-only | Routes exactly Electronics through Biomedical to the fixed record helpers, invalid family/stage fails closed | Parent calls after its roll and successful causal output |
| `brilliant_scientist_mengele_dispatch_conventional_incident` | Caller-authenticated settled output, read-only private family/stage selectors | Validates the exact family and its independent active/recovery state, loads intrinsic pressure, then rolls incident versus explicit no-op; result is `mengele_event016_conventional_incident_recorded` | Successful paid stage settlement; Materials and Biomedical native risky options |
| `brilliant_scientist_mengele_clear_<family>_incident` | None | Clears only active incident flag and modifier, preserves receipts and permanent history | Settlement and cleanup internals |
| `brilliant_scientist_mengele_begin_<family>_incident_recovery` | Native decision admission already succeeded, active incident, valid provider, no receipt, inclusive direct-cost affordability | Snapshots three direct costs, debits exactly once, creates active receipt | Matching native recovery decision only, never a general payment/start API |
| `brilliant_scientist_mengele_cancel_<family>_incident_recovery` | Exact active three-value receipt required for refund | Snapshots then clears receipt authority/values before refund, always clears malformed recovery remnants without refund, clears transient incident on invalid owner | Matching decision cancellation, invalid expiry, cleanup |
| `brilliant_scientist_mengele_finish_<family>_incident_recovery` | Exact receipt, active incident, valid provider | Clears receipt before success, removes penalty, records recovery flag/count once, invalid expiry routes to cancellation, outputs temporary `mengele_event016_conventional_recovery_finished` as 0/1 | Matching decision remove callback, which shows success only for result 1 |
| `brilliant_scientist_mengele_cleanup_<family>_incident` | None | Refunds complete receipt once, removes the native decision, clears transient state | Parent provider cleanup |
| `brilliant_scientist_mengele_cleanup_conventional_incidents` | None | Calls the five fixed cleanup helpers without changing parent selectors | Parent common provider cleanup |

Every record helper checks `brilliant_scientist_mengele_project_stage_provider_is_valid` through the package predicate and the four-stage predicate from the unchanged Computation core.
The package never writes either parent selector.
Fixed-family recovery callbacks do not depend on a mutable selector, so concurrent actions cannot cross-settle.
Missing variables have the engine's zero default for initial history increments.
No helper grants or removes technologies, stage outputs, projects, provider registration, or neutral knowledge.

### Example parent recording call

```txt
# Existing caller has already authenticated and settled a real output.
# The parent owns the approved chance roll. Inside its successful incident branch:
brilliant_scientist_mengele_record_requested_conventional_incident = yes
```

The dispatcher records deterministically and must never be called unconditionally as a substitute for the pending roll.
Calling a fixed record helper after an earlier incident has been recovered will create another incident.
It is the parent's actual-stage/native-option causal receipt that prevents replay, not a second lifetime guard in this package.

## Transactions and cleanup

Transient state per family consists of `mengele_event016_<family>_incident_active`, `mengele_event016_<family>_incident_recovery_active`, and `mengele_event016_<family>_incident_recovery_cost_{political_power,support_equipment,fuel}`.
Permanent history consists of `mengele_event016_<family>_incident_history`, `mengele_event016_<family>_incident_history_count`, `mengele_event016_<family>_recovery_history`, and `mengele_event016_<family>_recovery_history_count`.
Receipts are exact cost snapshots and remain independent if tuning changes during recovery.
All three values and the active flag are required for a valid refund/settlement receipt.
No missing component is inferred.
A malformed partial receipt is not a normal reachable state and is not refunded.
Normal cancellation, normal expiry, and parent cleanup all clear malformed recovery remnants rather than manufacturing payment.
An unresolved incident and its penalty remain active under a valid provider, allowing another paid recovery attempt without falsely recording success.
Started text is emitted only after the begin callback creates an exact receipt.
Cancellation text promises a refund only for a complete recorded payment.

The native decision owns the fourth cost through `civilian_factory_use`, owns its timer, and releases the reservation on completion/cancellation.
Cleanup explicitly calls `remove_decision` after refunding, which the vanilla documentation says does not execute `remove_effect`.
No second factory refund effect or refund variable exists.
The parent approved an order-independent native-only begin boundary on 2026-09-08.
The available/custom-cost gate checks all four costs, and the admitted begin callback rechecks requirements plus only the three direct payments through shared profile predicates.
It does not recheck free CIC after the engine may have reserved those factories.
Exact-CIC source transactions pass under modeled callback-before-reservation and reservation-before-callback orderings.
The installed engine's actual reservation ordering, resource caps, and native release behavior are not proved by the source interpreter.
A normal cancel helper invocation outside its native callback does not itself release a still-active decision, so external program cleanup must call the cleanup wrapper instead.
No event targets are necessary or created.

## Decisions, cost text, and assets

All five decisions use `mengele_clone_army_category`, with IDs `mengele_event016_<family>_incident_recovery`.
Visibility requires the family's incident, and availability shares the inclusive four-resource predicate with the custom-cost trigger.
The requirements tooltip does not expose raw nested provider predicates.
The four cost profiles each have four scripted-localisation selectors, so only unaffordable amounts and their texticons turn red.
All formatting characters live in English localisation.
No new category, GUI, event, evolution, country, achievement, or super-event is introduced.
The maximum local addition is five recovery actions, one per active family.
Parent review must account for the existing category's other stage actions when applying the full six-action presentation budget.

Each family reuses its existing Prototype sprite from `interface/016_brilliant_scientist_project_icons.gfx`, under `gfx/interface/decisions/016_brilliant_scientist/projects/`.
The suffixes are `electronics_guidance_prototype`, `advanced_materials_prototype`, `rocketry_propulsion_prototype`, `high_energy_physics_prototype`, and `biomedical_acceleration_prototype`.
The decision and dynamic modifier use `GFX_decision_brilliant_scientist_project_<suffix>`.
The regression resolves every sprite, reads each referenced DDS, and checks its DDS signature.
It does not claim visual pixel approval.

## Migration and parent integration

No existing Computation, bridge, or stage source was changed.
Shared equipment/fuel debits reuse `remove_support_equipment_from_stockpile` and `remove_fuel_from_stockpile` from `chaosx_dynamic_effects.txt`.
Common cost-profile predicates centralize four-resource affordability across families without hiding family-specific state.
Family-specific lifecycle code is deliberately explicit for receipt auditability.
There is no generic macro/template engine in the runtime.

Parent follow-up remains accepted and queued:
1. Resolve the comparison-tool gap: both absent-to-added comparisons were attempted but returned `PROBABILITY_SURFACE_EMPTY` because the frozen before sources contain no weighted blocks.
2. Validate the attached intrinsic four-stage pressure roll at 5/10/18.75/24 against the frozen baseline and declared scenarios.
3. Validate paid settlement and native risky-option dispatch together with duplicate callbacks and late adoption.
4. Parent integration calls `brilliant_scientist_mengele_cleanup_conventional_incidents` from `common/scripted_effects/016_mengele_project_stage_effects.txt` inside provider receipt cleanup, with final callback validation remaining parent-owned.
5. Preserve the current score-only evidence for the five recovery rows: `ai_urgent` resolves to 25 under explicit candidate overrides, not verified live eligibility or click probability.
6. Reconcile the canonical event docs, spec acceptance records, and workbook through the parent-owned final integration.

## Validation and limitations

Run `node .tools/audit_mengele_conventional_incident_contract.mjs`.
The interpreter executes the actual source AST for all five family transactions and shared stockpile debit helpers, failing on unsupported commands.
The current 363 scenarios include 165 transaction scenarios covering exact four-resource equality, each resource one below, duplicate incident/begin/cancel/finish calls, repeat incidents after recovery, original-cost refunds after tuning changes, invalid owner at cleanup and expiry, all five simultaneous recoveries, valid/invalid dispatcher selectors, all four profile colour selectors at equality and each separate resource shortage, and exact-CIC admission under both native reservation orderings for all six families including the parent's updated Computation source.
They additionally cover each missing receipt component at normal expiry in all six families and each direct-resource race after admission in both reservation orderings for the five conventional families, with no debit or started message when receipt creation fails.
Another 194 scenarios force the two dispatch branches across all five families and four stages, check exact pressure/complement values, reject invalid selectors/providers and matching-family active state, preserve other-family independence, and verify selector/history isolation.
Four scenarios execute the Materials and Biomedical native private hooks under both forced outcomes, including Prototype pressure and selector cleanup.
Forced outcomes are not probability evidence; this incident harness structurally checks paid receipt ordering and native reward once-only selection.
The separate `.tools/audit_mengele_project_adapter_contract.mjs` adds 630 executed paid-finish checks to its 3,968 existing assertions, for 4,598 total.
Those checks execute the actual five-array receipt match, clearing, refund, and recovery-completion code across five families and three paid stages, then retry the stage callback after recovery or provider restoration.
Family output and weighted dispatch are explicit counters, paid starting receipts are fixtures, and provider validity is supplied; these boundaries do not constitute engine or probability evidence.
The duplicate callback neither awards another output, dispatches again, refunds again, nor alters another family's receipt.
Checks also verify each private penalty matches its public source keys/constants, each native CIC mirror matches its cost profile, and existing sprite/DDS references resolve.
Provider validity is explicitly stubbed and native reservation/timer order is a declared model.
This is source/API regression evidence, never engine or live-game validation.

The required MCP focused event trace and state render returned partial analysis with zero indexed helpers.
Workspace helper projections and lifecycle passes were deferred, so the artifacts do not validate these helpers.
The exact artifact references and comparison outcome are recorded in the dated handoff.
Weighted incident dispatch and recovery AI are attached and MCP-evaluated.
The complete incident-versus-no-op pool returns conditional incident chances of 5%, 10%, 18.75%, and 24% for the four declared pressure inputs.
Both matching absent-to-added comparison calls returned `PROBABILITY_SURFACE_EMPTY`; there is no accepted numeric before/after delta or substitute current-versus-current comparison.
Six structural assertions require the exact shared urgent AI base with no additional modifiers in the five conventional decisions and Computation.
No probability acceptance is claimed from those source assertions, and full weighted closure remains unproven because the comparison boundary is unavailable.
No unapproved design simplification was made.
The package remains incomplete for end-to-end acceptance until its dispatch integration review and required comparisons are finished.

## Causal dispatch integration

Paid stage settlement consumes the exact active receipt before applying output and dispatches only when `mengele_event016_project_output_applied` is one.
The dispatcher rejects every family except the five listed here, so the shared paid-stage call does not add incidents to Computation or custom-unit families.
It executes before completed-native adoption, which preserves the paid stage selector and cannot replay a native Prototype roll.
Reconciliation and native adoption do not call this helper.
Materials and Biomedical native risky options use the same dispatcher at Prototype pressure under their existing `fire_only_once` reward boundary; their cautious options remain unchanged.
The strict private-provider branch never enters the public Kruger incident helper, and the current-Kruger-host branch retains that helper.
The pressure calculator reused from Computation writes only temporary scratch values and reads shared stage-capacity and accident-factor constants; it does not read or alter Computation receipts/history or Kruger Exposure.

## Future work

Keep recovery tied to the distinct existing incident rather than adding additional cost axes or duplicate action variants.
Any broader pressure redesign, new incident family, new visual surface, or public/private state merger requires separate accepted design.
