# Event016 native Prototype core implementation handoff

Date: 2026-10-03.
Role: chaosx_scripted_system_architect.
Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
Disposition: bounded new-file helper definitions implemented, parent integration and domain acceptance remain separate.
Acceptance basis: the explicit parent delegation to implement these new files under the accepted native Prototype ownership amendment, plus the parent's follow-up requests for six literal UI triggers and the durable fresh Cloning bridge proof.
The amendment's accepted and queued selection/provenance design remains the source of truth.
Native start/cancel synchronization and cancellation/reselection proof remain unresolved and are not waived.

The parent's bounded integration correction accepts own-selected exact completed sources through the literal selection gate, adds the existing family empty-paid-receipt predicate to release, and reuses those receipt predicates in private eligibility.
This correction modified only the new triggers file, matching API document, and this handoff.
The new constants and effects source remain byte-identical to their earlier delivery, with stable modes/results and existing private output behavior preserved.
The parent automatic driver reserves auto-adoption for unselected historical sources and uses explicit exact adoption for a selected source.

## Delivered files and ownership

Only these five new paths were written by this worker:

- common\script_constants\016_mengele_native_prototype_constants.txt
- common\scripted_triggers\016_mengele_native_prototype_triggers.txt
- common\scripted_effects\016_mengele_native_prototype_effects.txt
- common\scripted_effects\016_mengele_native_prototype_effects.md
- docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_native_prototype_core_implementation_2026-10-03.md

The matching effects document covers all 33 new effect/trigger declarations, inputs, outputs, defaults, scopes, side effects, cleanup, and parent call sites.
Three enum categories retain exactly the supplied stable source, mode, and result codes.
No costs, timers, thresholds, or AI tuning constants were added.
Internal helper call sites were implemented in the new effects file.
No existing file or external call site was edited by this worker.
The parent concurrently added the new Cloning receipt proof to its existing bridge, which was observed during a read-only source read.
That parent edit is not attributed to this worker and was not given an integrated acceptance claim.

No model, texture, animation, entity, public meter, GUI, country, focus, native project, technology ID, decision, AI weight, random pool, global/periodic hook, index mutation, or commit was produced.
Approved Portal Raider, alien, and autonomous robot models were not edited.
No game launch or live-game test was performed.
No fallback or implementation simplification was introduced within the requested core.
The larger Event016 lifecycle remains incomplete.

## Exact source behavior matrix

| Source | Private family/index | Selection prerequisite for incomplete native source | Output wrapper | Durable accepted receipt |
| --- | --- | --- | --- | --- |
| Cloning, code 1 | Cloning ID 8 / slot 7 | Existing private custom Cloning availability gate | brilliant_scientist_mengele_native_output_cloning | source 1 with fresh_output 1 or adopted_completed 2 |
| Flying Bomb, code 2 | Rocketry ID 4 / slot 3 | experimental_rockets | brilliant_scientist_mengele_native_output_rocketry_flying_bomb | source 2 with fresh_output 1 or adopted_completed 2 |
| Jet Engine, code 3 | Rocketry ID 4 / slot 3 | With By Blood Alone, engines_2 and improved_small_airframe or improved_medium_airframe. Otherwise fighter2 or tactical_bomber2. | brilliant_scientist_mengele_native_output_rocketry_air_jet_engine | source 3 with fresh_output 1 or adopted_completed 2 |

All selection/settlement paths also require the original strict provider, Theory, incomplete private Prototype, and empty matching family paid receipt.
Completed-source selection uses exact completed adoption and does not mint a fresh pending flag.
Native availability/payment/clock/rewards remain authoritative in their native object.

