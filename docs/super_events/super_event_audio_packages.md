# Super-Event Audio Packages

## Overview

This document records source, license, conversion, and wiring data for Chaos Redux super-event audio. Super-event audio is complete only when the selected track is verified, converted to a game-ready `.ogg`, wired through both music and sound-channel definitions, and documented here.

All source files below were downloaded from their legitimate Wikimedia Commons file pages into `docs/audio_sources/super_events/`. Final in-game `.ogg` files live in `music/`. Sound-channel derivatives live in `sound/` because `sound/chaosx_sound.asset` uses `.wav` source files for `soundeffect` wrappers.

## Fallout

- Super-event id or key: `4`, `super_event.4.*`, fallout air-contamination collapse
- Track title: Overture in C minor, Op. 62, "Coriolan"
- Creator or composer: Ludwig van Beethoven
- Performer or recording source: Fulda Symphonic Orchestra, conducted by Simon Schindler
- Source URL: `https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_Overt%C3%BCre_c-moll,_op._62.ogg`
- License: EFF Open Audio License v1
- License confidence: high; Wikimedia Commons metadata and embedded Vorbis comments list the EFF Open Audio License
- Usage terms: attribution required under the listed open audio license
- Duration: source `7:54.48`, final `1:59.50`
- Attribution text if required: `Overture in C minor, Op. 62, "Coriolan" by Ludwig van Beethoven, performed by the Fulda Symphonic Orchestra conducted by Simon Schindler; EFF Open Audio License v1.`
- Downloaded source path: `docs/audio_sources/super_events/beethoven-coriolan-overture.ogg`
- Final `.ogg` path: `music/super_event_fallout.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_fallout.wav`
- Sound definition id: `chaosx_super_event_fallout_track`
- Music definitions: `chaosx_super_event_4_0_5`, `chaosx_super_event_4_1_0`, `chaosx_super_event_4_1_5`, `chaosx_super_event_4_2_0`, `chaosx_super_event_4_2_5`, `chaosx_super_event_4_3_0`
- Soundeffect definitions: `chaosx_super_event_4_sound_0_5`, `chaosx_super_event_4_sound_1_0`, `chaosx_super_event_4_sound_1_5`, `chaosx_super_event_4_sound_2_0`, `chaosx_super_event_4_sound_2_5`, `chaosx_super_event_4_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: actual orchestral crisis music with a severe opening and controlled escalation for nuclear-weather collapse
- Uncertainties: license is clearly stated but is not public domain or Creative Commons; selected because the track is openly licensed and tone-appropriate

## The Buddha Mandate

- Super-event id or key: `7`, `super_event.7.*`, The Buddha Mandate
- Track title: Buddham Saranam Gacchami - Male Voice, with Female Chorus
- Creator or composer: Hariharan
- Performer or recording source: Hariharan; Wikimedia Commons source file credited to the Internet Archive item `BuddhamSaranamGacchami`
- Source URL: `https://commons.wikimedia.org/wiki/File:Buddham_Saranam_Gacchami_-_Male_Voice,_with_Female_Chorus.oga`
- License: CC0 1.0 Universal Public Domain Dedication
- License confidence: high; Wikimedia Commons lists CC0 1.0 for the uploaded recording
- Usage terms: CC0 public-domain dedication; no attribution required
- Duration: source `6:19.09`, final `1:59.50`
- Attribution text if required: none required by CC0
- Downloaded source path: `docs/audio_sources/super_events/buddham-saranam-gacchami.oga`
- Final `.ogg` path: `music/super_event_buddha_mandate.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_buddha_mandate.wav`
- Sound definition id: `chaosx_super_event_buddha_mandate_track`
- Music definitions: `chaosx_super_event_7_0_5`, `chaosx_super_event_7_1_0`, `chaosx_super_event_7_1_5`, `chaosx_super_event_7_2_0`, `chaosx_super_event_7_2_5`, `chaosx_super_event_7_3_0`
- Soundeffect definitions: `chaosx_super_event_7_sound_0_5`, `chaosx_super_event_7_sound_1_0`, `chaosx_super_event_7_sound_1_5`, `chaosx_super_event_7_sound_2_0`, `chaosx_super_event_7_sound_2_5`, `chaosx_super_event_7_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: vocal Buddhist chant with musical accompaniment fits the Mandate as a religious-political proclamation
- Uncertainties: source track is longer than the preferred range, but the final in-game excerpt is within the required `1` to `2` minute range

## Final Silence

- Super-event id or key: `8`, `super_event.8.*`, Final Silence; `9`, `super_event.9.*`, Thermonuclear Final Silence
- Track title: Requiem Mass in D minor, K. 626: VII. Lacrimosa
- Creator or composer: Wolfgang Amadeus Mozart
- Performer or recording source: IMSLP source recording hosted on Wikimedia Commons
- Source URL: `https://commons.wikimedia.org/wiki/File:PMLP02751-S002-07-Mozart_Requiem_Mass.ogg`
- License: Creative Commons Attribution-ShareAlike 3.0
- License confidence: high; Wikimedia Commons lists CC BY-SA 3.0 for the uploaded recording
- Usage terms: attribution and CC BY-SA 3.0 share-alike terms apply
- Duration: source `3m 02.49s`, final `1m 59.50s`
- Attribution text if required: `Requiem Mass in D minor, K. 626: VII. Lacrimosa by Wolfgang Amadeus Mozart; IMSLP source recording hosted on Wikimedia Commons; CC BY-SA 3.0.`
- Downloaded source path: `docs/audio_sources/super_events/mozart-requiem-lacrimosa-imslp.ogg`
- Final `.ogg` path: `music/super_event_final_silence.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_final_silence.wav`
- Sound definition id: `chaosx_super_event_final_silence_track`
- Music definitions: `chaosx_super_event_8_0_5`, `chaosx_super_event_8_1_0`, `chaosx_super_event_8_1_5`, `chaosx_super_event_8_2_0`, `chaosx_super_event_8_2_5`, `chaosx_super_event_8_3_0`, `chaosx_super_event_9_0_5`, `chaosx_super_event_9_1_0`, `chaosx_super_event_9_1_5`, `chaosx_super_event_9_2_0`, `chaosx_super_event_9_2_5`, `chaosx_super_event_9_3_0`
- Soundeffect definitions: `chaosx_super_event_8_sound_0_5`, `chaosx_super_event_8_sound_1_0`, `chaosx_super_event_8_sound_1_5`, `chaosx_super_event_8_sound_2_0`, `chaosx_super_event_8_sound_2_5`, `chaosx_super_event_8_sound_3_0`, `chaosx_super_event_9_sound_0_5`, `chaosx_super_event_9_sound_1_0`, `chaosx_super_event_9_sound_1_5`, `chaosx_super_event_9_sound_2_0`, `chaosx_super_event_9_sound_2_5`, `chaosx_super_event_9_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: choral requiem music fits both normal and thermonuclear Final Silence as linked world-end judgments
- Uncertainties: Commons metadata does not identify the performer; the recording license and source are still documented

## The Mandala Breaks

- Super-event id or key: `10`, `super_event.10.*`, The Mandala Breaks
- Track title: Symphony No. 5 in C minor, Op. 67: I. Allegro con brio
- Creator or composer: Ludwig van Beethoven
- Performer or recording source: Fulda Symphonic Orchestra, conducted by Simon Schindler
- Source URL: `https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_Symphonie_5_c-moll_-_1._Allegro_con_brio.ogg`
- License: public domain
- License confidence: high; Wikimedia Commons lists the recording as public domain
- Usage terms: public domain; no attribution required
- Duration: source `7:16.02`, final `1:59.50`
- Attribution text if required: none required by public domain status
- Downloaded source path: `docs/audio_sources/super_events/beethoven-symphony-5-allegro.ogg`
- Final `.ogg` path: `music/super_event_mandala_breaks.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_mandala_breaks.wav`
- Sound definition id: `chaosx_super_event_mandala_breaks_track`
- Music definitions: `chaosx_super_event_10_0_5`, `chaosx_super_event_10_1_0`, `chaosx_super_event_10_1_5`, `chaosx_super_event_10_2_0`, `chaosx_super_event_10_2_5`, `chaosx_super_event_10_3_0`
- Soundeffect definitions: `chaosx_super_event_10_sound_0_5`, `chaosx_super_event_10_sound_1_0`, `chaosx_super_event_10_sound_1_5`, `chaosx_super_event_10_sound_2_0`, `chaosx_super_event_10_sound_2_5`, `chaosx_super_event_10_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: forceful orchestral music gives the broken-mandala crisis an immediate, recognizable collapse rhythm
- Uncertainties: source track is longer than the preferred range, but the final in-game excerpt is within the required `1` to `2` minute range

