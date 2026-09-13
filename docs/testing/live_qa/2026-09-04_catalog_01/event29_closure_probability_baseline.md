# Event29 temporary closure AI willingness baseline

Audit date: 2026-09-05.

Status: bounded read-only baseline and virtual before/after comparison completed for the Event29 temporary closure decision. The owner brace patch was not applied, no gameplay file was edited, and no balance target was selected.

## Audited surface

The exact surface is `decision_riches_found_temporary_closure` and its `ai_will_do` block at `common/decisions/029_riches_found_decisions.txt:3741-3752` in the current worktree.

The current source has `base = constant:riches_found_decision_ai.medium` followed by the unchanged `is_major`, `has_war`, multiple-mine-priority, low-local-order, severe-extraction-pressure, and democratic modifiers.

At line 3747 the severe-pressure modifier has two closing braces after the `check_variable` body instead of three, so its outer `modifier` remains open when line 3748 is parsed.

The democratic modifier at line 3748 is therefore nested inside that still-open modifier and is exposed to the invalid trigger-modifier shape reported by the owner.

The proposed owner repair is syntax-only: add the missing close to line 3747, leave the democratic factor and threshold unchanged, and remove the compensating close at line 3749 so the democratic block is an `ai_will_do` sibling.

The source constants are `riches_found_decision_threshold.pressure_severe = 85` at `common/script_constants/029_riches_found_constants.txt:517`, `order_low = 35` at line 511, `riches_found_decision_ai.medium = 3` at line 623, `low_factor = 0.50` at line 626, `high_factor = 2` at line 627, and `urgent_factor = 4` at line 628.

## Required references

The audit read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md` before reviewing the source.

The offline Paradox wiki pages consulted were `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`.

The relevant wiki rules are that decision `ai_will_do` is an MTTH-style willingness score, `factor` modifiers multiply the base, strict `greater_than` does not include equality, and `ai_will_do` is not a click-probability declaration.

The vanilla documentation consulted was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `modifiers_documentation.md`, `effects_documentation.md`, and `script_concept_documentation.md`.

Vanilla decision precedents in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AFG.txt` and `BUL.txt` use sibling `modifier = { factor = ... trigger = ... }` blocks under `ai_will_do`, matching the proposed brace ownership.

## MCP inspection and provenance

The required first call was `hoi4.probability_inspect` with adapter `decision_ai_will_do`, the exact source path, identifier, one-candidate pool, and `refresh = true`.

The decision adapter returned `PROBABILITY_SOURCE_DISCOVERED` with `identifier_not_found` for the requested decision and suggested `mission_ai_will_do`; its discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9911f0ec56ee7d186244dce38a9e2b5741ea100402287ce774b5702b3d566157/829722a4da8e6ee34e14201787c78ae10bdb09adfef010ca6d253b28c2e56a29/probability-inspect-943110a2afa7.json`.

The matching mission adapter inspection completed with `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, `candidates = 1`, `availableCandidates = 0`, `requiredInputs = 4`, and `unresolved = 0`.

