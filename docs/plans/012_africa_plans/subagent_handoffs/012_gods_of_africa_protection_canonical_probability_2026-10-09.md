# Event012 protection canonical-completion probability audit — 2026-10-09

**Disposition:** unresolved for MCP-confirmed protection eligibility; baseline and the requested five-case after comparison are complete.

**Audited surface:** decision gods_of_africa_protect_partner, adapter decision_ai_will_do, source common/decisions/012_africa_gods_decisions.txt, definition at lines 1650–1725.

**Scope:** read-only probability audit of the canonical-completion correction. No gameplay, source, test, Git, or game files were edited by this auditor. Writes are limited to this handoff and its sibling evidence folder.

## Baseline and source identity

The parent-named baseline path had an extra of_africa segment. The repository’s actual baseline is docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_canonical_completion_2026-10-09_evidence/before/manifest.json. All four manifest SHA-256 values matched their frozen snapshots and live files at the start of this audit.

The supplied before bundle freezes the decision, the protection eligibility triggers, the general Gods triggers, and the contract effects. At the after signal, the two scripted-trigger files had changed hashes; the contract effects and decision file remained byte-identical to baseline. The after evidence folder freezes the current weighted decision file and records its manifest.

The target is gods_of_africa_protect_partner in common/decisions/012_africa_gods_decisions.txt. It is a target_array decision over gods_of_africa_participants; the scenario host is ROOT=ETH, the protected participant is FROM=GER, and event_target:africa_host=ETH.

## Scenario fixture and completeness

The same saved five-case fixture was used for baseline evaluation and before/after comparison: [scenario-set.before.json](012_gods_of_africa_protection_canonical_probability_2026-10-09_evidence/scenario-set.before.json), SHA-256 e8f591b78916c9850408d92a15715e7775f8a9dfba25cb5c7969573b04176c25; the MCP scenario hash was 1b0d7cc1811bde642337a7ca7ce42f2a7617c5fb1dc3e8abd813e5cc0ed1191e.

| Scenario | gods_of_africa_demands_fulfilled | gods_of_africa_compliance_count | Aid count / Wrath | Reliable-memory flag |
|---|---:|---:|---|---|
| ALL_PARTIAL_FINISHED_WITH_AID | 3 | 0 | 1 / 15 | absent |
| FULL_CLICK_FINISHED_WITH_AID | 3 | 3 | 1 / 15 | present |
| PARTIAL_UNFINISHED | 2 | 0 | 1 / 15 | absent |
| HIGH_WRATH | 3 | 3 | 1 / 65 | present |
| OCCUPIER | 3 | 3 | 1 / 15 | present |

The occupier fixture binds GER as controller of Ethiopian state 271, whose owner is ETH. Each case binds ROOT/host ETH and FROM/partner GER; the participant scope pool contains GER as its sole declared candidate. No candidate overrides or forced helper answers were supplied.

The one-ID candidate pool is complete only for this requested raw-score probe; it is not a complete decision-category or campaign target race. External-factor completeness is false. The scenario declares the host and participant states, flags, event target, and a one-member participant scope pool, but the evaluator leaves many source/helper inputs unresolved. The targeted inspect reported no direct required input paths, while evaluation still returned unresolved helper and trigger inputs.

## MCP results

The initial broad probability_inspect found 50 decision candidates, an incomplete pool, and required scope.FROM; it was retained only as discovery evidence. The corrected targeted inspect found one requested candidate and no direct required paths. Its poolComplete=true describes the one-candidate probe, not the full campaign pool.

Baseline probability_evaluate returned PROBABILITY_ANALYZED_PARTIAL, with zero eligible and five excluded case traces and 73 unresolved inputs. Each excluded candidate showed raw value 0/1 and conditionalProbability=null; that zero is an exclusion result, not an evaluated willingness score. No usable base value or modifier trace was returned, so this pass establishes neither the correction’s eligibility effect nor a numeric AI weight.

The before/after probability_compare used the same five-case scenario hash and the frozen before and after decision-file snapshots. It returned comparisonChanges=0, zero eligible and five excluded traces, and 74 unresolved items. The decision file hashes are identical, so this confirms the compared decision source contains no weight or cost change. The compare request did not include before/after helper overlays; the two changed helper files therefore are not historically isolated in this comparison. Do not read comparisonChanges=0 as proof that protection eligibility changed or as a probability result.

