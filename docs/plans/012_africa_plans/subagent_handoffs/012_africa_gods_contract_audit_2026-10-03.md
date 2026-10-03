# Event 012 Gods unique-contract audit

Requested filename date: 2026-10-03.
Final source read: 2026-10-03 21:01 UTC, which is 2026-10-04 locally.
Role: read-only event completion auditor.
Disposition: bounded audit delivered for parent review, unique-contract tranche partial with the source defects below.
This is not a Gods completion claim or native execution claim.

## Scope and acceptance

The parent authorized review of `common/scripted_effects/012_africa_gods_contract_effects.txt`, `common/scripted_triggers/012_africa_gods_contract_triggers.txt`, `common/script_constants/012_africa_gods_contract_constants.txt`, and their hooks in `012_africa_gods_effects.txt` and `012_africa_gods_lifecycle_effects.txt`.
Existing decision gates, registry, settlement, capitulation, and victor owners were read only to establish these exact call contracts.
No gameplay source, localisation, asset, spreadsheet, skill, Git state, or game process was changed.
The only audit write is this handoff.
Git was not used, so supplied working-diff size and baseline commits are not independently verified.

The acceptance basis is the parent's explicit bounded assignment and the recorded parent acceptance at `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_full_grading_rewards_design_2026-10-03.md:4-7`.
Its contract requirements at lines 61-144 are accepted design for this audit.
Lines 220-222 clarify that successful reconciliation may reset the current recovery streak and explicitly post-reconciliation fields while retaining lifetime outcomes and longest streak.
The recommendation is to correct the bounded issues below and repeat the affected source cases before committing this tranche.
No further design expansion or approval input is needed.
The parent retains implementation, acceptance promotion, integration review, and commit ownership.

Separate grading, paid-contribution, material reward, conduct, and recovery workers remain outside this audit.
Their unfinished work is not classified as a defect here.
The accepted grading plan remains accepted and queued for the wider parent-owned work, with this contract portion partially implemented.
This audit does not promote that plan to implemented or to an accepted spec.

## Status by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| First genuine contract history and retained lifetime counters | Finished in source | Lifecycle lines 6-13 invokes contract initialization before creating `history_count`. Existing history flag or even a zero-valued history field blocks new initialization. Cleanup does not zero these contract counters. |
| Immutable origin/owner proof on terminal ledger closure | Finished in source | Contract triggers lines 4-20 require owner `THIS.id`, immutable history origin, demand ID/generation, open flag, and no consumed receipt. Neutral closure needs no active host. |
| Unique issuance and current-contract opening | Partial | Open flag and last-closed tuple block ordinary repeated opening. Active peaceful future-deadline guard is present. D1 covers missing immutable history ownership checks. |
| Full and honored-substitute terminal closure | Partial | One-use fulfillment authorization is present and consumed before terminal counts. Failed substitution restores the original native family/mobile type/balance and does not rewrite the ledger's original family. D5 covers caller validation and write order. Actual measured delivery remains the separate contribution owner's scope. |
| Nonterminal partial followed by full | Finished in source for valid identity | Partial leaves the ledger open and changes no unique terminal count. Later full closes the same tuple once. |
| One-unit terminal partial | Missing reachable implementation | D2: strict less-than affordability excludes the equality case before the zero-balance closure branch. |
| Refusal, defiance, expiry, and war closure | Partial | Ordinary owners choose their explicit adverse enum before generic cleanup. Expiry checks the current stored deadline. D4 covers the victor/host-loss race and D5 covers receipt order. |
| Archive, host-loss, finalization, and generic cleanup | Partial | Neutral closure is host-independent and final classification retires inside its one-use guard before snapshots. D3 and D4 remain. |
| Host-accepted ordinary reconciliation and helper replay | Partial | Paid-offer sequence is consumed before counting, including direct repeat before flag cleanup. D1 covers immutable owner/origin validation and zero-sequence acceptance. |
| Documentation | Partial | The helper contract exists. Its last-unit partial claim is contradicted by the current affordability trigger. |
| MCP lifecycle and revision comparison proof | Blocked/limited | Focused event trace/render omit helper lifecycle analysis. Cached-revision comparison and artifact retrieval failed as recorded below. |
| Visual assets, dedicated GUI, portraits, country packages, focus trees, catalog | Outside scope | Private receipt fields introduce no asset requirement. This is not a goal-wide presentation or catalog audit. |
| Weighted AI/probability | Outside scope | The three new ledger files contain deterministic receipt/counter logic. No weighted expression or balance target is audited or changed. Existing decision weights and punishment selection remain with their owners. |

## Source defects and concrete cases

### D1. Opening and accepted reconciliation lack the immutable history identity gate

Priority: high for the requested missing/wrong-identity fail-closed contract.
`common/scripted_effects/012_africa_gods_contract_effects.txt:32-57` checks initialized contract history and a current native demand, but neither requires `history_owner_id = THIS.id` nor proves the current host origin equals durable `history_origin_host_id`.
The reused current-demand predicates at `common/scripted_triggers/012_africa_gods_triggers.txt:163-179,199-246` validate live membership and generation, not these durable identities.
Opening can therefore increase issued and create an origin receipt that the stronger closure trigger will subsequently reject.

