# Holy Realm Buddhahood Progression

## Overview

The Holy Realm route uses the existing `003_the_holy_realm` event package and adds a Buddhahood progression layer on top of the earlier Mandala counters.

The older counters remain active:

- `spiritual_legitimacy`
- `compassion_drift`
- `mandala_reach`
- `final_silence_pressure`
- `bodhisattva_bhumi`

The Buddhahood layer adds:

- `bodhi_progress`, capped at 108.
- `dhyana_depth`, capped at 4.
- `compassion`, capped at 100.
- `detachment`, capped at 100.
- `defilements`, capped at 100.
- `meditation_charge`, capped at 100.
- `world_suffering`, initialized from the Chaos Meter.
- `sangha_cohesion`, initialized from Spiritual Legitimacy.
- `teaching_successes`.
- `crisis_teaching_successes`.

Tuning is centralized in `common/script_constants/003_holy_realm_constants.txt` under `holy_realm_buddhahood`.

## Flow

1. Holy Realm formation initializes the older Mandala counters and the Buddhahood counters.
2. Existing Bodhisattva bhumi advancements also record teaching success, add Bodhi, improve Compassion, and reduce Defilements.
3. Teaching success during major chaos pressure records `crisis_teaching_successes`.
4. `THR_buddha_mandate` is localized as `The Unshaken Seat` and marks `holy_realm_focus_unshaken_seat`.
5. Buddhahood requires:
   - `bodhi_progress >= 108`
   - `dhyana_depth >= 4`
   - `defilements < 20`
   - `teaching_successes >= 12`
   - `crisis_teaching_successes >= 1`
   - `holy_realm_focus_unshaken_seat`
   - sovereignty and no previous Buddhahood
6. If Bodhi is complete while Defilements remain severe, the route records `holy_realm_false_buddha_schism_pressure` and applies a stability hit.
7. Buddhahood sets `holy_realm_buddhahood_attained`, uses the existing Buddha stage effect, applies the Buddha idea, and shows `The Awakened One` super-event slot.

## Meditation Fallback

HOI4 decisions do not support literal three-minute mouse holding, so the implemented fallback is a concentration sequence:

1. `Begin the Concentration Vow`
2. `Hold Intention`
3. `Hold Energy`
4. `Hold Mind`
5. `Hold Investigation`

The four hold decisions must be completed while the sequence flags are active. Completion grants Bodhi, Detachment, Meditation Charge, and can advance Dhyana if enough Meditation Charge is present.

## Buddha Powers

After Buddhahood, the `Powers of the Awakened` decision category appears. Powers spend Meditation Charge and target only countries passing `is_holy_realm_chaos_enemy`.

Valid chaos enemies include zombie outbreak countries, weaponized zombie countries, Great Revolution chaos states, alien or nonhuman chaos polities, and countries explicitly marked with chaos-country flags. Ordinary countries are intentionally excluded.

The implemented powers are:

- One Becomes Many
- Passing Through Walls
- Walking on Water
- Vanishing from Sight
- Seated in the Sky
- Touching the Sun and Moon
- Extinction of Defilements

Using any ordinary power sets `holy_realm_buddha_power_demonstrated`. The first Buddha power also shows the `Powers of the Awakened` super-event once per campaign. `Extinction of Defilements` is a self-targeted rite rather than an enemy debuff: it requires full Meditation Charge, Dhyana Depth 4, Defilements below 10, Buddhahood, and one previous anti-chaos power display. Completing it sets `holy_realm_final_silence_extinction_rite_completed`.

## Final Silence Split

Final Silence now has a ritual gate and an outcome gate.

The ritual can begin when the Holy Realm has Buddhahood, the final doctrine path, Final Silence armed and dominant in the doctrine balance, a controlled capital, no active False Buddha Schism, a previous anti-chaos power display, and the Extinction of Defilements rite.

If global Chaos is above 1000 and no other world-end is active or disabled, completion sets the terminal Final Silence world-end flags and shows the terminal `The Final Silence` super-event. If the world-end gate is not met, completion instead records `holy_realm_final_silence_nonterminal_completed`, changes the leader name to `The Empty Seat`, shows the non-terminal `The Final Silence` super-event, and leaves the world alive for reconstruction play.

## Achievement Tracking Hooks

The route now records achievement-ready flags without adding daily or monthly scans:

- `holy_realm_defilements_exceeded_clean_buddhahood_limit` is set if Defilements exceed 50 after Bodhi reaches 75.
- `holy_realm_four_dhyanas_under_fire_ready` is set when Dhyana Depth 4 is reached while the capital is controlled and a chaos enemy is at war with the Realm.
- `holy_realm_power_one_becomes_many_active` opens a timed mission window. Teaching successes during that window count toward `holy_realm_one_becomes_many_achievement_ready`.
- `holy_realm_ordinary_conquest_abuse` is set when the Realm declares war on a normal non-chaos country.
- `holy_realm_helped_defeat_chaos_country`, `holy_realm_wall_river_sky_achievement_ready`, and `holy_realm_sun_moon_achievement_ready` are set from capitulation outcomes involving chaos enemies.
- `holy_realm_capital_sanctuary_recently_fallen` is a timed 180-day flag set from `on_state_control_changed` when the capital sanctuary falls.
- `holy_realm_final_silence_world_end_achievement_ready` is set by terminal Final Silence only if the capital is controlled, has not recently fallen, and global Chaos is above 1000.
- `holy_realm_empty_seat_achievement_ready` is set by non-terminal Final Silence when the Empty Seat remains faction leader with at least three surviving faction members.
- `holy_realm_mercy_in_ashes_achievement_ready` is set after five tracked relief/refugee missions while Defilements remain below 20, with at least one credit from a threatened-capital or defensive-interposition mission.
- `holy_realm_sangha_of_nations_watch_started` records when the Mandala of Nations has at least eight non-chaos, non-puppet members and Sangha Cohesion is at least 70. The achievement checks that the watch has remained valid for 180 days.
- `holy_realm_lotus_bridge_watch_started` records the protected target for the Lotus Bridge relief power. The achievement checks that the saved target still exists, keeps its capital, and has remained protected for 180 days.

The achievement file now defines all 12 Buddhahood achievement ids from the spec. One id is intentionally gated behind a future readiness flag because its underlying system is not yet implemented:

- `holy_realm_false_buddha_debate_achievement_ready` for `Debate the Pretender`.

Two achievement definitions use the strongest currently available route evidence rather than a dedicated new subsystem:

- `No Empire of the Wheel` treats `Vow Against Annihilation` plus final-doctrine renunciation as the clean-route equivalent.
- `The Sun and Moon Were Within Reach` currently requires activation during world-collapse chaos pressure and a 365-day anti-chaos victory; the separate "two chaos sources or major capital" proof is not yet tracked.

## UI And Assets

The Holy Mandala decision GUI reuses `holy_realm_mandala_category_scripted_gui` and now displays:

- Spiritual Legitimacy
- Bodhi
- Dhyana
- Teaching successes
- Meditation Charge
- Defilements
- Chaos and Final Silence Pressure

Super-event presentation uses these wired slots:

- `The Awakened One`: slot 7, `GFX_super_event_buddha_mandate`, `music/super_event_buddha_mandate.ogg`, `sound/chaosx_super_event_buddha_mandate.wav`.
- `The Final Silence` non-terminal: slot 8, `GFX_super_event_final_silence`, `music/super_event_final_silence.ogg`, `sound/chaosx_super_event_final_silence.wav`.
- `The Final Silence` terminal: slot 9, `GFX_super_event_final_silence_thermonuclear`, `music/super_event_final_silence_thermonuclear.ogg`, `sound/chaosx_super_event_final_silence_thermonuclear.wav`.
- `Powers of the Awakened`: slot 61, `GFX_super_event_powers_of_the_awakened`, `music/super_event_powers_of_the_awakened.ogg`, `sound/chaosx_super_event_powers_of_the_awakened.wav`.

The `Powers of the Awakened` super-event currently uses `gfx/super_events/super_event_powers_of_the_awakened.dds`, copied from the existing Buddha Mandate image as a safe placeholder. Replace it with bespoke art when the final super-event image package is produced.

The audio source and rights record is in `docs/assets/003_holy_realm_buddhahood/audio_research/holy_realm_buddhahood_super_event_audio_research.md`. The `Powers of the Awakened` recording is CC BY 3.0 and requires attribution; the terminal Final Silence recording remains the only medium-confidence public-domain-chain item in the current package.

The Buddhahood achievement icon package is tracked under `docs/assets/003_holy_realm_buddhahood/achievement_icons/`, with package notes in `docs/assets/003_holy_realm_buddhahood/manifest.md` and `.gfx` handoff details in `docs/assets/003_holy_realm_buddhahood/gfx_handoff.md`. The final completed, grey, and not-eligible DDS triplets live in `gfx/achievements/holy_realm_*.dds` and are registered in `interface/chaosx_achievements.gfx`.

The new decision category reuses `GFX_decision_category_holy_mandala`; the new decisions use existing generic decision icons. Future bespoke art should use:

- Folder: `gfx/interface/decisions/holy_realm/`
- GFX file: `interface/003_holy_realm.gfx`
- Suggested icon names:
  - `GFX_decision_holy_realm_concentration_vow`
  - `GFX_decision_holy_realm_buddha_power`
  - `GFX_decision_category_holy_realm_buddha_powers`

## Future Plans

- Replace `gfx/super_events/super_event_powers_of_the_awakened.dds` with bespoke `Powers of the Awakened` super-event art.
- Consider replacing the terminal Final Silence audio if the project wants only explicit modern license grants and no public-domain-chain ambiguity.
- Add stage-specific mandala and portrait animation assets for Dhyana and Buddhahood.
- Expand `holy_realm_false_buddha_schism_pressure` into the full False Buddha Schism evolution.
- Implement the False Buddha debate system so its achievement-ready flag can be set from gameplay.
- Audit the focus tree for a dedicated visual route around `The Unshaken Seat`, rather than relying on the existing focus id.
