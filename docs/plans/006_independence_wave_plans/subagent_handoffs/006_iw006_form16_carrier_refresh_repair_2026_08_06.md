# Event 006 FORM-16 carrier readiness refresh repair

Date: 2026-08-06.

Scope: narrow lifecycle repair for the Transcaucasian Federation FORM-16 arbitration receipt and readiness publication.

## Finding

`independence_wave_form16_register_readiness` is carrier-scoped and requires the exact carrier to see the completed member/arbitration state. The arbitration completion effect previously invoked it only in the country that completed its own arbitration. If the carrier completed arbitration before the other two members, the final member could write its own receipt but could not publish the carrier's readiness receipt, leaving the generic formable registry fail-closed after all accepted member gates were satisfied.

## Repair

`common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt` now refreshes the exact ARM, GEO, and AZR carrier candidates after every arbitration completion. The existing `independence_wave_form16_register_readiness` predicate still requires the selected carrier, all three live members, peace, identity clearance, route compatibility, and arbitration receipt, so the fan-out changes only lifecycle ordering and does not loosen admission, territory, identity, tag, or consent gates.

## Evidence

- Read-only `hoi4.probability_inspect` on `common/decisions/006_independence_wave_transcaucasus_decisions.txt` with `decision_ai_will_do` completed as `PROBABILITY_SOURCE_INSPECTED` with `candidates=7`, `requiredInputs=13`, `unresolved=0`, and `poolComplete=false` under source hash `29b511ee5b19c61a68792ca7506a059644244ab778eaff5109b9630c2e9052fc`.
- Static review confirms the readiness effect remains fail-closed on `is_independence_wave_form16_carrier`, `has_independence_wave_form16_all_members_live`, `has_independence_wave_form16_member_peace`, `has_independence_wave_form16_identity_clearance`, `has_independence_wave_form16_route_compatibility`, and `has_independence_wave_form16_arbitration_receipt`.
- No tags, assets, flags, member policy, territory anchors, or runtime identifiers were added or relaxed.

## Remaining gates

FORM-16 remains behind its existing member, identity, anchor, consent, integration, transaction, and typed AI evidence gates. No live-game or save/load validation is claimed.
