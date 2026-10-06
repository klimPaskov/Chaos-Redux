# Event003 Mandala GUI Release Repair

Disposition: the authorized Mandala presentation changes are implemented, but visual acceptance is blocked. The exact post-change MCP render call timed out after 600 seconds without returning artifacts, and the parent-owned animated-frame and alpha replacement candidate is awaiting parent review and promotion.

## Ownership and Authorization

The owned surface is the existing `holy_realm_mandala_category_container` in `interface/chaosx_decisions.gui`. `common/scripted_guis/003_holy_realm_scripted_guis.txt` binds it through `holy_realm_mandala_category_scripted_gui` with `context_type = decision_category`; `common/decisions/categories/003_holy_realm_categories.txt` attaches that scripted GUI to Event003's `holy_realm_mandala_category`. The parent confirmed that there is no distinct Final Silence GUI window and directed this work to keep its content inside the existing Doctrine and Warnings tabs.

The parent accepted centered tab rows, a visible active-only `>` label, the phase-specific 3/3/3/4/4 value mapping, three UI-only denominator variables assigned from existing tuning constants, and the static dormant sprite as the base sprite while the current animated state getter remains active. The parent separately owns the real frame-by-frame animation and alpha repair.

## Changed Files

- `interface/chaosx_decisions.gui`: changed only the `holy_realm_mandala_category_container` block. The base sprite now names `GFX_holy_realm_mandala_dormant`; the unchanged scripted-GUI property still selects the animated state. The first tab row is at x=16/173/330 and the second row is centered at x=95/252. The three value text boxes call the accepted phase selectors, and five native button labels call flag-aware selected-label selectors. Existing controls, effects, tooltips, click targets, and tab count remain intact.
- `common/scripted_localisation/003_holy_realm_scripted_localisation.txt`: added primary, supporting, and conditional risk-row selectors plus five selected-label selectors. The Warnings risk row displays Chaos only when the existing `holy_realm_chaos_above_final_gate` trigger passes; this trigger checks `global.chaos_meter_value > constant:holy_realm_chaos.final_silence_gate`.
- `common/scripted_effects/003_holy_realm_effects.txt`: added three UI-only assignments inside `holy_realm_ensure_buddhahood_counters`: `holy_realm_ui_bodhi_max`, `holy_realm_ui_dhyana_max`, and `holy_realm_ui_teaching_successes_required`, each sourced from its corresponding `constant:holy_realm_buddhahood.*` value. No new mechanic gate reads them.
- `localisation/english/003_the_holy_realm_l_english.yml`: rewired the three existing value-line keys and added phase-specific row strings plus active-tab label strings. The original UTF-8 BOM is retained.
- `docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/reference_acceptance.md`: records the accepted reference mapping and current denominator authorization.

Before and after full-source snapshots, standalone GUI-block snapshots, an isolated unified patch (`gui_release_20261005_evidence/gui_release_source.diff`), and MCP artifacts are under `docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/`. The interface before/after full-file hashes are `620D8D7D94E14D0E44208D3E342EEAE5A5892D6BDC6763079DBBBA6FA232BD31` and `92C3C5855C0C8F8ABAEA31C81557F6A81F57F6C6440F4AC5329B1B97A538D828`. The exact container-block hashes are `D1FFD811047C7DD68D41D7CA595F568EC8EE6512BB02F129595072887FF7D560` and `E89E794DE43039D40D7C2DA63713602DA08BC2E0F69F2576DDDD05754AD82289`; a byte comparison confirmed that all bytes outside the owned block were unchanged at the time of the edit.

The effects-file hashes are `EC66BD83349BCE11B3DEA1DFD4C15008777A6BFBDB228C4DB08CDFD9C73CD710` before and `A4DAA20949944E69709F9046BABAD052B64203BF73FDCBC427E38C9D04D07CA4` after. The original effect-file body was verified byte-for-byte around the narrow insertion. The scripted-localisation file's original snapshot hash is `D144A965516024DBA9A627596CEEC66DBECBDF399D9942A0EC83396CC48C9BDB`; its current after snapshot hash is `E9FFFD502704E6E682A4C94ABB1E1E1044A01238AEAE9E607D74E66490DA91F5`. The localization hashes are `AE570FF0CC5FF26669B66C320899F1B45E2F5858929D4BD8DB8DF37B29C45D80` before and `489196E1308D01942D020FB5D48F698857576077C3867CDC1B1283736FAC7C70` after.

## Accepted Value Groups and Layout Budgets

