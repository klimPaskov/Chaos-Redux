# Gods recovery helper integration contract

Status: bounded recovery helper implementation delivered; parent integration, specialist probability evidence, and native acceptance remain pending.
Acceptance basis: the parent explicitly adopts the 2026-10-03 original-host recovery design and grants this disjoint new-file patch assignment.
No Git operations or game launch are authorized.

## Public API reserved for parent integration

These identifiers are implemented in the new recovery effects/triggers files.
Parent-owned existing files must supply the direct call sites.

- `gods_of_africa_authorize_initial_epoch`: committed host COUNTRY scope, binds epoch one only without loss/cancellation/recovery history, ROOT independent.
- `gods_of_africa_revoke_current_epoch`: departing host COUNTRY scope, records a monotonic loss once per epoch and revokes permission before core roster cleanup, ROOT independent.
- `gods_of_africa_epoch_permission_is_current`: COUNTRY object validator, exact authoritative host object, commit, ID/origin/shared generation, authorized epoch and physical/terminal gates, ROOT independent.
- `gods_of_africa_recovery_mandate_is_current`: host COUNTRY, checks committed recovery identity plus fresh current-member quorum, ROOT independent.
- `gods_of_africa_activation_wake_is_due`, `gods_of_africa_owner_wake_is_due`, `gods_of_africa_registry_wake_is_due`: host COUNTRY, current permission plus schedule receipt and present current due date before mutation.
- `gods_of_africa_recovery_member_request_is_current`: invited member COUNTRY, actual normal country-object reference plus identity receipts, never invokes an owner ROOT predicate.
- `gods_of_africa_original_host_recovery_is_open`: exact surviving original committed host recovery presentation gate.

Owner fields: `gods_of_africa_authority_epoch`, `gods_of_africa_authority_host_id`, `gods_of_africa_authority_origin_host_id`, `gods_of_africa_authority_host_generation`, `gods_of_africa_loss_sequence`, `gods_of_africa_loss_epoch`.
Owner flags: `gods_of_africa_epoch_authorized`, `gods_of_africa_recovery_open`, `gods_of_africa_recovery_epoch`, `gods_of_africa_original_mandate_restored`.
Recovery transaction fields and committed mandate fields are separate so closing invitations cannot invalidate the completed mandate during consolidation.

Parent initial setup calls the initial binder after shared host commit, and explicitly revokes on loss before clearing a live roster or global host target.
Activation requires current epoch permission and, when `gods_of_africa_recovery_epoch` is set, `gods_of_africa_recovery_mandate_is_current`.
Replace unconditional clock receipt deletion with the matching due predicate before any mutation.
Do not call initialization from a wake hint.
Extend participant/demand/reconciliation and personal victor request identity with this local epoch in parent-owned files.
Do not alter shared `africa_host_generation`.

The parent owns precise secured-continent/terminal proof, including distinguishing Scramble defeat-settled from secured-settled.
The recovery package will not consult generic Scramble settled phase as a terminal proof.
It guards explicit final-settlement/continental-settlement receipts and shared world/terminal flags.

Extend existing host-category visibility with `gods_of_africa_original_host_recovery_is_open`.
Extend participant-category visibility with `gods_of_africa_recovery_member_request_is_current`.
Pending member description key: `gods_of_africa_recovery_member_category_desc`.
Choose it before the normal participant description to avoid reading undefined Wrath for a nonparticipant.

