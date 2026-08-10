# Event 018 cave-unit audio recipe reconstruction

Status: `static_pass_with_one_byte_variance`.

The four Wikimedia Commons originals were freshly retrieved on 2026-08-10 and match the hashes recorded during production. No generated, synthesized, placeholder, normalized, amplified, or otherwise substituted audio is used. The runtime derivatives are mono 44.1 kHz signed 16-bit PCM WAV files.

## Immutable originals

| Role | Source page | Licence | SHA-256 |
| --- | --- | --- | --- |
| Idle bellow | `https://commons.wikimedia.org/wiki/File:Alligatorbellow1.ogg` | U.S. Fish and Wildlife Service public-domain work | `72A5612E99B6A941D751EFBCCF1E44F816C06C7884E3108C5298A2BA84B25169` |
| Gravel movement | `https://commons.wikimedia.org/wiki/File:Walking-on-gravel-38827.ogg` | CC0 1.0 | `14990DE1FD15418B55A2C939B0A99348446E613C1C4A5A307E49A87D228DE5EF` |
| Attack roar | `https://commons.wikimedia.org/wiki/File:Lion_raring-sound1TamilNadu178.ogg` | Public-domain self-release by தகவலுழவன் | `AB237D0F960E83412251D0C11F69959F3C2E8D3B14595F7181C3056F7FA18BF7` |
| Gravel collapse | `https://commons.wikimedia.org/wiki/File:Assorted_gravel_rock_and_stones.ogg` | Public-domain release by stephan | `BC254F5C70EE0252FDC79278F83E5428B6953807CFC21805052E6A617F2BB330` |

## Normalized derivation commands

The current verification environment is FFmpeg `N-123778-g3b55818764-20260331`. Paths below are basenames for readability; each output is written directly as PCM WAV.

```powershell
ffmpeg -i idle_alligator_bellow.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=24.2:d=0.04" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_idle.wav

ffmpeg -ss 0.0 -t 0.28 -i move_walking_on_gravel.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=0.26:d=0.02" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_move_foot_01.wav
ffmpeg -ss 1.5 -t 0.28 -i move_walking_on_gravel.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=0.26:d=0.02" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_move_foot_02.wav
ffmpeg -ss 3.0 -t 0.28 -i move_walking_on_gravel.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=0.26:d=0.02" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_move_foot_03.wav
ffmpeg -ss 4.5 -t 0.28 -i move_walking_on_gravel.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=0.26:d=0.02" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_move_foot_04.wav

ffmpeg -i attack_lion_roar.ogg -af "asetpts=N/SR/TB,afade=t=out:ss=35579:ns=882,atrim=end_sample=37120" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_attack_bounded.wav

ffmpeg -t 1.5 -i death_gravel_rocks.ogg -af "afade=t=in:st=0:d=0.02,afade=t=out:st=1.48:d=0.02" -ac 1 -ar 44100 -c:a pcm_s16le resources_found_cave_monster_death_bounded.wav
```

The attack source has a nonzero OGG start timestamp. `asetpts=N/SR/TB` is required before the sample-addressed fade and trim; without it, FFmpeg applies the fade against the source timestamp and does not reproduce the runtime cue.

## Reproduction results

| Runtime cue | Runtime SHA-256 | Fresh result |
| --- | --- | --- |
| Idle | `2F3C569FA0333ECBE870D93B71B4B0E094FBDFD5CA4F107885A7155D9BE95AAA` | Exact byte match |
| Move foot 01 | `8ECD3DC57E6E53D687740E386DEDB811A5E804D8B244BD3CDB3DA5C686AB62CF` | Exact byte match |
| Move foot 02 | `1B83E1257BD6FFEA65DC78866782E2D0A8D4387C570471B60B3769BA2667C2C0` | One least-significant PCM unit differs in the final sample only: fresh `-3`, runtime `-2`; all preceding 12,347 samples are identical |
| Move foot 03 | `DA7AE70FFC077E635E8938CDF4E6868272CDCDAB0F690E218BD63DC1983937E5` | Exact byte match |
| Move foot 04 | `9AE099698780D71DBF60B47710179E84830C57E48E8EBB67E4608D4774142300` | Exact byte match |
| Attack | `0437FB79CF23B8BA7D7B9A70E0CE95F72525A111E60D03AE5F16CAE193635949` | Exact byte match |
| Death | `CBBEE82F59FB93FCC7D9D569B3F4664DE32E5BFA8A7D3E402CA502A7528A6ADD` | Exact byte match |

The foot-02 variance is a single 16-bit quantization result at the faded endpoint, not a different interval, gain, channel mix, body waveform, or audible fallback. No sample patch is prescribed; the checked-in runtime byte and its hash remain authoritative. Cross-correlation establishes the four movement source starts at 0.0, 1.5, 3.0, and 4.5 seconds with unity gain, while direct reconstruction establishes that no gain or normalization filter was used for idle, attack, or death.

The historical six-second death derivative is also reproduced exactly by replacing `-t 1.5` with `-t 6` and the final fade with `afade=t=out:st=5.96:d=0.04`; its SHA-256 is `9A30E7216C87A4783EF2089368DE224E4693DAE59BED838A0BA34C685EDA7674`.

## Closure boundary

This reconstruction closes the missing-source, source-interval, fade, gain/normalization, and normalized-command gaps. Static format, clipping, duration, and entity-hook timing checks pass. Auditory balance and live action synchronization are not claimed from numerical analysis, and the task does not launch Hearts of Iron IV.