## Divine Sovereignty

- Super-event id or key: `11`, `super_event.11.*`, Divine Sovereignty
- Track title: Ave Maria from Gregorian Vespers
- Creator or composer: traditional Gregorian chant
- Performer or recording source: Schola Gregoriana from the Pallottine Seminary in Oltarzew, conducted by Dariusz Smolarek
- Source URL: `https://commons.wikimedia.org/wiki/File:Schola_Gregoriana-Ave_Maria.ogg`
- License: Creative Commons Attribution-ShareAlike 3.0
- License confidence: high; Wikimedia Commons lists CC BY-SA 3.0 and includes permission notes from the rights holders
- Usage terms: attribution and CC BY-SA 3.0 share-alike terms apply
- Duration: source `1:10.63`, final `1:10.63`
- Attribution text if required: `Ave Maria from Gregorian Vespers, performed by Schola Gregoriana from the Pallottine Seminary in Oltarzew, conducted by Dariusz Smolarek; CC BY-SA 3.0.`
- Downloaded source path: `docs/audio_sources/super_events/schola-gregoriana-ave-maria.ogg`
- Final `.ogg` path: `music/super_event_divine_sovereignty.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_divine_sovereignty.wav`
- Sound definition id: `chaosx_super_event_divine_sovereignty_track`
- Music definitions: `chaosx_super_event_11_0_5`, `chaosx_super_event_11_1_0`, `chaosx_super_event_11_1_5`, `chaosx_super_event_11_2_0`, `chaosx_super_event_11_2_5`, `chaosx_super_event_11_3_0`
- Soundeffect definitions: `chaosx_super_event_11_sound_0_5`, `chaosx_super_event_11_sound_1_0`, `chaosx_super_event_11_sound_1_5`, `chaosx_super_event_11_sound_2_0`, `chaosx_super_event_11_sound_2_5`, `chaosx_super_event_11_sound_3_0`
- Editing or conversion steps: encoded to Ogg Vorbis for the music-channel file and converted to WAV for the sound-channel wrapper
- Suitability: solemn sacred chant fits a doctrinal and sacred-political consolidation as actual liturgical music
- Uncertainties: none

