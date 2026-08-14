# Event 006 IW-171 OKN compatibility adapter handoff

Date: 2026-08-14

## Disposition

IW-171/Ryukyu remains high-chaos-only, dormant, and fail-closed. This tranche adds a package-local preservation boundary for a future named Ryukyu institution. It does not create a playable release, change Japanese history or focus content, widen central admission, or add an attestation, preflight, scenario, or Join entry.

## Source changes

- `common/scripted_triggers/006_independence_wave_iw171_okn_compatibility_triggers.txt`
  - `is_independence_wave_iw_171_okn_compatibility_context`
  - `has_independence_wave_iw_171_okn_anchor_surface`
  - `has_independence_wave_iw_171_okn_vanilla_surface`
  - `has_independence_wave_iw_171_okn_compatibility_contract`
- `common/scripted_effects/006_independence_wave_iw171_okn_compatibility_effects.txt`
  - `independence_wave_iw_171_okn_compatibility_clear_named_selection`
  - `independence_wave_cleanup_iw_171_okn_compatibility`

The context requires original tag `OKN`, active Event 006 origin, package id `iw_171`, and an explicit future named-institution marker. The anchor witness requires ownership and control of state 526, a state-526 capital, and the installed OKN core. The vanilla witness requires `OKN_hiroshi_sho`. Cleanup clears only the named-institution marker and is safe to repeat under the complete contract.

## Vanilla preservation evidence

- `history/countries/OKN - Okinawa.txt`: capital 526 and recruitment of `OKN_hiroshi_sho`.
- `history/states/526-Okinawa.txt`: installed state surface and OKN core.
- `common/characters/OKN.txt`: registered `OKN_hiroshi_sho` character and vanilla portrait token.
- The existing Japanese/OKN history, focus, and event behavior remains untouched; this adapter has no mutation effect beyond its future selector cleanup.

## Research and map binding

The accepted research row `IW-171` binds `OKN` to Ryukyu, state 526/Okinawa, reservation group `RG-526`, and a high-chaos-only disposition. The installed-map binding remains unchanged and requires the compact anchor to survive.

## Explicit boundaries

No central dispatch, attestation, normal or scenario preflight, Join, release selector, country/history, character, portrait, flag, localisation, workbook, or Japanese route source was changed. The adapter does not resolve the open period-institution, portrait, or symbol gates; those remain prerequisites for any future admission decision.

## Validation evidence

- Static source review: both new Clausewitz files have balanced braces, tab indentation, and no unsupported comparison operators. The marker-only effect has no weighted logic and no probability audit surface.
- `hoi4.map_inspect` for state 526 returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74e6ddc3c64bd7b42ca01eb0e4cad581d0af6bc07a4f40f5ec0adf159e5db7f3/2c950cdff2eeb8309a94c5517e97e74d7d98ce31be212dd9696ca2cc1a36f5e1/map-inspect.24bebf72ae84437c.json`. State membership and map geometry checks passed; workspace-wide building/port locator diagnostics remain unrelated and make aggregate validation false.
- `hoi4.event_inspect` focused on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec681e97d9e353a2727becefce79abed0ae43a5c34de776e8b225fd9fbb6080c/375dcab06ebdda5844fce2dbc2b5ee493624ce0cc17a5df38332e6cd5858015e/event-scan-741883f50501.json`. No selected blocking diagnostics were reported; workspace-wide helper/lifecycle analysis remains deferred.
