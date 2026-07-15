# Event 014 Localisation and Asset Consolidation Reaudit

Date: 2026-07-15
Scope: current post-refresh, post-runtime-consolidation Event 014 source and shipped assets
Verdict: **PASS for the audited content. No P0-P3 findings remain.**

This report supersedes the asset-rate and registry counts in `event014_localisation_asset_reaudit_2026-07-15.md`. The older report was corrected to the live 12 FPS portrait rate and now points here.

## Priority findings

| Priority | Remaining | Disposition |
| --- | ---: | --- |
| P0 | 0 | No secrecy leak, missing live asset, broken registration, or required fallback found. |
| P1 | 0 | No incomplete flag ladder, portrait set, animation package, super-event visual/audio package, or localisation family found. |
| P2 | 0 | No placeholder, cross-type art reuse, duplicate localisation key, stale `:0`, duplicate sprite name, or unresolved texture path found. |
| P3 | 0 | No unresolved low-priority content or documentation finding remains. |

### Non-finding tooling note

The optional `hoi4.event_inspect` and `hoi4.gui_*` artifact request encountered `ARTIFACT_STORAGE_LIMIT`, and a root-level retry encountered a closed MCP transport. These were external tooling-availability conditions, not Event 014 content defects or audit findings. Direct inspection of source, localisation, GFX, decoded textures, manifests, hashes, contact sheets, and audio fully covered this audit scope, while current focus MCP evidence exists separately. No priority is assigned to this note.

## Required-reference basis

The audit used the offline wiki pages required by `AGENTS.md`, including Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On Actions, Event Modding, Decision Modding, Idea Modding, AI Modding, Graphical Asset Modding, Interface Modding, Scripted GUI Modding, Music Modding, Sound Modding, and Portrait Modding. It also checked the current vanilla documentation and vanilla precedents for characters, scripted GUI, `frameAnimatedSpriteType`, and `buttonstate_blendframes.lua`.

## Secrecy closure

The public boundary is `has_global_flag = cannibalism_reveal_complete`. The consolidated runtime preserves the boundary across every requested surface.

| Surface | Current proof |
| --- | --- |
| Identity, face, title, and country | The ordinary-country creation effect sets `cannibalism_reveal_complete` before state transfer, CBL creation, focus loading, character promotion, threat, super-event emission, and public events. The Wendigo transformation likewise sets the flag before its cosmetic identity, character, focus, reports, news, and audio. The Hannibal characters exist roleless in country history and receive a visible country-leader role only in those post-flag effects. |
| Scenario selection | The two scenario-facing branches remain the generic **Hunger Lines** and **Convergence**. Their names and descriptions contain no Hannibal identity. |
| Event Details and evolutions | Scripted localisation has an explicit pre-reveal generic branch and a post-reveal identity branch. Evolution III title/description branches require both their stage state and `cannibalism_reveal_complete`, including history/detail views. |
| Focus trees | The ordinary unified tree requires the unified country and reveal flag and is loaded after the flag is set. The Wendigo tree requires the transformed country, reveal flag, and character. Registering art in GFX does not surface it before those trees can open. |
| Decisions and GUI | Unified decision access routes through `cannibalism_unified_decisions_are_open`, which requires the reveal. Wendigo access and counterwar surfaces require the reveal and route state. The ordinary revealed GUI and the Wendigo GUI each test the reveal explicitly. |
| Achievements | Native achievement entries remain hidden. Tracker entries whose wording or icon can identify Hannibal are reveal-gated; tracker 13 and its completion trigger require the reveal, while Wendigo rows additionally require the route. |
| Reports and news | Pre-reveal report/news images are generic field, burial, containment, ration, commune, island, and warlord scenes. The public-reveal panel containing a bald commander is only used by the gated reveal event. Reveal reports, captured-Hannibal report event 81, and news events 90/91 require the reveal. |
| Super-events and audio | IDs 49, 50, 52, and 53 all require the reveal in their emitters. Their audio is invoked by those emitters; zero-weight music station registration does not expose it through normal station selection. Internal filenames and comments are not player-facing. |

