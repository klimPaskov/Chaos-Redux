# Event 039 Murder Mystery — Super-Event Audio Research Handoff

Status: three final sourced WAV candidates prepared on 2026-08-29. This handoff owns audio research, source preservation, conversion, and provenance only. It does not edit `sound/chaosx_sound.asset`, the music catalogue, event files, scripted effects, localisation, GUI, or gameplay wiring.

## Package summary

| Role | Suggested playback audio ID | Suggested base sound definition | Final WAV | Duration | Rights confidence |
|---|---:|---|---|---:|---|
| Assassin State public reveal | `108` | `chaosx_super_event_assassin_state_reveal_track` | `sound/039_murder_mystery/super_event_108_assassin_state_reveal.wav` | `110.000000 s` | High |
| World of Anarchy terminal activation | `109` | `chaosx_super_event_world_of_anarchy_activation_track` | `sound/039_murder_mystery/super_event_109_world_of_anarchy_activation.wav` | `110.000000 s` | High |
| Brotherhood defeat aftermath | `110` | `chaosx_super_event_brotherhood_defeat_aftermath_track` | `sound/039_murder_mystery/super_event_110_brotherhood_defeat_aftermath.wav` | `110.000000 s` | High for rights; medium for performer label |

The workspace currently contains the three prepared files numbered `108`, `109`, and `110`. No `108–110` entries were found in the checked `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html`, `docs/super_events/super_event_audio_packages.md`, or existing event-scoped audio folders at the time of this handoff. The catalogue already contains pending rows for `104` and `105`, and the filenames changed during concurrent workspace activity, so the parent must recheck all live numeric collisions immediately before registration.

## Rights and source policy

Composition and recording rights were checked separately for every candidate. The two Musopen source pages state that the recordings were released to the public domain worldwide, while the Commons Brahms II file is explicitly CC0 1.0. The composers’ underlying works are public domain. No candidate is generated audio, a test tone, a sound effect, a drone, or an unclear-license recording.

The original downloads are retained under `docs/assets/039_murder_mystery/source_audio/` until the parent promotes durable provenance into permanent documentation and closes the event package. Do not delete the source workspace while the package is under review or awaiting parent wiring.

## Cue 108 — Assassin State public reveal

- Suggested role: public reveal after the Evolution III split and war setup commit, when a murderer-led movement has become a territorial state and the conflict is openly organized.
- Track title: `Tragic Overture, Op. 81`.
- Composer: Johannes Brahms (1833–1897).
- Performer / recording source: Musopen Symphony, credited as Musopen Symphony Orchestra in the Commons Ogg variant.
- Source page: <https://commons.wikimedia.org/wiki/File:Brahms_-_Tragic_Overture,_Op._81_(Musopen_Symphony).flac>.
- Frozen source-page revision: <https://commons.wikimedia.org/w/index.php?title=File:Brahms_-_Tragic_Overture,_Op._81_(Musopen_Symphony).flac&oldid=1096311478>.
- Musopen source record: <https://musopen.org/music/2120-tragic-overture-op-81/>.
- Archive collection reference: <https://archive.org/details/MusopenCollectionAsFlac>.
- Download URL used: <https://upload.wikimedia.org/wikipedia/commons/c/c4/Brahms_-_Tragic_Overture%2C_Op._81_%28Musopen_Symphony%29.flac>.
- Recording rights: public-domain release by Musopen, stated by the Commons file page to apply worldwide, with a fallback permission to use for any purpose where a public-domain dedication is not legally possible.
- Composition rights: public domain; the Commons page identifies Brahms and notes his 1897 death and pre-1931 U.S. publication status.
- License confidence: High.
- Attribution: no legal attribution required by the stated public-domain release. Courtesy credit recommended: `Johannes Brahms, Tragic Overture, Op. 81; Musopen Symphony; source recording via Wikimedia Commons.`
- Source path: `docs/assets/039_murder_mystery/source_audio/brahms_tragic_overture_musopen.flac`.
- Source technical profile: FLAC, stereo, 48,000 Hz, `829.723333 s`, `134270870` bytes.
- Source SHA-1: `2C38126257D167B1265C13BBF8EDA81C838B3546`.
- Source SHA-256: `540F340E6433C622ED1F58598693B04A1F596E07550768B0BD119E979A7A345A`.
- Final path: `sound/039_murder_mystery/super_event_108_assassin_state_reveal.wav`.
- Final technical profile: WAV, PCM signed little-endian 16-bit, two-channel stereo, 44,100 Hz, `110.000000 s`, `19404212` bytes.
- Final SHA-256: `8B7C55E2E1F901575C95A92713AF5C19CA81BB03274E229298A20585B40E25BC`.
- Edit: retained source `00:00:00.000–00:01:50.000`; applied a `1.500 s` fade-in and a `6.000 s` fade-out beginning at `00:01:44.000`.
- Conversion: FFmpeg `N-123778-g3b55818764-20260331`; one-pass `loudnorm=I=-19:TP=-1.5:LRA=11:linear=true`, SoX-resampler mode with `precision=28`, 44.1 kHz output, stereo downmix/channel count, PCM16 WAV, and stripped container metadata followed by descriptive title/artist/comment metadata.
- Suitability: High. The hard-edged overture supplies a disciplined, conspiratorial-to-military turn that makes the new state feel organized and dangerous rather than merely shocking. The opening 110 seconds reaches the reveal quickly and ends before any triumphant resolution can soften the threat.

