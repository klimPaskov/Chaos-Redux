# Event 006 Darfur Council Parent Handoff

## Scope

Implemented the Event 006 Darfur Council package around custom tag `DFR`.

## Gameplay wiring

- Added `DFR` country tag, country definition, country history, and country localisation.
- Seeded `DFR` as a high-chaos Event 006 local-polity candidate from South Darfur `887`.
- Added runtime DFR cores for South Darfur `887` and North Darfur `767`, with cleanup if the package is not selected.
- Used South Darfur `887` as the reduced-release anchor.
- Kept North Darfur `767` as later petition/proof territory because vanilla marks it impassable and force-links it to Kordofan.
- Added Darfur package constants, package identity, package label, national spirit, decisions, mission, effects, triggers, AI markers, focuses, event-log records, and event-log labels.

## Assets

- Flag assets were produced by asset subagent `019e933b-e6bc-7db2-b34e-affc94210c94` in commit `944b9f35 Add Event 006 Darfur flag assets`.
- Final flag files:
  - `gfx/flags/DFR.tga`
  - `gfx/flags/medium/DFR.tga`
  - `gfx/flags/small/DFR.tga`
- Asset manifest:
  - `docs/assets/006_independence_wave/flags/darfur/manifest.md`
- The package uses vanilla `GFX_portrait_generic_africa_male_01` for the institutional leader portrait.

## Documentation

- Updated Event006 implementation docs, country package spec, focus tree spec, focus icon manifest, and event catalog workbook.
- Documented that the DFR flag is a sourced reconstruction, not a proven archival Darfur Sultanate standard.
- Documented that no ideology-specific DFR flag variants are present.

## Remaining risks

- Broader Event006 is still incomplete; this handoff covers only the Darfur package tranche.
- The Darfur flag has source uncertainty. The manifest records the source trail and contact sheet.
- No new Darfur advisors, bespoke portraits, animated seals, or ideology-specific flags were created in this tranche.