Case: keep an otherwise valid live participant/current demand and initialized contract history, but remove its immutable history origin or give it a different owner/origin.
Opening still writes an issued receipt.
Closure rejects it without touching last-close or terminal counts, leaving an accounting gap if a caller then clears the native demand.
Registration at `012_africa_gods_effects.txt:337-342` fills missing fields but preserves conflicting existing fields, so registration does not establish the missing predicate for every caller.

The accepted-reconciliation helper at contract effects lines 141-163 has the same durable identity omission.
Its ROOT host check and `participant_can_reconcile` at core triggers lines 551-562 establish current live permission, not immutable history ownership/origin.
Case: a valid paid pending offer, an increasing sequence, current participant generation, and the true host as ROOT still increment reconciliation and reset recovery fields when durable history owner/origin is absent or wrong.
Also, a zero sequence with no last-accepted field passes its current OR branch, although genuine paid issuance advances the sequence from zero to one.

Recommended owner correction: validate the durable participant owner and matching history/current-host origin before opening or accepting, and require a positive genuine paid-offer sequence.
Preserve the existing replay receipt and avoid inventing history for missing receipts.
The closure helper's newly added immutable identity proof is verified and is not reported as missing.

### D2. Terminal one-unit partial cannot reach its closure branch

Priority: medium.
`common/scripted_triggers/012_africa_gods_triggers.txt:979-988` requires `partial_payment_amount < demand_remaining`.
`common/scripted_effects/012_africa_gods_effects.txt:2036-2039` applies that gate before transfer.
The new authorization and terminal close at lines 2067-2073 run only afterward when remaining is zero or less.

Case: frozen partial amount 1, remaining 1, sufficient capacity, valid future deadline, and no cooldown.
The less-than test fails, so no payment, authorization, fulfilled receipt, or mission cleanup occurs.
More generally, a positive balance and strictly smaller payment cannot reach zero after the current subtraction.
Partial 5 from balance 10 followed by ordinary full 5 works, but does not satisfy the explicitly requested terminal one-unit partial case.

Recommended owner correction: permit the exact remaining amount without allowing overpayment, and trace both equality and greater-than rejection through the existing resolver.
Align `common/scripted_effects/012_africa_gods_contract_effects.md:29` with the resulting reachable behavior.

### D3. Generic cleanup can decrement a replacement host's unrelated active count

Priority: high for the specifically requested cleanup isolation check.
`common/scripted_effects/012_africa_gods_effects.txt:2264-2278` now requires PREV's actual `demand_active` flag, which correctly fixes cleanup of a participant with no active demand.
It still subtracts from the current shared `africa_host` whenever that host's count is positive, without comparing that host to the demand's generation/origin.
Archive has the equivalent count mutation at lines 424-433.

Case: participant retains an active generation-7/origin-A contract, shared `africa_host` has changed to generation 8/origin-B, and B has one unrelated active demand.
The host-independent receipt may neutrally retire the old A contract, but `clear_demand` or archival also decrements B's count from one to zero.
No active-host requirement should be added to neutral retirement itself.

Recommended owner correction: isolate host-count mutation to the host generation and origin that owns that demand, retaining the PREV active flag check and allowing local retirement after authority ends.
This is a source-helper counterexample, not a claim that a particular observed game session traversed this state.

### D4. Victor capture followed by host-loss cleanup can retire an adverse open war contract

Priority: high for accepted plan lines 135-137 and the explicitly requested victor-cleanup review.
`common/on_actions/012_africa_gods_on_actions.txt:20-39` captures the capitulation victor before unifier-loss cleanup.
The other Event 012 callback also captures first at `common/on_actions/012_africa_world_order_on_actions.txt:504-511`.
`common/scripted_effects/012_africa_gods_victor_effects.txt:34-62` records the winner and sets victor exemption but does not close an outstanding tribute contract as war-broken.
Host-loss at `012_africa_gods_effects.txt:3368-3381` invokes `cancel_participant` for the roster, whose first action at lines 3410-3411 is unconditional neutral retirement.
The normal adverse war owner is called by the bounded owner tick at lines 116-124.

Case: a proven participant has an open demand, enters war with its host, and capitulates that host before the next owner cancellation pass.
Capture preserves the real victory, then cleanup writes retired rather than broken-by-war and leaves the compliance streak unchanged.
The same contract is removed from the final denominator despite actual adverse participant war.
After victor exemption, the ordinary current-generation predicate also rejects that participant, so merely calling the ordinary war helper later is insufficient.

Recommended owner correction: use the proven defeated-host/callback identity to close the outstanding matching contract adversely before victor exemption or neutral cancellation can consume it.
Keep other nonoffending participants' host-loss retirement neutral and retain the victor records.
The existence and frequency of the inter-tick race are not native-tested here.

### D5. Canonical terminal owners write closing history before receipt validation/consumption

Priority: medium for accepted receipt-order fidelity, high if malformed identity is reachable at these entry points.
Accepted plan line 111 requires the closed receipt before closing counts or history writes.
In full resolution, `012_africa_gods_effects.txt:2016` writes closing history before fulfillment authorization and closure at lines 2026-2029.
Refusal writes history at line 2858 before closure at lines 2872-2873.
War and expiry owners have the same sequence in `gods_of_africa_cancel_demand_for_war` and `gods_of_africa_fail_demand`.
The terminal partial branch likewise follows its earlier partial-history write.

