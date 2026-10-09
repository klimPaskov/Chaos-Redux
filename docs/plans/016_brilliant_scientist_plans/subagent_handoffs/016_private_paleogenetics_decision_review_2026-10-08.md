# Event016 private Paleogenetics decision integration review

Assigned audit date: 2026-10-08.
Sealed from retained review on 2026-10-09; the filename preserves the assigned date.
Disposition: bounded read-only source audit delivered, with two owner-resolved frontend findings and explicit pending AI, native and visual evidence.
Parent owns final integration and commit.

## Scope and conclusion

The accepted authority is [016_private_paleogenetics_deployment_acceptance_2026-10-08.md](../016_private_paleogenetics_deployment_acceptance_2026-10-08.md), SHA-256 c8c4fa1fb3887d2206b9e97fc68ad75ce39d8f55502bd18d33adeb1c43ca9b0e.
This review covers the first paired-construction tranche: free reserve/hatchery selection, the existing paid Deployment decision, retained construction proof, cancellation/recovery presentation, narrow generic dispatch/cleanup integration and the CXT observer.
Staff training and demobilization, the transport pen, handling kits and breeding remain accepted and queued.
Paired construction does not complete the full private Paleogenetics payoff or Event016.

No additional blocking source defect was confirmed in the bounded inspected paths after the parent fixes below.
This is a source-review conclusion at the sealed identities, not an engine, visual or AI acceptance claim.
The audit introduced no simplification and changed no gameplay source.
Only this assigned report was written; its destination was absent on disk and HEAD at the earlier retained check and remained absent on disk immediately before creation.
No fresh Git operation was performed during sealing on 2026-10-09.

## Findings, ordered by significance

1. **Open evidence dependency: weighted AI acceptance.**
The separate chaosx_ai_probability_auditor is resuming.
Its actual final report, named scenarios and applicable baseline/post-change comparison must be reviewed before an AI acceptance claim.
This audit does not supply willingness scores, click probabilities or balance approval.
The new reserve selection, hatchery selection and recovery rows use ai_medium; Deployment retains its existing medium score and war/factory modifiers, while reset uses zero.
No weight retune was made by this review or the final frontend polish.

2. **Open evidence dependency: native decision and row presentation.**
The bounded live decision inspection returned INTERNAL_ERROR without an evaluated scenario or artifact.
The GUI routes produced source/synthetic native-shell evidence, including an explicit empty idle fixture, rather than these decisions populated with actual campaign row data.
Native parameter behavior, reservation/clock/callback ordering and actual tooltip glyph/width/click-state presentation remain unverified.
These limits constrain completion claims; they are not proof of a source defect.

3. **Resolved source defect: incomplete or invalid selection could not be reset.**
At the reading point, mengele_event016_paleogenetics_clear_site_selection required selection_is_valid.
A reserve-only selection, or a selected pair whose capacity/control became invalid before payment, could therefore lose the reset action while no paid transaction existed.
The old site-decision reading-point hash was d3e79d5df4b35d3c7592caf1197d63a17fc050facea4245f5db55280e4321c15.
The parent changed lines 61-67 of common/decisions/016_mengele_paleogenetics_site_selection_decisions.txt to choice_is_open plus OR(has_variable selected_reserve, has_variable selected_hatchery).
The clear effect still requires the free-choice gate and clears candidate fields only.
The current file hash is cfd888f424460669e24c0b9e78afb65c2082169e7f480ef71a16b0d0594b9d65.
The parent added actual frontend cases for resetting/inverting an incomplete two-state pair and rejecting reset of a funded pair.
This finding is owner-resolved.

4. **Resolved parent preflight defect: native admission omitted the operational entitlement required by BEGIN.**
The parent identified this before commit.
The earlier requirements could admit the native four-factory/480-day decision even though the core would reject its direct-payment preflight for missing brilliant_scientist_paleogenetic_formations_tech.
The final requirements now explicitly require that technology at common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt:53.
The cancellation predicate at lines 119-127 also includes loss of private Prototype completion or this entitlement, alongside provider, receipt, payment-proof and current-site failures.
The requirement tooltip names restored-creature operational access.
The parent added actual native-consumer cases for absent-entitlement admission/debit rejection and entitlement-loss cancellation/refund before any output attempt.
The final trigger hash is 5863eb3de1256da1bb4efb51c236bb3653e49e9dfed3715eb88a83297b6c1ea6.
This finding is owner-resolved.

