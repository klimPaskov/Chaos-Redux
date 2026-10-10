# Event021 claimant missile source-scope repair

Disposition: implemented bounded split and uncached-region source repairs, with parent review of the region extension and no-child recovery unresolved.
Acceptance basis: the parent explicitly authorized source-accounting repairs and narrowly related cleanup inside `032_missiles_operations_effects.txt`, its matching documentation, this new handoff and an optional actual-source test.
The parent owns Event006 and Event021 source, integration, review and commit.
The parent reviewed the first split patch and its seven-test evidence, then explicitly extended writes to the region helper in `032_missiles_effects.txt`, its matching markdown, the same fixture and this handoff.
The appended region extension records that later authorization and supersedes the initial cached-only validation limit.

## Completed work and ownership

Changed paths are `common/scripted_effects/032_missiles_operations_effects.txt`, `common/scripted_effects/032_missiles_operations_effects.md`, new `.tools/test_event021_claimant_missile_scope.py` and this new handoff.
No other files were edited and no Git writes, game execution, desktop control or log searches were performed.
The missile source and its markdown had empty working-tree and index diffs at initial inspection and again immediately before editing.
Their initial SHA-256 values were `5ec05957945ad6f2f2e71adf4091edeca7b08e57a233f8267585b7428cbcd6e7` and `1d8d5aff79f46ea382f41f1d1e4477fca115c849a8300c39819872470fbf6d8b`.
HEAD moved from `6a2ebc838bd66a62b9716dcfd1496dab05e61ad4` to `cf3fea1c550c9dd5b26fad4901df4957a3d463b5` before editing and to `6679d3402d70e6a776eb4272b03668ca3472d239` during verification, while the approved source baseline remained unchanged before the patch.
Those movements are observations of the shared repository, not commits by this worker.

## Helper map and call sites

| Helper | Scope and input | Output and side effects | Call sites and change |
| --- | --- | --- | --- |
| `missiles_preflight_country_split` at 6811 | Actual donor COUNTRY, initialized programme, normal reserve and no active split transaction | Normal donor result defaults to rejected, accepted preflight aborts/cleans its operation, snapshots its programme, allocates a global sequence and marks controlled registered sites | Existing Event021 parent calls at 4528 and 4737 remain unchanged, STATE receipt reads and capacity credits now use regular `missiles_civil_war_parent` |
| `missiles_finalize_civil_war_split_child` at 6862 | Child COUNTRY after native state assignment, regular parent target with accepted active transaction | Child programme, matched site registry, inherited reserve share, donor debit and parent settlement | Existing alias `missiles_split_program_after_civil_war` at 7025, reached from Event021 parent callbacks at 3706 and 3901, STATE registry/capacity/controller accounting now uses the child iterator's `PREV` |
| `missiles_finalize_civil_war_split_parent` at 6969 | Actual donor COUNTRY and active unfinalized receipt | Retained site registry, cleared pending markers, original readiness/control with existing shock, normal finalized receipt and arithmetic residual | Existing call from child through saved parent and Event021 parent at 4249, STATE receipt comparison, registry and controller accounting now use the donor iterator's `PREV` |
| `missiles_abort_operation` at 6169 | Current COUNTRY and active operation receipt | Conditional reserve refund, aborted receipt and last-aborted history | Inspected without edits, called by preflight and parent finalization |
| `missiles_cleanup_operation` at 6180 | Current COUNTRY, one-shot cleanup flag and normal operation arrays | Payload release, mission removal, matching site receipt clear through `PREV`, cleared operation state and programme refresh | Inspected without edits and executed by tests, called immediately after abort |

No helper was added, no public inputs/defaults changed, and there is no call-site migration outside the approved file.
The repair replaces twelve incorrect source/child/parent references in the existing three split helpers.
It introduces no tuning constant, weight, GUI, unit, periodic hook or whole-world loop.
Existing shared reserve-share percentage, rounding, command loss and readiness loss remain unchanged.

## Scope and lifecycle trace

The government `.20` event enters the recorded claimant donor without rebinding ROOT.
Preflight snapshots and result records already belong to the current donor, and its saved regular `missiles_civil_war_parent` supplies the receipt read and capacity write inside STATE scope.
On child settlement, the STATE iterator's enclosing COUNTRY is the child, and on nested donor settlement it is the donor even if native ROOT is the child or the original government.
The existing direct parent debit reads the child's normal received capacity through `PREV`, consumes the unscoped child-reserve scratch before nested finalization and retains the same share calculation.
No new temporary outputs require an outer caller initializer.

