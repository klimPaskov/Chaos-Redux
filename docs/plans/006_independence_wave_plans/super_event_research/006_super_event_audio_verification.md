# Event 006 super-event audio verification

Research date: 2026-07-14

> Runtime reconciliation, 2026-07-16: this file preserves the original research
> and identifier audit. Audio 6002 has since been produced, registered, and
> wired through slot 24 and the settings-aware FIFO. Any statement below that
> calls 6002 absent or future work is superseded by
> `docs/super_events/006_independence_wave_super_event_research.md` and the final
> production manifest. Audio 6001 remains blocked and absent from runtime.

This note independently verifies the two accepted Event 006 super-event recordings. It records source identity, rights evidence, preserved-source state, timing, technical measurements, audio identifiers, and the exact production/wiring handoff. It does not change the accepted music choices, process final OGG/WAV derivatives, or wire gameplay.

## Outcome

| Audio ID | Super-event | Accepted recording | Rights verdict | Preserved source | Production state |
| ---: | --- | --- | --- | --- | --- |
| `6001` | The League of New States | Jeremiah Clarke, *A Trumpet Voluntary*, London Brass Players (1948 recording; 1949 release) | **Blocked.** The composition is public domain, but the exact recording is not cleared for United States redistribution. | Not downloaded | Do not process or wire |
| `6002` | Every Border a Casus Belli | Tchaikovsky, *1812 Overture*, United States Marine Band (2019) | **Verified on the stated U.S. federal-government public-domain basis.** | Downloaded and checksum-verified | Final OGG/WAV produced and asset wrappers wired |

The `6001` finding corrects the recording-rights conclusion in the accepted research without replacing the accepted selection. No substitute has been researched or proposed. The Event 006 two-track audio package therefore remains incomplete.

## References and precedents consulted

Before inspecting Chaos Redux audio surfaces, this pass consulted the offline wiki pages for Sound modding, Music modding, Event modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Decision modding, Idea modding, and AI modding. It also consulted vanilla `documentation/effects_documentation.md` for `play_song`, `scoped_play_song`, `sound_effect`, and `scoped_sound_effect`, plus the vanilla `events/MUN_Czechoslovakia.txt` scoped-song precedent and vanilla music asset/station definitions.

Current Chaos Redux precedent was taken from:

- `music/chaosx_super_event_music.asset`
- `music/chaosx_super_event_music.txt`
- `sound/chaosx_sound.asset`
- `common/scripted_effects/chaosx_settings_effects.txt`

At research time, the registered super-event audio surface topped out at ID
`56`; neither 6001 nor 6002 was registered. That collision finding established
both IDs as available. Audio 6002 is now registered. The unrelated
`priority = 6001` and `priority = 6002` values in `common/units/zombies.txt` are
not audio identifiers and do not collide.

## Audio ID 6001: The League of New States

### Recording identity

- Work: *A Trumpet Voluntary*
- Composer: Jeremiah Clarke (historically misattributed to Henry Purcell)
- Performers: London Brass Players; Harry Mortimer, trumpet; Reginald Foort, organ
- Conductor: George Weldon
- Recording: 8 November 1948, EMI Studio No. 1, Abbey Road, London
- First release: 1949
- Issue: Columbia DX 1536, matrix/order number CAX 10357
- Canonical source and rights page: <https://commons.wikimedia.org/wiki/File:CC0-CH_-_London_Brass_Players_-_A_Trumpet_Voluntary_-_Jeremiah_Clarke_-_Columbia-dx1536-cax10357.flac>
- Stable direct original: <https://upload.wikimedia.org/wikipedia/commons/7/75/CC0-CH_-_London_Brass_Players_-_A_Trumpet_Voluntary_-_Jeremiah_Clarke_-_Columbia-dx1536-cax10357.flac>
- Catalog corroboration: <https://pool.publicdomainproject.org/index.php/Columbia_DX_1536>
- Commons duration: `167.5730416667 s`
- Commons byte size: `53,445,574`
- Commons SHA-1: `6320e3d289d959acf0a871d1bea3cfa7b3d3b7fa`

### Rights evidence and blocker

The Clarke composition is public domain. The exact 1948/1949 sound recording is the blocker.

The Commons file's permission field contains `{{Cc-zero-project}} {{Pd-old-70}}`. `Cc-zero-project` identifies the Public Domain Project/Wikimedia cooperation; it is not the `{{Cc-zero}}` legal dedication. `Pd-old-70` supports the old composition/authorship, not a United States public-domain finding for the 1949 recording. The rendered Commons page also states that a United States public-domain tag must be supplied.

The Public Domain Project explains that its FLAC holdings are evaluated under Swiss copyright law: <https://pool.publicdomainproject.org/index.php/Copyright_term_(Copyright)>. Its project material says it shares recordings when they are out of copyright in Switzerland. No source reviewed shows that the project owned and waived the separate United States recording right or received a redistribution license from the record-rights holder.

