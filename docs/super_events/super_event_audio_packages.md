# Super-Event Audio Packages

This file records sourced super-event audio provenance and the current music runtime mapping. Every super-event cue plays through its OGG under `music/`; the settings-aware helper selects the music key for the playback audio ID, and the music asset files and `music/chaosx_super_event_music.txt` provide runtime playback and station registration. The game never loads a super-event WAV, so `sound/` holds no super-event recording or `soundeffect`; the original WAV of each cue is kept byte for byte in the LFS archive at `Documents/chaos_redux_lfs_archive/` under the same `sound/` path. The canonical catalogue lists the runtime OGG and its original WAV. Fifty-five current tracks use matching historical OGG files restored from commit `99f0b18dd^` with SHA-256 verified local Git LFS objects; sixteen tracks without a matching historical OGG were encoded from the final WAV with `ffmpeg -c:a libvorbis -q:a 6`. Every current audio ID has the six historical volume aliases plus a `_0` music key at zero volume. The Fallout blackout uses the same music route with its dedicated `fallout_world_end_blackout_0` mute key.
## Current OGG Conversion Details

16 current cues had no matching historical OGG path and were encoded from the listed final WAVs. Each encode used `ffmpeg -hide_banner -loglevel error -y -i <source WAV> -vn -c:a libvorbis -q:a 6 <runtime OGG>`. The command changes only the music copy; the archived WAV remains byte-identical to its source. The other 55 current event tracks use historical OGG bytes restored and SHA-256 verified from `99f0b18dd^`.

| Playback audio ID | Original WAV (LFS archive) | Runtime OGG | OGG duration |
|---|---|---|---:|
| `23` | `Documents/chaos_redux_lfs_archive/sound/006_independence_wave/super_event_23_enola_foam_march_110s.wav` | `music/006_independence_wave/super_event_23_enola_foam_march_110s.ogg` | 110.000s |
| `24` | `Documents/chaos_redux_lfs_archive/sound/006_independence_wave/super_event_24_every_border_a_casus_belli.wav` | `music/006_independence_wave/super_event_24_every_border_a_casus_belli.ogg` | 109.993s |
| `58` | `Documents/chaos_redux_lfs_archive/sound/012_africa/super_event_58_africa_is_one.wav` | `music/012_africa/super_event_58_africa_is_one.ogg` | 110.000s |
| `61` | `Documents/chaos_redux_lfs_archive/sound/012_africa/super_event_61_the_world.wav` | `music/012_africa/super_event_61_the_world.ogg` | 116.000s |
| `103` | `Documents/chaos_redux_lfs_archive/sound/020_black_plague/super_event_087_rat_king_defeat_aftermath.wav` | `music/020_black_plague/super_event_087_rat_king_defeat_aftermath.ogg` | 115.000s |
| `106` | `Documents/chaos_redux_lfs_archive/sound/035_great_depression/super_event_106_second_great_depression.wav` | `music/035_great_depression/super_event_106_second_great_depression.ogg` | 115.000s |
| `108` | `Documents/chaos_redux_lfs_archive/sound/023_sov_nuclear_bombs/super_event_108_first_major_exchange.wav` | `music/023_sov_nuclear_bombs/super_event_108_first_major_exchange.ogg` | 115.000s |
| `109` | `Documents/chaos_redux_lfs_archive/sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.wav` | `music/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.ogg` | 115.000s |
| `114` | `Documents/chaos_redux_lfs_archive/sound/031_random_terror/super_event_104_false_revelation_reveal.wav` | `music/031_random_terror/super_event_104_false_revelation_reveal.ogg` | 110.000s |
| `115` | `Documents/chaos_redux_lfs_archive/sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav` | `music/031_random_terror/super_event_105_false_revelation_defeat_aftermath.ogg` | 110.000s |
| `117` | `Documents/chaos_redux_lfs_archive/sound/033_acid_rain/super_event_033_acid_rain_formation.wav` | `music/033_acid_rain/super_event_033_acid_rain_formation.ogg` | 80.000s |
| `118` | `Documents/chaos_redux_lfs_archive/sound/012_africa/super_event_118_gods_of_africa.wav` | `music/012_africa/super_event_118_gods_of_africa.ogg` | 104.068s |
| `111` | `Documents/chaos_redux_lfs_archive/sound/039_murder_mystery/super_event_111_assassin_state_reveal.wav` | `music/039_murder_mystery/super_event_111_assassin_state_reveal.ogg` | 110.000s |
| `112` | `Documents/chaos_redux_lfs_archive/sound/039_murder_mystery/super_event_112_world_of_anarchy_activation.wav` | `music/039_murder_mystery/super_event_112_world_of_anarchy_activation.ogg` | 110.000s |
| `113` | `Documents/chaos_redux_lfs_archive/sound/039_murder_mystery/super_event_113_brotherhood_defeat_aftermath.wav` | `music/039_murder_mystery/super_event_113_brotherhood_defeat_aftermath.ogg` | 110.000s |
| `116` | `Documents/chaos_redux_lfs_archive/sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav` | `music/028_asteroid_incoming/super_event_028_asteroid_impact.ogg` | 115.000s |

## Zombie Outbreak

### Undead?

