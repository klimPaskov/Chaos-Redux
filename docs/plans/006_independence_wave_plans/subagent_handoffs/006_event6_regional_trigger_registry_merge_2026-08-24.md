# Event 006 regional package-trigger registry consolidation — 2026-08-24

## Scope

This source-layout pass folds the fourteen regional Event 006 package-trigger files into one parser registry without changing any trigger identifier, block body, regional comment, package gate, reservation mutex, or allocator behavior.

## Merged source

The former `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt` through `..._region_14_triggers.txt` files are now represented by `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`.

The registry preserves 149 `can_plan_independence_wave_package_iw_*` gates and the two explicit regional reservation-mutex triggers for states 354 and 441. Regional headings are condensed while package blocks and substantive in-block research comments remain grouped by their original region.

## Preservation and validation

- A duplicate-name scan finds 151 unique top-level trigger definitions in the registry.
- The parser-source reduction removes thirteen files and saves 2,692 source bytes.
- The maintained `.tools/audit_event6_allocator.py` now reads the registry path and passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 40 adapters, 32 attestations, 29 compatible groups, and the exact `3/4/5/7/10` ladder.
- No package admission, reservation group, automatic weight, tag, state, or fail-closed gate was changed.
- This is a parser-file-count reduction only; it provides no live MCP parser, runtime allocation, or gameplay acceptance evidence.

Package-owned effects, country shells, decisions, focus overlays, localisation, and ownership-sensitive callback files remain separate.
