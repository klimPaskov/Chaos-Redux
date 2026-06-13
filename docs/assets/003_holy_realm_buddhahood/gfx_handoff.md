# Holy Realm Buddhahood GFX Handoff

The achievement package originally did not edit any `.gfx` files. Achievement sprites are wired under the existing achievement sprite pattern. The `Powers of the Awakened` super-event image now reuses the already registered super-event sprite and texture path.

## Super-Event Images

| Super-event | Sprite alias | DDS | Notes |
| --- | --- | --- | --- |
| `Powers of the Awakened` | `GFX_super_event_powers_of_the_awakened` | `gfx/super_events/super_event_powers_of_the_awakened.dds` | Existing sprite path preserved; copied Buddha Mandate placeholder replaced with bespoke generated monochrome super-event art. |

## Holy Mandala Static GUI States

The decision-category Mandala panel now uses static fallback states. These are registered in `interface/003_holy_realm.gfx` and selected by `GetHolyRealmMandalaSprite` in `common/scripted_localisation/003_holy_realm_scripted_localisation.txt`.

| State | Sprite alias | DDS |
| --- | --- | --- |
| Dormant | `GFX_holy_realm_mandala_dormant` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant.dds` |
| Teaching | `GFX_holy_realm_mandala_teaching` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching.dds` |
| Meditation | `GFX_holy_realm_mandala_meditation` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation.dds` |
| Awakened | `GFX_holy_realm_mandala_awakened` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened.dds` |
| Wrathful | `GFX_holy_realm_mandala_wrathful` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful.dds` |
| Final Silence | `GFX_holy_realm_mandala_final_silence` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence.dds` |
| Empty Seat | `GFX_holy_realm_mandala_empty` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty.dds` |

Review assets:

- Processed PNGs: `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/mandala_static_contact_sheet.png`

## Holy Mandala Dormant Animation

The locked, early, or otherwise inactive Mandala state uses an animated frame sheet while preserving the static dormant DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_dormant` |
| Animated sprite alias | `GFX_holy_realm_mandala_dormant_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/sheets/holy_realm_mandala_dormant_sheet.png` |
| Frame size | `420x420` |
| Frame count | `8` |
| Sheet size | `3360x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite as the always-available fallback after all higher-priority Mandala states fail |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/core.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/previews/holy_realm_mandala_dormant_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/previews/holy_realm_mandala_dormant_contact.png`

## Holy Mandala Teaching Animation

The Dharma teaching and Bodhi-progress Mandala state uses an animated frame sheet while preserving the static teaching DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_teaching` |
| Animated sprite alias | `GFX_holy_realm_mandala_teaching_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/sheets/holy_realm_mandala_teaching_sheet.png` |
| Frame size | `420x420` |
| Frame count | `8` |
| Sheet size | `3360x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite for Dharma-teaching unlock, positive `teaching_successes`, or positive `bodhi_progress` after higher-priority states |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/core.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/previews/holy_realm_mandala_teaching_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/previews/holy_realm_mandala_teaching_contact.png`

## Holy Mandala Meditation Animation

The active concentration and Dhyana-progress Mandala state uses an animated frame sheet while preserving the static meditation DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_meditation` |
| Animated sprite alias | `GFX_holy_realm_mandala_meditation_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/sheets/holy_realm_mandala_meditation_sheet.png` |
| Frame size | `420x420` |
| Frame count | `12` |
| Sheet size | `5040x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite for concentration-step flags or any positive `dhyana_depth` before higher-priority states |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/core.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/previews/holy_realm_mandala_meditation_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/previews/holy_realm_mandala_meditation_contact.png`

## Holy Mandala Awakened Animation

The Buddhahood-complete Mandala state uses an animated frame sheet while preserving the static awakened DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_awakened` |
| Animated sprite alias | `GFX_holy_realm_mandala_awakened_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/sheets/holy_realm_mandala_awakened_sheet.png` |
| Frame size | `420x420` |
| Frame count | `12` |
| Sheet size | `5040x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite when `holy_realm_has_buddha_mandate = yes` |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/core.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/previews/holy_realm_mandala_awakened_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/previews/holy_realm_mandala_awakened_contact.png`

## Holy Mandala Final Silence Animation

The armed Final Silence ritual state uses an animated frame sheet while preserving the static Final Silence DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_final_silence` |
| Animated sprite alias | `GFX_holy_realm_mandala_final_silence_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/sheets/holy_realm_mandala_final_silence_sheet.png` |
| Frame size | `420x420` |
| Frame count | `12` |
| Sheet size | `5040x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite for armed or active Final Silence states |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/core.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/previews/holy_realm_mandala_final_silence_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/previews/holy_realm_mandala_final_silence_contact.png`

## Holy Mandala Wrathful Animation

