# Fallout Refugee Train bilateral consumer proof

Status: static implementation evidence only.

## Reservation and token contract

The reviewed Refugee Train candidate is id `415` with transaction key `710033`.

`fallout_event_pair_refugee_train_candidate_rows` pairs the two lowest reviewed registries that contain candidate `415`.

`fallout_event_schedule_selected_relationship_candidate` overrides only this candidate's bilateral token payload with opening tokens `1019` and `1020` plus response tokens `1021` and `1022`.

The shared bilateral arrays keep the exact ticket, generation, roles, partner pointers, control modes, visible costs, status, outcome, cancellation, and cleanup receipts.

## Opening route

The reconciler emits an opening envelope only for a reciprocal initiator row with status `reserved` and a due date at or before the current day.

The dispatch matcher requires the human or AI opening token, the matching control mode, the initiator role, the reserved status, the exact partner country, and the exact bilateral row shape.

The opening consumer calls `fallout_event_mark_issued_bilateral_opening_response_pending`.

The terminalizer accepts only the authenticated issued ticket and opening token, then commits both rows to `response_pending`.

The opening consumer pays branch-specific Food, Recognition, and Cohesion costs only after the pair commit succeeds.

## Response route

The reconciler emits a response envelope only for a reciprocal responder row with status `response_pending` and a due date at or before the current day.

The response matcher requires the human or AI response token, the matching control mode, the responder role, the response-pending status, the exact partner country, and the exact bilateral row shape.

The human response offers success, partial, and failure paths with separate visible resource gates.

The hidden AI response uses the initiator's durable branch variable through the authenticated country target and calls the same response resolver.

`fallout_event_resolve_issued_bilateral_response` commits the nonzero outcome to both rows before the current response envelope is consumed.

The existing bilateral reconciler then moves the resolved pair through cleanup pending and hidden cleanup delivery.

## Gameplay effects

Each participant receives branch outcome effects on Food, Recognition, Cohesion, Stability, War Support, family memory, border legitimacy, integration cohesion, and bilateral trust.

Each participant recovers its reviewed state target from the current candidate arrays.

Success improves reclamation, Supply Access, and exposure while adding a successful Refugee Train state memory and family modifier.

Partial resolution improves reclamation and Supply Access more slowly while adding frayed memory and exposure pressure.

Failure increases exposure, reduces Supply Access, records a failed state memory, and applies the broken-train modifier.

## Static checks

The touched Clausewitz files have balanced braces and quoted strings under a local parser.

The touched script and event files contain no literal `<=` or `>=` operators, em dashes, or semicolons.

The localisation file retains its UTF-8 BOM.

No HOI4 process was launched.

## Unproven surfaces

No runtime proof exists for event-token issuance, dynamic country scope selection, save recovery, multiplayer host authority, Event Log presentation, or cleanup timing.

The Fallout scheduler activation flags remain unset.

The four bilateral consumer blocks are not counted toward the `660` release floor.
