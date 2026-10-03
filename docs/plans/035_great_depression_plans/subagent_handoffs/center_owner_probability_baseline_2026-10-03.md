# Event 35 deterministic center-score baseline

Status: incomplete and MCP-blocked. This handoff preserves the bounded source trace and the exact baseline inputs. It does not establish analyzer-confirmed scores, ranks, probabilities, or balance.

## Scope and source identities

The audited surface is `great_depression_score_center_candidate` and its caller path from the actor country through an eligible controlled state to that candidate state's neighboring states. No other Event 35 score surface was audited.

The live source is `common\scripted_effects\035_great_depression_effects.txt`. Its SHA-256 is `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`. The immutable before-source copy at `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\035_great_depression_effects_before.txt` has the same SHA-256 and is byte-identical to the live source at baseline. The copy is 428,016 bytes and 7,323 lines; it was not modified.

Relevant source locations are `great_depression_score_center_candidate` at lines 1320–1348, its call from `every_controlled_state` at lines 1667–1681, the deterministic comparison and tie-break at lines 1682–1695, and winner registration at lines 1701–1724. `great_depression_register_initial_centers` is defined at line 1523 and called at line 3281.

The named fixture is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios.json`, SHA-256 `5539B8D4DCB64DB32D9EC3252953D5B684E4A517C45A9F3643A20B4D65256E1D`. Its five scenario IDs are preserved below. The current constants are `common\script_constants\035_great_depression_constants.txt`, SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

The selected coefficients in `great_depression_scaling` are `center_industry_weight = 4`, `center_infrastructure_weight = 2`, `center_population_weight = 1`, `center_capital_penalty = -16`, `center_adjacency_penalty = -10`, `invalid_center_candidate_score = -1`, and `center_tie_break_sentinel = 100000` (constants lines 1200–1206). The candidate population gate uses `minimum_viable_state_population_k = 1` (line 321).

## MCP route and evidence status

I read the exposed schemas for `mcp__hoi4_agent_tools__hoi4_probability_inspect`, `hoi4_probability_evaluate`, `hoi4_probability_sweep`, and `hoi4_probability_render`. The inspect schema accepts `source`, `workspaceId`, and optional adapter and pool selectors; evaluate requires `scenarioSet` and accepts `source`; sweep requires `scenarioSet`, `source`, and `sweep`; render requires an `analysisId`.

The mandatory first call was `mcp__hoi4_agent_tools__hoi4_probability_inspect` with `source: { path: "docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/035_great_depression_effects_before.txt" }` and workspace `mod_chaos_redux_ea3b2d67c2c0`. The call returned `isError: true` and the exact message: `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`. This was an availability error, not a terminal timeout, so no timeout retry was applicable. The tool returned no artifact URI, source revision, analysis ID, or scenario hash.

Because inspect did not run, evaluate and sweep were not called; I cannot claim that the fixture was translated into a supported `scenarioSet` or that the analyzer recognized this deterministic score surface. Render was unavailable in practice because there is no analyzer `analysisId` to render. No inspect/evaluate/sweep artifact or rendered evidence path exists. Compare was not run: this is a before-only audit, there is no after-source, and a current/current comparison would be invalid. No job, helper-expansion, or native-task route was used.

The required event probability guidance was read at `.agents\skills\chaos-redux-events\SKILL.md`, lines 353–355. The repo's `chaos-redux-subagents` skill requires a scenario-specific probability pass and explicitly forbids substituting source-only review when the probability route is unavailable. That limit applies here. No MTTH entry or timing weight is in the bounded target, so the MTTH skill and timing analysis were not applicable.

## Source-level score and scope trace

The helper builds a deterministic state score from industrial complexes, arms factories, dockyards, infrastructure, and `state_population_k`; it subtracts the capital penalty when `is_capital = yes`. It then checks `any_neighbor_state` for both `is_owned_by = ROOT` and `has_state_flag = great_depression_center`, and subtracts the adjacency penalty when that conjunction matches (source lines 1321–1347). The supplied `baseCandidate` values are 3 civilian factories, 2 military factories, 1 dockyard, infrastructure 3, population 500k, and non-capital by default. The capital scenario overrides `capital` to true. These are inputs and coefficients only; no aggregate score was hand-calculated.

The caller iterates controlled states and gates candidates on actor ownership, actor control, actor core status, passability, minimum population, at least one industrial building, and absence from the actor's existing center-state array (lines 1667–1680). It compares candidate scores with `greater_than`; equal scores prefer the smaller state ID (lines 1682–1694). After selecting a candidate, it adds that state to the actor's center-state array before the next slot (lines 1701–1724). This is a deterministic maximum-score selection with an ID tie-break, not an `ai_will_do` willingness value, a probability-proportional draw, or a timing distribution. The source establishes the selection rule, but no MCP score/rank result was obtained.

The relevant offline reference is `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`: the ROOT/PREV definitions are lines 260–263, neighbor-state scope definition is lines 385–386, and the `PREV usage` section explains parent scopes and chaining at lines 811–845. The relevant installed reference is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`: `any_neighbor_state` supports state scope at lines 1497–1503 and `is_owned_by` accepts ROOT and PREV targets at lines 6088–6094. These are local file identities, not MCP source revisions.

