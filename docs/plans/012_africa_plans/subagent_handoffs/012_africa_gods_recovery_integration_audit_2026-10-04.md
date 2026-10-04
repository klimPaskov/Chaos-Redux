# Event 012 Gods recovery integration audit

Date: 2026-10-04.
Disposition: bounded integration remains partial. The final R2–R6 append below is the current source disposition. Earlier sections retain review history.
This audit does not certify the Gods goal complete.
Only this audit handoff is written.
Gameplay, Git, HOI4 processes, assets, spreadsheets and other handoffs are untouched.

## Scope and acceptance

Read the full original-host recovery design and delivery handoff.
Acceptance is recorded in `012_africa_gods_original_host_recovery_design_2026-10-03.md:3–8`, corroborated by `012_africa_gods_recovery_helpers_2026-10-03.md:49–53`.
The accepted policy is an exact surviving original committed host, two or more fresh approvals forming a strict majority of the current eligible relationship pool, a Gods-only epoch, and current-permission/current-receipt/present-current-due wake hints.
The audit includes new recovery and epoch-binding source, their existing Gods integration hooks, and the narrow native loss/log dependencies needed to establish those hooks.
Separate grading, material rewards, unresolved-territory treaty logic and deferred payouts are outside this audit.
Their unfinished state is not classified as a recovery defect.
No dedicated scripted GUI, art, portrait, animation, custom 3D unit, new timer family, public meter or recurring world tick is introduced by this bounded source.

Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and the relevant acceptance/disposition and scope-control sections of `chaos-redux-improvement-loop` and `chaos-redux-event-planning`.
No skill is created or changed.

## High-value findings

### R1, source-corrected: healthy recovered epoch rejects a stale loss effect

Current evidence: `common/scripted_effects/012_africa_gods_effects.txt:3399–3418`.
The parent added a loss-proof OR before the cleanup-epoch guard.
It requires capitulation, disappearance, or actual shared-owner/terminal invalidation.
A healthy current epoch 2 now rejects the stale loss call before revocation, roster cleanup, history or public Strength writes.
Temporary loss of physical capital control alone does not make the owner-object validator false and therefore does not authorize cancellation.
A genuine epoch-2 capitulation passes, while an already-cleaned epoch 2 fails the cleanup guard.
Revocation still precedes the roster loop and there is no cancelled-flag outer skip.
These current source guard cases were evaluated in the bounded fixture pass described below.

This closes R1's healthy-current-owner case by source evidence.
Native loss timing and the full cleanup closure remain parent validation.
Keep the distinct former-object case in manual coverage: after a successor pointer replaces an old owner, local cleanup must not zero the successor's public Strength.
The core still writes global Strength at current line 3443, so this boundary must be checked if a caller permits old-object cleanup after replacement.

### R2, high: native annexation fails the host-loss bridge under foreign ROOT

Evidence: `common/on_actions/012_africa_world_order_on_actions.txt:345–366`, `common/scripted_triggers/012_africa_triggers.txt:431–439`, and `common/scripted_effects/012_africa_host_transfer_effects.txt:962–984`.
Installed vanilla `common/on_actions/00_on_actions.txt:1615–1616` explicitly identifies annexer ROOT and annexed FROM.
Both annexation branches invoke `africa_is_current_host` inside FROM.
That trigger compares the global host against native ROOT, which remains the annexer.
Both branches reject the actual annexed host.
The transfer effect also repeats the same ROOT-dependent guard.
The Gods `on_annex` block at `012_africa_gods_on_actions.txt:50–58` cleans a participant only and supplies no independent host revocation.

Manual case: native annexation of the committed Gods host without a preceding successful capitulation cleanup, with ROOT = annexer and FROM = host.
Expected: revoke the departing host before roster and global-pointer cleanup.
Current source has no successful Gods host-loss branch for that scope pair.
Parent action: repair the actual annexation caller and its callee using raw ROOT-independent departing-owner proof, without requiring healthy epoch permission after loss.
This is an existing native bridge defect exposed by the recovery integration requirement, not a newly introduced shared succession design.

### R3, medium: another loss during an open congress does not invalidate fresh consent

Evidence: `common/on_actions/012_africa_gods_on_actions.txt:29–39`, `common/scripted_effects/012_africa_gods_effects.txt:3407–3415`, `common/scripted_effects/012_africa_gods_recovery_effects.txt:51–73,102–105`, and `common/scripted_triggers/012_africa_gods_recovery_triggers.txt:52–77,118–131,155–196`.
After an earlier loss, an open recovery congress has `recovery_open` and cancellation, but no active/pending/activation-scheduled flag.
The native capitulation caller and cancellation helper therefore skip it.
Request closure exists in the revoke helper, but this path never reaches it.
The open-congress identity and member request validators do not require the host's physical return, so the old invitations/answers can remain current during that further capitulation and after its return.

Manual case: begin a congress, obtain approvals, capitulate the original host again before ratification, then restore physical control.
Expected: prior congress requests are invalidated and consent must be obtained for a fresh congress.
Current source retains the old transaction and answers.
Parent action: cover open-congress invalidation separately from authorized-epoch loss counting and roster-cleanup idempotence.
Do not invent another authority loss when that epoch was already revoked.

### R4, medium: corrected row still has an initial-consolidation category gap

Current evidence: `common/decisions/012_africa_gods_recovery_decisions.txt:80–95`, `common/decisions/categories/012_africa_gods_categories.txt:34–42`, `common/scripted_triggers/012_africa_gods_recovery_triggers.txt:309–320`, and `common/scripted_effects/012_africa_gods_recovery_effects.txt:410–434`.
The parent's explicit bounded replacement is present.
Both visible and available now use the general `gods_of_africa_recovery_can_resume` gate.
That closes the old row-level defect for active owner/registry repair.
The helper still tests the gate before its first persistent write, selects one actually due clock, preserves epoch/date/permission and existing receipt, and queues a one-day existing hint at most once per current day.
No new row, timer or AI base was introduced.

The outer host category still admits only an active host, cancelled original recovery, or committed recovery consolidation.
An initial authorized epoch-one consolidation has none of those three proofs.
It therefore cannot expose the same valid-due activation repair after a lost initial .600 delivery.
This conflicts with the parent's accepted ANY-current-authorized-due-activation repair boundary.
Current visibility fixtures: initial consolidation row true/category false, recovery consolidation true/true, active owner true/true, active registry true/true, absent current due/permission row false.

Manual case: initial epoch one is authorized and consolidating, its due .600 arrives during temporary invalid physical permission, then capital control returns.
Current activation receipt/date remain present and due.
Expected: the same existing resume row is reachable for that current activation.
Current source hides its parent category.
Parent action: extend the existing category only for the current valid-due repair gate, preserving the existing compact presentation.

The English requirement at `012_africa_gods_recovery_l_english.yml:18` also still describes elapsed consolidation and congress majority as unconditional requirements.
It remains inaccurate for active owner/registry repair.
Suggested wording: "Africa must own and control its capital and retain its current mandate. A continental obligation is due, and none has been resumed today. A renewed congress must retain its majority until consolidation ends."

### R5, medium: old-epoch demand cleanup can decrement a new epoch's live budget

Evidence: `common/scripted_effects/012_africa_gods_contract_effects.txt:174–206` and cleanup callers such as `common/scripted_effects/012_africa_gods_effects.txt:3451–3453`.
Ledger closure now uses epoch, but `gods_of_africa_release_demand_slot` validates only the frozen host object, ID, shared generation and origin before decrementing the host's current active-demand count.
It never requires the frozen demand authority epoch to match the owner's current epoch.
A stale epoch-1 contract with an unreleased slot can therefore debit healthy epoch 2 when both share the same original object and shared generation.

