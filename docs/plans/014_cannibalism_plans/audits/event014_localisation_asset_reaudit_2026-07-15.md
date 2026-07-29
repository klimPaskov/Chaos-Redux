# Event 014 Localisation, Asset, Audio, and Secrecy Reaudit

Date: 2026-07-15
Mode: final targeted audit with one narrow localisation repair
Verdict: completion-ready for the audited scope

Superseded for current consolidation facts by `event014_localisation_asset_consolidation_reaudit_2026-07-15.md`. The live portrait animation declarations were consolidated at 12 FPS with `buttonstate_blendframes.lua`; the corrected values below replace the earlier pre-consolidation 6 FPS prose.

## Final priority counts

| Priority | Remaining findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

## In-run repair

Seven command-power cost strings in `localisation/english/014_cannibalism_l_english.yml` still referenced retired `*_command_trigger` script-constant keys. They now reference the live `*_command_gate` keys for intensification, abandonment, alignment, synchronized attack, island operations, siege operations, and march operations.

The offline Localisation wiki states that the `0` variable formatter rounds to a whole number with zero decimals. The live gates therefore display the exact paired spend values: `7.99|0` displays 8 against a spend of -8; `4.99|0` displays 5 against -5; `9.99|0` displays 10 against -10; `14.99|0` displays 15 against -15; and `11.99|0` displays 12 against -12. The repaired strings do not expose fractional gate values or disagree with gameplay costs.

Post-repair evidence: 276 distinct visible `constant:category.key` references resolve, with zero missing constants. The edited YML retains its UTF-8 BOM.

## Localisation and token closure

The seven required YML files all retain UTF-8 BOM encoding and contain zero `:0` keys:

- `localisation/english/014_cannibalism_l_english.yml`
- `localisation/english/014_cannibalism_objectives_l_english.yml`
- `localisation/english/014_cannibalism_super_events_l_english.yml`
- `localisation/english/zz_014_cannibalism_focus_closure_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

The files contain 3,529 parsed localisation entries, all unique. Their 36 nested `$key$` references have zero missing targets. Their 33 `GetCannibalism...` calls all resolve to defined scripted-localisation selectors. The Event 014 GUI contains 74 explicit text or tooltip keys and all 74 resolve. The current three focus files contain 204 focus entries after excluding the three tree IDs; every focus has title and description localisation. The 18 Event 014 achievements have matching registry, name, description, and tooltip coverage.

No live Event 014 player-facing text contains a Prison Host name, an ancient-general or Carthaginian disclaimer, or a claim of authenticity for a living Indigenous or sacred tradition. Internal Hannibal identifiers remain permitted.

## Secrecy and reveal ordering

No player-visible Hannibal Lecter or Wendigo surface is available before `cannibalism_reveal_complete`.

- `common/scripted_effects/014_cannibalism_unification_effects.txt:528` sets the reveal flag before CBL ownership, character, portrait, country package, focus tree, or public threat presentation.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:474` sets the reveal flag before the transformed identity, portrait, focus, decisions, reports, news, or super-event call.
- `common/scripted_guis/014_cannibalism_scripted_gui.txt:215` gates the ordinary revealed-command window, and line 244 gates the transformed window. The transformed window also requires the Wendigo route and transformed country identity.
- All four Event 014 super-event emitters require the reveal flag at lines 51, 72, 96, and 118 of `common/scripted_effects/014_cannibalism_super_event_effects.txt`.
- Event Details excludes Evolution III and both terminal rows before reveal. The current gates are in `common/scripted_effects/chaosx_events_log_effects.txt:1095` and line 2112, with matching stage-title and stage-description gates in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.
- Spoiler-bearing achievement tracker entries remain staged behind reveal or their later route-specific public flags.

The live file set contains zero `Prison Host`, `prison_host`, or `Cannibal Prison Host` matches and zero retired Prison Host basenames.

## Runtime GFX closure

The nine Event 014-related GFX registries contain exactly 812 Event 014 texture references, 598 unique runtime paths, and zero missing paths:

| GFX registry | Event 014 references |
| --- | ---: |
| `interface/014_cannibalism.gfx` | 568 |
| `interface/014_cannibalism_achievement_tracker.gfx` | 2 |
| `interface/014_cannibalism_achievements.gfx` | 54 |
| `interface/014_cannibalism_aftermath_pictures.gfx` | 2 |
| `interface/014_cannibalism_focus_closure.gfx` | 6 |
| `interface/014_cannibalism_objectives.gfx` | 13 |
| `interface/014_cannibalism_warlord_focus_assets.gfx` | 136 |
| `interface/chaosx_pictures.gfx` | 27 |
| `interface/chaosx_super_events.gfx` | 4 |

All 598 DDS files have valid DDS headers and the expected uncompressed 32-bit BGRA masks. They also have 598 unique SHA-256 hashes, proving that no Event 014 runtime DDS is reused across categories.

## Flags, portraits, animations, and super-events

Flags:

- 13 families times 5 ideology forms times 3 sizes equals 195 live TGA files.
- Normal, medium, and small tiers contain 65 files each at 82x52, 41x26, and 10x7.
- All 195 are 32-bit, bottom-left-origin TGA files with 195 unique hashes and no missing family or ideology form.
- The package retains 65 separate built-in image-generation source masters and 65 processed flat masters. Visual inspection confirms 2 to 4 opaque flat colors, hard edges, and no physical-flag mockups.

