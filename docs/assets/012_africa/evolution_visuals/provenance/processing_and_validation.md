# Event 012 Africa Evolution Visual Processing and Validation

## Processing record

The three incident sources were processed with the repository's canonical report-event processor:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py <source_png> <processed_png>
```

The default deterministic contract produced a 210 x 176 transparent canvas, 192 x 153 image card, 4-degree tilt, soft drop shadow, monochrome/sepia treatment, restrained grain, and fixed seed 1337.

The three revised institutional portraits were scaled from their near-matching 1080-1081 x 1455-1456 source aspects to exact 156 x 210 output with Lanczos resampling:

```powershell
ffmpeg -loglevel error -y -i <source_png> -vf "scale=156:210:flags=lanczos" -frames:v 1 <processed_png>
```

The source aspect remains close to the registered portrait aspect, so the exact resize does not introduce a perceptible compositional change.

All six final textures were created with the repository's canonical converter:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed_png> --output <registered_dds> --width <width> --height <height>
```

## Validation method

Each DDS was audited for:

- `DDS ` magic and 124-byte legacy header;
- exact registered width and height;
- 32-byte pixel-format block, flags 65, no FourCC, and 32 bits per pixel;
- BGRA masks `00ff0000`, `0000ff00`, `000000ff`, and `ff000000`;
- `DDSCAPS_TEXTURE` and no mipmaps;
- exact payload length of `128 + width x height x 4` bytes;
- expected alpha range: 0-255 for report cards and 255-255 for opaque portraits;
- successful FFmpeg decode; and
- exact RGBA pixel equality between the processed PNG and decoded DDS.

Every test passed for all six assets. Exact results and SHA-256 hashes are in `../validation/evolution_visuals_validation.tsv`.

## Visual validation

The source, processed, and decoded output of every asset is shown in `../contact_sheets/evolution_visuals_source_processed_dds_contact_sheet.png`. The review is recorded in `../contact_sheets/contact_sheet_review.md`.
