# Radio Service Coordinator advisor processing blocker

- Final source master: `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v10.png`
- Source SHA-256: `1bf30d1994696037ceb994e9b5ba41249faaaec1df01739cb2190b2393531362`
- Source dimensions: 1254x1254
- ImageGen handle: `exec-8103dbe6-42b9-4070-b953-faa106b01080`
- Frozen processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
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
