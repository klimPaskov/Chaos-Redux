# Event 006 YAK and FER cleanup reference repairs — 2026-08-15

## Disposition

This bounded package-local repair corrects two concrete cleanup references without changing route behavior, costs, central admission, Join, maps, history, assets, or authority counts.

## Repairs

- YAK cleanup now removes `independence_wave_yak_hold_arctic_council`, matching the mission defined and localised by the IW-051 decision surface.
- FER cleanup now restores the `independence_wave_fer_*_party` and `_party_long` keys that FER setup and localisation actually define, instead of the unowned bare `FER_*` keys.

The changes are lifecycle-symmetric reference fixes only. They do not alter politics values, route selection, or party text.

## Validation

The YAK mission definition, cleanup reference, and localisation key now match exactly. All eight FER cleanup party keys resolve to the FER localisation file, and the FER/YAK package scripts remain balanced with no unsupported operators. The allocator and SCN-008 audits remain at 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder.

## Remaining gates

YAK and FER remain package-local and fail-closed. Identity/rights, flag provenance, ordered-anchor or host evidence, typed probability, central adapter, attestation, preflight, scenario, and Join decisions remain outside this repair.
