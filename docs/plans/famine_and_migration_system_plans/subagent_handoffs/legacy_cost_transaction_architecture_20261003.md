# Legacy custom-cost transaction architecture, 2026-10-03

Disposition: proposed architecture for the parent-accepted bounded affordability repair, queued for parent review and the frozen probability baseline.
The acceptance basis is the parent's explicit assignment to repair advertised spent-resource equality, complete fee-bundle parity, stale payment rejection, and unpaid continuations for the 25 existing legacy actions.
The parent subsequently confirmed that worker support equipment remains the exact strict non-spend prerequisite and that duplicate airlift and relief-candidate checks of spent resources must become inclusive.
Implementation is not claimed.

Ownership in this pass is only this new handoff.
No gameplay, localisation, workbook, asset, index, or commit was changed.
Other agents' work was preserved.
This document does not authorize another mechanic, category, GUI, mapmode, discount registry, whole-world scan, blanket refund rule, generic replay registry, or AI retune.

## Recommended boundary

Keep the existing independent famine and migration owners.
Add a neutral, fixed legacy fee table and pure inclusive component/profile triggers.
Keep actual debits, owner setup, delayed work, and the five measured refunds in their current decision paths.
Add narrowly owned action/state/payer receipts only where a later `remove_effect` can continue work.
Use the existing selected state as the receipt container so two actions or two states cannot overwrite a country-global payment flag.
The resulting boundary is selection eligibility, complete fee preflight, debit once, record paid work, consume the matching delayed receipt, and execute the existing continuation.

The source census is 25 actions, 18 distinct spent tuples, and 15 resource/tier getters.
The existing shared selector file contains 15 `GetHumanitarianCost*Cost` getters, rather than 13.
Four migration actions perform gameplay entirely in `complete_effect`, so their entire bodies need the final guard but no new delayed paid receipt: `migration_open_departure_routes`, `migration_restrict_departure`, `migration_controlled_medical_reception`, and `migration_local_integration`.
Twenty other actions pay upfront and have delayed effects.
`migration_negotiate_corridor` is the remaining delayed action and keeps its payment after successful offer submission.

## Constants and fee profiles

Recommended new file: `common/script_constants/humanitarian_legacy_cost_constants.txt`.
Define `humanitarian_legacy_cost` with a first-entry fixed-point schema and the following positive/negative pairs in one table.
Use names such as `pp_light` and `pp_light_debit`, with debit equal to the negative of the positive amount.
The keys below are the complete table, not additional costs.

| Pair | Positive | Negative | Exact current reader/debit token |
|---|---:|---:|---|
| `pp_light` | 10 | -10 | `has_political_power` / `add_political_power` |
| `pp_standard` | 20 | -20 | same |
| `pp_heavy` | 35 | -35 | same |
| `train_light` | 5 | -5 | `train_equipment` |
| `train_heavy` | 10 | -10 | `train_equipment` |
| `convoy_light` | 5 | -5 | `convoy` |
| `convoy_heavy` | 10 | -10 | `convoy` |
| `support_light` | 50 | -50 | `support_equipment` |
| `support_heavy` | 100 | -100 | `support_equipment` |
| `infantry_light` | 100 | -100 | `infantry_equipment` |
| `infantry_heavy` | 250 | -250 | `infantry_equipment` |
| `fuel_light` | 500 | -500 | `has_fuel` / `add_fuel` |
| `fuel_heavy` | 1000 | -1000 | same |
| `transport_planes` | 5 | -5 | `transport_plane_equipment` |
| `air_xp` | 10 | -10 | `has_air_experience` / `air_experience` |

Recommended new trigger file: `common/scripted_triggers/humanitarian_legacy_cost_triggers.txt`, with matching Markdown API documentation.
Component identifiers are `humanitarian_cost_<pair>_is_affordable`, for the 15 pair names above.
Each has COUNTRY scope, no inputs beyond the current payer and fresh table, a Boolean result, no saved outputs, no defaults, and no side effects.
Each uses the existing Open Reception structure, for example `NOT = { has_political_power < constant:humanitarian_legacy_cost.pp_standard }` or `NOT = { has_equipment = { convoy < constant:humanitarian_legacy_cost.convoy_heavy } }`.
Do not combine several resource checks as siblings within a single `NOT`, because that changes Boolean semantics.

