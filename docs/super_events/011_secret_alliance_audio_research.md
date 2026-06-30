# Event 011 Secret Alliance Super-Event Audio Research

This note covers audio research and handoff only for Event 011 `Secret Alliance`.

## Scope and repo check

- Requested super-event role: public reveal of the hidden pact as the visible `Anti-[target country] Pact`.
- Target mood: restrained diplomatic crisis, ominous and controlled, not apocalyptic.
- Requested audio ID direction: super-event slot `28`, track family `chaosx_super_event_28_*`, and sound definition `chaosx_super_event_secret_alliance_reveal_track`.
- Requested output path: this note plus a final game-ready `.ogg`.
- Repo guidance used: the prompt-provided `AGENTS.md` instructions, Chaos Redux super-event guidance, and repo audio docs.

Existing repo audio/docs inspected before web sourcing:

- `docs/super_events/super_event_audio_packages.md`
- `docs/super_events/010_death_super_event_audio_research.md`
- `docs/super_events/013_natural_disasters_super_event_research.md`
- `music/chaosx_music_track_list.html`
- existing `music/*.ogg` and `sound/*.wav` super-event files

Reuse result:

- I did not reuse an existing repo cue.
- Reason 1: the super-event audio skill requires a unique final track unless reuse is explicitly approved.
- Reason 2: the verified in-repo cues skew too apocalyptic, religious, terminal, or route-specific for a cold diplomatic reveal.
- Reason 3: several older super-event tracks in the repo still have provenance pending, so they are not safe reuse candidates.

## Selected track

- Track title: `Préludes, Book 2 - III. La Puerta Del Vino`
- Composer: Claude Debussy
- Performer / recording source: Giorgi Latsabidze
- Source URL: <https://commons.wikimedia.org/wiki/File:Debussy-_Preludes,_Book_2-_III._La_Puerta_Del_Vino.oga>
- Legitimate download URL used: <https://commons.wikimedia.org/wiki/Special:Redirect/file/Debussy-%20Preludes,%20Book%202-%20III.%20La%20Puerta%20Del%20Vino.oga>
- License:
  - Composition: public domain. Debussy died in 1918.
  - Recording: Free Art License 1.2 on the Wikimedia Commons file page for the performer-uploaded recording.
- License confidence: high
- Usage terms:
  - The composition is safe to use as public-domain music.
  - The recording is usable, but it is not public domain. Distribution of the derivative game cue should preserve attribution and the recording's Free Art License notice.
- Attribution text: `Giorgi Latsabidze, performance of Claude Debussy's "Préludes, Book 2 - III. La Puerta Del Vino," via Wikimedia Commons, Free Art License 1.2.`
- Source duration: `3:11.888`
- Original downloaded source path: `music/source/011_secret_alliance/secret_alliance_reveal_la_puerta_del_vino_source.oga`
- Final `.ogg` path: `music/super_event_secret_alliance_reveal.ogg`
- Final `.ogg` sample rate: `44100 Hz`
- Final duration: `1:52.000`
- Suggested audio ID: super-event slot `28`, track family `chaosx_super_event_28_*`
- Suggested sound definition id: `chaosx_super_event_secret_alliance_reveal_track`
- Suggested super-event use: Event 011 public reveal only

## Why this track fits

- The piece is tense and deliberate without becoming war-march bombast.
- Its pacing suggests maneuver, pressure, and concealed intent becoming visible rather than immediate world-end collapse.
- The darker harmonic color supports the prompt's `cold diplomatic menace` better than the repo's louder catastrophe cues.
- The trimmed opening sustains controlled unease for nearly two minutes and avoids sounding like a generic battle track.

## Candidate comparison

### 1. Selected: `Préludes, Book 2 - III. La Puerta Del Vino`

- Performer / source: Giorgi Latsabidze on Wikimedia Commons
- Source URL: <https://commons.wikimedia.org/wiki/File:Debussy-_Preludes,_Book_2-_III._La_Puerta_Del_Vino.oga>
- Composition rights: public domain
- Recording rights: Free Art License 1.2
- Duration: `3:11.888`
- Suitability: `9/10`
- Notes:
  - Best balance of menace and restraint.
  - Cleaner internal pacing than `Canope`.
  - Mild license burden because the recording is free-culture licensed, not CC0 or PD.