The Wrathful Protection, Sun and Moon crisis proof, and Touching Sun and Moon Mandala state uses an animated frame sheet while preserving the static wrathful DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_wrathful` |
| Animated sprite alias | `GFX_holy_realm_mandala_wrathful_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/sheets/holy_realm_mandala_wrathful_sheet.png` |
| Frame size | `420x420` |
| Frame count | `12` |
| Sheet size | `5040x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite for Wrathful Protection, Sun and Moon crisis proof, or Touching Sun and Moon power use |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_contact.png`

## Holy Mandala Empty Seat Animation

The non-terminal Final Silence afterstate and Empty Seat achievement-ready Mandala state uses an animated frame sheet while preserving the static empty-seat DDS as its fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_holy_realm_mandala_empty` |
| Animated sprite alias | `GFX_holy_realm_mandala_empty_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/sheets/holy_realm_mandala_empty_sheet.png` |
| Frame size | `420x420` |
| Frame count | `8` |
| Sheet size | `3360x420` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Target GUI | `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt` |
| State gate | `GetHolyRealmMandalaSprite` returns the animated sprite for non-terminal Final Silence completion or Empty Seat achievement readiness |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`, `interface/007_fury.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/previews/holy_realm_mandala_empty_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/previews/holy_realm_mandala_empty_contact.png`

## Holy Realm Dhyana Seal Decision Icon Animation

The concentration sequence uses an animated Dhyana Seal decision icon while preserving a static seal DDS as fallback.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_decision_holy_realm_dhyana_seal` |
| Animated sprite alias | `GFX_decision_holy_realm_dhyana_seal_animated` |
| Static fallback DDS | `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal.dds` |
| Animated sheet DDS | `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/sheets/holy_realm_dhyana_seal_sheet.png` |
| Frame size | `96x96` |
| Frame count | `8` |
| Sheet size | `768x96` |
| FPS | `8` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/003_holy_realm.gfx` |
| Gameplay use | `THR_begin_concentration_sequence`, `THR_hold_intention`, `THR_hold_energy`, `THR_hold_mind`, and `THR_hold_investigation` use the animated sprite as their decision icon |
| Wiring precedent | `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `interface/003_holy_realm.gfx` |

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_contact.png`

## Holy Realm Buddha Power Decision Icons

The named Buddha powers and repeated Dharma teaching decisions use custom static decision icons.

| Sprite alias | DDS | Gameplay use |
| --- | --- | --- |
| `GFX_decision_holy_realm_power_one_becomes_many` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_one_becomes_many.dds` | `THR_buddha_power_one_becomes_many` |
| `GFX_decision_holy_realm_power_passing_through_walls` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_passing_through_walls.dds` | `THR_buddha_power_passing_through_walls` |
| `GFX_decision_holy_realm_power_walking_on_water` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_walking_on_water.dds` | `THR_buddha_power_walking_on_water` |
| `GFX_decision_holy_realm_power_lotus_bridge` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_lotus_bridge.dds` | `THR_buddha_power_lotus_bridge` |
| `GFX_decision_holy_realm_power_vanishing_from_sight` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_vanishing_from_sight.dds` | `THR_buddha_power_vanishing_from_sight` |
| `GFX_decision_holy_realm_power_seated_in_sky` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_seated_in_sky.dds` | `THR_buddha_power_seated_in_sky` |
| `GFX_decision_holy_realm_power_touching_sun_moon` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_touching_sun_moon.dds` | `THR_buddha_power_touching_sun_moon` |
| `GFX_decision_holy_realm_power_extinction_defilements` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_power_extinction_defilements.dds` | `THR_buddha_power_extinction_defilements` |
| `GFX_decision_holy_realm_dharma_teaching` | `gfx/interface/decisions/holy_realm/powers/decision_holy_realm_dharma_teaching.dds` | `THR_hold_dharma_teaching`, `THR_bodhisattva_hold_teachings_for_refugees`, and `THR_bodhisattva_teach_foreign_officers` |

Review assets:

- Source PNGs: `docs/assets/003_holy_realm_buddhahood/decision_icons/source_png/`
- Processed PNGs: `docs/assets/003_holy_realm_buddhahood/decision_icons/processed_png/`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/decision_icons/decision_icons_contact_sheet.png`

## Holy Realm Buddha Mandate Leader Portrait Animation

The Buddhahood-stage presentation portrait uses an animated frame sheet while preserving the static Buddha Mandate DDS for the actual country-leader portrait.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_portrait_THR_buddha_mandate` |
| Animated sprite alias | `GFX_portrait_THR_buddha_mandate_animated` |
| Static fallback DDS | `gfx/leaders/THR/portrait_THR_buddha_mandate.dds` |
| Animated sheet DDS | `gfx/leaders/THR/portrait_THR_buddha_mandate_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/sheets/portrait_THR_buddha_mandate_sheet.png` |
| Frame size | `156x210` |
| Frame count | `16` |
| Sheet size | `2496x210` |
| FPS | `4` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/chaosx_characters.gfx` |
| Gameplay use | `holy_realm_set_stage_buddha_mandate` sets the country leader portrait to the static sprite |
| Event-details use | Holy Realm evolution stage 4 returns the animated portrait sprite |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `interface/007_fury.gfx` |

