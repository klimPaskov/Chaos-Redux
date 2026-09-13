# Event021 sponsor AI resource-guard audit

Date: 2026-09-02.

Repository: Chaos Redux at C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux.

Mode: read-only audit of the owner-applied sponsor decision patch.

Status: source change confirmed, MCP comparison completed, campaign balance and engine purchase behavior not certified because the adapter remains score-only and leaves required resource and surrender inputs unresolved.

## Scope and outcome

The audited weighted surface is the decision AI ai_will_do for event021_support_government, event021_support_opposition, and event021_offer_mediation in common/decisions/021_random_civil_war_decisions.txt.

The owner patch changes only that decision file. The two support ai_will_do hard-zero OR blocks now include the same political-power and convoy availability gates already present in their available and custom_cost_trigger blocks. The mediation ai_will_do adds a zero-factor OR for political power below 20, command power below 10, or convoys below 5.

The saved before body is the genuine prepatch source for this audit. The old September 1 diagnostic is not used as a baseline.

The exact same named SPN-01 through SPN-05 scenario body was evaluated against the saved before body and the current source, then passed to hoi4.probability_compare. The core comparison emitted 12 source-driven scenario changes and remained partial because the new political-power and command-power predicates are not resolvable in the declared adapter fixtures.

The baseline references were the completed pre-this-patch September 2 audit and the saved source bodies, not the September 1 documents docs/plans/021_random_civil_war_plans/subagent_handoffs/probability_ai_timing_2026-09-01.md or docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_spn_parent_diagnostic_2026-09-01.md.

No current source-side score bug was proven. The current MCP observability issue is that the decision adapter cannot resolve direct political-power, command-power, and surrender-progress inputs in these fixtures, so it emits unresolved score traces and can retain partial ranks beside unresolved candidates. This is not evidence of an engine purchase exploit.

## Exact source truth and dependency stability

The before bodies are saved under docs/plans/021_random_civil_war_plans/probability_snapshots/sponsor_resource_guard_before_2026-09-02/.

| Dependency | Before snapshot raw SHA-256 | Current source raw SHA-256 | Normalized semantic result |
| --- | --- | --- | --- |
| common/decisions/021_random_civil_war_decisions.txt | 3851afb4a8a3f4736b5333b3e8edd4320547f6bd02a671e9042513c023c884f1 | 9de76ff9027ea2a4f01daedb0aefa02bea671ac49215b6905eeba7312038886c | Decision-only patch; 12 added lines representing four support resource predicates, three mediation resource predicates, and their block structure. |
| common/scripted_triggers/021_random_civil_war_parent_triggers.txt | cb9c12a261de7ce9b0b4ef6d044ff6857651179bb730a93d8e6d9692075b37d5 | cb9c12a261de7ce9b0b4ef6d044ff6857651179bb730a93d8e6d9692075b37d5 | Byte-identical and semantically unchanged. |
| common/script_constants/021_random_civil_war_constants.txt | 87e8d6fefd322c0fa4f40c85af3f0da61f25da719d9ccaac17f14c405225710c | b02ae147ce8ce700792c2b9110d0bf34d5c65d1403ba15f685a968d8c1d09ec1 | Normalized LF SHA-256 is 87e8d6fefd322c0fa4f40c85af3f0da61f25da719d9ccaac17f14c405225710c; current raw difference is line-ending normalization only. |

The current constants file has 428 CRLF and 372 LF-only line endings, while the saved constants snapshot is LF-only. The normalized content hashes match, so the constants source is semantically stable during this audit.

The final dependency recheck after the MCP calls matched the initial source capture for the current decision and parent-trigger files, and matched the normalized constants hash. No relevant source changed during analysis.

The source constants used by both before and after fixtures are:

| Action | Political power gate | Command power gate | Infantry gate | Convoy gate |
| --- | ---: | ---: | ---: | ---: |
| Government support | 20 | Not applicable | 150 | 5 |
| Opposition support | 20 | Not applicable | 150 | 5 |
| Mediation | 20 | 10 | Not applicable | 5 |

event021_ai.exposure_mediator_stability is .65. The constants completion handoff records 231 supplied undefined unique keys and nine inferred tuning groups awaiting parent review; this audit did not alter or certify those pending groups.

