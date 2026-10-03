# Event 012 Gods: full historical grading and material settlement

Date: 2026-10-03.
Parent acceptance: accepted and queued on 2026-10-03 under the user's complete-Gods/no-simplification goal and explicit recommended-choice authorization.
The parent adopts the unique-contract and measured-contribution ledger, twelve-factor deterministic standings, frozen capability-scaled material obligation, source-reserved proportional batches, and existing end-phase delivery control.
Use the current installed native `equipment` transfer spelling corroborated by `USA_scripted_effects.txt:402–418` and `AAT_Finland.txt:3722–3735`; the older tooltip-only `type` example below is historical syntax evidence, not the selected implementation.
Implementation remains queued while the owner integrates receipt hooks and the deferred transaction; this acceptance does not claim native or weighted validation.
Owner: `chaosx_improvement_loop_planner`, design only.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Only this document was written.
No gameplay, localisation, assets, spreadsheet, Git, index, or game-launch action belongs to this assignment.

## Decision and disposition

Implement the accepted historical evaluation through a unique-contract ledger, actual paid contribution receipts, four deterministic standings, and a real equipment/fuel obligation that survives ordinary tribute cleanup.
Do not replace unavailable material support with the present 25/10/5 political-power grants.
Use the existing final-settlement owner, maintained candidate census, report `.608`, and final-settlement decision row for initial and deferred delivery.
No further broad Gods expansion is recommended by this handoff.

The accepted requirement is the user's instruction to complete Gods from `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md`, especially lines 1083–1165, without simplifications, choosing the recommended design without further questions.
Its twelve conduct/doctrine factors and the additional final-Strength reward factor are mandatory.
The quantitative anchors and transaction design below are the planner's selected recommendation within that authorization; the parent must record acceptance and review implementation before marking their disposition `implemented` or `promoted into an accepted spec`.
The filename, location, and this recommendation are not substitutes for that parent disposition.

Prior mobile, survivor, and victor tranches are reported by the parent as implemented in `42bb46`, `b609837`, and `49b8a77`.
Their source owners were inspected; these commit identities were supplied, not checked through Git.
The older global original-host reopening remains separately accepted and queued because epoch/callback identity must be safe.
This document neither reopens that design nor duplicates its plan.
The U1 membership-source correction is under parent review in the core trigger owner and must not be broadened here.
The grading/reward gap is the remaining accepted tranche, rather than another pass over an unresolved mobile or survivor proposal.

## What the existing source establishes

`common\scripted_effects\012_africa_gods_effects.txt:727–752` appends aligned history kind/day rows and increments coarse action counters.
It has no contract denominator, terminal-contract receipt, streak, paid quantity, or campaign-material receipt.
History `aid` is used by both host leniency/protection and genuine participant aid; partial history is also used for procedural actions.
These rows cannot establish unique fulfillment or contribution quantities by themselves.

`gods_of_africa_create_demand_contract`, lines 1741–1813, assigns the host sequence and generation, the demand family/type, amount, remaining balance, deadline, and active flag.
`gods_of_africa_transfer_payment`, lines 1841–1974, performs the payment; full resolution at 1979–2022 and partial resolution at 2024–2059 consume its success result.
Substitute resolution at 2081–2136 temporarily replaces payment family/remaining and restores the original contract if payment fails.
That restoration behavior must remain intact.

`common\scripted_triggers\012_africa_gods_triggers.txt:831–957` grades Favored through absolute compliance OR coarse aid counts and grades the other standings through flags, Wrath, and failure/refusal ceilings.
`gods_of_africa_mark_offender`, effects 2739–2773, also marks `broken_treaty` for generic proven offending; it does not establish an actual agreement breach.
`gods_of_africa_cancel_demand_for_war`, 2859–2875, records a treaty-break kind when war cancels a demand.
Do not treat either generic action as proof of a broken signed agreement.

`gods_of_africa_offer_voluntary_aid`, effects 4218–4297, has a useful separate `gods_of_africa_voluntary_aid_count`, actual 500-unit aid amounts, shortage checks, and the existing reserve/cooldown gates.
Its infantry branch currently removes equipment and adds equipment to the recipient stockpile; use a native shipment for this branch when installing paid-quantity receipts so actual variants are transferred.
Do not alter its 500 payment, 1000 capacity requirement, or cooldown.
The existing family-13 payment is 500 political power through the payment helper's nonmaterial branch; record that actual bilateral debit/credit as emergency assistance only in a proven emergency.
Do not relabel it as equipment or change its price.

The settlement helper files already establish retained history, exact owner/origin and current-or-one-inherited generation proof, four standing enum values, a captured report-chain host, and one-use outcome/reward receipts.
The final classifier snapshots generation, origin, historical generation, Strength, and doctrine before cleanup.
The present reward helper at effects 3045–3112 uses fixed 2500/1000 infantry and fuel packages, the common-defence ledger, and PP branches, setting its receipt before delivery.
`gods_of_africa_commit_final_settlement`, 3458–3482, performs one census pass, then cleans the live system.
The remaining design must strengthen these owners, not introduce a second authority system.

## Durable ledger and exact contract outcomes

All names in the following tables are COUNTRY normal fields on the genuinely enrolled participant unless explicitly marked HOST.
Use the full `gods_of_africa_` prefix shown in the current subsystem.
The shorter symbols in formulas are aliases only, never new public meters or spendable currencies.

Add fields inside the first-genuine-history branch of `gods_of_africa_initialize_participant_history` in `012_africa_gods_lifecycle_effects.txt`.
Set `gods_of_africa_grading_ledger_initialized` only there, with zero counts/quantities and empty new proof arrays.
An existing history marker with value zero is still existing history.
Re-entry, archival, capitulation, host loss, finalization, and acknowledgement must not clear or zero this ledger.
Do not manufacture initialized history for never-enrolled census objects.
Do not silently backfill unavailable past quantities or unique contracts from coarse history counts.
Any historical ledger already present without the new receipts is an evidence/migration limitation, not proof of zero contribution; a concrete migration, if needed by the parent, requires actual source receipts and remains unresolved where these are absent.

| Field | Meaning and write owner |
| --- | --- |
| `gods_of_africa_demands_issued` | Increment once when a genuine contract is committed. |
| `gods_of_africa_demands_retired` | Increment once for a neutral retirement; never a payment. |
| `gods_of_africa_demands_fulfilled` | Increment once for a successfully closed full balance or honored accepted substitute. |
| `gods_of_africa_demands_full_original` | Fulfilled through the original family; includes a final full balance after earlier partial payment. |
| `gods_of_africa_demands_honored_substitute` | Fulfilled through an accepted, actually paid substitute. |
| `gods_of_africa_demands_failed` / `gods_of_africa_demands_refused` | Mutually exclusive closing outcomes for each contract. |
| `gods_of_africa_demands_broken_by_war` | Unique adverse closure when the participant enters war with Africa while its contract is open. |
| `gods_of_africa_compliance_streak` / `gods_of_africa_longest_compliance_streak` | Consecutive unique fulfilled contracts; max retained forever. |
| `gods_of_africa_post_reconciliation_fulfilled` | Unique fulfilled contracts after the latest genuinely accepted reconciliation. |
| `gods_of_africa_post_reconciliation_failures` / `gods_of_africa_post_reconciliation_refusals` | Adverse unique outcomes after that acceptance. |
| `gods_of_africa_war_count` | Observed war-entry episodes against the explicitly proven host, deduplicated by the war-active flag. |
| `gods_of_africa_occupied_core_state_ids` | Unique African host-core states actually controlled by the participant while it is not the host. |
| `gods_of_africa_returned_core_state_ids` | Unique states actually relinquished through an owned return transaction and verified in Africa's ownership and control. |
| `gods_of_africa_treaty_break_count` | Actual owned-agreement breaches, not punishment, negotiation, or refusal clicks. |
| `gods_of_africa_reconciliation_count` | Actual host acceptance of a paid, valid reconciliation; offers do not count. |
| `gods_of_africa_observed_host_core_count` | Cached current core-occupation count, refreshed by an effect, never counted in a trigger. |
| `gods_of_africa_paid_<kind>_k` | Cumulative actual material quantity by kind, in thousands of that kind's native units. |
| `gods_of_africa_voluntary_paid_<kind>_k` | The voluntary subset of the corresponding actual material quantity. |
| `gods_of_africa_campaign_paid_<kind>_k` | The late-campaign subset of the corresponding actual material quantity. |
| `gods_of_africa_emergency_paid_<kind>_k` | The genuinely qualified emergency subset of the corresponding actual material quantity; excludes host gifts. |
| `gods_of_africa_emergency_paid_pp` | Actual family-13 PP debited from the participant and credited to the host under proven emergency need. |

