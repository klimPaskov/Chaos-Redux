# Repression Ledger UI Asset Manifest

## Status and source mode

The 24 static Repression Ledger assets are complete and live. The visual package is built from two frozen ImageGen sources: a full archival-ledger surface and a sixteen-cell period dossier emblem atlas. The processing pass preserves the `900x560` GUI contract, extracts the emblem family, derives textured panels and three-state buttons, and exports the accepted static warning layers. No historical photograph, leader likeness, flag, third-party image, readable generated text, or protected-class symbol is used in the final sprites.

- Build source: `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py`
- Frozen ImageGen sources: `docs/assets/system_camp_repression_rework/source/ui_imagegen/repression_ledger_window_imagegen_source.png` and `repression_ledger_icon_atlas_imagegen_source.png`
- Source PNGs: `docs/assets/system_camp_repression_rework/source/ui/`
- Processed PNGs: `docs/assets/system_camp_repression_rework/processed/ui/`
- Package DDS copies: `docs/assets/system_camp_repression_rework/dds/ui/`
- Live DDS files: `gfx/interface/camp_repression/`
- Contact sheet: `docs/assets/system_camp_repression_rework/contact_sheets/repression_ledger_ui_contact_sheet.jpg`
- DDS conversion: repository `.tools/convert_to_dds.py`, one mip, 32-bit BGRA/B8G8R8A8-style output.

Every row has a same-name `_source.png`, processed `.png`, package `.dds`, and live `.dds`.

## Registered assets

| Sprite id | Dimensions | Role |
| --- | ---: | --- |
| `GFX_decision_category_repression_ledger` | 53x53 | Decision-category ledger icon |
| `GFX_decision_open_repression_ledger` | 32x32 | Open/close ledger decision icon |
| `GFX_repression_ledger_window_bg` | 900x560 | Main ledger background |
| `GFX_repression_ledger_summary_strip` | 864x52 | National summary strip |
| `GFX_repression_ledger_card_bg` | 344x90 | Overview card background |
| `GFX_repression_ledger_country_card_bg` | 710x304 | Country/discovery panel background |
| `GFX_repression_ledger_tab_button` | 420x42 | Three-state 140x42 tab-button sheet |
| `GFX_repression_ledger_action_button` | 408x38 | Three-state 136x38 action-button sheet |
| `GFX_repression_ledger_tab_overview` | 32x32 | Overview tab mark |
| `GFX_repression_ledger_tab_state_pools` | 32x32 | State-pool tab mark |
| `GFX_repression_ledger_tab_sites` | 32x32 | Active-site tab mark |
| `GFX_repression_ledger_tab_country` | 32x32 | Country-system tab mark |
| `GFX_repression_ledger_tab_discovery` | 32x32 | Discovery/reform tab mark |
| `GFX_repression_ledger_population_pressure` | 24x24 | Population-loss consequence mark |
| `GFX_repression_ledger_labor_output` | 24x24 | Labor-output mark |
| `GFX_repression_ledger_evidence_risk` | 24x24 | Evidence-risk mark |
| `GFX_repression_ledger_reform_pressure` | 24x24 | Reform-pressure mark |
| `GFX_repression_ledger_guard_burden` | 24x24 | Guard-burden mark |
| `GFX_repression_ledger_rail_burden` | 24x24 | Rail-burden mark |
| `GFX_repression_ledger_warning_frame_static` | 710x48 | High-overstretch static warning |
| `GFX_repression_ledger_evidence_seal_static` | 112x112 | Discovered-evidence seal |
| `GFX_repression_ledger_reform_seal_static` | 112x112 | Reform-route seal |
| `GFX_repression_ledger_selected_state_frame_static` | 710x38 | Selected-state frame |
| `GFX_repression_ledger_critical_frame_static` | 710x48 | Critical breakdown static warning |

## Validation

- The two frozen ImageGen sources exist and feed all 24 derived source/processed/package/live chains.
- 24 processed PNGs and 24 live DDS files exist.
- Pillow decodes every DDS as RGBA; registered dimensions match the frozen GUI.
- Button sheets are exactly three horizontal frames.
- The icons and seals retain transparent pixels; panels preserve the generated leather, paper, brass, ink, wax, rail-map, and filing textures.
- The maintained ImageGen-derived sprites provide the static presentation. Part 6 accepts static presentation, so optional authored animation is not a missing runtime dependency.
- `interface/camp_repression_rework.gfx` points directly to every live DDS path.
