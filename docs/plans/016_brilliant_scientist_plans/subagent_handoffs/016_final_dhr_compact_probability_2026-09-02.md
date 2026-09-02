# Event 016 D’Rhondan Compact Response Probability Handoff

Status: prepatch read-only baseline and frozen-source postpatch comparison completed; the comparison is partial and no DHR gameplay, weight, localisation, or balance source was edited by this audit.

## Audited surface and retained source

The weighted surface is the three-option event `chaosx.nr16.49` in `events/016_dhrondan_country_events.txt:23-110`, using adapter `event_option_ai_chance` and candidate pool `chaosx.nr16.49.a`, `chaosx.nr16.49.b`, and `chaosx.nr16.49.c`.

The exact before-event source is retained from commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`, Git blob `047ab4aea29d38a322c354dc11bfa6e1b208eb92`, and working-tree SHA-256 `83c1aae6b2a625bdf4e34dc201c7298be108cef323df21e683f76bac72769945`.

The validity helper is `dhrondan_compact_response_is_valid` in `common/scripted_triggers/016_dhrondan_country_triggers.txt:178-195`; its exact before blob is `5c46fcb3fd7fce3a68f9dbd1eac5444bcf59541a` and its current working-tree SHA-256 is `791c97a24e2f97fcae0145087f1997d46f88ac4fe908b36ec5ad39176a1a4e81`.

The route helper `dhrondan_is_covenant_regime` is in `common/scripted_triggers/016_dhrondan_country_triggers.txt:52-55`, and offer cleanup `dhrondan_clear_diplomatic_offer` is in `common/scripted_effects/016_dhrondan_country_effects.txt:266-273`; the exact before effects blob is `ab2c5d38cebf325e1c1921649ec3bb6e45602147` and the current working-tree SHA-256 is `b6492039c1d17094ea912696f3daeb5d2128599b0b5a87071ed5279f352896f7`.

The helper/effects working-tree status differs from the retained commit only in line-ending representation under `git diff --ignore-space-at-eol`; no semantic helper/effect change was observed in this baseline checkpoint.

The source constants are in `common/script_constants/016_dhrondan_country_constants.txt` and resolve to accept base `70`, refuse base `30`, friendly factor `1.5`, hostile factor `3`, covenant-democratic factor `2`, positive opinion threshold `25`, and negative opinion threshold `-25`.

The full scenario bodies are preserved in [E016_DHR_COMPACT_RESPONSE_2026_09_02.scenarios.json](E016_DHR_COMPACT_RESPONSE_2026_09_02.scenarios.json).

## Mandatory MCP inspection

The first weighted call was `hoi4.probability_inspect` with workspace `mod_chaos_redux_ea3b2d67c2c0`, adapter `event_option_ai_chance`, source identifier `chaosx.nr16.49`, and path `events/016_dhrondan_country_events.txt`.

The inspect returned `PROBABILITY_SOURCE_INSPECTED` with source hash `e0c8f17d8553c44914f2627d6844b17f3537c900277684a6b17443c638e0c7f2`, source revision `4bf6c0dbd51ef142433d2ef25cb14befb0f75afb0da286136cdd4bdc42bfc06e`, three candidates, `poolComplete=true`, six required inputs, and zero inspect-unresolved items.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65cbe58b65c1c63eab11754bd9fa8bb3d9e9e4347c92cf2ccf9a6965d54bd13b/07a0f50d2a97b63fd1109fd1bd6e7089653038bb9d56ecfa8f504a6798d4432f/probability-inspect-e0c8f17d8553.json`.

The inspect identified `a` and `b` as weighted options and `c` as a trigger-gated option without an `ai_chance` block, with the selection rule reported as `proportional_categorical` and normalized probabilities available only when all candidate eligibility is resolved.

## Named baseline scenarios

The fixture contains thirteen bounded scenarios with ROOT recipient `ABC`, DHR actor target, and explicit route, active-offer, delivery-receipt, subject, opinion, government, war, non-aggression, and target-mismatch inputs.

The valid matrix is `E016_DHR_COMPACT_VALID_FRIENDLY_DEMOCRATIC`, `E016_DHR_COMPACT_VALID_FRIENDLY_NONDEMOCRATIC`, `E016_DHR_COMPACT_VALID_NEUTRAL_DEMOCRATIC`, `E016_DHR_COMPACT_VALID_NEUTRAL_NONDEMOCRATIC`, `E016_DHR_COMPACT_VALID_HOSTILE_DEMOCRATIC`, and `E016_DHR_COMPACT_VALID_HOSTILE_NONDEMOCRATIC`.