- Super-event ID: `1`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/002_zombie_outbreak/super_event_1_zombies.wav`
- Runtime music OGG: `music/002_zombie_outbreak/super_event_1_zombies.ogg`
- Music definition keys: `chaosx_super_event_1_0`, `chaosx_super_event_1_0_5`, `chaosx_super_event_1_1_0`, `chaosx_super_event_1_1_5`, `chaosx_super_event_1_2_0`, `chaosx_super_event_1_2_5`, and `chaosx_super_event_1_3_0`.
- Source title: `Scheherazade, Op. 35: I. The Sea and Sinbad's Ship`.
- Composer / creator: Nikolai Rimsky-Korsakov.
- Performer / recording: San Francisco Symphony conducted by Pierre Monteux, with Naoum Blinder as concertmaster.
- Source URLs: [Internet Archive recording item](https://archive.org/details/Sheherazade); [Wikimedia Commons file and CC0 record](https://commons.wikimedia.org/wiki/File:Rimsky-Korsakov._Scheherazade,_Symphonic_Suite,_Op._35_-_01_The_Sea_And_Sinbads_Ship.ogg?oldid=628862047).
- Source file: `docs/assets/002_zombie_outbreak/source_audio/rimsky_korsakov_scheherazade_i_archive_original.mp3` (19,953,265 bytes; SHA-256 `437AF712F594E92BB1ABAF863A8709C66894E93611A17C5C13B02EE1B4C71B1B`).
- License: the 1888 composition is public domain (Rimsky-Korsakov died in 1908); Internet Archive marks the 1942 recording source Public Domain, and the Commons file page dedicates the recording file under CC0 1.0. License confidence: high for this archived recording. Attribution is not required; courtesy credit is recommended.
- Duration: 498.817875 seconds original source; 105.000 seconds final excerpt.
- Conversion notes: the opening `00:00.000-01:45.000` is rendered to stereo 44.1 kHz PCM16 with entry and exit fades; the retained notes do not specify fade lengths. Decoded-PCM comparison aligns at source offset `0.000 s` with normalized correlation `0.998199` at runtime `00:40` and `0.997459` at `01:15`. Runtime SHA-256: `753778951E4AB1FC6F72AE54A00C5BE8BDC1C8CCA527DE9E9F9BA0C1CF3ACEAC`.

### The Alliance of Man

- Super-event ID: `2`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/002_zombie_outbreak/super_event_2_alliance_of_man.wav`
- Runtime music OGG: `music/002_zombie_outbreak/super_event_2_alliance_of_man.ogg`
- Music definition keys: `chaosx_super_event_2_0`, `chaosx_super_event_2_0_5`, `chaosx_super_event_2_1_0`, `chaosx_super_event_2_1_5`, `chaosx_super_event_2_2_0`, `chaosx_super_event_2_2_5`, and `chaosx_super_event_2_3_0`.
- Source title: `Battle Hymn of the Republic`
- Composer / creator: John William Steffe / Julia Ward Howe, arranged by Eric Richards.
- Performer / recording: United States Air Force Band Airmen of Note, Colonel Dennis M. Layendecker, Commander and Music Director.
- Source URL: <https://commons.wikimedia.org/wiki/File:Battle_Hymn_of_the_Republic_(USAFB).ogg>
- Source file: `docs/super_events/source_audio/battle_hymn_of_the_republic_usafb.ogg`
- License: public domain U.S. federal government recording; underlying composition public domain.
- Duration: 1:30 final excerpt.
- Conversion notes: sourced replacement for the prior generated cue; the final WAV is rendered from the preserved licensed recording.

### Zombie Apocalypse

- Super-event ID: `3`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/002_zombie_outbreak/super_event_3_zombie_apocalypse.wav`
- Runtime music OGG: `music/002_zombie_outbreak/super_event_3_zombie_apocalypse.ogg`
- Music definition keys: `chaosx_super_event_3_0`, `chaosx_super_event_3_0_5`, `chaosx_super_event_3_1_0`, `chaosx_super_event_3_1_5`, `chaosx_super_event_3_2_0`, `chaosx_super_event_3_2_5`, and `chaosx_super_event_3_3_0`.
- Source title: `Dies Irae`
- Composer / creator: traditional Gregorian chant; recording by Membeth.
- Performer / recording: Membeth.
- Source URL: <https://commons.wikimedia.org/wiki/File:Dies.irae.ogg>
- Source file: `docs/super_events/source_audio/dies_irae_gregorian_chant.ogg`
- License: public domain dedication by the recording author.
- Duration: 1:35 final excerpt.
- Conversion notes: sourced replacement for the prior generated cue; the final WAV is rendered from the preserved licensed recording.

### The Dead Are Buried

- Super-event ID: `5`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/002_zombie_outbreak/super_event_5_zombies_defeat.wav`
- Runtime music OGG: `music/002_zombie_outbreak/super_event_5_zombies_defeat.ogg`
- Music definition keys: `chaosx_super_event_5_0`, `chaosx_super_event_5_0_5`, `chaosx_super_event_5_1_0`, `chaosx_super_event_5_1_5`, `chaosx_super_event_5_2_0`, `chaosx_super_event_5_2_5`, and `chaosx_super_event_5_3_0`.
- Source title: `Music for the Royal Fireworks, HWV 351: IV. La Réjouissance`.
- Composer / creator: George Frideric Handel.
- Performer / recording: St Matthew Concert Choir, conducted by Paul Ayres.
- Source URLs: [Internet Archive recording item](https://archive.org/details/HandelMusicForTheRoyalFireworks2011) and [original `09TheRejoicing.mp3`](https://archive.org/download/HandelMusicForTheRoyalFireworks2011/09TheRejoicing.mp3); [Wikimedia Commons file and CC0 record](https://commons.wikimedia.org/wiki/File:Paul_Ayres_-_Handel%27s_Music_for_the_Royal_Fireworks,_HWV_351_-_IV._La_R%C3%A9jouissance.ogg?oldid=794973790).
- Source file: `docs/assets/002_zombie_outbreak/source_audio/handel_royal_fireworks_rejoicing_archive_original.mp3` (3,216,864 bytes; SHA-256 `80E353C2A2AD1B1850B2D291444EC55A66EB0F306B993EED2F0FCC270F9184AA`).
- License: Handel's composition is public domain; the Internet Archive item and Commons file page identify the Paul Ayres recording as CC0 1.0. License confidence: high for this archived recording. Attribution is not required; courtesy credit is recommended.
- Duration: 98.742857 seconds original source; 98.633741 seconds final cue.
- Conversion notes: the runtime aligns to source offset `0.000 s`, retaining the opening `00:00.000-01:38.634` with fades; the retained notes do not specify fade lengths. Decoded-PCM comparison has normalized correlation `0.997126` at runtime `00:08`, `0.996889` at `00:35`, and `0.997235` at `01:10`. Runtime SHA-256: `20FB149DF2AEE1DE553E3080CE1B2070CEC080AC53F285EBF67DAEF56D662389`.

### Wendigo

- Super-event ID: `6`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/002_zombie_outbreak/super_event_6_wendigo.wav`
- Runtime music OGG: `music/002_zombie_outbreak/super_event_6_wendigo.ogg`
- Music definition keys: `chaosx_super_event_6_0`, `chaosx_super_event_6_0_5`, `chaosx_super_event_6_1_0`, `chaosx_super_event_6_1_5`, `chaosx_super_event_6_2_0`, `chaosx_super_event_6_2_5`, and `chaosx_super_event_6_3_0`.
- Source title: `Má vlast: Vltava (The Moldau)`.
- Composer / creator: Bedřich Smetana.
- Performer / recording: Musopen Symphony Orchestra.
- Source URL: <https://commons.wikimedia.org/wiki/File:Smetana,_M%C3%A1_vlast_-_Vltava_-_The_Moldau.ogg>
- Source file: `docs/assets/002_zombie_outbreak/source_audio/duplicate_audio_replacements_2026-09-01/source/smetana_vltava_moldau.ogg`.
- License: public-domain composition and CC0 1.0 worldwide recording dedication.
- Duration: 1:45 final excerpt.
- Conversion notes: the rapids passage from 08:15 through 10:00 is rendered to stereo 44.1 kHz PCM16 with fades. Runtime SHA-256: `DC01CD34CF253C3D76FB275389247CD830B161988A68077908AD1A3153A7DDA5`.

## Fallout World End

### Blackout Transition

- Presentation owner: dedicated `fallout_world_end` system.
- Playback effect: `fallout_play_blackout_audio`.
- Runtime music file: `music/fallout_world_end/fallout_world_end_blackout.ogg`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/fallout_world_end/fallout_world_end_blackout.wav`.
- Music definition keys: `fallout_world_end_blackout_0`, `fallout_world_end_blackout_0_5`, `fallout_world_end_blackout_1_0`, `fallout_world_end_blackout_1_5`, `fallout_world_end_blackout_2_0`, `fallout_world_end_blackout_2_5`, and `fallout_world_end_blackout_3_0`.
- Source title: `Eyes In The Void`.
- Composer and recording owner: Scott Buckley.
- Official source page: <https://www.scottbuckley.com.au/library/eyes-in-the-void/>.
- License: Creative Commons Attribution 4.0 International.
- Duration: exactly 120 seconds.
- Conversion notes: Chaos Redux excerpted `02:22.370` through `04:22.370`, applied fades and 12 dB attenuation, then produced 44.1 kHz WAV output.
- Preference integration: the playback effect honors the shared super-event volume setting while retaining Fallout-owned wrappers and assets.
- Full source, attribution, hash, processing, and distribution ledger: `docs/assets/fallout_world_end/audio_manifest.md`.

## Holy Realm

### The Buddha Mandate

- Super-event ID: `7`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_7_buddha_mandate.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_7_buddha_mandate.ogg`
- Music definition keys: `chaosx_super_event_7_0`, `chaosx_super_event_7_0_5`, `chaosx_super_event_7_1_0`, `chaosx_super_event_7_1_5`, `chaosx_super_event_7_2_0`, `chaosx_super_event_7_2_5`, and `chaosx_super_event_7_3_0`.
- Source title: `Buddham Saranam Gacchami - Male Voice, with Female Chorus`
- Composer / creator: Hariharan.
- Performer / recording: Hariharan; Wikimedia Commons source file credited to the Internet Archive item `BuddhamSaranamGacchami`.
- Source URL: <https://commons.wikimedia.org/wiki/File:Buddham_Saranam_Gacchami_-_Male_Voice,_with_Female_Chorus.oga>
- License: CC0 1.0 Universal Public Domain Dedication.
- Duration: 2:30 processed cue.
- Conversion notes: first `150` seconds retained with fade-in and fade-out from the researched Holy Realm Buddhahood audio package.

### Powers of the Awakened

- Super-event ID: `61`
- Audio ID: `31`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_31_powers_of_the_awakened.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_31_powers_of_the_awakened.ogg`
- Music definition keys: `chaosx_super_event_31_0`, `chaosx_super_event_31_0_5`, `chaosx_super_event_31_1_0`, `chaosx_super_event_31_1_5`, `chaosx_super_event_31_2_0`, `chaosx_super_event_31_2_5`, and `chaosx_super_event_31_3_0`.
- Source title: `Bhikkhu Pāṭimokkha Pali`
- Composer / creator: traditional Pali monastic chant; recording uploaded by Wikimedia Commons account `Tevaprapas` / `พระวินัยธร`.
- Performer / recording: Buddhist monks chanting on Uposatha Day at Wat Khung Taphao, Uttaradit Province, Thailand.
- Source URL: <https://commons.wikimedia.org/wiki/File:Bhikkhu_P%C4%81%E1%B9%ADimokkha_Pali.ogg>
- License: Creative Commons Attribution 3.0 Unported.
- Duration: 2:15 processed cue.
- Conversion notes: starts at `01:00`, retains `135` seconds, and adds fade-in and fade-out. Attribution, license link, and modification notice are required.

### Final Silence

- Super-event ID: `8`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_8_final_silence.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_8_final_silence.ogg`
- Music definition keys: `chaosx_super_event_8_0`, `chaosx_super_event_8_0_5`, `chaosx_super_event_8_1_0`, `chaosx_super_event_8_1_5`, `chaosx_super_event_8_2_0`, `chaosx_super_event_8_2_5`, and `chaosx_super_event_8_3_0`.
- Source title: `Bore Xinjing (Heart Sutra) in Mandarin recited by a Chinese Buddhist layperson 2`
- Composer / creator: Heart Sutra text is ancient scripture; recording by Nyarlathotep1001.
- Performer / recording: Chinese Buddhist layperson recitation per Wikimedia Commons source page.
- Source URL: <https://commons.wikimedia.org/wiki/File:Bore_Xinjing_%E8%88%AC%E8%8B%A5%E5%BF%83%E7%BB%8F_(Heart_Sutra)_in_Mandarin_recited_by_a_Chinese_Buddhist_layperson_2.ogg>
- License: CC0 1.0 Universal Public Domain Dedication.
- Duration: 2:08.661 processed cue.
- Conversion notes: full source retained with fade-in and fade-out. No attribution is required by CC0; courtesy credit is recommended.

### Thermonuclear Final Silence

- Super-event ID: `9`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_9_final_silence_thermonuclear.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_9_final_silence_thermonuclear.ogg`
- Music definition keys: `chaosx_super_event_9_0`, `chaosx_super_event_9_0_5`, `chaosx_super_event_9_1_0`, `chaosx_super_event_9_1_5`, `chaosx_super_event_9_2_0`, `chaosx_super_event_9_2_5`, and `chaosx_super_event_9_3_0`.
- Source title: `Chanting at Lingyin Temple, Hangzhou`.
- Composer / creator: traditional Buddhist chant.
- Performer / recording: Louise Brown field recording.
- Source URL: <https://commons.wikimedia.org/wiki/File:Chanting_at_Lingyin_Temple,_Hangzhou.ogg>
- Source file: `docs/assets/003_holy_realm/source_audio/duplicate_audio_replacements_2026-09-01/source/chanting_lingyin_temple_hangzhou.ogg`.
- License: Creative Commons Attribution-ShareAlike 3.0 Unported.
- Duration: 1:03.188005 final cue.
- Notes: the near-complete source is rendered to stereo 44.1 kHz PCM16 with fades. Attribution, a modification notice, and compatible ShareAlike terms are required. Runtime SHA-256: `26BAA65E2095BC3A96DE73CF7B3B406AC42730FF5E06B9CC52CE7C7222A19DD7`.

### The Mandala Breaks

- Super-event ID: `10`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_10_mandala_breaks.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_10_mandala_breaks.ogg`
- Music definition keys: `chaosx_super_event_10_0`, `chaosx_super_event_10_0_5`, `chaosx_super_event_10_1_0`, `chaosx_super_event_10_1_5`, `chaosx_super_event_10_2_0`, `chaosx_super_event_10_2_5`, and `chaosx_super_event_10_3_0`.
- Source title: `Symphony No. 5 in C minor, Op. 67: I. Allegro con brio`
- Composer / creator: Ludwig van Beethoven.
- Performer / recording: Fulda Symphonic Orchestra, conducted by Simon Schindler.
- Source URL: <https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_Symphonie_5_c-moll_-_1._Allegro_con_brio.ogg>
- License: public domain.
- Duration: 1:59.5 restored cue.
- Conversion notes: restored the pre-placeholder track while retaining the stable file paths.
### Divine Sovereignty

- Super-event ID: `11`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_11_divine_sovereignty.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_11_divine_sovereignty.ogg`
- Music definition keys: `chaosx_super_event_11_0`, `chaosx_super_event_11_0_5`, `chaosx_super_event_11_1_0`, `chaosx_super_event_11_1_5`, `chaosx_super_event_11_2_0`, `chaosx_super_event_11_2_5`, and `chaosx_super_event_11_3_0`.
- Source title: `Ave Maria from Gregorian Vespers`
- Composer / creator: Traditional Gregorian chant.
- Performer / recording: Schola Gregoriana from the Pallottine Seminary in Oltarzew, conducted by Dariusz Smolarek.
- Source URL: <https://commons.wikimedia.org/wiki/File:Schola_Gregoriana-Ave_Maria.ogg>
- License: Creative Commons Attribution-ShareAlike 3.0.
- Duration: 1:10.627 restored cue.
- Conversion notes: restored the pre-placeholder track while retaining the stable file paths.

### Mandala of Nations

- Super-event ID: `51`
- Audio ID: `28`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_28_mandala_of_nations.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_28_mandala_of_nations.ogg`
- Music definition keys: `chaosx_super_event_28_0`, `chaosx_super_event_28_0_5`, `chaosx_super_event_28_1_0`, `chaosx_super_event_28_1_5`, `chaosx_super_event_28_2_0`, `chaosx_super_event_28_2_5`, and `chaosx_super_event_28_3_0`.
- Source title: `Shurangama Dharani Chant`, 120-150 second excerpt.
- Composer / creator: Ven. Chan Master Hsuan Hua recording excerpt.
- Performer / recording: Ven. Chan Master Hsuan Hua.
- Source URL: <https://commons.wikimedia.org/wiki/File:Buddhism_Shurangama_dharani_chant_120_150.ogg>
- Source file: `docs/super_events/source_audio/shurangama_dharani_chant_120_150.ogg`
- License: `CC BY-SA 3.0`.
- Duration: 30.071 seconds.
- Notes: sourced replacement for the prior generated cue. Attribution required: Ven. Chan Master Hsuan Hua, `Shurangama Dharani Chant` excerpt, via Wikimedia Commons / Internet Archive, licensed CC BY-SA 3.0.

## Fury

### Fury Becomes a State

- Super-event ID: `59`
- Audio ID: `29`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/007_fury/super_event_29_fury_becomes_a_state.wav`
- Runtime music OGG: `music/007_fury/super_event_29_fury_becomes_a_state.ogg`
- Music definition keys: `chaosx_super_event_29_0`, `chaosx_super_event_29_0_5`, `chaosx_super_event_29_1_0`, `chaosx_super_event_29_1_5`, `chaosx_super_event_29_2_0`, `chaosx_super_event_29_2_5`, and `chaosx_super_event_29_3_0`.
- Source title: `Symphony No. 9 in E minor "From the New World", Op. 95: IV. Allegro con fuoco`
- Composer / creator: Antonín Dvořák.
- Performer / recording: Musopen source recording hosted on Wikimedia Commons.
- Source URL: <https://commons.wikimedia.org/wiki/File:Antonin_Dvorak_-_symphony_no._9_in_e_minor_%27from_the_new_world%27,_op._95_-_iv._allegro_con_fuoco.ogg>
- Source file: `docs/super_events/source_audio/dvorak_new_world_iv_musopen_original.ogg`
- License: Wikimedia Commons lists the file as public-domain music from Musopen with attribution requested to Musopen, and states that redistribution, derivative work, commercial use, and all other use are permitted with proper attribution.
- Duration: 2:30 final cue.
- Conversion notes: first two and a half minutes rendered from the source OGG with short fade-in/fade-out and loudness normalization; the WAV is rendered from the preserved source.

### The World in Fury

- Super-event ID: `60`
- Audio ID: `30`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/007_fury/super_event_30_world_in_fury.wav`
- Runtime music OGG: `music/007_fury/super_event_30_world_in_fury.ogg`
- Music definition keys: `chaosx_super_event_30_0`, `chaosx_super_event_30_0_5`, `chaosx_super_event_30_1_0`, `chaosx_super_event_30_1_5`, `chaosx_super_event_30_2_0`, `chaosx_super_event_30_2_5`, and `chaosx_super_event_30_3_0`.
- Source title: `The Planets, Op. 32: I. Mars, the Bringer of War`
- Composer / creator: Gustav Holst.
- Performer / recording: Skidmore College Orchestra recording from Musopen, hosted on Wikimedia Commons.
- Source URL: <https://commons.wikimedia.org/wiki/File:Gustav_Holst_-_the_planets,_op._32_-_i._mars,_the_bringer_of_war.ogg>
- Source file: `docs/super_events/source_audio/holst_mars_musopen_original.ogg`
- License: Wikimedia Commons lists the file as public-domain music from Musopen with attribution requested to Musopen, and states that redistribution, derivative work, commercial use, and all other use are permitted with proper attribution.
- Duration: 3:00 final cue.
- Conversion notes: first three minutes rendered from the source OGG with short fade-in/fade-out and loudness normalization; the WAV is rendered from the preserved source.

## Mengele

### The Angel of Death Leaves the Camp

- Super-event ID: `12`
- Audio ID: `45`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.wav`
- Runtime music OGG: `music/system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.ogg`
- Music definition keys: `chaosx_super_event_45_0`, `chaosx_super_event_45_0_5`, `chaosx_super_event_45_1_0`, `chaosx_super_event_45_1_5`, `chaosx_super_event_45_2_0`, `chaosx_super_event_45_2_5`, and `chaosx_super_event_45_3_0`.
- Source title: `Passacaglia and Fugue in C minor, BWV 582`
- Composer / creator: Johann Sebastian Bach.
- Performer / recording: Awadagin Pratt, White House Evening of Classical Music, 2009.
- Source URL: <https://commons.wikimedia.org/wiki/File:20091104_Awadagin_Pratt_-_Bach%27s_Passacaglia_and_Fugue_in_C_minor,_BWV_582.ogg>
- License: public-domain composition; CC BY 3.0 performance/source file.
- Duration: 1:54 final excerpt.
- Conversion notes: opening silence removed, 48 kHz source resampled to 44.1 kHz, normalized, and faded. The cue is registered at all six settings-aware levels in both playback modes.

### Angelic World Order

- Super-event ID: `13`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/003_holy_realm/super_event_13_angelic_world_order.wav`
- Runtime music OGG: `music/003_holy_realm/super_event_13_angelic_world_order.ogg`
- Music definition keys: `chaosx_super_event_13_0`, `chaosx_super_event_13_0_5`, `chaosx_super_event_13_1_0`, `chaosx_super_event_13_1_5`, `chaosx_super_event_13_2_0`, `chaosx_super_event_13_2_5`, and `chaosx_super_event_13_3_0`.
- Source title: `Toccata and Fugue in D minor, BWV 565`
- Composer / creator: Johann Sebastian Bach.
- Performer / recording: Ashtar Moira, Tamburini organ recording.
- Source URL: <https://commons.wikimedia.org/wiki/File:Toccata_et_Fugue_BWV565.ogg>
- License: public domain.
- Duration: 1:59.5 restored cue.
- Conversion notes: restored the pre-placeholder track while retaining the stable file paths.

## Secret Alliance

### The Pact Unmasked

- Super-event ID: `73`
- Audio ID: `43`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/011_secret_alliance/super_event_43_public_reveal.wav`
- Runtime music OGG: `music/011_secret_alliance/super_event_43_public_reveal.ogg`
- Music definition keys: `chaosx_super_event_43_0`, `chaosx_super_event_43_0_5`, `chaosx_super_event_43_1_0`, `chaosx_super_event_43_1_5`, `chaosx_super_event_43_2_0`, `chaosx_super_event_43_2_5`, and `chaosx_super_event_43_3_0`.
- Source title: `Revelation`
- Composer / creator: William Paris Chambers, composed 1901.
- Performer / recording: United States Marine Band, directed by Col. John R. Bourgeois, from *Sound Off!* (1992).
- Source file: `docs/assets/011_secret_alliance/source_audio/revelation_us_marine_band_commons_source.ogg`
- Source record and rights: the United States Marine Band is a United States federal military ensemble. The selected federal-government recording is documented as public domain in `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md`.
- Duration: `86.101746` seconds.
- Music catalogue: `music/chaosx_music_track_list.html` records The Pact Unmasked, audio ID `43`, `Revelation`, William Paris Chambers, the United States Marine Band performance, duration `01:26`, and verified public-domain status.
- Conversion notes: the final WAV is derived from the licensed source, uses the unique Event 011 path, and is registered with the settings-aware music helper. No reused track, generated tone, placeholder, or attribution-dependent substitute is used.

## Camp Repression Rework

### The Evidence Crosses the Wire

- Super-event ID: `74`
- Audio ID: `44`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.wav`
- Runtime music OGG: `music/system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.ogg`
- Music definition keys: `chaosx_super_event_44_0`, `chaosx_super_event_44_0_5`, `chaosx_super_event_44_1_0`, `chaosx_super_event_44_1_5`, `chaosx_super_event_44_2_0`, `chaosx_super_event_44_2_5`, and `chaosx_super_event_44_3_0`.
- Source title: `Gnossienne No. 1`
- Composer / creator: Erik Satie.
- Performer / recording: La Pianista, 2010 self-recording.
- Source URL: <https://commons.wikimedia.org/wiki/File:Satie_-_Gnossienne_1.ogg>
- License: public-domain composition; CC BY-SA 3.0 performance.
- Duration: 1:52 final excerpt.
- Conversion notes: normalized and faded from the source opening; registered with the settings-aware music helper.

### The Empty Granaries

- Super-event ID: `75`
- Audio ID: `46`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.wav`
- Runtime music OGG: `music/system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.ogg`
- Music definition keys: `chaosx_super_event_46_0`, `chaosx_super_event_46_0_5`, `chaosx_super_event_46_1_0`, `chaosx_super_event_46_1_5`, `chaosx_super_event_46_2_0`, `chaosx_super_event_46_2_5`, and `chaosx_super_event_46_3_0`.
- Source title: `Hey, Plyve Kacha po Tysyni`
- Composer / creator: traditional Ukrainian Lemko folk lament.
- Performer / recording: Revutsky Capella, London, 2013.
- Source URL: <https://commons.wikimedia.org/wiki/File:%D0%9A%D0%B0%D0%BF%D0%B5%D0%BB%D0%B0_%D1%96%D0%BC._%D0%A0%D0%B5%D0%B2%D1%83%D1%86%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_-_%D0%93%D0%B5%D0%B9,_%D0%BF%D0%BB%D0%B8%D0%B2%D0%B5_%D0%BA%D0%B0%D1%87%D0%B0_%D0%BF%D0%BE_%D0%A2%D0%B8%D1%81%D0%B8%D0%BD%D1%96.webm>
- License: traditional composition; CC BY 3.0 recording.
- Duration: 1:56 final excerpt.
- Conversion notes: audio isolated from WebM, timestamps repaired, normalized, and faded; registered with the settings-aware music helper.

### The Pingfang Files

- Super-event ID: `76`
- Audio ID: `47`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/system_camp_repression_rework/super_event_47_pingfang_exposure.wav`
- Runtime music OGG: `music/system_camp_repression_rework/super_event_47_pingfang_exposure.ogg`
- Music definition keys: `chaosx_super_event_47_0`, `chaosx_super_event_47_0_5`, `chaosx_super_event_47_1_0`, `chaosx_super_event_47_1_5`, `chaosx_super_event_47_2_0`, `chaosx_super_event_47_2_5`, and `chaosx_super_event_47_3_0`.
- Source title: `Yangguan Sandie (Three Refrains on the Yang Pass Theme)`
- Composer / creator: traditional Chinese guqin repertory; `Qinxue Rumen` (1867) score source.
- Performer / recording: Charlie Huang / Charles R Tsua, 2013.
- Source URL: <https://commons.wikimedia.org/wiki/File:Guqin-Yangguan_Sandie.ogg>
- License: public-domain score source; CC BY-SA 3.0 performance.
- Duration: 1:49 final excerpt.
- Conversion notes: leading silence removed and the excerpt closed at the first extended musical pause; registered with the settings-aware music helper.

### The Empire's Accounts

- Super-event ID: `77`
- Audio ID: `48`
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/system_camp_repression_rework/super_event_48_colonial_reckoning.wav`
- Runtime music OGG: `music/system_camp_repression_rework/super_event_48_colonial_reckoning.ogg`
- Music definition keys: `chaosx_super_event_48_0`, `chaosx_super_event_48_0_5`, `chaosx_super_event_48_1_0`, `chaosx_super_event_48_1_5`, `chaosx_super_event_48_2_0`, `chaosx_super_event_48_2_5`, and `chaosx_super_event_48_3_0`.
- Source title: `Go Down Moses`
- Composer / creator: traditional nineteenth-century African American spiritual.
- Performer / recording: Les Petits Chanteurs de Montigny, Jamendo, 2005.
- Source URL: <https://commons.wikimedia.org/wiki/File:01_-_Go_down_Moses_(Negro_Spiritual).ogg>
- License: public-domain traditional composition; CC BY-SA 2.0 performance.
- Duration: 1:50 final excerpt.
- Conversion notes: normalized and faded while retaining the source license metadata; registered with the settings-aware music helper.

## Event 015 Utopia Manifesto

### Utopia Has Neighbors

- Super-event display slots: `96`, `97`, `98`, `99`, and `100`; playback audio ID: `57`.
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/015_utopia_manifesto/super_event_57_utopia_has_neighbors.wav`
- Runtime music OGG: `music/015_utopia_manifesto/super_event_57_utopia_has_neighbors.ogg`
- Music definition keys: `chaosx_super_event_57_0`, `chaosx_super_event_57_0_5`, `chaosx_super_event_57_1_0`, `chaosx_super_event_57_1_5`, `chaosx_super_event_57_2_0`, `chaosx_super_event_57_2_5`, and `chaosx_super_event_57_3_0`.
- Source title: Johannes Brahms, *Symphony No. 3 in F major, Op. 90*, III. *Poco allegretto*.
- Performer / recording source: Musopen Symphony Orchestra.
- Source URL: <https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._3_in_F_Major,_Op._90_-_III._Poco_allegretto.ogg>.
- Frozen source revision: <https://commons.wikimedia.org/w/index.php?title=File:Brahms,_Symphony_No._3_in_F_Major,_Op._90_-_III._Poco_allegretto.ogg&oldid=956414568>.
- Rights: public-domain composition and file-specific [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) recording. CC0 applies to the Commons file and supplies a worldwide waiver of copyright and related or neighbouring rights to the extent allowed by law. Attribution is not required, but courtesy credit is retained and no endorsement is implied.
- Preserved source: `docs/super_events/source_audio/015_utopia_manifesto/brahms_symphony_3_iii_poco_allegretto_musopen_cc0_original.ogg`; `8,770,243` bytes; Commons SHA-1 `38f129111cb55461c7749a52b7ac608a13709b11`; SHA-256 `ba1db2035d78954d5f15711594817ccceaa730bd83df68734cb724a2e3ba32df`.
- Edit: Chaos Redux retained `00:00.000-01:56.000`, applied a `0.500 s` fade-in and `6.000 s` fade-out, normalized to approximately `-18 LUFS`, and rendered the `116.000000 s` 44.1 kHz stereo runtime WAV.
- Final WAV hash: `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`.
- Uniqueness: the Event 015 recording is unique among the super-event cues.
- Full source, licence, edit, technical, and uniqueness ledger: `docs/super_events/015_utopia_manifesto/audio_research.md`.

## Event 018 Resources Found

The complete source, edit, hash, loudness, and rights ledger is `docs/assets/018_resources_found/audio_manifest.md`. All three cues are unique 60-to-120-second, 44.1 kHz stereo cues registered with the settings-aware music helper. Their stable durations are `115.000000 s`, `110.000000 s`, and `109.000000 s`.

### The Oth-Kesh Host Rises

- Super-event ID: `82`; audio ID: `54`.
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/018_resources_found/super_event_54_oth_kesh_emergence.wav`
- Runtime music OGG: `music/018_resources_found/super_event_54_oth_kesh_emergence.ogg`
- Music definition keys: `chaosx_super_event_54_0`, `chaosx_super_event_54_0_5`, `chaosx_super_event_54_1_0`, `chaosx_super_event_54_1_5`, `chaosx_super_event_54_2_0`, `chaosx_super_event_54_2_5`, and `chaosx_super_event_54_3_0`.
- Source: Modest Mussorgsky, *Pictures at an Exhibition* — `IV. Bydło`, performed by Skidmore College Orchestra; Musopen public-domain recording preserved with VRTS confirmation by Wikimedia Commons.
- Rights: public-domain composition and recording; courtesy credit retained.
- Edit: source `00:24.000–02:18.750` plus a `0.250 s` zero tail; `1.500 s` quarter-sine fade-in, `5.000 s` quarter-sine fade-out, fixed `-2.6 dB` gain, SoXr resample to 44.1 kHz, and WAV rendering by Chaos Redux. Final duration: `115.000000 s`.

### The Deep War Crosses the Seas

- Super-event ID: `83`; audio ID: `55`.
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/018_resources_found/super_event_55_deep_war_crosses_seas.wav`
- Runtime music OGG: `music/018_resources_found/super_event_55_deep_war_crosses_seas.ogg`
- Music definition keys: `chaosx_super_event_55_0`, `chaosx_super_event_55_0_5`, `chaosx_super_event_55_1_0`, `chaosx_super_event_55_1_5`, `chaosx_super_event_55_2_0`, `chaosx_super_event_55_2_5`, and `chaosx_super_event_55_3_0`.
- Source: Johannes Brahms, Symphony No. 1 in C minor, Op. 68 — I. `Un poco sostenuto - Allegro`; performed by the Czech National Symphony Orchestra and published as the Musopen Symphony Orchestra recording.
- Rights: public-domain composition and recording dedicated under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). CC0 supplies the worldwide copyright and neighbouring-rights waiver required for redistribution and adaptation.
- Courtesy credit: Johannes Brahms, Symphony No. 1 in C minor, Op. 68 - I. `Un poco sostenuto - Allegro`; Czech National Symphony Orchestra / Musopen Symphony Orchestra; source via Wikimedia Commons; CC0 1.0. No endorsement is implied.
- Edit: source `08:40.000–10:29.750` plus a `0.250 s` zero tail; `1.500 s` quarter-sine fade-in, `6.000 s` quarter-sine fade-out, SoXr resample to 44.1 kHz, and WAV rendering by Chaos Redux. No compression or limiting was applied. Final duration: `110.000000 s`.