Search closure:

- `localisation/english/014_cannibalism_l_english.yml` has zero ancient-general, Carthaginian, or Punic disclaimer text. No such disclaimer is used to excuse an early identity leak.
- The exact legacy label `Prison Host` and the identifier `prison_host` have zero matches in current Event 014 runtime/localisation/spec surfaces. Remaining repository matches occur only in historical removal/exclusion documentation.
- Portrait prompts, manifests, decoded portraits, and both warlord contact sheets contain no prison, jail, cell, cage, barred-window, sacred/religious motif, or actor-likeness treatment.

## Flag source and runtime proof

Canonical evidence is in:

- `docs/assets/014_cannibalism/flags_refresh/generation_evidence.json`
- `docs/assets/014_cannibalism/flags_refresh/validation.json`
- `docs/assets/014_cannibalism/flags_refresh/contact_sheets/source_vs_final_contact_sheet.png`
- `docs/assets/014_cannibalism/flags_refresh/contact_sheets/final_runtime_flags_contact_sheet.png`

The current corpus has exactly 65 design stems and 65 generation records, all marked `built-in-imagegen`. Every recorded built-in cache output, prompt file, and accepted source exists. Cache output and accepted source bytes match; prompt/source hashes match the evidence; and all 65 accepted source hashes are unique. No procedural or simple-shape substitute was used.

The shipped ladder is exact:

| Tier | Count | Dimensions | TGA properties | Palette |
| --- | ---: | --- | --- | --- |
| Normal | 65 | 82x52 | type 2, 32-bit RGBA, descriptor 8, opaque alpha | exactly 5 colours each |
| Medium | 65 | 41x26 | type 2, 32-bit RGBA, descriptor 8, opaque alpha | 4-5 colours each |
| Small | 65 | 10x7 | type 2, 32-bit RGBA, descriptor 8, opaque alpha | 3-5 colours each |

There are exactly 195 live TGAs for the CBA-H, CBL, and `ZZZ_CANNIBALISM_HANNIBAL` family, with 195 unique SHA-256 hashes. Fresh visual inspection found 65 distinct, flat, flag-like compositions with readable field/emblem hierarchy at the small tiers. The validation record is `passed` with revision `built-in-imagegen-regeneration-2026-07-15`.

## Warlord portrait proof

The live leader directory has exactly 60 DDS files: 56 warlord portraits, canonical `hannibal.dds`, canonical `hannibal_wendigo.dds`, and the two portrait animation sheets. No copied `hannibal_static.dds`, Wendigo static duplicate, or other non-contract leader DDS remains.

| Set | Count | Runtime format | Uniqueness and lineage | Visual disposition |
| --- | ---: | --- | --- | --- |
| CBA-D | 28 | 156x210 RGBA DDS | 28 unique accepted sources, 28 unique processed outputs, and every live DDS decoded-pixel-matches its processed source. All 28 accepted built-in ImageGen cache outputs are present and byte-match. The ledger records 43 invocations: 28 accepted, 10 superseded, 5 blocked, and no fallback. | Pass. `cba_cbd_warlords_contact_sheet.png` shows distinct bald/feral faces, poses, props, and actions rather than palette swaps. |
| CBE-H | 28 | 156x210 RGBA DDS | 28 unique accepted sources, 28 unique processed outputs, and every live DDS decoded-pixel-matches its processed source. All accepted cache outputs are present and byte-match; 27 were accepted on the first attempt and one on the second, with no fallback. | Pass. `processed_contact_sheet.png` shows a second distinct set of bald/feral faces, props, and actions. |

The two required review sheets are:

- `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/cba_cbd_warlords_contact_sheet.png`
- `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/processed_contact_sheet.png`

