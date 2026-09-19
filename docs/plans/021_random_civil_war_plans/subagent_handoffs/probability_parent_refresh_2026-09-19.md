# Event 021 parent probability refresh — 2026-09-19

Disposition: implemented evidence for test entry; independent specialist certification and the complete named matrix remain open.

This handoff records a fresh parent-owned read-only MCP pass after the current Event 006 surface repair. The pass is limited to the current Event 021 archetype random list because the accepted Event 021 severity contract is deterministic pressure-and-viability selection rather than a weighted severity pool.

## Current archetype source inspection

The source is `common/scripted_effects/021_random_civil_war_parent_effects.txt` and the complete candidate pool is:

- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.1`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.2`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.3`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.4`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.5`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1132.entry.6`

The first line-1120 probe correctly returned `PROBABILITY_SOURCE_DISCOVERED` with eight available candidates and identified the moved six-entry pool at line 1132. The corrected `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=true`, six candidates, six required inputs, zero unresolved inputs, and validation passed.

The inspection source revision is `354f0acde101e7776a1c1fae65af4ecea27c5a890f0ae7c988be2979961152a0`, and the source hash is `465d0389024968b574091571fa5ded0931d3fb6359127621245dad643b30c3cf`.

The inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/151df9e6ff700a81b6bf88e9fe09ad86af0a5a08e37d4747b3660e25f3f4651e/2d0430b6290555d4755f58c7dd096d6993d2557ec707aa99b4084fd47a82fbac/probability-inspect-465d03890249.json`.

## Current archetype fixture evaluation

The evaluation used adapter `random_list`, the same six-entry candidate pool, horizon one day, metrics `conditional_probability` and `raw_value`, and outputs JSON, ranking, matrix, and unresolved.

The scenario set id is `event021_archetype_current_gate_fixtures_2026_09_19` and contains three explicit fixtures: all six route variables at 100, Event 006 route at zero with the other five at 100, and ideological route at 100 with the other five at zero.

The evaluation returned `PROBABILITY_ANALYZED` with analysis id `probability-495721afa9f72867de4858e2`, `analysisStatus=complete`, 18 candidate rows, zero unresolved inputs, validation passed, and source revision `354f0acde101e7776a1c1fae65af4ecea27c5a890f0ae7c988be2979961152a0`.

The scenario hash is `2421a7e1858e8fa96a4f2eeb201f3da565d72a52952df71720eaf216b42d7ff2`.

The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ccab1de24631a7644b44041fa05eec34fd0dbab386a17c660388d869ffbfd14/4e4083b476b62313f9467b8b991317aeb760df14a8fbb06abf8eea67ca073a52/probability-495721afa9f72867de4858e2.json`.

The MCP reported seven expected design warnings: the zero Event 006 fixture leaves that route at the starvation threshold, and the ideological-only fixture intentionally produces one dominant route plus five starved alternatives. These warnings are evidence of the declared gate fixtures, not unresolved source inputs.

## Certification boundary

This is current parent-owned MCP evidence, not an independent `chaosx_ai_probability_auditor` certificate. The narrow specialist assigned to the same current archetype/severity request remained running through two bounded waits totaling five minutes, did not return a durable report after an interrupt request, and was closed with previous status `running`.

The current pass does not certify target-ticket normalization, Evolution I–III timing, front/force, sponsor, settlement, recurrence, global queue, Wars-cluster, scenario, Event 006 nested-package, or same-scenario before/after comparisons. The accepted deterministic severity contract remains source-proven but not a probability pool.
