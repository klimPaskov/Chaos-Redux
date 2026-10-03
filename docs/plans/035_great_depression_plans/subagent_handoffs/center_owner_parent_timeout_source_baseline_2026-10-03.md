# Event 35 parent-route status and source-only handoff

Status: source-only v2 comparison and v3 exclusion baseline are ready for parent review. Analyzer results remain unresolved. No gameplay source was edited.

## Parent and child MCP status

The parent relayed that its required before-source call used `mcp__hoi4_agent_tools__hoi4_probability_inspect({ source: { path: "docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/035_great_depression_effects_before.txt" }, workspaceId: "mod_chaos_redux_ea3b2d67c2c0" })` and completed after 600 seconds with `isError: true`, text `tool call error ... timed out awaiting tools/call after 600s`. It returned no artifact. The narrower retry with the same path plus `source.identifier = "great_depression_score_center_candidate"` and unchanged workspace is still running as parent cell 90; parent should wait on that same handle, not duplicate it. Parent cell 87 is completed and closed.

This parent domain-call timeout is distinct from the earlier child-context failures: the child's inspect invocation returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`; child resource-template discovery separately timed out during MCP startup after approximately 120 seconds on both attempts; refreshed child `ALL_TOOLS` had no probability routes. No new MCP call was made here. No analyzer artifact, scenario hash, source revision, comparison ID, or rendered evidence exists in this handoff. No normalized probability or engine-behavior claim is made.

## v2 comparison after the owner and first-valid changes

The exact v2 fixture remains `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios_v2.json`, SHA-256 `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`. It preserves the seven accepted scenario IDs. The immutable before-source is unchanged at SHA-256 `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`; constants are unchanged at SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

The current effects source at the targeted read was SHA-256 `6549B92D2BDB30CC5060F9CE33B45E8A967ED88E1C730DE0180DF9ED8751159F`. It uses `is_owned_by = PREV.PREV` in the candidate's `any_neighbor_state` block and checks `candidate_saved = 0` before the retained score and lower-ID tie-break conditions. All score coefficients, `invalid_center_candidate_score = -1`, and `center_tie_break_sentinel = 100000` are unchanged.

The following raw scores and winners are exact fixture arithmetic from the source, not analyzer output. Candidate 2 remains 525 in the original five cases.

| Scenario ID | State 1 score before → after | Winner before → after |
|---|---:|---:|
| `CTR35-ROOT-ACTOR` | 520 → 520 | 2 → 2 |
| `CTR35-ROOT-DIFFERENT` | 530 → 520 | 1 → 2 |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | 520 → 530 | 2 → 1 |
| `CTR35-NO-CENTER-NEIGHBOR` | 530 → 530 | 1 → 1 |
| `CTR35-CAPITAL` | 514 → 504 | 2 → 2 |
| `CTR35-TINY-CAPITAL` | -7 → -7 | none → 1 |
| `CTR35-NEGATIVE-TIE` | state 1: -1; state 2: 6 in both | 2 → 2 |

The two owner-sensitive cases change which neighbor receives the existing -10 adjacency term. The capital case keeps its -16 capital term and gains -10 adjacency after the owner fix. The tiny capital remains at -7 but is accepted by the first-valid condition. The negative-tie case still ends at state 2; state 1 ties the initial sentinel, not another candidate. No probabilities are computed from these deterministic scores.

## v3 exclusion baseline on the immutable before-source

The v3 fixture is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios_v3.json`, SHA-256 `2C92489F1C2764C729096B2FF88505A3E8F653D204E6F92F76B1627B4134BF66`. It preserves all seven v2 scenarios and adds the four permission cases. Its pools explicitly declare ownership, control, cores, passability, population, industrial getters, center flags, registry membership, episode metadata, and conversion-forbidden state. Episode metadata `-1` is optional unknown/not-applicable data, not an exclusion.

In the immutable before-source, the inherited-region seed condition at lines 1561–1567 checks event-target presence, owner, controller, core, and passability, then adds the seed to the center registry and sets its center flag at lines 1583–1608. The availability pass at lines 1628–1644 and score pass at lines 1667–1683 omit both the live `industrial_boom_region_conversion_forbidden` and the candidate's own `great_depression_center` permission check. At the targeted live-source read, the same exclusions were still absent.

The companion source has stronger guards. `common\scripted_effects\034_industrial_boom_collapse_handoff_effects.txt` records the exact snapshot state and state ID at lines 211–213, freezes the live conversion-forbidden flag at line 276, and carries the call state ID and frozen call-forbidden flag at lines 296–300. It blocks live/frozen-forbidden inheritance and accepts a flagged center only if its episode equals the receiving actor's episode at lines 317–330. The related `common\scripted_effects\035_great_depression_region_effects.txt` repeats the live/frozen and same-episode checks at lines 735–749 and checks current registry membership at line 753. Their review-time SHA-256 values were `AA8DC3A071992AB0285AADB3DA796781641451B00C3784EAB5F828EE82F7C5C5` and `2A58A6A5D94B4DB1E4D4E506CC4E8EFAEA78D14BD67560161408276A04760FA3`, respectively.

The four v3 cases give these bounded source traces, using the same 530/525 candidate scores and no adjacency penalty:

- `CTR35-FORBIDDEN-PRIMARY+validother`: the generic before-source pool can select live-forbidden state 1 over valid state 2. The permission gate should exclude state 1 and leave state 2.
- `CTR35-RESERVED-OTHER-EPISODE+validother`: state 1 is center-flagged for episode 34 while the receiver is episode 35 and its current registry is empty. The before-source can select state 1; the permission gate should select state 2.
- `CTR35-ALL-RESERVED-OR-FORBIDDEN`: state 1 is live-forbidden and state 2 is a center from another active episode. The before-source can select state 1; the permitted pool should be empty and the API gate should reject before map-state mutation.
- `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE`: Event 34 snapshot state ID, call state ID, and recipient source state ID are all 1; snapshot and call-forbidden flags are true while the live flag is false. The main generic candidate gate ignores that exact frozen proof and can select state 1; the permission gate should exclude only state 1 and leave state 2.

The frozen-forbidden case is a generic candidate-pool case, not an inherited seed. The Event 34 companion would not pass a frozen-forbidden state as `industrial_boom_inherited_region`, so the fixture does not claim that this companion-prohibited target reaches the seed block. The main seed block's missing local check is still a source fact; its effect on other callers or stale supplied targets is not established here.

The safe permission contract is uniform across seed, count, and score passes: reject the live conversion-forbidden flag; reject frozen proof only when the call-forbidden flag is true and recipient source ID exactly equals the Event 34 snapshot state ID; reject another episode's live center while allowing only an explicit same-receiving-episode inherited seed; and honor current actor-registry membership. An empty permitted pool must reject before map-state mutation. The frozen proof must not exclude any unrelated state by arbitrary ID.

## Handoff boundary

The v3 JSON parsed with all 11 IDs and complete required state fields. This is a bounded source baseline, not an analyzer evaluation. The parent retry on cell 90 is still the only in-flight MCP attempt reported here; no retry was launched from this child. Once live schemas and a completed inspect become available, use identical v2 bytes for the v2 compare and identical v3 bytes for the exclusion baseline and its post-patch compare. Do not invent `scenarioSet`, override, or scope-binding fields.

V1, v2, and the immutable before-source remain unchanged. The v3 file was already present in the shared tree and was adjusted only to remove inherited-seed markers from the live/frozen-forbidden candidate cases, consistent with the mapped companion gate. This handoff was newly written. No gameplay source was patched, staged, or committed.
