# Event 006 Western/North Atlantic package registry merge — 2026-08-25

## Scope

This is a source-layout-only consolidation for the three unmodified package trigger/effect pairs: Brittany (IW-004), Catalonia (IW-014), and Iceland (IW-012).

## Receiver files

- `common/scripted_triggers/006_independence_wave_western_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_western_package_effects.txt`

Each former file is retained as an explicit `# SOURCE:` block. Package-local identifiers, executable bodies, package constants, lifecycle gates, dispatch helpers, cleanup, and substantive comments are preserved; only redundant per-file header banners are condensed. The three trigger files supplied 33 unique top-level trigger identifiers; the three effect files supplied 84 unique top-level effect identifiers.

## Removed parser files

- `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_brittany_package_effects.txt`
- `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`
- `common/scripted_effects/006_independence_wave_ice_package_effects.txt`

## Audit evidence

- Receiver trigger definitions: 33 unique, no duplicates; braces 180/180.
- Receiver effect definitions: 84 unique, no duplicates; braces 555/555.
- Every former source's executable code-line sequence, including its file-scoped constants, is present in its receiver after normalizing line endings and removing comments/blanks.
- The two receivers save 2,190 source bytes versus the six former files after removing duplicate header banners and parser-file overhead.
- The Event 006 allocator, country API, scenario matrix, strict flag, FORM-16, and Statehood Ledger source audits passed after the preceding source-layout tranche; this merge changes no identifiers or gameplay logic.

No live parser, save/load, runtime, balance, admission, or gameplay completion claim is made. The merge changes file layout only.
