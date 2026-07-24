# IW-002 Wales portrait source handoff

This is a parent-owned wiring handoff for two source-cleared grounded male portrait candidates. No GFX file was edited in this subtask.

## Stable runtime consumers

| Existing sprite name | Reserved texture path | Proposed identity source | Source crop |
| --- | --- | --- | --- |
| `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | David Rhys Grenfell, Welsh Labour MP and Welsh civic figure | `exact_crops/david_grenfell_civic_crop.png` |
| `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | Major George Frederick Myddleton Cornwallis-West, Welsh-born Scots Guards officer | `exact_crops/george_cornwallis_west_commander_crop.png` |

The existing parent-owned `.gfx` consumer is `interface/006_independence_wave_region_01_portraits.gfx`. The existing national-council localisation still names Saunders Lewis, and this handoff deliberately does not change that identity wiring.

## Suggested downstream sprite definitions

The parent may retain the existing sprite names and texture paths without changing the interface contract.

```text
spriteType = {
    name = "GFX_portrait_WLS_independence_wave_national_council"
    texturefile = "gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds"
}

spriteType = {
    name = "GFX_portrait_WLS_independence_wave_mountain_commandant"
    texturefile = "gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds"
}
```

These are reference definitions only. The parent should not paste them into the existing `.gfx` file unless the texture files have passed the separate portrait review and DDS stage.

## Processing requirements

- Use the exact source crops as the sole identity references: `exact_crops/david_grenfell_civic_crop.png` and `exact_crops/george_cornwallis_west_commander_crop.png`.
- Use canonical vanilla leader or commander portraits only for style references, never as identity templates.
- Preserve facial geometry, eye spacing, nose and mouth shape, hairline, and distinctive moustache or glasses where present.
- Age David Grenfell from the 1922 source toward his 1936 age without changing identity geometry.
- Age George Cornwallis-West from the c.1900-1910 source toward his 1936 age without adding unsupported insignia or inventing a mountain-unit history.
- Produce and independently review a `156x210` PNG before DDS conversion.
- Preserve the Commons and institutional source credits in the final asset manifest.

No final PNG, DDS, or GFX wiring is present in this package. W. J. Gruffydd, William Ambrose Bebb, David Lloyd George, Gwilym Ivor Thomas, and the Hugh Evan-Thomas alternatives are not approved runtime replacements from this handoff.

