# Gods of Africa global-credibility super-event: audio candidate for user approval

Disposition: `blocked` on the user's permission to download one track (agent decisions L5, L17 and L31).

Prepared: 2026-10-05, by web research only. Nothing was downloaded, archived, converted or wired.

## Why this is blocked

Acceptance rows DOC-09 and DOC-10 require the Gods global-credibility super-event, and the super-event skill requires one unique licensed musical recording that no other super-event uses.
Every track archived in `music/chaosx_music_track_list.html` is already used by another super-event.
Downloading a new track needs the user's explicit permission, which no agent or orchestrator message can give.
No silent, duplicate, generated or synthesized cue is used in the meantime.

## Role

From `specs/012_gods_of_africa_assets_presentation.md` ("Super-event presentation direction") and `prompts/012_gods_of_africa_super_event_prompt.md`: the moment foreign powers accept that the Gods' threats have global reach.
Audio direction: one unique licensed musical recording, ceremonial, political and unsettling, possibly choral, orchestral, percussion-led or processional; generic tribal loops, generated audio, drones, ambient beds and one-shot effects are rejected.
Target edit length: about 110 to 120 seconds, as for the other Event 012 cues (110 s and 116 s).

## Proposed candidate

| Field | Value |
| --- | --- |
| Work | *Iyanetha* |
| Creator | John Bartmann (composition and recording) |
| Album | *Public Domain Soundtrack Music: Album One*, track 11, released 2018-08-28 |
| Source page | <https://freemusicarchive.org/music/John_Bartmann/Public_Domain_Soundtrack_Music_Album_One/iyanetha/> |
| Album page | <https://freemusicarchive.org/music/John_Bartmann/Public_Domain_Soundtrack_Music_Album_One/> |
| Licence shown | "Iyanetha by John Bartmann is licensed under a CC0 1.0 Universal License" (<https://creativecommons.org/publicdomain/zero/1.0/>); the album page shows CC0 1.0 for the whole album |
| Recording rights | The same creator controls composition and recording; CC0 waives both. No separate performer or label is named on the page. |
| Source duration | 2:45 (FMA page) |
| Proposed file name after archiving | `docs/super_events/source_audio/012_africa/role_05_iyanetha_john_bartmann_source.mp3` (or `.ogg` if a Commons mirror is preferred); runtime `sound/012_africa/super_event_<audio id>_gods_of_africa.wav`, a fixed 115-second excerpt |
| File size | Not published on the FMA page; it is recorded with the source SHA-256 at archive time |
| Uniqueness | Not used by any super-event; the two Event 012 Bartmann cues are *West in Africa* and *African Moon* from the same CC0 album |
| Fit | The FMA page marks the track as not instrumental, so it carries voices; its isiZulu/isiXhosa title ("it is raining") places it in a Southern African idiom rather than a European picture of Africa, which the presentation spec asks for ("Africa is the source of coordinated political power, not a distant exotic background"). Whether its structure is ceremonial and unsettling enough must be confirmed by listening before acceptance. |

## Checks required at archive time (after permission)

- Confirm that the downloaded file's embedded metadata agrees with the CC0 deed. The 2026-07-29 research (`subagent_handoffs/012_africa_super_event_audio_research_2026-07-29.md`) found CC BY-NC-ND 4.0 tags embedded in some files of this album; the 2026-08-03 handoff accepted *West in Africa* and *African Moon* on the archived FMA pages and Commons mirrors. If this file carries a contradicting licence tag, reject it and use the alternative below.
- Listen to the whole track and choose a 115-second excerpt with a clear opening and a resolved ending; no looping.
- Record source URL, download date, local SHA-256, size, codec, sample rate, channels, the excerpt in and out points, and the final WAV SHA-256, as the 2026-08-03 handoff does.

## Alternative if the candidate fails the checks

*Grand March* ("Triumphal March") from Verdi's *Aida*, transcribed by Giuseppe Creatore, performed by the United States Marine Band (Timothy Foley), recorded 2002 for the album *Retrospective*: <https://commons.wikimedia.org/wiki/File:Triumphal_March_from_Aida.ogg> (5:08).
The recording is a work of the United States federal government and therefore public domain; Verdi's composition is public domain; the copyright status of Creatore's transcription must be confirmed before use (Creatore died in 1952).
It is ceremonial and processional, but it is a European orientalist picture of Africa, which the presentation spec warns against, so it ranks second.

## Rejected during this research

- Samuel Coleridge-Taylor's *African Suite* and *Toussaint L'Ouverture*: the compositions are public domain, but no openly licensed recording was found (IMSLP lists none).
- Commons drum recordings such as *Village Drums of Freedom – Black Africa (djembe mix)*: generic percussion loops, which the prompt rejects.

## Wiring once a track is archived (one change)

Raw sound and six settings-volume wrappers in `sound/chaosx_sound.asset`, a unique audio ID and super-event slot in `common/script_constants/012_africa_world_order_constants.txt`, the image sprite, sourced quote, title, description and button keys under `chaosx_super_event.<slot>`, the one-time trigger in `common/scripted_effects/012_africa_gods_effects.txt` (when Strength first enters the Global band, or at activation if it already qualifies, through the existing `africa_world_emit_super_event` pattern), settings-aware playback, the `music/chaosx_music_track_list.html` row, the Gods guide, and `catalog_changes_pending.md`.
