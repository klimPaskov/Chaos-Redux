# Fallout Living World Pilot Report Event Asset Manifest

Status: `registered_event_attachment_pending`

Production date: 2026-07-15

## Scope and ownership

This package contains three dedicated fictional Fallout living-world report-event images for the accepted global anchors `The Last Inventory`, `River Intake at Dawn`, and `Rail Crew Twenty-Seven`.

The package is Fallout-owned. It does not reuse a zombie or other feature id, file, asset, audio file, sprite, or path. It does not create a super-event image. No `.gfx`, `.gui`, gameplay, localisation, event, focus, decision, idea, country, history, or spreadsheet file was edited.

Accepted source direction was taken from:

- `docs/specs/air_cleanliness_fallout_specs/SOURCE_OF_TRUTH_AND_SCOPE.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/04_global_survival_and_society_event_bible.md`
- `docs/specs/air_cleanliness_fallout_specs/matrices/fallout_global_event_family_matrix.md`
- `docs/specs/air_cleanliness_fallout_specs/matrices/baseline/fallout_asset_matrix.md`
- `docs/specs/air_cleanliness_fallout_specs/prompts/fallout_event_asset_prompt.md`
- `docs/specs/air_cleanliness_fallout_specs/prompts/fallout_living_world_implementation_prompt.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`

The report-event references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`, the existing Air Winter final report-event contact sheet, vanilla `interface/eventpictures.gfx`, and the offline Event modding wiki page were inspected before production.

## Shared technical profile

- Source mode: OpenAI built-in ImageGen, one distinct generation call per asset, no input images.
- Source rationale: all three scenes are fictional alternate-history documentary moments with no real person, historical photograph, or unique archival object to reproduce.
- Source PNG format: `1448x1086`, RGB PNG.
- Processed PNG format: `210x176`, RGBA PNG.
- Final DDS format: legacy one-level uncompressed 32-bit BGRA/B8G8R8A8, `210x176`, 128-byte DDS header, no mipmaps, `147,968` bytes.
- Report treatment: `192x153` documentary card on a transparent `210x176` canvas, 2-pixel paper border, soft shadow at `(4, 5)`, shadow blur `4.5`, opacity `0.50`, grain `6`, paper grain `2`, 4x rotation supersampling, edge soften `0.35`.
- Processing tool: `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- DDS converter: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. `texconv` was not available on `PATH`, so the converter used its supported ffmpeg raw-BGRA backend. The resulting files pass the complete legacy-header and exact-length checks below.
- Contact sheet: `docs/assets/fallout_world_end/living_world_pilot/contact_sheets/fallout_living_world_pilot_report_events_contact_sheet.png`, RGB PNG, `1420x1435`, SHA-256 `1ed7492865e512f3ee89497287f04e2682f8ae1fddae0c2ab6c6d30b31128b53`.
- Rights and provenance: each master was generated in this Codex task by OpenAI built-in ImageGen on 2026-07-15. No external source image, named person, brand asset, or third-party visual reference was supplied to the model. The depicted people and places are fictional. Project use and distribution remain subject to the applicable OpenAI output terms and repository distribution policy; this manifest records provenance and is not legal advice.

## `report_event_fallout_last_inventory`

