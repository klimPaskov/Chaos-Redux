# Event 012 Gods Response Phases Probability Audit

Status as of 2026-10-08: valid root-source comparisons ran for five host-policy scenarios and two host-answer scenarios, with unresolved eligibility throughout.
The continuation at the end records the current results and supersedes earlier deferred-comparison statements.
Complete AI conclusions remain unresolved because of scoped-trigger coverage, the empty victor-pool schema constraint and unfrozen helper dependencies.

This is a read-only, bounded audit of the 012 Gods response-phase weighted surfaces. No gameplay, AI, event, focus, decision, trigger, effect, constant, localisation, or runtime source was changed. No Git command or game launch was used.

## Audited surfaces and boundary

The three declared score-comparison pools are host policy representatives: gods_of_africa_prioritize_land, gods_of_africa_grant_leniency, and gods_of_africa_mark_offender; host pending answers: gods_of_africa_accept_substitute, gods_of_africa_reject_substitute, and gods_of_africa_accept_reconciliation; and participant preparations/entry: gods_of_africa_prepare_defensive_defiance, gods_of_africa_harden_stockpiles, gods_of_africa_secure_transport, gods_of_africa_prepare_countermeasures, and gods_of_africa_permanent_defiance.

The candidate source identifier for all three pools is common/decisions/012_africa_gods_decisions.txt. The 11-row inspect pool is complete for those named source definitions. The three smaller scenario pools are complete only for the declared micro-pools; they are not complete country decision races or denominators, and they do not support selection probabilities.

The parent-owned phase requirements are human host navigation bypassing AI, pending answers preempting discretionary views, targeted-row cache prewarming, participant preparation and defiance-entry gates during the ultimatum, and preservation of the separate paid-reconciliation and ultimatum clocks. Those are source-phase behavior claims. This probability handoff does not treat them as MCP probability evidence.

The Council phase is excluded as directed; the prior Council result is b0d53742e and was not retried.

## Frozen BEFORE source identity

The parent-provided BEFORE manifest is docs/plans/012_africa_plans/subagent_handoffs/012_gods_decision_phases_2026-10-07_evidence/before/manifest.json. All six snapshot copies matched their listed SHA-256 values when checked. The exact paths and hashes are recorded in evidence/source-identity.json.

The MCP inspect request bound the logical decision source to the frozen decision copy with path, snapshotPath, and expectedSourceHash. Its raw root hash was b39073b4370a8f7508ddc7902a6d9f4e5907942375313257fd063268a60fc6e8.

The shared live workspace changed while this audit was running. At the later hash capture, the decision, Gods trigger, Gods effect, and recovery-effect files no longer matched the six-file BEFORE manifest; constants and localisation still matched. These later hashes are recorded in source-identity.json and are not represented as an accepted or final AFTER state.

In particular, the live common/scripted_triggers/012_africa_gods_triggers.txt hash changed from the frozen BEFORE hash 5f8e6ff91f20ab804d6f6900120defee82a99f85ac04a734b8f5939e260e687b to 9db29e9384743ee26e476b69fb46e83ebe076e3475023917866de6f6dba2e2b2. The observed diff contains five insertions of the final-ultimatum-pending guard. The BEFORE helper copy used in this evidence is taken from the parent’s frozen six-file snapshot, not from that changed live file.

Transitive constants and scripted-trigger snapshots are under docs/plans/012_africa_plans/subagent_handoffs/012_gods_response_phases_probability_2026-10-07_evidence/dependencies_before/. Their source paths, snapshot paths, byte hashes, and live-hash comparisons are in dependency-snapshots.json. They include the AI constants, Africa action constants, contract, confirmation, victor, epoch-binding, recovery, contribution, and Africa host triggers.

## MCP and reference evidence

