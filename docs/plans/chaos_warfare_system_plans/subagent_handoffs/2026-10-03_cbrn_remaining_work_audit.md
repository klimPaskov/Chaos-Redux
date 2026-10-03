# CBRN bounded remaining-work audit

Disposition: read-only continuation audit, with confirmed neighboring cost-integration source omissions and separate evidence and design gaps.
This is not a completion claim for CBRN, Event 020, Event 026, or any model package.
Current-source update: the four ranked payment omissions below were implemented in the [immediate protection tranche](../2026-10-03_immediate_protection_sale_transactions.md) and [occupied/export tranche](../2026-10-03_occupied_export_sale_transactions.md).
The ranked sections retain their inspected historical bodies and hashes; they are superseded as a current source backlog by those reports, while their native acceptance limits remain open.
Only this handoff was written, with no gameplay edits, staging, commit, HOI4 launch, or request for logs.
The parent owns source implementation, final integration, specialist routing, and completion claims.

## Scope and authority

The user's explicit 2026-09-20 CBRN implementation request, recorded in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md`, controls conflicts in earlier package specifications.
The audit followed that amendment, the requirement ledger, completion report, and their current linked source and handoffs.
The current ledger links the Event 026 cost-surface registry as its ancillary integration boundary, so the four unadapted protection actions below are an actual source backlog for that neighboring contract.
They do not imply that completing these four actions completes the universal Event 026 registry.
No unrelated universal-cost owner was added to this audit.

The parent-owned Protective Aid factory-sale tranche and the scientist-holder and CSH-flag repairs were excluded from redundant implementation review.
The famine/migration package committed as `17a275e20` remains plan-only and must not be implemented from this audit.
Other owners' working and staged files were preserved.

The source snapshot ended with HEAD `02460b6d5c430f67b6b68175eedea46081c05f46`.
The shared worktree changed during the review, so the file hashes below identify the inspected versions more precisely than HEAD.
After this snapshot, the parent confirmed that other owners were editing the protection decisions/triggers and aid-adjacent localisation/triggers, including caller-output lifetime repairs.
The findings below must therefore be applied through fresh owner coordination and source identities rather than by overwriting the inspected file versions.

## Ranked source implementation still needed

### 1. Immediate emergency-distribution and hospital payments

The current registry explicitly classifies these protection actions as unadapted at `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:218`.
Their source confirms the omission rather than merely repeating an old handoff.

The existing reconditioning, conversion, and filter-simplification adapters cover bounded PP/support transactions and retain their ordinary native factory commitments.
They are not proof of full factory-family adaptation: conversion still commits three factories and filters two, which could quote lower sale capacity if the universal factory-family requirement applies to those purchases.
No missing-source finding is inferred for an accepted fixed-capacity exception without its approval basis being resolved.
This audit recommends disposition review of that boundary rather than silently relabeling those already adapted actions as wholly missing.

| Action | Exact current evidence | Missing integration |
| --- | --- | --- |
| `cbrn_emergency_state_mask_distribution` | `common/decisions/cbrn_protection_decisions.txt:341` calls its ordinary custom gate and ordinary state completion. `common/scripted_triggers/cbrn_protection_triggers.txt:564` requires the fixed `emergency_distribution_pp` constant. `common/scripted_effects/cbrn_protection_decision_effects.txt:145` delivers real crates and then debits that same ordinary constant at line 157. `localisation/english/cbrn_protection_l_english.yml:71` displays the ordinary PP getter. The constant is 10 at `common/script_constants/cbrn_system_constants.txt:977`. | No current-price sale PP quote, inclusive sale affordability, matching PP payment, or Event 026 transaction/achievement receipt reaches this action. |
| `cbrn_protect_hospitals_and_utilities` | `common/decisions/cbrn_protection_decisions.txt:428` calls `cbrn_state_hospital_payment_ready` and `cbrn_apply_hospital_utility_protection`. The trigger at `common/scripted_triggers/cbrn_protection_triggers.txt:773` checks the ordinary PP constant. The effect at `common/scripted_effects/cbrn_protection_decision_effects.txt:552` debits the ordinary alert-time mask/support amounts and ordinary PP at line 565. The cost row at `localisation/english/cbrn_protection_l_english.yml:87` still shows those ordinary values. | No sale-aware quotation/payment/receipt path exists for the registered qualifying components. |

