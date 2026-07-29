# Event 018 asset, audio, and super-event re-audit handoff

## Verdict

**PASS.**

The fresh asset/audio/super-event audit found no blocking asset, provenance, rights, uniqueness, registration, consumer, selector, trigger, or documentation mismatch. No fallback or simplification was accepted. The selected-field stills and Vhorruk still portrait are required accessibility/static presentation fallbacks paired with complete real-frame animation packages; they are not substitutes for missing animation.

- Audit date: 12 July 2026
- Audit mode: read-only static and binary inspection
- Gameplay launch: not performed, as required
- Authorized edit: this handoff only

## Sources and audit boundary

The audit used the complete chaos-redux-event-assets, chaos-redux-frame-animation, chaos-redux-super-events, and chaos-redux-subagents skills. It read Event 018 specification part 8, the asset, super-event, and achievement prompts, the acceptance matrix, the current asset and audio manifests, animation manifests, provenance ledger, GFX handoffs, specialist handoffs, and the reconciled combined super-event research.

The required offline Paradox wiki snapshot was consulted, including the core scripting pages and the graphical asset, sound, music, interface, scripted GUI, portrait, achievement, and national-focus pages. Relevant current vanilla documentation and vanilla GFX, sound, and music precedents were also inspected. No online Paradox wiki page was used.

The source-of-truth documents were re-read after the final documentation alignment:

- docs/assets/018_resources_found/manifest.md — SHA-256 371ef7163519f5658b027d9d7b73a746198e32e34e8cb983336a66c8f993aa3f
- docs/assets/018_resources_found/animations/selected_field_ui/manifest.md — SHA-256 24ebb757e96074b0806ba0de7d8dd0a0d7d2181ee7dd940aa04a4485a73cec7d
- docs/assets/018_resources_found/icon_generation_provenance_ledger.md — SHA-256 dff90959c1f6a212d2223d9598d952d5a3db1f8dfdd8b1f1514e0e80bc96a3fc
- docs/super_events/018_resources_found/overview.md — SHA-256 29aa19fe38623600c0378477e59a5d2d29d9b60bd9d4ff9286454b226fba1a29

The final comparison initially found one stale documentation cell: the consolidated manifest named interface/018_resources_found.gfx for the three super-event registrations even though the live definitions are in interface/chaosx_super_events.gfx. The parent corrected that cell during this audit. The current manifest bytes and all three live registrations were re-read after the correction; the mismatch is resolved and is not a remaining blocker.

## Icon and category-picture provenance

The exhaustive ledger contains exactly 150 rows:

| Family | Ledger rows | Unique source PNGs | Unique processed PNGs | Unique runtime DDS files | Runtime size |
| --- | ---: | ---: | ---: | ---: | ---: |
| Focus icons | 65 | 65 | 65 | 65 | 94 by 86 |
| Idea/state icons | 36 | 36 | 36 | 36 | 64 by 64 |
| Decision/category icons | 44 | 44 | 44 | 44 | 32 by 32 |
| Category pictures | 5 | 5 | 5 | 5 | 114 by 101 |
| Total | 150 | 150 | 150 | 150 | family-specific |

All 150 source, processed, and runtime files exist. Source, processed, runtime-file, and decoded-pixel hashes are unique within every family and across the 150-asset set. Every processed PNG is pixel-identical to its decoded DDS. Runtime DDS files are one-surface 32-bit BGRA with the documented channel masks and no mip chain; transparent icon families retain transparent unused pixels and category pictures are opaque.

Every one of the 150 preserved source PNGs contains binary C2PA assertions naming OpenAI Media Service API and trainedAlgorithmicMedia, plus C2PA manifest, claim, signature, data-hash, certificate-status, and timestamp structures. Manifest URNs and XMP instance IDs are unique across all 150. The binary history includes either the SSL.com or Trufo C2PA signing chain and OpenAI timestamp evidence for every source. Provenance was therefore established from the files rather than inferred from appearance or filenames.

The ledger handles the historical prompt evidence honestly. It records the preserved family brief plus one asset-specific subject per row and explicitly states that per-call verbatim API request bodies were not retained. It does not invent quotation-level prompt history. It also discloses that the production brief's named focus, idea, and decision reference folders are absent in this checkout and records the surviving Event 018 contact sheets plus vanilla libraries inspected under the skill's missing-reference-folder rule. No source is misrepresented as externally sourced, public-domain, archival, user-provided, or copied reference art.

All 150 sprite names are defined exactly once in interface/018_resources_found.gfx with the matching runtime path. Live consumer parity is exact:

