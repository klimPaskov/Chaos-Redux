# Event 006 bilateral foundation: bounded source review, 2026-10-07

Disposition: unresolved findings for parent-owned correction.
This is a read-only review, not a foreign-layer implementation plan.
The parent clarified that the general foreign queue and remnant layer already exist from October 4-6 and will not be rewritten.
The accepted foreign-reactions/remnant contract is the design authority; its user-approved 4/3/2/1, conflict -3, cutoff 6, and October 3 recommended-alternative acceptance were not reconsidered.
No roles were spawned and no balance targets were chosen.

## Reviewed source identities

Root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
The parent supplied foundation commit `240711ff9`; this review reads the current working files, not an assumed historical checkout.
Source hashes below were checked twice and remained unchanged during review.

| Alias | File | SHA-256 |
| --- | --- | --- |
| E | `common/scripted_effects/006_independence_wave_decision_effects.txt` | `995e1f1242865f9cb8ada8e66d292b6ecceb43960c2565f9da174f819d6b63e8` |
| T | `common/scripted_triggers/006_independence_wave_decision_triggers.txt` | `46c4fafdebbf65e7ec025c46f49824f6aef3726f724700787c7215bd51e7bde1` |
| D | `common/decisions/006_independence_wave_decisions.txt` | `bd48356b1acc47b74af7af3a54e1edf15a20527b419dcf15d922e10571148f19` |
| F | `common/scripted_effects/006_independence_wave_foreign_reaction_effects.txt` | `afd0e6be5e3d08102e61cb714fe8dcaf17a2e1bde620804f363800dcd48ccafd` |

Accepted contract: `docs/specs/006_independence_wave_specs/specs/006_foreign_reactions_and_remnant_petitions_contract.md`, SHA-256 `bdf28e6b0b542b4afa958c56105ea79d14fdd71aa44af1399975df27e83efc5b`.
Existing foreign callers were inspected only where they consume the bilateral API, at F:958-987 and F:1067-1085.
This is not an audit of their queue, remnant callbacks, AI policies, score ranking, or all foreign stances.

## Finding 1: caller-owned temporary result storage is missing

E:2092 and E:2151 first create `independence_wave_bilateral_receipt_new` inside the recognition and guarantee helpers.
DM-13 calls the guarantee helper at D:826 and checks its temporary result at D:828 without first initializing that output in the caller.
The existing foreign recognition caller does the same at F:965/967, and the foreign guarantee caller at F:1074/1076.
There is no caller preinitialization of this output in the reviewed decision or foreign-effect files.

The documented engine limitation is that temporary variables first created inside a scripted effect may disappear after return, whereas caller-preinitialized storage retains helper updates.
Consequently, a receipt or real guarantee can be written while the caller fails to see the new-result flag and skips its Statehood award, opinion and history block.
This is a concrete API lifetime violation; whether each engine execution loses the result is not established by this source review.

Narrow correction: immediately before each result-consuming call, initialize `independence_wave_bilateral_receipt_new` to `constant:independence_wave_value.minimum` in the consuming caller.
Leave the helper's reset and success writes intact.
Document the caller-owned storage requirement beside E:2085-2090 and E:2144-2149 and in the relevant owner API documentation.
Apply the same requirement to any recognition-result guard added while correcting the findings below.
No persistent variable or new central helper is needed.

## Finding 2: DM-16 awards recognition before checking or writing the shared receipt

DM-16 availability at D:973 only checks affordability.
At D:996-997 it unconditionally grants the target `value_major` Recognition, and D:1000 only then invokes `independence_wave_record_recognition_receipt`.
There is no receipt guard in that reward block and no use of the helper's new-result output.
The target filter at D:968 merely requires the target to have less Recognition than the campaign owner.

Concrete reproduction: actor A starts DM-16 toward released country R; while it runs, A uses the immediate Network recognition action DM-39, which writes A's receipt on R at D:2323-2324 and grants Recognition at D:2328-2329.
DM-39 has no DM-16 active-slot exclusion.
When DM-16 finishes, its shared receipt helper correctly finds the existing receipt and writes no new receipt, but Recognition was already awarded again at D:997.
Repeating DM-16 after its cooldown can also award the same actor/receiver/generation again whenever the lower-Recognition target filter still holds.

