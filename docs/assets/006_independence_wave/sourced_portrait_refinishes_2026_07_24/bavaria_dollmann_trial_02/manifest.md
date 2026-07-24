# IW-009 Bavaria Friedrich Dollmann trial 02

Status: `imagegen_safety_blocked_unwired`.

The immutable source remains the attributed 1940 Bundesarchiv photograph at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg`, SHA-256 `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`.

The explicit crop was recreated with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` at decoded-master rectangle `(300,120)-(500,450)`.

The retained lossless crop is `source_crops/BAY_friedrich_dollmann_exact_head_shoulders_300_120_500_450.png`, `200x330`, SHA-256 `D3A70235D56B6E8255AF31BD8330975BD1FC42370D1278272262EE210B9CDF97`.

The retained crop evidence is `source_crops/BAY_friedrich_dollmann_exact_head_shoulders_300_120_500_450.json`, SHA-256 `6D87A0BA4C7494069D16F16A7D58AA7D62574266629F4A431AA0F0DF861991D8`.

The evidence records `decoded_pixels_equal = true`; the decoded master rectangle and reopened crop share RGBA SHA-256 `1C910471860E2EDE9F5B446613FD419C24AFED8F60CC500337645181240FBFE9`.

The built-in ImageGen identity-preserving repaint attempt used only that exact crop and the prompt retained in `identity_repaint_prompt.md`.

ImageGen rejected the output at the safety stage with request ID `9454abe3-60fd-4828-b24a-7f908791776a`.

No raw ImageGen result, processed candidate, review sheet, DDS, sprite, gameplay, localisation, readiness, or fallback was created.

The existing Event 6 runtime portrait was not changed.

This candidate remains blocked unless a later approved source or ImageGen execution can complete the same mandatory source-locked workflow.
