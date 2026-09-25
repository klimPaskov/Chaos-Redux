# Event 021 Current-Source Probability Audit

Date: 2026-09-25

Disposition: read-only baseline audit; incomplete certification; Event 021 remains Needs Testing and this report is not final acceptance.

Scope: Event 021 Random Civil War, root chaosx.nr21.1, with SCN-018 The Fracture Cascade as the user-identified manual scenario. The audit covers current weighted timing, target selection, scenario selection and Maximum behavior, option and decision AI scores, mission AI scores, strange-incident selection, related random-list routing, AI strategy factors, and only the Event 004/007 shared interactions explicitly declared in the accepted Event 021 matrix.

No gameplay source was changed. The only authorized write is this handoff.

## Executive findings

- The parent supplied fresh exact declared-pool projections for two isolated parent-effect random lists. The six-entry archetype pool is exactly 1/6 per route when all six supplied weights are 80, 1/5 among the five survivors when the Event006 route is zero, and 100% ideological when it is the sole positive-weight candidate. The two-entry strange-incident pool was evaluated at the supplied 0.08/0.92 constants. These are conditional local pool results, not campaign incidence or event-firing probabilities.
- This audit independently confirmed both parent-effect candidate pools are complete for the cited entry ranges, with all required weight inputs present and unresolved=0. It did not independently reproduce the parent evaluations: the parent analysis IDs are not cached in this MCP process, the parent did not provide analysis artifact URIs or the strange-incident output rows, and probability_render returned PROBABILITY_ANALYSIS_NOT_CACHED.
- Event 021’s root event is triggered-only and has no local automatic MTTH. Automatic first-fire timing is controlled by the shared scheduler and event-pool path, whose complete live candidate pool, campaign bindings, external factors, and timer state were not available to the probability adapter. Campaign-level incidence and timing are unresolved.
- The target score is clamped and route-gated in source, but neither the complete live candidate pool nor its campaign-specific weights and shared load tickets could be inspected as a modelable pool. SCN-018 low/medium/high selection remains unresolved. Maximum is a deterministic all-eligible snapshot/freeze/commit path, not a weighted probability claim; campaign and performance acceptance remain unverified.
- Decision and mission AI surfaces are score races, not click probabilities. MCP confirms score-only semantics and exposes incomplete pools; no actor/scope fixture was supplied for a useful score trace, validity ranking, sweep, or rank-reversal analysis.
- A source integrity concern remains in recurrence timing: the review path requires earliest and latest recurrence dates, while the searched Event 021 common/events sources show a review-date assignment but no setter for those two required window variables. This is a source finding, not an MCP probability result; external assignment outside the searched paths is not excluded.
- The matrix scenario IDs are not certified. Parent fixtures were not mapped to matrix IDs, and the supplied scenario matrix lacks the actor tags, scope fixtures, campaign-variable bindings, candidate pools, and external-state values needed to bind its scenarios to the live adapter contract.

## Evidence provenance and current-source identity

The parent identified its current parent-effects local SHA-256 as 57DB1DFCDAD699482F9B3313E58A7A0FF87A14DBF00EDC7B0CA35CABFD90A781, matching MCP normalized sourceHash 774b917960c934d7cf9a8749449f70bddf154e74d3a953bee4f304c0458affec.

The independent inspections in this process saw the same normalized parent-effects sourceHash. The independent inspect sourceRevision was 1dd26d2bf27d1588e6265f1873c06a2c56da646ef364ced71ba42ee04e5206d. The parent’s evaluation sourceRevision was c50434ef2cb9a0f8ff3721d3dbe1e80e1a442a287d28e3ef031158c90e06e2be. These are distinct inspection/evaluation revisions for the same reported sourceHash; the parent’s analysis results are retained as parent-provided evidence.

Local raw SHA-256 values recorded for the audited sources:

- events/021_random_civil_war.txt — 0480E9EBB1FA78096A081A0B597AE8B1072B149D66C9990C5B32B1433D59685E
- common/scripted_effects/021_random_civil_war_parent_effects.txt — 57DB1DFCDAD699482F9B3313E58A7A0FF87A14DBF00EDC7B0CA35CABFD90A781
- common/scripted_triggers/021_random_civil_war_parent_triggers.txt — E409AE73BFA330A8B5A8A1739E27262CD0B561286CA9D51FC24FE92C7CBED2F5
- common/scripted_effects/021_random_civil_war_effects.txt — EBE72F40A94B0515A4F72D80A621BFFB2DBE0A33EA61B94769D30BB16775F68E
- common/scripted_triggers/021_random_civil_war_triggers.txt — B156B8FE56F6683035B76E96859198570A7FA0426C98368D37D07F000D078FA0
- common/scripted_effects/021_random_civil_war_decision_effects.txt — 3CB2E7C1214A6FCDCC4ED901F041D0FBDB05B8C853A2CA93AE92DA90E9DF8917
- common/decisions/021_random_civil_war_decisions.txt — DF61FCD80276C56FD2DB984921F92FEA9F85DBFF97938881BD4584503E322BA8
- common/mtth/021_random_civil_war_mtth.txt — 6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F
- common/script_constants/021_random_civil_war_constants.txt — 37DDEF2A1D2589B8B13F287A3781113AB6551759744A173772A2C1D9439B69AC
- common/ai_strategy/021_random_civil_war_ai_strategy.txt — 6ADBB93B2CD17665C4BD967368F08BC953738D81DB7A2069171241F45C309DCA
- common/scripted_effects/individual_crisis_targeting_effects.txt — 903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16
- common/scripted_triggers/individual_crisis_targeting_triggers.txt — AF537F93E969948CA5CB35E1D06C504F6797CCBAAF659A13C9A661DB8E510B70
- common/script_constants/individual_crisis_targeting_constants.txt — 8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002
- common/scripted_effects/chaosx_settings_effects.txt — A14DDE66F54D3740E6DF7F461E4B414CFC13AD5F80C3B3EAFE5B6B9055E9BC87
- common/on_actions/chaosx_on_actions_chaos_meter.txt — A9182B0040FE07D8166F0CA822C750EAC206734C9133D3A82F99FDA6553F95FA
- common/scripted_effects/chaosx_event_cluster_effects.txt — A24C14B44E04DE96B577ABEC867228231653FA5FCC5D79CBD891AED63DD18474
- common/script_constants/event_cluster_constants.txt — 0754C6FA517B0D65D6F2FB547D4334899F346E587EE366C5C40436865CF45CCF
- common/scripted_effects/004_random_war_effects.txt — 1527C5E02297FDC6F115FC4B70FDBC9A9E1443FABEDA8FD6590E1C6439C62BBD
- common/scripted_effects/007_fury_effects.txt — 73B18883E67B12564F30360A7BC0599BC5E9BC7C6718D2B4417CC12FCB3802C1
- events/004_random_war.txt — E9B3496B334F2194CEB024CE56BFB434D43D4031C219C7DB729F93E7C252BBA9
- events/007_fury.txt — 7A5B762DC546C58B9CEB2EE41E9AE0D877C10D41E42E8CE41F519F2F3D5CA27F

