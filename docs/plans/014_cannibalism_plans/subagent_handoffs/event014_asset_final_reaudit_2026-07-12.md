# Event 014 Asset, Audio, and Animation Final Reaudit

Date: 2026-07-12
Mode: read-only audit; no gameplay, asset, registry, or localisation files were edited
Verdict: **NOT COMPLETION-READY**

## Severity verdict

| Severity | Finding groups | Verdict |
| --- | ---: | --- |
| P0 | 0 | None. |
| P1 | 1 | All 18 achievement not-eligible variants use a prohibited locally drawn treatment instead of the mandatory exact overlay. This blocks asset completion. |
| P2 | 2 | Retired animation outputs are still documented as complete, and the top/generated-art manifests still claim absent or superseded runtime outputs and registries. |
| P3 | 0 | None. |

The live image and audio wiring is otherwise complete and internally consistent. The completion blocker is an asset-derivation violation, not a missing live GFX path.

## Required references consulted

- Repository `AGENTS.md`.
- Full repository skills: `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `chaos-redux-events`.
- Offline wiki core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Offline wiki system pages: Graphical asset modding, Interface modding, Scripted GUI modding, Portrait modding, Sound modding, and Music modding.
- Vanilla documentation and precedents: `common/scripted_guis/_documentation.md`, `common/characters/_documentation.md`, `documentation/fakegfx.txt`, `documentation/fakegfx2.txt`, `music/music.asset`, `music/_songs.txt`, `sound/sound.asset`, `sound/soundeffects.asset`, `interface/eventwindow.gfx`, and `interface/countrypoliticsview.gfx`.

No web Paradox wiki material was used.

## Findings

### P1 — 18 achievement not-eligible variants violate the mandatory overlay workflow

The authoritative Event 014 achievement package contains 18 completed masters, 18 grey variants, and 18 not-eligible variants. The 18 completed masters are unique and visually purpose-built; all 54 runtime DDS files are root-level, registered as exact triplets, 64x64, and hash-distinct.

However, `docs/assets/014_cannibalism/achievements_imagegen/process_achievement_icons.py:131-142` darkens each grey icon and manually draws a red X with `ImageDraw.line` and `ImageDraw.ellipse`. It does not copy the grey variant and composite the required exact overlay:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`

The overlay exists and has SHA-256 `89bc80c6ac975bf6f1ff000ff3070b20c337bfb8b8ae966ae35a5540c004d6dd`. The governing skill explicitly forbids not-eligible icons made by darkening or manually redrawing the grey icon. Consequently, every registered `gfx/achievements/014_cannibalism_*_not_eligible.dds` is non-compliant.

Required remediation: preserve the 18 completed masters; derive each grey variant as the package requires; copy that exact grey image; composite the exact overlay above without recreating it; rebuild all 18 not-eligible PNG/DDS variants; refresh package hashes/contact sheets; and recheck the 54 registered triplets.

### P2 — retired six-package animation manifest claims 12 absent DDS files are complete

`docs/assets/014_cannibalism/animations_imagegen/manifest.md:20-137` marks six superseded packages as `Status: complete` and names 12 final runtime DDS files that do not exist:

- `cannibalism_frontline_hunger_seal_{static,sheet}.dds`
- `cannibalism_cult_pressure_warning_{static,sheet}.dds`
- `cannibalism_island_signal_card_{static,sheet}.dds`
- `cannibalism_hannibal_resonance_seal_{static,sheet}.dds`
- `cannibalism_council_portrait_overlay_{static,sheet}.dds`
- `cannibalism_world_end_progress_border_{static,sheet}.dds`

None is registered by the live GFX. The current 14-package animation set is under `docs/assets/014_cannibalism/gui_animation_portraits/`. This is a stale source-of-truth claim, not a missing runtime dependency.

### P2 — top-level and generated-art manifests retain absent/superseded outputs and owners

