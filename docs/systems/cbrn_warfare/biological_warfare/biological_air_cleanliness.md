# Biological Air Cleanliness Integration

## Purpose

Ordinary biological outbreaks contribute to the existing global Air Cleanliness model only while an exact state has an active outbreak. Incubating seeds, rejected releases, covert preparation, idle biological stockpiles, and ordinary military activity do not contribute.

The contribution is a state-owned receipt keyed by the four stable biological agent slots. An affected state can therefore carry Anthrax, Plague, Tularemia, and Smallpox receipts at the same time without one agent overwriting another.

## Transition model

`common/scripted_effects/cbrn_biological_air_effects.txt` owns the biological component. `bio_lifecycle_set_current_agent_air_contribution` maps the active agent's current intensity to the accepted outbreak bands:

| Active intensity band | Air Cleanliness contribution | Gameplay meaning |
| --- | ---: | --- |
| Low, 20 through 39 | 1 basis point | Local active outbreak |
| Base, 40 through 59 | 3 basis points | Sustained regional outbreak |
| High, 60 and above | 5 basis points | Severe multi-state pressure |

These values are gameplay tuning with low historical confidence. They describe the Chaos Redux global meter rather than a measured atmospheric concentration.

The lifecycle calls the transition helper after a seed record is stored and after incubation activates an outbreak. Countermeasure successes, partial successes, and failures refresh each agent immediately after its intensity and exposed-share changes. Recovery clears the exact receipt and removes only that agent's contribution.

The contribution follows outbreak intensity, not weapon identity or delivery route. Tularemia, Anthrax, Plague, and Smallpox retain their distinct incubation, detection, spread, medical, evidence, death, and persistence profiles in the biological lifecycle. Deliberate delivery does not create an additional Air Cleanliness contribution for the same active outbreak.

## Settings and repair path

The existing Air Cleanliness toggle clears the chemical and biological component totals when disabled. Re-enabling the system calls the explicit `cbrn_chemical_rebuild_air_cleanliness_contributions` and `bio_lifecycle_rebuild_air_cleanliness_contributions` effects once, rebuilding receipts from exact state variables. These helpers are repair paths for a settings transition; they are not daily, weekly, monthly, or all-country periodic pulses.

The global meter exposes `global.air_contamination_bio_states`, `global.air_contamination_bio_bp`, and the derived `global.air_contamination_bio_percent`. The Chaos Meter popup shows the number of biological outbreak states and their contribution beside the chemical component. The existing winter and fallout model continues to consume the final global Air Cleanliness value; the biological component does not create a second meter.

## Engine and scope boundary

All ordinary updates are exact-state lifecycle transitions. No world scan is used to discover new outbreaks, and no continuous air or aircraft-presence estimator is used. The explicit rebuild is the only bounded `every_state` helper and is called only after the settings system is re-enabled.

The system does not infer agent activity from a seed, stockpile, division template, raid preparation, or a missing event target. A state must carry the corresponding `bio_agent_<slot>_active` flag before its intensity band can contribute.

## Related implementation surfaces

- Lifecycle state and agent hierarchy: `common/scripted_effects/biological_lifecycle_effects.txt` and `common/script_constants/biological_lifecycle_constants.txt`.
- Countermeasure transitions: `common/scripted_effects/biological_countermeasure_effects.txt`.
- Global meter integration: `common/scripted_effects/chaos_meter_effects.txt` and `interface/chaosx_chaos_meter_popup.gui`.
- Player-facing meter text: `localisation/english/chaosx_chaos_meter_l_english.yml`.
- Chemical component: `common/scripted_effects/cbrn_chemical_state_effects.txt`.

The five biological Air Cleanliness contribution thresholds and the global meter percentages require gameplay balance review after package scenario runs. They are not historical stockpile estimates or a substitute for the accepted disease lifecycle tuning.
