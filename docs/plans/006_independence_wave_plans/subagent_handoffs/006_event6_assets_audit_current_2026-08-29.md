# Event 006 non-portrait visual asset audit

Audit date: 2026-08-29.

Scope: current Event 006 report, news, super-event, GUI, animation, emblem, achievement, idea, decision, focus, and flag surfaces, together with their source, rights, era-fit, manifest, and handoff records.

This is a read-only audit handoff. No GFX, GUI, event, gameplay, flag, PNG, DDS, TGA, source, manifest, or package file was changed other than this dated handoff.

## Authority and method

The accepted presentation requirements are in `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md` and `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`.

The current path authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:5,275,281,285`, which places the consolidated non-portrait sprite definitions in `interface/006_independence_wave_small_assets.gfx` and the Statehood Ledger definitions in `interface/006_independence_wave.gfx`.

The canonical semantic references were checked under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`, including the report, news, super-event, flag, icon, and animation contact sheets and their catalog entries.

The audit compared the current runtime files with the named package manifests and handoffs, parsed the three current Event 006 GFX registries for duplicate sprite names and missing texture paths, checked image dimensions and DDS/TGA headers, inspected the generated event-scene and flag contact sheets, and searched for event consumers.

No game process or live engine validation was run in this read-only asset audit.

## Executive disposition

The current Event 006 non-portrait runtime set is structurally well-covered: all audited report/news/super-event images have the expected dimensions, all 16 achievement IDs have normal/grey/not-eligible triplets, all 102 custom-X candidate flag tags have normal/medium/small base ladders, and the current Event 006 GFX registries have no duplicate sprite names or unresolved texture paths.

The release surface is not cleanly closed. The actionable findings are a strict-grayscale defect in ASSET-004, stale GFX-file claims in multiple package documents, an Event 5/Event 6 AEX flag-scope collision, unapproved Northern/Western Europe ideology-alias files, incomplete but intentionally blocked ASSET-046 emblem coverage, and unresolved historical-rights or era-fit gates on specific generated flag packages.

The current image files are not generic scene placeholders. The generated report/news/super-event contact sheets show distinct period-documentary or alternate-history scenes, with report transparency and required target canvases preserved.

## Current runtime census

| Surface | Current files and dimensions | Audit result |
| --- | --- | --- |
| Event pictures | 14 DDS files under `gfx/event_pictures/006_independence_wave/`: 13 report cards at `210x176` and one news strip at `397x153` | Dimensions and RGBA DDS decoding pass; ASSET-004 has the grayscale finding below. |
| Super-events | `super_event_006_asset_005_league_formation.dds` and `super_event_006_asset_006_revisionist_milestone.dds` at `457x328` | Dimensions, legacy DDS headers, and full-canvas opacity pass. Image 005 is held by audio 23 rights, not by an image gap. |
| Statehood Ledger panel | `gfx/interface/006_independence_wave/independence_wave_status_panel.dds` at `700x500` | Matches `interface/006_independence_wave.gui` and the current panel consumer. |
| Status animations | Four sheets at `320x64`, `192x64`, `256x64`, and `256x64`, plus four `64x64` static fallbacks | Source frames, processed frames, sheets, static fallbacks, GIF previews, contacts, and runtime DDS files are present. |
| Formable emblems | `independence_wave_formable_form_05.dds` and `independence_wave_formable_form_48.dds`, each `128x128` | Both are registered in the current consolidated GFX file; all other planned formable and league emblem rows remain blocked by the package authority. |
| Focus icons | 121 DDS files under `gfx/interface/goals/006_independence_wave/`, all `94x86` | No size failure found in the audited Event 006 tree. |
| Idea icons | 43 DDS files under `gfx/interface/ideas/006_independence_wave/`, all `64x64` | ASSET-049 is present at `gfx/interface/ideas/006_independence_wave/idea_independence_wave_post_release_instability.dds` and registered as `GFX_idea_independence_wave_post_release_instability`. |
| Decision icons | 69 DDS files under `gfx/interface/decisions/006_independence_wave/`: 65 at `32x32` and four category icons at `52x40` | The four `52x40` files are category assets and are correctly treated as such; no wrong-size decision-row asset was found. |
| Achievement icons | 48 DDS files for the 16 matrix IDs, three states per ID, all `64x64` RGBA | 16/16 normal, grey, and not-eligible files exist; Assyria is supplied by the IW-043/IW-058 static-icon package. |
| Candidate flags | 102 unique Event 006 `resolved_tag` values ending in `X`; each has `82x52`, `41x26`, and `10x7` base TGAs | 306 base files exist with uncompressed 32-bit type-2 TGA headers and bottom-left origin; no base-ladder omission was found. |