AI recommendation announced before implementation: host start/finish 10, invite/resume 5, member approve 10, decline 1, with low-stability approve factor 0.25 and decline factor 4 below 0.35.
These values are not a completed probability/balance acceptance claim.
The parent's already queued `chaosx_ai_probability_auditor` owns the evidence pass, so no duplicate auditor was spawned.
Successful initial `hoi4.probability_inspect` on existing `gods_of_africa_seek_reconciliation` returned one candidate, poolComplete true and unresolved zero.
Source revision `883777bb9c863b62d8f83a0576841aec6d59f135046df8257b65a7bb52c8a1e3`, source hash `1692058d825b8bf3cd581548b0fc46c1662605ed5799a709f4d2cdca18863b13`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376c6a198a201bff6d7a31eacdcb7c4b01b1123d847495ffa4f3cb3e61aaa56/97fca09911e3bcfffef2853ef4d19f416a7c41e3e83acacb1cf2542e5979bb1a/probability-inspect-1692058d825b.json`.

## Delivered continuation, 2026-10-04

Acceptance basis remains the parent paragraph at lines 3–8 of `012_africa_gods_original_host_recovery_design_2026-10-03.md` and the explicit resumed disjoint-file assignment.
The original design file was read in full; this worker has not changed it or promoted unrelated proposals.
The parent subsequently confirmed that native World Order capitulation, package-actor loss and Scramble defeat preserve the original committed host pointer and shared generation, and defeat writes `africa_scramble_response_defeat` with a settled phase.
The parent explicitly chose `gods_of_africa_continent_is_secured` as the exact witness: explicit continental-settlement receipt or settled phase without the defeat response.
That helper remains parent-owned.

Changed files, all inside the assigned write boundary:

- `common/scripted_effects/012_africa_gods_recovery_effects.txt`: epoch binder/revocation, congress, targeted invitation, responses, commit, receipt-preserving residual cleanup, trusted current clock scheduling and resume.
- `common/scripted_effects/012_africa_gods_recovery_effects.md`: complete owner-local API, input/output lifetime, scope/default/side-effect contracts, state/cleanup/history map, tuning, examples, callers and migration.
- `common/scripted_triggers/012_africa_gods_recovery_triggers.txt`: ROOT-independent owner/epoch/request/mandate validators, original-owner action gates, bounded current-member recount and three permission/receipt/present-due predicates.
- `common/script_constants/012_africa_gods_recovery_constants.txt`: retained accepted minimum/strict-majority values and proposed AI values; added typed literal clock selectors.
- `common/decisions/012_africa_gods_recovery_decisions.txt`: additive start/invite/finish/resume/approve/decline rows in existing categories.
- `common/scripted_localisation/012_africa_gods_recovery_scripted_localisation.txt`: four integer display getters for current consent counts, quorum minimum and existing consolidation duration.
- `localisation/english/012_africa_gods_recovery_l_english.yml`: all six names/descriptions, category request description, requirements/effects, and getter display keys.
- This handoff, updated without discarding its original API reservations or earlier artifact references.

No existing core effect/trigger/constant, category, lifecycle, clock event, World Order/on-action, log, focus, spreadsheet, asset or other agent's assigned file was patched.
No staging, commit, HOI4 launch, external message, or plugin installation occurred.
No additional auditor was spawned because the original partial handoff already assigns the queued specialist evidence pass to the parent.

## Exact integration API and dependency changes

The full helper map, including every supporting identifier, scope, input/output, default, side effect, and local caller, is in `common/scripted_effects/012_africa_gods_recovery_effects.md`.
The API reserved earlier in this handoff is implemented.
Important integration details:

1. Actual initial setup must initialize `gods_of_africa_initial_epoch_setup = constant:gods_of_africa_value.one` immediately before `gods_of_africa_authorize_initial_epoch = yes`.
   The binder consumes this temp to zero, writes epoch one only with no existing epoch/loss/recovery history, and performs no legacy/wake migration.
2. `gods_of_africa_revoke_current_epoch` is ROOT-independent and records one loss per authorized epoch using its own retained authority-host ID, even after the pointer disappeared or a terminal flag was set.
   Call before core roster/pointer cleanup.
   It sets `gods_of_africa_cancelled_on_unifier_loss`, so the parent's existing cancellation guard must not then skip the remaining roster/history cleanup merely because that flag has just been set.
3. All country-object owner validators use exact current target equality and actual existence; none reuse `africa_is_current_host` inside foreign member ROOT.
   Physical return's `africa_focus_first_proof_satisfied` was read at `012_africa_triggers.txt:754–759`; it is only succeeded/recovered country flags and has no ROOT dependency.
4. Following the parent's final-endpoint correction, `gods_of_africa_authority_owner_object_is_current` and `gods_of_africa_epoch_permission_is_current` permit a newly secured continental witness for an already authorized live epoch.
   Initial authorization and original-host recovery separately exclude `gods_of_africa_continent_is_secured`.
   Existing final-settlement-committed and shared terminal receipts still block subsequent operation.
   This uses the existing validator API; no alternate endpoint hook is needed.
5. `.600/.606/.607` must check `gods_of_africa_activation_wake_is_due`, `gods_of_africa_owner_wake_is_due`, or `gods_of_africa_registry_wake_is_due` before any schedule deletion, initialization, roster mutation, dispatch, punishment or requeue.
   Missing current dates do not count as due.
   These helpers never initialize authority from a wake.
6. Commit stores separate `gods_of_africa_mandate_*` identity and a distinct committed approval roster, then closes only the invitation-open flag.
   During consolidation, new eligible members can be invited and answers can reverse without refreshing epoch or date.
   Activation rechecks the current unique relationship denominator and fresh approvals; a lost quorum blocks it.
7. `gods_of_africa_resume_original_host_recovery` requires present schedule/current due/permission/quorum and queues only a one-day existing `.600`, at most once in the current day.
   No missing-date initialization, epoch increment, full-delay refresh or authority grant occurs.
8. Parent integration must preserve `.608` and `.615` receipts on its native loss cleanup too.
   A source case exposed that existing `gods_of_africa_cancel_participant` clears final-outcome and settlement-report flags.
   The local `gods_of_africa_cancel_recovery_participant_preserving_receipts` wrapper snapshots exact existing final-outcome/settlement-report/victor-report flag presence, runs the real cancellation closure, and restores only prior flags; their normal identity fields remain untouched.
   The guarded residual cleanup uses that wrapper.
   The parent can reuse it in the native loss path, but this worker did not patch those callers.
9. Existing host category visibility must include original recovery and current committed pending consolidation; member category visibility must include current member requests.
   Select `gods_of_africa_recovery_member_category_desc` before the normal Wrath-bearing participant description.
10. Parent-owned participant, demand, reconciliation and victor-request epoch binding, direct timeout deadline guards, actual Strength recomputation, and restoration milestone-log integration are still required.
    The new append-only owner recovery-history arrays preserve host/loss/old epoch/new epoch/quorum/day locally and do not replace the shared log.

The six decision IDs are `gods_of_africa_restore_original_mandate`, `gods_of_africa_invite_original_mandate_member`, `gods_of_africa_finish_original_mandate`, `gods_of_africa_resume_original_mandate`, `gods_of_africa_approve_original_mandate`, and `gods_of_africa_decline_original_mandate`.
Each response caller explicitly sets the unscoped answer temp before its `= yes` call.
Start/finish use proposed willingness 10, invite/resume 5, approve 10, decline 1, with approve times 0.25 and decline times 4 below stability 0.35.
These are the user's assigned pending-audit proposals, not native acceptance or click probabilities.
Reversal-related AI churn is a meaningful scenario for the specialist pass.

Constants are grouped into schema-first `gods_of_africa_recovery` (`int`), `gods_of_africa_recovery_clock` (`int`), and `gods_of_africa_recovery_ai` (`fixed_point`).
Existing Gods zero/one and timing categories remain the source for delay and consolidation duration.
No new persistent event target is introduced; the normal invitation host variable is assigned from an actual native country scope.
No shared generation or doctrine write exists in the recovery grant.

## Meaningful source validation executed

A transient Python evaluator parsed the actual recovery effects/triggers and actual relevant existing Event 012 helpers/constants, including the parent's updated contract retirement helper.
It ran 17 source case groups and discarded temporary values first created in every returning scripted-effect/trigger frame while retaining caller-preinitialized storage.
No test file was added outside the assigned boundary.
The following fixtures/results were executed, not just proposed:

| Source case | Concrete fixture | Result |
| --- | --- | --- |
| Initial setup and foreign ROOT | Host object 1, origin 1, shared generation 7; binder temp one; permission tested with native ROOT 2 | Epoch one authorized; input consumed; object permission remained valid under foreign ROOT |
| Physical return alone | Revoke initial epoch, then call initial binder with its token again | No permission, new epoch, date or authority write |
| Duplicate revoke | Revoke epoch one twice | Loss sequence stays one; persistent state unchanged on repeat |
| Physical shortfall | Original host capitulated, then returned with capital controller 2 | Recovery start rejected in both cases |
| Fresh congress | Relationship objects 2/3/4 current generation 7; 2 and 3 invited and approve; doctrine 3; day 100 | Commit writes epoch 2 once, shared generation 7/doctrine 3 unchanged; due 280; one `.600` delay 180; duplicate commit inert |
| Strict majority | Add fourth eligible object 5 while only 2/3 approve; then one-member pool | Two of four and one-member pool cannot commit; no authority mutation |
| Current activation invalidation | Committed recovery due 280, approving object 2 becomes hostile, wrong generation, capitulated, special, nonhuman, deleted or victor-exempt | Each of seven invalidations rejects activation's current quorum |
| Old early activation hint | Day 100 against current due 280 | Due predicate false; explicit resume makes no persistent write or queue |
| Current due with no old temps | Clear all temporary state, day 280 against current due 280 | Current activation predicate succeeds; resume queues one-day `.600`; a second same-day resume is inert |
| Reversed consent | Member 2 declines after commit, then approves while consolidation pending | Mandate fails then recovers; duplicate invitation produces no duplicate invited row |
| Actual request object mismatch | Request scalar receipts still match but normal actual host reference changed to country object 6 | Member request rejected |
| Successor/cleared pointer | Global host changed to object 6 or cleared | Original recovery/member request/wake denied; resume inert; local original revoke still clears permission |
| Defeat-settled | Shared phase settled plus `africa_scramble_response_defeat` | Original recovery allowed |
| Secured versus final receipt | Settled without defeat or explicit continental-settlement receipt | New grant/recovery denied; already authorized epoch still validates for final endpoint; final-settlement receipt then blocks it |
| Active owner/registry wake | Current owner due 300, registry due 340; early 299, due 300, owner next due advanced to 330; registry at 340 and then missing date | Early/duplicate/missing-date checks reject; current due checks pass |
| Dead historic victor | Eligible pool's object 4 becomes deleted and retains victor exemption | Two surviving approvers can commit; no dead-victor requirement; exemption retained |
| Same-generation second loss | Revoke restored epoch 2, begin another congress without changing shared generation 7 | Loss sequence becomes 2; old member request invalid; old aligned recovery history retained |
| Residual cleanup | Actual participant cancellation/retirement closure; residual objects 2/3; object 2 has history days 10/20, victory count/sequence 1, final-outcome and `.608`/`.615` pending flags | Roster clears, displayed count derives as zero; history and report flags/identity fields persist; object 3 gets no fabricated receipt |
| Expired/invalidation request | Independently mismatch stored host ID, origin ID, shared generation, loss sequence, or cancelled epoch | All five request forms rejected before answer changes |
| Renewed quorum after elapsed due | Add eligible member 5 to committed two-of-four pool; invite and approve at due day 280 | Current quorum restored without changing epoch 2 or due 280 |
| Missing permission/schedule/date | Remove epoch permission, activation schedule receipt, or due field from current pending recovery | Wake and resume reject without persistent writes |
| Same-origin successor | Committed owner object 6, preserved origin 1; successor's own initial epoch/loss | Never becomes original-host recovery; separately, consumed successor flag blocks original commit |
| Changed original generation | Same original object and pointer, prior cancelled epoch bound to generation 7; current shared generation changed to 8 | Old loss mandate cannot reopen recovery; rejected start causes no persistent write |

Model boundaries: native country objects, flags, arrays, dates, capital ownership/control, mission removal and event queuing were modelled.
The parent secured witness and special/nonhuman classification predicates were explicit fixture boundaries.
Protection withdrawal, mobile quote cleanup and substitute-slot cleanup were out-of-scope mocked consumers; participant cancellation, report cleanup, permanent-opt-out preservation, reconciliation-review cleanup and contract retirement were actual source.
The fixture asserts that arrays being iterated do not mutate during these closures.
This is source behavior evidence, not observed engine execution, exact tooltip rendering, timed delivery, save lifetime, or live AI proof.
The first run stopped on an unmodelled newly introduced parent contract-retirement helper; it was loaded from its actual source for the successful rerun rather than replaced by a no-op.

The source cases found and fixed a concrete settlement-report preservation issue before delivery.
Category sprite identifiers were checked against `interface/012_africa.gfx:69–70`; no new art or GUI was created.
The decision/localisation cross-reference check covered all six rows and their custom requirements/effects/getter keys.

## Reference evidence

Installed docs and offline wiki were both consulted, with exact bounded sections read.
No Paradox web page was accessed.

| Reference | Read span | Source revision / evidence |
| --- | --- | --- |
| Installed `documentation/script_concept_documentation.md`, Script Constants | 216–222 | MCP revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, section `c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0` |
| Installed `common/script_constants/documentation.md`, schema-first format | 1–34 | MCP revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`, section `48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68` |
| Installed `documentation/triggers_documentation.md`, trigger temporary arithmetic | 713–719, 6455–6464 | Revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; add-to-temp section `5ed9172318061bc267563e9860325fa452e4971395f8267f4e5068d4a1a7320d` read through MCP, multiply read locally |
| Same installed trigger docs, all-of-scopes | 1052–1066 | Same revision, MCP-read section `7e8837031971c483faf98c3f318777dbe8c6aad6fa1cd3a8a4433bdc3314f173` |
| Same installed trigger docs, state ownership/control | 5381–5392, 6088–6099 | Same revision, direct local bounded reads |
| Installed `documentation/effects_documentation.md`, country event | 2943–2969 | Revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, local bounded read; delay fields and native COUNTRY scope |
| Same installed effect docs, native array iteration and target lifetime primitives | 4296–4318, 6496–6516 | Same revision, local bounded reads |
| Installed `common/decisions/_documentation.md` | 21–46 | Revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, local bounded targeted-scope/gate reads |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 248–272, 426–446, 1076–1111, 1145–1184 | Revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`; normal actual-object refs, unscoped/caller-owned temporary lifetime, native arrays/iterators; last span MCP-read |
| Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 243–267 | Revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, local bounded ROOT/THIS/PREV/FROM read |
| Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 512–559 | Revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, local bounded target-array and native ROOT/FROM read |
| Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 656–705 | Revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, MCP-read section `8466af7164ce523520ef7e725d7711b333cc284bf7a70f0eeb7834993db17bb8` |
| Vanilla `common/decisions/ETH.txt` | 1701–1743 | Direct array-targeted native decision precedent, with `target_array`, root gate, native FROM effects; physical hash recorded below |
| Mod `common/scripted_effects/012_africa_effects.txt` | 1026–1027 | Existing duplicate-guarded relationship-array insertion precedent |
| Mod `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` | Narrow opening helper registry/API sections | Read before creating the owner-local helpers; neutral shared helpers do not implement this transaction |

`hoi4.reference_context(surface=decision, limit=12)` returned 50 installed-document files, 54 offline-wiki files, no missing/omitted sources for that request, and unavailable `script_doc` coverage.
Context source listing was followed by the detailed reads above; a bundle alone was not treated as rule coverage.
The installed trigger docs link a `script_math_expression.md` that is absent at that path; available `documentation/script_math_functions.md` was located and read for the actual native math documentation.
No meta injection is needed in this package.

## MCP evidence and precise limits

Connected live declarations expose event inspect/render/compare, decision inspect, probability inspect/evaluate/compare/render and reference context/search/read/source lookup.
The exposed source-lookup schema here has no `view` or `keyPath`; no unsupported structural paging was used.
No callable service health/version route or `hoi4.script_validate` was exposed in this worker's inventory.
No helper-expansion job, task negotiation, job route, GUI rewrite, focus inspection, or map rewrite was invoked.
There is no focus/GUI/map surface changed by these helpers.

- Pre-edit weighted inspection on the existing reconciliation row completed via `source={path:common/decisions/012_africa_gods_decisions.txt}` with its single candidate pool.
  Source revision `a22ac82b35edbec5b7856208dd86d19fe6b7b7e84cb8889b84620d0dfb8c88f3`, source hash `1692058d825b8bf3cd581548b0fc46c1662605ed5799a709f4d2cdca18863b13`, `poolComplete=true`, zero inspect unresolved, zero available without a scenario.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eb7769c3e5188779a0306f8cdf2df7679ff13715f865bd540a4d83fb17a165d/79552fe5df375afc3bbeee8d2b6abd7df22885838093b825f42cdbcf374de9b2/probability-inspect-1692058d825b.json`.