Narrow correction: in the frozen target country, initialize the result, record recognition first, and grant the bilateral Recognition delta only if `independence_wave_bilateral_receipt_new` equals `constant:independence_wave_plan.loop_increment`.
Keep separately justified Network standing and League campaign effects outside that bilateral award guard.
This fixes deduplication without removing the campaign, changing its cost, or selecting new tuning values.

## Finding 3: DM-12 ignores an already-existing former-host recognition receipt

DM-11 can target the former host: T:540-548 does not exclude it.
A successful DM-11 records that government's receipt at D:651 and grants Recognition at D:653; it does not settle the host-outcome ledger.
DM-12 remains selectable while that ledger is unsettled (D:699).
On its success path, DM-12 records the same receipt at D:736 but ignores whether it was new, then grants the `value_decisive` Recognition delta at D:740 through D:744.
This is a concrete same-government/same-released-generation double-recognition path under the accepted shared-receipt contract.

Narrow correction: initialize the helper result before D:736 and condition the shared bilateral Recognition award on a newly written receipt.
Keep `independence_wave_set_host_outcome` at D:737-738 effective independently, so the former-host separation settlement still resolves.
The contract does not assign every Legitimacy or Instability term to recognition versus legal settlement; preserve independently justified settlement terms rather than removing the entire settlement package.
That attribution is parent-owned and is not a new balance proposal from this review.

## Finding 4: DM-34 does not gate its Statehood award on a new guarantee

D:2026-2028 promises that an existing guarantee is never rewarded twice.
DM-34 calls `independence_wave_apply_bilateral_guarantee` at D:2042 but never reads its new-result output.
It then unconditionally supplies `value_standard` Recognition at D:2048 and `value_major` Security at D:2050 to the country-delta helper at D:2052.
DM-34's patron filter permits an already-guaranteeing patron (T:559), so the existing-guarantee path is reachable.

Concrete reproduction: actor A first guarantees R through DM-13 or the foreign guarantee caller, which writes the guarantee receipt and supplies its Statehood award.
R later completes DM-34 with A.
The shared guarantee helper correctly returns no new act because the relationship or receipt already exists, but DM-34's Recognition and Security changes are still unconditional.
The source therefore does not enforce its stated guarantee-reward deduplication contract.

Narrow correction: initialize and consume the guarantee helper result and gate the guarantee-attributable Statehood award on a newly created guarantee.
Preserve the separate base/transit concession, patron-channel booking, dependency costs, and host-pressure consequences.
The source bundles treaty and guarantee deltas together and does not explicitly allocate their shares; the exact treaty-only Recognition/Security entitlement remains parent-owned and unresolved.
Do not zero or remove the whole treaty package as an inferred balance decision.

## Core helper contracts that are usable

No receiver/actor inversion was found in the bilateral receipt primitives.
Recognition writes at E:2103-2110 and guarantee writes at E:2131-2138 scope from receiver R into actor A and back into saved receiver R.
At the write, THIS is R and PREV is A, so the storage country is R and the targeted key is A; the value is R's generation.
The recognition reader at T:913-917 and guarantee reader at T:920-924 reconstruct R -> A -> PREV(R), leaving PREV=A inside the `_from_prev` trigger.
The targeted keys and generation reads therefore match their writes.
The `_from_root` recognition trigger at T:905-908 is correct for DM-39's actor ROOT at D:2314.

The native relationship direction is also correct: E:2164 executes `give_guarantee = PREV` in A with PREV=R.
T:929-934 closes the act when A already guarantees R or R already holds A's current-generation receipt.
E:2150-2168 therefore suppresses a duplicate native guarantee and only sets its new-result output when it attempts the new native grant.
This is source and documented-scope evidence, not proof that every native engine grant succeeds under every diplomatic restriction.
Callers retain responsibility for their scenario-specific eligibility and costs.