Case: native current contract remains valid but immutable ledger owner/origin is wrong or the live ledger tuple differs from native demand identity.
The full/refusal/failure owner can modify payment or Wrath/history before the terminal helper rejects closure, then generic cleanup removes the native demand.
The stronger helper therefore fails closed for unique counts but does not make the complete source call contract fail closed.

Recommended owner correction: validate the new ledger identity before terminal owner mutations when new contract history exists, and consume the terminal receipt before the closing history write.
Retain the distinction between legacy history without receipts and a genuine new ledger with malformed identity.
Do not backfill old unique outcomes and do not let this audit choose contribution-transaction behavior.
The first-refusal punishment safety comment at core effects lines 2854-2856 concerns the coarse history counter and should be preserved when ordering the new receipt.

The terminal helper itself does not stamp last-close early.
At contract effects lines 66-76 it validates identity, close kind, and fulfillment authorization before lines 78-85 consume and stamp the receipt.
An old generic `payment_success` value alone cannot authorize direct full closure in the reviewed source.

## Cases traced from current source

These are manual source-path cases, not a native scenario run or an executable fixture suite.

| Case | Source result |
| --- | --- |
| First genuine enrollment without history marker/count | Initializes contract counters before the history field, once. |
| Existing coarse history field equal to zero, no new receipts | Sets existing-history marker and does not initialize/backfill contract counters. Migration evidence remains unavailable. |
| Re-entry/archive/host-loss with existing contract counters | Counters and longest streak survive. |
| Repeated opening while ledger open | Issued remains unchanged on the second call. |
| Immediate reopen of the last consumed tuple | Last-closed origin/generation/ID prevents issuance. Older forged identity rewinds are not an audited supported caller. |
| Expired demand or participant already at war, direct opening | New current-demand gate rejects opening. |
| Wrong/missing closure owner, origin, demand ID/generation, or invalid kind | Closure changes no terminal counter or last-close receipt. Caller-side limits are D1/D5. |
| Direct full close with old payment_success but no authorization | Rejected before last-close or count mutation. |
| Authorized unique full close, then repeated close and neutral cleanup | Fulfilled and the selected original/substitute subtype increase once, current streak increases once, longest uses the documented clamp. Repeats do not retire it. |
| Failed accepted substitution after a failed transfer | Restores family/mobile type/balance, clears accepted work flag, retains ledger original family and open receipt, adds no terminal fulfillment. |
| Partial 5 of 10, then successful ordinary full 5 | One issued, zero terminal count after partial, one full-original fulfillment after full, no retired outcome. Measured shipment amounts remain the contribution worker's proof. |
| Last-unit partial 1 of remaining 1 | Fails before transfer. D2. |
| Neutral archival with no active host | Closes a valid immutable tuple as retired, preserves current and longest streak, adds no adverse or fulfilled count. |
| Refusal/defiance with an open demand | Refusal enum closes once before subsequent neutral cleanup. Defiance without a demand does not invent one. Receipt/history ordering is D5. |
| Actual war handled by normal owner pass | War enum closes once and resets current streak, subsequent cleanup is inert for terminal counters. |
| Victor defeats host before normal war cancellation | Neutral retirement can win the race. D4. |
| Old timeout invoked against replacement demand with future deadline | `fail_demand` checks that current stored deadline has elapsed before Wrath/history/closure, so it is inert. It is not a general proof of every stale callback identity. |
| Failed reconciliation mission with no tribute demand | Writes existing coarse review-failure history, but no unique tribute-failure count is added. |
| Paid ordinary offer accepted by true host, helper called twice before flag cleanup | Sequence receipt makes the second helper call inert, preserves lifetime terminal counts and longest streak, resets the permitted current recovery/post counters only once. |
| Offer/report without host ROOT, missing paid/pending flags, missing sequence, or sequence equal to last accepted | Accepted-record helper is inert. Wrong immutable history and sequence zero remain D1. |
| Victor authority renewal | Uses its separate owner and does not call the ordinary accepted-reconciliation counter helper. |
| Classifier without settlement permission | Retirement is inside `settlement_can_commit`, so no open receipt is consumed. |
| Valid classifier then guarded finalize | First neutral retirement precedes snapshots. Repeated finalize retirement is inert because the receipt was consumed. |
| Generic clear on participant with no demand_active | Parent's added PREV flag check prevents unrelated active-count decrement. Replacement-host ownership remains D3. |

## MCP evidence and exact limits

Live exposed ordinary event/reference/source schemas were inspected and used.
No MCP job, task, helper-expansion, rewrite, map, GUI, or game-launch route was used.
Server-version/client-task negotiation was not established, so helper expansion and jobs were deliberately not attempted.
The `hoi4.script_validate` route is absent from the exposed server tools.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
`hoi4.event_inspect` traced `chaosx.nr12.601` and then narrowly traced `chaosx.nr12.603` with refresh, both directions, depth 1, at most 10-12 nodes and 20-24 edges, without helper expansion.
Both returned `EVENT_INSPECTED_PARTIAL`, focused analysis, `counts.helpers = 0`, and revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`.
The refreshed .603 report URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2bd3c8da49e3106aae7351bb7cf491cd30c287029f43efe97b6cb9cbfa5b75a/08824ce3aa6ad66e7a23923d47e73993d0293f4efdde8c8160ec70b79de599c9/event-trace-828ca59a9a1f.json`.
Focused analysis covers event/on-action source rather than this scripted-helper lifecycle.
Its unchanged event revision across the parent's helper edits is not evidence that those edits were compared or validated.

