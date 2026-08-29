# Event 014/015 famine and migration adapter-owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25.

Owner: bounded Event 014 Cannibalism and Event 015 Utopia Manifesto adapter review.

## Verdict

No gameplay adapter was patched. Both event roots remain API-only because the current owner code does not expose the exact live facts required by the public famine or migration contracts. This is an intentional fail-closed result, not a replacement adapter or a new event/pacing surface.

No famine or migration event ID, random event, cluster queue, daily/weekly pulse, shared central file, localisation file, asset, achievement, workbook, or central source was changed.

## Files and identifiers reviewed

The bounded owner surface was reviewed in `events/014_cannibalism.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/on_actions/014_cannibalism_on_actions.txt`, `events/015_utopia_manifesto.txt`, `common/scripted_effects/015_utopia_manifesto_effects.txt`, `common/scripted_triggers/015_utopia_manifesto_triggers.txt`, and `common/on_actions/015_utopia_manifesto_on_actions.txt`.

The current source has no direct `famine_migration_*` callsite in either owner family. Event 014 effect and trigger files have concurrent edits from another agent; those edits were preserved and not mixed with this review.

## Event 014 exact facts and seam disposition

`cannibalism_consume_current_state` proves a valid target state, an active Event 014 actor, a positive requested and applied people amount, a consumption context, and the `cannibalism_consumption` Deaths reason. That transaction remains Event 014-owned and logged. It must not be forwarded to famine as ordinary hunger mortality, and no second famine debit is allowed.

`cannibalism_execute_selected_prisoner_feeding` reaches the same exact consumption path with a prisoner-feeding context and Event 014 logging. The mixed prisoner-feeding ledger remains Event 014 evidence; movement or famine mortality cannot be inferred from it.

`cannibalism_apply_external_pressure_to_current_actor` consumes only country-level external-hunger flags and increments Event 014 field hunger. The source does not prove a state-local food amount in people, a famine actor-proof bundle, or a deduplication receipt, so it cannot call `famine_migration_request_famine_pressure` or `famine_migration_apply_pressure_request`.

`cannibalism_execute_island_host_blockade` proves an Event 014 counterwar actor, an island-host target, a convoy/naval cost, and a timed Event 014 blockade flag. It does not prove the shared blockade contract's owner/controller war state, island or maritime dependence, route or port disruption, convoy or escort shortage, absent humanitarian corridor, and insufficient local food together. It also has no people-denominated food amount, so it cannot call the shared blockade-pressure wrapper.

`cannibalism_rescue_island_host_survivors` proves rescue flags and stability effects but no exact survivor cohort or relief amount. It cannot call a shared reception, relief, trapped-population, or movement helper.

The Event 014 spread queue proves source and target country/state identities, a route label such as prisoner transfer, convoy, or volunteer return, generation, due date, and status. It does not prove a civilian people amount or a migration cohort. The queue is an Event 014 spread mechanic, not central state-to-state movement, so no movement or reception call was added.

The accepted Event 014 seam therefore remains: Hunger Lines may later provide separate, owner-authored famine pressure, displacement, trapped-population, relief, or border receipts, but each receipt must supply the relevant exact state, actor, positive people amount or cohort, route, and proof before calling the corresponding public API. Cannibalism deaths remain Event 014; ordinary hunger deaths remain the shared famine owner.

## Event 015 exact facts and seam disposition

`utopia_manifesto_apply_purchase_settlement` and `utopia_manifesto_apply_lease_settlement` prove Event 015 founder/counterparty actors, active case states, territorial targets, and owner/controller transitions. These are territorial political settlements, not civilian population transfers, and expose no stores debit, refugee cohort, reception amount, or route transaction.

`utopia_manifesto_restore_active_case_state_to_target`, `utopia_manifesto_return_stewardship`, and `utopia_manifesto_integrate_stewardship` prove return targets, state ownership/controller changes, route policy, and integration stage facts. They do not prove a positive displaced cohort amount or a central transfer receipt, so no return, integration, resettlement, reception, or exact transfer helper was called.

