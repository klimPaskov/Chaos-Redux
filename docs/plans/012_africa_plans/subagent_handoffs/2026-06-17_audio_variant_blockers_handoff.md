# Event 012 Africa Variant Audio Handoff

Date: `2026-06-17`

Scope: remaining variant blockers only. This pass did not edit gameplay, localisation, event, GUI, scripted localisation, sound definition, music definition, or `.gfx` wiring files.

## Files changed

- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/assets/012_africa/super_events/audio/source/judith_bokor_valse_triste_sibelius.flac`
- `docs/assets/012_africa/super_events/audio/source/veni_sancte_spiritus_membeth.ogg`
- `docs/assets/012_africa/super_events/audio/source/philadelphia_symphony_danse_macabre_1925.ogg`
- `docs/assets/012_africa/super_events/audio/source/dies_irae_membeth.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_forest_parliament.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_root.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_root_and_fang.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_archive_world.ogg`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_audio_variant_blockers_handoff.md`

## Already accepted packaged roles confirmed on disk

- `africa_is_one_unification`
- `africa_scramble_reaction`
- `africa_old_seats_reveal`
- `africa_counterfeit_crowns`
- `africa_world_is_one_terminal`
- `africa_continent_sponsor`
- `africa_rsa_allies_peace`
- `africa_dynamic_cross_continent_union`

These eight finals already existed under `docs/assets/012_africa/super_events/audio/final/` before this pass and remain the accepted base package.

## Newly packaged variant roles

| Role | Final file | Source | License note | Confidence | Suggested later sound id |
| --- | --- | --- | --- | --- | --- |
| Forest Parliament reveal | `super_event_africa_forest_parliament.ogg` | `Judith Bokor plays Valse triste by Sibelius.flac` | Commons marks file public domain / free of known restrictions; 1925 publication and PD-origin notes | medium-high | `super_event_africa_forest_parliament` |
| World Root Mandate | `super_event_africa_world_root.ogg` | `Veni.sancte.spiritus.ogg` | Commons uploader dedicated recording to the public domain | high | `super_event_africa_world_root` |
| Parliament of root and fang escalation | `super_event_africa_root_and_fang.ogg` | `PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg` | Commons marks sound recording public domain in the U.S. because it was published before `1926-01-01` | medium-high | `super_event_africa_root_and_fang` |
| Archive-world union terminal | `super_event_africa_archive_world.ogg` | `Dies.irae.ogg` | Commons uploader dedicated recording to the public domain | high | `super_event_africa_archive_world` |

## Candidate notes

### Forest Parliament reveal

- Recommendation: keep `Valse triste`
- Why it fits: slow ceremonial entry, uncanny but not comic, suited to a congress reveal rather than a panic escalation
- Source URL: `https://commons.wikimedia.org/wiki/File:Judith_Bokor_plays_Valse_triste_by_Sibelius.flac`

### World Root Mandate

- Recommendation: keep `Veni Sancte Spiritus`
- Why it fits: ritual invocation rather than martial triumph, which matches the Covenant binding-order tone
- Source URL: `https://commons.wikimedia.org/wiki/File:Veni.sancte.spiritus.ogg`
- Caution: the source is explicitly Christian liturgical chant; acceptable sonically, but replace later if the parent wants a less ecclesiastical frame

### Parliament of root and fang escalation

- Recommendation: keep `Danse Macabre`
- Why it fits: strongest legally clean uncanny-escalation cue found in this pass
- Source URL: `https://commons.wikimedia.org/wiki/File:PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg`
- Caution: title association is explicit; reserve it for Bestiary escalation, not the softer forest reveal

### Archive-world union terminal

- Recommendation: keep `Dies irae`
- Why it fits: terminal judgment tone distinct from the already packaged base `World Is One`
- Source URL: `https://commons.wikimedia.org/wiki/File:Dies.irae.ogg`

## Rejected candidates and reasons

| Candidate | Role evaluated | Reason rejected | Source URL | License note |
| --- | --- | --- | --- | --- |
| Existing `super_event_africa_world_is_one.ogg` reuse | root variant terminal | do not silently reuse existing terminal audio for a new variant role | existing packaged file | base terminal package already assigned |
| Existing `super_event_africa_archive_world.ogg` reuse | root variant terminal | do not silently collapse archive-world and root-terminal roles without parent approval | existing packaged file | archive-terminal package assigned in this pass |
| `beethoven_symphony_7_allegretto_john_michel.ogg` | continent sponsor / possible reflective variant reuse | legally usable but too sparse and stop-start for a clean super-event package without heavier editorial intervention | `https://commons.wikimedia.org/wiki/File:JOHN_MICHEL_CELLO-BEETHOVEN_SYMPHONY_7_Allegretto.ogg` | `CC BY-SA 3.0`, VRT-confirmed |
| `elgar_nimrod_barbirolli_halle.ogg` | RSA peace / possible terminal variant reuse | tone fit was fine, but prior package docs already judged the licensing position less clean than the accepted U.S. Marine Band alternative | `https://commons.wikimedia.org/wiki/File:Elgar;_Enigma_variations,_Theme_IX._Nimrod.ogg` | Commons PD claim from expired recording rights |

## Remaining blocker

### `africa_world_is_one_root_variant_terminal`

- Status: blocked
- Reason: current docs identify a root variant terminal, but do not cleanly say whether it is:
  - a fully separate terminal super-event needing a third unique terminal track; or
  - a presentation variant allowed to share the existing base or archive terminal package
- Action taken: left blocked rather than silently reusing `super_event_africa_world_is_one.ogg` or `super_event_africa_archive_world.ogg`

## Conversion notes

- Workflow used for all four packaged roles:
  - preserve original download in `docs/assets/012_africa/super_events/audio/source/`
  - export final `44.1 kHz` Vorbis `.ogg` in `docs/assets/012_africa/super_events/audio/final/`
  - keep opening intact
  - trim to `118s` or `120s`
  - add `4s` fade-out

## Validation

`ffprobe` results for new finals:

- `super_event_africa_forest_parliament.ogg`: `44100 Hz`, `2` channels, `118.000000s`
- `super_event_africa_world_root.ogg`: `44100 Hz`, `2` channels, `120.000000s`
- `super_event_africa_root_and_fang.ogg`: `44100 Hz`, `2` channels, `118.000000s`
- `super_event_africa_archive_world.ogg`: `44100 Hz`, `2` channels, `120.000000s`

## Parent wiring note

Suggested ids above are handoff-only notes. This pass did not touch sound or music definition files.
