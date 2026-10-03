# Event 012 Gods survivor settlement and victor authority design

Date: 2026-10-03.
Owner: `chaosx_scripted_system_architect`, read-only gameplay design sidecar.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Only file written: this handoff.
No gameplay, localisation, skill, Git, index, runtime configuration, or game-launch operation was performed.
The parent owns implementation, final wiring, audits, and completion claims.

## Authority and disposition

**Accepted goal requirements:** the supplied parent assignment explicitly identifies the full Gods spec as accepted, reports the active user's instruction to complete Gods without simplifications and continue without more input using the recommended choice, and limits this sidecar to survivor settlement and victor authority.
That supplied acceptance basis applies to the requirements below, rather than being inferred from a spec filename or an old plan status.

- `012_gods_of_africa_full_spec.md:101–114` requires major/player enrollment, one record per participant, continued participation after loss of major rank, and archival of annexed or invalid actors.
- Lines 1061–1077 pause ordinary tribute during war, stop demands and punishments against the participant who capitulates Africa, require a defeat report and permanent hidden result, and require a separate Event 012 re-legitimation milestone before authority can return over that victor.
- Lines 1083–1105 require the authoritative continental endpoint to stop tribute and evaluate every surviving participant from the full conduct record, doctrine, and final Strength.
- Lines 1107–1163 describe the settlement outcomes and meaningful material/diplomatic results.

Disposition: survivor lifecycle/coverage is **implemented in source**, with independent audit in `012_africa_gods_survivor_settlement_audit_2026-10-03.md`; victor renewal is **accepted and queued** as the next authority tranche.
Parent acceptance on 2026-10-03 within the user's complete-Gods and recommended-choice authorization adopts the census/history/independent-receipt method and the explicit bilateral re-legitimation recommendation.
The survivor implementation and limits belong in `012_africa_gods_survivor_settlement_2026-10-03.md`.
The wider grading/reward requirements remain a separate accepted tranche; this disposition does not equate lifecycle coverage with those completed mechanics.
The parent reports `61cca7` as the completed durable-history/opt-out fix.
The current source contains its lifecycle helpers and call sites, but this sidecar did not inspect Git or verify that commit identity.
The earlier lifecycle audit's U1 membership distinction, U2 archived-survivor gap, and U3 country-object/event lifetime uncertainty remain the starting evidence.

**Recommended design:** use the maintained candidate census for one final settlement pass, introduce history and receipt predicates separate from live authority, capture a victor's exemption before unifier-loss cleanup, and restore authority only through an explicit bilateral Event 012 renewal.
The proposed helper identifiers and exact renewal transaction below are recommendations for parent acceptance within the supplied user-authorized scope.
They are not claimed to be an already approved detailed milestone or implemented gameplay.
No proposal here promotes an old successor mandate into re-legitimation.

## Current source facts

All relative paths below resolve under the workspace above.
Line ranges describe the source read during this sidecar, which may move while the parent works in the shared tree.

1. The actual census identifier is `gods_of_africa_candidate_registry`, not `gods_of_africa_candidates`.
   `012_africa_world_order_effects.txt:820–825,902–915` initializes it and fills it once from `global.countries`, including remembered minor and landless country objects.
   `012_africa_gods_triggers.txt:122–131` deduplicates and bounds insertion through `gods_of_africa_candidate_count` and `constant:gods_of_africa_timing.max_participants`, currently 640 at constants line 32.
   Transaction callbacks maintain that same census.
   Final settlement can iterate this existing host-owned array without a new world-discovery pass.

2. Enrollment at `012_africa_gods_effects.txt:310–352` assigns `gods_of_africa_participant_generation`, initializes the durable history, and inserts the live participant.
   `012_africa_gods_lifecycle_effects.txt:4–35` recognizes an existing `gods_of_africa_history_count` even when zero and otherwise initializes once.
   Thus a first enrolled country that has not answered a demand still has a valid history record.
   Archive at effects 389–500 clears live participation and contracts while retaining participant generation, history, and Wrath.
   Capitulation uses `gods_of_africa_clean_participant`, whose 3093–3122 prefix removes the live registry identity.

3. Settlement at effects 3434–3455 currently iterates only `gods_of_africa_participants`, evaluates, grants the reward, finalizes, and fires `.608`.
   Host cleanup at 3462–3490 then empties the live array and zeros the counters/Strength.
   Changing only the loop array is insufficient.
   Every final classifier at triggers 910–953 begins with `gods_of_africa_participant_generation_is_current`, which requires a live, non-capitulated participant flag at 160–173.
   An archived survivor would fail enemy, favored, and respected checks and fall into the distrusted default at effects 3013.