## The Angel of Death Leaves the Camp

- Super-event id or key: `12`, `super_event.12.*`, The Angel of Death Leaves the Camp
- Track title: A Night on the Bare Mountain
- Creator or composer: Modest Mussorgsky
- Performer or recording source: Musopen source recording hosted on Wikimedia Commons
- Source URL: `https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_night_on_bald_mountain.ogg`
- License: public domain
- License confidence: high; Wikimedia Commons lists the recording as public domain with VRT permission confirmation
- Usage terms: public domain; no attribution required
- Duration: source `12:13.20`, final `1:59.50`
- Attribution text if required: none required by public domain status
- Downloaded source path: `docs/audio_sources/super_events/mussorgsky-night-on-bald-mountain.ogg`
- Final `.ogg` path: `music/super_event_angel_directorate.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_angel_directorate.wav`
- Sound definition id: `chaosx_super_event_angel_directorate_track`
- Music definitions: `chaosx_super_event_12_0_5`, `chaosx_super_event_12_1_0`, `chaosx_super_event_12_1_5`, `chaosx_super_event_12_2_0`, `chaosx_super_event_12_2_5`, `chaosx_super_event_12_3_0`
- Soundeffect definitions: `chaosx_super_event_12_sound_0_5`, `chaosx_super_event_12_sound_1_0`, `chaosx_super_event_12_sound_1_5`, `chaosx_super_event_12_sound_2_0`, `chaosx_super_event_12_sound_2_5`, `chaosx_super_event_12_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: dark orchestral music supports the camp-to-directorate escalation without relying on industrial sound design
- Uncertainties: Commons metadata does not name the performer in the main artist field; the source and public domain status are documented

## Angelic World Order

- Super-event id or key: `13`, `super_event.13.*`, `[GetMengeleCloneWorldOrderTitle]`
- Track title: Toccata and Fugue in D minor, BWV 565
- Creator or composer: Johann Sebastian Bach
- Performer or recording source: Ashtar Moira, Tamburini organ recording
- Source URL: `https://commons.wikimedia.org/wiki/File:Toccata_et_Fugue_BWV565.ogg`
- License: public domain
- License confidence: high; Wikimedia Commons lists the recording as public domain
- Usage terms: public domain; no attribution required
- Duration: source `8:33.56`, final `1:59.50`
- Attribution text if required: none required by public domain status
- Downloaded source path: `docs/audio_sources/super_events/bach-toccata-et-fugue-bwv565.ogg`
- Final `.ogg` path: `music/super_event_angelic_world_order.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_angelic_world_order.wav`
- Sound definition id: `chaosx_super_event_angelic_world_order_track`
- Music definitions: `chaosx_super_event_13_0_5`, `chaosx_super_event_13_1_0`, `chaosx_super_event_13_1_5`, `chaosx_super_event_13_2_0`, `chaosx_super_event_13_2_5`, `chaosx_super_event_13_3_0`
- Soundeffect definitions: `chaosx_super_event_13_sound_0_5`, `chaosx_super_event_13_sound_1_0`, `chaosx_super_event_13_sound_1_5`, `chaosx_super_event_13_sound_2_0`, `chaosx_super_event_13_sound_2_5`, `chaosx_super_event_13_sound_3_0`
- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: full organ music gives the clone world-order reveal a ceremonial and ominous musical identity
- Uncertainties: source track is longer than the preferred range, but the final in-game excerpt is within the required `1` to `2` minute range

