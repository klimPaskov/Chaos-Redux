# Shared sprite QA and alpha repair

Run from the mod root with Python 3.9 or later.
Install dependencies with `python -m pip install -r .tools/gfx/requirements.txt`.
These tools operate only on explicitly selected paths; there is no implicit repository-wide mutation.
All repair and conversion outputs go to a separate directory for review before the asset owner installs them.

## Commands

```powershell
# Audit alpha, including every frame of a horizontal sheet.
python -B .tools/gfx/gfx.py alpha gfx/interface/goals/example.dds --json alpha.json
python -B .tools/gfx/gfx.py alpha gfx/texticons/example.dds --frames 2 --json alpha.json

# Batch input: JSON array of literal paths, or objects with a texture/path field.
python -B .tools/gfx/gfx.py alpha --list owned_paths.json --json alpha.json

# Erode one pixel of alpha, and bleed uncontaminated interior colour into edge pixels.
# The output mirrors input paths relative to --root; DDS inputs become lossless PNG previews.
python -B .tools/gfx/gfx.py defringe --list owned_paths.json --root . --out docs/plans/gfx_fix_2026-10/review --json defringe.json

# Check exact canvas, transparent margins and undersized subjects.
python -B .tools/gfx/gfx.py size gfx/interface/goals/example.dds --profile focus --json size.json
python -B .tools/gfx/gfx.py size gfx/interface/decisions/example.dds --profile category

# Compare the exact counter surface to an inspected installed-vanilla reference.
python -B .tools/gfx/gfx.py counter gfx/interface/counters/divisions_large/example.dds --surface large --reference "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds"

# Mechanical 2D DDS conversion: call the existing asset-skill writer and verify the bytes.
python -B .tools/gfx/gfx.py dds docs/plans/gfx_fix_2026-10/review/gfx/interface/goals/example.png --root docs/plans/gfx_fix_2026-10/review --out docs/plans/gfx_fix_2026-10/dds --json dds.json

# Narrowed adaptation of the review's gfx_sheets.py: all registered sprites in selected groups.
python -B .tools/gfx/gfx.py sheet --groups 015 shared_chaosx_texticons --out docs/plans/gfx_fix_2026-10/sheets --label before
```

Use the actual vanilla texture path from its `.gfx` definition; the counter command requires this explicit reference and does not guess it from a unit name.
Exit status is `0` when every requested operation/check succeeds, and `1` for findings or input errors.
JSON reports include each source hash, dimensions, per-frame alpha, visible bounds and detected chroma edge pixels.
Redirect console output to a file for large batches; `--json` writes the full structured report independently.
Existing output files are refused unless `--force` is supplied.
Non-force PNG/DDS installs use an exclusive same-directory hard link so a concurrent writer cannot silently replace another worker's output; filesystems without hard-link support fail closed.
Even `--force` cannot overwrite an input.
Input LFS pointers, unsupported images, incomplete frame widths and truncated DDS data fail rather than silently exporting a substitute.

## Alpha processing

`alpha` flags a mean below `200` across subject pixels with nonzero alpha, as required by cross-cutting rule 4.
Empty subjects also fail.
The check is per frame: a solid NATO frame cannot hide an almost invisible first frame.
Thin antialiased symbols and intentional disabled states can trigger this diagnostic and need consumer review; it is not permission to make every pixel opaque.

`defringe` is for existing transparent cut-outs with inherited key-colour contamination, not the normal production route for new art.
New icons must use native ImageGen transparency as required by the event-assets skill.
It shrinks the alpha boundary by one pixel using a zero-padded minimum filter, then extends the nearest uncontaminated opaque interior RGB into semitransparent/transparent pixels and contaminated edge pixels.
Magenta means both red and blue exceed green by more than 40; green means green exceeds red and blue by more than 40.
Interior seed pixels must have alpha at least 240 and survive a one-pixel erosion, so a key-coloured rim cannot become a source colour.
RGB bleeding does not alter alpha or subject colour inside that core.
Opaque chroma recolouring is restricted to the original two-pixel boundary band, preserving vivid green or purple paint inside the subject.
For a visually confirmed key-colour blob inside opaque artwork, `--spill-mask reviewed_mask.png` explicitly selects pixels for interior-colour bleeding; the grayscale mask must match the exact sheet dimensions, with nonzero values only at reviewed spill coordinates.
This opt-in mask does not infer a background or change alpha; retain the mask, source hash and reviewed pixel coordinates as repair evidence.
Each frame is processed separately to prevent colours bleeding across frame boundaries.
`--erosion 0` performs RGB bleeding without shrinking the silhouette when an owner has verified that erosion would damage a very small symbol.
The tool refuses empty subjects, images without transparent unused canvas, interiors too faint to supply reliable colours, and erosion that would erase the subject.
It does not remove opaque mattes, key entire images, unpremultiply colour, restore missing details or boost opacity.
Stray opaque blobs, broad glows, legitimate green objects near the edge, tiny thin lines and badly ghosted subjects need direct visual/source review.

