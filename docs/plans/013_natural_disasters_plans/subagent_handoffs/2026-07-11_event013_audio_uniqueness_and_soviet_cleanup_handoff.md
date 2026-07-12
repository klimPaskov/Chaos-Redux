# Event 013 audio uniqueness and Soviet Collapse cleanup handoff

Closure note, 2026-07-12: the parent implementation replaced Event 013 audio ID 37 at its stable paths, updated its source/rights/catalogue records, and removed unused Soviet Collapse IDs 16 and 19-27 from media, registration, localisation, and catalogue surfaces. Soviet IDs 14, 15, 17, and 18 remain live. The authoritative final production record is `docs/super_events/013_natural_disasters_super_event_audio_production.md`.

Date: 2026-07-11

Subagent: `chaosx_super_event_audio_researcher`

Skill used: `chaos-redux-super-events`

## Outcome

- Event 013 audio ID 37 was an actual recording-level duplicate of Soviet Collapse audio ID 14. The collision was present in both music and sound encodings.
- ID 37 now uses a legally reusable, role-fitting replacement at the same stable OGG and WAV paths. The source is preserved and its repository checksum matches the checksum published by Wikimedia Commons.
- Event 013 IDs 38–42 do not reuse any other registered super-event recording.
- Event 013 IDs 37–42 have unique identifiers and registered paths. No registry identifier or cross-ID path collision was found.
- Soviet Collapse IDs 16 and 19–27 are strong unused-audio deletion candidates. ID 17 is a conditional candidate because its setter helper exists but has no caller in the parent-authorized inspection roots. IDs 14, 15, and 18 should be retained.
- No Soviet file was deleted and no registry, scripted-localisation, event, or localisation wiring was edited.

## Event 013 comparison method

The registered corpus contained 55 audio IDs and 110 event-scoped files: 55 OGG files plus 55 WAV files. FFmpeg decoded every file to raw Chromaprint subfingerprints. Each Event 013 representative was compared against all 108 cross-ID encodings at every possible time offset with at least 160 subfingerprints, approximately 20 seconds, of overlap. Container SHA-256, raw-Chromaprint SHA-256, duration, codec, sample rate, and channels were also checked.

Verified same-recording controls scored `0.939946–0.995107`. Before replacement, the nonduplicate ceiling for Event 013 was `0.636282`. The old ID 37/14 pair scored about `0.994` over the entire ID 37 cue at zero offset, which is decisive recording reuse rather than a shared composition or filename coincidence.

## Original ID 37 collision evidence

The superseded ID 37 OGG had:

- path: `music/013_natural_disasters/super_event_37_earth_rupture.ogg`
- OGG SHA-256: `E294D65B251017897B6A98D31FDF8C850F22614A785D9064D8BF073309DA438F`
- raw-Chromaprint SHA-256: `A434009B68F31299267EFEF38A9C06075F2E56F00A3E798623B27357145F8FFA`
- duration: `118.000` seconds

Full-cue comparisons:

| Comparison | Similarity | Offset | Overlap |
| --- | ---: | ---: | ---: |
| Old ID 37 OGG vs ID 14 OGG | `0.993730` | `0` | `932/932` ID 37 frames |
| Old ID 37 OGG vs ID 14 WAV | `0.994434` | `0` | `932/932` ID 37 frames |
| Old ID 37 OGG vs preserved Event 013 *Egmont* source | `0.994937` | aligned opening | full final cue |
| ID 14 OGG vs preserved Event 013 *Egmont* source | `0.993743` | aligned opening | full final cue |
| ID 14 OGG vs preserved Event 013 *Coriolan* source | `0.575309` | best offset | nonmatch |

The HTML music table labels ID 14 as Beethoven's *Coriolan Overture* performed by the Fulda Symphonic Orchestra under the EFF Open Audio License. Its actual file is the same *Egmont Overture* / Musopen recording formerly used by ID 37. The parent should correct the ID 14 catalogue attribution even though ID 14 itself remains in use.

Event 013 ID 41 is not part of the collision despite also using *Coriolan Overture*. ID 41 matches its preserved Czech National Symphony Orchestra / Musopen *Coriolan* source at `0.995026`, while ID 41 versus ID 14 scores only `0.588452` for OGG and `0.587911` for WAV.

## ID 37 replacement

### Selection and fit