The scope chain at the owner test is actor country → candidate state (`every_controlled_state`) → neighboring state (`any_neighbor_state`). In the neighboring-state block, `PREV` is the candidate state and `PREV.PREV` is the actor country. The intervening `if`/`limit` blocks do not add scope nodes. ROOT names the root node of the executing block and can differ from the actor in inherited/conversion execution. Therefore the source-level safe actor reference at line 1342 is `PREV.PREV`, not `ROOT`. This is a bounded source-and-reference inference; the unavailable MCP route prevented analyzer confirmation.

## Named fixture traces

The fixture declares one shared candidate template and these scenario-specific actor/root/neighbor-owner inputs. A non-null `centerNeighborOwner` is treated here only as the fixture's intended adjacent center neighbor; the JSON does not separately encode a neighbor state ID, adjacency edge, or `great_depression_center` flag. The listed owner-predicate results are bounded source traces conditional on that fixture interpretation, not analyzer or live-game observations.

| Scenario ID | Actor / ROOT / declared neighbor owner | Fixture adjacency expectation | Current `is_owned_by = ROOT` trace | Audit classification |
|---|---|---|---|---|
| `CTR35-ROOT-ACTOR` | GER / GER / GER | Penalty expected | Owner test can match when the declared neighbor is adjacent and flagged as a center. | Bounded source trace; score and rank unresolved. |
| `CTR35-ROOT-DIFFERENT` | GER / ENG / GER | Penalty expected | Tests ENG ownership, so it misses the actor-owned GER neighbor under the fixture inputs. | Bounded source trace identifies a mismatch; score and rank unresolved. |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | GER / ENG / ENG | No penalty expected | Tests ENG ownership, so it can match the foreign ENG neighbor under the fixture inputs. | Bounded source trace identifies a mismatch; score and rank unresolved. |
| `CTR35-NO-CENTER-NEIGHBOR` | GER / ENG / null | No penalty expected | No declared qualifying center neighbor; the adjacency predicate should remain false under the fixture interpretation. | Bounded source trace; score and rank unresolved. |
| `CTR35-CAPITAL` | GER / ENG / GER; capital true | Adjacency penalty expected | The owner test misses the GER neighbor as in `CTR35-ROOT-DIFFERENT`; the capital penalty is a separate condition and remains applicable. | Bounded source trace; total score and rank unresolved. |

The fixture does not provide a complete candidate pool: it has one `baseCandidate` template, not all eligible states, their IDs, or their score inputs. It also omits candidate controller/core/passability and existing-center membership, actual neighbor topology and state flags, and state IDs required to resolve tie-breaks. Thus candidate-pool completeness is **incomplete** in every scenario. External-factor completeness is also **incomplete**. The scenario JSON's expected adjacency values are test expectations, not campaign observations or MCP results.

## Findings and uncertainty

- The helper's score is deterministic and uses centralized constants. No normalized probability or exact click/selection chance is supported or claimed.
- The `ROOT` owner test can omit the -10 adjacency modifier from an actor-owned center neighbor when ROOT is another country, and can apply it because a foreign ROOT-owned neighbor is flagged as a center. This can alter candidate ranks, but no actual rank reversal is established.
- The capital penalty is independent of the adjacency owner check. No total score was calculated for the capital fixture.
- The existing-center array exclusion plus winner registration before the next slot is source evidence against selecting the same registered state twice in that loop. No runtime repetition result was obtained.
- Dominance, starvation, score-scale sensitivity, rank-reversal thresholds, campaign repetition, and exploit magnitude remain unresolved because the analyzer was unavailable and the fixture lacks a complete candidate pool. Population is expressed in thousands while factory and infrastructure inputs are levels; whether that scale dominates other terms requires the mandated scenario sweep and is not asserted here.
- AI validity is not applicable to this helper. Timing drift and MTTH are not applicable. Random sampling, seeded simulation, and custom-pool sequence analysis were not applicable to the deterministic selector and were not run.

## Recommended owner action

The narrow scope correction to review is `common\scripted_effects\035_great_depression_effects.txt:1342`: use `is_owned_by = PREV.PREV` inside the candidate state's `any_neighbor_state` block so the ownership test is anchored to the actor country even when ROOT differs. This is a scope correction, not a balance recommendation; preserve all score coefficients and other selection logic unless the owner separately decides otherwise. No gameplay change was applied here.

For analyzer-confirmed follow-up, first rerun probability inspect on the preserved before-source and establish the accepted adapter/schema. Then evaluate the five exact fixture IDs and sweep the ROOT/neighbor-owner cases with a complete candidate pool and explicit state IDs. Keep outcomes classified as raw score/rank rather than probabilities. After the owner patch, compare the immutable before-source with the actual after-source under the identical fixture/scenario set; render only an analysis the route successfully returns. The current baseline contains no analyzer analysis ID, scenario hash, revision, comparison ID, artifact URI, or rendered evidence.

## Skipped analyses and completion state

Evaluate and sweep are blocked by the failed mandatory inspect route; render lacks an analysis ID; compare lacks an after-source in this baseline request. No vanilla gameplay source beyond the installed trigger documentation was needed for the bounded scope question. Event-chain inspect/render were not used because the requested target is a scripted scoring helper and its immediate scope path, not an event-chain audit. No game launch or live observation was performed.

Only this report was written. No gameplay, AI, event, or constants source was edited, and nothing was staged or committed. The baseline audit remains incomplete until the required probability route returns analyzer-backed evidence.
