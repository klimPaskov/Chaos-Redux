# Event 010 Death Super-Event Audio Research

This note covers audio research only for Event 010 `Death`.

The role labels below are planning labels, not final player-facing localisation.

## Scope result

- Mandatory roles completed: mainland reveal, world-end, defeat aftermath, whole world consumed.
- Optional role blocked: Herald oath reveal.
- No existing approved `music/*.ogg` track was reused.

## Packaging notes

- Preserved source downloads live under `music/source/010_death/`.
- Final candidates were exported to `44.1 kHz` `.ogg` under `music/`.
- Conversion used `ffmpeg`, `libvorbis`, quality `5`, plus a short fade-out on each final clip.
- I rejected unclear-license reuse, generated audio, and the repo's existing unverified `music/zombies_defeat.ogg`.

## Selected audio

### 1. Mainland reveal

- Role: first public mainland recognition, coastal absence, official naming of the crisis.
- Selected track: `La Cathédrale engloutie`
- Composer: Claude Debussy
- Performer / recording source: Ivan Ilic, own recording uploaded to Wikimedia Commons
- Source URL: https://commons.wikimedia.org/wiki/File:La_Cath%C3%A9drale_engloutie_-_Claude_Debussy_-_performed_by_Ivan_Ilic.ogg
- License:
  - Composition: public domain in the United States and other life+70 jurisdictions; Debussy died in 1918.
  - Recording: CC BY 3.0, explicitly licensed by performer on Wikimedia Commons.
- License confidence: high
- Attribution required: `Ivan Ilic, "La Cathédrale engloutie" recording, CC BY 3.0 via Wikimedia Commons.`
- Source duration: `5:24.920`
- Original downloaded source path: `music/source/010_death/death_reveal_la_cathedrale_engloutie_source.ogg`
- Final `.ogg` path: `music/super_event_death_reveal.ogg`
- Final duration: `1:52.000`
- Suggested music id: `super_event_death_reveal_music`
- Suggested sound definition id: `super_event_death_reveal_sound`
- Suggested super-event use: mainland reveal only
- Editing and conversion:
  - start `0:00`
  - end `1:52`
  - fade out `1:46-1:52`
  - export `44.1 kHz` Vorbis
- Why it fits:
  - The submerged-cathedral image matches the spec's drowned-shoreline and reinterpreted-island-report tone.
  - It feels like discovery and recognition, not yet total apocalypse.

### 2. World-end

- Role: terminal global spread, every coast exposed, the last safe borders failing.
- Selected track: `Piano Sonata No. 2 in B-flat minor, Op. 35 - III. Marche funèbre`
- Composer: Frédéric Chopin
- Performer / recording source: Andreas Xenopoulos performance distributed via Musopen and mirrored on Wikimedia Commons
- Source URL: https://commons.wikimedia.org/wiki/File:Frederic_Chopin_Piano_Sonata_No.2_in_B_flat_minor_Op35_-_III_Marche_Funebre.ogg
- License:
  - Composition: public domain; Chopin died in 1849.
  - Recording: CC0 / public-domain dedication on Wikimedia Commons; source traced to Musopen public-domain upload path.
- License confidence: high
- Attribution required: not legally required; courtesy credit recommended to performer and Musopen mirror.
- Source duration: `9:49.044`
- Original downloaded source path: `music/source/010_death/death_world_end_chopin_funeral_march_source.ogg`
- Final `.ogg` path: `music/super_event_death_world_end.ogg`
- Final duration: `1:57.980`
- Suggested music id: `super_event_death_world_end_music`
- Suggested sound definition id: `super_event_death_world_end_sound`
- Suggested super-event use: world-end only
- Editing and conversion:
  - start `0:00`
  - end `1:57.98`
  - fade out `1:52-1:57.98`
  - export `44.1 kHz` Vorbis
- Why it fits:
  - It gives the strongest finality of the researched set without sounding like an abstract drone.
  - The pacing feels continental and ceremonial rather than merely scary.

### 3. Defeat aftermath

- Role: costly victory, grief, empty land, no restoration.
- Selected track: `Sonata No. 8 in C minor, Op. 13 "Pathétique" - II. Adagio cantabile`
- Composer: Ludwig van Beethoven
- Performer / recording source: Paul Pitman performance distributed via Musopen and mirrored on Wikimedia Commons
- Source URL: https://commons.wikimedia.org/wiki/File:Beethoven%2C_Sonata_No._8_in_C_Minor_Pathetique%2C_Op._13_-_II._Adagio_cantabile.ogg
- License:
  - Composition: public domain; Beethoven died in 1827.
  - Recording: CC0 / public-domain dedication on Wikimedia Commons by the Musopen-derived uploader.
