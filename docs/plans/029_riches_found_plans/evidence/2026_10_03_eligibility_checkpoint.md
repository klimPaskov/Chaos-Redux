# Event 029 eligibility and probability checkpoint

Date: 2026-10-03.

Disposition: typed fixture construction and source-byte pinning are complete for this checkpoint; weighted-score, probability, and timing results remain unresolved. This is a read-only audit. No gameplay source, weights, tuning constants, or index entries were edited, and HOI4 was not launched.

## Typed scenario records and adapter binding

`2026_10_03_typed_scenarios.json` contains 39 complete records whose identifiers match the 39-entry registry in `2026_10_03_scenarios.json`, plus 31 complete supplemental records for foreign access, pending-country leases, cost equality, one-to-four-mine contribution, closed-risk/output gates, all ten Surface M pools, and the repeatable recipient pool. The seven adjacent typed suites contain 87 more records: 19 late-outcome, five aggregate-stage, 13 account-obligation, 12 anti-farm, four predatory-cost, 32 exposure/selector/pay-train/pressure, and two incident-age fixtures. `2026_10_03_all_glitters_typed_scenarios.json` adds five All That Glitters boundaries. Every one of these records was checked for both a root `state` object and `scopes.FROM.state`; none is missing either required record. The 39 registry comparison has zero missing or extra IDs. The 162 record total counts intentionally repeated named comparison cases in separate suites more than once.

Decision-inspector fixture envelope used: `{id,actor,date,closedFlags,flags,state,scopes,controls}`. The live probability evaluator rejected `controls` and `closedFlags` as non-scenario keys, and separately returned the exact requirement `Provide exactly one source or customPoolManifest` when a typed scenario omitted `source`. The evaluator projection used here is `{id,actor,date,flags,state,scopes}` with optional `eventTargets`, plus one source path. Fixture controls remain declared annotations; they are removed from the evaluator projection, not silently treated as game state. Typed scenario values beyond the explicit user-provided `RF_POLICY_01_STABLE_DEMOCRACY` values are representative boundary controls, not accepted balance values or campaign snapshots.

Bound country-state fields include political/command power, equipment and fuel stocks, convoys, manpower, stability, war support, factory counts, global chaos, controller mine counts, and selected-mine value. Bound state scopes include mine sequence/profile/quality/development, pressure, order, legitimacy, crisis flags, operating state, and separate ownership/controller scopes where relevant. Unknown or unrepresentable facts are retained in the per-scenario coverage ledgers.

## Probability MCP evidence and exact result status

All requests used explicit workspace ID `mod_chaos_redux_ea3b2d67c2c0` and mod-relative source paths.

The retained baseline `probability_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb24a045ace9b5aa91e15e07ce7bcb955c061fd7925b06ea8924d37941f56518/3ad3e1aa8ba465630212541a59707756cb2f6ed94c256f8ccf4e6768523a0d8a/probability-inspect-0f70e76d1dd0.json`, source revision `ee6db43d3e8566b2e74f54e0c5c14676faf88a985d30e734f40029a40be2fdc0`, analyzer source hash `0f70e76d1dd0c1b13cab670173a89b9eaa1d9500f2380a810c1a48b015953fd7`. Its 102-candidate catalog placed `decision_riches_found_select_mine` alone in `decision_ai_will_do` and `decision_riches_found_offtake` among 101 `mission_ai_will_do` entries. This is an unresolved adapter/source classification mismatch, not proof that the state-targeted decision is a native mission and not a click probability.

The current-source retry for `mission_ai_will_do` on `common/decisions/029_riches_found_decisions.txt`, restricted to `decision_riches_found_offtake`, reached its final tool result and timed out after 600 seconds. It returned no revision, source hash, artifact, candidate completeness, or weight trace. A distinct current-source `event_option_ai_chance` inspect for the complete five-option pool on `events/029_riches_found.txt` reached its final tool result and timed out after 600 seconds, returning no revision, source hash, artifact, candidate completeness, or option score. Earlier current-source `probability_evaluate` and threshold `probability_sweep` for the artifact-suggested mission adapter also timed out after 600 seconds.

