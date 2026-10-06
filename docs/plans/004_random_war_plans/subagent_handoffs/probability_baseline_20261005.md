# Event 004 Probability Audit Handoff

Status: Read-only audit is updated. Current event-option evaluations returned exact conditional shares for both complete option pools. Before/after option comparisons and direct-random distributions remain unresolved because their MCP calls timed out.

No gameplay files were edited. Exact pre-patch copies are preserved in `docs/plans/004_random_war_plans/probability_before_20261005/`.

## Weighted surfaces and source evidence

- Event `chaosx.nr4.2` has options `chaosx.nr4.2.a` and `.b` with `ai_chance` base scores 80 and 20 in the pre-patch source at `events/004_random_war.txt:48,58`.
- Event `chaosx.nr4.3` has options `chaosx.nr4.3.a` and `.b` with `ai_chance` base scores 70 and 30 in the pre-patch source at `events/004_random_war.txt:76,87`.
- The current event file retains those four base values at lines 59, 69, 88, and 98. No option has a source trigger or an `ai_chance` modifier, so each event has a two-option source pool with no source-local eligibility split.
- `random_war_set_declaration_profile` reads stage declarations and special-target threshold constants from `common/script_constants/004_random_war_constants.txt` through `common/scripted_effects/004_random_war_effects.txt:125-159`.
- The baseline stage declaration values are 1, 3, 4, 5, and 6 for baseline through Totalen Chaos, with a world-collapse min/max of 7/8 at `common/script_constants/004_random_war_constants.txt:30-43`.
- The baseline special-target threshold values are 0, 0, 20, 35, 55, and 70 from baseline through world collapse at `common/script_constants/004_random_war_constants.txt:45-57`.
- `random_war_select_pair` and `random_war_select_chain_next_pair` draw the special-target roll and compare it with `random_war_special_chance` at baseline effects lines 311-344 and 386-429.
- The special-target branch tries special aggressor and special target pairs before the ordinary stage-gated major, neighbor, and global fallback selections.
- The country selection candidates are dynamic because `random_country` and `random_other_country` are filtered by the triggers `random_war_country_can_be_aggressor`, `random_war_country_can_be_target`, `random_war_target_valid_for_prev_aggressor`, and `random_war_calm_world_pair_scale_valid_for_prev_aggressor` in `common/scripted_triggers/004_random_war_triggers.txt:5-47`.
- Those gates depend on existence, controlled states, subject and capitulation status, cooldown and chain-member flags, special-country status, war and alliance state, declaration legality, major or faction status, neighbor status, and global chaos stage.
- Chain selections alter the eligible pool through recent aggressor/target and chain-member flags, and a failed pair can stop the declaration loop before its target count is reached.

## Source snapshots and current revision

| Source | Pre-patch snapshot SHA-256 | Frozen current SHA-256 |
|---|---|---|
| `events/004_random_war.txt` | `E9B3496B334F2194CEB024CE56BFB434D43D4031C219C7DB729F93E7C252BBA9` | `7BC426FFA7C281106A2BC15E7A7CA39585863416110057857F1A6B4B58095CB5` |
| `common/scripted_effects/004_random_war_effects.txt` | `1527C5E02297FDC6F115FC4B70FDBC9A9E1443FABEDA8FD6590E1C6439C62BBD` | `5B4E3DBD5CE2479B393731A7D4FB6D83277B5E64D25083EA06205726D76460F5` |
| `common/script_constants/004_random_war_constants.txt` | `A4F63F4EE289A8720A06ED29D034CC83ACCDB86EB9A21793820FF2D5DDF35817` | `707C9D3A80C6232D0ED5D6B41546F98815A6D7AF3EAB6BD0FD63AA0CA2639DFE` |
| `common/scripted_triggers/004_random_war_triggers.txt` | `536F47BC1BFF39AAF73FCD0752847E4D44111A5911E6580F4AB787C623AC966C` | `536F47BC1BFF39AAF73FCD0752847E4D44111A5911E6580F4AB787C623AC966C` |