Manual case: owner epoch 2 has active-demand count 1, while a separate stale participant retains an active epoch-1 demand and unreleased-slot flag.
Run its neutral cleanup.
Expected: the old contract can retire locally without decrementing epoch 2's count.
Current source decrements that current count.
Parent action: use raw epoch identity for the owner budget adjustment while keeping old-contract neutral closure available after permission revocation.

### R6, medium: a continent secured during consolidation still activates ordinary Gods

Evidence: accepted design `012_africa_gods_original_host_recovery_design_2026-10-03.md:208–214`, `common/scripted_triggers/012_africa_gods_recovery_triggers.txt:277–288`, `common/scripted_triggers/012_africa_gods_triggers.txt:60–92`, and `common/scripted_effects/012_africa_gods_effects.txt:507–522,3652–3674`.
The secured witness correctly distinguishes defeat-settled from secured-settled.
New-grant gates exclude it.
An already authorized pending epoch deliberately remains permission-valid after the secured witness appears.
Neither the wake/activation guard nor consolidation readiness excludes current secured proof.
The due activation sets active authority, enrolls participants, publishes the proclamation and arms ordinary clocks.
A later owner tick can settle the system, but the ordinary activation has already occurred.

Manual case: ratify while unsecured, complete authoritative continental settlement during the 180-day interval, then deliver .600 at its current due with quorum intact.
Expected: stay closed to a fresh ordinary tribute lifecycle.
Current source opens it until a subsequent settlement path runs.
Parent action: supply an explicit consolidation endpoint for this case rather than opening an ordinary cycle.
This finding concerns recovery activation gating only, not the separate grading/reward/deferred-payout implementation.

## Status by bounded surface

| Surface | Status | Current evidence and limit |
| --- | --- | --- |
| Actual Evolution I initial binder | Source-present | `012_africa_evolution_effects.txt:27–51` reaches `012_africa_gods_effects.txt:3639–3649`, which initializes the caller token to one, authorizes epoch one, then initializes. Binder consumes the token. No wake initialization remains. |
| Three wake entry points | Source-present | Events .600/.606/.607 only delegate. Core wrappers at 3647/3674/3689 test permission, schedule receipt and present due before clearing or running work. Early/missing-date/missing-receipt returns are inert by source. Lifecycle evidence remains partial. |
| Normal authorized-epoch loss cleanup | Partial | Revoke runs before the roster loop. The outer guard no longer rejects the just-set cancelled flag. `last_loss_cleanup_epoch` permits a subsequent loss in a larger local epoch. R1's healthy-current-owner case is source-corrected. R2–R3 remain. |
| Current consent and original-host boundary | Source-present with lifecycle gap | Current relationship-array recount, minimum two and strict majority, genuine host-object validation independent of foreign ROOT, current member generation/relationship/war/exemption checks, and no successor/pointer/resolved/world-end revival. R3 remains. |
| Congress commit, history and 180-day consolidation | Source-present with endpoint gap | One local epoch increment, preserved shared generation/doctrine, separate committed mandate roster, append-only recovery history, preserved prior .608/.615 flags, current quorum recheck, and immediate real Strength refresh at activation. R6 remains. |
| Live participant/demand/review identity | Source-present | Participant binder runs after actual host-array insertion, demand binder in actual issuance, review binder at actual review start. Real object/ID/origin/epoch checks supplement actual roster and shared generation. |
| Contract tuple and native demand cleanup | Partial | Open/close/last-closed tuples include normal epoch. Neutral closure has no healthy-host requirement. Five native demand cleanup paths clear epoch after closure. R5 concerns the separate owner slot decrement. |
| Native victor proof and history | Source-present | `012_africa_gods_victor_triggers.txt:5–38` uses raw authorized epoch, real participant flag, actual roster, frozen actual host object/ID/origin/epoch and captured native defeated ROOT. No ordinary healthy permission is called after capitulation. Victory history is appended directly before exemption/cancellation. |
| Duplicate/winner attribution | Source-present | Only native FROM is passed to the recording effect. Exemption and subsequent roster cleanup reject a duplicate merged callback. No faction credit path appears in the reviewed closure. |
| Victor request and stale withdrawal | Source-present | Request stores/clears epoch, current renewal checks current permission/epoch, stale withdrawal remains accessible through category and return action. Re-entry history initialization retains an existing count/ledger and permanent opt-out. |
| Native demand/reconciliation timeouts | Source-present | Direct fail helpers at core 2910/3050 require current identity and a present elapsed current deadline before mutation. Reconciliation completion records accepted history before clearing transient epoch at 3025–3026. No durable history erasure appears in those paths. |
| Six recovery rows and category descriptions | Partial | Existing categories expose recovery/pending consolidation and current member requests. Pending member text wins before Wrath text. Rows are phase-gated, with targeted invitation using the current relationship array. The resume row is corrected, but initial epoch-one activation repair is hidden by the category under R4. Native decision presentation/target lifetimes remain parent validation. |
| Log 12209 | Source-present | Recovery commit emits at `012_africa_gods_recovery_effects.txt:341–343` after authorization/history commit. Constant is 12209. The shared description/title branches at `chaosx_scripted_localisation_events_log.txt:6758–6764,10604–10610` and English keys exist. No broad log UI edit is required. |
| AI/probability | Parent-owned pending evidence | Recovery scores remain proposals. Delivery handoff 40–42/68 assigns the pass to the already queued `chaosx_ai_probability_auditor`. No duplicate specialist or weighted job was launched. |
| Assets and dedicated GUI | Outside new scope | Reuses existing decision/category sprites. No new asset handoff or event UI worker is required by the reviewed change. Reused asset visual acceptance is not established by this audit. |
| Event docs and plan reconciliation | Stale/partial | Event documentation still describes generation-only reopening/old activation and asserts the broken annex bridge at `docs/events/012_africa/gods_of_africa.md:9–17,37`. Recovery API documentation 176–184 and delivery handoff 237 still list source-present parent integration as pending. |

## Follow-up: current resume visibility and restitution gates

This follow-up re-read the actual corrected source rather than comparing the old code frame.
Resume row visibility at `012_africa_gods_recovery_decisions.txt:82` is the general current-due helper.
Its availability uses the same helper.
The six-case category/row source matrix establishes the remaining outer-category limitation in R4.

The new private ownership predicate is at `012_africa_gods_epoch_binding_triggers.txt:63–66`.
It requires a current host target, iterates actual participant-owned states, and checks African continent plus explicit `is_core_of = event_target:africa_host`.
The pre-existing controlled-holder predicate at `012_africa_gods_triggers.txt:312–318` is unchanged.
Neither predicate computes a quantity or grade.

Host-accepted ordinary reconciliation at `012_africa_gods_triggers.txt:557–572` now rejects both predicates.
The ordinary offer and completion owners call that predicate before payment or accepted-history/authority mutation.
Victor request at `012_africa_gods_victor_triggers.txt:91–99` and current renewal acceptance at 71–88 also reject both.
An existing offer cannot bypass the recheck if the participant acquires ownership or control before host acceptance.
Stale withdrawal at 102–109 remains available independently of these acceptance gates.

Eight bounded territory source cases were evaluated across ordinary reconciliation, victor request and victor acceptance.
Ownership only, control only, both, and acquisition before acceptance are rejected.
No relevant territory, other countries' African cores, host cores outside Africa, and returned territory do not trigger this particular exclusion.
The other acceptance predicates were explicitly assumed satisfied in these fixtures.
Actual state iteration, transfer timing and native execution remain parent validation.

