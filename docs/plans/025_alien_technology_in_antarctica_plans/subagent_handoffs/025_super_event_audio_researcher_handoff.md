# Event 025 super-event audio researcher handoff

Status: audio research and candidate preparation complete; parent-owned slot, sound-definition, catalogue, and event wiring remain pending.

## Scope and package reading

- Event: `025 Alien Technology in Antarctica`.
- Parent brief: `docs/specs/025_alien_technology_in_antarctica_specs/prompts/025_super_event_audio_researcher_prompt.md`.
- Package manifest: `docs/specs/025_alien_technology_in_antarctica_specs/package_manifest.md`.
- Super-event/audio brief: `docs/specs/025_alien_technology_in_antarctica_specs/specs/010_assets_animation_and_super_event.md`.
- Existing pattern references: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_super_event_audio_research_handoff.md` and the Super Event 36 section in `docs/super_events/010_death/audio_research.md`.

The Event 025 package defines one opening super-event with a remote, cold, exploratory, tense, scientific, and uncertain role. The package describes final recovery as the terminal expedition operation, but it does not define a separate final-recovery super-event slot or numeric audio ID. This handoff therefore delivers one opening cue that can also support the final recovery outcome as a parent-approved reprise or source-derived edit, without inventing a second slot.

## Selected candidate

- Track title: `In the Steppes of Central Asia`.
- Composer: Alexander Borodin (1833–1887).
- Performer / recording source: Musopen Symphony, with embedded source metadata identifying the Czech National Symphony Orchestra.
- Source rights page: <https://commons.wikimedia.org/wiki/File:Borodin_-_In_the_Steppes_of_Central_Asia_(Musopen_Symphony).flac>.
- Source revision receipt: <https://commons.wikimedia.org/w/index.php?title=File:Borodin_-_In_the_Steppes_of_Central_Asia_(Musopen_Symphony).flac&oldid=963504941>.
- Direct original download: <https://upload.wikimedia.org/wikipedia/commons/c/c6/Borodin_-_In_the_Steppes_of_Central_Asia_%28Musopen_Symphony%29.flac>.
- Upstream catalogue: <https://musopen.org/music/681-in-the-steppes-of-central-asia/>.
- Upstream archive: <https://archive.org/details/MusopenCollectionAsFlac>.
- License: the composition is public domain; the Commons record states that Musopen released the recording worldwide into the public domain, with an unconditional fallback grant where a dedication is not legally possible. The CC0 deed is <https://creativecommons.org/publicdomain/zero/1.0/>.
- License confidence: high.
- Legal attribution: not required under the stated CC0 recording dedication. Courtesy attribution is recommended as `Alexander Borodin, In the Steppes of Central Asia; Musopen Symphony / Czech National Symphony Orchestra, CC0 recording via Musopen and Wikimedia Commons.`
- Source format and duration: FLAC, stereo, 48,000 Hz, 458.240 seconds, 73,785,694 bytes.
- Commons source SHA-1: `A25677D7B6435F8F18475F4F7E9D1EF75A895481`.
- Local source SHA-256: `6E53A2E3B48B070EF8ABE95A9D411D29BE68D7B2163347360405F33072648857`.

## Delivered files

- Preserved source: `docs/assets/025_alien_technology_in_antarctica/source_audio/borodin_in_the_steppes_of_central_asia_musopen_symphony_source.flac`.
- Rights-page receipt: `docs/assets/025_alien_technology_in_antarctica/source_receipts/commons_borodin_steppes_rights_page_oldid_963504941.html`.
- CC0 receipt: `docs/assets/025_alien_technology_in_antarctica/source_receipts/cc0_1.0_deed.html`.
- Requested final OGG candidate: `sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.ogg`.
- OGG SHA-256: `7C7A7D48B54B5A1E3E494EC7AFD2611AE9E937D611053204C040733C22B35E23`.
- Matching parent-engine WAV derivative: `sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.wav`.
- WAV SHA-256: `BCB9EE95809F01413A947D10D684859B8D20DA1B0319A1F1D384263E431EB126`.
- Final duration: exactly `115.000000` seconds.
- Final format: OGG is Vorbis, stereo, 44,100 Hz; WAV is signed 16-bit PCM, stereo, 44,100 Hz.
- Both final files decode successfully with FFmpeg.

## Role fit and pacing

The opening excerpt begins with restrained orchestral space and gradually adds motion, which supports the distant Antarctic signal, uncertain wreck report, and the scale of a scientific expedition before the race becomes urgent. Its structured orchestral writing gives the super-event a real musical arc instead of a drone or stinger. The same cue can land a final recovery outcome as a controlled, non-triumphal return to the recovered material; if the parent wants the recovery moment to have its own distinct sound surface, derive a later excerpt from the preserved FLAC and assign it a separate parent-owned ID.

The source is not reused by any existing Event 016 or Super Event 36 package, and repository title/performer searches found no Event 025 collision. Mendelssohn's otherwise strong polar-seascape candidate was not reused because the existing Event 013 package already owns *The Hebrides* recording.

## Editing and conversion record

The final edit takes source time `00:00.000` through `01:55.000`, retains the natural dynamics, applies a `0.25`-second fade-in, applies a `5`-second fade-out from `01:50.000` to `01:55.000`, and applies no limiting or synthetic layers. The source is resampled from 48,000 Hz to 44,100 Hz with FFmpeg's SoXr resampler and kept stereo.

Equivalent conversion commands were:

```text
ffmpeg -hide_banner -loglevel error -y -i <source.flac> -af "atrim=start=0:duration=115,asetpts=N/SR/TB,afade=t=in:st=0:d=0.25,afade=t=out:st=110:d=5,aresample=44100:resampler=soxr" -ac 2 -c:a libvorbis -q:a 6 <candidate.ogg>
ffmpeg -hide_banner -loglevel error -y -i <source.flac> -af "atrim=start=0:duration=115,asetpts=N/SR/TB,afade=t=in:st=0:d=0.25,afade=t=out:st=110:d=5,aresample=44100:resampler=soxr" -ac 2 -c:a pcm_s16le <candidate.wav>
```

The original FLAC remains untouched. If the parent applies a gain change after listening in context, create a new derivative from the preserved FLAC and record the new hash; do not normalize by repeatedly decoding the lossy OGG.

## Suggested IDs and runtime handoff

- Suggested base track ID: `chaosx_super_event_025_antarctic_first_reveal_track`.
- Suggested opening audio key: parent-assigned numeric super-event/audio ID, not reserved by this researcher.
- Suggested wrapper family after the parent assigns the numeric ID: `chaosx_super_event_<PARENT_ID>_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`.
- Suggested opening use: the full 115-second OGG/WAV excerpt for the one opening super-event.
- Suggested final-recovery use: only if the parent confirms that final recovery should play audio; treat exact reuse as the user-requested cross-use, or derive a distinct later-section cue and ID if the recovery outcome is a separate presentation surface.

The existing Event 016 and Super Event 36 pattern uses a base sound pointing to the event-owned WAV plus six settings-volume wrappers at `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`, with playback routed through the settings-aware helper. The parent must choose the final numeric ID, add the base definition and wrappers, set `global.current_super_event_audio_id`, and call `play_current_super_event_sound = yes`. No sound definition or gameplay file was edited here.

## Static fallback expectations

The opening super-event itself has a static visual presentation and does not need an animated-audio fallback. There is no legally equivalent static audio fallback asset. If audio is disabled or unavailable, retain the static super-event image/text presentation and omit playback through the settings-aware helper; do not substitute `default.ogg`, `world_revolution.ogg`, another super-event's track, a test tone, a synthesized drone, or a one-shot stinger. The event must not be marked audio-complete until the parent wires the delivered candidate and documents any approved recovery reuse.

## Candidate comparison and rejections

| Candidate | Rights result | Fit result |
| --- | --- | --- |
| Borodin, *In the Steppes of Central Asia*, Musopen Symphony | Selected; public-domain composition and worldwide CC0 recording release | Strong remote/exploratory orchestral build with enough tension for the first reveal and a controlled recovery landing |
| Holst, *Uranus, the Magician*, U.S. Air Force Heritage of America Band | Rejected for this package; Commons identifies a U.S. federal public-domain basis but not a comparable worldwide dedication | Strong alien/scientific association, but the global-rights basis is weaker than the selected CC0 source; source page: <https://commons.wikimedia.org/wiki/File:Holst-_uranus.ogg> |
| Bach, *Fugue No. 2 in C minor, BWV 847*, Kimiko Ishizaka | Legally usable CC0 recording, but not selected | Good methodical tension at 1:56, but solo piano is too intimate for the Antarctic expedition-scale reveal; source page: <https://commons.wikimedia.org/wiki/File:Kimiko_Ishizaka_-_Bach_-_Well-Tempered_Clavier,_Book_1_-_04_Fugue_No._2_in_C_minor,_BWV_847.ogg> |
| Debussy, *Nuages*, Reinhold Behringer digital-sample realization | Rejected under the brief's generated/sample-music restriction; CC BY-SA 3.0 | Tonally atmospheric, but it is a digital realization rather than the preferred intentional recording; source page: <https://commons.wikimedia.org/wiki/File:Debussy_Nocturnes1Nuages_VPO.ogg> |
| Mendelssohn, *The Hebrides (Fingal's Cave)*, Musopen Symphony | Rejected as reuse; existing Event 013 owns the recording | Excellent polar and seascape fit, but not unique to Event 025; existing package evidence: `docs/super_events/013_natural_disasters/audio_production.md` |

## Remaining parent work

1. Assign a unique numeric super-event/audio ID after the parent collision scan.
2. Decide whether the final recovery outcome is audio-bearing; if yes, document the approved reuse or derive a distinct edit from the preserved FLAC.
3. Rename or retain the delivered runtime file according to the assigned ID and the live audio path convention without changing its verified contents unless a new edit is intentional.
4. Add the base sound definition, six settings-volume wrappers, `global.current_super_event_audio_id`, and `play_current_super_event_sound = yes` in the parent-owned wiring change.
5. Add the final selected row to `music/chaosx_music_track_list.html` with title, composer, performer/source, duration, final path, CC0/public-domain rights, attribution courtesy text, and final checksum.
6. Keep the temporary `docs/assets/025_alien_technology_in_antarctica/` evidence workspace until parent review and event acceptance are complete; promote durable provenance before declaring the full Event 025 package complete.

## Blockers and simplifications

- No licensing blocker remains for the selected candidate.
- No source-download blocker remains; the original lossless FLAC and frozen rights receipts are present.
- The final numeric super-event/audio ID is not supplied by the package and was intentionally not invented or reserved.
- A separate final-recovery cue was not manufactured because the parent package defines only one opening super-event; the preserved CC0 source supports a later derived edit if the parent expands that presentation surface.
- No gameplay, event, localisation, GUI, GFX, spreadsheet, sound-definition, or canonical music-catalogue file was edited.