The `<kind>` inventory is exactly `infantry`, `support`, `trucks`, `artillery`, `armor`, `aircraft`, `fuel`, `convoys`, `trains`, and `manpower`.
Armor is the native sum actually transferred by the typed armor owner, not its quote or selected chassis enum.
Transport must record the branch actually used, convoy or train, rather than a generic transport count.
No arbitrary equipment family, disaster currency, national spirit, or new asset accompanies this ledger.

Durable flags are `gods_of_africa_prior_defiance`, `gods_of_africa_prior_war`, `gods_of_africa_prior_occupation`, and `gods_of_africa_prior_treaty_break`.
`gods_of_africa_permanent_opt_out` remains the authoritative unresolved opt-out flag.
Use `gods_of_africa_war_observation_active` to deduplicate a live war episode and `gods_of_africa_unresolved_treaty_break` for the actual outstanding agreement offense.
Acceptance may resolve outstanding offenses; it must retain their prior-history flags and counters.

Each live contract gains `gods_of_africa_contract_ledger_open`, immutable `gods_of_africa_contract_ledger_generation`, `gods_of_africa_contract_ledger_id`, `gods_of_africa_contract_ledger_origin_id`, and `gods_of_africa_contract_original_family`.
Its identity is the tuple `(origin, generation, demand_id)`, not a demand number alone.
Set `gods_of_africa_contract_ledger_closed` before any closing count or history write.
Retain the last closed tuple in normal `gods_of_africa_last_closed_contract_{origin_id,generation,id}` fields before clearing live work.
Closure requires an open, current matching tuple and no closed receipt.
Do not stamp new contract identity during substitute review.

Recommended helpers, all in the existing settlement/lifecycle owners, with no default receiver or inferred successful payment:

| Helper | Explicit scope, inputs, outputs and hooks |
| --- | --- |
| `gods_of_africa_open_contract_ledger` | PARTICIPANT; requires committed live demand identity and genuine initialized history; copies tuple, increments issued once. Call inside `gods_of_africa_create_demand_contract` after all demand fields are committed and before mission/event dispatch. |
| `gods_of_africa_close_contract_ledger` | PARTICIPANT; requires matching tuple and an explicit close-kind enum; writes closed receipt first, then exactly one terminal outcome and streak update. Call before contract clearing. |
| `gods_of_africa_record_paid_contribution` | PARTICIPANT; explicit actual paid kind/amount, source/receiver proof and voluntary/campaign booleans from an owned successful transaction. Adds actual quantity and subsets once; never called from `record_history`, report presentation, quotes, or affordability triggers. |
| `gods_of_africa_record_paid_emergency_aid` | PARTICIPANT; immutable family-13/emergency context and measured PP debit/credit; records emergency PP only after the real paid branch succeeds. Also supports actual material payments on a frozen emergency contract, with the material receipt owner below. |
| `gods_of_africa_refresh_grading_conduct` | PARTICIPANT; explicit captured current host and valid current/inherited history proof; observes war and core occupation, updates cached floor causes, never creates live membership. Call from the existing bounded owner review and before final classification. |
| `gods_of_africa_freeze_final_grade_inputs` | PARTICIPANT; owner endpoint committed, genuine history, no final outcome; freezes all grade inputs and final capability before any cleanup. |
| `gods_of_africa_initialize_settlement_obligation` | PARTICIPANT in the settling HOST transaction; requires frozen grade, exact source identity, and no obligation receipt; computes entitlement once, registers host totals, applies standing diplomacy once. Does not imply delivery. |
| `gods_of_africa_deliver_settlement_obligations` | HOST; exact committed settlement owner and retained census; bounded proportional distribution of real infantry/fuel to valid owing recipients. It never grades again. |

Closing kinds are `full_original = 1`, `honored_substitute = 2`, `failure = 3`, `refusal = 4`, `war_breach = 5`, and `retired = 6` in a new schema-bearing integer group `gods_of_africa_contract_close`.
Full-original or honored-substitute adds one fulfilled contract, increases current streak by one, updates the longest streak, and increments post-reconciliation fulfilled when that marker exists.
Failure, refusal, and adverse war closure reset the current streak to zero and increment only their own unique adverse count.
A neutral retirement leaves both streak counts unchanged and adds one retired contract.
It neither pads the numerator nor becomes an offense.

Neutral retirements include unfinished contracts canceled by the authoritative final endpoint, participant archival/capitulation cleanup, or host-generation invalidation where no adverse participant transaction has already closed the contract.
War cancellation caused by the participant's actual war with Africa is adverse, not a neutral escape from the denominator.
Permanent defiance with an open demand closes that demand as refusal once, then sets durable defiance separately; defiance without an open demand does not invent a demand.
A failed reconciliation mission is not a failed tribute contract.
Negotiation, extension, rejected substitute, and every partial-payment click leave the contract denominator, fulfilled count, and streak unchanged.
The actual partial material is recorded once; when its remaining balance is later fully paid, the original contract becomes one fulfilled contract with the combined actual paid quantity, not two fulfillments.

`gods_of_africa_clear_demand`, all archive/cleanup paths, and finalization call the neutral-retirement branch only if the live tuple is still open and has no terminal receipt.
The normal full/refusal/failure/war helpers call their specific closure first.
The existing aligned `history_kinds`/`history_days` writer remains presentation/history infrastructure and keeps its existing kind values; it must not become the source of these new quantity or contract counters.
New proof rows, if added for conduct, must append both arrays together exactly once.

## Actual aid, late support, and offense proof

At each material payment, preserve the actual payment family/type and amount before `gods_of_africa_transfer_payment` clears its work fields.
Read source and recipient native quantities before and after the owned effect, and credit no more than the positive common delivered amount: `min(requested, source_before - source_after, receiver_after - receiver_before)`.
For native equipment use the corresponding `num_equipment@<archetype>` readings for the immediate delta and the authoritative `has_equipment` stockpile gate for affordability.
For fuel use `fuel_k * 1000`; for manpower use the documented thousands reading converted to raw men for the immediate delta.
Do not use a requested amount or `payment_success = 1` alone as delivered-quantity proof.
Retain the typed mobile/armor owner's actual send receipt; do not infer artillery from a truck quote or chassis equipment from an abstract armor amount.
A successful material payment receipt is written by the transfer owner after the debit/credit, and consumed once by its caller.
Use durable participant `gods_of_africa_material_transfer_sequence` and `gods_of_africa_last_consumed_material_transfer_id`, initialized only with genuine history, plus live normal `gods_of_africa_material_transfer_receipt_{id,kind,amount,source_id,receiver_id,host_generation,origin_id,contract_id}` fields and a `gods_of_africa_material_transfer_receipt_pending` flag.
The native transfer owner increments the sequence and stamps that receipt only after measured delivery; the recorder requires the pending flag, a receipt ID greater than the consumed ID, exact owner/receiver and current contract proof or the genuine voluntary transaction proof, and the actual measured amount.
It consumes the pending flag and advances the consumed ID before adding cumulative quantities/subsets.
No direct caller may obtain credit merely by setting a requested kind and amount; it needs the owned native receipt.
The same receipt envelope can record the family-13 paid PP kind through the emergency helper, with zero material credit; stamp its own measured debit/credit rather than reusing an equipment receipt.
Receipt kinds are stable integers in `gods_of_africa_contribution_kind`: `infantry = 1`, `support = 2`, `trucks = 3`, `artillery = 4`, `armor = 5`, `aircraft = 6`, `fuel = 7`, `convoys = 8`, `trains = 9`, `manpower = 10`, `emergency_pp = 11`.
This group also begins with `schema = { any_key = yes data = int }`; kind 11 is routed exclusively to emergency-PP accounting.
The transfer owner stamps transient receipt flags `gods_of_africa_material_receipt_voluntary`, `gods_of_africa_material_receipt_emergency`, and `gods_of_africa_material_receipt_campaign` from the genuine transaction context before it publishes pending; the recorder consumes/clears these flags with the receipt.
Clear only its transaction work fields after consumption.
A full resolver must verify the intended remaining quantity was actually delivered before marking the contract fulfilled; a short transfer remains a partial balance with the measured debit retained and no repeat debit for that part.