- Post-write `hoi4.probability_inspect` enumerated all six new decision rows with `poolComplete=true`, zero inspect unresolved, no parser diagnostics, and zero available without scenario bindings.
  Source revision `6837f908374dd110e30b8b73f4aca6794878ff8f5be9edcd6c32126cc7ad31c7`, source hash `a816bc23166c199afe2f09f6769707a8f1433dbd716da16725d08c8ceb457c35`.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed0d5d2de071f9f1c8980ca3b50386b9aa68ed9bd4fac9ba4453c49c52f9e442/5f323622ebe0a04d1f4051a31a16bd6c2c249eb64891a113bc47219d5c607a18/probability-inspect-a816bc23166c.json`.
  This is discovery evidence only; no balance target, runtime selection probability, or specialist comparison is claimed.
- `hoi4.event_inspect` traced `.600` at depth one, eight nodes/twelve edges: `EVENT_INSPECTED_PARTIAL`, focused mode, zero helpers, unresolved aggregate nodes.
  Source revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`, graph hash `db36826f88e04b62673db3f3908a3ef1dbcc2e27abf44c1047338abd9c5ad351`.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f382fcb0cc5368cc8023b569e68b91a08bd59d4ebb3780a07994fc65ac55321a/01df5b67ddf533be0984f4e3782ebfd9d1a9b20bcfce0a08b900b0c95715690e/event-trace-828ca59a9a1f.json`.
- Matching narrow event render completed `EVENT_RENDERED_PARTIAL`, same focused revision, two selected nodes, zero helper expansion, 42,985 omitted aggregate nodes.
  JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4966e9b6f3ce3386ec5c188a1d7e37b3ca4ea5352f176f2a862ec64fd4b257b/88a06feaa1db00351e9217b6302d7a28b9571b415934f2c0281402b64188cebd/event-neighborhood-828ca59a9a1f.json`.
  Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/149944f18fe4527b129662e81c4273db8552125c282675e4683c07edbeefe5db/ed55386c49113246518e806a48d4c5a78abc5ec013a5c488917be1e3da8d7cc1/event-neighborhood-828ca59a9a1f-manifest.json`.
  These focused artifacts do not cover the new helper closure or establish native lifecycle behavior.
- Narrow existing-decision scenario inspection completed `DECISION_ANALYZED_PARTIAL`, `complete=false`, 218 unresolved definitions, declared absent-request fixture on ETH with closed flags and unbound state.
  Revision `65792d0c5cd8d2859f5f150d5e032cec1b3eb342931114a117abacc833d56efd`.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/753c6b25dcc2fb3d9fa4e9ef6a694e94c62d9a4717a77cdbb318a4b7ab8ebb1c/2df15a9ce19cb139d2f985e42032522def3a98123d59c67ae12acdbc6c3ae4fa/decision-01c7ea309e75f42945f61a93.json`.
  It is explicitly not a fulfilled recovery scenario or an actual runtime tag binding.