## The Union Unmade

- Super-event id or key: `14`, `super_event.14.*`, The Union Unmade
- Track title: Overture in C minor, Op. 62, "Coriolan"
- Creator or composer: Ludwig van Beethoven
- Performer or recording source: Fulda Symphonic Orchestra, conducted by Simon Schindler
- Source URL: `https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_Overt%C3%BCre_c-moll,_op._62.ogg`
- License: EFF Open Audio License v1
- License confidence: high; Wikimedia Commons metadata and embedded Vorbis comments list the EFF Open Audio License
- Usage terms: attribution required under the listed open audio license
- Duration: source `7:54.48`, final `1:59.50`
- Attribution text if required: `Overture in C minor, Op. 62, "Coriolan" by Ludwig van Beethoven, performed by the Fulda Symphonic Orchestra conducted by Simon Schindler; EFF Open Audio License v1.`
- Downloaded source path: `docs/audio_sources/super_events/beethoven-coriolan-overture.ogg`
- Final `.ogg` path: `music/super_event_union_unmade.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_union_unmade.wav`
- Sound definition id: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_14_0_5`, `chaosx_super_event_14_1_0`, `chaosx_super_event_14_1_5`, `chaosx_super_event_14_2_0`, `chaosx_super_event_14_2_5`, `chaosx_super_event_14_3_0`
- Soundeffect definitions: `chaosx_super_event_14_sound_0_5`, `chaosx_super_event_14_sound_1_0`, `chaosx_super_event_14_sound_1_5`, `chaosx_super_event_14_sound_2_0`, `chaosx_super_event_14_sound_2_5`, `chaosx_super_event_14_sound_3_0`

## Soviet Collapse Optional Branch Super-Events

- Super-event id or key: `15`, `super_event.15.*`, The Black Banner Returns
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_15_0_5`, `chaosx_super_event_15_1_0`, `chaosx_super_event_15_1_5`, `chaosx_super_event_15_2_0`, `chaosx_super_event_15_2_5`, `chaosx_super_event_15_3_0`
- Soundeffect definitions: `chaosx_super_event_15_sound_0_5`, `chaosx_super_event_15_sound_1_0`, `chaosx_super_event_15_sound_1_5`, `chaosx_super_event_15_sound_2_0`, `chaosx_super_event_15_sound_2_5`, `chaosx_super_event_15_sound_3_0`

