# Stone Cohorts and Forest Giants counter finalize handoff

Date: 2026-09-12.

Owner: `/root/stone_forest_finalize/stone_forest_counters`.

Status: both packages are complete as counter production packages, parent-accepted, and promoted.

Scope completed: bounded counter audit and replacement evidence for the existing `stone_cohorts` and `forest_giants` 3D repair packages.

The package outputs are versioned under `docs/assets/012_africa/models_3d/stone_cohorts/counters/finalize_20260912/` and `docs/assets/012_africa/models_3d/forest_giants/counters/finalize_20260912/`. The only handoff document added outside those package folders is this file.

The worker did not edit shared GFX, unit-definition, gameplay, runtime DDS, or old evidence files. The parent later promoted the four staged DDS outputs into the runtime texture folders in its own commit, as recorded by the package receipts below.

## Parent acceptance and promotion

Parent visual review accepted all four final DDS outputs and the parent promotion commit is `9fd0240264dfab28ca89cf1f8b780734957ccf57`.

The Stone receipt is `docs/assets/012_africa/models_3d/stone_cohorts/evidence/finalize_20260912/counter_parent_promotion_receipt.json`. It records `worker_runtime_mutations: false`, `runtime_byte_equality: true`, and `no_in_game_validation: true`. The staged `unit_stone_cohorts_icon.dds` SHA-256 `d94e7bdf5baf96d113290b0e6e95dd8c2806260ac915bb928212b16ec758971d` equals the current `gfx/interface/counters/divisions_large/unit_stone_cohorts_icon.dds` bytes, and staged `onmap_unit_stone_cohorts_icon.dds` SHA-256 `8dc53623a47442fd5e27aeea891bad9565ae788af8b135853d4f2ee5ba8d69bb` equals the current `gfx/interface/counters/divisions_small/onmap_unit_stone_cohorts_icon.dds` bytes.

The Forest receipt is `docs/assets/012_africa/models_3d/forest_giants/evidence/finalize_20260912/counter_parent_promotion_receipt.json`. It records `worker_runtime_mutations: false`, `runtime_byte_equality: true`, and `no_in_game_validation: true`. The staged `unit_forest_giants_icon.dds` SHA-256 `fbe279a142283186df9f61cb76a76a88ba3f6d395f181b4efcfb500e925875d9` equals the current `gfx/interface/counters/divisions_large/unit_forest_giants_icon.dds` bytes, and staged `onmap_unit_forest_giants_icon.dds` SHA-256 `6e4e4e6c0e6f785082a611f7bdea0db1b92cd537b2c5879b5a0640953d36d2bc` equals the current `gfx/interface/counters/divisions_small/onmap_unit_forest_giants_icon.dds` bytes.

This records parent visual acceptance and current runtime byte equality only; no in-game completion or live consumer validation is claimed.

## Reference and consumer audit

The matching canonical contact sheets were inspected before the individual references from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters`.

The installed consumer definition was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.

The installed large reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds` with SHA-256 `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23`.