Terminology/coverage limit: this verifies host-accepted ordinary reconciliation.
The separately named literal Public Pardon row still calls `gods_of_africa_can_public_pardon` at `012_africa_gods_triggers.txt:790–795`, which has neither territory exclusion.
Its owner at `012_africa_gods_effects.txt:2837–2841` clears an offender mark/lowers Wrath through leniency.
It does not end defiance or victor exemption.
Do not describe that separate action as restitution-gated on the strength of these reconciliation changes.
Whether the parent's phrase "ordinary pardon" also intends that separate action is an unresolved naming/scope boundary, not invented accepted design.

English review:

- `gods_of_africa_victor_renewal_requirements_tt` at core English line 463 says "We hold none of its African core territory", which is broad enough for ownership and control.
- `gods_of_africa_victor_accept_requirements_tt` at line 469 says only "occupies no African core territory", which omits ownership without control.
  Suggested wording: "This victor has offered recognition to the present African government. Peace holds and it owns or controls none of Africa's core territory."
- Ordinary reconciliation prose at lines 429/441 describes offered reparations and reopened relations without promising that territory can be retained.
  The actual ordinary decision requirements expose both native state exclusions.
  No contradictory ordinary English claim was found in the bounded strings.
- Resume requirement text remains the R4 wording gap.
  Its updated title/description/effect text already describe continental obligations.

The read-only source lookup completed for the new ownership predicate at semantic revision `ae19cd1aefa3f04847edcf5f1a094311fe87c08542c15f5e5c353106e95b924b`.
It returned one unshadowed definition at lines 63–66 and no artifact.
Its references were incomplete with zero returned references and 18,450 aggregate unresolved reference entries.
The three direct usage gates were therefore traced locally, not inferred from zero indexed usages.

Additional direct references read: installed trigger documentation 1318–1330,1612–1624,5390–5403,6006–6018 and offline Scopes 385–394.
Their physical revisions are already in the source inventory.
No duplicate event-chain or probability job was launched.
These eligibility changes remain routed to the parent's queued `chaosx_ai_probability_auditor` for the same named baseline/comparison scenarios plus owned-only, controlled-only and acquisition-before-acceptance fixtures.

## Accepted-plan disposition

The accepted restoration design remains partially implemented.
Do not use its old `accepted and queued` heading, its contradictory earlier proposal/blocked paragraphs, or the delivery handoff's completed helper status to certify integrated completion.
The recorded acceptance at design 3–8 and delivery 49–53 controls this bounded policy.
The parent should mark implemented claims with current source and validation limits, record R1's current-source correction and retain R2–R6 plus integrated validation as unresolved/blocked or accepted and queued with a concrete reason, and reconcile the source spec or name its accepted destination.
No evidence of that recovery-spec promotion was established in this bounded review.
Catalog alignment is a parent-owned follow-up after final wording and facts are stable.
The workbook and export-only CSVs were not read or changed, so their alignment is unassessed rather than asserted missing.

## Meaningful validation and manual cases

Performed: direct source tracing of the specified recovery/epoch files and actual parent call sites, native ROOT/FROM comparison against installed on-action examples, frozen-object/epoch and closure ordering review, live quorum arithmetic/receipt review, log selector/emitter review, and repeated physical SHA-256 checks.
No full integrated source evaluator, native queue/date/save-lifetime test, AI scenario evaluation or live-game test was run by this audit.
A later bounded repair pass evaluated the actual current resume/scheduler definitions and cancellation guard in an in-memory interpreter.
Its 24 named cases passed for three current due routes, same-day duplicate suppression, future/missing-date/missing-receipt/missing-permission/foreign-ROOT rejection, lost consolidation quorum, both active clocks due, healthy epoch-2 stale loss rejection, physical-only permission loss, genuine second-epoch capitulation, duplicate cleanup rejection and disappearance.
That earlier repair-frame evaluation found activation true, active owner false and active registry false at the row.
Those row results are superseded by the parent's explicit replacement and the follow-up category/row matrix below.
Native permission, quorum and shared-owner identity predicates were explicit fixture boundaries, while arithmetic, variable/flag writes and queue recording were modelled.
No full loss cleanup, mission, actual native queue, tooltip rendering or save lifetime is certified by that pass.
The first generic loader attempt stopped on a valueless equipment token outside the tested repair path. The rerun parsed the actual bounded cancellation definition rather than mocking it.
The helper delivery's 17 source fixture groups are prior helper evidence with explicit mocks and are not reclassified as current integrated runtime evidence.
The parent reports core parsing passed.
This auditor did not rerun or independently certify that parser result.

Retain these named manual cases for the parent fix/re-review and separate MCP/native validation:

| Case | Required assertion |
| --- | --- |
| Initial actual Evo I | Caller token one, epoch one, then initialization. Repeated binder or wake never recreates revoked permission. |
| Clock matrix | For each .600/.606/.607, early current-future due, missing due, missing schedule, missing permission and former owner produce zero persistent writes/queues. An authorized old hint at current due works once. |
| Same-day duplicate owner/review | First current due wake performs current work and advances due. Second hint sees the future due and is inert. |
| Quorum boundaries | Zero/one members fail. Two of three pass. Two of four fail. Current arrivals, departures, capitulation, war and reversed answers change the live denominator/approvals. |
| Foreign member ROOT | Stored real host validates independently of native member ROOT. Wrong object/ID/origin/generation/loss/cancelled epoch fails. |
| Original-owner terminal boundary | Cleared/replaced pointer, successor consumed, resolved event, world end and final receipt all reject recovery. Defeat-settled alone does not prove secured continent. |
| Loss sequence and stale effects | Normal current epoch loss revokes before cleanup once. Epoch 2 loss works after epoch 1. Healthy epoch 2 rejects the R1 stale loss invocation. |
| Annex scopes | Actual ROOT annexer / FROM host reaches raw departing-owner cleanup before pointer change, including no-prior-cap case R2. |
| Open-congress further loss | R3 closes invitations/answers despite inactive already-cancelled authority. No artificial duplicate loss count. |
| Interrupted clocks and visibility | Corrected row repairs current owner/review receipts once per day with original due/epoch. R4 still requires initial epoch-one due activation repair to be reachable through the category. |
| Old/new contract closure | Old neutral closure remains possible after revocation, never debits new epoch budget, and duplicate close never adds another terminal result. |
| Native victor merged ordering | Each on-action order, registered actual FROM, absent roster row, mismatched epoch/object, already exempt, nonparticipant and faction ally. Exactly one raw victory/history append for the proven winner before cleanup. |
| Re-entry and personal renewal | Existing history/opt-out survive enrollment after append. Stored old-epoch request cannot grant authority. Stale withdraw remains available and grants nothing. |
| Report preservation | Pending .608/.615 survive residual/native loss cleanup only if present before it, with frozen identity retained. Absent reports stay absent. |
| Native timeout matrix | Future/missing-demand deadline and future/missing-review deadline cause no failure or metadata mutation. Current due + current epoch fails once. |
| Recovery activation | Current quorum rechecked, current Strength recomputed immediately, shared generation/doctrine/history retained, and R6 secured-during-consolidation opens no ordinary cycle. |
| Log and category phases | Only actual ratification writes 12209. No failed start/finish/resume writes it. Pending member text reads no undefined Wrath and recovery phases expose no active tribute actions. |
| Probability specialist | Scarce quorum, two of three, exact half, stability below/at 0.35, reversal/churn, stale invitation, missing permission, elapsed repair, secured endpoint and successor fixtures use the same named baseline/comparison scenarios. |

## MCP artifacts and limits

Initial tool discovery exposed no HOI4 routes.
A later refreshed inventory exposed the live event routes, so that initial route-gap observation is superseded.
The required read-only narrow inspections and renders were then performed before the parent's final repair edits for .600, .606 and .607 with no helper-expansion job, full lifecycle job, native task or source rewrite.
All inspections returned `EVENT_INSPECTED_PARTIAL`, focused mode, zero helpers, 8,983 aggregate unresolved nodes, and an inline source inventory limited to 64 of 388 paths.
All renders returned `EVENT_RENDERED_PARTIAL`, focused mode, two selected nodes and 42,995 omitted aggregate nodes.
These aggregate counts do not establish a defect in this bounded recovery change.
The focused routes explicitly defer helper/lifecycle analysis and cannot validate the integrated closure.