| Scenario | Result | Ownership and provenance behavior |
| --- | --- | --- |
| Unsupported/none/fractional source, including contaminated private selectors | blocked 5 | No receipt initialization, index preparation, or persistent change. Selectors clear. |
| Eligible incomplete exact source with no family selection | selected 1 | One static selection set, matching retired intent cleared. No payment or timer. |
| Same incomplete source already selected | blocked 5 | Literal selection availability is false. Existing ownership remains. |
| Same selected exact source completed after an ineligible earlier output | adopted_settled 3 if private gates pass | Literal UI availability re-exposes the exact source, the selection core takes exact completed adoption, and matching selection is consumed with adopted provenance. |
| Opposite Rocketry source selected | blocked 5 | Cannot select or adopt the other source. Existing selected source remains. |
| Literal matching output with current selection, before completed query becomes true | fresh_settled 2 | Exact source/fresh_output recorded after changed Prototype. Matching selection consumed. |
| Generic fresh request without wrapper witness | blocked 5 | A selected or observed flag alone cannot establish fresh output. |
| Literal output with missing provider, Theory, selection, or with active paid family receipt | blocked 5 | Exact observed flag still records output. No private Prototype. Held selection and paid receipt survive. |
| Opposite Rocketry output during another source's selection | blocked 5 | Output observed and its source retired. Selected alternative survives. |
| Repeated matching output after successful private Prototype | blocked 5 | Observation remains. No repeated private output or history replacement. |
| Explicit exact completed source | adopted_settled 3 | Exact source/adopted_completed recorded without native output replay or invented observation. |
| Explicit retired completed source | adopted_settled 3 if private gates pass | Permitted explicitly. Historical retired flag remains. |
| Matching selection plus exact completed explicit adoption | adopted_settled 3 | Matching selection consumed with adopted mode. Opposite Rocketry selection still blocks. |
| Legacy Cloning completed alone | blocked 5 | sp_mengele_cloning/shared latch is never accepted as the custom source. |
| Automatic adoption with retired ownership | Ineligible | No Cloning retirement allowed. Neither Rocketry source may be retired. No silent alternative after release/rejection. |
| Automatic Rocketry adoption with both completed alternatives | Ineligible | Requires explicit exact-source acceptance. |
| Exact selected project currently being researched | blocked 5 on release | Selection remains. Query is a guard, not a cancellation callback. |
| Exact selected project no longer being researched, empty family paid receipt | released 4 | Matching selection cleared and retired. Native progress/rewards and observation/history preserved. Provider validity and incomplete private Prototype are not required. |
| Exact selected project with any funded family stage | blocked 5 on release | Matching selection and funded receipt survive, including when the stage appeared after UI availability evaluation. |
| Explicit incomplete reselection after release | selected 1 if gates pass | Matching retired intent cleared. This establishes no immutable callback-generation isolation. |
| Provider/terminal cleanup in original owner scope | released 4 if any selection, otherwise none 0 | All held selections cleared/retired. Native research, observed facts, paid receipts, and source/mode history preserved. |
| Delayed output after cleanup without a new matching selection | blocked 5 | Exact output observation preserved without a private receipt. |
| Cloning plus one Rocketry selection | Independent | Settlement consumes only the matching source and preserves other-family receipts/history. |
| Provenance arrays short or differently sized | Append-only schema extension | Each array independently reaches at least fifteen entries. Existing values and oversized tails survive. |

## Parent API and migration

The seven requested generic core effects and three literal wrappers are defined and documented.
Every source-taking effect maps its own exact family/Prototype stage and resets its private selectors on exit.
The request result is temporary mengele_event016_native_prototype_result and survives the cleanup epilogue.
Other transaction results still belong to their enclosing transaction.

The read-only literal selection/release wrappers are:

- brilliant_scientist_mengele_can_select_native_cloning
- brilliant_scientist_mengele_can_select_native_flying_bomb
- brilliant_scientist_mengele_can_select_native_jet_engine
- brilliant_scientist_mengele_can_release_native_cloning
- brilliant_scientist_mengele_can_release_native_flying_bomb
- brilliant_scientist_mengele_can_release_native_jet_engine