The installed map reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` with SHA-256 `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`.

The installed large sprite is `GFX_unit_infantry_icon_medium` with `noOfFrames = 2`, and the installed map sprite is `GFX_unit_infantry_icon_medium_white` with `noOfFrames = 2`.

The large canvas is 152x42 with two 76x42 frames, and the map canvas is 60x12 with two 30x12 frames.

The sampled vanilla large normal green anchors are `(20,34,21)`, `(73,106,73)`, and `(154,175,147)`, with dominant mid green `(73,106,73)`.

The inspected map family uses a neutral grayscale treatment for the normal map frame; the selected schematic has only subpixel channel differences in the reference and is treated as neutral grayscale for the custom package.

## Stone Cohorts

Source art is retained native ImageGen alpha with a complete polearm in all four source variants.

The source hashes are:

- `source/stone_cohorts_large_normal_imagegen.png`: `97ec596fddca496956a11d8f0198662f71713558927298c1e355f341f658a565`.
- `source/stone_cohorts_large_template_imagegen.png`: `5c906090e85e0f9f1cbe24610b5f3b2c8b470fce845c1dea3526c7b9895d3127`.
- `source/stone_cohorts_map_normal_imagegen.png`: `4688541faaeb5444034477fd56afde90b50e820f72586a69a771866f35541c14`.
- `source/stone_cohorts_map_template_imagegen.png`: `cfb95545632129a4a2649eb35ef7df2c38180a5cc760e60313b2178681984c7b`.

The prompt files and prompt hashes are recorded in `stone_cohorts/counters/finalize_20260912/manifest.json` and `validation.json`.

The processed PNG hashes are:

- `processed/stone_cohorts_large_normal_76x42.png`: `cbd3b8174252f99be8e6157d8ccfd289cee2a2ee72bb319035b62f02f3039893`.
- `processed/stone_cohorts_large_template_76x42.png`: `cbd0c88aad9f9152f2a2316c8a328492d1e7c598d713b2abc9c1de946aa577a1`.
- `processed/stone_cohorts_map_normal_30x12.png`: `c59866c2cae63ba3ed16f0852a46b2450621f01a2be4298341e2ea12ef44f4f4`.
- `processed/stone_cohorts_map_template_30x12.png`: `e4e63f64877f627767de404a038a50aea5a3be6401249f50df639f2870414a98`.
- `processed/stone_cohorts_large_strip.png`: `c79125becd88d50cef1c9134c6e868748df79d463e1675318bc3136908628eb7`.
- `processed/stone_cohorts_map_strip.png`: `f9a8e638c4396e1b2d794c4ba174535de6f910c8644d206933b95ec2122ec197`.

The final candidate DDS hashes are:

- `dds/unit_stone_cohorts_icon.dds`: `d94e7bdf5baf96d113290b0e6e95dd8c2806260ac915bb928212b16ec758971d`, 25,664 bytes, 152x42.
- `dds/onmap_unit_stone_cohorts_icon.dds`: `8dc53623a47442fd5e27aeea891bad9565ae788af8b135853d4f2ee5ba8d69bb`, 3,008 bytes, 60x12.

The large frame order is `[vanilla_green_custom_polearm, selected_neutral_custom_polearm]`.

The map frame order is `[map_neutral_custom_polearm, selected_neutral_custom_polearm]`.

The large normal opaque pixels are entirely in the sampled vanilla green family, and the large schematic plus both map frames are exact grayscale after processing.

The Stone normal map frame retained 103 nontransparent pixels and 16 fully opaque pixels, so alpha coverage is unchanged. Its opaque luminance moved from `65..133` with mean `100.062` and median `102.0` to `94..236` with mean `188.562` and median `199.5`, matching the installed vanilla frame 0 opaque range and key anchors q10 `154`, q25 `175`, median `189.5`, q75 `203`, and q90 `216`. The before image is `previews/stone_cohorts_map_normal_before_grading.png` with SHA-256 `1819aba9df0ec83e0d5a5f7f1506e7870e893d00dcb954220e5f9e555955cd36`, and the native-size plus nearest 10x dark-background comparison is `previews/stone_cohorts_map_normal_dark_comparison.png` with SHA-256 `2e2665d5e0f9c757359d81d0a195e42303924aa1fbf834813dd9cda3a26e979f`.

## Forest Giants

Source art is retained native ImageGen alpha with the complete broad axe and bound-log bundle in the normal and schematic variants.

The source hashes are:

- `source/forest_giants_large_frame0_imagegen.png`: `2858c6a756820de7fd783d37ddbc9f8f073d03c7f4e4434800b18d120987f3b0`.
- `source/forest_giants_large_frame1_imagegen.png`: `0a05d16f070cf14e7b1eb4d7ff9e9277e0fc66585fa02b2ce18eea520f8c25a8`.
- `source/forest_giants_map_frame0_imagegen.png`: `bf1b39c940b2c66cdde01750a00f012a91532b005bc9abcec84cb201f753e2c0`.
- `source/forest_giants_map_frame1_imagegen.png`: `cda275d842c56818be391038db175d6b28dfb5f407761745a85a05a221c682b1`.

The prompt files and prompt hashes are recorded in `forest_giants/counters/finalize_20260912/manifest.json` and `validation.json`.

The processed PNG hashes are:

- `processed/forest_giants_large_frame0_76x42.png`: `c684fb707f73186d5fd88b87f8cee2c42ca81ba66ef2eca74c88fb4a86667cf0`.
- `processed/forest_giants_large_frame1_76x42.png`: `e63179287ade5ef2ca78624ab9155857034a8286c812c328b2ecdb00ae5dbe79`.
- `processed/forest_giants_map_frame0_30x12.png`: `bf7e049ddff5663969e2eaa7dc5370d1c5e6a04257d3ee33914e9418731df0bf`.
- `processed/forest_giants_map_frame1_30x12.png`: `2e2a177cb276420ce86fd9c64ee4f99c0f6fa5b813c4287ae0d2227846bd5d42`.
- `processed/forest_giants_large_strip.png`: `a037189a72b9c542befcb0cb4f287bc1bdb5ea11281940727723e43a13cff277`.
- `processed/forest_giants_map_strip.png`: `950c21f66f8cfe952c72db9eff8f3286aa29118d8b44de45601935f898f29311`.

The final candidate DDS hashes are:

- `dds/unit_forest_giants_icon.dds`: `fbe279a142283186df9f61cb76a76a88ba3f6d395f181b4efcfb500e925875d9`, 25,664 bytes, 152x42.
- `dds/onmap_unit_forest_giants_icon.dds`: `6e4e4e6c0e6f785082a611f7bdea0db1b92cd537b2c5879b5a0640953d36d2bc`, 3,008 bytes, 60x12.

The large frame order is `[vanilla_green_custom_axe_log, selected_neutral_custom_axe_log]`.

The map frame order is `[map_neutral_custom_axe_log, selected_neutral_custom_axe_log]`.

The source map frame 0 was colored, while the installed small-map family is neutral grayscale, so the processed map frame 0 is luminance-graded neutral grayscale and retains the axe, branch crown, and bound-log identity. The final map frame 0 and frame 1 contain zero non-grayscale pixels.

The Forest normal map frame retained 119 nontransparent pixels and 18 fully opaque pixels, so alpha coverage is unchanged. Its opaque luminance moved from `52..100` with mean `71.333` and median `72.0` to `94..236` with mean `177.944` and median `186.5`, matching the installed vanilla frame 0 opaque range and key anchors q10 `154`, q25 `175`, median `189.5`, q75 `203`, and q90 `216`. The before image is `previews/forest_giants_map_normal_before_grading.png` with SHA-256 `e43716bf9bd4c8e5b94b16b62cb22013569698ab2350a81aff82212fc1de1063`, and the native-size plus nearest 10x dark-background comparison is `previews/forest_giants_map_normal_dark_comparison.png` with SHA-256 `f8d87d9d56043fb458e812be93e36b9eac5e1870811f4957e5d4be01b953b1ff`.

## Validation and review

Both packages were processed with `process_finalize.py` and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

Both packages were audited with `validate_finalize.py`.

The validation receipts verify strict legacy BGRA8 DDS headers, exact dimensions, exact uncompressed byte lengths, alpha extrema, frame bounds, source-copy byte equality, native transparent corners, and pixel-equal DDS decode round trips.

The decoded round-trip previews are `previews/stone_cohorts_large_dds_roundtrip.png`, `previews/stone_cohorts_map_dds_roundtrip.png`, `previews/forest_giants_large_dds_roundtrip.png`, and `previews/forest_giants_map_dds_roundtrip.png`.

The native-size and enlarged review sheets are each package's `contact_sheet.png`, `previews/*_large_enlarged.png`, and `previews/*_map_enlarged.png`.

Both `manifest.json` files enumerate source paths and hashes, prompt paths and hashes, processed PNGs, DDS outputs, previews, canonical references, installed consumer references, frame contracts, palette behavior, and validation status.

Both package handoffs are in `gfx_handoff.md`.

The final status for both packages is `parent_accepted_and_promoted`; the parent-owned runtime promotion and current byte-equality checks are recorded above. No in-game completion is claimed.

## Simplifications and blockers

No new ImageGen call was required because the existing current sources passed the native-alpha and role-identity gate, and no fallback transparency repair was used.

No Meshy, geometry, rig, skeletal animation, audio, GFX edit, or gameplay edit was in scope.

No unresolved production blocker remains inside these counter packages; parent visual acceptance and runtime promotion are complete, while live in-game validation remains unclaimed by the worker boundary.
