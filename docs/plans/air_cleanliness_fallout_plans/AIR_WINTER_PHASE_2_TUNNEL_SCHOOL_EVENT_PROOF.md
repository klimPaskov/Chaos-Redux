# Air Winter Phase 2 Tunnel School Event Proof

## Implemented surface

The mountain-capital tranche adds two manually authored event blocks to `events/fallout_world_end_events.txt`:

- `chaosx.fallout.16`, Classes Beneath the Capital
- `chaosx.fallout.17`, The Tunnel Bell

The opening has three choices with exact click-time validation, government-aware AI, ledger-aware AI, branch memory, temporary industry consequences, a bound original owner, and a thirty-day result. The result has five mutually exclusive deterministic options. Every option repeats the matching branch and result condition before changing state.

The tranche raises the Air Winter pilot from 41 to 43 blocks. The pilot contains 127 options, of which 126 have effects. The remaining option is the existing stale-order acknowledgement.

These are internal Air Winter scheduler incidents under the dedicated Fallout namespace. They do not create a numbered public Chaos event or scenario catalog row, so the event workbook and its exported CSV files remain unchanged.

## Exact mountain-capital selection

`air_winter_event_is_mountain_capital` combines the state presentation trigger `air_winter_presentation_is_highland` with the documented state trigger `is_capital = yes`. The Phase 2 route selector checks this exact identity before the generic city classifier. Mountain capitals therefore reach id 16 even when their state category is city, large city, metropolis, or megalopolis. Non-capital highland and polar states continue to use id 14.

The same selector records ordinary Phase 2 candidates and first-frost marker rows. Both candidate allowlists include typed id 16. The id freezes the identity at selection time. A first-frost event can still open if the capital moves before dispatch, but the saved state must remain highland, valid, and owned by the saved original country.

Installed engine references:

- `documentation/triggers_documentation.md` documents `is_capital` for state scope
- `common/scripted_triggers/fallout_consolidated_triggers.txt` owns the reviewed highland presentation class
- `common/scripted_effects/fallout_consolidated_effects.txt` routes Phase 2 candidates before candidate scoring

`has_terrain = mountain` is not used. Its documented scope does not provide the required state classifier.

## Schools, shelter, and industry

The engine has no school or shelter building. Tunnel schools are represented through branch flags, durable state memory, the existing Shelter Capacity ledger, and two temporary state dynamic modifiers.

- civic tunnel conversion uses `local_factories = -0.20`
- alternating school and workshop shifts use `local_factories = -0.10`
- both modifiers use a 31-day maximum duration and are removed by the 30-day result

The extra day ensures the industrial cost remains active until the delayed report resolves. Cancellation also removes both modifiers.

Installed engine references:

- `documentation/effects_documentation.md` documents `add_dynamic_modifier` for state scope and accepts a variable duration
- `documentation/modifiers_documentation.md` documents `local_factories` for state scope
- vanilla `common/dynamic_modifiers/0_dynamic_modifiers.txt` and `wuw_dynamic_modifiers.txt` use `local_factories` in state dynamic modifiers

## Population-loss consequence

Successful civic conversion, settled shared shifts, and a successful cellar network write `air_winter_memory_tunnel_school_protection`. The established monthly Air Winter population calculation checks this state memory after its normal exposure, food, shelter, infrastructure, occupation, and adaptation multiplier. It then multiplies the resulting death percentage by `constant:air_winter_deaths.tunnel_school_protection_multiplier`, which is 0.90.

This route therefore lowers the monthly civilian loss rate even when the shelter gain does not move the state above the separate low-shelter threshold. Applied deaths still use the shared exact state civilian-loss helper and Deaths reason 17. No new casualty path or Fallout survival coefficient is introduced.

## Deterministic result boundaries

Civic conversion succeeds when Building Damage Pressure is no more than 65 and Disease Pressure is no more than 65. The opening adds 15 Building Damage Pressure, so AI plausibility uses a pre-choice ceiling of 50.

The cellar network succeeds when Adaptation is at least 25 and Exposure is no more than 55. The opening adds 6 Adaptation and 1 Exposure, so AI plausibility uses pre-choice Adaptation 19 and Exposure 54.

Shared shifts use a fixed middle result. All five result branches apply distinct ledger consequences and durable result memory. No random list, MTTH roll, or hidden fallback selects an outcome.

## Affordability and AI

Civic conversion requires 500 manpower and 30 support equipment. Shared shifts require 200 manpower and 15 support equipment. The option trigger and click guard repeat the same values before payment. Dispersed cellar schools remain available and cost 1 percent Stability.

Democratic and communist governments favor civic conversion. Neutral governments and countries at peace favor shared shifts. Fascist governments and countries at war favor dispersed cellars. State shelter, building pressure, and the derived delayed-result boundaries modify these preferences. The result exposes only one option for the stored branch and state condition, so AI countries resolve the same deterministic transaction as the player.

## Delayed ownership and Fallout isolation

Every opening writes its branch before `air_winter_event_refresh_state` binds the pending owner. The delayed result requires the regular state target, regular country target, matching stored owner, current ownership, valid highland state, and one exact branch flag.

Branch cancellation clears all three tunnel branch flags, both temporary industry modifiers, the pending flag, and the stored owner. State reset also clears opening memory, result memory, and the shared population-protection memory. During the existing Fallout snapshot state pass, Air Winter values are frozen before pending chains are cancelled. A late tunnel result cannot mutate the frozen Fallout row.

Installed engine references:

- the offline Data structures page documents regular event targets across events fired by the same effect chain
- `documentation/effects_documentation.md` documents `save_event_target_as`
- `documentation/triggers_documentation.md` documents `has_event_target`

## Assets and text

Both blocks use `GFX_report_event_air_winter_phase_2`. Both temporary industry modifiers use `GFX_air_winter_phase_2`. The sprites and DDS files already live under dedicated Air Winter and Fallout paths. The asset manifest maps Phase 2 consumers through id 17. No zombie asset, sound, sprite, file, or path is used.

All titles, descriptions, choices, result descriptions, and exact tooltips are present in the Fallout event localisation file. The two new dynamic modifiers are localized in the Air Winter localisation file. Text names the affected state and uses the established government-aware authority term.

## Runtime boundary

Static source review proves typed-id wiring, selection order, state scope, trigger thresholds, temporary modifier registration, option affordability, branch cleanup, monthly Deaths integration, localisation keys, and dedicated asset references. It does not prove popup presentation, delayed regular-target retention, local factory behavior, AI choice behavior, save recovery, or monthly population results in a live session. Hearts of Iron IV was not launched, and no runtime claim is made.
