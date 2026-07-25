# The Men at Kilometer Twelve asset manifest

This is a dedicated Fallout report image for the armed checkpoint chain. It does not reuse zombie ids, files, sprites, audio, or paths.

| Stage | Path | Format and evidence |
|---|---|---|
| Source | `source/fallout_men_at_km12_source.png` | 1369 by 1149 RGB generated source |
| Processed | `processed/report_event_fallout_men_at_km12.png` | 210 by 176 RGBA report card |
| Preview | `previews/report_event_fallout_men_at_km12.png` | Review copy of the processed card |
| Runtime | `runtime/report_event_fallout_men_at_km12.dds` | One level uncompressed 32 bit BGRA DDS |
| Mod copy | `gfx/event_pictures/fallout_world_end/report_event_fallout_men_at_km12.dds` | Runtime copy used by the sprite |

The source SHA-256 is `5BD9D27C9EB58D1DC850EC5726BD17FB6166DAB3D076C88A1CB58EFF3EAAFCD1`.

The processed PNG SHA-256 is `ED5D0E1C42D1D847F777469C18C1C85DDC6D9B84786A02834712BFC25BD0DB13`.

The runtime and mod DDS SHA-256 is `EC772C1AAC6FBBB9C1FF09F1AA3AC21F35C5123DAC48A381A3A20E9F2AF512A7`.

The processed card used `process_report_event_image.py` and the DDS used the approved `convert_to_dds.py` DirectXTex backend. The asset is not wired to the blackout GUI because this chain is an ordinary delayed Fallout memory event.