They require no pre-existing temporary selector and write neither temporary nor persistent state.
Literal private gates mirror the original selector-based predecessor and reuse the existing Cloning/Rocketry decision receipt predicates for empty-family-receipt behavior.
Literal selection gates allow an own selected flag when that exact project is completed, while opposite Rocketry selection still blocks.
Literal release gates reuse the same family receipt predicate and add neither provider validity nor an incomplete private Prototype requirement.
The effect core rechecks the original gates after receipt initialization.

brilliant_scientist_mengele_native_cloning_fresh_receipt_is_present validates both array sizes against the existing Cloning family ID 8 before reading slot 7.
It accepts exactly source.cloning plus mode.fresh_output, with no temporary selector or completion-bit dependency.
Its static slot 7 is the existing Cloning family ID 8 minus one, matching the current family receipt predicate.
No reusable zero-based index constant was found, and documented unscoped temporary arithmetic would add scratch writes to this pure proof.
The retained literal is an explicit enumeration mapping rather than gameplay tuning or an undocumented dynamic-index substitute.
The parent bridge retains its existing strict provider/Theory/private Prototype gates and uses OR exact completed / this proven fresh receipt only in the Cloning operational grant.
The parent will call that idempotent grant after fresh_settled, before the original cbrn_complete_cloning_project call.
No operational technology grant is implemented by this worker.

brilliant_scientist_mengele_can_auto_adopt_exact_completed_native_prototype is available for parent-owned historical scanning.
It requires a named exact source, literal private eligibility and exact completion.
It rejects conflicting selections and retired source dispositions.
An exact matching selection may reconcile through its completed query as adopted_completed, with no reconstructed fresh callback.
For Rocketry, it rejects either retired alternative and both-completed ambiguity.
Explicit adoption may accept retired completed history or an explicitly chosen completed Rocketry source.
No historical scanner, polling hook, or AI chooser was implemented here.

Parent integration sequence:

1. Wire the three exact existing native country-output hooks once, preserving all original native/CBRN/legacy consumers once per output.
2. Exclude Cloning and Rocketry from unrelated aggregate completion scans and the old generic fresh recorder, so those paths cannot bypass exact ownership.
3. Wire the three instant literal source choices and mutually exclusive release controls, including parent-owned visible gates, localisation, icons, tooltips, and AI.
4. Wire explicit/unambiguous historical adoption and preserve the enclosing Theory callback's selectors/results through the existing outer-transaction restoration pattern.
5. Complete the Cloning bridge and immediate operational grant wiring described above.
6. Add selection cleanup to existing provider/terminal boundaries in the original owner scope.
7. Run integrated source/MCP, CXT, decision/localisation, and weighted-action evidence before the parent completion claim.

## Constants, event targets, and cleanup

The constants are stable receipt metadata, not gameplay tuning.
The existing fifteen-family count and ID-minus-one indexing remain authoritative.
No tuning table or balance target is proposed by this core.

No event target is created, persisted, or globally cleared.
No native numeric pointer is stored.
The two country provenance arrays retain accepted source/mode history.
Boolean static flags own selected, observed, and retired state.
Release clears only matching ownership after the exact research guard.
Provider/terminal cleanup retires all held selections while preserving durable facts.
The selector epilogue clears source/witness/mode, private family/stage/index/authorization, and the existing later-stage source selector through the current cleanup helper.
It never overwrites the dedicated request result.

## Meaningful validation

568 read-only source-contract cases passed using an in-memory Clausewitz parser/interpreter of the delivered files plus the current existing private stage receipt/predecessor/output core and family decision receipt predicates.
The exact parent provider validity and country completion/research/technology/DLC values were explicit scenario inputs.
The existing availability reconciliation and engine dynamic modifier behavior were explicit stubs.
Actual private Prototype flag/output logic and receipt initialization were executed from their existing source.
The transient driver ran through PowerShell stdin into python -X utf8 and created no validation file outside the five-path allowance.
Its code and result are retained in the task tool transcript.

