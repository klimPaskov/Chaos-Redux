# Event006 Khiva Package Handoff

## Scope

Parent implementation tranche for the Event006 Independence Wave Khiva historical-return package.

## Vanilla and Event005 separation evidence

- Vanilla `KHI` is registered in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt` and uses `countries/Khiva.txt`.
- Vanilla `KHI - Khiva.txt` sets capital state `831`.
- Vanilla states `831` Khiva and `832` Dashhowuz already core `KHI`.
- Vanilla `KHI` flag assets exist in normal, medium, and small flag folders for the ideology variants.
- Event005 references `KHI` in progressive-release candidate logic, while its bespoke Khwarazmian successor uses custom tag `KHW`. This tranche keeps Khiva behind Event006 high-chaos package gates and Event006 origin/package flags.

## Implemented wiring

- Added Event006 Khiva package constants, event-log types, package id, formation family, costs, thresholds, gains, integration stage, and failure pressure.
- Added high-chaos `KHI` package seeding, release-anchor preference for state `831`, package classification, startup spirit, achievement tracking, and event-log recorders.
- Added Khiva Formation Ledger decisions for the canal council, water charter, Khanate Assembly proclamation, and post-proclamation integration mission.
- Added two shared provisional focus-tree overlay nodes for Khiva canal council and water charter proof.
- Added Khiva national spirit, AI old-name package restraint, achievement eligibility, scripted package label, event-log scripted localisation, and player-facing localisation.
- Updated Event006 documentation and country-package source spec.

## Assets and files not touched

- No `gfx/flags`, `flags`, `common/countries`, or `history/countries` files were changed.
- No new flag art was needed because vanilla `KHI` assets exist.
- No Event005 files were edited by this tranche. The worktree still contains unrelated pre-existing Event005 modifications.

## Remaining risks

- Khiva uses shared Event006 icons and the existing Assyrian recognition congress idea picture as a placeholder-style package spirit image, matching the Bukhara tranche. Future route-specific art can replace this without renaming gameplay identifiers.
- Full Event006 source-spec completion still needs additional package depth and final audit passes.