These hashes identify the inspected workspace state; they do not imply source acceptance.

During the audit, a fresh on-disk hash pass found four shared files had changed relative to the earlier captured snapshot. I did not edit them. Their current diffs add a separate Equipment from Heavens daily pulse/prefire path and a separate Various Anomalies cluster/member definition; the diff does not alter the Event021-specific branch in the settings dispatcher or the Event021 scheduler call. The new cluster is registered in shared cluster arrays, so any effect on the global cluster candidate context is an unmodeled external factor; it is outside the accepted Event004/007 overlap scope and was not expanded into an audit of Event042/047. The affected current files were re-inspected with the probability adapter where applicable, and the hashes above reflect the final visible workspace state. This drift is retained as provenance uncertainty about when the pre-existing workspace edits landed.

## Exact parent-provided local pool projections

### Archetype random-list pool

Surface: common/scripted_effects/021_random_civil_war_parent_effects.txt entries 1155.entry.1 through 1155.entry.6.

Parent inspect: adapter random_list; poolComplete=true; candidate count 6; requiredInputs 6; unresolved 0; inspect revision caabcabe9d94e2b88ffdd814a731f5e11bd322c54537554329ec30764586d4b5.

Independent inspect: adapter random_list on the same exact six-entry pool; poolComplete=true; six required weight inputs; unresolved 0; normalized sourceHash 774b917960c934d7cf9a8749449f70bddf154e74d3a953bee4f304c0458affec; sourceRevision 1dd26d2bf27d1588e6265f1873c06a2c56da646ef364ced71ba42ee04e5206d. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c8b61fd414661d7da1c9ab3c7da1d5820903201e004f55553bb4966f04ff945/3d5c273cb68aa92bfb44ed246963fbd9500b3bb927de5deb28cf5bae4edf5c25/probability-inspect-774b917960c9.json.

The six candidate inputs map in entry order to ideological, legal, regional, Event006, command, and same-tag archetype weights. Parent evaluation analysisId probability-6d5fc2783def91e687bce541; scenario hash e010fa18761d3c3044019e4c9a24f3249e047f362269102e1caa72fe40131ef4; evaluation sourceRevision c50434ef2cb9a0f8ff3721d3dbe1e80e1a442a287d28e3ef031158c90e06e2be; complete with 18 scenario-candidate rows and unresolved=0.

| Parent fixture label | Supplied weights | Exact normalized local result | Classification |
| --- | --- | --- | --- |
| all-valid | Six weights are 80 | 1/6 each | Exact declared-pool projection |
| no-Event006 | Five weights are 80 and Event006 is 0 | Event006 0; each other entry 1/5 | Exact declared-pool projection |
| ideological-only | Ideological is 80 and the other five are 0 | Ideological 1; other entries 0 | Exact declared-pool projection |

The warnings reported by the parent were the deliberate zero-weight route and single-survivor fixtures. These fixture labels have no supplied scenario IDs and were not mapped to ARC or another matrix ID. They establish only normalized outcomes for the declared six-entry pool under the listed supplied weights. They do not certify route eligibility, campaign archetype incidence, or automatic event frequency.

### Strange-incident random-list pool

Surface: common/scripted_effects/021_random_civil_war_parent_effects.txt entries 6969.entry.1 and 6969.entry.2.

Independent inspect: adapter random_list; poolComplete=true; two candidates; required inputs are event021_parent_strange_incident_weight and event021_parent_no_strange_incident_weight; unresolved 0; normalized sourceHash 774b917960c934d7cf9a8749449f70bddf154e74d3a953bee4f304c0458affec; sourceRevision 1dd26d2bf27d1588e6265f1873c06a2c56da646ef364ced71ba42ee04e5206d. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e528d529284e2d8e7d0ec45e564a654a9744e483cd29a132d1e244eca95bc2bb/37c2f014624710483cbdf00f410556205803969ec98dd3aa3f4b46a2e97d3aff/probability-inspect-774b917960c9.json.