`hoi4.event_render` rendered the .603 neighborhood under the same narrow depth/node bounds and returned `EVENT_RENDERED_PARTIAL`, 3 selected nodes, and JSON/SVG/PNG artifacts.
JSON URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe1a5e9cc1de8d41bc84028ee980a40aab5e31b533860a89971183e9b687636a/e0d9758ff44acb5624b245b7234562f254021963e1b983a0f9e8485b81784b3e/event-neighborhood-828ca59a9a1f.json`.
PNG URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5091c729497687f0c19b63809e758852689a051df5cf083cdf9cbcae6db61095/d86e55c072229e49df5a2f761ffbb3d3d4136e5079e05dff7b9014b9be0c1f9b/event-neighborhood-828ca59a9a1f.png`.
The manifest byte-range read through the discovered resource template failed exactly with `Artifact provenance manifest is unavailable`.
Artifacts were emitted, but their complete contents and visual view were not verified by this audit.

`hoi4.event_compare` was attempted with the returned cached revision and a .603 selection, no rendered comparison, and bounds of 10 nodes.
It returned `EVENT_REVISION_NOT_CACHED` with blocker `Requested event graph revision is not cached or retained as a graph artifact`.
No comparison result or baseline-helper equivalence is claimed.
Initial selector/input validation errors were corrected with the exposed discriminated selector shape and a supported revision object before these final calls.

`hoi4.source_lookup` found the single nonoverridden closing helper, revision `130ca715cf3cde54f3215dab889e17405648d1ce14c851e91aa8b40f1fe09154`, at its earlier lines 62-123.
This lookup preceded the parent's later authorization patch and is not the final source snapshot.
Its reference inventory was incomplete (`referencesComplete = false`, 18,450 unresolved references), so the audit separately searched actual current source callers.

No weighted surface is included in this tranche's assessment, so no probability pass was substituted or performed by the completion auditor.
If the parent expands validation to existing AI weights or punishment probabilities, that separate pass must go through `chaosx_ai_probability_auditor`.
Do not treat these manual cases or focused MCP artifacts as equivalent helper/native validation.

## Reference evidence

The event reference-context bundle reported six omitted sources, not missing local files.
It was treated as source discovery, not complete detailed reference coverage.
The relevant detailed sections actually read were:

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:2110-2135`, `check_variable`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:2695-2712`, `clamp_variable`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:425-434` through reference-read, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and variable-types lines 435-442 directly.
- Installed vanilla `common\scripted_effects\BUL_scripted_effects.txt:3-12`, read directly as a real country-variable/clamp precedent, not a substitute for the unique contract design.

Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and the mission-timer/callback guidance in `chaos-redux-decisions-missions`.
No visual asset or custom 3D surface was in scope, so asset/model skills and workers were not invoked.
The existing accepted plan was reviewed rather than spawning another expansion planner.

## Final source identities

Hashes below identify the last full source read used for this report.
The parent was actively editing during review, so later coupled integration requires another review of changed relevant blocks.

| Path | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_contract_effects.txt` | `3799E546C2AEC4B921314838A6E723EA450D8EBB88B8DBAB66B6EF795043F4EE` |
| `common/scripted_triggers/012_africa_gods_contract_triggers.txt` | `3F9C894B31B5B0DEC252361507DF4601F572D7063D96D321E93A7F57B84789D5` |
| `common/script_constants/012_africa_gods_contract_constants.txt` | `13FB54037D0DAF14C8535C1FBD012C1971B17ECA2F061F6511198A6BDE87EF33` |
| `common/scripted_effects/012_africa_gods_effects.txt` | `E236EC9EE87C5A1A42FA9D12A35EF6A3D2729848509BC60F6229EF04E22676AC` |
| `common/scripted_effects/012_africa_gods_lifecycle_effects.txt` | `DF3D38C96EE5958A0F660BA42CE0A1E69228965DBA4CF1BC64567A99827403DB` |
| `common/scripted_triggers/012_africa_gods_triggers.txt` | `8ABAF42A84646715583F705B31150B786B6050CC4E428C36C91126C88DEAE28D` |
| `common/scripted_effects/012_africa_gods_contract_effects.md` | `5EB27C836B16CCCD64FC0DD9C021C51CC46B084E81834A18F3CDD8355C21784E` |

## Parent next actions and completion limits

Correct D1-D5 within the existing owners and align the false terminal-partial documentation claim.
Recheck the equality partial, wrong/missing identity, stale-host cleanup, and victor-before-owner-tick cases against the final coupled source.
Retain no-backfill behavior and report legacy history without receipts as an evidence limitation.
Preserve exact original-family identity across failed and successful substitutes and consume fulfillment authorization only once.
Recover a graph-bearing baseline and artifact provenance only through confirmed read-only MCP routes, or keep the exact comparison/helper-coverage blockers in the parent report.
No new broad expansion, asset handoff, UI worker, or balance redesign is recommended by this audit.
The parent must review this bounded report before promoting the contract tranche or committing it as complete.

## Owner-correction re-review, 2026-10-03 21:19 UTC

