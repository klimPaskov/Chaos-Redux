# Event 016 remaining timer probability audit — 2026-09-02

Status: read-only prepatch baseline, owner-applied same-fixture postpatch evaluation, and source comparison completed for the D’Rhondan compact response timer. The comparison is partial because the installed event-option adapter cannot resolve several scoped Clausewitz relationships in the declared fixtures. No gameplay, AI, balance, localisation, configuration, save, log, or runtime files were edited by this audit, and no commit was created.

## Scope and source ownership

The weighted surface is `chaosx.nr16.49` in `events/016_dhrondan_country_events.txt`, adapter `event_option_ai_chance`, with complete candidate pool `chaosx.nr16.49.a`, `chaosx.nr16.49.b`, and `chaosx.nr16.49.c`.

The exact source files reviewed are:

- `common/scripted_effects/016_dhrondan_country_effects.txt` for `dhrondan_refresh_compact_expiry`, `dhrondan_schedule_compact_expiry`, `dhrondan_close_owned_compact_response`, and receipt cleanup.
- `common/scripted_triggers/016_dhrondan_country_triggers.txt` for `dhrondan_compact_response_can_commit` and the shared receipt-validity helpers.
- `events/016_dhrondan_country_events.txt` for `.49` response options and `.52` expiry watchdog.
- `common/scripted_effects/020_black_plague_effects.txt` only for deterministic `black_plague_set_next_devastation_date` and `black_plague_process_current_state_pulse` date-axis receipts.
- `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` only for the latent `brilliant_scientist_evolution_next_check_date` metadata field and the real `.90` delay path.

The prepatch source checkpoint was captured before the owner’s DHR edit at Git `HEAD 5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55`. The prepatch raw SHA-256 values were `953B15AB38A0F71A2D4364D4CABEC6DCC78EACF1B16ADBCFFA9EB4AF5391FC56` for the DHR effects file, `0A948FACF31A241B3108FED3E81EB36E916B0E0A737DC5A27E61BB283ECE8A3A` for the DHR trigger file, and `6BFE2A945FA02DCDA157F8E3EB50C553B41530FFBA3D6BAE914312BF83115B00` for the DHR event file.

The postpatch raw SHA-256 values at handoff are `3C7D99F6A66D3D44DCFC90735A65689535BED7718A78FBADB7F8E69B5B10346B` for the DHR effects file, `9F09F73F935546CCD8DE374FC43E6251E07CD0B1F69A58D5CABACBCC172F631C` for the DHR trigger file, and `6B4D16096D3CDBC6AA2EE2FD504020B5A8707E7FAB2E4E2F5E9C056E08798D56` for the DHR event file.

The immutable scenario fixture is [E016_FINAL_REMAINING_TIMER_PROBABILITY_2026_09_02.scenarios.json](E016_FINAL_REMAINING_TIMER_PROBABILITY_2026_09_02.scenarios.json) with raw SHA-256 `B9D58CC5CEA5711572DABFBD257DE861C1C56EB7A27CA6F21F5E6664BFC1F3C7`. Its scenario-set identity is `E016_FINAL_REMAINING_TIMER_PROBABILITY_2026_09_02`; the evaluator-compatible body strips only the fixture’s audit-only `inputs`, `sourceExpectation`, `candidatePool`, and `externalFactors` fields before MCP submission, leaving every named scenario state and event-target binding unchanged.

The parent-owned DHR edit changed only the functional expiry field and date axis in the captured before/after DHR bytes. The event file changed four lines, replacing `dhrondan_diplomatic_offer_expiry_date` with `dhrondan_diplomatic_offer_expiry_num_days` and `global.date` with `global.num_days` in the `.49` and `.52` checks. The DHR effects file changed nine lines, changing the receipt clear/write/add/schedule field references and the remaining-delay subtraction to the elapsed-day field and `global.num_days`, plus two explanatory comment lines. The DHR trigger file changed two lines in `dhrondan_compact_response_can_commit`. No `ai_chance` base, factor, option trigger, timeout, diplomacy, reward, or event outcome changed in this edit.