4. `.608` at `events\012_africa_gods_of_africa.txt:138–154` also uses the live alias `africa_gods_of_africa_participant_is_current` plus pending report.
   Acknowledgement at effects 3284–3298 removes membership, decrements a positive participant counter without first proving membership, and clears `gods_of_africa_final_outcome_committed`.
   Receipt acknowledgement therefore needs its own gate and must retain the durable outcome/accounting proof.
   It must not be used to repair live authority by re-setting a participant flag.

5. Reward helper at effects 3021–3089 is already guarded by `gods_of_africa_settlement_reward_granted` and debits real host infantry equipment, fuel, and `africa_common_defence_stockpile` before crediting the recipient.
   Favored currently uses 2500 equipment and 2500 fuel, respected uses 1000 of each, with the existing PP branches of 25, 10, and 5 for favored, respected, and distrusted.
   Enemy receives no numeric grant in this helper.
   The host's reserve is evaluated per recipient in array order.
   Increasing covered recipients can therefore exhaust reserve earlier without minting resources.

6. `common\on_actions\012_africa_gods_on_actions.txt` cancels the Gods layer when ROOT loses, but never captures a participant victor from FROM.
   Effects 3303–3342 record the host defeat milestone and cancel only the live participant array.
   A permanent participant victor receipt, victor report, and exemption gate were not found in the Gods source.
   The World-order callback at `012_africa_world_order_on_actions.txt:504–568` has distinct package/weather/Scramble loss ownership.
   `africa_scramble_record_continental_defeat` at World-order effects 4073–4099 marks constitutional fragmentation and clears the Scramble response roster, not a Gods re-legitimation receipt.

7. Host transfer explicitly stages and restores the candidate census at `012_africa_host_transfer_effects.txt:115–120,467–478,735–737`.
   It cancels Gods before clearing the pointer at 960–982.
   Successor commit at 1127–1138 assigns the new pointer, `africa_host_successor_received_mandate`, origin ID, and incremented host generation.
   `.232` at `events\012_african_union.txt:263–277` reports that continuity mandate.
   These operations copy selected host state explicitly.
   They neither copy every participant object nor prove inheritance of its flags, variables, arrays, or queued reports.

8. Ordinary defiance reconciliation at effects 2922–2970 and triggers 549–561 requires a live participant, pending review, paid reparations, and an offer.
   The participant/host decisions at `012_africa_gods_decisions.txt:513–538,1042–1073` use live participation and `target_array = gods_of_africa_participants`.
   This is an intentional defiance pardon, not an implemented victor renewal.
   No explicit Gods victor re-legitimation owner was found in the scoped Event 012 source/spec search.
   A government change, uncapitulation, `.232`, ordinary pardon, numeric generation change, or successor activation is not documented acceptance for restoring authority over a victor.

## Recommended settlement method

### Eligibility and historical generations

Use one `for_each_scope_loop` over the committed host's existing `gods_of_africa_candidate_registry`.
Require `exists = yes` in the iterated country scope.
`country_exists` is appropriate when checking a stored country target from another scope, while `exists` directly answers this census iteration's question.
Do not use `scope_exists` to validate a variable-backed country pointer.
Capitulation and existence are separate installed triggers.
Consequently a capitulated but existing enrolled country remains a survivor for historical evaluation, even while it cannot enroll or receive an ordinary demand.
Major/player status must not be retested for final settlement.

Proposed `gods_of_africa_participant_has_settlement_history` requires a known history initializer flag or the existing history-count marker, an explicit stored participant generation, and a valid binding to the settling host's history lineage.
It does not require `gods_of_africa_participant`, live-array membership, a non-capitulated country, or an active host.
It must not initialize a previously unenrolled census candidate to manufacture eligibility.

For the normal current-host case, retain the existing archived generation and compare it exactly to the host's generation.
For the one-use successor path, preserve one exact old-generation scalar, proposed `gods_of_africa_inherited_history_generation`, in the existing transfer staging/restore transaction from `global.africa_host_transfer_old_generation`.
Bind that scalar to the explicitly transferred `africa_origin_host_id`.
Stamp `gods_of_africa_history_origin_host_id` on the participant at real enrollment, retaining it during archival and cleanup.
A historical-generation branch must match that origin and that exact inherited generation.
Do not accept every smaller generation, assign a new generation to an archived actor just for settlement, or treat census membership as evidence of past enrollment.
The one-use successor contract permits this small scalar design rather than a general ancestry registry.
If the parent actually extends transfer beyond one historical generation, use a small explicit authorized-generation history array carried through the same transaction instead of broad numeric inequalities.