Regional warlord portraits:

- 56 selected source PNGs, 56 processed 156x210 PNGs, and 56 live 156x210 DDS portraits are present.
- All 56 live portraits have unique hashes. The GFX exposes 64 aliases resolving to those 56 regional files, with the eight default/Europe aliases intentionally sharing their matching regional path.
- Contact-sheet inspection confirms 56 distinct fictional feral leaders, close portrait framing, bald heads, and no prison, cell, cage, restraint, or prisoner-uniform backgrounds.

Animations:

- Ordinary Hannibal has 12 unique generated source frames and 12 unique processed frames, a 1872x210 sheet DDS, a 156x210 static fallback, GIF, source and processed contact sheets, manifest, validation, and GFX handoff. Its live `frameAnimatedSpriteType` declares 12 frames at 12 FPS with `buttonstate_blendframes.lua`.
- Wendigo Hannibal has 16 unique generated source frames and 16 unique processed frames, a 2496x210 sheet DDS, a 156x210 static fallback, GIF, source and processed contact sheets, manifest, hashes, validation, and GFX handoff. Its live declaration has 16 frames at 12 FPS with `buttonstate_blendframes.lua`.
- The 12 non-portrait packages contain 114 unique source frames and 114 unique processed frames. Their counts are 8, 8, 8, 8, 8, 12, 12, 6, 12, 8, 12, and 12. Every package has source and processed frames, PNG/DDS sheet, PNG/DDS static fallback, GIF, contact sheet, manifest, frame inventory, brief, frame plan, live DDS pair, and GFX handoff.
- Contact-sheet inspection confirms semantic artwork progression inside each package. None is a transform-only animation of one still.

Super-event images:

- Four unique 457x328 runtime DDS files are registered with zero path mismatch.
- Reveal: convergence and pursuit, SHA-256 `b73a9e9274b411c1a637d01641a27c9aab69b05fdc25340106f3371aca760014`.
- Ordinary world-end: capital overrun, SHA-256 `2e6ab8e3af541a75d143885f12fbefd8d3c784a9bb998d69e77c2e10d132d512`.
- Global defeat: breakthrough and rescue, SHA-256 `61cf83f3c533b219f56345abe8f550725925dad5ca5ab92fdb0ab88f244eacd9`.
- Wendigo world-end: frozen pack hunt, SHA-256 `a7f5288912ef82c1539d5ee8c83a1125afb4943bb3a31691311333f9c76214fd`.

The four decoded scenes are action-heavy, compositionally distinct, and do not reuse any other Event 014 runtime DDS.

## Achievements

The live achievement registry contains 18 Event 014 achievements. `interface/014_cannibalism_achievements.gfx` contains 54 unique sprites: completed, grey, and not-eligible states for every achievement. All 54 runtime DDS files are 64x64 and have distinct hashes.

The current processor copies each grey variant and alpha-composites the exact required overlay from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`, SHA-256 `89bc80c6ac975bf6f1ff000ff3070b20c337bfb8b8ae966ae35a5540c004d6dd`. Its validation ledger contains 54 complete rows, with package and runtime DDS hashes aligned.

## Licensed audio and wiring

IDs 49, 50, 52, and 53 are fixed in `common/script_constants/014_cannibalism_core_constants.txt:28-31`. Each visual emitter assigns the same constant to `global.current_super_event_audio_id` before calling the shared playback helper.

The four distinct licensed cues are delivered as eight hash-distinct binaries: four Vorbis OGG files and four PCM s16le WAV files. Every file is stereo at 44100 Hz. Durations are 114.000 seconds for ID 49, 120.000 for ID 50, 116.100 OGG / 116.001 WAV for ID 52, and 118.000 for ID 53.

- ID 49: Saint-Saens, `Danse macabre`, 1925 Stokowski/Philadelphia recording; public-domain composition and recording record.
- ID 50: Wagner, `Siegfried's Funeral March and Finale`, United States Marine Band; public-domain composition and United States federal-government recording record.
- ID 52: Faure, `Elegie, Op. 24`, Goldstein/Kalman; CC BY-SA 2.0 attribution, adaptation notice, and share-alike record.
- ID 53: Grieg, `The Death of Aase`, Musopen Symphony; public-domain composition and recording record.

`music/chaosx_super_event_music.asset` registers six volume variants per ID, `music/chaosx_super_event_music.txt` suppresses their representative entries from normal selection, and `sound/chaosx_sound.asset` registers four WAV sources plus six settings-aware wrappers per ID. Source, rights, excerpt, processing, and output evidence is retained in `docs/super_events/014_cannibalism/audio_research.md` and `music/chaosx_music_track_list.html`. No generated tone or placeholder track is present.

## Changed files

- `localisation/english/014_cannibalism_l_english.yml`: repaired seven retired constant references.
- `docs/plans/014_cannibalism_plans/audits/event014_localisation_asset_reaudit_2026-07-15.md`: this audit.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localisation_asset_reaudit_handoff_2026-07-15.md`: audit handoff.

No gameplay script, GFX registry, image, animation, flag, achievement asset, or audio binary was changed by this audit.

## Simplifications, omissions, and blockers

None. All requested localisation, secrecy, GFX closure, flag, portrait, animation, super-event, achievement, and audio surfaces were included. No fallback was used. No blocker remains in the audited scope.

## Skills used

- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-subagents`

No skill was created or updated.
