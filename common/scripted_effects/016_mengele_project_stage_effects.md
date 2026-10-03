# Event 016 Mengele project-stage provider API

This helper family is a private country-scope receipt and settlement layer for the fifteen existing Event 016 project families: Computation, Electronics, Materials, Rocketry, High Energy, Biomedical, Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Biological Weapons, Alien Arms, Temporal, and Strategic Singularity.

## Contract

The temporary selectors are `mengele_event016_project_family` and `mengele_event016_requested_stage`.
Family IDs are one-based and receipt array indexes are family ID minus one.
`brilliant_scientist_mengele_initialize_project_stage_receipts` extends each receipt array independently to the shared family count by appending zeros, preserving existing values and never truncating longer arrays.
The size-based migration expands the earlier initialized one-slot Computation schema and becomes a no-op at fifteen slots.
When the private component-entry initialization marker is absent, it reconstructs the component array from surviving private flags and derives the count without erasing the flags.

The completion flags are `mengele_event016_<family>_theory_completed`, `mengele_event016_<family>_prototype_completed`, `mengele_event016_<family>_deployment_completed`, and `mengele_event016_<family>_weaponization_completed`. Singularity also keeps six provider-owned component flags and a component count for idempotent native component callbacks.

`brilliant_scientist_mengele_begin_project_stage` validates the strict active-program-owner predicate, request, predecessor, quote, payment, and empty receipt before debiting political power, support equipment, and fuel.
Civilian-factory/CIC quotes are stored in the receipt but never reserved or refunded by this API; the native parent decision owns that quote.

`brilliant_scientist_mengele_cancel_project_stage` and `brilliant_scientist_mengele_finish_project_stage` authenticate the exact family/stage receipt, snapshot direct costs, clear the slot, and refund once when no output is accepted. Repeated callbacks see an empty slot and are no-ops.

### Temporary output storage

Every consuming helper frame owns its nested temporary outputs before making the nested call.
The initializers remain in the consuming frame because creating a new temporary first inside another initializer helper would lose the storage under conservative helper-return lifetime.
The input selectors `mengele_event016_project_family` and `mengele_event016_requested_stage` retain their incoming values until the existing end-of-transaction selector cleanup.
No caller should infer a paid result from a temporary that it did not initialize before invoking this API.

