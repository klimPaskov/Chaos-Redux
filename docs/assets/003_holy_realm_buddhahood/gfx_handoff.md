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

Remaining animation handoff:

- These static states do not replace the final animated frame-sheet package from the asset spec.
- Future animation should preserve the sprite naming pattern by adding `_animated` variants, for example `GFX_holy_realm_mandala_awakened_animated`, with static fallbacks left in place.

## Holy Realm Static Leader Portrait Stages

The existing stage aliases in `interface/chaosx_characters.gfx` now point to separate static DDS files. These are static fallbacks derived from the existing fictional Holy Realm leader portrait and do not replace animated portrait frame sheets.

| Stage | Sprite alias | DDS |
| --- | --- | --- |
| Refuge Bodhisattva | `GFX_portrait_THR_refuge_bodhisattva` | `gfx/leaders/THR/portrait_THR_refuge_bodhisattva.dds` |
| Pramudita Bodhisattva | `GFX_portrait_THR_bodhisattva_pramudita` | `gfx/leaders/THR/portrait_THR_bodhisattva_pramudita.dds` |
| Acala Bodhisattva | `GFX_portrait_THR_bodhisattva_acala` | `gfx/leaders/THR/portrait_THR_bodhisattva_acala.dds` |
| Dharmamegha Bodhisattva | `GFX_portrait_THR_bodhisattva_dharmamegha` | `gfx/leaders/THR/portrait_THR_bodhisattva_dharmamegha.dds` |
| Arhat Administration | `GFX_portrait_THR_arhat_administration` | `gfx/leaders/THR/portrait_THR_arhat_administration.dds` |
| Buddha Mandate | `GFX_portrait_THR_buddha_mandate` | `gfx/leaders/THR/portrait_THR_buddha_mandate.dds` |
| Divine Sovereignty | `GFX_portrait_THR_divine_sovereignty` | `gfx/leaders/THR/portrait_THR_divine_sovereignty.dds` |
| Final Silence | `GFX_portrait_THR_final_silence` | `gfx/leaders/THR/portrait_THR_final_silence.dds` |

Review assets:

- Source PNG: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_png/portrait_THR_godly_figure_source.png`
- Processed PNGs: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/leader_portrait_static_contact_sheet.png`

Remaining animation handoff:

- Future animation should preserve the sprite naming pattern by adding `_animated` variants where the target surface supports a frame sheet.

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
