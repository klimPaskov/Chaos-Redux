# Vanilla GFX override repair evidence

## Scope and result

The state-view override was already synchronized with current vanilla when compared, except for the intentional extended building icon strip, so `interface/countrystateview.gfx` remains unchanged. `interface/countrytechtreeview.gfx` was missing exactly one current vanilla sprite definition and now includes it: `GFX_special_forces_doctrine_folder_icon`, with vanilla's texture path `gfx/interface/techtree/icons/special_forces_doctrine_folder_icon.dds`.

No interface GUI, gameplay, or asset files were edited. No game or window was launched.

## Source comparison

Compared the mod and installed-game `.gfx` files directly. Installed vanilla paths are under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/`.

| File | Mod before | Installed vanilla | Result |
|---|---|---|---|
| `countrystateview.gfx` | SHA-256 `54A9D01E19E0AB3CD54673A924050EDF1DC435AD5F581BFBC324A9965D2C5196` | SHA-256 `B12B196875611B51FB7DDE7F5F0893AFF0327D5AE848AFDA63D0AC77F18BBA8C` | All 246 sprite names are present in both. The only meaningful block difference is `GFX_buildings_strip`: mod `noOfFrames = 35`, vanilla `noOfFrames = 31`. A separate whitespace-only difference in `GFX_terrain_water_shallow_sea_night_rain` has no behavior change. The shallow-sea daytime sprite reported by the prior audit is already present in the current mod file. |
| `countrytechtreeview.gfx` | SHA-256 `377F11794627DD357C4E37B02A7779C289D576FC8F34CD733AE81768EFC1336E` | SHA-256 `A65A41F2A3D94B62C38DDD7311D2606CD4A8817872F374893D851F6EC517DC8C` | The mod had 294 sprite names against vanilla's 295. The sole missing definition was `GFX_special_forces_doctrine_folder_icon`; no mod-only definitions or changed same-name sprite blocks were found. |

The post-edit `countrytechtreeview.gfx` SHA-256 is `2812769CA69098EA21743DD88E05502555BA223A856F010B4D4366E614888914`. Its only change is the exact four-line vanilla sprite block placed alongside the doctrine-folder sprite definitions. It now has the previously missing vanilla sprite and no unrelated edits.

## Retained mod-specific difference and consumers

The `35`-frame strip is required by Chaos Redux building definitions and its current texture. `common/buildings/chaosx_buildings.txt` assigns frames 32 and 33 to the biowarfare and chemical-warfare facilities. `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md` records frames 34 and 35 for camp buildings. The strip texture exists at `gfx/interface/buildings/building_icon_strip.dds`; its DDS header declares `1610 x 46`, which is exactly 35 horizontal `46 x 46` frames. Installed vanilla's strip is `1426 x 46`, exactly 31 frames, so reverting the override to 31 would remove four frames used by mod buildings.

The new folder sprite points to an existing installed vanilla texture at `gfx/interface/techtree/icons/special_forces_doctrine_folder_icon.dds` (`91 x 61`). The existing technology-tree GUI contains the `tech_special_forces_tree` gridbox. This patch restores the vanilla sprite registration without changing that GUI or its layout.

## Reference evidence and limits

The HOI4 MCP reference context, search, read, and source lookup routes were available and used. Offline wiki evidence: `Graphical asset modding` (`paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, lines 30 to 100) documents `spriteType` fields and horizontal frame counts; `Building modding` (`paradox_wiki/Building modding - Hearts of Iron 4 Wiki.md`, revision `1e5fb5410a26af12b5b791b193f8f602c4ef8a3614ed897ae4c67084477f7bfc`, lines 135 to 152) establishes that `icon_frame` selects a `GFX_buildings_strip` frame and that extending it requires matching strip artwork and frame count; `Character modding` (`paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, revision `8ef3d5f9923026dd81f239944710b7331a8d06ad42e4345b32fce4e86dd95d98`, lines 631 to 654) explains sprite override evaluation and filename order. `Technology modding` (`paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md`, revision `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee`, lines 626 to 667) was read for the country technology tree's GFX sprite conventions. `Interface modding` (`paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, lines 178 to 195) confirms that GUI icon elements refer to spriteType definitions and can select a frame from a multi-frame sprite.

After the edit, `hoi4.source_lookup` resolves the new owner `GFX_special_forces_doctrine_folder_icon` at `mod:interface/countrytechtreeview.gfx`, lines 1650 to 1653, source revision `e75a9c34f4688d9fca67df50d1a50c091e5e905283c69616748bf46ebd48a98e`; the indexed lookup returned no explicit references for this convention-based folder sprite. The vanilla GUI contains the corresponding `tech_special_forces_tree` folder gridbox.

The installed game documentation directory contains no dedicated interface `.gfx` or `spriteType` documentation section surfaced by the bounded reference search. Current installed vanilla `.gfx` definitions and the installed vanilla DDS files were therefore used as the primary implementation precedents and consumer assets.

Validation was static: sprite-definition comparison, consumer reference search, texture-path existence, and DDS dimension/frame arithmetic. No live game or visual runtime validation was performed; that remains for the user.
