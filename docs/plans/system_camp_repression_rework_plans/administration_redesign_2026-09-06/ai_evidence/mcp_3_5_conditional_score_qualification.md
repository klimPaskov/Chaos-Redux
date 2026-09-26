# Conditional transfer willingness comparison

Disposition: implemented for the conditional source-weight comparison; route eligibility and engine behavior remain unresolved.
Acceptance basis: the user's request to fix the MCP comparison gap, using the preserved pre-edit source and the current decision without changing gameplay.

The built MCP server identified itself as `hoi4-agent-tools` 3.5.0 over stdio. `hoi4.probability_inspect` accepted the frozen baseline with its logical decision path and exact raw hash, then `hoi4.probability_compare` completed with no unresolved arithmetic. The [exact request](mcp_3_5_conditional_score_request.json) and [authoritative comparison JSON](mcp_3_5_conditional_score_comparison.json) retain the declarations, source identities, traces, and deltas. This was a local candidate-server qualification; it does not itself prove public package publication or the version in every existing client process.

The singleton candidate is `germany_transfer_prisoners_to_experiment_site`. These scenarios explicitly assume eligibility with `candidateOverrides` in order to isolate the willingness formula. The declared cap variables and `camp_ai_can_expand` flag still control the baseline's modifier; eligibility overrides do not force weight modifiers to apply.

| Declared condition | Baseline score | Current score | Delta |
| --- | ---: | ---: | ---: |
| Both caps clear | 55 | 55 | 0 |
| Site count at its cap | 0 | 55 | 55 |
| Experiment count at its cap | 0 | 55 | 55 |

The result uses the `decision_ai_will_do` score-only adapter. It establishes neither normalized click probabilities nor the actual availability, selected-source pointer, registry ordering, payment, transfer, or timer behavior in a campaign. It also does not compare whole historical workspaces: shared helpers and constants came from the configured current source. No gameplay weight was changed by this qualification.

## Source and implementation identity

- Frozen raw source SHA-256: `4e3e377165ac949b8d54cd9547c6cb6d903046b59915af4ff2dcca3a211edfd5`.
- Current raw source SHA-256: `e06525307514bb1f66b923f824a3d9ac00937202dc0194fc7ce53fab7633c0f2`.
- Comparison source revision: `70218efb4ff851fd310525e61383f6a5712af4d7af9f695e20cddcd35805db09`.
- Scenario hash: `d87681c3977cd85a5369c0e35b888e40ad620ddedc0546134bb2d0554b97e2dd`.
- Built probability service SHA-256: `78fcd2f2c06d78c5143fa52d29f9aa34c13af45f0de26eceb7f207f3a3d974b8`.
- Built shared condition evaluator SHA-256: `032c88eb4dc9cc0a0fd113dfeb1a354aca8df553bb0e240ffa5ee9a337b07377`.
- Built weight evaluator SHA-256: `bd05a03db7b5077324f1d513eac9700e244c2c4824af8b0e1e05bcfd3b583501`.

The earlier single-candidate artifact is readable through the configured resource server key `hoi4_agent_tools`. Its authoritative JSON already contains the exact current raw score 55 and an unresolved custom-tooltip eligibility wrapper; the package name with hyphens was the wrong resource server key. The candidate evaluator treats hidden and custom-tooltip wrappers as their enclosed conditions while excluding tooltip metadata. These source-level capabilities do not turn declared controller or date assumptions into engine receipts. The user reported no before/after saves, so the transfer and timer receipt gates remain open.