| Helper | Scope and inputs | Owned nested storage and defaults | Outputs and side effects |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_begin_project_stage` | COUNTRY, required literal family and requested stage | Index and all eight quote outputs start at zero in this frame | Existing `mengele_event016_stage_started` result, current-table direct debit, exact family receipt, existing selector cleanup |
| `brilliant_scientist_mengele_cancel_project_stage` | COUNTRY, required exact family and active stage | Index starts at zero, stored PP/support/fuel snapshots are assigned directly in this frame | Existing `mengele_event016_stage_cancelled` result, clear matching receipt before one stored-price refund, existing selector cleanup |
| `brilliant_scientist_mengele_finish_project_stage` | COUNTRY, required exact family and active stage | Index, output-applied fields, output gap, availability result, and both dispatchers' exported incident results start at zero | Existing finished/output results, clear receipt before output or stored-price refund, incident calls only after accepted output, after-Theory adoption with outer frame restored |
| `brilliant_scientist_mengele_apply_family_stage_output` | COUNTRY, existing family/stage and authorized-output input | Stage-package-applied starts at zero before either package helper | Existing private flags and package results, existing modifier refresh and availability reconciliation |
| `brilliant_scientist_mengele_grant_conventional_stage_package` | COUNTRY, existing family/stage | Conventional grant-applied starts at zero | Existing stage-package result, established neutral package grants and selector cleanup |
| `brilliant_scientist_mengele_grant_custom_stage_package` | COUNTRY, existing family/stage | Custom grant-applied and upgrade-applied start at zero | Existing stage-package result, established neutral grants/refinements and selector cleanup |
| `brilliant_scientist_mengele_adopt_completed_native_after_theory` | COUNTRY, accepted Theory output and enclosing output context | Aggregate native-prototype-synced starts at zero | Existing adoption and exact outer family/stage/index/output/gap/authorization/availability/component restoration |
| `brilliant_scientist_mengele_sync_native_project_prototypes` | COUNTRY, existing aggregate native request | Project-output-applied starts at zero | Existing synced result and authenticated Prototype output |
| `brilliant_scientist_mengele_record_native_project_prototype` | COUNTRY, existing private selector or existing host selector adapter | Synced and component-recorded start at zero | Existing native-prototype-recorded result, existing exact-family exclusions |
| `brilliant_scientist_mengele_cleanup_provider_receipts` | COUNTRY, original provider owner, no selector input | Index starts at zero before the bounded fifteen-family loop | Existing cleanup result, cancel/refund each surviving active receipt once, preserve durable flags and neutral entitlements |

The quote outputs are `mengele_event016_stage_quote_loaded`, `mengele_event016_stage_quote_duration_days`, `mengele_event016_stage_duration_loaded`, `mengele_event016_stage_quote_source_gap`, and the quote costs `mengele_event016_stage_quote_civilian_factories`, `mengele_event016_stage_quote_political_power`, `mengele_event016_stage_quote_support_equipment`, and `mengele_event016_stage_quote_fuel`.
An outer caller that consumes any of them after a quote or begin call initializes each consumed output to `constant:brilliant_scientist_value.zero` first.
An outer caller consuming `mengele_event016_stage_finished` or `mengele_event016_project_output_applied` after finish initializes those fields to zero in its own frame.
The seven existing custom Prototype decision callbacks own both result fields before finish and assign their literal operational-grant family after the finish helper clears the stage selectors.
`mengele_event016_stage_started` and `mengele_event016_stage_cancelled` have no external consumers in the current parent inventory, but callers added later must initialize them to zero when consuming them.
The same outer-storage rule applies to forwarded `mengele_event016_computation_incident_dispatched`, `mengele_event016_computation_incident_recorded`, `mengele_event016_conventional_incident_recorded`, aggregate sync/component results, and provider-cleanup results.

```txt
# COUNTRY completion callback, with result storage in the consuming frame.
set_temp_variable = { mengele_event016_project_family = constant:brilliant_scientist_project_family.cloning }
set_temp_variable = { mengele_event016_requested_stage = constant:brilliant_scientist_project_stage.prototype }
set_temp_variable = { mengele_event016_stage_finished = constant:brilliant_scientist_value.zero }
set_temp_variable = { mengele_event016_project_output_applied = constant:brilliant_scientist_value.zero }
brilliant_scientist_mengele_finish_project_stage = yes
# The existing callback consumes both results and the durable private flag.
```

Cancel and finish extend each surviving partial array independently only after the exact active family/stage receipt matches.
Missing cost entries append zero, so absent historical costs produce no fabricated refund.
Surviving stored prices and rows beyond the family count remain intact.
No factory creation effect, timer change, new tuning constant, event target, or periodic hook is introduced.
The executable cold-frame/economy driver, immutable pre-paid-fix baseline, source hashes, native regression results, MCP references, and outside-file incident lifetime follow-ups are retained in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_funded_provider_cold_lifetime_2026-10-03.md`.

## Quote provenance

The loader reads every duration from `brilliant_scientist_project_duration`, Theory/Deployment/Weaponization cost rows from `brilliant_scientist_project_stage_cost`, and all fifteen Prototype cost rows from `brilliant_scientist_project_fallback_prototype` in `016_brilliant_scientist_project_constants.txt`.
The direct affordability trigger uses the same shared Prototype keys and accepts exactly the quoted amounts.
Each valid quote sets `mengele_event016_stage_quote_loaded` and leaves `mengele_event016_stage_quote_source_gap` at zero.
Invalid family or stage selectors retain zero quote values and cannot begin.

