# Vanilla scripted GUI reference set

The accepted native-size game captures and current source-backed renderer views live under [`scripted_guis/`](../scripted_guis/), with source revisions, scenarios, crop bounds, and contact sheets in its manifest. Images elsewhere in this `interface/` tree are exploratory captures and are not evidence of current in-game visual parity. Each source precedent below remains useful for studying native GUI structure, but a new reference must pass the shelf's visual review before agents use it as an example.

Use these references to study hierarchy, spacing, value grouping, attachment geometry, repeated rows, progress states, and information density before generating a new scripted-GUI reference with Sunburst. The generated reference establishes the intended composition; the vanilla source establishes what native HOI4 controls and asset families can implement. Do not copy a vanilla window wholesale or wire these review PNGs into the mod.

## Categories

| Category | Vanilla window | Installed sources | Reusable pattern |
| --- | --- | --- | --- |
| Meters and pressure | `sov_paranoia_system_ui_window` | `interface/sov_paranoia_system_scripted_gui.gui`; `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` | A prominent focal meter, attached value line, threshold colour, and compact pressure summary. |
| Institutional boards | `usa_congress_decision_ui_window` | `interface/usa_congress_scripted_gui.gui`; `common/scripted_guis/USA_congress_scripted_gui.txt` | Two institutional blocs, large numeric state, visual seat distribution, and strong left/right grouping. |
| Faction relations | `bul_internal_factions_decision_ui_window` | `interface/bul_internal_factions_scripted_gui.gui`; `common/scripted_guis/BUL_internal_factions_scripted_gui.txt` | Repeated organization rows, role icons, aligned comparison columns, and quick scanning across groups. |
| Regional investment | `raj_local_leaders_investments_decision_ui_window` | `interface/raj_local_leaders_investments_decision_ui.gui`; `common/scripted_guis/RAJ_local_leaders_investments_scripted_gui.txt` | Repeated project rows, category icons, aligned chance/investment values, and regional development choices. |
| Campaign progress | `sov_propaganda_campaigns_ui_window` | `interface/sov_propaganda_campaigns_scripted_gui.gui`; `common/scripted_guis/SOV_propaganda_campaigns_scripted_gui.txt` | Repeated illustrated campaign cards with one concise live duration beneath each card. |
| Escalation status | `war_escalation_decision_ui_window` | `interface/war_escalation_scripted_gui.gui`; `common/scripted_guis/war_escalation_scripted_gui.txt` | A compact headline value and discrete escalation steps that remain readable at a glance. |

All installed source paths are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

## Capture recipe

A category render uses an explicit scenario, resolution, UI scale, and source revision. The current accepted crop and full-render hashes are in [REFERENCE_MANIFEST.md](../REFERENCE_MANIFEST.md). A source-only window that omits its parent panel is a component example, not a full-window example.

## Use in the scripted GUI workflow

1. Choose one or more categories that match the mechanic's information shape.
2. Capture or inspect the category's full render and contact sheet with the recipe above, then inspect both installed source files.
3. Generate the proposed composition with Sunburst, using the selected categories as style and geometry references rather than edit targets.
4. Map generated decoration to runtime textures and every label, value, meter, list, button, hover, tooltip, and click region to native controls.
5. Inspect and render the implementation with the HOI4 MCP at matching states and resolutions, compare it with the generated reference, and fix every visible alignment, spacing, scaling, clipping, background, overlap, state, and hitbox defect.

The reviewed PNGs under `scripted_guis/` are reference evidence, while contact sheets are review aids. Neither is a runtime asset.