- Focused `hoi4.source_lookup(gods_of_africa_cancel_participant, includeReferences=false)` completed, one definition, source revision `65792d0c5cd8d2859f5f150d5e032cec1b3eb342931114a117abacc833d56efd`, definition range then `3375–3462`, bounded returned lines `3375–3399` with continuation line 3400.
  The full relevant body and linked cleanup helpers were subsequently read locally; current line numbers changed during parent edits.

Transport/schema gaps were handled narrowly.
The probability selector's undocumented `source` shape rejected `{kind,id}` and `{decisionId}`; `{identifier:...}` returned `INTERNAL_ERROR: Unexpected internal error`.
The confirmed `{path:...}` route ultimately completed, so it is no longer recorded as wholly unavailable.
Long pending calls were observed with one-second bounded polling without escalating to job/task routes; their completed results above supersede the earlier temporary pending status.
The first compare shape `{after:{current:true}}` was rejected with `Unrecognized key: current at after`; a bounded retry omitted `after` to select the supported current-side default.
Final compare result, if returned, is appended below.

`hoi4.reference_search("arraycopy")` returned no documentation hits, and bounded local installed/offline source searches supplied no callable primitive or precedent.
This is a native array-copy documentation gap, not permission to invent syntax.
The current participant/invitation cancellation closures do not mutate their iterated roster; source fixtures assert that invariant.
Therefore this implementation does not replace a required mutating snapshot with a fallback.
If parent changes add in-loop removals, array-copy reference and snapshot validation are a prerequisite before that change.

