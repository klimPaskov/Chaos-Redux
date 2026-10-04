# Event 027 temporary-output contract and firing-protocol audit

Date: 2026-10-03.
Role: `chaosx_scripted_system_architect`.
Disposition: source audit completed, identified narrow fixes applied by the parent and rechecked, required domain MCP evidence unresolved.
Authority: the parent requested a fresh bounded audit and authorized only this handoff file as a write.
The parent explicitly chose the direct Settings dispatch and console-only canonical root bridge described below.
No gameplay, index, commit, external-tool source, or additional report file was changed by this architect.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Installed game root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Repository-relative paths below resolve under that repository root.
The main audit's runtime line references describe revision `147f45f2c397986655d077ca2e685048932bce241100e2fc58c43291034b2ba5`, before the parent's later owner-stamp edit.
The final delivery addendum gives the later owner-stamp and storage-fix revisions with refreshed runtime anchors.
It is authoritative for current status and supersedes the preliminary missing-storage findings recorded below.

## Findings and specific owner fixes

The requested AI, confirmation, receipt, display, and active-mastery declarations landed in the intended definitions.
The initial pass found three stage-helper call sites consuming outputs first created inside their callees.
The parent applied those fixes before final delivery, as recorded in the final addendum.
The offline variable-lifetime rule explicitly says caller declaration guarantees modification through a scripted helper, while callee-created storage may disappear on return.

| Priority | Current caller and source line | Undeclared output and subsequent use | Narrow parent fix |
| --- | --- | --- | --- |
| Required | `common\scripted_effects\027_doctrine_research_effects.txt:150`, `doctrine_research_process_evolution` | `doctrine_research_get_highest_enabled_stage` creates `doctrine_research_target_stage`, consumed at 154 and 189 | Declare `doctrine_research_target_stage = constant:doctrine_research_stage.baseline_calm_world` in the caller before the call |
| Required | Same file:174, same caller | `doctrine_research_get_next_enabled_stage` creates `doctrine_research_next_stage`, consumed at 178 and copied into persistent current stage at 183 | Declare `doctrine_research_next_stage = global.doctrine_research_current_stage` before the call |
| Required | Same file:204, `doctrine_research_prepare_evolution_stage` | Highest-stage output is copied into persistent current stage at 210 | Declare `doctrine_research_target_stage = constant:doctrine_research_stage.baseline_calm_world` before the call |
| Public API completeness | `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:14610`, `doctrine_research_apply_empty_track_mastery` | Its ordinary and Special Forces callees consume `transaction_pre_level` and `transaction_observed_level` after getter calls, but the public wrapper declares neither | Declare both `doctrine_research_transaction_pre_level = 0` and `doctrine_research_transaction_observed_level = 0` before private dispatch, matching the active-mastery wrapper |

The fourth row was a standalone public-helper contract gap, rather than an observed failure of the production confirmation path.
The parent also completed that public wrapper's storage contract before final delivery.
`doctrine_research_confirm_selection` already owns both getter outputs before calling the empty-track wrapper at runtime file:2597.
If direct debug entry to the private empty-track adapters is intended, their definitions at exact file:12686 and :14396 also need local pre/observed storage before their getter calls.
Otherwise document them as private adapters requiring inherited storage and keep direct entry outside their supported API.
Do not declare or reset the selected country-owned domain, track, branch, receipt identity, or an existing loop cursor merely to initialize outputs.

These are storage fixes in existing helpers and call sites, without new helpers or changed gameplay tuning.
Invoke scripted helpers with `= yes`, using their variable contract.
Do not introduce a named-argument helper API or qualify temporary storage as `ROOT.<temporary>` or `PREV.<temporary>`.

## Verified caller anchors and nested contracts

Names in the output column are exact suffixes after `doctrine_research_` unless written in full.

