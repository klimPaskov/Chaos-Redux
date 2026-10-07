# Biological native-raid probability audit for the temporary-output patch

Date: 2026-10-07.
Disposition: MCP-verified candidate structure for one reached random list, with numeric probability and before/after delta unresolved.
Mode: read-only audit of the frozen 63-declaration patch.
Baseline HEAD recorded by the patch manifest: c0f14281546a4b8f38a07349b752bfbd65e4c55d.
The baseline manifest records a mixed working tree, and this worker made no gameplay, AI, event, focus, decision, technology, index, or commit changes.

## Scope and source identity

The reviewed ordinary routes are bio_resolve_battlefield_dissemination, bio_resolve_strategic_raid_outcome, and bio_resolve_supply_chain_raid_outcome.
They are called from the biological battlefield, strategic, and sabotage raid definitions and hidden bridge event.
The exact scoped effect files are common\scripted_effects\biological_battlefield_effects.txt, common\scripted_effects\biological_raid_effects.txt, common\scripted_effects\biological_sabotage_raid_effects.txt, common\scripted_effects\biological_lifecycle_effects.txt, and common\scripted_effects\cbrn_diplomacy_effects.txt.
The native definitions are common\raids\biological_battlefield_raids.txt, common\raids\biological_raids.txt, and common\raids\biological_sabotage_raids.txt.
The bridge source is events\biological_native_raid_bridge_events.txt.
The prior caller map is docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-07_biological_raid_lifetime_audit.md.
The frozen insertion record is docs\testing\2026-10-07_biological_raid_lifetime\insertion_manifest.json.

Normalized source proof is exact for all five modified effect files.
Removing each manifest-recorded inserted statement at its frozen afterLine reproduces the entire before-snapshot SHA-256.
The current hashes also match the frozen patch handoff hashes.

| File | Before and normalized SHA-256 | Frozen/current SHA-256 | Insertions |
| --- | --- | --- | ---: |
| biological_battlefield_effects.txt | 441dc4dca276178b5489eb79f2f9af6519d53532ef3f9237b61f127d56ed7811 | 4c35b1c87c04ca027421a5d1a63f45ae1b42df29e6f65d5c9c2a3846078e7791 | 7 |
| biological_raid_effects.txt | c3ecff927917a2bd444123731cbd1accbb4c7ecd06c704d7d58d2aeb5b6a0b4b | b05ecae13e35c12b0e227114fa88206753dcb281b0d6fd448dd8f54fa9950080 | 5 |
| biological_sabotage_raid_effects.txt | f3c222581ebf7d6d518c0c4eec8dea3e35b8fd4d515288fde75f25b1b8465716 | f21e979a586b92519642db7e309ef098a2e2733f1d9b0ef6078831be6ee9b9bc | 4 |
| biological_lifecycle_effects.txt | 898724cc42eab7a09c12173b493902c1b8695fdd961251f169c947107f97965d | 3d611e3424da6f221446810f6f4ad49e4065b1a8c066bcf7bec3989038a5d3cc | 2 |
| cbrn_diplomacy_effects.txt | c005b6687b816c9fd8d09e1749f289a19239e63335afbd6c19641c7a33ef14d2 | 60b8c4c70a018328e64f19c8e2c5caf7cbbbfcbb99928f5c0b538b1d53278042 | 1 |

Machine-readable requests, outcomes, source hashes, and reference spans are retained under docs\testing\2026-10-07_biological_raid_probability\.

## Reached random surfaces and MCP coverage

The mandatory first probability inspection used hoi4.probability_inspect on biological_battlefield_effects.txt.
It found the random_list adapter and exactly two entries in bio_battlefield_attempt_friendly_blowback_internal at line 353.
Candidate identifiers are common/scripted_effects/biological_battlefield_effects.txt:353.entry.1 and common/scripted_effects/biological_battlefield_effects.txt:353.entry.2.
Candidate provenance SHA-256 equals the frozen current file hash 4c35b1c87c04ca027421a5d1a63f45ae1b42df29e6f65d5c9c2a3846078e7791.
Inspect source revision: 8c6885e19602bd833f1bfd9c248b776df2ab0c6f8106dec00395edc4565d03aa.
Inspect inventory hash: dda620d6da0f1ad573cd44371815521513ced4059510669654672e39ace8d71b.
Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3c60a303a7c2f067465b0907b98b370bfb455f5220c8dd7b4fea7e2a2efecd2/619b5373625833ae345b330ae2d6d9fc3d5f1555dcb02845dcd003a8764d22ce/probability-inspect-dda620d6da0f.json.
The inspect JSON was fully retrieved as 2,386 bytes.