The Cloning, Paleogenetics, Xenobiological Synthesis, Alien Arms, and Temporal cost rows define the native base, blocked, and hover variants for all four stages.
Blocked rows retain the same dynamic amounts and icons while colouring the displayed amounts red when the combined affordability gate fails.
The cost-row hover lists every dynamic direct payment and factory assignment, while the ordinary cost detail explains reservation and payment timing without duplicating the inline amounts.
These presentation strings do not change the shared quotes, payment, refund, or receipt logic.

Computation remains 2 civilian factories, 68 Political Power, 200 Support Equipment, and 100 fuel.
Its decision AI planning hint, four affordability comparisons, and four cost-localisation tokens read the shared keys directly, so the four private quote mirrors are removed.
The existing native decision modifier retains its file-scoped factory value because that field rejects shared tokens.
The DLC-aware decision/native presentation gate is unchanged, and native project callbacks do not invoke this payment path.
Shared resource reserve fields are requirements owned by the parent adapter, not extra direct-payment receipts.

## Component integrity helper

`brilliant_scientist_mengele_singularity_components_are_complete` is a read-only country-scope trigger with no parameters, defaults, writes, or event targets.
Its input is the private component array, its derived count, and six private completion flags, and its output is true only when both lengths equal the shared six-component total and all command-core, power-link, containment-lattice, temporal-authenticator, delivery-architecture, and fail-deadly-governor flags exist.
The Singularity Prototype predecessor branch and authenticated native completion branch both call it.
Five flags fail both gates even when the count says six, and a wrong count fails even when all six flags exist.

The initializer runs in country scope with no arguments.
Its outputs are receipt arrays of at least the shared family count, the receipt initialization flag, and, only if its marker is missing, the component initialization marker and a count reconstructed from existing flags.
It never charges, refunds, starts, settles, or cancels work and never creates a completed component.
Begin and native component callbacks retain their initializer calls, and provider cleanup calls it before scanning initialized receipts.
No new event-target lifecycle or scheduler is introduced.

```txt
# Country scope, including the earlier initialized Computation-only schema.
brilliant_scientist_mengele_initialize_project_stage_receipts = yes
```

## Output dispatch

`brilliant_scientist_mengele_apply_family_stage_output` records Theory and Prototype provider flags for every family. Native Prototype branches additionally clear their existing presentation availability flags. Conventional Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical Deployment use `chaosx_grant_conventional_technology_package`; Weaponization calls the deployment package first and then the weaponization package. The fixed source is `constant:mengele_event016_project_stage.provenance_mengele`.

Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Alien Arms, and Temporal Deployment use `chaosx_grant_custom_operational_technology`. Their Weaponization branches establish the operational package first and then call `chaosx_grant_custom_technology_upgrade`, with the existing custom selector and upgrade constants. Selectors are reset after each call.

Biological Weapons uses the native biological-operations route for its late output.
Singularity Deployment and Weaponization set only private stage flags and their existing stage modifiers after a valid paid receipt.
They do not establish physical construction, arm the device, alter Chaos, or submit a Fallout request; those later actions require independent live-site and terminal guards.

## Native adapters

`brilliant_scientist_mengele_adopt_completed_native_after_theory` is an internal country-scope settlement helper.
It runs after a successful paid Theory output, the refund decision, and the Theory incident dispatch, before the outer callback clears its selectors.
Successful paid outputs for Electronics, Materials, Rocketry, High Energy, and Biomedical also dispatch their private family incident before this adoption boundary.
The dispatcher rejects unsupported families and already-active family incidents; cancelled, rejected, duplicated, or merely reconciled outputs cannot reach a fresh stage roll through settlement.
Its inputs are the current private family/stage selectors and successful output result; the generic native authentication trigger must also confirm the strict owner, matching Theory receipt, and actual completed project.
It invokes the existing Prototype synchronization without paying again or replaying native completion.
After successful synchronization, the shared private native-package helper grants the same operational entitlement as the original native bridge for Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Alien Arms, and Temporal Mechanics.
That helper uses the saved family and the neutral technology API with Mengele provenance; conventional families receive no extra operational reward at Prototype.
The adoption helper then restores the outer family, stage, index, output results, gap result, authorization, and availability result.
The native synchronization result remains available as `mengele_event016_native_prototype_synced`; all normal finish results still describe the paid Theory callback.
This covers the fourteen ordinary families when native research precedes Theory.
For Singularity, the same post-settlement boundary walks the six component IDs through the existing exact native-component authentication helper, restoring the private family before each callback and the caller's component selector afterward.
Only actually completed native components acquire private receipts, and Prototype is recorded only when all six component receipts exist.
No component is completed by the adoption loop, and it cannot pay for, construct, arm, or detonate the device or change Chaos.
An absent native completion, failed Theory output, invalid owner, or duplicate finished receipt cannot create a Prototype through this hook.
The helper is not called by stage-output or availability reconciliation, so nested Prototype output cannot recursively adopt another stage.
Callers continue using `brilliant_scientist_mengele_finish_project_stage = yes`; they must not invoke the internal adoption helper as an independent grant API.