For extra country-object proof, stamp proposed `gods_of_africa_history_owner_id = THIS.id` only during genuine enrollment and compare it to the current country object's ID before using new-format receipts.
This helps reject a copied ledger whose recorded owner differs from the current object.
It does not prove that engine ID reuse cannot occur.
Do not auto-stamp arbitrary archived or new census candidates at settlement.
Existing current-generation histories without that new stamp can be handled using the already present country-local history and generation proof as a documented legacy source contract, with U3 runtime uncertainty retained.
A historical record with no origin proof cannot be silently rebound to a successor.
Report such migration coverage as unresolved if it cannot be proved by the actual registration/transfer evidence.

Evaluation should not silently redefine “surviving” to mean “currently eligible for a new demand.”
Evaluate every existing historically enrolled object, including a later special/nonhuman conversion, and exclude the current host from transfers to itself.
Keep the current special/nonhuman exclusions in enrollment and live authority.
For settlement, separate a historical outcome from any material/diplomatic receiver gate.
The installed reward effects support COUNTRY scope and document no special/nonhuman exclusion.
A decision to suppress an enrolled survivor's existing reward solely because of conversion would therefore be a separate design disposition, not an engine limitation established here.
Fail closed on an invalid or absent country object without pretending it survived or granting to a replacement tag.

### Classification, transaction, and presentation order

1. Before evaluating, freeze the host generation, origin, final Strength, and doctrine while the host remains valid.
   Reuse current values for computation before `gods_of_africa_clean_system` zeros public Strength.
   Store proposed participant `gods_of_africa_settlement_generation` and `gods_of_africa_settlement_origin_host_id` when committing the outcome.
   Save a regular `gods_of_africa_settlement_host` target for the receipt chain so `.608` does not accidentally read a later replacement of the shared global `africa_host` pointer.

2. Set the host final-commit flag before processing candidates to close normal contract responses and new dispatch.
   Replace only the authority preamble in the final classifiers with settlement-history proof.
   Preserve the current ordering and existing thresholds while the parent completes the accepted full-history grading contract.
   Durable `gods_of_africa_permanent_opt_out` must stand in for live defiance that archival/loss cleanup can clear.
   Treaty-break history is already stored as `constant:gods_of_africa_history_kind.treaty_break` in `gods_of_africa_history_kinds` and can be queried without a new event history scan.
   Temporary offender/priority flags cannot be the sole evidence for a historical enemy outcome.
   Persist a narrow unresolved-hostility receipt when the real offense owner commits it and resolve it only through its actual pardon/settlement owner.
   Do not infer that every prior offense remains unpardoned or that absence of a cleared live flag means innocence.

3. Per eligible object, require no outcome transaction already committed for that settlement generation.
   Call the existing final outcome and reward helpers once, finalize live contracts, explicitly clear the participant authority flag, then mark and issue the receipt.
   The evaluator and reward helper must each guard their own direct calls, not rely only on the outer host loop.
   Preserve final standing, the durable outcome receipt, reward receipt, and history after acknowledgement.
   Avoid granting in `.608` or acknowledgement, because repeated presentation must not charge or credit again.

4. Finalization removes demand/reconciliation missions, quotes, pending punishment and review authority, and owned protection relations.
   Preserve durable history, opt-out, victor facts, and settlement accounting.
   For archived actors, do not decrement live host counters just because they have a historical ledger.
   If a per-country cleanup removes membership, decrement only after proving actual membership and current-generation ownership.
   The host's final cleanup then clears the remaining live arrays/counters exactly once.

5. Proposed `gods_of_africa_settlement_receipt_is_current` gates `.608` and its acknowledgement using country existence, settlement/history generation and origin proof, the frozen settlement host's final-commit receipt, `gods_of_africa_final_outcome_committed`, `gods_of_africa_settlement_report_pending`, and a final-standing enum of favored/respected/distrusted/enemy.
   It must work after the live array has been emptied and the participant flag cleared.
   Acknowledgement consumes only pending presentation and any transient report payload.
   It must neither clear the durable outcome/reward receipt nor decrement an unrelated new host registry.
   A replay without pending presentation is a no-op.

6. Keep a victor's defeat report distinct from an ordinary `.608` settlement receipt.
   An unrelegitimized victor's permanent result must not be overwritten by a successor's enemy punishment or forced renewed tribute.
   If the successor later settles the continent, record any necessary historical evaluation without restoring authority or dispatching ordinary punishment to that victor.