The constants source snapshot was the completed handoff docs/plans/021_random_civil_war_plans/subagent_handoffs/script_constant_completion_2026-09-02.md as represented by the saved constants body and its normalized hash above.

The current source locations are event021_support_government at lines 380-433, event021_support_opposition at lines 435-488, and event021_offer_mediation at lines 490-531. The source-side available and custom_cost_trigger resource gates predate this patch and remain present.

## Scenario contract

The core candidate pool is complete for the decision adapter:

event021_support_government, event021_support_opposition, event021_offer_mediation.

The exact core scenario-set hash is 07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3.

The exact body reused for the prepatch baseline, postpatch evaluation, and core comparison is:

~~~javascript
const base = {
 actor:"CXT", date:"1936.1.1",
 state:{
  "scope.hidden_trigger":true,
  "scope.has_equipment":false,
  "scope.var:random_civil_war_exposure_source_country_scope":true,
  has_war:false, surrender_progress:0.10, has_same_ideology:false,
  has_variable:true, political_power:100, command_power:100,
  infantry_equipment:1000, convoys:100
 },
 flags:["random_civil_war_neighbor_exposure"]
};
const scenarioSet = {
 schemaVersion:"1.0",
 id:"event021_sponsor_ai_spn_01_05_postrepair_2026_09_02_final",
 scenarios:[
  {...base,id:"SPN-01",label:"Rich neutral major, one aligned viable side",flags:[...base.flags,"random_civil_war_opportunistic_sponsor_profile"],candidateOverrides:{"event021_support_opposition":false}},
  {...base,id:"SPN-02",label:"Sponsor in desperate war with low equipment",state:{...base.state,"scope.hidden_trigger":false,"scope.has_equipment":true,"scope.var:random_civil_war_exposure_source_country_scope":false,has_war:true,surrender_progress:0.80,political_power:10,command_power:5,infantry_equipment:50,convoys:1},flags:[...base.flags,"random_civil_war_opportunistic_sponsor_profile"]},
  {...base,id:"SPN-03",label:"Two rival sponsors and two viable sides",flags:[...base.flags,"random_civil_war_opportunistic_sponsor_profile","random_civil_war_government_side","random_civil_war_opposition_side"]},
  {...base,id:"SPN-04",label:"Side has no administration or survival path",state:{...base.state,"scope.var:random_civil_war_exposure_source_country_scope":false},candidateOverrides:{"event021_support_government":false,"event021_support_opposition":false}},
  {...base,id:"SPN-05",label:"Neutral mediator profile",flags:[...base.flags,"random_civil_war_mediator_profile"]}
 ]
};
~~~

External factors are limited to the declared actor, date, state values, flags, and candidate overrides above. No random seed, cadence, timer transition, or complete custom normalized pool was declared because this surface is decision score selection rather than a modeled probability or timing distribution.

The sweep reused the same five scenario bodies and added the declared uncertain input surrender_progress over the range 0 to 1 in five steps. Its scenario-set hash is 08d00630206417d93ffd8dc60285334cb2b4a5d06a1e1fe2e20c2a91316b3155.

## MCP evidence

The mandatory first call for the current surface was hoi4.probability_inspect with adapter decision_ai_will_do, the three-candidate pool, refresh=true, and source path common/decisions/021_random_civil_war_decisions.txt.

