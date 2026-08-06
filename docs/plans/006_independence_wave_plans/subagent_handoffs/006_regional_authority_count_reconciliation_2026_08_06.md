# Event 006 regional authority-count reconciliation

Date: 2026-08-06.

Scope: documentation-only cleanup of the Northern/Western Europe and Pacific country-package summaries after the current IW-026/IW-029 promotion and ordinary super-event numbering reconciliation.

## Current authority

The current Event 006 allocator boundary is 23 content-attested selectable packages across 22 compatible reservation groups, with 170 selectable rows still unattested out of 193 non-overlay rows. The central dispatcher exposes 32 package adapters, of which nine remain adapter-only and fail closed. Current ordinary super-event identifiers are 23 and 24; dated four-digit identifiers remain historical traceability only.

## Files changed

- `docs/events/006_independence_wave/northern_western_europe_packages.md` marks its 2026-08-03 regional snapshot historical and routes the current summary through the IW-026/IW-029 promotion and 23/22/170 authority.
- `docs/events/006_independence_wave/pacific_country_packages.md` replaces pre-promotion 21/20 and 19/18 current-sounding counts with the 23/22/170 authority while preserving the dated installed scan.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 23 attested packages and 22 compatible reservation groups.
- `git diff --check` passed on both regional pages.

No gameplay, asset, localisation, spreadsheet, tag, or runtime source was changed. The whole event remains HOLD / PARTIAL; the reconciliation does not promote a package, formable, audio source, or live evidence.