Parent conditional evaluation: constants 0.08 and 0.92; analysisId probability-ce806f542ade7bf6ca697dd8; scenario hash 721f080b92267db681ef6189e125bae78c5a3986c4696666019f8ca6b3d2efed; two candidates; unresolved 0; sourceHash 774b917960c934d7cf9a8749449f70bddf154e74d3a953bee4f304c0458affec. Numeric output rows and the evaluation artifact URI were not supplied. The parent did not provide a scenario ID.

Classification: exact conditional two-entry pool evaluation as reported by the parent, but not independently reproducible in this process. The incident is additionally gated by Evolution II, log and actor state, and the recent-incident cooldown; the 30-day cooldown changes the number of eligible rolls. Campaign-level incident probability, recurrence frequency, and cumulative incidence are unresolved.

## Surface-by-surface audit

### Automatic Event 021 timing and scheduler

Source: events/021_random_civil_war.txt root chaosx.nr21.1; common/scripted_effects/chaosx_settings_effects.txt; common/on_actions/chaosx_on_actions_chaos_meter.txt; common/scripted_effects/021_random_civil_war_parent_effects.txt.

The root is hidden and is_triggered_only=yes. It contains no standard automatic MTTH block. The daily global scheduler has a once-per-day guard, bounded registered-country review cursor, evolution processing, and a critical queue; it does not itself define a standalone first-fire probability. The shared settings dispatcher calls the Event021 prefire path and may reset the timer when no target is found.

Independent probability_inspect on events/021_random_civil_war.txt with event_mean_time_to_happen found zero MTTH candidates and suggested event_option_ai_chance because it found 11 option blocks in the file. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/567a3204b0684f14889ac5c9b4aa96d03d8a13cd2a2da4ae17e390d6ec72f186/3869dec4ee817967abb90a34103309d5d21d9e9f4e2cb1e64cd41eb869e43648/probability-inspect-d8275e2107ff.json. Normalized sourceHash d8275e2107ffde3195eb3d451fc839c7fe0b99ce2018d9aeb2321ccd21572b61; sourceRevision 03e6a85092c111b5010d1384baec9c389ad22f480b98c832571da2d9b4169d12.

Inspection of the shared dispatcher found no exposed complete Event021 pool. The custom_weighted_pool adapter on chaosx_settings_effects.txt returned zero candidates in the earlier pass; after the shared source hash drift, refreshed event_mean_time_to_happen and custom_weighted_pool inspections again found zero candidates, with poolComplete=false for the custom-pool adapter. Current sourceHash and sourceRevision values, plus artifact URIs, are recorded below. On the Event021 parent effects the custom-pool adapter failed twice with INTERNAL_ERROR and produced no artifact. The adapter could not expose the scheduler’s full target/event pool, timer state, or campaign bindings.

Classification: unresolved campaign timing and incidence. No exact or bounded firing interval is established by this audit. A trigger-only event’s local singleton option weight must not be mistaken for automatic firing likelihood.

### Target pool and target scoring

Sources: common/scripted_effects/021_random_civil_war_effects.txt, common/scripted_triggers/021_random_civil_war_triggers.txt, common/scripted_effects/021_random_civil_war_parent_effects.txt, common/scripted_triggers/021_random_civil_war_parent_triggers.txt, common/scripted_effects/individual_crisis_targeting_effects.txt, common/scripted_triggers/individual_crisis_targeting_triggers.txt, and their Event021/individual-targeting constants.

The source-side target score has base 10, fracture pressure times 4, authority failure/collapse bonuses 90/160, valid-route bonus 80, major-stage bonus 50, nearby exposure 60, recent-memory penalty -120, subject bonus 20, and player bonus 25. Major-target factor is 0.35; reserved candidates are set to zero; the result is clamped to 0–1000, rounded, and added only when positive. Parent opening gates also require a normal human, individual crisis below cap, no terminal/grace/incompatible/active/reservation state, generation permission, a valid opposition route, and global capacity.

The parent target path divides eligible target score by target_pool_weight_scale, rounds and clamps the contribution to 1–10, then applies shared individual-crisis load tickets: cap 3; load 0 contributes four tickets, load 1 two, and load 2 one. It draws without replacement and freezes a selected set before preflight and commit. These source-defined rules give bounded mechanics but not scenario probability: actual candidate scores, eligibility, reservation state, common-pool competition, and ticket arrays were not supplied to MCP.

Independent custom_weighted_pool inspect of the core Event021 effects returned poolComplete=false, zero candidates, and no required inputs (sourceHash 0401a6e0c32ef50370b012f9b419faccdbd521768bd6079029e9286c9ca2f156; sourceRevision 5d1e0c9a70df21aa50f95d375bd2fa0869f6f09e351faaf82892b1dd3b20b417). Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/508d7698559875198ea578394315f9c6b211250aa31f8bd92885d2e0bb876d83/10ec67d167351b226ca13afd390265f97c6ba77d2af26ca3865d44f59fc29d8d/probability-inspect-0401a6e0c32e.json. The same adapter on the parent effects produced two INTERNAL_ERROR results.

Classification: bounded source mechanics; unresolved scenario-specific pool completeness, relative target odds, invalid/dead target mass, target rank reversals, and campaign selection probability. No probability was calculated from source constants alone.

### Scenario selection and Maximum

Named manual scenario: SCN-018 The Fracture Cascade, supplied by the user. The probability matrix separately declares SCN-01 through SCN-07. Part 8 of the weighted spec still says the scenario identifier was not locked and suggests SCN-014; this documentation conflicts with the user’s current SCN-018 instruction. No document was changed.

Source behavior: target-share constants are low 0.10, medium 0.25, high 0.50. Scenario candidate target weights are low minor/major 4/1, medium 2/2, and high 1/3, then shared crisis-load tickets apply. Selection is without replacement; selected candidates are frozen, preflighted, and only valid frozen plans are committed. There is no reroll after preflight failure.