| Actual definition or caller | Verified storage before helper use | Consumer and result |
| --- | --- | --- |
| AI file:63, `ai_choose_scored_domain` | Five `ai_score_*` outputs initialized to zero at 65-69 | `ai_score_domains` at 70, then its five-entry `random_list` |
| AI file:106 and :262, grand/track choosers | `ai_candidate_score = 0` at 107 and 263 | All 13 grand scoring calls and 18 track scoring calls feed caller-owned weights |
| Runtime file:2765, `ai_score_domains` | `ai_domain_completion_found = 0` at 2777, 2792, 2806, 2820, 2834 | Each of five completion-helper calls precedes the corresponding completion-score check |
| Runtime file:2852, `ai_pick_choice` | Grand, track, and subdoctrine `*_found` outputs at 2853-2855 | Chooser result checks at 2861, 2867, 2869 |
| Runtime file:2874, `ai_resolve_active_batch` | `transaction_success = 0` at 2875 | Confirmation call at 2883 and success check at 2884 |
| Runtime file:2437, `confirm_selection` | Pre, observed, expected, point guard, track index, success, post, native completed, recovery proof, receipt found and receipt index at 2440-2450 | Getter, receipt preparation, native adapters and receipt finalization share declared scratch |
| Runtime file:2274, `prepare_receipt` | `transaction_track_index = invalid_index` at 2275 | `capture_track_index` at 2279 supplies receipt track index at 2288 |
| Runtime file:385, `prepare_display_levels` | Observed and pre initialized at 400-401 | Getter at 402 supplies persistent display current level at 403 |
| Exact file:14379, public `apply_mastery` | Success/post/native completed/pre/observed/expected/point guard initialized at 14380-14386, track index at 14387 | `capture_track_index` runs at 14388 before private calls at 14391 and 14393 |
| Exact file:13881 and :14001, private active adapters | Pre/observed at 13882-13883 and 14002-14003, plus their success/post/native outputs | Their getter calls can return values even on direct debug entry |

The public active-mastery wrapper is defined in the exact file, not the runtime file.
Its track index reset is followed by recomputation from the selected track before the private dispatch, so the old selected index is not simply erased.
The ordinary confirmation path captured native pre-level at runtime file:2582 and stored it in `doctrine_research_receipt_pre_levels` at :2290 through receipt preparation at :2587, before calling the wrapper at :2601.
Resetting pre-level scratch in the wrapper does not clear that persisted receipt column.
The private adapter rereads the actual current level and computes expected level as observed plus `mastery_levels_per_choice`.
Empty-track assignment has its own deliberate post-assignment receipt pre-level update and was not redesigned by this audit.

All 107 exact point-step helpers inherit observed/pre storage through the current confirmation or active wrapper call chain.
A local textual warning that a point-step helper lacks an observed declaration is therefore not an additional production defect.
They must retain the inherited current observed level rather than reset it to zero before their loop condition.
The real loop counter is `doctrine_research_transaction_step_guard`, initialized inside each point-step helper, rather than `transaction_point_guard`.
The declared point-guard scratch is currently unused by the native point loops and does not prove their limit behavior.

The human confirmation option at `events\027_doctrine_research.txt:4800` reads the persistent `doctrine_research_last_transaction_result` afterwards at :4802, :4806 and :4810.
It does not consume a returned temporary success scalar, so it needs no extra temporary declaration solely for that option.
Receipt lookup outputs are declared in both their current consumers: restore-selection at runtime file:2240-2241 and confirmation at :2449-2450.
Selections and display fields forwarded through the menu helpers are country-owned normal variables.
Event-owned scripted-localisation field getters compute their temporary option maximum directly within their own `text.trigger` or read normal display fields.
No Event 027 effect-output call was found inside the reviewed event-owned localisation getters or the Event 027 shared event-log selectors.
This is bounded Event 027 field-getter coverage, not a repository-wide localisation or shared-helper audit.

## Current firing protocol

The current producer is `doctrine_research_fire_global_batch` at runtime file:2026.
Source AST inspection found exactly one `every_country` at :2043, with a scope-capture body at :2045 and no doctrine grant, AI chooser, or receiver dispatch in that body.
The captured array is replayed at :2047-2050 into `doctrine_research_append_country_batch`.
That helper at :2144 appends country rows, copies the immutable firing ID, stage, size and date, and increments the caller-declared publication count.
It contains no start-next, AI-resolution, or country-event call.
The six persistent envelope arrays are firing IDs, stages, sizes, dates, History sequences and statuses at :2034-2039.
Country batches include the firing-ID column at :2151.

