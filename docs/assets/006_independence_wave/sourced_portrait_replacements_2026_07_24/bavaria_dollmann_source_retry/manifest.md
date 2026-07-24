# IW-009 Bavaria commander sourced portrait replacement

This package is a source-only replacement for the grounded male `BAY_independence_wave_mountain_commandant` commander token in Event 6, IW-009 Bavaria.

The selected identity is Friedrich Karl Albert Dollmann (2 February 1882 to 28 June 1944), a real male officer born in Würzburg who entered the Royal Bavarian Army and was alive in the 1936 setting.

The source mode is `grounded_source_only` and `internet source image` because Bavaria is a grounded historical polity and this named commander must remain a sourced real person.

Candidate verdict: `source_ready_needs_user_review`.

The source and explicit identity crop are rights-clear under the Wikimedia Commons record for the Bundesarchiv image, but the mandatory downstream source-locked HOI4 repaint and independent likeness/style/provenance audit are outside this retry and were not created.

No ImageGen result, processed `156x210` candidate, DDS, `.gfx` edit, gameplay edit, localisation edit, workbook edit, skill edit, or fallback was created.

## Candidate and role fit

Dollmann was born in Würzburg in 1882, entered the Royal Bavarian Army in 1899, served in Bavarian artillery and staff commands, and remained alive in 1936.

His Bavarian origin, artillery background, Würzburg service, and later army-level command make him a defensible sourced identity for the alternate IW-009 emergency command token.

The role is deliberately an alternate-history territorial-command abstraction rather than a claim that Dollmann historically served in the Gebirgstruppe.

The source photograph is from 1940 and visibly shows wartime uniform decorations and Nazi-era insignia, so a downstream portrait repaint must preserve identity while not silently presenting unsupported route-specific insignia as a 1936 Bavarian uniform.

## Immutable source master

| Field | Value |
| --- | --- |
| Path | `source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg` |
| Source page | <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_101I-052-1435-20,_Oberrhein,_Befestigung_am_Isteiner_Klotz.jpg> |
| Exact unchanged original download | <https://upload.wikimedia.org/wikipedia/commons/archive/1/11/20220702180551%21Bundesarchiv_Bild_101I-052-1435-20%2C_Oberrhein%2C_Befestigung_am_Isteiner_Klotz.jpg> |
| Official archive record | <https://www.bild.bundesarchiv.de/dba/de/search/?query=Bild+101I-052-1435-20> |
| Archive accession | `Bundesarchiv, Bild 101I-052-1435-20` |
| Archive/provider | German Federal Archive (Deutsches Bundesarchiv), collection `Bild 101 I` |
| Archive title | `Oberrhein, Befestigung am Isteiner Klotz` |
| Archive caption | `Im Westen, Oberrheinfront.- Generaloberst Friedrich Dollmann (r.) bei Besichtigung des Maschinenraumes (mit Gauleiter Weinrich, Mitte); PK 670` |
| Photographer | Unknown author (`o.Ang.` in the archive metadata) |
| Source date | `1940` (exact day not stated) |
| Original upload evidence | 12 December 2008, 20:31 UTC, `BArchBot`, `533x800`, 39,183 bytes |
| Original dimensions | `533x800` |
| Decoded mode/format | `L` grayscale JPEG |
| File size | `39,183` bytes |
| SHA-256 | `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12` |
| Rights | Creative Commons Attribution-ShareAlike 3.0 Germany (`CC BY-SA 3.0 DE`) as recorded on the Commons source page |
| Attribution | `Bundesarchiv, Bild 101I-052-1435-20 / CC-BY-SA 3.0` |
| License URL | <https://creativecommons.org/licenses/by-sa/3.0/de/deed.en> |
| Authenticity note | The Commons record states that the German Federal Archive supplied the image and guarantees authentic representation only from the original negative/positive or its digitisation. |

The retained JPEG is the archived 533x800 upload and is byte-for-byte unchanged from the direct download URL above.

The current Commons file revision is a 511x800 derivative cropped 4% horizontally on 2 July 2022; it was explicitly rejected and was not downloaded or used as the source master.

## Explicit face-visible head-and-shoulders crop

