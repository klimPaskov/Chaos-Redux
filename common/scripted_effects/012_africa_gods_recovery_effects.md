# Event 012 original-host Gods recovery API

This package implements the accepted restoration congress for the surviving original committed host.
It reads the existing `africa_host` pointer and never installs or reselects it.
World Order generation, government, doctrine, capitulation state, permanent opt-outs, victor exemptions, and prior history remain owned by their existing systems.
The parent owns integration into setup, loss, final settlement, clocks, categories, logs, and live participant/contract binding.

## Scope and identity

All public scripted-effect and scripted-trigger calls use `= yes` and have no parameters.
Temporary input and output variables are unscoped.
The generic owner-object validator compares `tag = event_target:africa_host`, checks actual existence, commit flags, origin/generation presence, event/evolution flags, and explicit shared terminal/transfer guards without comparing to native ROOT.
The physical-return helper checks uncapitulated status, current capital ownership and control through `PREV`, and `africa_focus_first_proof_satisfied`.
The latter's definition in `common/scripted_triggers/012_africa_triggers.txt` reads only the current country's succeeded/recovered flags and has no ROOT dependency.
Action gates for start, invite, finish, resume, and the trusted scheduler additionally require `tag = ROOT`.

The parent supplies `gods_of_africa_continent_is_secured`: explicit `africa_continental_settlement_complete` or settled Scramble phase without `africa_scramble_response_defeat`.
The generic owner validator and an already authorized epoch deliberately permit the new secured witness so the parent's one-use final-settlement endpoint remains reachable.
Initial epoch authorization and original-host recovery exclude the exact secured witness.
The final-settlement receipt excludes subsequent operation.
A defeat-settled Scramble alone is never a secured witness.

## Public effects

| Identifier | Scope and caller inputs | Outputs and side effects | Direct callers |
| --- | --- | --- | --- |
| `gods_of_africa_authorize_initial_epoch` | Actual setup owner object; required caller temp `gods_of_africa_initial_epoch_setup = constant:gods_of_africa_value.one` | Binds local epoch one and host/origin/generation receipts only if epoch, loss and recovery history are absent; consumes input to zero on every call | Parent's actual setup only, before initial clock scheduling; never wakes |
| `gods_of_africa_revoke_current_epoch` | Departing authorized owner object before roster/global-pointer cleanup; no input | Records one loss sequence/day per epoch, revokes permission, closes requests and clears schedules/dates; durable mandate/history receipts remain | Parent's loss, transfer, terminal and final cleanup |
| `gods_of_africa_begin_original_host_recovery` | Original host ROOT; no input | Opens a transaction with host/origin/generation/loss/cancelled-epoch/start-day receipts and a bounded unique eligible snapshot; grants no authority | `gods_of_africa_restore_original_mandate` |
| `gods_of_africa_invite_recovery_member` | Host ROOT, selected member FROM; no input | Saves a normal actual host object plus scalar identity receipts on the member, records invitation, and adds unique host-array rows | `gods_of_africa_invite_original_mandate_member` |
| `gods_of_africa_record_recovery_member_answer` | Member COUNTRY; required caller temp `gods_of_africa_recovery_answer` zero for decline or one for approval | Updates fresh answer/day and approval array; supports reversal during congress/consolidation; no fee or bonus | Approve/decline decision hidden effects initialize the input |
| `gods_of_africa_commit_original_host_recovery` | Host ROOT; no input | Rechecks identity/physical return/live quorum, cancels residual participants, increments epoch once, binds a committed mandate, appends local history, starts a fresh 180-day consolidation and schedules existing `.600` | `gods_of_africa_finish_original_mandate` |
| `gods_of_africa_schedule_current_clock` | Host ROOT; required caller temps `gods_of_africa_clock_kind`, `gods_of_africa_clock_due`, and caller-owned output `gods_of_africa_clock_days` initialized to zero | Verifies current permission and matching present owner date; computes delay, clamps at one day, sets current receipt and queues exactly one literal `.600`, `.606`, or `.607`; never changes dates or authority | Commit/resume locally; parent may use for due clock rearming |
| `gods_of_africa_resume_original_host_recovery` | Host ROOT; no input | After current authorization, schedule receipt, elapsed due and current quorum, queues a one-day `.600` at most once per current day; changes only repair-day receipt, no epoch/date refresh | `gods_of_africa_resume_original_mandate` |
| `gods_of_africa_clear_recovery_member_request` | Member COUNTRY; private cleanup, no input | Clears invitation, answers, object and scalar request fields only | Invite replacement and owner request cleanup |
| `gods_of_africa_close_recovery_requests` | Owner object; private cleanup, no input | Clears only requests belonging to this host through its tracked invited array; clears transient congress/approval arrays and transaction fields | Begin/revoke; parent may call after activation's quorum check |
| `gods_of_africa_clear_residual_recovery_roster` | Current host ROOT; private commit cleanup, no input | Calls existing participant cleanup on each residual participant, then clears live arrays, selection/need state and clocks; writes displayed participant count from final native cardinality | Guarded commit only |
| `gods_of_africa_cancel_recovery_participant_preserving_receipts` | Participant COUNTRY; no input | Calls existing cancellation while retaining exact pre-call final-outcome, settlement-report and victor-report flags; no new report or reward | Residual recovery cleanup; parent can reuse in loss cleanup |

