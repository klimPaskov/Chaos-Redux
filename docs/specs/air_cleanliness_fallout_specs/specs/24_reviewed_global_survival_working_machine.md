# Reviewed Global Survival Event: The Working Machine

## Contract

The Working Machine is the twenty-fourth reviewed Fallout global-survival candidate.
It follows the Manual Nobody Read memory and selects one owned automated facility in a native state with a surviving industrial complex, synthetic refinery, or arms factory.
The scheduler owns candidate `352`, transaction `710024`, route `7124`, and Event Log history `9129`.
The row stores one deterministic native state id and a weighted machine score before delivery.

The opening presents four authored policies.

1. Integrate the machine protocol into the civil authority with Power, Scrap, and Recognition.
2. Dismantle the machine for recoverable materials with Scrap, Shelter Capacity, and Filters.
3. Venerate the protocol council and preserve its operating rules with Medicine, Recognition, and Cohesion.
4. Isolate the facility behind a guarded perimeter with Power, Filters, and Medicine.

Every policy has a human report, a hidden AI lane, a forty-nine-day delayed result, a three-hundred-day inspection callback, branch-specific result grades, memory, Event Log payloads, and authenticated cleanup.
The chain remains dormant while scheduler activation, host authority, save recovery, multiplayer delivery, and the full-screen Fallout blackout remain unproven.

## Gates and deterministic grading

The candidate requires the current Fallout registry, durable survival resources, a closed Manual Nobody Read memory, campaign day 900 through 2399, Power at 18 or more, Scrap at 10 or more, Medicine at 6 or more, Recognition at 12 or more, Cohesion at 30 or more, exposure from 12 through 67, a surviving state population, and one affordable policy.
The selected state must be controlled by the owner, have a current produced Air Winter snapshot, and contain at least one non-damaged industrial complex, synthetic refinery, or arms factory.
The machine score weights industrial complexes by two, synthetic refineries by two, and arms factories by one.
The highest score wins and the lowest native state id breaks exact ties.

At schedule time the chain freezes Power, Scrap, Medicine, Cohesion, Recognition, the selected state id, the selected branch, and the registry generation.
Outcome grading combines the frozen Power, Scrap, Medicine, Cohesion, and Recognition values with a one hundred point clamp.
Each policy has its own success and partial thresholds.
Result failure removes a small state population share through the Deaths contract at 0.025 percent of remaining population.
Callback failure uses 0.012 percent.

## Player and AI behavior

Human choices are visible only while the ordinary receipt, target state, country registry, owner, generation, and branch cost remain valid.
The hidden AI lane prefers integration when Power is strong, dismantling when Scrap is strong, veneration when Recognition is strong, and isolation when Cohesion is strong.
It falls back through affordable branches and uses the same delayed result, callback, memory, Event Log, and cleanup effects as a human choice.

The result and callback authenticate ticket, event token, branch, mode, generation, owner, country registry, and continued ownership of the selected state.
An invalid receipt is cancelled and frozen country values are released.
Cleanup releases the callback receipt first, then the result receipt, preserves the selected state's machine memory, and clears all transaction variables.

## Numerical surfaces

Success returns Power, Scrap, Medicine, Recognition, Cohesion, Stability, and War Support and adds a branch-specific state production, supply, research, or resource modifier.
Partial results return smaller resources while increasing exposure and leaving the facility under a partial protocol.
Failure reduces resources and political cohesion, raises exposure, damages one surviving facility building, applies an unsafe modifier, and routes population loss through Deaths.
The callback can renew the chosen machine relationship, stabilize a partial protocol, or abandon the facility after a second contamination burden.

## Event Log and assets

History `9129` has twelve branch and outcome payloads plus three callback outcomes.
Detail localisation is provided by `GetFalloutEvent352EventLogDetail` and shared Event Log name and detail mappings.
The dedicated report image shows a frost and ash covered automated plant, warm service lamps, three winter-clad workers, a relay console, and a ruined civic tower.
The source, processed preview, DDS hash, and GFX handoff belong under `docs/assets/air_cleanliness_fallout/fallout_working_machine/`.

The state modifiers use reviewed existing icons.
`GFX_idea_generic_research_bonus` marks an integrated, venerated, or isolated protocol.
`GFX_idea_013_disaster_recovery_mobilization` marks a partial or dismantled protocol.
`GFX_idea_country_without_breath` marks unsafe service.
The report sprite is `GFX_report_event_fallout_working_machine` in `interface/fallout_world_end.gfx` and points to `gfx/event_pictures/fallout/report_event_fallout_working_machine.dds`.

## Future expansion

Later reviewed candidates may turn a renewed machine protocol into a machine polity contact, an automation crisis, a successor industrial identity, or a character chain for the surviving maintenance crew.
Those consumers remain separate candidates with their own gates, memories, assets, and audits.
This chain does not silently activate them.
