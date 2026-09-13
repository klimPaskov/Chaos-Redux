# Private conventional incidents handoff, 2026-09-08

## Disposition and authority

Implemented owner-local source, accepted and queued parent integration.
The parent task explicitly approved private counterparts for Electronics, Materials, Rocketry, High Energy, and Biomedical, reusing each existing public incident identity and penalty constants.
The parent confirmed that one incident/recovery means one concurrent pair per family, with later actual stage outputs allowed to create new incidents and preserve counts.
The parent approved the new package-local scripted-localisation file for per-resource cost colours.
The parent subsequently approved native-decision-only begin callbacks that trust prior native CIC admission and recheck only requirements and three direct payments.
No existing Computation, stage, bridge, callback, shared category, or shared dynamic helper file was edited.
No Git staging or commit was performed.

## Files added

- `common/scripted_effects/016_mengele_conventional_incident_effects.txt`
- `common/scripted_effects/016_mengele_conventional_incident_effects.md`
- `common/scripted_triggers/016_mengele_conventional_incident_triggers.txt`
- `common/decisions/016_mengele_conventional_incident_decisions.txt`
- `common/dynamic_modifiers/016_mengele_conventional_incident_modifiers.txt`
- `common/scripted_localisation/016_mengele_conventional_incident_localisation.txt`
- `localisation/english/016_mengele_conventional_incident_l_english.yml`
- `.tools/audit_mengele_conventional_incident_contract.mjs`

## Implemented surfaces

Five matching `mengele_event016_<family>_incident_recovery` decisions are appended to the existing `mengele_clone_army_category`.
The exact family tokens are `electronics`, `materials`, `rocketry`, `high_energy`, and `biomedical`.
Each owns `brilliant_scientist_mengele_<family>_incident`, independent incident/recovery flags and counts, and three direct-payment receipt variables.
The exact penalty fields/constants match the five entries in `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`.
They are guarded by private active state and the existing strict private provider lifecycle.
No public incident variables, native project state, learned technology, or provider output is changed.

Recovery profiles remain Electronics technical 35 PP/300 support/500 fuel/2 CIC/60 days, Materials and Rocketry industrial 50/600/1500/3/90, High Energy exotic 75/1000/2500/4/150, and Biomedical biological 60/800/750/3/120.
Only those four spendable axes are used.
The four native CIC file constants mirror existing profile constants, and regression checks equality.
Direct payments are snapshotted once and cleared before refund or settlement.
Cancellation and invalid expiry refund exactly once, successful recovery records history once, and full cleanup removes the native decision after refunding.
Malformed partial receipts do not generate an inferred payment, and normal expiry/cancellation now clear their recovery flag and leftover cost variables.
The unresolved incident and penalty remain under a valid provider, and no success history is recorded.
Started text follows exact receipt creation, success text requires the finish callback's explicit success result, and cancellation text is conditional on a complete recorded payment.
History and learned state survive every cleanup.

The helper reference documents every fixed record, clear, begin, cancel, finish, and cleanup identifier, input, output, side effect, and call site.
The single parent deterministic dispatcher is `brilliant_scientist_mengele_record_requested_conventional_incident`.
It reads existing `mengele_event016_project_family` and `mengele_event016_requested_stage` without writing either.
Its temporary result is `mengele_event016_conventional_incident_recorded`.
The aggregate cleanup hook is `brilliant_scientist_mengele_cleanup_conventional_incidents`.
No event target is required.

English localisation adds modifier names/descriptions, five recovery titles/descriptions/requirement/start/success keys, two common cancellation keys, and four profile cost families.
Each profile supplies its four normal/red resource entries, a cost row, blocked alias, and cost tooltip.
The 16 `GetMengeleIncident<Profile><Resource>` selectors turn only deficient costs red.
No formatting characters are stored in scripted localisation.

## Assets and references

Reused prototype sprites/DDS: `electronics_guidance_prototype`, `advanced_materials_prototype`, `rocketry_propulsion_prototype`, `high_energy_physics_prototype`, and `biomedical_acceleration_prototype`.
Each resolves from `interface/016_brilliant_scientist_project_icons.gfx` to `gfx/interface/decisions/016_brilliant_scientist/projects/<suffix>.dds`.
The source regression reads every referenced DDS and validates its signature.
The support texticon is defined in `interface/chaosx_texticons.gfx`, with PP, CIC, and fuel texticons in installed vanilla `interface/texticons.gfx`.
No asset generation, replacement, or sprite edit occurred.

Required references consulted include the offline core wiki pages, Decision modding timer/cancellation sections, Data structures event targets, Effects scripted effects and supported calls, vanilla effects/triggers/modifiers and localisation formatter documentation, script constants documentation, and `common/decisions/_documentation.md`.
The vanilla `GER.txt` fort-construction decision around lines 1573-1609 demonstrates native CIC modifiers, cancellation, and custom payment.
Existing private Computation effects/triggers/decision/modifier/localisation and matching markdown were read as lifecycle precedent.
Shared dynamic helper source and docs were checked and its support/fuel debit helpers reused.