The scenarios exercised invalid source rejection before array access, stale selector replacement, read-only literal UI independence, strict predecessor/paid receipt parity, every native technology prerequisite branch, fresh output before completed-bit visibility, selection/witness/provider/Theory/paid receipt rejection, wrong Rocketry output, adopted history and retirement, matching-selection historical reconciliation, ambiguous historical sources, release guard and reselection, original-owner cleanup followed by delayed output, cross-family receipt/history preservation, and independent append-only schema extension.
The durable Cloning proof received 256 source/mode/array-size cases with strict out-of-range array-read detection.
95 additional correction cases exercised the parent's concrete selected-completed adoption path, preserved opposite Rocketry exclusion, paid release guards across provider/private Prototype states, an intervening funded receipt after UI evaluation, pre-initialization release, and parity with parent selection/release visible gates.
All 33 delivered helper names are covered in the matching API document.

An initial broad closure check encountered the reused output core's post-application availability completion queries.
The relevant authorization closure was then checked separately from that existing availability publication.
No completed query authorizes fresh settlement in these new files.
No availability side effect was removed or rewritten.

This is source-model evidence, not engine execution or callback-order acceptance.
Decision AI weights and actual native payment/resource/timer behavior were not analyzed because those surfaces remain parent-owned and no weight/payment patch was made.
No probability claim is made.

## Simplifications, omissions, and blockers

No fallback or simplification was used within the authorized core.
The following work is explicitly outside this worker's implemented scope or unresolved:

- Native effect-bearing start/cancel synchronization remains unresolved, without a proven engine seam.
- Selection persistence through native cancellation, native cancellation cleanup, and same-project release/reselection delayed-generation isolation remain unresolved.
- A mutable temporary witness and a cleared retired flag do not prove immutable callback-generation ownership.
- Parent external hooks, historical reconciliation, decision/UI/localisation/AI integration, operational grant wiring, provider cleanup wiring, and CXT cases require parent review and acceptance.
- The native output boundary can also be emitted by scripted completion, so fresh_output does not independently prove native payment.
- No native project field or learned technology is changed by this worker.
- A pre-existing short/corrupt receipt schema and contradictory durable history require parent review rather than fabricated repair.
- Shared workspace changes made concurrently by other agents are not attributed to this worker.

The exact MCP evidence gap is no returned result from the read-only calls made in this session.
The coding-agent tool list exposed hoi4.event_inspect and the reference_context/search/read/source_lookup routes, which differs from the parent's report of absent desktop tools and does not prove service health.
The submitted event request used mode trace, selector eventId chaosx.nr016.1, depth 1, nodes/edges 8, and expandHelpers false.
The submitted event reference_context request used limit 4 for country helpers, arrays, constants, and native completed/research queries.
The bounded orchestration remained running without results and was explicitly terminated.
No returned source revision, artifact URI, coverage, diagnostic, or engine result was available to review.
Reference_search/read and source_lookup were not subsequently called, and no live reference read is claimed.
The required local references were read directly instead, with their bounded spans and hashes below.
No service outage or universal callback absence is asserted from this request gap.
A focused trace would not establish helper/lifecycle coverage even if it returned.
The parent owns route retry, read-only domain inspection/comparison, and integrated evidence.
No HOI4 script_validate route was exposed in the discovered coding-agent tool list.

Skills used: chaos-redux-events, chaos-redux-subagents, and relevant read-only UI trigger guidance in chaos-redux-decisions-missions.
No skill was created or updated under the new-file-only scope.
No commit was made, as explicitly forbidden by the parent.

## Delivered artifact revisions

The handoff does not hash itself.
The following hashes identify the delivered core and matching API document at validation.