The current classifiers do not themselves prove every factor in fullspec 1089–1103 is implemented, such as full compliance ratio, streaks, emergency support, and capability-scaled reward.
This sidecar recommends preserving the existing classifier/reward tuning while repairing lifecycle coverage.
It does not approve a simplified final-evaluation design or claim those broader accepted requirements complete.

## Recommended victor capture and re-legitimation

### Capture at the existing capitulation transaction

At the beginning of the existing Gods `on_capitulation` effect, before `gods_of_africa_cancel_on_unifier_loss`, call proposed `gods_of_africa_record_participant_victory` in FROM scope.
ROOT must be the recorded Event 012 host identified by its pointer/host commitment and generation.
Do not call the active-host predicate, which rejects a capitulated ROOT.
FROM must exist, have the already initialized participant history, match ROOT's participant generation, and have proven membership in ROOT's actual `gods_of_africa_participants` array at this transaction.
Do not credit every faction member, every enemy, or an annexation winner automatically.
The installed callback specifies FROM as the actual capitulation winner.

Write participant-local permanent `gods_of_africa_victor_recorded`, current exemption `gods_of_africa_victor_exempt`, and historical defeated host ID, origin, generation, and day.
Use separate transient `gods_of_africa_victor_report_pending` and a country-local report-generation/host receipt.
Do not encode exemption through defiance or through a numeric 0/1 variable.
Use `gods_of_africa_victor_recorded` plus the exact defeated-host episode for duplicate callback protection.
No stockpile, PP, Strength, Wrath, or reparations grant/debit is needed to recognize victory.
Capture the receipt directly rather than calling `gods_of_africa_record_history`, which requires live authority and can fail after host loss.
If an appended history kind is wanted, add a semantic `victor` enum and use a narrowly documented history writer that validates this explicit callback proof.

Then run the existing full host-loss cleanup.
It must retain victor/exemption/history flags and clear pending ordinary demand, punishment intent/tier, reconciliation review, mobile quote, payment/substitute permission, and owned protection.
Existing generic report clearing must not erase a just-created victor receipt.
Issue the report after cleanup from the frozen defeated-host chain, using a dedicated triggered country report.
`chaosx.nr12.615` had no matching definition/use in the scoped event/common/localisation ID search and is a proposed reservation only.
The parent must recheck collisions before assigning it.
Receipt acknowledgement consumes only presentation, preserving permanent historical victory and exemption.

Add `gods_of_africa_victor_exempt` rejection to enrollment/live mutation authority and the direct ordinary demand, payment, expiry, and punishment paths.
Retain U1's distinction: live authority should require current-generation membership, while settlement/defeat receipts require separate history proof.
The generation predicate used by presentation must not be strengthened blindly to live-array membership.
The raw punishment helper at effects 2416–2423 has no active-host gate today, so its own preflight must reject exempt victors and stale host authority even if a delayed caller arrives before cleanup finishes.
Re-registration must not clear exemption.
Civil-war onboarding, uncapitulation, release, host transfer, activation, and owner review must all preserve it.

### Exact milestone gap and selected recommendation

**Gap:** the accepted spec requires a separate Event 012 re-legitimation milestone but supplies no exact trigger, owner event, payment, or consent procedure for it.
No current Gods victor receipt/renewal helper implements such a milestone.
The successor continuity mandate and defiance reconciliation are adjacent existing mechanisms, with different authority semantics.
They do not establish that this missing milestone has already occurred.

**Selected recommendation for parent acceptance:** an explicit bilateral renewal of Gods authority over that one victor, using the existing participant/host decision categories and bounded candidate array, without a new route family, recurring clock, or GUI.
Suggested owner actions are `gods_of_africa_seek_victor_relegitimation` and `gods_of_africa_accept_victor_relegitimation`.
The victor voluntarily requests renewed relations, and the committed African host explicitly accepts.
The host acceptance targets the existing candidate census rather than the emptied live participant array.
This keeps consent possible while the victor remains exempt and unregistered.

Required gate: both country objects exist, the active restored host is committed to the same Event 012 origin, it is not capitulated or finally settled, Evolution I and the current Gods activation are valid, the victor's permanent result/exemption is present, and the exact request host/generation matches the accepting host.
Require no active war with Africa and no occupied current host core territory using the existing territory helper.
Require an explicit victor request receipt and explicit host acceptance, not elapsed time or a newly incremented generation.
The chosen bilateral renewal supplies the separate milestone even for a surviving recovered original host.
Same-host recovery would need a deliberately authorized host-lifecycle reopen path, because the current initializer's outer loss gate rejects it before its inner generation branch can run.
Do not weaken that gate accidentally while adding the victor path.