Voluntary aid uses `gods_of_africa_offer_voluntary_aid` and its existing separate count, but grading derives voluntary magnitude from the measured outbound quantities.
Replace its infantry remove/add sequence with native `send_equipment` under the same cost, need, reserve, and cooldown contract.
Host gifts, host leniency, protection grants, and their `history_kind.aid` rows add neither voluntary material nor donor contribution.
Receiving protection must never qualify the receiver as a donor.

Freeze `gods_of_africa_contract_emergency_qualified` only when the issued appeal has genuine current emergency need from the existing host need/emergency owner.
At the paid branch recheck that emergency context against the same host, rather than relying on a UI click or a global disaster flag unrelated to Africa.
For existing family 13, the actual paid helper records the measured 500-PP transaction or measured partial amount at its existing price, then clears only the transfer work.
Its normalized emergency credit cannot exceed the actually paid fraction of the unique obligation.
Emergency material shipped through another actual family records that material subset and uses the same emergency normalizers; do not award emergency status merely because a substitute was offered.
Host aid to a participant is never emergency aid supplied by that participant.

The late-campaign predicate is deterministic and source-based: proven active same-origin host, no final commit, and either `africa_evolution_iii_logged` with host binding to this Event 012 campaign or the explicit host currently has a war.
A globally logged Evolution III from another host/campaign is insufficient; retain the existing Event 012 host/origin proof.
The existing evolution owner must provide the same-origin activation proof if its global flag alone cannot establish it.
Compute this predicate when the material debit actually occurs.
Record only its actual material quantity in `campaign_paid_<kind>_k`, including qualifying voluntary aid; do not count the same quantity twice in total material.
A late negotiation, extension, ceremonial/recognition PP payment, host protection gift, or unpaid promise has zero late-material credit.
For sustained grade qualification, the late-material subtotal must reach one normalized package; a handful of one-unit payments does not qualify as final-campaign support.
The material reward formula also uses that measured subtotal continuously, without a per-click bonus.

### Core territory and Wrath floors

Before observation, prove `event_target:africa_host` exists, its owner/origin/generation matches the participant's current-or-one-explicitly-inherited history, and the participant is not that host.
Save regular explicit participant and host targets for the effect.
From the participant run `every_controlled_state` with `is_on_continent = africa` and `is_core_of = event_target:<proven_host>`.
Increment the cached current count through the explicit saved participant scope; add each previously unrecorded state ID to its durable occupied-state array once.
Do not nest an expensive country/state iterator inside a frequently evaluated trigger.
Do not count foreign ownership alone as current occupation; the controller observation is authoritative for occupation.
Owned African core territory still outstanding is a separate territorial claim check using `every_owned_state` in the same direct participant effect, cached as `gods_of_africa_owned_host_core_count`.
Reconciliation requires both current caches to be zero after actual return; merely ceasing control while retaining the land is insufficient.

The actual territory-return branch saves the selected state before transfer and records its pre-owner/controller and proven host-core status.
After transfer, record a unique positive return only if that state is owned and controlled by the proven host and the participant actually surrendered ownership or control.
Do not convert the present `territory_returned` flag, a territorial PP payment, unrelated border movement, or host conquest into this positive receipt.
The same state can contribute only once to the positive returned-state array, even if subsequently seized and returned again.
New occupation or war still refreshes the negative record.
This uses dynamic actual host cores, not a new list of countries, map regions, or claims.

From cached causes, set/clear the existing `war_floor` and `territory_floor` flags and compute the maximum applicable floor using existing `floor_war`, `floor_territory`, `floor_broken_treaty`, `floor_defiant`, and `floor_recent_extreme` constants.
The present sequential assignments in `gods_of_africa_enforce_wrath_floor` must not let a later lower floor overwrite a higher one.
An actual repaired/accepted agreement can clear its outstanding floor cause, never the prior offense record.
Final grading calls this direct observation once before freezing Wrath, including for archived or capitulated historical participants.

### Agreements and reconciliation

An agreement-breach receipt needs an existing owned agreement identity, a promised relation/obligation, an actual breach, and a once-only outstanding receipt.
Observe the relevant existing protection/reconciliation agreement owner at its explicit cancellation/war callback or bounded owner review.
Expiry, authorized withdrawal, host cleanup, generic refusal, and generic offender selection are not betrayal.
Remove unconditional treaty creation from generic `mark_offender`; retain ordinary offense/punishment behavior separately.
War cancellation writes war history; it writes treaty history only when an actual preceding agreement receipt proves betrayal.
Do not add a new treaty system or world observer.

`gods_of_africa_complete_reconciliation` requires its existing paid offer and host acceptance, plus the actual no-war/no-outstanding-core checks above.
After successful acceptance, retain `prior_defiance`/prior hostility, increment reconciliation count, stamp the current fulfilled count as its recovery baseline, and zero only the explicitly post-reconciliation counters and current recovery streak.
Never zero lifetime contract, quantity, refusal, war, treaty, occupied-state, or longest-streak history.
The existing reconciliation cost and all protection types remain unchanged.
No last-minute paid offer or host leniency immediately restores Favored.

## Twelve-factor deterministic classification

At the authoritative endpoint, neutral-retire any still-open ordinary demand before evaluating its denominator.
Let `N = issued - retired`, `F = fulfilled`, and `R = F / N` only when `N > 0`.
Require the accounting invariant `N = F + failed + refused + broken_by_war` at that endpoint.
If it does not hold, flag the participant grade unresolved; do not repair it by inventing fulfilled or failed contracts.
Zero eligible demands means `R = 0`, with a separate `no_contract_history` state, never 100 percent.
For engine comparison use `100 * F` against `ratio_percent * N`, rather than rounded division.

Normalized material packages use actual cumulative native quantities and the following central denominators.
These are grading/reward valuation anchors, not changes to any demanded cost, capacity gate, substitute price, protection type, or family-13 price.

| Actual kind | Native units per normalized package |
| --- | ---: |
| Infantry equipment | 1000 |
| Support equipment | 500 |
| Trucks | 100 |
| Artillery | 50 |
| Armor | 25 |
| Aircraft | 50 |
| Fuel | 1000 |
| Convoys | 20 |
| Trains | 20 |
| Manpower | 10000 men |

Let `M` be the sum of actual paid material divided by those denominators, `V` its voluntary subset, `L` its late-campaign subset, and `E` its emergency subset plus `emergency_paid_pp / 500`.
Emergency PP contributes to emergency conduct, not `M`, `V`, or `L` material quantities.
Pure recognition, industrial PP, access, and resource-rights effects may fulfill a genuine contract, but do not manufacture material contribution.
Use retained actual quantities, not counts, to derive these subtotals.
Exceptional voluntary/emergency/campaign aid means the corresponding subtotal reaches 1.0 package.
For arithmetic preserve quantity ledgers in thousands, and derive milli-packages with `paid_kind_k * (1000000 / kind_denominator)`; sum after limiting each term to the relevant comparison/reward bound.
Do not repeatedly round each small payment to a whole package.
The milli-package calculation keeps a one-man payment representable as 0.1 milli-package while offering no per-click qualification.