| Pass | Result and provenance |
| --- | --- |
| Current inspect | PROBABILITY_SOURCE_INSPECTED, pool complete, 3 candidates, 0 static available candidates, 7 required inputs, 0 unresolved. Source revision fe86d287c765cef45c87d0407c56b8a82c347f78843c734060b1e42f1267359; MCP canonical source hash 2873dfe6acc858000c00adc78dfe28af22ed592770e256b1c46e30727567922c. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c094930231da6978d08b62d6d97a86d79d842fc20686f6ac8fe4ace2e9f333bb/cc982cde527d3ad0e4db63402e699f998309ad959be3b471a3a73d3a3ddc102f/probability-inspect-2873dfe6acc8.json. |
| Saved-before inline inspect | Path-only inspection of the docs snapshot was not used because the inactive docs path returned PROBABILITY_SOURCE_DISCOVERED with no weighted surfaces. The exact saved body was then supplied through the documented inlineClausewitz source field. Result: PROBABILITY_SOURCE_INSPECTED, complete 3-candidate pool, 5 required inputs, 0 unresolved. MCP canonical inline hash b1f7133d0036b6f12a8604c7ad884f966e11f559cdb2aeeacec68a3e1c5ffbbd. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a2da48469d25e310e5a3014c7a7a2d001c9c394cf4a9f503758c4a71fba3c2b/7e78bdf22676751ed4a625d36f56e4dd4615a99d0e257cbc32f5c546b1e64711/probability-inspect-b1f7133d0036.json. |
| Before evaluate | Analysis probability-3604852908ac337b88c7a0bb, partial, 5 scenarios and 15 candidates, 2 unresolved. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25e603ec1511d9a230eee6f20d2d0282d74abb1c81f68fd6740e50e7fe9482bf/7e8cf97ca4e2a6813193e929cc17df6929ba882c4dda412e0a85b52e77ed4f2d/probability-3604852908ac337b88c7a0bb.json. |
| After evaluate | Analysis probability-73bbc20c3bf7cbcfa58cc9a2, partial, 5 scenarios and 15 candidates, 6 unresolved, 0 diagnostics. MCP canonical source hash 2873dfe6acc858000c00adc78dfe28af22ed592770e256b1c46e30727567922c. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78f6d40c06fa226d438a42d0acfe5bb7660bd8dee0b1a9bb94b724e17943d48d/8fdca861536e33fc95bf789d575f94292a65178d857f08d24d3ec2393b8a31ee/probability-73bbc20c3bf7cbcfa58cc9a2.json. |
| Sweep | Analysis probability-f8db8282527bae3e2fac68d5, partial, 25 sweep points, 6 unresolved, 0 diagnostics. The threshold render states 0 rank reversals and 0 threshold observations. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e69e335ee76ed23f1e18c0a419908d271dabf646769c9e0b6cf279710f553f51/f7ad648f947df2387820027c2a7d075298d4891659e042840fa81c6226fe5/probability-f8db8282527bae3e2fac68d5.json. |
| Core compare | Analysis probability-248f44a08b739e9eaafee94a, partial, same scenario hash 07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3, 5 scenarios and 15 candidates, 8 unresolved, 12 comparison changes, 0 diagnostics. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7834f53a1e9c5eade619079452f1630c69e99ca106c38e7133912c2ba22a3985/09560f4ae13e7bb334b0a31760daedbb00605121a25a521336cc2c64b7b163b9/probability-248f44a08b739e9eaafee94a.json. |
| Resource-edge compare | Analysis probability-d8847fd2701b83d03368dca7, partial, synthetic 5-scenario extension, 15 candidates, 5 unresolved, 4 expected fixture diagnostics, 7 comparison changes. Scenario hash 0a1d8ecf10b5fae7d5ce119c53c1309ab2861574a616f324a44979cf2e32894e. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c227243a1d5e3d276570d9cd4c5bf4d3e28ce5455a905ceed6d863916f32806c/6632139d082487dc719725b0ff4ddb438d4b93592215abed1a54064276e24cbf/probability-d8847fd2701b83d03368dca7.json. |

The before source object for compare used path and the decision identifier together with the complete saved before body in inlineClausewitz. The after source object used the current decision path and expected raw source hash 9de76ff9027ea2a4f01daedb0aefa02bea671ac49215b6905eeba7312038886c. No cached September 1 analysis was substituted.

The emitted MCP source revisions were current inspect fe86d287c765cef45c87d0407c56b8a82c347f78843c734060b1e42f1267359, saved-before inline inspect 6ec12bef989689968f7d636760f9e6cca9a173a1b2a1ea2b2d276be29ccecc91, before evaluate b062868e5600c609fe6cefc24757895e8071a5464869d84bf03ae661cb66cb16, after evaluate 6ec12bef989689968f7d636760f9e6cca9a173a1b2a1ea2b2d276be29ccecc91, sweep b062868e5600c609fe6cefc24757895e8071a5464869d84bf03ae661cb66cb16, core compare b062868e5600c609fe6cefc24757895e8071a5464869d84bf03ae661cb66cb16, and resource-edge compare c3607dbda7137c8a0eda36e3dd9f483d1b21bd11f5459ff90a4de6135f72a8c2. Local raw hashes above are the source-stability check; these emitted revisions are retained as MCP provenance and are not treated as interchangeable with local hashes.