The named scenario is biological_battlefield_blowback_audit / blowback_weights_unbound_external_factors, dated 1936-01-01.
The exact submitted input is docs\testing\2026-10-07_biological_raid_probability\scenario_set.json.
It contains an empty state record required by the live validator and no actor, victim, target, flag, or helper-return override.
MCP says the two-entry candidate pool is complete and both candidate entry gates are true.
It leaves the weights bio_battlefield_blowback_chance and bio_battlefield_no_blowback_chance unresolved.
Both raw values and conditional probabilities are null, both candidates have supportLevel unsupported, and the analysis is partial.
Scenario hash: ed77f49161457542352b003b1357d935e76d16de39f229d4f1b232ab59bc5888.
Candidate-pool hash: 60edc14b046be428b2d635717e52019c92c3bd08e5d0f49964585e9560efc9db.
Analysis ID: probability-6459113bd68b2f97446bae40.
Analysis source revision: 7d6cff909577a2e0a94508ace645040f30626c5973ac3f423c72c4177732b266.
Analysis JSON, fully retrieved across byte range 0-13007: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f14d1d6f672b728f990da43aefb464eba8b17f6ad548fae224ba14dfec1ba3f3/ea2349c56e1671ea7cd0e2384737d2d9395dfcf1ad68855f29cf7d4cb7229ea4/probability-6459113bd68b2f97446bae40.json.

The evaluator returned ranking SVG/PNG and unresolved SVG/PNG resources.
Their bodies were not retrieved locally, so their MCP URIs and declared sizes are retained as evidence.
Ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/467847ff6e0a30c444b4146e53b756b16c88be5db0ec63cd3db5026a634d2373/415e43e8b24236766d02e4acf95c274810c1885ae719ae33c1390aadde686e7f/probability-probability-6459113bd68b2f97446bae40-ranking.svg.
Ranking PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef300dde7a2312c70e14a39e572201833b1080eeeee1adfda86b2a29c5b8dac/5b2f233ff275dcc8852f805a940561b66cb8d1ef312b819cefd0f605644b32da/probability-probability-6459113bd68b2f97446bae40-ranking.png.
Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e78a6f065b63f8a7566902250e36035a122ad6d82f52967e6368307c3ef5878/84e4efd2d91bb9507a908e6cb65e710f4b3b3f41235b7524dac570cb00aa36bd/probability-probability-6459113bd68b2f97446bae40-unresolved.svg.
Unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a18b9e44ea1f234ccb20d6a06efc08d2d1ab55ad57b5cffb3c4a88a8ed4d8c1/620e917918b2b704dfb45e8a319079b5680d893093fef567cd3b04dc65e27d87/probability-probability-6459113bd68b2f97446bae40-unresolved.png.

The exact submitted probability_compare argument object is retained under compare.request in docs\testing\2026-10-07_biological_raid_probability\probability_evidence.json.
It used the before snapshot path object and current source path object, but candidatePool contained the current-source identifiers ending in line 353.entry.1 and line 353.entry.2 for both sides.
The before snapshot has different source-path and line-position candidate identifiers after removal of the 63 insertions, so the current-only candidate keys could themselves explain PROBABILITY_SURFACE_EMPTY.
The tool returned No weighted blocks matched this request and filesScanned was empty, without identifying whether the before path, candidate selector, or both caused the empty surface.
The cause of PROBABILITY_SURFACE_EMPTY is unresolved, and this result does not prove that the snapshot path is unsupported or that the route is unavailable.
The numeric before/after delta is unresolved, and a correctly remapped before/current candidate-pool comparison remains required.
Current-to-itself comparison was not attempted.

An explicit probability_render request for ranking and unresolved views returned PROBABILITY_ANALYSIS_STALE.
The tool reported analysis revision 7d6cff909577a2e0a94508ace645040f30626c5973ac3f423c72c4177732b266 versus current revision 5e94ee800b328e5b82486ac0480b12e339565b79ad9fbff84524e1c7be235acf, requested re-analysis, and returned zero visual resources.
No rerun was made after parent steering to freeze evidence.
The evaluator-generated view URIs above remain tied to the original evaluation provenance.

