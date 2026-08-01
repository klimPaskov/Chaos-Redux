# Fallout False Positive asset manifest

This package owns the dedicated report image for the dormant Quarantine chain False Positive.

| Consumer | Visual role | Source and processed files | Runtime texture | Sprite and event consumers |
|---|---|---|---|---|
| `691.false_positive.report_event` | Quarantine clerks compare a mistaken red seal with the corrected register while a cleared household waits at a frost gate | `source_png/report_event_fallout_false_positive_source.png` to `processed_png/report_event_fallout_false_positive.png` | `gfx/event_pictures/fallout_false_positive/report_event_fallout_false_positive.dds` | `GFX_report_event_fallout_false_positive`, events 691, 693, and 695 |

- Asset name: `report_event_fallout_false_positive`
- Intended in-game use: `210x176` Fallout report-event card for False Positive
- Source SHA-256: `f2f0017e7157f78c08e4b907fba8b3b76b931c6a1c03e5e94e403a3aefeba27e`
- Processed SHA-256: `f74ccc8522168ae9a0c3e3ad0115744e0388a4827495248af891ff2a92e56a9d`
- Final DDS SHA-256: `d282099a6ccc04961ae3f8e6da2796d089b5b629401fa23f99e7692dab02127b`
- Final DDS format: legacy one-level uncompressed BGRA, 32-bit, `210x176`, 128-byte header, exact length `147968` bytes
- Sprite name: `GFX_report_event_fallout_false_positive`
- Sprite registration: `interface/fallout_world_end.gfx`
- Runtime texture path: `gfx/event_pictures/fallout_false_positive/report_event_fallout_false_positive.dds`

The source was generated with the approved image workflow. It contains no baked text, real-world insignia, or reused First Red Line art. The processed crop is a direct cover fit to the report card dimensions. The final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The event chain remains dormant because the Fallout scheduler is not activated in this tranche. Hearts of Iron IV was not launched, so player-visible presentation remains unproven.
