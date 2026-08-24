# Event 006 regional package-publisher registry consolidation — 2026-08-24

## Scope

This source-layout pass folds the fourteen regional Event 006 package-publisher effect files into one parser registry without changing any effect identifier, block body, package metadata, weight, reservation publisher, regional rule, or allocator behavior.

## Merged source

The former `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` through `..._region_14_effects.txt` files are now represented by `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`.

The registry preserves 470 unique top-level effect definitions, including the 149 package loaders, weights, and reservation publishers consumed by the central allocator. Regional source headings are condensed while the package blocks and substantive in-block research comments remain grouped by their original region.

## Preservation and validation

- A body comparison against all fourteen pre-merge files finds no missing package block.
- A duplicate-name scan finds 470 unique effect identifiers.
- The maintained `.tools/audit_event6_allocator.py` now reads the registry path and passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 40 adapters, 32 attestations, 29 compatible groups, and the exact `3/4/5/7/10` ladder.
- The parser-source reduction removes thirteen files and saves 2,675 source bytes; it does not change gameplay behavior.
- This provides no live MCP parser, runtime allocation, or gameplay acceptance evidence.

Package-local effects, focus/decision overlays, country shells, localisation, and ownership-sensitive callbacks remain separate.
