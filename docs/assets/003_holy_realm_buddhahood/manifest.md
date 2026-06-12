# 003 Holy Realm Buddhahood Asset Manifest

Package scope: Holy Realm Buddhahood achievement icons, super-event handoffs, and Mandala GUI static fallback assets.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_grey.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_not_eligible.png`
- Additional Chaos Redux achievement examples in the same folder for framing, contrast, and readability checks.

Source mode:
- `$imagegen` for generated completed-state source art.
- Local ImageMagick processing for 64x64 resize, tonal cleanup, grey variant creation, not-eligible red-cross variant creation, contact sheet assembly, and DDS conversion.
- Local ImageMagick procedural composition for static Mandala GUI fallback states.
- Local ImageMagick stage treatment for static leader portrait fallbacks derived from the existing fictional Holy Realm leader portrait.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Final DDS files were validated for existence and `64x64` dimensions after export.

## Static Mandala GUI Fallbacks

These assets are static fallback states for the Holy Mandala decision-category scripted GUI. They are not animation frame sheets and should not be treated as the final animated Mandala package described by the asset specification.

Reference inspection completed:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/countrydecisionview.gui`
- `~/projects/Hearts of Iron IV/interface/core.gfx`

| State | Sprite alias | Processed PNG | Final DDS | In-game use |
| --- | --- | --- | --- | --- |
| Dormant | `GFX_holy_realm_mandala_dormant` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_dormant.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant.dds` | Early or locked Mandala state |
| Teaching | `GFX_holy_realm_mandala_teaching` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_teaching.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching.dds` | Teaching missions, Bodhi, or Dharma teachings unlocked |
| Meditation | `GFX_holy_realm_mandala_meditation` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_meditation.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation.dds` | Dhyana progress or active concentration sequence |
| Awakened | `GFX_holy_realm_mandala_awakened` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_awakened.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened.dds` | Buddhahood attained |
| Wrathful | `GFX_holy_realm_mandala_wrathful` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_wrathful.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful.dds` | Wrathful protection, Sun and Moon crisis proof, or equivalent emergency power state |
| Final Silence | `GFX_holy_realm_mandala_final_silence` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_final_silence.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence.dds` | Armed Final Silence, terminal world-end, or final stage |
| Empty Seat | `GFX_holy_realm_mandala_empty` | `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_empty.png` | `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty.dds` | Non-terminal Final Silence or Empty Seat aftermath |

Contact sheet: `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/mandala_static_contact_sheet.png`

Validation:
- All processed PNGs are `420x420`.
- All final DDS files are `420x420`.
- `interface/003_holy_realm.gfx` registers all seven static sprites.
- `common/scripted_localisation/003_holy_realm_scripted_localisation.txt` selects the active sprite through `GetHolyRealmMandalaSprite`.

## Static Leader Portrait Fallbacks

These assets provide visible stage changes for the existing Holy Realm leader portrait aliases. They are static DDS fallbacks derived from the existing fictional `GFX_portrait_THR_godly_figure` source and do not replace the animated portrait frame-sheet package requested by the full asset spec.

