# Event 006 fourteen-package static allocation witness

Date: 2026-08-03

Status: source/static PASS for one standalone allocation; not a live-game or save/load claim.

## Scope

The allocator audit now validates one concrete fourteen-package witness from the current installed binding CSV, the current content-attestation trigger, the package loaders, and vanilla `history/states`. The witness is deliberately separate from the ordinary ten-package capacity receipt and from SCN-008 execution. It proves that a simultaneous fourteen-package frozen plan can be formed from currently admitted packages without reusing an anchor or tag and without erasing a former host's vanilla remnant.

`IW-012` (ICE) is intentionally omitted from this particular witness. Iceland's single vanilla state is also its anchor and capital, so releasing that anchor cannot satisfy the accepted former-host survival rule. ICE remains content-attested and remains available only when the runtime host-survival predicates reject unsafe selection.

## Exact witness rows

| Package | Tag | Former host | Anchor | Compact footprint | Reservation group | Protected host state |
| --- | --- | --- | --- | --- | --- | --- |
| IW-001 | SCO | ENG | 121 | 121, 133 | RG-121-120-133 | 126 |
| IW-002 | WLS | ENG | 122 | 122 | RG-122 | 126 |
| IW-004 | BRI | FRA | 14 | 14 | RG-14 | 16 |
| IW-006 | AFX | BEL | 34 | 34 | RG-34 | 6 |
| IW-007 | AGX | HOL | 36 | 36 | RG-36 | 7 |
| IW-008 | RHI | GER | 51 | 51 | RG-RHINE-SAAR | 64 |
| IW-009 | BAY | GER | 52 | 52, 53, 54 | RG-52-53-54 | 64 |
| IW-010 | AJX | GER | 42 | 42 | RG-RHINE-SAAR | 64 |
| IW-017 | COR | FRA | 1 | 1 | RG-1 | 16 |
| IW-018 | ARX | ITA | 114 | 114 | RG-114 | 2 |
| IW-019 | ASX | ITA | 115 | 115 | RG-115 | 2 |
| IW-023 | TRA | ROM | 84 | 84, 76 | RG-DANUBE-BORDERLAND | 46 |
| IW-173 | HAW | USA | 629 | 629 | RG-629 | 361 |
| IW-184 | HBX | USA | 378 | 378 | RG-378 | 361 |

The fourteen rows contain fourteen distinct anchors and fourteen distinct resolved tags. The only shared reservation group is `RG-RHINE-SAAR`, whose installed capacity is two and whose two claims are the exact `51`/`42` pair. All other witness groups remain single-slot groups.

## Checks encoded in the allocator audit

`.tools/audit_event6_allocator.py` checks every witness row for an admitted readiness verdict, a package loader, an exact current anchor, a compact footprint containing that anchor, complete current-state bindings, a documented former-host owner, dispatch presence, and an exact tag-availability guard. It checks that every compact state is owned by that former host in the binding evidence and that reservation-group counts do not exceed the installed group capacity.

For each former host, the audit subtracts the complete witness compact footprint from the vanilla-owned state set, requires a non-empty remnant, and selects the documented capital when it survives. The current protected-state receipt is `BEL=6`, `ENG=126`, `FRA=16`, `GER=64`, `HOL=7`, `ITA=2`, `ROM=46`, and `USA=361`.

Run from the mod root with:

```text
python -B .tools/audit_event6_allocator.py
```

The audit also retains the independent source-order receipts for anchor allocation, compact/extended optional passes, the frozen lock, Event 005-first joint reservation, and compensating rollback. The witness does not claim that a live HOI4 transaction has executed, that a save/load has been observed, or that the 20-country World Collapse band is currently feasible. With fifteen admitted packages total, the twenty-country band remains correctly fail-closed.

## Limitations

This handoff is static source evidence only. It does not promote any new package, alter the attestation set, bypass the ICE host-survival guard, replace the unresolved package, asset, AI, balance, formable, catalog, audio, or live-runtime gates, or treat the obsolete pasted flag-log attachment as evidence.