Define the following 18 profile predicates by AND-composing only their components.
The profile identifier pattern is `humanitarian_cost_<profile>_is_affordable`.
The short numeric labels below describe the frozen baseline tuple and are proposed identifiers, not dynamic parameter APIs.
They have the same pure COUNTRY-scope contract as the components.

| Profile | Tuple | Exact callers |
|---|---|---|
| `pp20_support50_fuel500` | PP20, support50, fuel500 | `famine_release_reserves` |
| `pp20_convoy10_fuel500` | PP20, convoy10, fuel500 | `famine_emergency_imports` |
| `pp10_train5_fuel1000` | PP10, train5, fuel1000 | `famine_repair_relief_route` |
| `pp20_convoy10_support50_fuel1000` | PP20, convoy10, support50, fuel1000 | `famine_escorted_relief_convoy` |
| `pp20_planes5_fuel1000_airxp10` | PP20, transport planes5, fuel1000, airXP10 | `famine_emergency_airlift` |
| `pp20_convoy5_fuel500` | PP20, convoy5, fuel500 | `famine_invite_relief` |
| `pp20_train10_fuel1000` | PP20, train10, fuel1000 | `famine_evacuation` |
| `pp20_train5_fuel500` | PP20, train5, fuel500 | `famine_requisition_safer_state`, `migration_evacuate_vulnerable`, `migration_voluntary_return` |
| `pp10_infantry100_fuel500` | PP10, infantry100, fuel500 | `famine_conceal_crisis`, `migration_restrict_departure` |
| `pp10_train5_fuel500` | PP10, train5, fuel500 | `famine_maintain_extraction`, `migration_prepare_evacuation`, `migration_open_departure_routes`, `migration_distribute_arrivals` |
| `pp20_infantry250_fuel1000` | PP20, infantry250, fuel1000 | `migration_close_border`, `migration_enforce_closure` |
| `pp20_train10_fuel500` | PP20, train10, fuel500 | `migration_evacuate_workers` |
| `pp35_infantry100_fuel500` | PP35, infantry100, fuel500 | `migration_negotiate_corridor` |
| `pp20_support100_infantry100` | PP20, support100, infantry100 | `migration_controlled_medical_reception` |
| `pp10_convoy5_fuel500` | PP10, convoy5, fuel500 | `migration_transit_only` |
| `pp20_support100_fuel500` | PP20, support100, fuel500 | `migration_local_integration` |
| `pp35_train5_convoy5_fuel500` | PP35, train5, convoy5, fuel500 | `migration_third_country_resettlement` |
| `pp35_train10_fuel1000` | PP35, train10, fuel1000 | `migration_forced_repatriation` |

Call the exact profile in both `available` and `custom_cost_trigger` in acting-country scope.
Use the same profile immediately before the actual debit.
Keep target, cohort, policy, safety, route, mission-slot, and factory requirements in their current owning predicates.
At activation, revalidate the full relevant start preconditions before any setup, phase flags, debit, policy change, or service grant.
This means the current action eligibility and selected-state control/identity, not just enough stock.
A cost predicate alone cannot prove a valid relief contract or movement target.
Where extracting that repeated precondition is useful, place an action-specific Boolean `famine_<action>_can_start` or `migration_<action>_can_start` in the existing owner trigger file, with `= yes` calls and explicit COUNTRY/ROOT/FROM contracts.
Do not make a generic dynamic action mapper or move complete gameplay bodies into the payment layer.

Replace legacy payment/refund `@` macros with fresh central values where the exact native field accepts them.
If a payment field only accepts a variable, initialize an unscoped payment temporary from the central debit value and pass that variable.
Do not introduce unary negation of a variable token.
Keep current PP hint amounts 10/20/35 and all numeric AI weights unchanged.
The documentation does not establish `constant:` support for `ai_hint_pp_cost`, which requires a constant amount rather than a variable.
Retain the existing literal/file-local hint representation until supported central-token parsing is confirmed, and document that hint as a nominal AI hint rather than a second payment authority.

## Duplicate prerequisite and display parity