## Completion, omissions, and parent-owned work

Completed: bounded reusable helpers, documented API, direct decision callers, typed tuning, normal request-object/identity receipts, committed mandate/history, cleanup preservation, local resume and source case evidence.
No gameplay simplifications or fallback quorum/owner policies were used.
No new art/GUI/meters/scans were required or introduced.
The full Event 012 Gods goal is not certified complete by this worker.

Pending parent integration: secured-continent witness; actual setup binder input; revoke-before-cleanup/native ordering; three guarded wake wrappers; live contract/participant/victor epoch binding; native direct timeout deadline guards; category visibility/descriptions; real activation Strength and roster rebuilding; restoration log/runtime binding; shared docs/catalog reconciliation and final review.
Pending meaningful validation: `chaosx_ai_probability_auditor` named baseline/sweep/compare, full domain MCP helper/lifecycle and integrated-decision scenarios, native consumer/queued-event/date/save lifetime acceptance.
Reason: those surfaces are parent-owned or require the queued specialist and integrated source/fixture state; focused MCP reports cannot substitute for them.
The specialist should retain same named campaign cases for scarce quorum, two-of-three consent, exact-half rejection, low stability below/at 0.35, reversal during consolidation, stale invitations, missing current authority, elapsed resume, final secured state and successor owner.
Approval/decline oscillation is a meaningful AI behavior concern to inspect without changing the assigned proposals here.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or changed.
No focus file or focus call site was viewed or edited; the existing first-proof capability was read in the shared scripted-trigger source only.

