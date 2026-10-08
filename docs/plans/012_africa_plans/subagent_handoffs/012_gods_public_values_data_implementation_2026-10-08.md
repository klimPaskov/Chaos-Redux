# Event 012 Gods public-value data implementation

Disposition: implemented source, pending parent review and native acceptance.
Acceptance basis: the parent's October 8 assignment implements completion-audit F3 with exactly the existing Strength and personal Wrath values, floor-safe current displays, raw fills, optional native frames, qualitative movement and existing producer-bound observation.
The parent separately owns F2 protection eligibility, industrial design, GUI presentation and final integration/commit.
This handoff certifies the bounded data implementation and source-model findings, not whole-event or native completion.

## Files changed

| File | Ownership and change |
| --- | --- |
| `common\scripted_effects\012_africa_gods_public_values_effects.txt` | New private country-scope observers, committed-Wrath observation gate and presentation cleanup/reset effects. |
| `common\scripted_effects\012_africa_gods_public_values_effects.md` | New complete private API contract: helper map, scopes, inputs, outputs, defaults, side effects, examples, constants, hooks, cleanup, consumer boundaries and references. |
| `common\scripted_triggers\012_africa_gods_public_values_triggers.txt` | New pure actor visibility predicate `gods_of_africa_public_wrath_is_visible`. |
| `common\scripted_effects\012_africa_gods_effects.txt` | Thirteen presentation-only calls in ten existing owner bodies. No raw metric arithmetic, scoring, bands, costs, history, protection, AI, registry or gameplay guard changes. |
| `.tools\validation\test_012_gods_response_phases.js` | Exact owner/helper whitelist with one-call assertions, plus the specifically coordinated parent-owned F2 wrapper/predicate and constant exceptions. |
| `.tools\validation\test_012_gods_public_values.js` | New focused production-helper source model with eight test groups. |
| This handoff and `012_gods_public_values_2026-10-08_evidence\` | Immutable owned-file before snapshots, reviewed main hook diff, source hashes, named model results and retained MCP/reference evidence. |

No additional existing cleanup file needed editing because enrollment, archive, participant cancellation/finalization and host-loss/system cleanup already converge in the permitted main effects file.
No constants were added or changed by this subagent.
The parent-owned main constants, triggers, protection predicate file and localisation requirement key were read for preservation verification and were not edited.
No assets, GUI/GFX/localisation/category files, country/model/workbook files or Git mutations were made.

## UI data interface

| Identifier | Scope and semantics |
| --- | --- |
| `global.gods_of_africa_strength_display` | Floor of committed raw global Strength. |
| `global.gods_of_africa_strength_fill` | Raw global Strength divided by the existing maximum Strength constant, clamped to zero through one. |
| `global.gods_of_africa_strength_frame` | Floored Strength plus one, optional one-based native atlas cell. |
| `gods_of_africa_wrath_display` | Actor-country floor of committed raw personal Wrath. |
| `gods_of_africa_wrath_fill` | Actor raw Wrath divided by the existing maximum Wrath constant, clamped to zero through one. |
| `gods_of_africa_wrath_frame` | Actor floored Wrath plus one, optional native atlas cell. |
| `gods_of_africa_strength_trend_rising`, `gods_of_africa_strength_trend_falling` | Current host country flags. Neither means neutral. |
| `gods_of_africa_wrath_trend_rising`, `gods_of_africa_wrath_trend_falling` | Actor country flags. Neither means neutral. |
| `gods_of_africa_public_wrath_is_visible` | Pure country trigger: raw personal Wrath exists and THIS country is not the current `africa_host` target. With no target, an actor with raw Wrath remains eligible at this predicate level. Categories own context/lifetime gates. |

Both cache displays use the verified native `round_variable` command on a copy, then subtract one if the rounded copy exceeds raw value.
The raw values are never modified by these helpers.
Frames range from one through 101 under the existing zero through 100 raw ranges.
Fill uses the raw fraction and does not inherit whole-point flooring.
No native atlas or GUI consumer is installed by this data task.

Private previous samples are host `gods_of_africa_strength_previous_observed` with `gods_of_africa_strength_sample_known`, and actor `gods_of_africa_wrath_previous_observed` with `gods_of_africa_wrath_sample_known`.
The first or incomplete sample initializes accurate display data with neutral trend.
Changed observations compare the last committed raw value, including subpoint motion, rather than requested or projected deltas.
A steady real metric transaction records neutral.
An unchanged direct floor check without a positive in-flight Wrath request preserves the last actual observed movement and performs no duplicate cache observation.

## Helper and call-site map

The full helper scope/input/output/default/side-effect contracts and examples are in `common\scripted_effects\012_africa_gods_public_values_effects.md`.
All helpers have ordinary `= yes` calls, no dollar parameters, no temporary variables and no event-target mutations.

| Existing owner and current source line | Presentation call and placement |
| --- | --- |
| `gods_of_africa_initialize_system`, main effects lines 42 and 55 | Clears host Strength sample/trends on a fresh generation, then observes immediately after the existing initial global Strength assignment. |
| `gods_of_africa_register_participant`, line 419 | Clears personal cache/sample/trends before the existing durable-history initializer and floor refresh. The floor producer initializes accurate final Wrath presentation before the introduction. |
| `gods_of_africa_archive_invalid_participant`, line 600 | Clears personal presentation metadata after archival while retaining durable Wrath/history. |
| `gods_of_africa_refresh_strength`, line 807 | Observes immediately after smoothing, raw clamp, gameplay band selection and the committed global assignment. |
| `gods_of_africa_enforce_wrath_floor`, line 876 | Calls `gods_of_africa_observe_public_wrath_commit` after its final raw clamp. The private gate calls `gods_of_africa_observe_public_wrath` only for an initial/incomplete sample, changed committed raw value or in-flight positive Wrath transaction. |
| `gods_of_africa_clean_participant`, line 4239 | Clears personal presentation metadata on existing participant cleanup. |
| `gods_of_africa_finalize_participant`, line 4441 | Clears personal presentation metadata after settlement drops live membership. |
| `gods_of_africa_cancel_on_unifier_loss`, lines 4478 and 4507 | Clears retired-host Strength sample/trends regardless of target changes, then resets global cache to display/fill zero and frame one inside the same current-target guard that writes raw global Strength to zero. |
| `gods_of_africa_cancel_participant`, line 4524 | Clears personal presentation metadata on authority-loss participant cancellation, including the receipt-preserving recovery wrapper's existing call. |
| `gods_of_africa_clean_system`, lines 4692 and 4710 | Clears host observation metadata and resets the global cache alongside the existing global raw zero assignment. |

The Wrath transaction retains its existing single call to `gods_of_africa_enforce_wrath_floor` and gains no second observer.
Direct floor callers are `gods_of_africa_refresh_participant_floors` and `gods_of_africa_mark_offender`.
The registry refresh can record an agreement-war breach through `gods_of_africa_observe_agreement_war` → `gods_of_africa_record_treaty_breach` → `gods_of_africa_apply_wrath` before calling its outer floor helper.
The commit gate prevents that unchanged outer floor from wiping the breach's trend after the inner transaction has cleared its request.
It introduces no transaction temporary and cannot clobber material-transfer flooring.

## Constants, targets, cleanup and migration

The data helpers reuse `constant:gods_of_africa_value.zero`, `.one`, `.maximum_strength` and `.maximum_wrath`.
No tuning table or threshold changes are needed, and the existing Strength 20/40/60/80 and Wrath 15/30/50/70/85 boundaries remain authoritative.
Next-threshold text should read raw values or existing gameplay classification, and current whole-point text should read the presentation cache.

The only scope pointer is the existing `africa_host` target, which is read through a THIS-country `tag` check.
ROOT/FROM/PREV are not used as substitutes for the actor, and no new target needs cleanup.
Personal cleanup clears exactly display/fill/frame, previous sample, known-sample flag and trend flags, preserving durable raw Wrath, gameplay band, opt-out, history, grading and settlement receipts.
Host loss resets the global display to zero only where the existing owner also resets raw global Strength, so stale-host cleanup cannot erase a successor's cache through these hooks.

Producer-bound migration is deliberate.
First initialization and enrollment populate accurate caches, including enrollment floors.
An already running actor with raw values but missing presentation metadata gets an accurate neutral cache on its next existing producer call.
There is no startup backfill, new recurring hook or added world scan.
An absent cache before that call must remain pending/guarded at the UI consumer rather than be presented as an invented current zero.

Existing cause inputs remain available: host `gods_of_africa_strength_capital_lost`, `gods_of_africa_strength_sustain_factor`, native `surrender_progress`, actor war/territory/broken-treaty/recent-extreme floor flags, defiance and unresolved treaty/conduct flags.
The UI worker owns getter text, cause wording and next-threshold context.
No hidden component ledger or third public relationship value was exposed.

## Meaningful validation

`node .tools\validation\test_012_gods_public_values.js`: eight groups passed with zero failures.
The model executes production observer/commit/cleanup bodies and the pure predicate, full production `apply_wrath` and `enforce_wrath_floor` bodies, the raw initializer tail and the actual Strength smoothing/commit tail.
The full registry and native lifecycle remain outside that model.

| Named case | Result |
| --- | --- |
| Initial/missing/incomplete samples | No raw value creates no observer writes. Six incomplete-sample cases initialize accurate neutral data. |
| Rise/fall/steady/subpoint movement | Twelve observations record the committed raw direction, including changes within one floored point and neutral steady transactions. |
| Fractional threshold boundaries/endpoints | Forty-nine cases at and around every named Strength/Wrath boundary and zero/100 retain raw values and never display a higher band through nearest rounding. |
| Actual Strength smoothing | Three production-tail cases follow the smoothing step or immediate commit. The previous sample stores final Strength rather than projected target. |
| Floor-clamped Wrath | Fully clamped decreases remain neutral, partially applied decreases report falling, direct floor increases report rising, invalid-generation floor calls perform no writes, and unchanged direct floor repeats preserve the last movement. Each `apply_wrath` observes exactly once. |
| Enrollment/reentry | Production raw initializer tail plus real enrollment clear hook and floor owner include the initial floor, preserve durable restored Wrath/history and seed neutral presentation. |
| Cleanup/restoration/actor isolation | Cache metadata clears without raw/history/opt-out loss, restoration seeds neutral, wrong-host Strength observation cannot overwrite the global cache, and three distinct country fixtures remain isolated with unrelated ROOT. |
| Hook/write inventory | Exact producer ordering and lifecycle hooks are checked. New helpers write only the enumerated presentation fields/flags, with zero raw metric writes or temporary-variable writes. |

`node .tools\validation\test_012_gods_response_phases.js`: 22 existing groups passed with zero failures after the parent F2 patch was present.
The original Chaos normalization associated with `a2b23f1ef412b6c88e592ccca32a8d93b363064a` remains covered by its production-curve and owner AST comparisons.
The main owner comparison permits only the named presentation calls, once in each designated owner body.
Its parent-owned F2 exceptions require the exact `gods_of_africa_protection_target_requirements_tt` wrapper key, exactly one `gods_of_africa_protection_relationship_is_eligible = yes`, the unchanged original protection body and exactly `minimum_completed_demands = 3` in the existing protection constant category.
Every other old trigger/body and tuning field remains under the original comparison.
Protection policy remains an explicit legacy fixture boundary in phase cases, with actual criteria validation retained by the parent's separate focused test.

The source-model results are explicitly `SourceNoNativeProof`.
They use JavaScript arithmetic and the documented nearest-integer tie behavior, not native fixed-point execution.
Generation eligibility in the focused data model is an explicit fixture input, component producers are Strength-tail inputs, and native world scanning, material transactions, GUI rendering, save persistence and native event delivery are not simulated.

## References and MCP limits

The connected reference routes were verified and used before source editing.
Both installed documentation and the offline wiki were consulted, without web wiki access.
`mcp_evidence.json` retains read source paths, line spans, revisions, exact lookup results, tool checks and artifact references.

| Reference | Read coverage and revision |
| --- | --- |
| Installed `documentation\effects_documentation.md` | `round_variable` 6486–6495, `clamp_variable` 2695–2712, `divide_variable` 3609–3615, `set_variable` 7888–7895 through MCP, plus local syntax examples at 7888–7909. Revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. |
| Installed `documentation\triggers_documentation.md` | MCP `check_variable` 2110–2135, plus local `has_event_target` 3844–3852, `has_variable` 5006–5014 and `tag` 7649–7657. Revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`. |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | MCP round row 573, variable types 435–443 and scoping 444–480. Revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | Local current-scope, target and scope-type explanation at 27–53. This is supporting source reading, not native scope execution. |
| Vanilla and repository precedents | Vanilla `common\scripted_effects\BUL_scripted_effects.txt` 1604–1618 uses `round_variable`. Existing `chaosx_dynamic_effects.txt` 678–684 implements floor by round/correct, with its companion markdown 266–282. No generic helper was added. |

