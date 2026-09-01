# Super-event duplicate-audio replacement audit

Date: 2026-09-01.

This audit covers every base super-event WAV registered through `sound/**/*.asset` and the canonical rows in `music/chaosx_music_track_list.html`.

The audit treats the same normalized source title plus composer or creator as a documentation duplicate, and it also compares decoded Chromaprint fingerprints so renamed, remastered, trimmed, or differently encoded copies of one recording are still detected.

## Baseline findings

The registered runtime contained 69 base super-event cues.

Four decoded-audio reuse groups required replacement:

| Reused recording | Retained cue | Replaced cue |
|---|---|---|
| Brahms, *Tragic Overture*, Musopen Symphony | Playback 116, Event 028 asteroid impact | Playback 111, Event 039 assassin-state reveal |
| Mussorgsky, *Night on Bald Mountain*, Musopen | Playback 114, Event 031 false revelation | Playback 12, Angel Directorate reveal |
| Nyarlathotep1001 Heart Sutra recording | Playback 8, Mandala terminal cue | Playback 9, Final Silence |
| Membeth *Dies irae* recording | Playback 3, Zombie Apocalypse | Playback 102, Rat King world end |

The catalogue also contained one false metadata collision between playbacks 12 and 45, three repeated placeholder rows for playbacks 15, 17, and 18, three source-incomplete legacy rows for playbacks 1, 5, and 6, and no rows for registered Event 039 playbacks 111 through 113.

Playback 12's decoded recording matched playback 114 and was not the Bach recording claimed by its old catalogue row.

## Accepted runtime package

All target paths remain stable so no sound definition or gameplay consumer needed to change.

| ID | Runtime path | Accepted source | Composer or creator | Performer or recording | Rights basis | Edit | Final SHA-256 |
|---:|---|---|---|---|---|---|---|
| 1 | `sound/002_zombie_outbreak/super_event_1_zombies.wav` | *The Sea and Sinbad's Ship* from *Scheherazade*, movement I | Nikolai Rimsky-Korsakov | San Francisco Symphony, Pierre Monteux, and Naoum Blinder | Public-domain composition and CC0 1.0 recording | Opening 105 seconds with fades; 105.000000 seconds | `753778951E4AB1FC6F72AE54A00C5BE8BDC1C8CCA527DE9E9F9BA0C1CF3ACEAC` |
| 5 | `sound/002_zombie_outbreak/super_event_5_zombies_defeat.wav` | *La Réjouissance* from *Music for the Royal Fireworks*, HWV 351, movement IV | George Frideric Handel | St Matthew Concert Choir and Paul Ayres | Public-domain composition and CC0 1.0 recording | Full source with fades; 98.633741 seconds | `20FB149DF2AEE1DE553E3080CE1B2070CEC080AC53F285EBF67DAEF56D662389` |
| 6 | `sound/002_zombie_outbreak/super_event_6_wendigo.wav` | *Má vlast – Vltava (The Moldau)* | Bedřich Smetana | Musopen Symphony Orchestra | Public-domain composition and CC0 1.0 recording | Rapids section, source 495–600 seconds, with fades; 105.000000 seconds | `DC01CD34CF253C3D76FB275389247CD830B161988A68077908AD1A3153A7DDA5` |
| 9 | `sound/003_holy_realm/super_event_9_final_silence_thermonuclear.wav` | *Chanting at Lingyin Temple, Hangzhou* | Traditional Buddhist liturgical chant | Louise Brown field recording | CC BY-SA 3.0 recording | Near-complete source, stereo conversion, and fades; 63.188005 seconds | `26BAA65E2095BC3A96DE73CF7B3B406AC42730FF5E06B9CC52CE7C7222A19DD7` |
| 12 | `sound/003_holy_realm/super_event_12_angel_directorate.wav` | *Totentanz*, S. 126 | Franz Liszt | Neal O'Doan, piano, with orchestra | Public-domain composition and CC BY-SA 2.0 / EFF Open Audio License recording | Opening 110 seconds with fades; 110.000000 seconds | `1429AED56E4E71175A3FEED7FE5025A4901736FA165AA1F85F73D71323A08FBE` |
| 15 | `sound/005_soviet_collapse/super_event_15_black_banner_returns.wav` | *A las barricadas*, instrumental | Wacław Święcicki | CNT centenary recording directed by Luís Antonio Gamarra | Public-domain composition and CC BY-SA 3.0 recording | Full source with fades; 77.989955 seconds | `7E4E300998E0D25EAB49ED4DF1FEE40AA021BD22C19E0064A4D204ED5655AE0A` |
| 17 | `sound/005_soviet_collapse/super_event_17_workshops_choose_councils.wav` | *The Red Flag from Lansbury's Labour Weekly* | Jim Connell | Lansbury's Labour Weekly institutional recording, 1926 | Worldwide public-domain dedication with unconditional fallback | Opening 110 seconds with fades; 110.000000 seconds | `DD29D63DEED6489A33701CA2874111B039A43232D10344851BE07AA14686A2FE` |
| 18 | `sound/005_soviet_collapse/super_event_18_every_port_a_council.wav` | *Song of the Volga Boatmen (Эй, ухнем!)* | Traditional Russian folk song | Feodor Chaliapin, 1902 | PD-RusEmpire and pre-1931 U.S. public domain | Opening 105 seconds with fades; 104.976780 seconds | `36916C3078E48FE95A202BB429663921839E9BFF6771D0E1DFA84A04F9E117C7` |
| 102 | `sound/020_black_plague/super_event_102_rat_king_world_end.wav` | *Requiem in D minor, "Lacrimosa"*, piano arrangement | Wolfgang Amadeus Mozart, arranged by Sigismond Thalberg | Lệ Xuân | Public-domain composition and arrangement with CC BY-SA 4.0 recording | Opening 105 seconds with fades; 105.000000 seconds | `DE5CDF237958F73EF04C2A61602182C83DCAA2D91FCDF8ABE626D6EA9B55C1CD` |
| 111 | `sound/039_murder_mystery/super_event_111_assassin_state_reveal.wav` | *Piano Concerto No. 2 in C minor*, Op. 18, movement I, *Moderato* | Sergei Rachmaninoff | Musopen recording | Public-domain composition and worldwide public-domain recording dedication with unconditional fallback, VRTS 2008012110017088 | Opening 110 seconds with fades; 110.000000 seconds | `9533170D0E6D051B1FE0070C55F45BEAB278A389620D59784AF48E580982A50C` |