Reserve trace: `missiles_abort_operation` calls `missiles_refund_operation_reserve` in the current donor, where its own receipt, cost and reserved reserve control the credit.
That refund and its clamp in `032_missiles_effects.txt` contain no foreign ROOT accounting.
`missiles_reserve_for_operation` and abort refund retain their existing current-country contract and were not modified.
The higher preparation path `missiles_reserve_operation_resources:3349` projects allocations, reserves missiles, checks payload escrow, refunds a refused payload and then calls `missiles_mark_operation_sites_reserved:3272` on success.
That site's reservation marker helper still requires programme ROOT for its controller test, operation ID and idle-site removal.
Neither split preflight nor its abort/cleanup closure calls resource reservation or marks a new prepared operation, so this ROOT-bound preparation API was inspected and left outside the current split repair.
Payload trace: `missiles_release_operation_payload` at 4234 returns held nuclear/thermonuclear or biological escrow to the current country once and clears its own escrow fields.
There is no split-path special-payload consumption or chemical ledger debit, so local economy and chemical-system documents were not needed for a changed integration surface.
Operation-site cleanup compares each site's operation ID with the enclosing current country's active operation through `PREV`, and network/custody/phase refresh mostly retains the existing current-country contract, subject to the uncached-region dependency below.

Event target plan: retain only the existing regular parent target for the synchronous split chain, with automatic chain-end expiry and no unsupported manual clear.
State pending markers and split receipt IDs clear when their matching child or donor settlement consumes them.
The normal country finalized receipt remains as idempotence history.
The split active flag clears on donor settlement, and a no-child failure remains pending under the current owner contract.
No global event target or new variable/flag lifecycle was introduced.

## Meaningful validation

`python -B .tools/test_event021_claimant_missile_scope.py` passes seven tests, including government without programme/claimant with programme and two initialized programmes with distinct receipts, sites, reserves and prepared operations.
The fixtures execute the actual preflight, abort, reserve refund, nuclear escrow release, operation cleanup, network recount, custody projection, phase refresh, child allocation, donor debit and nested parent finalizer source rather than substituting a cleanup stub.
They assert that the government and its missile sites retain their normal variables, arrays, flags, missions and modeled nuclear stock.
The child fixtures explicitly supply native owner/controller assignment, test both government ROOT and child ROOT, validate typed stored-controller pointers and repeat parent settlement without a second debit.
Rejected preflight leaves the source operation, global sequence and government untouched, and the no-child fixture exposes pending source receipts rather than inventing rollback.

The interpreter keeps normal country/state storage, global storage, regular targets and unscoped temporaries separate.
Every returning scripted helper discards only temporary names first created inside that call, preserving modifications to caller-preinitialized storage.
An additional caller-owned custody-output test verifies that conservative rule.
The missing-region fixture raises on the unmodeled native region probe instead of supplying a permissive fallback.

The same fixture suite executed against `git show cf3fea1c550c9dd5b26fad4901df4957a3d463b5:common/scripted_effects/032_missiles_operations_effects.txt` detected seven failing assertions and zero interpreter errors.
That Git blob's SHA-256 is `5ec05957945ad6f2f2e71adf4091edeca7b08e57a233f8267585b7428cbcd6e7`, matching the initial physical source hash.
The existing targeted custody suite passes seven tests and special-payload suite passes eight tests using `python -B .tools/test_event32_reserve_custody.py` and `python -B .tools/test_event32_special_payload.py`.

Model boundaries: native civil-war assignment is a supplied fixture state, mission removal has no simulated cancellation callback, nuclear stock credit is idealized, ideas/modifiers are presentation receipts and engine scheduling is not simulated.
Decimal arithmetic uses `ROUND_HALF_UP` for the existing round operation without claiming native precision, rounding or overflow equivalence.
The zero residual in the modeled child transaction is source arithmetic evidence, not native conservation proof.
Biological escrow stock mutation and chemical stores were source-traced but not executed in this new model.

## MCP and source evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Connected tools confirmed and called: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, and `hoi4.script_validate`.
No helper-expansion job or native task capability was assumed or invoked.