The current matching inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd0c4d5ca1bd28f05ec0018df6e63181631402d48c02653de5349d024f701ed8/3ab48e28eaf0d120ca5be398df2e752cc550452a83268f8e119da5cfb47265b2/probability-inspect-943110a2afa7.json`.

The current path-backed MCP source hash is `943110a2afa75c8ff9eaf843775505f9ea6fc134b196f5e7a40b86d1d3f2784b`.

The source revision was `029c63120ed12fc88c6775e77188e0a9022f863ca987fb0336863f06d0a13744` during the first inspect and evaluate, then `21aa69078c4f20df4b31a2fbe8f96ce5d1c3cb2a0bc7d18f41016764771561a3` during the later inspect, sweep, and compare.

The source hash remained identical across that revision drift, which is consistent with the parent’s concurrent unrelated scalar/name repairs changing the file revision while leaving this weighted block byte-identical.

The MCP adapter identifies the surface as `mission_ai_will_do`, `score_only`, with `rawScore = true`, `normalizedProbability = false`, and `timeDistribution = false`.

## Scenario contract

The same six named scenarios were used for the baseline evaluate and virtual compare.

| Scenario id | Government | Extraction pressure | Strict threshold relation | Fixed other predicates |
| --- | --- | ---: | --- | --- |
| `RF29_CLOSURE_PRESSURE_BELOW_NON_DEMOCRATIC` | `fascism` | 84 | below 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |
| `RF29_CLOSURE_PRESSURE_AT_NON_DEMOCRATIC` | `fascism` | 85 | equal to 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |
| `RF29_CLOSURE_PRESSURE_ABOVE_NON_DEMOCRATIC` | `fascism` | 86 | above 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |
| `RF29_CLOSURE_PRESSURE_BELOW_DEMOCRATIC` | `democratic` | 84 | below 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |
| `RF29_CLOSURE_PRESSURE_AT_DEMOCRATIC` | `democratic` | 85 | equal to 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |
| `RF29_CLOSURE_PRESSURE_ABOVE_DEMOCRATIC` | `democratic` | 86 | above 85 | `is_major = no`, `has_war = no`, priority flag false, local order 60 |

The actor was `CXT` and the date was `1936.1.1` for every row.

The fixture also declared the target-state booleans for controlled ownership, mine-state, active-selected-or-only-mine, emergency phase, crisis phase, and an unset closed flag, plus scoped values for `riches_found_local_order`, `riches_found_extraction_pressure`, and `riches_found_multiple_mine_priority`.

The source candidate pool contains exactly `decision_riches_found_temporary_closure` and is complete at the discovered source boundary.

The adapter still reports the runtime candidate as unavailable and cannot bind the decision’s `FROM` state scope from the flat scenario declarations, so external-factor coverage is complete for the declared fixture fields but incomplete for engine-equivalent target scope resolution.

No seed, random input, cadence, timer transition, or terminal state was declared because this is a decision willingness score rather than a sampled pool or timing distribution.

## Baseline evaluation

`hoi4.probability_evaluate` used adapter `mission_ai_will_do`, the one-candidate pool, the six scenarios above, metric `raw_value`, and outputs `json`, `ranking`, `matrix`, `waterfall`, and `unresolved`.

The evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-486c8c9fb4bbf43e727c98a2`, scenario hash `b83074bcc4e048ea4bf1773d6d45aceaa6787979cfd417f86ec852c34b974954`, source revision `029c63120ed12fc88c6775e77188e0a9022f863ca987fb0336863f06d0a13744`, six scenarios, six candidate rows, and two aggregate unresolved categories.

The authoritative rendered JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d62058450efc4c78ad1328f897a85f5a4edcfb36ef370bb582548d0169be8fb/eb30cae508a1bec8100a29822ddd415b65b8f77a413671b8dea6000522df0ff0/probability-486c8c9fb4bbf43e727c98a2.json`.

The baseline ranking, matrix, waterfall, and unresolved render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09f4925c6dda988c621b4eae1c896830fee71cab537419dbc5d5167789488d41/9d6867d6075c1f86f957ab21ddaeffc7567194615ee40b655866322fa155bbb2/probability-probability-486c8c9fb4bbf43e727c98a2-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0308a9de39cd285c4dd38663eae519e0c4dcaf2482e8eddbdeccdb5eafb154f9/a960adeffb264ae76e8e8b0b7c687d0c40424308de34100bac1c6fc69f5d0e89/probability-probability-486c8c9fb4bbf43e727c98a2-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a85147dd338f65c8186060954969735f71341ee59eb59d1006bdbfcd5131b1a5/9f605b408677f8463e9cd8f26926bc53eed9ff4b64ba8e26acd6e423c457163b/probability-probability-486c8c9fb4bbf43e727c98a2-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee3280cbf5658f2045ead3c354a78d4f2298080922eff731ed4141ea1ff79b97/2305228d3630c3a1e3f98339fdfe3572afe566fd39f40a2f8b4cea4cc1b32fa5/probability-probability-486c8c9fb4bbf43e727c98a2-unresolved.svg`.

Every scenario has `poolComplete = true`, one candidate, `supportLevel = score_only`, and candidate `eligibility = unresolved` with no raw score and no rank.

The base expression resolves exactly to `3` in all six traces.

The `is_major = yes` factor resolves false and the `has_war = yes` factor resolves false in all six traces.

The multiple-mine-priority factor, low-local-order factor, and severe-pressure factor remain unresolved because each is reached through `FROM`.

