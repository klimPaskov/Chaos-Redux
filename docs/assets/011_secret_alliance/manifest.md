# Event 011 Secret Alliance raster asset manifest

Event id: `011`

Event slug: `secret_alliance`

Tranche owner: generated event art (`chaosx_generated_event_art`)

Generation date: `2026-07-10`

Package scope: seven report images, one public-coalition news image, and one reveal super-event image

## Package result

All nine requested raster assets have distinct generated source artwork, deterministic processed PNGs, exact-size 32-bit BGRA DDS files, review contact sheets, a super-event mask preview, prompt records, and a GFX handoff. The runtime DDS filenames and sprite names match `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_asset_register.md` exactly.

The original asset-production tranche did not edit gameplay, localisation, GUI, event, decision, idea, achievement, audio, or spreadsheet files. That statement is production chronology, not current wiring status. The final gameplay and balance freeze `1c87d923` registers these assets in `interface/011_secret_alliance.gfx` and `interface/chaosx_super_events.gfx` and uses them from the Event 011 event, decision, achievement, animation, and super-event surfaces.

## Source and rights status

- Source mode for every listed asset: built-in OpenAI `$imagegen` / `image_gen`, one distinct generation per asset.
- Source links, external authors, archives, and collections: not applicable; no internet or third-party source image was used.
- Rights status: generated output, not an archival work and not asserted to be public domain. No third-party image licence or attribution is attached to these images. Project use is subject to the applicable OpenAI generated-output terms.
- Real-person status: all people are fictional and anonymous. No real leader likeness was requested or intentionally fabricated.
- Historical-symbol status: no fixed national flag, extremist symbol, or attested coalition symbol was requested. The public-coalition scene uses an invented unlettered geometric emblem.
- Period fit: every prompt required 1936-1945 photographic technology, clothing, vehicles, architecture, physical props, and press composition. Final review found no modern surveillance technology, tactical clothing, street furniture, vehicles, UI, readable generated writing, or fixed national flags.

The exact prompts are preserved in `docs/assets/011_secret_alliance/prompts/generated_event_art_prompts.md`.

## Verified reference restoration

The current checkout did not contain the reference folders or report-card processor named by the asset skill and Event 011 production prompt. The exact project files were restored for read/use from two local Chaos Redux worktrees after byte verification. This was accepted by the parent implementation agent as restoration of the project workflow, not a fallback. No substitute reference art or processing step was used.

Verified worktrees:

- `C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux`
- `C:/Users/klimp/.codex.broken-20260627-113153/worktrees/7654/chaos_redux`

Both worktrees contain byte-identical copies of:

| Restored project reference | SHA-256 |
| --- | --- |
| `assets/report_event_images/report_event_soldiers_marching.png` | `79AB1C33676EBCC59E2991C8B5FA1C5C8C576170E62212E86D336FADFB04103A` |
| `assets/report_event_images/report_event_soldiers_parade.png` | `37FC071BA2A86B334CC8260DE2A39C7F46D25CF37953AAB16AD80ABAE3B1FC47` |
| `assets/news_event_images/news_event_001.png` | `2554112BCD6CFF83E703D950A18F44A6FC73E303FA0F10D711420C60C5165938` |
| `assets/news_event_images/news_event_002.png` | `90A133B56D81456B0C817C2C39F1CC0E020841DF1833E85C167FFDA1207E8760` |
| `assets/super_event_images/super_event_angel_directorate.png` | `C0EAFF9F7A4A65846E457C9000CA8062C5D9F333DC56DD2A42BA747136CD4EEB` |
| `assets/super_event_images/super_event_divine_sovereignty.png` | `B8709450A216B15FD0F94DF570E744E17D8A670BC18B3026AEBDC590D524663A` |
| `tools/process_report_event_image.py` | `5B51613F391934960A8310268041C66B00FDD31BC12DA2393EB02C8F3DC87BD9` |

The checkout's `.tools/report_event_template.psd` has SHA-256 `68A05328400F6B3011F558690708B4FAFC034A9F0CFC4C4399DEF8E49B1F2472`, matching the same file in the restored worktrees. The verified super-event frame inspected for final composition is `gfx/super_events/super_event_template.psd`, SHA-256 `4F2C509A690CB9EEF3262BEE9064AB8EA585826D7C2637B197F7B98A2A39E168`.