The deterministic owner edits were recorded separately from the DHR weighted comparison. The current Black Plague effects raw SHA-256 is `DFC020B21EBFE726892B74A8B05E43860A9252E4977644B62507EBAF1205BE40`, and the current evolution effects raw SHA-256 is `91EEB1EE01234F8B418191B88849F4896966A49CC5C8DCC327D4DA01E5845DED`. The Black Plague patch renames the functional receipt to `black_plague_next_devastation_num_days` and compares it with `global.num_days`; the evolution patch renames the latent metadata to `brilliant_scientist_evolution_next_check_num_days` and leaves `country_event = { id = chaosx.nr16.90 days = brilliant_scientist_evolution_scheduled_delay_days }` unchanged.

## Required reference review

The required offline Paradox wiki pages were read before source inspection: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The required vanilla documentation was read before source inspection: `dynamic_variables_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md` under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.

The relevant engine distinction is that `global.date` is a date value suitable for date presentation/comparison while `global.num_days` is the total elapsed-day value. The offline data-structures page gives the same distinction and notes that the date axis advances in fractional hourly increments. Vanilla `events/LaR_espionage_operations.txt:185-193` provides an elapsed-day subtraction precedent using `global.num_days`.

The offline event-modding and AI-modding pages state that event-option `ai_chance` uses probability proportional to eligible option weights, while the event timeout defaults to an automatic first-option selection when the player does not choose. The MCP adapter reports the same `proportional_categorical` rule, but it does not model the popup timeout/click transaction as a time-distribution adapter.

## Immutable scenario contract

The fixture’s complete candidate pool is the three `.49` options for every row. External factors are explicitly declared in the fixture: ROOT recipient identity, DHR actor identity, regular recipient and offer-target event targets, active and delivered receipt flags, covenant route, recipient/actor existence and subject status, world-end and prior-partner state, war and non-aggression relations, government, opinion, current date, elapsed-day receipt start, intended expiry day, newer-offer target, and the delivery flag required by the click-time commit helper.

The fixture does not claim that the MCP adapter can semantically resolve every scoped Clausewitz relation. The evaluator therefore keeps adapter-unresolved trigger rows visible and no normalized probability is inferred from source arithmetic.

The 14 named scenarios are:

| Scenario id | Declared case | Typed elapsed-day expectation |
| --- | --- | --- |
| `E016_DHR_COMPACT_VALID_ACCEPT` | Valid delivered compact, friendly opinion `+50`, democratic recipient. | Accept score trace `70 × 1.5 × 2 = 210`; expiry remains open while `global.num_days < intended_expiry_num_days`. |
| `E016_DHR_COMPACT_VALID_REFUSE` | Valid delivered compact, hostile opinion `-50`, non-democratic recipient. | Refuse score trace `30 × 3 = 90`; expiry remains open before the due day. |
| `E016_DHR_COMPACT_ALREADY_CONSUMED` | Recipient already has the compact-partner flag. | Shared response validity is false; the cleanup branch is expected to be the only eligible fallback when native routing reaches it. |
| `E016_DHR_COMPACT_TIMEOUT_DAY13` | Thirteen elapsed days after receipt, one grace day still before the `13 + 1` expiry. | Current day is `expiry - 1`; functional commit remains open, while native 13-day timeout behavior is a separate event-engine transition. |
| `E016_DHR_COMPACT_EXPIRED_DAY14` | Exact `13 + 1` elapsed-day deadline. | Current day equals expiry; commit guard is false and the actor-owned watchdog may clear the receipt. |
| `E016_DHR_COMPACT_EXPIRED_DAY15` | One elapsed day beyond the deadline. | No stale reschedule, popup reopen, or indefinite cleanup loop is expected. |
| `E016_DHR_COMPACT_WRONG_INITIATOR` | Receipt actor target is not DHR/covenant. | Response validity is false; unrelated actor state must not be cleared. |
| `E016_DHR_COMPACT_RECIPIENT_DESTROYED` | ROOT recipient no longer exists. | Popup delivery is not valid; actor cleanup ownership remains a lifecycle boundary rather than a normalized option probability. |
| `E016_DHR_COMPACT_NEWER_OFFER_ACTIVE` | Old popup points at a stale offer while a newer offer target is active. | Old response cleanup must not clear the newer offer’s receipt. |
| `E016_DHR_COMPACT_IMPOSSIBLE_CLEANUP_WHILE_VALID` | Identity/route/legality valid but delivered receipt flag is absent. | Shared validity is true, click-time commit remains false, and delivered-only cleanup is not expected. |
| `E016_DHR_COMPACT_MONTH_BOUNDARY_DAY13` | Receipt crosses January 31 to February 13. | Elapsed-day value is `expiry - 1`; date formatting must not affect eligibility. |
| `E016_DHR_COMPACT_MONTH_BOUNDARY_DAY14` | Exact month-boundary expiry day. | Elapsed-day equality expires the receipt. |
| `E016_DHR_COMPACT_YEAR_BOUNDARY_DAY13` | Receipt crosses December 31 to January 13. | Elapsed-day value is `expiry - 1`; the response remains eligible. |
| `E016_DHR_COMPACT_YEAR_BOUNDARY_DAY14` | Exact year-boundary expiry day. | Elapsed-day equality expires the receipt. |