- Asset name: The Last Inventory.
- Related system: Fallout living-world global survival and society event library.
- Related event id: reserved visible root `chaosx.fallout.100`.
- Asset type: report event image.
- Intended use: the opening food-inventory and ration-law anchor when orientation finds less than one month of food.
- Final identity: `report_event_fallout_last_inventory`.
- Registered sprite: `GFX_report_event_fallout_last_inventory`.
- Suggested `.gfx` file: `interface/fallout_world_end.gfx`.
- Localisation keys: `chaosx.fallout.107.t`, `chaosx.fallout.109.t`, `chaosx.fallout.110.t`, `chaosx.fallout.111.t`, `chaosx.fallout.121.t`, and `chaosx.fallout.112.t`.
- Source mode: OpenAI built-in ImageGen.
- Generation output record: Codex generation `exec-038ea798-8a9b-47c2-a28b-41737587f245.png` in generation session `019f6478-fc67-7742-9c1f-2fb19eec963b`; the workspace source PNG is an exact preserved copy.
- Source PNG: `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_last_inventory_source.png`, RGB PNG, `1448x1086`.
- Processed PNG: `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_last_inventory.png`, RGBA PNG, `210x176`.
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_last_inventory.dds`, uncompressed BGRA DDS, `210x176`.
- Processing parameters: angle `+3` degrees, deterministic seed `2026071501`; shared parameters above.
- Crop review: both ration clerks, the nearly empty crate, dwindling sealed tins, paper-wrapped stores, sacks, empty shelving, and plain ledger remain readable at the final crop. The visual subject remains distinct from a generic ruin scene.
- Text review: no rendered labels, words, numbers, logos, insignia, or watermark are visible.
- DDS QA: header pass; exact length pass; alpha range `0-255`; corner alpha `[0, 0, 0, 0]`; decoded DDS and processed PNG are pixel-identical with maximum channel delta `0`.
- SHA-256 source: `10c1f19be3c14322dd261bc8b80e923c5897207a646296def16abf73d7b82f8a`.
- SHA-256 processed: `27906ce566c4484b17b8c39171cc529085fb371b2defdbed5a7872a6ec4f7f90`.
- SHA-256 DDS: `6c4089ca59e27be9dfae102fcfb0de99f1b521cc5ee7f74a61c4fbf8449eb8c2`.
- Status: `registered_event_attachment_verified_dormant`.
- Risk: the image is fictional generated documentary art, not historical evidence. The anonymous clerks use generic mid-century civilian clothing rather than a country-specific uniform, which keeps the global anchor reusable but should not be described as a named historical institution.

### Generation prompt

```text
Use case: historical-scene
Asset type: Hearts of Iron IV report-event documentary source photograph, to be cropped into a 210x176 sepia card
Primary request: The Last Inventory, a grounded fictional post-collapse ration scene using 1940s material culture
Scene/backdrop: cramped concrete civil-defense storeroom in the aftermath of a catastrophic ash winter; mostly empty wooden shelves, a visibly dwindling but orderly group of sealed tins, waxed cartons, grain sacks, and ration crates; one bare protected lamp; dust and ash tracked at the threshold
Subject: two tired civilian ration clerks in practical late-1930s to mid-1940s work clothes count the final sealed stores; one clerk checks tins beside an open plain ledger with no readable writing while the other lifts a nearly empty crate
Style/medium: photorealistic period documentary photograph made with 1936-1945 camera technology; candid news-photography realism, authentic grain and imperfect exposure, not cinematic concept art
Composition/framing: horizontal 4:3 documentary frame, eye-level medium-wide shot; clerks and last supplies centered in the middle 75 percent so a later tight landscape cover crop remains readable; hands and faces natural; clear foreground-to-background depth
Lighting/mood: dim practical overhead light and faint cold doorway light; sober scarcity, administrative competence, fatigue
Color palette: restrained neutral period photographic color is acceptable because final processing will convert to monochrome sepia
Materials/textures: worn wool, cotton work coats, rough concrete, dented unbranded tins, old wood, waxed paper, dust
Constraints: fictional anonymous people only; accurate 1940s clothing, containers, shelving, ledger, and lighting; no rendered words or numbers; no labels; no logos; no insignia; no watermark; no title card; no border or tilted photo-card treatment in the generated source
Avoid: Fallout franchise imagery, retrofuturism, modern tactical gear, modern respirators, plastic packaging, supermarket shelves, modern lighting, readable handwriting, readable crate markings, glamorous posing, exaggerated ruins, gore, zombies, monsters, weapons, cinematic orange-teal grading, illustration, painterly concept art
```

## `report_event_fallout_river_intake_at_dawn`

- Asset name: River Intake at Dawn.
- Related system: Fallout living-world global survival and society event library.
- Related event id: reserved visible root `chaosx.fallout.107`.
- Asset type: report event image.
- Intended use: the water-intake anchor when ash, contamination, or upstream control threatens the main source.
- Final identity: `report_event_fallout_river_intake_at_dawn`.
- Registered sprite: `GFX_report_event_fallout_river_intake_at_dawn`.
- Suggested `.gfx` file: `interface/fallout_world_end.gfx`.
- Localisation key: pending implementation in the event ID ledger; the accepted working label is not final localisation.
- Source mode: OpenAI built-in ImageGen.
- Generation output record: Codex generation `exec-a8e714dd-c8b0-4d2c-a7ed-e7aeb6234a5c.png` in generation session `019f6478-fc67-7742-9c1f-2fb19eec963b`; the workspace source PNG is an exact preserved copy.
- Source PNG: `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_river_intake_at_dawn_source.png`, RGB PNG, `1448x1086`.
- Processed PNG: `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_river_intake_at_dawn.png`, RGBA PNG, `210x176`.
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_river_intake_at_dawn.dds`, uncompressed BGRA DDS, `210x176`.
- Processing parameters: angle `-3` degrees, deterministic seed `2026071502`; shared parameters above.
- Crop review: all three workers remain visible with the ash-clogged intake grate, pump, hoses, brick pump house, river, and weak dawn light. The crew's physical work remains the focal action after the report-event crop.
- Text review: no rendered labels, words, numbers, logos, insignia, or watermark are visible.
- DDS QA: header pass; exact length pass; alpha range `0-255`; corner alpha `[0, 0, 0, 0]`; decoded DDS and processed PNG are pixel-identical with maximum channel delta `0`.
- SHA-256 source: `fbc446066aa0e554c23221882b01938fc623a24ea2d3f551cf05b9e973e303df`.
- SHA-256 processed: `9bdcda16d09063a0e654cb3a15c74632880c978168dc457a5a237f3b5f10ad7a`.
- SHA-256 DDS: `9052a344237e64903d9cab3ec0d9db86a364a4935912b35104a46584fd2cea94`.
- Status: `registered_event_attachment_pending`.
- Risk: the generated pump and respirators are period-plausible generic industrial equipment, not verified models from a particular country. The image should remain attached to a global fictional anchor rather than a claim about a named real waterworks.