- Super-event id or key: `16`, `super_event.16.*`, The Dead Are Citizens
- Audio source package reused: Final Silence / `music/super_event_final_silence.ogg`
- Sound definition id reused: `chaosx_super_event_final_silence_track`
- Music definitions: `chaosx_super_event_16_0_5`, `chaosx_super_event_16_1_0`, `chaosx_super_event_16_1_5`, `chaosx_super_event_16_2_0`, `chaosx_super_event_16_2_5`, `chaosx_super_event_16_3_0`
- Soundeffect definitions: `chaosx_super_event_16_sound_0_5`, `chaosx_super_event_16_sound_1_0`, `chaosx_super_event_16_sound_1_5`, `chaosx_super_event_16_sound_2_0`, `chaosx_super_event_16_sound_2_5`, `chaosx_super_event_16_sound_3_0`

- Super-event id or key: `17`, `super_event.17.*`, The World as One Factory
- Audio source package reused: Angelic World Order / `music/super_event_angelic_world_order.ogg`
- Sound definition id reused: `chaosx_super_event_angelic_world_order_track`
- Music definitions: `chaosx_super_event_17_0_5`, `chaosx_super_event_17_1_0`, `chaosx_super_event_17_1_5`, `chaosx_super_event_17_2_0`, `chaosx_super_event_17_2_5`, `chaosx_super_event_17_3_0`
- Soundeffect definitions: `chaosx_super_event_17_sound_0_5`, `chaosx_super_event_17_sound_1_0`, `chaosx_super_event_17_sound_1_5`, `chaosx_super_event_17_sound_2_0`, `chaosx_super_event_17_sound_2_5`, `chaosx_super_event_17_sound_3_0`

- Super-event id or key: `18`, `super_event.18.*`, Every Port a Council
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_18_0_5`, `chaosx_super_event_18_1_0`, `chaosx_super_event_18_1_5`, `chaosx_super_event_18_2_0`, `chaosx_super_event_18_2_5`, `chaosx_super_event_18_3_0`
- Soundeffect definitions: `chaosx_super_event_18_sound_0_5`, `chaosx_super_event_18_sound_1_0`, `chaosx_super_event_18_sound_1_5`, `chaosx_super_event_18_sound_2_0`, `chaosx_super_event_18_sound_2_5`, `chaosx_super_event_18_sound_3_0`

- Super-event id or key: `19`, `super_event.19.*`, A Map Larger than the Union
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_19_0_5`, `chaosx_super_event_19_1_0`, `chaosx_super_event_19_1_5`, `chaosx_super_event_19_2_0`, `chaosx_super_event_19_2_5`, `chaosx_super_event_19_3_0`
- Soundeffect definitions: `chaosx_super_event_19_sound_0_5`, `chaosx_super_event_19_sound_1_0`, `chaosx_super_event_19_sound_1_5`, `chaosx_super_event_19_sound_2_0`, `chaosx_super_event_19_sound_2_5`, `chaosx_super_event_19_sound_3_0`
- Suitability: the controlled pressure and political tragedy of the same orchestral package fit the Ukraine route as a cold statecraft escalation linked to the wider Soviet-collapse crisis.