The invalid and lifecycle matrix is `E016_DHR_COMPACT_INVALID_ACTOR`, `E016_DHR_COMPACT_INVALID_RECIPIENT`, `E016_DHR_COMPACT_INVALID_ROUTE`, `E016_DHR_COMPACT_INVALID_WAR`, `E016_DHR_COMPACT_INVALID_SUBJECT`, `E016_DHR_COMPACT_DELIVERED_DUPLICATE`, and `E016_DHR_COMPACT_STALE_RESPONSE_RECEIPT`.

The candidate pool is complete as declared for every fixture row, but the fixture does not make an engine-level claim that the adapter can resolve scoped Clausewitz relations.

## Prepatch MCP evaluation

The source-backed `hoi4.probability_evaluate` used the exact event bytes from the retained commit as `inlineClausewitz`, the candidate pool above, and the identical thirteen-scenario fixture.

The result was `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-2a3f004b2e50e0ecd4450265`, source hash `e682360d976322756325d3461e6ab52c43a0edb95077c9f560a4368303872358`, source revision `a4ed0fe8b07fa8c9bd84db58c8156c49cc89fc952914ee53ded6f43cd610eba3`, scenario hash `bd600830ba0b953ccb964335a90e5e126c38b2d76bf8e060e44e9719befc6f5d`, candidate-pool hash `63eb069fbd0beb61983d7959ffbc8320d0833b261fc591bd0a7cbba9c2176e77`, and 39 candidate rows.

The authoritative evaluation JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a669c30275fb3ff3406436c0982f96b0014fca2d817a28569e80dce24ad8f01b/a590fa62bae36d140f86e3efec293f2c10814393f9ee46747c138c0d29e35b54/probability-2a3f004b2e50e0ecd4450265.json`.

The evaluation artifact reports `chaosx.nr16.49.a` raw value `0`, conditional probability `0`, and ineligible in all thirteen rows; it reports `chaosx.nr16.49.b` raw value `0`, conditional probability `0`, and ineligible in all thirteen rows; and it reports `chaosx.nr16.49.c` raw value `1`, conditional probability `1`, rank `1`, and eligible in all thirteen rows.

Those row values are adapter output, not campaign probabilities. The adapter evaluates `event_target:dhrondan_diplomatic_offer_target = { tag = ROOT }` as a literal `ROOT` comparison against the bound `ABC` target, so otherwise-valid a/b rows are rejected by the fixture binding. It also leaves `has_opinion`, `has_war_with`, and `has_non_aggression_pact_with` unresolved even though the fixture declares opinion and relationship fields.

The aggregate unresolved set is eight rows covering `has_war_with`, `has_non_aggression_pact_with`, and scoped or compound `has_opinion`. The adapter still reports `poolComplete=true`, but that schema-level completeness does not establish complete semantic eligibility for these scoped helpers; normalized option probabilities are therefore unresolved.

The adapter diagnostics include `EVENT_OPTION_FALLBACK_NOT_PROVEN`, `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for a and b, and `PROBABILITY_OUTCOME_DOMINANT_ACROSS_SCENARIOS` for c. These diagnostics describe the supplied adapter fixture and are not proof that cleanup c is the native AI choice in a valid campaign.

## Score-only source trace

The following are source-derived score traces only and must not be presented as MCP-certified probabilities until scoped validity and opinion relations are resolved.

| Scenario class | Accept score | Refuse score | Score-only normalized view |
| --- | ---: | ---: | --- |
| Friendly, democratic, opinion `+50` | `70 × 1.5 × 2 = 210` | `30` | `87.5% / 12.5%` |
| Friendly, non-democratic, opinion `+50` | `70 × 1.5 = 105` | `30` | `77.78% / 22.22%` |
| Neutral, democratic, opinion `0` | `70 × 2 = 140` | `30` | `82.35% / 17.65%` |
| Neutral, non-democratic, opinion `0` | `70` | `30` | `70% / 30%` |
| Hostile, democratic, opinion `-50` | `70 × 2 = 140` | `30 × 3 = 90` | `60.87% / 39.13%` |
| Hostile, non-democratic, opinion `-50` | `70` | `30 × 3 = 90` | `43.75% / 56.25%` |

The table is an audit of base values and modifier traces, not a claim that the event option pool is currently normalized in the engine.

## Prepatch lifecycle and validity findings

The valid options a and b share `dhrondan_compact_response_is_valid`, which checks ROOT existence, world-end exclusion, recipient subject status, prior compact-partner status, both event targets, target identity, DHR identity and existence, covenant route, active offer, DHR subject status, war exclusion, and non-aggression-pact exclusion.

The event immediate block sets `dhrondan_diplomatic_offer_delivered` before the option is selected, while the shared validity helper does not require that delivery flag to be absent. The delivered-duplicate scenario therefore remains a required lifecycle fixture; source review flags duplicate resolution as a risk, but the MCP adapter cannot prove native popup delivery or click timing.