- License confidence: high
- Attribution required: not legally required; courtesy credit recommended to Paul Pitman and Musopen.
- Source duration: `4:58.210`
- Original downloaded source path: `music/source/010_death/death_defeat_pathetique_adagio_source.ogg`
- Final `.ogg` path: `music/super_event_death_defeat_aftermath.ogg`
- Final duration: `1:56.000`
- Suggested music id: `super_event_death_defeat_aftermath_music`
- Suggested sound definition id: `super_event_death_defeat_aftermath_sound`
- Suggested super-event use: defeat aftermath only
- Editing and conversion:
  - start `0:00`
  - end `1:56`
  - fade out `1:50-1:56`
  - export `44.1 kHz` Vorbis
- Why it fits:
  - It is reflective and wounded rather than triumphant.
  - The melodic line supports mourning and vigilance better than a victory cue would.

### 4. Whole world consumed

- Role: final completion, silence, no witness, no record keeper.
- Selected track: `Piano Sonata No. 29 in B-flat major, Op. 106 "Hammerklavier" - III. Adagio sostenuto`
- Composer: Ludwig van Beethoven
- Performer / recording source: Paul Pitman performance distributed via Musopen and mirrored on Wikimedia Commons
- Source URL: https://commons.wikimedia.org/wiki/File:Beethoven%2C_Piano_Sonata_No._29_in_B-flat_Major%2C_Op._106_Hammerklavier_-_III._Adagio_sostenuto.ogg
- License:
  - Composition: public domain; Beethoven died in 1827.
  - Recording: CC0 / public-domain dedication on Wikimedia Commons by the Musopen-derived uploader.
- License confidence: high
- Attribution required: not legally required; courtesy credit recommended to Paul Pitman and Musopen.
- Source duration: `17:15.102`
- Original downloaded source path: `music/source/010_death/death_world_consumed_hammerklavier_adagio_source.ogg`
- Final `.ogg` path: `music/super_event_death_world_consumed.ogg`
- Final duration: `2:02.000`
- Suggested music id: `super_event_death_world_consumed_music`
- Suggested sound definition id: `super_event_death_world_consumed_sound`
- Suggested super-event use: whole world consumed only
- Editing and conversion:
  - start `0:00`
  - end `2:02`
  - fade out `1:56-2:02`
  - export `44.1 kHz` Vorbis
- Why it fits:
  - It is the sparsest and most exhausted of the finished set.
  - It reads as aftermath without survivors, which matches the no-audience end state.

## Blocked role

### Optional 5. Herald oath reveal

- Status: blocked
- Intended candidate: `Sonata No. 14 in C-sharp minor "Moonlight", Op. 27 No. 2 - I. Adagio sostenuto`, Paul Pitman for Musopen, with rights page at https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_sonata_no._14_in_c_sharp_minor_%27moonlight%27%2C_op._27_no._2_-_i._adagio_sostenuto.ogg
- Rights assessment:
  - Composition: public domain
  - Recording: rights page indicates a free-use / public-domain Musopen release path
- Blocker:
  - Wikimedia file host repeatedly returned `429 Too Many Requests` during source download attempts, leaving no preserved original source file in the repo.
  - Per task requirements, I am not treating a researched-but-undownloaded track as complete.
- Recommendation:
  - Retry download later from the same rights-verified source page, then trim to about `1:45-2:00` for the oath reveal if the route is implemented.

## Rejected or not selected

- `music/zombies_defeat.ogg`
  - Rejected because the repo track list marks it `Unknown / uncredited`.
- Share-alike Wikimedia piano-midi and chant uploads
  - Rejected for this package because stronger PD / CC0 options were available for the mandatory roles.
- Test tones, drones, generated ambience, and unclear YouTube mirrors
  - Rejected by brief.

## Conversion log

Final exports were created with this workflow:

```bash
ffmpeg -y -i <source>.ogg -ss <start> -t <duration> \
  -af 'afade=t=out:st=<fade_start>:d=6' \
  -ar 44100 -c:a libvorbis -q:a 5 <final>.ogg
```

## Final handoff summary

- Ready for wiring:
  - `music/super_event_death_reveal.ogg`
  - `music/super_event_death_world_end.ogg`
  - `music/super_event_death_defeat_aftermath.ogg`
  - `music/super_event_death_world_consumed.ogg`
- Preserved original sources:
  - `music/source/010_death/death_reveal_la_cathedrale_engloutie_source.ogg`
  - `music/source/010_death/death_world_end_chopin_funeral_march_source.ogg`
  - `music/source/010_death/death_defeat_pathetique_adagio_source.ogg`
  - `music/source/010_death/death_world_consumed_hammerklavier_adagio_source.ogg`
- Not ready:
  - optional Herald oath reveal audio remains blocked pending a successful preserved-source download