Review the source and processed PNG on dark, light and checker backgrounds at native size and enlarged size before installing any output.
Retain source hashes and the selected processed version; do not run erosion twice on a repaired runtime export.
Recheck subject bounds, alpha and fringes after DDS decoding.
The contact sheet shows the first frame plus the declared frame count; inspect every frame separately for counter or animation acceptance.

## Slots and counter conventions

Profiles use the explicit October GFX repair plan's slot contract:

| Profile | Per-frame canvas | Minimum margin |
|---|---|---|
| focus | 94x86 | 2 px |
| decision | 34x34 | 2 px |
| category (small icon) | 52x40 | 3 px |
| idea | 64x64 | 2 px |
| report | 210x176 | none |
| news | 397x153 | none |
| counter-large | 76x42 | 1 px |
| counter-small | 30x12 | none (vanilla fills the top/bottom) |
| texticon | 18x18 | 1 px |

`category` means the small category icon, not the separate 114x101 category illustration.
The task's 34x34 decision target takes precedence over the skill's older 32x32 default.
Always inspect the actual consumer; use `--canvas W H` and `--margin N` for a verified exception.
Horizontal strips require `--frames N`; canvas width is checked against the per-frame width multiplied by N.
Margins use alpha at least 16 to disregard negligible shadow tails.
Icon span below 80% of its canvas raises an undersized-art finding; the review plan targets roughly 90% with 2–4 px margin.
There is no automatic rescaling or cropping, because that cannot recover a clipped subject.

`counter` is a conservative automated triage check, not proof that the symbol depicts the right unit.
Its default frame count is two, so the returned alpha diagnostics describe both frames separately.
Large frame 1 must follow the muted flat vanilla-green silhouette palette sampled from the supplied reference.
Small frame 1 must predominantly be light grey/white at full opacity.
Frame 2 needs an opaque pale/white NATO field with a black line glyph, distinct from frame 1.
The check catches empty/ghosted subjects, wrong canvases, broad palette mismatches, identical frames and missing white/black structure.
It also compares the largest connected pale/black field's density, footprint and rectangular aspect to vanilla, flagging scattered white/black noise and unboxed glyphs.
Counter opacity and colour-spread comparisons use the supplied reference, since actual vanilla antialiased infantry silhouettes themselves average below 200 alpha.
The separate `alpha` command still reports the requested literal 200 threshold without that adjustment.
It cannot establish a recognizable silhouette, a complete box border, the correct NATO glyph, line weight or a readable support marker; those require native-size visual comparison to the exact vanilla family.
Do not apply this counter rule to unrelated 18x18 inline texticons or division-template emblems.

## DDS contract and shared-tree installation

The 2D writer imports `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and calls its canonical `write_bgra_dds` function.
It writes a legacy 128-byte DDS header, one uncompressed straight-alpha BGRA level, pixel-format block at byte 76 with `RGB | ALPHAPIXELS`, correct BGRA masks and `DDSCAPS_TEXTURE`.
It then validates every header field, exact `128 + width * height * 4` file length, and pixel equality through both strict parsing and Pillow decoding before atomically replacing the reviewed output file.
This writer is for mechanical 2D alpha processing, under the asset skill's explicit exception; general source-art conversion still uses the canonical converter's CLI.
It is not the compressed full-mip BC1/BC3 model-texture pipeline.
It does not resize, change frame counts, generate missing art or alter `.gfx` registrations.

Before installing an output, verify the runtime path still has the recorded source hash and that the owner has not edited it since selection.
Copy only the selected reviewed files; leave unrelated assets and shared registries alone.
Keep sprite names, canvas and frame count stable; edit `.gfx` only when those must change.
Use the shared-git-commit skill to commit only owned paths/hunks with a temporary index and compare-and-swap HEAD publication.
Live consumer checks belong to the orchestrator.