The MCP adapter identifies this surface as decision_ai_will_do, score_only, with normalizedProbability=false and timeDistribution=false. Therefore every numeric result below is an AI willingness score or a rank observation, never a click probability.

## SPN-01 through SPN-05 before and after

The before column comes from the saved before body. The after column comes from the current source. Unresolved means the adapter could not resolve one or more required trigger inputs and therefore the score or rank is not certifiable for that candidate.

| Scenario | Before saved-body result | After current-source result | Comparison interpretation |
| --- | --- | --- | --- |
| SPN-01 Rich neutral major, one aligned viable side | Government 1.6875, eligible, rank 1; mediation 0.75, eligible, rank 2; opposition 0, ineligible. Government retained an unresolved surrender trace even before the patch. | Opposition 0, ineligible. Government is eligible but score unresolved because political power and surrender are unresolved. Mediation is eligible but score unresolved because political power and command power are unresolved. | The compare records new unresolved resource-factor attribution for government and mediation. The prepatch government-over-mediation score race cannot be certified after the guard predicates become unresolved. |
| SPN-02 Sponsor in desperate war with low equipment | Government, opposition, and mediation were ineligible with raw score 0. Support traces included unresolved surrender. | All three remain raw 0 and ineligible in the declared fixture. Support traces add unresolved political power and mediation traces add unresolved political power and command power. | The hard-zero outcome is consistent with the declared desperate-war and low-resource fixture, but direct resource-gate execution is not independently resolved by this adapter. |
| SPN-03 Two rival sponsors and two viable sides | Government 1.6875 and opposition 1.6875, both eligible and tied at ranks 1 and 2; mediation 0.75, eligible, rank 3. | Government, opposition, and mediation are all unresolved because support candidates require surrender and political power while mediation requires political power and command power. | The compare records new unresolved resource-factor attribution for all three candidates. No postpatch tie or dominance conclusion is certifiable. |
| SPN-04 Side has no administration or survival path | Government and opposition 0 and ineligible; mediation 1, eligible, rank 1. | Government and opposition remain 0 and ineligible. Mediation is eligible but unresolved on political power and command power. | The support validity override remains a hard exclusion in the fixture. The mediation score cannot be compared as a determinate postpatch score. |
| SPN-05 Neutral mediator profile | Mediation 1.5, eligible, rank 1; government and opposition 0, eligible, ranks 2 and 3 because the mediator profile hard-zeroed both support candidates. | Support government and opposition remain raw 0 and are shown at partial ranks 1 and 2 because mediation is unresolved. Mediation is unresolved on political power and command power. | The source hard-zero for the support candidates remains present. The displayed after-ranks are not meaningful for dominance because the mediation candidate is unresolved; the compare records a rank delta for the two zero-score support rows but no probability change. |

The core compare reports adapterChanged=false and assumptionsChanged=false. Its compare-side before analysis ID is probability-ef3653a0f7742b79d4e4000c and after analysis ID is probability-1a5c796c836618d1e79bfc57. Its 12 UNRESOLVED_ANALYSIS_INTRODUCED entries are analyzer fixture regressions caused by the added resource predicates, not proven gameplay regressions. The compare does not establish a purchase exploit before or after the patch.

## Resource-edge extension

The extension was run only to isolate the new gates and is not a campaign fixture. All five scenarios used actor CXT, date 1936.1.1, the same complete three-candidate pool, valid hidden exposure state, high non-tested resources, and explicit candidate overrides that disabled the irrelevant opposition candidate. The four opposition never-eligible diagnostics are expected consequences of those isolation overrides.

| Fixture | Declared edge | MCP before/after evidence | Classification |
| --- | --- | --- | --- |
| RG-01-GOV-PP | Government support with political power 10, command power 100, infantry 1000, convoys 100. | The after government score is unresolved on political power and surrender. | Unresolved isolation fixture; no support-PP certification. |
| RG-02-GOV-CONVOYS | Government support with political power 100, command power 100, infantry 1000, convoys 1, and scope.has_equipment=true. | The after government row is raw 0 with the new guard attributed, but raw delta is 0. The same fixture also has a mediation drop from 0.75 to 0 on the convoy edge. | The support result is confounded by the adapter's scope.has_equipment shorthand and does not isolate a positive prepatch support score. The mediation convoy score drop is bounded score evidence only. |
| RG-03-MED-PP | Mediation with political power 10, command power 100, convoys 100. | The prepatch mediation trace contains the positive 1.5 factor; the after mediation score is unresolved on political power and command power. | Unresolved isolation fixture; no mediation-PP certification. |
| RG-04-MED-CP | Mediation with political power 100, command power 5, convoys 100. | The prepatch mediation trace contains the positive 1.5 factor; the after mediation score is unresolved on political power and command power. | Unresolved isolation fixture; no mediation-CP certification. |
| RG-05-MED-CONVOYS | Mediation with political power 100, command power 100, convoys 1. | The mediation raw score falls from 1.5 to 0, raw delta -1.5, with the new convoy guard attributed. | Determinate bounded score change for this synthetic edge, not a campaign probability. |