Maximum bypasses weighted drawing and selects all preflight-eligible normal human countries at confirmation, excluding nonhuman countries; the same-tag path is one-state. It is a deterministic all-eligible snapshot/freeze/commit policy, not an exact probability distribution. A live campaign/performance acceptance trace is absent.

Classification: bounded source behavior; all named campaign scenarios unresolved for actual pool membership, ratios, rank reversal, target omission, and post-preflight attrition. Maximum has no weighted probability claim and remains unverified for runtime/performance and acceptance.

### Evolution cadence and stage timing

Sources: common/mtth/021_random_civil_war_mtth.txt, common/scripted_effects/021_random_civil_war_parent_effects.txt, common/script_constants/021_random_civil_war_constants.txt.

The custom entries random_civil_war_evolution_i_days, random_civil_war_evolution_ii_days, and random_civil_war_evolution_iii_days are sampled once per stage, then clamped to 60–180 days and stored as due dates. This is not a standard event MTTH block sampled daily. Base values are 90, 135, and 120 days. Source modifier factors include authority fail 0.75, large country 0.85, extra actor 0.75, multifront 0.85, border 0.75, sponsor 0.75, Event006 front 0.80, severe war 0.80, near defeat 1.50, settlement phase 1.40, no extra actor 1.35, strong neighbor 1.25, and no exposure 1.25.

Independent event_mean_time_to_happen inspection of common/mtth/021_random_civil_war_mtth.txt found zero candidates (sourceHash c55a108bcbf249ce1d76875506cd0fe4b8c8db79646c426b503ba036d72405b8; sourceRevision ce86b3c585a6805954346e4f236e67331fcc4c3b11ed1f3fcb1dd33f61445fbd). Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0e04c9b04cc1441e4898c6011114ada014cc079b5550b45e4339f970c11cafa/6999c2d8b45f85be65d334c40d67d88134943b398f9b71fc9fb029071d02645f/probability-inspect-c55a108bcbf2.json. Inspection of the parent effects likewise found no standard MTTH entries and suggested the random_list adapter (sourceHash 774b917960c934d7cf9a8749449f70bddf154e74d3a953bee4f304c0458affec; sourceRevision 42b8e83a0cfd326794e0c8456b086e2e99e53430d41fa4ef7bf0e91d6edd5f40); artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c67097b4a8bd60a20090f6abde05cac89a3d87bb06caf5f74c9ea7b34dc81860/c0e4627e33f5658b9f0b7f8139fa24d3a3908f652ba03c25a835c9378040128e/probability-inspect-774b917960c9.json.

The shared dispatcher was refreshed after the workspace hash drift. On common/scripted_effects/chaosx_settings_effects.txt, event_mean_time_to_happen found zero candidates (sourceHash 8fdbff918d1496fe202f506fa1683ec4a05eb366d34b5e3f5d5071c2cead7c9f; sourceRevision 3cc3deb859e3b5cec4cd3bc0556ef7228318f51289fc492c94fe058d00a71bd8; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aa3b44afa47e399be04ae7934ae0af8e02e86086990261be092caee954a5e21/f20bba4b86c0aed6e27920dd481ad68f40fd80bf935ec3664733309ecbd1b0ed/probability-inspect-8fdbff918d14.json). custom_weighted_pool likewise found zero candidates, poolComplete=false, no required inputs and unresolved=0 (same sourceHash; sourceRevision 94c042eab9581f786923897ca1ab439b5280ddfbb7ea08bb3dd5a4303fac6fef; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7b9550183871261c84a2c2cea41d2571f3c33f64acff132c9bc1ac854bb43bb/f0dea2f7aca4b86ee134ecb7e5d6717fca433c545c186d9d4fed1deec76906df/probability-inspect-8fdbff918d14.json). The daily on-action source also exposed no MTTH candidates (sourceHash 1b5eb376118b3193db73ba6979944fa171493811d85792811d90ebb5322ba2d6; sourceRevision ff1a2d7f5977c42cc307ca720dc9f8d5708b0a6466494f4dd370f7c9c5e44459; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da7c7d0bda6e13659d84ec798a80d300e6e9ebee4dea8d109c1a8cac08526759/6bcb88be834112061f2a0f19c50166d359e532d34d0cd10310a2812f95df53fe/probability-inspect-1b5eb376118b.json). These adapter inventories confirm the shared dispatch/tick files do not expose a complete Event021 first-fire pool or local MTTH.

Exact modifier traces and due-date distributions were not evaluated because the adapter does not model these custom mtth entries and no actor/scope/state bindings were supplied. Actor selection source takes the first valid active-front side in array order; it is not a randomized actor pool, and no evidence was supplied to test array-order rank effects.

Classification: bounded source timing rules; unresolved effective timing distributions, matrix timing scenarios, actor-order consequences, and repetition behavior.

### Severity and front count

Source uses deterministic threshold and route-capacity logic for severity and side count; planned fronts are capped at five. No separate random_list was found for severity choice.

Classification: score/probability not applicable to the deterministic branch itself; scenario outcomes for SEV-01 through SEV-06 and FRT-01 through FRT-05 remain unresolved because the matrix cases were not bound to campaign values, route capacities, and target pools.

### Event-option ai_chance

The broad inspect of events/021_random_civil_war.txt found 11 option blocks across multiple independent categorical pools and marked the combined pool incomplete; it must not be normalized as one choice race. SourceHash d8275e2107ffde3195eb3d451fc839c7fe0b99ce2018d9aeb2321ccd21572b61; sourceRevision 6a3f1c3e93f6fe6e0700befe557ebbe5b1b570afb88aae4458ffaf82310e88c4. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11bbe7bb7c32da38754e7f5f87df947b9d8c8b4be695b641a1622fac38cda4b3/5d79cf2575a3ab0447846b5fb42a845ad9a1b2c7469de4646678208f80878532/probability-inspect-d8275e2107ff.json.

