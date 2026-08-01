# Super-Event Text and Audio Research

This note preserves the verified quote research and the original candidate comparison. Final Event 020 super-event audio is now selected, mastered, registered, and wired through the settings-aware wrappers. The durable source, licence, edit, hash, and 44.1 kHz evidence is in `docs/assets/020_black_plague/audio_manifest.md`.

## Final runtime audio reconciliation

- Rat King coronation uses `sound/020_black_plague/super_event_101_rat_king_coronation.wav`, a 110-second stereo 16-bit PCM file at 44,100 Hz derived from Kevin MacLeod's CC BY 3.0 `Gregorian Chant` recording. The runtime identifier is `101`.
- Rat King world end uses `sound/020_black_plague/super_event_102_rat_king_world_end.wav`, a 103.65-second stereo 16-bit PCM file at 44,100 Hz derived from Membeth's public-domain `Dies irae` recording. The runtime identifier is `102`.
- Both tracks have unique sound wrappers and settings-aware volume ladders in `sound/chaosx_sound.asset`; the Rat King coronation and world-end launchers select the corresponding identifier. The final files were read back as stereo 44.1 kHz WAVs before wiring.
- The older `De profundis` and untrimmed `Dies irae` paragraphs below are retained as rejected research history. They are not runtime fallbacks.

## Rat King coronation super-event

### Role

Global transformation. Scattered broods become one sentient Rat King country.

### Verified quote candidate

> “And out of the houses the rats came tumbling.”

- Author: Robert Browning
- Work: *The Pied Piper of Hamelin*
- Publication period: nineteenth century
- Source: Project Gutenberg, https://www.gutenberg.org/files/18343/18343-h/18343-h.htm
- Copyright note: public-domain text in the United States through Project Gutenberg
- Confidence: high
- Fit: the line is short, visual, and specific to mass rat emergence. It should be used only if the final coronation tone favors ominous movement over explicit kingship.

### Backup quote direction

Research a public-domain line about many bodies obeying one ruler, a kingdom arising from corruption, or hidden creatures entering cities. Do not invent a line.

### Button remark

Research required. Desired tone: a short grim or bitter cultural remark about a crown, a piper, or the city discovering who now commands it. A modern copyrighted fragment must remain very short.

### Audio lead 1

**De profundis.ogg**

- Source page: https://commons.wikimedia.org/wiki/File:De_profundis.ogg
- Recording source: sung by Rick Dechance, uploaded by Peirigill
- Duration: 3 minutes 30 seconds
- License: Creative Commons Attribution-ShareAlike options listed on the source page
- Potential use: Rat King coronation, after a licensed edit to one to two minutes
- Concerns: source metadata leaves the composition author field blank and the exact attribution package needs verification. The final audio researcher should confirm title, composition status, recording attribution, derivative terms, sample rate, and trim.
- Status: promising lead, not final

### Alternate audio direction

A dark processional, chant, or court piece with verified public-domain or Creative Commons recording rights. It must be musically structured, unique to this super-event, and no longer than two minutes after final edit unless approved.

## Rat King world-end super-event

### Role

Terminal scenario. The Rat King has taken over the world.

### Verified quote candidate

> “And I looked, and behold a pale horse: and his name that sat on him was Death.”

- Source: Revelation 6:8, King James Version
- Source page: https://www.biblegateway.com/passage/?search=Revelation+6%3A8&version=KJV
- Copyright note: the source page identifies the King James Version text as public domain
- Confidence: high
- Fit: the line connects death, judgment, and a sovereign figure without naming the rats directly. It is final enough for a terminal moment.

### Backup quote direction

Research a short public-domain line from Boccaccio, medieval plague writing, scripture, or judgment poetry that conveys emptied cities and the end of human order. Verify exact wording and translation.

### Button remark

Research required. Desired tone: final, brief, and cold. Avoid generic phrases about the end beginning or the world changing forever.

### Audio lead 1

**Dies.irae.ogg**

- Source page: https://commons.wikimedia.org/wiki/File:Dies.irae.ogg
- Recording: Gregorian chant recording by Membeth
- Date: 12 August 2010
- Duration: 7 minutes 14 seconds
- License: dedicated to the public domain by the uploader
- Potential use: Rat King world-end after selecting and trimming a one to two minute passage
- Required work: preserve the source, choose a musically complete excerpt, fade carefully, convert final WAV to 44.1 kHz, document the derivative and final duration, create a unique audio ID and sound wrapper
- Status: strong lead, not final wired track

### Audio exclusion

The coronation and world-end super-events cannot reuse the same track. No test tone, drone, beep, noise bed, or synthesized placeholder is acceptable.

## Optional Rat King defeat aftermath

This super-event exists only when the Rat King crisis was global, long, and catastrophic.

### Quote direction

Research public-domain writing about survival, rebuilding, memory, vigilance, or the cost of victory. Avoid a purely triumphant quote.

### Audio direction

A unique lament, memorial hymn, or restrained orchestral piece with verified rights. Do not reuse either rat victory track.

## Implementation research checklist

For each final super-event:

- final title researched or written as original localisation
- final description written from the spec direction
- button remark source verified when it uses a cultural reference
- quote exact wording, author, source, date, confidence, and public-domain or copyright note recorded
- audio title, creator, performer, source URL, license, duration, attribution, source path, final path, edit steps, and 44.1 kHz validation recorded
- unique audio ID and settings-aware playback
- final image, DDS, sprite, and manifest complete
- music track list HTML row updated with super-event ID
