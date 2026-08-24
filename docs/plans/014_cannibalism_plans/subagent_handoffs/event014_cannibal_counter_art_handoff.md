# Event 014 cannibal counter art handoff

Status: **replacement package and all nine registry families integrated; live consumer review pending**. Eight original counter families are installed across the large division, on-map, and texticon consumers, and the separate `cannibal_bone_riders` cavalry family has all three runtime consumers validated and registered. This handoff owns the art evidence; the parent owns in-game consumer review.

## Exact consumers and tokens

| Sub-unit id | Large division token | Small on-map token | Text-icon token | Visual identifier |
| --- | --- | --- | --- | --- |
| `cannibal_scavenger_warband` | `GFX_unit_cannibal_scavenger_warband_icon_medium` | `GFX_unit_cannibal_scavenger_warband_icon_medium_white` | `GFX_unit_cannibal_scavenger_warband_icon_small` | Spear-running skull-helmed feral scavenger with rib harness and tooth streamer |
| `cannibal_feast_guard` | `GFX_unit_cannibal_feast_guard_icon_medium` | `GFX_unit_cannibal_feast_guard_icon_medium_white` | `GFX_unit_cannibal_feast_guard_icon_small` | Cleaver plus boiler-plate shield, skull helm, rib guard and painted mouth |
| `cannibal_feast_cohort` | `GFX_unit_cannibal_feast_cohort_icon_medium` | `GFX_unit_cannibal_feast_cohort_icon_medium_white` | `GFX_unit_cannibal_feast_cohort_icon_small` | Forked polearm above a compact painted bone-armoured cohort |
| `cannibal_bone_guard` | `GFX_unit_cannibal_bone_guard_icon_medium` | `GFX_unit_cannibal_bone_guard_icon_medium_white` | `GFX_unit_cannibal_bone_guard_icon_small` | Heavy poleaxe elite with skull-and-rib armour and asymmetrical bone plate |
| `cannibal_island_reavers` | `GFX_unit_cannibal_island_reavers_icon_medium` | `GFX_unit_cannibal_island_reavers_icon_medium_white` | `GFX_unit_cannibal_island_reavers_icon_small` | Harpoon and boarding axe with rope loop, skull helm and rib harness |
| `cannibal_siege_eaters` | `GFX_unit_cannibal_siege_eaters_icon_medium` | `GFX_unit_cannibal_siege_eaters_icon_medium_white` | `GFX_unit_cannibal_siege_eaters_icon_small` | Sledgehammer breacher with skull face and bone shoulder armour |
| `cannibal_march_predation_column` | `GFX_unit_cannibal_march_predation_column_icon_medium` | `GFX_unit_cannibal_march_predation_column_icon_medium_white` | `GFX_unit_cannibal_march_predation_column_icon_small` | Plain bow pursuit runner with painted skull cap and rib harness |
| `cannibal_network_cadre` | `GFX_unit_cannibal_network_cadre_icon_medium` | `GFX_unit_cannibal_network_cadre_icon_medium_white` | `GFX_unit_cannibal_network_cadre_icon_small` | Short bow, courier knife, satchel and rib collar in a crouched cluster |

All selected sources visibly echo the approved fictional feral cult-warrior references: skull helmets or skull headgear, rib/bone armour, tooth/bone trophies, heavy non-specific skin/body paint, crude hide/rope bindings, primitive weapons, and manic silhouettes. No identifiable living Indigenous motifs, regalia, sacred symbols, culture-specific dress, or ceremonial weapon decoration were used. Prompt/source provenance is fully mapped in `docs/assets/014_cannibalism/counters/irregular_units/prompts/prompts.md`.