The malformed baseline trace also reports the democratic modifier as an unresolved nested `modifier`, so no baseline row proves whether the democracy factor is applied as an independent sibling.

The baseline is therefore classified `score-only` for adapter capability but `unresolved` for the candidate’s final scenario score and eligibility.

No normalized selection probability, click probability, timing distribution, effective MTTH, dominance, starvation, or recurrence rate is claimed.

## Threshold sweep

`hoi4.probability_sweep` reused the six scenario bodies and varied `scope.var:riches_found_extraction_pressure` at 84, 85, and 86 with three steps, pairwise sensitivity, and rank-reversal detection enabled.

The sweep returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-1c4510e679f89a15bc097aeb`, scenario hash `7694774360a69c3662b80c7319b97d82087cfbd36fae4bf54ec3e2aac2e9ae81`, source revision `21aa69078c4f20df4b31a2fbe8f96ce5d1c3cb2a0bc7d18f41016764771561a3`, six sweep points, and two aggregate unresolved categories.

The sweep reported no breakpoints, no local elasticities, no pairwise interactions, and an empty `rankReversals` array because the only candidate remained unresolved in every point.

The authoritative sweep JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36bd0277bc7dd634b54f3a9b85503881c72daf0ec6618715e04d9344c152c18a/1a902e9fc197134bad9007b109e73d941c4ebe42e950340cd0f896465190cef1/probability-1c4510e679f89a15bc097aeb.json`.

The sweep sensitivity, threshold, and unresolved render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3121cf38d713fcfb8cd303fc48d6648f2e8c7c71910c314fcdc3355c1a4bf79a/ec9c3392582a315723fe87d83cc9010d140afae77afc5819408d06453b3b3574/probability-probability-1c4510e679f89a15bc097aeb-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/69529de2886fea3d2c47ba2ed284613799d325dc2501af7868953ca350867b79/probability-probability-1c4510e679f89a15bc097aeb-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee3280cbf5658f2045ead3c354a78d4f2298080922eff731ed4141ea1ff79b97/84009d5784e70c4255596f6ef5552eb9e2dc58b961278f85c1122ecb2fe57159/probability-probability-1c4510e679f89a15bc097aeb-unresolved.svg`.

The empty reversal result is an adapter observation under unresolved scope bindings and is not evidence that the malformed source cannot produce a gameplay rank change.

## Virtual same-scenario comparison

The owner patch was modeled in memory by supplying the complete current file as `before.inlineClausewitz` and a second complete inline body with only the pressure modifier’s missing close added, the democratic modifier’s indentation normalized, and the compensating close removed.

Both sides used the same source path, identifier, candidate pool, six scenario ids, scenario state values, and adapter.

The comparison returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-34e0a3200f858567f3561da9`, scenario hash `b83074bcc4e048ea4bf1773d6d45aceaa6787979cfd417f86ec852c34b974954`, source revision `21aa69078c4f20df4b31a2fbe8f96ce5d1c3cb2a0bc7d18f41016764771561a3`, `beforeAnalysisId = probability-98a8c1d2de7c02982f2d6cbe`, `afterAnalysisId = probability-9ac2610a5550668c26ca6e47`, `comparisonChanges = 6`, zero diagnostics, and an empty regressions list.

The comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ab58036d26c0bb5a755c3f21f1af6b6104875220d4738eade74c38923701473/40ed7530dfabf4c5afa3478c0d95d2446f731bc6c2b3bb6caabce070255f9a10/probability-34e0a3200f858567f3561da9.json`.

The emitted comparison, ranking, matrix, and unresolved render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a7cbf1e08330875f00c1fea952d9721263ad12539b65145f80206c6feaf86cd/cfd61253948b5913f46f150caab48e04fe13f4a88ba84b5d542b403f7d52d557/probability-probability-34e0a3200f858567f3561da9-comparison.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50a25b6a42a083e8ec2702c36a4b00bc45d446d28c75c36e2ce770e5d783854a/9ddddc8d3f162adb342519b34e4df2d18b81d9500eb461b1ffa3a1da2cc9905d/probability-probability-34e0a3200f858567f3561da9-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0308a9de39cd285c4dd38663eae519e0c4dcaf2482e8eddbdeccdb5eafb154f9/51c161966b362ed80433e5419723431fe6d72ed51583bf0ab3bb1fcdd5ee1622/probability-probability-34e0a3200f858567f3561da9-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec6e4e8e8264cfacb928eef7e6b34ba75e1bc14271e83e0d90cd0b30c86e6ef2/42a2bcc6a18c4373baa9b3989dded3f711827d63aebc442340c949ef7d6d1bb9/probability-probability-34e0a3200f858567f3561da9-unresolved.svg`.

