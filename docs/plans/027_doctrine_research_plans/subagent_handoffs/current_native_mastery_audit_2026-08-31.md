# Event 027 native mastery audit

Date: 2026-08-31.

Scope: read-only review of the Event 027 mastery effects, exact mastery effects, scripted triggers, event confirmation flow, relevant specifications, offline Paradox wiki pages, and installed vanilla documentation.

Disposition: the normal source path is structurally fail-closed and uses the documented native effect, but acceptance is not complete because engine-level mastery and banked-progress behavior remain unproven. One recovery-path defect is concrete. Special Forces is safe only as a disclosed conditional limitation, not proven as fully supported.

No gameplay files were edited.

## Evidence

### Native `add_mastery` semantics

Vanilla documents `add_mastery` as a country effect that adds mastery points and accepts optional `folder`, `grand_doctrine`, `sub_doctrine`, `track`, and 0-indexed `index` filters (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:1477-1502`). The Event 027 exact adapters supply the folder, subdoctrine, track, and index on every exact-step family. Ordinary evidence is `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:17139-17161`. Special Forces evidence is `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:19683-19705`.

The current point increment is one and the loop has a bounded guard (`common\script_constants\027_doctrine_research_constants.txt:35-39`). This is source-consistent with one-point stepping, but the local engine has not proved the resulting level transition.

### Exactly one Event 027 mastery level

Each exact step reads `has_mastery_level`, adds one native mastery point, reads the level again, and marks success only when the observed level equals the expected level (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:17141-17159` and `:19685-19703` in the same file). Empty-track selection performs native `set_sub_doctrine`, reads the post-assignment level, and then requests one step only when the branch is not complete (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:19707-19724` and `:21407-21422` in the same file).

This is a source-level pass, not runtime proof. Vanilla documents `has_mastery_level` as a subdoctrine-wide reward-level check without track or index filters (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:4181-4196`). The readback therefore cannot independently prove track identity or fractional residual points. An overshoot leaves `transaction_success` unset and is quarantined, but the native point mutation itself is not rollback-capable.

One tuning hazard is that `mastery_point_increment` is also added to the expected level (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:21023-21031` and `:20905-20914`). It is currently one, but changing that point constant would request more than one Event 027 level per receipt and violate the one-level contract.

### Banked mastery

The empty-track adapters do not reset, subtract, or cap native mastery. They assign the selected subdoctrine, read the resulting level, and either add one event step or mark native completion (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:19707-19724`, `:21407-21422`, and `:21621-21641`). The caller records native completion as `native_adoption`, clears the pending flag, and does not invoke the choice-consuming finalizer (`common\scripted_effects\027_doctrine_research_effects.txt:3240-3249`). Event `chaosx.nr27.13` returns to the valid pool without an Event 027 mastery choice decrement (`events\027_doctrine_research.txt:4880-4900`).

This matches the intended sequence in `docs\specs\027_doctrine_research_specs\027_doctrine_research_spec_part_2_choice_flow.md:140-149` and `:368-377` in the same file, but partial-bank, multi-level-bank, and native-completion runtime cases remain unverified.

### Choice consumption

The normal finalizer records the post-level, decrements exactly one remaining choice, then marks the receipt `choice_consumed` (`common\scripted_effects\027_doctrine_research_effects.txt:3037-3048`). The fresh confirmation path calls it only when `transaction_success > 0` (`common\scripted_effects\027_doctrine_research_effects.txt:3219-3239`). Invalid, ambiguous, and native-adoption paths do not call it.

Concrete recovery defect: an `effect_applied` receipt restores its stored post-level and only re-reads mastery when that stored value is zero (`common\scripted_effects\027_doctrine_research_effects.txt:3164-3173`). It then finalizes whenever the stored or reread post-level is positive (`common\scripted_effects\027_doctrine_research_effects.txt:3176-3188`). There is no comparison against the receipt pre-level plus exactly one, no stable target identity check, and no current reread when the stored post-level is already positive. A save or interruption followed by external mastery can therefore consume the choice without re-proving the exact Event 027 step required by `docs\specs\027_doctrine_research_specs\027_doctrine_research_acceptance_criteria.md:56-63` and `docs\specs\027_doctrine_research_specs\027_doctrine_research_spec_part_2_choice_flow.md:394`.

## Special Forces dual-track limitation

Vanilla defines distinct `special_forces_first` and `special_forces_second` tracks, with the second gated by `can_unlock_second_track_of_sf_doctrine` (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\tracks\special_forces_tracks.txt:1-32`). The shared Special Forces subdoctrines can be assigned to either track, for example `mountaineers_1` and `mountaineers_2` (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\subdoctrines\special_forces\special_forces_subdoctrines.txt:1-17` and `:92-108` in the same file). Since the documented mastery readback is subdoctrine-wide, the Event 027 trigger deliberately allows active mastery only when the selected track is occupied and the other Special Forces track is empty (`common\scripted_triggers\027_doctrine_research_triggers.txt:627-630` and `:2047-2056`). Both occupied tracks therefore fail closed, while ordinary domains remain selectable.

The current registry nevertheless declares Special Forces enabled and one-step capable (`common\scripted_effects\027_doctrine_research_effects.txt:65-74`), and the native adapter gate includes the Special Forces domain (`common\scripted_triggers\027_doctrine_research_triggers.txt:3875-3890`). The safety behavior is permitted by the specs' fail-closed rules, but the binary acceptance wording requires supported Special Forces content to be “fully adapted or explicitly absent” (`docs\specs\027_doctrine_research_specs\027_doctrine_research_acceptance_criteria.md:68-79`). The registry matrix likewise says Special Forces is conditional on a verified compatible graph and must otherwise be omitted (`docs\specs\027_doctrine_research_specs\027_doctrine_research_doctrine_registry_matrix.md:88-103`). Therefore the no-action behavior is safe, but partial state-level exposure is not explicitly accepted as completion. Record Special Forces as unresolved unless the owner explicitly defines this state-level absence as “explicitly absent under the current ruleset.”

## Evidence gaps and follow-up

- No agent-launched HOI4 runtime test is permitted, so native one-point transitions, fractional residual preservation, and exact track-qualified Special Forces readback remain unproven.
- The current Event MCP result is partial, with direct artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7faef9cc972786b89c5360ad2750fa208e701481bd6bdf7ea51336fa8824bafe/fc61f03b86e179f8d3d9b4ea09839a43d961099417e7df72d4757508953b1657/event-lint-cfdc65be2a28.json`; it reports `EVENT_INSPECTED_PARTIAL`, inline files are truncated, and validation is false because the workspace-wide helper/lifecycle pass was deferred.
- The current Special Forces technology inspection is also partial, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32b9350116d6fe881a9e878a9125d3b9d1d16e673e875dc975901c9e59e03d6d/0ac01bdc5b593873310681806b241b293e68264ce0de97d46d649e37f37f78db/technology-scan-d6dfe1c52db0.json`; it found no legacy doctrine nodes and validation is false, so it is not accepted as doctrine graph proof.
- Required runtime scenarios are active low, middle, and final levels, empty track with no bank, partial bank, bank completing the branch, both Special Forces tracks occupied, one occupied track, and save or interruption recovery after native mutation.
- Weighted AI and probability surfaces were outside this bounded native mastery audit, so no probability or balance disposition is made here.

An independent read-only completion audit was run with `fork_context=false`; it made no edits and reached the same source-pass, runtime-gap disposition.