## Final artifacts and physical source receipts

The narrow event compare retry returned `EVENT_REVISION_NOT_CACHED`: `Requested event graph revision is not cached or retained as a graph artifact`.
No comparison artifact or helper-delta proof is claimed.
Parent integrated lifecycle/event comparison remains blocked on a retained graph-bearing baseline or other supported source comparison input.
The report-only focused trace/render artifacts were not converted into invented graph evidence.

The matching `.606` and `.607` narrow read-only inspections also returned `EVENT_INSPECTED_PARTIAL`, focused mode, zero helpers, the same cached revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92` and graph hash already recorded above.
These two results were obtained during the final evidence pass, after the local helper design; they do not retroactively establish pre-design per-clock inspection or current helper coverage.
Their artifacts are:

- `.606`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8b796b097d4d80c55e4bcca46d85fd0c56a7c01c2c54754536edb6c5f73a2f9/d49f54fd6978a48db688edab2b11e4c2d13a65c8c001de7cb3693cb5fe38a799/event-trace-828ca59a9a1f.json`.
- `.607`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e69a24fa304e772f6378dfced604dab2b56e795222bb091476dd63891ae603bd/cb42b2a6ba7a00aa2582f958a4c0c063ac0ea69372361d2b8258a0596fcd7f83/event-trace-828ca59a9a1f.json`.

New recovery-decision inventory returned `DECISION_ANALYZED_PARTIAL`, revision `e4bc672fe557abe235c477f9f9c5b29f3d16f594c96aacb23779806f19182423`, `complete=false`, zero scenarios, 218 unresolved definitions and failed decision-coverage validation.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cc305d2e8340300187ea042f04b44f8c9669924048dbefa8ece9e852e0c8f9b/7f9d971768b0ebc8bc124ae0103f4a5e100d5a8cfe98a79ad3c17487c9f8e3a7/decision-3827a857d0f9d6d1ed604582.json`.
It confirms an inventory was produced and does not certify live recovery eligibility, category rendering or effect execution.