Recommended next action: implement one bounded immediate-payment owner tranche, starting with emergency PP because its real-mask distribution and no-delivery guard already provide a clear completion boundary.
Preserve the exact alert, one-surge marker, actual mask consumption, target, protection, and congestion behavior.
For hospitals, keep one source of truth for the state quote, affordability, actual debits, completion gate, display, and atomic-failure disposition.
Classify physically delivered masks separately from a qualifying fee rather than fabricating crates or treating a lower shipment as the same outcome.
Keep the existing willingness formulas, with any necessary PP saving-hint change separately audited.

Required named scenarios for the probability specialist and owner checks: ordinary, sale, and Evolution I, each below/at/above the displayed PP price, sufficient/insufficient material stocks, invalid exact alert, and zero actual delivery.
The baseline is not supplied by this audit and must precede owner edits.

### 2. Occupied Population PP and native-factory integration

`cbrn_supply_occupied_population` remains one fixed two-factory definition at `common/decisions/cbrn_protection_decisions.txt:375`.
Its pre-click gate at `common/scripted_triggers/cbrn_protection_triggers.txt:609` requires the ordinary factory constant, and the shared non-factory selection predicate at line 616 requires ordinary PP.
`cbrn_begin_occupied_distribution_program` at `common/scripted_effects/cbrn_protection_decision_effects.txt:246` reserves exact model crates per eligible state and debits the fixed `occupied_distribution_pp` constant at line 274.
The current constants are 25 PP and two factories at `common/script_constants/cbrn_system_constants.txt:983`.
The row at `localisation/english/cbrn_protection_l_english.yml:79` displays the ordinary PP and factory getters.
The current registry's unadapted status is therefore consistent with source.

Recommended next action: adapt the PP fee and native factory commitment using the already implemented Protective Aid architecture as a precedent, while retaining this action's own country-wide target set and 30-day timer.
Preserve full physical five-model escrow, threatened non-core-state eligibility, receipt-limited completion, unused-model refunds, control-transfer cleanup, and the distinction between pre-click free-factory affordability and post-selection continuing validity.
Freeze the selected fee/factory mode through sale expiry and give all native variants one reenabling/active-action contract.
Do not discount a physical delivery by issuing masks that were never reserved.

Required scenarios: ordinary/sale/Evolution I selection, native commitment already applied at the selection callback, sale expiry before completion, cancellation, state-control transfer, partially used escrow, and empty national stock after lawful reservation.
This source work is distinct from the already closed occupied-selection free-factory repair.

### 3. Export fee and delayed transaction identity

`cbrn_export_protective_equipment` at `common/decisions/cbrn_protection_decisions.txt:214` still starts one fixed one-factory timer and uses the ordinary export gate.
`cbrn_can_pay_protective_equipment_export` at `common/scripted_triggers/cbrn_protection_triggers.txt:45` checks the ordinary factory and PP constants.
`cbrn_begin_protective_equipment_export` at `common/scripted_effects/cbrn_protection_decision_effects.txt:385` spends ordinary PP immediately.
`cbrn_export_masks_to_protection_partner` at line 402 sends the fixed shipment through `send_equipment` at completion and updates its aid totals.
The constants are 15 PP, one factory, and 500 crates at `common/script_constants/cbrn_system_constants.txt:985`, and the current row/hover at `localisation/english/cbrn_protection_l_english.yml:45` quotes that ordinary transaction.
There is no Event 026 receipt or frozen delayed sale-price state in this action's current call path.

Recommended next action: provide a bounded export adapter that freezes the selected fee and logical transaction identity, preserves the existing preparation duration, exact partner, export-reserve requirement, and full physical shipment, and follows the owner-approved cancellation/refund policy.
One factory may remain one whole factory at both sale tiers, but that integer-floor result still needs an explicit registered quote/disposition rather than an unadapted fixed field.
Credit a delayed purchase only from the accepted completion contract, with no synthetic proof of engine delivery.
The source `send_equipment` request does not itself establish actual delivered quantity.

Required scenarios: ordinary/sale/Evolution I fee boundaries, sale expiry during preparation, donor stock loss, partner invalidation, cancellation, and exactly-once delayed credit.
Native equipment-transfer success and actual delivered quantity remain a separate engine-evidence boundary.

## Completion status by surface

