# Event003 Mandala Visual Reference and Native Mapping

The annotated reference is `reference_mandala_tabs_values_annotated.png`. It was created from the verified pre-change production render for `holy_realm_mandala_category_container`, TIB on 1 January 1936, at 1920x1080 and UI scale 1. Dashed cyan and amber boxes are review annotations for native button bounds, not runtime controls or asset art.

## Acceptance Basis

The parent authorized a bounded repair of Event003's existing Mandala decision-category panel and confirmed that Final Silence remains content inside the Doctrine and Warnings tabs. The parent accepted centering the tab rows and using an active-only `>` label for the selected native button. The parent also accepted the phase-specific value-count mapping of 3, 3, 3, 4, and 4 mechanic values for Refuge, Arhats, Diplomacy, Doctrine, and Warnings, respectively.

The parent authorized only presentation changes to the existing panel, its event-owned scripted-localisation selectors, and the corresponding Event003 English localisation keys. No separate Final Silence window is accepted or present in the inspected event-owned source.

The denominator display uses three parent-authorized UI-only variables sourced from the existing Bodhi, Dhyana, and teaching-success constants. The variables are assigned by the existing `holy_realm_ensure_buddhahood_counters` initialization effect and are read only by the Mandala display; they do not gate or change gameplay.

## Event Ownership and Entry Point

`common/scripted_guis/003_holy_realm_scripted_guis.txt` defines `holy_realm_mandala_category_scripted_gui` with `context_type = decision_category` and `window_name = "holy_realm_mandala_category_container"`. `common/decisions/categories/003_holy_realm_categories.txt` attaches that scripted GUI to the Event003-owned `holy_realm_mandala_category`, whose decisions are defined in `common/decisions/003_holy_realm_decisions.txt`.

`interface/chaosx_decisions.gui` defines the exact attached container and its five tab controls. The parent confirmed that the linked Event003 source contains no dedicated Final Silence Ledger window, so this work uses the existing Warnings and Doctrine tabs only.

## Reference Region Mapping

| Reference region | Native element and usable bounds | Content and interaction | Asset or state | Constraint and accepted adaptation |
| --- | --- | --- | --- | --- |
| Central Mandala | `holy_realm_mandala_core`, x=126, y=12, 218.4x218.4 rendered bounds in a 470x560 container | Shows the current Mandala state through the existing scripted-localisation `image` property | The element's base sprite now points to the existing static dormant sibling, while the unchanged dynamic property continues to select the active animated state | Preserve center alignment and `scale = 0.52`; keep the existing state getter and current asset identifiers |
| Primary value row | `holy_realm_mandala_values`, x=8, y=238, 454x26 | One primary value selected by the existing tab flags | TIB Refuge fixture selects only `holy_realm_mandala_tab_refuge` | Keep all dynamic values in native text and use an event-owned scripted-localisation selector |
| Supporting value row | `holy_realm_mandala_secondary`, x=8, y=266, 454x24 | Up to two supporting values selected by the existing tab flags | Same single-tab fixtures | Keep the existing line pitch and font family |
| Conditional risk row | `holy_realm_mandala_chaos`, x=8, y=292, 454x24 | Empty for Refuge, Arhats, and Diplomacy; Defilements for Doctrine; Chaos for Warnings | The two fourth values are independently gated by the accepted tab design | Use a dynamic scripted-localisation output; do not repeat metric values on other tabs |
| Stage and doctrine | `holy_realm_mandala_stage` at x=8, y=320, 218x24 and `holy_realm_mandala_doctrine` at x=242, y=320, 220x24 | Displays current route and doctrine status | Existing source helpers and localisation | Preserve current two-column alignment |
| First tab row | `holy_realm_panel_tab_refuge_button`, `holy_realm_panel_tab_arhats_button`, `holy_realm_panel_tab_diplomacy_button` | Real native buttons and existing click effects | Selected control receives `>` in its visible label; all other labels remain unchanged | Center the 123x36 control bounds at x=16, 173, and 330, y=356 |
| Second tab row | `holy_realm_panel_tab_doctrine_button`, `holy_realm_panel_tab_warnings_button` | Real native buttons and existing click effects | Selected control receives `>` in its visible label | Center the 123x36 control bounds at x=95 and 252, y=394 |
| Tab body | `holy_realm_panel_tab_content`, x=8, y=436, 454x110 | Current tab-specific explanation and choices | Existing `GetHolyRealmPanelTabContent` helper | Preserve its body text and the native wrapping region |

The five accepted value groups use only current Event003 variables. Refuge shows `spiritual_legitimacy`, `compassion_drift`, and `sangha_cohesion`. Arhats shows `spiritual_legitimacy`, `defilements`, and `sangha_cohesion`. Diplomacy shows `mandala_reach`, `spiritual_legitimacy`, and `sangha_cohesion`. Doctrine shows `bodhi_progress`, `dhyana_depth`, `teaching_successes`, and `defilements`. Warnings shows `final_silence_pressure`, `meditation_charge`, `defilements`, and `global.chaos_meter_value`.

The bounded search found no separate `refuge_legitimacy` or `arhat_influence` variable in the named Event003 sources. `sangha_cohesion` is initialized from `spiritual_legitimacy` by `holy_realm_ensure_buddhahood_counters` and is thereafter changed by Event003 decisions and effects.

## Engine Adaptations and Asset Ownership

The panel is a native attached decision-category container without a painted background in its current consumer. The composition keeps native text, buttons, the scripted state sprite, and the existing five-tab layout. The active-only `>` marker is ordinary button text so the selection remains live and clickable. The selected styling is an explicit text cue because the current native button sprite uses the same frame and shader for selected and normal tabs.

`interface/003_holy_realm.gfx` defines both `GFX_holy_realm_mandala_dormant` and `GFX_holy_realm_mandala_dormant_animated`. The static 420x420 DXT1 sprite is the fallback base, and the animated 420x420, 16-frame DDS remains the active scripted state. The selected animated source has no alpha channel; the parent owns frame replacement and alpha repair. The current GFX file SHA-256 is `DBA73B7BBFDECD3866756FC8320B51CB238CC163E88CEF667ED13B1033C5E8FD`.

The current `.gui` source hash is recorded beside `chaosx_decisions.gui.before`; the standalone Mandala container block is preserved as `gui_mandala_container.before.gui`. The baseline MCP full, cropped, annotated, source-map, click-region, hierarchy, layout, scenario, fidelity, and validation artifacts are preserved in this evidence folder with their SHA-256 values.