- title: *Peer Gynt Suite No. 1*, Op. 46, IV. *In the Hall of the Mountain King*
- composer: Edvard Grieg
- performer / recording source: Czech National Symphony Orchestra, published as Musopen Symphony
- recording date: 2012
- source duration: `154.091021` seconds
- source page: <https://commons.wikimedia.org/wiki/File%3AGrieg_-_Peer_Gynt_Suite_No._1%2C_Op._46_-_IV._In_the_Hall_of_the_Mountain_King_%28Musopen_Symphony%29.flac>
- direct preserved original: <https://upload.wikimedia.org/wikipedia/commons/8/84/Grieg_-_Peer_Gynt_Suite_No._1%2C_Op._46_-_IV._In_the_Hall_of_the_Mountain_King_%28Musopen_Symphony%29.flac>
- upstream work page: <https://musopen.org/music/777-peer-gynt-suite-no-1-op-46/>

The cue begins with controlled low-orchestral motion, accumulates pressure, and reaches a violent full-orchestra climax. The resulting arc fits a rupture propagating through foundations and coastlines while remaining structured music rather than a drone, sound effect, oscillator cue, or stinger.

### Rights and provenance

- rights checked: 2026-07-11
- composition: public domain; Grieg died in 1907 and Commons records pre-1931 U.S. publication status
- recording: released into the public domain worldwide by Musopen; where waiver is unavailable, Musopen grants unrestricted use for any purpose
- license confidence: high
- attribution requirement: none stated; courtesy credit is still appropriate
- courtesy attribution: `Edvard Grieg, Peer Gynt Suite No. 1, IV. In the Hall of the Mountain King; Czech National Symphony Orchestra / Musopen Symphony; public-domain source via Wikimedia Commons.`
- preserved source path: `docs/assets/013_natural_disasters/audio_source/earth_rupture_grieg_mountain_king_source.flac`
- source SHA-1: `7D34C97620149EFF83BC14A1E838EF5D8E66746B`
- Commons-published SHA-1: `7d34c97620149eff83bc14a1e838ef5d8e66746b`, exact match
- source SHA-256: `1C1BE6B3E0042EE031CEE42A8D151B04C78BFCCF3126C4DE6271E7B2FDCB6937`

### Edit and conversion

- excerpt: source `00:36.091–02:34.091`
- final duration: `118.000` seconds
- fade: six-second fade-out from final `00:06`
- normalization: two-pass EBU R128 loudness normalization; post-encode measurement `-18.1 LUFS`, `-1.63 dBTP`
- source format: 48 kHz stereo FLAC
- final music format: 44.1 kHz stereo Vorbis OGG
- final sound format: 44.1 kHz stereo signed-16-bit PCM WAV decoded from the final OGG, ensuring both playback modes render the same mastered signal
- final OGG path: `music/013_natural_disasters/super_event_37_earth_rupture.ogg`
- final OGG SHA-256: `189AF2FD28DEFD122CDF80CA0CCBF34317268148B3379C0BEE382285F17346A8`
- final WAV path: `sound/013_natural_disasters/super_event_37_earth_rupture.wav`
- final WAV SHA-256: `1D527BAD4BC93D77AC4265D4791D3B8ADABBA88C38C745F9A7623D554B6B7CFF`
- canonical decoded 44.1 kHz stereo s16 PCM SHA-256 for both files: `0657C8A2E6897428E44C0423D2BEF0B3B4BDE15CB74BCC2C17B06F9AC0B911FE`
- raw-Chromaprint SHA-256 for both files: `60948D34D558E23FF83846B94DFBF63AB307444667639D186E9A4B5FDB459298`

The replacement matches its preserved source at `0.923771` over 931 aligned Chromaprint frames; `99.14%` of aligned frames differ by no more than six bits. Its nearest non-Event-013 registered file scores only `0.589419`, so no replacement collision remains.

## Event 013 final uniqueness table

