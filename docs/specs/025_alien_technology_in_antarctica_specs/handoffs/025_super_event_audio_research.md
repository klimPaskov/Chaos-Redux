# Event 025 Super-Event Audio Provenance and Wiring Audit

Audit date: 2026-09-04.

Audit status: conditional acceptance. The preserved source and final runtime WAV are verified and the current sound-definition/catalogue wiring is coherent in the working tree. The separately documented edited OGG is absent, and the event-side audio assignment and settings-aware playback call remain unverified because gameplay implementation files are outside this audit scope.

## Scope and evidence

This audit covers the Event 025 super-event audio brief, the Event 025 asset/super-event specification, the Event 025 implementation-architecture and acceptance requirements relevant to audio, the prior audio-research handoff, the current Event 025 sound folder, `sound/chaosx_sound.asset`, the canonical music catalogue, the shared super-event interface alias, and the Event 025 source receipts.

Audited repository evidence:

- `docs/specs/025_alien_technology_in_antarctica_specs/prompts/025_super_event_audio_researcher_prompt.md`
- `docs/specs/025_alien_technology_in_antarctica_specs/specs/010_assets_animation_and_super_event.md`
- `docs/specs/025_alien_technology_in_antarctica_specs/specs/013_implementation_architecture.md`
- `docs/specs/025_alien_technology_in_antarctica_specs/specs/014_acceptance_criteria.md`
- `docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_super_event_audio_researcher_handoff.md`
- `docs/assets/025_alien_technology_in_antarctica/source_audio/borodin_in_the_steppes_of_central_asia_musopen_symphony_source.flac`
- `docs/assets/025_alien_technology_in_antarctica/source_receipts/commons_borodin_steppes_rights_page_oldid_963504941.html`
- `docs/assets/025_alien_technology_in_antarctica/source_receipts/cc0_1.0_deed.html`
- `sound/025_alien_technology_in_antarctica/`
- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`
- `interface/chaosx_super_events.gfx`
- `interface/025_alien_technology_in_antarctica.gfx`
- `interface/chaosx_super_events.gui`

The Event 025 package specifies one opening first-reveal super-event with a remote, cold, exploratory, tense, scientific, and uncertain role. It does not specify a separate final-recovery super-event slot or numeric audio ID.

## Selected track and rights

| Field | Audited result |
| --- | --- |
| Track title | `In the Steppes of Central Asia` |
| Composer | Alexander Borodin (1833–1887) |
| Performer / recording source | Wikimedia Commons credits Musopen Symphony; embedded FLAC tags identify the Czech National Symphony Orchestra. The durable courtesy attribution should retain both names rather than silently choosing one. |
| Source record | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Borodin_-_In_the_Steppes_of_Central_Asia_(Musopen_Symphony).flac) and frozen revision `oldid=963504941` |
| Direct original download | `https://upload.wikimedia.org/wikipedia/commons/c/c6/Borodin_-_In_the_Steppes_of_Central_Asia_%28Musopen_Symphony%29.flac` |
| Upstream source references | `https://musopen.org/music/681-in-the-steppes-of-central-asia/` and `https://archive.org/details/MusopenCollectionAsFlac` |
| Composition rights | Public domain according to the file-specific source receipt; the Commons record identifies Borodin's 1887 death date and public-domain composition status. |
| Recording rights | The file-specific Commons record states that Musopen released this recording worldwide into the public domain, with an unconditional fallback grant where a dedication is not legally possible. The preserved [CC0 1.0 deed](https://creativecommons.org/publicdomain/zero/1.0/) permits copying, modification, distribution, and performance without permission or required attribution. |
| License confidence | High for this specific recording and source record. This is not a blanket assertion that every Musopen recording or Musopen-owned material is free to use. |
| Required attribution | No legal attribution is required under the stated CC0 recording dedication. Courtesy attribution is recommended: `Alexander Borodin, In the Steppes of Central Asia; Musopen Symphony / Czech National Symphony Orchestra, CC0 recording via Musopen and Wikimedia Commons.` |

Composition rights and recording rights were checked separately. The source is suitable for the super-event brief because it is structured orchestral music with a restrained opening and gradual motion, not a generated tone, synthetic drone, stinger, sound effect, or ambience bed.

## File and hash verification

| Artifact | Current status | Format and duration | SHA-1 | SHA-256 |
| --- | --- | --- | --- | --- |
| Preserved source FLAC: `docs/assets/025_alien_technology_in_antarctica/source_audio/borodin_in_the_steppes_of_central_asia_musopen_symphony_source.flac` | Present and unchanged relative to the prior handoff's recorded values | FLAC, stereo, 48,000 Hz, 458.240000 s, 73,785,694 bytes | `A25677D7B6435F8F18475F4F7E9D1EF75A895481` | `6E53A2E3B48B070EF8ABE95A9D411D29BE68D7B2163347360405F33072648857` |
| Final runtime WAV: `sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.wav` | Present; hash matches the prior handoff and the canonical catalogue row | signed 16-bit PCM, stereo, 44,100 Hz, 115.000000 s, 20,286,484 bytes | not recomputed for this audit | `BCB9EE95809F01413A947D10D684859B8D20DA1B0319A1F1D384263E431EB126` |
| Documented edited OGG candidate: `sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.ogg` | Missing from the current Event 025 sound folder; the prior handoff's recorded OGG hash cannot be independently verified | No local container available to probe | not verifiable | prior handoff only: `7C7A7D48B54B5A1E3E494EC7AFD2611AE9E937D611053204C040733C22B35E23` |

FFprobe successfully decodes the current WAV as `pcm_s16le`, stereo, 44,100 Hz, 16-bit, with an exact 115-second duration. FFprobe successfully decodes the preserved source as stereo FLAC at 48,000 Hz with an exact 458.240-second duration.

The missing OGG is distinct from the upstream Commons OGG derivative referenced by the source page. The upstream file is not evidence that the local 115-second edited OGG candidate exists.

## Editing and conversion record

The prior researcher handoff records a source-derived excerpt from `00:00.000` through `01:55.000`, a `0.25`-second fade-in, a `5`-second fade-out from `01:50.000` through `01:55.000`, no limiting or synthetic layers, stereo output, and resampling from 48,000 Hz to 44,100 Hz with the FFmpeg SoXr resampler.

The documented WAV conversion is equivalent to:

```text
ffmpeg -hide_banner -loglevel error -y -i <source.flac> -af "atrim=start=0:duration=115,asetpts=N/SR/TB,afade=t=in:st=0:d=0.25,afade=t=out:st=110:d=5,aresample=44100:resampler=soxr" -ac 2 -c:a pcm_s16le <final.wav>
```

The original FLAC remains preserved. No destructive re-edit or gain change was performed during this audit.

## Current sound-definition wiring

The current working-tree `sound/chaosx_sound.asset` contains a complete base sound and six settings-volume wrappers for numeric audio registration ID `109`:

| Definition | Current wiring |
| --- | --- |
| Base sound | `chaosx_super_event_109_track` points to `025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.wav` at `sound/chaosx_sound.asset:1949`. |
| Volume wrapper `0_5` | `chaosx_super_event_109_sound_0_5`, volume `0.67`, `max_audible = 1`, `max_audible_behaviour = fail`. |
| Volume wrapper `1_0` | `chaosx_super_event_109_sound_1_0`, volume `1.33`, same audible-limit pattern. |
| Volume wrapper `1_5` | `chaosx_super_event_109_sound_1_5`, volume `2.00`, same audible-limit pattern. |
| Volume wrapper `2_0` | `chaosx_super_event_109_sound_2_0`, volume `2.67`, same audible-limit pattern. |
| Volume wrapper `2_5` | `chaosx_super_event_109_sound_2_5`, volume `3.33`, same audible-limit pattern. |
| Volume wrapper `3_0` | `chaosx_super_event_109_sound_3_0`, volume `4.00`, same audible-limit pattern. |

The wrapper names are also present in the sound-effect registration list at `sound/chaosx_sound.asset:475-480`. The definitions point to the same base sound and do not reference `default.ogg`, `world_revolution.ogg`, another super-event cue, a test tone, a noise bed, or an unsupported OGG path.

The suggested descriptive base ID from the earlier audio handoff, `chaosx_super_event_025_antarctic_first_reveal_track`, was not used by the current parent-owned wiring. The current numeric base ID `chaosx_super_event_109_track` is internally consistent with the six wrappers, the catalogue row, and the visual alias. It is acceptable as the chosen unique registration name if the parent confirms that `109` is the intended slot/audio ID.

## Catalogue and interface alias cross-check

The canonical row in `music/chaosx_music_track_list.html:713-720` records the final WAV path, title, composer, Musopen Symphony / Czech National Symphony Orchestra source, `01:55` duration, public-domain composition and worldwide CC0 recording status, and the final WAV SHA-256. The row is internally consistent with the current WAV. It does not claim that the missing local OGG exists or record the prior handoff's OGG hash.

The live shared alias in `interface/chaosx_super_events.gfx:224-225` is:

```text
GFX_super_event_109_antarctic_first_reveal -> gfx/super_events/025_alien_technology_in_antarctica/super_event_025_discovery.dds
```

The target DDS exists and has SHA-256 `2CE386C14B7309B73BE9B82836651B0B8F7ECE7019D7578733A3347397DA194B`. `interface/025_alien_technology_in_antarctica.gfx` explicitly leaves the 457x328 super-event canvas on the dedicated shared alias rather than defining a second local super-event alias. `interface/chaosx_super_events.gui` consumes the dynamic image property and contains no separate audio route.

There is a non-audio documentation drift to carry to the parent: `docs/assets/025_alien_technology_in_antarctica/gfx_handoff.md:9` proposes `GFX_super_event_025_discovery`, while the live alias is `GFX_super_event_109_antarctic_first_reveal`. This does not change the audio hash or sound-definition result, but the visual handoff should be reconciled before the package is called fully complete.

## Event-side audio ID and playback status

The current sound asset, canonical catalogue row, and shared interface alias consistently use `109` as the Event 025 opening presentation's current numeric registration identifier. The Event 025 specification requires a unique audio ID, settings-aware volume wrappers, `global.current_super_event_audio_id`, and `play_current_super_event_sound = yes`.

This audit did not read the Event 025 gameplay implementation file. Therefore it does not independently verify that the event-side code assigns `global.current_super_event_audio_id = 109` at the opening trigger or calls `play_current_super_event_sound = yes`. The prior audio handoff explicitly left those parent-owned steps pending. The sound-definition and alias evidence is not a substitute for verifying that event-side call path.

## Fallbacks, unsupported routes, and blockers

- The local edited OGG candidate is missing. Do not use the prior handoff's OGG hash as current-file evidence, and do not point runtime wiring at that absent path.
- The current WAV route is supported and verified for the parent sound definition. The missing OGG is an incomplete parallel deliverable, not a runtime fallback to another track.
- The prior handoff documents the allowed unavailable-audio behavior as retaining the static super-event image/text presentation and omitting settings-aware playback. That is a presentation fallback, not an alternate audio asset.
- No default, world-revolution, unrelated super-event, generated tone, synthetic drone, or one-shot stinger fallback was found in the inspected Event 025 audio definitions.
- The package defines one opening super-event only. A final-recovery reprise must not be treated as a second super-event or implicit shared audio use without parent approval and explicit documentation; a distinct recovery cue would require a new source-derived edit and ID.
- Event-side assignment and playback-helper invocation remain unverified until the parent performs the gameplay wiring review.

## Parent handoff

1. Treat the current WAV and source FLAC as the verified audio pair, preserving the recorded hashes.
2. Decide whether the missing edited OGG is required as a retained derivative. If required, recreate it from the preserved FLAC and record a newly verified hash rather than relying on the prior handoff value.
3. Verify that the opening event sets `global.current_super_event_audio_id` to `109` and calls `play_current_super_event_sound = yes` through the settings-aware helper.
4. Keep the base sound and six wrapper IDs aligned with the chosen numeric ID and ensure the working-tree sound/interface changes are included in the parent-owned integration commit.
5. Reconcile the stale visual alias name in the temporary GFX handoff, without changing the audio package.
6. Do not add a final-recovery audio route unless the Event 025 design is explicitly expanded and the reuse or new cue is documented.

## Audit change boundary

This audit added only this handoff note. It did not edit gameplay, event, localisation, sound-definition, music-catalogue, GUI, or GFX files. The existing Event025 WAV, sound-definition changes, and interface changes were present in the working tree before this note was created and remain parent-owned.