Success calls the shared repeatable handler at :2064 after publication count equals captured-recipient count.
Failure calls the same handler at :2095 in the mutually exclusive `else` branch.
Neither branch performs owner producer work after its handler call.
The shared handler at `common\scripted_effects\chaosx_logic_effects.txt:1205` records History at :1241 before the Random Stuff callback at :1245.

AST inspection located exactly one `doctrine_research_bind_firing_history` call at `common\scripted_effects\chaosx_events_log_effects.txt:819`, inside the actual `record_events_log_history_entry` definition beginning at :677.
It is not an orphan hook in an evolution recorder.
History sequence and payload are appended before this hook.
The binder validates exact firing ID and status, stores the actual History sequence, consumes ID/index context before releasing wakes, and issues `chaosx.nr27.14` at runtime file:2119.
The recipient event is defined at `events\027_doctrine_research.txt:26-29` and enters its recipient country as ROOT through the country-event contract.
Its wake helper clears scheduled delivery and starts only an inactive live country's persisted queue.
It does not reconstruct a profile from a temporary sender value.

On failed publication, runtime file:2073-2084 revisits captured countries and changes only an aligned country's last row whose firing ID matches this exact current firing.
It preserves older batch statuses, marks the new matching row quarantined, clears recipients at :2085, and records payload zero.
The blocked binder branch at :2124-2132 stores History sequence, consumes the context and issues no wakes.
The earlier architecture handoff's recommendation and historical orphan concern are superseded by these current source anchors for implementation existence.
That handoff is not evidence of native execution.

Settings direct dispatch at `common\scripted_effects\chaosx_settings_effects.txt:4344-4349` calls the producer in its Event 027 branch and keeps generic root/type dispatch in the alternative branch.
The canonical `chaosx.nr27.1` at event file:13-21 is the forced console bridge into the same producer.
This is the parent-selected entry-path deviation, not an independently chosen architecture change.
The source explicitly clears primary and secondary actor override activation before shared recording.
No country actor is inferred from sender ROOT or iterator THIS by this audit, and no live actor-output result is claimed.

## Helper map, tuning and cleanup

| Existing helper family | Scope and inputs | Outputs and side effects | Call sites and contract action |
| --- | --- | --- | --- |
| Highest/next enabled stage getters | Caller context, evolution gates and persistent current stage | Temporary target/next stage, no doctrine mutation | Three stage callers above need declarations |
| AI scores and choosers | Country, live native legality and selected IDs | Temporary scores/presence, normal selected IDs and temporary selection scratch | Current caller anchors verified, probability evidence remains separate |
| Native level getter | Country, selected registered subdoctrine | Temporary pre/observed reward count | Display, confirmation and native adapters must own outputs |
| Track-index getter | Country selected track | Temporary native numeric track index, default invalid index | Receipt and active wrapper declare and recompute |
| Active/empty native mastery wrappers | Country selected domain/grand/track/subdoctrine, verified eligibility | Temporary success/post/native completion and native doctrine mutation | Keep existing confirmation calls, complete empty wrapper's standalone storage contract |
| Receipt prepare/find/finalize | Country active batch, choice number, persistent exact pending receipt ID | Durable receipt rows and transaction result, temporary found/index/success | Existing confirmation owns outputs, retain pending identity and terminal cleanup |
| Producer/append | Country launcher, captured recipient scopes, frozen envelope index | Persistent envelope/country rows, shared History and pacing | Settings direct branch and console bridge, append remains publication-only |
| History binder/wake | Same-chain firing ID/index, actual recorded sequence, recipient country queue | History association and bounded country wake scheduling | Actual normal recorder hook, hidden recipient event |

No new constants or tuning tables are needed for these storage fixes.
Preserve the five batch sizes 1-5, pacing 90 days, level reward delta 1, native point increment 1, scan coverage 20, invalid index -1, maximum batch choices 5, and existing firing-status category.
The 1,000 iteration guard is an existing engine constraint, not a validated safe-queue guarantee.
Installed `MAX_EFFECT_ITERATION` and offline scope documentation establish the for/while cap.
Neither the inspected installed `for_each_scope_loop` section nor its vanilla precedent proves a foreach exemption.
Batch scans at runtime file:2183-2191, receipt lookup at :2222-2236, and other historical ledger loops still require the parent's separate safe-queue resolution.
This audit proposes no queue redesign or limit bypass.