Shared returned semantic revision: `6b9a6428e7573efc5012d443d97c822ff503dfc95bfa7688d849b8093c88c733`.
Shared graph hash: `953f84b7e8b2fb596118e7f28ad466f155a09346e53965d72ebc77f93411ad36`.
These are separate from physical source hashes below.
These focused artifacts precede the final repair helper/guard revision and are retained as provenance, not current repair validation.
No stale-frame comparison or duplicate MCP job was performed after the parent's repair correction.
The returned summaries were inspected.
Full linked report/render artifacts were not retrieved.
The generic resource bridge rejected `hoi4-agent-tools` with `unknown MCP server 'hoi4-agent-tools'`, and the generic resource inventory listed no HOI4 resource server.
That artifact-access limit does not mean the domain event routes failed.

The bounded .600 baseline comparison used the prior helper-handoff revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`.
It returned `EVENT_REVISION_NOT_CACHED`: `Requested event graph revision is not cached or retained as a graph artifact`.
No comparison artifact or helper delta proof is claimed.
The parent needs a retained graph-bearing baseline or another supported compare input for its integrated comparison.
The specialist probability pass and native lifetime/consumer evidence remain separate parent-owned gates.


Artifact receipts:

- chaosx.nr12.600 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f102c22992fc53d75f6c1359495399f5ca8a6095d7d121642dd98df65c8e11e8/d70dd8a1fd92886812c230fd49d8f4eb08ebe44bc8162a3ea7ab66963fb08f14/event-trace-6b9a6428e757.json`.
- chaosx.nr12.600 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91a4f435aadf1df1e081e9cfc933915e5da67f00ba55993a968c827f0e71a43a/0b4367e64f6571597440dc161c335933b3a0262f7a16710452cd4c34606ba178/event-neighborhood-6b9a6428e757.json`.
- chaosx.nr12.600 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc3f9007e0bbbb0652cad7243dd306a90536358f0a283b681ef0b122007b44ff/cc668a0e1fb4af3bc0c617d950d09248efe4a81634bc2b86e481a6921de9305b/event-neighborhood-6b9a6428e757-manifest.json`.
- chaosx.nr12.606 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c7cf8080bf67bdd69390ad6270d96a49fcd9c2878377bec1d7f112d8d392e65/25d724b46fd62818faa73a0c97e8fa4bed94b520ca4153c8cc4e6baf9c53e6e3/event-trace-6b9a6428e757.json`.
- chaosx.nr12.606 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23b27017f7872a735141daed816b81acd2b36e59ba2345a0b826ab57ec197c88/283e61aff20d241dda67ad8ddf6f787991f13d99442ca034c4625176ddf23dbe/event-neighborhood-6b9a6428e757.json`.
- chaosx.nr12.606 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17b20302565f957389f08edf548171abfbea8c565624845ff5ffcb9a4c5bf51a/1230e9ce5d2b55d43b024c576546ab4552a9c1592e05d522c7749ad121875ea0/event-neighborhood-6b9a6428e757-manifest.json`.
- chaosx.nr12.607 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0b72e301e10d0b61acdaf2108c4852dbc58b43e3261d2d02794fb904c26945c/adb26ea0c3b906e6163c69a48cd2877eb434027a0beeb56125ad065a1f9dd43a/event-trace-6b9a6428e757.json`.
- chaosx.nr12.607 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71cbad4da86c483649b800226bb3b211c43ea810ee0e2eca2d48a795c852acfa/ab6ab36176d2bed279af1846c759a00f9eb1eee4bacc5014c1b7639a34947cc1/event-neighborhood-6b9a6428e757.json`.
- chaosx.nr12.607 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d1264c5638e8f39205dfdbb8c7c34fc0f0d2d8addd4947b33ebd24320f0f0d4/ed80d31c8047c7bca789359cddd245c88fb0f0ae125eb5c19ce484fafa7c0512/event-neighborhood-6b9a6428e757-manifest.json`.

## Direct reference evidence

The offline wiki and installed game sources below were read directly for the bounded rules used in this audit.
No Paradox wiki web page was accessed.
Physical revisions appear in the following hash inventory.

