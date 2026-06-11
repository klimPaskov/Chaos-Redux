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
7. Buddhahood sets `holy_realm_buddhahood_attained`, uses the existing Buddha stage effect, applies the Buddha idea, and shows the existing Buddha super-event slot.

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

Using any ordinary power sets `holy_realm_buddha_power_demonstrated`. `Extinction of Defilements` is a self-targeted rite rather than an enemy debuff: it requires full Meditation Charge, Dhyana Depth 4, Defilements below 10, Buddhahood, and one previous anti-chaos power display. Completing it sets `holy_realm_final_silence_extinction_rite_completed`.

## Final Silence Split

Final Silence now has a ritual gate and an outcome gate.

The ritual can begin when the Holy Realm has Buddhahood, the final doctrine path, Final Silence armed and dominant in the doctrine balance, a controlled capital, no active False Buddha Schism, a previous anti-chaos power display, and the Extinction of Defilements rite.

If global Chaos is above 1000 and no other world-end is active or disabled, completion sets the terminal Final Silence world-end flags. If the world-end gate is not met, completion instead records `holy_realm_final_silence_nonterminal_completed`, changes the leader name to `The Empty Seat`, and leaves the world alive for reconstruction play.

## Achievement Tracking Hooks

The route now records achievement-ready flags without adding daily or monthly scans:

- `holy_realm_defilements_exceeded_clean_buddhahood_limit` is set if Defilements exceed 50 after Bodhi reaches 75.
- `holy_realm_four_dhyanas_under_fire_ready` is set when Dhyana Depth 4 is reached while the capital is controlled and a chaos enemy is at war with the Realm.
- `holy_realm_power_one_becomes_many_active` opens a timed mission window. Teaching successes during that window count toward `holy_realm_one_becomes_many_achievement_ready`.
- `holy_realm_ordinary_conquest_abuse` is set when the Realm declares war on a normal non-chaos country.
- `holy_realm_helped_defeat_chaos_country`, `holy_realm_wall_river_sky_achievement_ready`, and `holy_realm_sun_moon_achievement_ready` are set from capitulation outcomes involving chaos enemies.

## UI And Assets

The Holy Mandala decision GUI reuses `holy_realm_mandala_category_scripted_gui` and now displays:

- Spiritual Legitimacy
- Bodhi
- Dhyana
- Teaching successes
- Meditation Charge
- Defilements
- Chaos and Final Silence Pressure

No new sprite files are required for this tranche. The new decision category reuses `GFX_decision_category_holy_mandala`; the new decisions use existing generic decision icons. Future bespoke art should use:

- Folder: `gfx/interface/decisions/holy_realm/`
- GFX file: `interface/003_holy_realm.gfx`
- Suggested icon names:
  - `GFX_decision_holy_realm_concentration_vow`
  - `GFX_decision_holy_realm_buddha_power`
  - `GFX_decision_category_holy_realm_buddha_powers`

## Future Plans

- Replace the reused Buddha Mandate super-event copy with the spec's `The Awakened One` presentation once quote and licensed audio research are complete.
- Add stage-specific mandala and portrait animation assets for Dhyana and Buddhahood.
- Expand `holy_realm_false_buddha_schism_pressure` into the full False Buddha Schism evolution.
- Add achievement rows for the new Buddhahood and Buddha-power milestones.
- Audit the focus tree for a dedicated visual route around `The Unshaken Seat`, rather than relying on the existing focus id.