- 65 national focuses use 65 unique matching GFX_focus_DHO_* sprites.
- 36 unique idea/state sprites cover 37 live picture tokens; cave_burrow_war_doctrine is the one intentional shared picture.
- 125 visible decisions and missions have 125 exact mappings in gfx_handoff.md and use 39 action-family sprites.
- The nine hidden scheduler clocks are intentionally iconless and are not counted among the 125 visible mappings.
- Five decision categories each have one exact icon mapping and one exact category-picture mapping.

No omitted, stale, duplicate, cross-family-resized, or placeholder icon mapping was found. The four contact sheets were visually inspected and show distinct, readable, family-appropriate identities.

## Other visual assets and runtime consumers

The generated-event-art package is complete and distinct:

- 10 report images at 210 by 176, all unique, with transparent report masks and exact PNG/DDS parity.
- 6 news images at 397 by 153, all unique, true grayscale processed masters, and exact PNG/DDS parity.
- 3 super-event images at 457 by 328, all unique and used only by their assigned Event 018 slot.
- Four large Oth-Kesh portraits at 156 by 210, three commander portraits at 50 by 67, and the separate eight-frame Vhorruk animation sheet.
- Six original flag identities delivered at 82 by 52, 41 by 26, and 10 by 7, for 18 uncompressed 32-bit TGA files with exact processed-pixel parity.

The generated report, news, super-event, portrait, and achievement sprites are each registered once at the documented runtime path. Vhorruk's static leader portrait is consumed by DHO_vhorruk; the separate animated sprite is consumed by the Event Details portrait selector.

The achievement registry contains exactly 15 Event 018 achievement identities. Each has a unique generated source master and unique completed, grey, and not-eligible runtime state, for 45 unique DDS hashes and 45 exact registrations. All states are 64 by 64 with decoded pixel parity. The grey transform and unavailable-state alpha composite match the documented canonical operations, including the canonical red-X overlay.

## Real-frame animation package

The selected-field package contains 56 unique source frames and 56 unique processed frames:

| State | Frames | FPS | Runtime sheet |
| --- | ---: | ---: | --- |
| Seal | 10 | 8 | 1280 by 128 |
| Unsafe | 10 | 8 | 1280 by 128 |
| Disturbance | 12 | 9 | 1536 by 128 |
| Breach | 12 | 10 | 1536 by 128 |
| Sealing | 12 | 8 | 1536 by 128 |

Every 128 by 128 sheet segment is pixel-identical to its processed frame, every review GIF has the exact frame count, and every static fallback is pixel-identical to approved frame 000. Panel, Suspended, and Closed have their own generated sources and exact PNG/DDS parity. The source/processed contact sheets visibly show separately redrawn machinery, supports, fractures, rubble, silhouettes, concrete, pumps, shutters, tools, dust, hoses, and related local scene changes; the animation is not produced by translating, scaling, rotating, warping, blurring, recoloring, or filtering one still.

The live GFX has the exact frame counts, FPS values, looping, play-on-show, and zero pause-on-loop settings. The live GUI consumes all five animated sprites, all five static fallbacks, Panel, Suspended, and Closed. Scripted GUI triggers select animation or static presentation through resources_found_animations_disabled. Closed is presentation-only history sourced from resources_found_last_closed_field and is not reassigned to the active field pointer.

Vhorruk likewise has eight unique 156 by 210 generated source frames, eight unique processed frames, an exact horizontal DDS sheet, an eight-frame preview, and a static portrait equal to approved frame 000. Contact-sheet inspection shows substantive redrawing of the face plate, slits, dust, and lighting rather than transform-only motion.

## Audio IDs 54–56

All three active cues are real performances, unique by file hash and decoded audio, and within the required 60–120-second range:

| Audio ID | OGG profile and SHA-256 | WAV profile and SHA-256 | Decoded OGG PCM SHA-256 |
| ---: | --- | --- | --- |
| 54 | 115.000000 s, Vorbis, 44.1 kHz stereo; 88d3b749fd51bcc106daf352ae9791c51d3452e7bce9a01ebf8971dad57385c0 | 115.000000 s, PCM s16le, 44.1 kHz stereo; daf27599720d281eaa96fe828dc38337553026054b634a57d652a41236050575 | 4ab371aa335a3689413a71739284e0041b8d49f366bca0a32ea594e126eb31b1 |
| 55 | 110.000000 s, Vorbis, 44.1 kHz stereo; b6888c95658dafbf40dd822550d05c505e9a653ce4daa01191e00a6500c28215 | 110.000000 s, PCM s16le, 44.1 kHz stereo; f0ee745abfbe432cd26b37ad14fb800ab4bcbf77e442eb11d06f8f8f991e1266 | 17d07bdeae93b40ecd5a5b3276943149de05b2eca187aef8bea981ecbd002eaa |
| 56 | 109.000000 s, Vorbis, 44.1 kHz stereo; b1131b009a715c20598bf720d485c05038d583accbc1e46744dbc182d1f7631e | 109.000000 s, PCM s16le, 44.1 kHz stereo; 9be248a28861b96a8c454ab729af8d710727c2b3289eb4820efa98b1cba8fcc9 | 40dd0c8bed140da0f2039c3a631c89b50b1e3ddae52c01d058fb3bd30951bd7b |

