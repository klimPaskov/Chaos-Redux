# Captured Biological Facility Scenario Audit

Date: 2026-07-22

## Scope and result

This audit traces the captured-facility tranche through its exact source branches. It is implementation evidence for S06-08, not a claim that the complete Stage 7 package or Stage 14 live scenarios are finished.

All deployment and recovery actions remain native land raids. No decision, inferred state, substitute target, country-wide headquarters proxy, payload refund, or periodic world pulse exists in this tranche.

## Scenario matrix

| Scenario | Required source behavior | Source result |
| --- | --- | --- |
| First hostile capture with four agents | Snapshot each live unallocated payload count, remove the aggregate national amount once, store four state ledgers, original custodian, controller, and one due date. | Implemented by `bio_facility_capture_initialize_exact_state_ledger`. Negative stock removal omits `producer`, so domestic and foreign-produced equipment are included in the same aggregate debit. |
| Mixed-producer stockpile | The state ledger and national debit must cover the same total. | Implemented. `num_equipment@...` reads the aggregate count and the matching negative `add_equipment_to_stockpile` effects omit the producer filter documented to restrict removal. Positive recovery/transfers name the receiving country as producer. |
| One-unit agent under limited preservation/destruction | A limited result must not become a full result through integer rounding. | Implemented. The generic limited-fraction helper leaves one unit whenever a sub-100-percent rounded amount would consume the complete agent ledger. A one-unit agent therefore moves zero units and remains unresolved. |
| Failure or delayed hazard with one remaining unit | An actual release must consume at least one and may exhaust the final agent. | Implemented. Only `bio_facility_capture_debit_selected_release` calls `bio_facility_capture_enforce_release_minimum`; secure/destroy fractions never call it. |
| Third-party control change | Preserve all payload and timing records; update only the exact controller. | Implemented by `bio_facility_capture_update_exact_controller`, reached only from the exact `FROM.FROM` state callback. |
| Original recapture without replacement arsenal | Restore exact remaining payload, rebind the original state and pointer source, resume stockpile monitor. | Implemented by `bio_facility_capture_restore_on_original_recapture`. |
| Original recapture with replacement arsenal | Restore exact remaining payload but keep the replacement as the sole active designation. | Implemented. The captured-state marker is cleared while the replacement country pointer remains untouched. |
| Original custodian eliminated | Resolve the outbreak in the exact state against its current controller without assigning responsibility to another country. | Implemented. Victim and debit proof remain mandatory; missing actor proof is accepted only for the extinct recorded custodian, and no proxy is selected. |
| Stale delayed event after resolution | Produce no release, reschedule, or substitute state. | Implemented. The hidden state event requires the exact unresolved flag, complete ledger, current controller pointer, positive payload, scheduled flag, and due day. |
| Failed raid exhausting final payload | Debit the last exact agent amount once, dispatch the accident, and clear stale hazard scheduling. | Implemented. The release helper recomputes the ledger and clears the due flag/date when no payload remains. |
| Secure limited/full | Limited transfers bounded per-agent shares and keeps the site unresolved; full transfers all and clears the hazard. | Implemented through `bio_facility_capture_secure_limited`, `bio_facility_capture_secure_success`, and `bio_facility_capture_secure_critical`. |
| Destroy limited/full | Limited destroys bounded per-agent shares and keeps the site unresolved; full destroys all and removes one facility level. | Implemented through `bio_facility_capture_destroy_limited`, `bio_facility_capture_destroy_success`, and `bio_facility_capture_destroy_critical`. |
| Assigned HQ requirement | Only the selected BSA formation's assigned Army Headquarters may satisfy Biological Security. | Implemented through character-scoped `bio_facility_*_hq_requirement` and `bio_facility_*_hq_security` factors. Missing the exact section applies a fail-closed -10 success weight; an unrelated headquarters cannot satisfy the trigger. |
| AI route choice | Defensive/democratic/advanced handlers prefer preservation; unrestricted/high-hazard/weak handlers prefer destruction. | Implemented in the two native raid `ai_will_do` blocks. Missing assigned HQ falls below the native minimum-success threshold. |

## Lifecycle contract audit

The captured-facility accident validation branch requires:

- source `bio_lifecycle_source.captured_facility`;
- route `bio_lifecycle_route.captured_facility_release`;
- accident result;
- exact current-controller victim event target and supplied victim proof;
- current state controller matching that victim;
- supplied payload-debit proof;
- positive required and consumed amounts;
- consumed amount no greater than required.

The caller supplies the exact debited amount as both required and consumed. Actor proof is supplied from `bio_stockpile_safety_arsenal_actor` only while that exact country exists. The attribution helper keeps captured-facility records accident-class, and no deliberate-use or confirmed-use history is created.

## Engine limits still open

Installed raid documentation permits arbitrary state target triggers, but vanilla has no land-raid precedent for an enemy-owned state already controlled by the actor. This exact target presentation remains a Stage 14 scenario risk. If the native UI suppresses the target, the route is unsupported until a verified native hook exists; it must not be replaced by a decision.

The documented `unit_requirements` schema accepts battalion and equipment checks but no character trigger. The selected formation can therefore remain visible even when its assigned leader lacks a Biological Security Section. The character-scoped success requirement makes that formation unable to succeed and makes the deficiency visible in native unit selection; there is no national-HQ or inferred-assignment substitute.

The optional event graph inspection produced no artifact because the repository exceeded the tool's fixed 100,000-node ceiling. Direct source tracing and installed documentation were used. This is not a runtime validation pass.
