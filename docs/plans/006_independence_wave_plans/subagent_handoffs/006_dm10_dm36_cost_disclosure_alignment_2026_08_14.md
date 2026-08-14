# Event 006 DM-10 and DM-36 cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented as a bounded selector and localisation repair.

DM-10 `independence_wave_establish_treasury_and_currency` is accepted as administration standard plus three civilian factories, but its decision card selected the standard administration triplet, which displays two civilian factories. Its modifier already reserves `civilian_factory_major`.

DM-36 `independence_wave_buy_out_concession` is accepted as a strategic cost plus three civilian factories, but its decision card selected the standard strategic triplet, which displays two civilian factories. Its modifier already reserves `civilian_factory_major`.

## Changes

- `common/decisions/006_independence_wave_decisions.txt:483` now selects `independence_wave_cost_administration_major` for DM-10.
- `common/decisions/006_independence_wave_decisions.txt:1920` now selects `independence_wave_cost_strategic_major` for DM-36.
- `localisation/english/006_independence_wave_decisions_l_english.yml` adds complete base, `_tooltip`, and `_blocked` triplets for both selectors, displaying `civilian_factory_major` while retaining the existing command-power, manpower, stability, war-support, and convoy/train values.

No affordability trigger, payment effect, factory reservation, AI score, target gate, duration, cancellation, cleanup, admission, Join, package, or catalog behavior changed.

## Evidence basis

- `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` identifies DM-10 as administration standard plus a civilian-factory burden and DM-36 as civilian factories plus strategic cost.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_matrix_current_audit_2026_08_02.md` resolves those accepted rows to two factories for ordinary standard administration and three factories for DM-10 and DM-36.
- `common/script_constants/006_independence_wave_decision_constants.txt` defines `civilian_factory_standard = 2` and `civilian_factory_major = 3`.
- The live decision modifiers for both rows already use `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_MAJOR`; only the player-facing selector was inaccurate.

## Validation

The localisation file retains its UTF-8 BOM and each of the six new keys occurs exactly once. The two decision blocks resolve to their new selectors and retain the major factory modifier. The scoped source diff contains only the two selector changes, with no incidental line-ending change in the decision file. No MCP probability compare was required because the repair changes only cost text and does not change any weighted or eligibility surface.

## Boundary

This repair does not imply that every generic decision cost selector with a factory modifier is safe to rewrite. Package-specific keys, accepted cost palettes, and older unadmitted rows remain subject to their own matrix and owner review. Event 006 remains HOLD / PARTIAL at 40 adapters, 32 attestations, 29 compatible reservation groups, and 161 unattested selectable rows.