Convert the spent-resource duplicates to the same inclusive components.
This includes the explicit airlift aircraft5/airXP10 checks, the paid train checks for evacuation/distribution, and stock checks in `famine_relief_has_land_candidate`, `famine_relief_has_sea_candidate`, `famine_relief_has_air_candidate`, and `famine_relief_action_route_inputs_are_valid`.
The land candidate's existing convoy5/fuel500 logistics floor remains convoy5/fuel500 even though emergency imports pay convoy10/fuel500.
Sea retains convoy10/support50/fuel1000, and air retains aircraft5/fuel1000/airXP10.
Keep route facts and sparse donor selection unchanged.
These pre-setup stock checks must not be copied into delayed delivery after the resources have been spent.

Preserve workers' exact `has_equipment = { support_equipment > 50 }` prerequisite as a non-spend requirement, per the parent's clarification.
Its tooltip and 50 threshold remain separate from the spent tuple.
Preserve `famine_decision_threshold.air_experience_minimum = 50` and the AI-only strict 50-XP factor.
The actual airlift spent bundle includes 10 XP in `available`, `custom_cost_trigger`, component colours, and payment.

Keep all 15 getter names and their 30 ready/blocked localisation keys stable.
Each ready branch calls its matching inclusive component, and the fallback retains the blocked key.
Replace literal displayed amounts in `localisation/english/humanitarian_cost_l_english.yml` with display-only normal variables such as `humanitarian_cost_quote_pp_standard`, formatted as integers.
Recommended COUNTRY effect: `humanitarian_project_legacy_cost_quote`, in `common/scripted_effects/humanitarian_legacy_cost_effects.txt` with matching Markdown documentation and a public index entry in `chaosx_dynamic_effects.md`.
Inputs/defaults: none.
Outputs: 15 country-owned display variables, one per positive fee key.
Side effects: writes only those display variables from fresh central tuning, without payment, eligibility, receipt, population, or policy changes.
Call it at the beginning of `famine_refresh_decision_phase_from_country` and `migration_refresh_decision_phase_from_country`, and only any already bounded registration seam needed to guarantee a first visible row has a quote.
The existing `migration_project_reception_preparation_cost_quote` is the local precedent, not a source for the legacy amounts.
Do not add another periodic scan, metric, global cache, discount source, or price registry.
Cached quote variables never govern a gate, payment, refund, or receipt.
Keep all existing base, `_blocked`, and `_tooltip` aliases.
Retain the three four-resource inline rows, following the binding prompt and explicit parent direction, without deleting or concealing any resource.
No clipping or fit result is established here.

## Paid-action receipts and continuation guards

Use static action-specific state fields for the 20 upfront delayed actions.
For decision ID `<action>`, the proposed names are `<action>_cost_paid` as a STATE flag and `<action>_cost_payer` as a normal STATE scope-valued variable.
The state itself supplies selected-state identity, and the static action name supplies action identity.
Record payer with `set_variable = { <action>_cost_payer = ROOT }` only after the complete tuple has been debited successfully in the ROOT country.
There is no global payment flag and no new country-global selected-state pointer.
Do not overwrite an existing receipt for the same action/state, and never clear it at the start of an unaffordable click.
Different action names and different state containers remain independent.

Each delayed continuation requires the specific paid flag, the payer variable, a real existing payer country matching callback ROOT, selected FROM state identity, and the action's existing control/owner condition.
Use `exists = yes` only inside the stored COUNTRY scope, never to validate a STATE pointer.
For instance, `FROM = { has_state_flag = famine_evacuation_cost_paid has_variable = famine_evacuation_cost_payer var:famine_evacuation_cost_payer = { exists = yes tag = ROOT } }` supplies the identity part of the guard.
Retain the exact action-specific state-control requirements rather than tightening every controlled-state action to owned-and-controlled by default.
In the matching continuation, consume the paid flag before downstream work, then execute the entire current `remove_effect` body under that accepted branch.
Keep a caller-initialized temporary if the same block needs an accepted-payment result after a helper returns.
Clear only this receipt's payer metadata on branch completion, and only if it still identifies the captured payer.
An unmatched callback must not erase another payer's receipt or run existing generic route cleanup.
This covers success writes, state mutations, stability consequences, mission activation, achievement/report calls, transfers, and refunds, rather than guarding only the principal transfer helper.