The first weighted-surface call was hoi4.probability_inspect on adapter decision_ai_will_do. It returned status ok, code PROBABILITY_SOURCE_INSPECTED, 11 candidates, candidatePoolComplete true, no unresolved parser items, and required input scope.FROM. The source revision was 71e101b011f7bef180428c6451a85f2559b4d39870b01824ced6cbb17236201a; the MCP source hash was e06981c9a01c406e50a156a4c60cda9b215c6e7aef3f9cc88c5eb1002ae4581b.

The full inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/89e9468e5b1dddb76194f4c1cecc2d3fc4cfb88e98ec64f0e2554814872d3004/a998f78fb138d8a81d2622aef989b09efc7b0086d71a42ce71425cbcbfcffe6d/probability-inspect-e06981c9a01c.json. Its artifact SHA-256 is 89e9468e5b1dddb76194f4c1cecc2d3fc4cfb88e98ec64f0e2554814872d3004 and declared size is 326,478 bytes. The request and inspect receipt are in probability-inspect-before-request.json and probability-inspect-before-receipt.json.

I discovered the artifact byte-range template on server hoi4_agent_tools. Reads at offset 0 with length 16000 and metadata=manifest both failed with the exact error “Artifact provenance manifest is unavailable.” Therefore the full inspect artifact’s helper-source list, adapter-version detail, and per-candidate provenance could not be recovered for this handoff.

The inspect request bound the frozen decision file, but the live schema does not document a helper-dependency overlay field. Because the shared helper file changed during this audit and the inspect artifact could not be read, I cannot verify which helper revision the MCP inspect resolved. I therefore do not claim an effective BEFORE score trace from that inspection.

hoi4.source_lookup returned status ok but its indexed source revision did not line up with the frozen snapshot. For the decision path, indexed line 1162 resolved to choose_strategic_ambiguity inside a different block, while frozen BEFORE line 1162 is gods_of_africa_prioritize_land. For the trigger path, indexed line 1273 resolved to a file comment rather than the frozen trigger at that line. The returned index revisions were 1867c78c866e18628c17c7edfc419dd155ad034865815e75ffc613b5d4422548 and 2154276b64501cd93ddf4e1f842b8c67bf881d3dbefcfb3d276e5788faa2db8e. I used the hash-verified local BEFORE copies for source review and do not treat those source_lookup locations as baseline evidence.

The offline Paradox Wiki references were read through revision-bound HOI4 MCP references:

- AI modding, MTTH blocks, path paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md, lines 26-37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818.
- Decision modding, AI, path paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, lines 357-374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Decision modding, Checking for target, the same path, lines 519-530, the same revision.

Installed-game documentation was read through the same MCP:

- Country Decisions, path C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md, lines 1-46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
- research_weight_factor, path C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md, lines 603-612, revision 70f5d755ae7ed4060e49cc64a393d1a0dc5611b3acc8abc6dfb4538781c915a1.

The Decision modding AI section and AI modding explain that ai_will_do values are score inputs in a highest-score race and can receive later strategy modifiers. Event-option ai_chance and random_list use proportional sampling instead. These decision scores are not click probabilities and are not timing distributions. The adapter inspection itself did not return an evaluated rank or normalized probability.

The MTTH skill was read because the decision syntax is MTTH-shaped. None of these 11 decision blocks uses an mtth: entry or an event MTTH surface, so no timing distribution is in scope.

## Raw named scenario fixtures

The raw BEFORE scenario JSON files were frozen with SHA-256 hashes in scenario-set-index.json:

| Declared pool | Scenario file | Scenario IDs | Candidate IDs |
| --- | --- | --- | --- |
| host_policy_representatives | host-policy-scenarios-before.json | HOST_DOCTRINE_ALL_NEEDS, HOST_PRIORITY_VIEW, HOST_PARTNER_VIEW, HOST_JUDGMENT_VIEW, AI_HOST_VIEW_BYPASS | gods_of_africa_prioritize_land, gods_of_africa_grant_leniency, gods_of_africa_mark_offender |
| host_pending_answers | host-answer-scenarios-before.json | HOST_PENDING_SUBSTITUTE, HOST_PAID_RECONCILIATION, HOST_VICTOR_RENEWAL | gods_of_africa_accept_substitute, gods_of_africa_reject_substitute, gods_of_africa_accept_reconciliation |
| participant_preparations | participant-preparation-scenarios-before.json | PARTICIPANT_TWO_CLOCKS, PARTICIPANT_PENDING_ULTIMATUM_ENTRY, PARTICIPANT_AFTER_ULTIMATUM | gods_of_africa_prepare_defensive_defiance, gods_of_africa_harden_stockpiles, gods_of_africa_secure_transport, gods_of_africa_prepare_countermeasures, gods_of_africa_permanent_defiance |