| Reference | Read span | Purpose |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md` | 2943–2969,4296–4318 | Country event delay and actual scope-array iteration |
| Installed `documentation/triggers_documentation.md` | 1052–1066 | Array trigger iteration and false-return behavior |
| Installed `common/on_actions/00_on_actions.txt` | 923–939,1607–1624 | Native cap ROOT/FROM and annex ROOT/FROM |
| Installed `common/decisions/_documentation.md` | 21–46 | Native actor/target decision scope and row creation |
| Vanilla `common/decisions/ETH.txt` | 1701–1732 | Actual array-targeted decision precedent |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | 257–269 | ROOT remains native root when entering FROM, real object scopes |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 426–446 | Actual-object variable assignment and caller-owned temp lifetime |
| Offline `Decision modding - Hearts of Iron 4 Wiki.md` | 512–540 | ROOT actor, FROM target, country-array targeting |

## Physical current-source SHA-256 inventory

Paths below are relative to the Chaos Redux root unless absolute.
The first bounded source frame was stable on rehash.
After the parent's repair correction, all five changed source files were re-read and reviewed as current source.
The inventory below was refreshed for that corrected frame.
MCP semantic revisions are not substituted for these file receipts.

| File | SHA-256 |
| --- | --- |
| `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_original_host_recovery_design_2026-10-03.md` | `9e5059d81116cd79a58716ea2ce49e3230df54d822c2667e26a0424bf9386576` |
| `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_recovery_helpers_2026-10-03.md` | `d5b18f2a6c131dfd9631b288a6814f39634c294c9ee264c948a6325615fd918b` |
| `common\scripted_effects\012_africa_gods_recovery_effects.txt` | `55932cb10e1a6cb021caa4b8c4d4b385755c0af18677624403b4ca1f0a29ed12` |
| `common\scripted_triggers\012_africa_gods_recovery_triggers.txt` | `47cb1edf07780af380c6f977fcc48a8075f58b0531635cead14cb6adde0bdcb4` |
| `common\script_constants\012_africa_gods_recovery_constants.txt` | `4fb023940ce5cb8695f849a01c9f65696e2b5f7b48ad5aa129877fa797a424cf` |
| `common\decisions\012_africa_gods_recovery_decisions.txt` | `cb6c0965f03b25e2d3e7a4d653edee380c1fe70c0e1791766914643124e6cfd1` |
| `common\scripted_localisation\012_africa_gods_recovery_scripted_localisation.txt` | `5a6539506a819b23e0c9a72bad621781c3bc740c9c3df9245630701f387e20c7` |
| `localisation\english\012_africa_gods_recovery_l_english.yml` | `c4bf2bfa4e5faeb2f9ca8c054b10d56e3279fa37da7b5b8f7fad3b979fc01092` |
| `common\scripted_effects\012_africa_gods_epoch_binding_effects.txt` | `cf93227cd8c9eb725b31757152984c190c2da49259e8eb12080f142c1a90cb1f` |
| `common\scripted_triggers\012_africa_gods_epoch_binding_triggers.txt` | `5afb48b7e53e2d1aa2f47fde96742add41f85c7203c94842093bdf674effb67e` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `b40adf998a11b2a27f5be8e516e1296d4a6fd3f83e96237ca05f1b6e7fccbb51` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `06e8b2f32d12427e3f475db2704c5b13f7a138923d0886aafdc07d8098676596` |
| `events\012_africa_gods_of_africa.txt` | `9130d9a956ec6ae17e03bd787be5d0177cd4021c07fea80d94f7072b5915df53` |
| `common\scripted_effects\012_africa_gods_lifecycle_effects.txt` | `82251fa4676b2ba4cf09746baac42b8cd4ee788dd2f38565fa76f601b8092e3f` |
| `common\scripted_effects\012_africa_gods_contract_effects.txt` | `4bf1c062cbb3eb1de58c006f183c90ae04f1934581b6a9d94d7095e4af1b5795` |
| `common\scripted_triggers\012_africa_gods_contract_triggers.txt` | `45b50892fb269e4c54e0fbd00b252353ad5088e957a1ef50abb60189ec323a02` |
| `common\scripted_effects\012_africa_gods_victor_effects.txt` | `ab38bb4e73ab76efc090851260dbc01ae927f88fc0f527532776d85c861cf137` |
| `common\scripted_triggers\012_africa_gods_victor_triggers.txt` | `cc394916aabbe95b58448349f9da4519ae07e35a4bed1d57acbbf4cd3e75cc88` |
| `common\decisions\categories\012_africa_gods_categories.txt` | `88272d874647ceff2596ca8c840226e6ac91e41a012dc800214a28c32aa9f581` |
| `common\scripted_localisation\012_africa_gods_scripted_localisation.txt` | `9cb1fc4d1f5dcdfba29358b8dd363c6cf9f78286de5fa50cf0478460afcec527` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `3dd3bda112a5abd035b3bf77f38a213373ea1fb1bfa54e142d5c7a83b0a5c04a` |
| `common\on_actions\012_africa_world_order_on_actions.txt` | `0a1723a4599bff187146eff6d4e61be1320b360ac504b1a7f8b9632b6813c35a` |
| `common\scripted_triggers\012_africa_triggers.txt` | `b90d5163ed5c1e4891ba49ec5eb4bbaa6b580cea2aa0a0395cec4bdc9166b4bc` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `6b752c49ea7e65ebf8c6d25f11e7c313b45a36426045325d934cf6379ef74588` |
| `common\scripted_effects\012_africa_evolution_effects.txt` | `628acb439d4d867ba0a88b28f2874b2632344fed61400b7c5bf3e5595874ac90` |
| `common\scripted_effects\012_africa_gods_recovery_effects.md` | `8b0c473dcb94fb32bd827fc67efbd5b97f9c28d993f09179c2cc917aa8cbc82e` |
| `docs\events\012_africa\gods_of_africa.md` | `bb8ca64d0499c5c2ef905bcfc364065416c9f40a6b6df5396c55730c9bbe8dec` |
| `common\script_constants\012_africa_event_log_constants.txt` | `b6183401f16c34d3336dd4ec390df0dc980c55d72f709546487c2a3c273f20f3` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `64b1355f8206e1c35d75728c46a02959706034b74eb0e1e1b8701dc7048df863` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `7fde6b681e3bd62a38eb2c01a22ffab8fc262ad2b0e37e7d0fede43c028d9b81` |
| `common\decisions\012_africa_gods_decisions.txt` | `6d6fb4a7efc3750ce15a4925ffeeb4b42a38b689a9ec345f045fd78944ecf0f0` |
| `common\scripted_effects\012_africa_world_order_effects.txt` | `6a9b793ddc2f3998394aa9909706bed61859769cc63ad09bdfe815fc228b6e7a` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\00_on_actions.txt` | `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\ETH.txt` | `a50f6aa755cf6dd619957e8ef73c196fe8a422b261a2805789426f43a373504f` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |

Additional English source receipt: `localisation\english\012_africa_gods_l_english.yml` SHA-256 `a68d86bd4cac6438e5c2b61053127d2017e613bc5df55563958c79cc48e6d45a`.

## Recommended next actions

Parent applies the remaining bounded fixes for R2–R6, then requests the same-case source re-review.
Reconcile recovery acceptance/dispositions and stale integration documentation after the source stabilizes.
The queued `chaosx_ai_probability_auditor` retains the named scenarios and performs baseline/evaluation/comparison through the probability routes.
Parent integrated MCP comparison and native validation remain separate from this source handoff.
No completion claim or unrelated expansion is recommended.

## Final bounded SOURCE re-review after owner R2–R6 patches

This append is the current disposition and supersedes earlier R2–R6 findings where marked source-corrected below.
It includes the parent's shared native-scope bridge correction and frozen demand-owner epoch correction.
Only this audit document is written.
No Git, gameplay edit, HOI4 launch, treaty review, grade/reward review, deferred-payout review or goal-wide completion claim is made.
The timing redirect was honored without another graph job or wait.

### Resolved source cases

| Item | Current source disposition | Evidence |
| --- | --- | --- |
| R2 Gods-owned annex cleanup | Source-corrected | `012_africa_gods_on_actions.txt:51–62` enters actual FROM, proves durable authority self-ID, sets the bounded native annex callback flag, cancels, clears that callback flag, and retains the annexed-original blocker. ROOT remains the annexer. |
| R2 shared entry gates | Source-corrected, old entry blocker superseded | `012_africa_host_transfer_triggers.txt:103–110` validates the current country through `event_target:africa_host = { tag = PREV }`. The two on-annex FROM gates at `012_africa_world_order_on_actions.txt:358,365` and entry gates at transfer effects 965/1024 use it. The common `africa_is_current_host` definition is unchanged. |
| R2 native role intent | Source-present | Transfer effects 969 captures ROOT as resolver. Terminal effects 1064 retains ROOT as secondary log actor, and 1067–1069 sends the terminal notice to ROOT. Global staging array copies use PREV for the iterated object, so their enclosing ROOT blocks are not themselves scope defects. |
| R3 repeated loss during open congress | Source-corrected | Native cap OR includes recovery-open at Gods on-actions 33. Core cancellation includes it both in its phase gate at 3409 and as a bypass of already-recorded cleanup epoch at 3415. Actual revoke closes requests. Loss epoch/sequence and public log sequence are deduplicated independently. Both shared transfer loss OR gates include open congress. |
| R4 row and requirement | Source-corrected, outer category still partial | Recovery decision 82 uses exactly the general current-due gate, with the same availability gate. Requirement English line 18 now says the current mandate is valid and a continental obligation is due. Initial-consolidation category access remains F4 below. |
| R5 owner slot budget | Source-corrected | Contract effects 189/199–200 require frozen demand epoch and compare it against the actual stored owner's authority epoch before decrement. Same revoked epoch can release neutrally. Stale epoch one cannot debit epoch two. |
| R5 interrupted-war owner proof | Source-corrected | Contract triggers 54/59–60 now prove the frozen owner epoch. Stale epoch-one/current-epoch-two war does not become a new adverse war outcome. The internal old tuple can still close neutrally, without active permission. |
| R6 secured consolidation endpoint | Source-corrected for the named due-hint cases | System activation trigger 63 excludes secured continent. Core .600 wrapper 3672 checks current permission/schedule/present elapsed due before clearing anything, then 3674 sends secured state to the extended preactive endpoint. Final endpoint 3566–3567 refreshes real Strength immediately before final commitment, and 3570–3575 visits retained census only when candidate-count presence permits it. Existing historical selector rejects never-enrolled candidates without prior history/generation. No ordinary activation, introductions or active clocks are dispatched in this branch. |
| Raw victor ordering/history | Source-present, no source regression observed | Native cap still captures the actual winner before cancellation. Victor source files are unchanged in this re-review. Raw native ROOT/actual FROM, authorized frozen epoch and actual roster proof remain separate from ordinary healthy permission. Direct history append still precedes exemption and cleanup. |

