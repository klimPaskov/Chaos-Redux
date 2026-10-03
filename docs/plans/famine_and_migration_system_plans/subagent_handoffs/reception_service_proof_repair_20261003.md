# Reception service proof repair

Date: 2026-10-03.

Disposition: implemented, with source review complete and runtime validation reserved for the user/orchestrator.
Acceptance basis: the user requires working reception, complete valid player and AI responses, and no simplified capacity substitute; the existing public adapter contract explicitly accepts a positive proof token.

## Defect and correction

Both `migration_set_reception_shelter_service` and `migration_set_reception_medical_service` required their request proof to be greater than `constant:migration_capacity.one`.
The constants define `one = 1`, and ordinary reception decisions supply exactly that canonical proof.
Consequently `migration_open_reception` could pay for shelter and medical services without either service being stored, while `migration_controlled_medical_reception` could pay its cost without creating its medical service or observation mission.

Both adapter guards now require a proof greater than `constant:migration_capacity.zero`, matching the documented positive-proof contract.
Positive service amounts and `humanitarian_state_is_valid` remain mandatory.
The accepted service amount, canonical persisted proof, sparse registration, dirty-country propagation, public result, and one-shot input cleanup are otherwise unchanged.
Larger positive owner tokens remain valid and do not scale the capacity amount.
This preserves the current Event 012 service caller while allowing the canonical proof used by normal decisions.

## Changed files and consumers

- `common/scripted_effects/migration_capacity_effects.txt`: the two service proof guards only.
- `common/scripted_effects/migration_capacity_effects.md`: explicit canonical-one, missing/zero-proof, and larger-token behavior.
- This handoff.

The exact current decision consumers are the shelter and medical bootstrap branches of `migration_open_reception` and the medical-service branch of `migration_controlled_medical_reception` in `common/decisions/migration_decisions.txt`.
The Event 012 reception adapter in `common/scripted_effects/migration_adapter_effects.txt` is another positive-proof consumer and belongs to its own concurrent owner.
No decision score, weighted target expression, cost, duration, population transfer, reception-load ledger, or capacity formula was changed.

## Source validation

The caller-to-adapter trace establishes that a positive amount with canonical proof `1` passes the corrected service guard, while zero/missing proof, a non-positive amount, or an invalid state remains rejected.
Both adapters still reset the request amount and proof after either outcome.
An accepted service writes its actual requested amount once and registers the state idempotently; it creates no population or Deaths transaction.
The old source SHA-256 was `6E67FDB164C14852440683FFE5308906B157C43C3A319C1F2278B7DC2D80E73C`; the corrected source SHA-256 is `62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B`.

Relevant reference sections read directly are installed `documentation/triggers_documentation.md:2110` (`check_variable` and strict `greater_than`), `documentation/effects_documentation.md:7820` (`set_temp_variable`), and offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:563` (temporary variables and strict comparison semantics).
The installed vanilla `common/scripted_triggers/00_scripted_triggers.txt:19` supplies the `exists = yes` object-validity precedent used in the related country-validation review; that separate proposed correction is not included here.

## Validation limits

A narrow reference search and an isolated source-backed `hoi4.mechanic_test` for canonical shelter proof were requested through the connected service.
Their final returned evidence is recorded in the current parent reconciliation, rather than treating a pending request as a pass.
No game was launched and no error log was read.
In-game service persistence, capacity recomputation, mission entry, and asset consumers remain user/orchestrator-owned validation.

No fallback, tuning substitute, fabricated capacity, or population side effect was introduced.