No new event target is needed.
The producer's temporary recipient array is same-chain scratch, while envelope and country rows are persistent cross-event inputs.
Ordinary temporary variables do not carry into the recipient event.
Annexation cleanup clears the country firing-ID column and wake flag at runtime file:2911-2912 together with the existing country ledgers.
The publication failure path quarantines only its own newly published rows and keeps historical rows intact.
Unmatched/corrupt binder context and synchronous reentry during wake delivery remain separate runtime acceptance concerns rather than proven recovery behavior.

Migration consists of adding caller storage at the identified boundaries and documenting these output defaults in `docs\events\027_doctrine_research\overview.md` or the matching owner helper documentation.
No row migration, new flag, global event target, tuning change, central router, wrapper skill, or gameplay redesign is required by the temporary-output fixes.
Do not turn historical recommendations about `add_mastery.index` into current source instructions.
The parent's supplied native rejection is why the current file deliberately omits that field despite installed documentation showing it.

## Meaningful validation and evidence limits

An in-memory Clausewitz AST audit checked actual definition ownership, declaration ordering, getter consumers, and normal-recorder binder ownership.
An initial shell quoting failure produced no audit result and no file mutation, and the successful AST checks ran through Node stdin instead.
An overinclusive local declaration scan was reconciled with inherited caller storage before classifying missing outputs.

After the parent's latest active-wrapper edit, the grouped getter was checked again at exact-file SHA-256 `6feddd521eb6283f169cd684ac95bb4a4a0fa253c58f877303ab20fb0fc0ccbf`.
It has 99 branches with 99 unique selected IDs and 1,980 native threshold predicates, reading levels 1-20.
For each ID, modeled reached levels 0-20 produce matching pre/observed outputs with conservative cleanup of storage created only inside a returning helper.
All 2,079 source cases passed with caller-owned outputs.
This verifies the current source mapping under declared predicate inputs, not native reward timing, bank behavior, engine performance, or equivalence against an independently preserved old source.
The parent's prior 2,079-case preservation finding remains a parent-reported source comparison.

The current 107 `add_mastery` blocks each contain only amount and the three filters `folder`, `sub_doctrine`, `track`.
Amount uses the file-local point-increment token whose value is 1, and no native grant contains an index field.
The public active wrapper AST has all eight declarations and a track-index getter call before private dispatch.
These source checks do not establish exact native one-level or fractional/banked transaction behavior.
No game was launched and no save was supplied.
Full GUI, focus, map, asset, event-completion and gameplay balance audits were outside this bounded helper/firing task.

## MCP evidence and exact blockers

This architect's live tool inventory exposes reference context/search/read, source lookup, event inspect, probability inspect and technology inspect.
Local package metadata reports `hoi4-agent-tools` version 3.6.0, but that package version does not prove connected-process identity or task negotiation.
No helper expansion, job-control or native-task capability was assumed.
The parent-supplied fresh initialize/list health result remains parent evidence.

Successful fresh reference calls returned workspace `mod_chaos_redux_ea3b2d67c2c0` and no artifact URI.
`reference_context(surface = event, limit = 2)` returned installed/wiki source kinds, `missing = []`, and omitted source topics including Data structures, Event modding, Scopes and Localisation.
Their relevant detailed sections were read locally rather than claiming that the compact context established coverage.
The separate `script_doc` source kind is unavailable.

| Successful citation | ID | Revision and exact read |
| --- | --- | --- |
| Installed temporary assignment | `36a1da49ada7cbbbc2e6f6945a02701b9ecbba08b10d02beb4bee699da5f1003` | Effects revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, `reference_read` 7820-7827, `nextLine = null` |
| Installed scope-array iteration | `39465998aed3c09c94d7410956040e41c63044a573d4d6c4202e8ea58e95a7d3` | Same effects revision, `reference_read` 4296-4311, `nextLine = null` |

