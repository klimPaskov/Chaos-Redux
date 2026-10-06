# Holy Mandala Animation Review Index

Status: `parent_approved` on 2026-10-06. The approved preview package was promoted to the exact runtime DDS paths.

The 218px panel GIFs use the production MCP crop at 471x484 and replace only the old Mandala art rectangle with the sampled native background RGB `23, 32, 42` (`#17202A`). Each GIF contains 16 frames with alternating 120ms and 130ms durations, for an exact 2.000-second loop and average 8 fps. The per-state `contact_218_light_gray.png` grids expose any remaining color fringe against a light background.

| State | 218px production-panel loop | Native 420px frame contact | 4x frame contact | 218px light-gray alpha check |
| --- | --- | --- | --- | --- |
| dormant | `previews/holy_realm_mandala_dormant_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_dormant_contact_native.png` | `contact_sheets/holy_realm_mandala_dormant_contact_4x.png` | `contact_sheets/holy_realm_mandala_dormant_contact_218_light_gray.png` |
| teaching | `previews/holy_realm_mandala_teaching_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_teaching_contact_native.png` | `contact_sheets/holy_realm_mandala_teaching_contact_4x.png` | `contact_sheets/holy_realm_mandala_teaching_contact_218_light_gray.png` |
| meditation | `previews/holy_realm_mandala_meditation_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_meditation_contact_native.png` | `contact_sheets/holy_realm_mandala_meditation_contact_4x.png` | `contact_sheets/holy_realm_mandala_meditation_contact_218_light_gray.png` |
| awakened | `previews/holy_realm_mandala_awakened_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_awakened_contact_native.png` | `contact_sheets/holy_realm_mandala_awakened_contact_4x.png` | `contact_sheets/holy_realm_mandala_awakened_contact_218_light_gray.png` |
| wrathful | `previews/holy_realm_mandala_wrathful_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_wrathful_contact_native.png` | `contact_sheets/holy_realm_mandala_wrathful_contact_4x.png` | `contact_sheets/holy_realm_mandala_wrathful_contact_218_light_gray.png` |
| final_silence | `previews/holy_realm_mandala_final_silence_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_final_silence_contact_native.png` | `contact_sheets/holy_realm_mandala_final_silence_contact_4x.png` | `contact_sheets/holy_realm_mandala_final_silence_contact_218_light_gray.png` |
| empty | `previews/holy_realm_mandala_empty_preview_218_panel.gif` | `contact_sheets/holy_realm_mandala_empty_contact_native.png` | `contact_sheets/holy_realm_mandala_empty_contact_4x.png` | `contact_sheets/holy_realm_mandala_empty_contact_218_light_gray.png` |

The shared consumer crop is `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/gui_render_before_refuge_19360101_cropped.png`. Its icon position is `(126,12)` and displayed size is 218x218 at UI scale 1.0. Its blank margin samples are exactly `#17202A`.

The per-frame source crops, processed PNGs, static fallback previews, horizontal sheet PNGs, candidate atlases, prompts, trial composites, and metadata are stored beside this index. Candidate DDS outputs and runtime copies are byte-identical; `notes/runtime_promotion_report.json` records their package digest and hashes.