Across the 56 portraits, the visible differentiation includes dog tags, gloves, teeth, masks, skull/cup objects, a spoon, coin, puppet, rat, papers, tools, and distinct hand actions. They use ruined/outdoor command environments, not prisons. No sacred iconography or identifiable actor likeness was found.

## Canonical Hannibal statics and portrait animation

Live static sprites bind directly to the canonical DDS files:

- `GFX_portrait_CBL_hannibal` and its revealed static alias use `gfx/leaders/014_cannibalism/hannibal.dds`.
- `GFX_portrait_ZZZ_hannibal_wendigo` and its Wendigo static alias use `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- Ordinary animation uses the 1872x210 sheet: 12 frames of 156x210 at **12 FPS**.
- Wendigo animation uses the 2496x210 sheet: 16 frames of 156x210 at **12 FPS**.
- Both live portrait declarations use `buttonstate_blendframes.lua` for smooth interpolation.

Decoded-pixel comparison proves that each canonical DDS, its processed static, and sheet frame 000 are identical. Each sheet is an exact horizontal concatenation of the declared processed frames. The live sheets pixel-match the package sheets. Ordinary and Wendigo source-frame sets are internally unique, as are both processed-frame sets.

Canonical hashes:

| Asset | SHA-256 |
| --- | --- |
| `hannibal.dds` | `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88` |
| ordinary sheet DDS | `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587` |
| `hannibal_wendigo.dds` | `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717` |
| Wendigo sheet DDS | `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b` |

Visual sequence review confirms semantic action: the ordinary portrait raises a fork, licks/bites, chews, and resets; the Wendigo portrait opens its jaw, captures and crushes a fragment with its tongue, chews, swallows, and resets. Neither sequence is a transform-only animation.

## Complete animation inventory

All 14 packages contain an animation brief/frame plan, separately authored source frames, processed frames, exact sheet PNG/DDS, static PNG/DDS fallback, GIF preview, contact sheet, manifest, and frame inventory. All 114 nonportrait source frames have unique hashes, as do their processed outputs; the ordinary/Wendigo portrait packages add 12 and 16 unique source frames respectively. Package DDS files pixel-match their PNG counterparts, live DDS files match their package deliverables, sheets are exact horizontal concatenations, and static fallbacks equal frame 000.

| Package | Frames | FPS | Frame size | Sheet size | Semantic change verified |
| --- | ---: | ---: | --- | --- | --- |
| early warning seal | 8 | 8 | 64x64 | 512x64 | seal/alert activation |
| cult cohesion emblem | 8 | 8 | 64x64 | 512x64 | cohesion state progression |
| network threads | 12 | 8 | 824x120 | 9888x120 | network lines propagate across the strip |
| island alert | 8 | 8 | 64x64 | 512x64 | island warning state changes |
| selected target overlay | 6 | 6 | 374x64 | 2244x64 | target-selection overlay resolves |
| critical Larder glow | 8 | 8 | 64x64 | 512x64 | critical reserve warning changes |
| frenzy border | 8 | 8 | 142x54 | 1136x54 | border intensity advances |
| warlord route emblem | 8 | 8 | 94x86 | 752x86 | route emblem assembles/changes state |
| unification seal | 12 | 8 | 94x86 | 1128x86 | seal progresses to unification |
| ordinary terminal frame | 12 | 8 | 438x40 | 5256x40 | terminal world-end strip advances |
| Wendigo anchor pulse | 12 | 8 | 64x64 | 768x64 | anchor state pulses through separately authored frames |
| Wendigo terminal frame | 12 | 8 | 438x40 | 5256x40 | winter terminal strip advances |
| ordinary Hannibal portrait | 12 | 12 | 156x210 | 1872x210 | fork/bite/chew/reset action |
| Wendigo Hannibal portrait | 16 | 12 | 156x210 | 2496x210 | jaw/tongue/crush/chew/swallow/reset action |

Every live animation declaration has the exact declared frame count/rate, loop/play-on-show behavior, and `buttonstate_blendframes.lua` binding. Fresh contact-sheet inspection confirmed that none of the 14 is a still image animated only through movement, scaling, rotation, warping, blur, recolouring, or filtering.

## Super-event visual and audio closure

The four live 457x328 DDS images are unique, decoded-pixel-match their processed PNGs, and are registered exactly once in `interface/chaosx_super_events.gfx`:

| ID | Image disposition | Image SHA-256 | Gate |
| ---: | --- | --- | --- |
| 49 | pursuit/convergence action: a commander directs an attack from a truck while civilians flee | `b73a9e9274b411c1a637d01641a27c9aab69b05fdc25340106f3371aca760014` | reveal flag plus once-only emitter |
| 50 | ordinary world-end action: a capital is overrun | `2e6ab8e3af541a75d143885f12fbefd8d3c784a9bb998d69e77c2e10d132d512` | reveal + ordinary world-end + global world-end + once-only emitter |
| 52 | defeat aftermath action: breakthrough and rescue | `61cf83f3c533b219f56345abe8f550725925dad5ca5ab92fdb0ab88f244eacd9` | eligible defeat aftermath + reveal + not world-end + once-only emitter |
| 53 | Wendigo world-end action: a frozen pack hunt | `a7f5288912ef82c1539d5ee8c83a1125afb4943bb3a31691311333f9c76214fd` | reveal + Wendigo world-end + global world-end + once-only emitter |

The ID 52 eligibility gate additionally requires global victory, at least 5,000k consumed population, at least 12 maximum controlled states, at least 365 days of duration, and at least two contributors. The four source prompts, accepted built-in ImageGen cache outputs, repository sources, processed files, and final DDS images are retained in `docs/assets/014_cannibalism/static_event_art_imagegen/`; the accepted cache outputs byte-match their sources. The contact sheet is `contact_sheets/super_events_final_dds_contact_sheet.png`. No actor likeness or sacred motif is present.

Each ID has its own music asset and sound wrapper; no cue is reused:

| ID | Runtime audio | OGG duration | Format | Rights disposition |
| ---: | --- | ---: | --- | --- |
| 49 | `Danse macabre`, Stokowski (1925) | 114.0 s | Vorbis, 44.1 kHz stereo | public domain source documented |
| 50 | `Siegfried's Funeral March`, U.S. Marine Band | 120.0 s | Vorbis, 44.1 kHz stereo | U.S. federal public-domain source documented, with jurisdiction note |
| 52 | Fauré `Élégie`, Goldstein/Kalman | 116.1 s | Vorbis, 44.1 kHz stereo | CC BY-SA 2.0 attribution/change notice retained |
| 53 | Grieg `Death of Åse`, Musopen performance | 118.0 s | Vorbis, 44.1 kHz stereo | worldwide public-domain disposition documented |