Reference inspection completed:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/_leader_portraits.gfx`
- `interface/chaosx_characters.gfx`

| Stage | Sprite alias | Processed PNG | Final DDS | In-game use |
| --- | --- | --- | --- | --- |
| Refuge Bodhisattva | `GFX_portrait_THR_refuge_bodhisattva` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_refuge_bodhisattva.png` | `gfx/leaders/THR/portrait_THR_refuge_bodhisattva.dds` | Initial Holy Realm refuge leader stage |
| Pramudita Bodhisattva | `GFX_portrait_THR_bodhisattva_pramudita` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_bodhisattva_pramudita.png` | `gfx/leaders/THR/portrait_THR_bodhisattva_pramudita.dds` | Early Bodhisattva and protectorate leader stage |
| Acala Bodhisattva | `GFX_portrait_THR_bodhisattva_acala` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_bodhisattva_acala.png` | `gfx/leaders/THR/portrait_THR_bodhisattva_acala.dds` | High-bhumi immovable leader stage |
| Dharmamegha Bodhisattva | `GFX_portrait_THR_bodhisattva_dharmamegha` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_bodhisattva_dharmamegha.png` | `gfx/leaders/THR/portrait_THR_bodhisattva_dharmamegha.dds` | Tenth-bhumi leader stage |
| Arhat Administration | `GFX_portrait_THR_arhat_administration` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_arhat_administration.png` | `gfx/leaders/THR/portrait_THR_arhat_administration.dds` | Arhat Administration stage |
| Buddha Mandate | `GFX_portrait_THR_buddha_mandate` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_buddha_mandate.png` | `gfx/leaders/THR/portrait_THR_buddha_mandate.dds` | Buddhahood and Buddha Mandate stage |
| Divine Sovereignty | `GFX_portrait_THR_divine_sovereignty` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_divine_sovereignty.png` | `gfx/leaders/THR/portrait_THR_divine_sovereignty.dds` | Divine Sovereignty stage |
| Final Silence | `GFX_portrait_THR_final_silence` | `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_final_silence.png` | `gfx/leaders/THR/portrait_THR_final_silence.dds` | Final Silence and Empty Seat aftermath portrait stage |

Source PNG: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_png/portrait_THR_godly_figure_source.png`

Contact sheet: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/leader_portrait_static_contact_sheet.png`

Validation:
- All processed PNGs are `156x210`.
- All final DDS files are `156x210`.
- `interface/chaosx_characters.gfx` points each existing Holy Realm stage alias at its matching DDS.

## Assets

### `holy_realm_no_empire_of_the_wheel`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_NO_EMPIRE_OF_THE_WHEEL`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_no_empire_of_the_wheel_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_empire_of_the_wheel.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_empire_of_the_wheel_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_empire_of_the_wheel_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_no_empire_of_the_wheel.dds`
- Final DDS grey: `gfx/achievements/holy_realm_no_empire_of_the_wheel_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_no_empire_of_the_wheel_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: golden dharma wheel above a closed sword
- Notes: Centered sacred-war restraint composition with clear wheel and sheathed blade silhouettes.
- Asset status: `complete`

### `holy_realm_four_dhyanas_under_fire`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_FOUR_DHYANAS_UNDER_FIRE`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_four_dhyanas_under_fire_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_four_dhyanas_under_fire.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_four_dhyanas_under_fire_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_four_dhyanas_under_fire_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_four_dhyanas_under_fire.dds`
- Final DDS grey: `gfx/achievements/holy_realm_four_dhyanas_under_fire_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_four_dhyanas_under_fire_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: seated meditating figure with falling shells behind
- Notes: Foreground Buddha silhouette stays readable while the distant bombardment remains secondary.
- Asset status: `complete`

### `holy_realm_one_becomes_many`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_ONE_BECOMES_MANY`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_one_becomes_many_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_one_becomes_many.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_one_becomes_many_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_one_becomes_many_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_one_becomes_many.dds`
- Final DDS grey: `gfx/achievements/holy_realm_one_becomes_many_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_one_becomes_many_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: one central lamp with repeated silhouettes around it
- Notes: Lamp and repeated figures form a clear radial composition without crowd clutter.
- Asset status: `complete`

### `holy_realm_wall_river_sky`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_WALL_RIVER_SKY`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_wall_river_sky_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_wall_river_sky.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_wall_river_sky_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_wall_river_sky_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_wall_river_sky.dds`
- Final DDS grey: `gfx/achievements/holy_realm_wall_river_sky_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_wall_river_sky_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: mountain wall, river, and sky lotus in one stacked icon
- Notes: Uses a vertically layered composition to keep all three miracle symbols legible at icon size.
- Asset status: `complete`