### Generation prompt

```text
Use case: historical-scene
Asset type: Hearts of Iron IV report-event documentary source photograph, to be cropped into a 210x176 sepia card
Primary request: River Intake at Dawn, a grounded fictional post-collapse water-survival scene using 1940s material culture
Scene/backdrop: broad gray river at cold dawn beneath an ash-loaded sky; a low brick municipal pump house and exposed iron intake grating at the muddy bank; fine ash has settled on the river edge, machinery, and workers' coats
Subject: a small civilian intake crew of three workers in late-1930s to mid-1940s rubberized coats, wool layers, boots, simple cloth-and-canister respirators, and plain goggles; they labor at the intake, one clearing ash from the iron grate with a long shovel, one hauling a clogged filter basket, one checking a hand-operated pump and hose; practical protective work, not soldiers
Style/medium: photorealistic period documentary photograph made with 1936-1945 camera technology; candid municipal field documentation, authentic grain and imperfect exposure, not cinematic concept art
Composition/framing: horizontal 4:3 documentary frame, eye-level medium-wide shot from the bank; the three workers and intake machinery occupy the central middle 75 percent so a later tight landscape cover crop remains readable; river and pale dawn establish context behind them
Lighting/mood: weak dawn light through ash haze, damp cold air, severe but competent emergency work
Color palette: restrained neutral period photographic color is acceptable because final processing will convert to monochrome sepia
Materials/textures: wet brick, riveted iron, mud, ash, aged rubberized cloth, wood-handled tools, canvas hose, rippled dirty water
Constraints: fictional anonymous people only; accurate 1940s clothing, respirators, hand tools, pump equipment, and brick infrastructure; no rendered words or numbers; no signs; no logos; no insignia; no watermark; no title card; no border or tilted photo-card treatment in the generated source
Avoid: Fallout franchise imagery, retrofuturism, modern hazmat suits, modern tactical equipment, modern full-face respirators, fluorescent safety clothing, plastic pumps, modern concrete floodworks, readable text, glamorous posing, soldiers, weapons, gore, bodies, zombies, monsters, cinematic orange-teal grading, illustration, painterly concept art
```

## `report_event_fallout_rail_crew_twenty_seven`

