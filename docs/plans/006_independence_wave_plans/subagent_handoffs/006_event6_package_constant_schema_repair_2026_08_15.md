# Event 006 package constant schema repair — 2026-08-15

## Disposition

This is a bounded script-constant consistency repair for package-local Event 006 tuning files. It does not change any constant values, gameplay formulas, central adapters, attestations, preflights, scenario selection, deterministic Join, map ownership, history, assets, or authority counts.

## Changes

Explicit schema blocks were added to the existing pressure, duration, cost, politics, and package-specific force groups where they were missing in these package-local files: ALT, BSK, BYA, KHA, KOM, MEL, and UDM. Pressure and politics groups use `fixed_point`, duration and cost groups use `int`, and the ALT force group uses `int`.

The repair brings these package-local groups into the same documented script-constants form already used by the FER and YAK tranches. Existing values, names, references, and package gates remain unchanged.

KUB and TAT were intentionally excluded because their current worktree differences are BOM-only changes from unrelated concurrent work.

## Validation

All seven touched files retain balanced Clausewitz blocks and their original numeric values. The Event 006 allocator and SCN-008 scenario audits remain unchanged at 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder.

## Remaining boundary

The package-local schema repair does not make any package admitted or selectable. Identity, rights, map, host, asset, typed-probability, central-attestation, preflight, scenario, and Join gates remain governed by their existing fail-closed contracts.
