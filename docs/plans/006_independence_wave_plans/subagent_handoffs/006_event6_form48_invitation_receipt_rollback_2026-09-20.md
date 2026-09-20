# Event 006 FORM-48 invitation-receipt rollback cleanup — 2026-09-20

## Status

**IMPLEMENTED / PACKAGE-LOCAL / ADMISSION UNCHANGED**

The Pacific Regional Federation now clears its dedicated human invitation-response receipts when the exact founding proposal closes.

## Defect and boundary

`independence_wave_form48_accept_autonomous_invitation` and `independence_wave_form48_withhold_autonomous_invitation` set `independence_wave_form48_autonomous_invitation_authorized` or `independence_wave_form48_autonomous_invitation_withheld` on HAW/FSM.

The shared `independence_wave_formable_clear_founding_invitation_from_root` cleanup already protects the inviting carrier, generation, family, and proposal sequence, but it only cleared the generic invitation state. A failed pre-integration transaction could therefore leave one of the two FORM-48 response receipts on an exact Pacific member after the generic invitation had been removed.

## Source change

`common/scripted_effects/006_independence_wave_formable_registry_effects.txt` now clears both FORM-48 response receipts inside the existing exact-carrier cleanup block, gated by `independence_wave_formable_invitation_family = constant:independence_wave_formable_family.pacific_regional_federation`, before the generic invitation state is cleared.

The existing carrier, generation, family, and proposal-sequence limits remain authoritative. A newer invitation owned by another carrier or proposal is not touched, and no autonomous member binding, identity adapter, central admission list, FSM readiness flag, allocator input, or weighted surface changes.

This covers failed pre-integration rollback and normal closure of the exact Pacific proposal without adding a new scan or periodic hook.

## Validation

`python -B .tools/audit_event6_allocator.py --strict` passed with the unchanged 3/4/5/7/10 ladder, World Collapse 10, 32 attested packages, 40 adapters, and eight adapter-only fail-closed IDs.

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases with the existing publication order.

`python -B .tools/audit_event6_flags.py --strict` passed with 102 registered and complete Event 006 flag families.

The read-only `hoi4.event_inspect` lint on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, with zero blocking diagnostics and the documented large-workspace helper/lifecycle deferral; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98dbd0445095bf31e447e4aa7023b94658c3c3d04f4b69cd6ead633a079593ac/0f59c1552cdaf5ecc3be9ebe0947d4eb2586aa8e6703e83efec684c3cbe30122/event-lint-a8fde3e58546.json`.

Live Hearts of Iron IV, save/load, and user-owned visual acceptance were not run by the agent.

## Remaining status

Whole Event 006 remains **HOLD / PARTIAL** under the current completion audit because package coverage, source and rights gates, GUI evidence, audio acceptance, typed probability fixtures, formable reachability, and live runtime evidence remain unresolved.