| Tab | Primary row | Supporting row | Conditional third row | Total values shown |
| --- | --- | --- | --- | ---: |
| Refuge | Spiritual Legitimacy | Compassion Drift; Sangha Cohesion | blank | 3 |
| Arhats | Spiritual Legitimacy | Defilements; Sangha Cohesion | blank | 3 |
| Diplomacy | Mandala Reach | Spiritual Legitimacy; Sangha Cohesion | blank | 3 |
| Doctrine | Bodhi Progress / sourced maximum | Dhyana Depth / sourced maximum; Teaching Successes / sourced requirement | Defilements | 4 |
| Warnings | Final Silence Pressure | Meditation Charge; Defilements | Global Chaos, only above the existing final-silence gate | 3 or 4 |

These rows use only variables already present in Event003. The source search found no Event003 `refuge_legitimacy` or `arhat_influence` variables, so neither is invented. Bodhi, Dhyana, and teaching maxima are not duplicated as source literals in player-facing localization. No new gameplay action or cost appears in this container. Its five native controls remain navigation buttons, and every existing tooltip and click effect is preserved.

The selected cue uses native button text: `> Refuge`, `> Arhats`, `> Diplomacy`, `> Doctrine`, or `> Alert`. Other labels remain their current text. It avoids a global selected state and uses each existing mutually exclusive tab flag. Baseline source inspection found no persistent selected-frame distinction in `GFX_button_123x34`; native frame and shader values were identical on the selected and normal tabs.

The existing tab body continues to give a brief consequence or response for the current phase. The five button tooltips remain attached to their native controls. Costs, requirements, scripted outcomes, AI weights, cleanup, and route design were not changed.

The intended after-state matrix is one explicitly selected tab per fixture, with the four siblings normal; no scenario sets every button selected. The only supported resolution passed to the GUI MCP route was 1920x1080 at UI scale 1. The post-change render request exercised only the initial Refuge fixture and returned no artifact, so none of these after states are visually accepted yet.

| Fixture | Source-backed state | Expected value-row count | After-render status |
| --- | --- | ---: | --- |
| `evt003_tib_refuge_initial` | TIB, 1936.1.1; `holy_realm_active`, Refuge tab flag; spiritual legitimacy 55, Mandala Reach 35, doctrine rigidity 10, meditation charge 20, Defilements 45, Sangha 55, global Chaos 0 | 3 | Attempted; MCP render timed out after 600s |
| `evt003_tib_arhats_initial` | Same initial country fixture with only the Arhats tab flag and Arhats button selected | 3 | Not rendered |
| `evt003_tib_diplomacy_initial` | Same initial country fixture with only the Diplomacy tab flag and Diplomacy button selected | 3 | Not rendered |
| `evt003_tib_bodhisattva_doctrine` | Later-state preview derived from the existing Bodhisattva stage and teaching-success flow; only the Doctrine tab selected; explicit preview assumptions must be recorded with its values | 4 | Not rendered |
| `evt003_tib_warnings_quiet` | Warnings tab selected, `final_silence_pressure = 0`, `global.chaos_meter_value = 0`, no final-warning flag | 3 | Not rendered |
| `evt003_tib_warnings_terminal_pressure` | Warnings tab selected, `holy_realm_final_warning_sent`, `final_silence_pressure > 59`, `global.chaos_meter_value > constant:holy_realm_chaos.final_silence_gate` | 4 | Not rendered |

## Reference, Sources, and Asset Mapping

The intended correction reference is `gui_release_20261005_evidence/reference_mandala_tabs_values_annotated.png`, created from the verified pre-change production render before source edits. Dashed outlines mark native button bounds; the image does not flatten text, buttons, or the Mandala into runtime artwork. `reference_acceptance.md` maps the reference regions to the bounded native controls and preserves the 470x560 container hierarchy.

The exact production crop used as the asset-edge reference is `gui_release_20261005_evidence/gui_render_before_refuge_19360101_cropped.png`, 471x484 pixels from a 1920x1080 render at UI scale 1 with no post-crop resize or color transform. Its clear margin samples RGB (23, 32, 42), `#17202A`. This crop and color sample were sent to `/root/mandala_real_frames` for alpha-edge review.

`interface/003_holy_realm.gfx` defines the static dormant sprite and the dormant animated sibling. The static 420x420 DDS has SHA-256 `B637D9C4730A072F1338F216C828688417F1997E5851072880763A4184382EB0`; the current 420x420 animated DDS has SHA-256 `D19FED1D8B3128DBA6D3C08AA03FCE6D040A6F9FCF6ED98E166935E7F08B8A99`. The GUI base now links the static fallback consumer-side, while the unchanged `GetHolyRealmMandalaSprite` scripted property continues to select the active animation. The frame worker supplied a seven-state candidate package at `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/preview_index.md`, digest `F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56`, with per-file DDS hashes in `notes/dds_roundtrip_report.json`. The worker states these candidates await parent review and have not been promoted to runtime paths, so they are not yet render inputs. The parent owns animation-frame production, real-frame validation, alpha review, and promotion.