## Exact native later-stage receipts

The exact native later-stage output wrappers settle only Electronics Deployment, Electronics Weaponization, Rocketry Deployment and Weaponization, and High Energy Deployment and Weaponization.
Project outputs call their ID-specific wrapper from the existing `country_effects` block; the `radio_detection`, `centimetric_radar`, and `phased_array` technology definitions call their matching hidden `on_research_complete` wrapper.
Electronics Deployment requires both the `sp_air_radar` output marker and `radio_detection`; the marker flag is set only for a valid Mengele provider and is removed by provider cleanup.

`brilliant_scientist_mengele_settle_exact_native_later_stage` requires the strict provider gate, a valid family/stage/source tuple, the exact private predecessor, and an empty matching active receipt.
It calls `brilliant_scientist_mengele_apply_family_stage_output` once, records the exact native source in the aligned `mengele_event016_native_later_stage_deployment_source_entries` or `mengele_event016_native_later_stage_weaponization_source_entries` array, and never starts, cancels, refunds, or converts a paid receipt.
The source arrays are append-only initialized to the fifteen-family count and are cleared with provider receipts.
If the matching paid receipt is active, native settlement fails closed and leaves that existing receipt to its current decision lifecycle, as the user explicitly directed on 2026-09-26.
This hook adds no retry scheduler or timer policy.

The native source table rejects cross-family and cross-stage tuples.
Rocketry records which of its two exact alternatives settled each stage, while repeated or opposite-alternative completions cannot replace a completed provider receipt.
High Energy records the exact reactor, nuclear-bomb, thermonuclear-bomb, or warhead project that settled its corresponding stage.

The mod-side project and technology files mirror nine existing installed vanilla project definitions and three existing vanilla technology definitions because partial same-ID merging is not established by the inspected documentation or reference mods.
The mirrors preserve their current vanilla definitions and add only hidden Event 016 completion calls; review them against the installed vanilla sources after game updates.
No project or technology IDs are added.

