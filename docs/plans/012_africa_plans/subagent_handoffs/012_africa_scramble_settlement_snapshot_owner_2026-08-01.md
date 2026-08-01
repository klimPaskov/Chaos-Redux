# Event 012 Scramble settlement snapshot owner handoff

Date: 2026-08-01

Scope: narrow non-model achievement-owner correction.

## Changed files

- `common/scripted_effects/012_africa_world_order_effects.txt`
- `docs/events/012_africa/world_order.md`

## Runtime correction

`africa_achievement_capture_scramble_settlement_snapshot` now runs from both `africa_scramble_ratify_aftermath` and `africa_scramble_close_continental_docket`, immediately before aftermath materials and response-roster cleanup. The existing helper records the current hostile non-African control count and can set `africa_achievement_no_hostile_foreign_control` only when the separate coalition-defeat proof already exists. It does not create a new achievement proxy, alter settlement gates, or install an external package.

The coalition-break action keeps its existing immediate snapshot call. Repeated calls are harmless because the settlement paths are flag-gated and the helper writes the current settled state.

## Validation and remaining risk

The two settlement callers and the helper resolve by literal source reference. Static brace and unsupported-operator checks remain required before commit. Engine and live achievement acceptance remain open because this workspace is not launching Hearts of Iron IV.
