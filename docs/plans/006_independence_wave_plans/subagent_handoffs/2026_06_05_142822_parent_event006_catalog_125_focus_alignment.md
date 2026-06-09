# Event 006 Catalog 125-Focus Alignment Parent Handoff

## Superseded Status

Partially superseded by the 2026-06-05 user correction. This handoff remains useful for the 125-focus catalog alignment history, but any wording that treated Kuban (`KUB`) or Altai (`ALT`) as current Event 006 package summaries or focus-overlay scope is no longer source-of-truth. The current accepted new-country lane is niche generic releases such as `ASN`, `KBN`, `PLM`, and `AYM` sharing `independence_wave_liberation_provisional_tree`.

## Scope

Updated count-bearing Event 006 catalog and focus-icon documentation after the live Liberation Provisional focus tree reached 125 focuses.

This was a catalog and asset-ledger alignment pass only. No gameplay, localisation, flags, image assets, `.gfx`, `.gui`, or source specs were edited.

## Files Changed

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_142822_parent_event006_catalog_125_focus_alignment.md`

## Workbook Cells Updated

Sheet: `Main Sheet`, row `7`.

- `C7`: changed the implementation summary from the stale 123-focus tree reference to the current shared 125-focus Liberation Provisional tree.
- `G7`: historical note only after the correction: this row previously added Kuban, Altai, and Zulu package summaries to the Evo IV package list. Kuban and Altai are superseded as current package scope; Zulu remains accepted.
- `O7`: changed the catalog summary from the stale 121-focus tree reference to the current 125-focus Liberation Provisional tree.

Status cells remain intentionally unchanged:

- `L7`: `In progress`
- `R7`: `In progress`

Event 006 is still not complete.

## Focus Icon Ledger Updates

- `manifest.md`: changed focus references from 123 to 125.
- `reuse_ledger.md`: changed the reuse count from 115 to 125 and added the ten missing current focus-to-sprite mappings:
  - `independence_wave_don_river_records`
  - `independence_wave_don_petition_map`
  - `independence_wave_kuban_black_sea_records` (superseded as current requested scope)
  - `independence_wave_kuban_petition_map` (superseded as current requested scope)
  - `independence_wave_altai_oyrot_records` (superseded as current requested scope)
  - `independence_wave_altai_petition_map` (superseded as current requested scope)
  - `independence_wave_darfur_records`
  - `independence_wave_darfur_petition_map`
  - `independence_wave_zulu_records`
  - `independence_wave_zulu_petition_map`

## Validation

- Live focus count: 125 `focus = {` blocks.
- Live focus icon assignments: 125 assignments across 25 unique `GFX_focus_independence_wave_*` sprites.
- Focus icon ledger coverage after patch: 125 mappings, 0 missing mappings, 0 extra mappings.
- Source workbook archive test: `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx` passed.
- Source workbook XML scan: `125-focus` count 2; stale `121-focus`, `123-focus`, `115-focus`, `119-focus`, `117-focus`, `99-focus`, `79-focus`, and `60-focus` count 0; formula-error strings count 0.
- LibreOffice headless conversion to `/tmp/chaosx_catalog_validate_event006_125/chaos_redux_events_catalog.xlsx` passed.
- Converted workbook archive test passed.
- Converted workbook XML scan: `125-focus` count 2; stale focus-count strings count 0; formula markers count 30; formula-error strings count 0.
- Focused Event 006 brace-balance check passed for event, scripted effect, scripted trigger, decision, focus, scripted GUI, and GUI files.
- Focused Event 006 localisation reference check found 0 missing core event/focus/decision/GUI keys.
- Workbook row remains `In progress` in both status cells because package depth, final visual support, final audits, and completion validation remain open.

## Remaining Risks And Omissions

- This pass does not implement new packages, formables, GUI states, assets, or validation scenarios.
- Event 006 remains incomplete as a full source-spec pack.
