# The Missing Patrol asset manifest

This is a dedicated Fallout report image for the missing-patrol chain. It does not reuse zombie ids, files, sprites, audio, or paths.

| Stage | Path | Format and evidence |
|---|---|---|
| Source | `source/fallout_missing_patrol_source.png` | 1672 by 941 RGB generated source |
| Processed | `processed/report_event_fallout_missing_patrol.png` | 210 by 176 RGBA report card |
| Preview | `previews/report_event_fallout_missing_patrol.png` | Review copy of the processed card |
| Runtime | `runtime/report_event_fallout_missing_patrol.dds` | One level uncompressed 32 bit BGRA DDS |
| Mod copy | `gfx/event_pictures/fallout_world_end/report_event_fallout_missing_patrol.dds` | Runtime copy used by the sprite |

The source SHA-256 is `560890D3ABDCF2D9ED46E844480CFB39E31F8F778238C9D44380D7B2104B7E0D`.

The processed PNG SHA-256 is `A8F9174CE60927FD3A3EC40364801AC0A76BDA83C40777D3A2F8FE37F42E669D`.

The runtime and mod DDS SHA-256 is `6756020068247307151C80193970767E2016787C34AEF27530458223701BDED3`.

The processed card used `process_report_event_image.py` and the DDS used the approved `convert_to_dds.py` DirectXTex backend. The asset is not wired to the blackout GUI because this chain is an ordinary delayed Fallout memory event.
