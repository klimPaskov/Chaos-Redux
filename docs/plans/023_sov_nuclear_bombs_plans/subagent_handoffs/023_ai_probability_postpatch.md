# Event 023 AI probability post-patch handoff

Status: implemented with MCP evidence limits recorded.

Scope: read-only post-patch audit of Event 023 target selection and mission/decision weighting. The owner-applied target-factor patch is present in `common/script_constants/023_sov_nuclear_bombs_constants.txt`; this handoff records the required same-scenario inspection, evaluation, and comparison evidence.

## Candidate pool

The bounded target pool contains exactly these twelve targetable decisions: `sov_nuclear_bombs_operational_command`, `sov_nuclear_bombs_collapse_command`, `sov_nuclear_bombs_harden_storage_site`, `sov_nuclear_bombs_disperse_reserve_package`, `sov_nuclear_bombs_expand_fissile_production`, `sov_nuclear_bombs_survey_remote_test_state`, `sov_nuclear_bombs_select_coercion_target`, `sov_nuclear_bombs_redirect_strike_state`, `sov_nuclear_bombs_select_retaliation_target`, `sov_nuclear_bombs_select_disputed_depot`, `sov_nuclear_bombs_select_dismantlement_site`, and `sov_nuclear_bombs_breakaway_request_return`.

The MCP candidate-pool inspection reported `count=12`, `poolComplete=true`, `availableCandidates=0`, `requiredInputs=7`, and `unresolvedInputs=0`.

## MCP evidence

The mission/decision inspection used the current Event 023 source and returned the following artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46a2c513.../f5b20e65.../probability-inspect-cbbd14a0088a.json`

The bounded twelve-target pool inspection returned:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fddc958.../b07bea0e.../probability-inspect-cbbd14a0088a.json`

The post-patch evaluation used the same named candidate pool and the same three-scenario set. It returned analysis `probability-c2b7ed1203c90154cee7ae47`, source revision `3adea0...`, source hash `cbbd14...`, scenario hash `7889ef3...`, `scenarios=3`, `candidates=36`, `unresolved=46`, `diagnostics=14`, and `visualResources=6`.

Post-patch evaluation artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/849f415d.../19c51ef.../probability-c2b7ed1203c90154cee7ae47.json`

The mandatory comparison used the same scenario set and candidate pool against an in-memory reconstructed pre-patch source with the eight Event 023 target-factor modifier fragments removed. It did not write that reconstructed source to the repository. The comparison returned analysis `probability-1f8161a897643df6a774a43e`, source hash `9f3ac3...`, scenario hash `7889ef3...`, `scenarios=3`, `candidates=36`, `unresolved=63`, `diagnostics=14`, `comparisonChanges=36`, and `visualResources=6`.

Comparison artifacts:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82d7950e.../32f732ff.../probability-1f8161a897643df6a774a43e.json`

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/436d7ae1.../7ff474d2.../probability-probability-1f8161a897643df6a774a43e-comparison.svg`

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/781821d7.../f4b5f758.../probability-probability-1f8161a897643df6a774a43e-comparison.png`

## Limitation

The MCP adapter could not bind the nested country/state flags and event-target conditions in the supplied flat scenarios. As a result, every evaluated candidate was reported as never eligible under the adapter scenarios and the result remains `PROBABILITY_ANALYZED_PARTIAL`. The evidence proves the candidate surface and records the before/after comparison, but it is not a normalized gameplay probability claim. Live scenario validation remains a user-owned check.