All cases declare synthetic ETH and GER scopes, flags, variables, the two separate clocks where relevant, the bounded participant and candidate-registry arrays, and eventTargets.africa_host = ETH. The scope aliases event_target:africa_host and var:authority_host are both bound to the ETH country scope. Country identity values remain string tags; no ordinal is substituted for a country identity.

Target pools are complete only within each synthetic fixture. The host answer cases model one GER participant; the victor case models GER only in the candidate registry. The participant universe in a real campaign is not represented as complete. No complete African-core ownership/control map or live AI strategy-factor state is included. No helper results are force-set.

Raw fixture hashes are local SHA-256 values only. No MCP canonical scenario hash exists because no probability_evaluate result returned. No scenario has an evaluated score trace yet.

HOST_DOCTRINE_ALL_NEEDS models the five core shortages and emergency need in a doctrine-unset state. It does not model each advanced-focus variant in the improvement addendum; those are parent-owned source-phase acceptance cases and are not probability evidence.

PARTICIPANT_PENDING_ULTIMATUM_ENTRY is an additional bounded case to isolate a non-defiant entry row while only the ultimatum is pending. It is a synthetic model, not an observed country state.

## Frozen-source score formulas

These are source-defined base values and modifier tables only. They are not MCP-evaluated effective weights.

| Decision | Frozen base | Source modifiers or zero gates | Frozen decision source |
| --- | --- | --- | --- |
| gods_of_africa_prioritize_land | Literal base 2 | No source modifier in the block. | common/decisions/012_africa_gods_decisions.txt:1180 |
| gods_of_africa_grant_leniency | mercy_base 3 | mercy_favored_track 3; mercy_hardship 3; mercy_loyal 2; mercy_holds_core 0.1; reciprocal 2; exaction 0.5; zero gate for invalid, defiant, or already-lenient targets. | common/decisions/012_africa_gods_decisions.txt:1383; common/script_constants/012_africa_gods_constants.txt:930-936 |
| gods_of_africa_mark_offender | judgment_base 5 | holds_core 4; at_war 3; defiant 2; target_collapsing 0.2; weak_africa 0.5; exaction 1.5; reciprocal 0.5; zero gate for collapsing Africa, full offender capacity, or invalid target. | common/decisions/012_africa_gods_decisions.txt:1838; common/script_constants/012_africa_gods_constants.txt:921-928 |
| gods_of_africa_accept_substitute | accept_substitute_base 10 | emergency 2; reliable 1.5; high_wrath 0.5; zero gate for unaffordable offer, unclear transfer, closed retry, or unneeded family. | common/decisions/012_africa_gods_decisions.txt:1582; common/script_constants/012_africa_gods_constants.txt:938-941 |
| gods_of_africa_reject_substitute | reject_substitute_base 2 | unneeded 5; high_wrath 2. | common/decisions/012_africa_gods_decisions.txt:1643; common/script_constants/012_africa_gods_constants.txt:942-944 |
| gods_of_africa_accept_reconciliation | accept_reconciliation_base 4 | near_collapse 2; reciprocal 1.5; exaction 0.5. | common/decisions/012_africa_gods_decisions.txt:1768; common/script_constants/012_africa_gods_constants.txt:946-949 |
| Four participant preparations | defense_base 8 each | high_wrath 1.5; dominant_africa 1.5; weak_africa 0.5; each has a per-action zero gate through its can_prepare helper. | common/decisions/012_africa_gods_decisions.txt:930, 960, 990, 1020; common/script_constants/012_africa_gods_constants.txt:898-901 |
| gods_of_africa_permanent_defiance | defiance_base 2 | loyal 0.05; holds_core 4; hostile_faction 3; offender 2; high_wrath 3; low_credibility 3; dominant_africa 0.3; demand_active 2; heavy_burden 1.5; zero gate when the action is invalid, reconciliation is pending, or no defiance rationale is present. | common/decisions/012_africa_gods_decisions.txt:874; common/script_constants/012_africa_gods_constants.txt:886-896 |