## Transaction, lifecycle and exploit review

The free-choice gate requires the private provider and Prototype, unfinished Deployment, no pending paid deployment and an empty family receipt.
Reserve and hatchery selection use state_target = any_owned_state and on_map_mode = map_only.
FROM is the native selected state; candidate predicates qualify against ROOT, while selection effects recheck against the immediate payer PREV.
The paid pair is distinct and frozen before debit, with actor/action/family/stage/serial and quantity one for each component.
Free reselection cannot alter paid pointers.

Native admission requires four available civilian factories plus the direct resources and operational requirements.
The literal Deployment complete_effect alone sets the native-entry marker.
BEGIN consumes that marker on every path, requires the exact family/stage and rechecks non-CIC admission conditions.
It does not recheck its own already-admitted native factory reservation.
The current direct quote and debit path carries 130 PP, 975 aggregate support equipment and 1,500 fuel; the native decision carries four CIC for 480 days.
The generic quote branch loads only those three direct costs and the factory commitment.
The older table's truck/train/manpower/XP entries are not additional charges in this transaction.

The generic begin/cancel/finish wrappers dispatch exact Paleogenetics Deployment to the specialized core and retain their default paths for other requests.
Consuming wrapper/core frames initialize the temporary outputs they use.
The retained driver includes a cold/warm temporary-storage boundary and an actual non-Paleogenetics Alien Theory regression; that single regression is not exhaustive proof of every unrelated family.

Each construction attempt measures its own immediate native before/after level and credits only an exact increment of one.
Competing construction cannot satisfy the receipt.
A delivered component is skipped on recovery; a capacity-blocked undelivered component can wait.
Full Deployment history and success are published only after both measured outputs and current qualification exist, before the generic active row is retired.
The core preserves durable paid scopes, quantities and component measurements after success.
It does not grant neutral Prototype access again or write Kruger history.

Before any construction attempt, authenticated cancellation refunds the three recorded direct costs once.
A partial output keeps the paid authority and physical output; recovery attempts only the remainder, with no second debit, timer or factory assignment.
Ambiguous zero/fractional/extra construction readback and unverified payment/refund are quarantined rather than blindly retried or fully refunded.
The retained refund fields preserve the observed credits and original obligation if the default refund already retired its generic row.

Provider cleanup's bounded family loop calls the public cancel wrapper, which dispatches this exact family/stage to the specialized cancellation path.
This preserves partial/fault proof and handles authenticated no-attempt refund on provider loss.
No new periodic hook, world scan or blanket demolition was introduced.
Repeated callbacks are guarded by pending/delivered/busy/receipt proof at the source level.
A mutable current serial and entry marker still do not establish native same-action callback generation identity.
This report makes no claim that remove_decision executes remove_effect.

Recovery visibility intentionally uses provider + pending + paid_identity_is_valid + inactive timer.
Availability uses recovery_is_ready, which requires actual positive matching payments, current provider/Prototype/technology/sites, no busy/construction fault and capacity for an outstanding component.
Thus valid identity can keep a fault row visible while actual construction remains unavailable.
The paid-site name getter uses identity-only reads; the status getter distinguishes payment/refund uncertainty, construction uncertainty and lost current sites.

## Decision presentation and cognitive load

Selection is map-only and phase exclusive.
Deployment requires a selected valid pair; reset remains available for partial/unbuildable candidates, and pending work blocks free choice.
The recovery row replaces admission during retained work and has no native timer or CIC modifier.
This supports the accepted five-current-stage-rows plus one reset budget for the added Paleogenetics surface.
The simultaneous state of every other Biological Programs family was outside this audit, so no category-wide maximum is certified.

