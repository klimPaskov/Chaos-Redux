# The Captain Refuses asset manifest

This is a dedicated Fallout report image for the command-fracture chain. It does not reuse zombie ids, files, sprites, audio, or paths.

| Stage | Path | Format and evidence |
|---|---|---|
| Source | `source/fallout_captain_refuses_source.png` | 1672 by 941 RGB generated source |
| Processed | `processed/report_event_fallout_captain_refuses.png` | 210 by 176 RGBA report card |
| Preview | `previews/report_event_fallout_captain_refuses.png` | Review copy of the processed card |
| Runtime | `runtime/report_event_fallout_captain_refuses.dds` | One level uncompressed 32 bit BGRA DDS |
| Mod copy | `gfx/event_pictures/fallout_world_end/report_event_fallout_captain_refuses.dds` | Runtime copy used by the sprite |

The source SHA-256 is `662DC7B458D703C8B6E7FA836145636101EF5E916A949CAD2334CCEDB3EB5973`.

The processed PNG SHA-256 is `0265124EF75E3DBB758C0C489E7453371291D54C6365BC40DB51AE7C3B36E3CE`.

The runtime and mod DDS SHA-256 is `AF44539F129DF9908E4B24A744B539FF98847DF18D595D2CC0F1CED2BBFE97E0`.

The processed card used `process_report_event_image.py` and the DDS used the approved `convert_to_dds.py` DirectXTex backend. The asset is not wired to the blackout GUI because this chain is an ordinary delayed Fallout memory event.