| Accepted factor | Exact final consequence |
| --- | --- |
| 1. Current Wrath | Existing low-Wrath Favored boundary remains strictly below 40; Respected strictly below 70; extreme Wrath strictly above 80 is Enemy. These boundaries are not reused as contribution scores. |
| 2. Full compliance ratio | Full-original and honored paid substitutes form `F`; Favored requires 80/90/80 percent by doctrine; Respected requires at least 50 percent or the exceptional-aid/return path below. |
| 3. Compliance streaks | Favored requires current and longest fulfilled streaks of 2/4/3 by doctrine; adverse unique closures reset current streak. Negotiation and partial clicks do not increase it. |
| 4. Voluntary aid | `V`, actual outbound material, supplies reciprocal exceptional cooperation and the material-reward contribution premium. Existing voluntary count supports receipt audit only. |
| 5. Emergency aid | `E`, actually paid qualified emergency assistance, supplies exceptional cooperation; unpaid offers and host gifts do not. Family 13 remains priced exactly as in its owner. |
| 6. War and occupation history | Current war/current controlled or owned African host-core territory is unresolved major hostility. Prior war/occupation remains a rehabilitation barrier even after the immediate condition ends. |
| 7. Broken agreements | Actual unresolved agreement breach is Enemy. A prior resolved breach remains a rehabilitation barrier; generic offending does not invent a treaty. |
| 8. Territory returned | Verified unique returned-state count supplies positive restitution; all current owned/controlled host-core territory must be relinquished for rehabilitation. It does not erase prior occupation. |
| 9. Permanent defiance | Existing unresolved opt-out/live defiance is Enemy; durable prior-defiance survives acceptance and requires demonstrated recovery. |
| 10. Reconciliation | Only paid, host-accepted reconciliation resolves pardonable outstanding offense. It opens post-acceptance recovery accounting; an offer alone cannot change the standing. |
| 11. Final campaign support | `L >= 1` supplies exceptional sustained support and `L` supplies a contribution premium; only actual late material, with explicit host proof, counts. |
| 12. Doctrine | Reciprocal covenant rewards cooperative need-based history more readily and multiplies material reciprocity; sovereign exaction requires a longer/higher compliance record; strategic ambiguity retains its wider failure/refusal tolerance. |

The thirteenth listed spec input, final Strength, is frozen for material capability scaling below.
It does not excuse hostility or turn an unpaid participant into Favored.

Evaluate in the existing priority order Enemy, Favored, Respected, Distrusted, preserving enum values 4/1/2/3.
No random score, weighted AI change, national spirit ladder, or public grade meter is introduced.

**Enemy:** any current war with the proven host, current outstanding owned/controlled host-core territory, actual unresolved treaty breach, unresolved permanent opt-out/live defiance, an actual unresolved major-offense mark, or Wrath above 80.
Also classify three or more unique refusals as Enemy until a valid host-accepted reconciliation; afterward this repeated-refusal test uses post-acceptance refusals while retaining the lifetime record.
Do not clear live major-offense marks merely to improve a grade.
A generic offender-selection flag without its source cause must be reconciled to its actual offense, not blindly relabeled a broken agreement.

**Favored:** no Enemy cause, Wrath below 40, `M >= 2`, the doctrine's minimum fulfilled count and ratio, both streak requirements, no unique failures in the applicable record, and its exceptional-cooperation test below.
Normally the failure record is lifetime unique failures; after genuinely accepted reconciliation use the post-acceptance failures but retain the recovery barrier.
Any prior defiance, war, occupation, or actual treaty break additionally requires genuine reconciliation, zero post-acceptance failures/refusals, and at least four post-acceptance fulfilled contracts with current streak at least four.
Thus a forgiven enemy cannot jump directly to Favored at the council.

| Doctrine | Minimum fulfilled | Ratio | Current and longest streak | Additional positive record |
| --- | ---: | ---: | ---: | --- |
| Reciprocal covenant | 2 | 80% | 2 | `V >= 1`, `E >= 1`, `L >= 1`, at least one verified returned state, or at least four fulfilled contracts. |
| Sovereign exaction | 4 | 90% | 4 | `V + E + L >= 2`, or at least six fulfilled contracts. |
| Strategic ambiguity / no chosen doctrine | 3 | 80% | 3 | `V + E + L >= 1`, or at least five fulfilled contracts. |

**Respected:** no Enemy cause, Wrath below 70, unique failures and refusals each strictly below two, or strictly below three under strategic ambiguity.
Use post-acceptance adverse counts after accepted reconciliation; retain all lifetime marks.
Also require either `N > 0`, `F >= 1`, and `R >= 50%`; or `V >= 1`; or `E >= 1`; or `L >= 1`; or a verified returned state.
Prior major hostility additionally requires genuine reconciliation and at least two post-acceptance fulfilled contracts with current streak at least two.
This creates a meaningful mixed-history result without granting a reward for enrollment alone.

**Distrusted:** every remaining proven surviving historical participant, including zero-conduct enrollment, procedural-only history, unrecovered past hostility without a current Enemy cause, or an inconsistent record outside the better gates.
Ordinary diplomacy remains possible and negative memories remain available to existing Event 012 diplomatic consumers.
Distrusted and Enemy receive no physical settlement obligation or automatic PP grant.
Existing relation memories, hostile exclusions, and World Is One record consumers remain attached to their four standings.
No new country, focus route, diplomatic institution, or super-event is required.

## Capability-scaled obligation with no free audience grant

Freeze once on the host `gods_of_africa_settlement_final_strength` and `gods_of_africa_settlement_final_doctrine` before the census classification pass.
All participant snapshots use that same frozen capability, not a Strength value recomputed after another recipient is paid.
Retain the existing participant `settlement_strength`, `settlement_doctrine`, generation, origin, and historical-generation fields.

Define `S = clamp(frozen Strength, 0, 100) / 100` and `C = min(16, M + 0.5 * V + 0.5 * L)`.
The voluntary and late quantities are premiums over their already counted material, not second transfers or extra contract fulfillments.
Family-13 PP, protection received, negotiations, late ceremonial clicks, and enrollment have zero contribution to `C`.
Use milli-packages to calculate `C` without rounding a payment into a whole package.

For Favored, `B = (1 + 2 * S) * doctrine_multiplier`, with reciprocal covenant 1.25 and sovereign exaction, strategic ambiguity, or no choice 1.0.
For Respected, `B = 0.25 + 0.75 * S`, with doctrine multiplier 1.0.
For Distrusted/Enemy, `B = 0`.
These are deterministic economic normalizations, not AI/probability weights.

The one-time equipment entitlement is `floor(min(equipment_ceiling, 1000 * C * B))` actual infantry-equipment units.
The separate fuel entitlement is `floor(min(fuel_ceiling, 500 * C * B))` actual raw fuel units.
Favored ceilings are 50000 equipment and 25000 fuel; Respected ceilings are 10000 equipment and 5000 fuel.
Zero actual material yields zero entitlement even if diplomatic history qualifies for Respected.
There is no flat 2500/1000 base added for being on the participant list.
A substantial sustained contributor can receive tens of thousands of rifles plus operational fuel, rather than PP dust, within Africa's real donor capacity.

All new constants live in the existing `common\script_constants\012_africa_gods_constants.txt`.
Each new top-level group must start with its mandatory `schema`; no naked tuning namespace is allowed.
Use `schema = { any_key = yes data = int }` for `gods_of_africa_contract_close`, `gods_of_africa_grading`, `gods_of_africa_contribution_units`, and `gods_of_africa_reward_units`.
Use `schema = { any_key = yes data = fixed_point }` for `gods_of_africa_reward_scale`.
Access arithmetic constants through `constant:<group>.<key>`; do not cross-reference one script-constant file from another.