`hoi4.source_lookup` found the exact floor producer at original main effects 852–872 under workspace revision `2e92f40c9cde866c8cbcbf95e3916cbed6ea4e0982f2b41fe348f9dd693de751`.
Its references were incomplete with 20,205 unresolved workspace references, so source lookup was not used to claim complete callers or helper closure.
Direct source searches established the three floor call sites and the agreement-war nested path.

Explicit country-scope `hoi4.script_validate` checks returned `valid = true` for both metadata cleanup effects and the pure Wrath visibility predicate, covering only syntax, native command kinds and declared scope.
Both numeric observers returned `valid = null` with 11 unchecked native argument blocks each, and the global cache reset returned `valid = null` with three unchecked argument blocks.
The committed-Wrath gate returned `valid = null` with three unchecked `check_variable` blocks and an unresolved scripted-observer reference in the native-command-only checker.
That named helper is defined in the same production file and executed by the focused source model.
Parameters and engine behavior remain unproved, and omitted supported findings are not treated as complete validation.

Focused event inspect/scan/render results retained revision `e59ab758e239e5ea62d20e5c085f4aa12ec8c39fae3ec9dac0d5ddca379ebd2d` and reported `analysisMode = focused`, zero indexed helpers and partial coverage.
The `.600` scope render selected zero nodes and omitted 46,265 nodes, so its artifacts do not establish a Gods layout or helper lifecycle.
Reading the retained scan artifact failed with the exact blocker `Artifact provenance manifest is unavailable`.
A full `state_flow` attempt using the initial literal `chaosx.nr012.1` selector timed out awaiting `tools/call` after 600 seconds.
Source clarified the actual Gods namespace `chaosx.nr12`, and the corrected focused calls use `chaosx.nr12.600`.
No corrected full helper-lifecycle result was obtained, and the timed-out initial selector is not evidence that every full route is unavailable.
The final `hoi4.event_compare` attempt against the retained graph baseline returned `ARTIFACT_NOT_FOUND` with `Artifact provenance manifest is unavailable`.
Post-change `.600` scope rendering again selected zero nodes under the same focused revision, so it supplies no successful lifecycle comparison.
The separate exact `hoi4.source_lookup` did find `chaosx.nr12.600` in `mod:events/012_africa_gods_of_africa.txt` lines 13–20 under source-index revision `efc5cb9452cb970096053afdf5516781685d6c45f12d9473cd6a08deca615e1b`.
The event source therefore exists in the exact source index despite the focused render's empty selection, and that discrepancy remains an inspection coverage limitation.
Final tool results and artifact URIs are retained in `mcp_final_domain_results.json`, with the added committed-Wrath checker and final reference reads in `mcp_final_supplement.json`.

## Simplifications, omissions, blockers and parent follow-up

No gameplay simplifications or balance changes were made.
The documented neutral first-cache behavior on the next existing producer is the only migration boundary.
Native parameter/fixed-point behavior, persistence and full event-helper lifecycle acceptance remain unresolved rather than replaced with source-only engine claims.
No probability-bearing helper or AI surface was changed, so this data task claims no probability-auditor result.

The requested visibility helper is intentional consumer scaffolding for the parent's UI worker and has no installed GUI consumer in this patch.
UI worker `01a11ac5-6943-7a50-a08d-978b6a8f5558` remains under the parent's reference-only phase and acceptance review.
The parent/UI worker owns actual category/GUI attachment, getters, causes, threshold text, atlas choice if used, and mandatory matching GUI inspect/render evidence.
This subagent did not assume layout acceptance or edit those files.
Parent review and commit remain pending, and native acceptance belongs to the user.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or updated because these event-specific data names and decisions belong in the private API/handoff.