This appended review supersedes the earlier D1-D5 disposition and recommendations wherever corrected source is cited below.
The earlier findings and hashes remain historical audit evidence.
Scope is unchanged, including exact callers, participant cleanup, victor cleanup, and helper documentation.
Only this audit handoff was edited by the auditor.
No Git, source patch, game launch, probability audit, new broad plan, or additional expensive MCP request was performed.
The previously recorded MCP/helper/comparison limits remain explicit limits, not evidence for the revised helpers.

Status: D1, D2, and D5's specified normal-path corrections are verified in source.
D3 is corrected for the four modified cleanup owners but remains unresolved at the native participant cleanup owner.
D4's real-victor and ordinary archive/host-loss race corrections are verified for valid frozen host identity, with the malformed stored-pointer case below unresolved.
Three precise remaining source cases are R1-R3 below.
No native completion or overall Gods completion is claimed.

### Resolved requirements and cases

| Original finding/case | Revised source evidence | Re-review result |
| --- | --- | --- |
| D1 missing/wrong immutable history owner or origin at opening | `012_africa_gods_contract_triggers.txt:35-42` requires initialized contract history, present owner/origin, owner equal to THIS.id, existing actual host with origin, and equal durable/current origin. `012_africa_gods_contract_effects.txt:35` invokes it. | Missing fields or mismatched owner/origin prevent issuance. |
| D1 creation should fail before consuming host sequence | `012_africa_gods_effects.txt:1751-1767` performs the participant identity preflight inside creation's limit before host sequence increment. | Wrong immutable identity produces no host-sequence increment, demand dispatch, or new slot. |
| D1 accepted-reconciliation counter requires identity and positive paid sequence | Contract effects lines 144-156 require immutable identity and positive offer sequence, then consume an increasing sequence before counters. | Missing, zero, or replayed sequence makes the counter helper inert. Missing/wrong owner/origin also blocks it. |
| D1 ordinary seek/complete caller identity | Core effects lines 3011 and 3876 guard immutable identity before pardon or bilateral debit. | Missing/wrong owner/origin cannot pay or pardon through these ordinary callers. Remaining sequence-envelope behavior is R2. |
| D2 terminal partial 1 of remaining 1 | Core triggers lines 979-988 use positive amount and `less_than_or_equals`, with hidden ledger gate. Core effects lines 2042-2055 validate ledger, transfer, subtract the amount, authorize and close zero balance before history. | Equality is reachable. One successful unit payment closes one full-original contract. Amount above remaining is rejected. |
| D3 frozen native slot owner | Core effects lines 1773-1778 reset slot release and freeze native host scope, ID, origin, and generation. Contract effects lines 170-200 consume a one-use flag and decrement only the stored existing object matching ID, origin, and generation. | Replacing global africa_host cannot route this helper's decrement to the replacement. Repeated release cannot decrement twice. Missing or wrong frozen object identity produces no host-count mutation. |
| D3 four modified cleanup callers | Archive at core effects lines 397-398, clear at 2272-2273, guarded finalize at 3273-3274, and host-loss cancel at 3425-3426 invoke receipt cleanup and frozen slot release before clearing native fields. | Correct for these four owners. This does not cover the fifth owner `clean_participant`, which remains R1. |
| D4 actual credited victor defeats host before owner war tick | `012_africa_gods_victor_effects.txt:49-60` closes war_breach before victory history and victor exemption. `012_africa_gods_victor_triggers.txt:5-17` binds native winner/callback, defeated host, and participant generation. | A valid matching open contract becomes broken-by-war once, current streak resets, later neutral cleanup cannot relabel it retired. Victory arrays and reports remain retained. |
| D4 another actor's archive or host-loss cleanup races war observer | Contract effects lines 205-216 choose adverse closure for a valid open ledger whose stored host exists and is currently at war with the participant. Otherwise they use neutral retirement. Archive and cancel invoke this helper first. | For a correct frozen host pointer, all such actors receive the adverse result without new Wrath or punishment after authority ends. Pointer consistency remains R3. |
| D5 full and terminal partial receipt ordering | Core effects lines 1992-2003 and 2042-2055 validate ledger before payment and consume authorized closure immediately after payment success or zero balance. History/relationship/report changes follow. | The earlier receipt-order defect is resolved for these paths. An old payment_success value alone remains insufficient for direct full closure. |
| D5 refusal, failure, war, and defiance ordering | Core effects lines 2852-2854, 2889-2894, 2910-2916, and 2944-2950 validate and close before outcome history/Wrath/report changes. Defiance without a demand invokes no terminal count. | The requested terminal owners reject malformed ledger identity before those mutations. First-refusal punishment still precedes the coarse refusal-history write. |
| D5 last-close stamped before validation | Contract effects lines 66-85 retain identity/kind/authorization checks before consuming permission and writing last-close. | No early last-close write found. |
| Single closure enum owner | Repository search finds one `gods_of_africa_contract_close` group, in contract constants lines 2-9. No `.war` consumer remains. `.war_breach = 5` is used by contract, core, and victor owners. | The duplicate grading closure enum is absent. No enum-owner conflict remains. |
| Failed substitution rollback | Core effects `gods_of_africa_resolve_substitute` retains the original family/mobile type/remaining snapshot and restores it when the full resolver leaves demand active. | Failed debit or failed ledger preflight does not fulfill, consume the ledger, or replace immutable original family. |
| Partial then ordinary full | Nonterminal partial does not enter the zero-balance closure branch. Later full closes the same open tuple. | One issued and one fulfilled contract, with one full-original subtype count. No extra fulfillment or neutral retirement. |
| Host-independent neutral retirement | Closure still compares immutable local receipt/history and does not require an active global host. | A valid peaceful archive/host-loss contract retires once and preserves current and longest streak. |
| Deadline replay | `gods_of_africa_fail_demand` retains a present current deadline and elapsed-date check before closure or Wrath. | An old timeout against a replacement future deadline remains inert. |
| First genuine history and no backfill | Lifecycle initialization ordering is unchanged and existing history, including a zero count, continues to block new receipt initialization. | Prior accepted no-backfill case remains resolved. Legacy receipt absence remains an evidence limitation. |

