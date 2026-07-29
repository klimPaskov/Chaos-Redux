# Provenance: Event 012 Africa priority-member report art

## Source mode and reference basis

All four images are original fictional/alternate-history scenes generated with the official built-in `$imagegen` workflow on 2026-07-29.

Generation was chosen because the brief calls for bespoke invented polities, negotiations, consensual border settlement, and an agreed departure, none of which require a real person, real event, or verifiable archival photograph.

The matching canonical family inspected before generation was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`, specifically `README.md`, `CATALOG.md`, and `contact_sheet.png` with the five period report references.

The generated scenes use period-authentic 1936–1945 clothing, architecture, props, surveying tools, frontier equipment, and restrained hand-painted press-illustration texture while excluding modern objects, readable generated text, watermarks, UI, caricature, and combat substitutes.

## Generation records

| Asset | Built-in ImageGen output evidence | Prompt record | Source SHA-256 |
| --- | --- | --- | --- |
| `report_event_012_africa_priority_member_political_settlement` | `C:\Users\klimp\.codex\generated_images\019fad9b-5ee9-72a0-a76a-066f738c1b30\exec-0cb05f7a-3348-40e9-92d4-9a7d289e897f.png` | `prompts/report_event_012_africa_priority_member_political_settlement.txt` | `bb8296a2022dfb5e9aa031de70300bb3c31928048d6a6f0c71b9a71f4df8b828` |
| `report_event_012_africa_priority_member_league_bargain` | `C:\Users\klimp\.codex\generated_images\019fad9b-5ee9-72a0-a76a-066f738c1b30\exec-a42ff143-6c27-4719-8604-93f30f223128.png` | `prompts/report_event_012_africa_priority_member_league_bargain.txt` | `ff8badffe118011c0b52c667c35b2764d0f5609332264bfd6f0bb0be20e30b9f` |
| `report_event_012_africa_priority_member_overlap_settlement` | `C:\Users\klimp\.codex\generated_images\019fad9b-5ee9-72a0-a76a-066f738c1b30\exec-0f6e455a-25e3-4d96-9f5b-2e9b759caba8.png` | `prompts/report_event_012_africa_priority_member_overlap_settlement.txt` | `6990aa64d42648a5849a27ec53495f4d96858749e0c7025976aff9fbe0d5da68` |
| `report_event_012_africa_priority_member_departure` | `C:\Users\klimp\.codex\generated_images\019fad9b-5ee9-72a0-a76a-066f738c1b30\exec-be75b6b5-d194-4a64-a370-a2065747607b.png` | `prompts/report_event_012_africa_priority_member_departure.txt` | `b4ecf67938404df53a8594f78aa4875bf17d039a46b744d2983ecdeeac957112` |

The built-in generator output remains in its default Codex evidence folder and is copied byte-for-byte into this package's `source_png/` shelf before deterministic processing.

## Processing and conversion record

Each source PNG was center-fitted to 350x240 with Pillow `ImageOps.fit`, using Lanczos resampling and RGB output, and retained in `processed_png/`.

Each processed PNG was converted with `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <final.dds> --width 350 --height 240`.

Each DDS was reopened with Pillow and decoded to `validation/decoded_png/` for dimension and visual evidence.

The validation record confirms legacy one-level uncompressed BGRA headers, exact 350x240 dimensions, exact 336128-byte payload lengths, `DDSCAPS_TEXTURE`, BGRA masks, and alpha extrema 255/255 for all four opaque report pictures.

No internet source, real-person likeness, historical flag claim, or licensing attribution applies to these fictional generated scenes.