`brilliant_scientist_mengele_reconcile_reused_native_project_prototypes` is a country-scope, no-argument completion adapter for Electronics, Rocketry, High Energy, and Biological Weapons.
The separate strict-Mengele branch of `on_project_completion` calls it; the existing Kruger synchronization and historical capture remain host-only.
It uses four private family selectors and the existing authentic recording API, which requires matching Theory and native completion and rejects an already-recorded Prototype.
Each recording call clears its selectors; no event target, cost, Capacity access, native output replay, or Kruger history is introduced.
It reconciles all four eligible families on one completion notification without a periodic scheduler or whole-world scan.
Source inventory and scenario evidence are in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_native_callback_audit_2026-09-06.md` and the matching implementation handoff.

`brilliant_scientist_mengele_sync_native_project_prototypes` accepts only `brilliant_scientist_mengele_project_native_output_is_authentic`, which requires the strict live owner, the matching Theory receipt, and the exact existing special-project completion.
Rocketry accepts either Flying Bomb or Air Jet Engine completion, matching its native alternative-project gate; it does not require both.
Biological Weapons authenticates its existing native-project alternatives.

`brilliant_scientist_mengele_record_native_project_prototype` accepts a private family selector or copies the existing native family selector, then routes all ordinary families through the generic adapter.
`brilliant_scientist_mengele_record_singularity_component` authenticates the exact component selector and native special project, appends that component to the private array only when absent, derives the count from the array, sets its provider completion flag, and records the Singularity Prototype only after all six components are present.
Its result marker stays false for an already recorded component; a duplicate callback cannot create another receipt.
Initialization reconstructs the array once from durable provider component flags when migrating an earlier provider receipt schema.
It does not call the Kruger component registry or create Kruger history.

The bridge effect `brilliant_scientist_record_mengele_project_prototype` invokes the native adapter for Electronics, Rocketry, High Energy, Cloning, Biological Weapons, and all previously supported families. Custom native families then receive the existing custom operational API. `brilliant_scientist_record_mengele_singularity_component` is available for the parent Strategic Singularity output branch.

## Cleanup and parent boundary

`brilliant_scientist_mengele_restore_deployment_project_modifiers` restores the existing seven custom-family Deployment modifiers only for the strict private owner with the matching durable paid Deployment receipt.
It runs through the existing availability reconciliation boundary after successful stage output and existing lifecycle reconciliation calls.
It neither grants neutral technology nor creates a Deployment receipt, and native Prototype history alone cannot satisfy it.
The modifier's own enable/removal conditions accept the current Kruger host or the strict private owner with that exact private receipt, preserving the existing host behavior and removing private benefits on provider loss.
This provides the existing operational-modifier payoff in addition to the idempotent technology grant.
It does not implement the remaining physical-site, production, control, or strategic-action counterparts; those remain under parent design review and require separate integration before Deployment is complete.

`brilliant_scientist_mengele_restore_early_project_modifiers` is a no-argument country-scope restoration helper called by the existing `brilliant_scientist_mengele_reconcile_project_availability` entry point.
It requires the strict valid private owner, checks each exact durable Theory/Prototype completion flag, and adds only its missing matching existing modifier ID before one modifier refresh.
It never calls stage-output, payment, native-project completion, neutral grant, or history helpers and does not write selectors, receipt arrays, slots, equipment, or Directorate state.
Present modifiers are not re-added, and conventional learned packages converge on the same IDs without duplication.
Private Theory is not inferred from Prototype, and no private history is inferred from a neutral operational flag or a broader Directorate completion flag.
Restoration occurs when the existing country reconciliation is invoked, including successful-stage-output and CXT call sites, the strictly guarded tail of `germany_mengele_mark_victory`, and the strictly guarded `MCL_directorate_project_registry` completion reward after its existing availability grant.
The victory tail runs after master-claim handling and cleanup, so an overthrow cannot restore private modifiers; the focus establishes the registry flag before reconciliation.
No periodic hook or automatic validity-change detector is added.
The availability helper retains its Computation behavior and also publishes Electronics, Materials, Rocketry, High Energy, and Biomedical native Prototype paths for the strict live private owner after matching Theory.
Each path is cleared when its private Prototype, shared completion receipt, or matching native project is complete; Rocketry treats Flying Bomb and Air Jet Engine as alternatives.
The five conventional paths are not touched by this reconciliation for a non-private owner; provider cleanup retains responsibility for their removal on program loss.
Availability publication never invokes stage output or creates project history, payments, or technology rewards.
This resolves the missing receipt-to-modifier restoration path recorded by the early-modifier gate audit, with current evidence in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_early_modifier_restoration_2026-09-06.md`.
The gameplay invocation boundary is documented in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_lifecycle_reconciliation_2026-09-06.md`.

`brilliant_scientist_mengele_cleanup_provider_receipts` extends an initialized receipt schema before walking the fifteen family slots, cancels active receipts, clears presentation availability flags, and preserves durable completion flags and neutral entitlements.
It retains the existing Computation incident cleanup hook and invokes aggregate cleanup for the five conventional private incidents before the stage-receipt loop.
Each family refunds only its exact stored recovery receipt before removing its native recovery decision, clears transient penalties and payment state, and preserves permanent history and learned technology.
The existing provider-loss, defeat, transfer, and terminal callers of the provider cleanup helper therefore include these recoveries without another scheduler or world scan.
Cleanup also removes the exact native later-stage source arrays and the Electronics radar-pair marker while preserving learned neutral packages and completed native projects.

The parent still owns native project visibility, pending Prototype receipts, Strategic Singularity stage and terminal decisions, provider Fallout integration, localisation, and the remaining event/special-project definitions.
This tranche does not claim full Event 016 portfolio completion.

## Validation evidence

Current quote and migration evidence is recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_quote_integration_2026-09-06.md`.
Source-model tests cover all fifteen quotes, inclusive affordability, settlement, concurrent receipts, migration, and component integrity.
Current full `state_flow` and narrow `trace` MCP inspections for `chaosx.nr16.901` both timed out after 180 seconds, so current engine lifecycle, render, and comparison evidence remain blocked.
Earlier focused traces are historical evidence only.
The exact native output source copies were compared against the installed vanilla definitions, and their only semantic additions are the hidden marker calls.
Post-change `hoi4.tech_inspect` traces for `radio_detection`, `centimetric_radar`, and `phased_array` each timed out after 180 seconds; a narrower refreshed explain query for `centimetric_radar` timed out after 180 seconds as well.
The focused `centimetric_radar` `hoi4.tech_render` attempt then returned `Transport closed`, so no post-change technology render or compare was produced.
The MCP package exposes no special-project-specific route.
The exact output hooks therefore have source evidence but no current MCP graph evidence or live-game acceptance.

