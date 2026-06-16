# Event 012 Africa Super-Event Audio Manifest

Updated: `2026-06-16`

Scope: second-pass packaged audio only. This manifest records the preserved source downloads, final `44.1 kHz` `.ogg` exports, licensing position, conversion commands, and role status for the finalized package.

## Finalized roles

### `africa_is_one_unification`

- Status: finalized
- Suggested sound definition id: `super_event_africa_unification`
- Suggested super-event use: Africa unification / Charter League reveal
- Title: `South African national anthem`
- Creator / composer: Enoch Sontonga and M. L. de Villiers; arranged by M. Kumhalo and Jeanne Zaidel-Rudolph
- Performer / recording source: United States Navy Band
- Source URL: `https://commons.wikimedia.org/wiki/File:South_African_national_anthem.oga`
- License: U.S. federal government public domain / free of known restrictions on Commons
- License confidence: high
- Duration:
  - source: `122.618776s`
  - final: `120.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/south_african_national_anthem.oga`
- Source SHA-256: `826879d15e57d42b521d37abcaccdb45126cdbd40c308de8f19aadb728d3cfdf`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
- Final SHA-256: `2a6c6fec4d8792cfbd21df247d188923648d96199fe4f82458155f85070a4908`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/south_african_national_anthem.oga -af "atrim=start=0:duration=120,asetpts=N/SR/TB,afade=t=out:st=117:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg
```

- Editing and conversion steps: kept the opening intact, trimmed to two minutes, applied a `3s` fade-out, re-encoded to Vorbis at `44.1 kHz`
- Suitability: ceremonial, continental, and recognizably African without sounding apocalyptic
- Uncertainty: national-anthem framing is overtly state-formal; if the parent wants a less state-anthemy unifier tone, this role should be reconsidered later rather than silently reused elsewhere

### `africa_scramble_reaction`

- Status: finalized
- Suggested sound definition id: `super_event_africa_scramble`
- Suggested super-event use: Scramble for Africa reaction / imperial crisis escalation
- Title: `Mars, the Bringer of War` from *The Planets*
- Creator / composer: Gustav Holst
- Performer / recording source: United States Air Force Band, transcription by Merlin Patterson, edited by Capt. Lang and MSgt Aldo Forte
- Source URL: `https://commons.wikimedia.org/wiki/File:Holst-_mars.ogg`
- License: U.S. federal government performance; composition public domain
- License confidence: high
- Duration:
  - source: `477.544490s`
  - final: `118.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/holst_mars.ogg`
- Source SHA-256: `36ea4f5898e5f0b6cfffb88bbaeee736575bff12ed57e83d1be9b536cb0f35a0`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_scramble.ogg`
- Final SHA-256: `9a2467f64db693215b1eb5f087ccb49f87db602d73155f929cc06c3e07eaee9f`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/holst_mars.ogg -af "atrim=start=0.64:duration=118,asetpts=N/SR/TB,afade=t=out:st=115:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_scramble.ogg
```

- Editing and conversion steps: removed the opening silence, kept the immediate martial drive, trimmed to `118s`, applied a `3s` fade-out, preserved stereo, re-encoded at `44.1 kHz`
- Suitability: this is the strongest cleanly licensed panic-and-war cue in the package
- Uncertainty: none beyond the normal dramatic bluntness of a very famous cue

### `africa_old_seats_reveal`

- Status: finalized
- Suggested sound definition id: `super_event_africa_old_seats`
- Suggested super-event use: Authority Atlas / Archive of Old Seats reveal
- Title: `First Suite in E-flat for Military Band, III. March`
- Creator / composer: Gustav Holst
- Performer / recording source: United States Marine Band from *The Bicentennial Collection, Disc 10: Guest Conductors*
- Source URL: `https://commons.wikimedia.org/wiki/File:Holst_First_Suite_March.ogg`
- License: public domain on Commons
- License confidence: high
- Duration:
  - source: `172.571859s`
  - final: `112.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/holst_first_suite_march.ogg`
- Source SHA-256: `cbd13dbd93ffd47fc2ee0e6d5a1000fdb485f6eef6bc34cf124d8d9607d0a3a2`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_old_seats.ogg`
- Final SHA-256: `8538dec6431b868eecd7ed9b9ea793101a0fa8d3f2942eca017dddd687fbab96`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/holst_first_suite_march.ogg -af "atrim=start=0.41:duration=112,asetpts=N/SR/TB,afade=t=out:st=109:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_old_seats.ogg
```

- Editing and conversion steps: removed the opening silence, trimmed to the first `112s`, added a `3s` fade-out, re-encoded to `44.1 kHz`
- Suitability: bureaucratic, martial, and archival without sounding like a generic triumph cue
- Uncertainty: none significant

### `africa_counterfeit_crowns`