All 10 famine actions use this pattern.
The migration upfront delayed set is `migration_prepare_evacuation`, `migration_close_border`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_distribute_arrivals`, `migration_transit_only`, `migration_enforce_closure`, `migration_third_country_resettlement`, `migration_voluntary_return`, and `migration_forced_repatriation`.
The four immediate migration actions instead place their entire current `complete_effect` under the start/affordability branch and do not invent a delayed receipt.

For cleanup, add a small subsystem-owned STATE cleanup helper in each existing decision-owner effects file, with its matching Markdown API contract.
Recommended identifiers are `famine_clear_stale_paid_decision_receipts` and `migration_clear_stale_paid_decision_receipts`.
They enumerate only that subsystem's finite static receipt fields on the current state.
Normal remove/cancel paths clear only their matching action and payer.
The existing state-control callbacks call stale cleanup on the exact changed state, clearing only receipts whose recorded payer lost the action's required control.
When the callback supplies old-controller proof, match that country explicitly rather than assuming callback ROOT is the payer.
A receipt valid for a current payer must survive a stale cancel callback from a former payer.
Subsystem retirement cleanup clears only its owned receipts on the exact retiring state.
Keep all existing cancellation behavior and timing values, including `cancel_if_not_visible = no`, unless a separately proven native requirement calls for a change.
Cancellation/control-loss cleanup is not an authorization to refund funded work.

The matching helpers have STATE scope, existing receipt fields and explicit callback/controller identity as inputs, no public outputs, no default actor, and effects limited to clearing owned invalid flags and variables.
Their exact native callback contracts require owner validation before source edits.
No new global event target is necessary.
Existing relief and civilian-transfer regular event targets remain chain-local.
Do not assume a regular event target survives from `complete_effect` to a separately executed `remove_effect`.
Use normal state variables for persistence.
Initialize every helper-produced temporary that the caller consumes before its call, including helpers used inside `if.limit` and nested owner calls.
ROOT does not rebind on scope entry, and temporary variables must never use `ROOT.` or `PREV.` prefixes.

This receipt design relies on the native same-action/state pending-decision contract.
It does not prove that an old callback from a former activation cannot arrive after a new receipt for the same action/state/payer is written.
No callback generation UID is exposed by the inspected source/documentation.
Action/state/payer checks reject unpaid, wrong-action, wrong-state, and wrong-payer continuations and consume an ordinary repeated continuation once while no new activation intervenes.
They are not proof against an arbitrary same-payer ABA callback.
Do not invent a UID, a fake generation, or claim general replay safety.

## Four famine relief setup actions

For imports, escorted convoy, airlift, and invitation, put the full start and complete-fee guard before reserve refresh, request/mode writes, donor selection, and contract creation.
Retain selection before debit so a failed donor/route setup remains uncharged.
Immediately after setup, recheck the exact current contract and complete tuple in ROOT before debit.
A contract created by this attempt must not survive a rejected final payment.
Keep existing valid invitation-staged contracts untouched when another attempted imports payment rejects.
Distinguish newly created setup from reused setup with a caller-owned temporary and exact captured contract identity, not a blanket `famine_relief_cleanup_contract` rejection path.

Record the action's paid receipt only after debit, alongside the existing contract generation and exact donor-state pointer for that action.
Proposed extra fields are `<action>_cost_contract_generation` and `<action>_cost_donor_state` for these four actions.
Before delayed work, require the current contract's actor, fixed action mode, stored donor, and generation to match that paid receipt.
The existing generation is `global.date` at creation, so it is additional identity evidence rather than a globally unique nonce.
Do not claim it distinguishes two same-day reconstructed contracts with identical endpoints.

Guard the entire imports/convoy/airlift `remove_effect`, including the call to `famine_relief_deliver_contract` and its later success consequences.
The only current decision delivery callers are these three, so caller guards are the smallest repair.
Do not change the public finalizer to guess an action from route mode or an invitation receipt.
Retain its donor, stock, endpoint, relation, capacity, control, and exact-transfer checks.
Do not require another full fee at delivery after payment already spent it.
Guard invitation's later stability branch with its distinct paid receipt and matching land contract.
Consume only the invitation paid-action receipt after its removal, leaving the staged land contract for a later independently paid imports action.
If imports delivers before invitation's removal, the existing invitation contract check already prevents stability after the contract has gone, and that behavior remains unchanged.
Contract cleanup must clear only relief metadata belonging to the exact rejected/expired contract, leaving independent action receipts untouched unless their own identity is invalidated.

## Deferred negotiation and measured refunds

`migration_negotiate_corridor` gets a STATE pending flag and payer variable, `migration_negotiate_corridor_cost_pending` and `migration_negotiate_corridor_cost_payer`.
Its new bounded `complete_effect` records that pending action only after current start conditions and the full PP35/infantry100/fuel500 bundle pass.
It pays nothing there.
At removal, match and consume the pending action, recheck the full bundle in ROOT before request writes and `humanitarian_corridor_prepare_contract`, then recheck immediately before `humanitarian_corridor_submit_offer`.
Preserve the current debit only after a valid submission result.
The submit helper is synchronous source work, but its downstream side effects must be reviewed for any payer mutation before the final debit.
If a final affordability branch rejects after a new offer exists, retire only that exact attempt/offer through the existing owner cleanup before exposing an unpaid offer, without cancelling another pending counterpart contract.
Do not convert this action into an upfront deposit or charge rejected preparation/submission.

Keep the five existing refunds exactly tied to the measured `civilian_transfer_actual_origin_debit` branch: `famine_evacuation`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_voluntary_return`, and `migration_forced_repatriation`.
Refund only within a consumed matching paid-action continuation and use the original frozen tuple from central tuning.
No paid receipt means no transfer and no refund.
Positive actual origin debit means no blanket late-failure refund.
No new refund is proposed for partial delivery, funded repair, normal policy work, actual passage, requisition, integration, or resettlement.
Any broader failure-policy issue stays a separate unresolved design finding.

