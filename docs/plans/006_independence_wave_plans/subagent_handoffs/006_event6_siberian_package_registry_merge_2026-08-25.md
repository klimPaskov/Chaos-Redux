# Event 006 Siberian package registry merge — 2026-08-25

## Scope

This is a source-layout-only consolidation for the four unmodified Siberian package trigger/effect pairs: Altai (IW-053), Buryatia (IW-052), Khakassia (IW-054), and Sakha (IW-051).

## Receiver files

- `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`

Each former file is retained as an explicit `# SOURCE:` block. Package-local identifiers, executable bodies, lifecycle gates, dispatch helpers, cleanup, and substantive comments are preserved; only redundant per-file header banners are condensed. The four trigger files supplied 69 unique top-level trigger identifiers; the four effect files supplied 138 unique top-level effect identifiers.

## Removed parser files

- `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_buryatia_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_khakassia_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_altai_package_effects.txt`
- `common/scripted_effects/006_independence_wave_buryatia_package_effects.txt`
- `common/scripted_effects/006_independence_wave_khakassia_package_effects.txt`
- `common/scripted_effects/006_independence_wave_sakha_package_effects.txt`

Komi, Tatarstan, Udmurtia, and Ruthenia remain in their original files because their trigger files have active concurrent edits; this tranche does not absorb or stage those changes.

## Audit evidence

- Receiver trigger definitions: 69 unique, no duplicates; braces 349/349.
- Receiver effect definitions: 138 unique, no duplicates; braces 864/864.
- Every former source's executable code-line sequence is present in its receiver after normalizing line endings and removing comments/blanks.
- The two receivers save 4,069 source bytes versus the eight former files after removing duplicate header banners and parser-file overhead.
- The Event 006 allocator, country API, scenario matrix, strict flag, FORM-16, and Statehood Ledger source audits were already passing immediately before this source-only merge; this tranche changes no identifiers or gameplay logic.

No live parser, save/load, runtime, balance, admission, or gameplay completion claim is made. The merge changes file layout only.
