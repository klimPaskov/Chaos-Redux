# Event 006 country-opening report image manifest

## Use and consumer

Asset family: ASSET-048 regional and country-opening report images.
Accepted use: one region-neutral civic opening image for `chaosx.nr6.41` in all 14 Event 006 regions.
Consumer: standard Hearts of Iron IV country-event picture.
Runtime size: 210×176 pixels.
Background: full-canvas opaque.
Generation: built-in native ImageGen with two focused edits to make clothing and architecture region-neutral; no sourced image or real person is depicted.

## Selected output

Selected candidate: CAND-006, an architecture edit of CAND-005.
The final scene shows a civic speaker, a second speaker holding an unmarked paper, waiting residents, a plain public-hall doorway, and two guards kept secondary at one side.
The level ground has no steps, platform, parade, national symbols, heraldry, readable text, map, or identifiable person.
The parent reviewed the processed target preview on 2026-09-27 and accepted it for the shared ASSET-048 use.

| File | Purpose | Dimensions / encoding | SHA-256 |
| --- | --- | --- | --- |
| `gfx/event_pictures/006_independence_wave/report_event_006_country_opening.dds` | Final runtime image | 210×176 BGRA8 DDS, 147,968 bytes, alpha fully opaque | `91b565fb48d4b880dc1af5303b2f26e92a14233dbb26bbb35e900cd2b223e351` |
| `docs/assets/006_independence_wave/country_opening_2026_09_27/source_png/report_event_006_country_opening_source.png` | Selected generated source | 1369×1149 RGB | `70f4980e94cf12a227cef660d13bd86120dec17d760a597ff2e5bbccc0453010` |
| `docs/assets/006_independence_wave/country_opening_2026_09_27/processed_png/report_event_006_country_opening.png` | Reviewed target preview | 210×176 RGB | `d7eb25b872ad3ceb318bc729f3b4555f99423e09471efeb01ac7b32d077d7e9f` |
| `docs/assets/006_independence_wave/country_opening_2026_09_27/prompts/candidate-006_edit.prompt.md` | Exact selected edit prompt | UTF-8 text | `ad94e79b94be536c7755e65e482d0957db48a622f7b2029d3904ad6850136f11` |
| `docs/assets/006_independence_wave/country_opening_2026_09_27/contact_sheets/report_event_006_country_opening_review.png` | Source, preview, and DDS round-trip review sheet | 2102×515 PNG | `155a83d9590ba4d78b42a876517a71be66937862c285c2c9ea5011bad598ce5c` |
| `docs/assets/006_independence_wave/country_opening_2026_09_27/contact_sheets/report_event_006_country_opening_contact_sheet.png` | Candidate lineage and final decode | 2102×515 PNG | `42dbfe960cc7f2817ff3da79e8c55076856a3fc434491b9b62fb826484cf7396` |

The DDS header is 124 bytes with a 32-byte BGRA8 pixel-format block and no mipmaps; the file length is the expected 128-byte header plus 210×176×4 pixel bytes.
The DDS-decoded PNG matches the processed preview in every RGB channel, and decoded alpha is 255 throughout.
The selected source was cropped from 1369×1149 to 1369×1147 and resized to 210×176 with Lanczos filtering.
No background-removal fallback was used.

## Candidate lineage

| Candidate | Disposition | Reason |
| --- | --- | --- |
| CAND-001 | Rejected | Regional clothing and architectural cues remained. |
| CAND-002 | Rejected edit | Regional facade and uniform cues remained. |
| CAND-003 | Rejected | Its broad steps-and-crowd composition contradicted the no-steps, small-exchange direction. |
| CAND-004 | Rejected | Headwear and shawl-like clothing retained region-coded cues. |
| CAND-005 | Rejected edit | Clothing improved, but a pitched-roof annex and divided windows remained region-coded. |
| CAND-006 | Selected | Anonymous hall wall and doorway, plain period clothing, level ground, modest exchange, and secondary guards. |

The source archive, full prompt file, candidate contact sheets, validation note, DDS round-trip PNG, and rejected candidate files remain in the local `docs/assets/006_independence_wave/country_opening_2026_09_27/` work archive.
The repository intentionally ignores `docs/assets/` as working data; this tracked manifest records the selected source, prompt, review, and runtime hashes without changing that policy.

## Exact selected edit prompt

Use case: style-transfer
Asset type: final refinement of one opaque Hearts of Iron IV report-event image, ultimately processed to 210x176
Input image: Image 1, CAND-005 generated source; edit target only.
Primary request: Make the modest public hall visually anonymous across fictional regions by simplifying its architecture. Preserve the current human exchange and its clear, quiet uncertainty.
Scene/backdrop: Replace the visible divided windows, pitched roof, and background annex with one plain, unadorned plaster or masonry hall wall and a simple deep rectangular doorway. Keep the building modest and recognizable only as a public hall through the doorway and the gathered community. Keep the forecourt completely level.
Subject: Preserve the current civic speakers, waiting neighbors, two guards, approximate figure count, positions, scale, gestures, plain clothing, and single safely lowered rifle. Preserve natural incidental faces and the speaker's blank paper. Do not add, remove, or rearrange people.
Style/medium: Preserve the restrained hand-painted documentary realism, matte brush texture, period report-illustration treatment, muted archival earth tones, and soft overcast light.
Composition/framing: Preserve the source's full-bleed horizontal framing, eye-level viewpoint, group geometry, foreground listeners, and broad readable silhouettes. Keep a small loosely spaced exchange with guards secondary on one side. Keep the hall doorway at the center. Full opaque image through every edge.
Lighting/mood: Preserve soft daylight, quiet uncertainty, and practical resolve.
Text (verbatim): None.
Constraints: Preserve the level ground and keep the image free of architectural or clothing cues tied to a specific country, people, or region. No steps, stairs, raised entrance, platform, windows, visible roofline, annex, ornament, columns, arches, carved stone, distinctive building style, flags, symbols, heraldry, badges, insignia, readable writing, watermarks, map boundaries, modern objects, or UI artifacts.
Avoid: Changing the scene into a parliament, ceremonial hall, formal council, mass rally, parade, or political ceremony. Avoid added people, new objects, decorative framing, cinematic color grading, caricature, and meme styling.

## Runtime wiring and limits

Sprite: `GFX_report_event_006_country_opening`.
GFX definition: `interface/006_independence_wave_small_assets.gfx`.
Picture consumer: `picture = GFX_report_event_006_country_opening` in `events/006_independence_wave.txt`, event `chaosx.nr6.41`.
No button icon, portrait, flag, country symbol, UI overlay, or second runtime variant is needed.
Visual review found a dense line of listeners along the lower edge and a partly cropped far-right guard, both readable at the target size.
The event graph renderer is not an in-game event-picture render, so the image's in-game presentation has not been claimed.