The four archival WAVs are PCM s16le, 44.1 kHz stereo; all four WAV hashes and all four OGG hashes are unique. Each ID resolves through six expected music helpers, six sound wrappers, its own scripted-localisation image/title/quote/button/description mapping, and a zero-chance 1.5 station entry. The track table has four rows. Five preserved rights/evidence HTML files cover the four sources and the CC BY-SA legal code. The canonical research record is `docs/super_events/014_cannibalism_super_event_audio_research.md`. No generated audio, default cue, reused cue, or undocumented fallback is present.

## GFX and localisation registry closure

The three Event 014 GFX registration surfaces are:

1. `interface/014_cannibalism.gfx`
2. `interface/chaosx_pictures.gfx`
3. `interface/chaosx_super_events.gfx`

Fresh parsing of the Event 014 declarations found:

- 812 texture references and 812 unique sprite names;
- 598 unique texture paths, all 598 present;
- 598 unique SHA-256 hashes for those 598 paths, so no cross-family or cross-type art reuse exists;
- zero duplicate sprite names;
- 204 focus textures, 62 idea textures, 135 decision/category textures, 54 achievement textures, 60 leader textures, 29 event/news pictures, 4 super-event pictures, 26 GUI statics, and 24 nonportrait animation static/sheet textures.

