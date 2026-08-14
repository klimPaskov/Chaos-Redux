# IW-047 Mari El generated route flag asset handoff

Date: 2026-08-14

Owner scope: flat generated route flag production and evidence only. No gameplay, localisation, `.gfx`, central attestation, Join, country, cosmetic registry, focus, decision, event, or workbook files were edited.

## Completion

The four explicitly approved route tags are complete:

- `MEL_INDEPENDENCE_WAVE_CIVICX`
- `MEL_INDEPENDENCE_WAVE_FORESTX`
- `MEL_INDEPENDENCE_WAVE_SOCIALISTX`
- `MEL_INDEPENDENCE_WAVE_EMERGENCYX`

Each has a distinct native ImageGen master, prompt record, processed PNG, normal 82x52 / medium 41x26 / small 10x7 bottom-left-origin TGA ladder, copied runtime TGA files, standard BGRA DDS evidence, and native-size comparison contact sheet.

## Runtime outputs

- `gfx/flags/MEL_INDEPENDENCE_WAVE_{CIVICX,FORESTX,SOCIALISTX,EMERGENCYX}.tga`
- `gfx/flags/medium/MEL_INDEPENDENCE_WAVE_{CIVICX,FORESTX,SOCIALISTX,EMERGENCYX}.tga`
- `gfx/flags/small/MEL_INDEPENDENCE_WAVE_{CIVICX,FORESTX,SOCIALISTX,EMERGENCYX}.tga`

No `MEL.tga` no-suffix override exists and the vanilla `MEL_{communism,democratic,fascism,neutrality}` ladder remains untouched. Country flags use tag/ideology filename lookup; no `.gfx` snippet is needed.

## Evidence package

`docs/assets/006_independence_wave/iw047_mari_flags_2026_08_14/`

- `manifest.md`: source mode, alternate-history boundary, route crosswalk, visual notes, preservation limits, and status.
- `gfx_handoff.md`: exact runtime paths and parent wiring limits.
- `source_png/`: four byte-preserved ImageGen masters.
- `prompts/`: route prompt records.
- `processed_png/` and `processed_tga/`: mechanical ladder outputs.
- `dds_evidence/`: 12 standard-converter DDS outputs.
- `contact_sheets/flag_ladders_contact_sheet.png`: master + normal/medium/small comparison.
- `validation/qa_results.json`: complete TGA/DDS header, dimension, opacity, and round-trip evidence.
- `validation/processing_metadata.json`: source sizes and output records.
- `hashes/sha256.txt`: source and processed hashes.

## QA result

TGA: 12/12 pass exact dimensions, type-2 uncompressed 24-bit BGR headers, bottom-left origin, exact length, opaque RGB, and decoded PNG equality. DDS: 12/12 pass standard legacy 128-byte BGRA headers/masks, texture caps, exact payload lengths, dimensions, opaque alpha, and ffmpeg decoded round-trip equality.

## Historical classification

Research found no defensible neutral 1936 Mari El flag; the designs are explicitly `alternate_history_synthesis` route identities. They must not be described as an attested 1936 state flag or used to replace the vanilla base/ideology ladder.

## Parent next action

Wire these exact route tag filenames only within the parent-owned IW-047 package after admission and origin/attestation gates remain active. DDS outputs are evidence-only; runtime lookup consumes the TGA basenames.