The initial event selector requests were rejected for missing `selector.kind`, then for using `id` instead of `eventId`.
Those schema errors were corrected and are not event-source diagnostics.
The accepted narrow call was `event_inspect(mode = trace, selector = { kind = event, eventId = chaosx.nr27.1 }, maxDepth = 1, maxNodes = 5, maxEdges = 5)`.
Its client observation budget expired after 30 seconds with no graph or coverage result.
`source_lookup` for `doctrine_research_get_highest_enabled_stage`, first bounded with references and then retried with `includeReferences = false`, one definition and eight lines, also exhausted each 30-second observation budget.
The targeted wiki `reference_search(query = Variable types, sources = [wiki], limit = 1)` did not deliver within its 30-second observation budget, although installed reference lookup/read succeeded.
The corrected technology request `tech_inspect(mode = explain, technologyId = mobile_infantry, maxNodes = 1, maxDepth = 1)` likewise delivered no result within 30 seconds.
An initial `maxDepth = 0` was rejected by the live schema and corrected.
The architect's initial `probability_inspect` did not deliver a result before its execution observer was terminated.
Ending client observation does not establish that a server tool was cancelled or failed.
No domain artifact URI, domain revision, native outcome, completed comparison, or negotiated job handle was delivered by these attempts.
There were no 600-second blocking waits or tool-source substitutions.

The probability evidence pass was delegated read-only to `chaosx_ai_probability_auditor`, agent `01a1025f-47c0-7412-a36b-a612bf20c2fe`, without inherited context or file-write authorization.
The current chooser is weighted `random_list`, not a deterministic maximum-score selector.
The auditor was directed to preserve all weights and use existing named baseline scenarios rather than choose balance targets.
Its returned evidence or exact blocker is recorded in the final delivery addendum below.
Source contract checks above are not substitutes for required probability, event lifecycle, or doctrine MCP evidence.

## Local references and observed source revisions

| Reference | Selected sections read | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 303-325 regular targets, 429-449 variable types/lifetime/scoping | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 24-65 scope semantics, 749-784 array scope iteration, 891-892 for/while cap | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 25-35 recipient ROOT and event-target transfer | Local detailed read, no fresh MCP revision |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 729-791 temporary display and text-trigger lifetime | Local detailed read, no fresh MCP revision |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 4683-4697 scripted-effect definition and Boolean call | Local detailed read, no fresh MCP revision |
| Installed `documentation\effects_documentation.md` | 1477-1504 mastery filters, 2943-2966 country events, 4296-4329 iteration, 7774-7789 assignment, 7820-7827 temporary assignment, 8573-8586 while | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | 4181-4196 native reward-count predicate | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\script_concept_documentation.md` | 216-245 script constants and supported-field restriction | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | Full category schema and examples | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common\scripted_effects\NORDIC_scripted_effects.txt` | 1-15 country capture/replay precedent, differing array names not copied | `dabbc05c1d76c7469e3431582f83a5c2d054678c3b2ec19209b21c4af9682707` |
| Installed `common\scripted_localisation\SEA_PRC_scripted_loc.txt` | 37-54 temporary calculations in the owning text trigger | `387cced4840ef6988e3ba6af4a72b99dc0ba71e82201cfcacd2f875fe5d64a0e` |
| Installed `history\countries\GER - Germany.txt` | 753-769 doctrine selection and filtered mastery source precedent | Source precedent only, not exact-step execution |
| Installed `common\defines\00_defines.lua` | 25, `MAX_EFFECT_ITERATION = 1000` | No foreach exemption established |

Installed temporary-assignment documentation establishes supported assignment syntax, but does not independently specify scripted-helper return storage lifetime.
The exact caller-lifetime caveat is in offline Data structures:440-442 and the current events skill's Helper output lifetime section.
Neither source reading nor a generic reference context proves an engine transaction outcome.