These results are manual traces of current source branches and guards.
They do not establish native equipment-delivery quantities, in-game callback timing, or the separate grading/contribution/recovery workers' completion.

### R1. Native participant cleanup still bypasses retirement and frozen slot release

Priority: high.
This is the remaining D3 integration path and a neutral-retirement gap inside the existing bounded lifecycle scope.
`common/scripted_effects/012_africa_gods_effects.txt:3165-3259`, `gods_of_africa_clean_participant`, has neither a retirement call nor `gods_of_africa_release_demand_slot`.
At lines 3173-3190 it still decrements the shared global host's active count, checking only PREV's demand_active flag.
At lines 3195 and 3224-3232 it clears demand_active and native identity/balance/deadline.
Its known real callers are `common/on_actions/012_africa_gods_on_actions.txt:45,56`, for participant capitulation and annexation.

Case R1a: a genuine participant with one valid open contract capitulates peacefully relative to the tribute host.
This native path clears the live demand without increasing retired or consuming the open ledger.
Afterward closure rejects it because demand_active/native identity are gone, so an issued contract has no terminal outcome and its old open receipt can obstruct later issuance.

Case R1b: retain an old origin-A/generation-7 active demand while shared africa_host points at origin-B/generation-8 with an unrelated active count of one.
The same native cleanup decrements B's count to zero, bypassing the new frozen release helper.
It also ignores an already-consumed demand_slot_released flag when demand_active remains present.

Recommended bounded correction: give this fifth owner the interrupted-retirement and frozen-slot-release calls before clearing native state, remove its old shared-pointer active-count block, and clear native host work fields consistently with the other cleanup owners.
This does not require changing participant-count or priority-offender policy, which is outside this particular contract finding.

### R2. Ordinary complete-reconciliation can pardon a sequence-invalid offer

Priority: medium, malformed-input/source-helper fail-closed case.
D1's immutable identity correction is verified at `common/scripted_effects/012_africa_gods_effects.txt:3011`.
However, the public ordinary completion owner at lines 3006-3031 does not validate that the offer sequence exists and is positive before continuing after its recorder call.
The stronger recorder at contract effects lines 149-154 rejects missing/zero sequence.
The caller at core effects lines 3016-3031 then still removes the mission, clears defiance/opt-out and paid/pending flags, applies pardon Wrath, and writes reconciliation history/opinions.

Case: valid immutable history, current participant permission, true host ROOT, and paid/pending flags, but remove the offer sequence or leave it at zero.
The recorder adds no accepted-reconciliation receipt or count, but the outer completion still pardons the participant.
The ordinary payment owner does mint a positive sequence, so this is not reported as a normal paid transaction failing.
It is the remaining malformed-input acceptance boundary required by the requested fail-closed review.

Recommended bounded correction: validate the genuine positive offer envelope in the ordinary completion owner before pardon, and preserve the supported case where the recorder has already consumed that same genuine sequence before flag cleanup.
Do not simply reject every equal last-accepted sequence without deciding how that legitimate two-step completion finishes.

### R3. Interrupted war closure does not validate the stored host pointer against its frozen identity fields

Priority: medium, malformed-pointer identity case within the D4 correction.
`common/scripted_effects/012_africa_gods_contract_effects.txt:205-214` requires local ledger identity, a stored demand_host variable, existence of that object, and war against that object.
It does not cross-check the object against frozen demand_host_id, demand_origin_host_id, or demand_generation.
Those object identity checks are already present in the release helper at lines 187-192.
The local closure trigger proves ledger/history origin but does not prove the stored host pointer names that origin's actual demand owner.

Case: preserve valid local ledger/history/native ID-generation fields, but make stored demand_host point to another existing country whose ID differs from frozen demand_host_id.
The participant is at war with that other country and is at peace with its genuine demand host.
Interrupted cleanup still writes war_breach and resets current streak for the genuine tribute contract.
Slot release correctly rejects the mismatched object, so the two helpers disagree about whether host identity is proven.

Recommended bounded correction: establish frozen object ID/origin/generation consistency before using that object as adverse war evidence, keeping current-global-host validity and post-authority punishment out of this cleanup path.
No normal writer was found that intentionally changes the stored pointer during an open contract.
This is a fail-closed input case, not an observed native corruption or a claim that ordinary creation freezes the wrong pointer.

### Documentation and evidence disposition

