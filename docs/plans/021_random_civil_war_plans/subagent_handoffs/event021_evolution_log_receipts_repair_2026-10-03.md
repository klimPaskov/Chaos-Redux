# Event 021 evolution log receipts repair

Disposition: implemented source repair, live evidence and broader evolution behavior unresolved.
Acceptance basis: the full Event 021 goal requires three truthful evolution records, and the accepted active-war Evolution I repair addendum identifies incorrect attribution to the global scheduler as a defect.

## Implemented behavior

All three parent evolution callbacks keep caller-owned storage for the event ID and evolution type before invoking `event021_prepare_evolution_log_context`.
They assign their existing stage and tier afterwards.
They initialize the actor indicator to zero and invoke `event021_select_verified_evolution_log_actor` immediately before the shared recorder.
This event-owned selector supplies context only.
Shared recording, history projection, sanitization, and Event Details remain in the existing shared logger.

The selector validates aligned front arrays, active row status, positive front and crisis IDs, live human canonical host with the same crisis, and live registered actor with matching immutable front and crisis IDs.
It selects the first verified row in the existing array order.
Human Event 006 actors remain eligible, while actual nonhuman actors are excluded.
No valid row produces the existing no-actor record.
A stale regular actor target does not override the explicit zero indicator.
No evolution admission, MTTH, weighted target score, cap, generation, force allocation, Chaos outcome, or public log count changes.

## Files and validation

- `common/scripted_effects/021_random_civil_war_evolution_log_effects.txt` implements the verified context selector.
- Its companion Markdown documents scope, caller-owned output, source-only inputs, effects, and no-actor behavior.
- The parent effects change only the three callbacks' input storage and actor-context calls in this repair.
- `021_random_civil_war_effects.md` documents the existing context helper's caller-storage contract.
- `.tools/test_event021_evolution_log.py` interprets the actual selector, context helper, shared logger actor gate, and committed sponsor receipt definition against declared fixtures.

`python .tools/test_event021_evolution_log.py` passes ten test methods.
It tests live participant selection instead of the scheduler, fourteen invalid actor/host/registry cases, human Event 006 admission, no-actor prefire, stale actor target handling through the shared logger's actual gate, caller ordering in all three callbacks, the final valid row after 1,001 rejected rows, and callback ID/type survival under conservative helper-frame cleanup.
It also tests a valid sponsor receipt with a third-country ROOT and nine missing, dead, inactive, or mismatched sponsor cases for commit `1f90ca368a06d2e12a6db4dd897a605908f6458b`.
The test interprets only the explicitly listed commands and uses declared fixture results for the shared actual-nonhuman classifier.
It does not emulate campaign scheduling, AI, missions, country creation, engine temporary-variable behavior, or live UI rendering.

The native array loop and regular target contracts were read in installed `documentation/effects_documentation.md`, lines 4279-4312 and 6496-6504, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Temporary output lifetime was read in offline Data structures, line 440, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The shared logger's existing explicit actor-indicator branch is the repository precedent.

The first narrow event trace on `chaosx.nr21.2` timed out after 600 seconds.
The required narrower retry on `chaosx.nr21.11`, depth one and two nodes, was requested before declaring a route gap.
MCP evidence remains pending until that retry returns, and focused trace coverage cannot prove helper or lifecycle completeness.
The separate architect review also remains pending at report creation.

## Remaining goal work

Accurate metadata is a separate repair from active-war evolution gameplay.
The bounded active theater review, source-owned front receipt, live force bridge, management phase, native temporary-country capacity proof, broader actor/asset acceptance, full probability checks, completion audit, and live acceptance retain their recorded unfinished status.
This repair does not establish a clean full error.log or completion of Event 021.
No fallback or gameplay simplification was introduced by this metadata repair.
Skills used are `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