The fixed values and the four target-pool candidate lists above are not a normalized denominator. No arithmetic was performed to manufacture effective weights.

## Findings and recommended owner checks

The source has explicit zero-weight gates for invalid leniency and offender targets, unaffordable or unneeded substitute offers, per-action preparation validity, and invalid permanent-defiance requests. This is a source finding only; no scenario result proves those helpers evaluate true in the declared synthetic cases.

No missing or duplicate candidate definition was reported by probability_inspect for the named 11-row micro-pool. The generic gods_of_africa_substitute_demand row and the three named substitute slots are outside these three requested weight pools; their phase visibility remains with the parent source-phase tests.

No numeric tuning target is selected. The human host-view architecture is expected to bypass AI while leaving all numeric weights and prices unchanged; this remains unverified until the same-scenario MCP compare succeeds.

If the parent later authorizes weight maintenance, the literal base 2 on gods_of_africa_prioritize_land is the only directly observed hardcoded AI base in these 11 rows; it could be moved to a named entry under gods_of_africa_ai_response in common/script_constants/012_africa_gods_constants.txt while preserving value 2. No balance change is recommended from source alone.

After the parent AFTER signal, run one bounded probability_compare per declared pool using the exact scenario files above and before/after source manifests that bind helper dependencies as well as the decision file. If the live route cannot overlay the frozen dependency set, keep the affected comparison and conclusions unresolved rather than using mismatched helpers. Render only successful analysis IDs that benefit from ranking, matrix, sensitivity, or unresolved views.

## Skipped analyses, blockers, and uncertainty

hoi4.probability_evaluate was not called. The live decision and trigger source files had diverged from the parent BEFORE manifest, while the artifact helper-source list could not be recovered. An evaluation without a verified helper overlay would not establish a BEFORE trace.

hoi4.probability_sweep was not called for the same dependency reason; no threshold, sensitivity, or rank-reversal claim is made.

hoi4.probability_compare is deferred until the parent AFTER signal. Current live hashes are observations during this audit and are not treated as a final accepted AFTER source set.

hoi4.probability_render was not called because no evaluate or sweep analysis ID exists. probability_simulate was not used because no uncertain-input distributions were declared. probability_sequence is not applicable because no custom weighted pool, cadence, and state transitions are in scope.

The artifact read route is blocked by the exact MCP error “Artifact provenance manifest is unavailable.” The source_lookup index does not match the frozen file line map. Both limitations are preserved in evidence/mcp-attempts.json.

There are no evaluated score traces, effective modifier waterfalls, rankings, timing results, thresholds, sensitivity breakpoints, rank reversals, dominance/starvation results, repetition rates, or exploit probabilities. The raw scenario files have file hashes but no MCP canonical hashes. These results remain unresolved until a source-complete probability pass succeeds.

The following skills were read and applied: chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-decisions-missions, and chaos-redux-mtth. The HOI4 MCP offline-reference context/search/read and source lookup routes were used; no gameplay-source or test files were edited.

## AFTER phase update (2026-10-07)

The parent AFTER signal was received. The user-reported paid-reconciliation source-review fix is present in the frozen AFTER decision snapshot with SHA-256 e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93.