## Meaningful validation

`node .tools/audit_mengele_conventional_incident_contract.mjs` passed 363 source/API scenarios, comprising the original 165 behavioral cases, 194 forced-dispatch cases, and four native private-hook cases.
This executes the actual source AST and the unchanged shared debit helpers under explicit stubs, rather than independently restating desired arithmetic.
It covers four-resource equality and each one-below boundary, duplicate record/begin/cancel/finish calls, later incident history, invalid provider at cleanup and expiry, original receipt refund after profile tuning changes, simultaneous families, selector routing and invalid selectors, per-resource cost colouring, and exact-CIC admission under both modeled native reservation orderings for all six families.
The sixth-family cases read the parent's updated Computation effects, triggers, and decision without editing those files.
The final run's conventional effects SHA256 is `b26e66f7aa38faf7e34f72007b6a9b86dbd59ed992ce810639978e26eb8e97c9`, and conventional trigger SHA256 is `e087d0a19e3a04546e8a69d795aa5fc2863edb9958411408823af22e5d2b8f49`.
The command emits all eleven source hashes for repeatable comparison, including parent stage source `386b7dc701070e03e02e82c6ea1e140934c8f579ebfd74b31e310e5b06c7718e` and native project source `f395e6d7de1df08185d8f304ed871b568f62866803b97d76198bc1b9984109ce`.
After the parent's approved AI attachment, the checker replaces its obsolete absent-AI assertion with exact AST equality for all six recovery decisions.
Each must contain only `base = constant:brilliant_scientist_project_board.ai_urgent`, with no modifier or extra entry.
The AI-only reconciliation preserved the initial 165 behavioral scenarios plus six structural AI assertions.
The dispatcher extension adds 194 cases, and the Materials/Biomedical native private branches add four cases, for the current total of 363 scenarios.
The weighted conventional decision source SHA256 is `2ca8448ad530c334b4143eed719a2d048eb1afe28d9107e289bebe30ad36b881`, and Computation decision SHA256 is `896a8d98dc7f6ac3b9f9d8ea78fe7fa91998cc3fbe05fbe4a17d32ee89424309`.
This test-only reconciliation changes no gameplay and does not replace the parent's pending probability comparison.
It checks exact penalty parity, CIC profile mirrors, sprite definitions, and DDS paths.
Provider validity and native timer/reservation ordering are model assumptions, and engine resource caps are not modeled.
No engine acceptance claim follows from this regression.
Forced dispatch executes the actual two-entry `random_list` AST and existing Computation pressure-loader AST under an explicit branch index, never a PRNG.
Both outcomes are exercised for every family and all four stages, with pressure/complement pairs 5/95, 10/90, 18.75/81.25, and 24/76.
Coverage includes invalid or absent family/stage selectors, invalid provider, own incident/recovery guards, every distinct other-family active/recovery pair, selector and persistent-history isolation, and immediate duplicate suppression after a real recorded incident.
The checker also structurally verifies that the paid-stage receipt-match branch clears its active receipt before the successful-output-gated incident hook and invokes that hook before native late adoption.
It does not execute the array-backed paid-stage receipt lifecycle, so replay prevention after incident recovery remains an explicit untested causal-receipt limit.
The output sets `probabilityValidation: false`, and no forced-branch result is presented as probability, sampling, or timing evidence.
Native risky-option checks inspect the exact `sp_brilliant_scientist_advanced_materials_reward_self_propagating_batch` and `sp_brilliant_scientist_biomedical_acceleration_reward_unlicensed_trial` reward blocks.
They retain `fire_only_once = yes`, use the strict private provider gate first, and retain a current-public-host fallback with the existing public pressure/accident calls.
Both forced private outcomes execute the actual branch for Materials and Biomedical, verify Prototype pressure 10/90, and verify private family/stage selectors clear afterward without writing public selectors.
The native once-only selection and public fallback are structural source checks, not engine reward-selection or public-outcome execution evidence.
The strict parser extracts only the named native reward blocks because unrelated bare-token reward lists are outside its transaction subset.

A read-only decision auditor ran as `/root/mengele_conventional_incidents/review_incidents`.
Its first review identified stranded malformed receipts at normal expiry, unconditional refund wording, and started wording despite failed direct-cost recheck.
All three findings were patched within the five-family ownership.
Regression adds 15 five-family malformed-expiry cases, 30 direct-cost race cases over both reservation orderings, and three separate Computation malformed-expiry cases against the parent's corrected source.
The same auditor accepted the correction review with no remaining source/API findings in scope and independently reran the 165-scenario regression successfully.
It confirmed malformed cleanup, start feedback gating, conditional refund text, and the parent aggregate cleanup hook.
The reviewer made no file changes and retained the explicit engine-evidence limitations.
Its earlier unwired-cleanup statement is superseded by the verified parent hook in `common/scripted_effects/016_mengele_project_stage_effects.txt`, inside `brilliant_scientist_mengele_cleanup_provider_receipts`.

