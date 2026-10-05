# Event 005 Super-Event Audio Provenance Audit, 2026-10-05

## Scope and disposition

This is a read-only audit of the four Event 005 super-event audio assignments that have sound definitions and the current music catalogue entries.

The connected audit found no WAV source files or dedicated audio research note under `docs/assets/005_soviet_collapse/source_audio/`.

The audit did not edit or replace audio and does not establish complete legal clearance for every recording.

## Active audio assignments

| Super-event | Base sound | Runtime duration and format | Runtime SHA-256 | Catalogue status |
| --- | --- | --- | --- | --- |
| 14, Union Unmade | `chaox_super_event_union_unmade_track` | 119.500 s, 44.1 kHz stereo, 32-bit float PCM, 42,159,714 bytes | `912E2AE6389835EC5E3CAA9FD44201149DC9989388452D670CC03B6A39F6F083` | Hash absent; only float-PCM file among the four. |
| 15, Black Banner Returns | `chaox_super_event_black_banner_returns_track` | 77.990 s, 44.1 kHz stereo, 16-bit PCM, 13,757,506 bytes | `7E4E300998E0D25EAB49ED4DF1FEE40AA021BD22C19E0064A4D204ED5655AE0A` | Hash matches catalogue. |
| 17, Workshops Choose Councils | `chaox_super_event_workshops_choose_councils_track` | 110.000 s, 44.1 kHz stereo, 16-bit PCM, 19,404,078 bytes | `DD29D63DEED6489A33701CA2874111B039A43232D10344851BE07AA14686A2FE` | Hash matches catalogue. |
| 18, Every Port a Council | `chaox_super_event_every_port_a_council_track` | 104.977 s, 44.1 kHz stereo, 16-bit PCM, 18,517,982 bytes | `36916C3078E48FE95A202BB429663921839E9BFF6771D0E1DFA84A04F9E117C7` | Hash matches catalogue. |

Definitions are in `sound/chaox_sound.asset:695-712`, and the catalogue rows are in `music/chaox_music_track_list.html:223` onward.

Each assignment has six sound wrappers from `_sound_0_5` through `_sound_3_0`, with recorded volumes 0.67, 1.33, 2.00, 2.67, 3.33, and 4.00.

The wired effect setters are IDs 14, 15, 17, and 18; IDs 16 and 19–22 have no current WAV, sound definition, wrapper, catalogue row, or setter and remain dormant presentation candidates.

## Source and rights evidence

- **14:** The catalogue identifies Beethoven and the Czech National Symphony Orchestra / Musopen recording but omits the source link, downloaded-source path, trim/fade recipe, and runtime hash. The Event 013 archive records the [Commons source page](https://commons.wikimedia.org/wiki/File%3ABeethoven_-_Egmont_Overture%2C_Op._84_%28Musopen_Symphony%29.flac) and [Musopen page](https://musopen.org/music/13441), describes the worldwide public-domain dedication and unconditional-use fallback, and gives a courtesy credit.
- **15:** The [Commons recording page](https://commons.wikimedia.org/wiki/File:A_las_barricadas_(Instrumental).ogg) identifies the CNT centenary re-recording and CC BY-SA 3.0 terms. The catalogue records the conservatory, director, source link, excerpt, fades, and ShareAlike distribution but lacks a precise attribution line and substantiation for its composition public-domain statement.
- **17:** The [Commons recording page](https://commons.wikimedia.org/wiki/File:The_Red_Flag_from_Lansbury%27s_Labour_Weekly.ogg) identifies the 1926 recording and a worldwide public-domain dedication with an unconditional-use fallback; the [Bishopsgate Institute page](https://www.bishopsgate.org.uk/archives/our-archives-online/recordings-from-lansburys-labour-weekly-1) identifies the holding institution. The catalogue names Jim Connell as composer while the recording page credits Lansbury's Labour Weekly, so any future source note should distinguish composition authorship from recording authorship.
- **18:** The [Commons recording page](https://commons.wikimedia.org/wiki/File%3A%D0%AD%D0%B9%2C_%D1%83%D1%85%D0%BD%D0%B5%D0%BC%21_-_%D0%A4%D1%91%D0%B4%D0%BE%D1%80_%D0%A8%D0%B0%D0%BB%D1%8F%D0%BF%D0%B8%D0%BD.ogg) identifies Feodor Chaliapin's 1902 recording and its SovietMusic source. The catalogue records the traditional composition, PD-RusEmpire basis, pre-1931 U.S. recording status, and a 105-second excerpt with fades; the cited page does not give a worldwide recording-rights dedication.

All four files contain an encoder tag but no embedded source or license metadata.

The Event 013 archive and production note document the inherited Egmont source and Soviet audio cleanup, but the cited `docs/assets/013_natural_disasters` archive is absent from this checkout.

## Remaining work

The owner must decide whether the float-PCM encoding of ID 14 is accepted for the game, then record the tested format decision and final file hash.

The owner should create a durable Event 005 audio note with source download path, attribution, license basis, excerpt bounds, fades, final hashes, and any required conversion recipe after reviewing each source against current rights evidence.

No audio claim should be made for dormant IDs 16 and 19–22 until a setter, sound asset, and licensed or public-domain source package exist.