## Cue 109 — World of Anarchy terminal activation

- Suggested role: terminal activation after the World of Anarchy setup commits, when coordinated attacks on ordinary government leadership become a global command failure.
- Track title: `Symphony No. 6 in B minor, Op. 74 “Pathétique”, I. Adagio — Allegro non troppo`.
- Composer: Pyotr Ilyich Tchaikovsky (1840–1893).
- Performer / recording source: Musopen Symphony.
- Source page: <https://commons.wikimedia.org/wiki/File:Tchaikovsky_-_Symphony_No._6_in_B_minor,_Op._74_%27Path%C3%A9tique%27_-_I._Adagio_-_Allegro_non_troppo_%28Musopen_Symphony%29.flac>.
- Frozen source-page revision: <https://commons.wikimedia.org/w/index.php?title=File:Tchaikovsky_-_Symphony_No._6_in_B_minor,_Op._74_%27Path%C3%A9tique%27_-_I._Adagio_-_Allegro_non_troppo_(Musopen_Symphony).flac&oldid=963516983>.
- Musopen source record: <https://musopen.org/music/80-symphony-no-6-in-b-minor-pathetique-op-74/>.
- Archive collection reference: <https://archive.org/details/MusopenCollectionAsFlac>.
- Download URL used: <https://upload.wikimedia.org/wikipedia/commons/1/1a/Tchaikovsky_-_Symphony_No._6_in_B_minor%2C_Op._74_%27Path%C3%A9tique%27_-_I._Adagio_-_Allegro_non_troppo_%28Musopen_Symphony%29.flac>.
- Recording rights: public-domain release by Musopen, stated by the Commons file page to apply worldwide, with a fallback permission to use for any purpose where a public-domain dedication is not legally possible.
- Composition rights: public domain; the Commons page identifies Tchaikovsky and notes his 1893 death and pre-1931 U.S. publication status.
- License confidence: High.
- Attribution: no legal attribution required by the stated public-domain release. Courtesy credit recommended: `Pyotr Ilyich Tchaikovsky, Symphony No. 6 in B minor, Op. 74, I. Adagio — Allegro non troppo; Musopen Symphony; source recording via Wikimedia Commons.`
- Source path: `docs/assets/039_murder_mystery/source_audio/tchaikovsky_symphony_6_i_musopen.flac`.
- Source technical profile: FLAC, stereo, 48,000 Hz, `1051.132396 s`, `147106209` bytes.
- Source SHA-1: `DFAE546CACDB682477861249FAFE0D564B5C0F72`.
- Source SHA-256: `D00A50D86AD87E572BA586AD3F99F17DE3B93860E93D031B153EFF4A4494CA7F`.
- Final path: `sound/039_murder_mystery/super_event_109_world_of_anarchy_activation.wav`.
- Final technical profile: WAV, PCM signed little-endian 16-bit, two-channel stereo, 44,100 Hz, `110.000000 s`, `19404212` bytes.
- Final SHA-256: `F015E83C8EF4F2B5D848015522A8101DA0DDBABD05EDC5F313EE90EECC9BAA0B`.
- Edit: skipped the movement’s initial slow introduction and retained source `00:02:00.000–00:03:50.000`, entering the Allegro material as the terminal escalation is declared. Applied a `1.500 s` fade-in and a `6.000 s` fade-out beginning at `00:01:44.000` of the derivative.
- Conversion: FFmpeg `N-123778-g3b55818764-20260331`; one-pass `loudnorm=I=-19:TP=-1.5:LRA=11:linear=true`, SoX-resampler mode with `precision=28`, 44.1 kHz output, stereo channel count, PCM16 WAV, and stripped container metadata followed by descriptive title/artist/comment metadata.
- Suitability: High. Starting at the Allegro avoids a long prelude and places the cue directly in the movement’s mounting instability. Repeated figures and violent orchestral surges suggest command systems losing coherence across the world; the excerpt stops before resolution so the sound remains an activation of anarchy rather than a victory march.

## Cue 110 — Brotherhood defeat aftermath