The fixture records `receipt_start_num_days`, `intended_expiry_num_days`, `global.num_days`, and presentation-only calendar date values for the month/year boundary rows. The arithmetic mirror is a review aid and is not an engine proof.

## Mandatory MCP probability inspection

The first weighted call for this audit was `hoi4.probability_inspect` with adapter `event_option_ai_chance`, source identifier `chaosx.nr16.49`, path `events/016_dhrondan_country_events.txt`, the complete three-candidate pool, and `refresh=true`.

The prepatch inspect returned `PROBABILITY_SOURCE_INSPECTED` with workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `601c8a57705d1fcb3c2c859c05dd75aad8016e3c83ddce150c845deed871778e`, MCP source hash `d08b1a2e6ccdd8992541f953e9978b09f74a4513e2444bf2485a868b74308c93`, `poolComplete=true`, three candidates, six required inputs, zero inspect-unresolved items, and no statically available candidates. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd95bcd50269f94091c5e8ced378ea2cb468aeb3676667bfed8c4ddee20ed0bd/4a58b8995157e0d7d3b5b2b5ad3510448a365176eb947b3a5536f4799f879085/probability-inspect-d08b1a2e6ccd.json`.

The postpatch mandatory inspect returned `PROBABILITY_SOURCE_INSPECTED` with source revision `8012ad69a31d6b06b8c682ae436677e3b7014e0eda6a4b30d1e8e1c9afafaa49`, MCP source hash `7599a442e217ef8853f4b71eb5187b4b0b7cdffd55798a63a7b9bff050731f80`, `poolComplete=true`, three candidates, six required inputs, zero inspect-unresolved items, and no statically available candidates. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d49c233e028e834f1adcc24444b0e90f38971d4b7be05129e2af4aaf7bc6cfee/f2cd7d720430593efab176fdfa2b84f661a5d5046fa63f4e5424ee722dd65ffa/probability-inspect-7599a442e217.json`.

The two inspections agree on the complete three-option source pool and six required inputs. The source revision and MCP canonical hash differ because the owner edit changed the event source’s timer field references, while the option-weight definitions remained unchanged.

## Prepatch bounded probability baseline

The prepatch `hoi4.probability_evaluate` used the exact held prepatch event bytes through `inlineClausewitz`, the complete three-option pool, and the evaluator-compatible form of the immutable 14-row fixture.

The result was `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-c504bc1079ec4e09fac9baf3`, adapter `event_option_ai_chance`, source revision `b6eb2e68f6b8357368fdecf4c00fb6b926923c30b663a6f7f370e003816b85d1`, MCP source hash `b146164d3452f3d865e739fbf244ca14f99c458e152e2e26eb1918011ea0e2f2`, scenario hash `1fed22d9f63e8ba99020db7dd22b6671aaa0f75cbd7e33e2cd647c676a4474d1`, candidate-pool hash `63eb069fbd0beb61983d7959ffbc8320d0833b261fc591bd0a7cbba9c2176e77`, 14 scenarios, 42 candidate rows, 9 unresolved items, 18 diagnostics, and seven emitted artifacts.

