# Event 021 candidate output lifetime handoff

Disposition: implemented within the delegated candidate-helper write scope, with parent integration and native evidence unresolved.
Acceptance basis: the parent's 2026-10-07 bounded follow-up explicitly authorized candidate-file output ownership repairs, source-backed execution tests, helper documentation and this handoff.
The parent owns the active collector, active source caller, remnant repair, active tests, opening outer callers, final review and commits.

## Changed files and identifiers

- `common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt`
- `common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.md`
- `.tools/test_event021_candidate_output_lifetime.py`, new
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_candidate_output_lifetime_2026-10-07.md`, new

`event021_parent_collect_dynamic_optional_front_candidates` directly creates all 27 scratch arrays before `event021_parent_reset_dynamic_optional_front_candidates` runs.
The initialization is in the collector itself rather than delegated to another helper, so nested reset, grower, package collector and appender returns retain the storage.

`event021_parent_append_dynamic_ordinary_front_candidate` initializes `event021_planned_front_route` and `event021_planned_front_goal` before the existing route-source and objective mappers run.
Its scope comment is corrected to STATE because the shared grower calls it inside the selected-anchor scope.

`event021_parent_grow_dynamic_ordinary_front_regions` initializes `event021_dynamic_candidate_state_count` immediately before the appender whose returned count it subtracts from the active state budget.
It preserves existing aligned rows and current count, capacity, cursor and budget inputs.

All three candidate-file calls to `event021_parent_score_anchor_state` directly initialize `event021_anchor_state_score` before consuming the returned value.
The call sites are the Event 006 appender, the grower's rebuilt remaining-anchor pool, and the opening collector's initial anchor pool.

`event021_parent_collect_dynamic_event6_front_candidates` forwards existing collector-owned arrays through its package appender without resetting prior rows.
The documentation lists all 17 aligned output arrays, the 27 scratch-array contract, scalar initial values, scopes, inputs, side effects and an outer-caller usage example.

No constants, numeric scoring rules, weights, capacities, predicates, route caps, event targets, persistent cleanup fields or gameplay design were added or changed.
Temporary scratch initialization follows the existing fresh-collection reset semantics.
No parent-owned file or existing test was edited, no Git write was performed, and no game, desktop or log inspection was used.

## Meaningful validation

`python -B .tools/test_event021_candidate_output_lifetime.py` passes five test groups.

The tests execute the actual candidate collector, grower, ordinary and Event 006 appenders, package loop, span validator, and parent route/goal mapper bodies.
They keep temporary scalars, temporary arrays, country values, globals, and chain-local targets separate.
Every helper return drops new temporary scalar and array storage that its caller had not initialized.

Coverage includes the four ordinary route/objective combinations, all aligned metadata columns, two complete opening rows forwarded through nested calls, the 27 directly owned reset arrays, all three scorer boundaries, retained prior rows during active budget consumption, Event 006 package metadata and score forwarding, and the deliberate disappearance of unowned outer outputs.
The tests preserve an unrelated caller cursor and check that collector-private scratch does not become a public outer output.

Running the same test script with `CHAOSX_EVENT021_TEST_REVISION=545c509bf4531d48ebece6d9c0bfcc4f211d19c0` reproduces failures in four of the five groups, with seven unittest failure records because the route test has four subcases.
The baseline loses all four ordinary route tokens, returns zero fixture scores in opening and Event 006 rows, and fails to spend the returned active region count.
This is a read-only baseline execution, not a checkout or Git mutation.
The parent's integral validator and deadline tests were not rerun or duplicated.

Eligibility, state adjacency, native anchor scores, free dynamic tags, and admitted Event 006 packages are explicitly declared fixtures.
Package finder and identity transaction callbacks are fixture boundaries and are not validated by this test.
Decimal arithmetic and ROUND_HALF_UP model the bounded fixture calculations only, with unique anchor scores to avoid asserting native tie behavior.
These tests prove source execution and conservative storage lifetime, not native graph scoring, probability balance, engine rounding, package admission, rollback conservation or live campaign behavior.

## Parent integration still required

The following parent-owned outer callers do not establish the candidate storage they consume after helper return in the inspected source:

| Caller and source location | Returning helper | Required parent repair |
| --- | --- | --- |
| `event021_parent_build_front_plan`, `021_random_civil_war_parent_effects.txt:2034` | `event021_parent_collect_dynamic_optional_front_candidates` | Directly create the 17 aligned output arrays and initialize optional validity/count before fresh collection, preserving any frozen-path inputs |
| `event021_parent_freeze_scenario_plan`, `021_random_civil_war_parent_effects.txt:7598` | `event021_parent_collect_dynamic_optional_front_candidates` | Directly create the same arrays and scalar outputs before collection and consumption by the freezer |
| `event021_parent_apply_frozen_scenario_plan`, `021_random_civil_war_parent_effects.txt:7673` | `event021_parent_load_scenario_optional_front_rows` | Directly create the same arrays and scalar outputs before replay so the caller can forward them to the later builder |

These line anchors can move with the parent's shared work.
The caller names and helper boundary are the durable identifiers.
The negative unowned-outer-output test intentionally demonstrates the remaining boundary rather than treating a successful internal collector as integrated completion.
The parent must also retain output ownership across any higher caller that forwards these arrays beyond those wrappers.

The active source caller's 17 aligned outputs, active collector's 27 scratch arrays, active scorer and remnant membership array remain the parent's assigned work.
The parent subsequently reports those ownership repairs implemented, with three active-remnant test groups passing and the connected-leaf case failing against commit `545c509bf4531d48ebece6d9c0bfcc4f211d19c0`.
Those are parent-reported results and were not independently rerun or edited by this worker.
The parent explicitly queues final commit-boundary remnant proof and borrowed-global cleanup for the next tranche.
No central router, wrapper skill, balance fallback or eligibility substitute was introduced.

## Reference and MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
The connected live schemas expose reference context/search/read, source lookup, script validation and event inspection.
The current reference-context request for temporary array/scalar output ownership and the narrow `chaosx.nr21.20` lint request both timed out awaiting `tools/call` after 600 seconds.
The narrowed documentation search for `clear_temp_array` succeeded and returned installed `documentation/effects_documentation.md:2763-2772`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, citation ID `dcdebea75360185b5af6d53465dd1ea6882c026351191d75ff538b6c962e81ae`.
Its revision-bound read also returned `OK` for the complete ten-line cited section.

The earlier successful live wiki read in this same task is `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, citation ID `93a8a69289bba58764f83d5e14f30b8ecd53bf302360aa6db24d21dcb7c17578`.
Line 440 establishes caller-preinitialized temporary output storage across scripted helpers.
Direct local reads confirm the same wiki and installed-documentation sections.
Vanilla precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/operation_strat_effects.txt:77-87` directly initializes temporary operation and score arrays before populating them.
The source-only fixture checks do not replace unavailable MCP lifecycle evidence.

The focused source lookup returned `OK` for `event021_parent_collect_dynamic_optional_front_candidates`, index revision `76ac93d5d8e8b7d24d6040ad266df6752504ce0007b68a57be4d7f6889d4d0a4`, with one unshadowed, non-overridden definition at then-current lines 830-1091.
It returned the first ten lines and `nextLine=840`, so this is bounded location evidence rather than closure coverage.
Subsequent scope-contract comments shift the collector's final line anchor, with its identifier and direct array initialization unchanged.
The two-command COUNTRY initialization snippet returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, checks for syntax, command kind and declared scope, and `parametersChecked=false`.
Both commands are documented for the declared scope, while the `set_temp_variable` argument block remains explicitly unchecked by that validator.
The installed assignment syntax and examples at `effects_documentation.md:7820-7841` were read locally and match the existing repository form, without turning this partial result into engine proof.
No lifecycle or rendering artifact has been returned for the candidate closure.

Final candidate source SHA-256: `78aad935549ee9631d2617701049837fdf482362f35c4d3ec076ae9302988589`.
Final source execution test SHA-256: `10f9a904ccbeb70461509cf57f801242b0af07b9631b0b5d3c2132efc0889c49`.

## Limits and disposition

The delegated helper patch and five test groups are complete.
Integrated opening lifetime safety remains unresolved until the parent applies and reviews its outer caller changes, with active ownership completion reported separately above.
Native behavior, full event lifecycle coverage, and live package/force restoration remain unproven.
No gameplay simplification was made.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, particularly their output lifetime, source execution and bounded ownership rules.
No skill file was changed because the existing events skill already covers this failure mode.