## Migration and next-owner handoff

1. Parent reviews this plan and the immutable archive, including bytes/hashes and source coverage, before the source owner patches.
The parent subsequently reported archive commit `e6ec73bc` committed with all 12 raw source blobs verified against their copied-byte hashes.
That is parent-supplied evidence, not an independently repeated Git audit in this pass.
Use the fresh baseline and exact saved scenarios from the active probability auditor, then its required same-case comparison.
This architecture does not replace either result.
2. Add the central table, component/profile predicates, and display projection with actual call sites and Markdown docs.
3. Replace all 25 availability/native custom-cost gates and the matching 15 resource selectors, including airXP10 in the airlift custom-cost gate.
4. Convert duplicated spent stock requirements and relief pre-setup logistics checks to inclusive components, preserving the separate strict worker support50 and AI-only50XP checks.
5. Guard all 24 upfront payment paths and their whole effect bodies.
Add the 20 delayed receipts and matching whole-continuation/cancellation guards, then the four exact relief contract bindings.
6. Add the negotiation pending boundary and deferred rechecks without changing charge timing.
7. Wire stale receipt cleanup to the existing exact state control/retirement paths, then document the five preserved refund branches and callback limits.
8. Run actual-source causal cases and the mandatory auditor comparison, review final docs and localisation, and let the parent own final integration/commit.

Recommended source files are the two existing decision files, `humanitarian_legacy_cost_constants.txt`, `humanitarian_legacy_cost_triggers.txt/.md`, `humanitarian_legacy_cost_effects.txt/.md`, `humanitarian_cost_scripted_localisation.txt`, `humanitarian_cost_l_english.yml`, both existing decision-phase effect files, both decision-owner effects/docs, `famine_relief_triggers.txt`, and the existing exact cleanup call sites in `famine_core_effects.txt` and `migration_core_effects.txt`.
`famine_relief_effects.txt/.md` needs a narrow update only if exact attempted-contract cleanup or paid identity lifecycle requires it.
Update `chaosx_dynamic_effects.md` for the neutral public quote API and link the component/profile contract, then the existing `docs/systems/famine_system.md` and `docs/systems/migration_system.md` for owner lifecycle evidence.
There are no new icons or assets, and existing cost texticons remain consumers.
There are no new events, focus surfaces, scripted GUI buttons, map writes, categories, or workbook changes in this repair.

## Meaningful causal validation

Use the actual production component/profile triggers, decision guard bodies, receipt writes/consumption, debit primitives, and existing refund paths.
Mocks may stand in for native reserves and out-of-scope transfer execution but must record that boundary.
Do not count a mocked receipt or synthetic success counter as proof of the actual mapper.

