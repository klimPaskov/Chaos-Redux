# Event 029 contract helper repairs

Disposition: implemented source repairs with required MCP comparison and completion review pending.
The user's full Event 029 specification request supplies the acceptance basis for exclusive concessions, one state-owned contract, and correct controller refresh.

## Changed implementation

Changed files: `common/scripted_effects/029_riches_found_effects.txt` and `common/scripted_effects/029_riches_found_incident_effects.txt`.
Changed helpers: `riches_found_begin_contract`, `riches_found_extend_limited_contract`, `riches_found_prepare_random_event_fire`, and `riches_found_prepare_scored_foreign_partner`.

The exclusive-concession caller writes `riches_found_contract_exclusive_request = 1`.
The helper formerly tested whether the request was greater than 1, so that caller could not mark the contract exclusive through the helper.
The helper now requires the request to equal 1 and the stored contract type to be `exclusive_concession`.
The type guard also prevents an earlier temporary exclusive request in the same effect chain from marking a subsequent limited, offtake, or infrastructure-access contract exclusive.

The limited-contract amendment helper runs in state scope.
Its former direct call to `riches_found_refresh_mine_state` entered a country-owned controlled-state iterator from that state.
The amendment now enters the existing current `CONTROLLER` country before calling the same refresh helper, guarded by `exists = yes`.
The partner, term record, review cadence, and action amounts remain those of the existing contract.

Each discovery preparation now resets its readiness value to zero.
The state-selection helper sets that same readiness value to one only after saving the state selected in the current call.
It publishes readiness only when the current recipient pool was nonempty and the prepared ordinary country and owned, controlled, valid state still form a valid pair.
The final gate also requires the fresh state-selection receipt and resets readiness to zero when validation fails.
The temporary pool is cleared after that validation.
Regular event targets left by an earlier preparation in the same effect chain therefore cannot make an empty current pool ready.

The scored foreign-partner selector already clears its state pointer and availability flag and starts its best score at zero.
It now publishes a selected partner only after a current eligible candidate produced a positive score.
Contract creation additionally requires that published state pointer to match the regular partner target.
An old partner target surviving in the effect chain can no longer authorize a new contract after an empty current candidate pass.

## Source scenario review

| Input | Required result from corrected condition |
| --- | --- |
| Request 1, exclusive type | Set the exclusive contract and achievement-history flags. |
| Request 0, exclusive type | Do not authorize exclusivity. |
| Stale request 1, limited type | Do not mark the limited contract exclusive. |
| Stale request 1, offtake or infrastructure-access type | Do not mark the amended contract exclusive. |
| Amendment with an existing controller | Execute the country refresh from that controller's scope. |
| Amendment with no existing controller | Skip the country refresh. |
| Empty recipient pool with prior owner/state targets | Keep discovery readiness at zero. |
| Current prepared state no longer belongs to the prepared country | Keep discovery readiness at zero. |
| Empty foreign-candidate pass with a prior regular partner target | Do not publish a foreign target or open a contract. |
| Fresh scored partner differs from the stored published pointer | Reject contract creation. |

These are source control-flow findings, not executed game scenarios.
The complete immutable pre-edit source is `../evidence/2026_10_03_before/common__scripted_effects__029_riches_found_effects.txt`, SHA-256 `a991dde1db89165ced86dbf714228975113d012163d073723c898873941e987c`.
The incident-effect before source is `../evidence/2026_10_03_before/common__scripted_effects__029_riches_found_incident_effects.txt`, SHA-256 `01648014f105c149509f789be9ae3d30e013545921203ba867cbbd16d5c2f9fc`.
The read-only probability auditor was notified to retain both before sources and compare the same foreign-concession and repeat-recipient scenarios against the current helper sources.

## Outstanding acceptance

The foreign availability predicate currently admits neighboring land controllers and needs reconciliation with the specified distant naval-power case.
The per-invocation prefire and foreign-target source guards are implemented, and their same-scenario MCP evidence remains pending.
Shared inclusive custom-cost affordability and delayed decision completion ownership remain under the decision audit.
No AI weight was changed in this repair.
No route, asset, or reward was replaced with a fallback, placeholder, or simplified substitute.
The complete Event 029 package remains incomplete.
