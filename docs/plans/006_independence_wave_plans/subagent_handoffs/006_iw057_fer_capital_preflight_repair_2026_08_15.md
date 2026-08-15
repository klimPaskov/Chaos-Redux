# IW-057 Far Eastern Republic capital preflight repair — 2026-08-15

## Disposition

Applied one package-local trigger repair so the dormant vanilla FER history capital does not prevent the Event 006 package from reaching its accepted 408/409 runtime anchors.

## Source change

`common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt` now lets `is_independence_wave_exact_package_iw_057_tag_available` accept either the selected 408/409 capital anchor or vanilla dormant FER capital state 563.

The exception is limited to the pre-release identity gate. `is_independence_wave_exact_package_iw_057_runtime_ready` and `can_initialize_independence_wave_iw_057_package` still require a 408/409 capital anchor, and the shared execution pass sets the selected anchor before package setup.

## Why this is safe

`is_independence_wave_candidate_origin_available` still requires the FER country to be absent and not reserved by another origin system. The 563 branch therefore does not admit a living FER country or create a second runtime capital. It only accommodates the vanilla dormant history row while the generic Event 006 execution pass reanchors the package to the selected 408/409 state.

## Scope boundaries

This does not clear FER identity, institutional-roster, portrait, flag, probability, central-attestation, normal-preflight, scenario-preflight, or Join gates. No central adapter/attestation/Join files, history files, flags, portraits, localisation, or AI weights were changed.

## Validation

The relevant trigger block remains balanced and the existing FER package references are unchanged apart from the bounded pre-release capital OR. A fresh Event 006 inspect/render pass is required after the edit; the installed MCP commonly reports partial workspace-wide helper projection, so source and engine evidence must remain distinguished.