Option c is the invalidation cleanup branch and has no declared `ai_chance` block. Its trigger is the negation of the shared validity helper, and its effect can clear the DHR active/delivered flags and the global offer target through `dhrondan_clear_diplomatic_offer`. The stale-response fixture is necessary because a stale target can fail the shared identity check while the cleanup effect still addresses the actor’s current receipt; native ordering and receipt identity are unresolved by this option adapter.

The event-level trigger is separate from option eligibility and includes a delivered-absent fallback path. This audit does not claim that an invalid or stale popup reaches c in every runtime path, because the probability adapter evaluates option triggers rather than the full event-delivery scheduler.

## Structural MCP evidence

The narrow `hoi4.event_inspect` trace for `{ kind: event, eventId: chaosx.nr16.49 }` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics, focused revision `18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f`, and graph hash `e12130ac480e90a1098f39e8c272668599c42b61125c7a027bb8e84ebe6652d9`.

The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab08aa826d9e6d15e9fc02f3f38fbca71c052f31d423c5281c2b335dc8279b9b/048c2ee7cca0f876f36544a009b757f1a6de7e841617336f48cfe087556e2974/event-trace-18bf807c8be3.json`.

The matching narrow `hoi4.event_render` options view returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash with layout hash `cee7031be5d8d8ae165904f528ae19c61cfa8c321525de52bd55e83145caffcc`, JSON hash `a8b33dad39de4c66eefcff563ac11db897970c88fb8bcb3916e800becb339736`, SVG hash `4d3c2cc8eee32012d1cab3e16b31a39a276c1437514640fc13f109385c299903`, and PNG hash `b24e9edbc8352ed1008967c93a6d907adfb3f76e9017bf64a69ff2592652f38b`.

The options render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80aef687986785fc509eb716d42d71ee0c763fd986acdd583f42071bce4bf1f4/2ff56e01cd500a9eabadc6922800a7c1c6093e7fe13b75c694ca537a4b2ef259/event-options-18bf807c8be3-manifest.json`; the source-linked SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d3c2cc8eee32012d1cab3e16b31a39a276c1437514640fc13f109385c299903/1de216c2992345786a1d52eef03088c7c7f3142cbd3c9dc5483df8f8f36d405c/event-options-18bf807c8be3.svg`.

Both structural views remain partial because the large workspace deferred workspace-wide helper and lifecycle projections.

## Frozen-source postpatch comparison

After the owner freeze, a fresh mandatory `hoi4.probability_inspect` against `events/016_dhrondan_country_events.txt` and `chaosx.nr16.49` returned `PROBABILITY_SOURCE_INSPECTED` with source hash `d08b1a2e6ccdd8992541f953e9978b09f74a4513e2444bf2485a868b74308c93`, source revision `3ef5b3068a4601057c94b62fc772f0e2eefdf51b2838ed1da60df17658c6f262`, three candidates, `poolComplete=true`, six required inputs, and zero inspect-unresolved items.

The post-freeze inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bde739689eea283de0e1538bb628a8e046b6d0dc1e97da89673706df4e67a197/ef0d3e1cda22e29d7e2f3574d056475bce149f3a393374caab52c8496c474580/probability-inspect-d08b1a2e6ccd.json`.

The frozen working-tree SHA-256 values are `6bfe2a945fa02dcda157f8e3eb50c553b41530ffba3d6bae914312bf83115b00` for `events/016_dhrondan_country_events.txt`, `e82b7b4f44ff3b38ff0561a268960f811d04363071555cdd6e30ebebebe53ee2` for `common/scripted_triggers/016_dhrondan_country_triggers.txt`, and `953b15ab38a0f71a2d4364d4cabec6dcc78eacf1b16adbcffa9eb4af5391fc56` for `common/scripted_effects/016_dhrondan_country_effects.txt`.

The exact same fixture and candidate pool were passed to `hoi4.probability_compare`, with the before source object built from the retained `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd` event bytes and the after source object built from the frozen current event bytes.

Comparison scope limitation: both `inlineClausewitz` source objects contained the event bytes only, so the probability service expanded scripted helpers and constants from the current workspace for both sides. The comparison therefore isolates the event source object but does not isolate prepatch versus postpatch helper definitions. The standalone prepatch evaluation remains the retained baseline for the prepatch helper context; no helper-isolated before/after comparison is claimed.

