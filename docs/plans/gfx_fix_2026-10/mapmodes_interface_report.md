# Mapmode icon repair

Disposition: implemented asset repairs; MCP GUI visual gate remains blocked.
Acceptance basis: the graphics-fix task explicitly requests every finding in this group.

| Finding | Result | Runtime file |
|---|---|---|
| Famine deselected, severity 1 (`GFX_mapmode_buttons_deselected_small_famine_state_map_mode`) | Native ImageGen wheat silhouette, solid light grey, centred at 20×18 | `gfx/interface/mapmode/custom/famine_state_map_mode_deselected.dds` |
| Migration deselected, severity 1 (`GFX_mapmode_buttons_deselected_small_migration_state_map_mode`) | Native ImageGen walking civilians with bundles, both figures retained, solid light grey | `gfx/interface/mapmode/custom/migration_state_map_mode_deselected.dds` |
| Famine selected, severity 2 (`GFX_mapmode_buttons_selected_small_famine_state_map_mode`) | Same wheat silhouette in beige over an opaque charcoal interior; existing gold border retained | `gfx/interface/mapmode/custom/famine_state_map_mode_selected.dds` |
| Migration selected, severity 2 (`GFX_mapmode_buttons_selected_small_migration_state_map_mode`) | Same civilian silhouette in beige over an opaque charcoal interior; existing gold border retained | `gfx/interface/mapmode/custom/migration_state_map_mode_selected.dds` |

## Production and review

The stable sprite names and 20×18 canvases remain registered in `interface/mapmodes_interface.gfx`; no registry or GUI edits were needed.
The installed vanilla `interface/mapmodes_interface.gfx`, `interface/mapmodes_interface.gui`, and both vanilla small mapmode strips establish the frame and palette family.
The exact custom deaths selected/deselected pair establishes the existing custom-button treatment.
Native ImageGen supplied transparent glyph sources; alpha-mask cleanup removed isolated specks and flattened the intended opaque silhouette without removing a background.
The initial bowl source was rejected at native size because its disconnected wheat marks were unclear.
The replacement wheat source is `docs/assets/gfx_fix_shared_ui/famine_source_v2.png`; migration uses `migration_source.png` in the same retained workspace.
The original prompts request a solid light-grey wheat bundle and walking civilians with bundles, no text, glow or scenery, with native transparency.
The generated-source paths are recorded by their original native ImageGen basenames in the shared UI workspace; originals remain under `C:/Users/klimp/.codex/generated_images/01a10fb7-f6ce-7862-9e28-a192ae914d46/`.

Conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` with Microsoft DirectXTex.
All four decoded runtime DDS images exactly match their processed PNGs.
Every selected interior pixel is opaque; the inactive glyphs use alpha 255 instead of the former ghosted opacity.
Native-size and 5× nearest-neighbour reviews are in `docs/assets/gfx_fix_shared_ui/mapmode_before.png` and `mapmode_after.png`.
The regenerated group sheet is `docs/assets/gfx_fix_shared_ui/contact_sheets/mapmodes_interface_1.jpg`; the original review sheet is retained beside it as `old_mapmodes_interface_1.jpg`.
`docs/assets/gfx_fix_shared_ui/validation.json` records final dimensions, SHA-256 and pixel comparisons.

## Reference and MCP evidence

`hoi4.reference_read` read offline `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, lines 30–99, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, including `texturefile` and `noOfFrames` rules.
Installed `common/scripted_guis/_documentation.md`, lines 1–35, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, was read through the same route.
`hoi4.source_lookup` returned both mod and vanilla `GFX_mapmode_buttons_selected_small` definitions, lines 18–22, source revision `a874904e876d8d45494aae78a9f10a31e7bb854436fc3e59e8c2d786f5978ef1`.
The context bundle omitted unrelated sections; no full GUI or scope coverage is claimed.
The narrow `hoi4.gui_inspect` call for `MapmodesInterface_Ingame`, scenario `shared_mapmode_before`, date `1936.1.1`, `closedFlags=true`, stalled without returning artifacts and was stopped before asset promotion.
No before/after production GUI render or `validation.json` was returned, so contact sheets do not substitute for that evidence.
The native custom mapmode rows are populated by the engine; their live selection and hover remain unobserved.

## Orchestrator live checks

Load any 1936 country and open the mapmode chooser.
Find Famine and Migration, inspect them while inactive, select each, then switch back to Political.
Both inactive symbols must remain clearly visible in light grey; selected buttons must show the same symbol in beige inside a filled dark gold-bordered button.
Check both symbols at 1920×1080, UI scale 1, and the smallest supported resolution for cropping or overlap.

No artwork substitutions or omitted findings were used in this group; the outstanding limitation is the MCP GUI artifact gate.
