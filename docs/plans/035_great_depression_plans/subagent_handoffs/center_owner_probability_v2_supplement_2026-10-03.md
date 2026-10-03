# Event 35 center-selection v2 baseline supplement

Status: bounded source baseline established on the immutable before-source. The mandatory MCP probability evidence remains unavailable, so analyzer-confirmed scores, rankings, and probabilities are unresolved. No source patch was made.

## Preserved inputs and v1 disposition

The before-source remains `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\035_great_depression_effects_before.txt`, SHA-256 `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`. It is unchanged and is the source for this baseline inference.

The original `scenarios.json` remains byte-preserved at SHA-256 `5539B8D4DCB64DB32D9EC3252953D5B684E4A517C45A9F3643A20B4D65256E1D`. Its single `baseCandidate` and five owner/root cases do not declare a complete candidate pool, candidate eligibility fields, neighbor topology/flags, or registry membership. It is superseded only as the input for future complete baseline and compare runs; the earlier baseline and compare handoffs remain historical evidence and were not rewritten.

The supplemental `scenarios_v2.json` is now the shared fixture for both the before-source re-audit and any later post-patch compare that the live MCP schema accepts. Its SHA-256 is `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`. It preserves all five v1 IDs and adds `CTR35-TINY-CAPITAL` and `CTR35-NEGATIVE-TIE`. Its fixture fields describe domain facts; they are not claimed to be MCP `scenarioSet`, AST, or scope-binding keys.

The constants file `common\script_constants\035_great_depression_constants.txt` remains SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`. Relevant values are `minimum_center_cap = 1` at line 22, `minimum_viable_state_population_k = 1` at line 321, industry/infrastructure/population weights `4/2/1` at lines 1200–1202, capital penalty `-16` at line 1203, adjacency penalty `-10` at line 1204, invalid candidate score `-1` at line 1205, and tie-break state-ID sentinel `100000` at line 1206.

## Additional source finding on the before-source

In `great_depression_register_initial_centers`, the required center count starts at `minimum_center_cap = 1` (before-source line 1540). With an empty center registry and exactly one eligible state, the availability pass counts one candidate, the required count remains one, and one selection slot runs (lines 1624–1659).

Each slot initializes `great_depression_center_candidate_saved` to zero, `great_depression_center_best_score` to `invalid_center_candidate_score` (-1), and the best state ID to `center_tie_break_sentinel` (100000) (line 1664–1666). A candidate is saved only when its score is greater than the current best, or when scores are equal and its ID is smaller (lines 1683–1696). If no candidate is saved, the registration effect marks failure when the center count is zero or below the required count (lines 1730–1740).

`CTR35-TINY-CAPITAL` is one otherwise eligible GER candidate: owned and controlled by GER, a GER core, passable, population 5k (greater than the 1k minimum), one civilian factory, no military factory/dockyard/infrastructure, not already registered as a center, and no adjacent center. Its exact source arithmetic is `1 × 4 + 5 × 1 + 0 × 2 - 16 = -7`. The candidate is valid under the enumerated gates but `-7` neither exceeds nor equals the initial `-1` best score, so `candidate_saved` remains zero. With the one required slot, the source leaves the slot unfilled and marks center registration failed. The helper contains no major/player eligibility test; this is a source-local counterexample for any actor reaching this selector, not a live campaign observation proving an outer caller path.

`CTR35-NEGATIVE-TIE` contains one capital candidate scoring exactly `-1` (`1 × 4 + 11 × 1 - 16`) and one non-capital plain candidate scoring `6` (`1 × 4 + 2 × 1`). Both pass the declared eligibility gates. State 1 ties the initial score sentinel and its ID is below 100000, so the existing equality/ID branch accepts it; state 2 then exceeds it and becomes the selected candidate. The fixture therefore avoids inventing a second capital or a negative non-capital. It exercises a tie against the sentinel, not an equal-score tie between candidates.

The narrow safe selection correction is to accept the first valid candidate explicitly using the existing `candidate_saved = 0` state, while preserving the score comparison, lower-ID tie-break, `invalid_center_candidate_score = -1`, and all weights. This does not choose a new balance target. No source change was applied.

As fixture-derived expectations for that future source change, `CTR35-TINY-CAPITAL` should save/select its sole state 1 despite the -7 score, while `CTR35-NEGATIVE-TIE` should still finish with state 2 above state 1. In the baseline, state 1 of `CTR35-NEGATIVE-TIE` exercises the current equality-to-sentinel and smaller-ID branch; the fixture has no equal-score candidate pair, so preserving the candidate-to-candidate tie-break also requires source review after the patch. These are expectations only, not after-source or MCP results.

## Explicit fixture arithmetic, not analyzer output

For the original five cases, state 1 has raw base score 530 and state 2 has 525; the capital case makes state 1's pre-adjacency score 514. The existing adjacency term is -10 when the before-source ROOT-owned-center test matches. The table gives the before-source's resulting raw scores and actual selector outcome under the sentinel comparison; it is arithmetic from the declared fixture and constants, not an MCP result.

| Scenario ID | Before-source raw scores | Before-source selector outcome |
|---|---|---|
| `CTR35-ROOT-ACTOR` | state 1: 520; state 2: 525 | state 2 selected |
| `CTR35-ROOT-DIFFERENT` | state 1: 530; state 2: 525 | state 1 selected |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | state 1: 520; state 2: 525 | state 2 selected |
| `CTR35-NO-CENTER-NEIGHBOR` | state 1: 530; state 2: 525 | state 1 selected |
| `CTR35-CAPITAL` | state 1: 514; state 2: 525 | state 2 selected |
| `CTR35-TINY-CAPITAL` | state 1: -7 | no candidate saved; the sole eligible state is rejected by the sentinel comparison |
| `CTR35-NEGATIVE-TIE` | state 1: -1; state 2: 6 | state 1 ties the sentinel and is saved by the ID condition; state 2 then wins |

The v2 JSON was parsed and checked for the exact seven IDs, declared candidate/neighbor fields, eligibility facts, and resolved adjacency IDs. The original five have exactly candidates 1 and 2; the tiny-capital case has only candidate 1; the negative-tie case has candidates 1 and 2. Neighbor state 3 is separately declared and excluded from GER candidates by registry membership when GER-owned or by ENG ownership/control in the foreign-neighbor case. No candidate-to-candidate score tie or undisclosed eligible candidate is asserted.

## MCP status and required parent query

The prior mandatory `hoi4.probability_inspect` attempt used this same immutable before-source and returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`. In the subsequent route rediscovery, `list_mcp_resource_templates({ server: "hoi4_agent_tools" })` failed twice with `resources/templates/list failed: failed to get client: MCP startup failed: timed out handshaking with MCP server after 119.9999976s`; the refreshed `ALL_TOOLS` metadata contained no probability inspect, evaluate, sweep, compare, or render routes. This is the child-context route gap, not evidence about the parent's connected tool context.