| Field | Value |
| --- | --- |
| Path | `source_crops/BAY_friedrich_dollmann_head_shoulders_300_120_500_450.png` |
| Source master | `source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg` |
| Crop coordinates | `(left=300, top=120, right=500, bottom=450)` in source-master pixels |
| Crop dimensions | `200x330` |
| Decoded mode/format | `L` grayscale PNG |
| File size | `35,833` bytes |
| SHA-256 | `C19C7D634EE585CB32853ED1A0F28BC4D37724AEAC2F58FF2509E20DE6C9B071` |
| Crop method | Direct source-pixel `Pillow.Image.crop`, no resampling, retouching, recolouring, or face alteration |
| Framing | Face-visible head, cap, both shoulders, collar, and upper tunic of the archive-captioned right-hand subject; the crop excludes the other man's face. |
| Intended use | Immutable identity reference for the future source-locked HOI4 commander-family repaint and likeness review; not a runtime portrait. |

The crop is an evidence crop only and must not be promoted directly to the game as a raw or merely resized commander portrait.

## Source comparison and provenance evidence

| Evidence | Path | Dimensions | SHA-256 |
| --- | --- | ---: | --- |
| Unchanged master plus explicit crop comparison | `evidence/BAY_friedrich_dollmann_source_master_crop_comparison.png` | `1120x1120` | `58B36189021E1D5F83D3A5A627B92CB7747EF79FE6DACE694DCBB10812E8CD18` |

The comparison sheet shows the complete unchanged 533x800 source on the left and the explicit crop at 4x nearest-neighbour scale on the right.

The comparison sheet is review evidence only and is not a final portrait or a runtime texture.

The canonical commander-family reference inspected for style and framing was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`, including `ger_erich_von_manstein.png`, `ger_erwin_von_witzleben.png`, and `eng_bernard_montgomery.png`.

## Subject-ownership gate

The exact and variant forms checked were `Friedrich Dollmann`, `Friedrich Dollman`, `Friedrich Karl Albert Dollmann`, `Friedrich Karl Dollmann`, `Dollmann, Friedrich`, `Dollmann Friedrich`, `Generaloberst Dollmann`, `General der Artillerie Dollmann`, `Friedrich_Dollmann`, `Friedrich-Dollmann`, `friedrich_dollmann`, `GER_friedrich_dollmann`, `Dollmann`, and `Dollman`.

Current Chaos Redux character, country-history, leader-portrait, interface, and localisation roots returned no Dollmann/Dollman owner.

Installed vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` roots returned no Dollmann/Dollman character, recruitment, portrait, `.gfx` consumer, or localisation owner.

Installed vanilla `history/units/GER_1939.txt` and `history/units/GER_1939_nsb.txt` contain only the incidental comments `7. Armee (CO: Dollmann)`; these are not character definitions, recruitment, portraits, or officeholder consumers.

Approved reference mods `1521695605`, `2265420196`, and `1458561226` returned no Dollmann/Dollman identity owner in their character, country-history, leader-portrait, interface, or localisation roots and no Dollmann/Dollman-named file.

No reference-mod art or source was copied.

No origin character exists, so no guarded transfer contract is needed; the stable IW-009 target remains the generated-character token `BAY_independence_wave_mountain_commandant`.

## Stable consumer and processing boundary

The stable token remains `BAY_independence_wave_mountain_commandant`.

The existing consumer assigns the same full portrait to the civilian-large and army-large slots and requires a corps commander.

The stable sprite remains `GFX_portrait_BAY_independence_wave_mountain_commandant` in `interface/006_independence_wave_region_01_portraits.gfx`.

The reserved runtime texture remains `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`, but this source-only retry intentionally creates no DDS and does not change that file.

The downstream processor must use the unchanged source master and exact crop as identity inputs, compare against the canonical commander references for style only, produce a source-locked identity-preserving repaint at `156x210`, and stop for an independent likeness/style/provenance audit before any conversion or runtime wiring.

## Exact alternate-role wording

Recommended role label: `Bavarian Emergency Passes-and-Depots Commandant`.

Exact role caveat: `Friedrich Dollmann is used here as Bavaria's emergency passes-and-depots commandant; this is a territorial-command abstraction, not a claim of historical Gebirgstruppe service.`

Suggested player-facing descriptor: `Born in Würzburg and formed in the Royal Bavarian Army, Friedrich Dollmann brings artillery and army-command experience to Bavaria's emergency passes and depots.`

## Status and uncertainty

Status is `source_ready_needs_user_review` rather than `complete` because the required source-locked repaint, independent visual audit, final DDS, and runtime wiring were explicitly outside this source retry.

The source rights chain is defensible under the Commons CC BY-SA 3.0 Germany record, with attribution and license URL preserved above.

Uncertainty remains on the exact photograph date and photographer because the archive records only `1940` and `o.Ang.`.

The image is a wartime 1940 photograph with visible Nazi-era insignia; any future repaint must preserve the identity without treating those source-visible details as an approved 1936 route uniform.

No simplification or fallback was used.