Frozen-owner selection at E:2040-2047 saves the selected state's owner as a country pointer and R's generation for DM-11/12/13/34.
DM-16 at E:2052-2062 freezes the selected released country's pointer and its own generation.
Its temporary generation is consumed inside the same helper before return, so it does not have Finding 1's cross-helper output lifetime issue.
T:941-953 validates the saved counterpart's existence, non-self and peace relationship and the saved released country's matching generation in decision ROOT scope.
The reviewed delayed settlements use the saved variable rather than the selected state's later owner.
No capital-ownership-change redirect was found.
Do not reuse this decision-ROOT validator from an arbitrary foreign-event ROOT without satisfying its documented payer scope contract.

T:65-83 includes every shared frozen-slot decision: DM-11, DM-12, DM-13, DM-16 and DM-34.
Each of their target-root filters checks this active-action guard (D:609, 700, 785, 961 and 2010).
Their ordinary and cancellation paths clear the shared frozen slot (D:670/682, 759/768, 845/857, 1011/1026 and 2063/2080).
No missing shared-slot decision was found in this bounded review.

Cleanup at E:2174-2186 iterates only the receiver's recorded actor arrays.
Inside the saved receiver block, PREV is the iterated actor, so it clears the same targeted receipt key, clears both actor arrays and clears the frozen slot.
E:1150 wires it into decision-layer cleanup, which `independence_wave_reset_current_generation` calls in `common/scripted_effects/006_independence_wave_effects.txt:476`, before clearing the generation at :612.
No targeted-key cleanup inversion or omission was found.
The helpers intentionally leave real engine guarantees intact.
The regular event targets are effect-chain pointers rather than global persistent targets and do not require global-target cleanup.

## Reference and MCP evidence

The connected live tool metadata exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.script_validate`, `hoi4.event_inspect` and `hoi4.event_render`.
Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.
No helper-expansion mode, job-inspection route, native task negotiation, viewer, GUI rewrite or mutation route was used.
Server version/health was not inferred from tool exposure.

Revision-bound reference reads completed:

| Reference | Windows path | Read lines | Source revision |
| --- | --- | --- | --- |
| Variable types and helper temporary lifetime | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` under the root | 435-443, especially 440 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| PREV usage | `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` under the root | 811-871 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Native guarantee | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 4565-4573 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Save regular event target | Same installed effects documentation | 6496-6504 | Same revision |
| Scope-array cleanup iterator | Same installed effects documentation | 4296-4311 | Same revision |