The initial binder requires an explicit one-call temporary authorization supplied by the actual setup path.
No callback may set that input or call the binder.
The binder performs no migration of live legacy state.
The parent must call revoke before its existing `gods_of_africa_cancel_on_unifier_loss` guard examines cancellation, since revoke sets the cancellation flag; that parent guard must accept the newly revoked epoch rather than skip remaining roster/history cleanup.
Recovery never calls the core initializer, whose old generation-reset branch would reset doctrine and unrelated state.

Example actual setup call, after shared host commit and first-proof/evolution readiness:

```txt
set_temp_variable = { gods_of_africa_initial_epoch_setup = constant:gods_of_africa_value.one }
gods_of_africa_authorize_initial_epoch = yes
```

Example trusted owner rearm after the parent's due wrapper has completed work and written its next owner date:

```txt
set_temp_variable = { gods_of_africa_clock_kind = constant:gods_of_africa_recovery_clock.owner }
set_temp_variable = { gods_of_africa_clock_due = gods_of_africa_next_owner_tick_day }
set_temp_variable = { gods_of_africa_clock_days = constant:gods_of_africa_value.zero }
gods_of_africa_schedule_current_clock = yes
```

Clock kind selectors are `constant:gods_of_africa_recovery_clock.activation`, `.owner`, and `.registry`.
The due input must match the corresponding existing, present date.
Only trusted setup/commit/rearm/repair paths call scheduling; a wake first checks its matching due trigger and never schedules on an early or invalid return.

## Public triggers and temporary recount

| Identifier | Scope | Result and use |
| --- | --- | --- |
| `gods_of_africa_authority_owner_object_is_current` | COUNTRY object, ROOT independent | Exact committed live pointer identity and shared terminal safety; permits new secured witness for final endpoint |
| `gods_of_africa_authority_owner_has_physical_return` | COUNTRY object, ROOT independent | Uncapitulated country owns and controls its current capital and has existing first-proof capability |
| `gods_of_africa_epoch_permission_is_current` | COUNTRY object, ROOT independent | Explicit permission, positive epoch, exact host/origin/generation, physical return and no cancellation |
| `gods_of_africa_original_host_recovery_is_open` | COUNTRY object, ROOT independent | Surviving exact original, cancelled current loss, no restored mandate for that loss, no secured/successor/terminal result; physical shortfalls remain visible |
| `gods_of_africa_original_host_recovery_can_start` | Host ROOT | Presentation gate plus physical return, no open congress and at least two current eligible members |
| `gods_of_africa_recovery_congress_identity_is_current` | Host object, ROOT independent | Open congress's stored host/origin/generation/loss/cancelled epoch still current |
| `gods_of_africa_recovery_committed_identity_is_current` | Host object, ROOT independent | Separate committed mandate identity matches authorized recovery epoch and preserved loss |
| `gods_of_africa_recovery_member_is_eligible` | Member COUNTRY | Existing uncapitulated human nonspecial, nonhost current Charter/autonomous-federal/integrated member, actual relationship-array membership, current generation, no war/victor exemption |
| `gods_of_africa_recovery_member_receipt_is_current` | Member COUNTRY | Normal actual host object exists and matches global host, plus host ID/origin/generation/loss/cancelled-epoch receipts; safe in foreign native ROOT |
| `gods_of_africa_recovery_member_request_is_current` | Member COUNTRY | Receipt valid and congress or authorized consolidation pending, no competing live demand/negotiation/reconciliation |
| `gods_of_africa_recovery_member_approval_is_current` | Member COUNTRY | Fresh approved receipt, no decline, and membership in the current congress or committed approval roster |
| `gods_of_africa_recount_recovery_mandate` | Host object | Always-true temporary-output trigger: current eligible count, fresh approved count, approved count times strict-majority multiplier |
| `gods_of_africa_recovery_quorum_is_satisfied` | Host object | Recount gives at least two approvals and approved times two strictly greater than current eligible count |
| `gods_of_africa_recovery_mandate_is_current` | Host object, ROOT independent | Committed identity plus fresh live quorum, independent of closed invitation-open flag |
| `gods_of_africa_recovery_can_finish` | Host ROOT | Current open identity, physical return and live quorum |
| `gods_of_africa_recovery_can_invite` | Host ROOT | Physical return, valid open congress or current pending consolidation |
| `gods_of_africa_activation_wake_is_due` | Host object, ROOT independent | Current permission, pending receipt, activation schedule, PRESENT elapsed due, no active/committed activation, and fresh mandate for a recovery epoch |
| `gods_of_africa_owner_wake_is_due` | Host object, ROOT independent | Current permission, active/committed activation, schedule receipt, PRESENT elapsed current owner date |
| `gods_of_africa_registry_wake_is_due` | Host object, ROOT independent | Current permission, active/committed activation, schedule receipt, PRESENT elapsed current registry date |
| `gods_of_africa_recovery_can_resume` | Host ROOT | Current due activation, recovery epoch, fresh quorum and no repair today |