| Audited source | SHA-256 |
| --- | --- |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `147f45f2c397986655d077ca2e685048932bce241100e2fc58c43291034b2ba5` |
| `common\scripted_effects\027_doctrine_research_ai_effects.txt` | `c969af5e7eb0c9f0924a5bdad8f367e4a53f248f31399302d283107141563480` |
| `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt`, final wrapper revision | `6feddd521eb6283f169cd684ac95bb4a4a0fa253c58f877303ab20fb0fc0ccbf` |
| `events\027_doctrine_research.txt` | `777149623bf633fc07c04cf4f7f747a208024d2afee00d6e7120ae4bf9e01751` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt` | `f072dd1d70f7c8aee0ebfc002d2967e119578aa08733fca65806f4c6619d0a60` |
| `common\scripted_localisation\027_doctrine_research_scripted_localisation.txt` | `7bbd4ebf37eb14b634aa1f781aa7945d1c019601f01a5a0bb21ad683b925321a` |
| `common\script_constants\027_doctrine_research_constants.txt` | `a7b5af2152b80855571c18a3607916a6068f71924593604e4a5dedae809e8724` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `7fde6b681e3bd62a38eb2c01a22ffab8fc262ad2b0e37e7d0fede43c028d9b81` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `34c5695ea3f125dc3336e9f796b1d3a418cb1663c9fce6d01a3b177904a50252` |
| `common\scripted_effects\chaosx_logic_effects.txt` | `c28ee6eab4a2ceea866c81cffd6488e04a0b9d9ed509f650cfddcc3f49b7548e` |

## Delivery status

Completed: bounded current-source output contract audit, refreshed exact-wrapper anchors, source getter scenario model, publication/quarantine/History/root protocol review, and concrete parent fixes.
Files changed by this architect: this handoff only.
Helper documentation, gameplay call sites, constants and cleanup logic changed by this architect: none.
Skipped meaningful validation: native bank/rounding/readback execution, delayed/synchronous wake execution, very large queue coverage, and domain MCP render/compare, because no game execution is authorized and domain inspection did not deliver usable results within the bounded observation budget.
Known follow-up: document the final output storage contract, keep private empty adapters restricted to their declared public wrapper unless direct debug entry is explicitly supported, retain the separate probability comparison and safe-queue blockers, and reconcile native acceptance through the parent's existing workflow.
No gameplay simplification or fallback was implemented.
No Event 027 completion claim is made.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, read completely.
No skill was created or changed.

## Final delivery addendum

### Probability specialist result

`chaosx_ai_probability_auditor` returned a completed bounded audit with an unresolved probability result.
Its source-object `probability_inspect`, custom-weighted-pool inspect retry and bounded chooser `source_lookup` each stopped observation at about 30 seconds without delivered artifacts, revisions or analysis IDs.
Server outcomes remain unknown.
The exposed custom-pool fields do not establish that this helper's weighted random pools were extracted or evaluated.

The existing scenario matrix is `docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_probability_scenarios_20261003.md`, SHA-256 `234b41494cb8aaa0929d88b36cb311d6f01ccc43c3e71ec48b3d49d7cfc45783`.
Relevant groups are DR-A01-A06, DR-B01-B04, DR-C01-C07, DR-D01-D06, DR-E01-E06 and DR-G01-G03.
DR-F01-F05 concern the separate repeatable/cluster pool.
The saved same-37 compare attempt JSON, SHA-256 `dfd69bb173f69f2eb81fb82e1a5e09db7af44cc74553bdc91d9749da0f4ec255`, records an unresolved compare and empty state maps.
Eligibility, ranking, normalized shares, dominance, starvation, repeated selection and exploit conclusions are unresolved.
No weights, pool manifest or scenario fixture was changed and the specialist wrote no file.

### Parent owner-stamp refinement

The parent then added an owner stamp at `common\scripted_effects\027_doctrine_research_effects.txt:217-231` and refined both assignment and comparison to explicit numeric `THIS.id`.
The final observed runtime SHA-256 is `4ceaa46ee6a5b3da8d8cb04c44b8013af12f12c0e37dc5f284e2ca3981406bee`.
The actual comparison at :224 is `check_variable = { var = doctrine_research_ledger_owner_country value = THIS.id compare = equals }`.
Assignment at :231 is `set_variable = { doctrine_research_ledger_owner_country = THIS.id }`.
No raw `value = THIS` comparison remains in this owner check.

| Current runtime anchor | Current line |
| --- | --- |
| Display definition and getter storage/call | 399, 414-416 |
| Producer, capture, append replay, success/failure shared calls | 2040, 2057, 2063, 2078 and 2109 |
| Exact-ID failure quarantine and recipient clear | 2090-2098 and 2099 |
| Binder, wake dispatch and blocked branch | 2116, 2133 and 2138-2146 |
| Append and country firing-ID column | 2158 and 2165 |
| Receipt preparation and track-index storage/getter | 2288, 2289 and 2293 |
| Confirmation definition and top output declarations | 2451 and 2454-2464 |
| Active confirmation pre-capture, receipt prepare, empty/active wrapper calls | 2596, 2601, 2611 and 2615 |
| Domain completion output declarations | 2791, 2806, 2820, 2834 and 2848 |
| Choice presence declarations | 2867-2869 |
| AI confirmation-success declaration/call/check | 2889, 2897 and 2898 |
| Country discard definition, firing-ID cleanup and wake cleanup | 2923, 2925 and 2926 |

The initialization prefix checks for an existing normal owner field, compares it to the current country identity, and invokes discard only in that current country if they differ.
It clears that country's three copied achievement flags at :227-229 and stamps the current identity after cleanup.
The discard body at :2923-2965 has no scope transfer to the recorded original owner and no recursive initialize call.
It clears the scoped country's batch/receipt arrays, delivery/pending/active state and selection.
Thus source structure confines rejection to the initialized recipient country.
This is the intended guard against a current-build country B inheriting A's stamped ledger, not native proof of civil-war copying.
Missing-owner legacy data skips the mismatch branch and receives a current identity stamp.
That preserves existing data without inventing an old firing ID, stage, size, human snapshot or historical entitlement.
No new global event or recurring world hook accompanies this prefix.

Primary installed `effects_documentation.md:7888-7907` documents `set_variable` assignment from a value or another variable.
Primary installed `triggers_documentation.md:2110-2134` documents comparing a variable with a number or another variable.
Primary installed `effects_documentation.md:2663-2670` describes `change_tag_from` as changing the player to another country.
That supports separating player transfer from the stamped country object, but is not a complete specification of every country-identity lifecycle transition.
Offline Data structures:429-431 describes internal numeric database IDs and :1484 explicitly documents country `id` as the country's internal ID.
Scoped normal-variable access is documented at :444-449.
The installed generated `dynamic_variables_documentation.md` country section does not enumerate `id`, and no country-specific `THIS.id` entry was found in the installed documentation.
This is a primary-document coverage gap, not evidence that the numeric expression is rejected.
Installed vanilla `SOV_scripted_effects.txt:8302` uses `THIS.id` for a state pointer, and native `00_scripted_triggers.txt:35-55` compares state `id` through a variable.
These establish numeric scope-ID source precedents for states and must not be presented as country-specific execution proof.

The current repository's Event 005 country-reference comparisons use `ROOT.id` and `PREV.id` at `005_soviet_collapse_effects.txt:5021,5039,5051,5055`, with country-reference assignment at :5085.
Event 006 stores country scopes as normal references at `006_independence_wave_effects.txt:2681,3917`.
Those are repository source precedents, while their working status was supplied by the parent.
The earlier raw-scope comparison was never established as a supported `check_variable.value` argument by this audit and is not claimed as proven.
The refined numeric comparison matches documented number/variable comparison, explicit offline country-ID documentation and repository country-reference usage.
No native variable-evaluation result or unsupported-argument error was delivered, so actual rejection is not alleged.
Native identity stability and copied-variable behavior remain runtime evidence limits.

The installed effects documentation links `script_math_expression.md`, which is absent at the linked installed documentation path.
No substitute math-expression claim was used for the stamp.
The owner-stamp refinement does not itself resolve storage findings or expand native/probability acceptance claims.

### Final parent-applied storage fixes and current anchors

The last reread found the parent had applied all three stage declarations and completed the public empty-track wrapper.
Current runtime revision: `4f9a91505fce035da57f135858f8786d1bd0ebfe91cae5b978c3d8998df3faa4`.
Current exact adapter revision: `21b79db0a43776f359cf5a0269c8bc71fa8019efc452cff6e068522a9a0b7395`.
These revisions supersede the intermediate owner-stamp revision and exact-wrapper revision above for current status.

| Former finding or current boundary | Verified current source |
| --- | --- |
| Process-evolution highest output | Runtime :150 declares target, :151 calls highest getter |
| Process-evolution next output | Runtime :175 declares next from persistent current stage, :176 calls next getter |
| Prepare-evolution highest output | Runtime :206 declares target, :207 calls highest getter |
| Public active wrapper | Exact :14379, declarations :14380-14386, track-index recomputation :14387, private calls :14390 and :14392 |
| Public empty wrapper | Exact :14609, pre/observed/expected/index at :14610-14613, recomputation :14614, success/post/native outputs :14615-14617, private calls :14622 and :14624 |
| Confirm root scratch | Runtime :2454, outputs :2457-2466 |
| Display getter storage | Runtime :417-418, getter :419 |
| Receipt track-index storage/getter | Runtime :2292 and :2296 |
| Completion output storage | Runtime :2793,2808,2822,2836,2850 |
| AI choice presence storage | Runtime :2869-2871 |
| AI success storage | Runtime :2891, confirmation :2899, success check :2900 |
| Producer, capture and append | Runtime :2043, :2060, :2066 |
| Success/failure shared handlers | Runtime :2081 and :2112 |
| Binder and wake dispatch | Runtime :2119 and :2136, normal-recorder call remains shared log :819 |
| Country append and firing-ID column | Runtime :2161 and :2168 |
| Owner stamp prefix | Runtime :220-234, numeric comparison :227 and numeric assignment :234 |
| Country-only discard | Runtime :2925, firing-ID cleanup :2927, wake cleanup :2928 |

The parent removed the unused `transaction_point_guard` declarations from confirmation and the active wrapper.
The actual `transaction_step_guard` remains owned by each native point-step helper.
This does not reset an inherited observed level or receipt pre-level and does not change native grant filters.
The public empty wrapper now owns the getter and expected-level scratch, so its private empty adapters inherit storage on both the normal confirmation path and direct public-wrapper entry.
The private empty adapters still lack their own local pre/observed declarations, so unsupported direct entry to those private definitions is not promoted to a public contract.
No unresolved missing temporary-output declaration remains on the reviewed production paths.
The final actual-source AST repeat at these two unchanged hashes passed all 2,079 getter cases and verified prior storage at all three stage getter calls (:151, :176 and :207).
This remains a source model with conservative helper-return cleanup and supplied reached-level predicates, not native execution.
Country-ID typing and runtime clone behavior retain the evidence limits already recorded.

### Follow-up closure and generic scope-ID reference check

The parent confirmed the three stage-output declarations, public empty-wrapper declarations and track-index recomputation, and removal of unused point-guard scratch.
All reviewed public-helper storage findings are closed at source level.
This closure does not establish engine return lifetime, native mastery execution or asynchronous firing behavior.

The exposed `source_lookup` schema remains the legacy symbol/kind/line-bounds schema.
It exposes neither `view` nor `keyPath`, and no such arguments were sent.
The parent's newer reference-read and highest-stage lookup in its own exec cell 28 were reported pending, with no artifact yet supplied.
That parent-owned cell is not this architect's tool handle, and no completed result is inferred from it.

A further local primary-document search found no country-specific or generic `scope.id` type declaration in the installed Markdown documentation.
The generated dynamic-variable country table omits `id`, so it cannot independently establish that property's exact country type.
The fresh `reference_search(query = country internal ID, sources = [game_doc], limit = 2)` returned resource-modifier matches, not a scope-ID declaration.
Those irrelevant matches were not treated as supporting evidence.
A narrow `source_lookup(symbol = id, kind = dynamic_variable, includeReferences = false, maxDefinitions = 1, maxLines = 8, maxReferences = 0)` supplied no result within the 30-second observation budget.
Its server outcome remains unknown.

The exact country-ID evidence therefore remains offline Data structures:1479-1484, read directly, supported by scoped regular-variable access at :444-449 and the Event 005 country-reference comparisons at :5021, :5039, :5051 and :5055.
The installed `set_variable` and `check_variable` definitions establish value/variable assignment and number/variable comparison, while the native state-ID precedents establish numeric scope-ID usage for states.
The combination supports the current numeric identity design at source level, but does not fill the missing primary country-specific property declaration or prove runtime object identity retention.
No source or delivered engine result establishes an unsupported-argument defect in the current `THIS.id` assignment or comparison.
No such defect is claimed, and no raw-scope comparison is described as proven.