Player-facing values have clear roles: the named candidate pair is editable before payment, the named paid pair is immutable transaction identity, and the two delivered/outstanding statuses identify what remains funded.
Costs, current ownership/control, capacity, Prototype and operational access are described near the action.
The descriptions use concise native text rather than raw trigger lists or numeric-ledger dumps.

The final Deployment output tooltip now calls GetMengelePaleogeneticsDeploymentComponentQuantity for both components.
That pure getter copies constant:mengele_paleogenetics_deployment.component_quantity to a temporary display scalar and selects mengele_event016_paleogenetics_display_quantity.
The English key uses integer |0 formatting.
It displays one infrastructure increment and one civilian factory without duplicating a tuning value in prose.
The getter adds no payment, construction, receipt, history or AI behavior.
Its actual rendered width and repeated getter evaluation remain outside the empty native-view evidence.

There are no mission definitions in these scoped files.
The 480-day construction action is a timed decision owned by the private payer in mengele_biological_programs_category, targeting the frozen reserve and hatchery.
Success requires both physical increments; failure/cancellation retains or refunds proof according to the attempt boundary.
Duplicate-output risk is addressed by the paid receipt, attempted/delivered flags and measured component state.

The cost-count audit finds four spendable/committed types: PP, support equipment, fuel and native CIC.
Three direct costs appear inline with pol_power, support_equipment_text_icon and GFX_fuel_texticon; the factory commitment uses civ_factory in its native cost tooltip.
Base, blocked and tooltip keys are present.
The three colour getters use the same individual affordability predicates consumed by native admission.
No fifth charge was found in the inspected debit path.
Selection, reset and recovery cost zero.

## CXT and source-test evidence

The inspected chaosx_cxt_event016_probe_paleogenetics_deployment body is gated to initialized CXT.
It reads production selection, authentication, delivery, recovery/fault and measured-payment state into CXT-owned flags/scalars.
It contains no production grant, debit, refund, construction or history call.

The sealed parent receipts report **51 core cases + 29 additional frontend/native-consumer/CXT cases = 80 modeled source cases**.
This auditor read the results and verified current recorded source hashes; it did not independently rerun the drivers.
The current [parent_core_result.json](../../../testing/event016_private_paleogenetics_20261008/parent_core_result.json) is the current dependency receipt after the final parent requirement fix.
The worker [core_results.json](../../../testing/event016_private_paleogenetics_20261008/core_results.json) remains its 51-case delivery reading point; its older stage-decision-trigger dependency hash is historical after the parent-only preflight fix.
The current [parent_frontend_result.json](../../../testing/event016_private_paleogenetics_20261008/parent_frontend_result.json) records the final 29 cases and 51 core cases.

The frontend cases cover each direct resource below/equal/above its quote, CIC 3/4/5, already-reserved native entry, literal complete/remove/recovery callbacks, missing/lost entitlement, incomplete reset/inversion, funded-reset rejection, fault-visible-but-unavailable recovery, six CXT phases and two observer rejections.
The core delivery covers actual quote/debit/refund/receipt/restoration/dispatcher source, partial delivery in both orders, duplicate/reentry boundaries, depleted resources after payment, competing construction, identity/serial/row/payment corruption and neutral/private-history isolation.
The two external provider-identity helpers are explicit stubs.
Native pointers, aggregate stockpiles, slots, instant building increments and clock/operation effects remain modeled inputs, with Decimal arithmetic rather than native fixed-point proof.
The defaults are not mocked no-ops.

The current [core_handoff.md](../../../testing/event016_private_paleogenetics_20261008/core_handoff.md), companion API markdown and core validation/results are present and were read.
The retained core validator evidence is partial: prior whole-file command/scope checks reported valid = null with unchecked argument blocks; explicit snippets also retained unresolved scripted-helper/argument findings.
Source-model passing cases do not turn those into parameter or engine validation.
The parent-domain bundle is retained for parent review; a fulfilled tool promise alone is not an acceptance result.

## Retained MCP and reference evidence