The shared entry repair does not establish complete shared inheritance or the full native host-transfer transaction.
The downstream failures below are distinct from the now-corrected entry gates.

### Remaining high-value source findings

**F1, high: subject release targets the annexer rather than the iterated member.**
Transfer effects 988–992 and terminal effects 1029–1033 enter each recorded subject member under native annexer ROOT.
The predicate at `012_africa_triggers.txt:997–1003` is correctly ROOT-safe through OVERLORD and the explicit global host.
The release effect at `012_africa_effects.txt:1131` still executes `end_puppet = ROOT` inside the host scope.
With ROOT = annexer 2 and member = country 3, that targets country 2 while clearing country 3's private settlement/command flags.
Manual case: normal and consumed-terminal annexation with one genuine federal/integrated subject.
Required: release that member and preserve the annexer's role.
Observed source target: annexer.
Parent action: fix the effect's actual member target without changing the intentional native ROOT role.

**F2, high: successor member-autonomy reconciliation also targets annexer/resolver ROOT.**
Transfer effects 1323 and 1370 call `africa_apply_member_autonomy_for_current_relationship` on each member.
Its two native `set_autonomy` targets at `012_africa_effects.txt:1150,1168` are ROOT.
Member metadata is written on the iterated member, while the native command targets the annexer/resolver.
Manual case: designated and congress-selected successors, with one member needing a federal/integrated autonomy change.
Required: native autonomy and metadata refer to that same member.
Observed source targets in both branches: annexer 2 rather than member 3.
Native behavior of an invalid/unintended autonomy target was not simulated.
Parent action: correct the member target and retain ROOT for resolver/log/notice work.

**F3, high when further evolutions remain: successor follow-up host gates reject the preserved annexer ROOT.**
At transfer effects 1365–1367, current COUNTRY is the committed successor while native ROOT remains the annexer/resolver.
Focus load/layout helpers at `012_africa_effects.txt:1629,1643,1655,1667` use the unchanged ROOT-dependent current-host trigger.
Evolution scheduling at `012_africa_evolution_effects.txt:148` uses `africa_evolution_clock_can_run`, whose first condition at evolution triggers 9 is the same ROOT-dependent host trigger.
The source fixture returns false with current successor COUNTRY / annexer ROOT and true when native ROOT is the successor.
The successor notice `events/012_african_union.txt:267–289` has no scheduler repair call.
The transfer already directly loads/marks the tree at 1340–1352, so this finding does not assert that no tree is loaded.
Manual case: a successful transfer before Evolution III, with no successor evolution clock yet armed.
Required: the new owner's continuation actually schedules its clock.
Parent action: supply a successor-owned continuation or appropriate object-scoped follow-up gates while retaining intentional annexer ROOT roles.
Other native repair hooks and complete inherited state remain unassessed.

**F4, medium: valid initial epoch-one activation repair remains hidden by the category.**
The corrected row is visible, but `012_africa_gods_categories.txt:34–42` still admits only active authority, cancelled-original recovery, or committed recovery consolidation.
An authorized initial consolidation has none of those category proofs.
Manual case: initial .600 delivery is lost during temporary invalid physical permission, then the original current owner regains control with its existing due receipt intact.
Required: the same current-due repair row is reachable.
Observed source: row true, category false.
Recovery consolidation and active owner/registry repair are reachable.
Parent action: cover the current valid-due repair gate in the existing category.

**F5, conditional stale-owner case: local loss cleanup can zero a successor's public Strength.**
Core cancellation deliberately allows an invalid former-owner object to clean local state.
At `012_africa_gods_effects.txt:3446` it still unconditionally writes `global.gods_of_africa_strength = 0`.
A departing former object with residual active state and an unconsumed cleanup epoch passes this local cleanup under native annex proof even when the current authoritative pointer identifies a healthy successor.
The source guard/global-write fixture has FROM owner 1, current owner 9, durable self-ID 1 and successor Strength 80.
The cleanup branch is accepted and the unconditional global write resolves to zero.
This is the previously recorded former-object cleanup boundary, not a claim that a correctly completed transfer necessarily leaves residual active state.
Manual case: that stale former-object callback must clean only its owned state and preserve successor Strength.
Parent action: scope the public Strength write to the actual current owner, while preserving local cleanup after pointer loss.
Full participant-cleanup scope consumers were not executed in that focused case.

Minor remaining wording: core English line 469 still says a victor "occupies no African core territory", omitting ownership without control.
Its acceptance gate rejects both.
Use "owns or controls none of Africa's core territory".
The general resume requirement is corrected.
The literal Public Pardon action remains a separate offender-mark leniency path and is not certified restitution-gated by the reconciliation checks.

### Source fixtures and limits

The 18 bounded current Gods fixture groups completed:
- native annexer ROOT host FROM.
- annex callback self-ID mismatch.
- released annexed original cannot recover.
- recap open congress after same epoch cleanup.
- genuine epoch two loss and duplicate.
- healthy epoch two stale loss inert.
- stale one versus healthy two.
- current revoked neutral release.
- current healthy release.
- current zero budget.
- first consolidation secured no actors.
- first consolidation census but never enrolled.
- recovery consolidation retained historical actors.
- secured endpoint early.
- secured endpoint missing due.
- secured endpoint missing schedule.
- secured endpoint missing permission.
- secured endpoint lost recovery quorum.

The 15 shared entry/frozen-owner checks completed:
- normal source FROM under annexer ROOT.
- consumed source terminal under annexer ROOT.
- shared source rejects wrong pointer.
- shared source rejects missing generation.
- shared source rejects missing commit.
- shared source rejects inactive event.
- shared source rejects missing target.
- annexed native object need not pass exists.
- normal resolver capture retains ROOT.
- terminal secondary actor and notice retain ROOT.
- frozen same epoch revoked owner proof stays valid.
- frozen old epoch versus new epoch owner proof rejects.
- old internal tuple neutral closure still available.
- old epoch current war does not become war breach.
- revoked same epoch current war remains attributable.

These are source-model checks.
Actual callback bodies, cancellation/revoke/request closure, slot release, .600 wrapper/final endpoint/owner cleanup, historical selector, shared entry predicates, target tokens, evolution gate and frozen-owner/internal-tuple predicates were evaluated.
Native physical return, secured witness, quorum, war relationship and supplied country-object state are declared fixture inputs.
Full participant cleanup, victor capture, numerical Strength calculation and economic/grade/payout consumers were explicit mocks or excluded consumers.
No native execution, event delivery lifetime, save lifetime, autonomy result, payout result or native visual acceptance is claimed.
F1–F3 and F5 are observed source-invariant failures, not additional passed acceptance cases.
No large native scenario fixture was launched.
Complete shared transaction/inheritance and parent-native cases remain validation gaps.

### Evidence routes and documentation

Parent-provided .600 source lookup: one unshadowed definition at `mod:events/012_africa_gods_of_africa.txt:13–20`, revision `669a9ad00120f961896461aba9dcc8fff61f7ed2611a7d0578a3718284e7089d`, with immediate delegation only.
Parent-provided .600 trace/render: focused partial revision `f04d3e8...`, zero helpers, zero selected nodes and artifact manifest ending `32603`.
Those supplied records are not helper or native visual acceptance.

Before the timing redirect, the auditor's narrow .230/.233 inspect/render calls completed focused partial at revision `f04d3e8b171882e6063d871273ef0049f645e58d09abedf8b4933b34a4507c8a`.
They reported zero helpers, 8,984 aggregate unresolved nodes, and render two selected nodes with 42,996 omitted nodes.
The narrow .230 comparison returned `EVENT_REVISION_NOT_CACHED` for the previously retained revision.
No comparison artifact was produced.
No duplicate global-graph wait, helper expansion or full native job remains part of this final re-review.
The linked full artifacts were not retrieved through the unavailable generic HOI4 resource bridge.
The parent's integrated helper/native validation and queued `chaosx_ai_probability_auditor` remain separate required evidence.
Source fixtures are not substituted for them.