| Case | Required source-model result |
|---|---|
| Each component at zero or one below, all other components exact | Component red, profile false, available false, custom cost false, no debit/setup/paid flag |
| Complete exact tuple and one above | All components ready, profile/gates true, exactly one complete tuple debit |
| Exact aircraft5, fuel1000, XP10, PP20 with valid air route | Duplicated spent checks do not mask equality, airXP10 included in all four cost surfaces |
| Worker support50 and support51 with its spent tuple exact | Strict non-spend support50 requirement preserved independently, no support debit |
| AI airXP49/50/51 | Existing strict AI-only50XP modifier unchanged, no additional fee |
| Reserves fall after selection | No setup, phase/policy/service writes, charge, receipt, later work, or refund when final start fails |
| New relief contract created then final payment refused | No funded receipt and no live unpaid contract from that attempt, no reserve delivery or invitation stability |
| Imports payment refused with pre-existing invitation contract | Existing invitation contract/receipt retained, imports remove cannot deliver |
| Paid invitation then paid imports | Two separate current fees, invitation does not deliver, imports delivers only under its own paid receipt |
| Paid delayed action with payer's reserves exhausted afterward | Existing funded continuation uses paid proof rather than charging or checking nominal stock again |
| Wrong action/state/payer callback, repeated callback before new activation | No unrelated work/cleanup/refund, ordinary matching receipt consumed once |
| Two states or two actions pending | Independent receipts, one cancellation leaves other receipt intact |
| State control lost then stale cancel/remove | Exact former-payer receipt invalidated, new valid payer receipt untouched, no old-payer continuation |
| Negotiation short at removal or before submission | No preparation/submission/debit when corresponding full guard rejects, pending attempt closed |
| Negotiation succeeds/fails setup/submission | Current successful offer charged once, rejected setup/submission uncharged |
| Each of the five measured zero-origin-debit cases | Only matching paid action refunded exactly once, every tuple component restored |
| Positive origin debit with later partial/deadly outcome | No blanket refund and no replayed origin debit |
| Display variable poisoned or stale | Affordability/debit/refund use fresh central tuning, quote refresh restores visible amounts |

Probability scenarios must come from the binding source matrix and the auditor's frozen fixtures.
Relevant named authorities include `prob_famine_relief_dense`, `prob_famine_relief_blocked_island`, `prob_relief_donor`, `prob_corridor_acceptance`, `prob_nuclear_evacuation`, `prob_outbreak_reception`, `prob_capacity_exhausted_border`, `prob_forced_return`, and `prob_integration`, with explicit fee boundary cases added by the owner/auditor.
The working improvement package's `fm09_service_affordability` row is descriptive provenance, not acceptance authority for a replacement scenario fixture.
Keep all willingness weights numerically identical while measuring the changed eligible pool.

## Evidence, unsupported fields, and limits

The connected tool list exposed reference context/search/read, source lookup, decision inspect, event inspect, probability inspect/compare, and GUI/map routes.
Live schemas were inspected, including declared decision scenarios and revision-bound reference reads.
No new expensive MCP retry was made, following the parent's explicit direction and recorded actual 600-second cost-reference timeouts.
The required reference route is exposed but has no successful cost-context/search/read result for this task, so local document reads below are the reference fallback and are not MCP retrieval evidence.
No linked event, focus, scripted GUI, or map surface is introduced by this architecture.

