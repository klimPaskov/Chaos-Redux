# Event 006 IW-155 Bali compatibility adapter handoff

Date: 2026-08-14

## Disposition

IW-155/BLI remains dormant and fail-closed. This tranche adds only a package-local preservation boundary for a future source-backed Balinese institution. It does not create a playable package, add a central adapter, add content attestation, alter normal or scenario preflight, widen Join, or select a flag, portrait, leader identity, or route.

## Source changes

- `common/scripted_triggers/006_independence_wave_iw155_bli_compatibility_triggers.txt`
  - `is_independence_wave_iw_155_bli_compatibility_context`
  - `has_independence_wave_iw_155_bli_anchor_surface`
  - `has_independence_wave_iw_155_bli_vanilla_surface`
  - `has_independence_wave_iw_155_bli_compatibility_contract`
- `common/scripted_effects/006_independence_wave_iw155_bli_compatibility_effects.txt`
  - `independence_wave_iw_155_bli_compatibility_clear_institution_selection`
  - `independence_wave_cleanup_iw_155_bli_compatibility`

The context requires original tag `BLI`, active Event 006 origin, the IW-155 package id, and an explicit future institution-selection marker. The anchor witness requires ownership and control of state 1052, a capital in state 1052, and the existing BLI core. The vanilla witness requires `INS_dewa_geg` and Indonesia's `INS_releasables` entry for BLI. The cleanup effect clears only the future selector marker and is idempotent under the full contract.

## Vanilla preservation evidence

- `history/countries/BLI - Bali.txt`: capital 1052 and `INS_dewa_geg` recruitment.
- `history/states/1052-Bali.txt`: Indonesian owner, BLI core, and the installed Bali state surface.
- `history/countries/INS - Indonesia.txt`: `BLI` is present in `INS_releasables`.
- `common/characters/INS.txt`: `INS_dewa_geg` is the installed vanilla BLI-linked leader.
- `common/scripted_effects/INS_scripted_effects.txt`: `indonesia_transfer_BLI` remains the vanilla owner of leader transfer behavior and was not modified.

## Engine evidence

The mandatory map inspection was retried without a duplicate allocation request after the first attempt returned `MAP_STATE_ID_COLLISION`. The focused state-1052 inspection returned `MAP_INSPECTED` with selected membership/network checks passing. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f04868042f3be9e9c18e25dcaa082e054fa061a5c14859dbadc364dce5b39f52/91c31ae457eb16b3fb78c8229720f47d01e69a673c359bf9ea3324dee1cf607e/map-inspect.24bebf72ae84437c.json`.

Aggregate map validation remains false only because the workspace contains unrelated building/port locator diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`). No map rewrite was performed.

## Explicit boundaries and follow-up

No country/history, leader, portrait, flag, localisation, asset, central dispatch, attestation, preflight, scenario, Join, or vanilla Indonesia source was changed. The source contract is intentionally inert until a named Balinese institution, period-fit identity, portrait provenance, and symbol policy are accepted. The existing IW-155 research, portrait, and symbol handoffs remain the admission authority; this adapter does not supersede their HOLD/fail-closed findings.