A minimal typed evaluation was submitted for `RF_POLICY_01_STABLE_DEMOCRACY`, adapter `decision_ai_will_do`, candidate `decision_riches_found_select_mine`, source `common/decisions/029_riches_found_decisions.txt`, metric `raw_value`. It used the fixture's complete typed actor, date, flags, root state, and scopes, with evaluator-unsupported annotations removed. The call reached its final tool result and timed out after 600 seconds. No numeric base value, modifier trace, score, rank, scenario hash, or artifact was returned.

A same-fixture `probability_compare` was submitted for `RF_AI_TWO_MINES_NO_SELECTED_POINTER`, using adapter `decision_ai_will_do`, the immutable initial decision snapshot SHA-256 `1a485534b48a59d780a53c09642e4618659c69f8fcedda9f735cca412f886a14` as before, the pinned checkpoint decision source SHA-256 `b9607d97bb1304dadbb718f37b4fdc3b774c041fcc59a0ff56e44fe9a547ec05` as after, and candidate `decision_riches_found_select_mine`. It reached its final tool result and timed out after 600 seconds. No before/after score delta, rank change, scenario hash, comparison ID, or artifact was returned. This remains unresolved, not a pass.

No `probability_render` artifact exists because none of these calls returned an analysis ID. The source-restricted one-candidate evaluation/compare, even if they had returned, would be score-only and would not establish a candidate race or click probability. No exact or bounded selection probability, ranking, starvation, rank reversal, or timing distribution is claimed.

## Pinned current source bytes and comparison boundary

The exact eligibility-checkpoint bytes were copied into `evidence/2026_10_03_eligibility_checkpoint_after/` and each copy hash matched its source file at capture:

| Current source | SHA-256 |
| --- | --- |
| `common/decisions/029_riches_found_decisions.txt` | `b9607d97bb1304dadbb718f37b4fdc3b774c041fcc59a0ff56e44fe9a547ec05` |
| `common/scripted_triggers/029_riches_found_triggers.txt` | `3e0ad55e96ea6e6f94ebfa390b95acf349d9f44f1112e1a1a1415b0b04cba585` |
| `common/scripted_effects/029_riches_found_effects.txt` | `def976bce0b6ef3fe4d7d1b54370a6ec08f0c37838a9992903b56c2f79b91651` |
| `common/scripted_effects/029_riches_found_incident_effects.txt` | `56317b35db83231099b7229dbf110b5a9a1545f9c12d2606951d8b19def71369` |
| `common/scripted_effects/029_riches_found_maintenance_effects.txt` | `77141c5f31404b83b37f6e07df1616022d15d07daf59a30b1cb0e03026f9c1d0` |
| `common/scripted_effects/029_riches_found_exposure_effects.txt` | `f63673e1a5ffc7a78a67752be86f59de0d1acce3307a3ee3d62b67897a5627d2` |
| `common/scripted_effects/029_riches_found_account_effects.txt` | `b5cbb98db09a02bf7525b2f5775792638e5bcd63b5e24fb2b84cbdef03f7320e` |
| `common/scripted_effects/029_riches_found_late_outcome_effects.txt` | `501906c902bd17a2a0107fbf6c61cb93f2a7473f465d1e688cae6f12022f84af` |
| `common/scripted_effects/029_riches_found_aggregate_stage_effects.txt` | `1b70dfe1adb0f3efa09132c9b0e5d2a0df1d831a1a557f71029a6cf6e3d7dee9` |
| `common/scripted_effects/029_riches_found_achievement_effects.txt` | `64a63320da1e4a22707c36a3518d0302118372f2f25a5bac405f88ee4d8d7c09` |
| `common/scripted_triggers/029_riches_found_achievement_triggers.txt` | `e2020f19cf356a8a7710e2730b0fcd22fc7e89ea66a66661d2935a37d5d72614` |
| `common/mtth/029_riches_found_mtth.txt` | `32c989917b468b76c5a6a98a4190b0d490c38651f1be429eadd667b2927acb5f` |
| `events/029_riches_found.txt` | `45c0ce4f5c22d503af9b627ce8300eea463894deef2be54dbbac41864a29dcca` |
| `events/029_riches_found_verification.txt` | `428b61979a1aef41489c7e40b8a5cf79979b3dd97731c3880f89e1cc9bd36ffd` |
| `common/script_constants/029_riches_found_constants.txt` | `87dcb0df00896f3f1ce176c12cb73d73111690c960df7af557b0b8856e43efa3` |
| `common/ideas/029_riches_found_ideas.txt` | `b0400ae250ec13a910f2210d8dd444391b39cbff66368ec395c19acc0f6ab297` |
| `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` | `0331857939315df313bfd18e44ce5c9fa94538a74c7fa59550ba2d5410c2aabe` |

