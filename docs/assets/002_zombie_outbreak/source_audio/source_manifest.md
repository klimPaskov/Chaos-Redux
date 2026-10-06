# Event 002 Audio Source Archive

This archive restores verifiable source evidence for the existing Zombie Outbreak super-event WAVs as of 2026-10-06. It does not change any runtime audio.

## Confirmed source recordings

### Super-event ID 1 — Undead?

- Source title: Nikolai Rimsky-Korsakov, *Scheherazade*, Op. 35, I. “The Sea and Sinbad’s Ship,” composed 1888.
- Performer and recording: San Francisco Symphony Orchestra conducted by Pierre Monteux, violin solo by Naoum Blinder; recorded in 1942 and transferred from Victor DM-920 by Bob Varney.
- Source pages: [Internet Archive item](https://archive.org/details/Sheherazade), whose rights field marks the recording Public Domain; [Wikimedia Commons file revision 628862047](https://commons.wikimedia.org/wiki/File:Rimsky-Korsakov._Scheherazade,_Symphonic_Suite,_Op._35_-_01_The_Sea_And_Sinbads_Ship.ogg?oldid=628862047), whose file-specific license is CC0 1.0.
- Composition rights: the 1888 composition is public domain; Rimsky-Korsakov died in 1908.
- Recording rights: the Internet Archive item marks use Public Domain, and the Commons OGG file page records a worldwide CC0 dedication. License confidence is high for the recording preserved here.
- Attribution: CC0 requires none; courtesy credit is recommended as “Nikolai Rimsky-Korsakov, *Scheherazade*, I. ‘The Sea and Sinbad’s Ship,’ San Francisco Symphony Orchestra, Pierre Monteux, Naoum Blinder; 1942 recording transferred by Bob Varney; source via Internet Archive.”
- Downloaded source: `rimsky_korsakov_scheherazade_i_archive_original.mp3`, 19,953,265 bytes, 498.817875 seconds, SHA-1 `f8f5d1744c8e64fb905c36897dc4db130d0e0064`, SHA-256 `437af712f594e92bb1abaf863a8709c66894e93611a17c5c13b02ee1b4c71b1b`.
- Runtime: `sound/002_zombie_outbreak/super_event_1_zombies.wav`, sound definition `chaosx_super_event_zombies_track`, 105.000000 seconds, SHA-256 `753778951e4ab1fc6f72ae54a00c5be8bdc1c8cca527de9e9f9ba0c1cf3aceac`.
- Edit evidence: the runtime uses the source opening `00:00.000-01:45.000`, rendered as stereo 44.1 kHz PCM16 with entry and exit fades; the retained notes do not give fade lengths. Decoded-PCM correlation aligns to source offset `0.000 s`, with coefficients `0.998199` at runtime `00:40` and `0.997459` at `01:15`; the `0.957256` coefficient at `00:10` may reflect the entry fade or the different source encoding, and the retained evidence does not distinguish those causes.
- Suggested use: opening outbreak reveal.

### Super-event ID 5 — The Dead Are Buried

- Source title: George Frideric Handel, *Music for the Royal Fireworks*, HWV 351, IV. “La Réjouissance.”
- Performer and recording: Paul Ayres; Internet Archive identifies the selected recording as `09TheRejoicing.mp3` in *Handel Music for the Royal Fireworks (2011)*.
- Source pages: [Internet Archive item](https://archive.org/details/HandelMusicForTheRoyalFireworks2011), [direct original MP3](https://archive.org/download/HandelMusicForTheRoyalFireworks2011/09TheRejoicing.mp3), and [Wikimedia Commons file revision 794973790](https://commons.wikimedia.org/wiki/File:Paul_Ayres_-_Handel%27s_Music_for_the_Royal_Fireworks,_HWV_351_-_IV._La_R%C3%A9jouissance.ogg?oldid=794973790).
- Composition rights: Handel’s composition is public domain.
- Recording rights: the Internet Archive item and Commons file page identify the Paul Ayres recording as CC0 1.0. License confidence is high for the recording preserved here.
- Attribution: CC0 requires none; courtesy credit is recommended as “George Frideric Handel, *Music for the Royal Fireworks*, IV. ‘La Réjouissance,’ performed by Paul Ayres; source via Internet Archive; CC0 1.0.”
- Downloaded source: `handel_royal_fireworks_rejoicing_archive_original.mp3`, 3,216,864 bytes, 98.742857 seconds, SHA-1 `39bccf51a21ee753474796c3640621def052d8e5`, SHA-256 `80e353c2a2ad1b1850b2d291444ec55a66eb0f306b993eed2f0fcc270f9184aa`.
- Runtime: `sound/002_zombie_outbreak/super_event_5_zombies_defeat.wav`, sound definition `chaosx_super_event_zombies_defeat_track`, 98.633741 seconds, SHA-256 `20fb149df2aee1de553e3080ce1b2070cec080ac53f285ebf67daef56d662389`.
- Edit evidence: decoded-PCM comparisons align at source offset `0.000 s`, with coefficients `0.997126` at runtime `00:08`, `0.996889` at `00:35`, and `0.997235` at `01:10`. The runtime retains the source opening and is 0.109116 seconds shorter than the source; entry and exit fades are documented, but their lengths are not retained.
- Suggested use: defeat aftermath and burial.

## Source records awaiting local bytes

The Commons file pages below identify legally usable recordings and publish their file sizes and SHA-1 checksums. No local original was recovered for these rows, so no source-to-runtime comparison is claimed.

| Super-event ID and title | Sound definition | Recording and source | Rights evidence, confidence, and attribution | Commons source metadata and local source path | Runtime evidence | Suggested use |
| --- | --- | --- | --- | --- | --- | --- |
| 2 — The Alliance of Man | `chaosx_super_event_alliance_of_man_track` | Composition by John William Steffe and Julia Ward Howe, arranged by Eric Richards; performed by the United States Air Force Band Airmen of Note, conducted by Col. Dennis M. Layendecker; [Commons revision 1030745773](https://commons.wikimedia.org/wiki/File:Battle_Hymn_of_the_Republic_(USAFB).ogg?oldid=1030745773). | Commons identifies an official U.S. Air Force employee recording and marks it Public Domain in the United States; the page also records Public Domain Mark 1.0 and the 1861 composition. Confidence: high per the file page. No attribution is required; courtesy credit is optional. | 326.608980 seconds; 6,322,760 bytes; SHA-1 `1acfc958af0455849032cf0e405a38f5a051e2b0`. Local source path: not recovered. | Runtime `sound/002_zombie_outbreak/super_event_2_alliance_of_man.wav`, 89.978776 seconds, SHA-256 `181c48a3e69b94cd0fb0f805af18c90a565eb7b9d4475dcb92d4ab03c8f023ec`; source match untested and edit details are not retained here. | Human alliance response. |
| 3 — Zombie Apocalypse | `chaosx_super_event_zombie_apocalypse_track` | Gregorian *Dies Irae* recorded by Membeth; [Commons revision 1205385897](https://commons.wikimedia.org/wiki/File:Dies.irae.ogg?oldid=1205385897). | The medieval chant composition is public domain; Membeth’s file page says the recording was released worldwide into the public domain by its copyright holder. Confidence: high per the file page. No attribution is required; courtesy credit is optional. | 434.000952 seconds; 6,562,097 bytes; SHA-1 `d13e914db3016ab43bcb89c695e501ac8fd19605`. Local source path: not recovered. | Runtime `sound/002_zombie_outbreak/super_event_3_zombie_apocalypse.wav`, 95.000000 seconds, SHA-256 `a3fb7d844507f05cbc277d845f24e9d561dce508adaef77a0c163edc8524867d`; source match untested and edit details are not retained here. | Catastrophic outbreak escalation. |
| 6 — Wendigo | `chaosx_super_event_wendigo_track` | Musopen Symphony Orchestra, *Má vlast: Vltava (The Moldau)*; [Commons revision 955954082](https://commons.wikimedia.org/wiki/File:Smetana,_M%C3%A1_vlast_-_Vltava_-_The_Moldau.ogg?oldid=955954082), with the [current Musopen piece page](https://musopen.org/music/25719-ma-vlast-vltava-the-moldau/). | Smetana composed the work in 1874 and died in 1884; the Commons page dedicates this recording file under CC0 1.0. Confidence: high for the Commons file. Attribution is not required; courtesy credit to Musopen is optional. | 12:51 source duration; 20,531,794 bytes; SHA-1 `a0025fa04c0774296d2528a44b68e6a6938b2ae3`. Local source path: not recovered. | Runtime `sound/002_zombie_outbreak/super_event_6_wendigo.wav`, 105.000000 seconds, SHA-256 `dc01cd34cf253c3d76fb275389247cd830b161988a68077908ad1a3153a7dda5`; source match untested and edit details are not retained here. | Wendigo branch reveal. |

## Retrieval blocker

The initial Commons original-file request returned HTTP 429 with a Wikimedia bot-traffic notice before any Commons recording was saved; I stopped the batch at that response and did not retry or work around the limit. Internet Archive source files for IDs 1 and 5 were retrieved through their directly linked archive records instead. The USAF source link on the Commons page did not return accessible page content in the web fetch. The current Musopen track page is readable, but its direct fetch returned a JavaScript/Cloudflare challenge, so it did not yield a source audio file.