The current gods_of_africa_accept_reconciliation row has target_trigger = FROM exists. Its available block retains FROM exists and the original OR between current victor renewal and participant_can_reconcile plus reparations_paid plus reconciliation_offer_pending. The current visible helper is gods_of_africa_reconciliation_answer_is_current in common/scripted_triggers/012_africa_gods_response_context_triggers.txt; its reconciliation branch is can_reconcile plus paid plus offer, and its victor-renewal branch remains an OR. No extra participant flag sits outside the original branch.

The AFTER identity is frozen in after-source-manifest.json and after/source_snapshots/. It contains 19 logical sources, including the current response-context helper at SHA-256 91665ade663c79702514bfe28c75f17f2b880ddfaf8f90c776e92b404611dcac. post-compare-source-check.json confirms all 19 live files still match the frozen AFTER hashes after the compare attempt, so this source set does not require refresh.

The original six-file BEFORE manifest and snapshots remain unchanged. The response-context helper has no byte snapshot in the supplied BEFORE manifest or this task's pre-AFTER evidence. The separate response-context handoff says it adds seven helpers, but the exact source presence and bytes at the probability baseline cut are not bound by the original six-file snapshot. before-context-source-status.json records this uncertainty; no pre-AFTER helper content was invented.

I made one bounded hoi4.probability_compare request for host_policy_representatives, using the unchanged HOST_DOCTRINE_ALL_NEEDS, HOST_PRIORITY_VIEW, HOST_PARTNER_VIEW, HOST_JUDGMENT_VIEW and AI_HOST_VIEW_BYPASS fixtures. The request bound the decision source on both sides with path, snapshotPath and expectedSourceHash, and supplied the full before and AFTER multi-file manifests.

MCP rejected that request before analysis with: “Invalid input: expected object, received undefined at beforeManifest.selection; expected array, received undefined at beforeManifest.candidates; expected array, received undefined at beforeManifest.transitions; unrecognized key sources at beforeManifest”; the same errors were returned for afterManifest. The live schema treats these two fields as custom weighted-pool manifests, so it cannot overlay the source-file manifests in the submitted form. The exact request summary and MCP error are in compare-host-policy-request.json and compare-host-policy-result.json.

I did not try alternate manifest shapes. The host-answer and participant-preparation compare calls were not sent because the same shared schema blocker prevents a source-complete comparison. No analysis ID, comparison ID, canonical scenario hash, score delta, ranking, or rendered comparison was produced. The five named host-policy cases and both remaining scenario sets are still preserved with their raw file hashes.

No click probability was requested or inferred. Human-view navigation is outside the probability metric, and the ai_will_do rows remain willingness-score inputs. Because the full helper overlay did not run, the claim that numeric weights are unchanged remains unverified by MCP comparison. No numeric tuning target was selected, and no source or price patch was made by this auditor.

Remaining blockers are the source-manifest overlay route and the unbound BEFORE response-context helper bytes. The single rejected compare is preserved as partial MCP coverage; the other two pools remain unresolved. Source-only phase tests and the parent’s independent source review/test remain parent-owned. Skills applied remain chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-decisions-missions, and chaos-redux-mtth.

## Probability continuation (2026-10-08)

This continuation supersedes the earlier statement that the two host comparisons were deferred. It preserves the rejected manifest-shaped call as history and records the corrected root-source comparisons below. No gameplay source, tests, or Git state were changed by this audit.

The weighted surface is the decision_ai_will_do score race in common/decisions/012_africa_gods_decisions.txt. The initial probability_inspect succeeded with code PROBABILITY_SOURCE_INSPECTED, source revision a053df7d864a8de00c2f9611c6275379a6b8c204ea93f593cbb249ecd20df24d, MCP source hash 489f4cbef94ed11f166a51e81921ef9fb3300f2e1a5d451465c95119a123f1fb, 11 candidates, complete discovered pool, required input scope.FROM, and zero parser-unresolved items. Its artifact and hash are retained in continuation-2026-10-08.json.

