# Event 006 RG-RHINE-SAAR shared-capacity re-audit v22

Date: 2026-07-27

Role: read-only Event 006 completion auditor

Snapshot: source state after the RG-RHINE-SAAR repair commit `54871211d` and the follow-up matrix/documentation reconciliation.

Status: **SOURCE-LEVEL PASS / RUNTIME HOLD**

## Bounded conclusion

The accepted IW-008 and IW-010 pair now has a complete source-level path through candidate admission, central reservation, deterministic cluster-capacity proof, and lock-time invariant validation.
The exact-ten static capacity blocker from `006_event_completion_audit_v21_2026_07_27.md` is superseded for this bounded surface.
The repair does not weaken any other reservation-group cap.
Event 006 and its exact-ten branches remain incomplete until the runtime scenarios below are evidenced.

## Accepted pair and anchor evidence

The current Event 006 source-of-truth mapping remains:

| Package | Country | Anchor | Group | Evidence |
|---|---|---:|---|---|
| IW-008 | RHI | 51 | RG-RHINE-SAAR | `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:99`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:9` |
| IW-010 | AJX | 42 | RG-RHINE-SAAR | `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:129`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:11` |

The pair therefore uses distinct package IDs, target countries, and mandatory anchor states.
This audit preserves the accepted numeric mapping.

The installed vanilla state names expose a separate source-of-truth discrepancy: `history/states/42-Rhineland.txt:15` and `history/states/51-Moselland.txt:14` both start under GER, while the Event 006 research labels IW-008 anchor 51 as Rhineland and IW-010 anchor 42 as Moselland/Saar.
The mod does not replace these two state-history files.
Do not silently swap the gameplay anchors as part of the capacity repair.
Rebind or explicitly confirm the package geography in the canonical research before final package promotion.

## Completion status by capacity surface

| Surface | Result | Static evidence |
|---|---|---|
| Package candidate admission | PASS | `can_plan_independence_wave_package_iw_008` and `can_plan_independence_wave_package_iw_010` admit an unused group or the already-selected reciprocal sibling at `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:56` and `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:81`. |
| Central country reservation | PASS | `liberation_release_add_country_reservation` admits only IW-008 after IW-010 or IW-010 after IW-008 within RG-RHINE-SAAR at `common/scripted_effects/chaosx_liberation_release_effects.txt:444`. Duplicate package, country, anchor, protected-state, host, and plan gates remain active. |
| Exact-ten capacity witness | PASS | The IW-008 and IW-010 witness blocks apply the same reciprocal exception at `common/scripted_triggers/006_independence_wave_triggers.txt:733` and `common/scripted_triggers/006_independence_wave_triggers.txt:795`. The deterministic path calls both blocks and still requires ten aligned package, country, anchor, and group rows at `common/scripted_triggers/006_independence_wave_triggers.txt:941`. |
| Lock-time invariant | PASS | `liberation_release_validate_set_invariants` exempts only the unordered IW-008/IW-010 reciprocal pair in RG-RHINE-SAAR at `common/scripted_effects/chaosx_liberation_release_effects.txt:843`. Duplicate package IDs remain rejected before the group exception. |
| Other reservation groups | PASS | Other package triggers retain the unused-group requirement. The central effect and lock invariant retain the one-package rule for every group other than the exact RG-RHINE-SAAR pair. |
| Exact-ten static count | PASS | `.tools/audit_event6_allocator.py` reports ten attested packages, nine group IDs, two admitted RG-RHINE-SAAR package slots, and valid 3/4/5/7/10 plus World Collapse 10 counts. |
| Same-host remnant selection | PARTIAL | In the installed starting map both anchors are owned by GER, so the pair normally shares one host reservation rather than two independent host remnants. The first package reuses the host's single protected state for the second at `common/scripted_effects/chaosx_liberation_release_effects.txt:247`. |

## Exact-ten proof and limits

The deterministic capacity witness can count all ten attested packages because its package, country, and anchor rows remain injective while the aligned group array intentionally contains RG-RHINE-SAAR twice.
The final witness checks array length, unique country and anchor admission, Event 005 clearance, and the existence of an owned state outside the selected anchors.
The lock validator accepts that duplicate group only when the two row package IDs are exactly IW-008 and IW-010 in either order.
A duplicate IW-008, duplicate IW-010, third package, unrelated duplicate group, country collision, or anchor collision remains rejected.

The static witness does not simulate the host protected-state priority.
The first same-host package excludes only its own current anchor when selecting the GER remnant.
In a changed map where the protected-state selector chooses the counterpart anchor, the second package can still fail even when another safe remnant exists.
That is an order-sensitive runtime gap, not a reason to reopen other group caps.

## Accepted-plan disposition

The narrow IW-008/IW-010 capacity rule is implemented across all four required script consumers and is accepted at source level.
The earlier v21 statement that ten attested IDs across nine group IDs necessarily fail exact ten is superseded by this report.
The whole-event HOLD and all unrelated v21 findings remain unchanged.

The canonical reservation-group row now declares capacity `2` for the exact IW-008/IW-010 pair and documents the distinct-anchor and per-host protected-remnant gates.
For the installed starting ownership both anchors are owned by GER, so the pair may share GER's one protected remnant row; no independent-host assumption is made.

## Meaningful validation

- Ran `python .tools\audit_event6_allocator.py` against the current working tree. It passed and reported ten attested packages, two distinct RG-RHINE-SAAR package slots, and valid exact-ten and World Collapse counts.
- Traced both package orders through the candidate triggers, central reservation exception, capacity-witness exception, aligned-array count, and unordered lock-invariant exception.
- Confirmed the two loaders use different country scopes and anchors 51 and 42.
- Confirmed non-pair package triggers and the central default path still apply one-package-per-group behavior.
- Confirmed the repair diff passes `git diff --check`. Line-ending warnings do not change the static result.

The allocator audit checks the presence of both witness package tokens and only one lock-pair orientation.
It does not structurally prove that both tokens occur inside the correct blocks, that the group guard is present, that the reverse lock orientation exists, or that a third package remains blocked.
Its PASS is supporting evidence, not runtime proof.

## Remaining runtime blockers

Record focused execution evidence for:

1. IW-008 followed by IW-010 and IW-010 followed by IW-008.
2. Both anchors under GER, and a split-ownership case where the anchors have different hosts.
3. The protected state on neither anchor, on state 51, and on state 42, including one-safe-remnant and no-safe-remnant cases.
4. Event 005 reserving a conflicting country, anchor, or host remnant before Event 006.
5. Rejection of a duplicate package, duplicate anchor, unrelated duplicate group, and any attempted third RG-RHINE-SAAR member.
6. Lock, execution, rollback, and save/load with the exact-ten frozen plan.
7. Exact-ten automatic execution and World Collapse execution reaching ten distinct released countries while every original host survives.

## Safe follow-up

Keep the reciprocal exception identical in the two package triggers, two capacity-witness blocks, central reservation effect, and unordered lock invariant.
Do not generalize RG-RHINE-SAAR to an unrestricted group count of two and do not relax any other group.
The comments, repair handoff, source-of-truth map, resume packet, and canonical group-capacity row now use the distinct-anchor/per-host-remnant wording.
The source-level repair is committed; runtime proof remains the only bounded capacity follow-up.

No gameplay files were edited by this auditor.