| Path | Read span / artifact | SHA-256 |
| --- | --- | --- |
| `common\script_constants\016_mengele_native_prototype_constants.txt` | complete delivered file | `175e6281d9c6c4fb86f5e0ef5d8a677965c11e28bfa4a3ad10ceb7b3238116c4` |
| `common\scripted_triggers\016_mengele_native_prototype_triggers.txt` | complete delivered file | `6316a57859bdbf65914d8d11ec935d908d5a3e7b43b7c7a7a350a66441c19982` |
| `common\scripted_effects\016_mengele_native_prototype_effects.txt` | complete delivered file | `f3ebe41d73c86160313119d5fef8a135c670a34569da715d718194c4bacc13d9` |
| `common\scripted_effects\016_mengele_native_prototype_effects.md` | complete delivered file | `3009526c71bc78d2090e8bd324a310299dfc00eef8d542a36eda247d7363a92d` |

## Final validation source revisions

The final 568-case run checked the delivered core/document hashes above and the existing stage/bridge/decision source inputs below before and after execution.
Those hashes were unchanged during that run.
The parent had concurrently changed the existing stage effects and bridge triggers after the earlier bounded reads, so the final validation used their updated source rather than claiming the earlier source revisions were current.
The bounded reference ledger below retains the earlier read-time citations and hashes.
The complete source-contract driver parsed the existing stage effect/trigger and bridge trigger files in memory for the final scenarios.
It also parsed the existing Cloning/conventional decision receipt definitions and parent native selection presentation triggers for the correction scenarios.

