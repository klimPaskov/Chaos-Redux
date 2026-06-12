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
4. The focus tree exposes the main gates before `THR_buddha_mandate`:
   - Teaching route: `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, and `THR_many_lamps_one_flame`. `Many Lamps, One Flame` requires `teaching_successes >= 12` and `crisis_teaching_successes >= 1`.
   - Meditation route: `THR_sit_beneath_prayer_flags`, `THR_first_quiet`, `THR_second_quiet`, `THR_third_quiet`, and `THR_fourth_quiet`. Each quiet focus requires the corresponding `dhyana_depth` milestone from the concentration sequence.
   - Governance route: exactly one of `THR_council_of_abbots`, `THR_name_protector_regent`, or `THR_seat_pilgrim_assembly`.
5. `THR_buddha_mandate` is localized as `The Unshaken Seat`, requires those route gates in addition to the existing Arhat path prerequisites, and marks `holy_realm_focus_unshaken_seat`.
6. Buddhahood requires:
   - `bodhi_progress >= 108`
   - `dhyana_depth >= 4`
   - `defilements < 20`
   - `teaching_successes >= 12`
   - `crisis_teaching_successes >= 1`
   - `holy_realm_focus_unshaken_seat`
   - sovereignty and no previous Buddhahood
7. If Bodhi is complete while Defilements remain severe, the route records `holy_realm_false_buddha_schism_pressure` and applies a stability hit.
8. Buddhahood sets `holy_realm_buddhahood_attained`, uses the existing Buddha stage effect, applies the Buddha idea, and shows `The Awakened One` super-event slot.

## Meditation Sequence

The meditation route uses a concentration sequence because HOI4 scripted GUI exposes click effects, visibility, scripted properties, and tooltips, but does not provide a reliable continuous held-mouse timer for a 180-second channel. The implemented sequence preserves the required visible commitment without turning meditation into an instant purchase:

1. `Begin the Concentration Vow`
2. `Hold Intention`
3. `Hold Energy`
4. `Hold Mind`
5. `Hold Investigation`

The four hold decisions must be completed while the sequence flags are active. Each hold beat is a timed decision with its own Political Power cost, so the fallback remains a visible commitment rather than an instant purchase. The animated Dhyana Seal icon and meditation Mandala state mark the active vow. Completion grants Bodhi, Detachment, Meditation Charge, and can advance Dhyana if enough Meditation Charge is present.

## Buddha Powers

After Buddhahood, the `Powers of the Awakened` decision category appears. Powers spend Meditation Charge and target only countries passing `is_special_chaos_country`.

Valid chaos targets are read from the shared special-chaos-country classifier. Ordinary countries are intentionally excluded unless that shared trigger classifies them as a chaos country.

AI power use is tuned through `holy_realm_ai` script constants. The AI reserves charge when low, prioritizes current chaos war enemies and major chaos sources, and gives `Touching the Sun and Moon` its strongest push during world-collapse or major-crisis conditions. `Lotus Bridge` remains a lower-weight relief power for protected friendly targets rather than a chaos-enemy attack.

The implemented powers are:

- One Becomes Many
- Passing Through Walls
- Walking on Water
- Vanishing from Sight
- Seated in the Sky
- Touching the Sun and Moon
- Extinction of Defilements

Using any ordinary power sets `holy_realm_buddha_power_demonstrated`. The first Buddha power also shows the `Powers of the Awakened` super-event once per campaign. `Extinction of Defilements` is a self-targeted rite rather than an enemy debuff: it requires full Meditation Charge, Dhyana Depth 4, Defilements below 10, Buddhahood, and one previous anti-chaos power display. Completing it sets `holy_realm_final_silence_extinction_rite_completed`.

The post-Buddhahood focus branch exposes and paces the powers:

- `THR_the_awakened_one` requires realized Buddhahood and adds charge/detachment.
- `THR_show_the_powers` requires a demonstrated Buddha power against a valid chaos country.
- `THR_powers_are_not_toys` requires Detachment and sets `holy_realm_power_restraint_doctrine`, reducing ordinary Buddha power Meditation Charge cost from 20 to 15.
- `THR_read_pattern_suffering` records the Pattern of Suffering route from teaching evidence, chaos-front pressure, or the existing evolution.
- `THR_one_becomes_many_focus`, `THR_path_through_walls`, and `THR_lotus_bridge_focus` turn demonstrated powers into route payoffs for teaching, chaos-front movement, and compact relief.
- `THR_vanishing_from_sight_focus` and `THR_seated_in_sky_focus` give the stealth and emergency sky-display powers their own route payoffs before the capstone.
- `THR_touch_sun_moon_focus` is the anti-chaos capstone and now requires the full named-power lattice before it can complete.

## Final Silence Split

Final Silence has a ritual gate and an outcome gate.

The final focus sequence uses `THR_doctrine_last_war` as the Last Wheel, then requires `THR_witnesses_gather`, the Extinction of Defilements Buddha-power rite, and `THR_extinction_of_defilements_focus` before `THR_final_silence`.

The ritual can begin when the Holy Realm has Buddhahood, the final doctrine path, Final Silence armed and dominant in the doctrine balance, a controlled capital, no active False Buddha Schism, a previous anti-chaos power display, and the Extinction of Defilements rite.

If global Chaos is above 1000 and no other world-end is active or disabled, completion sets the terminal Final Silence world-end flags and shows the terminal `The Final Silence` super-event. If the world-end gate is not met, completion instead records `holy_realm_final_silence_nonterminal_completed`, changes the leader name to `The Empty Seat`, shows the non-terminal `The Final Silence` super-event, and leaves the world alive for reconstruction play.

## Achievement Tracking Hooks

The route records achievement-ready flags without adding daily or monthly scans:

- `holy_realm_defilements_exceeded_clean_buddhahood_limit` is set if Defilements exceed 50 after Bodhi reaches 75.
- `holy_realm_four_dhyanas_under_fire_ready` is set when Dhyana Depth 4 is reached while the capital is controlled and a chaos enemy is at war with the Realm.
- `holy_realm_power_one_becomes_many_active` opens a timed mission window. Teaching successes during that window count toward `holy_realm_one_becomes_many_achievement_ready`.
- `holy_realm_ordinary_conquest_abuse` is set when the Realm declares war on a normal non-chaos country.
- `holy_realm_helped_defeat_chaos_country`, `holy_realm_wall_river_sky_achievement_ready`, and `holy_realm_sun_moon_achievement_ready` are set from capitulation outcomes involving chaos enemies.
- `holy_realm_capital_sanctuary_recently_fallen` is a timed 180-day flag set from `on_state_control_changed` when the capital sanctuary falls.
- `holy_realm_final_silence_world_end_achievement_ready` is set by terminal Final Silence only if the capital is controlled, has not recently fallen, and global Chaos is above 1000.
- `holy_realm_empty_seat_achievement_ready` is set by non-terminal Final Silence when the Empty Seat remains faction leader with at least three surviving faction members.
- `holy_realm_mercy_in_ashes_achievement_ready` is set after five tracked relief/refugee missions while Defilements remain below 20, with at least one credit from a threatened-capital or defensive-interposition mission.
- `holy_realm_sangha_of_nations_watch_started` records when the Mandala of Nations has at least eight non-chaos, non-puppet members and Sangha Cohesion is at least 70. `holy_realm_sangha_of_nations_watch_maturing` times the watch using `@HOLY_REALM_SANGHA_OF_NATIONS_WATCH_DAYS`, mirrored to `constant:holy_realm_buddhahood.sangha_of_nations_watch_days`; invalid membership or cohesion clears the watch.
- `holy_realm_lotus_bridge_watch_started` records the protected target for the Lotus Bridge relief power. `holy_realm_lotus_bridge_watch_maturing` times the watch using `@HOLY_REALM_LOTUS_BRIDGE_WATCH_DAYS`, mirrored to `constant:holy_realm_buddhahood.lotus_bridge_watch_days`; the achievement checks that the saved global target still exists and keeps its capital.
- `holy_realm_false_buddha_schism_triggered`, `holy_realm_false_buddha_debate_resolved`, and `holy_realm_false_buddha_suppressed` distinguish the False Buddha Schism paths. `Debate the Pretender` requires the debate path and rejects suppression.
- The False Buddha Schism also opens a conditional focus branch after the evolution has been recorded. `THR_debate_the_pretender_focus` mirrors the clean debate path, `THR_exile_the_echo` removes the immediate pressure while leaving an abroad echo, `THR_break_false_mandala` mirrors suppression and raises chaos, and `THR_absorb_the_shadow` is a Totalen Chaos shortcut that raises Meditation Charge and Final Silence Pressure while recording a corrupted Buddhahood route.

The achievement file now defines all 12 Buddhahood achievement ids from the spec with gameplay-facing unlock conditions. `No Empire of the Wheel` uses the spec's allowed equivalent clean-route focus path: `Vow Against Annihilation`, Final Silence renunciation, no ordinary offensive conquest abuse, and a recorded anti-chaos victory.

`The Sun and Moon Were Within Reach` now records `holy_realm_sun_moon_crisis_proof` when Touching the Sun and Moon is activated during world-collapse chaos while at least two active chaos enemies exist, or while the targeted chaos source is a major or controls a major capital.

## UI And Assets

The Holy Mandala decision GUI reuses `holy_realm_mandala_category_scripted_gui` and displays:

- a central Mandala state image selected by `GetHolyRealmMandalaSprite`
- Spiritual Legitimacy
- Bodhi
- Dhyana
- Teaching successes
- Meditation Charge
- Defilements
- Chaos and Final Silence Pressure
- clickable Refuge, Arhats, Diplomacy, Doctrine, and Ledger tabs for contextual route text

The panel is attached to `holy_realm_mandala_category` through the decision-category scripted GUI path. Its interface container is `holy_realm_mandala_category_container` in `interface/chaosx_decisions.gui`; its scripted behavior is in `common/scripted_guis/chaosx_scripted_guis.txt`. A separate full-screen replacement panel can deepen presentation later, but the required live Mandala panel surface is the current decision-category GUI.

The Mandala states are registered in `interface/003_holy_realm.gfx`:

- `GFX_holy_realm_mandala_dormant`
- `GFX_holy_realm_mandala_dormant_animated`
- `GFX_holy_realm_mandala_teaching`
- `GFX_holy_realm_mandala_teaching_animated`
- `GFX_holy_realm_mandala_meditation`
- `GFX_holy_realm_mandala_meditation_animated`
- `GFX_holy_realm_mandala_awakened`
- `GFX_holy_realm_mandala_awakened_animated`
- `GFX_holy_realm_mandala_wrathful`
- `GFX_holy_realm_mandala_wrathful_animated`
- `GFX_holy_realm_mandala_final_silence`
- `GFX_holy_realm_mandala_final_silence_animated`
- `GFX_holy_realm_mandala_empty`
- `GFX_holy_realm_mandala_empty_animated`

Super-event presentation uses these wired slots:

- `The Awakened One`: slot 7, `GFX_super_event_buddha_mandate`, `music/super_event_buddha_mandate.ogg`, `sound/chaosx_super_event_buddha_mandate.wav`.
- `The Final Silence` non-terminal: slot 8, `GFX_super_event_final_silence`, `music/super_event_final_silence.ogg`, `sound/chaosx_super_event_final_silence.wav`.
- `The Final Silence` terminal: slot 9, `GFX_super_event_final_silence_terminal`, `music/super_event_final_silence_thermonuclear.ogg`, `sound/chaosx_super_event_final_silence_thermonuclear.wav`.
- `Powers of the Awakened`: slot 61, `GFX_super_event_powers_of_the_awakened`, `music/super_event_powers_of_the_awakened.ogg`, `sound/chaosx_super_event_powers_of_the_awakened.wav`.

The `Powers of the Awakened` super-event uses bespoke generated monochrome battlefield art at `gfx/super_events/super_event_powers_of_the_awakened.dds`. Source, prompt, processed PNG, and handoff notes live under `docs/assets/003_holy_realm_buddhahood/super_event_images/`.

The event-log evolution pane tracks four authored Buddhahood evolutions rather than the ordinary stage ladder:

- `Pattern of Suffering`: recorded after repeated successful teaching under chaos or world-end pressure.
- `False Buddha Schism`: recorded when high Defilements corrupt a Buddhahood attempt and the schism pressure begins.
- `Relic Mandala`: recorded after Mandala Reach or Sangha membership proves the Realm's sacred network outside the mountains.
- `Wrathful Protection`: recorded when the Sun and Moon crisis is answered through awakened anti-chaos protection.

Baseline states such as Mountain Refuge, Bodhisattva, Arhat Administration, Buddha Mandate, Divine Sovereignty, and Final Silence remain focus and country-flag stages. They do not create event-log evolution rows.

The audio source and rights record is in `docs/assets/003_holy_realm_buddhahood/audio_research/holy_realm_buddhahood_super_event_audio_research.md`. The `Powers of the Awakened` recording is CC BY 3.0 and requires attribution; the other current Holy Realm Buddhahood super-event recordings are CC0.

The Buddhahood achievement icon package is tracked under `docs/assets/003_holy_realm_buddhahood/achievement_icons/`, with package notes in `docs/assets/003_holy_realm_buddhahood/manifest.md` and `.gfx` handoff details in `docs/assets/003_holy_realm_buddhahood/gfx_handoff.md`. The final completed, grey, and not-eligible DDS triplets live in `gfx/achievements/holy_realm_*.dds` and are registered in `interface/chaosx_achievements.gfx`.

The new decision category reuses `GFX_decision_category_holy_mandala`; the new decisions use existing generic decision icons. Future bespoke art should use:

- Folder: `gfx/interface/decisions/holy_realm/`
- GFX file: `interface/003_holy_realm.gfx`
- Suggested icon names:
  - `GFX_decision_holy_realm_concentration_vow`
  - `GFX_decision_holy_realm_dhyana_seal`
  - `GFX_decision_holy_realm_dhyana_seal_animated`
  - `GFX_decision_holy_realm_buddha_power`
  - `GFX_decision_category_holy_realm_buddha_powers`

## Future Plans

- Keep the terminal Final Silence audio on the CC0 Heart Sutra recording unless a future pass deliberately changes the terminal tone.
- Static fallback Mandala and leader portrait stage DDS files are wired; all Mandala states plus the Buddha Mandate and Empty Seat leader portraits have animated frame sheets.
- Add deeper power-specific decision upgrades if later balance passes show the focus lattice needs more than route flags and Meditation Charge rewards.
- Expand `holy_realm_false_buddha_echo_abroad` into a full rival cult country or portrait-stage return chain if the exiled echo route needs a later foreign crisis.
- Audit the focus tree for a dedicated visual route around `The Unshaken Seat`, rather than relying on the existing focus id.