No v2 scenario was translated into an analyzer schema, and no evaluate, sweep, compare, or render result exists. The exact parent-side request is: inspect the immutable before-source using `source: { path: "docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/035_great_depression_effects_before.txt" }` first; use only the returned live schema to translate all seven IDs and their complete pools from the immutable v2 fixture for the before-source baseline; then compare with `before: { path: "docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/035_great_depression_effects_before.txt" }`, `after: { path: "common/scripted_effects/035_great_depression_effects.txt" }`, and that identical translated v2 scenario set after the owner-applied sentinel correction. Do not add guessed candidate overrides or scope/AST keys. If an inline source form is used, first confirm that form in the live compare schema and keep the before/after texts limited to the supported weighted surface.

At the last targeted read, the live effects file's whole-file SHA-256 was `A1DC71304D3C0CB73BBE7E98460159D138E07ED6F59B95427ED27922A90BE3E1`; the sentinel initialization and comparator at live lines 1666–1698 still matched the before-source logic. The whole-file hash changed while the shared tree was being read, so it is a point-in-time identity only; this supplement makes no claim about disjoint changes outside the target.

## Completion boundary

This is a bounded source baseline for the sentinel rejection and fixture arithmetic. It is not analyzer-confirmed and supports no normalized probability claim. The same immutable v2 fixture must be used for any analyzer baseline and subsequent comparison if the live schema can represent it. Only the v2 fixture and this supplemental handoff were written; v1 and earlier handoffs were preserved, and no gameplay source was edited, staged, or committed.
