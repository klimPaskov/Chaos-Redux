# MCP probability call trace

Surface: `common/scripted_effects/012_africa_gods_effects.txt` / `gods_of_africa_refresh_strength`.

Workspace: the connected MCP workspace id returned by successful reference calls was `mod_chaos_redux_ea3b2d67c2c0`; the probability calls returned no workspace id or payload.

The live exposed `hoi4.probability_inspect` schema accepts a mod-relative `source`, optional `candidatePool`, and optional adapter enum. The exposed adapter enum has no dedicated deterministic weighted-score-component route. Automatic adapter selection was used in every call by omitting `adapter`. The exact helper name was passed as the sole candidate annotation, without `customPoolManifest`.

1. Initial BEFORE inspection request: `source: { path: "common/scripted_effects/012_africa_gods_effects.txt" }`, `candidatePool: ["gods_of_africa_refresh_strength"]`. The call yielded as still running after about 31 seconds; bounded waits returned no response, and the caller terminated the wait. No artifact, adapter, revision, or scenario hash was returned.

2. Thin immutable BEFORE retry: `source.path` remained `common/scripted_effects/012_africa_gods_effects.txt`; `source.snapshotPath` was `docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_probability_2026-10-08_evidence/strength_helper_before.txt`; `source.expectedSourceHash` was `b928b86a1758fc66c11130270606cd5216883a536ee7443c93ba9f6c4f66f402`; `candidatePool` was the same exact helper; `refresh` was true. The call yielded as still running after about 31 seconds and returned no result during one bounded poll of about 16 seconds; the caller terminated the wait. No artifact, adapter, revision, or scenario hash was returned.

3. Thin immutable AFTER inspection: `source.path` remained `common/scripted_effects/012_africa_gods_effects.txt`; `source.snapshotPath` was `docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_probability_2026-10-08_evidence/strength_helper_after.txt`; `source.expectedSourceHash` was `396dfa52f7176deb4feb72707e9370dc2aa2eb8e382bdb2e9711bfcf0a953282`; `candidatePool` was the same exact helper; `refresh` was omitted. The call yielded as still running after about 31 seconds and returned no result during one bounded poll of about 11 seconds; the caller terminated the wait. No artifact, adapter, revision, or scenario hash was returned.

`hoi4.probability_compare` was not called. Its exposed schema requires a `scenarioSet`, but its type is opaque and none of the inspections returned an accepted scenario contract or recognized adapter. The parent’s production-node test rows are deterministic source-model evidence, not a saved MCP scenario set. Constructing an unverified scenario envelope would be a guessed request, so the native comparison remains unresolved.

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were not called because no probability adapter or candidate race was returned for this scalar helper. `hoi4.probability_simulate` and `hoi4.probability_sequence` were not called because the helper has no declared uncertainty or stochastic pool. `hoi4.probability_render` was not called because no analysis id or renderable MCP artifact exists.

Outcome classification: the source helper is deterministic weighted arithmetic by source inspection and parent-supplied production-node cases. The MCP adapter classification remains pending/unknown, not confirmed empty or unsupported. No probability claim, comparison id, MCP scenario id/hash, artifact URI, or rendered probability evidence was obtained.