Additional current-project precedents inspected:

- `docs/assets/010_death/contact_sheets/death_report_event_images_contact.png`
- `docs/assets/010_death/processed_png/news_event_death_mainland_reveal.png`
- `gfx/super_events/super_event_image_template_457x328.psd`
- vanilla report/news event picture references and sprite usage under the installed Hearts of Iron IV `events/` and `interface/` folders

## Processing and conversion

- Report cards: the byte-verified project `process_report_event_image.py`, with explicit `210x176` canvas, `192x153` card, `4.0` degree tilt, `4 5` shadow offset, `4.5` blur, `0.50` opacity, deterministic grain, transparent margins, and per-asset deterministic seeds.
- News image: deterministic centered cover crop to `397x153`, autocontrast, restrained press contrast/sharpness, true grayscale mode `L`, and deterministic monochrome grain.
- Super-event image: deterministic centered cover crop to `457x328`, restrained tonal normalization/sharpness, deterministic monochrome grain, and review through the verified super-event aperture.
- DDS conversion: `.tools/convert_to_dds.py`, 32-bit uncompressed BGRA/B8G8R8A8 masks, one mip level. Validation confirms final DDS pixels are identical to the matching processed PNG pixels after RGBA decoding.
- Reproduction entrypoint: `docs/assets/011_secret_alliance/_tooling/process_event_011_raster_assets.py`.

## Asset ledger

### `report_first_pattern`

- Asset type: report event image
- Intended use: first noticeable pattern incident; railway dispatch evidence comparison
- Related events: `chaosx.nr11.3`, `chaosx.nr11.9`, `chaosx.nr11.12`, `chaosx.nr11.193`, `chaosx.nr11.196`, `chaosx.nr11.197`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_first_pattern`
- Era-fit note: 1938 railway office, period clerks, pigeonholes, clock, dispatch envelopes, and telegraph equipment
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_first_pattern_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_first_pattern.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_first_pattern.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_first_pattern`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_missing_courier`

- Asset type: report event image
- Intended use: courier disappearance and route investigation
- Related event: `chaosx.nr11.6`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_missing_courier`
- Era-fit note: 1939 rural border road, period bicycle, satchel, border barrier, uniforms, and muddy field search
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_missing_courier_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_missing_courier.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_missing_courier.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_missing_courier`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_machine_sabotage`

- Asset type: report event image
- Intended use: industrial sabotage evidence
- Related event: `chaosx.nr11.7`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_machine_sabotage`
- Era-fit note: 1940 machine shop, belt-driven industrial equipment, work coats, damaged gears, and practical work lamp
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_machine_sabotage_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_machine_sabotage.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_machine_sabotage.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_machine_sabotage`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_safehouse_raid`

- Asset type: report event image
- Intended use: successful safehouse, raid, or courier mission
- Related events: `chaosx.nr11.11`, `chaosx.nr11.13`, `chaosx.nr11.15`, `chaosx.nr11.194`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_safehouse_raid`
- Era-fit note: 1941 rented room, valve radio, interwar luggage, iron bed, blackout curtains, and plain-clothes search team
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_safehouse_raid_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_safehouse_raid.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_safehouse_raid.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_safehouse_raid`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_border_survey`