## Exact installed reference gate

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` defines the large `GFX_unit_infantry_icon_medium` and on-map `GFX_unit_infantry_icon_medium_white` consumers.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/texticons.gfx#GFX_unit_irregular_infantry_icon_small` defines the texticon consumer.
- `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` is an uncompressed 152x42 two-frame strip with two 76x42 frames.
- `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` is an uncompressed 60x12 two-frame strip with two 30x12 frames.
- `gfx/texticons/unit_irregular_infantry_icon_small.dds` is an uncompressed 60x12 two-frame strip with two 30x12 frames.
- Canonical skill-local contact sheets and references were inspected under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/` before generation.
- The normal large/texticon frames use the installed sampled vanilla-green ramp, including the dominant `(73,106,73)` anchor. The normal on-map frame uses the inspected neutral grayscale treatment. Frame 1 preserves the installed pale/selected state behavior. Transparent unused canvas, two-frame ordering, and alpha corners are preserved.

## Ready-to-copy parent definitions

The parent may copy these definitions verbatim into `interface/chaosx_subuniticons.gfx`:

```text
spriteType = { name = "GFX_unit_cannibal_scavenger_warband_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_scavenger_warband_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_scavenger_warband_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_scavenger_warband_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_feast_guard_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_feast_guard_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_feast_guard_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_feast_guard_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_feast_cohort_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_feast_cohort_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_feast_cohort_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_feast_cohort_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_bone_guard_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_bone_guard_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_bone_guard_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_bone_guard_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_island_reavers_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_island_reavers_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_island_reavers_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_island_reavers_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_siege_eaters_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_siege_eaters_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_siege_eaters_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_siege_eaters_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_march_predation_column_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_march_predation_column_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_march_predation_column_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_march_predation_column_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_network_cadre_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_network_cadre_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_network_cadre_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_network_cadre_icon.dds" noOfFrames = 2 }
```

The parent may copy these definitions verbatim into `interface/chaosx_texticons.gfx`:

```text
spriteType = {
	name = "GFX_unit_cannibal_scavenger_warband_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_scavenger_warband_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_feast_guard_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_feast_guard_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_feast_cohort_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_feast_cohort_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_bone_guard_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_bone_guard_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_island_reavers_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_island_reavers_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_siege_eaters_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_siege_eaters_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_march_predation_column_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_march_predation_column_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
spriteType = {
	name = "GFX_unit_cannibal_network_cadre_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_network_cadre_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
```

## Evidence and validation

| Consumer | Source | Processed | Decoded round-trip | Contact sheet |
| --- | --- | --- | --- | --- |
| Large | `docs/assets/014_cannibalism/counters/irregular_units/source_png/large_replacement/` | `processed_png/large/` | `decoded_dds/large/` | `contact_sheets/large_roundtrip_replacement_contact.png` |
| On-map | `docs/assets/014_cannibalism/counters/irregular_units/source_png/small_replacement/` | `processed_png/small/` | `decoded_dds/small/` | `contact_sheets/small_roundtrip_replacement_contact.png` |
| Texticon | `docs/assets/014_cannibalism/counters/irregular_units/source_png/texticons_replacement/` | `processed_png/texticons/` | `decoded_dds/texticon/` | `contact_sheets/texticon_roundtrip_replacement_contact.png` |

`validation/dds_validation.json` records 24/24 passing assets: complete legacy 128-byte header, exact lengths (`25664` bytes for 152x42 and `3008` bytes for 60x12), uncompressed BGRA masks, dimensions, two frames, alpha corners, and exact processed-to-decoded pixel equality. `validation/visible_bounds.json` records each frame bbox, alpha statistics, source/processed/runtime hashes, and the sampled reference bounds. `contact_sheets/all_24_replacement_contact.png` shows all three consumers and decoded runtime identity in one labeled matrix. The final full-size and native-size replacement sheets were visually reviewed and accepted by the parent.

The on-map normal frame was checked against the decoded installed cavalry/infantry neutral grayscale reference rather than the enlarged sheet alone: all eight replacement normal frames now use histogram-stretched neutral grayscale with maximum value 230 and mean luminance in the installed reference range, while the pale state frame remains unchanged. Large and texticon normal frames retain the sampled vanilla-green ramp.

The only alpha fallbacks are documented in `counters/irregular_units/prompts/prompts.md`; opaque ImageGen candidates remain preserved under the `*_replacement_opaque` directories. The fallback tool was the installed `remove_chroma_key.py` with white-key tolerance 24, soft matte, threshold 24/64, spill cleanup, and edge contract 2 for large Bone Guard or 1 for the small/texticon fallbacks.

## Ninth cavalry family: `cannibal_bone_riders`

The ninth family uses the exact installed cavalry consumers rather than the irregular-infantry consumers. The art shows one bone-armoured horse with one skull-helmeted feral rider casting a sling, with culture-neutral invented paint, bone armour, tooth trophies, and crude rope bindings.

| Consumer | Installed reference | Replacement runtime | Evidence |
| --- | --- | --- | --- |
| Large division | `gfx/interface/counters/divisions_large/unit_cavalry_icon.dds` (`152x42`, `2x76x42`) | `gfx/interface/counters/divisions_large/unit_cannibal_bone_riders_icon.dds` | `source_png/bone_riders_replacement/large/`, `processed_png/bone_riders/large/`, `decoded_dds/bone_riders/cannibal_bone_riders_large.png` |
| On-map | `gfx/interface/counters/divisions_small/onmap_unit_cavalry_icon.dds` (`60x12`, `2x30x12`) | `gfx/interface/counters/divisions_small/onmap_unit_cannibal_bone_riders_icon.dds` | `source_png/bone_riders_replacement/small/`, `processed_png/bone_riders/small/`, `decoded_dds/bone_riders/cannibal_bone_riders_small.png` |
| Texticon | `gfx/texticons/unit_cavalry_icon_small.dds` (`60x12`, `2x30x12`) | `gfx/texticons/unit_cannibal_bone_riders_icon_small.dds` | `source_png/bone_riders_replacement/texticon/`, `processed_png/bone_riders/texticon/`, `decoded_dds/bone_riders/cannibal_bone_riders_texticon.png` |

The exact installed cavalry definitions were inspected in `interface/subuniticons.gfx` and `interface/texticons.gfx`, and the decoded reference contact sheet is `docs/assets/014_cannibalism/counters/irregular_units/contact_sheets/cavalry_reference_contact.png`. Its normal large frame bbox is `[14,6,61,39]`, selected large frame bbox `[13,9,64,38]`, normal small/text bbox `[5,0,24,12]`, and selected small/text bbox `[2,0,27,12]`. The replacement strips preserve the two-frame order and sampled cavalry green/neutral/pale value behavior. `validation/cavalry_reference_gate.json` records complete legacy headers and reference hashes.

Ready-to-copy definitions for `interface/chaosx_subuniticons.gfx`:

```text
spriteType = { name = "GFX_unit_cannibal_bone_riders_icon_medium"
	textureFile = "gfx/interface/counters/divisions_large/unit_cannibal_bone_riders_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_cannibal_bone_riders_icon_medium_white"
	textureFile = "gfx/interface/counters/divisions_small/onmap_unit_cannibal_bone_riders_icon.dds" noOfFrames = 2 }
```

Ready-to-copy definition for `interface/chaosx_texticons.gfx`:

```text
spriteType = {
	name = "GFX_unit_cannibal_bone_riders_icon_small"
	texturefile = "gfx/texticons/unit_cannibal_bone_riders_icon_small.dds"
	legacy_lazy_load = no
	noOfFrames = 2
}
```

`validation/bone_riders_dds_validation.json` records 3/3 passing assets with exact dimensions, 128-byte legacy headers, BGRA masks, alpha corners, and processed-to-decoded pixel equality. `validation/bone_riders_visible_bounds.json` records each source/processed/runtime/decoded frame bbox and hash. Runtime SHA-256 values are `fa0ca9f1e5fec9931b89dca0e29843720f0e9d15c9a8d3372d5e2d60b5b15504` (large), `babf1034ae0180b890a2ebb38e78c2a6228264e58e33e84439801eff22dba5fd` (on-map), and `3799fb8e85b608800529eb8cfb879114756a214a24006d86c16882226055a304` (texticon). The generated family contact sheet is `contact_sheets/cannibal_bone_riders_replacement_contact.png`; its native-size strip/frame evidence is `contact_sheets/cannibal_bone_riders_native_grid.png`.

## Complete runtime SHA-256 table

| Family | Slug | Runtime DDS SHA-256 |
| --- | --- | --- |
| large | `cannibal_scavenger_warband` | `82db80534e536e7714b68082f044a9b9b14b7bb64c00ac7a59880944a09d9b7a` |
| large | `cannibal_feast_guard` | `16183a6fc30940d7d8b3fc76a6c8d0649425617b21250deca7d0369abe028791` |
| large | `cannibal_feast_cohort` | `5138156d36d8792bb4199e37ef3b6a0a30778fb419cb640c463cd5f4c6fb81a3` |
| large | `cannibal_bone_guard` | `4189a8e5f1f943151d90847a003484bed676805606b2eecdf347616345da62d1` |
| large | `cannibal_island_reavers` | `95c4c676facb086bc06d3d0cf312d776e9063b3deac6ea2b6f6a0c5d10d7b789` |
| large | `cannibal_siege_eaters` | `38bb73744db081350aa35aa2f7075dffcd98561652a422294c5a1f93e1ada2fa` |
| large | `cannibal_march_predation_column` | `515f6617d57fd72496a1fb853fdc92cac563d271e31d97c813f7445c384c4e38` |
| large | `cannibal_network_cadre` | `5ff4f29b90062accd9405460f5585637eff7fd2bf3ccc1795863913b5d7d3376` |
| small | `cannibal_scavenger_warband` | `7593f9e064a4fd28923216ac3c5204fee7584a4a222a19d966ecdd5cd9665411` |
| small | `cannibal_feast_guard` | `7619f643c531045e9a7c0b84094a1f7204985d45a48e1a9a4014c22910fa94f0` |
| small | `cannibal_feast_cohort` | `4be249b4a74a8a89b8cc84f6fa293ca606939849748539f8dcf9b30e35f672ca` |
| small | `cannibal_bone_guard` | `21aa17a7c2d3d0e366f9ef42b307d3f4dbd77a8dc1381929eb5464715e313bba` |
| small | `cannibal_island_reavers` | `c9b2f062206fd883cee011c02edd8e1ca602edaf05a443d8130532de2d54c222` |
| small | `cannibal_siege_eaters` | `062969fb55e754d2332f2110460c2cb618f30c0b414620ca27f31f05cb9cf17c` |
| small | `cannibal_march_predation_column` | `752e2b01a52f2fb49926d9c4aad2de5c55a3ba5dc79a1404c3f9de92ac588df1` |
| small | `cannibal_network_cadre` | `27aa2aabf2bdd4118063961247401951a4fbcb1afa9c7edaf0152a59926fbc8c` |
| texticon | `cannibal_scavenger_warband` | `51527b0df60d23b5876edf8a0d47b08e51104dd1c53aa83d8e19f83449e114cb` |
| texticon | `cannibal_feast_guard` | `ba283a182b3fc13cedb11fb1ba0b7d9c910910433f98e64da6b4825667489db9` |
| texticon | `cannibal_feast_cohort` | `869062d8e0c84971d17a8c0dd680eb6e9dfaf7d168574257c865196d54a3a520` |
| texticon | `cannibal_bone_guard` | `c3b380aaf7d42bfa6e838ab172db313762fab7e68913c9693fc41f175ee5ed32` |
| texticon | `cannibal_island_reavers` | `559e75128e8c912a6196db017dc4a21e173b06ae02f9dbd9f13920cdbb7eae5d` |
| texticon | `cannibal_siege_eaters` | `d5637f955bc8115ade3f2d09772924fe0b146ee61657d27b6cafd5276688470c` |
| texticon | `cannibal_march_predation_column` | `4e371fbb3c2a6f7a702359052d6a4818c55a36009396f9b4480ed86f74dc4e78` |
| texticon | `cannibal_network_cadre` | `30cd4888f2def5bf13c587faf5a1ff188da6ee4f2d31af55fbb1e8bb30824b81` |

## Parent boundary and remaining work

The counter worker did not edit gameplay, localisation, events, decisions, focuses, or spreadsheets. The existing eight-family registrations remain valid because their source tokens, runtime filenames, dimensions, frame counts, and frame order are unchanged. The parent integrated all three ninth-family cavalry sprites into the shared registries. Live consumer review remains parent-owned.