The single-path probability_sweep varied scopes.FROM.state.gods_of_africa_demands_fulfilled from 2 to 3 in the ALL_PARTIAL_FINISHED_WITH_AID fixture. It returned two points, zero eligible candidates, and 73 unresolved items. No threshold, sensitivity, or rank-reversal conclusion is supported. The one-candidate pool cannot establish a rank reversal against other decisions.

The adapter declares decision AI results as score-only and does not model normalized selection probability. No exact click probability is claimed. Dominance, starvation, rank reversal, repetition, and exploit risk remain unresolved because the candidate race and relevant external factors are incomplete and the returned cases have no usable score traces.

## Source and reference evidence

The baseline source lookup located gods_of_africa_participant_can_receive_protection in common/scripted_triggers/012_africa_gods_triggers.txt:755–777; the inspected baseline helper included the reliable-memory flag alongside relationship, generation, registration, war, event-target, and cooldown gates. The baseline gods_of_africa_ai_is_proven_partner helper at lines 1423–1428 uses the coarse compliance counter or aid count for its separate AI factor. The parent’s after-ready message reports that the protection eligibility path now uses the canonical completion counter at threshold 3 and removes the reliable-memory flag gate; the live hashes confirm the relevant trigger files changed, but this probability pass did not independently prove the source-model or focused-test behavior.

The relevant installed documentation was read from C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1–46 (revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019). It defines target_root_trigger and target_trigger scopes and checks, including ROOT and FROM on targeted decisions. The offline wiki sections paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357–374 and :531–537 (revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162) describe AI decision weights as MTTH-style willingness scoring and identify ROOT as the decision country and FROM as the target.

## Weighted findings and recommendation

The decision’s base expression is constant:gods_of_africa_ai_response.protect_base; its source modifiers are the zero factor when the protection package is unaffordable, the proven-partner factor, the shared-enemy factor, and the near-collapse factor. The analyzer reported the near-collapse modifier inactive in the submitted scenarios, but did not return usable traces for the other modifiers or numeric constants. The parent’s intended correction preserves threshold 3, costs, all remaining gates, and the decision weights.

Keep the canonical gate gods_of_africa_demands_fulfilled >= 3 and remove only the redundant reliable-memory requirement from the protection eligibility helper, as directed by the parent. Do not retune the AI weight or protection cost from this partial score evidence. The parent-reported focused test includes all-partial completion and the coarse-100-without-ledger-completion counterexample; it was not executed or independently verified in this audit.

## Skipped analyses

probability_simulate was skipped because no uncertain input distribution was declared. probability_sequence was skipped because this is not a complete custom weighted pool with cadence and state transitions. Full category ranking and normalization were not attempted because only one candidate was in scope and the campaign pool is incomplete. Structural decision availability review remains parent-owned; event-chain inspection and rendering were out of scope because this is a targeted decision-weight surface.

## Render evidence, limits, and handoff

The baseline evaluation returned unresolved SVG and PNG artifacts. The after comparison returned unresolved SVG and PNG artifacts. The sweep returned threshold, sensitivity, and unresolved SVG/PNG artifacts. Their URIs and all source revisions, hashes, scenario hashes, and analysis IDs are recorded in [mcp_receipts.json](012_gods_of_africa_protection_canonical_probability_2026-10-09_evidence/mcp_receipts.json).

Explicit probability_render calls for the baseline unresolved view and after-sweep threshold/sensitivity/unresolved views returned PROBABILITY_ANALYSIS_STALE (analysisRevision=c83c4eba99270de25fc7404460a243b60156cf9ce6bba6924142fd704b49d7bd, currentRevision=7fb5ef64f6dc24bba266563a98d1e90892f16195b5ab9b2477cffd5b75f5a44f; and analysisRevision=74a21bf8ee2bd6607ddf8e98e9f61a61f23025d9e428f30d2c36f4ee7fee13ca, currentRevision=19a1ea454b26c6443a8b0b8954229c442075acfc24f3bf3b770667def010c292). Each returned no rendered visual resource. No further render or ranking pass was run.

**Completed:** baseline inspect, five-case baseline evaluation and after comparison, one canonical-counter boundary sweep, source/hash identity checks, offline wiki and installed documentation reads, and this read-only handoff.

**Unresolved:** MCP proof that the new helper admits the all-partial case while retaining unfinished-partial, high-Wrath, occupier, war, core, unresolved-hostility, and cooldown gates. The parent’s source-model and focused-test evidence remains the authority for that actual-case claim. No test or in-game run was performed by this auditor.

**Skills used:** chaos-redux-subagents and chaos-redux-decisions-missions. No skill files were created or updated.
