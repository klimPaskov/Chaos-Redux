# Italian focus-only closure AI score

Disposition: source patch implemented with a partial matched MCP comparison; eligibility and full-pool acceptance remain unresolved.
The five named score fixtures do not establish that the focus-only decision is offered or selected in a running campaign.
Acceptance basis: the approved country-kit reconciliation requires Italy's explicit postwar or abandon-camps focus route to remain meaningful for AI as well as the player.

The `ita_close_desert_camps` decision was visible to fascist, unexposed Italy through either `ita_focus_postwar_colonial_reform` or `ita_focus_abandon_colonial_camps`, but its blocked base and three other modifiers gave that focus-only route an AI score of zero.
The source now adds the existing centralized `constant:camp_rework_ai_weight.italy_reform` value of 70 only when Italy is fascist, unexposed, below the retreat threshold, and has one of those focus flags.
The exposure, losing-war and regime-change comparator branches remain separate, so this adds no new tunable number.

The exact pre-edit decision file is frozen at `italy_focus_reform_before_2026-09-27.txt` with raw SHA-256 `CBC9C620D2C116E4AD26231B422740172C87DDC56654736DC471CE0B51A9089D`.
It was reconstructed by removing only the new focus modifier from the current file and verified against the raw pre-patch hash captured before the edit; the unrelated September 1 baseline was rejected.

| Scenario | Before raw score | Current raw score |
| --- | ---: | ---: |
| Focus: postwar reform, fascist, unexposed, not losing | 0 | 70 |
| Focus: abandon camps, fascist, unexposed, not losing | 0 | 70 |
| Exposure comparator | 70 | 70 |
| Fascist losing comparator | 10 | 10 |
| Regime-change comparator | 85 | 85 |

`hoi4.probability_inspect` ran before evaluation.
The baseline evaluation source hash was `a5659a891048743c8be418a038f03617c7a06d13d5a972a209653d3e9a32172f`, revision `ae105d9102f39061bca3a641eafb130734a7a868bf220083febfd35fa152f35d`; the [baseline JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e548977da4bf9767d0e3ffbaff4382263c5506b13ea3f762a0be7e3907657f72/8b151dc5cdead10c009d03f4b2b4356119d9d18c5549dab9cc8f7538e4d5259e/probability-d59e3f5416b074f9b04eccf8.json) retains its source trace.
The current evaluation source hash was `9e0d0adbbd2e2d45a67621cad98a6073978d16eb829e64dfc1971b34c17be558`, revision `a33ddab64fb4d7ecb89b35280e3f799244eae89a0b1422b44f6884aa71096f5e`; the [current JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b305f4cfbdd1aef68f5ec9d9edb31debc34c98c683b30e50415450b76043dde7/ed71f79f84c3c9a5461e04f80bc13cf57d96fa84a3e8ae2963cae7c3c6de5e0a/probability-a52c1953023e7b280d0d0ede.json) used the same scenario hash `5df77ae07788c1d7827912af90003583d424e12b4560d459c5c06fa56520a8ac`.
The evaluator returned `score_only` results and unresolved `has_decision`, active/closable site counts and `all_of_scopes`; neither eligibility nor choice probability is proven.
The first `hoi4.probability_compare` attempt with the exact before file timed out after 180 seconds. A lean path retry returned `PROBABILITY_SURFACE_EMPTY` because the frozen file under `docs/` was not indexed as a decision surface.
The read-only AI auditor then verified the before-file SHA-256, extracted the exact pre-edit `camp_repression_network_category` decision block in memory, and called `probability_compare` with `before.inlineClausewitz`, current `after.path`, the same five scenarios and the same singleton candidate pool.
That call returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-c2a70a5f38316f749b8d1cbe`, compare revision `e85b8f17cd02feee758e017ea7c531dc1feb6fbb1c58f9b46b50edb8439344da`, and [comparison JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1c41cb055a7ddd6365197eb35a36f9be09a7bd61db3e0212de60d763983a58c/b3423dfbbe36b4e7f1e81addfd801d477a51a5feabea25722b93fbec23f0fe48/probability-c2a70a5f38316f749b8d1cbe.json).
It found exactly two changed scenarios: the focus-only scores rose from 0 to 70; exposure, losing-war and regime-change comparators remained 70, 10 and 85.
Four eligibility inputs remained unresolved, including `has_decision`, active/closable-site counts and `all_of_scopes`; the adapter is score-only and does not establish a click probability or the full game decision pool.
