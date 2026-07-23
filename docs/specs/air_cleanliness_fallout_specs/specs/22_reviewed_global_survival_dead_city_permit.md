# Reviewed Global Survival Event: The Dead City Permit

## Contract

The Dead City Permit is the twenty-second reviewed Fallout global-survival candidate.
It follows the closed Sealed Warehouse memory and selects one owned city or large-city state already graded as a dead city.
The scheduler owns candidate `338`, transaction `710022`, route `7122`, and Event Log history `9127`.
The candidate stores one deterministic native state id in the country registry and does not scan the world at event delivery time.

The opening uses four authored policies.

1. Send a state expedition with Scrap, Fuel, and Medicine.
2. License guilds with Scrap, Recognition, and Fuel.
3. Seize the city road with Scrap, Fuel, and Power.
4. Forbid entry with Shelter Capacity, Filters, and Scrap.

Each policy has a human report, a hidden AI lane, a twenty-eight-day delayed result, a two hundred ten-day permit review, a result memory, a callback memory, and authenticated cleanup.
The selected state receives the reclamation, supply, contamination, building, and Deaths consequences.
The chain remains dormant while scheduler activation, host authority, save recovery, multiplayer delivery, and the full-screen Fallout blackout remain unproven.

## Gates and deterministic grading

The candidate requires the current Fallout country registry, a durable survival resource row, the closed Sealed Warehouse memory, a city or large-city dead-state grade, exposure at 42 or more, at least one thousand people in the selected state, campaign day 730 through 2000, Scrap at 25 or more, Medicine at 14 or more, Fuel at 18 or more, Recognition at 12 or more, Cohesion at 20 or more, and one affordable policy.
Candidate selection takes the lowest eligible native state id.
The result grade is a weighted value from Scrap, Medicine, Fuel, and Cohesion.
The branch threshold changes by policy, so military seizure does not share the survey route's success test.

At schedule time the chain freezes Scrap, Medicine, Fuel, Cohesion, Recognition, the selected state id, and the registry generation.
Failure applies the Deaths contract to the selected state at 0.025 percent of remaining population.
Callback failure applies 0.012 percent.

## Player and AI behavior

Human choices are visible only when the ordinary receipt, country registry, selected state, and host country still match.
The hidden AI lane prefers a survey when all survey costs are affordable, then military seizure, licensed guilds, and finally exclusion.
The AI uses the same delayed result, callback, memory, and cleanup effects as a human choice.

The result and callback authenticate ticket, event token, branch, mode, generation, owner, country registry, and continued ownership of the selected state.
An invalid receipt is cancelled and frozen country values are released.
Cleanup releases the callback receipt first, then the result receipt, and preserves the selected state's durable permit memory while clearing transaction variables.

## Numerical surfaces

Success returns Scrap, Medicine, Fuel, Power, Recognition, Cohesion, stability, and War Support.
The selected state gains reclamation, local supply impact, and a permit modifier.
Partial results produce smaller gains and keep the road contested.
Failure damages infrastructure, raises exposure, reduces local supply, applies a contaminated modifier, and routes deaths through the Deaths system.
The callback can renew the permit, leave a partial road, or abandon the route with a second contamination burden.

## Event Log and assets

History `9127` has fifteen payloads covering four policy grades and three callback grades.
Detail localisation is provided by `GetFalloutEvent338EventLogDetail` and shared Event Log name and detail mappings.
The dedicated report image shows an ash-covered city checkpoint, an old truck, masked expedition workers, and a stamped permit.
The source, processed preview, DDS hash, and GFX handoff belong under `docs/assets/air_cleanliness_fallout/fallout_dead_city_permit/`.

The four state modifiers reuse reviewed vanilla-style modifier icons.
`GFX_idea_generic_research_bonus` is defined in existing idea GFX and marks a successful or renewed permit.
`GFX_idea_013_disaster_recovery_mobilization` is defined in `interface/013_natural_disasters.gfx` and marks a partial permit.
`GFX_idea_country_without_breath` is defined in `interface/chaosx_ideas.gfx` and marks contamination.
The report sprite is `GFX_report_event_fallout_dead_city_permit` in `interface/fallout_world_end.gfx` and points to `gfx/event_pictures/fallout_world_end/report_event_fallout_dead_city_permit.dds`.

## Future expansion

The next reviewed additions may turn a durable city claim into a scavenger character, a regional permit dispute, or a cause-memory chain about unknown military material.
Those consumers remain separate candidates and must receive their own gates, ledgers, assets, and audits.
This chain does not silently activate them.
