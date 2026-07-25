# Ashline Firebreak asset manifest

| Artifact | Path | Role |
| --- | --- | --- |
| Generated source | `docs/assets/air_cleanliness_fallout/fallout_ashline_firebreak/fallout_ashline_firebreak_source.png` | Provider source for a fictional ash aftermath report image |
| Processed source | `docs/assets/air_cleanliness_fallout/fallout_ashline_firebreak/fallout_ashline_firebreak_processed.png` | Cropped and resized 210 by 176 review image |
| Runtime report picture | `gfx/event_pictures/fallout_world_end/report_event_fallout_ashline_firebreak.dds` | Uncompressed 32 bit BGRA report picture |
| Sprite | `GFX_report_event_fallout_ashline_firebreak` | `interface/fallout_world_end.gfx` registration |

The source was generated for fictional Fallout presentation. It contains no real person, flag, attested insignia, text, or borrowed zombie asset. The natural-disaster source helper remains the sole owner of the low capped Air Contamination contribution.

The runtime DDS was produced through the repository converter at 210 by 176. The available local conversion backend used the converter's BGRA ffmpeg path because no DirectXTex executable was present in the configured workspace. This is recorded as an asset-processing simplification and does not change the report-picture dimensions or runtime path.

SHA256 evidence:

- Source PNG: `7C9380968E4DDC619D22B236714061AECEBE3237D010CDDE712BBB6B6A746D69`
- Processed PNG: `BF0610DC6E26589BD0659EC33A2BB9AA8334A0C6F10C422EE5F091DDAF6990BA`
- Runtime DDS: `22930F137F69AC267917EAA6E0E228CD03289455914F97FEB46A067AE2D12488`