### 2. Backup: `Préludes, Book 2 - X. Canope`

- Performer / source: Giorgi Latsabidze on Wikimedia Commons
- Source URL: <https://commons.wikimedia.org/wiki/File:Debussy-_Preludes,_Book_2-_X._Canope.oga>
- Composition rights: public domain
- Recording rights: Free Art License 1.2
- Duration: `2:46.819`
- Suitability: `8/10`
- Notes:
  - Strong cold and ceremonial mood.
  - More static and sparse in the usable middle than the selected cue.
  - Good fallback if a quieter, more cryptic reveal is preferred later.

### 3. Backup: `Préludes, Book 2 - II. Feuilles mortes`

- Performer / source: Giorgi Latsabidze on Wikimedia Commons
- Source URL: <https://commons.wikimedia.org/wiki/File:Debussy-_Preludes,_Book_2-_II._Feuilles_Mortes.oga>
- Composition rights: public domain
- Recording rights: Free Art License 1.2
- Duration: `2:59.895`
- Suitability: `7/10`
- Notes:
  - Legally usable and tonally serious.
  - Reads more mournful and reflective than threatening.
  - Better for aftermath than reveal.

## Rejected repo-side options

- Existing verified in-repo super-event tracks:
  - Rejected for Event 011 because the repo audio guidance expects a unique final track unless reuse is explicitly approved, and the best-documented in-repo tracks are already strongly tied to other route identities.
- Existing unverified / provenance-pending repo tracks:
  - Rejected because unclear source or licensing remains a blocker.

## Editing and conversion

Source analysis:

- Source codec: `vorbis`
- Source sample rate: `44100 Hz`
- Source channels: `2`
- The selected source has about `1.80` seconds of opening silence and a dead tail section near the end.

Final edit used:

- Start: `1.797`
- Duration retained: `112` seconds
- Fade in: `0.0-0.4`
- Fade out: `106.0-112.0`
- Loudness treatment: `loudnorm=I=-18:TP=-1.5:LRA=11`
- Silence removal: removed the opening silence by starting after the initial dead air

Conversion command used:

```powershell
ffmpeg -y -i "music/source/011_secret_alliance/secret_alliance_reveal_la_puerta_del_vino_source.oga" `
  -af "atrim=start=1.797:duration=112,asetpts=N/SR/TB,afade=t=in:st=0:d=0.4,afade=t=out:st=106:d=6,loudnorm=I=-18:TP=-1.5:LRA=11" `
  -ar 44100 -c:a libvorbis -q:a 5 "music/super_event_secret_alliance_reveal.ogg"
```

Validation:

- `music/super_event_secret_alliance_reveal.ogg` exists.
- Final codec: `vorbis`
- Final sample rate: `44100 Hz`
- Final channels: `2`
- Final duration: `112.000000`
- Final SHA-256: `6E1CE23A95947C845AAA605DBCBE9559A588499C5BF736A8F00D6ED01255EE20`

## Handoff summary

- Final candidate is usable.
- Final selected track: `Préludes, Book 2 - III. La Puerta Del Vino`
- Final game-ready file prepared: `music/super_event_secret_alliance_reveal.ogg`
- Preserved source file: `music/source/011_secret_alliance/secret_alliance_reveal_la_puerta_del_vino_source.oga`
- Suggested audio ID: super-event slot `28`, track family `chaosx_super_event_28_*`
- Suggested sound definition id: `chaosx_super_event_secret_alliance_reveal_track`
- Music track list row: `music/chaosx_music_track_list.html` documents slot `28` for `La Puerta Del Vino`.

## Uncertainties and follow-up notes

- The rights chain is clear, but the recording is under Free Art License 1.2 rather than CC0 or plain public domain. That is legally usable, but the final implementation/docs should carry the attribution and license notice with the mod distribution.
- I did not edit `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, `sound/chaosx_sound.asset`, GUI, GFX, localisation, or event scripts in this pass.
- If the main agent wants a quieter and more funereal reveal, `Canope` is the strongest alternate already downloaded for fast substitution.