`docs/assets/014_cannibalism/manifest.md` still points to the superseded 13-ID achievement package at line 22, the retired animation manifest at line 26, the absent `gfx/leaders/014_cannibalism/CBL_table_council.dds` at line 39, and the wrong achievement registry `interface/chaosx_achievements.gfx` at line 47. The authoritative live registry is `interface/014_cannibalism_achievements.gfx`.

`docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md:15-18,50-52` also marks absent superseded files as complete, including the old network/islands/world-end/defeat super-event DDS files, `leader_CBL_warlord.dds`, and `CBL_table_council.dds`. The four live regenerated super-event files and the current Hannibal portrait packages use different runtime paths.

These records must be marked superseded/archival or updated to the current package owners and paths. No absent path from either stale manifest is referenced by live Event 014 GFX.

## Runtime GFX inventory and path closure

Nine Event 014-related GFX registries were audited:

- `interface/014_cannibalism.gfx`
- `interface/014_cannibalism_achievement_tracker.gfx`
- `interface/014_cannibalism_achievements.gfx`
- `interface/014_cannibalism_aftermath_pictures.gfx`
- `interface/014_cannibalism_focus_closure.gfx`
- `interface/014_cannibalism_objectives.gfx`
- `interface/014_cannibalism_warlord_focus_assets.gfx`
- `interface/chaosx_pictures.gfx`
- `interface/chaosx_super_events.gfx`

Result: **816 Event 014 texture references, 598 unique runtime texture paths, zero missing paths, and 598 unique SHA-256 hashes**. All 598 DDS files have valid DDS headers, expected dimensions, and 32-bit BGRA channel masks.

| Runtime class | Unique DDS paths | Dimensions / notes |
| --- | ---: | --- |
| Achievements | 54 | 18 exact 64x64 triplets; P1 derivation finding applies to the 18 not-eligible files. |
| Animation under `gfx/interface/animated` | 24 | 12 sheet/static pairs. |
| Decisions and category panels | 137 | 124 32x32 icons and 13 114x101 panels. |
| Focuses | 208 | 208 94x86 icons. |
| Static scripted-GUI assets | 26 | Native dimensions from 166x220 through 860x620. |
| Ideas | 56 | 56 64x64 icons. |
| Leaders | 60 | 56 regional warlords plus four Hannibal animated/static sheet paths. |
| News | 7 | 7 397x153 images. |
| Report events | 22 | 22 210x176 images. |
| Super-events | 4 | 4 457x328 images. |
| **Total** | **598** | **Zero duplicate runtime texture hashes.** |

