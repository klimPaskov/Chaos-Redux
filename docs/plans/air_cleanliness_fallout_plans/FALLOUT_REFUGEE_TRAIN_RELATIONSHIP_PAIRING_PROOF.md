# Fallout Refugee Train relationship pairing proof

## Static implementation evidence

The producer effect `fallout_event_pair_refugee_train_candidate_rows` runs immediately after `fallout_event_build_pilot_candidate_registries` and before the human and AI review passes in `fallout_event_scheduler_reconcile`.

It resets the two global pairing cursors to the typed no-partner sentinel, scans `global.fallout_event_registry_countries`, admits only reviewed registries containing candidate id `constant:fallout_event_candidate_pilot.refugee_train_candidate_id`, retains the two lowest registry indices, and writes reciprocal partner indices into the exact candidate row on both countries.

The mutation is idempotent for a fixed generation. Rebuilding candidate arrays resets every partner slot to the typed no-partner sentinel before the pairing pass runs again. If either selected registry has no exact candidate row, the pass clears its pairing cursors and leaves the candidate rows unchanged.

## Ledger and conflict boundary

The producer does not write `fallout_event_bilateral_*` arrays, ordinary receipts, delayed rows, major arcs, event targets, tags, relations, or dispatch envelopes. Reservation remains owned by `fallout_event_schedule_selected_relationship_candidate` and `fallout_event_reserve_bilateral_transaction`.

The reciprocal candidate trigger remains the exact proof boundary. It authenticates generation, candidate identity, transaction key, class, bilateral opportunity, token pair, bounded visible cost, and back-reference equality. Candidate eligibility still applies the bilateral pair-family memory and capacity gates before reservation.

## Engine-sensitive surfaces not claimed

No HOI4 session was run. This proof does not claim that `any_of` candidate scans, dynamic array assignment, or `var:global.fallout_event_registry_countries^<index>` scope selection have been accepted by the live engine. It does not claim bilateral opening delivery, response dispatch, save recovery, multiplayer synchronization, host authority, runtime Event Log display, or release-floor credit.

The pairing is intentionally dormant because no scheduler activation flag is set. The authored Refugee Train bilateral consumer is wired to the bilateral response envelope in static source, while engine issuance and runtime delivery remain unproven.