Seven actual ai_chance options were independently inspected as singleton local pools: events 2, 3, 4, 6, 7, 8 option a, and event 17 option chaosx.nr21.1.skip. Each has base 100 and is the only option in its own event; each singleton inspect was complete with zero required inputs and unresolved=0. The shared normalized sourceHash is d8275e2107ffde3195eb3d451fc839c7fe0b99ce2018d9aeb2321ccd21572b61; singleton inspect sourceRevision is e6bcfcbd874d481bce260e355a5da8e866ed2a97aff7f9f828bf106854b5f732. Artifact URIs: event 2 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d784e0cd3085778afe16e0d6c67ccf581d1c35528de93a9eb033baf09c2168cd/39e0e4d136bf1824a590a605aafea42edc493e79f2392ea3b58e02c6f7e852cf/probability-inspect-d8275e2107ff.json; event 3 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/772ed52a5ac354d687d8efffabeebe350fec12fb33fd37fcecde59f19145c868/302c6ab3bba3a8df4e316d3e09791eaf30cf43aa07ba0d4e00eb8636c2120463/probability-inspect-d8275e2107ff.json; event 4 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2e7c64ef740a059927b6249f128090dcc7da2f642ae15d9c5cb91edf58ed53a/553ee69cebf24c5bbeffc4a5f93e306a234b7b3dd154351bc5ca94bc1e507205/probability-inspect-d8275e2107ff.json; event 6 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed308b29022ed6c1fa4e33283fa1eb7956105ac532d6a373834f4d2c9709bbe7/82c6d9cf12795299c8ed5908147ec6222ccb3669c12459270fb55858f844d722/probability-inspect-d8275e2107ff.json; event 7 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f63bd6b4873f5c5d4519565632f1541b11c6f9977c4f5205c9b1b325336fcc1c/a0c9da201ac8c892bdf9143bf32aedf645723a3bcaafef17bb2231890c636b09/probability-inspect-d8275e2107ff.json; event 8 option a — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3799d47c6deeb9c3130acdb32d0dbe89ae7da8fe07e21465a793e854c2b286f4/b9c303111d6ed3289d0a269af440ca2844574e7ba04614731d84ea683217be06/probability-inspect-d8275e2107ff.json; event 17 option chaosx.nr21.1.skip — hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9706fae78a828faed73ba922e2eccbd5c1f6059469c7b11b4b03bbe82a93c44d/b816ffc7b1af5345aac758d7c0658644aebd8b463162fb9957c8c8d12c126a2f/probability-inspect-d8275e2107ff.json. Because these are separate events, the singleton score is not an automatic event-firing probability and does not compare outcomes across the campaign.

Classification: exact singleton local option score structure; unresolved multi-option preference, actual actor-specific score traces, and any campaign frequency. The other discovered option blocks were not combined into a false normalized pool.

### Decision AI and mission AI

Decision source: common/decisions/021_random_civil_war_decisions.txt. The decision_ai_will_do adapter found 18 candidates, poolComplete=false, available=0 in the empty/default inspection, 12 required inputs, unresolved=0. Adapter contract is rawScore=true, normalizedProbability=false, selectionRule=score_only, and complete pool not required. SourceHash 2e3a02e6a44b5cec62f035f404df0f56443dfe01136c6b3d9b26c21b085acc6a; sourceRevision 3bc4afa2a4093f718320526f37b67b92ecd6047195fd224520751b6084f904c0. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cce738f2afb96db9b27336fc0d346083cb73dee7ec23fe52a7f484938346c0b/7b93ef044e86caff38fb77c31f0a7bbf08089d17276a1bb72e962e786abef74c/probability-inspect-2e3a02e6a44b.json.

The 18 candidates are event021_complete_coalition_governance, event021_complete_disarmament, event021_defend_capital, event021_end_sponsor_commitment, event021_integrate_formations, event021_monitor_border, event021_offer_emergency_settlement, event021_offer_mediation, event021_open_relief_corridor, event021_protect_communications, event021_reconstruct_administration, event021_review_loyalty, event021_review_regional_administration, event021_secure_arsenals, event021_seize_depot, event021_set_priority_front, event021_support_government, and event021_support_opposition.

Required input constructs include capital_scope, check_variable, command_power, custom_trigger_tooltip, has_equipment, has_political_power, has_variable, has_war, hidden_trigger, surrender_progress, and the variables random_civil_war_exposure_source_country_scope and random_civil_war_priority_front_state. Source base values include action 1, priority_major 1.5, and discourage_concession/discourage_repression 0.75; role and purpose modifiers plus explicit zero factors govern eligibility and resources. Without actual actor, role, targets, hidden-trigger state, and resources, no trace is supportable.

Mission source is in the same normalized sourceHash. mission_ai_will_do inspection found three candidates, poolComplete=false, available=0, three required inputs, unresolved=0; it is also score-only, raw score, not normalized probability. SourceRevision 8e75f6ba0c85a49326aa8c16e80e9397daf9dcd4999b82304b65ba0e55b65e28. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ffaea68406b6f3098421549112007e1a4e372d419516c84f7562dfb1e8699bf/9a662d560064f79c1b07c96de3579df1733bf5a0a6022f956a37da3f629fe788/probability-inspect-2e3a02e6a44b.json. Missions: event021_hold_the_capital_mission, event021_secure_rail_spine_mission, event021_hold_settlement_terms_mission. Base and typical role/stage factors include 1 and 1.5. The rail mission requires random_civil_war_rail_mission_state; other inputs include custom_trigger_tooltip and has_variable.