The immutable initial before copies remain in `evidence/2026_10_03_before/`: decisions `1a485534...`, triggers `01c6e98c...`, core effects `a991dde1...`, incident effects `01648014...`, MTTH `32c98991...`, root events `618f87c3...`, and constants `49939421...`. The aggregate-stage tranche retains its own before copies of ideas (`29bdb204...`), dynamic modifiers (`b3857b05...`), and constants (`3323c89e...`) in `evidence/2026_10_03_aggregate_stage_before/`.

This is an exact initial/per-stage baseline, not a captured immediate pre-repair worktree. Earlier handoff checkpoints mention intermediate live hashes `d22d82ab...` for the core effect and `5474ceaa...` for the maintenance helper, but their exact bytes were not retained in an immutable before folder. Do not describe the current compare as an exact delta from those intermediate hashes. New maintenance, exposure, account, late-outcome, aggregate-stage, achievement, and verification files have no matching pre-tranche source copy in the initial baseline. Their current after bytes are pinned here; their missing before-closure is explicit coverage loss, not an assumed empty source.

## Current eligibility, pulse, and All That Glitters source findings

`riches_found_state_is_active_selected_or_only_mine` in `common/scripted_triggers/029_riches_found_triggers.txt:171-` admits the registered-mine path when the current controller is AI, while the human branch checks the selected pointer. `decision_riches_found_select_mine` remains in the immutable decision file; its current score source uses the existing minimum/base/claims terms. No new AI coefficient is identified in this tranche. The raw-score evaluation and same-fixture comparison nevertheless timed out, so numeric equality is not established.

The current core initializes the state-owned `riches_found_last_pressure_growth_date` on mine entry. `riches_found_run_maintenance_pulse` computes that date plus `constant:riches_found_duration.controller_pulse_days`, requires the mine to be operating and the due date reached, writes the state-owned receipt, and only then grows pressure. This is source evidence for a 30-day per-mine cadence guard against duplicate country pulses; it does not prove cumulative runtime equivalence or callback cadence. Contract lifecycle/account service and pre-entry exposure remain before this operating-only pressure block; incident review is separately guarded by active-mine status. Existing mission progress dates remain a distinct lifecycle path.

The new `2026_10_03_all_glitters_typed_scenarios.json` contains five typed cases: 179-day and 180-day window edges, a closed registered terminal tombstone in the denominator, exact aggregate caps versus a value just above cap, and an excluded CXT fixture mine. Current source counts every controlled registered state before the terminal-maintenance filter, while safe contribution count is accumulated only inside the controller-output branch and the safe-state trigger requires open/regulated status. The All That Glitters predicate checks safe count equals `riches_found_controller_registered_mine_count`; its five aggregate checks reject only values greater than their caps, so equality is accepted. The authored hold is 180 days. This matches the user's required denominator/window/cap/fixture exclusions at source level. No probability MCP route establishes achievement evaluation, native date behavior, callback delivery, or continuous-window runtime behavior.