The U.S. Copyright Office's Music Modernization Act FAQ explains that recordings first published from 1947 through 1956 receive a 95-year term plus a 15-year transition period: <https://www.copyright.gov/music-modernization/faq.html>. On the documented 1949 first release, the recording remains protected in the United States through 2059 and does not enter the U.S. public domain before 1 January 2060 absent a separate permission or dedication. Wikimedia Commons' United States rules state the same 110-year result for this publication band: <https://commons.wikimedia.org/wiki/Commons:Copyright_rules_by_territory/United_States>.

Accordingly:

- the source was deliberately **not downloaded**;
- no local SHA-256 exists;
- no loudness or stream analysis was performed;
- no final derivative or wrapper may be created from this recording;
- no Event 006 implementation should set `global.current_super_event_audio_id = 6001` until the recording right is cleared.

Unblocking requires either explicit permission/waiver covering redistribution of this exact recording in the United States, or user approval to reopen selection research. The latter would be a replacement, so it has not been attempted here.

### Accepted editorial plan, held pending clearance

- Accepted excerpt: `00:23.000-02:13.000`, exactly `110.000 s`
- Accepted fade-in: `1.500 s`
- Accepted fade-out: `2.000 s`, beginning at excerpt time `108.000 s`
- Playback: one-shot; no loop
- Reserved OGG path: `music/006_independence_wave/super_event_006_01_league_of_new_states.ogg`
- Reserved WAV mirror: `sound/006_independence_wave/super_event_006_01_league_of_new_states.wav`
- Reserved audio ID: `6001`

Courtesy attribution to carry if the recording is later cleared:

> Jeremiah Clarke, *A Trumpet Voluntary*; London Brass Players; Harry Mortimer, trumpet; Reginald Foort, organ; George Weldon, conductor; recorded 8 November 1948 and released on Columbia DX 1536 in 1949; source via the Public Domain Project and Wikimedia Commons; edited excerpt.

## Audio ID 6002: Every Border a Casus Belli

### Recording identity and rights

- Work: *1812 Overture, Op. 49*
- Composer: Pyotr Ilyich Tchaikovsky
- Transcription: Master Gunnery Sergeant Donald Patterson
- Performer: United States Marine Band
- Conductor: Colonel Jason K. Fettig
- Performance date: 26 May 2019
- Canonical source and rights page: <https://commons.wikimedia.org/wiki/File:1812_Overture_-_United_States_Marine_Band.opus>
- Stable direct original: <https://upload.wikimedia.org/wikipedia/commons/6/66/1812_Overture_-_United_States_Marine_Band.opus>

The exact Commons permission field separates the rights bases:

- composition: `{{PD-old-auto-expired|deathyear=1893}}`;
- transcription, performance, and recording: `{{PD-USGov-Military-Marines}}`.

The composition is public domain, and Commons identifies the Patterson transcription, Marine Band performance, and recording as works produced by United States Marines in official duties. Attribution is not required by those public-domain tags, but courtesy attribution should be retained. This is a U.S. federal public-domain basis rather than a worldwide CC0 dedication; that jurisdiction note should remain attached to the asset record. It matches the existing Chaos Redux treatment of identified U.S. federal band recordings.

Courtesy attribution:

> Pyotr Ilyich Tchaikovsky, *1812 Overture, Op. 49*; transcription by Master Gunnery Sergeant Donald Patterson; United States Marine Band; Colonel Jason K. Fettig, conductor; performed 26 May 2019; source via Wikimedia Commons; public-domain composition and U.S. federal-government transcription, performance, and recording; edited excerpt.

### Preserved source verification

- Local source: `docs/assets/006_independence_wave/super_events/audio/source/1812_Overture_-_United_States_Marine_Band.opus`
- Bytes: `12,999,461`
- Local SHA-1: `760e68775d9625542eaecfdc863efd7fe50853e4`
- Commons SHA-1: `760e68775d9625542eaecfdc863efd7fe50853e4`
- Local SHA-256: `93c141a2e5782385e8a9b53f5f622afcb604da6f361fe1ca2e160ea4bfe92d3d`
- Container/codec: Ogg Opus
- Source rate/layout: `48,000 Hz`, stereo
- FFprobe duration: `754.647500 s`
- Commons duration: `754.641 s`
- Approximate source bitrate: `137,806 bit/s`

The local SHA-1 exactly matches Commons. FFmpeg and FFprobe decode the source successfully.

### Exact excerpt and technical suitability

The accepted `10:45-12:35` notation is rounded to displayed whole seconds. The source actually ends at approximately `12:34.641`; starting at exactly `10:45.000` yields only about `109.641 s`. The accepted edit plan also says to retain the final 110 seconds. The precise production interval that satisfies that requirement is therefore:

- start: `00:10:44.641` (`644.641 s`)
- duration: `110.000 s`
- end: `00:12:34.641`
- fade-in: `1.500 s`
- fade-out: `2.000 s`, starting at excerpt time `108.000 s`
- playback: one-shot; no loop