The extension's compare-side before analysis ID is probability-0c755be42a5847f774c36e19 and after analysis ID is probability-e8ec226e3b8681f8aa25cbd8. Its 5 unresolved entries are the mediation resource traces. Its four diagnostics concern the deliberately disabled opposition candidate, not the new guard logic. The extension therefore gives direct bounded evidence for the mediation convoy zero factor, while PP and CP edges remain unresolved and the government convoy edge remains confounded.

## Findings

Validity: SPN-02 and SPN-04 retain hard exclusions for the declared invalid, nonviable, or desperate-war fixtures. The parent scripted-trigger source is unchanged and its mediator, target-validity, viability, alignment, equipment, overextension, and surrender-related behavior was not reclassified from source inspection alone.

Score race: Before-patch score-only observations show government over mediation in SPN-01, a government/opposition tie in SPN-03, and mediation over the support rows in SPN-04 and SPN-05. Postpatch resource predicates make the affected after traces partial, so no after dominance claim is made.

Rank reversal: The five-step surrender sweep produced 25 points and the threshold render reported zero observed rank reversals and zero threshold observations. Because resource predicates remain unresolved, this is a bounded analyzer observation rather than a balance certification.

Starvation: SPN-02 shows all candidates at raw zero or ineligible under the declared desperate-war and low-resource fixture. The audit cannot quantify whether normal campaigns encounter unintended starvation because direct resources and surrender are not resolved by the adapter.

Repetition and timing: No sequence or timing result is claimed. This pass did not have a complete declared custom pool, cadence, cooldown transition model, seed, or event MTTH surface for probability simulation or sequence analysis.

Score-versus-availability bug: The prior positive unavailable score was a score/availability inconsistency in the AI surface, not a proven engine purchase exploit because available and custom_cost_trigger already gated the same costs. The owner patch aligns the support AI hard-zero predicates with those existing gates and adds the corresponding mediation hard-zero. MCP cannot currently prove the runtime purchase path.

Future target-audit blocker: the later broader audit should separately address the target-pool normalization behavior that rounds score / 100 and clamps it to 1 through 10 before shared load, so a normal low-score 90 and a major score around 31.5 can both become one ticket. This is outside SPN-01 through SPN-05 and was not expanded here.

## Recommendations without applying them

1. Keep the owner patch as a bounded source correction pending a typed MCP fixture or adapter route that resolves political power, command power, equipment quantities, war state, and surrender progress directly.
2. Rerun the exact saved-before and current-after SPN-01 through SPN-05 body, plus the five resource-edge fixture bodies, once those inputs are supported, and require a clean hoi4.probability_compare result before certifying the score race.
3. Preserve the existing available and custom_cost_trigger gates as the engine-side purchase guard; do not infer purchase safety from AI score traces alone.
4. Keep scope and surrender validation unresolved until the analyzer can resolve the source-country target scope and the surrender_progress trigger in the same fixture.
5. Treat the target-pool ticket quantization issue as a separate future target-audit blocker and do not fold it into this sponsor result.

## Skipped analyses and blockers

hoi4.probability_simulate was skipped because no uncertain resource distribution and seed contract was declared and the adapter did not resolve the required resource inputs.

hoi4.probability_sequence and event MTTH timing analysis were skipped because this decision-score surface did not supply a complete custom pool, cadence, timer, state-transition, and terminal-state contract.

Campaign selection probabilities, campaign timing distributions, purchase-exploit claims, and final balance certification remain unresolved.

