# Event 32 generated event-art QA handoff

Disposition: implemented and superseded by the parent runtime installation pass. The QA verdicts remain valid; the historical statement that the package was only handed off is superseded by the current GFX/runtime wiring documented in `docs/events/032_missiles/asset_audit.md`.

Audit date: 2026-09-01.

Scope: the three existing generated full-canvas assets in `docs/assets/032_missiles/`.

The audit used the Event 32 asset prompt, the Event 32 asset specification, the existing asset prompts and manifest, and only the matching canonical reference families under `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`.

## Overall decision

All three required full-canvas assets are present and technically valid.

No asset is absent or invalid enough to justify a native ImageGen replacement.

No repair was performed.

The three source PNGs, processed PNGs, DDS files, prompts, manifest, existing `gfx_handoff.md`, and contact sheet remain untouched.

The package is `handed_off` for parent installation, not runtime-wired.

No ImageGen call was made during this QA pass.

## Reference gate

The report family contact sheet and five report references were inspected at the canonical `210x176` family canvas.

The report family uses a black-and-white or sepia documentary card with a tilted image, a soft shadow, and transparent edge corners.

The news family contact sheet and five news references were inspected at the canonical opaque `397x153` family canvas.

The news family uses black-and-white period press imagery with a strong horizontal subject and no transparent runtime border.

The decision-category-picture contact sheet and all thirteen references were inspected at the canonical `114x101` reference canvas.

The category-picture family is an opaque larger thematic picture surface, separate from the small category icon and from scripted-GUI backgrounds.

The category-picture contact sheet exists and is labelled with filenames and native dimensions.

## Asset decisions and evidence

### `032_missiles_country_report`

Decision: `PASS`, preserve, no repair.

Status: `handed_off` for parent installation.

The source is an official built-in ImageGen output recorded as generated fictional alternate-history World War II documentary art.

Generation date recorded in the package manifest: 2026-08-29.

The recorded ImageGen source path is `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-a836f221-f671-422c-a790-31143ecf1029.png`.

The retained source shows a practical experimental liquid-fuel rocket on a rugged rail trolley, two anonymous engineers in period work coats and helmets, a concrete instrument shelter, cables, a rail spur, winter scrub, and distant hills.

The scene has no readable text, national insignia, modern equipment, identifiable person, watermarked element, UI artifact, explosion, or mushroom cloud.

The heavy missile and guarded launch infrastructure satisfy the accepted country-report subject even though the source uses a rail trolley and concrete shelter rather than a fully buried entrance.

| Surface | Path | Dimensions | Mode or alpha | SHA-256 |
| --- | --- | ---: | --- | --- |
| Source PNG | `docs/assets/032_missiles/source_png/032_missiles_country_report_source.png` | `1122x1402` | RGB, effective alpha `255-255` | `c6e961abaa616bc5d32315da27e57a2c50c5f43a46330dc3a9e5b528f71c0284` |
| Processed PNG | `docs/assets/032_missiles/processed_png/032_missiles_country_report.png` | `210x176` | RGBA, alpha `0-255` | `56a75ddf1f47f913620dd4be2e58e7f353a95cbc8ce6a69e7ff2c3ab4115c430` |
| DDS | `docs/assets/032_missiles/dds/032_missiles_country_report.dds` | `210x176` | Legacy one-level BGRA, `147968` bytes | `6f9429f0f6d4b8743b1e554a2b3c50b6cbd51722fd6a0cc51ca8e7992a64f685` |

Processing used `process_report_event_image.py` and produced the required sepia documentary card, visible slight tilt, soft shadow, and transparent corners.

DDS validation passed the required `DDS ` magic, 124-byte header, 32-byte pixel-format block, flags `65`, fourCC `0`, 32-bit BGRA masks, texture caps `0x1000`, exact file length, declared dimensions, and alpha range.

The DDS decoded pixels equal the processed PNG pixels exactly.

### `032_missiles_global_proliferation_news`

Decision: `PASS`, preserve, no repair.

Status: `handed_off` for parent installation, with a non-blocking composition note below.

The source is an official built-in ImageGen output recorded as generated fictional alternate-history World War II press photography.

Generation date recorded in the package manifest: 2026-08-29.

The recorded ImageGen source path is `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-40f996cf-6429-4eff-ae6c-81a626aa3a08.png`.

The source shows a large experimental rocket launching from a rail structure, a broad industrial valley, multiple distant smoke columns, overcast sky, and a long line of anonymous wartime observers.

The scene has no readable text, flags, modern logos, modern equipment, identifiable person, watermarked element, UI artifact, or recognizable real tragedy photography.

The retained production prompt specifies one unmistakable launch as the central subject, while the Event 32 specification gives the stronger directional preference of several launch columns or transport silhouettes.

The current scene remains a clear period-news image of missile proliferation entering public view and matches the retained package prompt, so this variance is recorded for parent awareness rather than treated as an invalid asset.

If the parent applies “several launch columns or transport silhouettes” as a hard acceptance gate, hold this row for explicit user review before runtime promotion and request a separately approved ImageGen repair.