Classification: score-only structural evidence. No AI score traces, rank, starvation, or rank-reversal result is certified. Do not describe an AI score as a click probability.

### AI strategy factors

Source: common/ai_strategy/021_random_civil_war_ai_strategy.txt. probability_inspect with ai_strategy_factor discovered zero candidates; sourceHash 74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9; sourceRevision 8cdecfc1b9069897d27a9d5ddb54b3c48b39c76f3a1c54fc5f6a8aa0bbda3140. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7283f1530b046381d7f271774d23c05ccef33a748d7cbb4736024864b5588e6/77e6e5aa1e8c686664ae3b0f738b7aa20dff2d52e64d30ead607cd6a1907bcb7/probability-inspect-74d73084d977.json.

Source review found 12 role profiles, with build_army factors ranging 65–135, equipment/infrastructure factors 35–95, and avoid-start-wars values -50 to 150. The adapter does not recognize these ai_strategy blocks, so their impact on the Event021 AI score races is not certified.

Classification: unresolved adapter coverage and effective AI-strategy impact.

### Recurrence timing and cooldown

Source review found event021_prepare_recurrence sets a recurrence score and writes random_civil_war_recurrence_review_date to global.date plus random_civil_war_timing.recurrence_minimum_days (60). The recurrence review and trigger require random_civil_war_recurrence_earliest_date and random_civil_war_recurrence_latest_date and require the current date to fall within that window. A search across common and events found checks/reads/clears but no assignment of either required window variable. The maximum timing constant is 180 but does not itself initialize the latest date.

Classification: unresolved recurrence eligibility/timing, with a source integrity warning. The search does not rule out assignment from a runtime path outside the searched common/events files. Recommended review: identify the intended owner and initialize both bounds consistently before treating recurrence scenarios as valid.

### Event 004/007 shared cluster interactions

Scope is limited to the overlap declared by the Event021 matrix. Shared source: common/scripted_effects/chaosx_event_cluster_effects.txt and common/script_constants/event_cluster_constants.txt. Event004 is a required cluster member; Event007 and Event021 are optional members.

The source defines tier-based cluster activation chances, severity/count/fatigue/participation multipliers, trigger multiplicity bonus, and a 1–90 clamp. Optional member participation uses a base chance, eligible-count factor, and 0.95 decay, then integer rounding and a 1–100 clamp. Optional entries are ordered with random bias and independently roll integer 1–100; successful optional entries increase the optional decay. These are source observations only; no hand-derived exact probabilities are claimed.

The cluster source was refreshed against its current on-disk contents. custom_weighted_pool found zero candidates, poolComplete=false, no required inputs and unresolved=0; sourceHash 998526f08f3672feeba7730c311cd22e84823eaabe26e7fd1e76a9340251d6b1; sourceRevision b47eb07f861dd67fc79c2bb69eddec47fea5bb111ab6b903d11fe9888b5c1e8c; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d89ff82d07e79c8d9ee1834b589042faddec043860dc03d03a4c757c532db53/c57d14c7476d4e49bf26bf46c3c625d304a0ad7a24605f696c35b5057703c808/probability-inspect-998526f08f36.json. random_list also found zero candidates, sourceRevision 94c042eab9581f786923897ca1ab439b5280ddfbb7ea08bb3dd5a4303fac6fef; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca90b359a1b6983763c0611631393b7841b9460ce2b7e4487280035611111e97/748ef1b0809a98f3cd484f8ca7b50a94a77ad46f64775e5c3f22c0a1e7e84a8f/probability-inspect-998526f08f36.json. direct_random reported no weighted surfaces, sourceRevision 8aef774b4f22a5039b7a51a2070a2f9812a401e74bb324a50a07ac4c5a33c729; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ff9b3cd8672fecb59c132684896b5878b0bd86c0810d7886665414904b08894/9d41bcd8da86b98ce1ec37771ee4e5513742f09af3f4473e5731226a19106bbf/probability-inspect-998526f08f36.json.

Event004 selection source inspections also discovered no pool candidates. Its normalized sourceHash was f94e186994d01eeb51b5e9e8ab05a55c13366b39f3b35b8df8e76189de0b24f1; custom-pool sourceRevision 537ae17252befc5676644d2dea25ab3dbd7fedd912e3da8b16373caa724e49dd. Artifacts: custom pool hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50e6774ff6112e0ffd9ad59fda7ebd4674118675f4adc232ce4aea860c337bc7/b45f4cde96a779ae62f145bf98726054946bfb975a5dfbe76780adaeff9a1261/probability-inspect-f94e186994d0.json; random list hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/110d36bf0c0fdb6c42c887114ff0bb27058d4ba76c1155467152743a6924cc17/56b43c1ae9da322fba4f3913c9822af86ac41e1c6f21b20e8e14ef931e396bed/probability-inspect-f94e186994d0.json; direct random hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2961d4c96fef9bdea523a53e4e098ce1fe6da103467f670081007592140b1c8c/addd6ae3a5772f29ae04e1e3f459b8153ccc7137b9c4e1be54a6fbb13b8e27cf/probability-inspect-f94e186994d0.json.