| Audio ID | Final OGG SHA-256 | Raw-Chromaprint SHA-256 | Actual duration | Nearest non-Event-013 score | Verdict |
| ---: | --- | --- | ---: | ---: | --- |
| 37 | `189AF2FD28DEFD122CDF80CA0CCBF34317268148B3379C0BEE382285F17346A8` | `60948D34D558E23FF83846B94DFBF63AB307444667639D186E9A4B5FDB459298` | `118 s` | `0.589419` | unique replacement |
| 38 | `3744B32D01E4F6DA4660ECCC556A35FD871855CDA28F4CF0C84AB00C01883A84` | `BE4B47ECF141E9623EFF89E41FD06A8F9884557C3DEED196A7CF7A843DCAC3C7` | `115 s` | `0.604360` | unique |
| 39 | `560106A9D5490EBD11903BD420A2988E923B83033E168F6639F930D175A10D4B` | `10D6C24F630CB24A2ABE845DC1924A99C23DCFF68685B5F571DA4B2FE6E16262` | `118 s` | `0.603588` | unique |
| 40 | `4E6C3AFAC403CD7AA2B6257CD83F0AD85AA951FEA2D6A3A08C0A1C3B7D0DC289` | `45CFB445257B40A061D629B6C1A0BB1C1BF9142928A4AF12E9B86866F20189B2` | `115 s` | `0.579044` | unique |
| 41 | `87F058595719F13F52799AFBC3C6410E807784AD96B1D52FEB684A5DB7E45939` | `4B5CB5E37CB6C9E0A36AF5F4BBB40B223D6F9D25D4B633A9B9DD61926F5937F4` | `110 s` | `0.636282` | unique |
| 42 | `E3077C188F5F06F563311CFC7C4B2DF21A55729D7E42A5B103AD8E1AEB88228F` | `11E79EF57098B2159522F01E9B30B88230F021F8F09F19C23663A05B7B2C0804` | `115 s` | `0.608631` | unique |

For each Event 013 ID, six unique music-volume definitions point only to its OGG, one representative music-station entry exists, one unique raw sound wrapper points to its WAV, and six unique sound-effect-volume definitions exist. No duplicate music definition name, sound-effect definition name, sound-wrapper name, or cross-ID Event 013 OGG path was found.

## Event 013 parent documentation changes still required

No registry path or identifier change is needed because ID 37 retained its stable filenames and wrapper IDs. The parent should update `music/chaosx_music_track_list.html` as follows:

- ID 37 row around lines 485–493:
  - track: `Peer Gynt Suite No. 1, Op. 46: IV. In the Hall of the Mountain King`
  - composer: `Edvard Grieg`
  - performer: `Czech National Symphony Orchestra / Musopen Symphony; source via Wikimedia Commons`
  - duration: `01:58`
  - rights: `public-domain composition and worldwide public-domain recording dedication`
- ID 14 row around lines 255–264:
  - correct the false *Coriolan* / Fulda / EFF attribution to the actual *Egmont Overture*, Czech National Symphony Orchestra / Musopen recording
  - retain the approximately `02:00` duration
  - use the public-domain/CC0 recording basis documented by the Event 013 *Egmont* source record
- Correct the remaining Event 013 duration cells, which currently all say `01:50`:
  - ID 38: `01:55`
  - ID 39: `01:58`
  - ID 40: `01:55`
  - ID 41: `01:50`
  - ID 42: `01:55`

The Event 013 manifest and audio-research note were updated in this handoff. The superseded source remains preserved as `docs/assets/013_natural_disasters/audio_source/earth_rupture_egmont_source.flac` for audit history.

## Soviet Collapse runtime-use audit

All IDs 14–27 have OGG and WAV files, full music and sound registration, a representative station entry, music-label localisation, and an HTML catalogue row. Registration alone cannot play a track. `soviet_collapse_emit_super_event` assigns `global.current_super_event_audio_id` from `soviet_collapse_super_event_id`, and the settings helper only plays the assigned ID. A track is reachable only when a live call chain first assigns its ID and invokes the emitter.

| Audio ID | Registered | Referenced state | Runtime conclusion |
| ---: | --- | --- | --- |
| 14 | OGG, WAV, music/sound variants, station, labels, catalogue | Union Unmade setter at `common/scripted_effects/005_soviet_collapse_effects.txt:2689–2706`; invoked by normal evaluation and the triggerable scenario | keep |
| 15 | fully registered | Black Banner setter at `:3727–3732`; called by `soviet_collapse_complete_black_banner_endgame` at `:18804` | keep conservatively |
| 16 | fully registered; presentation localisation/selectors remain | no setter or emitter call | strong deletion candidate |
| 17 | fully registered; presentation localisation/selectors remain | setter helper at `:3736–3741`, but zero callers in the permitted roots | conditional deletion candidate; exact-name check outside the permitted roots required before deletion |
| 18 | fully registered | Every Port setter at `:3745–3750`; called by `soviet_collapse_complete_port_council_endgame` at `:18779` | keep conservatively |
| 19–22 | fully registered; presentation localisation/selectors remain | gameplay equivalents use ordinary news events `.140–.143` at `:3754–3783`; no audio setter | strong deletion candidates |
| 23 | fully registered | registry, catalogue, and music-label localisation only; no super-event selectors or event text | strong deletion candidate |
| 24 | fully registered | gameplay uses ordinary news event `.36` at `:3786–3791`; no audio setter or super-event selectors | strong deletion candidate |
| 25–26 | fully registered | league formation uses ordinary news events `.30` and `.31` around `:12034` and `:12049`; no audio setter or super-event selectors | strong deletion candidates |
| 27 | fully registered | registry, catalogue, and music-label localisation only; no super-event selectors or event text | strong deletion candidate |

