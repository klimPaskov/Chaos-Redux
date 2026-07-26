# Event 006 RG-RHINE-SAAR shared-capacity repair

Date: 2026-07-27

Status: implemented; bounded re-audit v22 is source-level PASS / runtime HOLD.

## Decision

IW-008 Rhineland and IW-010 Saar remain two separate accepted Event 006 packages. They share the coarse `RG-RHINE-SAAR` reservation group in the research matrix, but their accepted anchor states are distinct (`51` and `42`). The pair still uses the ordinary per-host protected-state selector: both rows may share GER's host-protection row when the map gives them the same host, and the plan fails closed if no safe remnant remains. The group therefore admits this exact pair, while every other reservation group keeps the one-package rule.

## Implementation

- `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt` no longer precludes the accepted pair solely because the coarse group is already present.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` permits the second member only when the candidate is IW-008 with IW-010 already selected, or IW-010 with IW-008 already selected.
- `common/scripted_triggers/006_independence_wave_triggers.txt` lets the Liberations capacity witness count the counterpart after the first sibling has been admitted.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` exempts only the IW-008/IW-010 reciprocal pair from the lock-time duplicate-group invariant.
- The central reservation effect still requires an unused country, a unique unprotected anchor, a valid host, and a live release plan. Optional compact and extended states remain subject to trimming.

This is a narrow capacity rule, not a general group relaxation. It does not permit duplicate package IDs, a third package in the group, living tags, or anchor/state collisions.

## Validation target

The bounded re-audit `006_rhine_saar_shared_group_capacity_reaudit_v22_2026_07_27.md` replaces the previous “ten attested IDs / nine compatible groups fail exact-ten” finding with a source-level pair-capacity PASS. Runtime proof remains open for both package orders, shared-host protected-remnant cases, Event 005 collisions, rollback/save-load, exact-ten execution, and World Collapse.