The Event 014 runtime asset directories contain no unregistered current DDS. The only unregistered DDS files are the two deliberately protected archival portraits `gfx/leaders/014_cannibalism/hannibal.dds` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`; neither is registered or consumed by current gameplay. The 50 PNG files in the runtime interface folders are documented mirrors/fallback source surfaces, not missing GFX registrations.

## Animation completion

The live package contains 14 independently sourced animations with 142 source frames and 142 processed frames:

- `leader_CBL_hannibal`: 12 frames, 6 fps, 1872x210 sheet, 156x210 fallback.
- `leader_ZZZ_hannibal_wendigo`: 16 frames, 6 fps, 2496x210 sheet, 156x210 fallback.
- Twelve non-portrait packages: early-warning seal, cult-cohesion emblem, network threads, island alert, selected-target overlay, critical-larder glow, frenzy border, warlord-route emblem, unification seal, ordinary terminal frame, Wendigo anchor pulse, and Wendigo terminal frame. Their frame counts are 8, 8, 12, 8, 6, 8, 8, 8, 12, 12, 12, and 12.

For all 14 packages, expected source and processed frame counts match; every frame is hash-distinct within its package; sheet dimensions equal frame width multiplied by the declared frame count; the runtime DDS sheets and fallbacks match the PNG dimensions; and source frames, processed frames, sheet PNG, sheet DDS, fallback PNG/DDS, GIF preview, contact sheet, manifest, and GFX handoff are present. `interface/014_cannibalism_frontline_hunger.gui` consumes every motion sprite and its static fallback. `common/scripted_guis/014_cannibalism_scripted_gui.txt` keeps the motion layers active by default under the existing reveal and route gates while the static siblings remain registered but hidden.

Source contact sheets show independently rendered pose/action progression rather than transform-only movement, scaling, rotation, warping, blur, recolour, or filtering of one still. The ordinary Hannibal sequence is a 12-frame skull-raise/lick action; the Wendigo sequence has 16 separately rendered predatory-action frames. The twelve UI animations also contain real per-frame artwork changes.

## Static visual packages

### Four regenerated super-events

The reveal, ordinary world-end, global-defeat aftermath, and Wendigo world-end DDS files are all 457x328, have four unique hashes, match their processed source packages, and are registered by `interface/chaosx_super_events.gfx`. The decoded contact sheet shows four distinct action compositions: convergence/pursuit, capital overrun, breakthrough/rescue, and frozen pack hunt. No default image, placeholder, or cross-type reuse was found.

### 56 regional warlord portraits

There are 56 source PNGs, 56 processed 156x210 PNGs, and 56 runtime 156x210 DDS files. Every source, processed output, and runtime DDS is hash-distinct within its stage. The GFX contains 64 region/slot sprite aliases resolving to these 56 unique paths; the eight unsuffixed aliases intentionally share the eight Europe paths with their `_europe` aliases. The decoded all-regions contact sheet confirms distinct characters and compositions, not placeholder or default portraits.

### Flags

Thirteen flag families each provide base, communism, democratic, fascism, and neutrality variants in all three engine sizes: 65 normal 82x52, 65 medium 41x26, and 65 small 10x7 TGA files, for **195 total**. All are 32-bit bottom-left-origin TGA files; each size set contains 65 unique hashes; no family/ideology/size file is missing.

### Focus, idea, decision, report, news, unit-visible, GUI, and closure coverage

- 208 focus icons, 56 idea icons, 124 decision icons, and 13 decision-category panels are registered, present, dimension-correct, and runtime-hash distinct.
- 22 report images and 7 news images are present and registered. Decoded contact sheets show distinct documentary/action compositions.
- Scripted-GUI static art contains 26 registered DDS textures with matching PNG mirrors.
- The 2026-07-12 closure package contains **21 unique assets**: 20 32x32 icons and one 114x101 achievement-tracker panel. Source, processed, packaged DDS, live runtime, and GFX mapping counts match 21/21 with exact hashes.
- No separate Event 014 `GFX_unit_*`, equipment, or division art contract is registered. The unit-facing surfaces that do exist are covered by the purpose-built recruitment/operation decision icons and `gfx/interface/014_cannibalism/wendigo_unit_capacity.dds`; no unresolved unit-art reference was found.

## Licensed super-event audio

The four packages use stable unique IDs 49, 50, 52, and 53 from `common/script_constants/014_cannibalism_core_constants.txt:28-31`. `common/scripted_effects/014_cannibalism_super_event_effects.txt` sets both visible and audio IDs through those constants, and reveal playback is gated behind `cannibalism_reveal_complete`.

| ID | Final cue | OGG | WAV | Rights record |
| ---: | --- | --- | --- | --- |
| 49 | Saint-Saëns, *Danse macabre*, Stokowski/Philadelphia (1925) | Vorbis, 44100 Hz, stereo, 114.000 s | PCM s16le, 44100 Hz, stereo, 114.000 s | Public-domain composition and documented public-domain 1925 recording treatment. |
| 50 | Wagner, *Siegfried's Funeral March and Finale*, U.S. Marine Band | Vorbis, 44100 Hz, stereo, 120.000 s | PCM s16le, 44100 Hz, stereo, 120.000 s | Public-domain composition and U.S. federal-government recording. |
| 52 | Fauré, *Élégie, Op. 24*, Goldstein/Kalman | Vorbis, 44100 Hz, stereo, 116.100 s | PCM s16le, 44100 Hz, stereo, 116.001 s | CC BY-SA 2.0 recording; attribution, modification notice, and share-alike record are present. |
| 53 | Grieg, *The Death of Aase*, Musopen Symphony | Vorbis, 44100 Hz, stereo, 118.000 s | PCM s16le, 44100 Hz, stereo, 118.000 s | Public-domain composition and Musopen public-domain recording. |

The four archived OGG hashes are unique, the four WAV hashes are unique, and none duplicates another repository audio binary. `sound/chaosx_sound.asset` registers four WAV sources plus six settings-aware sound-effect wrappers per ID. `music/chaosx_music_track_list.html` and `docs/super_events/014_cannibalism/audio_research.md` preserve the source and license records.

## Visual safety and secrecy review

Decoded final contact sheets were inspected for the 598 registered texture set, with focused review of all report/news images, four super-events, 56 regional portraits, both Hannibal animations, 18 achievement triplets, 195 flags, twelve non-portrait animation packages, and 21 closure assets.

- No default or placeholder texture and no cross-type reuse was found; the 598 globally unique runtime hashes corroborate the visual review.
- No identifiable actor likeness was found. Hannibal is represented as a fictional bald/gaunt period commander, not a copied film still or identifiable performer.
- No antlers, horns, feathers, regalia, runes, sacred dress, living Indigenous identity claim, or other borrowed living-cultural motif was found in the Wendigo or route art.
- Pre-reveal report/news/UI surfaces use field evidence, ration records, camps, routes, and anonymous figures. They do not expose Hannibal's face, name, transformed form, or terminal imagery before the scripted reveal gates.
- Post-reveal Hannibal/Wendigo art is confined to reveal-complete and route-specific presentation surfaces in the live GUI/super-event wiring.

## Simplifications, omissions, and blockers

- **Blocker:** the 18 not-eligible achievement variants must be rebuilt with the mandatory exact overlay before Event 014 asset completion can be claimed.
- **Documentation blockers:** the retired animation manifest and the top/generated-art manifests must be reconciled with the live package ownership and paths before documentation completion can be claimed.
- No runtime asset, flag family, regional portrait, animation package, closure icon, super-event image, or requested audio package was omitted from this audit.
- No fallback or simplification was accepted. The implementation remains incomplete solely for the P1 derivation violation and the two P2 documentation groups above.

## Remediation recheck — 2026-07-13

The three finding groups above were remediated and independently rechecked on 2026-07-13.

- `docs/assets/014_cannibalism/achievements_imagegen/process_achievement_icons.py` now requires the exact 64x64 RGBA overlay at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`, copies each grey variant without alteration, and alpha-composites that overlay on top. The brightness adjustment and locally drawn X were removed.
- The processor regenerated and validated all 18 masters / 54 variants. An independent pixel comparison found 18 exact grey-copy overlay composites and zero mismatches. The 54 package DDS files exactly match the 54 live DDS files; all 54 live hashes remain distinct.
- `docs/assets/014_cannibalism/animations_imagegen/manifest.md` now identifies all six early experiments as retired source/provenance only and makes no claim that their 12 absent DDS files or sprites are live.
- `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md` now preserves historical source/processed provenance without assigning absent final DDS/TGA paths or superseded sprite ownership.
- `docs/assets/014_cannibalism/manifest.md` now points to the authoritative 18-achievement package, 14-animation package, current four Hannibal portrait sheet/fallback files, and `interface/014_cannibalism_achievements.gfx`.
- The nine-file GFX closure remains exactly 816 references / 598 unique texture paths / zero missing paths / 598 unique SHA-256 hashes.
- The accepted animation package remains 14 packages / 142 source frames / 142 processed frames, with zero count mismatches, zero within-package source or processed hash duplicates, zero missing preview/contact pairs, zero missing PNG sheet/fallback pairs, zero missing live DDS pairs, and complete 14-package handoff coverage.
- A targeted stale-claim scan found zero remaining references to the retired animation DDS names, absent council/leader/old-super-event DDS names, superseded achievement package, or stale achievement registry in the reconciled manifests.

### Final post-remediation verdict

| Severity | Remaining finding groups |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

**Final verdict: COMPLETION-READY for the Event 014 asset, audio, and animation scope.** No simplifications, omissions, fallbacks, or remaining blockers were found in the remediated scope.
