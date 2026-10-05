# Event 004 Probability Audit Handoff

Status: Read-only baseline review is complete. The event-option scores are recorded from source, while normalized option probabilities and random-draw distributions remain unresolved because the required MCP evaluation and comparison calls timed out.

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

## MCP analyses and results

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

- The baseline direct-random probability inspection timed out after 600 seconds.
- Both event-option evaluations and both event-option comparisons timed out after 600 seconds.
- The event-options renderer timed out after 600 seconds, so no comparison or matrix view is available.
- The corrected Event004 structural trace timed out after 600 seconds. The direct-random comparison timed out after 600 seconds and predates the latest effects hash.
- The direct-random pool has no complete scenario-specific country inventory or state-transition manifest, so target identity, special-pool frequency, repetition, and final fired declaration-count behavior remain unresolved.

No balance target was selected and no gameplay change was applied by this auditor.

Parent integration addendum: the owner subsequently marked the shared Settings failure receipt at the two manual failure sends, preventing duplicate owner and generic feedback.
The resulting current effects SHA-256 is `624c579e7ed14b9c395b202ba06b5423b9430c7c6311b38e9f16ff6fe006b860`.
This change affects feedback idempotence, with no chance or score change.
The recorded timed-out comparison does not validate this current revision.