`utopia_manifesto_relieve_active_case_deficit`, `utopia_manifesto_relieve_stored_case_family`, `utopia_manifesto_record_stewardship_provision`, and league reserve contribution paths use policy scores, reserve scores, case deficit inputs, and provision inputs. These are Event 015 policy units, not people-denominated food or relief amounts. They cannot be converted into famine pressure or reception deltas without an owner-provided people receipt.

`utopia_manifesto_state_is_suitable_for_refugee_municipality` proves population, infrastructure, and free-slot suitability only. Suitability is not proof that a refugee cohort arrived, was received, or was integrated, so it cannot call migration APIs.

Event 015 island, sanctuary, refuge-district, redistribution, and inspection flags likewise do not satisfy the shared blockade proof contract or expose exact food/cohort transactions. Island blockade is not asserted through the shared system.

The accepted Event 015 seam therefore remains: common stores/rationing, blockade/shortage, refugee districts, sanctuary, redistribution, relief, return, and integration may connect only when Event 015 supplies separate famine-owned and migration-owned receipts. No generic combined pressure request was introduced.

## Public API and ownership proof

The shared `famine_migration_request_famine_pressure` and `famine_migration_request_blockade_pressure` wrappers require a valid state, a positive people amount, a known source, proven actor, and the applicable proof contract. The shared flight/displacement wrapper requires the same exact owner facts for migration pressure. Trapped-population registration, reception delta, return, integration, and exact transfer require positive people/cohort amounts and route or safety proof. The owner files do not currently expose those inputs for either event family.

Exact state-to-state movement remains exclusively on the central transaction path. No direct population mutation, proxy state, fixed total, duplicate reception, or event-local cohort ledger was added.

Deaths ownership is preserved: Event 014's exact cannibalism consumption stays Event 014-owned and logged; ordinary starvation remains famine-owned; movement is not death; no Deaths reason or famine amount is double-debited. Event 015 currently owns political territorial transitions and has no exact civilian death transaction to adapt.

## Helper, constants, target, and migration plans

No new helper is proposed because no truthful callsite exists. Existing public APIs remain the only future callsites.

No constants or tuning values were added. Event 015 policy scores were not mirrored as people, and Event 014 flags were not promoted into synthetic famine or migration amounts.

No event target or global target was created. Existing owner event targets remain scoped to their event chains; no shared target lifecycle or cleanup obligation was introduced.

