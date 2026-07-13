# Stage 4 HQ and commander-ability generation prompts

## Source mode and shared scaffold

All final artwork in this package uses the built-in `$imagegen` workflow for fictional symbolic game art. Each source capture was generated as its own PNG; the green-background captures were cleaned with the official `remove_chroma_key.py` helper. No source is a photograph, archival image, real company logo, or copied reference asset.

Shared visual scaffold for every prompt:

> Chaos Redux HOI4 icon art for a late-interwar/WWII CBRN headquarters system; tactile painted field-manual finish; subdued olive drab, khaki, charcoal steel, oxidized brass, bone highlights, toxic green used only as a small state accent; one clear central subject; strong dark outline; high contrast at the target size; no text or labels; transparent unused pixels after processing; no modern hazmat suits, modern UI, warning labels, skulls, biological bombs, swastikas, camp/genocide imagery, zombies, white halo, sticker border, fake checkerboard, glow, watermark, or opaque square backdrop. The source capture uses a perfectly flat `#00ff00` chroma-key background with no shadow, gradient, reflection, or floor plane.

## Large counter frame prompts

Each frame was generated separately for a `76x42` large-counter source. Frame 000 is the active composition; frame 001 is a distinct muted-state composition. The second frame was not made by moving, recoloring, or resizing frame 000.

| Source frame | Prompt delta |
|---|---|
| `cbrn_hq_operations_section_frame_000_source.png` | Folded field map, plotting compass, signal handset, and sealed command dossier clasp; centered operations emblem. |
| `cbrn_hq_operations_section_frame_001_source.png` | Map spread wider, handset laid across the dossier, compass route marker moved; alert operational arrangement. |
| `cbrn_hq_intelligence_weather_cell_frame_000_source.png` | Field binoculars, brass aneroid barometer, sealed detector canister, weather dial, and folded observation sheet. |
| `cbrn_hq_intelligence_weather_cell_frame_001_source.png` | Raised binoculars, detector canister, rain gauge, and folded wind pennant; changed weather-intelligence arrangement. |
| `cbrn_hq_protective_logistics_section_frame_000_source.png` | Plain respirator storage crates, sealed filter tin, canvas harness, supply satchel, and hand-truck wheel; blank equipment panels only. |
| `cbrn_hq_protective_logistics_section_frame_001_source.png` | Open supply crate, two filter tins, canvas harness, and compact hand truck in an issue-state arrangement; blank equipment panels only. |
| `cbrn_hq_mobile_decontamination_column_frame_000_source.png` | Wheeled wash column, coiled canvas hose, hand pump, spray nozzle, and sealed decontamination drum. |
| `cbrn_hq_mobile_decontamination_column_frame_001_source.png` | Same equipment family with hose uncoiled into a working loop, nozzle forward, and drum valve open; operating arrangement. |
| `cbrn_hq_medical_countermeasure_directorate_frame_000_source.png` | Closed padded ampoule case, medical satchel, rolled syringe kit, plain blank treatment plate, and brass clasp. |
| `cbrn_hq_medical_countermeasure_directorate_frame_001_source.png` | Open ampoule case, padded tray, unfurled syringe roll, and forward plain cross plate; active-response arrangement. |
| `cbrn_hq_biological_security_section_frame_000_source.png` | Sealed specimen case, protective visor, shielded gauntlet, inspection lens, and stoppered sample vials. |
| `cbrn_hq_biological_security_section_frame_001_source.png` | Latched specimen case, visor turned toward inspection lens, gauntlet holding a vial rack, and boundary plate; containment arrangement. |

## Small on-map counter frame prompts

Each frame was generated separately as a `30x12` long horizontal white-on-transparent counter composition. These are not crops, downsizes, or recolors of the large counter masters.

| Source frame | Prompt delta |
|---|---|
| `cbrn_hq_operations_section_frame_000_source.png` | Field map, plotting compass, and old handset in a compact bone-white silhouette. |
| `cbrn_hq_operations_section_frame_001_source.png` | Wider map with compass needle and handset laid across it; purposeful companion silhouette. |
| `cbrn_hq_intelligence_weather_cell_frame_000_source.png` | Binoculars joined to a weather dial and detector canister. |
| `cbrn_hq_intelligence_weather_cell_frame_001_source.png` | Binoculars beside anemometer cups and a slim weather pennant. |
| `cbrn_hq_protective_logistics_section_frame_000_source.png` | Respirator crate, filter tin, and strapped supply satchel. |
| `cbrn_hq_protective_logistics_section_frame_001_source.png` | Open supply case with two filter tins, canvas straps, and hand-truck wheel. |
| `cbrn_hq_mobile_decontamination_column_frame_000_source.png` | Low wheeled wash cart, hose reel, hand pump, and spray nozzle. |
| `cbrn_hq_mobile_decontamination_column_frame_001_source.png` | Low wash cart with uncoiled hose, forward nozzle, and sealed drum. |
| `cbrn_hq_medical_countermeasure_directorate_frame_000_source.png` | Plain medical cross plate, sealed ampoule case, and compact syringe roll. |
| `cbrn_hq_medical_countermeasure_directorate_frame_001_source.png` | Open ampoule tray, syringe case, and folded medical satchel. |
| `cbrn_hq_biological_security_section_frame_000_source.png` | Sealed visor, compact shield, and two stoppered specimen vials in a case. |
| `cbrn_hq_biological_security_section_frame_001_source.png` | Latched specimen case, protective gauntlet, and shielded inspection lens. |

## Ability icon prompts

Each ability was generated as its own `34x33` transparent icon, with the compact subject and contrast tuned for the ability list rather than derived from a counter or technology icon.

| Source | Prompt delta |
|---|---|
| `cbrn_prepare_chemical_offensive_source.png` | Sealed artillery shell in a loading cradle beside a capped breech and locked preparation lever; staging only, no discharge or cloud. |
| `cbrn_theater_protective_posture_source.png` | Service respirator nested behind a reinforced shield plate with a folded protective hood and filter tin. |
| `cbrn_decontamination_corridor_source.png` | Coiled field hose and spray wand crossing between two small wash posts; no spray cloud. |
| `cbrn_seal_operational_area_source.png` | Steel gate bar clamped across a folded field-map panel with padlock and boundary stakes. |
| `cbrn_mass_antidote_response_source.png` | Tray of sealed antidote ampoules, rugged syringe case, and plain medical cross plate. |
| `cbrn_seal_infection_corridor_source.png` | Latched specimen case behind a closed quarantine gate with one stoppered vial; no biohazard glyph. |
| `cbrn_combined_overmatch_source.png` | Command compass layered with sealed shell, respirator filter, and decontamination nozzle; disciplined integrated emblem. |

## Technology icon prompt

`cbrn_theater_cbrn_headquarters_source.png`: dedicated `64x64` technology emblem with a large command compass over a sealed headquarters map folio, respirator filter, decontamination hose coupling, medical ampoule case, and old radio handset. A blank green wax seal is used instead of a hazard glyph; the subject represents integrated theater CBRN command and is not a resized doctrine or existing technology icon.