The comparison returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-385a5e5b7beb22671bf36688`, source hash `b146164d3452f3d865e739fbf244ca14f99c458e152e2e26eb1918011ea0e2f2`, source revision `47df6d03db2f33ce9ee84630aadf4d938cd2f2ccae245485e52d8b0f0fd38bae`, the unchanged scenario hash `bd600830ba0b953ccb964335a90e5e126c38b2d76bf8e060e44e9719befc6f5d`, the unchanged candidate-pool hash `63eb069fbd0beb61983d7959ffbc8320d0833b261fc591bd0a7cbba9c2176e77`, 13 scenarios, 39 rows, 10 aggregate unresolved items, 17 diagnostics, and `comparisonChanges=0`.

The authoritative comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98334de4e2e5c2aaa4efa13199ee26e0a379554340b3eb27b02eb83ec980b644/3dde672bfb25928623ebe25cf5e2bb31ab8493abc9b8606f278005578d0ca52b/probability-385a5e5b7beb22671bf36688.json`.

The comparison object records `beforeAnalysisId=probability-192d159a1cd56a664b28909b` and `afterAnalysisId=probability-0959401caec3dc4bb6951d95`, with `adapterChanged=false`, `assumptionsChanged=false`, an empty `scenarioChanges` array, and no regressions.

The comparison ranking, matrix, comparison, and unresolved renders are retained in the same MCP result; the direct comparison SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/fc2ccd740cdb5e4158cf4d999ceb58473fd17fbfd566964c649ee7a9fc920dc1/probability-probability-385a5e5b7beb22671bf36688-comparison.svg`.

The frozen source adds `dhrondan_compact_receipt_matches_recipient` at `common/scripted_triggers/016_dhrondan_country_triggers.txt:178-188`, folds it into `dhrondan_compact_response_is_valid` at `:192-204`, adds `dhrondan_compact_response_can_commit` at `:207-215`, and changes the event to a 13-day native timeout with delivery/expiry guards at `events/016_dhrondan_country_events.txt:28-46` and click-time guards at `:63-113`.

The retained fixture intentionally has the global actor and offer-target bindings but no regular `dhrondan_diplomatic_recipient` binding, because that target did not exist in the prepatch source. In the after trace, `has_event_target = dhrondan_diplomatic_recipient` is therefore false at helper line 180 and both `tag = event_target:...` identity comparisons at lines 182-183 are false. This is an exact explanation of why the unchanged adapter rows still show a/b ineligible and c at raw value `1`; it is a fixture compatibility limitation, not proof that the owner’s new receipt guard rejects valid in-game recipients.

The after per-scenario rows remain `a=0`, `b=0`, `c=1` with `poolComplete=true`, while each scenario remains support-limited by unresolved `has_war_with` and `has_non_aggression_pact_with` in `dhrondan_compact_response_is_valid` and unsupported scoped `has_opinion` in the a/b AI modifiers. The new explicit actor-to-recipient relation is also not semantically evaluable by this adapter when the target is represented only as a Clausewitz event target.

No weight or AI formula changed: the a/b bases and friendly, hostile, and democratic modifiers remain the same 70/30, 1.5, 3, and 2 values documented above. The comparison therefore finds no measurable ranking or score delta, but it does not certify the new delivery, expiry, click-time commit, timeout watchdog, or stale-receipt behavior.

The postpatch result is consequently a valid same-scenario source comparison with zero measurable changes and partial probability support, not a full normalized campaign-probability or lifecycle-equivalence proof.

## Recommended owner follow-up

1. Retain the owner’s ordinary delivery, receipt-identity, expiry, click-time commit, timeout, and owned-cleanup lifecycle patch as the current source-review state; this audit found no weight change to request.

2. Treat the current comparison’s unchanged rows as fixture-limited evidence, not as proof of the new helper’s native validity; a future adapter-capability pass may use a separate fixture that declares the regular recipient target without mutating this retained baseline fixture.

3. Preserve the existing a/b source scores and c cleanup intent unless a separate balance request changes them; this audit found no evidence requiring weight edits.

4. Reuse the exact scenario hash and source-object compare if a later DHR source or weight change occurs, and retain the scoped `event_target`, opinion, war, and pact limitations if the adapter still cannot bind them.

## Blockers and uncertainty

The MCP probability adapter cannot express the ROOT identity relation for `event_target:dhrondan_diplomatic_offer_target`, cannot evaluate the compound `has_opinion`, `has_war_with`, or `has_non_aggression_pact_with` triggers, and does not model event popup delivery, immediate effects, click ordering, or receipt races.

Therefore no exact normalized campaign probability, duplicate-popup rate, stale-cleanup rate, or event-delivery probability is established by this baseline.

No probability sweep, simulation, or sequence analysis was run because the required complete eligible pool and lifecycle cadence were not resolved.

The owner freeze and same-scenario postpatch `hoi4.probability_compare` are complete; the remaining uncertainty is the explicitly documented helper-scope and lifecycle-adapter boundary, not a missing compare call.

Offline Paradox wiki pages and the required vanilla documentation for event options, triggers, effects, scopes, and AI weighting were consulted alongside the source and MCP evidence.