The previous structural-inventory correction is carried forward: the same-revision parent event-render manifest contains 368 source hashes, including the mod on-action and event files, with selected root event:chaosx.nr21.3 and its option and terminal nodes. This handoff makes no game-only inventory claim. The helper-deferred validation remains false and is outside this decision-only comparison.

Manifest reference: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/909f0e9c8fb99fb70f04ec8d4c2aa2aa30e4261e3fe37f69a441b9b872dcc2f9/044b9532f9aa9bcc64c1eaaa36af1adba12cbd37fe1d3aeb46331770861defc8/event-options-23d07f38466b-manifest.json.

## Rendered evidence

After core evaluation ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ffa816d9e08edd1ba74e88acb5761bf587d164ed2589a6f7c838aa5da36aec1/7d5813c65f0639b6f50a077978e3e3c9a93ba7e2dc8176fda25884767f0da2c4/probability-probability-73bbc20c3bf7cbcfa58cc9a2-ranking.svg.

After core evaluation matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94c097a7153186e7f9e16e569c0fd587861e7668b2e0526eabf42a2ec4aee10a/b0c8396e135a7dfd5f540470eaf0e86f63d1fda03bc160545519a17dfbfa4f7a/probability-probability-73bbc20c3bf7cbcfa58cc9a2-matrix.svg.

After core evaluation waterfall: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1968a1cad43661bd3681df9bb5f8b1b3c13c4289cab89ea927e2a10e14427318/384ea84873dcd1c9edfcf95ea7234964998efbc03972890f84ae5851ae94a928/probability-probability-73bbc20c3bf7cbcfa58cc9a2-waterfall.svg.

After core unresolved view: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a06a3c0cfda377b7f61effd43e2fd1cc582c2c05d9a693e4449730e77c964daf/67710fe802f2174c31155aa1e69205c4d17f2d4e83c76f6264a2527625d002fb/probability-probability-73bbc20c3bf7cbcfa58cc9a2-unresolved.svg.

Sweep sensitivity: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/372c8363e344fea4b913d74292162ca7962c6b79e61ac311003220e3c3262534/08880d3aa92254a891377457b1ad97faaef4b1836c51e9462e235d70852d625b/probability-probability-f8db8282527bae3e2fac68d5-sensitivity.svg.

Sweep threshold: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/9369e3b753e04ca0052441eed859c25c989b531821320f26af39c38a5eae02aa/probability-probability-f8db8282527bae3e2fac68d5-threshold.svg.

Core comparison render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a8a3964b6e3051d8b83f676568ccaedf86d8e6719ac86c949b04d7bc509617b/67b4c108137d534876c73ecae9fc20d3e86ef13a3e97bf22ca8c5fc8c80ba509/probability-probability-248f44a08b739e9eaafee94a-comparison.svg.

Resource-edge ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/238b43414139c8a0a0c0989a31796d0a8524fa7cee02f4dfe393cb7e41694e8a/8d61ffd9f89fbe090a9bebfa41c6643d1ad801573c2d4ee473a1622e74239e1e/probability-probability-d8847fd2701b83d03368dca7-ranking.svg.

Resource-edge matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d90d8081342cbbfe2a50e8afb2f853a1181d5b4e4cc7a40ee9056003cc572b3d/27272432a8b4f4d641415bd1ef5f196cb75aa0672ab03fd9d31168918fd7526e/probability-probability-d8847fd2701b83d03368dca7-matrix.svg.

Resource-edge comparison render: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dac32ec84e8491baff35754fac5836443941eca5289e62f61e8c350500403996/caf361bab3bb6dcf52b4ced8c8fc452a5724376fab4eec0b6b060d25646b6a19/probability-probability-d8847fd2701b83d03368dca7-comparison.svg.

Resource-edge unresolved view: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98508ff1c2824c2515009363c810265fe07d93f190d7c514b71c082dd23632f9/8f84d761bafc4aca37600aa3a79d83829f073e2c2a7971302a15e5e2481a8eb3/probability-probability-d8847fd2701b83d03368dca7-unresolved.svg.

## File and ownership record

Created only this handoff: docs/plans/021_random_civil_war_plans/subagent_handoffs/probability_sponsor_resource_guards_2026-09-02.md.

No gameplay, decision, trigger, constants, manifest, configuration, or runtime file was edited by this auditor. No commit was created. Parent-owned lifecycle helpers and receipts were not touched.