Event007 selection source inspections discovered no pool candidates. Normalized sourceHash f359bcca8f552080d974d616e2937b90d5a7e2c34d5928e162ec00a1da3bba08. Artifacts: custom pool hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6138777db2ebb93259f055c01ca9ba85c8d2ce2eaaa70f906403ef4049e5ac91/b8bf09db29f29a6a4fe01bd58fe2d0aac32ed61fb2e042bff3de560dd1f86c98/probability-inspect-f359bcca8f55.json; random list hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1322c34cc911cf6ba3bba8de13e505f594a20a6c00dfd565ee92deb9fd7e685/fb0425a1b2bdc35d85dfc828ab925b8828d18058f70a9eab9e9132a7b1c357bc/probability-inspect-f359bcca8f55.json; direct random hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f5e75644e8d6f265694bd1fb2a4f5d9ecf6570e5d39b831088eca802e2af9ca/330327292083d5b8a868bd0f63f1df4d2c78d33fd8b2ba32ef0a361753f8896e/probability-inspect-f359bcca8f55.json.

The adapter exposes no manifest schema or discovered pool for the custom cluster rolls; no pool manifest, eligible target arrays, or scenario-bound external values were supplied. Thus CLU-01 through CLU-05 remain unresolved, including calm target diversity, intentional Event004/Event021 overlap, Fury actor exclusion, Event006 tag reservation, and no-target skip behavior.

Classification: bounded source structure; unresolved exact/bounded/sampled cluster odds and each matrix case.

## Matrix scenario coverage

The matrix file is docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md. Its declared IDs are recorded below. Unless explicitly called out as a local parent fixture above, no matrix ID had a complete live adapter scenario with actor tag, state variables, flags, scopes, pool membership, campaign bindings, and external factors. Therefore none of these IDs is certified by this audit.

| Surface family | Scenario IDs | Audit status |
| --- | --- | --- |
| Targeting | TGT-01 through TGT-10 | Unresolved: no complete live target pool or actor/campaign bindings |
| Archetype selection | ARC-01 through ARC-08 | Unresolved at matrix-scenario level; parent’s all-valid, no-Event006, and ideological-only fixtures are exact local pool projections but are not mapped to these IDs |
| Severity | SEV-01 through SEV-06 | Unresolved scenario outcomes; source branch is deterministic |
| Front count | FRT-01 through FRT-05 | Unresolved: no capacity/route/candidate fixture |
| Spawn behavior | SPN-01 through SPN-05 | Unresolved: no complete spawn candidate/route state |
| Strategy behavior | STR-01 through STR-05 | Unresolved: strategy adapter does not recognize source blocks and no role fixture was supplied |
| Settings | SET-01 through SET-06 | Unresolved: shared dispatcher and complete timer/campaign pool not exposed |
| Recovery | REC-01 through REC-06 | Unresolved: recovery state transitions and complete campaign bindings absent |
| Global behavior | GLB-01 through GLB-07 | Unresolved: no complete global scheduler/capacity fixture |
| Shared cluster | CLU-01 through CLU-05 | Unresolved: custom cluster pool/manifest and cross-event candidate arrays unavailable |
| Evolution I | EVO1-01 and EVO1-02 | Unresolved: custom MTTH adapter gap and no runtime scopes |
| Evolution II | EVO2-01 and EVO2-02 | Unresolved; strange incident has a separate exact conditional two-entry pool report, not mapped to either ID |
| Evolution III | EVO3-01 and EVO3-02 | Unresolved: custom MTTH adapter gap and no runtime scopes |
| Manual scenario | SCN-018 The Fracture Cascade | User-named current manual scenario; unresolved campaign selection and Maximum acceptance |

The weighted Event021 spec Part 8 still mentions SCN-014 and says its identifier is not locked. This is stale relative to the explicit current SCN-018 instruction and should be reconciled by the spec owner; no edit was made during this audit.

## Weighted surfaces not certified

- Automatic Event021 first-fire timing and campaign incidence through the shared scheduler/global pool.
- Complete target candidate pool, candidate validity, target ranking, common target competition, crisis-load ticket effects, and target-rank reversals.
- SCN-018 low/medium/high candidate distributions and all seven matrix scenario IDs SCN-01 through SCN-07; Maximum’s deterministic campaign snapshot, capacity, and performance acceptance.
- Effective Evolution I/II/III due-date distributions, modifier traces, first-valid actor ordering consequences, stage starvation, repetition, and timing rank reversals.
- Matrix scenario outcomes for TGT-01..10, ARC-01..08, SEV-01..06, FRT-01..05, SPN-01..05, STR-01..05, SET-01..06, REC-01..06, GLB-01..07, EVO1-01/02, EVO2-01/02, EVO3-01/02, and CLU-01..05. The matrix coverage table retains the family-specific missing inputs.
- Multi-option Event021 ai_chance competition, any campaign frequency implied by the seven singleton option scores, and actor-bound option score traces.
- Actor/role/resource/target-bound decision and mission AI score races, gates, rank reversal, starvation, and dominance.
- Effective Event021 ai_strategy factor impact on decision/mission scores and other role-dependent AI races.
- Campaign incidence and cumulative recurrence of the strange incident across its Evolution II gate and 30-day cooldown.
- Recurrence-window timing/eligibility pending the unexplained earliest/latest date assignments.
- Event004/Event007 shared cluster overlap outcomes for CLU-01..05. The current shared cluster pool route exposes no candidates and no accepted cluster manifest/candidate-array evidence was available.

For decisions and missions, MCP established only that the engine-facing adapter contract is score-only, not normalized probability. This audit found no scenario evidence proving a live choice is dominant, starved, or invalid, and no scenario evidence ruling those conditions out. The source does show route/resource zero-gates, bounded target scores, selection without replacement, and incident cooldown safeguards; their campaign-level effectiveness and exploit resistance remain unverified. Parent archetype fixtures demonstrate expected zero-weight elimination and deterministic single-survivor behavior only within their declared six-entry pool.

