# Event 006 flag-atlas ideology variant repair — 2026-08-03

## Symptom

The engine log reported `flagtextureatlas.cpp:510` for Event 006 tags with `Ideology democratic` and an empty `gfx/flags/` path. The registered tags had normal, medium, and small unsuffixed TGA triplets, but most had no ideology-specific flag names.

## Repair

Every tag registered in `common/country_tags/006_independence_wave_countries.txt` now has the complete engine-facing family in each flag atlas:

- `gfx/flags/<TAG>.tga` plus `_communism`, `_democratic`, `_fascism`, and `_neutrality`;
- `gfx/flags/medium/<TAG>.tga` plus the same four ideology suffixes;
- `gfx/flags/small/<TAG>.tga` plus the same four ideology suffixes.

The 1,188 missing suffixed files were copied from each tag's existing reviewed normal, medium, or small master. This preserves the accepted national or historical flag design across ideology changes; it does not introduce placeholder artwork or a second flag design. The source and processed masters remain in the Event 006 asset packages under `docs/assets/006_independence_wave/`.

## Audit change

`.tools/audit_event6_flags.py` now checks the unsuffixed triplet and all four ideology variants, because HOI4 resolves ideology-specific names before the unsuffixed fallback. The audit reports complete flag families instead of only triplets.

## Evidence

`python -B .tools/audit_event6_flags.py --strict` reports 102 registered tags, 102 complete flag families, and 0 incomplete families. A direct suffix scan reports 0 missing Event 006 ideology variants.

No gameplay, tag identity, history, or package-readiness flags were changed. No live game or save/load evidence is claimed.

## Remaining status

This repairs the reported flag-atlas error. The overall Event 006 goal remains HOLD/PARTIAL for the separate package research/rights, formable readiness, 6001 audio, catalog promotion, AI/balance evidence, and runtime-proof gates recorded in the current completion handoff.
