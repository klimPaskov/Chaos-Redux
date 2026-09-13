# Event32 contracts20 probability evidence

Audit status: baseline READY for the parent-owned output correction review on 2026-09-05.

This read-only pass covers `common/scripted_effects/032_missiles_operations_effects.txt` at the parent-provided post-temp19 SHA-256 `54EAC3B29FE7980A16AA381AA860880A12D37C600B86DEC3428ED455923643CA`. The only in-scope source sites are the country best-score assignment at current line 1651 and cleanup at 1659, plus the state best-score assignment at current line 1814 and cleanup at 1819. No source file was edited here.

## Mandatory probability baseline

The declared scenario family is `E32-C20-country-first`, `E32-C20-country-higher`, `E32-C20-country-lower`, `E32-C20-country-tie`, `E32-C20-country-invalid`, `E32-C20-state-owned-first`, `E32-C20-state-controlled-higher`, `E32-C20-state-controlled-lower`, `E32-C20-state-tie`, and `E32-C20-state-invalid`.

The narrow `hoi4.probability_inspect` call was run for `missiles_score_target_country_candidate` and repeated for `missiles_score_operation_target_state_candidate` against the same source with `refresh=true`.

Both calls returned `status=ok`, `code=PROBABILITY_SOURCE_DISCOVERED`, MCP `sourceRevision=204fb8b364cf43d6650e6cbd324d3eba0c705263a92a4ddd3fdfdc7657094105`, and MCP `sourceHash=683a00643a06fd558157cd7b7a0e0d705e62ff7a7a019a893a79e3359212bee3`.

The shared artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c844500089e816982ac1ecd1979b1eda9eb04493df04a05c54c4d9d1faac606e/96f49108f906d300efda7a5ada1c5c4126ca180757fc204e693612257680672a/probability-inspect-683a00643a06.json` with artifact SHA-256 `c844500089e816982ac1ecd1979b1eda9eb04493df04a05c54c4d9d1faac606e`.

The inspect found `candidates=0` and `identifierMatches=0` for both requested helpers. It suggested the `random_list` adapter only because source inventory found 19 later candidates, currently represented as `032_missiles_operations_effects.txt:2492.entry.*`; that tail corresponds to the earlier pre-deletion line-2517 inventory and is explicitly outside this audit.

This is a deterministic score audit with no valid probability-proportional candidate pool. No numeric probability, timing distribution, seeded simulation, rank reversal, dominance, starvation, repetition, or exploit-risk result is claimed.

## Output and score-flow proof

The country helper initializes `missiles_target_candidate_score` unconditionally at line 1609 with `constant:missiles_target_score.baseline`, then adds the profile, major, factory, controlled-state, war, history, island, resistance, and strategic-depth terms before comparing that same unscoped variable at line 1648 against `ROOT.missiles_best_target_country_score` using strict `greater_than`.

The current best-output assignment at line 1651 instead reads `PREV.missiles_target_candidate_score` inside the nested `ROOT` block. The total is initialized before every local read and all additions are complete before the comparison, but the scoped `PREV` namespace is not proven to resolve the unscoped temporary. The parent-authorized correction removes only the `PREV.` prefix so the best-score output reads the same unscoped total that the strict-greater condition compared.

The country cleanup at line 1659 follows the comparison and output writes. Removing it does not alter initialization, any score addition, the strict-greater condition, candidate filters, `global.enabled_countries_list` traversal, target event-target save, target id output, flag, or tie order. The output correction can change durable best-score data and therefore selected-target behavior where the malformed scoped read previously failed or resolved differently; that is the intended functional correction and is not a weight change.

The state helper initializes `missiles_target_state_candidate_score` unconditionally at line 1752 and adds profile, infrastructure, buildings, frontline, island, resistance, secure-state, and poor-guidance-isolation terms before comparing that same unscoped variable at line 1810 against `ROOT.missiles_best_target_state_score` using strict `greater_than`.

The current best-output assignment at line 1814 instead reads `PREV.missiles_target_state_candidate_score` inside the nested `ROOT` block. The total is initialized before every local read and all additions are complete before the comparison, but the same scoped-`PREV` versus unscoped-temporary contract is unresolved. The parent-authorized correction removes only the `PREV.` prefix so the best-score output reads the total used by the comparison.

The state cleanup at line 1819 follows the comparison and output writes. Removing it does not alter initialization, arithmetic, strict-greater behavior, owned/controlled filters, traversal order, event-target save, selected-state output, or selection-result flag. The corrected output may change which state is recorded when the malformed scoped read did not carry the compared total; this is output correction evidence, not evidence of a tuning change.

The country scenario checks are score-only structural cases: first valid candidate writes its compared total, a higher next candidate replaces it, a lower next candidate leaves the earlier best, an exact tie leaves the first because comparison is strict `greater_than`, and an invalid candidate contributes no score or update because the ordinary-target validity gate fails.

The state scenario checks are likewise score-only structural cases: the first valid owned-state candidate establishes the best, a higher controlled-state candidate replaces it, a lower controlled-state candidate leaves the earlier best, an exact tie leaves the first traversal result, and an invalid or profileless state is excluded by the existing state filters.

The state selector still traverses `every_owned_state` before `every_controlled_state`, with `missiles_target_state_is_valid = yes` and `missiles_operation_target_has_profile_value = yes` on both loops. The audit does not deduplicate a state appearing in both loops or change either filter.

## Candidate pools and continuation limits

The country candidate pool is dynamic `global.enabled_countries_list` filtered by `missiles_ordinary_target_is_valid`; the actual runtime list and trigger values were not supplied to the MCP, so it is incomplete for probability normalization.

The state candidate pool is dynamic owned and controlled states of the selected target filtered by the two existing state predicates; the actual runtime state set and profile/building values were not supplied, so it is incomplete for probability normalization.

Relevant external factors include the operating country's profile and score variables, candidate validity, major status, factory and controlled-state counts, war and incident-history flags, capital island and resistance state, target profile, state buildings and infrastructure, neighboring ownership, guidance, and the selected target scope. These factors were preserved as source conditions and were not assigned invented values.

After the scorer, `missiles_select_operation_target_state` calls `random_owned_controlled_state` at lines 1852-1859 whenever the selected target is valid and can overwrite `missiles_operation_target_state`. Therefore the scenarios above validate the scorer's best-score output and selection-result writes only; they do not establish the final operation target after that later continuation or its fallback calls.

## Unsupported routes and follow-up

The consulted vanilla effects documentation documents `set_temp_variable` and regular `clear_variable`, but has no `clear_temp_variable` effect entry. The offline data-structures reference describes temporary variables as unscoped scratch values and does not provide a supported cleanup equivalent for these sites.

The parent may apply only the two `PREV.`-prefix removals and the two terminal cleanup deletions, preserving all constants, score additions, comparisons, filters, loop order, event-target writes, output identifiers, and random continuations. This report does not authorize sentinel, reserve, weight, threshold, or selection changes.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, and `hoi4.probability_render` have no valid in-scope adapter or complete candidate pool to consume. No probability comparison was started in the baseline pass, and the later random-list surface is not a substitute. A post-source inspect and comparison can be recorded after the parent supplies the patch hash only if the service exposes a matching deterministic score projection; otherwise the exact unsupported deterministic route remains the blocker.