Recount initializes its own working values, but every caller consuming or forwarding its output must preinitialize all three temporary values before entering the nested helper.
The outer commit effect, quorum trigger, start trigger, and scripted-localisation getters do so.
No temporary uses ROOT/PREV/THIS qualification.
No temporary value needs to survive a delayed hint.

```txt
set_temp_variable = { gods_of_africa_recovery_eligible_count = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_recovery_approved_count = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_recovery_majority_count = constant:gods_of_africa_value.zero }
# In a trigger block:
gods_of_africa_recount_recovery_mandate = yes
```

The authoritative denominator is the existing unique `africa_relationship_countries`, not the opening eligible snapshot or the current approval-array length.
Its existing registration path in `012_africa_effects.txt` guards duplicate insertion.
Recount always visits all entries and excludes hostile/stale/deleted/capitulated/special/nonhuman/exempt members at the transaction boundary.
Approval rows and invitation rows are unique by explicit insertion guards.
New current members can be invited during consolidation without changing its date or epoch.

## State, history, constants and cleanup

Owner permission fields are `gods_of_africa_authority_epoch`, `gods_of_africa_authority_host_id`, `gods_of_africa_authority_origin_host_id`, and `gods_of_africa_authority_host_generation`.
Owner loss history is `gods_of_africa_loss_sequence`, `gods_of_africa_loss_epoch`, and `gods_of_africa_loss_day`.
These normal fields persist across callbacks and are never based on the wake's age.
Permission flag is `gods_of_africa_epoch_authorized`.
Congress flag is `gods_of_africa_recovery_open`; authorized recovery flag is `gods_of_africa_recovery_epoch`; accepted historical milestone flag is `gods_of_africa_original_mandate_restored`.

Congress fields use `gods_of_africa_recovery_` followed by `host_id`, `origin_host_id`, `host_generation`, `loss_sequence`, `cancelled_epoch`, and `start_day`.
Congress arrays are `gods_of_africa_recovery_eligible_members`, `gods_of_africa_recovery_invited_members`, and `gods_of_africa_recovery_approved_members`.
Committed mandate fields use `gods_of_africa_mandate_` followed by `host_id`, `origin_host_id`, `host_generation`, `loss_sequence`, `cancelled_epoch`, `authority_epoch`, `eligible_at_commit`, `approvals_at_commit`, and `day`.
The separate committed roster is `gods_of_africa_mandate_approved_members`.
Committed fields survive transaction closure; the live roster remains through consolidation and may be cleared only after activation's final quorum check.

Member flags are `gods_of_africa_recovery_invited`, `gods_of_africa_recovery_approved`, and `gods_of_africa_recovery_declined`.
The normal actual country pointer is `gods_of_africa_recovery_request_host`, assigned from native ROOT in the host's targeted invitation.
Member scalar fields use `gods_of_africa_recovery_request_` followed by `host_id`, `origin_host_id`, `host_generation`, `loss_sequence`, and `cancelled_epoch`; answer day is `gods_of_africa_recovery_answer_day`.
Cleanup does not reconstruct a country from a scalar epoch or arbitrary number and needs no new event target.

Append-only local recovery-history arrays use `gods_of_africa_recovery_history_` followed by `host_ids`, `loss_sequences`, `old_epochs`, `new_epochs`, `eligible_counts`, `approval_counts`, and `days`.
Every successful commit adds exactly one aligned row.
These arrays do not replace the parent-owned shared milestone log or participant history.
The parent adds its log receipt from the committed fields and keeps it idempotent for the loss sequence.

