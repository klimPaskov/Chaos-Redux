# IW-009 Bavaria commander source-clearance candidate

This package records a source-only candidate for the grounded male `BAY_independence_wave_mountain_commandant` commander token in Event 6, IW-009 Bavaria.

The candidate is Konrad Christoph Heinrich Krafft von Dellmensingen (24 November 1862 to 21 February 1953), a Bavarian Army general associated with the formation of Bavarian mountain troops and alive in the 1936 setting.

The candidate is not the primary clearance result. Its image is a pre-1933 military portrait without Nazi-era political insignia, but the retained source is a Commons scan of a 1933 book rather than an object-level institutional archive record. The package is therefore `needs_user_review` and is retained as a documented alternative only.

No ImageGen result, processed `156x210` candidate, DDS, `.gfx` edit, gameplay edit, localisation edit, workbook edit, or fallback was created.

## Source master

| Field | Value |
| --- | --- |
| Path | `source_masters/BAY_konrad_krafft_von_dellmensingen_hjb10_1933_original.jpg` |
| Source page | <https://commons.wikimedia.org/wiki/File:HJB10_%E2%80%93_Krafft_von_Dellmensingen.jpg> |
| Direct source URL | <https://upload.wikimedia.org/wikipedia/commons/f/f5/HJB10_%E2%80%93_Krafft_von_Dellmensingen.jpg> |
| Source publication | Fritz Jung, `Die Goslarer Jäger im Weltkriege`, Hildesheim, Buchdruckerei Lax, 1933 |
| Commons page ID | `24820909` |
| Commons revision captured in API snapshot | `1169554479`, 2026-02-20T23:48:36Z |
| Source subject | Konrad Krafft von Dellmensingen |
| Photograph date | Before 1933; exact date and photographer are not identified |
| Original dimensions | `471x593` |
| Decoded mode/format | `RGB` JPEG |
| Source SHA-1 | `a17098177fb3a4f5a968b267b35799b82d6c3cf0` |
| Source SHA-256 | `e1755fcc24808453eec7d36c6adc972956583a9c3255910aeafcf900c962527a` |
| Snapshot files | `source_page_snapshots/commons_file_page.html`, `source_page_snapshots/commons_file_api.json`, `source_page_snapshots/google_books_source_record.html` |

The source master is byte-for-byte the direct Commons file returned by the captured API metadata.

The Commons record identifies the author as unknown, cites the 1933 publication, and applies `PD-anon-70-EU` with a public-domain label and no attribution requirement. This is a published-scan provenance chain rather than an institutional archive object, so worldwide redistribution remains a review point.

## Exact identity crop

| Field | Value |
| --- | --- |
| Path | `source_crops/BAY_konrad_krafft_von_dellmensingen_head_shoulders_30_0_450_580.png` |
| Metadata | `source_crops/BAY_konrad_krafft_von_dellmensingen_head_shoulders_30_0_450_580.json` |
| Crop coordinates | `(left=30, top=0, right=450, bottom=580)` in source-master pixels |
| Crop dimensions | `420x580` |
| Crop SHA-256 | `77bc8d48de6fc7cfa036ea1b262a24927aafbdace1c4633c74b3a04b3d1e5d7e` |
| Crop method | `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, direct Pillow crop, no resampling or retouching |
| Equality evidence | Metadata reports `decoded_pixels_equal: true`; source crop and output RGBA SHA-256 both `7d3d45dbad83e962f27a5c6a21745d317523c5e11697c7f7d4dfc246c402c235` |
| Framing | Full head, both shoulders, collar, medals, crossed forearms, and upper torso of the single identified officer |

The crop is an immutable identity reference only and must not be promoted directly to the game as a raw or merely resized portrait.

## Historical and visual fit

Krafft von Dellmensingen was a Bavarian Army general and a plausible alternate-history emergency commander for Bavaria in the 1936 setting.

The portrait is pre-1933 and contains no Nazi-era political insignia, making it safer for a source-locked identity-preserving repaint than the 1940 Dollmann image.

The source is only 471x593 and is halftone printed, so the future repaint must preserve the face geometry without treating print texture as facial detail.

## Subject ownership gate

The exact and variant forms checked were `Konrad Krafft von Dellmensingen`, `Konrad Krafft-Dellmensingen`, `Krafft von Dellmensingen`, `Krafft-Dellmensingen`, `Krafft_Dellmensingen`, `Konrad_Dellmensingen`, `konrad_krafft`, and `Dellmensingen`.

The current Chaos Redux character, country-history, leader-portrait, interface, and localisation roots returned no identity owner.

Installed vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` roots returned no character, recruitment, portrait, `.gfx` consumer, or localisation owner.

Approved reference mods `1521695605`, `2265420196`, and `1458561226` returned no matching identity owner in their character, country-history, leader-portrait, interface, or localisation roots.

No origin character exists, so no guarded transfer contract is needed. The stable IW-009 target remains the generated-character token `BAY_independence_wave_mountain_commandant`.

## Stable consumer and downstream boundary

The stable sprite remains `GFX_portrait_BAY_independence_wave_mountain_commandant` in parent-owned `interface/006_independence_wave_region_01_portraits.gfx`.

The reserved runtime texture remains `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

The next processing pass must use the exact crop as the sole identity input, use the canonical commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/` for style only, produce an identity-preserving `156x210` repaint, and stop for independent likeness/style/provenance review before DDS conversion or runtime wiring.

## Status and uncertainty

Status is `needs_user_review` rather than `source_ready` because the source page is a Commons publication scan and does not expose an object-level institutional archive accession or worldwide rights statement for the underlying unknown photographer.

This candidate is retained as a no-political-insignia alternative, not as a replacement for the parent-owned Dollmann trial.

