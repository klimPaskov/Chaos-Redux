# Event 32 Payload Cost Icon Handoff

Disposition: both chemical and biological production are implemented and parent-approved, and nuclear cost art reuses the exact vanilla sprite.

The parent task explicitly authorized only the two shared static cost sprites listed here and required source/processed/final files, transparent alpha, reference evidence, and a parent review.

After review, the parent preserved all 40 production evidence files under the permanent `docs/events/032_missiles/assets/payload_cost_icons/` archive, retaining relative paths and exact image/prompt bytes.
The file table below records the original production locations, which remain in the ignored active workspace until full event closure.
The permanent archive's manifest and GFX handoff use the durable paths, while submitted prompt JSON retains its actual historical input paths.

## Files Produced

| Role | Path |
| --- | --- |
| Chemical ImageGen source, rejected radiation-mark candidate | `docs/assets/032_missiles/chemical_receipt_cost_icons/source_png/cbrn_chemical_payload_texticon_imagegen_attempt_02.png` |
| Chemical selected ImageGen edit source | `docs/assets/032_missiles/chemical_receipt_cost_icons/source_png/cbrn_chemical_payload_texticon_imagegen_edit_03.png` |
| Chemical processed PNG | `docs/assets/032_missiles/chemical_receipt_cost_icons/processed_png/cbrn_chemical_payload_texticon.png` |
| Chemical runtime DDS | `gfx/texticons/cbrn_chemical_payload_texticon.dds` |
| Biological selected ImageGen edit source | `docs/assets/032_missiles/chemical_receipt_cost_icons/source_png/cbrn_biological_payload_texticon_imagegen_edit_04.png` |
| Biological processed PNG | `docs/assets/032_missiles/chemical_receipt_cost_icons/processed_png/cbrn_biological_payload_texticon.png` |
| Biological runtime DDS | `gfx/texticons/cbrn_biological_payload_texticon.dds` |
| Parent-approved chemical review sheet | `docs/assets/032_missiles/chemical_receipt_cost_icons/contact_sheet.png` |
| Current combined review sheet | `docs/assets/032_missiles/chemical_receipt_cost_icons/contact_sheet_current.png` |
| Manifest | `docs/assets/032_missiles/chemical_receipt_cost_icons/manifest.md` |
| GFX handoff | `docs/assets/032_missiles/chemical_receipt_cost_icons/gfx_handoff.md` |

Prompt records and review evidence remain under `docs/assets/032_missiles/chemical_receipt_cost_icons/prompts/` and `evidence/`.

The parent-created registry `interface/cbrn_payload_texticons.gfx` was read but not edited.

## Asset Findings

The selected chemical source came from built-in ImageGen with genuine transparency, then a targeted edit replaced a radiation trefoil with a poison warning mark while preserving the canister silhouette and canvas.

The processed chemical PNG is 30×12 RGBA, and the final DDS is a 30×12 one-level BGRA32 file whose decoded pixels exactly match the processed PNG.

The parent approved the chemical canister silhouette, muted palette, alpha, and small poison mark when paired with the exact tooltip context.

One biological prompt was refused by ImageGen with request ID `dfa3a081-163e-4bc8-bbcd-6227b56330ab`; that prompt and refusal remain in the evidence package.

The parent supplied a revised benign pictogram brief, which generated a transparent standard three-lobed symbol; a focused same-route edit simplified the strokes for the 12×12 footprint.

The biological source, processed 30×12 RGBA PNG, and one-level 30×12 BGRA DDS now exist at the exact registered path; decoded DDS pixels equal the processed PNG.

The parent inspected `contact_sheet_current.png` at native and 4× sizes and approved the biological glyph's distinct three-lobed silhouette, muted contrast, centered footprint and transparent edges.

The nuclear cost reuses the exact unmodified vanilla `GFX_unit_nuclear_missile_icon_small_texticon`; no new nuclear filename was created.

## Reference and Consumer Evidence

The exact support-equipment comparator is Chaos Redux shared content at `interface/chaosx_texticons.gfx:89-94`; its two-frame 60×12 DDS has 30×12 frames.

The exact nuclear sprite is installed vanilla content at `interface/texticons.gfx:2945-2950`; its two-frame 60×12 DDS also has 30×12 frames and is not overridden.

The three existing Event 32 value texticons at `interface/032_missiles.gfx:18-20` are 24×24 and represent other values, so none was reused for chemical or biological costs.

No exact shared chemical or biological stockpile-cost texticon was found in the bounded vanilla/Chaos Redux texticon registry and DDS audit; CBRN-named unit icons belong to another consumer family.

The canonical modifier contact sheet was inspected before the individual 30×20 Vanilla modifier reference; no visual-component layer was used.

Offline reference evidence and revisions are recorded in the asset manifest.

## Validation and Limits

The native chemical source has a genuine alpha channel, transparent corners, and complete inset subject bounds at alpha thresholds 1, 8, and 16.

Both processed PNGs retain native alpha, transparent unused canvas, exact 30×12 dimensions, and alpha range 0–255.

Both DDS headers, dimensions, BGRA masks, byte lengths, and decoded pixel equality were checked against their processed PNGs.

The parent reviewed and approved both icons and wired their cost consumers through `032_missiles_payload_cost_localisation.txt`, the English decision localisation and `interface/cbrn_payload_texticons.gfx`.
This is asset and source-wiring evidence; live decision-row fit is not established by the contact sheet.

No game was launched, and the worker did not run Git/index operations.

## Simplifications, Omissions, and Blockers

There are no omitted requested art files in this two-icon cost package.

The earlier built-in ImageGen refusals are preserved in the evidence history, and no alternate backend, background-removal fallback, local drawing, generic placeholder, reused unit icon, Event 32-only nuclear duplicate, animation, portrait, country art, model, or other icon family was created.

