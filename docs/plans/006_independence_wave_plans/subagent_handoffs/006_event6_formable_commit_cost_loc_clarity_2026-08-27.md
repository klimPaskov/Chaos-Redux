# Event 006 formable commitment cost localization clarity

Date: 2026-08-27

## Scope

This handoff records a parent-owned localization-only correction for the shared Event 006 formable commitment cost row.

## Changed surface

- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `independence_wave_formable_commit_cost_civic`
- `independence_wave_formable_commit_cost_revolutionary`
- `independence_wave_formable_commit_cost_military`

## Correction

The three rows no longer advertise the `war_support_minor` token because the selected formable commitment payment helpers do not consume war support.

The rows now use `GetIndependenceWaveDiplomaticStandardTransportCostText`, which displays the convoy-or-train alternative selected by the existing diplomatic payment helper instead of showing both transport icons as simultaneous charges.

The remaining stability, command power, manpower, army experience, infantry equipment, and support equipment values continue to match the selected method's payment effects and trigger thresholds.

## Validation and boundary

The localization file retains its UTF-8 BOM and the changed keys remain unique.

This handoff makes no gameplay, package-admission, asset, GUI, spreadsheet, or event-lifecycle change and makes no live-game claim.

Event 006 remains HOLD / PARTIAL pending the documented package, identity, rights, MCP, probability, GUI, super-event, and live lifecycle blockers.