The authoritative baseline JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca64f0aef360b119d625876157ee3a448fc2a3c2cdf74d2e16f5d3d5e01170a0/91fb04dfe3bb549b44fac8ca46e413523a6efda30dbcb89bab96a8ffdd958ef3/probability-c504bc1079ec4e09fac9baf3.json`.

The baseline emitted ranking, matrix, and unresolved visual evidence within the same result. Their URIs are:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/188553db03d5717b3e54548209ca6ef33cc1974727d230bc692a4d5541de3fdc/e6a84bcc0d497d59948c878231f38d8c99cdd4f516b51da73422dd6d9e2b1056/probability-probability-c504bc1079ec4e09fac9baf3-ranking.svg`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf11ce624e9677481d875e3e2da61f7f194e76d36f790d50bea6bdb664f770ee/e8870eb5a117c08dee74029459947e5217878c4795818ab54e6ce1bbd11a17f3/probability-probability-c504bc1079ec4e09fac9baf3-matrix.svg`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c34c62df96231987af61954f29f83adebffa09ebf249df4ce2bd0981004a8b49/e5599590ed8487f3a5f1d004c5fbe84e8cc1e92c11eb259c5cf27008e7c931eb/probability-probability-c504bc1079ec4e09fac9baf3-unresolved.svg`.

The adapter observed `chaosx.nr16.49.a` and `.b` as never eligible and `.c` as dominant in all 14 rows, but these are not campaign probabilities. The declared event-target binding and scoped helper representation leave the adapter unable to certify valid a/b eligibility in this fixture, and the unresolved set includes scoped or compound `has_opinion`, `has_war_with`, `has_non_aggression_pact_with`, and a government-state dependency. No normalized accept/refuse probability is claimed.

The 18 baseline diagnostics include `EVENT_OPTION_FALLBACK_NOT_PROVEN`, one `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostic each for `.a` and `.b`, one `PROBABILITY_OUTCOME_DOMINANT_ACROSS_SCENARIOS` diagnostic for `.c`, and per-scenario `PROBABILITY_DOMINANT_OUTCOME` warnings caused by the adapter’s resolved cleanup fallback. These diagnostics describe the bounded fixture and unresolved helper semantics; they do not establish a gameplay cleanup dominance or duplicate-resolution outcome.

## Typed source score truth

The option formulas are source-level willingness scores, not click probabilities unless the complete eligible pool is engine-resolved. The source constants are accept base `70`, refuse base `30`, friendly opinion factor `1.5` above `25`, hostile opinion factor `3` below `-25`, and democratic-recipient covenant factor `2`.

| Typed recipient state | Accept score | Refuse score | Classification |
| --- | ---: | ---: | --- |
| Friendly `+50`, democratic | `70 × 1.5 × 2 = 210` | `30` | Score-only source trace. |
| Friendly `+50`, non-democratic | `70 × 1.5 = 105` | `30` | Score-only source trace. |
| Neutral `0`, democratic | `70 × 2 = 140` | `30` | Score-only source trace. |
| Neutral `0`, non-democratic | `70` | `30` | Score-only source trace. |
| Hostile `-50`, democratic | `70 × 2 = 140` | `30 × 3 = 90` | Score-only source trace. |
| Hostile `-50`, non-democratic | `70` | `30 × 3 = 90` | Score-only source trace. |

The source formulas, constants, and candidate pool were unchanged by the timer patch. The theoretical normalized pairs above are intentionally not reported as MCP or engine probabilities.

## Timer and lifecycle findings

Before the owner edit, `dhrondan_refresh_compact_expiry` wrote `dhrondan_diplomatic_offer_expiry_date = global.date` and added the 13-day response timeout plus one-day grace constant. The `.49` trigger, `.52` watchdog, `dhrondan_compact_response_can_commit`, and `dhrondan_schedule_compact_expiry` read or subtracted that date-valued receipt as if it were an elapsed-day integer.

The repaired source stores `dhrondan_diplomatic_offer_expiry_num_days = global.num_days`, adds the same 13 and 1 constants, compares the receipt with `global.num_days`, and subtracts `global.num_days` for the `.52` delay. The native `.49` timeout remains 13 days, and the extra one-day grace remains a cleanup-only buffer.

At the typed fixture level, day 13 rows remain below the intended expiry, exact day 14 rows fail the strict `< expiry` commit test, and day 15 rows remain expired. Month and year boundary rows preserve the same elapsed-day result regardless of their formatted calendar date. These timer conclusions are exact source arithmetic and typed eligibility policy, not proof of native event delivery ordering.

The valid acceptance and refusal rows retain the same source score traces before and after the patch. The already-consumed, wrong-initiator, destroyed-recipient, newer-offer, and impossible-cleanup rows remain lifecycle guard cases with no normalized probability claim. The watchdog and cleanup ownership remain deterministic state transitions outside the event-option probability adapter.

## Deterministic helper inspections

The required probability-inspect route was also used only on the named deterministic helper surfaces and the evolution metadata. Each completed inspection returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, zero available adapters, zero required inputs, and zero unresolved items.

Prepatch exact helper-block inspections were:

- `black_plague_set_next_devastation_date`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eeb583b0a0006f49c4d6d1e16e9ddf7e7901ae3b69c45ffe96bd447560030dd/698776d9690c78f705bf7f68ad2e4721a272508489244b6340f53a84be9014ca/probability-inspect-99bfbe1bcc19.json`, source hash `99bfbe1bcc19f55f89dab7a3e1745a8061f06e01716858f6ffde6568d54afe13`.
- `black_plague_process_current_state_pulse`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3deb2d2428f3e93e2a26f1625d0767a880907a027ddcd0b3c87046ef9e9fdd0/a5c96083be444dfb2ba93fde6a9e1e7b71281ee208aefbf3d532c1ba38cdc633/probability-inspect-96e0579441d8.json`, source hash `96e0579441d8b296e9b857320cd89cd71c814b4071e5d7d663fb01dd74e7d5ba`.
- `brilliant_scientist_schedule_next_evolution_check`, the block containing the latent next-check metadata and the real `.90` delay, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a0550e048c5fb8d4d5f4075c0b711cf4383ae7edab3250fe60ef0bc19a3ef8b/1ffb762512c037d11d192f6c50734c35af9ce4e6b76cd1a825438210aadfde9b/probability-inspect-8db5484423c0.json`, source hash `8db5484423c045543d4e4d2dc1bcc836ca947a8d6f4d3f0598c56413b771340f`.