| Group | Required recommended entries |
| --- | --- |
| `gods_of_africa_grading` | `ratio_percent_reciprocal = 80`, `ratio_percent_exaction = 90`, `ratio_percent_ambiguity = 80`, `ratio_percent_respected = 50`, `fulfilled_reciprocal = 2`, `fulfilled_exaction = 4`, `fulfilled_ambiguity = 3`, `streak_reciprocal = 2`, `streak_exaction = 4`, `streak_ambiguity = 3`, `exceptional_packages_milli = 1000`, `favored_material_packages_milli = 2000`, `recovery_favored = 4`, `recovery_respected = 2`, `repeated_refusals = 3`, `reciprocal_alternative_fulfilled = 4`, `exaction_alternative_fulfilled = 6`, `ambiguity_alternative_fulfilled = 5`, `exaction_exceptional_milli = 2000`. Use existing Wrath/failure/refusal constants where their exact existing boundary applies. |
| `gods_of_africa_contribution_units` | The ten denominators in the quantity table, plus `units_per_thousand = 1000`, `milli_packages_per_package = 1000`, `emergency_pp_per_package = 500`. |
| `gods_of_africa_reward_units` | `equipment_per_package = 1000`, `fuel_per_package = 500`, `favored_equipment_ceiling = 50000`, `favored_fuel_ceiling = 25000`, `respected_equipment_ceiling = 10000`, `respected_fuel_ceiling = 5000`, `batch_equipment_ceiling = 20000`, `batch_fuel_ceiling = 20000`, `availability_search_iterations = 16`. |
| `gods_of_africa_reward_scale` | `strength_divisor = 100`, `contribution_packages_ceiling = 16`, `voluntary_premium = 0.5`, `campaign_premium = 0.5`, `favored_base = 1`, `favored_strength_multiplier = 2`, `reciprocal_multiplier = 1.25`, `other_doctrine_multiplier = 1`, `respected_base = 0.25`, `respected_strength_multiplier = 0.75`, `army_equipment_reserve_fraction = 0.10`. |

These entries replace the final reward helper's fixed payout/PP branch use, not old tribute/protection/relief cost constants.
Do not remove old constants while other live consumers still use them.

## Frozen source, owed balances, and bounded delivery

On each recipient retain `gods_of_africa_reward_source_id`, `gods_of_africa_reward_source_generation`, `gods_of_africa_reward_source_origin_id`, and `gods_of_africa_reward_receiver_id = THIS.id`.
Source is the actual settling HOST object, not whichever object a later global `africa_host` target points to.
Keep separate normal fields `gods_of_africa_reward_equipment_entitlement`, `gods_of_africa_reward_fuel_entitlement`, `gods_of_africa_reward_equipment_owed`, `gods_of_africa_reward_fuel_owed`, `gods_of_africa_reward_equipment_delivered`, and `gods_of_africa_reward_fuel_delivered` in native units.
All are initialized once from the frozen grade, never recalculated after later aid, doctrine, or host-pointer changes.

Use `gods_of_africa_settlement_obligation_committed` for entitlement initialization and `gods_of_africa_settlement_diplomacy_applied` for once-only standing relations.
Preserve `gods_of_africa_settlement_reward_granted` as the permanent complete-delivery receipt; set it only after both owed balances are zero.
A zero-entitlement standing can set the complete-delivery receipt without a grant.
For an owing participant use `gods_of_africa_settlement_delivery_pending`; partial deliveries retain it and never set complete-delivery.
Report acknowledgement consumes only report-pending presentation, never any owed amount, contribution history, outcome, or delivery receipt.

The committed HOST retains the existing `gods_of_africa_candidate_registry` as its bounded historical census after live cleanup.
Do not clear it, discover a second audience, create another participant registry, or revive ordinary participation merely to deliver settlement goods.
Maintain host `gods_of_africa_reward_equipment_owed_total_k` and `gods_of_africa_reward_fuel_owed_total_k` in thousands of native units and `gods_of_africa_settlement_delivery_initialized`.
Thousands avoid a raw total of 50 million overflowing when a large historical audience receives capped entitlements.
Recompute these totals from valid owing receipts in the existing census at the beginning of each player/owner-triggered batch; do not trust a count of participants as a quantity total.
A vanished receiver is excluded from a current delivery batch but its retained receipt is not transferred to a substitute country.

Change the owner endpoint into three bounded phases over that same census:

1. Close ordinary dispatch with the existing host final-commit receipt, freeze host capability/doctrine, neutral-retire unfinished contracts, observe conduct, and classify every valid historical survivor.
2. Initialize each valid recipient's immutable material obligation and standing diplomacy, accumulating both owed totals.
3. Deliver a bounded donor-backed batch proportionally, then finalize ordinary authority and issue `.608` using the captured regular settlement host.

Do not pay recipients while the total obligation is still being discovered.
Do not clear a participant's historic inputs before its classifier/entitlement runs.
If either classification or obligation initialization is unresolved, preserve the evidence and do not pretend that zero entitlement completed it.

### Protected actual donor budget

For equipment, compute `equipment_floor = max(existing capacity_floor_equipment, ceil(0.10 * num_target_equipment_in_armies_k@infantry_equipment * 1000))` in the actual source HOST.
The existing floor is 500 equipment; keep the operating reserve and army requirement independent of owed totals.
For the common-defence ledger, spend no more than `max(0, africa_common_defence_stockpile - existing capacity_floor_equipment)`.
For fuel, spend no more than `max(0, floor(fuel_k * 1000) - existing capacity_floor_fuel)`; its existing floor is 500 raw fuel.
Receiver fuel headroom is `max(0, floor((max_fuel_k - fuel_k) * 1000))`; a full recipient fuel tank does not extinguish the fuel obligation.

Native spendable infantry is established with `has_equipment` in the source COUNTRY, not the common-defence scalar alone.
Search the greatest integer shipment `q` between zero and the smaller of batch ceiling, owed total, and spendable common ledger for which `NOT = { has_equipment = { infantry_equipment < q_plus_floor } }` is true.
`q_plus_floor` is a normal/temporary arithmetic value prepared before the check.
A bounded integer binary search needs at most 16 iterations over the 0–20000 batch range and does not enumerate variants or countries.
There is no required whole-world or global daily hook.
The actual immediate stock delta still verifies the delivered quantity after `send_equipment`.

Use the minimum of native spendable infantry and spendable common ledger as the equipment batch budget, limited to 20000 units.
Use actual spendable source fuel as the fuel batch budget, limited to 20000 units.
Neither budget assumes that promises, final Strength, expected production, or a bookkeeping reserve created inventory.
Equipment and fuel are independent components; a fuel shortage cannot force an available equipment shipment into a PP branch.

### Proportional source allocation and exact once-accounting

Within each component, compute its valid pending total `T_k` in thousands and freeze its physical batch budget `A` in native units.
For equipment, each recipient's allocation basis is its positive equipment owed balance.
For fuel, each recipient's allocation basis is `min(fuel owed, current receiver fuel headroom)`; zero-headroom recipients remain owed but are excluded from that component's currently claimable total.
`T_k` sums these component-specific allocation bases, while host permanent owed totals continue to include every undelivered obligation.
For each valid recipient with `allocation_basis_k = allocation_basis / 1000`, allocate `floor(A * allocation_basis_k / T_k)` units, capped by its live owed balance and fuel headroom where applicable.
Multiply `A * allocation_basis_k` before dividing; do not store a tiny `A / total_units` or `owed / total_units` fraction first.
The largest intermediate is `20000 * 50 = 1000000` for equipment, below the problematic multi-million raw audience total.
If `T_k = 0`, perform no division and no shipment.
Allocate integer rounding residue in one additional census pass, at most one unit per eligible recipient, in existing census order while budget remains.
Use the bounded initial allocation pass and one residual scope-array pass rather than an unbounded numeric loop; each payment still rechecks its actual source reserve.
Fuel that cannot fit a recipient stays with Africa; its blocked share is not classified as rounding residue and is not distributed one unit at a time.
The next explicitly triggered batch recomputes the available audience/headroom and can supply those unpaid balances when delivery is possible.
Never consume a source budget for a blocked recipient.