| Surface | Bounded status | Remaining category |
| --- | --- | --- |
| Policy, native raid categories/bridges, unit/HQ consolidation, project grants, protection backend, Condemnation, technology costs, and MIO identities | Current ledger records source implementation. No additional confirmed core source omission was found in this continuation beyond the four cost integrations above. This was not an exhaustive new mechanic audit. | Native lifecycle, source-aware comparisons, weighted scenarios, and consumer evidence remain open. |
| CBRN/Event 026 protection integration | Four current logical actions remain unadapted, with source evidence above. | Actual implementation work. |
| Protective Aid, dated scientist ownership, and CSH flags | Parent-reported source-complete tranches, excluded from duplicate implementation review. | Native evidence and parent integration only. |
| Event 020 category visibility and neutral unorganized-capacity candidate | The event UI worker handoff exists, proves event ownership, gives the reference/native mapping, and records five changed source files. | Required matching current-source post-inspect/render/state/resolution/hierarchy/click-region/comparison evidence did not return, so its visual/source acceptance and isolated commit remain blocked. No missing-worker claim is justified. |
| Event 020 shorter interaction/cost loop | The six-lane addendum explicitly remains an unresolved, unaccepted proposal. Its full-category census invalidates the earlier local-only six-row matrix. | Design/acceptance gap, not an accepted unimplemented route. Do not implement the partial matrix. |
| Historical scientist role/skill proposals and extra 1939 stocks/industry | Individual proposals and unsourced calibrations remain unresolved. Later accepted chronology corrections supersede earlier counts and Henderson findings. | Historical design disposition or engine recruitment evidence, not permission to add speculative grants. |
| Technology layout, facility material response, current MIO cards, and current texticons | Source-linked placement/wiring and prior artifacts exist. Three generic organization files still contain 36 total trait nodes. | Native consumer and comparison evidence, rather than missing generic families or icons. |
| Chaos Assault Battalion | Commit `802006bf51887824dc3a1084598d68e36460c068` supplies a rebuilt runtime model, eight distinct registered actions, `lance_nozzle`, spray particles, and retimed sound events. | Current audio/provenance and native-consumer acceptance remain limited. The older geometry-repair blockers must not be reopened from the stale manifest. |
| Famine/migration overhaul | Commit `17a275e20` is plan-only and excluded. | No implementation authorized by this audit. |

## Asset and documentation gaps

The old `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/manifest.json` and `2026-09-12_chaos_assault_battalion_finalize.md` still describe an unselected inherited-geometry repair.
The runtime sources and current `docs/systems/3d_model_pipeline/chaosx_chaos_assault_battalion_model.md` instead describe the later September 27 rebuild.
Reconcile their disposition and current source-of-truth link without repeating the old repair.

The current model guide points to `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/source_manifest.md`, which is absent.
The older `audio/recovery_20260912/sound_handoff.md`, source receipts, and derived manifest do retain Internet source pages, licenses, original checksums, and PCM16 candidate evidence.
However, all nine WAVs referenced by `sound/chaos_assault_battalion_sound.asset` are now mono 44.1 kHz `pcm_f32le`, 32-bit, and none matches its archived PCM16 candidate checksum.
For example, the active idle WAV has 1,103,276 bytes while its archived derived candidate has 551,670 bytes.
These are actual RIFF audio files, not Git LFS pointer mismatches.
No current source-to-final transformation/checksum crosswalk was located in the bounded model ledger and guide.
This is a current asset provenance/format acceptance gap, not a claim that the licensed candidate sources are absent or that the rebuilt model is missing.
The parent/model owner should supply the current conversion recipe, original-to-derived-to-runtime hashes, exact format/consumer evidence, and post-rebuild action synchronization crosswalk, or convert the selected preserved candidates to the verified delivery format.
One sampled installed weather WAV is PCM16, but it is not the exact unit sound consumer and does not by itself prove native rejection of these float WAVs.
The model pipeline's separate mandatory selection-audio contract also remains unresolved for this broadly available subunit: the older handoff explicitly records no verified per-subunit voice consumer, and the current sound file defines entity-state sounds rather than a selection binding.
Record that engine-routing blocker rather than treating idle entry as selection or replacing a country's ordinary infantry voices.

The report's successive raw-constant counts of 513/502/395 and earlier unbound CBRN-cost cohorts are historical tranche snapshots.
The current ledger explicitly records later binding closure, and a current scan of CBRN/chemical/biological/plague English localisation files found no `[?constant:]` interpolation.
Do not turn those historical counts into new source work.
The remaining unrelated Event 016 fallback cohort is outside the bounded CBRN source list.

The legacy six-family MIO account and four unsupported achievement proposals are already marked superseded or removed with recorded user disposition in `documentation_state.md` and the current MIO reaudit.
No duplicate MIO production, resurrection of the four achievement proposals, or generic additional 1939 grants is recommended.

