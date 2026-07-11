# System Camp Repression Rework Audio Wiring Handoff

## Scope and implementation status

The five final cue pairs exist, decode successfully, and are fully wired. This file preserves the production-to-integration handoff as provenance; the live implementation is recorded in `audio_manifest.md` and `docs/super_events/super_event_audio_packages.md`.

Audio IDs `44–48` continue the live registry after ID `43`. The `camp_rework_super_event` constants map those audio IDs to visible slots `74`, `12`, `75`, `76`, and `77`. Audio IDs remain project-wide and independent of visible super-event slots.

## Stable file and identifier map

| Audio ID | Visible slot | Super-event role | Music path relative to `music/` | Sound path relative to `sound/` | Final base sound ID |
| --- | --- | --- | --- | --- | --- |
| `44` | `74` | Global Atrocity Evidence Discovery | `system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.ogg` | `system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.wav` | `chaosx_super_event_camp_global_discovery_track` |
| `45` | `12` | Angel of Death Directorate Revolt | `system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.ogg` | `system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.wav` | `chaosx_super_event_camp_angel_directorate_revolt_track` |
| `46` | `75` | Soviet Famine Catastrophe | `system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.ogg` | `system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.wav` | `chaosx_super_event_camp_soviet_famine_catastrophe_track` |
| `47` | `76` | Pingfang Exposure | `system_camp_repression_rework/super_event_47_pingfang_exposure.ogg` | `system_camp_repression_rework/super_event_47_pingfang_exposure.wav` | `chaosx_super_event_camp_pingfang_exposure_track` |
| `48` | `77` | Colonial Reckoning | `system_camp_repression_rework/super_event_48_colonial_reckoning.ogg` | `system_camp_repression_rework/super_event_48_colonial_reckoning.wav` | `chaosx_super_event_camp_colonial_reckoning_track` |

Keep the final filenames unchanged. The paths already match the event/system-scoped audio layout required by the super-event skill.

## Music definition wiring

Target: `music/chaosx_super_event_music.asset`

Each row above uses six settings-aware definitions following the exact ID `43` pattern:

```text
music = { name = "chaosx_super_event_<id>_0_5" file = "<music path>" volume = 0.67 }
music = { name = "chaosx_super_event_<id>_1_0" file = "<music path>" volume = 1.33 }
music = { name = "chaosx_super_event_<id>_1_5" file = "<music path>" volume = 2.00 }
music = { name = "chaosx_super_event_<id>_2_0" file = "<music path>" volume = 2.67 }
music = { name = "chaosx_super_event_<id>_2_5" file = "<music path>" volume = 3.33 }
music = { name = "chaosx_super_event_<id>_3_0" file = "<music path>" volume = 4.00 }
```

This yields these stable helper families:

- `chaosx_super_event_44_{0_5,1_0,1_5,2_0,2_5,3_0}`
- `chaosx_super_event_45_{0_5,1_0,1_5,2_0,2_5,3_0}`
- `chaosx_super_event_46_{0_5,1_0,1_5,2_0,2_5,3_0}`
- `chaosx_super_event_47_{0_5,1_0,1_5,2_0,2_5,3_0}`
- `chaosx_super_event_48_{0_5,1_0,1_5,2_0,2_5,3_0}`

Target: `music/chaosx_super_event_music.txt`

One zero-chance representative entry per cue is registered:

```text
# Global Atrocity Evidence Discovery
music = { song = "chaosx_super_event_44_1_5" chance = { factor = 0 } }

# Angel of Death Directorate Revolt
music = { song = "chaosx_super_event_45_1_5" chance = { factor = 0 } }

# Soviet Famine Catastrophe
music = { song = "chaosx_super_event_46_1_5" chance = { factor = 0 } }

# Pingfang Exposure
music = { song = "chaosx_super_event_47_1_5" chance = { factor = 0 } }

# Colonial Reckoning
music = { song = "chaosx_super_event_48_1_5" chance = { factor = 0 } }
```

The comments use the accepted role names. The stable music IDs and files remain independent of visible localisation.

## Sound definition wiring

Target: `sound/chaosx_sound.asset`

Add these base sound records:

```text
sound = { name = chaosx_super_event_camp_global_discovery_track file = "system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.wav" }
sound = { name = chaosx_super_event_camp_angel_directorate_revolt_track file = "system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.wav" }
sound = { name = chaosx_super_event_camp_soviet_famine_catastrophe_track file = "system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.wav" }
sound = { name = chaosx_super_event_camp_pingfang_exposure_track file = "system_camp_repression_rework/super_event_47_pingfang_exposure.wav" }
sound = { name = chaosx_super_event_camp_colonial_reckoning_track file = "system_camp_repression_rework/super_event_48_colonial_reckoning.wav" }
```

For each audio ID, add the six sound-effect wrappers using the same volume map as the music channel:

