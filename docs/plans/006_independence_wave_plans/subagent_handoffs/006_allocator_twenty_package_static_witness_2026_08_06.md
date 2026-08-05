# Event 006 twenty-package static capacity witness

Date: 2026-08-06

## Scope

The allocator audit previously proved only a sixteen-package standalone witness even though the current content-attestation set contains 21 packages. A source-only subset search was run against the installed binding ledger and vanilla state history. It found a valid 20-package witness by excluding only IW-012 ICE, whose one vanilla state is also its former-host remnant.

## Witness IDs

`IW-001`, `IW-002`, `IW-004`, `IW-006`, `IW-007`, `IW-008`, `IW-009`, `IW-010`, `IW-014`, `IW-017`, `IW-018`, `IW-019`, `IW-023`, `IW-033`, `IW-041`, `IW-070`, `IW-071`, `IW-072`, `IW-173`, and `IW-184`.

The excluded attested row is `IW-012` ICE. It remains a valid runtime candidate only when its owner/host state differs from the one-state vanilla baseline and all ordinary preflight gates pass.

## Checks proved

- Every witness ID is centrally content-attested and has a package loader.
- Every row has one unique anchor and one unique resolved tag.
- Compact footprints contain their anchors, are pairwise disjoint, and are owned by the documented former host in the installed binding ledger.
- The two-slot `RG-RHINE-SAAR` exception remains limited to IW-008 and IW-010.
- Every former host retains at least one vanilla-owned state, with capital preference when its capital survives.
- The automatic ladder remains `6 / 8 / 10 / 14 / 20`, with World Collapse at 20.

## Changed source

- `.tools/audit_event6_allocator.py` now uses `STATIC_20_WITNESS_IDS` and validates 20 unique anchors/tags through `validate_static_20_witness`.

No gameplay, country, state, tag, portrait, flag, advisor, localisation, or runtime execution file was changed by this capacity proof.

## Validation

```text
python -B .tools/audit_event6_allocator.py
```

Result: pass. The audit reports 21 attested packages, 20 compatible reservation groups, and a 20-package static standalone witness with protected former-host states `BEL=6`, `ENG=126`, `FIN=111`, `FRA=16`, `GER=64`, `HOL=7`, `ITA=2`, `ROM=46`, `SOV=219`, `SPR=41`, and `USA=361`.

## Boundary

This is source/static evidence, not a live save or engine transaction. It does not admit ICE in the vanilla one-state baseline, promote any unattested package, or close the separate package, asset, formable, AI, audio, catalog, and runtime-evidence gates.