Vanilla precedents inspected: installed `interface/sov_paranoia_system_scripted_gui.gui` and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` for category-attached native GUI composition, and `interface/countrydecisionview.gui` around lines 114-120 for native checkbox state. Installed GUI documentation `_documentation.md` was read at lines 1-146, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`. Offline wiki sections read: Scripted GUI Effects lines 179-193 and Template lines 549-628, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`; Interface `buttonType` lines 227-256, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.

## MCP Evidence and Validation

Pre-change `hoi4.gui_inspect` resolved the exact panel with workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `evt003_tib_refuge_initial`, source revision `b22c8078a1013ed6f2cdb2be898f9e7e866b10b62f9fd73ac9e81d35a051672c`, and full artifact SHA-256 `22705232c90a39d39985a20621fc3cc7c599ec4692d6bef7c30b4b286ee5745e`. Its URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22705232c90a39d39985a20621fc3cc7c599ec4692d6bef7c30b4b286ee5745e/91132a0a56df3f23cd86b0ce133bcdd36c9e69e3dba4c1fecf69df2326a8409a/gui-inspect.b22c8078a1013ed6.json`. The artifact was recovered in 32766-byte chunks, byte-count and SHA verified, and retained locally as `gui_inspect_before_refuge_19360101.json`.

The pre-change render used TIB, 1936.1.1, Refuge selected, 1920x1080, UI scale 1, and `generatedScenarios.enabled = false`. Its source revision was `2ec2fb605ed8294e2b1e8da881db1f90e5891f341d91d9222a0027f23afba20b`; its validation JSON SHA-256 is `2b927256c7b7613a0196c739506753f9cfbeb361d3fa5a43ded95e4fbac8a595`. Full, cropped, annotated, click-region, source-map, hierarchy, layout, scenario, fidelity, and validation artifacts are saved beside the reference. The baseline showed the first tab row slightly left of panel center and the lower pair left-clustered. The selected native tab had no persistent frame cue. Visible text remained inside its boxes.

The first post-source `hoi4.gui_inspect` attempt for the exact panel timed out after 600 seconds. It started after the layout, metric selectors, selected cues, static base sprite, and denominator assignments had been applied, but before the final source-backed Warnings risk-row gate condition was added. A second inspect was attempted against the final source and explicit Refuge fixture; it returned `isError = true` without structured diagnostics, artifacts, or a source revision. The subsequent `hoi4.gui_render` attempt was made after that gate condition, against `evt003_tib_refuge_initial`, TIB on 1936.1.1, 1920x1080, UI scale 1, `generatedScenarios.enabled = false`, and with the saved prior `.gui` source supplied as `sourceBaseline`. It failed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render; timed out awaiting tools/call after 600s`. No after-render artifact or source revision was returned, so no post-change image, click-region, layout, hierarchy, or comparison review can be claimed. These are MCP route blockers, not clean validation results. A final inspect/render must be run on the integrated source after the parent-owned animation and alpha replacement is installed.

`hoi4.script_validate` was run on the three UI-only `set_variable` assignments against installed effect documentation. It returned `SCRIPT_CHECK_PARTIAL`, found the `set_variable` commands supported in country scope, and left the native argument blocks unchecked (`valid = null`). The installed effect documentation's `set_variable` section at lines 7888-7895 was read separately. This validator result does not certify the constant parameters.

A focused source wiring check confirmed that all eight display and selected-label getters referenced by the panel are defined, their Event003 Mandala/tab localisation targets exist, and each UI-only denominator is assigned exactly once in the initialization effect. The Warnings fourth-row selector references the existing final-gate scripted trigger.

## Remaining Work and Limits

Post-change visual acceptance remains blocked until the MCP inspect/render route returns matched artifacts and the Mandala is rerendered against the parent-promoted replacement sheets and alpha package. The after-render must cover supported explicit tab selections without setting every tab selected, at 1920x1080 and UI scale 1; verify button label centering, click regions, value-row overflow, image edges, and the conditional Warnings row. The exact MCP artifact cache route described by the parent must be used if resource reads are closed; verify returned sizes, SHA values, provenance, and PNG/JSON signatures before review.

No separate Final Silence window was created. Parent/event003 integration retains terminal-ending and super-event wiring. No shared Event Log, event-details, settings, or super-event framework GUI was modified. No costs, requirements, effects, AI weights, balance targets, or gameplay outcomes changed beyond the three explicitly authorized display variables. No game launch or live campaign validation was performed; the user owns that evidence. No files were staged or committed.
