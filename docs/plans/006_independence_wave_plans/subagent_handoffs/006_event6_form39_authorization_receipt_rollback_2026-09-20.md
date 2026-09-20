# Event 006 FORM-39 authorization-receipt rollback cleanup — 2026-09-20

## Status

**IMPLEMENTED / PACKAGE-LOCAL / ADMISSION UNCHANGED**

The Melanesian Federation now clears stale member authorization receipts when a FORM-39 transaction rolls back or its runtime is later cleaned up.

## Defect and boundary

The FORM-39 invitation decisions in `common/decisions/006_independence_wave_formable_decisions.txt` set `independence_wave_formable_full_integration_authorized` or `independence_wave_formable_autonomous_membership_authorized` on PNG/WPG so the integration adapter can choose the accepted member path.

The shared invitation cleanup removes the generic pending and consent state but must not clear these receipts before the successful integration adapter consumes them. On a failed pre-integration transaction, however, the rollback helper only visited already-bound autonomous members, so a full-integration or unbound autonomous receipt could survive and block both authorization decisions on a later invitation.

## Source change

`common/scripted_effects/006_independence_wave_formable_registry_effects.txt` now clears both authorization receipts while `independence_wave_form39_cleanup_frozen_members` traverses the exact member ledger, limited to PNG/WPG rows and a Melanesian Federation carrier profile.

The helper is called by FORM-39 identity rollback and runtime cleanup. The successful integration path is unchanged: the adapter reads the authorization flags before this helper is reached, and the normal founding-proposal close does not invoke this rollback cleanup.

No central package attestation, Join, allocator, SCN-008, identity, FSM, FORM-48, or weighted surface changes.

## Validation

`python -B .tools/audit_event6_allocator.py --strict` passed with the unchanged 3/4/5/7/10 ladder, World Collapse 10, 32 attested packages, 40 adapters, and eight adapter-only fail-closed IDs.

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases with the existing publication order.

`python -B .tools/audit_event6_country_api.py` passed with 242 broad unique tags, 191 resolved carriers, zero missing tags, zero duplicates, and the IW-031 crosswalk pass.

`python -B .tools/audit_event6_flags.py --strict` passed with 102 registered and complete Event 006 flag families.

The read-only `hoi4.event_inspect` lint on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, with zero blocking diagnostics and the documented large-workspace helper/lifecycle deferral; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98dbd0445095bf31e447e4aa7023b94658c3c3d04f4b69cd6ead633a079593ac/0f59c1552cdaf5ecc3be9ebe0947d4eb2586aa8e6703e83efec684c3cbe30122/event-lint-a8fde3e58546.json`.

Live Hearts of Iron IV, save/load, and user-owned visual acceptance were not run by the agent.

## Remaining status

Whole Event 006 remains **HOLD / PARTIAL** under the current completion audit because package coverage, source and rights gates, GUI evidence, audio acceptance, typed probability fixtures, formable reachability, and live runtime evidence remain unresolved.