Future owner migration should add a narrow receipt at the exact transaction point, prove state/actor/amount/cohort/route, call one public famine or migration wrapper, and retain the event-specific ledger only for premise/political context. If one action has both food and movement consequences, separate proven facts must select separate famine and migration branches.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Pre-review narrow `hoi4.event_inspect` for both `chaosx.nr14.1` and `chaosx.nr15.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `59143acd4a234aef98ca0b6cfbb7b07211d4aa80f99536718b30e126b1deb6f9`, graph hash `05a83fd72cbf3aa808f3f48e2ce14384b2da160472498d76344f3d950a7b0ed6`, no blocking diagnostics, and the inline-file truncation diagnostic `MCP_INLINE_FILES_TRUNCATED` for 355 total and 64 returned paths. The earlier Event 014 state-flow artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/850bd94abb81e7ec2f657f2e3379af208d366cbabda283165625fe7aa6e7281a/6f2de55bd5789da1d6132d0f1f33d112b4214c906396dc0c7d0f2ec633b497c6/event-state_flow-59143acd4a23.json`; the earlier Event 015 artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0651dc9081d3ad65734d734d20ea9bada34b71ef36b557d6ff2d95b50d9fcc5/7b8575d47ef274e60adbc5d0387252a005fc2fc021fbef97369ed49f7668b7a7/event-state_flow-59143acd4a23.json`.

Post-review narrow `hoi4.event_inspect` repeated successfully with `EVENT_INSPECTED_PARTIAL`, the same revision and graph hash, no blockers, and the same inline-file truncation diagnostic. The current post-review artifacts were Event 014 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ada0df7867e17710eccbe0ea1fa78fb5ed8da4f7aa650d113fea2d7d92a7399a/ed9c10b3404fd4daa8356ff4b243604108efdf5ad9751bf44a207fec3eab6469/event-state_flow-59143acd4a23.json` and Event 015 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/069886cf70562ade9df45fd9b0d975d38d879b12663ce3ea1e68fb5710f4a377/3d315b8e74e937a08c899756243435946c16caa75d326a74a154cf905220baa1/event-state_flow-59143acd4a23.json`.

Post-review bounded `hoi4.event_render` for both roots returned `EVENT_RENDERED_PARTIAL`, status `ok`, no blockers, and the same inline-file truncation diagnostic. Event 014 render artifacts were manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7256c30fdc55d04365a5c3ce01061e0ba5e7f4cc79a78d2ee498e1e7d06d5a7f/1e053078b08d78127f8a6594d9c35dac415077ca3d09d23213360acc66e923ad/event-state-59143acd4a23-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd827f0a92b2456904dacfccacf5b9b0e7c0fd4a31ab5f63c2464ad321b01ebd/caf9155c2bf867ed17d3408fdfb100ba11cdb8a6c2579fdc22c1041af1c5a387/event-state-59143acd4a23.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13273cd59248d6e1c22b6efa3c8e2dfad56e1f4005daaf7dd35d4bb079cd7948/137425ce3e7bc1bb1299bbbe13ff66d5ddb02bfb221ccfe6a4345d3117a800de/event-state-59143acd4a23.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/493d5a135db1d2b967ae89708f595fae672dc93108917dccdea9c805c9079c05/0a380d5797ed4016d7a6a0ab61c945bcaa7f3a5aaf3ee04474e847d96216dfef/event-state-59143acd4a23.png`. Event 015 render artifacts were manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a3fd3ef73b8f5e8b6efb19adf9eb198cf644c64e66a7495c8f4cbfa6829acac/bf8a1a43897382e915ec1a3aee7f7080dd809ff4a306e5fb3744928be8be277c/event-state-59143acd4a23-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1cd3f8054df33b8583b2ebe99e331a56c7bb9a5b962a146f17a74628625b6d36/6ce4c1f6e6d0483064705965f45fedb177d15c652d1a2a597485c17cd84cc545/event-state-59143acd4a23.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13273cd59248d6e1c22b6efa3c8e2dfad56e1f4005daaf7dd35d4bb079cd7948/76c11c05a44de2e834ee01e0203eab31ef0763b2b5bf4856548edeff06656f0b/event-state-59143acd4a23.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/493d5a135db1d2b967ae89708f595fae672dc93108917dccdea9c805c9079c05/ccba2f80b0a8762ed38687980d84f75c4dbfdd9fefcc2abdd6be4e96ba3efe5d/event-state-59143acd4a23.png`.

An initial Event 014 render attempt timed out after 180 seconds. The bounded post-review retry completed; both post renders remain partial because selected nodes were zero and workspace helper/lifecycle projections were deferred.

`hoi4.event_compare` was attempted against the same current full revision and returned `EVENT_REVISION_NOT_CACHED`. A second artifact-pair attempt returned `EVENT_GRAPH_ARTIFACT_INVALID` because the state-flow artifacts use an unsupported comparison schema. No before/after comparison artifact or semantic change claim exists.

## Validation and blockers

Validation consisted of source-level traces for the exact Event 014 consumption, external-pressure, blockade, rescue, spread, and relief paths; Event 015 settlement, return, integration, policy relief, refugee suitability, sanctuary, and island paths; public API proof triggers/effects; the integration matrix; death-reason ownership matrix; all eight spec parts; the required offline wiki pages; and the required vanilla documentation pages.

No probability or `chaosx_ai_probability_auditor` pass was run because no AI weight, MTTH, random-list weight, decision score, or probability-bearing helper changed.

The remaining blockers are owner-fact blockers, not safe local syntax fixes: Event 014 lacks a shared food or civilian-cohort receipt outside its already-owned cannibalism loss; Event 015 lacks exact stores, refugee intake, return, integration, and relief receipts; and MCP compare lacks a valid cached baseline/artifact schema. The post-inspect/render partial diagnostics are recorded above.

## Simplifications and follow-up

No simplification or fallback was introduced. Leaving both adapters unchanged is the required safe outcome until the event owners expose exact people-denominated facts and proof bundles. A future implementation should patch only the exact source transaction that produces those facts and should keep famine and migration as separate adapter branches.