The three current Event 006 GFX registries contain 397 unique `name` entries with zero duplicate sprite names and no missing referenced texture path in the parsed scope. The 260 runtime image files in the event-scoped `gfx` folders covered by those registries are all referenced by at least one current Event 006 registry entry. Flags and achievements are engine-discovered filename surfaces and are not expected to appear in those GFX registries.

## Core scene coverage

ASSET-001, ASSET-002, and ASSET-003 each have their source PNG, processed `210x176` report card, final DDS, prompt, contact-sheet evidence, and manifest row in `docs/assets/006_independence_wave/generated_event_scenes_manifest.md`. Their current sprites are `GFX_report_event_006_asset_001_wave_summary`, `GFX_report_event_006_asset_002_host_crisis`, and `GFX_report_event_006_asset_003_first_recognition` in `interface/006_independence_wave_small_assets.gfx:129-139`, with event consumers in `events/006_independence_wave.txt` and `events/006_independence_wave_support_events.txt`.

ASSET-004 has its source PNG, processed PNG, final DDS, prompt, contact-sheet evidence, manifest row, and current sprite `GFX_news_event_006_asset_004_league_congress` in `interface/006_independence_wave_small_assets.gfx:153-155`. The event uses it at `events/006_independence_wave.txt:101` for `chaosx.nr6.35`.

