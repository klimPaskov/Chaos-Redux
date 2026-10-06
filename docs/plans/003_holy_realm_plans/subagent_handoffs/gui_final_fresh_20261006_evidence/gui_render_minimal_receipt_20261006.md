# Event003 Mandala Minimal Production Render Receipt

Disposition: partial visual review completed; the full state and tab matrix remains unresolved.

## Source and fixture identity

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Window: `holy_realm_mandala_category_container`, owned by Event003 through `holy_realm_mandala_category_scripted_gui` and `holy_realm_mandala_category`.

The immediately preceding exact-window inspect returned shared revision `09fd358650db3dd6b8ed913664d93d8a1299fd1bb0915abbcef64adc8cbaf0f1`. The current whole shared file SHA-256 is `4A87919352BE1A3748551085A34749B6BDC5F4C849A839846CEF97D1A0C564AD`. The normalized, line-ending-independent Mandala block snapshot at `gui_mandala_container_current.gui` has SHA-256 `E89E794DE43039D40D7C2DA63713602DA08BC2E0F69F2576DDDD05754AD82289` and compares line-for-line with the previously accepted block (`diffCount = 0`). The whole-file hash includes the parent's separate Event002 repair.

The only production scenario rendered was `evt003_tib_refuge_default_no_other_tabs_minimal_20261006`: TIB, 1936.1.1, `l_english`, 1920x1080 at UI scale 1, normal state, `generatedScenarios = { enabled = false }`, `values.is_ai = false`, and only `holy_realm_active = yes` in `flags`. No Mandala tab flags were set. Only the Refuge tab control was selected; its four siblings were normal. Getter overrides used their bare scripted-localisation names in `scenario.values`.

The request omitted `refresh`, `relatedScenarios`, `sourceBaseline`, and `comparisonScenario`. It returned `GUI_RENDERED` with status `ok`.

## Reviewed production images

The full view, crop, annotated view, click-region view, and source-map view were retrieved as bounded artifact byte ranges and SHA-256 checked against their content-addressed URIs. The full and crop views were reviewed directly. The annotated, click-region, and source-map PNGs are also copied into this evidence folder.

| View | Size | SHA-256 | Content-addressed artifact |
| --- | ---: | --- | --- |
| Full window PNG | 116,222 bytes | `4bc1f13b3590260f91a127e5aa12e60bb2a44b3f345ed850d92a1c457411a678` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4bc1f13b3590260f91a127e5aa12e60bb2a44b3f345ed850d92a1c457411a678/0a772c302b897fb4d44a6fa9d4f65c34b84b3128e4b6fc213de250a0c434c56c/holy_realm_mandala_category_container-full.png` |
| Cropped panel PNG | 99,963 bytes | `092dbdb8f6dee606029f93711c7b33046db87619777ddb2aa4a6faa1e9bf28cc` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/092dbdb8f6dee606029f93711c7b33046db87619777ddb2aa4a6faa1e9bf28cc/32dfe042932794167d987108b43750ef9383786e3d1cc3a383d888852abde6b8/holy_realm_mandala_category_container-cropped.png` |
| Annotated PNG | 140,236 bytes | `94be39328bffd823ace0158c5a9d167c2ca118915b1ca65185a8df98aa77fd14` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94be39328bffd823ace0158c5a9d167c2ca118915b1ca65185a8df98aa77fd14/ff22d2f0ef9e8c3e07e650d34a3988b5c7f256c458da4dd05935a325adb61dfb/holy_realm_mandala_category_container-annotated.png` |
| Click-region PNG | 123,597 bytes | `c71c42e2dff62f9cbfa571594e5f0f1c2dc2fafef83357ec1c0e01f6b9dceed9` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c71c42e2dff62f9cbfa571594e5f0f1c2dc2fafef83357ec1c0e01f6b9dceed9/aaf8148dff1fb3fab96a4d377e923d856830f86d1bdc7604a999ce3e8e88e6d0/holy_realm_mandala_category_container-click-regions.png` |
| Source-map PNG | 108,365 bytes | `6c493c5c1bed9d9390b200862bf4a1e73beb98b0d1c12f85dea492dd347b107e` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c493c5c1bed9d9390b200862bf4a1e73beb98b0d1c12f85dea492dd347b107e/b4c5b08a9b2d126d4392e8a99158d00cb5b346f8909e10fb365e533baa4c8427/holy_realm_mandala_category_container-source-map.png` |
| Scenario JSON | 2,005 bytes | `2e8b729e116ca3a2a6b7de2e90f0579de8829d5bba5152afe5b5d25f42d81c38` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e8b729e116ca3a2a6b7de2e90f0579de8829d5bba5152afe5b5d25f42d81c38/b964b1860c66f28be7aafcdbc8afce7bc2af008c7c500ad02c032b994d534a73/holy_realm_mandala_category_container-scenario.json` |
| Fidelity JSON | 31,032 bytes | `8352f13d310929b229a8d119a85c6fafd848e887165bc41166950d38ce0baaaa` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8352f13d310929b229a8d119a85c6fafd848e887165bc41166950d38ce0baaaa/15da37acca4f3fc2d4996672a5df8945d4dc2779c1ea3ff7898ad28d68b6e66b/holy_realm_mandala_category_container-fidelity.json` |
| Validation JSON | 8,017 bytes | `1ab1be56f01ababe9f509413e30b522acfa3740cf21dce0538651c1761715184` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ab1be56f01ababe9f509413e30b522acfa3740cf21dce0538651c1761715184/5e771dabd853826d1bcc43a0f56e3aca816ad76d7e65feba23e6f6428b1cfd6d/holy_realm_mandala_category_container-validation.json` |

