# Fallout relationship candidate reservation addendum

Date: 2026-07-26

Status: accepted for dormant reservation-substrate implementation. The Refugee Train consumer was added in the later `2026-07-26_refugee_train_bilateral_consumer_addendum.md`. This addendum does not authorize scheduler activation, a new event range, or release-floor credit.

## Scope

The reviewed candidate producer already carries four relationship-class rows, but the selector rejects them because their complete reciprocal payload is not proven. This tranche adds the fail-closed reservation path without activating any row. It uses only existing candidate ids, transaction keys, event tokens, and bilateral ledger APIs.

The path is deliberately structural. The Refugee Train row now has an authored bilateral response consumer at events `1019` through `1022`, while the other relationship event consumers remain later content tranches with their own accepted addenda.

## Ownership

`common/scripted_effects/fallout_consolidated_effects.txt` owns the relationship-row no-partner sentinel and the authored payload handoff point.

`common/scripted_triggers/fallout_consolidated_triggers.txt` owns the generation-bound reciprocal candidate proof. A relationship row is eligible only when its partner index is current, both candidate registries are current and aligned, and the partner carries the exact reciprocal candidate identity, transaction key, class, bilateral opportunity, event-token pair, visible cost, and back-reference to the source registry index.

`common/scripted_effects/fallout_consolidated_effects.txt` owns the selected relationship wrapper and partner-row lookup. It freezes the initiator and responder response tokens, control modes, visible costs, shared due day, parent arc ticket, and cleanup token, then calls the existing `fallout_event_reserve_bilateral_transaction` API.

`docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`, `README_IMPLEMENTATION_STATUS.md`, and `source_of_truth_map.md` own the proof and status reconciliation.

## Atomic contract

The wrapper loads `event_target:fallout_event_requested_bilateral_partner` from the candidate's frozen partner registry index. It finds the exact same candidate id on the partner row and copies that row's human token and AI token into temporary request fields. The authored visible cost is used for a human-visible participant and is normalized to zero for a hidden-AI participant. The initiator uses the selected country's human or hidden-AI lane. The responder mode is derived from the partner's live AI state. A human-visible lane must carry a positive cost. A hidden-AI lane must carry zero visible cost. Both costs remain bounded by the shared scheduler maximum.

The cleanup token is the candidate identity and the parent arc ticket is the candidate's frozen parent ticket. The wrapper never invents a target, actor, or event id. A missing partner, a mismatched reciprocal row, a duplicate token pair, a stale generation, a full participant ledger, a conflicting issued pair, or a control-mode and cost mismatch returns `fallout_event_transaction_accepted = 0` without mutation.

The existing bilateral API remains the only writer. It allocates one ticket, appends both reciprocal rows, proves both rows, and rolls both rows back when the second commit fails. Exact retries match the complete immutable payload before capacity checks. Human cooldown is applied symmetrically by the existing API. The pair starts in `reserved` status and is not issued by this reservation tranche. The authored Refugee Train consumer marks the exact pair `response_pending` before bilateral dispatch. Other relationship rows remain without a consumer.

## Selection integration

`fallout_event_candidate_row_is_eligible` admits a relationship row only through the reciprocal candidate proof. `fallout_event_commit_selected_candidate` routes relationship rows to the bilateral wrapper and all other classes to the ordinary receipt wrapper. The ordinary receipt reconciliation and ordinary dispatch envelope are skipped for an accepted relationship reservation. The pair is left for the existing bilateral reconciler and an authored relationship consumer.

The Refugee Train row now has a dormant reciprocal pairing pass recorded in `2026-07-26_refugee_train_relationship_pairing_addendum.md`. The pass selects the two lowest reviewed registries that carry candidate `415` and writes each registry index into the other row. The other three relationship rows retain the typed no-partner sentinel and have no authored consumer. No current relationship row reaches the new wrapper until the reciprocal proof, pair-family memory, current participant state, and bilateral capacity gates all pass. No scheduler activation flag is touched, and the reviewed count remains 460 defined blocks and 0 of 660 countable blocks.

## Validation evidence

Static review must confirm balanced Clausewitz blocks, aligned candidate arrays, no new ids, no new scheduler activation setter, no ordinary wrapper call on the relationship branch, and no mutation when the reciprocal proof is false. The bilateral API remains the only ledger writer. This addendum does not claim runtime save, multiplayer, host-authority, or event-consumer proof.
