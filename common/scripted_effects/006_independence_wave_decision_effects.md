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

## Event 006 IW-093 / IW-098 decision effects

### Purpose

The IW-093 and IW-098 helpers now live in the canonical
`common/scripted_effects/006_independence_wave_decision_effects.txt` registry
under the marked `MERGED SOURCE` section. They own the local paid decision
ledger, project completion, staged-idea lifecycle, and reset cleanup for the
Asante and Sokoto signature categories. They do not create formations, grant
stockpiled equipment, set runtime content attestations, or proclaim a formable.

### Scope and transaction inputs

All helpers run in country scope. Before calling a `begin_paid_decision_transaction`
helper, the decision sets the package-prefixed temporary cost variables. IW-093
accepts command power, infantry equipment, trains, and convoys; IW-098 also
accepts support equipment. A successful start spends those resources, records
the normal `paid_*` variables, and sets one transaction flag. Closing the
transaction clears its ledger only; it never refunds resources.

### Lifecycle helpers

- `independence_wave_iw093_initialize_decision_content` and its IW-098
  counterpart add the opening staged idea in either prepared or active package
  scope. The owning package setup calls this after its values initialize.
- `independence_wave_iw093_resolve_cocoa_depot_project` and
  `independence_wave_iw093_resolve_kumasi_rail_project` validate state 274,
  then apply the paid reconstruction result or failure.
- `independence_wave_iw098_resolve_caravan_wells_project` and
  `independence_wave_iw098_resolve_livestock_market_project` do the same for
  state 902.
- `independence_wave_iw093_begin_host_negotiation` and its IW-098 counterpart
  dispatch a country event to the exact frozen former host only after that
  country is living, independent, non-capitulated, outside a direct war, and
  still owns its capital. The released country remains in the shared active
  diplomacy lock until the host answers.
- The recognized and association settlement helpers write a host-outcome
  ledger, all eight bilateral values, all five country values, network
  standing, package values, and the final settlement receipt. A refusal writes
  the reclamation-conflict outcome and leaves an unresolved crisis instead of
  fabricating a local agreement.
- `independence_wave_iw093_ratify_post_crisis_settlement` and its IW-098
  counterpart close that crisis only after the shared host outcome has changed
  to recognition, guarded coexistence, client settlement, or host collapse.
  The 75-day ratification costs 10 command power and five trains, writes the
  final receipt, and adds a non-aggression pact only if the former host still
  survives.
- `independence_wave_iw093_cleanup_decision_content` and
  `independence_wave_iw098_cleanup_decision_content` remove all package
  decisions, package-local flags, ledgers, and staged ideas. Durable diplomatic
  consequences such as a non-aggression pact, guarantee, embargo, or wargoal
  are not erased by generation cleanup. The owning package cleanup must call
  the helper before it clears package setup state.

### Example

An IW-093 decision sets the four `independence_wave_iw093_decision_*_cost`
temporary variables, calls `independence_wave_iw093_begin_paid_decision_transaction`,
and checks `independence_wave_iw093_decision_transaction_result`. Its completion,
failure, and cancellation branches close the same transaction and clear their
active flag.

The former-host path deliberately separates preparation from outcome. The
90-day decision pays the diplomatic logistics and sends the protocol; it does
not write the receipt. Event `chaosx.nr006.9301` or `9801` gives the exact host
three substantive choices, and response events `9302`-`9304` or `9802`-`9804`
show the result to the released country.