| Tuning | Type and location | Value |
| --- | --- | --- |
| Quorum minimum / majority multiplier | `int`, `012_africa_gods_recovery_constants.txt`, category `gods_of_africa_recovery` | 2 / 2 with strict greater-than |
| Clock selectors | `int`, same file, `gods_of_africa_recovery_clock` | activation 1, owner 2, registry 3 |
| AI start/finish, invite/resume, approve, decline | `fixed_point`, same file, `gods_of_africa_recovery_ai` | 10, 5, 10, 1 |
| AI stability threshold and approve/decline factors | `fixed_point`, same category | below 0.35: times 0.25 / times 4 |
| Consolidation / owner / registry timing | Existing `int` `gods_of_africa_timing` | 180 / 30 / 90 days, unchanged |
| Zero/one and minimum delay | Existing `int` `gods_of_africa_value` | Existing zero/one, no duplicated tuning |

Every category declares its schema first.
AI willingness scores remain a proposal pending the parent's specialist baseline/compare; they are not native click probabilities or an acceptance claim.

Request cleanup iterates the owner's invited roster without removing rows from that roster inside its loop.
Residual cleanup calls the existing participant cancellation closure, which currently does not remove participant-array rows during iteration; the outer effect clears that array afterwards.
No unverified `arraycopy` primitive is assumed.
If the parent introduces in-loop array removal, verified native array-copy syntax and snapshot evidence become a prerequisite before retaining this loop.
Queued hints cannot be cancelled by these helpers and are instead made inert by current permission/date checks.
Revoke clears local permission and schedules even if the global pointer has already disappeared, using the retained actual owner's authority-host receipt.
It never writes successor/global Strength.
Permanent history, victor exemptions, victory reports and final-settlement reports belong to existing durable receipts and are not acknowledged here.
The recovery participant wrapper snapshots the prior final-outcome/settlement-report/victor-report flags in helper-local working temps, calls the actual core cancellation, and restores only flags that were already present.
This avoids the core cancellation's final-outcome and settlement-report clears without recreating an absent receipt, firing a report, granting a reward, or changing its normal identity fields.
The parent must apply the same preservation contract to its native loss cleanup; a recovery commit cannot reconstruct a receipt erased earlier by another owner.

## Decisions, localisation and assets

Six named decision IDs cover start, invitation, finish, resume, approval and decline.
They are additive to `gods_of_africa_host_category` and `gods_of_africa_participant_category` and use phase gates.
The parent extends host category visibility for cancelled original recovery and pending committed consolidation, and member category visibility for current requests.
Choose `gods_of_africa_recovery_member_category_desc` before a normal participant description so invited nonparticipants do not read undefined Wrath.
The four getters in `012_africa_gods_recovery_scripted_localisation.txt` display live eligible/approved counts, existing consolidation duration, and quorum minimum as integers.
The companion English localisation includes names, descriptions, requirements and effects.
The congress consumes no resource and grants no generic stat reward; physical return, fresh political consent, and consolidation provide its constraints.

Existing sprites only:

- `GFX_decision_012_africa_gods_public_pardon`, defined in `interface/012_africa.gfx`, texture `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_public_pardon.dds`.
- `GFX_decision_012_africa_gods_escalate_offense`, same GFX file, texture `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_escalate_offense.dds`.

No new art, GUI, category, meter, focus, or world scan is implemented.
Existing asset definitions were verified; native visual acceptance is not claimed.

## Parent migration and follow-up

1. Implement the exact ROOT-independent secured-continent witness and use it in both old final endpoints, excluding defeat-settled as the parent has chosen.
2. Bind initial epoch only in actual setup with the required temp input and call revoke before any roster/pointer cleanup, updating the old cancellation guard for that ordering.
3. Gate `.600/.606/.607` before any mutation by their matching due predicates, remove wake initialization, and rearm dates only after completed due work.
4. Extend participant, demand, reconciliation, and victor-request live receipts with authority epoch and actual host lineage; add direct current-deadline timeout guards.
5. Recompute real activation Strength and onboard the current roster after the final recovery-quorum check, preserving doctrine and history.
6. Extend existing category visibility/descriptions and log the committed restoration milestone/history from the new normal receipts.
7. Complete specialist probability baseline/compare under the same named fixtures and domain MCP source/scenario comparison after parent integration.

Future extension suggestions remain proposals: show which current members withheld consent in existing category descriptions, and add a parent-owned milestone narrative using the committed consent counts.
Neither is required for these helpers and neither changes the accepted quorum policy.
Validation results, exact reference citations, MCP artifacts, unsupported fields and integration limits are recorded in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_recovery_helpers_2026-10-03.md`.