- Suggested role: conditional defeat aftermath only after the Brotherhood reaches the Part 15 scale gate and the movement-defeat transaction commits; it must remain unused for small local defeats.
- Track title: `Symphony No. 2 in D major, Op. 73, II. Adagio non troppo`.
- Composer: Johannes Brahms (1833–1897).
- Performer / recording source: Commons summary credits Musopen Symphony Orchestra; embedded metadata identifies Czech National Orchestra. Treat the recording label as a source-page discrepancy and preserve both attributions in the permanent note.
- Source page: <https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._2_in_D_Major,_Op._73_-_II._Adagio_non_troppo.ogg>.
- Frozen source-page revision: <https://commons.wikimedia.org/w/index.php?title=File:Brahms,_Symphony_No._2_in_D_Major,_Op._73_-_II._Adagio_non_troppo.ogg&oldid=956416249>.
- Musopen source record: <http://www.musopen.org/music/piece/1565>.
- Download URL used: <https://upload.wikimedia.org/wikipedia/commons/7/77/Brahms%2C_Symphony_No._2_in_D_Major%2C_Op._73_-_II._Adagio_non_troppo.ogg>.
- Recording rights: CC0 1.0 Universal Public Domain Dedication on the Commons source page, allowing copying, modification, distribution, and performance without permission or conditions to the extent allowed by law.
- Composition rights: public domain; Brahms died in 1897 and the work is also represented as public-domain music in the linked source record.
- License confidence: High for legal use; Medium for exact performer label because of the source-page metadata discrepancy.
- Attribution: no legal attribution required under CC0. Courtesy credit recommended: `Johannes Brahms, Symphony No. 2 in D major, Op. 73, II. Adagio non troppo; Musopen Symphony Orchestra / Czech National Orchestra as credited on the source page; CC0 source via Wikimedia Commons.`
- Source path: `docs/assets/039_murder_mystery/source_audio/brahms_symphony_2_ii_musopen.ogg`.
- Source technical profile: Ogg Vorbis, stereo, 48,000 Hz, `556.272000 s`, `12073302` bytes.
- Source SHA-1: `CDE9CD789CAB48EA8D85C02A5481B015607D1176`.
- Source SHA-256: `2AB877E96E654AFB4495D2AAEDFA71388A2A64C1DDB15871D28A63C2FA62ADB6`.
- Final path: `sound/039_murder_mystery/super_event_110_brotherhood_defeat_aftermath.wav`.
- Final technical profile: WAV, PCM signed little-endian 16-bit, two-channel stereo, 44,100 Hz, `110.000000 s`, `19404212` bytes.
- Final SHA-256: `DA574770CDBCB8AFD390D823005560942452D806C230F72E0340D5D56BAE7E78`.
- Edit: retained source `00:00:00.000–00:01:50.000`; applied a `1.500 s` fade-in and a `6.000 s` fade-out beginning at `00:01:44.000`.
- Conversion: FFmpeg `N-123778-g3b55818764-20260331`; one-pass `loudnorm=I=-19:TP=-1.5:LRA=11:linear=true`, SoX-resampler mode with `precision=28`, 44.1 kHz output, stereo channel count, PCM16 WAV, and stripped container metadata followed by descriptive title/artist/comment metadata.
- Suitability: High. The restrained Adagio gives the aftermath dignity without clean triumph. Its lyrical continuation and gentle tension fit captured records, dismantled structures, guarded reconstruction, surviving cells, and a restoration that remains unstable.

## Parent wiring handoff

The parent should add one base `sound` definition per cue to `sound/chaosx_sound.asset` and six settings-aware `soundeffect` wrappers per cue. The wrapper names must be `chaosx_super_event_<audio_id>_sound_0_5`, `chaosx_super_event_<audio_id>_sound_1_0`, `chaosx_super_event_<audio_id>_sound_1_5`, `chaosx_super_event_<audio_id>_sound_2_0`, `chaosx_super_event_<audio_id>_sound_2_5`, and `chaosx_super_event_<audio_id>_sound_3_0`.

Each wrapper should follow the live pattern of volumes `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`, point to its cue’s base sound, and retain `max_audible = 1` and `max_audible_behaviour = fail`. The parent playback effect should set `global.current_super_event_audio_id` to `108`, `109`, or `110` and call `play_current_super_event_sound = yes`; do not bypass the settings-aware helper.

Suggested base sound mappings are `chaosx_super_event_assassin_state_reveal_track` → `039_murder_mystery/super_event_108_assassin_state_reveal.wav`, `chaosx_super_event_world_of_anarchy_activation_track` → `039_murder_mystery/super_event_109_world_of_anarchy_activation.wav`, and `chaosx_super_event_brotherhood_defeat_aftermath_track` → `039_murder_mystery/super_event_110_brotherhood_defeat_aftermath.wav`.

The parent-owned `music/chaosx_music_track_list.html` rows should preserve the exact title, composer, source/performer label, `01:50` duration, source URL, rights basis, and playback IDs above. The two Musopen entries can be marked public-domain recording plus public-domain composition. The Brahms II row should say CC0 recording plus public-domain composition and retain the performer-label uncertainty.

## Validation and blockers

- The three source downloads match the byte counts and SHA-1 checksums published by their Commons pages.
- The three final derivatives are distinct files with distinct SHA-256 hashes and no source file was modified.
- FFprobe verified WAV format, `pcm_s16le`, `44100` Hz, two channels, 16 bits per sample, and exactly `110.000000` seconds for every final cue.
- No licensing, download, or conversion blocker remains for these candidates.
- The only recorded uncertainty is the Brahms II source page’s conflicting performer labels; this does not weaken the explicit CC0 recording status.
- Parent integration remains required: sound definitions, settings wrappers, playback IDs, catalogue rows, slot wiring, trigger wiring, and final live validation were intentionally left outside this subagent’s scope.
