# Country object validity repair

Date: 2026-10-03.
Disposition: implemented source correction; mandatory probability comparison and live validation remain unresolved.
Acceptance basis: the user requires valid actor and destination proofs, exact transfers, stale-target cleanup, and no fabricated replacement objects.

## Source defect and correction

`humanitarian_country_is_valid` checked `scope_exists` and the special/nonhuman exclusions but did not check whether the country exists in the game.
The transitive shared classifiers contain no country-existence predicate.
Installed documentation explicitly distinguishes `scope_exists` from country `exists` and states that variable scopes are always valid scopes.
A stored country scope can therefore remain resolvable after the country ceases to exist without meeting the intended live-country contract.

The country predicate now also requires `exists = yes`.
The existing scope check and both exclusions remain intact.
This correction supplies no new actor, destination, population, amount, route, or world iteration.
It also strengthens state validation through its existing OWNER/CONTROLLER checks.
Destination selection and foreign relief consume the same shared guard, so their target eligibility inherits the correction without score or weight changes.

## Files changed

- `common/scripted_triggers/humanitarian_validation_triggers.txt`: one explicit country-object guard.
- `common/scripted_triggers/humanitarian_validation_triggers.md`: scopes, inputs, defaults, side effects, limitations, and usage.
- `docs/systems/civilian_transfer_system.md`: live country-object proof rule.
- `docs/plans/famine_and_migration_system_plans/evidence/20261003_country_validity/before/humanitarian_validation_triggers.txt`: immutable pre-edit source, SHA-256 `2E2D5AC68749F621EDC1D61BE7F38B3D93D1027A7DB2EFF13C8832C50C9D64A1`.
- This handoff.

## References and source trace

- Installed `documentation/triggers_documentation.md:2709-2715` defines COUNTRY-scoped `exists`.
- Installed `documentation/triggers_documentation.md:7450-7470` defines `scope_exists`, distinguishes object existence, and describes always-valid variable scopes.
- The installed trigger documentation SHA-256 is `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
- Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:638` supplies the country `exists = yes` rule.
- Installed vanilla `common/scripted_triggers/00_scripted_triggers.txt:19-23`, `can_ROOT_get_wargoal_on_THIS`, demonstrates an explicit existence gate before target relations.
- Current `common/scripted_triggers/chaosx_dynamic_triggers.txt:10-67` confirms the shared special/nonhuman classifiers provide exclusions only.
- Current migration destination actor/owner gates, relief actor gates, state OWNER/CONTROLLER validation, and dirty-capacity registration consume the corrected predicate.

## Audit and validation limits

The read-only probability auditor captured the exact pre-edit identity and reviewed current destination/donor consumers before the owner patch.
Its broad and narrowed attempts returned no baseline artifact; the final narrow `hoi4.probability_inspect` retry returned an actual `timed out awaiting tools/call after 600s` error.
Historical August decision-source artifacts are different identities and are not a baseline for this change.
The fixed case names are `prob_country_live_target_valid_20261003` and `prob_country_dormant_or_annexed_target_invalid_20261003`.
The auditor retains the same-case comparison obligation, supported fixture encoding, and returned inspect/compare evidence as outstanding work; source review does not replace it.

The source proof establishes that a current ordinary human country still meets this added existence requirement, while a non-existing country is rejected and special/nonhuman countries remain excluded.
There is no new formula, numeric AI score, normalized probability, or runtime reachability claim.
No game was launched, no log was read, and no historical death total or population fallback was introduced.
