# Event 006 focus layout current receipt — 2026-08-14

## Current engine evidence

The mandatory current `hoi4.focus_inspect` for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` returned `FOCUS_INSPECTED` at source revision `1fbce5b0e266a11a72230b5fa28ea6b265e3a0cde9d17525931e9295c2110a57`. The tree resolves 184 focuses and 196 connectors with zero crossings, zero node intersections, two long connectors, and no same-row spacing violations. The latest inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42b84867f0b243741cb08d3e18b213be884167dafb7cf0b3ad235c8d11827adf/b0c567c6501a1e3b4157af83f86d878e2f97080645fb20fa607e0693ce335e7c/focus-inspect.1fbce5b0e266a11a.json`.

The matching current `hoi4.focus_render` returned `FOCUS_RENDERED` at the same source revision. HTML, SVG, JSON, source-map, and plan artifacts are recorded under the latest render roots `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1febc1150e6bd05ff229f394220d3bdc27a575749ec0339905c18f224139dc09/e4a6e85eb1adb55f64359e1fa7939ef3c09dff30ccd529417b6e74d6a146bceb/` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2885cf3e1a4476386bd36c3716ca87926e34fa19d5727409a7b3c0315c8b0e2/2c37b3a1c40a8e6a900d7e67abd352652609516eb14703ae96076b7cee221b2a/`, with JSON/source-map/plan siblings returned by the render call.

## Remaining authored layout findings

Six Event 006 authored layout findings remain: four mechanically linear detours in the economy, army, and formable lanes, plus two long connectors from the military-archetype choice to independent command and from former-host policy to successor ledger. The remaining missing continuous-focus icon references are unrelated vanilla diagnostics. A coordinate-only trial was rejected because it introduced three node intersections and two same-row spacing violations; the final source preserves the prior zero-intersection layout and all gameplay prerequisites, availability gates, rewards, and route locks.

## Disposition

The focus framework remains structurally usable but layout acceptance is still bounded by the six authored findings and unrelated vanilla icon diagnostics. No gameplay, localisation, icon, adapter, Join, or attestation source was changed by this receipt.