For each transfer, save regular explicit donor/receiver targets from the actual HOST/census transaction, and verify source ID/generation/origin, recipient ID, immutable obligation, valid standing, and positive owed quantity.
A forged `FROM`, an unrelated census candidate, a clone with another owner ID, or a later global host replacement cannot pass this gate.
The donor effect uses native `send_equipment = { type = infantry_equipment amount = <verified shipment variable> target = event_target:<captured_receiver> }`.
The installed vanilla precedent uses `type`; current Gods call sites use `equipment`, so the parent must validate the accepted engine spelling against the installed rule and actual send result rather than silently relying on that discrepancy.
Do not create recipient equipment with `add_equipment_to_stockpile`, unlock recipient equipment technology for the gift, or require a DLC/market transaction.

Immediately measure donor decrease and recipient increase.
For delivered infantry `q_actual`, subtract exactly `q_actual` from the host common-defence ledger and the recipient equipment owed balance, add it to equipment delivered, and subtract `q_actual / 1000` from the host owed total.
For fuel, first reserve/check the recipient headroom and source floor, debit through the existing `remove_fuel_from_stockpile` helper, credit exactly the same raw fuel amount, measure both sides, and update only actual delivered fuel accounting.
Never debit the common-defence infantry ledger for fuel.
If actual transferred quantity is less than the requested quantity, consume only actual delivery from the obligation; preserve the remainder.
A source/receiver delta mismatch is a transaction defect requiring parent investigation, not permission to print compensating equipment/fuel.
No later report or replay retries the already delivered portion.

After both owed balances reach zero, set `settlement_reward_granted`, clear delivery-pending, retain entitlement and delivered totals, and hide the shipment action for that receiver.
The invariant for each component is always `entitlement = delivered + owed`, all values nonnegative.
Every increase of recipient inventory must be matched by a native donor decrease; every common-defence ledger debit must match actual infantry delivered.

### Deferred delivery through the existing row

Repurpose `gods_of_africa_commit_settlement` in `common\decisions\012_africa_gods_decisions.txt:1011–1065` after the endpoint into the settlement shipment action.
Retain its pre-endpoint owner-commit behavior.
In its end phase, use the retained candidate census, exact immutable source/receiver receipts, and pending owed balances instead of live membership/active-Gods triggers.
The existing HOST category visibility becomes `(ordinary active host) OR (this COUNTRY is an exact committed settlement source with valid pending obligations)`.
This end-phase branch must check the actual decision actor directly; it must not follow the global host pointer.

A valid end-phase click calls `gods_of_africa_deliver_settlement_obligations` on that owning HOST and distributes one bounded batch fairly across its valid pending census.
It does not give the clicked target priority over others, recommit the final standing, reopen demands, or reissue all reports.
This provides an explicit owner-triggered claim/delivery route for stocked material after the initial batch, without a clock, new mission, extra category, new row family, or new window.
If the donor has no spendable equipment/fuel, keep the row visible and disabled with the concrete reserve/stock requirement; the debt survives.
If the old settling source vanishes or its immutable identity changes, freeze remaining owed receipts as undeliverable pending evidence; do not redirect them to a successor or a new global host automatically.
A later source recovery/obligation transfer would need its separately accepted identity-safe owner transaction and is not designed here.

Existing AI weights are not chosen or patched by this plan.
The repurposed decision's shared effect must support an AI owner as well as a human owner, using exactly the same source/receipt/reserve gates.
The parent must route the affected existing decision availability/score and any requested weight change through `chaosx_ai_probability_auditor`, beginning with `hoi4.probability_inspect`; a weight patch requires the separate baseline and same-scenario comparison.
Deterministic grading/normalization is not a custom random pool.

## Existing presentation and exact wording

Keep `.608` and `GFX_report_event_012_africa_gods_settlement` in `interface\012_africa_event_pictures.gfx`.
Reuse `GFX_goal_012_africa_gods_continental_settlement` for the repurposed row, and the existing category icon/picture.
No new artwork, icon, portrait, animation, country, tree, window, or super-event request is made.
The native category is an ordinary decision surface; it does not have an event-owned scripted GUI attachment.
Do not assign the shared decision window to `chaosx_event_ui_worker` or change its layout as part of grading.

Keep Strength/Wrath as the mechanic's public values.
The final standing is an outcome label, and its shipment tooltip reports actual material units and outstanding obligation, not a third continuously tracked favor currency.
Do not display `M`, `V`, `L`, internal ratio cutoffs, every historic counter, or the economic normalization formula as a meter.
The user explicitly requests exact UI wording in this bounded handoff; the following selected strings are therefore implementation content rather than unresearched flavor examples.

| Surface/key | Selected text and binding |
| --- | --- |
| End-phase row name `gods_of_africa_settlement_delivery_name` | `Deliver settlement support` |
| End-phase row description `gods_of_africa_settlement_delivery_desc` | `Africa's settlement promises remain binding. Send available equipment and fuel to the countries owed support.` |
| Effect `gods_of_africa_settlement_delivery_effect_tt` | `Distribute available infantry equipment and fuel among the countries owed settlement support. Africa retains its operating reserves.` |
| Disabled stock reason `gods_of_africa_settlement_delivery_stock_tt` | `Africa needs infantry equipment or fuel beyond its operating reserves.` |
| Receiver/source mismatch `gods_of_africa_settlement_delivery_source_tt` | `This settlement must be supplied by the African government that made it.` |
| Complete result `gods_of_africa_settlement_delivery_complete_tt` | `All promised equipment and fuel have been delivered.` |
| Receipt amount `gods_of_africa_settlement_delivery_amounts_tt` | `Delivered: [equipment delivered] infantry equipment and [fuel delivered] fuel. Still owed: [equipment owed] infantry equipment and [fuel owed] fuel.` Bind these placeholders to the participant's frozen normal receipt fields, not host work values. |
| Frozen-source unavailable `gods_of_africa_settlement_delivery_unavailable_tt` | `The government responsible for this shipment cannot currently deliver it. The unpaid balance remains recorded.` |

The report's standing paragraph uses a concise cause summary selected from the frozen grade: sustained fulfilled obligations and aid, mixed cooperation, inconsistent conduct, or unresolved hostility.
Its material paragraph distinguishes delivered goods from goods still owed.
Acknowledgement promises no additional transfer and erases no accounting.
Resolve host naming in `.608` through the captured regular `gods_of_africa_settlement_host` carried by that report chain, never a replaced global pointer.
Ordinary decision name/description switching and tooltip bindings belong in the existing Gods localisation/scripted-localisation owners.
No final gift text may say that promised equipment has arrived when only the obligation was recorded.

## Quantitative acceptance scenarios

These are selected deterministic fixture outcomes, not observed game runs or a probability balance claim.
Use the same named cases for parent production-helper/decision validation and the separately scoped AI review where availability affects existing scores.
All material values below are native units and all supplied source identities must match the current or explicitly inherited origin contract.