The false one-unit-partial claim is now backed by reachable source.
The owner appended slot-ownership and correction notes at `common/scripted_effects/012_africa_gods_contract_effects.md:55-67`.
Its absolute replacement-host/repeated-cleanup claim at lines 65-66 remains too broad while R1 is open.
The usage example at lines 39-43 still invokes full closure without illustrating its required successful-owner authorization, so a literal unqualified use would reject full closure and fall through to neutral cleanup.
The parent should qualify that example as post-success owner usage or show the ordinary resolver entry point.
These are bounded helper-documentation follow-ups, not new event/catalog/asset work.

The initial accepted grading plan remains accepted parent-owned design.
This appended audit records implementation evidence and remaining cases only, not spec promotion, balance approval, or permission to publish incomplete work.
There were no new simplifications introduced by the auditor.
The remaining source defects and MCP/native limits must stay visible in the parent's completion report.

### Revised source snapshot

Last bounded read: 2026-10-03 21:19:17 UTC.
The parent was editing concurrently, so these hashes pin the evidence above and later changes require review of the affected blocks only.

| Path | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_contract_effects.txt` | `AC7A27648D289B03C2A38EA9F10B4BA569D63829E4379B118D8C707479E0B50B` |
| `common/scripted_triggers/012_africa_gods_contract_triggers.txt` | `65215A246E34C0956AFF6925FA300B8F398498234044F63790E16460795BDE34` |
| `common/script_constants/012_africa_gods_contract_constants.txt` | `23E6DBA1A4A20DCD10A6612888D74A8280B23BA3120C3F2008C8C1EC6836880F` |
| `common/scripted_effects/012_africa_gods_effects.txt` | `F692EBA36E29CD32DDE0E247B0D34E81BB5B442700E5E3F9A1F53F82E384399A` |
| `common/scripted_triggers/012_africa_gods_triggers.txt` | `9158C91DF0C32FB2CBE020F02046828C2DB54DD0E3F4A853EF6CC9F08CE3FEF4` |
| `common/scripted_effects/012_africa_gods_victor_effects.txt` | `DB24EE955D922EF9B675B3E93958687AF1044E701F3854940D32893C15030500` |
| `common/scripted_effects/012_africa_gods_contract_effects.md` | `89D6D0B0A86F70056025EF63392BB75A127093AB5672CE52A389F9930D5264A5` |

Parent next action: review and correct R1-R3, align the bounded documentation claims, and retrace those exact cases before treating the unique-contract tranche as source-complete.
No additional expensive graph job or broader scope is a prerequisite for this bounded source-review decision.

## Final bounded R1-R3 re-review, 2026-10-03 21:26 UTC

This final appended review supersedes the preceding open R1-R3 findings and related documentation follow-ups for the source hashes below.
Verdict: no remaining source defects found in the existing bounded D1-D5 and R1-R3 cases.
The unique-contract source review is clean for parent review and commit consideration.
This verdict is not native validation, overall Gods completion, or approval of the separate grading, contribution, recovery, or reward work.
No additional implementation scope was audited.
Only this handoff was edited by the auditor.

### R1 resolved: native participant cleanup retires and releases before clearing

`common/scripted_effects/012_africa_gods_effects.txt:3171-3173` invokes interrupted retirement and frozen slot release at the start of `gods_of_africa_clean_participant`.
Its native participant capitulation/annexation callers remain `common/on_actions/012_africa_gods_on_actions.txt:45,56`.
The old shared-host active-demand decrement has been removed from the cleanup body.
Frozen native host scope/ID/origin and fulfillment authorization are cleared at core effects lines 3229-3232 before the remaining native demand fields.
A bounded multiline search across the Gods effect owners finds the only active-demand subtraction at `012_africa_gods_contract_effects.txt:196`, inside frozen slot release.

| Existing R1 case | Revised source result |
| --- | --- |
| Participant capitulates or is annexed with a valid peaceful open contract | Retired increases once before active/native identity is cleared. Open permission is consumed and cannot strand the issued contract. |
| Same cleanup with a proven current war against the frozen host | Interrupted retirement writes war_breach once before fields are cleared. It does not apply Wrath or punishment after authority ends. |
| Old A/generation-7 contract, global pointer replaced by B/generation-8 | Release targets stored A only when its frozen object proof matches. B's unrelated count remains unchanged. |
| Already released slot while demand_active remains present | One-use release flag prevents another count subtraction. Subsequent cleanup clears demand_active. |
| Repeated native cleanup after active identity was cleared | Neither terminal ledger nor slot release repeats. |
| No active current host during local cleanup | Retirement remains independent of active global authority. Stored-object checks govern count mutation. |

### R2 resolved: sequence-invalid ordinary offers cannot pardon

`common/scripted_effects/012_africa_gods_effects.txt:3014-3018` now requires a present positive offer sequence and either no last-accepted sequence or an offer at least as recent as that sequence, before the recorder call and all pardon effects.
The recorder at `012_africa_gods_contract_effects.txt:149-156` retains its stricter greater-than consumption gate.
The ordinary completion consumes paid/pending/reconciliation flags after the recorder at core effects lines 3022-3028.

| Existing R2 case | Revised source result |
| --- | --- |
| Missing offer sequence | Outer completion rejects before mission removal, pardon, history, or opinion mutations. |
| Zero offer sequence | Same fail-closed result even when paid/pending flags exist. |
| Positive offer older than last accepted | Outer completion rejects before pardon. |
| Genuine positive offer with no accepted sequence | Recorder counts once, then ordinary completion finishes and consumes flags. |
| Genuine newer positive offer | Recorder consumes and counts once before ordinary completion finishes. |
| Recorder first, ordinary completion second, same positive sequence | Outer equality branch permits completion. Recorder is inert on equality, so accepted count and recovery reset do not repeat. Pardon then consumes the pending flags. |
| Repeat completion after those flags were consumed | Existing participant/paid/pending gates reject it. |
| Missing/wrong immutable history owner/origin | Existing identity gate still rejects before pardon. |

### R3 resolved: interrupted war evidence requires the frozen owner object

`common/scripted_triggers/012_africa_gods_contract_triggers.txt:46-60`, `gods_of_africa_demand_owner_object_is_proven`, requires the frozen scope/ID/origin/generation, a present positive native demand ID, object existence, and exact stored-object ID/origin/generation matches.
`common/scripted_effects/012_africa_gods_contract_effects.txt:208-210` requires that predicate before treating war against the stored object as adverse evidence.
Its neutral branch retains the separate immutable local closure checks.

| Existing R3 case | Revised source result |
| --- | --- |
| Stored pointer names another existing country, frozen host ID still names genuine owner | Object proof fails. War against the unrelated country does not produce war_breach. A valid local ledger follows the intended neutral retirement branch. |
| Stored object origin or generation differs from frozen fields | Same rejection of adverse war evidence. Frozen release also prevents unrelated count mutation. |
| Stored scope or required frozen identity field is missing | No adverse inference from an unproven object. Neutral local retirement still requires valid immutable ledger identity. |
| Native demand ID is absent or zero | The new owner-object proof fails. Missing native ID also fails local closure. No adverse war count is manufactured. |
| Correct frozen object and actual current war against it | Exactly one war_breach closure and current-streak reset, followed by one-use slot release. |
| Correct frozen object, no current war | Neutral retirement preserves current and longest streak. |

### Documentation and final disposition

`common/scripted_effects/012_africa_gods_contract_effects.md:37-43` now uses the canonical `gods_of_africa_resolve_full_compliance` entry point and explains its actual payment and one-use authorization.
The bare unauthorized full-close example has been removed.
Its added native-cleanup, stored-object proof, and recorder-first completion notes at lines 69-71 match the reviewed source.
The previous bounded documentation findings are resolved.

The prior source-verified D1-D5 corrections remain resolved with these final integration fixes.
The accepted contract portion has source implementation and bounded review evidence with no remaining simplification found in these cases.
Parent review still owns integration, any design/spec disposition, and the commit.
The accepted grading plan's wider disposition is not changed by this narrow review.

All cases above are manual source-path traces.
Previously recorded focused MCP/helper coverage, artifact provenance, cached comparison, and native-execution limits remain unchanged.
No additional expensive MCP call, job, helper expansion, gameplay edit, Git action, or HOI4 launch was performed for this final review.
No source-only result is promoted to equivalent native or complete MCP lifecycle evidence.

### Final pinned source

Read time: 2026-10-03 21:26:53 UTC.

| Path | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_contract_effects.txt` | `080BDB797FE80F80B7BC96714D52D3FBDA76D87B6219FD23CD0A5605F751B737` |
| `common/scripted_triggers/012_africa_gods_contract_triggers.txt` | `96E8D54AC68A2CAAF73D4D24AF0806005C056DA15173CD6CEEF6A9946BD33D8A` |
| `common/script_constants/012_africa_gods_contract_constants.txt` | `23E6DBA1A4A20DCD10A6612888D74A8280B23BA3120C3F2008C8C1EC6836880F` |
| `common/scripted_effects/012_africa_gods_effects.txt` | `2219E7B77E39BE17F466A132F909BA1D8D3B7E63776CF71B680C56040CBC3FE9` |
| `common/scripted_effects/012_africa_gods_lifecycle_effects.txt` | `DF3D38C96EE5958A0F660BA42CE0A1E69228965DBA4CF1BC64567A99827403DB` |
| `common/scripted_triggers/012_africa_gods_triggers.txt` | `9158C91DF0C32FB2CBE020F02046828C2DB54DD0E3F4A853EF6CC9F08CE3FEF4` |
| `common/scripted_effects/012_africa_gods_victor_effects.txt` | `DB24EE955D922EF9B675B3E93958687AF1044E701F3854940D32893C15030500` |
| `common/scripted_effects/012_africa_gods_contract_effects.md` | `0E44928214D47E8DD04B02C244A84AAEC8D89F41A6116D378B280D169A4285C3` |

Final concurrent-change check at 21:28:52 UTC found two additional initialization guards, `exists = yes` and `has_country_flag = gods_of_africa_participant`, in the contract history initializer.
The relevant effect blocks were re-read and the R1-R3 verdict is unchanged.
The final contract-effects SHA-256 is `98CA94781A73A995D09251A8EA80392A406E58DF8A2E6AC712C7CB0C32B84B3E`, superseding its immediately preceding hash in this final-review table.
Within that file, subsequent line citations shift by two: slot subtraction is at line 198, interrupted retirement at lines 207-217, and reconciliation sequence guards/consumption at lines 151-158.
Core effects and contract triggers still match their pinned final-review hashes.