Postpatch exact helper-block inspections were:

- `black_plague_set_next_devastation_date`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1244eb41d57513dd4baf9496f05c01ef41ab0f3085ef68352bb666ae954f2b0/a42cd9512ffb6e9fdf257be3a348cddf62300db33375f742a5705dfec98ce022/probability-inspect-6088191c40ad.json`, source hash `6088191c40ad0472a314e83d50593991f9179dd818765b317fb1939a4421f5de`.
- `black_plague_process_current_state_pulse`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75dd2e130934b0009c4c19fda84af1b324904fe632f388ddf80e59d008d4f687/401972b18af6f645d9a23f702cd67127bdc10ff063783bf545be9bee9edf8c2e/probability-inspect-1c452f809afc.json`, source hash `1c452f809afcf5e1ab9e0f0996bc89089fbb8e8c0a994f1b20581c319e56dc43`.
- `brilliant_scientist_schedule_next_evolution_check`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e96caa96b869aa5d66b93d2a16e8e8fc87748629dc3e57617db6857ba5ebe842/d66c7234576fd79ad28f06eea1cf8cf1dddd94545400cc0b117d2de4e12a7e30/probability-inspect-90c98a9dc406.json`, source hash `90c98a9dc406e6da569fa7d07503093f3f9b06cb30a9ed7b641caa64c92d4cce`.

A path-only postpatch inspect of the evolution effects source also returned no weighted surfaces with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2304a211e27d8ae03433af7a6cc2f2fee5d8d09100f27b656641829d9a99250/8ecaee04dc0bf89a55cf7718c0019209ddf79be9af8f326e362066c506426b80/probability-inspect-b2fa563c6946.json` and source hash `b2fa563c694634a280e899d3dca70dfa667eae774087241e19c03ae784c5ab34`.

The initial full-file deterministic inspect attempts for the Black Plague pulse and evolution metadata returned `INTERNAL_ERROR` when the helper was represented as a large inline file. They were not treated as evidence; the exact helper-block retries above are the authoritative no-weight results. No broad Black Plague scheduler or activation analysis was performed.

Because these helpers are deterministic date/receipt transitions and expose no weighted adapter, no probability evaluation, sweep, simulation, or sequence analysis was attempted for them. Their month/year boundary values remain typed source scenarios in the immutable fixture and are not presented as normalized probabilities.

## Postpatch same-fixture evaluation and comparison

