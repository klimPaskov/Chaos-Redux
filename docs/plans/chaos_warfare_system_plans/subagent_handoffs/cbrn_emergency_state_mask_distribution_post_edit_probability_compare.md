# `cbrn_emergency_state_mask_distribution` Post-Edit Probability Pass

Status: post-edit source inspection completed; the comparison is unresolved because the MCP compare request rejected historical source identity fields and no exact pre-edit source file is available.

## Source identities

The analyzed weighted surface remains `cbrn_emergency_state_mask_distribution` in `common/decisions/cbrn_protection_decisions.txt`.

Pre-edit evidence from the baseline handoff records local Git revision `e4c197bba88a5f6c748eb5ede0c062700e83e769`, local decision-file SHA-256 `7c029e52c4344b8503cde7257cc4d8d27ee9992e659666751e374ca70fa60a2b`, MCP evaluation revision `a76d6ac48f2ace9c10db31394d4c5fb06007afcf8a07ca27aad70a27d213c8b0`, and MCP source hash `9981b52f2d2f96f5aa2546cb52fed7de41eef9093cc49e0fc0e1b4aaee4ad3ae`.

The frozen post-edit workspace had local Git revision `9e9f6efd2ee52eae71007119335cbd68d1e69d3b`, decision-file SHA-256 `2c4cc22fa39c0a05d33810d66f4c07c50862ec1f4e160ef8fa5ec18e6cdab276`, and modified helper-trigger file SHA-256 `4f80bca22f449e977f0d4f53fc941dc1e80d0b64e824dd37218607a7baf51e7d`. `common/scripted_triggers/cbrn_triggers.txt` remained `892391b2ec11cb022f885cc69e21ad9c48c616f62b4747425ffb9155434caf4a`, and `common/script_constants/cbrn_system_constants.txt` remained `3dae2d3ab97cccb78f0164dca1854ee0801cee04f68f1ed83146e0d1f1a6971f`.

The post-edit `hoi4.probability_inspect` selected `decision_ai_will_do`, reported five candidates in the inspected file, `poolComplete: false`, zero available candidates, two required inputs, and zero unresolved inputs at inspection time. Its source revision was `b79179665b409b28c4212d672ebff0a3321796a398bc78c9ed61a981fa90cab7`; its source hash was `a4b3fac687c2c20501f45eaefe780d138c26b4b960c98960e8135dafe8a618c0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35094625c7b5011059fef92413754850aae0bfbb63de3c6b61e90d4a56614947/36498d00b460e3bb12ab20d4465c8c9e7d428bf0bf8d4ce5e4c496a93ea68baa/probability-inspect-a4b3fac687c2.json`.

## Fixture and comparison attempt

The saved fixture [cbrn_emergency_state_mask_distribution_baseline_fixture.json](cbrn_emergency_state_mask_distribution_baseline_fixture.json) was supplied unchanged, with candidate pool `["cbrn_emergency_state_mask_distribution"]` and scenario set `cbrn_emergency_state_mask_distribution_baseline_2026-09-25`. Its pre-edit evaluation scenario hash was `6edad30d3de7b147eeef0e91fdd533a75610998d99fc2199a8df6c8c92a67e1`.

One `hoi4.probability_compare` attempt used the pre-edit source path and recorded source revision/hash in `before`, and the frozen post-edit path and revision/hash in `after`. The tool returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Unrecognized keys: "sourceRevision", "sourceHash" at before; Unrecognized keys: "sourceRevision", "sourceHash" at after`. It returned no comparison id, scenario hash, source revision, artifact, or rendered evidence.

The same nonempty path would be required for both `before.path` and `after.path` to name this decision, but only the post-edit working file is available. The prior handoff preserves the pre-edit hash/revision and fixture, not the old source file. The Git blob at the recorded pre-edit revision has SHA-256 `c85b5e58bf79a3bba84aea0fcfc75e3e6729cfd3be570413eee74e424dad1e2e`, which does not match the recorded pre-edit working-file hash; it therefore cannot be presented as an exact historical source snapshot. Per the probability skill, the current source was not supplied as both sides of a purported historical comparison.

No post-edit `hoi4.probability_evaluate` artifact was produced after the single compare attempt failed; further MCP retries were stopped as requested. There is no post-edit scenario hash to report. The baseline evaluation artifact and its ranking/unresolved render URIs remain in the baseline handoff.

## Findings and limits

The current source diff leaves the decision's `ai_will_do` base and its alert, contamination, and capital modifiers textually unchanged. It replaces the native 10 PP cost with `ai_hint_pp_cost`, adds custom affordability/cost rows, and changes `cbrn_state_has_emergency_distribution_gap` to use the variable mask reservation quote. This is source-review evidence only; no MCP comparison proves that the weighted result is unchanged.

The baseline scenario hash remains the only evaluated hash. Its `has_equipment` value did not bind the compound stock trigger, and its primitive fixture did not resolve target state ownership, population, contamination variables, emergency distribution coverage, capital status, or custom reservation quote inputs. The named stock exact/above and eligible/stale cases remain collapsed or unresolved; PP values 9/10/11 do not prove post-edit affordability. Candidate-pool completeness for target states and category-wide selection remains unresolved, and the adapter remains score-only with no click-probability normalization.

Classification: the unchanged weight expression is verified by source diff; current effective score, eligibility, post-edit rank, stock threshold behavior, PP affordability, target-pool competition, and before/after comparison are unresolved. No starvation, dominance, repetition, or exploit conclusion can be made from this result.

No gameplay or AI source was edited by this auditor. The parent should provide an exact historical pre-edit source file or a supported revision-addressable compare input before a probability comparison is claimed.