Both valid comparisons bind the logical decision path to the frozen BEFORE snapshot with SHA-256 b39073b4370a8f7508ddc7902a6d9f4e5907942375313257fd063268a60fc6e8 and to the frozen AFTER decision snapshot with SHA-256 e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93. These are root-only source selectors. The compared source revision does not freeze transitive helpers: current helpers are resolved on both sides, so neither comparison proves historical BEFORE helper behavior.

For host_policy_representatives, the complete declared micro-pool is gods_of_africa_prioritize_land, gods_of_africa_grant_leniency, and gods_of_africa_mark_offender. The five scenarios are HOST_DOCTRINE_ALL_NEEDS, HOST_PRIORITY_VIEW, HOST_PARTNER_VIEW, HOST_JUDGMENT_VIEW, and AI_HOST_VIEW_BYPASS, from fixture hash 7a0157ee372178d8b0ba942e941829133db57f51477d32a1bec5d96149b29cea. The refreshed comparison returned PROBABILITY_ANALYZED_PARTIAL for analysisId probability-3668172d415f8e591242a764, scenario hash 1d908b3a8c0a3909618303f7e21d47f8f538870ea13150e1d1c3e4c62878c3d5, source revision c95ed1326873b3cc55a5754d580caa3100115494000ad67274ec3d3e10b89554, 15 candidate-scenario rows, 61 unresolved inputs, zero eligible rows, and 15 excluded rows. The declared candidate pool is complete only for these synthetic host-policy cases, not for a country’s full decision denominator.

The first host-policy compare artifact was read completely by validated byte ranges. It reports 15 unresolved-analysis regressions, rawDelta 0 and unresolvedDelta 11 for each candidate-scenario row, and null ranks and conditional probabilities. The refreshed compare returned the same scenario hash and partial counters, but its JSON artifact was not read. Because the candidates remain unresolved, neither the reported zero raw deltas nor the analyzer’s PROBABILITY_OUTCOME_NEVER_ELIGIBLE warnings establish score equivalence or actual in-game invalidity. The adapter could not resolve capital_scope, any_of_scopes, any_controlled_state, any_owned_state, any_enemy_country, has_opinion, tag-valued identity checks used as numeric operands, several array and war/faction comparisons, or global.num_days against the priority-change timer.

The complete host_pending_answers fixture contains HOST_PENDING_SUBSTITUTE, HOST_PAID_RECONCILIATION, and HOST_VICTOR_RENEWAL, with candidate pool gods_of_africa_accept_substitute, gods_of_africa_reject_substitute, and gods_of_africa_accept_reconciliation. The full fixture was rejected before analysis with the exact validation error: “Too small: expected array to have >=1 items at scenarioSet.scenarios[2].scopePools[0].candidates”. HOST_VICTOR_RENEWAL declares a complete empty participant pool; no participant was fabricated. The accepted bounded subset retains the original two nonempty scenarios HOST_PENDING_SUBSTITUTE and HOST_PAID_RECONCILIATION, with the full three-decision candidate pool, and is explicitly identified as a two-of-three subset. Its refreshed comparison returned PROBABILITY_ANALYZED_PARTIAL for analysisId probability-2bd61910a8345e841e5debae, scenario hash 3563d847b41a452a9c4ef1f498d0ec650ba28c50674f4f5e1678680703d16672, source revision d48d209d69e7e6703a13d177187b0971b90e3a0aeac9041790c3d51b9262b21f, six candidate-scenario rows, 179 unresolved inputs, zero eligible rows, and six excluded rows. MCP reported comparisonChanges 0, but the unresolved traces do not support a numeric before-and-after conclusion. HOST_VICTOR_RENEWAL remains separately blocked by the validator constraint.

The third declared set, participant_preparations, remains un-compared. Its scenario ids are PARTICIPANT_TWO_CLOCKS, PARTICIPANT_PENDING_ULTIMATUM_ENTRY, and PARTICIPANT_AFTER_ULTIMATUM; its complete declared micro-pool contains gods_of_africa_prepare_defensive_defiance, gods_of_africa_harden_stockpiles, gods_of_africa_secure_transport, gods_of_africa_prepare_countermeasures, and gods_of_africa_permanent_defiance. The relevant helpers changed between the snapshots, and the response-context helper has no BEFORE byte snapshot by design. No frozen BEFORE helper resolution is claimed.