Workspace: mod_chaos_redux_ea3b2d67c2c0.
The relevant live schemas were exposed and used.
Offline Decision modding sections read directly through MCP were lines 576-595 (state targets, FROM and map_only) and 284-311 (native/custom costs), revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
Installed dynamic_variables_documentation.md:608-611 was read for factories available to a new project, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda.
The earlier source_lookup located the exact reset decision/category at line 59, index revision d5c89d09eb0d6df4cd47d4085c6a8e2462f2a557354c956ea8dd4090bc191c85; final source bytes were checked separately by SHA-256.
Context bundles had omitted general sections; no complete wiki/documentation-surface coverage is claimed.

The corrected narrow decision_inspect request targeted mengele_event016_paleogenetics_deployment with one idle-closed-no-program scenario, GER, closed flags, date 1936.1.1 and zero declared PP/factory inputs.
It returned INTERNAL_ERROR / Unexpected internal error, no scenario result and no artifact.
The parent's earlier exact-quote inspection returned JOB_WORKER_EXIT, and its inventory ignored the requested ID and returned a global 8,320-decision report.
Those are retained failures/global discovery, not focused decision acceptance.
Earlier request-shape rejections were corrected and are not classified as service-health results.

Native countrydecisionview GUI inspection initially used a generated idle scenario and then the explicit paleogenetics-idle-closed-explicit scenario with generated scenarios disabled.
The explicit source graph inspected 14 shell elements at shared revision 64dd530dc99519ec762d32ce1924233e2f4bc082bb4deeef728078551b90d763.
GUI_RENDERED used that same explicit scenario/revision, 1920x1080 at UI scale 1, normal and empty-list states, with full/cropped/annotated/click-region/source-map variants and offlineRepresentation = true.
Actual Paleogenetics decision rows, populated tooltips and their availability states were not supplied by this evidence.
No full visual completion is claimed, and image metadata alone is not a pixel review.

Retained retrievable artifact identities:

- Generated GUI inspection JSON: SHA-256 4fbf6f5aeacc74febd36117114fd5a4cbcc134ed6f7b575017ed007e76fe13d9, 530774 bytes; URI hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fbf6f5aeacc74febd36117114fd5a4cbcc134ed6f7b575017ed007e76fe13d9/1b61e0f6386ada19c2369f5e18c469a81af7b2b64088f8b160c8efb8311f25f6/gui-inspect.64dd530dc99519ec.json.
- Explicit native-shell full PNG: SHA-256 11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33, 109428 bytes; URI hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11745615bd90cf03c811fa07d691838a4696547addb0330a9e101959d30a7e33/9191dde7413986c85668ea96f918c7b6c69145c82a330f30497e568f97974a58/countrydecisionview-full.png.
- Explicit native-shell cropped PNG: SHA-256 83c3f31f66de7cf43bc12499be8ba0c60379cc0182f543b5f9cb9d0040c5df24, 92327 bytes; URI hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83c3f31f66de7cf43bc12499be8ba0c60379cc0182f543b5f9cb9d0040c5df24/f34ba722deb7ebac16287b1d477b4d578faecde8a6d69a36fd0120979d7dab6c/countrydecisionview-cropped.png.

The exposed generic resource inventory did not provide HOI4 artifact resources for direct pixel retrieval in this session.
The native-shell route also reported shared vanilla clipping: countrydecisionview 550 to 544 pixels wide, header 543 to 542, and child-outside-clipped-parent/alignment warnings.
These diagnostics remain open; no renderer-difference excuse or unauthorized shared-GUI patch was made.
Hover/selected/disabled/warning/active/completed/full-list/long-text and actual row cost/tooltip clipping were not covered.
The late quantity wording and preflight fixes have source/test evidence only, with no populated post-change visual comparison.

## Sealed source identities

All paths below are repository relative.
These are the final reading-point hashes; mixed shared files were reviewed only at the named dispatch/cleanup boundaries.

