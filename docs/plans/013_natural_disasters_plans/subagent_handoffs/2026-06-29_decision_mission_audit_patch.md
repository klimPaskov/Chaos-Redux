# Event 013 decision and mission audit patch handoff

## Changed files

- `common/decisions/013_natural_disasters_decisions.txt`
- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

## Changed ids

- All `nd_*_mission` selectable aftermath missions now use family-tuned mission timer constants and have `ai_will_do`.
- `natural_disasters_decision_cost.mission_days_fast`
- `natural_disasters_decision_cost.mission_days_short`
- `natural_disasters_decision_cost.mission_days_standard`
- `natural_disasters_decision_cost.mission_days_coastal`
- `natural_disasters_decision_cost.mission_days_heavy`
- `natural_disasters_decision_cost.mission_days_regional`
- `natural_disasters_set_profile_for_active_family`
- `natural_disasters_clear_target_family_categories_if_inactive`
- `natural_disasters_cleanup_inactive_country_categories`
- `nd_cost_evacuation_text`, `nd_cost_evacuation_text_blocked`, `nd_cost_evacuation_text_tooltip`
- `nd_cost_engineers_text`, `nd_cost_engineers_text_blocked`, `nd_cost_engineers_text_tooltip`
- `nd_cost_relief_text`, `nd_cost_relief_text_blocked`, `nd_cost_relief_text_tooltip`
- `nd_cost_shelter_text`, `nd_cost_shelter_text_blocked`, `nd_cost_shelter_text_tooltip`

## Before and after behavior

Before, every aftermath mission used the same 120 day timeout. AI weights were present on recovery decisions, but not on the selectable mission blocks themselves. Mission failure population loss copied the active family id, then used the default flood profile values for loss-rate setup. Family category flags only cleared when every aftermath state in the country was gone.

After, aftermath missions use varied constants by family severity and expected recovery complexity. Each selectable mission has a moderate AI completion weight with a wartime urgency modifier. Mission failure loss now loads the active family profile before preparing the percentage-based loss rate. Category cleanup now checks each disaster family and clears stale family category flags while preserving any caller recovery target.

## Validation

- Counted 21 selectable missions and 21 mission-level `ai_will_do` blocks.
- Confirmed no mission still uses the old shared `natural_disasters_decision_cost.mission_days` timeout.
- Confirmed aftermath failure path loads `natural_disasters_set_profile_for_active_family` before `natural_disasters_prepare_loss_rate` and `natural_disasters_register_state_population_loss`.
- Confirmed all four custom cost text bases have matching `_blocked` and `_tooltip` localisation keys.
- Checked patched script files for unsupported comparison operators and whitespace errors.

## Remaining parent fixes

- The current decision surface is still a scaffold for many families. Most family categories have one warning action, one recovery action, and one mission. The spec calls for deeper family-specific values, more distinct choices, partial outcomes, and regional objectives.
- Mission objectives are mostly resource-payment completion gates. A parent pass should add family objectives tied to ports, rail corridors, supply nodes, shelter coverage, state control, local support, or affected-state count.
- Heat routing only guards against the country idea `heat_wave`. If Event 51 uses another active marker, add a shared scripted trigger so Event 13 heat cannot stack with Event 51 under that marker.
- Severe storm, drought, landslide, and skyfall subcategory cleanup is family-level. If variant-specific simultaneous incidents become common, add variant-aware target checks before claiming full category lifecycle completion.
