# Event 008 Post-patch Probability Compare — 2026-10-05

**Status: incomplete; no comparison artifact was returned.** This read-only handoff records the required `hoi4.probability_compare` attempts after the owner’s Event 008 source changes. Every completed compare call returned the exact 600-second MCP timeout; the final post-marker batch remained pending and was stopped at the parent’s instruction. No numeric source delta, ranking, timing result, scenario hash, comparison ID, or rendered artifact is available.

No gameplay, AI, event, trigger, idea, or tuning source was edited by this auditor. Temporary baseline copies and the exact submitted scenario-set JSON were created under `.tools\tmp\008_probability_compare_2026-10-05\` because no original source snapshot files existed.

## Baseline copies and current source identities

The prior baseline handoff records capture commit `8d0a28d7fe9866113718bf41a54c33996a76c722` and exact working-tree hashes for the two subsequently edited files. Their Git blobs use LF line endings; I reconstructed byte copies with the captured CRLF working-tree form and verified both SHA-256 values match the original baseline handoff exactly.

| Surface | `before.path` | Baseline SHA-256 | `after.path` | After SHA-256 at final attempt |
| --- | --- | --- | --- | --- |
| Event 008 gates | `.tools/tmp/008_probability_compare_2026-10-05/before/common_scripted_triggers_008_tensions_rising_triggers.txt` | `FDC722EF70F6C8901472D46052F8EE0A49ADD7583F15C558A11698FFDFB727D4` | `common/scripted_triggers/008_tensions_rising_triggers.txt` | `9A79F56008BB7F6C2B6A3A6F89AF9ACC9D42FADE3938724255D035C67DEC687E` |
| Follow-ups, pulse, and AI posture helper | `.tools/tmp/008_probability_compare_2026-10-05/before/common_scripted_effects_008_tensions_rising_effects.txt` | `4A912025DCFD60634BE365DEB9666FC0627FA88373E43E78B1E4CAE3A9ABAE65` | `common/scripted_effects/008_tensions_rising_effects.txt` | `1467A556530B7B1147A9D70A66AA06E6CA519ACBD26114FD8FCE435AD8A89A86` |

The scenario input fixture is `.tools\tmp\008_probability_compare_2026-10-05\scenario_sets.json`, SHA-256 `EDC97F230E6EAD66DC091F7EFBF778213F914343A13B50029CF2A5F5493BCF4F`. This is a local request-fixture hash, not an MCP scenario hash.

Two earlier compare batches used changing after-source bytes. Batch one was submitted with trigger/effect hashes `03BDEC22307B94C75314BD4D9D8D069407457B1A9EAD30508534738722D1D7B0` and `7646C39D3AC24F764A9B4E0C1943E03BBB349C33F2F71C90B3912254B8856367`; its four adapter calls all returned the exact 600-second timeout. The line-ending-normalized batch was submitted with hashes `9A79F56008BB7F6C2B6A3A6F89AF9ACC9D42FADE3938724255D035C67DEC687E` and `263F1CBC530DA64A667D78A6D3D192199FFF9F502523525A587D806533169B5C`; the wait handle was later unavailable (`exec cell 94 not found`), so no terminal MCP result or artifact was recovered for that batch. The owner then refreshed the One Denial actor-window marker; the final attempt below used the current effects hash `1467A556...` alongside the unchanged trigger hash.

## Submitted scenario sets and fixture limits

The live compare schema required `scenarioSet.id` and each `scenarioSet.scenarios[i].id` plus a record-valued `state`. Every submitted scenario used `actor = USA`, `date = 1936.1.1`, and `state = {}`. The baseline handoff’s stage/tension/flag descriptions were retained in scenario IDs and the baseline scenario table, but no unverified flag aliases or candidate state were inserted into the request. Therefore these are named empty-state comparison fixtures, not evaluated campaign scenarios.

| Scenario-set ID | Scenario IDs | Intended surface |
| --- | --- | --- |
| `E008_POSTPATCH_FOLLOWUP_COMPARE_2026-10-05` | `e008-followup-stage1-below-fullWT`, `e008-followup-stage1-fullWT`, `e008-followup-stage2-below-fullWT-no-relation-damage`, `e008-followup-stage2-fullWT-no-relation-damage`, `e008-followup-stage2-recent-relation-damage`, `e008-followup-stage3-below-fullWT-no-relation-damage`, `e008-followup-stage3-fullWT-no-relation-damage`, `e008-followup-stage3-fullWT-recent-relation-damage`, `e008-followup-stage4-first-briefing-fullWT`, `e008-followup-stage4-first-briefing-below-fullWT`, `e008-followup-stage4-recent-relation-damage`, `e008-followup-stage4-after-briefing-fullWT`, `e008-followup-stage4-after-briefing-below-fullWT` | Five branch-local `random_list` pools and Stage I/II full-tension precedence. |
| `E008_POSTPATCH_ROOT_POOL_COMPARE_2026-10-05` | `e008-root-pool-USA-1936-01-01-calm`, `e008-root-pool-USA-1936-01-01-stage0-fullWT`, `e008-root-pool-USA-1936-01-01-stage1-fullWT` | Event 8 stage/evolution/world-tension eligibility. |
| `E008_POSTPATCH_TIMER_COMPARE_2026-10-05` | `e008-followup-stage1-fullWT`, `e008-followup-stage2-fullWT-no-relation-damage`, `e008-followup-stage3-fullWT-no-relation-damage`, `e008-followup-stage4-after-briefing-fullWT` | Timer-pulse draw and expiry/cadence consequences, requested with a 365-day horizon. |
| `E008_POSTPATCH_AI_COMPARE_2026-10-05` | `e008-ai-posture-stage1-USA-1936-01-01`, `e008-ai-posture-stage2-USA-1936-01-01`, `e008-ai-posture-stage3-USA-1936-01-01`, `e008-ai-posture-stage4-USA-1936-01-01` | Stage-specific timed AI-idea application and modifier context. |

The literal follow-up candidate IDs remain present in the source pool rows, so the `random_list` compare omitted an external `candidatePool` override and left the parsed rows as the candidate source. The global automatic event pool is not complete in the scenario fixture: its active candidates and weights depend on the full event registry, settings, fired/disabled flags, caps, chaos tier, world tension, and event-specific eligibility gates. No custom-pool manifest was supplied for that surface.

The border-war actor/target/state sets also remain incomplete without a campaign snapshot of country validity, AI status, divisions, wars, subjects, factions, cooldowns, neighbor states, and control. The AI posture candidate set has the same limitation. Empty state records do not resolve these inputs.

## Compare calls and results

| Batch | Adapter | Before/after source | Scenario set | Result |
| --- | --- | --- | --- | --- |
| Initial post-edit attempt | `random_list` | Event 008 effects snapshot to current effects path; initial after hash `7646C39D...` | `E008_POSTPATCH_FOLLOWUP_COMPARE_2026-10-05` | `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`. No comparison artifact or source revision. |
| Initial post-edit attempt | `custom_weighted_pool` | Event 008 trigger snapshot to current trigger path; initial after hash `03BDEC22...`; no pool manifest supplied | `E008_POSTPATCH_ROOT_POOL_COMPARE_2026-10-05` | Same exact 600-second timeout. No comparison artifact, pool result, or source revision. |
| Initial post-edit attempt | `direct_random` | Event 008 effects snapshot to current effects path; initial after hash `7646C39D...`; horizon 365 days | `E008_POSTPATCH_TIMER_COMPARE_2026-10-05` | Same exact 600-second timeout. No timing or comparison artifact. |
| Initial post-edit attempt | `ai_strategy_factor` | Event 008 effects snapshot to current effects path; initial after hash `7646C39D...` | `E008_POSTPATCH_AI_COMPARE_2026-10-05` | Same exact 600-second timeout. No AI modifier comparison or source revision. |
| Line-ending-normalized attempt | Same four adapters and corresponding scenario sets | Trigger `9A79F560...`; effects `263F1CBC...` | Same IDs | No final MCP payload or artifact could be retrieved after the parent’s follow-up source edit; the wait handle returned `exec cell 94 not found`. This batch is not counted as a completed compare. |
| Final post-marker attempt | `random_list` | Effects snapshot to current effects path | `E008_POSTPATCH_FOLLOWUP_COMPARE_2026-10-05` | The request remained pending and was stopped under the parent’s instruction. No terminal MCP payload, comparison ID, or artifact returned. |
| Final post-marker attempt | `custom_weighted_pool` | Trigger snapshot to current trigger path; no incomplete global-pool manifest added | `E008_POSTPATCH_ROOT_POOL_COMPARE_2026-10-05` | The request remained pending and was stopped under the parent’s instruction. No terminal MCP payload, comparison ID, or artifact returned. |
| Final post-marker attempt | `direct_random` | Effects snapshot to current effects path; horizon 365 days | `E008_POSTPATCH_TIMER_COMPARE_2026-10-05` | The request remained pending and was stopped under the parent’s instruction. No terminal MCP payload, comparison ID, or artifact returned. |
| Final post-marker attempt | `ai_strategy_factor` | Effects snapshot to current effects path | `E008_POSTPATCH_AI_COMPARE_2026-10-05` | The request remained pending and was stopped under the parent’s instruction. No terminal MCP payload, comparison ID, or artifact returned. |

The final batch was submitted with trigger hash `9A79F56008BB7F6C2B6A3A6F89AF9ACC9D42FADE3938724255D035C67DEC687E` and effects hash `1467A556530B7B1147A9D70A66AA06E6CA519ACBD26114FD8FCE435AD8A89A86`. The final sources remained at those hashes when rechecked after the calls were stopped. The parent stated that the last effect edit only moved/refreshed the One Denial actor-window marker; its weighted/timing effect is not established by a returned comparison.

No `hoi4.probability_render` call followed because no `analysisId` or comparison artifact was returned. No before/after numeric delta is claimed from the local source diff. The global pool comparison remains unresolved rather than substituting a partial candidate pool, and the empty scenario state records cannot establish stage, full-tension, evolution-disable, world-end, AI, or target eligibility.

## Remaining uncertainty and owner follow-up

All four comparison surfaces remain unresolved because the connected compare route timed out or delivered no terminal payload. Root event pool probabilities remain unresolved because no complete active global candidate set and event-weight state was available. Follow-up branch ordering is source-reviewed, but no normalized branch result or post-patch delta was produced. Timer-pulse expiry/cadence and AI modifier application also lack evaluated results.

If probability service delivery returns, re-run `hoi4.probability_compare` using the same four saved scenario-set IDs, the exact baseline paths and hashes above, the final after hashes, and explicitly populated source-supported state fields. Keep the full global event pool unresolved until its active candidates and dynamic weights are supplied; do not infer rates from the source values alone.