ASSET-005 and ASSET-006 have their source PNGs, processed PNGs, final `457x328` DDS files, prompts, decoded reviews, manifest rows, and current sprites in `interface/006_independence_wave_small_assets.gfx:156-163`. Shared super-event image dispatch selects ASSET-005 for visible slot 23 and ASSET-006 for visible slot 24 in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:4-9`.

The generated scene package records these exact source, processed, and DDS hashes:

| Asset | Source SHA-256 | Processed SHA-256 | Runtime DDS SHA-256 |
| --- | --- | --- | --- |
| ASSET-001 | `1a536eba8854331fa3119094f15432c5268cae63e2499c69fcdd73ad43a50801` | `fc9b7c44deeefac21ae6dafd4672ecec7d52d5e4b1ccfa5b2889adf37c9718ef` | `639dcff0f332221d69f23de4197e8aa679544e1151f10eeadcaacd788846f2f2` |
| ASSET-002 | `96d110574182bb83749c9ea9a5304d92c3c0fc73c58ec1f6fb3056233303116d` | `260d01723f797e16947df191e91e2f5caa9fbe8fdcd435987b65dc64944b01e8` | `7292256c6b389a83d56853ad3f27edcf0ac033469bfd2efdfa8c5318c01ed3c6` |
| ASSET-003 | `d4502cba12b34ad7802f83a8e6630ffe5d2690ed2769487815541b9b265a4837` | `5cbd9e4cdf54e3abd277c0fa0e36032b6510a694ff7ad2b45c12ff37fbb59a78` | `664a21255d874a675b9b8365858ee93d4d4e8b2cec055291352dc6e5f298b230` |
| ASSET-004 | `7f11bae7083ba0044ace8ac3de8214c2cdc031f63313f68a380fe44e37364781` | `981f45f949887f14b6ebf6bc319f36e8c9596a41a72e677e652f7756ac36fb03` | `794d5a720bec58837a18f044dffac84bb6cf69b72d956d792ec5b3f67792b14e` |
| ASSET-005 | `ae05125f6441b35f32f7ba59545ceca9e745d06555557b98cd68768746d5d54e` | `4c21ff34255a9727dd3ad0379fbdbd6239a07735b8220051efc25b2a929cd3af` | `e9f4a4f24d7f134e8bd3ef04724a7a04b020f0d9dc559c3c0928ac464cd79781` |
| ASSET-006 | `52be9c45e6f5a09c03eb15fdf4932769212993b2d62dca494cc9334c4b67d67d` | `bb246b65d72dfa40001f1cf031aeeb27ea8c6bca6f1141b08e51f8a1f52ba876` | `a7abec9c821a709bbd6412b2904db6124e59914d739f79944cf0fd40d5187542` |

## Findings requiring follow-up

### P1 — ASSET-004 is not strict channel-equal black and white

`docs/assets/006_independence_wave/processed_png/event_pictures/news_event_006_asset_004_league_congress.png` and the identical decoded runtime DDS are `397x153` RGBA and visually monochrome, but only 30,491 of 60,741 pixels have equal RGB channels, or `50.198%`.

The maximum RGB channel spread is `7`, the mean spread is `1.1211`, and the first non-gray pixel is `(0, 6, 2, 255)`. The runtime corners are opaque as expected for a news strip.

The manifest says ASSET-004 was converted to black and white, but the retained press-grain pass introduced measurable chroma. The generated-event-art owner should reprocess this same source to strict grayscale, regenerate only the processed PNG and DDS, update the two hashes and the manifest record, and preserve the stable sprite basename `GFX_news_event_006_asset_004_league_congress`. No replacement or processing was performed in this audit.

### P1 — AEX has an Event 5/Event 6 flag-scope collision, not a safe deletion target

The Event 006 candidate row for IW-005 lists provisional tag `AEX`, but `resolved_tag` is blank and `tag_policy` is `reuse_vanilla_route_overlay`; the row describes the non-selectable `BEL_flanders` cosmetic overlay. The Event 006 source and GFX handoffs explicitly require that standalone AEX flag paths remain absent.

The current global runtime nevertheless contains:

| Runtime path | Dimensions and header | SHA-256 |
| --- | --- | --- |
| `gfx/flags/AEX.tga` | `82x52`, 32-bit type-2, descriptor `8` | `49D1205A64D792E2EA7BDD04049DA5C89E88BF024F1418F7B50DA27508FA4F5E` |
| `gfx/flags/medium/AEX.tga` | `41x26`, 32-bit type-2, descriptor `8` | `AC656B8F8F86EEED03C7ACDC545980DA31DDC63B87E131DE3BA725E129D699B8` |
| `gfx/flags/small/AEX.tga` | `10x7`, 32-bit type-2, descriptor `8` | `32059E03D495B36142C3CD2A67A1CE366E31CC947C5607D5620FC9F35D270A01` |

These files are not supported by an Event 006 AEX source/processed/final package. However, `common/country_tags/chaosx_countries.txt:18` owns AEX as the Event 5 Basmachi Confederation, and Event 5 has AEX country, focus, idea, decision, leader, and related surfaces. Therefore the files cannot be removed as an Event 006 cleanup without cross-event ownership review.

The exact conflict is that `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md` and `northern_western_europe_generated_art_gfx_handoff.md` require AEX runtime paths to be absent and their builder rejects existing AEX paths, while Event 5 legitimately uses the same global basename. The main agent and Event 5 owner should either make the NWE validation scope-aware or perform a separately reviewed cross-event tag migration. Do not create an Event 006 AEX flag and do not treat the existing files as Flanders art.

### P1 — Northern/Western Europe has 48 unapproved ideology-alias files

The NWE manifest and GFX handoff authorize only unsuffixed ACX, AFX, AGX, and AJX base ladders and explicitly state that no `<TAG>_democratic`, `<TAG>_communism`, `<TAG>_fascism`, or `<TAG>_neutrality` files are created.

The current runtime contains all four suffix aliases for each of ACX, AFX, AGX, and AJX at all three sizes, for 48 files total. Within each tag and size, the four aliases are byte-identical to one another and to the unsuffixed base. This is an unapproved alias surface, not a cross-tag duplicate-base problem.

The unsuffixed base hashes are unique across all 102 Event 006 custom-X candidate tags, so no duplicate or generic base flag was found. The only Event 006 candidate whose suffix aliases differ from its unsuffixed base is AXX; its package explicitly records a parent-accepted alternate-history replacement, so that difference requires package review rather than an automatic overwrite.

The NWE asset owner should remove the 48 aliases or document an accepted route-to-filename contract after the main agent resolves the cross-event flag policy. No aliases were deleted here.

### P1 — ASSET-046 is intentionally incomplete and must not receive generic emblems

The current Event 006 emblem directory contains only:

| Runtime path | Sprite | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` | `GFX_independence_wave_formable_form_05` | `128x128` | `08DDDF415C532570848D022B6E2391E634FD08539BA129E26DB518289A594DB4` |
| `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds` | `GFX_independence_wave_formable_form_48` | `128x128` | `6CFA1B3A342F588F17B42802D189C72E6AAB6F7C0E12CB3349AEDDE8E2ECD222` |

Both are registered in `interface/006_independence_wave_small_assets.gfx:23-29` and have package source, processed, final, contact-sheet, and handoff evidence.