Direct native references additionally read: installed effect docs 3662–3674 and 6586–6617, and offline Effects 1440–1447.
They establish that end-puppet/autonomy commands act on their explicit target.
The shared current-host trigger at 431–440 is unchanged with physical SHA-256 `b90d5163ed5c1e4891ba49ec5eb4bbaa6b580cea2aa0a0395cec4bdc9166b4bc`.
The focus-tree skill was used only for the bounded existing settlement caller and successor focus-call boundary, without a full tree/AI/layout audit.

Current parent event guide lines 208–229 records the Gods-only epoch, native FROM annex proof, shared PREV object bridge and epoch-protected slots.
The old shared entry-gate blocker is superseded.
The recovery helper API still describes activation-only resume at rows 34/89, so that API wording needs reconciliation with all-clock repair.
Accepted recovery design remains accepted and partially implemented, with source-corrected claims above, remaining F1–F5, documentation alignment and explicit validation gaps.
No assets, dedicated GUI, catalog, treaty or payout completion is inferred from this bounded pass.

### Current physical SHA-256 receipts

The sources below were rehashed for this append.
The final native Gods on-action re-read changed only whitespace relative to the semantic fixture frame.
No Git revision is claimed.

| File | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `151c914f6e1bb28ea1f62dcf86d9ba20672619d8b867753dd9b9cdeb0d08c14d` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `f81df99fab3159791f03d60b2c05447b9ca2dfb49907156f8606e5977646be24` |
| `common\scripted_effects\012_africa_gods_contract_effects.txt` | `3067b25ebf00d0f36a28967d9ca047e07ba3a8e48704cbecb55fce220c4fcdfd` |
| `common\scripted_triggers\012_africa_gods_contract_triggers.txt` | `7ede23a1a12fdd6b5e88b15420596f6cc10ff6af9a5b54f3083778292712c34f` |
| `common\scripted_triggers\012_africa_gods_recovery_triggers.txt` | `3664ab41fa1bfc62eca631c5e1618cfa94e3e3dda7568d0c749c816e5e34369c` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `98992adb8164679ef28d094ab3b716a4a08eaf00e67bdc41ecc672a70109a51d` |
| `common\scripted_effects\012_africa_gods_recovery_effects.txt` | `55932cb10e1a6cb021caa4b8c4d4b385755c0af18677624403b4ca1f0a29ed12` |
| `common\decisions\012_africa_gods_recovery_decisions.txt` | `cb6c0965f03b25e2d3e7a4d653edee380c1fe70c0e1791766914643124e6cfd1` |
| `common\decisions\categories\012_africa_gods_categories.txt` | `88272d874647ceff2596ca8c840226e6ac91e41a012dc800214a28c32aa9f581` |
| `common\scripted_triggers\012_africa_host_transfer_triggers.txt` | `4b14a938144c2df1d40006b24ed44d5b66a6c1ce5d426863fe56752811ee0fb2` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `77a61cd5f0bc5b6c6feb06b8d3813c0f48d442fd01f354f0b8852c76f214c829` |
| `common\on_actions\012_africa_world_order_on_actions.txt` | `22696497548c867a86db190586010ed97cca8ac9fb5cd84d7b5b2c7c8ca0a9f2` |
| `common\scripted_effects\012_africa_effects.txt` | `67a0c2fab984a0613e905f721123b05dca0e1fa8539a201797192c7eaee0b5ff` |
| `common\scripted_triggers\012_africa_triggers.txt` | `b90d5163ed5c1e4891ba49ec5eb4bbaa6b580cea2aa0a0395cec4bdc9166b4bc` |
| `common\scripted_triggers\012_africa_evolution_triggers.txt` | `f55c635a3b5d611a92bb42d7798b2522d47dddf65914c3f60e41296cf4e33946` |
| `common\scripted_effects\012_africa_evolution_effects.txt` | `628acb439d4d867ba0a88b28f2874b2632344fed61400b7c5bf3e5595874ac90` |
| `events\012_african_union.txt` | `9627bed4f2f1aa5527c88d86cdf1c81b412446218574e0153d36cc02d5891401` |
| `localisation\english\012_africa_gods_recovery_l_english.yml` | `15d9907e49a9d5a34ee988bee0198c4fe2e236a3d8c133cdfaa080ce96072df6` |
| `localisation\english\012_africa_gods_l_english.yml` | `a68d86bd4cac6438e5c2b61053127d2017e613bc5df55563958c79cc48e6d45a` |
| `common\scripted_effects\012_africa_gods_victor_effects.txt` | `ab38bb4e73ab76efc090851260dbc01ae927f88fc0f527532776d85c861cf137` |
| `common\scripted_triggers\012_africa_gods_victor_triggers.txt` | `cc394916aabbe95b58448349f9da4519ae07e35a4bed1d57acbbf4cd3e75cc88` |
| `common\scripted_effects\012_africa_gods_settlement_effects.txt` | `0d636486d9a49ac7d6107b95e02cd2d4a5df4334f2b349a8496361b0f2781046` |
| `common\scripted_triggers\012_africa_gods_settlement_triggers.txt` | `f56c45b8813807be97f69f72af3ea05e97cbffc7529febd4a19c8856f3dfd4d1` |
| `events\012_africa_gods_of_africa.txt` | `9130d9a956ec6ae17e03bd787be5d0177cd4021c07fea80d94f7072b5915df53` |

The parent should address the bounded remaining scope/visibility/ownership findings, then request these same cases for re-review.
No goal-completion claim is recommended.

## Latest F1–F5 manual SOURCE verdict

Verdict: F1–F4 and F5's direct public-Strength write are source-corrected.
One concrete F5 downstream ownership defect remains, so this is not an all-clear source verdict.

Resolved current cases:

- F1: actual member is saved before entering host scope at `012_africa_effects.txt:1129`. Native end-puppet targets that regular member target at 1132.
- F2: the same capture precedes autonomy dispatch at 1141. Federal/integrated targets at 1152/1170 are the actual member, preserving annexer ROOT. A second member refreshes the regular target.
- F3: existing .232 immediate at `events/012_african_union.txt:281–288` runs the four owner helpers under native successor ROOT, guarded by current host, successor mandate and consumed successor proof. Foreign ROOT, absent mandate/consumption and replaced pointer reject that continuation.
- F4: category OR at `012_africa_gods_categories.txt:37` now admits the current valid-due repair gate, so initial consolidation repair is reachable. The row and same-day/current-permission/current-receipt/current-date constraints remain as previously reviewed.
- F5 direct Strength: `012_africa_gods_effects.txt:3446–3449` now writes public Strength only when the country object equals the actual global host, independently of annexer ROOT.
- Victor acceptance English at line 469 correctly says "owns or controls".
- The small first-enrollment hook at `012_africa_gods_lifecycle_effects.txt:12–15` matches the published initializer contract: caller temp one, grading initialization before contract initialization and history count. The first-no-issued guard is satisfied in that order. Retained count, including zero, or retained history marker skips the branch. Existing registration assigns original identity afterward at core 335–340. No standing-alias, grade, quantity, treaty or payout implementation is reviewed or certified here.

Remaining F5 defect:

The departing owner's loss loop still calls participant cleanup unconditionally at core 3423–3425.
The preservation wrapper invokes `gods_of_africa_cancel_participant` at recovery effects 239.
That helper's enemy-marker branch at core 3474–3485 decrements `gods_of_africa_priority_offender_count` on `event_target:africa_host`, which may now be the successor.
It does not validate that the counter owner is the participant's frozen old authority object/epoch.

