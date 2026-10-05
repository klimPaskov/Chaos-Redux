# Event 018 selected-field panel reference

This is the scoped reference for the accepted three-core-plus-one-contextual-value correction to Event 018's existing player-only decision-category panel.

## Acceptance and source basis

The parent explicitly accepted the three-plus-one value hierarchy and priority order under the user's release-quality G4/G5/G6 authorization on 2026-10-05, and authorized the narrow reference and the three source files listed here.

The accepted Event 018 spec describes a compact attached field header with the selected state, resource composition, four baseline values, one status image, and field navigation in [018_resources_found_spec_part_2_resource_field_mechanic.md](../../../specs/018_resources_found_specs/specs/018_resources_found_spec_part_2_resource_field_mechanic.md:7). The acceptance matrix records the selected-state header and multi-field cycling requirements in [acceptance_criteria.md](../../../specs/018_resources_found_specs/matrices/acceptance_criteria.md:65). The parent acceptance authorizes replacing the four baseline rows plus independently revealed pressure rows with three persistent core values and one exclusive contextual fourth value.

The prior UI handoff names an accepted cropped PNG at `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/f6/f69f5dce32ff81683ebaa1ff8cb3b06ebaf39fa1137c6c4b0018fa021a5ae9d4/resources_found_field_window-cropped.png`. That file is absent. The old Event 018 asset workspace currently contains only `models_3d`, and the `hoi4_agent_tools` MCP resource list is empty, so the historical image could not be recovered.

## Reference files

The ImageGen reference is [resources_found_field_3plus1_breach_reference.png](resources_found_field_3plus1_breach_reference.png), 1559×1009, SHA-256 `1B55609B51C7B32685E63AB491AF2120F87D781AF1BDD4EC194A069C5608E4D9`. It keeps the source panel's landscape ratio, but the generator did not return the requested 470×304 pixel dimensions; the panel and sprite consumer dimensions remain those verified from the source assets.

The source panel was decoded without alteration from `gfx/interface/018_resources_found/resource_field_panel.dds` to [resource_field_panel_reference.png](resource_field_panel_reference.png). The existing static Breach sprite was decoded without alteration from `gfx/interface/animated/018_resources_found/resource_field_breach_static.dds` to [resource_field_breach_static_reference.png](resource_field_breach_static_reference.png). The reference output uses those two inputs and is review material only; it is not runtime art.

## Native mapping and usable bounds

| Reference or background region | Native GUI IDs and bounds | Content and interaction | Assets and states | Constraint or adaptation |
| --- | --- | --- | --- | --- |
| Full panel | `resources_found_gui_panel`, root 470×304 at x=0,y=0 | Painted background only | `GFX_018_resource_field_panel` | Keep the exact installed panel DDS. The ImageGen mockup redraws some interior texture and is not a request to replace the source art. |
| Top rail title | `resources_found_gui_title`, x=24..272, y=7..27 | Localized title | `hoi_18mbs` | Preserve the existing title placement. |
| State header | `resources_found_gui_state` or `resources_found_gui_closed_state`, x=24..272, y=28..66 | Active selected field and position/count, or sealed history identity | Existing active/closed localization | The mockup's Arizona name and 1/2 count are sample assumptions, not campaign evidence. |
| Compact resource summary | `resources_found_gui_resources`, root x=24,y=74, w=248,h=18 | Added and current state resource totals with a tooltip for the six-resource ledger | `resources_found.gui.resource_summary` | Preserve this accepted ledger summary and its current tooltip. It is separate from the four field-mechanic metric slots. |
| Three core metrics | `resources_found_gui_values` / `resources_found_gui_closed_values`, root x=24,y=94, w=248, h=66 | Developed Yield, Excavation Depth, Workforce Safety | Existing dynamic selected-field and last-closed localization/bands | Keep exactly these three core metric rows in both active and history surfaces. |
| Contextual fourth metric | New active and closed Foreign Pressure text elements share the existing conditional row at root x=24,y=164, w=248,h=18 with the existing Disturbance row; baseline Breach at root y=184 moves to this row | Show exactly one value in priority order: Breach Pressure, otherwise Subsurface Disturbance, otherwise Foreign Pressure; suppress Disturbance/Breach under the existing suspended-state rule | Existing Disturbance and Breach keys plus new Foreign Pressure keys; breach state uses the existing seal sprite | Breach must exclude Disturbance in the visibility trigger. No metric is baked into art. |
| State art | Active/closed state icon in the existing right recess, root x=306..434,y=72..200 | Decorative state cue | Existing Seal, Unsafe, Disturbance, Breach, Sealing, Suspended, and Closed sprites with existing static fallbacks | Keep all sprite files and frame definitions unchanged. |
| Status band | `resources_found_gui_status` / `resources_found_gui_closed_status`, root x=24,y=204, w=248,h=48 | Existing authority, stage, lifecycle, contract, and commission text | Existing status localization | The mockup's boxed status inset is generated embellishment and will not be added to the runtime background. |
| Navigation and display controls | `resources_found_gui_previous` at x=31,y=261; `resources_found_gui_next` at x=79,y=261; `resources_found_gui_goto` at x=128,y=258; `resources_found_gui_animation` at x=239,y=258; `resources_found_gui_history` at x=350,y=258 | Navigate active fields, show the field state, toggle animation, or view closed history | Existing arrow sprites and two-frame `GFX_018_resource_field_action_button` | Preserve the source positions and effect wiring. These are information/navigation controls, not gameplay actions. |

The accepted 3+1 hierarchy keeps the first three values visible and chooses one fourth value by state. In routine and unsafe states the fourth value is Foreign Pressure. When Disturbance is revealed it replaces Foreign Pressure. When Breach is revealed it replaces both, including when the Disturbance flag also remains set. If the field is suspended, the existing semantics hide Disturbance and Breach, so the fourth slot falls back to Foreign Pressure.