No `form_01` through `form_04`, `form_06` through `form_47`, or league-emblem DDS/sprite is present. `docs/assets/006_independence_wave/manifest.md:131-159` explicitly keeps the unresolved formable identities and per-family emblem set blocked pending final tag, public identity, motif, palette, consumer, and route decisions. This is a known completeness blocker, not an accidental missing texture. The older root `docs/assets/006_independence_wave/gfx_handoff.md:141-146` still says all formable sprites are blocked even though FORM-05 and FORM-48 are live, so the handoff itself also needs reconciliation.

The next owner is the main agent for accepted formable/league consumers and the generated-art owner only after those identities and motifs are approved. Do not invent generic seals, resize flags into emblems, or promote blocked rows.

### P1 — BWX flag ladder is technically complete but rights/era acceptance is blocked

The runtime BWX normal/medium/small ladder exists and matches package copies, but `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw049_bwx_symbol_research_2026_08_15.md` marks it blocked as a historically sourced neutral 1936 flag.

The package source is ImageGen and its only cited design references are Erzya and Moksha Wikipedia pages. The handoff records no provider/source date or source licence for the generated source and no primary or official source attesting an independent Erzya–Moksha federal flag in 1936. The 1934 Mordovian ASSR flag is an archive-backed Soviet reference, not a neutral federal identity. The existing ladder must remain evidence-only until the parent accepts a clearly labelled alternate-history synthesis and resolves identity, map, and rights gates.

This is a source/era blocker, not a missing-file gap. Do not promote the existing BWX TGA files or call the design historically attested.

### P1 — Fourteen chunk-3 flag ladders remain needs-user-review

`docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk3/manifest.md:9-24` marks these generated flag ladders `needs_user_review`: `GMX`, `GZX`, `HAX`, `HDX`, `HEX`, `IBX`, `GIX`, `GRX`, `HFX`, `HGX`, `HKX`, `HPX`, `HSX`, and `HUX`.

Their normal/medium/small TGAs exist and have source masters, processed previews, hashes, and uncertainty notes, but the notes explicitly cite alternate-history synthesis, lack of a single 1936 historical flag, community or institutional review, simplified seals, or modern-symbol exclusion. Their technical presence does not clear the source, identity, or community-review gate.

The remaining chunk-3 tags `GTX`, `GYX`, and `HCX` are marked `handed_off` in the package manifest. The COX–EBX package is also technically complete and records generated synthesis or historical-reference caveats per row; map-only rows `HYX`, `DKX`, and `DLX` remain uncertainty-bearing and are not exact historical standards.

### P2 — Broad flag metadata does not establish per-reference licence/date clearance

The AKX–CLX package and COX–EBX package retain ImageGen source masters, processed ladders, final TGA copies, prompts, design-reference URLs, hashes, and TGA validation. Their machine-readable validation records do not contain per-row `license`, `author`, `archive`, or `source_date` fields.

The package manifests state when a design is generated, historical, or alternate-history and provide explicit notes for special cases such as AXX and BBX, but `handed_off` is a technical delivery state rather than a blanket rights clearance. Treat unlisted reference licences and dates as unknown rather than public domain. The source/rights owner should add or confirm row-level rights and era notes before admitting historically grounded designs.

### P2 — Status-animation manifest disagrees with current `play_on_show`

`docs/assets/006_independence_wave/animations/manifest.md:7` records `play_on_show = no` for parent-controlled state display, while `interface/006_independence_wave.gfx:67,70,73,76` and `docs/assets/006_independence_wave/animations/gfx_handoff.md:26,31` set and document `play_on_show = yes` for the explicit animated siblings.

The animation files themselves are complete and the current GUI uses the state strips and animated siblings at `interface/006_independence_wave.gui:23-31`. This is documentation drift, not an image or frame defect. The animation owner should reconcile the manifest to the current accepted GUI behavior.

### P2 — Multiple package handoffs still name removed GFX parser files

The current source-of-truth map says the 2026-08-26 merge moved the FORM-03, Pacific, Mediterranean, IW-043/IW-058, Rhineland/Bavaria, and Wallonia/Frisia sprite blocks into `interface/006_independence_wave_small_assets.gfx` and removed the old parser files.

The following package records still claim the removed files are current owners:

- `docs/assets/006_independence_wave/generated_event_scenes_manifest.md:47` and `generated_event_scenes_gfx_handoff.md:5` cite `interface/006_independence_wave_event_pictures.gfx`.
- `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md:18,37`, its metadata JSON, and `gfx_runtime_handoff.md` cite `interface/006_independence_wave_event_pictures.gfx`.
- `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/manifest.md:10` and `gfx_handoff.md:3` cite `interface/006_independence_wave_mediterranean_assets.gfx`.
- `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md:114` cites `interface/006_independence_wave_form05.gfx`.
- `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifests/asset_manifest.json:1126,1176` and `gfx_handoff.md:24` cite `interface/006_independence_wave_event_pictures.gfx`.
- `docs/assets/006_independence_wave/manifest.md:172` and related ASSET-048 prose repeat the removed event-picture registry claim.