## MCP evidence and blockers

The dispatcher test extension first invoked `hoi4.probability_inspect` on the exact conventional effects file.
It returned `PROBABILITY_SOURCE_INSPECTED`, adapter `random_list`, two candidates, two required inputs, complete pool, and zero unresolved entries.
Discovery artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbbf301039a14d2b56b862abf7420407c6490d0cba042e607211556eedf10b41/1b283aef03a9e5e67b0bf83ea5fc2191ad0fbb09c42a9e7be4c1d52f3cc877e1/probability-inspect-d0e0a8ff1492.json`.
This is discovery only, while the parent probability auditor owns the comparison and probabilistic acceptance.

Narrow Event 016 trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, indexed helpers 0, 8737 unresolved nodes, and one blocking diagnostic in the analysis counts.
Its validation states that workspace-wide helper projections and lifecycle passes were deferred.
This is navigation evidence only.
Trace artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ed8cf0e613233c3f83a8a369e2e4e62aa3d59df76837fb8afbe922db57433b1/ee37c07b70207c3ba36c3fbd0c21adf878191f29b3295264f317b085905770a1/event-trace-4bccb6ec7fe1.json`.

Matching narrow state render returned `EVENT_RENDERED_PARTIAL` with the same focused boundary and helper count.
State render data:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01ca07de523e04a698fa03bbc0878787a52a52c4287eb7af5fabccbca3b446b5/670ab986438f3d3212f4e842f6411b5c8a42f0e9fa932ca3436d33ff4087f59e/event-state-4bccb6ec7fe1.json`.
Render manifest:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/896e593da0bea0f48cb2d52b21d072dd3c55efed19f4aad4121a1de0665cec91/42cbe870de2a9687ae7ad7a957786a1303c6a34e8e40916a0722e0ef962197f5/event-state-4bccb6ec7fe1-manifest.json`.

Comparison using before revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d` returned `EVENT_REVISION_NOT_CACHED`, with blocker text "Requested event graph revision is not cached".
No before/after engine helper evidence was available from this route.
The trace/render report was not relabeled as a graph-bearing comparison artifact.

## Parent work still required

1. The parent obtained the absent-surface baseline and attached the existing Computation `ai_urgent` recovery score to all five rows; the matching probability comparison and auditor acceptance remain pending.
2. The parent attached intrinsic stage pressure at 5/10/18.75/24 through the existing pure Computation pressure loader, without Kruger Exposure, with probability acceptance remaining parent-owned.
3. The parent attached `brilliant_scientist_mengele_dispatch_conventional_incident` after successful paid-stage output and before native late adoption, with causal-receipt replay validation still requiring the parent's full stage harness.
4. The parent reports aggregate cleanup attached in `brilliant_scientist_mengele_cleanup_provider_receipts` immediately after existing Computation cleanup, and owns final callback validation.
5. The parent wired the Materials and Biomedical native risky options with retained `fire_only_once`, strict private dispatch, current-public-host fallback, and private selector cleanup, with native selection acceptance remaining parent-owned.
6. Reconcile event docs, acceptance specs, workbook, and parent final audits.
7. Review total action budget in the existing private category, since this package alone adds at most five visible emergency recoveries.

Parent AI attachment uses the accepted 2026-09-08 private incident contract and baseline fixture `testing/016_mengele_conventional_incident_probability_baseline_2026-09-08.json`.
The AI attachment changed no admission predicate.
The subsequent parent-owned weighted dispatcher uses its own exact five-family validity predicate and the two-entry existing pressure/complement pool.
The frozen baseline contained no weighted candidates, which is not equivalent to a zero willingness score.

Native CIC reservation ordering relative to complete_effect and native release were not engine-tested.
The parent-approved begin boundary is independent of reservation order.
Four shared direct-cost profile predicates check PP/support/fuel, full four-cost predicates invoke them plus CIC for decision admission, and begin callbacks recheck requirements/direct costs without rechecking already-reserved factories.
These begin helpers are native-decision-only callbacks and must not be exposed as general payment/start APIs.
Exact-CIC tests demonstrate debit and refund under both modeled orderings.
This source proof must not be described as a validated engine transaction.
Likewise, refunds issue the original script amounts but native resource caps may limit the resulting stored total.

No unapproved gameplay simplification was made.
End-to-end completion remains blocked by parent integration and the stated engine evidence limits.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents.
No skill was created or changed.