The successful baseline `probability_inspect` for `event_option_ai_chance` used `events/004_random_war.txt`, reported source hash `40acb5894af992775c633480f6abc38b63d952197987ac69c3844b48f0d66b94` and source revision `461a5a698adcb9e794c2f536fc3eba99dc8a0b9a13c6cd1fb395f0cc1595c6b1`, and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/575b8d89d043b34a98b4e32b12f518f7ece12267bcbd8946a2a9a7cb944b39f9/27862ce18d54afbdb0aa791109d01a9e0ed9a89c3988f58f93fb74a54c26232b/probability-inspect-40acb5894af9.json`.

That artifact identifies four active, unshadowed option candidates across two event pools, requires each selected pool to be complete before normalization, and reports `MULTIPLE_CATEGORICAL_POOLS` when both roots are passed together. The adapter is `event_option_ai_chance`, version `hoi4-1.19.2.v1`, and the artifact verifies game version Operation Postern 1.19.2.0 (d245). Its selection rule is proportional categorical selection with the documented runtime d100 limitation.

## Scenarios and completeness

The submitted scenario set is `004_random_war_baseline_20261005` with `calm_baseline_1936` on 1936.1.1, `tier2_special_available` on 1939.1.1, `tier3_special_unavailable` on 1940.1.1, and `final_declaration_count` on 1945.1.1. Each declared actor is GER and each state object is empty because the event-option source contains no stage-dependent weights, triggers, or source-local modifiers.

Those scenario IDs were supplied to the event-option evaluation and comparison requests with separate fixed candidate pools `[chaosx.nr4.2.a, chaosx.nr4.2.b]` and `[chaosx.nr4.3.a, chaosx.nr4.3.b]`. The overall inspector pool is incomplete until one of those event-specific pools is selected. The source contains no event-option external modifiers, but the analyzer did not return the evaluations needed to confirm normalized results.

The scenario names `tier2_special_available`, `tier3_special_unavailable`, and `final_declaration_count` were not encoded as stage variables or country-pool overrides in the submitted scenario objects. The special-target selection pool and its external country-state factors are therefore incomplete for every random-target scenario.

| Scenario ID | Event-option candidates and factors | Direct-random candidates and factors |
|---|---|---|
| `calm_baseline_1936` | Each selected event pool contains its two source options with no source-local eligibility trigger or modifier. The evaluation timed out before normalization was confirmed. | The declared state is empty and the country pool is unprovided. Source profile values set this context to baseline when the caller supplies that stage, but no direct-random scenario state was evaluated. |
| `tier2_special_available` | Same two source options and no source-local eligibility trigger or modifier. The evaluation timed out before normalization was confirmed. | The ID is only a label in the submitted scenario set. Special-target availability, candidate identities, and all legal-pair filters are unprovided. |
| `tier3_special_unavailable` | Same two source options and no source-local eligibility trigger or modifier. The evaluation timed out before normalization was confirmed. | The ID is only a label in the submitted scenario set. The unavailable-special-pool condition and remaining ordinary target pool are not encoded. |
| `final_declaration_count` | Same two source options and no source-local eligibility trigger or modifier. The evaluation timed out before normalization was confirmed. | The ID is only a label in the submitted scenario set. The documented source count bounds are available, but eligible countries, chain state, and realized declaration count are unprovided. |

## Baseline MCP analyses and results, 2026-10-05

- `hoi4.probability_inspect` succeeded for `event_option_ai_chance` and found the four candidates described above.
- Separate `hoi4.probability_evaluate` calls for the two fixed option pools used the same four named scenarios and both timed out after 600 seconds. The source values 80/20 and 70/30 are therefore score-only evidence, not MCP-confirmed normalized probabilities.
- Separate `hoi4.probability_compare` calls for those same two pools used the genuine pre-patch event snapshot and current `events/004_random_war.txt` with the same scenario set. Both timed out after 600 seconds, so no numeric before/after delta, scenario hash, comparison ID, or rendered comparison artifact was returned.
- `hoi4.probability_inspect` for `direct_random` on `common/scripted_effects/004_random_war_effects.txt` timed out after 600 seconds. This adapter result is unavailable and all special-target frequency and final-count distribution conclusions remain unresolved.
- `hoi4.probability_evaluate` and `hoi4.probability_sweep` were not run for the direct-random surface after the inspector timeout. No probability simulator or sequence analyzer was used because the candidate-country pool and full state-transition manifest were not declared.
- A direct-random comparison submitted before the final bounds and temporary-variable edits used the baseline effects snapshot and current effects path, but timed out after 600 seconds without a comparison ID, scenario hash, or artifact.
- A direct-random `hoi4.probability_compare` using the baseline effects snapshot, current effects path, and shared scenario set timed out after 600 seconds. The request preceded the latest actor-persistence profile edit, so it does not establish a delta for current effects hash `5B4E3DBD5CE2479B393731A7D4FB6D83277B5E64D25083EA06205726D76460F5`.
- No `hoi4.probability_render` artifact can be produced without a completed analysis ID. The event-options render request timed out after 600 seconds.
- The corrected narrow `hoi4.event_inspect` trace for `chaosx.nr4.1` through `.3` used typed event endpoints, an event selector, and a bounded depth, but timed out after 600 seconds. Earlier validation attempts reported that trace `from` and `to` values require a typed `kind`, then that trace requires a `selector`.

## Random bounds and before/after findings

The installed game documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7910-7926` defines `set_variable_to_random` values over the half-open interval `[min,max)` and supports integer output. The matching `set_temp_variable_to_random` section is at lines 7842-7858. The offline wiki Effects page line 707 and Data structures page line 564 describe the same exclusive upper bound and show the temporary-variable form.