- Super-event id or key: `20`, `super_event.20.*`, The Steppe Beyond History
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_20_0_5`, `chaosx_super_event_20_1_0`, `chaosx_super_event_20_1_5`, `chaosx_super_event_20_2_0`, `chaosx_super_event_20_2_5`, `chaosx_super_event_20_3_0`
- Soundeffect definitions: `chaosx_super_event_20_sound_0_5`, `chaosx_super_event_20_sound_1_0`, `chaosx_super_event_20_sound_1_5`, `chaosx_super_event_20_sound_2_0`, `chaosx_super_event_20_sound_2_5`, `chaosx_super_event_20_sound_3_0`
- Suitability: the same orchestral pressure fits the Kazakhstan steppe route as a large political horizon opening from the Soviet crisis.

- Super-event id or key: `21`, `super_event.21.*`, The Corridors Decide
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_21_0_5`, `chaosx_super_event_21_1_0`, `chaosx_super_event_21_1_5`, `chaosx_super_event_21_2_0`, `chaosx_super_event_21_2_5`, `chaosx_super_event_21_3_0`
- Soundeffect definitions: `chaosx_super_event_21_sound_0_5`, `chaosx_super_event_21_sound_1_0`, `chaosx_super_event_21_sound_1_5`, `chaosx_super_event_21_sound_2_0`, `chaosx_super_event_21_sound_2_5`, `chaosx_super_event_21_sound_3_0`
- Suitability: the controlled tempo and political crisis tone fit Belarus turning rail access, border passage, and corridor administration into sovereign leverage.

- Super-event id or key: `22`, `super_event.22.*`, The Bread State
- Audio source package reused: Final Silence / `music/super_event_final_silence.ogg`
- Sound definition id reused: `chaosx_super_event_final_silence_track`
- Music definitions: `chaosx_super_event_22_0_5`, `chaosx_super_event_22_1_0`, `chaosx_super_event_22_1_5`, `chaosx_super_event_22_2_0`, `chaosx_super_event_22_2_5`, `chaosx_super_event_22_3_0`
- Soundeffect definitions: `chaosx_super_event_22_sound_0_5`, `chaosx_super_event_22_sound_1_0`, `chaosx_super_event_22_sound_1_5`, `chaosx_super_event_22_sound_2_0`, `chaosx_super_event_22_sound_2_5`, `chaosx_super_event_22_sound_3_0`
- Suitability: the sparse Requiem package fits Ukraine's ration-state route as a grim political transformation rather than a battlefield victory.