All 28 Soviet media files are distinct by SHA-256 and are 44.1 kHz stereo. The deletion verdict is based on script reachability, not filenames or duplicate media.

## Strong Soviet media deletion set

Delete both the OGG under `music/005_soviet_collapse/` and the WAV under `sound/005_soviet_collapse/` for each stem:

- `super_event_16_northern_signals_break`
- `super_event_19_map_larger_than_union`
- `super_event_20_steppe_beyond_history`
- `super_event_21_corridors_decide`
- `super_event_22_bread_state`
- `super_event_23_league_of_equal_republics`
- `super_event_24_steppe_federation`
- `super_event_25_baltic_league`
- `super_event_26_caucasus_league`
- `super_event_27_eastern_buffer_coalition`

This is 20 files totaling `140,350,169` bytes, approximately `133.85 MiB`.

## Conditional Soviet media deletion set

If a final exact-name scan of national focuses, decisions, and any other roots outside this subagent's inspection boundary confirms that the ID 17 helper has no caller, also delete:

- `music/005_soviet_collapse/super_event_17_workshops_choose_councils.ogg`
- `sound/005_soviet_collapse/super_event_17_workshops_choose_councils.wav`

Including ID 17 raises the cleanup to 22 files and approximately `150.27 MiB`.

## Registry, labels, and catalogue cleanup for the strong set

Identifiers are the source of truth; line numbers are included as navigation aids and may shift with concurrent work.

- `music/chaosx_super_event_music.asset`
  - remove all six volume blocks for ID 16, current lines 483–517
  - remove all six volume blocks for each ID 19–27, current lines 591–913
- `music/chaosx_super_event_music.txt`
  - remove the ID 16 representative entry, current lines 135–141
  - remove representative entries for IDs 19–27, current lines 159–229
- `sound/chaosx_sound.asset`
  - remove category registrations for ID 16 and IDs 19–27, current lines 98–103 and 116–169
  - remove raw sound definitions for ID 16 and IDs 19–27, current lines 482–485 and 497–540
  - remove six volume sound-effect wrappers per ID for ID 16 and IDs 19–27, current lines 1286–1332 and 1430–1860
- `localisation/english/chaosx_music_l_english.yml`
  - remove the six music-label keys for ID 16 and each ID 19–27, current lines 98–103 and 116–169
- `music/chaosx_music_track_list.html`
  - remove the ID 16 row, current lines 275–284
  - remove rows for IDs 19–27, current lines 305–394

If ID 17 is confirmed unused, additionally remove:

- music asset blocks: current lines 519–553
- music station entry: current lines 143–149
- sound category entries: current lines 104–109
- raw sound definition: current lines 487–490
- sound-effect wrappers: current lines 1334–1380
- music-label localisation: current lines 104–109
- HTML catalogue row: current lines 285–294

No Soviet-specific per-ID audio rows exist under `docs/super_events`. `docs/events/005_soviet_collapse.md` contains only generic asset-directory references and needs no audio-row deletion.

## Optional dormant presentation cleanup

If the parent removes the unused super-event presentations themselves rather than only their audio packages, IDs 16, 17, and 19–22 leave dormant presentation text and selectors:

- `localisation/english/005_soviet_collapse_l_english.yml`: current lines 1884–1891 and 1896–1911
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
  - image selectors: current lines 112–123 and 130–153
  - titles: current lines 458–469 and 476–499
  - quotes: current lines 695–706 and 713–736
  - buttons: current lines 932–943 and 950–973
  - descriptions: current lines 1169–1180 and 1187–1210

IDs 23–27 have no equivalent super-event presentation selectors or `.t/.d/.a/.q` localisation. Interface/GFX cleanup was outside this audit boundary.

## Files changed by this subagent

- `docs/assets/013_natural_disasters/audio_source/earth_rupture_grieg_mountain_king_source.flac`
- `music/013_natural_disasters/super_event_37_earth_rupture.ogg`
- `sound/013_natural_disasters/super_event_37_earth_rupture.wav`
- `docs/assets/013_natural_disasters/audio_manifest.md`
- `docs/super_events/013_natural_disasters_super_event_audio_research.md`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-11_event013_audio_uniqueness_and_soviet_cleanup_handoff.md`

No `.asset`, music-station `.txt`, scripted localisation, event, gameplay localisation, GUI/GFX, spreadsheet, or Soviet media file was edited or deleted.