The same priority applies to the closed-history surface using `resources_found_last_closed_field`. If the country has neither an active field nor a closed-history record, the scripted GUI and its decision category remain hidden rather than displaying an empty reference panel.

The source triggers implement that priority with mutually exclusive text visibility: unsuspended Breach wins; unsuspended Disturbance is visible only without a Breach flag; Foreign Pressure is visible when neither flag is revealed or while the field is suspended. The active and closed paths use the same rule against `resources_found_selected_field` and `resources_found_last_closed_field` respectively.

## Fixture values and visual budget

The reference depicts a synthetic Breach fixture with Arizona, active field 1/2, Developed Yield 72 Industrial, Excavation Depth 84 Abyssal, Workforce Safety 28 Critical, and Breach Pressure 72 Severe. These values are visual examples only; they are not observed save or campaign values.

The panel presents three core mechanic values and one mutually exclusive contextual value. The separate `Added` and `Total` resource ledger summary remains as required by the accepted spec. The panel contains two navigation arrows and three information/display controls, no gameplay-changing button, and no displayed gameplay cost.

## Implemented source delta

The accepted correction is implemented in `interface/018_resources_found.gui`, `common/scripted_guis/018_resources_found_scripted_gui.txt`, and `localisation/english/018_resources_found_system_l_english.yml`. The active and closed metric strings now contain three core rows. New active and closed Foreign Pressure text elements use the shared fourth-row bounds at local x=8,y=92; both Breach elements also use that row. The active and closed Disturbance triggers now exclude Breach, and the new Foreign Pressure triggers provide the default and suspended fallback.

| File | Pre-change SHA-256 | Post-change SHA-256 |
| --- | --- | --- |
| `interface/018_resources_found.gui` | `66F9C9C0805B8D84D4185EBAF9E38230415B0663CF6B6F22608C5D54E39B41D7` | `C33A160A10A3EC1EC70CF539D67489F55980858B98AC98D6E89D9BF617155685` |
| `common/scripted_guis/018_resources_found_scripted_gui.txt` | `7F582FFA6ED291CE2B5EA5DF07436D3184343D85B61EEEA828A2229AA6ED9CF0` | `B44657B425490053B4E2D3FE262DEDBF143E0841C0203B021ECD904FB3B3E32A` |
| `localisation/english/018_resources_found_system_l_english.yml` | `C17A802C5BA3B05BFD20794688B0333ABC06F44BD57151EEDC0FC13C7BA9B62D` | `A252ADA3F976015E41454C232C911FC4500C8FFAFBBBD78EB9CA9AFA78208C4A` |

The English localisation file retains its UTF-8 BOM.

## Generation prompt and limitations

The built-in ImageGen tool generated one opaque UI reference from the decoded panel and Breach sprite. The prompt was:

> Use case: ui-mockup. Asset type: reference-only layout blueprint for the existing HOI4 Event 018 decision-category panel, not runtime art. Input image 1 is the exact 470x304 painted panel background; input image 2 is the existing static Breach state sprite. Create one reference mockup showing the existing panel with the approved compact three-core-plus-one-contextual-metric layout. Preserve the dark steel frame, engraved top rail, slate writing area, circular medallion recess, and four lower wells as faithfully as possible. Place the existing Breach sprite in the medallion. Keep the title in the top rail; the state header in the upper-left slate; the three core rows Developed Yield, Excavation Depth, and Workforce Safety in the left content area; and exactly one contextual fourth row, Breach Pressure, below them. Keep the existing status band below the values and all text clear of the right medallion. Along the bottom, show left and right navigation arrows in the first engraved well, then Show State, Animation, and History in the remaining wells. Text: “RESOURCE FIELD RECORD”; “Field: Arizona”; “Active field 1/2”; “Developed Yield 72 Industrial”; “Excavation Depth 84 Abyssal”; “Workforce Safety 28 Critical”; “Breach Pressure 72 Severe”; “National Works · Deep Works”; “Breach active”; “C: Open M: None”; “Show State”; “Animation”; “History”. Use restrained vintage HOI4 typography and the existing dark steel and brass treatment. Exactly four visible field-mechanic values; do not show Foreign Pressure or Subsurface Disturbance in this Breach fixture. Do not add any other metrics, gauges, menus, tabs, costs, icons, decorative panels, or controls. This image is reference only; the final UI uses native controls, localization, state triggers, and the unchanged source background. No watermark or HOI4 logo.

ImageGen slightly re-rendered the panel texture and introduced separator/status-frame embellishments. Those details are nonbinding and will not enter the runtime layout. The parent accepted the 3+1 composition; exact source art, positions, native controls, localization, and state logic remain authoritative.

## MCP evidence status before implementation

The exact pre-change `hoi4_gui_inspect` call for `resources_found_field_window` with scenario `{id:'usa_1936_field',date:'1936.1.1'}` timed out awaiting `tools/call` after 600 seconds. The matching baseline `hoi4_gui_render` request also timed out after 600 seconds. The short GUI `reference_context` request timed out after 600 seconds. The post-change `gui_inspect` request was issued once but remained pending without an error response when waiting stopped after those confirmed timeouts. These route gaps remain unresolved; the reference image and source mapping do not replace required MCP visual evidence.

The one lightweight post-change `hoi4_gui_render` request, with the pre-change `.gui` text supplied as `sourceBaseline`, also timed out awaiting `tools/call` after 600 seconds. No before or after production image, diagnostic JSON, source revision, hierarchy, click-region, or comparison artifacts were returned.