| Scenario | Required result |
| --- | --- |
| `G12_zero_history` | Genuine enrolled survivor with `issued = 0`, no paid material/return/hostility, Wrath 8: `N = 0`, no automatic perfect ratio, Distrusted, zero entitlement, one permanent outcome. Never-enrolled census object receives no outcome at all. |
| `G12_consistent_donor` | Reciprocal, six fulfilled material contracts, `N = 6`, current/longest streak 6, no failures/refusals, Wrath 8, `M = 8`, `V = 2`, `L = 2`, Strength 80: Favored, `C = 10`, `B = 3.25`, 32500 equipment and 16250 fuel entitlement. Initial equipment batch is at most 20000; a later owned batch supplies the remainder from real stock. |
| `G12_negotiation_only_spam` | One issued contract, any number of procedural history/partial-kind extension rows, zero actual payment, ultimately neutral-retired at endpoint: `N = 0`, `F = 0`, streak 0, material 0, Distrusted, zero material. If it ends in actual refusal, `N = 1`, refused 1, no fake fulfillment. |
| `G12_high_wrath_offense` | Any contribution with Wrath 90 or current proven war/occupation/unresolved treaty/opt-out: Enemy, no material entitlement. Existing hostility/exclusion consumers retain the actual offense. |
| `G12_partial_then_full` | One 1000-infantry demand: actual partial 500 and actual final remaining 500 yield issued 1, fulfilled 1, `N = 1`, ratio 100%, current streak 1, 1000 actual paid infantry. Neither click alone creates two fulfillments or satisfies the minimum Favored streak. A replay adds zero quantity and zero count. |
| `G12_honored_substitute` | An accepted substitute actually supplies its full negotiated remaining obligation: the original tuple closes once, honored-substitute 1, fulfilled 1. The material ledger uses the actual substitute kind and actual quantity. Submission, rejection, or failed affordability closes nothing. |
| `G12_forgiven_defiance` | Paid host-accepted reconciliation removes opt-out but retains prior-defiance and lifetime offense. Immediate final council is not Favored; two subsequent valid fulfilled contracts can qualify for Respected; four consecutive post-acceptance fulfillments plus all Favored doctrine/ratio/material conditions can qualify for Favored. A new refusal/war resets that recovery. |
| `G12_inherited_same_origin` | Archived historical survivor from the one explicitly inherited generation and matching origin/owner keeps issued/paid/streak/offense history and can be classified exactly once. Another older generation, wrong origin, or wrong owner ID is rejected, not treated as zero-conduct enrollment. |
| `G12_weak_host_many_donors` | 1000 valid Favored donors with the consistent-donor quantities above but Strength 20 have `B = 1.75`, 17500 equipment/8750 fuel each. Host has only 1500 spare native infantry and at least 1500 spare common ledger: total owed is 17500k, base share is `floor(1500 * 17.5 / 17500) = 1` rifle each, with 500 remaining rifles distributed as rounding residue. Exactly 1500 rifles leave the host; all other balances remain owed. Do not multiply a free package or PP fallback by 1000. |
| `G12_strong_host_low_contribution` | Reciprocal, two valid fulfilled contracts plus qualified voluntary aid, Wrath 8, `M = 3`, `V = 1`, `L = 0`, Strength 100: Favored if both streaks are 2, `C = 3.5`, `B = 3.75`, equipment 13125 and fuel 6562. A single recent shipment with streak 1 is not Favored despite large stock. |
| `G12_strong_host_high_contribution` | Reciprocal, sufficient compliant history, `M = 12`, `V = 2`, `L = 4`, Strength 100: `C = 15`, unconstrained equipment 56250/fuel 28125, entitlements 50000/25000 at the central ceilings. Source-funded batches are required; a large accounting reserve without native stock delivers zero. |
| `G12_respected_material` | Default doctrine, `N = 4`, `F = 3`, one unique failure, Wrath 45, `M = 3`, `V = L = 0`, Strength 80: Respected, `B = 0.85`, equipment 2550 and fuel 1275. Diplomatic-only cooperation with `M = 0` receives the standing diplomacy and zero fabricated material. |
| `G12_stock_lost_before_transfer` | Preview quoted sufficient stock, but the source falls below floor before click or a receiver loses headroom: effect recomputes physical budget and component cap. It transfers only current actual available goods or none; entitlement remains frozen, owed is preserved, and complete-delivery receipt remains absent. |
| `G12_emergency_paid_case` | Genuine frozen/current emergency family 13, actual participant debit/host credit 500 PP: `E` gains 1, emergency-paid PP gains 500, material contribution gains zero. Host leniency/protection, unpaid emergency offer, unrelated disaster, and negotiation each yield zero emergency credit. The 500 price is unchanged. |
| `G12_actual_late_support` | A real 1000-infantry payment during same-origin Evolution III or host war records one material package in both total and late subset, then contributes `1 + 0.5` packages to `C`. Earlier material has no late premium; late 10-unit material contributes its quantity only and does not independently meet the 1-package exceptional-support gate. |
| `G12_return_and_reoccupation` | A specific proven host-core state actually returned to host ownership/control counts once. Repeated return of that ID cannot farm positive state count. Reoccupation restores current hostility and floor regardless of the positive receipt. |
| `G12_replay_new_host_pointer` | Repeat final commit, reward call, `.608` acknowledgement, and deferred batch after full delivery: no regrading/debit/gift. Replace global `africa_host` with another actor: old source/receiver receipts remain bound to the original settling object; another actor cannot pay, steal, or rewrite them. The original source may pay its own pending obligation through its direct actor proof while it still exists and matches identity. |

For each transaction case retain the native donor/receiver before-and-after quantities, common-ledger delta, entitlement/delivered/owed equality, and exact source/receiver identity.
For the many-donor case also retain component totals in thousands, per-recipient shares, rounding residual, and unchanged protected floors.
These are material balance tests, not merely syntax hygiene.

## Read evidence, limits, and parent implementation handoff

The accepted full-spec SHA-256 read for this task is `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798`.
The core effects snapshot was `ea62d37f38e9c3f19c1c9be6e6a483281f7358d93998028176b87c6349096a2f`; core triggers `8abaf42a84646715583f705b31150b786b6050cc4e428c36c91126c88deae28d`; Gods constants `75e120b52aa741eb3614b046a9f50dc4b8e2de76374ff669b79f68ece4a3f540`.
Settlement effects were `0d636486d9a49ac7d6107b95e02cd2d4a5df4334f2b349a8496361b0f2781046`; settlement triggers `f56c45b8813807be97f69f72af3ea05e97cbffc7529febd4a19c8856f3dfd4d1`.
The shared tree may move while the parent works; these are inspected snapshots, not a repository-wide freeze.

### Installed and offline reference evidence

Installed reference root is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline wiki root is `<workspace>\paradox_wiki`; no online Paradox wiki was used.
Successful live `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup` routes established availability and returned the following revision-bound sections; direct local reads supplied the additional pertinent sections.

| Reference path relative to its root | Read lines and rule | Revision/hash where available |
| --- | --- | --- |
| Installed `documentation\script_concept_documentation.md` | 216–222: scoped-variable access to fixed-point `constant:` values; supported fields only. | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1–34: mandatory first-entry schema, `int` and `fixed_point`, and no assumption that every field accepts constants. | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `documentation\effects_documentation.md` | 6550–6558 native COUNTRY equipment send; 1388–1396 COUNTRY fuel addition; 3800–3814 controlled-state iterator; 4076–4090 owned-state iterator; 6496–6511 local/global event-target effects. | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | 3835–3849 equipment stored/target presence; 3957–3974 raw fuel amount check. | Context revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; pertinent sections read locally. |
| Installed `documentation\dynamic_variables_documentation.md` | 385–387 fuel thousands; 483–485 maximum fuel thousands; 557–564 equipment quantities; 687–692 army required equipment/raw and thousands. | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Offline `Effects - Hearts of Iron 4 Wiki.md` | 2246–2263, including native send removing source equipment and shortfall behavior; the live reader returned a continuation within the long table, so only the read portion is claimed. | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 303–327: regular event target lifetime includes fired event chains, then ends; it is not indefinite deferred-delivery storage. | Local direct read; durable deferred identity uses normal fields and direct owner scope instead. |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | 526–539: country-owned/core/controlled state iterators and their actual domains. | Local direct read. |
| Offline `Decision modding - Hearts of Iron 4 Wiki.md` | 530–548: targeted decision ROOT actor/FROM target, bounded target arrays, continuously checked visibility/availability, and explicit activation. | Local direct read. |
| Installed `common\scripted_effects\SAF_german_coup_effects.txt` | 52–93, especially real non-AI branch 83–90: `send_equipment` uses literal `type`, `amount`, and target in donor COUNTRY scope. Do not copy its separate AI stockpile remove/add workaround. | Live source lookup revision `82b215f3acdd27296442f9556427e2bb3911a0a5d73db00cd5c51b57ff1e61fa`, plus underlying direct read. |
| Mod `common\scripted_effects\chaosx_dynamic_effects.txt` | 810–812: `remove_fuel_from_stockpile` negates its temp amount then calls native `add_fuel`. | Local direct read; reuse this existing helper. |

