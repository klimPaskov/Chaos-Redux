# Chemical native-raid caller-storage probability audit

Date: 2026-10-07.
Disposition: the five exact scripted random draws are preserved in source, while direct_random adapter coverage and their numeric distributions remain unresolved.
Mode: read-only audit of the frozen chemical caller-storage patch.

## Baseline and source identity

The source manifest records baseline HEAD 9c3418607b164096d4c3ddaf3e7f380c576bb669.
The frozen patch covers six files and 207 caller-owned declarations.
The scoped common\scripted_effects\cbrn_chemical_raid_effects.txt file contains 67 scalar declarations in that patch.
Its exact before archive hash is b770477f77423347eeda57e644ee3acfa3eb6aae9e492347a9ff71e049c67d8c.
Its after archive and current source hash are both 30b3238b2e3aab404e7709bd3a911e8e5e4f6fe8b4e30439087b8bf67836d385.
The normalized text segment from lines 58-155 has SHA-256 1308f2589f18812c954f258cd6278b9b3a24b6c5f0e250ee3ff8eb3e7f1e1ab3 in the before archive, after archive, and current source.
All five draws occur before the inserted owner block around line 223, and their original line positions remain 65, 113, 120, 135, and 142.
This source-only equality proves that these draw bodies, bounds, and threshold are unchanged across the caller-storage patch.

## Reached scripted random draws

Line 65 belongs to cbrn_chemical_air_raid_select_failure_result_internal.
It draws cbrn_raid_failure_split_roll between the script constants cbrn_chemical_raid_resolution.random_minimum and random_maximum.
The helper compares that draw with cbrn_chemical_raid_resolution.aborted_failure_split and sets cbrn_raid_result to aborted or failed.
This branch runs only after the native engine result is failure.

Lines 113 and 120 belong to cbrn_chemical_air_raid_set_consumption_and_dose_internal.
Both draw cbrn_raid_intended_dose_ratio for a partial native success.
Controlled dispersal selects the cbrn_aerosol_designer_effect.controlled_partial_dose_min/max constants at line 113.
Without controlled dispersal, the draw uses cbrn_chemical_raid_outcome.partial_dose_min/max at line 120.

Lines 135 and 142 draw the same cbrn_raid_intended_dose_ratio for a catastrophic native outcome.
Controlled dispersal selects cbrn_aerosol_designer_effect.controlled_catastrophic_dose_min/max at line 135.
Without controlled dispersal, the draw uses cbrn_chemical_raid_outcome.catastrophic_dose_min/max at line 142.
A successful native result assigns cbrn_chemical_raid_outcome.success_dose directly and does not use these dose draws.
The outer reservation helper calls the dose helper only after a valid agent class and non-none result.

These are continuous script-variable draws with numeric bounds, not a discrete random_list candidate pool.
The failure draw selects one of two deterministic result branches after the scalar is drawn.
The four dose draws choose a scalar interval used in downstream output calculations.
Pool normalization, weighted dominance, starvation, and rank reversal do not apply to these five draws.

## MCP probability inspection

The live probability-inspect schema accepts adapter direct_random, and source is exposed as an unknown input type.
Each request used the exact source path and one of the five parent-named lines with refresh true.
All five calls returned PROBABILITY_SOURCE_DISCOVERED with discoveryReason no_weighted_surfaces, zero candidates, zero required inputs, and no unresolved inputs.
The adapter inventory exposed 11 adapters, but none matched the named getter surface.
The exact submitted requests, returned source revisions, hashes, and artifact URIs are in docs\testing\2026-10-07_chemical_raid_probability\probability_inspect_requests_results.json.

Line 65 source revision: 0fd3084ad4055fb482b86866c529f0849077202567879368366b4ccaac83b86b.
Its inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9514c0160e2566f95c39f78221fa73d7bb49b79dfc81a09dd18a0fd66c38d7c9/1cc647358563adcb7cf15050c2ddc41edb4fe83d08f895e5418859c814c525c9/probability-inspect-c2edcf4a3d81.json.
Lines 113 and 120 source revision: 0a262f80b0e5f94b31c2d91cbe2a41083c04ec86630f0ed6e191b001af99e24e.
Line 135 returned the same source revision and artifact.
Their shared inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b4cbafae8279f6c5713869ff2f854f51b400230c91f4121bf534675154f4e9b/44d9ec35950c45966c671b5d859c61e24cc43a902f5fa07f6f8b0de2c3a8be/probability-inspect-c2edcf4a3d81.json.
Line 142 source revision: c1bd1933a39e1cb7d43144b3536c8d1447c0dd83c641cbd4d4c04ed76112319b.
Its inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc388cb8581e6f73b22e1fab75c27f012acfe827900a71144eb35b6c11ee95c4/883072c32c4c9d478aee427854be823079c046a5652f2a166f739906f9587549/probability-inspect-c2edcf4a3d81.json.
Each artifact link declares 384 bytes, and no artifact body was retrieved.

The adapter result does not establish whether direct_random intentionally excludes set_temp_variable_to_random or needs a different supported source representation.
It does not prove the draws are constant, impossible, or zero probability.
No candidate IDs or required scenario inputs were returned, so no four-branch evaluation or numeric range result was submitted.
No probability_compare was submitted because no candidate mapping exists, and the parent owns the broader comparator graph.
No sweep, simulation, sequence, or render is applicable without an analysis ID or supported input model.

## Reference basis

The offline Paradox wiki Effects page has the set_variable_to_random row at line 707.
The installed Hearts of Iron IV effects documentation section set_variable_to_random spans lines 7910-7926 at source revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
The installed documentation defines the draw's half-open min/max range, while this source supplies explicit constant-backed bounds for all five draws.
The exact documentation references were already read in the prior bounded timing audit and are recorded under docs\testing\2026-10-07_biological_raid_probability\reference_manifest.json.

## Sampled and tested limits

The parent reports an 18-case source suite for this patch using the native-success air-raid path.
That suite explicitly does not evaluate the native-failure split or the partial and catastrophic random-dose branches.
It is source-lifetime coverage, not a sampled distribution or gameplay frequency estimate.
No statistical random samples, Monte Carlo simulations, or live-game observations were supplied or run.

Native raid success-level probabilities are a separate engine surface.
This audit analyzes only conditional script randomness after the native engine result has already been selected.
No end-to-end raid success probability is claimed.

## Findings and recommendation

The source inspection proves that all five random getter bodies, min/max expressions, and failure threshold are unchanged by the frozen caller-storage patch.
The MCP probability tool did not surface any of those draws as a supported direct_random candidate, so their numeric distributions and the exact returned-value lifetime are unresolved by the analyzer.
Keep the original random bounds and result mapping while reviewing the caller-owned outputs.
Do not retune these values based on this audit.
If the probability adapter later supports these getter blocks, evaluate failure, partial, controlled partial, catastrophic, and controlled catastrophic cases only with schema-supported inputs and exact before/after source identifiers.
Parent-owned comparator graph work and native raid engine probabilities remain separate.

No gameplay, AI, event, or runtime source was changed by this worker.
Skills used: chaos-redux-subagents, chaos-redux-native-raids, and chaos-redux-events.