Before the owner fix, the special roll used min/max 1/100, so the documented upper bound excluded 100, and the world-collapse declaration count used 7/8, so the documented upper bound excluded 8. The parent corrected the current constants to `random_war_roll.minimum = 1`, `random_war_roll.maximum = 101`, `world_collapse_min = 7`, and `world_collapse_max = 9`, which match the intended documented domains. The parent also changed all three random assignments to `set_temp_variable_to_random`, avoiding persistent normal-variable writes for the declaration count and scratch special roll.

The documented source domains are bounded, but their probability distributions remain unresolved because the direct-random inspector and comparison timed out. No hand arithmetic is used to translate the threshold constants into selection probabilities.

The event-option weights did not change in the current event file. The effects and constants changed for report aggregation, response delivery, helper output initialization, random-range scope, and persistence of the prepared stage profile across nested effect frames. The prepared stage, chaos tier, declaration count, and special-target threshold are stored with the selected actor and pair, restored by `random_war_setup_context`, then cleared after consumption. Resetting the event context after a run also allows a later invocation to choose fresh pairs, so repeated-selection behavior depends on the dynamic candidate pool and remains unquantified.

The current source retains the declaration counts 1, 3, 4, 5, and 6 before world collapse, and the special-target threshold values 0, 0, 20, 35, 55, and 70. The final random fixes change the exclusive upper bounds to 101 and 9 and use temporary-variable draws, without changing those stage thresholds or event-option base scores. The prepared-context persistence preserves the initially selected stage profile and pair across later helper frames. Its effect on repeated or clustered random selection was not MCP-quantified.

## Validity, risk, and recommendations

Both event-option pools have positive source base scores for each option and no source option trigger was found. The raw scores preserve the same ordering in the four named contexts because the source defines no stage modifier. The analyzer did not confirm rank, normalized share, d100 outcome, starvation, or dominance results because the evaluation calls timed out.

The source-only review found no zero-score or explicitly blocked option. It cannot prove that either special-target or ordinary target candidate pool is nonempty in any campaign state. When no special pair is selected, source flow falls through to the ordinary major, neighbor, or global selection helpers according to stage and the remaining legal country set.

Do not tune the AI option weights from this report. Re-run the two fixed-pool evaluations and comparisons when the MCP route is responsive, retaining the same scenario IDs and genuine baseline and current paths.

For exact branch-level analysis, provide scenario-bound country state, subject and capitulation state, recent flags, war and faction relations, declaration legality, special-country eligibility, neighbor relations, chain membership, and the complete eligible target pool at each draw. The current analyzer timeout and missing dynamic pool prevent a probability claim.

The direct-random comparison used the saved effects snapshot and current effects path, but it was submitted before the latest actor-persistence edit and timed out without an after-source hash. It cannot support current effects hash `5B4E3DBD5CE2479B393731A7D4FB6D83277B5E64D25083EA06205726D76460F5`. The before snapshot directory also contains the matching baseline constants, while the current workspace has final constants. A path-only comparison may bind both effects versions against current script constants. Preserve any reported constant-resolution limitation and keep the direct-random delta unresolved if the analyzer cannot bind the baseline constants or temporary-random construct. No additional comparison retry was made after the timeout.

## Reference evidence