| Existing validation input | SHA-256 during the final stable run |
| --- | --- |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `adefae1a96a2d141434ba74e60cb5c6f56ae0951daf174e962eba419ff7c4881` |
| `common\scripted_triggers\016_mengele_project_stage_triggers.txt` | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common\scripted_triggers\016_mengele_project_bridge_triggers.txt` | `f1489f0c8137a47d05b2c0ecc369b2d638000a7e4d74c3c1d0ec0e87e482cd19` |
| `common\scripted_triggers\016_mengele_cloning_stage_decision_triggers.txt` | `7318ff6926bbe23321df66658355e19e88998954c0918861a33b994a45369a8d` |
| `common\scripted_triggers\016_mengele_conventional_stage_decision_triggers.txt` | `1e361c5f85585c4eb51aa0ea7bb2345cc21287a2ea0c7858ce93263f737b2a38` |
| `common\scripted_triggers\016_mengele_native_selection_decision_triggers.txt` | `f3aa2d778f847166e36f39a245a04799fe1e31c7818ceab91825f0d9932989d1` |

No competing definitions of the 33 helper identifiers or three enum categories were found in the current scripted-effect, scripted-trigger, and constant registries.
This source collision review does not establish domain or runtime acceptance.

## Bounded local reference and source ledger

Additional correction reads cover `common\scripted_triggers\016_mengele_cloning_stage_decision_triggers.txt` lines 1-42, `common\scripted_triggers\016_mengele_conventional_stage_decision_triggers.txt` lines 31-59, and `common\scripted_triggers\016_mengele_native_selection_decision_triggers.txt` lines 1-62, with hashes in the final validation table above.
Temporary-trigger arithmetic and its unscoped lifetime were checked against installed `documentation\triggers_documentation.md` lines 7482-7500 and offline Data structures lines 437-443 and 1070-1076, with the same reference hashes below.
The proof keeps static Cloning slot 7 as a documented ID-minus-one enumeration mapping to preserve its no-write contract, rather than introducing unscoped scratch state or claiming undocumented constant-token index support.

Paths are Windows native paths.
Relative paths are rooted in the repository above.
SHA-256 identifies the actual local file revision, not a live game revision.
The offline wiki is the repository snapshot and no web wiki access was used.
Source hashes should be refreshed by the parent if concurrent integration changes the relevant files.

| Path | Read span / artifact | SHA-256 |
| --- | --- | --- |
| `AGENTS.md` | complete file | `38e479cb75828ba888860be8bc3739f9286c0d925cc7d8de5ecd3b8dadec46cf` |
| `.agents\skills\chaos-redux-events\SKILL.md` | event ownership, helper, MCP, documentation and completion sections | `c38b0fd3ff89279ff465ccf1c5e4e848ee9dbb7ce6e652baaca0b5d9013dd777` |
| `.agents\skills\chaos-redux-subagents\SKILL.md` | role, authority, handoff and parent review sections | `62d1531407a24bbbe0d7844cca3439132cfc4a1bf2cccbf4180c76725af69d31` |
| `.agents\skills\chaos-redux-decisions-missions\SKILL.md` | 1-42, 246-282 and UI, lifecycle, AI ownership sections | `2b2805e38e89271c41d19259e34b236a32c8838d9a4f51e88bc126a289115130` |
| `docs\specs\016_brilliant_scientist_specs\specs\016_native_prototype_ownership_amendment_2026-10-03.md` | complete file | `3164c6379e26e285f73359ce914b0202d7e0247131da15b758b792c4b008bbb1` |
| `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_native_prototype_ownership_architecture_2026-10-03.md` | complete file | `6cecb3d38a69d5f6a72b504a53ef1351274d00b6008058becaa1e28b68d82690` |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | 11-76, 769-831, 895-923, 985-1005, 1094-1120, 1290-1357, 1464-1571, 1666-1709 | `adefae1a96a2d141434ba74e60cb5c6f56ae0951daf174e962eba419ff7c4881` |
| `common\scripted_triggers\016_mengele_project_stage_triggers.txt` | 16-84, 152-193, 224-240, 317-328, 1282-1348, 1448-1498 | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common\scripted_triggers\016_mengele_project_bridge_triggers.txt` | 8-10, 77-86 | `f1489f0c8137a47d05b2c0ecc369b2d638000a7e4d74c3c1d0ec0e87e482cd19` |
| `common\scripted_effects\016_mengele_project_bridge_effects.txt` | 9-40, 88-111, concurrent parent integration observed | `f42d53e42f302ef970ab318751c98014247e628435fc30261846834abf6ce87c` |
| `common\script_constants\016_brilliant_scientist_constants.txt` | 16-48, 333-369 | `adfee7fe6093933c394c34c8a6a162795d4bdb4575512c476b417c1173b6e4a6` |
| `common\scripted_effects\chaosx_dynamic_effects.txt` | 1-59 | `91b4609d44fc19d619fc8b6d22ef4a32b78d20ac14f9f2ef58a1b9da152d7c04` |
| `common\scripted_effects\chaosx_dynamic_effects.md` | 1-5, 46-86 | `d013e259e57db26690501f0d876e7197740b756227a3073dcf35cca5f1a5f375` |
| `common\special_projects\projects\016_brilliant_scientist_projects.txt` | 397-427 | `7746dea576b0dfc51182e205d6caad4c3306cc562f0a81482bc550e75723917d` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\rocket_projects.txt` | 10-78, exact available.FROM at 49-53 | `c2aa6f2822c6a5dc1f7edc34d917ef2440f245c47ea02358ad05f8f38c7de6da` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\air_projects.txt` | 793-859, exact available.FROM at 802-819 | `9a8e41f1dd41d22bcb6ba8974bc217ae9f2404f262e508a4d32b3f7c10c077e1` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\documentation.md` | 1-65, 158-163, 198-225 | `16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-245 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-83 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2278-2291, 2733-2749, 2792-2799, 6496-6512, 6730-6737, 7820-7839, 7888-7907, 8573-8586 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 2110-2134, 3624-3638, 3738-3746, 3844-3851, 4882-4889, 6228-6256 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 102-125, 263-291, 301-313, 437-443, 550-575, 1070-1088 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 885-886, 2359-2400 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 4454-4490, 4683-4707 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 53-61, 254-259 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 41-48 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