Playbacks 5 and 18 retain their identifiable underlying recordings after exact-source verification and a clean PCM16 remaster.

The other eight targets use replacement recordings.

## Source pages and preserved evidence

- Playback 1: <https://commons.wikimedia.org/wiki/File:Rimsky-Korsakov,_Scheherazade,_Symphonic_Suite,_Op._35_-_01_The_Sea_and_Sinbads_Ship.ogg>
- Playback 5: <https://commons.wikimedia.org/wiki/File:Paul_Ayres_-_Handel%27s_Music_for_the_Royal_Fireworks,_HWV_351_-_IV._La_R%C3%A9jouissance.ogg>
- Playback 6: <https://commons.wikimedia.org/wiki/File:Smetana,_Má_vlast_-_Vltava_-_The_Moldau.ogg>
- Playback 9: <https://commons.wikimedia.org/wiki/File:Chanting_at_Lingyin_Temple,_Hangzhou.ogg>
- Playback 12: <https://commons.wikimedia.org/wiki/File:Liszt_Totentanz.ogg>
- Playback 15: <https://commons.wikimedia.org/wiki/File:A_las_barricadas_(Instrumental).ogg>
- Playback 17: <https://commons.wikimedia.org/wiki/File:The_Red_Flag_from_Lansbury%27s_Labour_Weekly.ogg>
- Playback 18: <https://commons.wikimedia.org/wiki/File:%D0%AD%D0%B9,_%D1%83%D1%85%D0%BD%D0%B5%D0%BC!_-_%D0%A4%D1%91%D0%B4%D0%BE%D1%80_%D0%A8%D0%B0%D0%BB%D1%8F%D0%BF%D0%B8%D0%BD.ogg>
- Playback 102: <https://commons.wikimedia.org/wiki/File:Mozart,_Requiem_in_D_minor,_%27Lacrimosa%27_%E2%80%93_piano_arrangement.ogg>
- Playback 111: <https://commons.wikimedia.org/wiki/File:Sergei_Rachmaninoff_-_piano_concerto_no._2_in_c_minor,_op._18_-_i._moderato.ogg>

The original source files, captured source pages, and staged derivatives are preserved under each affected event's `docs/assets/<event>/source_audio/duplicate_audio_replacements_2026-09-01/` directory.

The independent comparison in `duplicate_audio_alternatives_9_111_2026-09-01.md` confirms the Lingyin cue as the stronger rights choice for playback 9 and independently accepts the Rachmaninoff cue for playback 111.

## Validation

Every installed target decodes as stereo signed 16-bit PCM at 44,100 Hz and is shorter than 120 seconds.

The staged and installed SHA-256 values match for all ten targets.

The post-install decoded Chromaprint audit compared all 69 registered base cues with an offset-tolerant normalized Hamming-distance pass.

No pair remained below the conservative duplicate-review threshold of `0.18`.

The replacement researcher's target-specific comparison also found no staged-to-base reuse for the eight new recordings and exact expected identity only for the two reverified legacy sources.

## Rights caveat

Playback 18's 1902 Chaliapin recording is documented as public domain in the Russian Empire source jurisdiction and the United States rather than under an unconditional worldwide license.

The catalogue states that territorial basis directly and does not describe the recording as CC0 or universally dedicated.
