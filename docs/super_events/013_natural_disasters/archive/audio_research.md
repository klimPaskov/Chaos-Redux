# Event 013 Natural Disasters super-event audio research

> Implementation closure, 2026-07-11: this file preserves the original research snapshot. All six accepted roles are implemented in slots 67-72 with unique audio ids 37-42, sourced rights and hashes, WAV derivatives, sound registration, settings-aware playback, and final role-specific localisation. The blocker lists below are historical and are superseded by `docs/super_events/013_natural_disasters/audio_production.md` and `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md`.

> Uniqueness correction, 2026-07-11: decoded-audio fingerprinting proved that the implemented ID 37 *Egmont Overture* cue duplicated Soviet Collapse ID 14, despite conflicting catalogue attribution. ID 37's WAV were replaced at their stable paths with Grieg's *In the Hall of the Mountain King*, performed by the Czech National Symphony Orchestra / Musopen Symphony. Commons documents a worldwide public-domain dedication for the recording and public-domain status for the composition. The checksum match, edit, conversion, final hashes, and fingerprint evidence are recorded in `docs/super_events/013_natural_disasters/audio_production.md`. The original ID 37 recommendation below is retained only as superseded research history; the HTML music table records the final Grieg cue.

## Scope and status

This is an audio-research handoff for the four Event 013 abnormal outcomes retained by the accepted specification and text-research pass:

- whole-earth rupture
- massive eruption
- destructive meteor impacts / skyfall
- moving storm corridor

No audio was downloaded, converted, edited, or wired during this pass. No gameplay, localisation, sound-definition, music-definition, spreadsheet, or asset file was changed. The cue windows below are editorial starting points that must be auditioned against the final super-event timing before they are locked.

The repository check found no Event 013 audio package. Existing super-event tracks were not selected for reuse because the super-event workflow requires a unique final track for each role and because several older repository cues have incomplete rights provenance. At the time of this check, `sound/chaosx_sound.asset` defined audio ids through `36`; this does **not** reserve `37` onward. The implementing agent must recheck ids immediately before wiring because other work may allocate them first.

License status below was checked on 2026-07-09. Re-open each file page at acquisition time and preserve the rights statement with the source manifest because hosting metadata can change.

## Recommendation summary

| Event 013 role | Recommended source recording | Source duration | Proposed final cue | Loop | Rights confidence |
| --- | --- | ---: | ---: | --- | --- |
| Whole-earth rupture | Beethoven, *Egmont Overture*, Op. 84, Czech National Symphony Orchestra / Musopen | `9:00.897` | opening `0:00-1:58`, six-second fade-out | no | high |
| Massive eruption | Tchaikovsky, Symphony No. 6, IV. *Adagio lamentoso*, Musopen Symphony Orchestra | `10:18.919` | opening `0:00-1:55`, six-second fade-out | no | high |
| Meteor impacts / skyfall | Mahler, Symphony No. 2, V. *Im Tempo des Scherzos*, DuPage Symphony Orchestra, Barbara Schubert | `35:27` | opening `0:00-1:58`, six-second fade-out | no | high |
| Moving storm corridor | Rossini, *William Tell Overture*, finale, United States Marine Band, Timothy Foley | `11:02` | finale `7:30-9:25`, six-second fade-out | no | high under established repository treatment of U.S. federal recordings; see jurisdiction note |

All four are structured musical performances, not drones, stingers, generated tones, oscillator cues, or sound-effect beds. They are different compositions and different recordings.

## 1. Whole-earth rupture

### Recommended recording