- Asset type: report event image
- Intended use: military preparation clue and border reconnaissance
- Related events: `chaosx.nr11.5`, `chaosx.nr11.8`, `chaosx.nr11.192`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_border_survey`
- Era-fit note: 1930s stone bridge, mountain pass, optical survey tripod, measuring rods, civilian surveyors, and concealed border observers
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_border_survey_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_border_survey.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_border_survey.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_border_survey`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_political_attack`

- Asset type: report event image
- Intended use: Evolution II attempted killing or threat aftermath
- Related events: `chaosx.nr11.4`, `chaosx.nr11.10`, `chaosx.nr11.21`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_political_attack`
- Era-fit note: 1942 government steps, period staff car, shattered window, winter coats, and restrained security perimeter
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_political_attack_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_political_attack.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_political_attack.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_political_attack`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `report_turned_channel`

- Asset type: report event image
- Intended use: turned member, controlled channel, or counter-network success
- Related events: `chaosx.nr11.14`, `chaosx.nr11.16`, `chaosx.nr11.191`, `chaosx.nr11.195`, `chaosx.nr11.198`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `report_event_turned_channel`
- Era-fit note: 1943 provincial railway waiting room, period coats and hats, travel case, practical lamps, and natural facial obscuration
- Source PNG: `docs/assets/011_secret_alliance/source_png/report_event_turned_channel_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/report_event_turned_channel.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/report_event_turned_channel.dds`
- Target size: `210x176`
- Sprite: `GFX_report_event_011_secret_alliance_turned_channel`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `news_public_coalition`

- Asset type: public news-event image
- Intended use: public anti-target faction formation
- Related event: `chaosx.nr11.200`
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `news_event_public_coalition`
- Era-fit note: 1941 wire-service group portrait, period microphones, mixed civilian delegations and generic military staff, stone civic architecture, and invented unlettered emblem
- Source PNG: `docs/assets/011_secret_alliance/source_png/news_event_public_coalition_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/news_event_public_coalition.png`
- Final DDS: `gfx/event_pictures/011_secret_alliance/news_event_public_coalition.dds`
- Target size: `397x153`, true black-and-white/grayscale
- Sprite: `GFX_news_event_011_secret_alliance_public_coalition`
- Target GFX: `interface/011_secret_alliance.gfx` (wired)
- Localisation key: not applicable
- Status: `wired_complete`

### `super_event_reveal`

- Asset type: reveal super-event image
- Intended use: first public reveal and common coalition commitment
- Related super-event: research-selected slot `73`; hostile-war, pact-controlled, player-forced, and fractured reveal routes
- Source mode: generated with built-in `$imagegen`
- Exact generation prompt: `prompts/generated_event_art_prompts.md`, section `super_event_public_reveal`
- Era-fit note: 1942 formal council hall, mixed civilian and military delegations, press cameras, practical chamber lighting, folded unlabelled map, and broken seal as secondary props
- Source PNG: `docs/assets/011_secret_alliance/source_png/super_event_public_reveal_source.png`
- Processed PNG: `docs/assets/011_secret_alliance/processed_png/super_event_public_reveal.png`
- Final DDS: `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`
- Target size: `457x328`
- Sprite: `GFX_super_event_011_secret_alliance_public_reveal`
- Target GFX: `interface/chaosx_super_events.gfx` (wired)
- Localisation key: selected separately by the Event 011 super-event text package
- Status: `wired_complete`

## Review files

- Source contact sheet: `docs/assets/011_secret_alliance/contact_sheets/event_011_raster_source_contact_sheet.png`
- Processed contact sheet: `docs/assets/011_secret_alliance/contact_sheets/event_011_raster_processed_contact_sheet.png`
- Super-event UI mask preview: `docs/assets/011_secret_alliance/contact_sheets/super_event_public_reveal_ui_mask_preview.png`
- Machine-readable/reproducible checks: `docs/assets/011_secret_alliance/notes/validation.md`

## Validation summary

- All seven report processed PNGs and DDS files are exactly `210x176`.
- All report cards have transparent corner pixels, visible subtle tilt, transparent edge space, and soft shadow.
- The news processed PNG and DDS are exactly `397x153`; the PNG is true grayscale mode `L` before conversion.
- The super-event processed PNG and DDS are exactly `457x328`; the important delegation/table composition remains clear inside the verified UI aperture.
- Every DDS has 32-bit BGRA/B8G8R8A8 channel masks and decodes pixel-identically to its processed PNG.
- The nine source PNGs have nine distinct SHA-256 hashes.
- No placeholder, reused art, map-only composition, readable generated text, or unprocessed model output is used as a final asset.

## Simplifications, omissions, and blockers

None. The raster tranche delivered every requested final asset, and final Event 011 gameplay and balance freeze `1c87d923` preserves all GFX and gameplay/super-event wiring. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; that separate authority is not an asset blocker.
