# Event 012 Africa full-action AI dispatcher handoff

## Scope

This handoff covers the autonomous host controller for the previously un-dispatched Event 012 action ranges 1–76 and 93–102. Actions 77–92 remain on the existing late dispatcher and shared mission path.

## Files changed

- `common/scripted_effects/012_africa_ai_profile_effects.txt`
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt`
- `common/script_constants/012_africa_ai_constants.txt`
- `common/decisions/012_africa_decisions.txt`

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `africa_ai_action_controller_is_active` | host trigger | AI host, event-active flag, capacity, proof state | controller availability | none | `africa_charter_council_category` visibility/availability |
| `africa_ai_prepare_early_action_family_weights` | host effect | refreshed registry family weights and bounded-candidate triggers | twelve temporary family weights and total | zeroes unavailable families; recovery phase suppresses non-101 families | `africa_ai_run_profiled_action_cycle` |
| `africa_ai_pick_action_in_selected_family` | host effect | selected family | one temporary action ID | no persistent action stores | three tournament draws in `africa_ai_choose_and_dispatch_early_action` |
| `africa_ai_apply_early_action_priority` | host effect | temporary action ID and scored action weight | adjusted temporary action weight | clamps the sampled score | sampled tournament |
| `africa_ai_consider_sampled_early_action` | host effect | approved sampled action and weight | temporary best action ID/family/weight | no persistent action stores | sampled tournament |
| `africa_ai_prepare_action_state_cursor` | host effect | action profile, selected country target, target mode | bounded selected state candidate/target arrays | clears stale state cursor, marks only controlled African states | shared late helper and early target commit |
| `africa_ai_commit_selected_action_target` | host effect | regular `africa_action_target` | selected-country cursor and state candidates | reuses existing selected arrays/flags; invokes shared AI validation/launch helper | all bounded target arrays |
| `africa_ai_dispatch_selected_early_action_target` | host effect | selected action ID/profile | regular action target and shared action attempt | reads only capped selected/relationship/world/scramble arrays; increments no-candidate record when empty | sampled winner |
| `africa_ai_choose_and_dispatch_early_action` | host effect | family weights and profile registry | one sampled-tournament winner | three bounded samples and shared target dispatch | generic cycle |
| `africa_ai_run_profiled_action_cycle` | host effect | generic controller trigger | early or existing late dispatch | refreshes bounded rosters only on controller decision cadence | `africa_charter_council_category` completion effect |

## Action coverage

The picker contains one exact branch for every action ID 1–76 and 93–102. A source audit against `africa_action` constants reports 86 required IDs, 86 picker references, and no missing IDs. Existing late branches continue to cover 77–92, giving structural 102/102 dispatch reachability.

Family routing is:

- protection 1–10
- accession 11–20
- regional congress 21–30
- integration 31–40
- economy 41–50
- diaspora 51–58
- rival bloc 59–66
- high chaos 67–76
- constitutional crisis 93–99
- post-unification 100
- host opening recovery 101
- regional restorations 102

## Candidate construction and gates

Country, state, and region targets are selected only from the existing bounded rosters. The dispatcher checks `africa_selected_targets`, `africa_relationship_countries`, `africa_selected_country_targets`, and then the already-maintained world/scramble actor arrays. Host and global profiles use the current host event target. No action branch creates a target, performs a whole-world scan, changes ownership/core/tag state, or treats opinion as integration authority.

`africa_ai_selected_target_is_candidate_for_action` adds narrow prefilters for neighbour sanctuary, voluntary diaspora consent, diaspora emergency, charter confidence, integration relationship state, high-chaos actors/sites, disease crisis/research, rival/leaving/war gates, constitutional marker targets, restoration membership, and Action 101 same-overlay recovery markers. `africa_validate_action_specific_requirements` remains the authoritative final semantic gate and shared `africa_begin_quoted_action_against_target` owns payment, records, missions, full/partial/failure outcomes, and cleanup.

State and region actions rebuild the existing selected-state cursor from the chosen country target. State actions cap at one state; region actions cap at `africa_action_capacity.maximum_region_state_targets`. Project-active, non-African, or uncontrolled states are excluded. Action 91 still uses its dedicated capital-region cursor.

## Scoring and tuning

The controller first weights families with the existing 64-profile registry and context MTTH factors. Twelve shared family priorities and seven coarse action priorities live in `africa_ai_controller`; no 86-action persistent weight table is introduced. The selected family then draws three action IDs. Every draw runs `africa_ai_evaluate_requested_action`, applies the shared risk/approval score and action priority, and retains the highest approved temporary weight. The winner is evaluated again against the actual bounded target before launch, so profile/context and risk ceilings can reject a draw or change the winner rather than merely influencing a cosmetic log.

## Proof and recovery lifecycle

The generic controller is disabled while `africa_first_proof_active` is live, leaving the existing playbook selector and protection-before-integration proof semantics authoritative. A failed proof is admitted to the controller solely for Action 101 recovery; all other early family weights are zeroed until the recovery contract closes. Recovery still requires the existing host validity, same-overlay target, durable route, and no-active-contract predicates.

## Validation evidence

- Brace-depth audit on all four changed script files returned depth zero with no early close.
- A raw operator audit found no unsupported `<=` or `>=` tokens in changed files.
- Action constant comparison found all 86 required early/route IDs in the picker and retained late 77–92 coverage in the same effect file.
- Controller, helper, and constant references were searched for duplicate/undefined names; all new `africa_ai_controller` references resolve to the shared constant block.
- Read-only Event MCP inspection was run against the `chaosx.nr12` namespace with a bounded depth/node request. The partial scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aee5c91b970e41204fbcae396185d967acbbaba8b69456c40ffdf16433d48a2f/a7e6dbeb3d5650d07e2d8563884743983d4537a1b06684f225c331a259b87b82/event-scan-6205a23277ea.json`; it confirms the read-only graph surface but does not prove runtime weighted selection.
- Read-only probability inspection of `common/decisions/012_africa_decisions.txt` returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/862936035026e595386792078031e559938b5d029744d192117a42f6228b8c24/2dfa21c0210a5ea1581390bda9341e1f4a8298576ec3b4dd00933562625a2258/probability-inspect-f015e10c377e.json`. The decision adapter found 140 candidate decisions with no unresolved inputs, but the whole-file pool is incomplete for the Event 012 dispatcher and is not a runtime action-selection proof.

## Skipped validation and limitations

No live HOI4 save, MCP weighted sweep, or runtime mission launch was available in this subtask, so target-array population, scope-root behavior, and random-list execution remain runtime risks for parent review. The Event MCP scan was partial and reported unresolved analysis outside the bounded Event 012 surface; it is not a substitute for a scenario audit. The opening Action 5 colonial-holder path intentionally does not add a broad discovery scan; it can launch only against an already registered bounded target and otherwise records no candidate. Action-specific validation remains a retry boundary rather than a fallback target mechanism.

## Follow-up

The parent should run the Event 012 AI weighted/scenario audit across opening, failed-proof recovery, regional consent/refusal, integration, diaspora consent, high-chaos Evolution III, constitutional crises, post-unification review, and late 77–92/world-order states. Any scope or target-array issue should be fixed in this dispatcher before claiming full runtime completion.