```text
soundeffect = { name = "chaosx_super_event_<id>_sound_0_5" volume = 0.67 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
soundeffect = { name = "chaosx_super_event_<id>_sound_1_0" volume = 1.33 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
soundeffect = { name = "chaosx_super_event_<id>_sound_1_5" volume = 2.00 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
soundeffect = { name = "chaosx_super_event_<id>_sound_2_0" volume = 2.67 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
soundeffect = { name = "chaosx_super_event_<id>_sound_2_5" volume = 3.33 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
soundeffect = { name = "chaosx_super_event_<id>_sound_3_0" volume = 4.00 sounds = { sound = <base sound ID> } max_audible = 1 max_audible_behaviour = fail }
```

All 30 wrapper IDs (`44–48`, six suffixes each) are present in the existing `category = { name = "Effects" ... }` sound-effects list.

## Gameplay and settings-aware dispatch

The shared audio-ID dispatch covers both playback modes, and each accepted trigger supplies this value:

| Visible slot | Role | Required audio value before the existing playback helper runs |
| --- | --- | --- |
| `74` | Global Atrocity Evidence Discovery | `44`, currently supplied by `constant:camp_rework_super_event.global_discovery_audio` |
| `12` | Angel of Death Directorate Revolt | `45`, currently supplied by `constant:camp_rework_super_event.angel_directorate_audio` |
| `75` | Soviet Famine Catastrophe | `46`, currently supplied by `constant:camp_rework_super_event.soviet_famine_audio` |
| `76` | Pingfang Exposure | `47`, currently supplied by `constant:camp_rework_super_event.pingfang_exposure_audio` |
| `77` | Colonial Reckoning | `48`, currently supplied by `constant:camp_rework_super_event.colonial_reckoning_audio` |

Use the existing `play_current_super_event_audio` settings-aware helper. Do not call a music or sound wrapper directly from an event. Confirm that every volume setting resolves to the corresponding `chaosx_super_event_<id>_<volume>` music ID or `chaosx_super_event_<id>_sound_<volume>` sound-effect ID.

Each reserved slot, text/image getter, trigger, and audio ID is aligned. Slot `12` uses audio ID `45`; the catalogue and package docs no longer assign its former cue to that slot.

## Documentation and catalogue wiring

Target: `music/chaosx_music_track_list.html`

The catalogue has one row per track using these confirmed visible titles, slots, and source facts:

| Audio ID | Visible slot for “Super Event IDs” | Source title | Composer / creator | Performer / recording | Duration | Attribution status |
| --- | --- | --- | --- | --- | --- | --- |
| `44` | `74` | *Gnossienne No. 1* | Erik Satie | La Pianista, 2010 | `01:52` | Verified; public-domain composition, CC BY-SA 3.0 performance |
| `45` | `12` | *Passacaglia and Fugue in C minor, BWV 582* | Johann Sebastian Bach | Awadagin Pratt, White House, 2009 | `01:54` | Verified; public-domain composition, CC BY 3.0 performance/source file |
| `46` | `75` | *Hey, Plyve Kacha po Tysyni* | Traditional Ukrainian Lemko folk song | Revutsky Capella, London, 2013 | `01:56` | Verified; traditional composition, CC BY 3.0 recording |
| `47` | `76` | *Yangguan Sandie (Three Refrains on the Yang Pass Theme)* | Traditional Chinese guqin repertory; *Qinxue Rumen* (1867) score source | Charlie Huang / Charles R Tsua, 2013 | `01:49` | Verified; public-domain score source, CC BY-SA 3.0 performance |
| `48` | `77` | *Go Down Moses* | Traditional African American spiritual | Les Petits Chanteurs de Montigny, Jamendo, 2005 | `01:50` | Verified; public-domain traditional composition, CC BY-SA 2.0 performance |

The row's “Super Event IDs” column must list the visible super-event slot, not the numeric audio ID, unless the table schema is deliberately changed. The current table happens to align those values for many older entries but they are separate concepts.

`docs/super_events/super_event_audio_packages.md` records the visible slots, final sound-definition IDs, and settings-aware registration. Detailed attribution and license terms remain in `audio_manifest.md` and `docs/super_events/system_camp_repression_rework_super_event_research.md`.

## Final wiring checklist

- [x] Audio IDs `44–48` are unique in the shared registry.
- [x] Six music variants are registered for each ID.
- [x] Five representative zero-chance station records are registered.
- [x] Five base WAV sounds and thirty sound-effect wrappers are registered.
- [x] All thirty wrappers are in the `Effects` category.
- [x] Both branches of the settings-aware ID dispatch resolve IDs `44–48`.
- [x] Each accepted trigger sets the matching audio ID and visible slot.
- [x] The catalogue records all five final cues and visible slots.
- [x] The implemented packages are recorded in `docs/super_events/super_event_audio_packages.md`.
- [x] CC BY and CC BY-SA attribution and derivative terms remain recorded in `audio_manifest.md`.

No fallback, reused track, placeholder, uncertain-license cue, generated cue, or non-musical substitute is present in this handoff.
