# Event 015 Super-Event Audio Research Handoff

Date: 2026-07-01
Event: `015_utopia_manifesto`
Scope: audio research, source verification, download, processing, and handoff only

## Result

Two unique, legally usable candidates were secured and processed for the late `utopia_manifesto` super-events:

- `New Utopia`
- `Marked Bounds State`

I checked the existing documented Chaos Redux super-event audio package list first and did not reuse any of the currently documented tracks in [docs/super_events/super_event_audio_packages.md](/C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/super_events/super_event_audio_packages.md:1).

## Final Package A

### Super-event use

- Super-event: `New Utopia`
- Suggested sound definition id: `chaosx_super_event_new_utopia_track`
- Suggested wrapper / audio id stem: `new_utopia`
- Intended mood: solemn proclamation, communal dignity, quiet hope, residual unease

### Selected track

- Title: `Ave Maria`
- Composer: Anton Bruckner
- Performer / recording source: United States Navy Band, Sea Chanters ensemble
- Source page: <https://commons.wikimedia.org/wiki/File:Ave_Maria_(USNB).ogg>
- Underlying source noted by the file page: `http://www.navyband.navy.mil/Sounds/Sea%20Chanters/Ave%20Maria.mp3`
- License: public domain U.S. federal government recording; Commons also marks it with Public Domain Mark 1.0
- License / source proof:
  - Wikimedia Commons states the recording is a work of a U.S. Navy employee made as part of official duties.
  - The Commons page also states the file is free of known restrictions under copyright law.
- License confidence: high
- Composition rights status: public-domain composition
- Recording rights status: public-domain U.S. federal government recording
- Original duration: `3:13.698`
- Final processed duration: `1:56.000`

### Attribution text

No attribution is legally required for U.S. federal public-domain status, but a courtesy credit is recommended:

`Anton Bruckner, "Ave Maria," performed by the United States Navy Band Sea Chanters ensemble. Public domain U.S. federal government recording via Wikimedia Commons.`

### Files

- Original downloaded source: `docs/super_events/source_audio/015_utopia_manifesto/ave_maria_usnb_original.ogg`
- Final 44.1 kHz OGG: `docs/super_events/source_audio/015_utopia_manifesto/super_event_new_utopia_final.ogg`

### Editing and conversion steps

1. Downloaded the original OGG from Wikimedia Commons.
2. Kept the original source file unmodified.
3. Trimmed to the opening `116` seconds.
4. Added a `0.75` second fade-in.
5. Added a `5` second fade-out starting at `111` seconds.
6. Applied loudness normalization.
7. Rendered final OGG as Vorbis at `44100 Hz`.

### Why it fits

This recording is more sacred than civic, but it matches the prompt's needed mix of ceremonial dignity and restrained unease better than the other clean-license options I found. The choir texture gives `New Utopia` a public, processional feeling without sounding triumphant or militaristic, which suits a fragile proclamation of a new commonwealth rather than a victory parade.

## Final Package B

### Super-event use

- Super-event: `Marked Bounds State`
- Suggested sound definition id: `chaosx_super_event_marked_bounds_state_track`
- Suggested wrapper / audio id stem: `marked_bounds_state`
- Intended mood: austere doctrine, coercive order, grim procession, territorial menace

### Selected track

- Title: `Funeral March, Op. posth. 72 no. 2`
- Composer: Frederic Chopin
- Performer / recording source: Aya Higuchi, via Musopen-hosted source mirrored on Wikimedia Commons
- Source page: <https://commons.wikimedia.org/wiki/File:Funeral_March_Chopin_Op_72_2.ogg>
- Underlying source noted by the file page: <https://musopen.org/music/2608/frederic-chopin/funeral-march-in-c-minor-op-posth-72-no-2/>
- License: `CC0 1.0 Universal Public Domain Dedication`
- License / source proof:
  - Wikimedia Commons explicitly marks the file as `CC0 1.0 Universal Public Domain Dedication`.
  - The file page identifies Aya Higuchi as performer and links the Musopen source entry.
- License confidence: high
- Composition rights status: public-domain composition
- Recording rights status: CC0-dedicated recording
- Original duration: `5:51.768`
- Original source sample rate: `48000 Hz`
- Final processed duration: `1:50.000`

### Attribution text

Not legally required under CC0, but a courtesy credit is recommended:

`Frederic Chopin, "Funeral March, Op. posth. 72 no. 2," performed by Aya Higuchi. CC0 recording via Wikimedia Commons / Musopen.`

### Files

- Original downloaded source: `docs/super_events/source_audio/015_utopia_manifesto/chopin_funeral_march_op72_no2_original.ogg`
- Final 44.1 kHz OGG: `docs/super_events/source_audio/015_utopia_manifesto/super_event_marked_bounds_state_final.ogg`

### Editing and conversion steps

1. Downloaded the original OGG from Wikimedia Commons.
2. Kept the original source file unmodified.
3. Trimmed to the opening `110` seconds.
4. Added a `0.75` second fade-in.
5. Added a `5` second fade-out starting at `105` seconds.
6. Applied loudness normalization.
7. Resampled from `48000 Hz` to `44100 Hz`.
8. Rendered final OGG as Vorbis at `44100 Hz`.

### Why it fits

This cue is not an overt martial march, which is an advantage here. `Marked Bounds State` reads less as battlefield release and more as a cold public doctrine becoming visible through survey posts, guarded settlement, and coercive boundary logic. The piano funeral march gives the route a legalistic, state-funereal severity that supports the super-event's reveal of public good rhetoric curdling into territorial force.

## Validation

- `docs/super_events/source_audio/015_utopia_manifesto/super_event_new_utopia_final.ogg`
  - codec: Vorbis
  - sample rate: `44100 Hz`
  - duration: `116.000` seconds
- `docs/super_events/source_audio/015_utopia_manifesto/super_event_marked_bounds_state_final.ogg`
  - codec: Vorbis
  - sample rate: `44100 Hz`
  - duration: `110.000` seconds

## Non-selected leads

These were researched but rejected for final packaging:

- `The Tudor Consort - Palestrina - Sicut lilium inter spinas`
  - Good tonal fit for `New Utopia`, but the Wikimedia Commons mirror is still flagged `License review needed`, so I did not use it as the final package.
- `Tallis if ye love me performed by the dwsChorale`
  - Better textual / emotional fit than some instrumental options, but the licensing path is older `GFDL-self` transwiki material and was less practical for a clean mod-package handoff than the U.S. Navy Band public-domain recording.
- `Funeral March for Queen Mary - H. Purcell`
  - Good tonal fit for `Marked Bounds State`, but the Commons upload is a YouTube-imported `CC BY 3.0` file still marked `License review needed`, so I rejected it in favor of the clearer CC0 Chopin recording.

## Blockers and uncertainties

No licensing blocker prevented delivery.

Remaining uncertainty is aesthetic rather than legal:

- `New Utopia` would ideally have an even more explicitly early-modern civic or choral source, but the strongest thematic matches I found had weaker license-review status than the selected public-domain Navy Band recording.
- `Marked Bounds State` could also support a harsher orchestral cue, but the cleaner-rights options in that direction were less trustworthy than the chosen CC0 recording.

## Suggested next wiring handoff fields

For the main agent when wiring later:

- `New Utopia`
  - music file candidate: `music/super_event_new_utopia.ogg`
  - sound-channel candidate id: `chaosx_super_event_new_utopia_track`
- `Marked Bounds State`
  - music file candidate: `music/super_event_marked_bounds_state.ogg`
  - sound-channel candidate id: `chaosx_super_event_marked_bounds_state_track`
