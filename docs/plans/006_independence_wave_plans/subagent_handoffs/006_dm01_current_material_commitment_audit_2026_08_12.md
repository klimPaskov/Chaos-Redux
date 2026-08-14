# Event 006 DM-01 material-commitment audit — 2026-08-12

> Current-authority note (2026-08-14): this DM-01 source receipt remains valid for the material-cost contract, but its dated whole-event counts are superseded by the current 40-adapter / 32-attestation / 29-group / 161-unattested boundary. Do not use the older arithmetic below for current routing.

## Disposition

DM-01, `independence_wave_secure_provisional_capital`, is currently implemented as the automatic country-scoped founding mission described by the accepted matrix and mechanics specification. It keeps the assigned-division and capital-control objective, adds the specified infantry/support-equipment commitment, uses the isolated-capital train-or-motorized alternative, and preserves the 30-to-75-day founding window. This handoff supersedes the earlier garrison-only/no-click-cost findings in `006_dm01_spec_alignment_audit_2026_08_12.md` and `006_event006_decision_mission_audit_2026_08_11.md`; those files remain historical traceability rather than current source authority.

## Current source contract

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt` gates activation on an active, complete package, capital control, force-tier garrison, force-tier equipment stock, and either a capital supply node or the isolated transport reserve.
- Fragile, viable, and armed/high-chaos force levels require the light, standard, and major infantry/support tiers respectively. A legacy or incomplete package with no published `independence_wave_force_level` uses the standard tier.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` consumes the matching infantry/support tier at activation. An isolated capital consumes ten trains when that reserve is available, otherwise one hundred motorized equipment. The commitment is sunk and is not refunded on mission cancellation.
- `common/script_constants/006_independence_wave_decision_constants.txt` centralizes displayed spend, strict-`>` affordability gates, the 75-day ceiling, the fragile/viable adjustments, and the train/truck quantities.
- The mission starts only through `independence_wave_start_provisional_capital_mission`, which sets the reservation flag, pays once, activates the automatic mission, and subtracts 45 days for fragile or 30 days for viable force levels. Armed and high-chaos retain 75 days.
- Mission success records `independence_wave_dm01_capital_secured` and `independence_wave_dm01_capital_administration_ready`; failure on lost capital control or garrison records the failure/relocation state, applies the founding pressure deltas, refreshes the collapsed-cabinet/warlord ideas, and fires `chaosx.nr6.311` for an owned-and-controlled relocation choice or dispersed emergency offices.
- Decision-layer cleanup removes the mission and clears reservation, success, failure, administration, and relocation flags, so a later valid generation cannot inherit a stale DM-01 receipt.

## Narrow consistency repair

The activation trigger's no-force-level fallback requires the standard material gates. The payment effect now has an explicit no-force-level branch that consumes the standard infantry/support spend before the major-tier fallback for published armed/high-chaos values. This keeps the affordability witness and the sunk payment identical for legacy or incomplete package setup.

## Validation and limits

Focused source inspection confirms balanced DM-01 blocks, the four equipment-tier branches, the train/motorized alternative, the 30/45/75-day timeout arithmetic, and cleanup of the reservation/failure lifecycle. The allocator and scenario-matrix figures cited by this dated DM-01 audit are historical snapshots. Current Event 006 routing is 32 content-attested packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters (`32/29/161/40`). A fresh `hoi4.probability_inspect` and narrow Event 006 inspection were attempted against the then-current workspace, but the MCP returned `ARTIFACT_MANIFEST_INVALID` (`Artifact provenance manifest is invalid`) before scanning; no current engine, live execution, save/load, or quantitative probability claim follows.

The whole Event 006 objective remains **HOLD / PARTIAL** because 161 selectable rows are unattested under the current 32/29/161/40 authority, eight adapter-only packages remain fail-closed, ordinary League super-event 23 audio/wrappers/firing remain unresolved, and current MCP evidence remains partial for workspace-wide lifecycle projection.