| Source | SHA-256 |
|---|---|
| common/decisions/016_mengele_paleogenetics_stage_decisions.txt | 0ad338e3597d2f855b80282c505acda4cf6fceba5e468de8204de0fb97a41653 |
| common/decisions/016_mengele_paleogenetics_site_selection_decisions.txt | cfd888f424460669e24c0b9e78afb65c2082169e7f480ef71a16b0d0594b9d65 |
| common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt | 5863eb3de1256da1bb4efb51c236bb3653e49e9dfed3715eb88a83297b6c1ea6 |
| common/scripted_localisation/016_mengele_paleogenetics_deployment_localisation.txt | e791bbbead711e156f668102b17c4e7574db8a495de8a347dfbe5517f56c426b |
| localisation/english/016_mengele_paleogenetics_stage_l_english.yml | 0e0a699a7723f8961e711e335462f952bb81b06d731574455223c584625ca14d |
| localisation/english/016_mengele_paleogenetics_deployment_l_english.yml | 40f82355557c297c203ac56709d91b712f3a84ac84501c6917b86a7965dae157 |
| localisation/english/016_mengele_provider_program_categories_l_english.yml | 1f07c777a95279123265dea98a8b5da5bb17d7a4871b784f23e04053e89cd833 |
| common/scripted_effects/016_mengele_paleogenetics_deployment_cxt_effects.txt | e2ee36088ffd1b556523a8c680f9132ee82e707e2b5d05c7c025d7e434fc163b |
| common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt | e63d9796f7c4d60f397d28a36c36ddc62d86fa4d339ea03513a907e7591be2b8 |
| common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt | e91c16b6e6e3cbac98402f2793fbc2d50679f57dedb40cbbcce4855efd1eb429 |
| common/script_constants/016_mengele_paleogenetics_deployment_constants.txt | 89658928cf2db2cc7d602b5306f25c58c9ccd42b6882bc4a556453810fb3b0c8 |
| common/scripted_effects/016_mengele_paleogenetics_deployment_effects.md | 13af3ee3d009793a293034b1994ecccf17c302ba2affd7d2391aa3ad56300952 |
| common/scripted_effects/016_mengele_project_stage_effects.txt | 1ba88b35ca82d5a03364d2b2e19ba689fa29603af3173228f02841c74eaac4a7 |
| common/scripted_triggers/016_mengele_project_stage_triggers.txt | 6675660ef5967de9fbf1a729b9e33bcef68fe05bb0542ef1ef8a080644ebf706 |

Current evidence hashes:

- parent_core_result.json: 4c140a08aa3ccf70e1ffc590fe7568422b8e529b95afe1f99d4e4ccc9f7ed84a.
- parent_frontend_result.json: 59e42507b4c3ecef7bc330db7cc80765a0f98effff2389cf9e9b4bbab5f456d4.
- core_results.json: 74eae0e7d1378f6d405b72a640b564a5686978f6f781780b7ee9ec2625bf3669.
- core_handoff.md: 95a830356fb7636506a3c4954f9d3ce80230c8fb0b859b73c683ca376974064d.
- core_source_tests.py: 41a3a2ae6fa52cbc501d528865c09e2206b84217dfb878a1f1df19e94e9f2238.
- parent_frontend_tests.py: 06ceb5a49def26a62dc505a382850e6a58b56606deefb58f9ed52d2781e20d4a.
- core_validation.json: 9922ad5312080e4e69f5c337b3401297c6a70f47a38687ae835c2e6e74d5167a.

## Remaining parent acceptance limits

Concrete model/design/original-producer restoration cannot be reconstructed from the aggregate shared support-equipment refund.
Native fuel clipping, immediate versus delayed stockpile/building recount, interrupted effect acknowledgment, fixed-point/overflow behavior, state-pointer/partial-control semantics, unique building identity/health, reservation and 480-day callback timing, and stale same-action generation remain unproved.
A positive measured increment is not a unique factory-ownership claim.
No parameter-complete validator, populated native-row visual comparison or final AI report is asserted.

The parent should review the separate probability auditor's actual final evidence, retain these native/UI limits in the first-tranche integration record, and preserve the accepted-and-queued staffing/transport/breeding scope.
No further local gameplay fix is recommended from the inspected source after the two verified parent resolutions.
The full private payoff and Event016 remain incomplete.

Guidance used: AGENTS.md and chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-subagents and chaos-redux-scripted-gui.
No skill was created or updated.
## Owner-resolved appendix: frozen paid CIC, 2026-10-09