No reparations payment, punishment, reward, or automatic defiance pardon is proposed for this victor renewal.
The existing defiance reparations belong to their separate accepted mechanic.
If the parent elects to couple the two, it must record that design choice and use the existing payment receipt to debit once, with no refund/redebit on stale offers.

On valid acceptance, proposed `gods_of_africa_commit_victor_relegitimation` records the request's defeated-host episode and restored-host generation, clears only `gods_of_africa_victor_exempt`, consumes renewal request/acceptance state, and then uses normal enrollment if eligible.
Retain `gods_of_africa_victor_recorded` and all prior conduct history permanently.
Leave independent permanent defiance opt-out intact until its own accepted reconciliation succeeds.
A live entrant receives the normal first-demand delay, not a reinstated cancelled contract or an immediate retroactive charge.
Repeated acceptance has no effect once its request episode has been consumed.
A later real capitulation victory against another authorized host episode sets exemption again and cannot be pardoned by an older renewal receipt.

Acceptance basis for choosing a narrow renewal implementation is the supplied user direction to finish the accepted Gods scope and choose the recommended route without further input.
The exact bilateral mechanism remains this architect's recommendation until the parent records its acceptance within that scope.
An unimplemented renewal must remain an explicit gap, rather than silently making exemption irreversible or allowing a successor generation to clear it.

## Proposed helper map and API

All new effect calls use caller-set temporary inputs followed by `helper = yes`.
No named argument blocks, `$...$` macros, or central router are proposed.
Temporary inputs/outputs are unscoped and caller-initialized before invoking a helper.
Permanent identity, generation, history, and accounting proof is country-local regular state.

| Helper | Scope | Inputs and outputs | Side effects and direct call sites |
| --- | --- | --- | --- |
| `gods_of_africa_participant_has_settlement_history` | Historical participant COUNTRY | Reads initializer/count, participant generation, origin/object proof and settling host | Pure predicate for final census pass and final classifiers |
| `gods_of_africa_settlement_receipt_is_current` | Receipt recipient COUNTRY | Reads frozen settlement target, generation/origin, final commit/outcome, pending, standing | Pure predicate for `.608` trigger and acknowledgement preflight |
| `gods_of_africa_commit_participant_settlement` | Historical participant COUNTRY | Caller supplies temp `gods_of_africa_settlement_host_generation`, initialized result temp `gods_of_africa_settlement_applied = 0` | Writes frozen outcome/accounting/report proof, calls existing evaluation/reward/finalize, sets applied to one on success, used by final census pass |
| `gods_of_africa_record_participant_victory` | FROM COUNTRY in capitulation chain | Caller supplies temp defeated host generation and initializes `gods_of_africa_victory_recorded = 0`, regular defeated-host target identifies ROOT | Writes permanent victory/exemption and pending report exactly once, before host-loss cancellation |
| `gods_of_africa_victor_receipt_is_current` | Victor COUNTRY | Reads recipient-local defeat episode, pending, frozen defeated-host report proof | Pure predicate for proposed `.615` and its acknowledgement |
| `gods_of_africa_victor_can_request_relegitimation` | Exempt victor COUNTRY | Reads explicit defeat/origin, restored host, peace and territory gates | Pure predicate for renewal request action, does not confer participation |
| `gods_of_africa_commit_victor_relegitimation` | Exempt victor COUNTRY | Caller supplies temp expected renewal host generation and initializes `gods_of_africa_relegitimation_applied = 0` | Consumes exact bilateral request, records renewal, clears current exemption, normal enrollment where valid, invoked only by explicit host acceptance |

Example effect-side API, with caller variables initialized in the surrounding effect block:

```txt
set_temp_variable = { gods_of_africa_settlement_host_generation = africa_host_generation }
set_temp_variable = { gods_of_africa_settlement_applied = constant:gods_of_africa_value.zero }
for_each_scope_loop = {
	array = gods_of_africa_candidate_registry
	set_temp_variable = { gods_of_africa_settlement_applied = constant:gods_of_africa_value.zero }
	if = {
		limit = { gods_of_africa_participant_has_settlement_history = yes }
		gods_of_africa_commit_participant_settlement = yes
	}
}
```

The helper must copy any temporary expected generation into its durable receipt before firing an event.
Do not use temporary inputs as asynchronous report state.
Missing mandatory host/episode input must cause no transaction and leave the caller-initialized result at zero.
Audit existing callees for temporary-name collisions and reinitialize negated stockpile-debit inputs on every transfer.

## Constants, cleanup, and migration plan