The first event context bundle reported omitted On actions and Localisation sources; this handoff does not claim full engine/reference coverage from that bundle.
No new on-action, localisation formatting construct, GUI layout, or clock is proposed.
The parent must obtain the relevant installed/offline documentation sections for its actual integration edits and retain their citations.
The live source lookup schema exposed in this session did not offer `view`/`keyPath`; no unsupported structural route was assumed.

### Regional research basis

The [OAU Charter, 25 May 1963](https://au.int/en/treaties/oau-charter-addis-ababa-25-may-1963) and the African Union's [institutional overview](https://au.int/en/overview) connect continental solidarity and cooperation with territorial integrity and liberation.
That is a later historical analogy supporting real aid, restitution, and a distinction between occupation and ordinary bargaining.
It is not evidence for a real shared African pantheon or a 1930s Gods institution.
The accepted spec explicitly treats the Gods doctrine as fictional and plural African religious traditions as distinct.
No historical ritual, quotation, deity identity, border claim, or new political route is invented from this analogy.

### MCP evidence and unresolved visual/runtime conclusions

Connected reference/source routes returned successfully for workspace `mod_chaos_redux_ea3b2d67c2c0`.
`hoi4.event_inspect` tracing `chaosx.nr12.608`, depth 1, nodes 8, edges 12, without helper expansion, returned `EVENT_INSPECTED_PARTIAL` at revision `97de3911c913e133e3bcea9fa55b020301f6c9f1da3a379805087dab5ccc87bc`.
Its direct-source boundary does not prove the proposed ledger or payout behavior.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/480eab4c48ab4d38974ebac7589c76a0c952836fbaa8aa7fa41285cefb5a104b/df82c1d1251464a4d1b85c427f1527772a53a399a55cb71d8d01a75107b197b8/event-trace-97de3911c913.json`.

`hoi4.event_render` options for the same event, depth 1/nodes 2/no helper expansion, returned `EVENT_RENDERED_PARTIAL` with the same revision and PNG hash `4eb3a154be6714cb16ecf1005d5529b98ee13e5f12c3a703fe3f25e667572fc7`.
PNG resource: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eb3a154be6714cb16ecf1005d5529b98ee13e5f12c3a703fe3f25e667572fc7/8b633f031142f2bb09eac027822f842e9c215369e513061d819244e03a536aa7/event-options-97de3911c913.png`.
A bounded PNG resource read failed with `-32603: Artifact provenance manifest is unavailable`.
Accordingly, image inspection and the event visual conclusion remain unresolved; a render status is not proof that the image was reviewed.
No comparison against implemented grading source is possible because this subagent writes no gameplay.

`hoi4.gui_inspect` for the native `countrydecisionview` shell and scenario `gods_settlement_native_category_baseline` returned `GUI_INSPECTED`, revision `bb78dcd13e0bf7050731568d6aa0d4d97f7e48697c535a7e104a013fa61bcaf7`.
It inspected 14 shell elements and reported clipping/overlap warnings and two unsupported fields; it did not establish rendered Gods row/content coverage.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea4834691f9e41551667bad08cdce2caa71d48a232eb0bac6fc812235748b855/fb0d58a58b9a507bec886ba47ff7eec062c2f2520e843f8d333537c73975e61a/gui-inspect.bb78dcd13e0bf705.json`.
Native-window render was requested for 1920×1080 and 1366×768 at scale 1 with normal/disabled/long-text states; no final result was observed before the user's immediate-delivery instruction.
The pending result and an unbound native shell cannot satisfy final category visual acceptance.
These warnings are parent-owned evidence, not authority to modify a shared window in this task.

`hoi4.map_inspect` lookup-only query `Africa`, limit 3, returned `MAP_LOOKUP_COMPLETED`, revision `ae5a6a499910f1e63f67794b754ac4261499b39a27a1ba175d0ae7365b8511e3`, with 1081 states and three query matches.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b7c08cc7049ffdd31d6071f126d9d6a278fc5f2edae070a69a18fbac661966/c120d05a6c4d48fd5b276a72f62dfe28ce9148ad0ec0dbb6bf16a5321e1a09fa/map-lookup.ae5a6a499910f1e6.5f54c6f1bff79ef2.json`.
A narrower state-541 lookup/render was requested but its final result was not observed before immediate delivery.
This is no proof of a campaign's dynamically changed cores or occupation; final dynamic core scenarios remain unresolved pending parent evidence.
State 541 is only a bounded tool fixture, not a hardcoded design requirement.

Package/config inspection found `.codex\config.toml` launching the global `hoi4-agent-tools.cmd` in this workspace and installed package `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools`, version 3.6.0.
Its package entrypoints are stdio/http/setup; the inspected package file inventory has technology service/render/query code and documentation, but no standalone Technology Tree Viewer executable/entrypoint.
Record that verified absence within this installed package as a standalone-viewer package gap, independently of working reference/event service calls and technology tool exposure.
This does not claim no viewer exists anywhere else on the machine.
No technology or national-focus tree is designed or changed here; the Gods doctrine enum is not a technology/doctrine tree.
No helper-expansion, job-inspection/cancellation, native-task, rewrite, or external tool-source route was used.
Initial invalid narrow requests were corrected against actual validation feedback; they establish no gameplay failure.

### Parent work and acceptance boundary

Implement only in the existing Gods owners: lifecycle initialization; core contract/payment/refusal/failure/war/reconciliation/voluntary/territory hooks; settlement effects/triggers; current constants; existing decisions/categories; existing Gods localisation/scripted-localisation and `.608` report bindings.
Document helper contracts in the existing settlement/helper Markdown owners and align the event docs after implementation facts exist.
Route workbook alignment afterward to its existing spreadsheet owner; this planner does not edit the workbook or export CSVs.
The parent reviews U1's core membership correction independently and must preserve history eligibility without converting it into live membership.

The parent should accept this selected design explicitly, implement the ledger and source-funded obligation, run the named production scenarios, and obtain decision/payment/localisation/completion audits.
Any availability or weighted behavior affected by the existing row requires the separately routed read-only AI auditor and its probability evidence; this document neither chooses AI targets nor substitutes an arithmetic table for that audit.
Final ordinary-category and event visual conclusions, actual native variant/fuel delta semantics, clone/object lifetime, incomplete legacy quantity proof, and any unavailable evolution-origin proof remain explicit evidence limits until resolved.
Do not claim Gods complete from this plan or from a tool success summary.

Keep this file in `docs\plans\012_africa_plans\subagent_handoffs` until parent disposition is recorded.
On acceptance, promote the twelve-factor rule, numerical anchors, material obligation/delivery contract, and existing-row end phase into the accepted full spec's final-evaluation/reward section, recording the user's authorization and the parent's selected-design acceptance.
Keep source hashes, tool artifacts, defects, and implementation receipts in this handoff or the parent validation report rather than embedding an audit ledger in the source spec.
After implementation link current source evidence and validation limits and mark this tranche `implemented`; retain the separate queued original-host reopening disposition unchanged.

No requested design factor was omitted, no PP/material substitute was accepted, and no new broad mechanic or asset was added by this recommendation.
Implementation and final evidence remain parent-owned and incomplete at handoff.