### The Last Depth Is Sealed

- Super-event ID: `84`; audio ID: `56`.
- Original recording (LFS archive): `Documents/chaos_redux_lfs_archive/sound/018_resources_found/super_event_56_last_depth_sealed.wav`
- Runtime music OGG: `music/018_resources_found/super_event_56_last_depth_sealed.ogg`
- Music definition keys: `chaosx_super_event_56_0`, `chaosx_super_event_56_0_5`, `chaosx_super_event_56_1_0`, `chaosx_super_event_56_1_5`, `chaosx_super_event_56_2_0`, `chaosx_super_event_56_2_5`, and `chaosx_super_event_56_3_0`.
- Required credit: Frédéric Chopin, Prelude in E minor, Op. 28 No. 4; performed by Ivan Ilić, Paris, October 2005; source via Wikimedia Commons / IMSLP. Recording licensed [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
- Edit: Chaos Redux excerpted `00:00.450–01:49.200`, applied a `1.250 s` quarter-sine fade-in, `5.000 s` quarter-sine fade-out, fixed `+6.5 dB` gain, and a `0.250 s` zero tail, then rendered the runtime WAV. Final duration: `109.000000 s`. No endorsement by Ivan Ilić is implied.


## Music Station Registration

All seven music keys for each of the 71 current super-event audio IDs, including each zero-volume `_0` mute key, are registered in `music/chaosx_super_event_music.txt` with `chance = { factor = 0 }`. The seven Fallout blackout keys are registered the same way, so none of these cues enters random station playback.
