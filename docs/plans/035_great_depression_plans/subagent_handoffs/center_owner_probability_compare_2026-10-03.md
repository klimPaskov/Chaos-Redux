# Event 35 center-owner post-patch comparison

Status: source-level before/after comparison complete; required MCP comparison unavailable in this child context. Analyzer-confirmed score, ranking, and probability results remain unresolved.

## Scope and preserved identities

The comparison is restricted to `great_depression_score_center_candidate` and its actor-country → candidate-state → neighboring-state owner test. Disjoint changes elsewhere in the live effects file were not inspected and are outside this comparison.

The immutable before-source is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\035_great_depression_effects_before.txt`, SHA-256 `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`. Its bytes remain unchanged. The after-source is `common\scripted_effects\035_great_depression_effects.txt`, whole-file SHA-256 `6D8B6D628E5416F7A7997CD4B7D1527DC4C998E1CA4ECE1D489782704C55CA83`.

The exact fixture remains `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios.json`, SHA-256 `5539B8D4DCB64DB32D9EC3252953D5B684E4A517C45A9F3643A20B4D65256E1D`. Its five unchanged scenario IDs are `CTR35-ROOT-ACTOR`, `CTR35-ROOT-DIFFERENT`, `CTR35-FOREIGN-ROOT-NEIGHBOR`, `CTR35-NO-CENTER-NEIGHBOR`, and `CTR35-CAPITAL`. Constants remain unchanged at `common\script_constants\035_great_depression_constants.txt`, SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`; the adjacency coefficient remains -10 and the capital coefficient remains -16.

The whole-file source hashes differ, as expected from the parent-reported disjoint changes. The targeted helper moved from lines 1320–1348 in the before-source to lines 1322–1350 in the after-source. A line comparison of those complete helper blocks found exactly one changed line: `is_owned_by = ROOT` became `is_owned_by = PREV.PREV`. All score terms, weights, capital handling, and adjacency penalty application inside the helper are otherwise unchanged.

## MCP route discovery and blocker

As requested, I first called `list_mcp_resource_templates({ server: "hoi4_agent_tools" })`. It failed with: `resources/templates/list failed: failed to get client: MCP startup failed: timed out handshaking with MCP server after 119.9999976s`. I retried the same server-scoped request once; it returned the identical startup-handshake timeout and no running handle.

After each attempt, `ALL_TOOLS` contained no `mcp__hoi4_agent_tools__hoi4_probability_inspect` or `mcp__hoi4_agent_tools__hoi4_probability_compare` metadata. Therefore this child has no live schemas with which to translate the saved fixture or invoke the comparison. The prior baseline inspect attempt used the immutable before-source and returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`. No post-patch inspect or probability compare could be made through the current child tool context.

No compare artifact, comparison ID, analyzer revision, scenario hash, result data, or rendered view was returned. I did not invent scenario fields or candidate overrides, call a current/current comparison, or use a source-only result as analyzer evidence. This is a child-context route gap; it does not establish that the parent context's route is unavailable.

## Source-level score delta by named fixture case

The fixture supplies one `baseCandidate` (3 civilian factories, 2 military factories, 1 dockyard, infrastructure 3, population 500k, non-capital unless overridden) and owner/root cases. Its `centerNeighborOwner` field is treated as indicating the intended adjacent center neighbor when non-null; the JSON does not separately identify the map edge, neighbor state ID, or neighbor center flag. The table below is a bounded source trace conditional on that fixture interpretation. Deltas are the change to this candidate's score from the existing -10 adjacency term only, after minus before; they are not analyzer-computed aggregate scores.

| Scenario ID | Before owner test (`ROOT`) | After owner test (`PREV.PREV`) | Expected adjacency outcome | Source score delta |
|---|---|---|---|---:|
| `CTR35-ROOT-ACTOR` | GER neighbor can match GER root | GER neighbor can match GER actor | Penalty applies before and after | 0 |
| `CTR35-ROOT-DIFFERENT` | GER neighbor does not match ENG root | GER neighbor matches GER actor | Penalty applies after correction | -10 |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | ENG neighbor matches ENG root | ENG neighbor does not match GER actor | Penalty does not apply after correction | +10 |
| `CTR35-NO-CENTER-NEIGHBOR` | No declared qualifying neighbor | No declared qualifying neighbor | No penalty before or after | 0 |
| `CTR35-CAPITAL` | GER neighbor does not match ENG root | GER neighbor matches GER actor | Adjacency penalty applies after correction; capital penalty remains separate | -10 adjacency; capital unchanged |

For `CTR35-CAPITAL`, the existing -16 capital term remains applicable because `capital` is true in that fixture case; it is not part of the before/after delta. No absolute candidate score was calculated. The selection source compares raw scores and uses smaller state ID for equal-score ties, but the fixture does not provide the complete eligible candidate pool, candidate IDs, or competing score inputs. Candidate-pool and external-factor completeness are therefore incomplete for every scenario, and no rank change or rank reversal is established.

## Evidence classification and remaining uncertainty

The changed predicate now follows the declared actor → owned candidate state → neighbor path even when ROOT is ENG and actor is GER. The named owner cases align with their fixture expectations at source level, subject to the adjacency/center-flag assumption above. Classification: bounded source comparison. The analyzer comparison, numeric aggregate scores, candidate rankings, normalized selection probabilities, sensitivity, dominance, starvation, and rank-reversal outcomes are unresolved.

This surface is a deterministic highest-score selection with an ID tie-break, not probability-proportional sampling, an AI willingness score, or an MTTH timing distribution. There are no normalized probabilities to infer from these source deltas. Potential ranking effects from the corrected adjacency term require the complete eligible pool and the mandated analyzer sweep/compare. No timing, seeded simulation, or custom weighted-pool sequence analysis was applicable or run.

## Handoff state

The owner-applied patch is confirmed within the named helper, with the centralized weights unchanged. No additional gameplay recommendation or balance target is made. The required post-patch `hoi4.probability_inspect` and same-scenario `hoi4.probability_compare` remain blocked by the child MCP startup/tool-availability gap above; parent-context analyzer evidence is still required for numeric or ranking claims.

Only this handoff report was written. No gameplay or constants files were edited, and nothing was staged or committed.
