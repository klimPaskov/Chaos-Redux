# IW-184 California/HBX civic convention chair source manifest

Status: `sourced` and source-clearance `PASS`; this package is not promoted to runtime and intentionally contains no ImageGen repaint, processed `156x210` candidate, DDS, `.gfx` edit, or gameplay edit.

## Requirement

The fictional working identity `HBX_independence_wave_civic_convention_chair` / Daniel Mercer requires one real, male Californian civic or state figure who was alive and active in the 1936 setting and is plausible as a constitutional-convention chair.

Selected candidate: William Dennison Stephens (usually styled William D. Stephens), former California governor and Los Angeles civic leader.

Identity classification: `grounded_source_only`.

Source mode: attributed archival photograph from the Library of Congress George Grantham Bain Collection.

Gender constraint: male-presenting; no female source or substitute was considered.

## Selected source

| Field | Evidence |
| --- | --- |
| Archive/object URL | [Library of Congress item 2014715011](https://www.loc.gov/pictures/item/2014715011/) |
| Persistent handle | [hdl.loc.gov/loc.pnp/ggbain.34859](https://hdl.loc.gov/loc.pnp/ggbain.34859) |
| Direct unchanged download used | [34859v.jpg](https://cdn.loc.gov/service/pnp/ggbain/34800/34859v.jpg) |
| Secondary identity cross-check | [Wikimedia Commons file record](https://commons.wikimedia.org/wiki/File:William_D._Stephens_LCCN2014715011_(cropped).jpg) labels the subject "William D. Stephens, Governor of California" and maps back to LOC LCCN 2014715011; the Commons copy is not used as the retained master. |
| Retrieval date | 2026-07-24 (UTC) |
| Catalog title | `Wm. D. Stephens` |
| Creator/publisher | Bain News Service, publisher |
| Collection/repository | George Grantham Bain Collection, Library of Congress Prints and Photographs Division, Washington, D.C. |
| Catalog date | Between circa 1920 and circa 1925; LOC page also exposes `dc.date=1920`. |
| Physical source | One glass negative, 5 x 7 inches or smaller; LOC reproduction `LC-DIG-ggbain-34859`. |
| Rights/publication basis | LOC item rights advisory: "No known restrictions on publication"; the record links the [Bain Collection rights guidance](https://www.loc.gov/rr/print/res/274_bain.html). This is a repository rights advisory, not a claimed Creative Commons license. |
| Source-era fit | A contemporary interwar portrait of a former California governor, period clothing and studio photographic treatment, with no modern objects or reenactment cues. |

The unchanged source master is retained at `docs/assets/006_independence_wave_california_civic_source_clearance/source_png/william_stephens_loc_master.jpg`.

Master dimensions are `743x1024`, decoded mode `L`, file size `111194` bytes, and SHA-256 `5ba60d2fd0fab9a0dcf6a47b08a89bed486e35e5c14fc200c7fc6204b8652b5d`.

The source master is the exact LOC-served JPEG from the direct download URL and has not been resized, retouched, recoloured, enhanced, or overwritten.

## Identity and role evidence

The [California State Library Governors' Gallery entry for William Stephens](https://governors.library.ca.gov/24-Stephens.html) records his California governorship as `1917-1923`, birth in 1859, death in Los Angeles on April 24, 1944, his prior service as U.S. Congressman and lieutenant governor, and his service as director of the Los Angeles Chamber of Commerce from 1902 to 1911.

That state-library record establishes a real Californian state and civic officeholder who was alive in 1936 and whose gubernatorial and chamber leadership make a fictional constitutional-convention chair assignment plausible without asserting that he chaired a real 1936 convention.

The LOC object title, collection record, and source image identify the photographed subject as `Wm. D. Stephens`; the state-library record supplies the California office chronology, and the secondary Commons record supplies the expanded `William D. Stephens` form. The Commons copy is identity cross-check evidence only and is not used as the retained master.

## Exact source crop and equality proof

The explicit head-and-shoulders crop was made with the repository Pillow utility, not ffmpeg or ImageMagick.

Command:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
  docs/assets/006_independence_wave_california_civic_source_clearance/source_png/william_stephens_loc_master.jpg `
  docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders.png `
  --crop 75 130 685 940 `
  --metadata docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders_crop.json
```

| Crop artifact | Value |
| --- | --- |
| Crop box | `[75, 130, 685, 940]` in half-open Pillow coordinates |
| Crop dimensions | `610x810` |
| Crop PNG path | `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders.png` |
| Crop PNG size | `274399` bytes |
| Crop PNG SHA-256 | `d87f5fe6773844b597a4a1175dd26a6016a5a9df87a6295ce074f92d33ea2085` |
| Crop metadata path | `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders_crop.json` |
| Crop metadata SHA-256 | `4e7c4625a712eb55931902e004cfe316bedf0db96db437ad7c5da5c71c55f7b0` |
| Equality state | `exact_source_crop_verified` and `decoded_pixels_equal: true` |
| Equality mode | RGBA comparison after Pillow decode and lossless PNG reopen |
| Master-rectangle RGBA SHA-256 | `3d3d617eefff51f0fc629625a41a36c167d35f26c98239ccd81e3ee36a82f883` |
| Reopened-crop RGBA SHA-256 | `3d3d617eefff51f0fc629625a41a36c167d35f26c98239ccd81e3ee36a82f883` |
| Pixel count | `494100` |

The crop intentionally removes the negative's handwritten catalog markings while preserving the face, collar, tie, and shoulders. It is identity evidence only and is not a runtime texture.

## Ownership gate

Search roots were the current Chaos Redux project (`common/`, `history/`, `gfx/`, `interface/`, `localisation/`), installed vanilla HOI4 at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`, and the approved reference mods `1521695605`, `2265420196`, and `1458561226`.

Search terms included `William D. Stephens`, `William Dennison Stephens`, `William Stephens`, `Wm. D. Stephens`, `Stephens William`, `William D Stephens`, `W. D. Stephens`, `Governor Stephens`, `Gov. Stephens`, `Stephens governor`, `william_d_stephens`, `william_stephens`, `stephens_william`, and `w_d_stephens`, across character definitions, country histories, portrait paths, `.gfx`/interface consumers, and localisation.

Results: no exact or variant identity match in the current project, installed vanilla, or any approved reference mod; no matching leader, commander, operative, officeholder, or portrait consumer was found. Filename scans found only unrelated surname strings such as `Donald_Stephens.dds`, `AST_percy_reginald_stephensen.png`, `AST_stephenson`, and `CAN_william_samuel_stephenson`, none of which resolve to William Dennison Stephens.

Hiram Johnson was considered and rejected because Kaiserreich/ACC defines and portrait-owns `ACC_hiram_johnson` in `common/characters/ACC characters.txt:44`, `interface/kaiserreich/portraits/ACC_portraits.gfx:15`, and `localisation/english/KR_country_specific/ACC - American Constitutional Coalition l_english.yml:556`; this rejection is recorded to prevent accidental substitution.

Disposition: William D. Stephens is ownership-clear for this package, with no transfer guard required because no origin owner exists.

## Runtime handoff state

Proposed identity replacement for parent review: `William D. Stephens` in the `HBX_independence_wave_civic_convention_chair` role.

Suggested source role family for the later full portrait pipeline: country leader or named officeholder, full `156x210` HOI4 portrait, using the canonical leader references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`.

This source-clearance package stops before source-locked ImageGen repaint, deterministic `156x210` processing, independent likeness/style/provenance audit, DDS conversion, and runtime wiring. The parent agent must complete those gates before any `.gfx` or character consumer is changed.

Asset status: `sourced`; runtime status: `not_promoted` / `pending_full_portrait_pipeline`.

## Risks and uncertainties

- LOC says "No known restrictions on publication" and does not issue a Creative Commons or public-domain dedication for this item; retain the LOC rights advisory and Bain rights-guidance links with any distribution.
- The catalog dates the negative to circa 1920-1925, so it is not a 1936 portrait; the subject identity and period clothing remain appropriate for a 1936 officeholder depiction.
- The fictional convention-chair assignment is an alternate-history role fit, not a claim that Stephens chaired a real 1936 constitutional convention.
- The LOC-served JPEG is the available large download from the object record; the higher-resolution TIFF endpoint returned a truncated, undecodable response during retrieval and was discarded rather than treated as provenance.