Reuse `gods_of_africa_timing.max_participants`, `first_demand_delay_days`, current final-standing enums, current doctrine thresholds, and existing settlement transaction constants.
Do not add a new duration, review clock, probability weight, or tuning ladder merely to solve these lifecycle gaps.
If a history `victor`/`relegitimation` kind is appended, add semantic integer enums under the existing history-kind category without renumbering saved IDs.
If fuel headroom calculation needs a unit conversion, use a named shared fixed-point constant for thousands-to-units rather than a magic number.

Preserve the existing global `africa_host` owner and its cleanup contract.
Use regular chain-local `gods_of_africa_settlement_host` and `gods_of_africa_defeated_host` targets for frozen reports and the existing settlement-participant target for bilateral opinion writes.
No new persistent global target is needed.
Durable defeated/settlement identity is recorded numerically on the recipient, with existence checked before resolving any pointer.
A deleted defeated host must not suppress the victor's permanent fact or re-enable authority.
For reports whose host no longer exists, supply a historical wording variant from the already frozen receipt instead of attempting native mutations against the absent country.
Do not claim that a regular target proves lifetime after engine object replacement.

Migration order for the parent:

1. Define/document the history, live-authority, and receipt predicates in the existing Gods helper family.
2. Stamp country-local origin/object proof during genuine registration and the exact historical generation in the existing host-transfer staging/restore path.
3. Replace the final pass with the maintained census and update classifier prerequisites together.
4. Make finalization/acknowledgement safe for archived recipients and retain one-time accounting proof.
5. Capture the winner at the existing capitulation callback before cancellation and add the independent report/exemption gates.
6. Implement and record acceptance of the distinct bilateral renewal, then integrate its request cleanup with the existing named callbacks and owner review.
7. Update matching helper Markdown, the dynamic-helper index in `chaosx_dynamic_effects.md`, canonical Gods event documentation, relevant event/decision localisation and requirement tooltips.
   Existing report/decision assets can be considered for reuse, with the exact consumer inspected by the parent before wiring.
   No asset was created or visually reviewed here.

Clear transient renewal offers on host-generation change, host loss, war/territory invalidation, participant deletion, or final settlement.
This cleanup never clears permanent victory, history, opt-out, or reward/outcome accounting.
Use existing callbacks and bounded owner review for repair, without adding `on_worldday` or any ordinary all-country clock.
Parent changes can remain in the existing Gods effects/triggers/events/callbacks and the narrow transfer metadata blocks.
This sidecar creates no helper without call sites.

## Reward accounting and native receiver limits

Reuse `gods_of_africa_grant_settlement_reward` with its current real-debit branches and named amounts.
Retain a lifetime/per-settlement reward receipt after acknowledgement and successor transfer.
If a later valid settlement episode may award again, require an explicitly recorded new settlement-generation receipt rather than clearing the old flag in registration.
Do not implicitly assume repeat rewards are accepted.

Before granting, validate recipient `exists = yes`, frozen paying-host existence, final enum, and absence of a completed reward receipt.
Capitulation alone is not documented as making the COUNTRY stockpile/fuel/PP effects unsupported.
The current helper does not validate recipient fuel headroom.
Installed dynamic variables expose `fuel_k` and `max_fuel_k` in thousands, enabling an explicit recipient-headroom check.
If the parent adds exact headroom accounting, compute effective fuel as the minimum of the intended package, valid host availability, and nonnegative recipient headroom in native fuel units, then debit and credit that same effective amount.
Record intended and applied amounts separately and reuse the existing receipt text mechanism for actual results.
Do not charge the host for units the native receiver cannot retain.
Native rounding, clamping, capitulated receiver behavior, and possible stockpile losses were not established by an engine scenario here.

The current PP-equivalent branches are source facts, not proof of separate approval of a fallback design or fulfilment of the fullspec's meaningful, capability-scaled reward promise.
Do not add a different PP substitution, retry grant, artificial resource grant, or new reward target in this sidecar's implementation scope.
If the existing package policy itself needs redesign, the parent must disposition it explicitly against fullspec 1111–1123.
This handoff intentionally preserves existing amounts and classification tuning for the bounded coverage fix, with those wider acceptance limits stated.

## Meaningful validation scenarios for the parent

The following are deterministic source/engine scenarios to preserve as named evidence, not claims that they were executed here.