Intentional same-semantic aliases are limited to the expected cases: base/shine focus sprites point to their own focus texture; default/region warlord portrait aliases point to the intended leader portrait; and revealed/static Hannibal portrait aliases point directly to the canonical DDS. They are not cross-type reuse.

The achievement set is exactly 18 bases with an exact normal/grey/not-eligible triplet for each: 54 distinct DDS files and 54 resolving GFX declarations. The decoded contact sheet confirms all three states for all 18.

No unresolved, missing, default, TODO, or placeholder basename/path remains. `goal_CBL_map_the_origin_templates.dds` is a legitimate focus asset; the substring `temp` inside `templates` is not a placeholder token. Event 014 defines no bespoke equipment type or unit model, so no Event 014 equipment/unit GFX registration is absent.

`localisation/english/014_cannibalism_l_english.yml` has a UTF-8 BOM and 1,974 quoted localisation entries after the `l_english` header. It has:

- zero duplicate keys in the file and zero duplicate Event 014 keys in other English localisation files;
- zero `:0` keys;
- 36 nested `$key$` references, all resolving;
- 74 direct GUI localisation references, all resolving;
- 113 explicit Event 014 event/news references, all resolving;
- all 204 focus names and descriptions plus all 204 focus tooltips;
- all extracted 127 decision names/descriptions and 288 explicit decision tooltip/cost references;
- all 37 idea names and descriptions;
- all 18 achievement tracker names/descriptions and their native name/description/tooltip families.

Visual review of decoded focus, decision, idea, achievement, GUI, report/news, leader, flag, animation, and super-event contact sheets found no placeholder art or accidental cross-type substitution. Player-facing wording describes the current game state and choices; no implementation-history, fallback, or ancient-general disclaimer wording is exposed.

## Visual dispositions

| Family | Disposition | Reason |
| --- | --- | --- |
| 65 flag masters / 195 runtime flags | Accept | distinct built-in ImageGen lineage, exact ladders, flat flag grammar, readable palettes |
| 56 warlord portraits | Accept | unique 156x210 faces/poses/props/actions; bald/feral brief met; no prison/sacred/actor treatment |
| canonical ordinary/Wendigo portraits | Accept | direct static binding, frame-000 identity, no redundant static copies |
| 14 animation packages | Accept | separate source frames, semantic motion, exact sheets/statics/GFX, blendframes; portraits at 12 FPS |
| 4 super-event images | Accept | unique action-led compositions with exact runtime registration and gates |
| reports/news | Accept | generic pre-reveal scenes; identity-bearing reveal art only after the gate |
| focus/decision/idea/category/GUI icons | Accept | decoded sheets inspected; distinct semantic imagery and no placeholder/cross-type substitution |
| 18 achievement triplets | Accept | exact 54-state set, readable state differentiation, resolving registry/localisation |
| super-event audio IDs 49/50/52/53 | Accept | unique 44.1 kHz tracks, exact wrappers/mappings, documented rights |
| Repaired or rejected visual assets | None in current runtime | Superseded generations remain only as documented source history; none is shipped or used as fallback. |

## Files changed by this reaudit

- Added `docs/plans/014_cannibalism_plans/audits/event014_localisation_asset_consolidation_reaudit_2026-07-15.md`.
- Corrected the stale 6 FPS portrait prose and added a supersession pointer in `docs/plans/014_cannibalism_plans/audits/event014_localisation_asset_reaudit_2026-07-15.md`.

No gameplay, localisation, GFX, image, flag, portrait, animation, or audio file was changed by this audit.

## Simplifications, omissions, fallbacks, and blockers

No content or asset simplification, omission, placeholder, fallback, or blocker remains. All requested current-runtime surfaces were inspected through source/registry evidence and the applicable visual/audio evidence. The external MCP availability note above is not an audit finding and does not reduce the completed coverage.