Both probability_compare calls generated ranking, matrix, waterfall, comparison, and unresolved SVG/PNG resources. Standalone probability_render was attempted for both refreshed analysis ids, but returned PROBABILITY_ANALYSIS_STALE and no visual resources: the host-policy analysis revision c95ed1326873b3cc55a5754d580caa3100115494000ad67274ec3d3e10b89554 was compared with current revision 1855039237c094bacffed602b672f50f6860e10bc97252ece56891cb020bb856, and the host-answer-subset analysis revision d48d209d69e7e6703a13d177187b0971b90e3a0aeac9041790c3d51b9262b21f was compared with current revision fb89e46285558ac80708981d19a71eb96fd4e74f8959b3d4512fca997d40ab27. The compare-generated visuals and all returned or stale artifact URIs are recorded in the evidence JSON; no further refresh was attempted.

The frozen AFTER manifest still identifies 19 logical sources. A current hash check found 18 unchanged and one intentional wording-only localization update: localisation/english/012_africa_gods_l_english.yml changed from the frozen AFTER hash 7cbe3cd5a5b67bc3dd21ca29d9cc455930867e0a0ae90d9186ce84c52b10e28d to current hash 3efe9abb5a29c62cae79699857f21411240840f3e59749c1896ffc14963e2b65. The parent identifies four changed strings (overview, priorities, navigation label, and ordinary host boilerplate); the pre-wording AFTER snapshot remains untouched. This wording update is not gameplay evidence and does not expand the analyzed decision source.

Source review and parent evidence identify the relevant changed gameplay dependencies as common/scripted_triggers/012_africa_gods_triggers.txt, including the participant preparation guards; common/scripted_triggers/012_africa_gods_response_context_triggers.txt, added after the BEFORE cut; common/scripted_triggers/012_africa_gods_response_view_triggers.txt; common/scripted_effects/012_africa_gods_response_view_effects.txt; common/script_constants/012_africa_gods_response_constants.txt; common/scripted_localisation/012_africa_gods_response_scripted_localisation.txt; and the changed decision, effect, and recovery-effect files listed in the saved manifests. The response-context helper’s AFTER hash is 91665ade663c79702514bfe28c75f17f2b880ddfaf8f90c776e92b404611dcac. No documented source.virtualPatch schema was found in the live tool contract or the relevant local guidance, so no guessed overlay was attempted.

Parent source review says host view flags gate presentation for human hosts while AI bypasses navigation, and that four participant preparations plus permanent defiance are suppressed during the final ultimatum. HOST_PRIORITY_VIEW, HOST_JUDGMENT_VIEW, and AI_HOST_VIEW_BYPASS were present in the bounded fixtures, but the analyzer could not resolve the helper chain; these behavior statements therefore remain parent source evidence, not MCP probability proof. The parent also reports that numeric AI blocks and prices were unchanged and that 21 source test groups passed. No numeric tuning target is recommended from this audit.

This remains score-only and unresolved for ranking, dominance, starvation, rank reversal, repetition, and exploit-risk claims. Decision ai_will_do values are willingness scores in a highest-score race, not click probabilities or timing distributions. Standalone probability_evaluate and probability_sweep were not run after the partial comparisons because all candidate traces remained unresolved and no meaningful numeric threshold or rank-reversal basis was available. Simulation was not used because no uncertain-input distribution was declared; sequence analysis is inapplicable because these are not custom weighted pools. The concrete next evidence needed is analyzer support for the listed scoped triggers and tag-valued identities, a valid representation for a complete empty scope pool, and a documented dependency overlay before any claim about historical helper resolution. No gameplay patch is recommended or applied.

For this continuation, the skills read and applied were chaos-redux-subagents and chaos-redux-decisions-missions. Earlier skill and offline-reference evidence remains in the dated sections above.