| Scenario | Required result |
| --- | --- |
| `S1_live_and_archived_cap_survivor` | Same history on live and archived capitulated existing actors gives the same standing, one receipt and one allowed reward transaction, with neither archival nor receipt reopening live authority |
| `S2_zero_conduct_minor_survivor` | A real enrollment with zero history entries and later loss of major rank still settles, while an unenrolled census minor does not |
| `S3_absent_and_converted_objects` | An absent actor receives no mutation, a surviving converted actor retains historical evaluation, self-transfer to the host is excluded, and any deliberate reward exclusion is reported with design authority |
| `S4_final_replay_and_ack` | Duplicate final calls, duplicate `.608`, and repeated acknowledgement cannot repeat debits/rewards, change permanent standing, or alter a new generation's live counter |
| `S5_transfer_archived_history` | Exact old generation/origin proof survives the explicit candidate staging/restore transaction, a valid archived historical survivor settles, and unrelated/missing-origin records cannot claim ancestry |
| `S6_copied_nonmember_state` | Hypothetical matching flags/generation outside the actual live registry cannot create ordinary authority or a victor receipt, while valid archived history still presents settlement |
| `V1_actual_participant_winner` | ROOT host capitulates to FROM registered participant, defeat/exemption is recorded before cancellation, pending demand/punishment ceases, and defeat report leaves a permanent fact |
| `V2_other_winner_and_callback_replay` | Third-party/faction-by-association victory and duplicate callback cannot create another reward or credit an unregistered actor |
| `V3_successor_and_same_host_recovery` | Pointer succession, `.232`, new generation, release, civil war onboarding, and original-host recovery never clear victor exemption automatically |
| `V4_explicit_renewal` | Valid victor request plus explicit restored-host acceptance commits a distinct milestone once, retains prior victory/defiance history, and uses ordinary enrollment/first delay only where eligible |
| `V5_stale_offer_or_new_defeat` | A stale generation, changed host, war, lost country, or final settlement prevents renewal, while a later actual victory restores exemption and invalidates old renewal authority |
| `R1_reserve_exhaustion_and_native_caps` | Several favored/respected live and archived survivors debit actual host resources once, consume the finite reserve in defined order, record receiver-limited applied amounts, and cannot farm acknowledgement |

This sidecar traced the current source paths for settlement, receipt gating, callbacks, transfer staging, and reconciliation.
It found the classifier failure and acknowledgement durability/counter risk that a loop-only fix would miss.
No engine scenario, save inspection, balance sweep, graphical render, event comparison, or live consumer test was run.
No save was supplied.
U3 remains unresolved for country-object deletion/recreation, dynamic-slot reuse, civil-war state inheritance, and queued-event lifetime.
Do not assume flags/variables were copied across country objects.

## MCP evidence blocker and audit routing

The connected `ALL_TOOLS` inventory was searched for `hoi4`, `hoi4_agent_tools`, reference/source routes, domain inspect routes, and tool-discovery entries.
No `mcp__hoi4_agent_tools__hoi4_*` callable tool was exposed in this sidecar turn.
In particular, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, and `hoi4.script_validate` were unavailable as callable routes.
No live schemas, server revision/health, native task negotiation, continuation URI, or MCP artifact was returned.
There was no timeout on a callable HOI4 route to retry.
The earlier lifecycle audit's failed bindings are earlier evidence and are not represented as new calls from this sidecar.
Required MCP event/domain acceptance is **blocked by missing tool exposure**.
Local source/reference reads below provide design advice only and are not equivalent engine evidence.
No focus, map, GUI layout, or technology source was designed or edited here.

No probability-bearing helper, balance weight, MTTH score, or random selection was designed or patched here.
For parent changes that alter eligibility in weighted decision/focus/event consumers, or add AI to the explicit renewal actions, require `chaosx_ai_probability_auditor` to start with `hoi4.probability_inspect`, retain the real pre-edit sources, and perform same-scenario audit/compare.
That probability evidence is not supplied by this deterministic authority sidecar.
Do not assign unaudited AI weights or claim that consent-based renewal alone fulfils AI integration.

## Local reference evidence

Installed-game root below is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Every table row names the exact local path, read section, and SHA-256 revision.
Installed documentation is the primary syntax authority, with the offline wiki read in parallel.
No Paradox web wiki was used.