- Super-event id or key: `23`, `super_event.23.*`, The League of Equal Republics
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_23_0_5`, `chaosx_super_event_23_1_0`, `chaosx_super_event_23_1_5`, `chaosx_super_event_23_2_0`, `chaosx_super_event_23_2_5`, `chaosx_super_event_23_3_0`
- Soundeffect definitions: `chaosx_super_event_23_sound_0_5`, `chaosx_super_event_23_sound_1_0`, `chaosx_super_event_23_sound_1_5`, `chaosx_super_event_23_sound_2_0`, `chaosx_super_event_23_sound_2_5`, `chaosx_super_event_23_sound_3_0`
- Suitability: the restrained orchestral crisis package fits a constitutional order forming from Soviet collapse without making the League route sound like simple victory.

- Super-event id or key: `24`, `super_event.24.*`, The Steppe Federation
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_24_0_5`, `chaosx_super_event_24_1_0`, `chaosx_super_event_24_1_5`, `chaosx_super_event_24_2_0`, `chaosx_super_event_24_2_5`, `chaosx_super_event_24_3_0`
- Soundeffect definitions: `chaosx_super_event_24_sound_0_5`, `chaosx_super_event_24_sound_1_0`, `chaosx_super_event_24_sound_1_5`, `chaosx_super_event_24_sound_2_0`, `chaosx_super_event_24_sound_2_5`, `chaosx_super_event_24_sound_3_0`
- Suitability: the restrained orchestral crisis package fits a continental federation built from rail access, garrison politics, and uneasy patron pressure.

- Super-event id or key: `25`, `super_event.25.*`, The Baltic Restoration Pact
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_25_0_5`, `chaosx_super_event_25_1_0`, `chaosx_super_event_25_1_5`, `chaosx_super_event_25_2_0`, `chaosx_super_event_25_2_5`, `chaosx_super_event_25_3_0`
- Soundeffect definitions: `chaosx_super_event_25_sound_0_5`, `chaosx_super_event_25_sound_1_0`, `chaosx_super_event_25_sound_1_5`, `chaosx_super_event_25_sound_2_0`, `chaosx_super_event_25_sound_2_5`, `chaosx_super_event_25_sound_3_0`
- Suitability: the restrained orchestral crisis package fits Baltic restoration politics, defensive legal continuity, and coast-watch pact formation.

- Super-event id or key: `26`, `super_event.26.*`, The Caucasus Defense Compact
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_26_0_5`, `chaosx_super_event_26_1_0`, `chaosx_super_event_26_1_5`, `chaosx_super_event_26_2_0`, `chaosx_super_event_26_2_5`, `chaosx_super_event_26_3_0`
- Soundeffect definitions: `chaosx_super_event_26_sound_0_5`, `chaosx_super_event_26_sound_1_0`, `chaosx_super_event_26_sound_1_5`, `chaosx_super_event_26_sound_2_0`, `chaosx_super_event_26_sound_2_5`, `chaosx_super_event_26_sound_3_0`
- Suitability: the restrained orchestral crisis package fits mountain compact politics, defended passes, oil-road bargaining, and patron pressure around the southern collapse frontier.

- Super-event id or key: `27`, `super_event.27.*`, The Eastern Buffer Coalition
- Audio source package reused: Beethoven Coriolan / `music/super_event_union_unmade.ogg`
- Sound definition id reused: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_27_0_5`, `chaosx_super_event_27_1_0`, `chaosx_super_event_27_1_5`, `chaosx_super_event_27_2_0`, `chaosx_super_event_27_2_5`, `chaosx_super_event_27_3_0`
- Soundeffect definitions: `chaosx_super_event_27_sound_0_5`, `chaosx_super_event_27_sound_1_0`, `chaosx_super_event_27_sound_1_5`, `chaosx_super_event_27_sound_2_0`, `chaosx_super_event_27_sound_2_5`, `chaosx_super_event_27_sound_3_0`
- Suitability: the restrained orchestral crisis package fits a defensive western line built from border desks, rail junctions, foreign missions, and anti-reconquest pressure.

- Editing or conversion steps: trimmed to the first `119.5` seconds, faded out over the last `5` seconds, encoded to Ogg Vorbis, and converted to WAV for the sound-channel wrapper
- Suitability: actual orchestral crisis music with restrained martial pressure and political tragedy for a union authority collapse
- Uncertainties: the same Coriolan source recording is also used for the Fallout super-event; Soviet Collapse slots `15`, `18`, `19`, `20`, `21`, `23`, `24`, `25`, `26`, and `27` intentionally share the slot `14` final file while keeping separate super-event ids and playback definitions.