- Status: finalized
- Suggested sound definition id: `super_event_africa_counterfeit_crowns`
- Suggested super-event use: counterfeit crowns / false-regalia exposure / sponsor-adjacent pressure role
- Title: `Egmont Overture, Op. 84`
- Creator / composer: Ludwig van Beethoven
- Performer / recording source: Czech National Symphony Orchestra via Musopen upload mirrored on Commons
- Source URL: `https://commons.wikimedia.org/wiki/File:Beethoven_EgmontOvertureOp.84_LudwigVanBeethoven-EgmontOvertureOp.84.ogg`
- License: `CC0 1.0 Universal Public Domain Dedication`
- License confidence: high
- Duration:
  - source: `540.896688s`
  - final: `118.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/beethoven_egmont_overture_op84.ogg`
- Source SHA-256: `2007b57e8ab1dbe6c9df4d3c91d3de185457ad70cbeb9b4c2864e5161a64c3ae`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_counterfeit_crowns.ogg`
- Final SHA-256: `2bc75407d8aaf1519216d4c91ca337ba9b8da19e3c6145b3cc90865139370e1d`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/beethoven_egmont_overture_op84.ogg -af "atrim=start=0:duration=118,asetpts=N/SR/TB,afade=t=out:st=115:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_counterfeit_crowns.ogg
```

- Editing and conversion steps: kept the opening confrontation, trimmed to `118s`, applied a `3s` fade-out, resampled from `48 kHz` to `44.1 kHz`
- Suitability: authoritative and accusatory, with enough tension for false-sovereignty exposure or heavily pressured sponsor-state framing
- Uncertainty: this package is locked to `counterfeit_crowns` for uniqueness; do not reuse it for a separate `continent_sponsor` final without explicit approval

### `africa_world_is_one_terminal`

- Status: finalized
- Suggested sound definition id: `super_event_africa_world_is_one`
- Suggested super-event use: terminal World Is One branch
- Title: `Funeral March in C minor, Op. posth. 72 no. 2`
- Creator / composer: Frédéric Chopin
- Performer / recording source: Aya Higuchi via Musopen upload mirrored on Commons
- Source URL: `https://commons.wikimedia.org/wiki/File:Funeral_March_Chopin_Op_72_2.ogg`
- License: `CC0 1.0 Universal Public Domain Dedication`
- License confidence: high
- Duration:
  - source: `351.768000s`
  - final: `120.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/chopin_funeral_march_op72_no2.ogg`
- Source SHA-256: `2e3d83683bbc12e12459a8ded6afcdb4c3553de8c987b9a3fba79f8b9fc36936`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one.ogg`
- Final SHA-256: `655559b6f03e5866090b725be466a26ffa3211730c9dd82e84e72858a873c7f0`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/chopin_funeral_march_op72_no2.ogg -af "atrim=start=0.81:duration=120,asetpts=N/SR/TB,afade=t=out:st=116:d=4" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one.ogg
```

- Editing and conversion steps: removed the opening silence, trimmed to `120s`, applied a `4s` fade-out, resampled from `48 kHz` to `44.1 kHz`
- Suitability: grave, terminal, and legible in-game without the dead-air problems of the rejected Beethoven 7 cello file
- Uncertainty: world-end scale is carried more by finality than by massed orchestral shock; if the parent later wants a more cosmic terminal cue, replace rather than repurpose another packaged role

### `africa_continent_sponsor`

- Status: finalized
- Suggested sound definition id: `super_event_africa_continent_sponsor`
- Suggested super-event use: continent sponsor / Africa as continental-union precedent
- Title: `The Thunderer`
- Creator / composer: John Philip Sousa
- Performer / recording source: United States Marine Band, 2017 recording from *The Complete Marches of John Philip Sousa*
- Source URL: `https://commons.wikimedia.org/wiki/File:Sousa%27s_%22The_Thunderer%22_-_United_States_Marine_Band_(2017).ogg`
- License: public domain composition and U.S. federal government public domain performance/recording on Commons
- License confidence: high
- Duration:
  - source: `168.387083s`
  - final: `120.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/sousa_the_thunderer_us_marine_band_2017.ogg`
- Source SHA-256: `9a67bcf71a67705d3a5f98b24783e2bdb2a3f2534cd981d18f0f636658146f23`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_continent_sponsor.ogg`
- Final SHA-256: `77ee7af6039b942348e0c2d92a9ffa68c90cd0e2351d222660f8b4e48c63fcfe`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/sousa_the_thunderer_us_marine_band_2017.ogg -af "atrim=start=0:duration=120,asetpts=N/SR/TB,afade=t=out:st=117:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_continent_sponsor.ogg
```

- Editing and conversion steps: kept the energetic opening march, trimmed to `120s`, applied a `3s` fade-out, preserved stereo, re-encoded at `44.1 kHz`
- Suitability: assertive and export-facing without sounding like a world-end cue; the public-domain military-band recording fits a doctrine being carried abroad
- Uncertainty: the cue is not African-sourced. It is used for the sponsor/export role because the licensing and musical role fit are stronger than the rejected cello candidate.

### `africa_rsa_allies_peace`

