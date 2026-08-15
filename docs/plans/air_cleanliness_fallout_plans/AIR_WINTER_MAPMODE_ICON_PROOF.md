# Air Winter Mapmode Icon Proof

Status: static frame geometry and sprite ownership proven.

## Engine contract

Vanilla `common/map_modes/documentation.md` states that a scripted mapmode named `air_winter_state_map_mode` resolves `GFX_mapmode_buttons_selected_small_air_winter_state_map_mode` and `GFX_mapmode_buttons_deselected_small_air_winter_state_map_mode` for its icons.

The shared strip is therefore not the ownership surface for the Air Winter icon. Air Winter uses two dedicated sprite definitions in `interface/mapmodes_interface.gfx`, one selected and one deselected sprite for its single mapmode.

## Shared strip geometry

The installed vanilla selected and deselected strips are both 360 by 18 pixels with `noOfFrames = 18`. Each vanilla frame is 20 by 18 pixels.

The Chaos Redux selected and deselected strips are both 380 by 18 pixels with `noOfFrames = 19`. Each Chaos Redux frame is also exactly 20 by 18 pixels. The declared frame count divides the source width without a remainder.

Pixel comparison after DDS decoding found:

- frames 1 through 17 match the corresponding vanilla frames
- vanilla frame 18 is fully transparent
- Chaos Redux frame 18 exactly matches the dedicated Deaths mapmode icon
- Chaos Redux frame 19 exactly matches the dedicated contaminated-states mapmode icon
- the Air Winter icon pair is not duplicated in the shared strip

The comment that Chaos Redux reuses vanilla slot 18 and appends slot 19 is accurate. The earlier plan claim that the strip needed 20 frames was incorrect.

## Air Winter icon ownership

Both Air Winter icon files decode to 20 by 18 pixels:

- `gfx/interface/mapmode/custom/air_winter_state_map_mode_selected.dds`
- `gfx/interface/mapmode/custom/air_winter_state_map_mode_deselected.dds`

Their sprite names exactly follow the official scripted-mapmode naming rule. No strip append and no frame-number allocation is required for Air Winter.

## Source identity

The inspected strip hashes are:

- Chaos Redux selected: `79FE30531421E42DA39761247034723F052BD328068A03EA78EC3D6A73FA065B`
- Chaos Redux deselected: `D95EC03889A4ECC31EB8421DE73FFC6E3AA785E6BE65AA244E731E418B1E1A0E`
- installed vanilla selected: `9CF3B03EF108FBD62DFD6F067A22D9EB7A949E6C53DCD50C8D97FAD418836EE0`
- installed vanilla deselected: `856730DD270DDC8804971EE3D678319BE7232EA4973F7C0320BD001D4A2261F3`

## MCP boundary

The final `hoi4.map_inspect` pass produced artifact hash `8ce66a122e6c0936098b9666d73660ce0c25771637e480d785a7213bb90478da`. Province definitions, bitmap geometry, state and strategic-region membership, adjacencies, supply nodes, and railways passed. The global map validation remains false on `map/buildings.txt` position and floating-harbor diagnostics, a file outside this mapmode consolidation.

The `hoi4.gui_inspect` scenario `single_air_winter_mapmode` inspected zero GUI elements because a scripted mapmode key is not a scripted GUI window. The installed MCP exposes no scripted-mapmode selector, so it cannot directly count or render these registrations. The one-mapmode result is therefore bounded to the official scripted-mapmode naming contract plus the complete source, sprite, localisation, and asset reference audit. It is not presented as equivalent to a dedicated MCP scripted-mapmode render.

## Verdict

The frame-count, frame-width, and slot-ownership gate is closed. Air Winter owns one scripted mapmode and one selected and deselected icon pair. This is static source proof. It does not claim that a player clicked or observed the mapmode in a running game.
