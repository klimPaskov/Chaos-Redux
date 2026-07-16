# Air Cleanliness Treaty Inspection Proof

## Proof boundary

This document records the static engine and transaction proof for the Air Cleanliness Treaty Verification Mission. Hearts of Iron IV was not launched. The optional HOI4 event inspector returned `ARTIFACT_STORAGE_LIMIT` without scanning a file or producing an artifact, so it is not part of this proof basis.

The implemented slice preserves the existing Air Winter and Fallout tuning formulas. It contains a secretariat-owned targeted mission, an inspected-member response event, an exact seven-day delayed result, three manually authored outcomes, government-aware text, AI weights, diplomatic memory, and paired cleanup. It does not change Air Contamination, survival grading, Fallout eligibility, or Fallout grading. Refusal invokes the accepted treaty violation consequences and can remove an existing relief route.

## Required references and precedents

The implementation follows these required local references:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- installed `documentation/effects_documentation.md`
- installed `documentation/triggers_documentation.md`
- installed `documentation/script_concept_documentation.md`
- installed `common/decisions/_documentation.md`
- vanilla `common/decisions/AST.txt`, decision `AST_supply_arms_to_nation`
- Chaos Redux Joint Filter Convoy in `common/decisions/air_cleanliness_treaty_decisions.txt`

## Event catalog alignment

Events `chaosx_air_treaty.6` through `chaosx_air_treaty.9` are internal treaty report and dispatch subevents in the existing `chaosx_air_treaty` namespace. They are not numbered root events in the `chaosx.nr<ID>.1` public event registry. Existing treaty reports `.1` through `.5` also have no workbook row. The public event catalog workbook therefore receives no new row for this tranche, and none of its export-only CSV files are edited.

## Engine-sensitive surfaces

| Surface | Static engine evidence | Implemented contract |
| --- | --- | --- |
| Targeted country decision | Official decision documentation defines ROOT as actor, FROM as target, `target_root_trigger` as the actor prefilter, and `target_array` as the bounded candidate source. Vanilla `AST_supply_arms_to_nation` uses the same target-array ROOT and FROM pattern. | ROOT must be the persistent treaty founder. FROM must be a distinct live member stored in `global.air_cleanliness_treaty_members`. No world-country selector is used. |
| Timed decision lifecycle | Official decision documentation defines `complete_effect` at selection, `days_remove`, `cancel_trigger`, `cancel_effect`, and `remove_effect`. | Start payment and paired reservation occur in `complete_effect`. Fourteen days of factory use follow. Invalid receipts call cancellation. Valid expiry opens the inspected-member response. |
| Delayed result | Official effects documentation defines `country_event` with a `days` delay. | The response stores its outcome first, then issues hidden dispatcher `.9` with the file-scoped mirror of the seven-day script constant. On that day the dispatcher opens visible report `.7` only for the exact pending transaction and clears an invalid receipt immediately. |
| Event-target retention | The offline Data Structures page defines regular event targets as chain-local scope pointers that carry into fired events. | Inspector and subject identities are also stored as country-scope variables. Events `.6`, `.7`, and `.8` rebuild their localisation event targets in `immediate`, so visible text does not depend only on inherited pointers. |
| Country-scope variables | Official effects documentation defines `set_variable` and `clear_variable`. Official triggers documentation defines `has_variable` and `check_variable`. | Both countries store inspector, subject, generation, and transaction. The response phase also stores the same outcome on both countries. Every phase compares both sides. |
| Bounded scope arrays | Official effects documentation defines array add, remove, clear, and scope iteration. Official trigger documentation defines `is_in_array`. | `global.air_cleanliness_treaty_active_inspectors` stores exact transaction owners. `global.air_cleanliness_treaty_verification_cancellations` is a separate mutation queue. |
| Timed country flags | Existing treaty invitations, Cleaning Day, and Filter Convoy use timed country flags with file-scoped duration mirrors. | The secretariat cooldown lasts ninety days. The inspected-member recency gate lasts one hundred eighty days. Operational cleanup preserves both timed flags. |
| Equipment payment | Existing Air Winter payment helpers negate a temporary amount before `add_equipment_to_stockpile`, which is the established dynamic removal pattern. | The secretariat pays support equipment and convoys at dispatch. Full and restricted responses pay different support equipment and train costs before the outcome becomes pending. |
| Opinion outcomes | Vanilla opinion modifiers support value, month lifetime, decay, and a separate trade switch. The engine effect surface supports add and remove operations. | Current members first remove all three inspection outcome modifiers against the subject, then add exactly one result with `trade = no`. Refusal then uses the existing treaty-owned violation sanctions. |
| Event AI | Offline event and AI documentation define `ai_chance`. The decision documentation requires `ai_will_do` for AI use. | Dispatch has centralized decision weights. All three response options, all three result acknowledgement options, and the depot-recount acknowledgement have centralized AI weights. |
| Fallout boundary | The existing transition sets `fallout_transition_active` before blackout scheduling and calls the treaty pause transaction. | Both Fallout flags invalidate every inspection phase. The pause copies active inspectors into the cancellation queue and clears paired operational receipts without firing a report. |

## Transaction phases and receipts

### Global receipt