The live sprite names and texture paths are present in `interface/006_independence_wave_small_assets.gfx`, so this does not indicate an engine-facing missing texture. The main agent or documentation curator should update these path claims while preserving the dated removed-file references as historical provenance. No GFX registry was edited here.

## Intentionally absent or dormant assets

IW-057 FER has no Event 006 runtime flag or emblem by design. `006_event6_iw057_fer_symbol_source_gate_2026-08-28.md` is `BLOCKED / FAIL-CLOSED / NO RUNTIME SYMBOL` because no directly attested neutral 1936 FER identity was found and the strongest 1920 source has unresolved underlying scan rights. Do not reuse vanilla FER, Event 5 FEV, or create a synthetic fallback.

The 17 tags in `docs/assets/006_independence_wave/reservation_flags_2026_08_02/manifest.md` are dormant `reservation_art`. Their normal/medium/small runtime ladders exist, but the manifest explicitly says they are fictional symbolic designs with no playable package, country history, localisation, event, or GFX wiring. Their lack of consumer is intentional and must not be treated as an orphan requiring promotion.

The 13 candidate rows with blank `resolved_tag` are intentional overlay-only routes, including IW-005 Flanders, and must not receive standalone Event 006 flag basenames. Existing vanilla or Event 5 files with a colliding basename require cross-event ownership review before cleanup.

## Achievement, animation, and report package disposition

All 16 IDs in `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv` have normal, grey, and not-eligible DDS files under `gfx/achievements/`, all `64x64` RGBA. Source and processed files exist for every ID; `chaosx_006_assyria_survives` is correctly supplied by `iw043_iw058_static_icons_2026_07_18` with its own final DDS and validation records. The achievement surface has no missing or wrong-size non-portrait asset found in this audit.

ASSET-040 through ASSET-043 are complete as real frame-by-frame packages under `docs/assets/006_independence_wave/animations/`. The build report records source frames, processed frames, sheet/static/GIF/contact outputs, hashes, 64x64 frame size, 5 FPS, 200 ms frame timing, and runtime paths. The only finding is the `play_on_show` documentation mismatch above.

ASSET-048 regional report variants are present at the expected `210x176` size with source/processed/runtime evidence in the AFX, Mediterranean, FORM-03, IW-043/IW-058, and Rhineland/Bavaria packages. Current event consumers include AFX at `events/006_independence_wave_support_events.txt:613,666,723`, Mediterranean at `:794-1004`, FORM-03 at `events/006_independence_wave.txt:230-525`, IW-043/IW-058 at `events/006_independence_wave_support_events.txt:365,1678-3027`, and RHI/BAY at `:1287-1619`. Their package manifests are technically complete; only the stale owning-GFX paths listed above require documentation reconciliation.

## Character portrait boundary

All character, leader, commander, officeholder, institutional portrait, and portrait-source files were excluded from this audit, including portrait-looking files in mixed package folders. They are owned by `chaosx_portrait_creator` and must not be counted as missing or defective Event 006 non-portrait assets here.

No Event 006 advisor icon, dossier card, commander-small, or other portrait-derived UI asset was inferred from the GUI, focus, idea, decision, or event consumers.

## Next-owner handoff

The main agent owns final integration and should:

- coordinate the ASSET-004 strict-grayscale reprocess and hash/manifest update;
- resolve the AEX cross-event basename ownership before changing the NWE builder or any global flag files;
- reconcile stale package GFX paths to `interface/006_independence_wave_small_assets.gfx`;
- keep ASSET-046 blocked until accepted formable and league identities have approved motifs and stable consumers;
- preserve FER fail-closed and dormant reservation-art boundaries; and
- keep ASSET-005 image registration held behind the separately blocked audio-23 rights gate.

The non-portrait source/rights owner should review BWX, the fourteen chunk-3 `needs_user_review` flags, row-level licences/dates for generated flag references, and the 48 unapproved NWE ideology aliases. No generated replacement, fallback, deletion, or promotion was performed in this audit.

## Simplifications, omissions, and blockers

This handoff deliberately does not process ASSET-004, delete AEX or ideology-alias files, create emblems, generate flags, copy external references, alter GFX registries, inspect portrait readiness, or run live game validation. Those actions require the owners and approvals listed above.