| Exact source path | Read lines and bearing on design | SHA-256 |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\00_on_actions.txt` | 931–960, ROOT capitulated/FROM winner contract and native GER/SOV winner check | `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 1252–1265 equipment amount variables, 1388–1395 fuel, 1854–1861 PP, 4296–4310 scope-array loop, 6083–6091 mission removal, 6496–6510 event targets, 7820–7839 temporary inputs | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 2412–2419 targeted country existence, 2708–2715 current country existence, 3352–3359 capitulation, 5672–5684 exact membership | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md` | 385–391 current fuel and 483–485 fuel capacity in thousands | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216–245 global constants, supported fields and fixed-point access | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1–65 schema and examples | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\COG_scripted_effects.txt` | 197–213 native `global.countries` scope-array precedent, including nonexistent tags | `77fd69835f9a7115fc60d85de61c5c31e4c7880e30fb6d6e8ae494f318b02710` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263–326 target lifetime/localisation, 435–442 temporary lifetime, 1147–1156 membership, 1243–1269 loop/PREV and absent scopes, game-variable `id` entry at 1484 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 262–270 PREV/FROM, targets and variable scopes | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 250–263 capitulation/winner timing, uncapitulation, annexation, releases | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 461,638,1089 targeted/current existence and capitulation entries | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 1068,1718 PP and fuel effects, the latter narrower than installed amount documentation | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 531–538 recipient/variable namespace use | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 145–147 triggered report gating and delayed trigger re-evaluation | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 465–478 explicit mission activation/removal context | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |

Native precedents inspected directly are the installed capitulation winner check and COG country-array iteration.
Existing Chaos Redux debit helper implementation at `chaosx_dynamic_effects.txt:800–807` and its caller-input documentation at `chaosx_dynamic_effects.md:307–323` establish the local boolean-helper and amount-negation pattern to reuse.
The installed fuel/PP effect entries do not document exact clamping or rollback semantics.
Those fields remain runtime/accounting validation questions rather than inferred guarantees.

## Source revisions and final sidecar status

These SHA-256 values identify the read shared-tree snapshot, not an immutable final parent commit.
The parent should re-read changed bodies before applying this design.
Concurrent parent edits moved effect line positions during the read pass.
The final settlement, cleanup, acknowledgement, outcome, and related helper positions were rechecked against the listed effects revision before closing the sidecar.

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `7def8a688e56dd54571cbca0356f3d5ad487d9bbf4a95e9f07be465b59bb26f8` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `7250742b4bc2392203a24f819b16f2646fd7d086766d4e15ff9cbab5b074af26` |
| `common\scripted_effects\012_africa_gods_lifecycle_effects.txt` | `e506c7315a2f7046d8af3b9204f009448f949ec4be6cb176b3c971fd8cc9623b` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `129e048309e535f68ea9e199df4ae601dc45ebd73ed7fa747146b879798c26e0` |
| `common\on_actions\012_africa_world_order_on_actions.txt` | `01aa58fd5324d6ad7e7941782d4b6e75a04952e28e24529a83e8756164370bb2` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `1618810a08c9caf4c89f900299b0b4347e814e531ba1c8712574f1089a70e04d` |
| `common\scripted_effects\012_africa_world_order_effects.txt` | `6a9b793ddc2f3998394aa9909706bed61859769cc63ad09bdfe815fc228b6e7a` |
| `events\012_africa_gods_of_africa.txt` | `5d2f37e1f854b7bc97158ada548810c02b6d047cae75e9c120804a43335a04f8` |
| `events\012_african_union.txt` | `9627bed4f2f1aa5527c88d86cdf1c81b412446218574e0153d36cc02d5891401` |
| `common\script_constants\012_africa_gods_constants.txt` | `53e01ee0705a641ed2d66410ae7fe42a9f1c1a5d70dc85df6fb14193f687fe11` |
| `common\decisions\012_africa_gods_decisions.txt` | `230f9f22136cda7a6625641ef45e4d14666b846457e2c466656824d2b0d3f8b6` |
| `common\scripted_effects\chaosx_dynamic_effects.txt` | `8b4db4f595a607d041d0f072de65dd906cdb10c40246690f78d3e4305dab4d49` |
| `common\scripted_effects\chaosx_dynamic_effects.md` | `fe6a2bbc2ed8feef157f5373f2c93a0f137692679ad190647f04d3e96ac5e134` |
| `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md` | `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798` |
| `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_lifecycle_audit_2026-10-03.md` | `c89bdcb07edf96e1b843d96f2d57748a0b86cf8037eed969831ed54a4e951940` |

Completed: bounded design/authority proof, helper/call-site map, exact reference reads, accounting and cleanup advice, migration sequence, named validation scenarios, and this sole documentation artifact.
Blocked: mandatory MCP event/reference/source validation because the routes are not exposed in this turn.
Unresolved: exact parent acceptance of the recommended bilateral milestone, historical migration without origin proof, runtime country-object/event lifetime, native receiver accounting, and broader fullspec grading/reward acceptance.
No gameplay simplification, new ordinary clock, new world scan, fallback implementation, skill change, Git operation, or game launch was introduced.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions` for the bounded renewal decision advice.
No skill was created or updated.
This is completed architecture advice, not overall Event 012 or Gods implementation completion.