- Offline Event modding wiki snapshot, `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:159`, describes event-option `ai_chance` as proportional and notes the engine d100 selection behavior.
- Offline Effects wiki snapshot, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:102`, describes `random_other_country` as selecting a random eligible country other than the current country. The reference-search source revision is `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- Offline Effects wiki snapshot, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:707`, and Data structures wiki snapshot, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:564`, document random range endpoints and the temporary random-variable variant. The Data structures search revision is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Installed effects documentation `set_variable_to_random` and `set_temp_variable_to_random` sections are lines 7910-7926 and 7842-7858. The reference-context source revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `hoi4.reference_context(surface="event")` succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0` but omitted Event modding under its three-section limit. The targeted search for event-option `ai_chance` and both revision-bound `reference_read` requests timed out after 600 seconds. Local offline files were read directly for the cited sections.

## Remaining blockers

- The baseline and fresh direct-random probability inspections timed out after 600 seconds. Random-target outcome probabilities remain unresolved.
- The baseline event-option evaluations timed out. The 2026-10-06 follow-up returned exact current evaluations, but the two before/after event-option comparisons still timed out after 600 seconds.
- The earlier event-options structural renderer and both separate `probability_render` requests timed out after 600 seconds. Current probability-evaluation results include ranking and matrix render artifacts.
- The corrected Event004 structural trace timed out after 600 seconds. The direct-random comparison timed out and did not bind the latest effects hash.
- The direct-random pool has no complete scenario-specific country inventory or state-transition manifest, so target identity, special-pool frequency, repetition, and final fired declaration-count behavior remain unresolved.

No balance target was selected and no gameplay change was applied by this auditor.

Parent integration addendum: the owner subsequently marked the shared Settings failure receipt at the two manual failure sends, preventing duplicate owner and generic feedback.
The resulting current effects SHA-256 is `624c579e7ed14b9c395b202ba06b5423b9430c7c6311b38e9f16ff6fe006b860`.
This change affects feedback idempotence, with no chance or score change.
The recorded timed-out comparison does not validate this current revision.

## Live MCP recovery follow-up, 2026-10-06

The live checkout reports HEAD `973dea61c8c5059b1dd188f01c205a85562f5cd0`. Parent confirmed its Event004 commit `c45a0f4988574390182f3683eb1d4b8e249e8bf4` is an ancestor and that other owners have published later commits. This audit remains bound to the verified Event004 source hashes in the table above, not a changed checkout.

Current `hoi4.probability_inspect` succeeded separately for the complete attacker pool `[chaosx.nr4.2.a, chaosx.nr4.2.b]` and defender pool `[chaosx.nr4.3.a, chaosx.nr4.3.b]`. Each inspection found exactly two active options, `poolComplete = true`, `analysisSupport = exact`, no eligibility conditions, no required inputs, and zero unresolved candidates. Both bind to event source hash `7a22c703c0bdba95727d05a201be4251c3964386fa52606b45404fed5540f1ba`. The inspector revision was `0a15314ebb757b4827eed0a9138e91902e505324aa6b5e1b2ab484c84d73e10d`, and the adapter is `event_option_ai_chance` version `hoi4-1.19.2.v1` for verified game version Operation Postern 1.19.2.0 (d245).

The attacker-pool inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53b1a5d42bb63d003b15db41aa33232947d90c9ddde2ef7cdffa4ce6d3aa897c/df54f9030c2c3aa628c9c027d24cb9b5787f85574d0ac73d49fa451446db2009/probability-inspect-7a22c703c0bd.json`. The defender-pool inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cac0a05f5cb66e8c6858c06d428013644186377f7121d0a7ea39d19c26aba1f1/962a6b05aa92c85ecd922b2c54fdadb320964c2a7062035121c7f4b776ddf176/probability-inspect-7a22c703c0bd.json`.

The shared scenario set remained `004_random_war_baseline_20261005`: `calm_baseline_1936` at 1936.1.1, `tier2_special_available` at 1939.1.1, `tier3_special_unavailable` at 1940.1.1, and `final_declaration_count` at 1945.1.1. All four declarations retain actor GER and empty state. These are the documented event-option contexts. They do not encode stage variables, resource balances, special-country availability, or any target-country pool state.

Separate current-source `probability_evaluate` calls succeeded for both fixed pools across all four scenarios. They share scenario hash `9bb06be6872fbdefed26af55a526b72ae6540228765674caf61c415a9efde5e2`, source hash `7a22c703c0bdba95727d05a201be4251c3964386fa52606b45404fed5540f1ba`, source revision `98594bcf0fe170e68feac98f9abf8941bdfc69d70c27eeb4a81f5b76f7234088`, and adapter version `hoi4-1.19.2.v1`. Both analyses report complete pools, eight candidate instances across four scenarios, eight eligible, none excluded, zero diagnostics, and zero unresolved.

| Event option pool | Candidate | Raw score | Exact conditional share | Rank in all four scenarios |
|---|---|---:|---:|---:|
| Attacker `chaosx.nr4.2` | `chaosx.nr4.2.a` | 80 | 4/5 = 0.8 | 1 |
| Attacker `chaosx.nr4.2` | `chaosx.nr4.2.b` | 20 | 1/5 = 0.2 | 2 |
| Defender `chaosx.nr4.3` | `chaosx.nr4.3.a` | 70 | 7/10 = 0.7 | 1 |
| Defender `chaosx.nr4.3` | `chaosx.nr4.3.b` | 30 | 3/10 = 0.3 | 2 |

Each result is exact for the local event-option choice after the event fires and has an available complete option pool. The engine event-option adapter uses proportional categorical selection with a d100 path, and these outcomes exceed its sub-one-percent resolution limit. The result does not estimate event firing frequency. The four named scenarios do not change these static scores, so no rank reversal occurred among them.

In every analyzed scenario both options remain eligible with positive shares. No option is impossible, blocked, excluded, or starved, and neither pool has a 100% dominant outcome. The result describes one choice per event presentation, not popup frequency or repeated War Contagion outcomes. Current delivery aggregation limits responses per participant per invocation, while repeated cluster selection and target-country repetition remain unresolved under the failed direct-random inspection.

The source has no event-option trigger or resource eligibility gate. The political power, command power, stability, and war-support values are option effects applied after selection. The numeric evaluation therefore conditions on the event being presented and does not gate an option on whether the actor can pay its stated effect. The effects do not change the evaluated eligibility, ranking, or conditional shares.

The attacker evaluation ID is `probability-26a7600c072928d38ff45e45`, with JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70416d46ab3d2115bf85b0a6bc9e6210a43486b72bdab02e775e4938353f37c5/746d13644f20800c58f5efebca327b228d2e8e372ce4e359c16f3593cd9509e8/probability-26a7600c072928d38ff45e45.json`, ranking image `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eaf2629b08b37c878eb455297b054cd3b7531aeb170e56ac59de0c18d0faa38/1fc5c9d8877f8f2fd10f2ce2c49f911e8535e37e11263dafb4739b48cd1022ca/probability-probability-26a7600c072928d38ff45e45-ranking.png`, and matrix image `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b123e95ad76f55d6e94f0d04c6c873958b0617666511e010ae07e6b0e7c46ca/42c57adf01483f5f30a9875065f382262f259dbc380724921e3538dccf7d0ad6/probability-probability-26a7600c072928d38ff45e45-matrix.png`.