Additional pertinent local sections were read directly: targeted variable keys in Data structures:547-553, installed triggers documentation `check_variable`:2110-2135, `has_decision`:3693-3699, `has_guaranteed`:4016-4024 and `is_in_array`:5672-5685, and installed effects documentation `add_to_array`:2278-2292 and `set_variable`:7888-7895.
Installed triggers document revision cited by the validator: `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The initial decision context bundle omitted Localisation; that unrelated text surface was not claimed as reviewed.
The existing dynamic-effect source and matching Markdown registry were inspected for their owner-API boundary; no central helper extraction is warranted here.

`hoi4.source_lookup` returned the exact recognition-helper definition E:2091-2115, with `complete = true`, one definition, no truncation, `includeReferences = false`, and source revision `cb8d66dba54f48f0368336027c46babd6d906ac7f835b17351149fb7966c699d`.
It returned no artifact URI for that bounded definition.
No source-only claim is presented as engine execution evidence.

Three bounded `hoi4.script_validate` snippets used country scope.
Event-target bindings must use the exact `event_target:name` string in the live validator; bare target names initially left the nested scopes unresolved.
With full binding tokens, the native guarantee snippet returned `SCRIPT_CHECKED`, `valid = true`, one native command checked and no unresolved findings.
The receipt reader returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, four commands checked and one unchecked `check_variable` argument block.
The receipt writer returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, six commands checked and three unchecked argument blocks (`is_in_array`, `add_to_array`, `set_variable`).
All three report only syntax, command kind and declared scope checks; `parametersChecked = false`.
Their installed-documentation aggregate revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The validator does not establish targeted-key equality, receipt-generation semantics, temporary call-frame lifetime, native guarantee success or reward deduplication at runtime.

A focused read-only `.65` trace (`maxDepth = 1`, `maxNodes = 8`, `maxEdges = 12`, no helper expansion) and `.65` scope render (`maxDepth = 1`, `maxNodes = 8`, no helper expansion) both returned `status = error`, `code = JOB_WORKER_EXIT`.
Exact blocker: `The worker stopped without publishing a terminal job outcome`.
Neither returned source artifacts or validated lifecycle coverage.
There is no completed before/after event comparison because source was not changed and the required inspect/render routes failed.
No live game was launched and no logs were searched or requested.

## Completion and parent boundary

Completed: bounded helper/caller scope, frozen-owner, generation, active-slot, receipt/reward and cleanup review, with the findings above returned inline to the parent.
Files changed: this handoff only.
Helper documentation, call sites, constants and cleanup source changed: none.
No new foreign-layer plan, design fallback, simplification, country work or balancing change was made.
No skills were created or updated; the events, decisions/missions and subagents skills were applied.
No Git index operation or commit was performed under the explicit read-only assignment.

Unresolved: parent correction of Findings 1-4, including the independent host-settlement/treaty reward attribution limits stated above, and engine lifecycle evidence blocked by the event worker failure.
No feature-completion or successful in-game behavior claim is made.

## Final route outcomes and exact source-location evidence

The initial bounded state-flow request for variable `independence_wave_diplomatic_counterpart` (`maxNodes = 30`, `maxEdges = 50`, no helper expansion) finally returned a client tool error: `timed out awaiting tools/call after 600s`.
This is an observation timeout, not proof of the server worker's terminal outcome.
No job route was invoked to infer or recover an unverified outcome.
The source review does not substitute for that missing lifecycle coverage.

The initial `hoi4.source_lookup` with E's path and `line = 2110` completed separately with `sourceScope = source_location`, `complete = true` and revision `1951d10f3c4626decd589355f17f6a5ee46a03f1be19a670c0e6c741f0b26f9a`.
It identified owner `independence_wave_record_recognition_receipt` and keyPath `if[0] -> event_target:independence_wave_bilateral_actor[0] -> event_target:independence_wave_bilateral_receiver[0] -> set_variable[0]`, confirming the reviewed nested write location.

The final `hoi4.source_lookup` with D's path, `line = 997`, `view = source` and `includeReferences = false` completed with `sourceScope = source_location`, `complete = true` and revision `923e002b903fa4cc90fb4a4f07fd1835795f3d325dd68397b9aa4aa40c319b35`.
It identified decision `independence_wave_coordinate_recognition_campaign` (D:952-1028), category `independence_wave_recognition_category`, and keyPath `remove_effect[0] -> hidden_effect[0] -> if[0] -> var:independence_wave_diplomatic_counterpart[0] -> independence_wave_change_recognition[0]`.
Both source-location calls returned no artifact URI, no truncated key chain and no source write.

## Owner patch re-review, 2026-10-07

Disposition: Findings 1-4 implemented by the owner and resolved in bounded source review.
The historical findings above are retained as the baseline, not a description of the patched source.
No remaining scripted counterexample was found in the requested patched caller paths.
The parent explicitly accepted the attribution of DM-34 Recognition and Security to the one-guarantee reward receipt under contract line 57; Capacity, concession, tradeoffs, patron changes and host ledgers remain independent treaty results.
This acceptance resolves the reward-attribution uncertainty in Finding 4.

### Patched source and counterexample review

| Previously failing path | Current source | Result of source trace |
| --- | --- | --- |
| DM-13 first-created temporary output | D:831-834 | Caller initializes the result before the guarantee helper; its returned modification is read in caller-owned storage. |
| Foreign recognition first-created temporary output | F:965-968 | Caller initializes before receipt creation and consumes the result immediately; reward/opinion/history remain in the new-receipt branch. |
| Foreign guarantee first-created temporary output | F:1075-1078 | Caller initializes before native-guarantee application and consumes the result immediately; duplicate relationships/receipts do not enter the reward branch. |
| DM-11 recognition followed by DM-12 host settlement | D:736-749 | Receipt result zero leaves Recognition delta zero, while host outcome, Legitimacy and Instability still settle. A new receipt selects the existing decisive Recognition value. |
| DM-39 recognition during a running DM-16, or repeated DM-16 | D:1002-1019 | Receipt is recorded before the Recognition guard. Existing receipt selects no Recognition call; target Network standing, actor Network standing and League effects remain outside the guard. |
| Existing guarantee followed by DM-34 | D:2052-2078 | Guarantee result is initialized, returned and copied to caller-owned `independence_wave_dm34_guarantee_new` before patron helpers. Recognition/Security start at zero and acquire their existing values only when that copy equals loop_increment. Capacity, concession, patron channel, Legitimacy/Instability tradeoffs and host ledgers still execute. |

The DM-34 copy is created in the consuming removal callback, not in the returning guarantee or patron helper.
The reviewed source contains no other writer of `independence_wave_dm34_guarantee_new`; patron helper calls therefore do not overwrite the value used by D:2064.
The DM-12 host-outcome setter was inspected and does not overwrite the bilateral new-result token.
The country-delta adapter at E:14-24 consumes the explicit Recognition and Security delta variables, so the new zero defaults actually reach the value changers rather than a different reward channel.
No recipient or actor scope was moved by these guards.
The original frozen-counterpart/generation validation and cancellation/cleanup contracts remain applicable.
No changes to costs, timing or AI were introduced by the reviewed reward/result handling.

Helper output documentation is also present in current E:2091-2092 and E:2152, explicitly requiring caller initialization before result-consuming calls.
That file's changed hash reflects the reviewed helper comments; its primitives retain the inspected storage and scope structure.

### Localisation review

The three owner-updated tooltip keys are at `localisation/english/006_independence_wave_decisions_l_english.yml:306`, :308 and :309.
DM-16's first-endorsement Recognition condition and DM-34's first-guarantee Recognition/Security condition match the patched source and accepted attribution.
Minor nonblocking wording counterexample at :306: after the sentence making Recognition conditional on a first endorsement, `Otherwise it refuses` can be read as saying an already-endorsing but friendly former host refuses.
The actual code still accepts the legal separation and applies Legitimacy/Instability in that case.
Narrow wording correction: replace `Otherwise it refuses` with `If neither acceptance condition is met, it refuses`, leaving the remaining consequences unchanged.
No localisation was edited by this reviewer.

### Re-review hashes

| Source | SHA-256 |
| --- | --- |
| D | `0a6385a7d7138f32063efa3971ea6c75f00a19ce224a3b2e8578b12f5e52376e` |
| F | `31bb0602c8e9c2ef21768e09ef2e63f62b0fecd8698a0abb12b77ce0f3b9626e` |
| E | `5681fcc878ca8f37628ad61b0e521cf872031d206537c8c5f79e4378c378daf4` |
| T, unchanged from baseline | `46c4fafdebbf65e7ec025c46f49824f6aef3726f724700787c7215bd51e7bde1` |
| Tooltip localisation | `437ea7513bce9e6f33417f15342cea904856f92afbf65b24f24e3a861d7e7ea0` |

Validation is a direct read of the patched source, output-writer searches and conservative caller/helper lifetime traces against the already-read engine references.
These are source traces, not an engine execution or a new numeric balance audit.
No broad MCP request, new role, new foreign-layer plan or live-game run was made during re-review.
The earlier MCP scope evidence and its partial argument-check coverage remain recorded above; failed event-worker and 600-second observation-timeout limits are not cleared by this source patch.
The patched callback snippets introduce no new native command or scope construct needing a repeated command-kind check.
Only this report was appended by the reviewer; all owner source and localisation were left unchanged.
No simplification, design fallback or balance change was introduced by the review.
Skills used remain events, decisions/missions and subagents; no skill was changed.
