# Event 006 Balkan package registry merge — 2026-08-25

## Scope

This is a source-layout-only consolidation for the seven unmodified Balkan package trigger/effect pairs: Banat (IW-024), Bosnia (IW-029), Epirus (IW-028), Macedonia (IW-026), Montenegro (IW-030), Thrace (IW-027), and Transylvania (IW-023).

## Receiver files

- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`

Each former file is retained as an explicit `# SOURCE:` block. Package-local identifiers, executable bodies, fixed-anchor proofs, lifecycle gates, dispatch helpers, cleanup, and substantive comments are preserved; only redundant per-file header banners are condensed. The seven trigger files supplied 79 unique top-level trigger identifiers; the seven effect files supplied 194 unique top-level effect identifiers.

## Removed parser files

- `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_macedonia_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_banat_package_effects.txt`
- `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt`
- `common/scripted_effects/006_independence_wave_epirus_package_effects.txt`
- `common/scripted_effects/006_independence_wave_macedonia_package_effects.txt`
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`
- `common/scripted_effects/006_independence_wave_thrace_package_effects.txt`
- `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt`

Kosovo remains in its original trigger/effect files because its trigger has an active concurrent cost change in the working tree; this tranche does not absorb or stage that unrelated edit.

## Audit evidence

- Receiver trigger definitions: 79 unique, no duplicates; braces 510/510.
- Receiver effect definitions: 194 unique, no duplicates; braces 1272/1272.
- Every former source's executable code-line sequence is present in its receiver after normalizing line endings and removing comments/blanks.
- The two receivers save 6,506 source bytes versus the fourteen former files after removing duplicate header banners and parser-file overhead.
- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and the exact 3/4/5/7/10 ladder.
- `python -B .tools/audit_event6_country_api.py` passed with zero missing or duplicate carriers.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 cells and eight edge cases.
- `python -B .tools/audit_event6_flags.py --strict` passed all 102 flag families.
- `python -B .tools/audit_event6_form16.py` and `python -B .tools/audit_event6_gui_matrix.py` passed.

No live parser, save/load, runtime, balance, admission, or gameplay completion claim is made. The merge changes file layout only.