The latest `legacy_custom_cost_affordability_audit_20261003.md` records a narrow negotiation `hoi4.decision_inspect` result, `DECISION_ANALYZED_PARTIAL`, with decision coverage false and an unbound scenario.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86f9a727fe3ab30767f110f133df4edaaa1e2c1670e816108c714541ebcf0875/242759efc89dfa2d55d29126e5f888efb7f6cae26e02ca81a7047865a3a98e94/decision-cb25461a3621fb9d0a57fe79.json`.
The audit's attempted range read failed with `Mcp error: -32603: Artifact provenance manifest is unavailable` and returned no artifact body.
No complete decision scenario inspection for these 25 actions, native click result, timed callback execution, render, or probability comparison is established by this handoff.
The parent must retain those exact gaps and the active auditor's final evidence.
The parent subsequently reported a live baseline inspect route with an empty decision adapter and authorized source work after accepting this handoff, while leaving the numeric evidence gate outstanding.
Route availability and the frozen archive therefore do not become a measured eligible-pool comparison.

Avoid the existing universal resource adapter in this bounded patch.
`chaosx_universal_cost_triggers.txt:386-404` reads `train_equipment_1` and `convoy_1`, while these decisions use `train_equipment` and `convoy` archetypes for both checks and debits.
`chaosx_dynamic_effects.txt:790-793` also removes `convoy_1` in its convenience helper, so it is not an interchangeable debit primitive for this repair without separate proof.
The existing stockpile helpers were reviewed at `chaosx_dynamic_effects.txt:746-813` and documented at `chaosx_dynamic_effects.md:302-324`.
They do not provide complete profile gates, paid action identity, or deferred continuation protection.

Source anchors reviewed include `famine_decisions.txt:229-307,389-453,614-645,776-807,898-929,982-1115`, `migration_decisions.txt:528-543,584-645,705-728,773-1118,1176-1198,1319-1362,1451-1551,1639-1701,1754-1838,1899-1959,2049-2114,2157-2484`, `famine_relief_effects.txt:363-421,426-521,562-605`, and `famine_relief_triggers.txt:134-201,360-411,551-607`.
Existing lifecycle paths are `humanitarian_runtime_effects.txt:30-32,74-76,94-96`, `famine_core_effects.txt:2950-2961`, `migration_core_effects.txt:2147-2160`, and `humanitarian_runtime_on_actions.txt`'s exact control-change/annex scopes.
Existing quote and inclusive precedents are `migration_decision_phase_effects.txt:6-17` and `migration_reception_preparation_triggers.txt:4-10`.

| Direct local reference read | Relevant lines | SHA-256 revision |
|---|---|---|
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 305-355, native cost keys/manual debit and complete/remove/cancel order | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 263-327, 435-449, event-target and scoped/temporary lifetime | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 255-267, ROOT/THIS/PREV/FROM and owner/controller | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| Installed `common/decisions/_documentation.md` | 1-45, actor/target scopes and evaluation frequency | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |
| Installed `documentation/script_concept_documentation.md` | 216-245, shared constants and explicit field support | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `common/script_constants/documentation.md` | Complete schema and basic examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed `documentation/triggers_documentation.md` | 3073-3081,3835-3851,3957-3966,4547-4554,7561-7568,7649-7656 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `documentation/effects_documentation.md` | 1252-1265,1388-1395,1854-1861,2486-2493,6496-6512 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed vanilla `common/decisions/AFG.txt` | 490-500, native custom row with manually charged complete effect | `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7` |

Installed paths in this table are under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Additional direct wiki reads were `Triggers:2359-2400`, `Effects:4683-4715`, and `Localisation:184-210` for Boolean helper calls and formatted variable display.
No installed documentation filename dedicated to scripted localisation was found in the bounded documentation filename search, so the actual Open Reception selector/YML precedent and local wiki formatting rules remain the evidence for that projection.

Current source SHA-256 revisions at this read are `famine_decisions.txt` `52E84B51B6C9FAF5827F3152613870E4EBBD65215EDD35D70E913D18BA01DFAA`, `migration_decisions.txt` `66D5DACCB52B11787A53A899B748B2E8F5427E0A8B46A4B303E8BB6A37A01D2F`, `famine_relief_effects.txt` `571C9A3BCC299CF67A0A32F1844859D226137C4E434026A7E9AB899E733B2959`, `famine_relief_triggers.txt` `A90EF53B81102D7E3BBCA5D0A6856EA4054428E46DEE2B4AC14DC596B2347B4F`, and `humanitarian_cost_scripted_localisation.txt` `73022A01B7FC1521DE409B97395C628A3373A86B8F687D7AF6C489EC730551D1`.
Part 6 was read with SHA-256 `F7486EFC6155FAC0E32306082B48A92F1798392E4809B6625615B29B2F1CB2A4`, and the current decision prompt with `1A96686AD9D4629A93708E980528CE06615EC2C0DF28DAFCF788AD7D8DF0AC0B`.
The prompt changed from the audit's earlier cited hash, so this handoff does not claim that old revision is current.

Native uncertainties remain exact: field-specific `constant:` parsing, native equipment archetype subtraction/aggregation, click-time revalidation, targeted callback identity/pending exclusivity, same-payer ABA after another activation, native cooldown after rejected setup, and actual inline width.
Source logic can be checked without settling those native behaviors.
No fallback or simplification was implemented.
The architecture preserves all requested fee types, numeric AI weights, timing, worker prerequisite, and measured refund boundaries.
Implementation, complete MCP scenario coverage, frozen-baseline/same-case comparison, and parent integration remain outstanding.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was changed.