## Validation performed and route limits

Performed: current decision-to-trigger-to-effect-to-cost-text tracing for all four ranked actions, comparison against the current owner registry, a current in-scope raw-constant scan, generic MIO trait-node count, commit/source verification of the later battalion rebuild, WAV probes for all nine active unit files, and comparison with the archived derived hashes.
These checks establish source omissions and conflicting asset evidence, not Clausewitz execution, UI fit, real stock settlement, or AI choice.

Direct connected `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.probability_inspect/evaluate/compare/render`, `hoi4.gui_inspect/render`, and `hoi4.reference_context/search/read/source_lookup` are absent from this agent's `ALL_TOOLS` inventory.
This is the exact MCP blocker for fresh domain evidence in this audit.
The parent owns the recovered isolated SDK MCP client v3.6.0.
No second server or shared-configuration mutation was attempted.
The existing completion report's partial event traces and failed cache comparisons were retained as limits, rather than upgraded to complete evidence.

Every changed weighted surface must receive a baseline and matching post-change comparison through `chaosx_ai_probability_auditor`, including any change to saving hints or sale-sensitive eligibility.
This completion audit performed no numerical probability analysis and supplies no probability-comparison artifact.
Named scenarios above are recommendations for the required specialist pass, not results.
Unavailable or unresolved adapters for native raid AI, timed decisions, special-project rewards, and advisor/MIO choices remain evidence blockers.

Local references read because the connected reference routes were absent:

| Source | Read span and relevant boundary | SHA-256 |
| --- | --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md` | 167–181, creation-time essential equipment collection. 297–301, shared actor/victim outcome scope. No cancellation-refund contract was inferred. | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 308–355, custom costs require explicit debit, selection versus removal timing, timer modifiers, and cancellation effects. | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md` | 2202–2205, integer `civilian_factory_use` country/war-production field. | `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AST.txt` | 14–45, timed native one-factory modifier and removal-effect precedent. | `aad50da745f5a93c5f7470e06ed990a49a5416c81810849c8a2312600e81f4f2` |

## Accepted-plan disposition

The accepted overhaul amendment and its implemented corrections retain their current ledger dispositions.
The native factory-sale tranche and scientist fixes retain the parent's source-complete, native-evidence-pending disposition.
Event 020's accepted category/capacity repair is implemented as a source candidate but blocked on mandatory post-change visual evidence.
Its six-lane addendum remains `unresolved`, with no accepted promotion inferred from its path, status label, or old source inventory.
The old battalion repair should be recorded as `superseded` by the September 27 rebuild while preserving the current audio and consumer limitations.
Famine/migration remains plan-only, and individual unsourced historical proposals remain unresolved.
No new design, fallback, source simplification, or completion promotion was made by this audit.

## Inspected source identities

| Path | SHA-256 |
| --- | --- |
| `common/decisions/cbrn_protection_decisions.txt` | `1cea14ecf1bd15929d90a15fca5c115c529d5edc3af936eb888fa2eac9d91d03` |
| `common/scripted_effects/cbrn_protection_decision_effects.txt` | `eacb3a35edbf6aeb4d095dbcb14c4030e9b5a6bf554c4d8822903a2bdf273818` |
| `common/scripted_triggers/cbrn_protection_triggers.txt` | `a681319bf4f59c64cb270e3b9b89f07de07d8c2f6f971ae5edc893521c17f698` |
| `localisation/english/cbrn_protection_l_english.yml` | `0f5f7cae5fcb49dd8bf48dd6bf531db66d906116649487fdcf8e341d3497529c` |
| `2026-09-20_cbrn_overhaul_requirement_ledger.md` | `52e69b545d85fdddb0de86adb4dac0551fd647bc74449f51c085bbeab0218a91` |
| `2026-09-25_cbrn_overhaul_completion_report.md` | `42c60bce86c485c4a69f059fa24ff8750bf7d66d27ec656c183325ee71bc246c` |
| `specs/13_2026_09_20_accepted_cbrn_overhaul.md` | `41af9890acc8220c381a7d54b3d9c91fc0b99f0e566b137466573138e479d086` |
| `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md` | `35fe46166fd56f5d3e44eff7d9df2d9287cc39efb1e681ddc948a1efdca45f3f` |

Skills applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-3d-model-pipeline`, `chaos-redux-native-raids`, `chaos-redux-decisions-missions`, and `chaos-redux-scripted-gui`.
No skill was edited.