An analysis-only FFmpeg pass using this exact interval and the accepted fades measured:

| Measurement | Value |
| --- | ---: |
| Integrated loudness | `-13.78 LUFS` |
| True peak | `-0.05 dBTP` |
| Loudness range | `16.30 LU` |
| Loudness threshold | `-24.91 LUFS` |

No silence interval of at least `0.25 s` at `-50 dBFS` was detected in the retained interval. The source is very close to full scale and must be attenuated, but its `16.3 LU` range should not be flattened. A two-pass linear loudness pass targeting `-18 LUFS` with a `-1.8 dBTP` ceiling and an LRA target of `20` preserves the dynamics. The local analysis pipeline produced `-18.0 LUFS`, `-4.3 dBTP`, and `16.2 LU` after resampling to `44.1 kHz`.

Recommended later production filter, using the verified source unchanged:

```text
atrim=start=644.641:duration=110,
asetpts=N/SR/TB,
afade=t=in:st=0:d=1.5,
afade=t=out:st=108:d=2,
loudnorm=I=-18:TP=-1.8:LRA=20:measured_I=-13.78:measured_TP=-0.05:measured_LRA=16.30:measured_thresh=-24.91:offset=-0.29:linear=true,
aresample=44100
```

The measured values are reproducible with the current preserved source and local FFmpeg. Re-run the first pass if the source or FFmpeg version changes. Validate the encoded OGG after production because Vorbis reconstruction can move true peak slightly.

Reserved final derivatives:

- OGG: `music/006_independence_wave/super_event_006_02_every_border_a_casus_belli.ogg`
- WAV mirror: `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav`
- Audio ID: `6002`
- OGG delivery: Ogg Vorbis, `44,100 Hz`, stereo
- WAV delivery: PCM signed 16-bit little-endian, `44,100 Hz`, stereo

The final derivatives were produced in the implementation pass from the
preserved source and exact accepted interval. Post-encode verification found:

- OGG: `109.992517 s`, Ogg Vorbis, 44.1 kHz stereo, `-18.05 LUFS`,
  `-3.81 dBTP`, `16.40 LU`, SHA-256
  `6B62C5AFA03E83C5BEB7D36E203E41BDC1EE51AEDD89269410A48BA0FCBC0DF0`;
- WAV: `109.992517 s`, PCM signed 16-bit little-endian, 44.1 kHz stereo,
  `-18.00 LUFS`, `-4.27 dBTP`, `16.30 LU`, SHA-256
  `3A7C58C94016EDA80842E328DEBC3D00B2D1755085F0C87F580AAAB3B4E0BC08`.

The full production record is in
`docs/assets/006_independence_wave/super_events/audio/production_manifest.md`.

## Implemented 6002 wiring record

The current settings helper is already dynamic. `play_dynamic_super_event_music` builds `chaosx_super_event_[SUPER_EVENT_ID]_[VOLUME_SUFFIX]`, and `play_dynamic_super_event_sound` builds `chaosx_super_event_[SUPER_EVENT_ID]_sound_[VOLUME_SUFFIX]`. No helper rewrite is required for IDs `6001` or `6002`.

For each cleared audio ID, register the six established suffixes and volumes:

| Suffix | Asset/wrapper volume |
| --- | ---: |
| `0_5` | `0.67` |
| `1_0` | `1.33` |
| `1_5` | `2.00` |
| `2_0` | `2.67` |
| `2_5` | `3.33` |
| `3_0` | `4.00` |

For the verified cue, the required identifiers are:

- music assets: `chaosx_super_event_6002_0_5` through `chaosx_super_event_6002_3_0`;
- representative station row: `chaosx_super_event_6002_1_5`, with `chance = { factor = 0 }`;
- raw sound name: `chaosx_super_event_independence_wave_every_border_a_casus_belli_track`;
- sound wrappers: `chaosx_super_event_6002_sound_0_5` through `chaosx_super_event_6002_sound_3_0`;
- each sound wrapper should retain `max_audible = 1` and `max_audible_behaviour = fail` and should not enable looping.

The implemented dangerous-milestone publisher submits audio ID 6002 and slot 24
to the settings-aware FIFO; its dispatcher assigns the ID immediately before
the existing playback call. Do not register or fire the parallel 6001 audio
identifiers while its recording license is blocked.

## Remaining uncertainties and blockers

1. Audio ID `6001` has no verified United States redistribution right for the accepted 1949 recording. This is a material blocker, not an attribution omission.
2. Audio ID `6002` rests on the U.S. federal public-domain basis stated by Commons and used by current repository precedent; it is not accompanied by a worldwide CC0 waiver.
3. The `6002` gameplay threshold submits the registered ID and slot 24 to the
   settings-aware FIFO; its dispatcher assigns the ID immediately before the
   playback call.
4. No fallback, replacement, or substitute recording was used.