The pre-edit exact helper lookup returned workspace-index revision `c55e37fe3e2098fe44bee5169a4bd67a04e834ba146b02eced4c3c88f0f48fae`, one definition at 6811-6854 and no skipped sources.
The post-edit location lookup at 6847 returned revision `2ec0cbc9648e29c34fada8ad1214901bfc891503bb214125d4d95fd2146a50d3`, owner `missiles_preflight_country_split` at 6811-6856, and key path `if[0]/every_controlled_state[0]/set_variable[0]` containing the recorded-source receipt read.
An initial lookup requested `maxLines=100`, received a schema rejection requiring at most 80, and was corrected to 65 and later a 12-line location query.

The narrow Event021 `.20` event trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, zero indexed helpers and one blocking graph diagnostic.
Its revision is `4495e77851dc0c9ee60d7951092c239a04924d4bac48bc4bf83047d20eb0d1da` and graph hash is `00e4d808f71a4ba38c1b7c88a3482a47248c8290431fa7f4e87e945c8970d491`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7231007cdd176ccc0e9d4eeb15499d452dea7b751f0ea6da563e8dc9b6bdbb0/fa52eeaea14122252fdc12c2f023fbf7fa8def64ec976caaca27982fa9434a03/event-trace-4495e77851dc.json`.
The trace summary has a 64-path inline inventory limit out of 403 sources and does not establish helper or lifecycle coverage.
The artifact was not used as runtime or helper-expansion proof.
An optional narrow `hoi4.event_render` scope view for `.20`, depth 1 and five nodes, did not deliver an observed final result before the client wait was terminated.
The server render outcome remains unobserved, and no render artifact or successful comparison is claimed.
Event-graph comparison was not used to certify this helper-only patch because the focused graph excludes scripted-helper lifecycle evidence and parent Event021 edits were concurrent.

`hoi4.script_validate` was called with explicit COUNTRY preflight-body and STATE write-body scopes.
The first attempt tried binding reserved ROOT/PREV and returned `SCRIPT_BINDING_RESERVED`, then retries removed those bindings.
The broad country result retained unresolved helpers, unchecked variable argument blocks and omitted findings, so it was narrowed to the edited source-to-state accounting with the exact binding name `event_target:missiles_civil_war_parent`.
The final narrow COUNTRY result checked five commands with seven findings, two unchecked argument blocks and no omitted findings.
The final narrow STATE result checked six commands with ten findings, four unchecked argument blocks and no omitted findings.
Both returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, `checksPerformed=[syntax, command_kind, declared_scope]` and `parametersChecked=false` against documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
These results confirm the checked command kinds and declared country/state traversal, while variable targeting semantics and native execution remain outside that checker.

Required offline references read through the connected reference tools:

| Source path | Relevant lines | Source revision |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 303-328 regular event targets, 435-443 variable types and conservative helper output lifetime | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260 ROOT, 262 PREV | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2278-2292 array insertion, 3800-3819 current-country controlled-state traversal, 6496-6504 regular target saving, 7888-7909 variable assignment and examples | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |

The event context bundle omitted Scopes and Event modding at its eight-source limit, so targeted ROOT/PREV searches and reads covered the actual scope rule.
No event definition or callback grammar was edited.
Vanilla precedent read directly: `events\Generic.txt:145-152` saves the current-country `alliance_inviter` regular target and the `FROM` country as `alliance_applicant` before later consumers.
Its installed source SHA-256 is `96d510e119ec0548c3957689395674c7361c6689d2c7d0d65d1c0e024956ec26`.
Existing Chaos Redux precedents read include `missiles_rebalance_site_custody`, `missiles_recalculate_network`, the dynamic effects registry and matching documentation.
The reference index reported the optional script-doc source kind unavailable, while the required installed markdown and offline wiki sources were available.

## Precise dependencies for the parent

1. The uncached-region ROOT dependency is implemented in the region extension below.
   `missiles_assign_site_strategic_region` records its actual native controller before the nested state query, uses that named country for all scratch and result reads, and retains the existing loop and cache behavior.
   The extended actual-source fixtures exercise uncached source and child sites and government scratch preservation, so closure is supported by code and regression evidence rather than documentation alone.
   Native strategic-region query behavior remains unobserved.

2. `common/scripted_effects/021_random_civil_war_parent_effects.txt:4528` accepts missile preflight before native secondary civil war.
   The inspected `event021_parent_reject_secondary_transfer:4651` and `event021_parent_rollback_transaction:7063`, together with active bridge documentation, do not demonstrate matching missile rollback if accepted preflight is followed by no child callback.
   No rollback helper is defined in the approved missile operations file, and invoking parent finalization as compensation would apply the existing civil-war command/readiness shock rather than restore the original preflight state.
   The no-child model therefore leaves the donor transaction/site markers pending and records the missing callback contract.
   The parent must settle or explicitly retain that receipt under its owned failure path without undoing a completed child or refunding an already released payload twice.

## Source hashes at initial split validation

| Path | SHA-256 |
| --- | --- |
| Patched `common/scripted_effects/032_missiles_operations_effects.txt` | `ade2b9ea236d85af1ae847eb5ba38b3901405582f27b61c7d8e9d43d10545f2b` |
| Updated `common/scripted_effects/032_missiles_operations_effects.md` | `8931f878d7bf3a181d15725a9bd467baa03ce854c94d0781c38b6ad519909792` |
| New `.tools/test_event021_claimant_missile_scope.py` | `6fcb2cc6c6f543435d547f4ad8bc7dd076dd26aa6b43e55f43b530ed44cffe5f` |
| Unedited `common/script_constants/032_missiles_constants.txt` | `1dabadf3281586ef3106819e5b130f0685c726c85d495a5ef59798fa3c368a94` |
| Unedited `common/scripted_effects/032_missiles_effects.txt` | `b28ef2a3ce3e88c177e29fcf7deefc0ae253531d17ff41afb1eabee90a7f4e64` |
| Unedited `common/scripted_effects/032_missiles_achievement_effects.txt` | `ca46822817bb927a3ef3e92bf791cb24e84486c7b2bb0efd11e39c11f8bb7c51` |
| Unedited `common/scripted_triggers/032_missiles_triggers.txt` | `11bf9495ad7c1daaabe0af1d5caad5cd444fd6873a14da48b031ba1df148a611` |
| Unedited `common/scripted_triggers/032_missiles_operations_triggers.txt` | `424e1749a463c7621c89f8a881eccfd05109f78b8911f6598601c7d324948504` |
| Unedited `common/scripted_triggers/032_missiles_preparation_cost_triggers.txt` | `e4ee30d2c87985947b5a2148486a30241712292c491672453648bcd78e87cdb3` |

## Limits, skipped proof and review

No gameplay simplification or fallback was used in the implementation.
No balance or probability patch was made, so no probability-auditor pass is claimed or required for this bounded repair.
No focus, GUI or map layout was designed or changed.
No live-game, native civil-war transfer, mission-callback, native stockpile, save/reload or engine conservation proof was run, under the parent's explicit boundary.
The no-child rollback finding remains unresolved, and the model and partial MCP checks do not supply a recovery API.
The initial split patch has parent review, while region-extension review and commit remain outstanding.
Skills used were `chaos-redux-events` and `chaos-redux-subagents`, with no skills changed.

## Uncached-region extension after parent review

Acceptance basis: the parent explicitly authorized the exact lookup and its direct caller contract after reviewing the first split patch.
Additional changed paths are `common/scripted_effects/032_missiles_effects.txt`, new `common/scripted_effects/032_missiles_effects.md`, the existing claimant fixture and this handoff.
The core effects file had no worktree or index diff at HEAD `3d6c406ad94193fb62837385e7c6b8f9c4bf7f82`, rechecked immediately before applying the helper edit, and the matching markdown did not exist.
The core file's baseline SHA-256 was `b28ef2a3ce3e88c177e29fcf7deefc0ae253531d17ff41afb1eabee90a7f4e64`.
HEAD later moved to `c0f14281546a4b8f38a07349b752bfbd65e4c55d` through shared work, with no Git writes by this worker.
The additional source diff is confined to the helper and its attached contract comments, with no changes to other function bodies, tuning, query range, loops or map data.
No new gameplay helper or call-site migration was required.

Helper map: `missiles_assign_site_strategic_region` is STATE-scoped with the actual native controller as its COUNTRY context.
It returns normal state cache `missiles_site_strategic_region`, preserves an existing cache as a complete bypass, and retains the existing configured-range zero result.
Before entering the nested `any_state_in` STATE query, it saves the exact source state as regular `missiles_region_probe_state` and its actual controller as regular `missiles_region_probe_country`.
The controller's scratch array and normal result scalars are initialized and cleaned in that named country, with the final state write reading the same named country.
There is no ROOT reference or PREV-dependent owner inference in this helper.
The new country target and existing state target expire with their originating chain and are rebound for each uncached state, while helper-local loop and break temporaries need no caller output storage.

Direct caller proof: `missiles_select_best_site` restricts its owned-state candidate iterator to control by program ROOT before `missiles_score_site_candidate` calls the probe.
`missiles_register_site` requires both ownership and control by program ROOT before its direct probe call.
`missiles_recalculate_network` enters only states controlled by its current COUNTRY, including legally foreign-owned occupied sites, so the captured actual controller is that source country even when event ROOT is another government.
This also handles `on_war_relation_added` on FROM and child/donor finalization under a foreign ROOT.
The helper deliberately ignores legal owner and stale `missiles_site_current_controller` records when binding the native controller.
These direct callers retain their existing bodies and tuning.

The fixture now executes actual `meta_trigger` token replacement, native-selector fixture membership, and the existing bounded `for_loop_effect` including its inclusive upper bound and early break.
The model preserves normal typed scope pointers separately from displayed numeric IDs and discards newly created temporary arrays as well as temporary scalars at helper return.
Native region membership is an explicit fixture input rather than an invented query result or live map claim.
The existing native one-thousand-iteration ceiling is respected by modeled loops, and the unchanged region probe range stays within that ceiling.

`python -B .tools/test_event021_claimant_missile_scope.py` passes eleven tests against current source.
The initial receipt, rejection, abort/refund/cleanup, child commit, idempotence, no-child pending and temporary-lifetime cases are retained, with the old unsupported-region case replaced by execution coverage.
Region cases cover government without/with programme, claimant-owned and government-owned claimant-controlled sites, stale historical controller pointers, an uncached foreign-controlled stale registry entry, complete cached bypass, and uncached child/donor settlement.
They protect pre-existing government probe scalars and its scratch array, preventing cleanup from masking an accidental government write.
The last region ID in the unchanged range is exercised explicitly.
The existing custody suite also passes seven tests.

A regression run substituting only the pre-extension core source from `3d6c406ad94193fb62837385e7c6b8f9c4bf7f82` while retaining the current split helpers detected six failed assertions and no interpreter errors in the then ten-test suite.
That isolates the region dependency from the original split bug, and the copied Git source SHA-256 matches the physical pre-edit core hash above.
The added eleventh test invokes the actual existing parent finalizer with no native child and verifies that it preserves the modeled reserve while applying readiness/control loss, split flags and site isolation.

Current cleanup source includes the parent's extracted `missiles_release_chemical_payload_receipt` and split site-settlement calls.
The fixture loads and executes `032_missiles_payload_receipt_effects.txt` and `cbrn_payload_reservation_effects.txt` with their current constants instead of stubbing these helpers.
The chemical operation receipt flag is absent and `cbrn_payload_open_receipts` is empty in these nuclear/conventional fixtures, so active chemical refund, transfer, loss and stockpile paths are not modeled or certified here.
Relevant chemical release documentation was read to retain that boundary, and no payload, economy or chemical source was edited.
The parent owns that positive-receipt validation.

MCP evidence for the extension uses workspace `mod_chaos_redux_ea3b2d67c2c0`.
The pre-edit source-location lookup at 668 returned revision `fbb4607ee8730d9962a3035619b541dbddb7e2737459cc0e55cf342fa17ebd7f` with the existing region-helper owner.
The post-edit exact lookup returned revision `0ef503d655d31750c8492f77c1e54ab850582762b2b00e804246954ae81ae5d5`, one helper definition at 671-714 and no skipped sources.
Its twelve-line source view exposes the controller capture and named-country entry, while full source was read locally.
Its reference projection returned zero usages and 20,077 unresolved references, so caller completeness was established from direct source searches and reads rather than inferred from that incomplete projection.
No helper-expansion task or job capability was assumed.

The STATE effect validation checks controller capture, named COUNTRY array work and named STATE cache output with explicit event-target scope bindings.
It returned `SCRIPT_CHECK_PARTIAL`, five checked commands, two unchecked argument blocks and zero omitted findings.
The COUNTRY trigger validation of the region selector returned `SCRIPT_CHECK_PARTIAL`, one checked command, one unchecked argument block and zero omitted findings.
Both retain `valid=null`, `parametersChecked=false` and checks limited to syntax, command kind and declared scope against installed documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The actual meta construction and controller/array semantics are covered by source/reference review and the explicit model, not native execution.

Additional cited sections read through the current MCP reference routes:

| Source path | Lines and rule | Revision |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 1693-1714 `any_state_in` supports any scope and strategic-region selection, 6404-6423 `meta_trigger` syntax | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 4312-4330 loop cursor and break are temporary variables | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 383 region selector STATE traversal | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |

Installed vanilla precedent read directly: `common\scripted_effects\CHI_scripted_effects.txt:995-1009` uses `any_state_in` with literal strategic regions under the selected source context.
Its installed source SHA-256 is `7b0cc310aac5be303efdd941921739ee2bc0da81e65ede8acf10d231549d6aa9`.
The existing Event032 meta probe supplies the dynamic-selector precedent, which this patch preserves.

Read-only no-child API result: no existing safe missile rollback API was found for accepted preflight followed by no child callback.
The current exact lookup for `missiles_finalize_civil_war_split_parent` returned revision `1a03b340abde5b66d82cbc34f41b44c06f371d861fa4359fb5aed4e492d944fc`, definition at 7010-7064, and its complete body was read from current source.
Its exact settlement entry is `missiles_finalize_civil_war_split_parent = yes` in the actual donor COUNTRY with an active, unfinalized receipt.
It is safe only for its existing civil-war settlement contract, and must not be described as a no-child rollback because it isolates matched sites, applies the original readiness/control shock and disables retaliation posture.
`missiles_split_program_after_civil_war` and its child finalizer require an actual child callback, `missiles_cleanup_operation` does not retire split receipts, planned-inheritance cancellation clears a different STATE contract, and `missiles_cleanup_removed_country` destroys or transfers a removed actor's programme.
None is safe compensation for a live claimant's failed native split.
No new rollback design, Event021 edit or compensation call was implemented.

Other-file findings remain bounded: `missiles_score_site_candidate` and `missiles_register_site` retain their documented program-ROOT requirements, and the new chemical receipt bodies have separate owner validation outside this region patch.
The earlier region-dependency sentence in `032_missiles_operations_effects.md` is stale after this extension and remains a parent documentation update, since this follow-up only writes the newly authorized core helper documentation, fixture and handoff.
No additional foreign-ROOT mutation was found in the modeled current region/split/empty-chemical-receipt closure.
No gameplay simplification or fallback was introduced, and no native map, stockpile, save/reload or conservation proof is claimed.

Extension hashes:

| Path | SHA-256 |
| --- | --- |
| Patched `common/scripted_effects/032_missiles_effects.txt` | `f6a0cf8553491baf8067bbf19c600b37471cf7cf111e6db195462e0787a95da4` |
| New `common/scripted_effects/032_missiles_effects.md` | `2265860c0b446c766085891852ef7c0bc43ce0d4b0c0d42cec95ab792693cee9` |
| Extended `.tools/test_event021_claimant_missile_scope.py` | `546283123ee1b56133bbadaa9d2d38c877f12f451433e321e7a2bc44d55b50a8` |

The parent-owned operations and payload files changed concurrently, so their earlier hashes are historical and must not be used as identities for this extension's current-source results.
The final eleven-test run checked dependency hashes both before and after execution and found them stable for that run:

| Read-only dependency | SHA-256 during final fixtures |
| --- | --- |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `ac2b1556e639dfdb6194caab32ea2177b67a736a87f98510da46af99d846dc69` |
| `common/scripted_effects/032_missiles_payload_receipt_effects.txt` | `c0c1f9a5882c5a5a5cc8d652d96ed8da1810686c5b7a22e2172d25b918306834` |
| `common/scripted_effects/cbrn_payload_reservation_effects.txt` | `052eb60ca529401e521b29a7236e9d3b73ec42850cd6a4888bdb51c1c6a85a84` |
| `common/script_constants/cbrn_payload_reservation_constants.txt` | `498d969175382aca6e8157806746e1438eac09e283e5b8df5557347c9f0cc293` |
| `common/script_constants/cbrn_system_constants.txt` | `72fba3f6dfc259a2e79dc41469312433e763302ae899b05e632ba7b87e4de618` |
