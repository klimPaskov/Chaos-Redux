# Alien infantry counter reconciliation

Status: final counter files exist and are registered; parent visual/runtime review remains parent-owned. The 3D worker did not recreate or overwrite them.

## Consumers and installed files

- Owning subunit and sprite token: `alien_infantry`.
- Model consumer: `alien_infantry_entity`.
- `GFX_group_alien_infantry_icon` and `GFX_unit_alien_infantry_icon_medium` resolve through `interface/alien_infantry_system.gfx` to `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds`.
- Large DDS: 152x42, two 76x42 frames, 25,664 bytes, SHA-256 `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`.
- `GFX_unit_alien_infantry_icon_medium_white` resolves through the same GFX file to `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`.
- On-map DDS: 60x12, two 30x12 frames, 3,008 bytes, SHA-256 `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`.

## Vanilla and skill-local reconciliation

- Installed definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, SHA-256 `0D7B62CAF328B3C296EC27AB85318F3CC78CC760B02923538BF5240815963335`; infantry entries at lines 46 and 199 use `noOfFrames = 2`.
- Installed DDS references: `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.
- Matching skill-local families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`, including their contact sheets and decoded infantry references.
- Required large-counter behavior: transparent 152x42 strip, normal muted vanilla-green silhouette in the left frame and separate sparse pale schematic state in the right frame.
- Required map-counter behavior: transparent 60x12 strip with two 30x12 states and the same restrained silhouette/state language.
- Recorded palette anchor: RGB 73,106,73 with nearby shaded greens such as 74,107,74, sampled from the decoded installed reference rather than chosen arbitrarily.

## Package evidence

The producing package is `docs/assets/016_brilliant_scientist/dhrondan_icon_package/`. Its `manifest.md` records both consumers as complete, `package_records/dds_validation.json` records decoded DDS size/alpha/header evidence, and `contact_sheet/dhrondan_icon_package_contact_sheet.png` is the comparison sheet. The package records native ImageGen transparency with no background-removal fallback.

Parent-owned status: the GFX registration already exists. Live counter display and final visual acceptance remain parent/user-owned and are not claimed by this model package.