- `global.air_cleanliness_treaty_verification_transaction` is monotonic.
- `global.air_cleanliness_treaty_active_inspectors` contains the exact secretariat owner.
- `global.air_cleanliness_treaty_verification_cancellations` is the only array used to mutate the active-owner registry during reconciliation.

### Secretariat receipt

- `air_cleanliness_treaty_verification_active`
- one of `air_cleanliness_treaty_verification_mission_active`, `air_cleanliness_treaty_verification_awaiting_response`, or `air_cleanliness_treaty_verification_result_pending`
- `air_cleanliness_treaty_verification_transaction`
- `air_cleanliness_treaty_verification_generation`
- `air_cleanliness_treaty_verification_subject`
- `air_cleanliness_treaty_verification_outcome` only after a response

### Inspected-member receipt

- `air_cleanliness_treaty_inspection_reserved`
- either `air_cleanliness_treaty_inspection_request_pending` or `air_cleanliness_treaty_inspection_response_pending` after travel
- `air_cleanliness_treaty_inspection_inspector`
- `air_cleanliness_treaty_inspection_transaction`
- `air_cleanliness_treaty_inspection_generation`
- `air_cleanliness_treaty_inspection_outcome` only after a response

The transaction trigger accepts exactly three shapes:

1. travelling mission with no request or result flags
2. waiting secretariat with one subject request flag
3. pending result with the same valid outcome on both countries

Every shape requires current membership, current founder authority, the current treaty generation, peace between the pair, exact cross-country identity, and an active-inspector registry entry.

## Outcome and memory contract

| Outcome | Subject payment | Delayed diplomatic result | Permanent memory |
| --- | --- | --- | --- |
| Full access | 30 support equipment and 5 trains | current members gain 20 opinion for up to 12 months | opened inspection |
| Records only | 12 support equipment and 2 trains | current members lose 15 opinion for up to 9 months | restricted inspection |
| Refusal | none | current members lose 40 opinion for up to 18 months, then apply expulsion, relief loss, the standing violator penalty, and treaty-owned embargoes | refused inspection and treaty betrayal |

All three outcomes write last partner, last date, last outcome, completed transaction, and completed generation on both countries. Full access and records-only access do not alter membership or relief. Refusal sets its own cause memory and calls the existing member-violation consequence path. That path removes membership and active relief, registers the treaty embargo owner, applies the standing violator opinion modifier, and preserves betrayal memory. It does not claim unconventional-weapon use, fire the weapon-use report, or set a Fallout value.

## Cleanup proof

The exact paired transaction is cleared by:

- timed-decision cancellation
- invalid mission expiry
- monthly bounded reconciliation
- membership loss
- unconventional-weapons violation through membership loss
- founder succession
- war between inspector and subject
- annexation of either country
- treaty dissolution
- inactive-runtime cleanup
- schema migration
- Fallout transition or active Fallout

`air_cleanliness_treaty_clear_verification_transaction` first recovers the stored subject and clears subject receipts only when its stored inspector equals the exact secretariat. It then clears the secretariat phase and payload and removes every duplicate owner row. Historical outcome flags and last-result variables remain. Cancellation does not mutate the active array while that array is being inspected.

## Static acceptance scenarios

- A non-founder cannot see or start the mission as actor.
- The founder cannot target itself, a nonmember, a member at war with it, another active inspector, a reserved member, or a recently inspected member.
- A founder without the dispatch equipment or available civilian factory cannot begin.
- Starting twice is blocked by the active flag, active-owner array, and cooldown.
- Mission expiry opens one response only when both paired receipts remain exact.
- Full and restricted access are unavailable when the inspected member cannot pay their distinct costs.
- Refusal remains available without equipment.
- If equipment or trains are spent while the response is open, the selected paid response opens one government-aware depot recount, preserves the request, and presents only currently affordable choices again.
- If membership, founder authority, peace, or the paired receipt fails while the response is open, selecting an old option cancels the exact operation immediately.
- A response writes one outcome to both countries before the delayed event command is issued.
- A second response cannot issue another result because the request flag is consumed.
- The hidden seven-day dispatcher opens the delayed report only for the matching transaction and generation. It clears an invalid receipt on the scheduled day instead of waiting for monthly reconciliation.
- Full, restricted, and refused results are mutually exclusive and replace the prior current-member inspection opinion.
- Membership, war, annexation, founder, generation, or Fallout drift clears the operation without applying a result.
- No inspection path changes a Winter or Fallout tuning formula. Refusal can remove the existing relief-route input through treaty expulsion.
- No periodic `every_country` or `every_state` loop is added.

## Runtime observation gates

Static source cannot prove:

- targeted-decision FROM persistence across save and load
- the exact day on which the engine presents the subject event after mission expiry
- the exact seven-day presentation of the result event
- regular event-target retention in delayed multiplayer event chains
- timed flag expiry under multiplayer pause and host migration
- AI campaign pacing and response distribution
- displayed opinion duration and decay

These are runtime observation gates. No passing runtime result is claimed.

## Simplifications and exclusions

No simplification was substituted inside the implemented inspection transaction. The accepted member obligation is enforced. Refusal causes expulsion, treaty-owned embargoes, opinion penalties, and loss of treaty relief access. New Air Winter bonuses, Fallout coefficients, and successor effects are outside this tranche and remain explicit future work rather than hidden behavior.