The renderer also returned hierarchy, layout, source-graph, scenario-matrix, state-matrix, resolution-scale, and comparison artifacts. Its comparison JSON reports zero changed pixels because this minimal request did not supply a before source or `comparisonScenario`; it is not a pre/post source comparison. The first comparison render that did include the archived `sourceBaseline` timed out after 600 seconds and returned no artifacts.

## Visual findings from the rendered Refuge state

The Mandala has clean transparent edges against the dark native interface field and stays within its usable 470x560 container. The primary and supporting rows fit without clipping. The risk row is blank as the Refuge selector specifies. Stage and doctrine labels remain separated into two columns. All five native buttons remain visually distinct, the Refuge cue reads `> Refuge`, the tab rows are centered as accepted, and the explanatory body wraps to two lines inside its 454x110 text box.

The click-region image shows five separate 123x34 regions aligned with the painted button faces. The source map shows the 218.4x218.4 Mandala element, the value rows, both status columns, both tab rows, and the body contained inside the root container. The visually reviewed Refuge view shows no visible clipping or overflow.

## Diagnostics and limits

The validation artifact reports no visible overlap, text overflow, inconsistent alignment, off-center button label, click-bounds mismatch, conflicting click regions, missing sprite/texture/localisation, z-order risk, parent-window error, tab-state conflict, or resolution drift. It does report `GUI_ACCIDENTAL_CLIPPING` for a floating-point extent of 218.4 versus 218.39999999999998 pixels, `GUI_MISSING_FONT` for the blank `holy_realm_mandala_chaos` row using `hoi_16mbs`, and informational `GUI_INCONSISTENT_SPACING` where vertical gaps range from 2 to 12 pixels. These findings remain recorded; the current image proves only that the default Refuge view has no visible edge cut or spacing defect.

The validation matrix lists 13 unrendered states: hover, global selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation. The Refuge button itself is explicitly selected in this scenario, but the selected-tab matrix is otherwise untested. Tooltip strings are localized in source, while this render lists `pdx_tooltip` as fidelity-ignored and no tooltip view was requested.

The render source is bound to the immediately preceding current-source inspect revision `09fd358650db3dd6b8ed913664d93d8a1299fd1bb0915abbcef64adc8cbaf0f1`; the local whole-file SHA-256 and accepted Mandala block hash above remained unchanged throughout this minimal render. This is an offline production render, not live-game evidence.
