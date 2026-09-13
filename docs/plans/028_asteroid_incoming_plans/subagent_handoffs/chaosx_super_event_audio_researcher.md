# Chaos Redux Super-Event Audio Researcher Handoff

> Research handoff. Parent-owned Event 116 registry, sprite, sound asset, settings-aware playback, and catalog wiring are now present; current evidence and remaining blockers are in `../final_audit.md`.

## Status

Complete for the bounded Event 028 audio package; shared sound wiring remains parent-owned.

## Recommendation

Use Johannes Brahms’s *Tragic Overture, Op. 81*, performed by the Czech National Symphony Orchestra and published as the Musopen Symphony recording.

The prepared excerpt is the opening 1:55. It has immediate orchestral weight for the asteroid impact reveal, retains structured development for the destroyed-state and spreading-dust visuals, and ends with a controlled fade rather than a hard musical stop.

The recording is distinct from existing Chaos Redux super-event audio. The exact composition was not found in `music/chaosx_music_track_list.html`, although other Brahms works are already catalogued.

## Files delivered

Original preserved source: `docs/assets/028_asteroid_incoming/source_audio/Brahms_Tragic_Overture_Op81_Musopen_Symphony.flac`.

Original source SHA-256: `540F340E6433C622ED1F58598693B04A1F596E07550768B0BD119E979A7A345A`.

The local source SHA-1 is `2C38126257D167B1265C13BBF8EDA81C838B3546`, matching the checksum published on the Wikimedia Commons file page.

Final game-ready WAV: `sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav`.

Final SHA-256: `AC3841688C9235404FCF3717630A69A44DAFCA362775F7A372EFB7E093CBFE59`.

Companion audio-worker OGG: `sound/028_asteroid_incoming/super_event_028_asteroid_impact.ogg`.

Companion OGG SHA-256: `B2D135EF6CDE86824F74037135F09E26ACD368FE3D9C83A23D99B3A221CAB2E0`.

Final probe: PCM signed 16-bit little-endian, stereo, 44,100 Hz, exactly 115.000000 seconds.

Research note: `docs/super_events/028_asteroid_incoming_super_event_research.md`.

## Rights evidence

Composition: Brahms’s 1880 *Tragic Overture, Op. 81* is public domain.

Recording: the [Wikimedia Commons FLAC record](https://commons.wikimedia.org/wiki/File:Brahms_-_Tragic_Overture,_Op._81_%28Musopen_Symphony%29.flac) identifies the performance as released into the worldwide public domain by Musopen and links the [Musopen work page](https://musopen.org/music/2120-tragic-overture-op-81/) and [Musopen FLAC archive](https://archive.org/details/MusopenCollectionAsFlac).

Direct source URL used: `https://upload.wikimedia.org/wikipedia/commons/c/c4/Brahms_-_Tragic_Overture%2C_Op._81_%28Musopen_Symphony%29.flac`.

Attribution to retain: “*Tragic Overture, Op. 81* — Johannes Brahms; performed by the Czech National Symphony Orchestra (Musopen Symphony). Recording source: Musopen, via Wikimedia Commons. Recording released to the public domain by Musopen; composition public domain.”

## Conversion record

The source was cut from 00:00.000 to 01:55.000, given a 0.10-second fade-in and a 5-second fade-out beginning at 01:50.000, normalized with `loudnorm=I=-19:TP=-2:LRA=11:linear=false`, and converted to stereo 44.1 kHz PCM16 WAV.

The companion OGG was encoded from the verified WAV with `libvorbis -q:a 5` at 44.1 kHz stereo; the requested WAV remains the canonical Event 028 artifact.

No pitch shift, time stretch, loop, synthetic layer, noise bed, drone, test tone, explosion, or placeholder was used.

## Suggested parent wiring

Suggested base sound definition id: `chaosx_super_event_028_asteroid_impact_track`.

Suggested catalogue display title: `The Stone's Verdict`.

The parent assigned distinct shared presentation slot `116` and created the matching timing wrappers. Slot `28` is already used by the Holy Realm cue at `sound/003_holy_realm/super_event_28_mandala_of_nations.wav`, with existing wrapper ids `chaosx_super_event_28_sound_0_5`, `chaosx_super_event_28_sound_1_0`, `chaosx_super_event_28_sound_1_5`, `chaosx_super_event_28_sound_2_0`, `chaosx_super_event_28_sound_2_5`, and `chaosx_super_event_28_sound_3_0`.

No edit was made to `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html`, event files, localisation, GFX, GUI, or spreadsheets.

Repository note: the existing `.gitignore` excludes `docs/assets/` and `docs/super_events/`, so the preserved source and full research note are present on disk but may require explicit force-staging by the parent if they are intended to be committed. No git index changes were made here.

## Candidate review summary

Other real recordings reviewed were Strauss’s *Also sprach Zarathustra — Einleitung* (CC BY 3.0, rejected for triumphal sunrise association), Mussorgsky’s *Night on Bald Mountain* (Musopen public-domain recording, rejected for occult/folkloric role fit), Saint-Saëns’s cello-concerto movement (Musopen public-domain recording, rejected for intimate scale), Brahms’s *Symphony No. 2* slow movement (CC0 Musopen recording, rejected for pacing and distinctiveness), Beethoven’s *Symphony No. 7 Allegretto* in John Michel’s CC BY-SA 3.0 cello arrangement (rejected for scale and edit cost), and Allegri’s *Miserere* (Commons-documented CC BY 3.0 YouTube-derived recording, rejected under the high-confidence provenance rule).

All candidate rights and source links are recorded in the full research note.