The six comparison changes all add the independent democratic factor at `ai_will_do.modifier[5].factor` in `proposed:inline-probability-source.txt`.

For the three non-democratic scenarios the comparison records the new factor as false and reduces the unresolved count by one, while the attribution remains the generic `source or scenario metadata changed` because the malformed before AST did not expose a separate democratic sibling.

For the three democratic scenarios the comparison records `added factor:constant:riches_found_decision_ai.high_factor:true:` and resolves that factor to `2`, while also reducing the unresolved count by one.

The pressure factor remains unresolved on both sides because the adapter cannot bind `FROM`, so the comparison proves the structural sibling change and democratic factor application but does not prove a final pressure-dependent runtime score.

The virtual compare is classified `bounded structural compare with unresolved score and eligibility`, not a balance certification.

An explicit follow-up `hoi4.probability_render` for the comparison analysis returned `PROBABILITY_ANALYSIS_NOT_CACHED` with the exact blocker `Render requires an analysis ID produced by this server process`; the comparison call itself already emitted the comparison, ranking, matrix, and unresolved resources listed above.

## Validity and risk findings

The decision’s `visible`, `available`, and `target_trigger` blocks require a `FROM` state controlled by `ROOT`, flagged as a mine state, active-selected-or-only-mine, in emergency and crisis phases, and not closed, while `target_root_trigger` requires at least one controlled mine state.

The adapter’s unresolved `FROM` binding means the audit cannot prove that the positive willingness score is attached only to a valid target in the live target pool.

The inspection’s `availableCandidates = 0` is an adapter boundary result under the unresolved target context and is not promoted to an exact impossible-choice finding.

The one-candidate pool cannot exhibit competitive dominance, starvation, or a meaningful rank reversal, and no such conclusion is claimed.

The score-only adapter does not model decision cadence or repeated selection, so repetition, timing drift, and campaign recurrence remain unresolved.

The exact source risk is parser structure: before the virtual repair, the democracy block is nested under the pressure modifier and can produce the reported invalid trigger-modifier behavior; after the virtual repair, it is a sibling factor with unchanged factor value and threshold.

Under source semantics, `greater_than` against the severe threshold excludes exactly 85 and activates only above 85, but the MCP could not evaluate that boundary through the unresolved `FROM` scope.

## Recommended owner action

After parent approval, move one closing brace in `common/decisions/029_riches_found_decisions.txt` so the severe-pressure modifier closes on its own line and remove the compensating close that currently follows the democratic line.

Preserve `constant:riches_found_decision_threshold.pressure_severe`, `compare = greater_than`, `constant:riches_found_decision_ai.urgent_factor`, `constant:riches_found_decision_ai.high_factor`, every other factor, and every threshold exactly as authored.

Rerun the matching mission adapter inspection, evaluate the same six scenario ids, and compare the same before/after bodies after the owner patch is applied.

Treat the result as fully resolved only if the target scope is bound or the adapter limitation is explicitly accepted, and keep any remaining score, eligibility, or probability result classified according to the MCP output.

## Skipped analyses and blockers

`hoi4.probability_simulate` was skipped because no uncertain input distribution or seed was declared for this score-only surface.

`hoi4.probability_sequence` was skipped because the decision is not a declared custom pool with cadence, recovery, cooldown, removal, reset, and terminal-state semantics.

Event structural inspect/render was skipped because this bounded task audits only the decision AI score and does not certify the broader Event29 chain.

No live game or desktop validation was performed because live validation belongs to the user.

The persistent blockers are the decision-to-mission adapter mismatch for the requested identifier and the unresolved `FROM` target scope in every evaluated scenario.

No source gameplay file was changed, staged, or committed by this audit.

No simplification or unapproved fallback was used; unresolved MCP evidence is reported as unresolved rather than replaced with source-only probability claims.