## Exact remaining blockers

- `decision_riches_found_offtake` remains misclassified between the decision and mission adapters; the current mission inspection timed out. The complete 101-entry mission-side candidate race and all external strategy/modifier factors are unresolved.
- The one-item selected-mine candidate request is suitable only for a raw score. The decision catalog provenance is baseline-only; no current full candidate pool or rank was returned.
- The five root policy `ai_chance` options are a separate adapter surface. Its current inspect is pending at this handoff capture; its result must be recorded after completion. No option probability is inferred from source weights.
- Ten incident/random-list families and Evolution I/II/III MTTH timing remain without complete probability artifacts. Prior random-list and MTTH inspections timed out; no complete candidate pool, uncertain-input distributions, full cadence/transition manifest, or rank/timing sweep is available.
- External foreign sponsor enumeration, complete neighborhood/faction/opinion/access inputs, current event-target freshness, native country/state scope semantics, and maintenance/event callback timing remain unresolved.
- No `probability_evaluate`, sweep, or compare produced a number or artifact at this checkpoint. All weights remain unchanged by this auditor, and no balance signoff is given.

No source simplification or fallback was applied. The outstanding limitations are MCP analysis/candidate-coverage gaps and missing immutable before bytes for newly introduced helper files.

## Subsequent live-source drift, preserved for the next pass

After the eligibility-checkpoint copy and its probability comparison request were submitted, six live files changed. Their exact current bytes are separately pinned in `evidence/2026_10_03_eligibility_followup_live/`; the checkpoint copies above were not overwritten. These diffs add account-resolution/containment and bind-terms behavior: account close/bind decisions gain receipt and validity gates; scripted triggers gain sealing-access/account-binding predicates and suspend output during account containment; core effects add bound-account contribution state and account-resolution cleanup; the account helper adds deadline-warning and resolution/containment/binding receipts; aggregate stage detection switches from `account_closed` to `account_closure_finalized`; constants add account-resolution choices plus bound integrity/pressure values.

The decision-source diff contains no changed `ai_will_do`, `ai_hint_pp_cost`, or AI-weight lines, and the constants diff contains no changed AI-weight lines (`Compare-Object` on those source lines returned zero differences). These later account-phase edits are outside the frozen eligibility comparison; they are not included in the reported comparison request and require their own same-fixture pass if they affect weighted candidate validity or timing. The request used the frozen `eligibility_checkpoint_after` decision copy, so it remains an exact source pair despite later live edits. Its final tool result was the 600-second timeout already recorded above; there is no numeric result to carry forward.

| Later live file | SHA-256 in `eligibility_followup_live/` |
| --- | --- |
| `common/decisions/029_riches_found_decisions.txt` | `5cb3798d0dd3c76d41e3be99eb23edccd88d62d140127bb0d5ab143578a6e7c3` |
| `common/scripted_triggers/029_riches_found_triggers.txt` | `0584bd7297eac88fb98f2b4e0b317ce4a410306d86483db6653562944a6324cd` |
| `common/scripted_effects/029_riches_found_effects.txt` | `cefc4912fef7528fb83a6967fd2ce49997af633f3e651a69daa9f7c7b1964451` |
| `common/scripted_effects/029_riches_found_account_effects.txt` | `6118906ec832ab34cf8b1a243ca0bc1ed203e76d5098dda95bdf233a9992759d` |
| `common/scripted_effects/029_riches_found_aggregate_stage_effects.txt` | `1d549b978469a503e5efe352a2a82e4a804e33222a1faba89bb73651366f0a54` |
| `common/script_constants/029_riches_found_constants.txt` | `2389827a34592c98ef68a33a57310ae43c72a352e2536fc040dc9b3412e90fbd` |
