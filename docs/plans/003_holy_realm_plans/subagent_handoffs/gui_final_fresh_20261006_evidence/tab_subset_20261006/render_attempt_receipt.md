# Event003 Four-Tab Render Attempt Receipt — 2026-10-06

Disposition: unresolved; the one authorized narrow production render returned `Transport closed` before structured content or artifacts, and was not retried.

## Request and source identity

Route: `hoi4.gui_render` for workspace `mod_chaos_redux_ea3b2d67c2c0`, exact window `holy_realm_mandala_category_container`.

The request contained exactly four source-backed TIB scenarios dated 1936.1.1 in `l_english`, with `values.is_ai = false`, `generatedScenarios = { enabled = false }`, `states = ["normal"]`, and a single 1920×1080/UI1 resolution.

No `sourceBaseline`, `comparisonScenario`, or `refresh` field was sent.

The primary scenario was `evt003_tib_arhats_selected_20261006_narrow`; the three related scenarios were `evt003_tib_diplomacy_selected_20261006_narrow`, `evt003_tib_doctrine_selected_four_metrics_20261006_narrow`, and `evt003_tib_warnings_selected_chaos_1001_20261006_narrow`.

Each fixture set `holy_realm_active` plus only its selected tab flag, supplied all five explicit per-control button states, and left the Mandala sprite getter on its natural dormant result using the exact initial TIB variables and no progression flags.

The Arhats fixture also set its unselected Refuge button to `hover` while keeping Arhats selected; this was part of the same scenario and added no fifth fixture.

The Doctrine fixture showed all four accepted values at source starting values: Bodhi `0/108`, Dhyana `0/4`, teaching successes `0/12`, and Defilements `45`; with no teaching, concentration, awakening, wrathful, or final-route facts set, the source sprite getter still resolved to Dormant.

The Warnings fixture used `global.chaos_meter_value = 1001`; the strict final-gate getter consequently returned the nonempty localized line `Chaos: §R1001§!` while the warning-body getter remained the source's calm line because no warning-stage flags were present.

## Budget preflight and tool result

The conservative estimate was four viewport planes `4 × 1920 × 1080 = 8,294,400` pixels plus one dormant animation sheet plane `6720 × 420 = 2,822,400`, for `11,116,800` pixels against the fixed `67,108,864` limit.

This estimate is only a preflight; the tool returned `isError = true` and the exact text `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render; Caused by: Transport closed` before returning `structuredContent`, an artifact list, diagnostics, or validation.

No artifact URI or SHA-256 exists for this request; there are no render images to review or copy from the cache.

No retry, split request, refresh, alternate route, or source edit was made after the failure.

## Coverage consequence

Arhats, Diplomacy, Doctrine, and Warnings selected layouts, the same-scenario Refuge hover, the Warnings 1001 risk line, and the click-region alignment for those selected tabs remain visually unresolved by this request.

The previously accepted Refuge default production render at 1920×1080/UI1 remains the only successful current-source panel image in this audit.