Physical SHA-256 receipts are below.
MCP's semantic source hashes and cached aggregate revisions are separate from these physical file hashes.
The shared tree is concurrent; rehash dependencies before final parent review.

| Physical file | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_recovery_effects.txt` | `705f14292dce29303d636d89a594b3b2b61ef0fd1451b7811b3fd11f88986207` |
| `common/scripted_effects/012_africa_gods_recovery_effects.md` | `8b0c473dcb94fb32bd827fc67efbd5b97f9c28d993f09179c2cc917aa8cbc82e` |
| `common/scripted_triggers/012_africa_gods_recovery_triggers.txt` | `74dd82cf3c4d92a4cf4d1762768a7562d74dbf755bf22395be9601be1e9165be` |
| `common/script_constants/012_africa_gods_recovery_constants.txt` | `4fb023940ce5cb8695f849a01c9f65696e2b5f7b48ad5aa129877fa797a424cf` |
| `common/decisions/012_africa_gods_recovery_decisions.txt` | `7a24177dfaa4275dcedbb8f4132c70c0154c2df90f1768c4fb788756b4e9e36e` |
| `common/scripted_localisation/012_africa_gods_recovery_scripted_localisation.txt` | `5a6539506a819b23e0c9a72bad621781c3bc740c9c3df9245630701f387e20c7` |
| `localisation/english/012_africa_gods_recovery_l_english.yml` | `0c85fc4d68d766359ba67d1b2005658338b19271af6235cd12036c14399a2b1e` |
| Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/ETH.txt` | `a50f6aa755cf6dd619957e8ef73c196fe8a422b261a2805789426f43a373504f` |

