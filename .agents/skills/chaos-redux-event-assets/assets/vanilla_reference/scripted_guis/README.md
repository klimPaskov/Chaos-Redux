# Vanilla scripted GUI reference set

This set provides reusable structural references for scripted GUI planning. Each category contains an exact 1920x1080 full render produced by the HOI4 MCP from the installed vanilla interface and scripted-GUI sources, plus a labeled contact sheet cropped only for easier review. The root [contact sheet](contact_sheet.png) compares all categories.

Use these references to study hierarchy, spacing, value grouping, attachment geometry, repeated rows, progress states, and information density before generating a new scripted-GUI reference with Sunburst. The generated reference establishes the intended composition; the vanilla source establishes what native HOI4 controls and asset families can implement. Do not copy a vanilla window wholesale or wire these review PNGs into the mod.

## Categories

| Category | Vanilla window | Installed sources | Reusable pattern |
| --- | --- | --- | --- |
| [Meters and pressure](meters_and_pressure/) | `sov_paranoia_system_ui_window` | `interface/sov_paranoia_system_scripted_gui.gui`; `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` | A prominent focal meter, attached value line, threshold colour, and compact pressure summary. |
| [Institutional boards](institutional_boards/) | `usa_congress_decision_ui_window` | `interface/usa_congress_scripted_gui.gui`; `common/scripted_guis/USA_congress_scripted_gui.txt` | Two institutional blocs, large numeric state, visual seat distribution, and strong left/right grouping. |
| [Faction relations](faction_relations/) | `bul_internal_factions_decision_ui_window` | `interface/bul_internal_factions_scripted_gui.gui`; `common/scripted_guis/BUL_internal_factions_scripted_gui.txt` | Repeated organization rows, role icons, aligned comparison columns, and quick scanning across groups. |
| [Regional investment](regional_investment/) | `raj_local_leaders_investments_decision_ui_window` | `interface/raj_local_leaders_investments_decision_ui.gui`; `common/scripted_guis/RAJ_local_leaders_investments_scripted_gui.txt` | Repeated project rows, category icons, aligned chance/investment values, and regional development choices. |
| [Campaign progress](campaign_progress/) | `sov_propaganda_campaigns_ui_window` | `interface/sov_propaganda_campaigns_scripted_gui.gui`; `common/scripted_guis/SOV_propaganda_campaigns_scripted_gui.txt` | Repeated illustrated campaign cards with one concise live duration beneath each card. |
| [Escalation status](escalation_status/) | `war_escalation_decision_ui_window` | `interface/war_escalation_scripted_gui.gui`; `common/scripted_guis/war_escalation_scripted_gui.txt` | A compact headline value and discrete escalation steps that remain readable at a glance. |

All installed source paths are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

## Render evidence

The six renders use MCP workspace `mod_chaos_redux_ea3b2d67c2c0`, state `normal`, resolution `1920x1080`, and UI scale `1`. Each saved PNG was reconstructed from bounded MCP resource reads and verified against the artifact SHA-256 in [REFERENCE_MANIFEST.md](../REFERENCE_MANIFEST.md).

The Soviet paranoia render reports the installed vanilla `GFX_SOV_paranoia_needle` sheet width as not divisible by its declared 21 frames. The United States Congress render reports the same installed-source diagnostic for `GFX_decision_category_usa_congress_house_ui`. These diagnostics belong to the inspected vanilla source and are recorded so future reviewers do not misattribute them to Chaos Redux. The other four renders returned no hard diagnostics.

## Use in the scripted GUI workflow

1. Choose one or more categories that match the mechanic's information shape.
2. Inspect the full PNG, its category contact sheet, and both installed source files.
3. Generate the proposed composition with Sunburst, using the selected categories as style and geometry references rather than edit targets.
4. Map generated decoration to runtime textures and every label, value, meter, list, button, hover, tooltip, and click region to native controls.
5. Inspect and render the implementation with the HOI4 MCP at matching states and resolutions, compare it with the generated reference, and fix every visible alignment, spacing, scaling, clipping, background, overlap, state, and hitbox defect.

The MCP full PNGs are reference evidence, while their contact sheets are review aids. Neither is a runtime asset.