The WAV files have matching sample counts, matching quarter-sine fade/edit structure, and zeroed tails. Their decoded waveforms correlate at 0.9988, 0.9983, and 0.9995 respectively, which is consistent with the WAV master and lossy OGG carrying the same three edits. All six final files decode.

Rights and source disposition is clean:

- ID 54 is Mussorgsky's Bydło performed by Skidmore College Orchestra from the Musopen/VRTS-confirmed worldwide public-domain release.
- ID 55 is Brahms Symphony No. 1, movement I, with Czech National Symphony Orchestra embedded identity and Musopen Symphony Orchestra publication identity. The file-specific recording grant is CC0 1.0 Universal and provides the required worldwide waiver for redistribution and adaptation.
- ID 56 is Chopin's Prelude in E minor, Op. 28 No. 4, performed by Ivan Ilić under CC BY 3.0. The required performer/composer credit, source and licence links, excerpt/fade/gain/tail/encoding change notice, non-endorsement statement, and no-additional-restrictions treatment are retained in the audio manifest, split research, combined research, shared audio-package documentation, Event 018 documentation, and music catalogue.

All nine frozen source/deed/legal-code snapshots exist and match the SHA-256 inventory in source/audio/license_evidence/README.md. The three preserved source masters match their documented hashes and profiles. The superseded Debussy/USAF file is retained only as rejected research history; it has no Event 018 runtime definition, helper, localisation title, catalogue row, or final-cue mapping. The live stable ID 55 mapping is Brahms/CC0 everywhere.

Runtime audio wiring is exact: 18 sound wrappers provide six volume variants per ID at 0.67, 1.33, 2.00, 2.67, 3.33, and 4.00. Each family points to the correct final filename/base sound. Display IDs 82–84, audio IDs 54–56, wrapper names, sound-track names, and runtime filenames remain stable. The shared player dispatches the correct sound path according to volume.

## Combined super-event reconciliation

The combined research document agrees with the live implementation:

| Slot | Audio | Title | Image |
| ---: | ---: | --- | --- |
| 82 | 54 | THE OTH-KESH HOST RISES | GFX_super_event_018_cave_emergence |
| 83 | 55 | THE DEEP WAR CROSSES THE SEAS | GFX_super_event_018_world_end |
| 84 | 56 | THE LAST DEPTH IS SEALED | GFX_super_event_018_global_defeat |

For each slot, common/scripted_localisation/chaosx_scripted_localisation_super_events.txt contains exactly five matching selector entries: image, title, quote, button, and description. The three sprites are each defined once in interface/chaosx_super_events.gfx and resolve to distinct 457 by 328 runtime files. The .t, .d, .q, and .a localisation in 018_resources_found_system_l_english.yml agrees with the combined research, including the intentionally lower-case opening of the Aeschylus terminal clause.

The three live quotations and attributions were checked against their direct primary-source pages: Job 28:5 in the World English Bible, the Buckley Project Gutenberg Prometheus Bound text, and Herodotus Histories 1.87.4 in the Godley Perseus text. The combined note records their public-domain or licensed source disposition and preserves rejected quotation context separately.

The runtime trigger contract also agrees:

- Slot 82 is the one-shot first successful Oth-Kesh country emergence.
- Slot 83 is emitted only by the terminal world-end effect reached from DHO_the_world_opens_below after its world-end gates are rechecked.
- Slot 84 requires the global/near-global defeat eligibility flag and complete defeat/cleanup path; regional containment does not emit it.

The constants bind displays 82, 83, and 84 to audio 54, 55, and 56 for fourteen days. Each emission sets the matching global audio ID and calls the shared player helper.

## Waived live-session checks

The following checks were deliberately not claimed because this task did not launch HOI4:

- final in-engine super-event mask composition and display scaling;
- live selected-field and Vhorruk animation playback;
- live audio loudness, volume-mode behavior, transitions, and audible tail behavior;
- fourteen-day display timing and end-to-end event sequencing.

Static file inspection, decoded pixel/audio analysis, selector/consumer reconciliation, and trigger review found no issue that would block those live-session checks.

## Simplifications, omissions, and blockers

None. The audit found no missing requested asset, no placeholder, no unapproved substitute, no unresolved source or licence caveat, no omitted AI/runtime mapping within this audit surface, and no stale Event 018 asset/audio/super-event documentation. Accessibility/static fallbacks are present exactly as required and are backed by complete real-frame animation packages.