This appendix updates the current source identities and test total after the narrow parent fix.
The original report, its 51+29/80-case count and its hash tables above remain the earlier sealed reading point.
The current bounded record contains three owner-resolved source findings and 51 core + 31 additional frontend/native-consumer/CXT cases, for 82 modeled source cases.
The older native/visual/parameter/generation limits remain open.

### Third resolved finding: funded work compared its CIC receipt with a mutable current quote

At the original sealed trigger hash e91c16b6e6e3cbac98402f2793fbc2d50679f57dedb40cbbcce4855efd1eb429, pending authentication compared family-row9's recorded factory commitment with the current global Paleogenetics Deployment CIC constant.
A paid receipt recorded at four CIC therefore failed authentication if a later table retune changed the nominal quote to six.
The parent reproduced authentication false and unfinished paid work through the actual-source driver.
This was a paid-quote preservation defect.

The parent fixed BEGIN at common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt:79 to freeze mengele_event016_paleogenetics_paid_cic from mengele_event016_stage_quote_civilian_factories before pending publication and the default debit.
Pending authentication at common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt:78-79 now requires positive frozen paid_cic and exact equality between family-row9's recorded commitment and that frozen value.
It no longer compares existing funded work with the mutable current cost table.
The auditor verified these current assignments and predicates by read-only source inspection.

The final GetMengelePaleogeneticsConstructionStatus branch also reports unconfirmed payment when a deployment is pending but pending_is_authenticated is false, even without an explicit payment/refund fault flag.
That branch is read-only and does not authorize recovery, charge resources or alter paid proof.
Recovery availability continues to require the stricter recovery_is_ready predicate.

The two additional parent cases are “funded CIC snapshot survives later nominal quote retuning” and “mismatched frozen CIC receipt cannot authorize construction.”
The current parent_core_result.json reports 51 cases and the current parent_frontend_result.json reports 31 additional cases with core_cases_passed = 51.
Every recorded source hash in those two current receipts matched the live file at this appendix's sealing check.
This auditor read and checked the receipts; it did not independently execute the drivers.

No new weight, price, duration or factory reservation was introduced.
The production recipe remains 130 PP, 975 support equipment, 1,500 fuel, four native CIC and 480 days.
The frozen field preserves that paid quote if tuning changes later.
The shared quote/constants and literal native decision sources are unchanged from the prior reading point.

### Current identities for this narrow fix

| Source/evidence | Current SHA-256 |
|---|---|
| common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt | 465dba6695e859cb75998ef6e8aebd71dfcd70b56e887b5897188a0f09e1d187 |
| common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt | 460d7dca11f9951417827f4c805c0d0526ca7142b52fa8386c434757c80ae8fe |
| common/scripted_localisation/016_mengele_paleogenetics_deployment_localisation.txt | cf3d26942061b063244b037c57705a46b315129a8ad04389e599a74117fe98d9 |
| docs/testing/event016_private_paleogenetics_20261008/parent_core_result.json | 672c39acdc8f60eb73e09be28a7b0ffdca46c26d95e791558b6b5eea7b6f6b27 |
| docs/testing/event016_private_paleogenetics_20261008/parent_frontend_result.json | 142b93564bb2a6dc374e09921cd8fac18971c88fb78a299e877603c09bcbc996 |
| docs/testing/event016_private_paleogenetics_20261008/parent_frontend_tests.py | 7ed6103654b04f982ed5f6b34f0041f5156f6ac650b7dd1dea26f126fe08d763 |

The worker's earlier core_results.json/core_handoff.md and the previous tables are retained delivery evidence, not replacement manifests for this parent-owned patch.
The separate probability auditor is running the final comparison over the same eight scenarios; AI acceptance remains pending until its actual final report is reviewed.
No new MCP GUI render was requested or run for this appendix.
The retained INTERNAL_ERROR, synthetic/empty native-row evidence, shared clipping diagnostics and unverified engine behavior remain unchanged.
No further source defect was confirmed in this narrow fix.
Staffing, transport and breeding remain accepted and queued; no full private-payoff or Event016 completion claim is made.