Source mode: `$imagegen`, eight individual key-state portraits expanded into sixteen playback frames by mirrored ordering.

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/previews/portrait_THR_buddha_mandate_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/previews/portrait_THR_buddha_mandate_contact.png`

## Holy Realm Empty Seat Leader Portrait Animation

The Final Silence aftermath presentation portrait uses a dedicated Empty Seat frame sheet while preserving a static Empty Seat DDS for the actual country-leader portrait.

| Field | Value |
| --- | --- |
| Static sprite alias | `GFX_portrait_THR_empty_seat` |
| Animated sprite alias | `GFX_portrait_THR_empty_seat_animated` |
| Static fallback DDS | `gfx/leaders/THR/portrait_THR_empty_seat.dds` |
| Animated sheet DDS | `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds` |
| Sheet PNG | `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/sheets/portrait_THR_empty_seat_sheet.png` |
| Frame size | `156x210` |
| Frame count | `16` |
| Sheet size | `2496x210` |
| FPS | `4` |
| Loop | `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Target `.gfx` | `interface/chaosx_characters.gfx` |
| Gameplay use | `holy_realm_set_stage_final_silence` sets the country leader portrait to the static sprite |
| Event-details use | Holy Realm evolution stage 6 returns the animated portrait sprite |
| Wiring precedent | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `interface/chaosx_characters.gfx` |

Source mode: `$imagegen`, eight individual key-state portraits expanded into sixteen playback frames by mirrored ordering.

Review assets:

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/processed_frames/`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/previews/portrait_THR_empty_seat_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/previews/portrait_THR_empty_seat_contact.png`

## Holy Realm Static Leader Portrait Stages

The existing stage aliases in `interface/chaosx_characters.gfx` point to separate static DDS files. Refuge Bodhisattva, Pramudita, Acala, Dharmamegha, Arhat Administration, False Buddha, Divine Sovereignty, and Final Silence are sourced from a generated 4x2 static portrait sheet that uses `portrait_THR_godly_figure.dds` as the identity/edit anchor. Buddha Mandate and Empty Seat static fallbacks come from frame 000 of their animation packages, which also use the same source portrait as their identity anchor.

| Stage | Sprite alias | DDS |
| --- | --- | --- |
| Refuge Bodhisattva | `GFX_portrait_THR_refuge_bodhisattva` | `gfx/leaders/THR/portrait_THR_refuge_bodhisattva.dds` |
| Pramudita Bodhisattva | `GFX_portrait_THR_bodhisattva_pramudita` | `gfx/leaders/THR/portrait_THR_bodhisattva_pramudita.dds` |
| Acala Bodhisattva | `GFX_portrait_THR_bodhisattva_acala` | `gfx/leaders/THR/portrait_THR_bodhisattva_acala.dds` |
| Dharmamegha Bodhisattva | `GFX_portrait_THR_bodhisattva_dharmamegha` | `gfx/leaders/THR/portrait_THR_bodhisattva_dharmamegha.dds` |
| Arhat Administration | `GFX_portrait_THR_arhat_administration` | `gfx/leaders/THR/portrait_THR_arhat_administration.dds` |
| Buddha Mandate | `GFX_portrait_THR_buddha_mandate` | `gfx/leaders/THR/portrait_THR_buddha_mandate.dds` |
| False Buddha | `GFX_portrait_THR_false_buddha` | `gfx/leaders/THR/portrait_THR_false_buddha.dds` |
| Divine Sovereignty | `GFX_portrait_THR_divine_sovereignty` | `gfx/leaders/THR/portrait_THR_divine_sovereignty.dds` |
| Final Silence | `GFX_portrait_THR_final_silence` | `gfx/leaders/THR/portrait_THR_final_silence.dds` |
| Empty Seat | `GFX_portrait_THR_empty_seat` | `gfx/leaders/THR/portrait_THR_empty_seat.dds` |

Review assets:

- Static reference, source sheet, and split sources: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_png/`
- Static source prompt/order record: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_prompts.md`
- Buddha Mandate and Empty Seat static fallbacks: frame 000 from their animation packages, copied into `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/`
- Processed PNGs: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/leader_portrait_static_contact_sheet.png`

Portrait animation handoff:

- Buddha Mandate and Empty Seat animated portrait sheets are recorded in the sections above and registered in `interface/chaosx_characters.gfx`.

## Completed DDS triplets

| Achievement id | Base DDS | Grey DDS | Not-eligible DDS | Proposed sprite alias |
| --- | --- | --- | --- | --- |
| `HOLY_REALM_NO_EMPIRE_OF_THE_WHEEL` | `gfx/achievements/holy_realm_no_empire_of_the_wheel.dds` | `gfx/achievements/holy_realm_no_empire_of_the_wheel_grey.dds` | `gfx/achievements/holy_realm_no_empire_of_the_wheel_not_eligible.dds` | `GFX_achievement_holy_realm_no_empire_of_the_wheel` |
| `HOLY_REALM_FOUR_DHYANAS_UNDER_FIRE` | `gfx/achievements/holy_realm_four_dhyanas_under_fire.dds` | `gfx/achievements/holy_realm_four_dhyanas_under_fire_grey.dds` | `gfx/achievements/holy_realm_four_dhyanas_under_fire_not_eligible.dds` | `GFX_achievement_holy_realm_four_dhyanas_under_fire` |
| `HOLY_REALM_ONE_BECOMES_MANY` | `gfx/achievements/holy_realm_one_becomes_many.dds` | `gfx/achievements/holy_realm_one_becomes_many_grey.dds` | `gfx/achievements/holy_realm_one_becomes_many_not_eligible.dds` | `GFX_achievement_holy_realm_one_becomes_many` |
| `HOLY_REALM_WALL_RIVER_SKY` | `gfx/achievements/holy_realm_wall_river_sky.dds` | `gfx/achievements/holy_realm_wall_river_sky_grey.dds` | `gfx/achievements/holy_realm_wall_river_sky_not_eligible.dds` | `GFX_achievement_holy_realm_wall_river_sky` |
| `HOLY_REALM_EMPTY_SEAT` | `gfx/achievements/holy_realm_empty_seat.dds` | `gfx/achievements/holy_realm_empty_seat_grey.dds` | `gfx/achievements/holy_realm_empty_seat_not_eligible.dds` | `GFX_achievement_holy_realm_empty_seat` |
| `HOLY_REALM_FINAL_SILENCE_WORLD_END` | `gfx/achievements/holy_realm_final_silence_world_end.dds` | `gfx/achievements/holy_realm_final_silence_world_end_grey.dds` | `gfx/achievements/holy_realm_final_silence_world_end_not_eligible.dds` | `GFX_achievement_holy_realm_final_silence_world_end` |
| `HOLY_REALM_NO_FALSE_BUDDHA` | `gfx/achievements/holy_realm_no_false_buddha.dds` | `gfx/achievements/holy_realm_no_false_buddha_grey.dds` | `gfx/achievements/holy_realm_no_false_buddha_not_eligible.dds` | `GFX_achievement_holy_realm_no_false_buddha` |
| `HOLY_REALM_DEBATE_THE_PRETENDER` | `gfx/achievements/holy_realm_debate_the_pretender.dds` | `gfx/achievements/holy_realm_debate_the_pretender_grey.dds` | `gfx/achievements/holy_realm_debate_the_pretender_not_eligible.dds` | `GFX_achievement_holy_realm_debate_the_pretender` |
| `HOLY_REALM_SANGHA_OF_NATIONS` | `gfx/achievements/holy_realm_sangha_of_nations.dds` | `gfx/achievements/holy_realm_sangha_of_nations_grey.dds` | `gfx/achievements/holy_realm_sangha_of_nations_not_eligible.dds` | `GFX_achievement_holy_realm_sangha_of_nations` |
| `HOLY_REALM_MERCY_IN_THE_ASHES` | `gfx/achievements/holy_realm_mercy_in_the_ashes.dds` | `gfx/achievements/holy_realm_mercy_in_the_ashes_grey.dds` | `gfx/achievements/holy_realm_mercy_in_the_ashes_not_eligible.dds` | `GFX_achievement_holy_realm_mercy_in_the_ashes` |
| `HOLY_REALM_SUN_AND_MOON` | `gfx/achievements/holy_realm_sun_and_moon.dds` | `gfx/achievements/holy_realm_sun_and_moon_grey.dds` | `gfx/achievements/holy_realm_sun_and_moon_not_eligible.dds` | `GFX_achievement_holy_realm_sun_and_moon` |
| `HOLY_REALM_LOTUS_BRIDGE` | `gfx/achievements/holy_realm_lotus_bridge.dds` | `gfx/achievements/holy_realm_lotus_bridge_grey.dds` | `gfx/achievements/holy_realm_lotus_bridge_not_eligible.dds` | `GFX_achievement_holy_realm_lotus_bridge` |

## Package review files

- Source PNGs: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/`
- Processed PNGs: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/`
- Contact sheets: `docs/assets/003_holy_realm_buddhahood/achievement_icons/contact_sheets/`