Exact existing stale-owner case: old owner 1 has a residual row for participant 3 still bound to owner 1/epoch 1 and carrying its old enemy marker.
The current global host is successor 9/epoch 2 with its own positive offender count.
The new Strength guard correctly preserves successor Strength, but participant teardown still decrements successor 9's offender count.
The source-model traversal observed count 5 becoming 4.
The same branch applies to a valid positive count of 1, incorrectly making it 0.
Expected: old-object cleanup closes only its owned participant state/counters and leaves the successor's counter unchanged.
Parent action: bind this counter decrement to the frozen participant/departing owner identity rather than the replacement global pointer, without requiring healthy permission after loss.

Fourteen current targeted source checks completed for member capture/targets, refreshed next-member target, no repeated native autonomy dispatch when already current, .232 role guards/dispatch, category reachability and Strength-owner gating.
The old-participant counter case remains a failed ownership invariant.
Other participant consumers and owner-helper internals were explicitly mocked in that focused source traversal.
No native runtime, full transfer, full grading/payout, source-wide completion, new MCP job or wait is claimed.
All earlier MCP partial/unavailable provenance remains retained.

Current SHA-256 receipts:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_effects.txt` | `d679a31fa1ffcf610ca6eba05afb4fcab0b41aa9cc08751fb065b108ca2a8bc8` |
| `events/012_african_union.txt` | `b9e7df4ac87feb5bb789deb49ed3fd261a0782ef4d6f84281acc1e0e49c722ee` |
| `common/decisions/categories/012_africa_gods_categories.txt` | `dc1b56ccff54a4c6ee6de8a7aa44448f901b99a936d733c1a05687284d49731c` |
| `common/scripted_effects/012_africa_gods_effects.txt` | `3b92fe8a8db0111a4882d94abf951f7ca9c6c50f537a4541884bc12424c12a56` |
| `common/scripted_effects/012_africa_gods_lifecycle_effects.txt` | `4f59f78944f5707f58128f22b61a61018c7e3aa310ad1dd75119dfeb77a39f86` |
| `localisation/english/012_africa_gods_l_english.yml` | `32d85f7049bbb0de167a56a8af4c90dc05c370cfd19060496ef474200b656305` |

Only this report append is written.

## Offender-release F5 follow-up

The new `gods_of_africa_release_owned_offender_mark` at epoch-binding effects 55–86 fixes the requested owned-slot release cases by source evidence.
It consumes the actual marker before validating the stored real owner and ID/origin/shared-generation/epoch tuple.
It does not require active permission.
Six bounded source cases passed: old owner 1 preserves successor 9's count, matching revoked owner releases its own slot, duplicate no-op, advanced epoch rejects old debit, wrong ID rejects debit, and missing owner consumes only the marker.

One concrete caller defect remains.
`gods_of_africa_clean_participant` invokes the participant-scoped helper inside `event_target:africa_host` at core 3171.
Archive at 405, finalize at 3274 and cancel at 3435 correctly invoke it in participant scope.
The clean caller passes the host country instead.
For an actual marked participant, that host normally has no enemy marker, so the helper does nothing.
The later participant marker clear then erases the receipt without releasing its frozen owner's counter.
The source fixture confirmed that the participant marker and old owned count remain untouched when this helper is invoked in the host frame.
This also leaves a phantom offender count during normal current-owner participant cleanup, without requiring a stale callback.

Required bounded correction: invoke the helper in participant scope before entering the host block.
The helper itself needs no ownership-policy change for the reviewed cases.
Verdict: requested helper cases are source-corrected, but F5 is not source-clear until this clean-participant call scope is corrected.
No native execution, unrelated cleanup, grading/payout review or additional MCP job is claimed.
Only this report append is written.

Current SHA-256:
- Core Gods effects: `d3bf373dd9a390aeebeee5467ba0615715469eb9ea4c47d6761bae105af6de10`.
- Epoch-binding effects: `00132b89309640cf9bfa0f4a86605eeb0b910b78b61cabf18c5c3c4a217a2908`.

## Final offender caller-scope verdict

Bounded SOURCE verdict: ready for the reviewed F1–F5 cases.
The last F5 caller-scope defect is resolved.

The current clean-participant entry at core 3160 calls `gods_of_africa_release_owned_offender_mark` first, in participant COUNTRY scope, before the host block.
An AST traversal of each complete current caller found exactly one call, with no enclosing host/variable/ROOT/FROM scope switch:
- Archive: core 405, participant scope.
- Clean participant: core 3160, participant scope.
- Finalize: core 3275, participant scope.
- Cancel: core 3436, participant scope.

Native cap invokes clean on participant ROOT at Gods on-actions 46.
Native annex invokes clean on participant FROM at 68.
The source-loss participant loop enters each participant before the receipt-preservation wrapper calls cancel.
Thus these entry routes reach the offender helper in the required actor scope.

The helper is byte-identical to the version used for the six executed bounded source cases.
Those cases retain old-owner-1/successor-9 isolation, matching revoked-owner release, duplicate no-op, advanced-epoch rejection, wrong-ID rejection and missing-owner marker consumption.
No additional unexpected scope defect was found in these requested helper/caller cases.
Earlier failed clean-caller and counter-pointer findings are superseded by the owned helper plus corrected caller placement.

Current SHA-256:
- Core Gods effects: `58762bde4768ec0f1340996883550121a5f2bf74c67950fec3de1746b0cf0db0`.
- Epoch-binding effects: `00132b89309640cf9bfa0f4a86605eeb0b910b78b61cabf18c5c3c4a217a2908`.
- Native Gods callbacks: `f81df99fab3159791f03d60b2c05447b9ca2dfb49907156f8606e5977646be24`.

Only this report append is written.
No MCP job/wait, Git operation, gameplay edit, HOI4 launch, native-runtime pass, full transaction/inheritance claim or goal-wide completion claim is made.
All prior validation limits remain recorded.





### Completed narrow transfer artifacts

These are focused provenance artifacts, not helper or native transaction acceptance.

- chaosx.nr12.230 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a15fb220c9f79b2d7e98c9406bcacd56160a3e7f2ab2fb6520c7ba01e5b5abd/bfbb7020883fc1993f63d018adc1a006aa8d54979f6a09bfe6c9b1f9207a2e89/event-trace-f04d3e8b1718.json`.
- chaosx.nr12.230 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1a8701ee6294d06286f54db1da9af235d4bb063957b7eeb20c0ec7e22bfc005/75aa7803788d9aea47c246a026c193f0e1b0268c2ef064ffa13a2570e750904b/event-neighborhood-f04d3e8b1718-manifest.json`.
- chaosx.nr12.230 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12f3f8c7b39e42619108a7589807992fc04415090a05ac6baef99a45aeef2ed8/7fb025ac4f62a969b59fc2e39d10784ac3982e6990187506c1a4ce002f509d19/event-neighborhood-f04d3e8b1718.json`.
- chaosx.nr12.233 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f13a80a8c164a06d2168a51b4381b6f4c37aaa82417cf97fafcb228ab3e28262/35445af196b2902c456a9a175442485c12714b0fee6f93320abfd51633348207/event-trace-f04d3e8b1718.json`.
- chaosx.nr12.233 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48da957c1c44df535057641e4bc42d2c2adb981c5b73362f5c82ed871c0a0b61/3a58fb697d0b7848dc0a189a3a8ad7e6238c154e7e9833064bdc2f6671f9bfa7/event-neighborhood-f04d3e8b1718-manifest.json`.
- chaosx.nr12.233 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b90fd8fef507fd8c7337917e942da2872ee806799e3771b7b5112c4ebab3e9b6/a79887d7c77f7a7a119a4213aca7cf62a624e6c4c6ae41688998c3ce75b59781/event-neighborhood-f04d3e8b1718.json`.
