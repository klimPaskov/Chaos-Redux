# Radio Service Coordinator advisor processing blocker

- Final source master: `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v10.png`
- Source SHA-256: `1bf30d1994696037ceb994e9b5ba41249faaaec1df01739cb2190b2393531362`
- Source dimensions: 1254x1254
- ImageGen handle: `exec-8103dbe6-42b9-4070-b953-faa106b01080`
- Frozen processor: `retired_advisor_card_processor_REMOVED`
- Processor SHA-256: `e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`
- Runtime: Python 3.9.12 and Pillow 11.1.0
- Attempted processed output: `processed/advisors/NZL_fallout_radio_service_coordinator.png` not created
- Attempted comparison sheet: `reviews/advisors/NZL_fallout_radio_service_coordinator_review.png` not created
- Frozen v5 result: `ValueError: No advisor candidate passes every frozen vanilla native-style band with the required margin`
- Final attempted candidates: 96
- Retained portrait candidates: 3
- Retained paper candidates: 32
- Rejections: `portrait_top_left_native_bands` 680, `portrait_background_identity` 505, `portrait_palette` 42, `paper_identity_or_palette` 18, `native_band_paper_mean` 78, `native_band_paper_std` 63, `native_band_bottom_area_variation` 96
- Closest rejected card: portrait mean `118.005392` passed its band with margin, paper mean `198.560036` failed band `[198.866806, 201.553207]` with normalized margin `-0.114194`, and bottom-area variation `16.669304` failed band `[12.158621, 15.613644]` with normalized margin `-0.305544`

No DDS was created. The radio advisor remains blocked and unwired. No fallback, threshold change, manual filtering, or substitute portrait is authorized.

## Fresh frozen-gate remediation attempts (2026-07-22)

The following genuinely new ImageGen source generations were run through the unchanged processor/evaluation contract. None produced a candidate PNG, review sheet, metadata JSON, DDS, or approval record.

| Source | SHA-256 | ImageGen handle | Crop / face box | Frozen result |
|---|---|---|---|---|
| `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v11.png` | `bc8feb7f47548d515743588fc83d9605499ef57d14118f76318b64cd2cd9a123` | `exec-6b82da98-9c11-4adf-96cd-0ff53d5a523e` | `[0,0,1254,1254]` / `[500,240,860,700]` | Rejected after 1,230 attempts: `portrait_top_left_native_bands` 580, `portrait_background_identity` 514, `portrait_palette` 36, `portrait_source_face_identity` 100. |
| `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v12.png` | `c88f4b188c0865e49f8c90e0ebe1b0093402459ff3a4a43c1e731eddade2a055` | `exec-fb38ffc5-4f38-4572-91e1-4836e25f9c0d` | `[0,0,1254,1254]` / `[430,250,800,700]` | Rejected after 192 final attempts. Closest card passed paper and portrait-family gates but failed the required 0.03 interior margin only at `bottom_area_variation`: value `15.567252`, band `[12.158621,15.613644]`, normalized margin `0.013427` (required `>= 0.03`). Other closest metrics: top-frame variation `17.061062`, left-rail variation `19.418113`, left-rail mean `50.312467`, left-rail std `35.486381`, paper mean `200.236964`, paper std `28.194299`, paper samples `851`, portrait mean `102.811410`. |
| `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v13.png` | `dca6aecfe6a27c2f769c00f908af33de0ef0161ab1874679885e601ce2f342f3` | `exec-61750235-4238-493d-acb3-a5ae722cefe2` | `[0,0,1254,1254]` / `[430,240,810,700]` | Rejected after 1,230 attempts: `portrait_top_left_native_bands` 541, `portrait_background_identity` 589, `portrait_palette` 100. |

All attempts used Python 3.9.12, Pillow 11.1.0, processor SHA `e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`, render configuration SHA `e9f8d54d1ea7fc8845bf22675c09686acc7196556a56f96f5a1b46268b134637`, the manifest-pinned advisor overlays, and the unchanged six-reference alpha/paper-family hashes. The blocker is retained; no thresholds were relaxed and no fallback or substitute portrait was created.

Review contact sheet: `reviews/advisors/NZL_fallout_radio_service_coordinator_remediation_contact_sheet.png` (v10 through v13 source alternatives; review evidence only, not a runtime asset).

## Authorized v14 remediation attempt (2026-07-22)

- Source: `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v14.png`
- Source SHA-256: `a1085e9c2839f740b6f34deab8f587ffc8333bf6f787507f299294d42014a342`
- ImageGen handle: `exec-1889068a-b52e-470a-bc47-24a657c5b8bf`
- Generation mode: ImageGen edit of the approved v12 identity/composition reference; v12 input SHA `c88f4b188c0865e49f8c90e0ebe1b0093402459ff3a4a43c1e731eddade2a055`
- Crop / face box: `[0,0,1254,1254]` / `[430,250,800,700]`
- Frozen processor result: no candidate passed every native-style band with required margin after `480` final attempts; retained portrait candidates `15`, paper candidates `32`.
- Rejections: `portrait_top_left_native_bands` `660`, `portrait_background_identity` `555`, `paper_identity_or_palette` `18`, `native_band_paper_mean` `318`, `native_band_paper_std` `330`, `native_band_bottom_area_variation` `230`, `native_band_portrait_mean` `352`, `native_band_paper_samples` `130`.
- Closest rejected card: top-frame variation `16.786007`, left-rail variation `19.753292`, left-rail mean `50.506289`, left-rail std `35.892537`, paper mean `198.848766` vs band `[198.866806,201.553207]` (normalized margin `-0.006715`), paper std `28.367895`, paper samples `848`, portrait mean `106.263591`, bottom-area variation `15.683616` vs band `[12.158621,15.613644]` (normalized margin `-0.020252`); minimum margin `-0.020252`.

No v14 candidate PNG, review sheet, metadata JSON, approval record, DDS, or sprite wiring was created. The frozen processor, thresholds, overlays, crop, face box, runtime, and render configuration were not changed. No fallback or manual adjustment is authorized.
