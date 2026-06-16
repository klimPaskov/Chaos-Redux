# Event 012 Africa Missing Super-Event Roles Audio Handoff

Updated: 2026-06-16

Scope:

- Audio-only package for two missing Event 012 Africa super-event roles.
- No gameplay, localisation, interface, or sound-definition files were edited.
- Final output is documentation plus preserved source audio and processed docs-side `.ogg` candidates only.

Roles completed:

- `africa_rsa_allies_peace`
- `africa_dynamic_cross_continent_union`

## Files created or updated

- Updated manifest:
  - `docs/assets/012_africa/super_events/audio/manifest.md`
- New handoff:
  - `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_super_event_missing_roles_audio_handoff.md`
- Preserved source downloads:
  - `docs/assets/012_africa/super_events/audio/source/granados_intermezzo_goyescas_us_marine_band.ogg`
  - `docs/assets/012_africa/super_events/audio/source/gounod_grand_march_la_reine_de_saba_us_marine_band.ogg`
  - `docs/assets/012_africa/super_events/audio/source/elgar_nimrod_barbirolli_halle.ogg`
- Final docs-side game-ready candidates:
  - `docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg`
  - `docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg`

## Selected package 1: `africa_rsa_allies_peace`

- Suggested sound definition id: `super_event_africa_rsa_allies_peace`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg`
- Source path: `docs/assets/012_africa/super_events/audio/source/granados_intermezzo_goyescas_us_marine_band.ogg`
- Track title: `Intermezzo from Goyescas`
- Composer: Enrique Granados
- Performer / recording source: United States Marine Band, transcription by John R. Bourgeois, from *Director's Choice*
- Source URL: `https://commons.wikimedia.org/wiki/File:Intermezzo_from_Goyescas_-_U.S._Marine_Band.ogg`
- License: public domain composition and U.S. Marine Band public-domain performance/recording on Commons
- License confidence: high
- Source duration: `327.079184s`
- Final duration: `116.000000s`
- Source SHA-256: `42bc530bea5429bc839374a3a95a3acd43c882de3f0b96c646a84cd870d6cf7a`
- Final SHA-256: `a77c48ad39590de67caf671e23c6bcf19778aaa045954332020436b4f7888127`
- Attribution required: no
- Processing command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/granados_intermezzo_goyescas_us_marine_band.ogg -af "atrim=start=0:duration=116,asetpts=N/SR/TB,afade=t=out:st=113:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg
```

- Why it fits:
  - Reflective and tired rather than celebratory.
  - Formal enough for treaty language and irreversible settlement.
  - Carries the civil-war aftermath mood without slipping into terminal doom.

## Selected package 2: `africa_dynamic_cross_continent_union`

- Suggested sound definition id: `super_event_africa_dynamic_cross_continent_union`
- Final path: `docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg`
- Source path: `docs/assets/012_africa/super_events/audio/source/gounod_grand_march_la_reine_de_saba_us_marine_band.ogg`
- Track title: `Grand March from La reine de Saba`
- Composer: Charles-Francois Gounod
- Performer / recording source: U.S. Marine Band under LtCol William F. Santelmann, from *From Fife and Drum: Marine Band Recordings 1890-1988*
- Source URL: `https://commons.wikimedia.org/wiki/File:Charles_Gounod_-_U.S._Marine_Band_-_Grand_March_from_La_reine_de_Saba.ogg`
- License: public domain composition and U.S. Marine Band public-domain performance/recording on Commons
- License confidence: high
- Source duration: `305.946122s`
- Final duration: `118.006349s`
- Source SHA-256: `9d7b2df0de474465e530e53c7744f35de5e43cb09ac70b8fbcc633149714980c`
- Final SHA-256: `af56784510a2c190f2c84542b7dfba2fcbfb4d8d7428f83b62694208c7b53d2a`
- Attribution required: no
- Processing command:

```bash
ffmpeg -y -i docs/assets/012_africa/super_events/audio/source/gounod_grand_march_la_reine_de_saba_us_marine_band.ogg -af "atrim=start=0.564:duration=118,asetpts=N/SR/TB,afade=t=out:st=115:d=3" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg
```

- Why it fits:
  - Sounds like a congressional procession or charter ceremony, not a final world-ending revelation.
  - Large enough for merged continents and shared institutions.
  - Distinct from the existing Event 012 unification and terminal-world cues.

## Evaluated but not selected

### `elgar_nimrod_barbirolli_halle`

- Source path: `docs/assets/012_africa/super_events/audio/source/elgar_nimrod_barbirolli_halle.ogg`
- Source URL: `https://commons.wikimedia.org/wiki/File:Elgar;_Enigma_variations,_Theme_IX._Nimrod.ogg`
- Source SHA-256: `1cdf75f6bd96fe03357130c7e6d192409f3c72f3200906033b3354ac28601c82`
- Role evaluated: `africa_rsa_allies_peace`
- Why rejected:
  - Strong tonal fit.
  - Weaker licensing confidence than the selected U.S. Marine Band source because Commons classifies it under expired EU recording rights from an Archive.org source rather than a cleaner U.S. government recording.

## Validation notes

- Both final candidates exist under `docs/assets/012_africa/super_events/audio/final/`.
- Both final candidates probe as stereo `44100 Hz` Vorbis:
  - `super_event_africa_rsa_allies_peace.ogg`: `116.000000s`
  - `super_event_africa_dynamic_cross_continent_union.ogg`: `118.006349s`
- No existing finalized Event 012 track was reused for either missing role.

## Blockers

- No blocker remains for these two roles.