## Parent integration continuation

The parent wires the initial grant from actual Evolution I setup and removes initialization from all three queued wake wrappers.
Every wrapper validates current permission, actual schedule receipt, and a present elapsed date before clearing or mutating anything.
Registration, native demands, ordinary reconciliation, and personal victor renewal bind the current local epoch; historical reports remain independent.
Native loss revokes before roster cleanup and preserves only existing final/victory report receipts.
A repeat loss before congress ratification invalidates invitations and approvals without inventing another loss of already revoked authority.
Frozen demand-slot release compares the local epoch as well as host ID/origin/shared generation.

The existing resume row handles a current due activation, owner, or registry obligation, at most once in the current day, without changing authority or any completion date.
This bounded extension preserves a live loop after a temporarily invalid wake instead of introducing a polling hook, new row, or new clock event.
The requirement and effect text describe continental obligations rather than private scheduler bookkeeping.

The secured-continent witness is implemented in the private epoch-binding trigger owner.
Consolidation cannot activate ordinary tribute after this witness; the existing due activation hint finalizes the retained enrolled-history census without manufacturing new participant history.
Activation and this endpoint recompute actual Strength immediately.
Actual ratification records Event 012 milestone `12209`; all six named rows retain their proposed AI tuning pending the specialist evidence pass.

Native Gods annexation cleanup runs on FROM with its explicit callback witness, independently of annexer ROOT.
It prevents reselecting an annexed original Gods owner after release.
The shared World Order host-transfer bridge still contains its separate ROOT-dependent FROM check, so shared succession/terminal acceptance remains unresolved and is not presented as repaired by this bounded cleanup.

Current integration findings and dispositions belong to `012_africa_gods_recovery_integration_audit_2026-10-04.md`; native, probability, and MCP artifact/comparison limits remain separate.

Parent source correction: the shared on-annex bridge and its two departing-host entry effects use the new ROOT-independent `africa_host_transfer_source_object_is_current` validator.
It compares the current FROM object against the authoritative host through PREV while retaining native ROOT as the annexer/resolver.
Subject release already uses its actual OVERLORD against the explicit global host, and the intentional ROOT resolver/log fields remain unchanged.
This corrects the bounded bridge entry failure; the complete inherited-ledger and native succession transaction still requires separate source/native acceptance.
The earlier unresolved-bridge note above records the pre-correction finding and is superseded for these entry gates.

The successor's existing `.232` notice supplies its own native ROOT continuation for focus loading/layout, evolution scheduling, and actual initial Gods setup, preserving annexer ROOT in the shared transfer transaction.
The actual member is captured before native subject release/autonomy commands enter host scope; those commands no longer target the annexer.
Initial due repair is visible in the host category, and former-owner local cleanup cannot zero a healthy successor's public Strength.
The first-genuine-history owner invokes the published grading initializer before contract initialization, with its consumed unscoped authorization input; retained history is not backfilled.
Final grader binding, measured payments, and deferred payouts remain separate unfinished integration.

Final bounded parent/source review resolves the remaining member-target, successor continuation, initial repair-category, Strength ownership, offender ownership and caller-scope findings.
The independent audit confirms all four native cleanup owners call the frozen offender-slot helper in participant scope.
The helper consumes only that enrollment's marker and stored owner/ID/origin/shared generation/local epoch; a current successor loses neither public Strength nor unrelated demand/offender slots.
The source tranche is ready for publication, while exact native callback, probability ranking, visual artifact, and full Gods completion claims remain open as recorded in the companion reports.
