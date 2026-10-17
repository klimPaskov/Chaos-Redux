# Event 006 shared decision effect helpers

This file documents the shared package helpers appended to `006_independence_wave_decision_effects.txt` and `006_independence_wave_minor_overlay_effects_registry.txt`.
Every package, decision, focus, and event option calls these helpers directly instead of a per-tag copy.
The helpers take no parameters and read or write only the temporary variables named below.
They add no event targets, flags, or cleanup lifecycle.

## Country delta packages

Each helper sets the five temporary `independence_wave_decision_*_delta` values from `independence_wave_decision_effect` constants and then calls `independence_wave_decision_apply_country_deltas`.
All of them run in country scope.

| Helper | Package |
| --- | --- |
| `independence_wave_apply_administrative_progress` | Minor legitimacy, standard capacity, minor security gain, minor instability relief |
| `independence_wave_apply_security_progress` | Minor legitimacy and capacity, standard security gain, minor instability relief |
| `independence_wave_apply_diplomatic_progress` | Minor legitimacy and capacity, standard recognition gain, minor instability relief |
| `independence_wave_apply_major_settlement` | Standard legitimacy, recognition and capacity gain, minor security gain, standard instability relief |
| `independence_wave_apply_project_failure` | Standard legitimacy, capacity and security loss, minor recognition loss, major instability |

Usage: `independence_wave_apply_major_settlement = yes` inside a decision `complete_effect`, a focus reward, or an event option.
Package helpers that also move a package ledger call one of these first and then write their own ledger deltas.
The regional helpers `independence_wave_mediterranean_apply_security_progress`, `independence_wave_mediterranean_apply_diplomatic_progress`, `independence_wave_mediterranean_apply_major_settlement`, and `independence_wave_rhine_bavaria_settle_former_host_ledgers` remain as one-line wrappers because Event 006 support events call them by those names.

## Former-host settlement

All three helpers do nothing unless `has_independence_wave_living_former_host` holds. They then set the eight bilateral host deltas and call `independence_wave_decision_apply_host_deltas`.

| Helper | Extra requirement |
| --- | --- |
| `independence_wave_apply_former_host_settlement` | None |
| `independence_wave_apply_former_host_settlement_unless_at_war` | The former host is not at war with the calling country (`PREV` inside the host scope) |
| `independence_wave_apply_former_host_settlement_unless_at_war_with_root` | The former host is not at war with `ROOT` |

The Mediterranean and Pacific packages keep their own former-host packages because their claim delta differs.

## Delta resets

| Helper | Zeroes |
| --- | --- |
| `independence_wave_reset_country_deltas` | The five temporary country deltas |
| `independence_wave_reset_host_deltas` | The eight temporary bilateral host deltas |
| `independence_wave_reset_decision_deltas` | All thirteen, by calling both helpers |

Call a reset before an option writes only the dimensions it actually changes.

## Baseline laws

`independence_wave_ensure_baseline_laws` installs civilian economy, export focus, and volunteer only in country scope when the country does not already hold them.
Package setup effects call it once during admitted setup.

## Overlay payment effects

`independence_wave_region_overlay_pay_cabinet`, `_depot`, `_force`, `_guard`, and `_charter` spend the materials priced by `independence_wave_iw_region_overlay_cost` for the regional overlay packages.
`independence_wave_cog_overlay_pay_cabinet`, `_depot`, `_force`, `_guard`, and `_charter` do the same from `independence_wave_iw_cog_overlay_cost` for the Congo overlay packages.
Overlay start and decision effects call the matching helper directly.