The defender evaluation ID is `probability-a9775cecdb4a46a4ac23547d`, with JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc88d62c5221df71113327bd88ade32754d2cd841755dcd47c95e47efb0dca10/6fa7988387779b4f42f7b52cc1255fb67d2ab34f8e3bcf55ea8f267caf8db231/probability-a9775cecdb4a46a4ac23547d.json`, ranking image `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba131ec23c8e6c71f42864daacff23a7231fdaf5e289a9b853097f14634b5590/f0c232376d5e001aa5a5bae74172acdc3a42ecc7e3cac4a2c95283802ed6f9d3/probability-probability-a9775cecdb4a46a4ac23547d-ranking.png`, and matrix image `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e1f50cbd4b4b0f50dee1fe0d89defb09ee66bee71858f1800b334799985ed07/e21396cd741d17f1846331beb57e0a73b9f87baabf4d7eab100581f33e8f7da3/probability-probability-a9775cecdb4a46a4ac23547d-matrix.png`.

The JSON artifacts were read as JSON text. The returned ranges were complete at 20,127 and 20,139 bytes, matching their declared sizes, with no continuation URI.

The before/after event-option comparisons used the preserved baseline event path, current event path, same candidate pools, and identical scenario set, but both timed out after 600 seconds. No comparison ID, source delta, or comparison artifact was returned. The current conditional shares are MCP-proven above, and the baseline source snapshot retains the same raw scores, but there is no MCP-proven numeric before/after delta.

The fresh `direct_random` inspection on current `common/scripted_effects/004_random_war_effects.txt` timed out after 600 seconds. Per parent instruction, this route was not retried and no direct-random evaluation, sweep, or comparison was submitted. Source documentation and constants show integer ranges `[1, 101)` for the special roll and `[7, 9)` for the final declaration target count, but direct-random probability and actual candidate-country coverage remain unresolved. The four scenario labels do not provide special-target country identities or a complete eligible pool.

Separate `probability_render` requests for the two completed event-option analysis IDs timed out after 600 seconds. The evaluation calls themselves returned ranking, matrix, waterfall, and unresolved image artifacts, so those evaluation-provided resources remain available for review. No option-weight change or balance target is recommended by this audit.

No event-option sweep was run because these complete pools have no parameter or external-factor path to vary and their rankings are invariant across the four scenarios. The direct-random threshold sweep was blocked by its inspection timeout and incomplete target-country pools. No simulation or sequence analysis was run because no uncertain inputs or complete custom-pool lifecycle manifest were declared.