The postpatch `hoi4.probability_evaluate` reused the identical evaluator-compatible 14-row body, candidate pool, and scenario-set identity. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-8d7eaefb19b1423c601f6d4c`, source revision `8012ad69a31d6b06b8c682ae436677e3b7014e0eda6a4b30d1e8e1c9afafaa49`, MCP source hash `7599a442e217ef8853f4b71eb5187b4b0b7cdffd55798a63a7b9bff050731f80`, and the same scenario hash `1fed22d9f63e8ba99020db7dd22b6671aaa0f75cbd7e33e2cd647c676a4474d1`. It produced 14 scenarios, 42 candidate rows, 9 unresolved items, 18 diagnostics, and seven emitted artifacts.

The authoritative postpatch JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f73e2f829a151fd715381e71c5663989e8fdaffd99cbc000ba52bd0717ec2ff4/743385366daeafc0b578d5701db4c21fab5f53966dc974466ac6eeb67f5ef187/probability-8d7eaefb19b1423c601f6d4c.json`.

The postpatch evaluator emitted the same ranking, matrix, and unresolved view classes as the baseline. The option-level diagnostic pattern remains the same: fallback not proven, `.a` and `.b` never eligible under the adapter’s fixture interpretation, and `.c` dominant under that same unresolved interpretation. This is unchanged adapter observability, not a claim that the timer repair changes cleanup selection.

The same-fixture `hoi4.probability_compare` used the held prepatch event bytes as `before.inlineClausewitz` and the current owner-edited event bytes as `after.inlineClausewitz`, with the identical three-candidate pool and scenario-set body. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-9d161494020a35561f9bf10d`, the unchanged scenario hash `1fed22d9f63e8ba99020db7dd22b6671aaa0f75cbd7e33e2cd647c676a4474d1`, 14 scenarios, 42 candidate rows, 12 aggregate unresolved items, 18 diagnostics, and `comparisonChanges=0`.

The authoritative comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e650935042fb50c7a8b014f65cbb1f47c23b983af41f7004bfa40bda566f949/194a1390b4a467f45356610e3d90d7d5fcd11908637a85d3fd7d288754abe53e/probability-9d161494020a35561f9bf10d.json`.

The comparison emitted ranking, matrix, comparison, and unresolved resources. The direct comparison SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/9e548a24b5c763d6c54b8b29047286a2cf7656f6360828e5017ddfca26701f9b/probability-probability-9d161494020a35561f9bf10d-comparison.svg`.

The comparison’s zero source-driven changes, unchanged scenario hash, unchanged candidate pool, and unchanged score diagnostics show that the owner patch did not alter `.49` ai_chance weights, modifiers, or the declared candidate race. This result is a score/provenance comparison and does not certify native date scheduling, popup timeout ordering, or lifecycle cleanup equivalence.

The compare service evaluates scripted helpers from the current workspace while comparing the two inline event bodies. Therefore the compare isolates the DHR event source field changes and candidate formulas, but it does not provide a helper-isolated before/after execution proof for the trigger/effects files. The prepatch evaluation and local before/after byte diff preserve the before helper context and exact owner change boundary; no helper-isolated probability claim is made.

## Structural event evidence

The narrow read-only `hoi4.event_inspect` trace was requested for `{kind:event,eventId:chaosx.nr16.49}` and `{kind:event,eventId:chaosx.nr16.52}` with both directions, helper expansion, depth 3, and node/edge bounds. Both returned `EVENT_INSPECTED_PARTIAL`, focused revision `46be3d59f3ccef8446fa4fe1c9f41fbe061df3294949220d874c29f393518c08`, graph hash `ba9ec7f07ca8a39c3856d8744a1364bd4b27efff4637ebfb58c4b67b0f17551f`, zero blocking diagnostics, and a large-workspace deferred-helper/lifecycle limitation with `helpers=0` and `8684` unresolved nodes. The `.49` trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a53ec339836738586794b348d7f140a9d2ea4054a03c8a124a003220e918262f/70522507da9cb298aaf00844a36f21f769eb179801d03aafc3d5240cbc3df58a/event-trace-46be3d59f3cc.json`, and the `.52` trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6bcf80e442e970d4cbeebca416902940b33fcee62d19f9f3d92f59b21fd95b7b/96e31d823fe183bee5de35dc197ecba4914be5ebf3a22e7e848f103d392dbc8d/event-trace-46be3d59f3cc.json`.

The matching `hoi4.event_render` options view for `.49` returned `EVENT_RENDERED_PARTIAL` with layout hash `27533b940e91dcf40bb06993d831b863008a94275c29725345410fcf97da98bc`; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4232685faaa1d86af8f70e2aea36aa63cd1528495725952660a53b7cca0f3f64/280f74f8b1caab54ea56d9c8ee0673daa4c36668eaab397cc8d48facc394a38f/event-options-46be3d59f3cc-manifest.json`.

