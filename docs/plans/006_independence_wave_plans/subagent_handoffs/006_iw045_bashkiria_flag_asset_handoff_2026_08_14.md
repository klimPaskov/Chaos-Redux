# IW-045 Bashkiria generated route flag asset handoff

Date: 2026-08-14

Owner scope: generated non-icon flat route flag assets only. No gameplay, localisation, cosmetic registry, central adapter/attestation/Join, `.gfx`, event, country, focus, or spreadsheet files were edited.

## Completion

The four requested route families are complete as asset packages and ready for parent-owned route wiring:

- `BSK_INDEPENDENCE_WAVE_CIVICX`
- `BSK_INDEPENDENCE_WAVE_AGRARIANX`
- `BSK_INDEPENDENCE_WAVE_SOCIALISTX`
- `BSK_INDEPENDENCE_WAVE_EMERGENCYX`

Each has a byte-preserved parent-supplied native ImageGen master, reconstructed prompt record, center-cropped processed PNG, normal 82x52 / medium 41x26 / small 10x7 PNG and bottom-left-origin 24-bit TGA ladder, standard-converter BGRA DDS evidence at all three sizes, source/output hashes, and native-size comparison sheet.

## Runtime files copied

- `gfx/flags/BSK_INDEPENDENCE_WAVE_{CIVICX,AGRARIANX,SOCIALISTX,EMERGENCYX}.tga`
- `gfx/flags/medium/BSK_INDEPENDENCE_WAVE_{CIVICX,AGRARIANX,SOCIALISTX,EMERGENCYX}.tga`
- `gfx/flags/small/BSK_INDEPENDENCE_WAVE_{CIVICX,AGRARIANX,SOCIALISTX,EMERGENCYX}.tga`

Country flags use tag/ideology filename lookup, so no `.gfx` sprite definition is proposed. Parent must wire cosmetic tags only after the IW-045 route and adapter/origin gates are admitted.

## Runtime ownership\n\nOnly the TGA ladders copied under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` are runtime outputs. The DDS files remain evidence-only in the temporary package.\n\n## Evidence package

`docs/assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/`

- `manifest.md`: source mode, identity boundary, requirement-to-runtime crosswalk, visual notes, status, and QA references.
- `gfx_handoff.md`: exact runtime paths and wiring limits.
- `source_png/`: four supplied ImageGen masters copied without modifying the originals.
- `prompts/`: route-specific reconstructed visual brief records and inventories. The original ImageGen prompts were not supplied; records do not claim verbatim prompt text.
- `processed_png/`, `processed_tga/`: mechanical crop/resize/export ladders.
- `dds_evidence/`: 12 DDS outputs from `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- `contact_sheets/flag_ladders_contact_sheet.png`: each master plus normal, medium, and small exports for visual review.
- `validation/qa_results.json`: 12/12 TGA and 12/12 DDS passes.
- `validation/runtime_tga_dimensions.txt`: runtime file dimensions and decoded modes.
- `validation/processing_metadata.json`: source sizes, crop boxes, and output metadata.
- `hashes/sha256.txt`: retained source and processed PNG/TGA SHA-256 ledger.

## Identity and historical boundary

There is no attested neutral 1936 Bashkiria flag in the retained research. These four designs are generated alternate-history route symbols and must not be described as a historical 1936 flag. No no-suffix `BSK.tga` was created; no installed vanilla `BSK_{communism,democratic,fascism,neutrality}` file was replaced. The package does not reuse the 1918 Bashkurdistan reconstruction or Soviet Bashkir ASSR institutional designs as runtime art.

## QA details

The TGA files use uncompressed true-colour type 2, 24-bit BGR payloads, bottom-left origin (`descriptor=0`), exact lengths, and decoded RGB equality against processed PNGs. DDS outputs pass the repository standard legacy 128-byte header, 32-bit BGRA masks (`0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`), texture caps, exact lengths, declared dimensions, and ffmpeg pixel round-trip equality.

## Parent next action

Wire the exact four route tag filenames in the parent-owned country/cosmetic surfaces only after the IW-045 BSK package is admitted and the existing fail-closed origin/attestation gates remain active. Keep the temporary `docs/assets/` package while the event is active; promote durable facts before any eventual event-workspace cleanup. Do not stage or commit this handoff from the subagent.