### `holy_realm_empty_seat`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_EMPTY_SEAT`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_empty_seat_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_empty_seat.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_empty_seat_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_empty_seat_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_empty_seat.dds`
- Final DDS grey: `gfx/achievements/holy_realm_empty_seat_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_empty_seat_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: empty throne with lotus and bell
- Notes: The vacant ceremonial seat remains the dominant silhouette, with lotus and bell as clear supporting motifs.
- Asset status: `complete`

### `holy_realm_final_silence_world_end`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_FINAL_SILENCE_WORLD_END`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_final_silence_world_end_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_final_silence_world_end.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_final_silence_world_end_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_final_silence_world_end_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_final_silence_world_end.dds`
- Final DDS grey: `gfx/achievements/holy_realm_final_silence_world_end_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_final_silence_world_end_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: extinguished dark world with one surviving lotus
- Notes: Keeps the world-end mood severe by reducing the globe to a dark mass with a single luminous lotus anchor.
- Asset status: `complete`

### `holy_realm_no_false_buddha`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_NO_FALSE_BUDDHA`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_no_false_buddha_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_false_buddha.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_false_buddha_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_no_false_buddha_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_no_false_buddha.dds`
- Final DDS grey: `gfx/achievements/holy_realm_no_false_buddha_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_no_false_buddha_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: clean mandala with unbroken mirror
- Notes: Balanced sacred-symbol composition emphasizing legitimacy and clarity rather than conflict.
- Asset status: `complete`

### `holy_realm_debate_the_pretender`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_DEBATE_THE_PRETENDER`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_debate_the_pretender_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_debate_the_pretender.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_debate_the_pretender_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_debate_the_pretender_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_debate_the_pretender.dds`
- Final DDS grey: `gfx/achievements/holy_realm_debate_the_pretender_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_debate_the_pretender_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: two seated figures divided by a cracked wheel
- Notes: Debate remains readable because the figures are broad silhouettes and the cracked wheel is centered between them.
- Asset status: `complete`

### `holy_realm_sangha_of_nations`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_SANGHA_OF_NATIONS`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_sangha_of_nations_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sangha_of_nations.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sangha_of_nations_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sangha_of_nations_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_sangha_of_nations.dds`
- Final DDS grey: `gfx/achievements/holy_realm_sangha_of_nations_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_sangha_of_nations_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: ring of lamps around a mountain
- Notes: Circular lamp ring reinforces cohesion while the central mountain keeps the icon from dissolving into small details.
- Asset status: `complete`

### `holy_realm_mercy_in_the_ashes`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_MERCY_IN_THE_ASHES`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_mercy_in_the_ashes_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_mercy_in_the_ashes.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_mercy_in_the_ashes_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_mercy_in_the_ashes_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_mercy_in_the_ashes.dds`
- Final DDS grey: `gfx/achievements/holy_realm_mercy_in_the_ashes_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_mercy_in_the_ashes_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: hands lifting a lamp from ruins
- Notes: Relief-through-ruin contrast stays legible through a large flame shape and restrained rubble detail.
- Asset status: `complete`

### `holy_realm_sun_and_moon`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_SUN_AND_MOON`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_sun_and_moon_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sun_and_moon.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sun_and_moon_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_sun_and_moon_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_sun_and_moon.dds`
- Final DDS grey: `gfx/achievements/holy_realm_sun_and_moon_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_sun_and_moon_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: upward-reaching hand toward sun and moon over a mandala
- Notes: The hand, sun, and moon remain oversized enough to survive small-size viewing.
- Asset status: `complete`

### `holy_realm_lotus_bridge`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `HOLY_REALM_LOTUS_BRIDGE`
- Source mode: `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/source_png/holy_realm_lotus_bridge_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_lotus_bridge.png`
- Processed PNG grey: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_lotus_bridge_grey.png`
- Processed PNG not eligible: `docs/assets/003_holy_realm_buddhahood/achievement_icons/processed_png/holy_realm_lotus_bridge_not_eligible.png`
- Final DDS: `gfx/achievements/holy_realm_lotus_bridge.dds`
- Final DDS grey: `gfx/achievements/holy_realm_lotus_bridge_grey.dds`
- Final DDS not eligible: `gfx/achievements/holy_realm_lotus_bridge_not_eligible.dds`
- Target size: `64x64`
- Prompt summary: lotus path across water toward a safe shore
- Notes: Uses a bright lotus path over dark water to preserve route readability at icon size.
- Asset status: `complete`