- Asset name: Rail Crew Twenty-Seven.
- Related system: Fallout living-world global survival and society event library.
- Related event id: reserved visible root `chaosx.fallout.114`.
- Asset type: report event image.
- Intended use: the protected rail-repair anchor on a critical frozen or contaminated corridor.
- Final identity: `report_event_fallout_rail_crew_twenty_seven`.
- Registered sprite: `GFX_report_event_fallout_rail_crew_twenty_seven`.
- Suggested `.gfx` file: `interface/fallout_world_end.gfx`.
- Localisation key: pending implementation in the event ID ledger; the accepted working label is not final localisation.
- Source mode: OpenAI built-in ImageGen.
- Generation output record: Codex generation `exec-6a302639-fa52-46d3-81a5-d7e23b70ec9c.png` in generation session `019f6478-fc67-7742-9c1f-2fb19eec963b`; the workspace source PNG is an exact preserved copy.
- Source PNG: `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_rail_crew_twenty_seven_source.png`, RGB PNG, `1448x1086`.
- Processed PNG: `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_rail_crew_twenty_seven.png`, RGBA PNG, `210x176`.
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_rail_crew_twenty_seven.dds`, uncompressed BGRA DDS, `210x176`.
- Processing parameters: angle `+3` degrees, deterministic seed `2026071503`; shared parameters above.
- Crop review: all four protected workers remain identifiable with the damaged joint, hand jack, bars, wrench, dirty snow, telegraph corridor, and secondary period work train. The foreground repair action remains readable at native report-event size.
- Text review: no rendered labels, words, numbers, logos, insignia, or watermark are visible.
- DDS QA: header pass; exact length pass; alpha range `0-255`; corner alpha `[0, 0, 0, 0]`; decoded DDS and processed PNG are pixel-identical with maximum channel delta `0`.
- SHA-256 source: `99f4cadd9b958b84f2db72f6bcaabd611474e2ee0ae216a37ecbdb56e8b0e370`.
- SHA-256 processed: `874511450181e12f082101faa840c972dccb513e71972a5584248a32eaf123bb`.
- SHA-256 DDS: `29f9e6ff523d9883df34cc617692c711ff84de5cca082ae0cad7302a10120b5f`.
- Status: `registered_event_attachment_pending`.
- Risk: the distant rail vehicle is intentionally secondary and is not model-identifiable at the final crop. The workers' generic industrial protection should not be described as one named railway's exact issued equipment.

### Generation prompt

```text
Use case: historical-scene
Asset type: Hearts of Iron IV report-event documentary source photograph, to be cropped into a 210x176 sepia card
Primary request: Rail Crew Twenty-Seven, a grounded fictional post-collapse protected railway-repair scene using 1940s material culture
Scene/backdrop: exposed rail corridor through a frozen ash-contaminated landscape; dirty snow over ballast, telegraph poles fading into haze, a damaged rail joint and scattered ice on the line; a small steam maintenance wagon or period work train remains distant and secondary
Subject: four civilian railway workers in late-1930s to mid-1940s heavy wool coats, leather gloves, boots, simple cloth-and-canister respirators and plain goggles repair the critical track; two workers align a replacement rail with bars and hand jacks, one tightens a fishplate with a long wrench, and a protected foreman checks the joint; equipment crates and canvas protective wraps nearby
Style/medium: photorealistic period documentary photograph made with 1936-1945 camera technology; candid railway engineering documentation, authentic grain and imperfect winter exposure, not cinematic concept art
Composition/framing: horizontal 4:3 documentary frame, low eye-level medium-wide shot along the rails; crew and damaged joint centered in the middle 75 percent so a later tight landscape cover crop remains readable; converging rails establish the corridor without making the train the main subject
Lighting/mood: flat freezing daylight under dirty ash haze, visible breath if subtle; arduous, dangerous, disciplined collective repair
Color palette: restrained neutral period photographic color is acceptable because final processing will convert to monochrome sepia
Materials/textures: frost-coated steel, oily wood sleepers, dirty snow, wool, canvas, leather, iron hand tools
Constraints: fictional anonymous people only; accurate 1940s railway clothing, protective gear, hand tools, track hardware, telegraph poles, and rolling stock; no rendered words or numbers; no signs; no logos; no insignia; no watermark; no title card; no border or tilted photo-card treatment in the generated source
Avoid: Fallout franchise imagery, retrofuturism, modern high-visibility vests, hard hats, modern tactical gear, modern full-face respirators, power tools, modern locomotives, modern concrete sleepers, readable text, forced-labor imagery, guards, weapons, heroic propaganda posing, gore, bodies, zombies, monsters, cinematic orange-teal grading, illustration, painterly concept art
```

## Package review and remaining work

All three source PNGs, processed PNGs, final DDS files, and the contact sheet exist. Each DDS decodes at `210x176`, uses the required header layout, retains transparent card corners, and matches its processed PNG.

The three sprites are registered in `interface/fallout_world_end.gfx`. The reserved Fallout roots `chaosx.fallout.100`, `chaosx.fallout.107`, and `chaosx.fallout.114` are not defined, so event attachment remains pending. The package is registered, not event-wired or complete.

No visual placeholder, cross-feature reuse, generic-ruins substitution, or content simplification was used.