| Surface | Path | Dimensions | Mode or alpha | SHA-256 |
| --- | --- | ---: | --- | --- |
| Source PNG | `docs/assets/032_missiles/source_png/032_missiles_global_proliferation_news_source.png` | `1792x878` | RGB, effective alpha `255-255` | `738ce640d57147fc873a07d1c6a2ab6e9c3b08a2d1bde5cfd8c2ccd8d475a4a9` |
| Processed PNG | `docs/assets/032_missiles/processed_png/032_missiles_global_proliferation_news.png` | `397x153` | RGBA, alpha `255-255` | `ac92b24cf9d44a66170a5238915d7b64bace41b593e05d4cce187407988547d7` |
| DDS | `docs/assets/032_missiles/dds/032_missiles_global_proliferation_news.dds` | `397x153` | Legacy one-level BGRA, `243092` bytes | `c9da74d25c7a1d2462293d363df5c0e88928251c9f9cd216d2e5a237b1b9f444` |

Processing used the recorded deterministic cover crop, grayscale conversion, autocontrast, contrast, blur, and seeded film grain pass.

DDS validation passed the required `DDS ` magic, 124-byte header, 32-byte pixel-format block, flags `65`, fourCC `0`, 32-bit BGRA masks, texture caps `0x1000`, exact file length, declared dimensions, and alpha range.

The DDS decoded pixels equal the processed PNG pixels exactly.

### `032_missiles_program_category`

Decision: `PASS`, preserve, no repair.

Status: `handed_off` for parent installation.

The source is an official built-in ImageGen output recorded as generated fictional alternate-history World War II thematic panel art.

Generation date recorded in the package manifest: 2026-08-29.

The recorded ImageGen source path is `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-de19b24b-e7c7-453b-8a3c-3fbdb6b649d4.png`.

The source shows one large experimental rocket on a launch cradle beside a hardened concrete bunker, an observation mast, and a narrow smoke column.

The compact crop keeps the rocket silhouette and bunker readable at `114x101`.

The image has no readable text, fake buttons, meters, dynamic values, painted UI affordances, modern equipment, flags, identifiable person, watermarked element, or scripted-GUI framing.

The asset is correctly classified as a static decision-category picture, not a small category icon and not a mechanic-window background.

| Surface | Path | Dimensions | Mode or alpha | SHA-256 |
| --- | --- | ---: | --- | --- |
| Source PNG | `docs/assets/032_missiles/source_png/032_missiles_program_category_source.png` | `1254x1254` | RGB, effective alpha `255-255` | `5045035288b0885280b9577f5494e12d440ceac91fe412060eb37281dd68efbe` |
| Processed PNG | `docs/assets/032_missiles/processed_png/032_missiles_program_category.png` | `114x101` | RGB, effective alpha `255-255` | `a6196c6209159c6c45d363e5233c5f6738b8b1a29d28cdecefa3a17877971bb9` |
| DDS | `docs/assets/032_missiles/dds/032_missiles_program_category.dds` | `114x101` | Legacy one-level BGRA, `46184` bytes | `cd43aa6161a99cb8aad74a434e239328a2f014029ee7c0b90478ee01041e0d15` |

Processing used the recorded deterministic `114x101` cover crop with restrained contrast and blur.

DDS validation passed the required `DDS ` magic, 124-byte header, 32-byte pixel-format block, flags `65`, fourCC `0`, 32-bit BGRA masks, texture caps `0x1000`, exact file length, declared dimensions, and alpha range.

The DDS decoded pixels equal the processed PNG pixels exactly.

## Contact-sheet evidence

The retained review sheet is `docs/assets/032_missiles/contact_sheets/032_missiles_contact_sheet.png`.

Its dimensions are `1486x933`, its mode is RGB, its size is `543655` bytes, and its SHA-256 is `ff801325d35b51f9bc9f136059e24a8ce62ed0094c76e894841051c13b220840`.

It presents the native ImageGen source, processed PNG, and decoded DDS round-trip for all three assets.

## Parent installation requirements

The parent agent owns final runtime installation, `.gfx` registration, event references, category references, and live consumer validation.

Copy the report DDS to `gfx/event_pictures/032_missiles/032_missiles_country_report.dds`.

Copy the news DDS to `gfx/event_pictures/032_missiles/032_missiles_global_proliferation_news.dds`.

Copy the category-picture DDS to `gfx/interface/decisions/032_missiles/032_missiles_program_category.dds`.

Do not point runtime textures at `docs/assets/032_missiles/`.

Register the report and news sprites in the existing event-picture registry, expected by the package handoff to be `interface/events.gfx`.

Register the category sprite in the existing decision registry, expected by the package handoff to be `interface/decisions.gfx`.

The existing package handoff proposes `GFX_032_missiles_country_report`, `GFX_032_missiles_global_proliferation_news`, and `GFX_032_missiles_program_category`.

The Event 32 asset prompt also lists illustrative names `GFX_report_event_032_missiles_country_report`, `GFX_news_event_032_missiles_global_proliferation`, and `GFX_decision_category_032_missiles_program`.

The art is independent of these identifiers, so the parent must resolve the stable sprite names against the live consumer and use one consistent name per asset.

Do not register both naming sets or change filenames without an explicit wiring need.

Use the category asset through the category picture field as a static `114x101` picture.

Do not use the category DDS as the small category icon, a decision icon, a mission icon, or a scripted-GUI background.

Keep the temporary asset workspace until the parent has promoted durable provenance and wiring facts into permanent Event 32 documentation and confirmed that no runtime reference points into `docs/assets/`.

No gameplay, localisation, interface, GFX, decision, event, achievement, spreadsheet, portrait, flag, animation, 3D, or GUI file was edited by this handoff.