- **Title:** *Egmont Overture*, Op. 84
- **Composer:** Ludwig van Beethoven (1770-1827)
- **Performer / recording source:** Czech National Symphony Orchestra, identified by Wikimedia Commons as Musopen Symphony
- **Recording date shown by source:** 2012
- **Source duration:** `9:00.897`
- **Canonical source and rights page:** [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File%3ABeethoven_-_Egmont_Overture%2C_Op._84_%28Musopen_Symphony%29.flac)
- **Upstream catalog page:** [Musopen recording page](https://musopen.org/music/13441)
- **Upstream preservation collection:** [Internet Archive, Musopen Collection as FLAC](https://archive.org/details/MusopenCollectionAsFlac)
- **Direct original file:** <https://upload.wikimedia.org/wikipedia/commons/8/85/Beethoven_-_Egmont_Overture%2C_Op._84_%28Musopen_Symphony%29.flac>

### Rights record

- **Composition:** public domain. Commons records Beethoven's death in 1827 and identifies the composition as public domain in its country of origin, jurisdictions with a life-plus-100 term or shorter, and the United States.
- **Recording:** Commons states that Musopen released the recording into the public domain worldwide and, where a waiver is not legally possible, grants unconditional use for any purpose. Commons structured data identifies the recording with a CC0 public-domain status.
- **License confidence:** high.
- **Attribution requirement:** none stated. Courtesy credit should still read: `Ludwig van Beethoven, Egmont Overture, Op. 84; Czech National Symphony Orchestra / Musopen; source via Wikimedia Commons.`
- **Modification notice:** not legally required by the stated public-domain grant, but the Event 013 audio manifest should record the trim, fade, resample, and normalization.

### Why it fits

The overture's opening has low orchestral weight, repeated disruptive attacks, and unresolved pressure. It supports the rupture text direction's broken foundations and coast movement without sounding triumphant or like a conventional battle cue. The opening is also less terminal than the overture's victorious ending, which matters because Event 013 continues after the abnormal threshold.

### Cue and processing direction

- Preserve the original FLAC as `docs/assets/013_natural_disasters/audio_source/earth_rupture_egmont_source.flac`.
- Audition `0:00-1:58` as the first cut.
- Keep the first attack intact; do not add a long fade-in.
- Fade out approximately `1:52-1:58` so the excerpt does not end abruptly in the slow introduction.
- Do not loop. The attacks and harmonic pressure form a reveal arc and would make a seam conspicuous.
- Proposed final path template: `sound/013_natural_disasters/super_event_<audio_id>_earth_rupture.wav`.
- Proposed sound mirror template: `sound/013_natural_disasters/super_event_<audio_id>_earth_rupture.wav`.
- Proposed sound wrapper direction: `chaosx_super_event_natural_disasters_earth_rupture_track`.

### Blockers

- The exact edit is not cue-locked until it is auditioned against the final popup duration and voice/text pacing.
- A unique audio id is not reserved.
- The final implementation still needs `.ogg` and WAV exports, asset definitions, settings-aware playback, the music catalog row, and source-manifest hashes.

## 2. Massive eruption

### Recommended recording

- **Title:** Symphony No. 6 in B minor, Op. 74, *Pathetique* - IV. Finale, *Adagio lamentoso*
- **Composer:** Pyotr Ilyich Tchaikovsky (1840-1893)
- **Performer / recording source:** Musopen Symphony Orchestra
- **Source duration:** `10:18.919`
- **Canonical source and rights page:** [Wikimedia Commons OGG file page](https://commons.wikimedia.org/wiki/File%3ATchaikovsky%2C_Symphony_No._6_in_B_minor%2C_Op._74%2C_%27Pathetique%27_-_IV._Finale_Adagio_lamentoso.ogg)
- **Current upstream catalog page for the work:** [Musopen, Symphony No. 6](https://musopen.org/music/80-symphony-no-6-in-b-minor-pathetique-op-74/)
- **Direct original file:** <https://upload.wikimedia.org/wikipedia/commons/e/e8/Tchaikovsky%2C_Symphony_No._6_in_B_minor%2C_Op._74%2C_%27Pathetique%27_-_IV._Finale_Adagio_lamentoso.ogg>

### Rights record

- **Composition:** public domain. Commons records Tchaikovsky's death in 1893 and identifies the composition as public domain in jurisdictions with a life-plus-100 term or shorter and in the United States.
- **Recording:** [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/). The Commons file page expressly permits copying, modification, distribution, performance, and commercial use without permission.
- **License confidence:** high.
- **Attribution requirement:** none under CC0. Courtesy credit should read: `Pyotr Ilyich Tchaikovsky, Symphony No. 6, IV. Adagio lamentoso; Musopen Symphony Orchestra; CC0 source via Wikimedia Commons.`
- **Modification notice:** not required by CC0, but the repository manifest should document the derivative excerpt.

### Why it fits

The movement is slow, orchestral, and catastrophic without becoming an ambient bed. Its descending string writing supports ashfall, darkness, evacuation, and a region continuing to fail after the initial eruption. It also avoids the explosive-action cliche that would flatten the eruption into a single blast.

### Cue and processing direction

- Preserve the source as `docs/assets/013_natural_disasters/audio_source/massive_eruption_pathetique_iv_source.ogg`.
- Audition the opening `0:00-1:55`; it establishes the lament immediately and remains within the preferred super-event range.
- Fade approximately `1:49-1:55` after selecting a musically defensible endpoint.
- Do not use the final two minutes by default. Their dying cadence is powerful but risks making a non-terminal crisis sound like the campaign has ended.
- Do not loop; the bowed phrasing would expose a loop seam and weaken the sense of one irreversible reveal.
- Proposed final path template: `sound/013_natural_disasters/super_event_<audio_id>_massive_eruption.wav`.
- Proposed sound mirror template: `sound/013_natural_disasters/super_event_<audio_id>_massive_eruption.wav`.
- Proposed sound wrapper direction: `chaosx_super_event_natural_disasters_massive_eruption_track`.

### Blockers

- The exact fade point requires an audition; the proposed time may fall inside a sustained phrase.
- A unique audio id is not reserved.
- Final exports, definitions, settings-aware playback, catalog documentation, and source hashes remain implementation work.

## 3. Meteor impacts / skyfall

### Recommended recording

- **Title:** Symphony No. 2 in C minor, V. *Im Tempo des Scherzos*
- **Composer:** Gustav Mahler (1860-1911)
- **Conductor and recording source:** Barbara Schubert and the DuPage Symphony Orchestra
- **Performance date:** 22 May 2004
- **Source duration:** `35:27`
- **Canonical source and rights page:** [Wikimedia Commons OGG file page](https://commons.wikimedia.org/wiki/File%3AMahler_Symphony_no._2%2C_V._Im_Tempo_des_Scherzos.ogg)
- **Upstream performance source:** [Internet Archive, DuPage Symphony Orchestra performance](https://archive.org/details/dupageso-2004-05-22/dso-2004-05-22)
- **Direct original file:** <https://upload.wikimedia.org/wikipedia/commons/c/c9/Mahler_Symphony_no._2%2C_V._Im_Tempo_des_Scherzos.ogg>

### Rights record

- **Composition:** public domain. Mahler died in 1911 and the symphony dates to the nineteenth century; the underlying score is outside the life-plus-100 and pre-1931 thresholds relevant to the other selected public-domain compositions.
- **Recording:** [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/). The Commons page names Schubert and the DuPage Symphony Orchestra as the authors of the recording and states that the file may be copied, modified, distributed, performed, and used commercially without permission.
- **License confidence:** high.
- **Attribution requirement:** none under CC0. Courtesy credit should read: `Gustav Mahler, Symphony No. 2, V; Barbara Schubert and the DuPage Symphony Orchestra; CC0 source via Wikimedia Commons.`
- **Modification notice:** not required by CC0, but the derivative excerpt must be documented in the Event 013 manifest.

### Why it fits

The finale opens with an abrupt orchestral catastrophe and then creates distance and scale. That gives the first confirmed ground-impact cluster a cosmic and liturgical frame without relying on film music, electronic pulses, or a pure choir/drone bed. The opening can support the text-research requirement that the event represent destructive impacts, not an ordinary harmless meteor shower.

### Cue and processing direction

- Preserve the source as `docs/assets/013_natural_disasters/audio_source/skyfall_mahler_2_v_source.ogg`.
- Audition `0:00-1:58` first. The initial attack should occur immediately with the reveal.
- Do not fade in over the opening impact. Use only a de-click if the source needs it.
- Fade approximately `1:52-1:58` after locating a phrase boundary.
- Do not loop. The opening attack would become an obvious repeated stinger, and the super-event requires a one-shot musical arc.
- Proposed final path template: `sound/013_natural_disasters/super_event_<audio_id>_skyfall.wav`.
- Proposed sound mirror template: `sound/013_natural_disasters/super_event_<audio_id>_skyfall.wav`.
- Proposed sound wrapper direction: `chaosx_super_event_natural_disasters_skyfall_track`.

### Blockers

- The source is a full thirty-five-minute movement. The first cut must be auditioned and checked for a clean endpoint rather than accepted solely from the timestamp.
- A unique audio id is not reserved.
- The implementation trigger must still require confirmed destructive impacts; using this cue for a merely visible meteor shower would overstate the event.
- Final exports, definitions, settings-aware playback, catalog documentation, and source hashes remain implementation work.

## 4. Moving storm corridor

### Recommended recording

- **Title:** *William Tell Overture*, finale
- **Composer:** Gioachino Rossini (1792-1868)
- **Transcription:** Wenzel Sedlak
- **Performer:** United States Marine Band
- **Director:** Timothy Foley
- **Recording date and place:** 5-9 June 2000, Center for the Arts, George Mason University, Fairfax, Virginia
- **Source duration:** `11:02`
- **Canonical source and rights page:** [Wikimedia Commons OGG file page](https://commons.wikimedia.org/wiki/File%3AGioachino_Rossini%2C_William_Tell_Overture_%28military_band_version%2C_2000%29.ogg)
- **Archived upstream source:** [U.S. Marine Band download captured by the Internet Archive](https://web.archive.org/web/1/www.marineband.usmc.mil/downloads/audio/overture_to_william_tell.mp3)
- **Direct original file:** <https://upload.wikimedia.org/wikipedia/commons/4/43/Gioachino_Rossini%2C_William_Tell_Overture_%28military_band_version%2C_2000%29.ogg>

### Rights record

- **Composition:** public domain. Commons identifies Rossini's work as public domain in its country of origin and jurisdictions with a life-plus-100 term or shorter.
- **Performance / recording:** Commons identifies the recording as a work made by United States Marines or employees in their official duties and therefore public domain as a U.S. federal government work. The file page also marks the file free of known copyright restrictions, including related and neighboring rights.
- **License confidence:** high under the repository's existing acceptance of U.S. federal band recordings. The legal basis is U.S. federal public domain rather than a worldwide CC0 dedication; if the project later adopts a policy requiring an affirmative worldwide license for every recording, this candidate must be replaced or separately cleared.
- **Attribution requirement:** none under the stated U.S. federal public-domain basis. Courtesy credit should read: `Gioachino Rossini, William Tell Overture; United States Marine Band, Timothy Foley, director; public-domain U.S. federal recording via Wikimedia Commons.`
- **Modification notice:** not legally required by the source statement, but the excerpt and conversion must be documented.

### Why it fits

Commons documents that the finale begins at `7:30`. The finale supplies fast, structured forward motion and march-adjacent orchestration without becoming a wind sound-effect loop. It fits a corridor that crosses multiple regions and makes the path feel like a moving front. It should be reserved for the accepted sustained multi-region corridor, not one local storm.

### Cue and processing direction

- Preserve the source as `docs/assets/013_natural_disasters/audio_source/storm_corridor_william_tell_source.ogg`.
- Begin at the documented finale boundary `7:30` and audition through `9:25` for a `1:55` first cut.
- Preserve the energetic entrance. Fade approximately `9:19-9:25` only after locating the least disruptive cadence in that window.
- Do not loop. The galloping figure would reveal a loop seam and could continue after the super-event closes.
- Proposed final path template: `sound/013_natural_disasters/super_event_<audio_id>_storm_corridor.wav`.
- Proposed sound mirror template: `sound/013_natural_disasters/super_event_<audio_id>_storm_corridor.wav`.
- Proposed sound wrapper direction: `chaosx_super_event_natural_disasters_storm_corridor_track`.

### Blockers

- The final cut needs audition and a clean phrase endpoint.
- A unique audio id is not reserved.
- The U.S.-federal public-domain basis should be rechecked if the project adopts a worldwide-license-only policy.
- The refreshed super-event image follows the accepted sustained multi-state moving storm/tornado-corridor interpretation. This cue fits that moving-front role; no visual/phenomenon mismatch remains.
- Final exports, definitions, settings-aware playback, catalog documentation, and source hashes remain implementation work.

## Acquisition and conversion handoff

The implementing audio pass should use this order:

1. Re-open the canonical Commons page and confirm that its rights block is unchanged.
2. Download the original file from Commons, not a YouTube mirror, streaming re-upload, or search-result preview.
3. Store the untouched source under `docs/assets/013_natural_disasters/audio_source/` using the proposed names above.
4. Record the canonical page URL, direct file URL, access date, source duration, file size, and SHA-256 hash in the Event 013 asset/audio manifest.
5. Audition the proposed window and move the endpoint to a nearby musical cadence if necessary. Preserve the proposed role and duration rather than forcing the exact timestamp.
6. Normalize the four excerpts as one set so perceived volume is consistent. Measure first; use the same integrated-loudness and true-peak target for all four rather than peak-normalizing each independently. The Event 010 audio package is the closest repository precedent.
7. Export the music file as stereo Vorbis `.ogg`, `44.1 kHz`, with a quality setting comparable to the Event 010 package (libvorbis quality `5` is the current documented precedent).
8. If a sound file is required by the existing playback helper, mirror the current working repository format: stereo PCM WAV at `44.1 kHz`. The inspected Event 010 mirror is `pcm_s16le`, `44.1 kHz`, stereo; confirm that this remains the active convention before exporting.
9. Set every sound wrapper to one-shot playback. None of the selected excerpts should loop.
10. Allocate four unique audio ids only after rechecking the final repository state. Keep those ids aligned across script constants, `global.current_super_event_audio_id`, sound definitions, sound definitions, filenames, docs, and `music/chaosx_music_track_list.html`.

A suitable conversion pattern after the cue window and loudness target are approved is:

```bash
ffmpeg -i <preserved-source> \
  -af "atrim=start=<start>:end=<end>,asetpts=N/SR/TB,afade=t=out:st=<fade_start>:d=<fade_duration>,loudnorm=<approved-shared-target>" \
  -ar 44100 -c:a libvorbis -q:a 5 <final>.ogg
```

This is a process template, not a locked command. The Mahler and Beethoven openings should not receive a generic fade-in that removes their initial attacks.

## Alternatives and rejected sources

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Haydn, *The Creation*: `The Representation of Chaos`, St Matthew's Choir / Phiroz Dalal | strong thematic alternate for rupture, not primary | [Commons](https://commons.wikimedia.org/wiki/File%3AHaydn_-_The_Creation_%28Dalal%29_-_1_The_Representation_of_Chaos.oga) records an explicit public-domain dedication, but it uses Creative Commons' retired pre-CC0 dedication and warns that the tool may not be effective outside the United States. Beethoven has the cleaner rights record. |
| Richard Strauss, *Also sprach Zarathustra* introduction, Kevin MacLeod recording | licensed alternate for skyfall, not selected | [Commons](https://commons.wikimedia.org/wiki/File%3AAlso_Sprach_Zarathustra_-_Einleitung.ogg) lists CC BY 3.0 and a useful `1:26` duration, but the recording is culturally coded as majestic ascent and felt less destructive than Mahler's opening. Attribution would be mandatory. |
| Berlioz, *A Dream of a Witches' Sabbath*, U.S. Marine Band | legally usable alternate, not selected | [Commons](https://commons.wikimedia.org/wiki/File%3AA_Dream_of_a_Witches%27_Sabbath_-_transcribed_by_Lt._Col._Jack_T._Cline_-_U.S._Marine_Band.ogg) documents a public-domain composition and U.S. federal performance. Its supernatural program and title would pull the natural-disaster package toward occult spectacle. |
| Wagner, *Ride of the Valkyries*, 1921 Edison recording | rejected | The [Commons page](https://commons.wikimedia.org/wiki/File%3ARichard_Wagner_-_Ride_of_the_Valkyries.ogg) states that the Edison rights donation is unclear and warns that the recording may remain copyrighted in some countries. This does not satisfy the required license confidence. |
| Existing Chaos Redux super-event audio | rejected for Event 013 | Reuse would violate the unique-track direction unless the user approved the exact reuse, and the current catalog contains several older tracks with unverified or incomplete provenance. |

## Explicit blockers before implementation

- No source files have been acquired or hashed.
- No candidate has been auditioned as a final cut inside the super-event UI timing.
- No `.ogg` or WAV derivative exists.
- No final audio ids are reserved; ids above `36` only appeared unused at the time of research.
- No sound asset, settings-aware playback call, script constant, or event trigger has been wired.
- `music/chaosx_music_track_list.html` has no Event 013 rows.
- The storm candidate relies on the project's established acceptance of U.S. federal public-domain recordings. A future worldwide-license-only policy would require a replacement with CC0 or an affirmative worldwide license.
- The moving-storm art/phenomenon caveat and the meteor destructive-impact trigger caveat from the text research remain unresolved implementation concerns.

Until those blockers are cleared, these are source-backed recommendations, not final audio assets.