- Status: finalized
- Suggested sound definition id: `super_event_africa_rsa_allies_peace`
- Suggested super-event use: RSA continental victory / Allied peace / exhausted settlement aftermath
- Title: `Intermezzo from Goyescas`
- Creator / composer: Enrique Granados
- Performer / recording source: United States Marine Band, transcription by John R. Bourgeois, from *Director's Choice*
- Source URL: `https://commons.wikimedia.org/wiki/File:Intermezzo_from_Goyescas_-_U.S._Marine_Band.ogg`
- License: public domain composition and U.S. Marine Band public-domain performance/recording on Commons
- License confidence: high
- Duration:
  - source: `327.079184s`
  - final: `116.000000s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/granados_intermezzo_goyescas_us_marine_band.ogg`
- Source SHA-256: `42bc530bea5429bc839374a3a95a3acd43c882de3f0b96c646a84cd870d6cf7a`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg`
- Final SHA-256: `a77c48ad39590de67caf671e23c6bcf19778aaa045954332020436b4f7888127`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/granados_intermezzo_goyescas_us_marine_band.ogg -af "atrim=start=0:duration=116,asetpts=N/SR/TB,afade=t=out:st=113:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg
```

- Editing and conversion steps: kept the opening intact, trimmed to the first `116s`, applied a `3s` fade-out, preserved stereo, and re-encoded to `44.1 kHz` Vorbis
- Suitability: reflective without sounding terminal, formal without jubilation, and strong for an administrative peace forced by one side's exhausted victory in a continental civil rupture
- Uncertainty: none significant; this is cleaner legally and tonally than the evaluated `Nimrod` alternative

### `africa_dynamic_cross_continent_union`

- Status: finalized
- Suggested sound definition id: `super_event_africa_dynamic_cross_continent_union`
- Suggested super-event use: Africa-led cross-continent federation / congress / chartered union short of terminal world union
- Title: `Grand March from La reine de Saba`
- Creator / composer: Charles-Francois Gounod
- Performer / recording source: U.S. Marine Band under LtCol William F. Santelmann, from *From Fife and Drum: Marine Band Recordings 1890-1988*
- Source URL: `https://commons.wikimedia.org/wiki/File:Charles_Gounod_-_U.S._Marine_Band_-_Grand_March_from_La_reine_de_Saba.ogg`
- License: public domain composition and U.S. Marine Band public-domain performance/recording on Commons
- License confidence: high
- Duration:
  - source: `305.946122s`
  - final: `118.006349s`
- Attribution text if required: none required
- Original downloaded source path: `docs/assets/012_africa/super_events/audio/source/gounod_grand_march_la_reine_de_saba_us_marine_band.ogg`
- Source SHA-256: `9d7b2df0de474465e530e53c7744f35de5e43cb09ac70b8fbcc633149714980c`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg`
- Final SHA-256: `af56784510a2c190f2c84542b7dfba2fcbfb4d8d7428f83b62694208c7b53d2a`
- Conversion command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/gounod_grand_march_la_reine_de_saba_us_marine_band.ogg -af "atrim=start=0.564:duration=118,asetpts=N/SR/TB,afade=t=out:st=115:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg
```

- Editing and conversion steps: removed `0.564s` of opening silence, trimmed to `118s`, applied a `3s` fade-out, preserved stereo, and re-encoded to `44.1 kHz` Vorbis
- Suitability: formal, processional, and congress-scale rather than apocalyptic; it reads as a chartered transcontinental union rather than the terminal `World Is One` end-state
- Uncertainty: the source title's Queen of Sheba framing is more regionally resonant for Africa-Middle East outcomes than for every possible dynamic union, but the music itself remains broad enough for a federation/congress role

## Rejected / preserved evaluation source

### `beethoven_symphony_7_allegretto_john_michel`

- Status: rejected for final Event 012 use
- Role evaluated: `africa_continent_sponsor`
- Notes:
  - `docs/assets/012_africa/super_events/audio/source/beethoven_symphony_7_allegretto_john_michel.ogg` was preserved during evaluation
  - source URL: `https://commons.wikimedia.org/wiki/File:JOHN_MICHEL_CELLO-BEETHOVEN_SYMPHONY_7_Allegretto.ogg`
  - license position: `CC BY-SA 3.0`, VRT-confirmed, legally usable
- blocker: the solo-cello recording has long low-energy gaps that made it a weak final in-game package for the sponsor role without a more invasive edit pass
- action: do not wire; the sponsor role now uses `The Thunderer`

### `elgar_nimrod_barbirolli_halle`

- Status: rejected for final Event 012 use
- Role evaluated: `africa_rsa_allies_peace`
- Notes:
  - `docs/assets/012_africa/super_events/audio/source/elgar_nimrod_barbirolli_halle.ogg` was preserved during evaluation
  - source URL: `https://commons.wikimedia.org/wiki/File:Elgar;_Enigma_variations,_Theme_IX._Nimrod.ogg`
  - source SHA-256: `1cdf75f6bd96fe03357130c7e6d192409f3c72f3200906033b3354ac28601c82`
  - license position: Commons marks it public domain under expired EU recording rights sourced from Archive.org
  - blocker: the tone fit was strong, but the licensing position was less clean for a high-confidence mod handoff than the selected U.S. Marine Band public-domain recording
  - action: do not wire; the peace role now uses `Intermezzo from Goyescas`