No new icons, localisation, GUI, event, focus, model, or asset files are required by this helper layer.

## Remaining integration

The parent still owns non-Computation decision presentation, reserve requirements, factory commitments, and literal stage callbacks.
Singularity's paid component presentation must establish authentic private component receipts before Prototype entry, and its native six-component completion already delivers Prototype without another payment.
Singularity's paid late-stage flags and modifiers are implemented; playable decisions, physical build proof, and the terminal/Fallout route remain open.
Longer-than-current receipt arrays are preserved without truncation, but the current cleanup contract visits only the fifteen defined families.
The migration cannot reconstruct missing historical payment values and does not fabricate them from current quotes.

The approved exact output hooks live in same-relative-path vanilla file replacements for air_projects.txt, radar_projects.txt, rocket_projects.txt, nuclear_projects.txt, and electronic_mechanical_engineering.txt.
These replace the standalone duplicate-ID files after the 2026-10-03 live QA found duplicated project output entries.
The full-file source comparison and effective-ID inventory are recorded in 016_native_marker_file_replacement_review_2026-10-03.json.

## Electronics completion ordering

After the literal brilliant_scientist_mengele_native_output_electronics_radar wrapper or exact adoption adapter applies a private Electronics Prototype and stores its durable provenance, it calls the existing exact radar-pair settlement helper once.
The sp_air_radar output marker and radio_detection completion may both arrive before the native Prototype callback, so this handoff supplies the remaining attempt after the predecessor exists.
The helper still requires the exact output-seen flag and radio_detection, then authenticates the live provider, private predecessor, and empty matching paid receipt.
It retains the dedicated native Prototype result marker, introduces no payment or timer, and clears its temporary family/stage selectors through the existing cleanup.
Other families do not enter the radar-pair helper from this handoff.
The initial ordering review is 016_radar_prototype_ordering_review_2026-10-03.md; the current ownership boundary is reviewed in 016_native_electronics_core_2026-10-03.md and 016_native_electronics_integration_2026-10-03.md.
Electronics is excluded from the generic completion synchronizer and unrelated-completion scan.
The exact later-stage settlement core initializes its own index, output-applied and stage-package output storage before nested mapping/output calls, without resetting the caller's family, requested stage or literal source.
This permits the radar marker and named technology completion callback to record the correct Electronics provenance slot even when they enter with no inherited temporary fields.
The caller must initialize mengele_event016_native_later_stage_settled before calling if it consumes that temporary result after return.
Live callback ordering remains part of Event 016 acceptance.