## MCP workflow, rendered evidence, and limitations

Weighted surfaces were started with probability_inspect. The available probability adapters used were event_mean_time_to_happen, event_option_ai_chance, random_list, custom_weighted_pool, decision_ai_will_do, mission_ai_will_do, ai_strategy_factor, and direct_random. Independent exact candidate-pool inspections and their evidence URIs are given above.

The parent’s probability-evaluate analyses were probability-6d5fc2783def91e687bce541 and probability-ce806f542ade7bf6ca697dd8. Attempts to render both in this process failed with PROBABILITY_ANALYSIS_NOT_CACHED, with the server message that render requires an analysis ID produced by this server process. No render artifact was produced for those analyses. This is a process-local cache limitation, not evidence that the parent evaluations are invalid.

No evaluate or sweep was run for target, timing, decision, mission, strategy, or cluster surfaces because there was no complete scenario fixture accepted by the live schema. No sequence was run because the required complete custom-pool manifest, cadence, transitions, cooldown/recovery, cap, removal/reset, and terminal states were not available. No simulate was run because uncertain-input distributions and seeds were not declared. No compare was run because this is a baseline audit with no before/after patch and no authorized candidate change.

Event structural MCP evidence was also collected as the event-related structural pass. event_inspect selected chaosx.nr21.1 and returned partial coverage: revision cc097d15c00f15159a92e4fc4de590cfe2b67224170be81d9d17e55e0c16c587; graphHash e4df4522cdd4460f8b3b9cc188e6ae4bcd45f20941f3a607e67d77b6cab4d019; no blockers or critical diagnostics in the selected partial projection. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e7b80b365b38277a1d37dbcfb6dc4b2c4d5e423465f34179842ac7c1531a303/7a39388cb25709c76e76eb491615fa53b5cd0e0691459d5875b092a8f16962d4/event-lint-cc097d15c00f.json.

event_render overview used the same revision and graphHash but is partial: layoutHash 3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8; selectedNodes 2; omittedNodes 42785. Artifacts: JSON hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8b1afb7ddcba366533c5e7352669d59a69367dc24e4d74743bbae3665024d3c/dd4d33df51a16e8748ab0288b38b7fe49d6ebe7e6a99bb267bc675ab27b1e51a/event-overview-cc097d15c00f.json; SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc80f2706fa8b48b1ace5a3c485c0eb1398907b1229fb42a702518faa8ca4b29/85b9d091a3b64d8173d72c943b328b4d9372f5f495d92f78dcbb0ad70ca31295/event-overview-cc097d15c00f.svg; PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df9d56536faf0e228de42ff326bd93de1b59d795d553de3057d803736bbf7572/e6f02842d0ff9eba0ba9dec06537b50f9c411f20a86106b0dd0d8b47979ccdd3/event-overview-cc097d15c00f.png. A manifest was returned, but its exact URI was not preserved in the audit capture and is intentionally not reconstructed. The view covers a very large workspace graph (9,824 events, 15,175 options, 1,166 entries, 8,858 unresolved nodes, 2,195 diagnostics, zero blockers); it was rendered before the shared-file hash refresh and is not Event021-specific or current-workspace certification.

## Risks and recommended follow-up

1. Supply complete scenarioSet fixtures using the confirmed live contract: top-level id and scenarios array; each scenario has id, actor as a string, state as a flat primitive-value map, flags as a string array, and scopes as a record whose entries contain id and state. The currently missing evidence is valid actor tags, state/variable bindings, flags, scope IDs and state, candidate target arrays, and external campaign values for the matrix cases. Do not invent fixture fields or campaign-variable bindings. Map each fixture to its matrix ID and declare external factors and scheduled state changes.
2. Obtain or add supported probability-adapter coverage for the Event021 shared scheduler, dynamic target pool/ticket draw, custom MTTH entries, and EventCluster custom rolls. Until then, keep the campaign-level conclusions unresolved; do not infer probabilities by normalizing source constants.
3. Reconcile SCN-018 The Fracture Cascade with the stale SCN-014 reference in the weighted Event021 spec.
4. Review recurrence initialization at event021_prepare_recurrence and the earliest/latest checks in event021_parent_review_recurrence_window. Establish where both bound variables are written and whether their min/max semantics match the intended recurrence window.
5. Run actor/role/resource/target-bound decision and mission score evaluations once valid scenarios exist. Report raw scores and score races, then sweep the declared modifiers for rank reversals and zero-gate/validity behavior; never report click probabilities.
6. Evaluate the complete low/medium/high scenario target pools and shared crisis-load tickets, including preflight attrition without reroll. Review Maximum separately as a deterministic snapshot path with live runtime/performance evidence, not a weighted race.
7. Evaluate strange-incident incidence across the Evolution II gate and 30-day cooldown in a complete campaign sequence once a full declared manifest and state transitions are available.
8. Review the twelve Event021 AI strategy role profiles with an adapter or scenario route that recognizes them, then compare their factor impacts against decision/mission score traces.

## Independent certification boundary

Parent diagnostics: the two parent probability-evaluate results and their claimed exact local projections are included as supplied. This process independently inspected the exact candidate pools and source identity but could not render or replay the parent analyses because their IDs were not cached here.

Independent evidence: current-source probability inspections and the partial event structural inspect/render artifacts listed above. No full current-source campaign evaluation, sweep, sequence, comparison, or Event021-specific complete event graph certificate was produced.

Accordingly, this is a read-only baseline and test-entry aid, not balance approval, final acceptance, or evidence that all matrix scenarios pass. All matrix scenario families listed above and the campaign-level weighted surfaces remain uncertified where marked unresolved.