The matching `.52` timing view returned `EVENT_RENDERED_PARTIAL` with layout hash `cb2c55195ec96915e60d93cc54311a2211c0a5187c2b6d4fb452fbb69f8d4318`; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af3877284823b5ebcf43ad1800ac6009a2a36f5ee82a59ab83240c1fc05c19ac/200aabc33477db963bddc94d20ce56da71d7770f5b4b0d3fcf114db950fa2b91/event-timing-46be3d59f3cc-manifest.json`.

The structural artifacts are supporting evidence for event wiring and selected branch/timing nodes only. Their deferred workspace-wide projections cannot prove the runtime scope of every receipt or helper.

## Balance and exploit-risk conclusions

No weight balance change is indicated. The option base and modifiers remain `70/30`, `1.5`, `3`, and `2`, and the same-fixture compare reports zero measurable source-driven score or rank changes.

No normalized accept/refuse probability is certified because the event adapter cannot resolve all scoped legality and opinion inputs in the fixture, even though the static three-option pool is complete.

The timer repair removes the identified date-axis unit mismatch in the functional DHR receipt, but native popup delivery, timeout auto-selection, click ordering, stale target ownership, recipient destruction, and actor cleanup cadence remain outside this adapter’s probability model.

The fixture explicitly covers valid acceptance/refusal, already consumed state, exact day 13/14/15 timeout/expiry boundaries, wrong initiator, destroyed recipient, newer offer ownership, impossible cleanup while valid, and month/year calendar boundaries. The valid rows retain deterministic score-only formulas; invalid and lifecycle rows remain bounded eligibility/cleanup scenarios.

No dominance, starvation, repetition, or snowball balance conclusion is promoted from the adapter’s fixture-limited `.c` dominance warning. The warning is retained as unresolved evidence because `.a` and `.b` were made ineligible by unresolved scoped target/helper semantics.

## Skipped analyses, blockers, and uncertainty

- `hoi4.probability_render` was attempted for the baseline analysis id but returned `PROBABILITY_ANALYSIS_NOT_CACHED` because the render endpoint requires an analysis id from the same server process. The evaluator-emitted ranking, matrix, and unresolved resources are retained instead.
- `hoi4.probability_sweep` was not run because this task requests a fixed timer fixture and no tunable weight, threshold, or uncertain input. A sweep cannot prove date-axis correctness for a deterministic receipt.
- `hoi4.probability_simulate` was not run because no uncertain input distribution or approved seed was declared, and the event adapter is not a timer-distribution model.
- `hoi4.probability_sequence` was not run because the DHR popup/watchdog path is not a declared complete custom weighted sequence with cadence, cooldown, recovery, reset, and terminal-state manifest.
- The first large-inline deterministic helper attempts for the Black Plague pulse and evolution metadata returned `INTERNAL_ERROR`; exact helper-block retries returned authoritative no-weight inspections and are the evidence used here.
- No broad Black Plague scheduler or activation trace was inspected, per scope ownership with the timer/transaction auditor.
- Structural event inspection and render are partial because the large workspace deferred helper and lifecycle projections and truncated the source inventory to 64 of 368 files.
- The compare service’s helper context is current-workspace-expanded for both inline event bodies, so no helper-isolated before/after claim is made.
- No game launch, save inspection, log search, or runtime validation was performed.

## Parent handoff

The source freeze was released before the DHR edit with exact Git head, raw hashes, held prepatch event bytes, and fixture SHA. The owner may retain the three elapsed-day repairs and unchanged option weights/durations/outcomes. The exact same-fixture postpatch evaluation and compare show `comparisonChanges=0`; remaining uncertainty is limited to adapter scope semantics and native runtime ordering described above.
