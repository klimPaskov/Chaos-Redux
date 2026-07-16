# Event 006 generated event-scene manifest

## Coverage

This manifest owns ASSET-001 through ASSET-006 only. ASSET-007 through ASSET-038 are owned by the separate icon-art package. No flag, portrait, animation, achievement, UI, gameplay, localisation, `.gfx`, or `.gui` file is part of this tranche.

All six scenes are generated fictional or alternate-history documentary art. Generation is the correct source mode because the depicted Event 006 moments do not correspond to a real photograph and contain no real-person likeness. The production prompts are preserved in `prompts/generated_event_scenes.md`.

| Asset | Use | Source PNG | Processed PNG | Final DDS | Size | Proposed sprite | Status |
|---|---|---|---|---|---:|---|---|
| ASSET-001 | Wave summary report | `source_png/event_pictures/report_event_006_asset_001_wave_summary_source.png` | `processed_png/event_pictures/report_event_006_asset_001_wave_summary.png` | `gfx/event_pictures/006_independence_wave/report_event_006_asset_001_wave_summary.dds` | 210x176 | `GFX_report_event_006_asset_001_wave_summary` | handed_off |
| ASSET-002 | Host crisis report | `source_png/event_pictures/report_event_006_asset_002_host_crisis_source.png` | `processed_png/event_pictures/report_event_006_asset_002_host_crisis.png` | `gfx/event_pictures/006_independence_wave/report_event_006_asset_002_host_crisis.dds` | 210x176 | `GFX_report_event_006_asset_002_host_crisis` | handed_off |
| ASSET-003 | First recognition report | `source_png/event_pictures/report_event_006_asset_003_first_recognition_source.png` | `processed_png/event_pictures/report_event_006_asset_003_first_recognition.png` | `gfx/event_pictures/006_independence_wave/report_event_006_asset_003_first_recognition.dds` | 210x176 | `GFX_report_event_006_asset_003_first_recognition` | handed_off |
| ASSET-004 | League congress news | `source_png/event_pictures/news_event_006_asset_004_league_congress_source.png` | `processed_png/event_pictures/news_event_006_asset_004_league_congress.png` | `gfx/event_pictures/006_independence_wave/news_event_006_asset_004_league_congress.dds` | 397x153 | `GFX_news_event_006_asset_004_league_congress` | handed_off |
| ASSET-005 | League formation super-event | `source_png/super_events/super_event_006_asset_005_league_formation_source.png` | `processed_png/super_events/super_event_006_asset_005_league_formation.png` | `gfx/super_events/006_independence_wave/super_event_006_asset_005_league_formation.dds` | 457x328 | `GFX_super_event_006_asset_005_league_formation` | registered, runtime held |
| ASSET-006 | Revisionist milestone super-event | `source_png/super_events/super_event_006_asset_006_revisionist_milestone_source.png` | `processed_png/super_events/super_event_006_asset_006_revisionist_milestone.png` | `gfx/super_events/006_independence_wave/super_event_006_asset_006_revisionist_milestone.dds` | 457x328 | `GFX_super_event_006_asset_006_revisionist_milestone` | registered and wired to slot 24 |

## Processing record

- ASSET-001 through ASSET-003 were processed with the prescribed repo-skill tool `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, using its standard 210x176 card treatment and deterministic seeds 6001, 6002, and 6003. The outputs are sepia black-and-white RGBA cards with subtle tilt, soft shadow, and transparent corners.
- ASSET-004 was center-cropped to 397x153, converted to black and white, contrast-adjusted, and given deterministic period press grain with FFmpeg.
- ASSET-005 and ASSET-006 were center-cropped to 457x328 with Lanczos resampling and restrained contrast/saturation normalization with FFmpeg.
- All six final files were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to one-level legacy uncompressed 32-bit BGRA DDS.
- `contact_sheets/generated_event_scenes_source_contact_sheet.png` shows every source.
- `contact_sheets/generated_event_scenes_final_dds_decoded_contact_sheet.png` shows every final DDS after decoding, with report transparency composited over a neutral paper color for review.
- `dds_decoded_png/` contains the decoded review copies used for pixel comparison.

## Validation evidence

All six DDS files have the required 128-byte legacy header, declared dimensions, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, and exact byte length. ASSET-001 through ASSET-003 contain alpha from 0 to 255 and have transparent corner pixels. ASSET-004 through ASSET-006 are intentionally opaque. Every DDS-decoded image is pixel-identical to its processed PNG.

Visual review confirmed that the three report cards preserve their central subject after tilt and crop; the news image remains readable at 397x153; both super-event images retain their central action and period setting at 457x328. No scene contains readable generated text, a modern object, a real-person likeness, or a real flag copied as a fictional state identity.

## SHA-256 record

| Asset | Source SHA-256 | Processed SHA-256 | DDS SHA-256 |
|---|---|---|---|
| ASSET-001 | `1a536eba8854331fa3119094f15432c5268cae63e2499c69fcdd73ad43a50801` | `fc9b7c44deeefac21ae6dafd4672ecec7d52d5e4b1ccfa5b2889adf37c9718ef` | `639dcff0f332221d69f23de4197e8aa679544e1151f10eeadcaacd788846f2f2` |
| ASSET-002 | `96d110574182bb83749c9ea9a5304d92c3c0fc73c58ec1f6fb3056233303116d` | `260d01723f797e16947df191e91e2f5caa9fbe8fdcd435987b65dc64944b01e8` | `7292256c6b389a83d56853ad3f27edcf0ac033469bfd2efdfa8c5318c01ed3c6` |
| ASSET-003 | `d4502cba12b34ad7802f83a8e6630ffe5d2690ed2769487815541b9b265a4837` | `5cbd9e4cdf54e3abd277c0fa0e36032b6510a694ff7ad2b45c12ff37fbb59a78` | `664a21255d874a675b9b8365858ee93d4d4e8b2cec055291352dc6e5f298b230` |
| ASSET-004 | `7f11bae7083ba0044ace8ac3de8214c2cdc031f63313f68a380fe44e37364781` | `981f45f949887f14b6ebf6bc319f36e8c9596a41a72e677e652f7756ac36fb03` | `794d5a720bec58837a18f044dffac84bb6cf69b72d956d792ec5b3f67792b14e` |
| ASSET-005 | `ae05125f6441b35f32f7ba59545ceca9e745d06555557b98cd68768746d5d54e` | `4c21ff34255a9727dd3ad0379fbdbd6239a07735b8220051efc25b2a929cd3af` | `e9f4a4f24d7f134e8bd3ef04724a7a04b020f0d9dc559c3c0928ac464cd79781` |
| ASSET-006 | `52be9c45e6f5a09c03eb15fdf4932769212993b2d62dca494cc9334c4b67d67d` | `bb246b65d72dfa40001f1cf031aeeb27ea8c6bca6f1141b08e51f8a1f52ba876` | `a7abec9c821a709bbd6412b2904db6124e59914d739f79944cf0fd40d5187542` |

## Wiring state

All six sprites are registered in `interface/006_independence_wave_event_pictures.gfx`. ASSET-001 is the committed wave report and ASSET-006 is the runtime image for dangerous milestone slot 24. ASSET-005 stays registered as the static final asset for the accepted league-formation package, but that package remains absent from runtime while audio 6001 is blocked. Do not rename the files without updating the interface registry, scripted-localisation dispatch, and source/processed records.
