# Event 006 central capacity attested-carrier completion

Date: 2026-08-06

Disposition: source implementation tranche; whole-event status remains HOLD / PARTIAL.

## Scope

The central Liberations-cluster availability predicate previously exposed only sixteen of the twenty-three current Event 006 content-attested package IDs. That meant its own greedy capacity witness could never reach the accepted World Collapse target of twenty, even though the regional allocator, package dispatcher, scenario ranker, and static package registry already contained the remaining carriers.

## Changes

`common/scripted_triggers/006_independence_wave_triggers.txt` now contains one exact runtime wrapper and one capacity transaction candidate for every current attested ID: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-026, IW-029, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184.

The new candidates preserve the accepted chaos-band gates, unique country and anchor arrays, reservation-group uniqueness, current reservation/protected-state checks, and surviving-host check. IW-026 and IW-029 additionally require their documented YUG former host at the exact anchor, matching their package setup/runtime contracts.

The central host witness no longer rejects every SOV-owned anchor before a joint plan exists. Event 005 still contributes its anchors first in `liberations_joint_prepare_and_execute_incident`, and the Event 006 candidate anchor/country predicates reroll any tag or state reserved by that contribution. This keeps standalone Transcaucasus releases possible while preserving the accepted joint collision barrier.

`common/scripted_triggers/006_independence_wave_macedonia_package_triggers.txt` and `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt` now require `tag = YUG` for their exact dormant anchor owner, preventing scenario or regional dispatch from selecting a package that would fail its package-specific former-host contract.

## Static validation

`python -B .tools/audit_event6_allocator.py` passes with twenty-three capacity wrappers/tries, twenty-three content attestations, twenty-two compatible reservation groups, and the accepted 6/8/10/14/20 ladder.

`python -B .tools/audit_event6_scenario_matrix.py`, `.tools/audit_event6_flags.py`, `.tools/audit_chaosx_country_tags.py`, and `.tools/audit_event6_gui_matrix.py` all pass after the change.

The touched trigger files contain no unsupported `<=` or `>=` operators, and `git diff --check` is clean.

## Evidence boundary

The capacity predicate is a deterministic fail-closed availability witness, not a live allocation receipt. The required HOI4 MCP probability audit is recorded separately in `006_capacity_tranche_probability_audit_e72b717d2_2026_08_06.md` for the preceding tranche; a fresh audit of this expanded weighted surface remains required before any quantitative probability, starvation, dominance, or live World Collapse claim.

The whole event remains incomplete because most registry packages, factual/asset gates, typed AI evidence, formable reachability, super-event 23 rights/audio/wrappers/firing, and broader MCP/runtime evidence remain open.