Probability inspection on biological_sabotage_raid_effects.txt returned no_weighted_surfaces with zero candidates.
Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af5199de0466b3b9b0d6884121183cf68d6a60a55d39797620739e716fee8da8/0f656ffa3749263857e4e94666759ddc2963e4c7b905d75367b9c8902ce08a80/probability-inspect-595d240f2c6e.json.
The sabotage resolver maps native engine outcomes deterministically and contains no source random_list block.
The exact strategic and lifecycle source inspections each timed out with the client error timed out awaiting tools/call after 600s.
They were not retried after parent steering against further inspect breadth.

## Source review of other reached randomness

The strategic resolver reaches two branch-local random_list blocks in bio_strategic_raid_select_outcome_internal.
The failure pool has bio_raid_failed_delivery_weight and bio_raid_attacker_accident_weight, with actor insecurity and actor technology, HQ, designer, and containment factors modifying the latter.
The success pool has bio_raid_hidden_contamination_weight and bio_raid_detected_seed_weight, with actor attribution and precision-release effects on the former and victim surveillance or response technologies on the latter.
Each source pool contains two entries.
The strategic MCP inspection timed out, so its source pools have no MCP-confirmed coverage, numeric trace, ranking, or probability.
No balance conclusion is based on those source expressions.

The strategic resolver also reaches bio_strategic_raid_select_internal_handling_state.
It prefers a valid capital and otherwise invokes random_owned_controlled_state for states passing the handling-candidate limit.
This has no weighted table and depends on current ownership, control, capital validity, and the source predicate.
No state-selection probability is claimed.

A valid seed dispatch reaches bio_lifecycle_schedule_incubation_for_current_agent, then bio_lifecycle_prepare_incubation_delay and set_temp_variable_to_random.
The source selects agent-specific base and random-day constants, draws from the documented default [0, 1) range, scales and adds the draw, then rounds and clamps it.
The patch gives the accepted agent selector caller-owned storage across the helper return, so this correct-agent scheduling branch can survive.
The lifecycle MCP inspection timed out, and no numeric delay distribution is claimed.
Detection random selection occurs later on activation when forced detection is absent, while spread random selection occurs in later lifecycle ticks.
Those later choices are outside the immediate resolver path.
The reached biological retaliation classifier in cbrn_diplomacy_effects.txt is deterministic and contains no random-list or random-number operation.

## Findings

The battlefield candidate pool and entry identities are exact MCP findings.
MCP confirms both static entries are eligible, but it cannot resolve either effect-derived temporary weight from the submitted source and scenario.
Scenario external factors are incomplete because no real actor, victim, target state, readiness, protection, doctrine, or eligible-neighbor context is bound.
No numeric probability, expected branch frequency, timing estimate, bounded range, sampled result, score-only result, rank, dominance, starvation, or rank reversal is established.
The null ranks and the analyzer's zero-gap closest-rank-reversal diagnostic are consequences of unresolved values, not a measured tie or reversal.

The selected blowback entry has a later outcome gate.
It searches an adjacent actor-controlled eligible state containing an actor-owned division and does nothing when none exists.
A selected branch therefore does not prove friendly seed or exposure.
Any future scenario or player-facing statement must separate weighted branch selection from child-effect target validity.

This task covers scripted outcome randomness, not AI willingness or strategy-factor scores.
No native raid success_levels probability adapter was exposed by the live inventory, so engine completion chances remain unresolved and separate from the scripted random lists.
The parent reported event_compare status EVENT_REVISION_NOT_CACHED with no artifact URI supplied.
The parent reported script_validate as partial: 153 commands, zero findings, five unknown roots, and 82 unchecked argument blocks.
Those parent results are context only and do not substitute for probability evidence.
Callback cardinality, repeat suppression, and live transaction behavior remain unresolved.

## Recommendations and blockers

Do not retune the battlefield random-list weights from this evidence.
The complete two-entry pool still has unresolved effect-derived weights, and the same-scenario compare returned no matched surface.
The strategic random lists and incubation timing remain unassessed by MCP due to the exact inspect timeouts.
If the parent later retries, keep the same candidate pools and scenario identity and provide only schema-supported actor and state bindings that resolve the source values, without helper-return overrides.
If the analyzer cannot bind those values, preserve the unresolved result and report weighted-branch selection separately from whether its target-gated child effect runs.
Native raid success levels need an analyzer route that supports that engine surface before end-to-end completion chance is stated.

No weights, thresholds, candidates, routes, or gameplay files were changed by this worker.
No simulation, sweep, sequence, tests, or live-game claim was made.
Skills read: chaos-redux-subagents, chaos-redux-native-raids, and chaos-redux-events.
