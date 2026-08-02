# Reviewed Global Survival Event: The Manual Nobody Read

## Contract

The Manual Nobody Read is the twenty-third reviewed Fallout global-survival candidate.
It follows the closed Dead City Permit memory and selects one owned technical facility in a native state with a surviving industrial complex or arms factory.
The scheduler owns candidate `345`, transaction `710023`, route `7123`, and Event Log history `9128`.
The row stores one deterministic native state id and a weighted facility score before delivery.

The opening presents four authored policies.

1. Follow the surviving procedure with Power, Scrap, and Medicine.
2. Improvise with the tools at hand using Power and Scrap.
3. Recruit an engineer from abroad with Power, Medicine, and Recognition.
4. Seal the facility and ration its shelter with Shelter Capacity, Filters, and Scrap.

Every policy has a human report, a hidden AI lane, a thirty-five-day delayed result, a two hundred forty-day inspection callback, branch-specific result grades, memory, Event Log payloads, and authenticated cleanup.
The selected state receives facility, reclamation, supply, exposure, building, and Deaths consequences.
The chain remains dormant while scheduler activation, host authority, save recovery, multiplayer delivery, and the full-screen Fallout blackout remain unproven.

## Gates and deterministic grading

The candidate requires the current Fallout registry, durable survival resources, a closed Dead City Permit memory, campaign day 820 through 2199, Power at 14 or more, Scrap at 12 or more, Medicine at 8 or more, Recognition at 10 or more, Cohesion at 25 or more, exposure from 18 through 69, a surviving state population, and one affordable policy.
The selected state must be controlled by the owner, have a current Air Winter snapshot, and contain at least one non-damaged industrial complex or arms factory.
Facility score weights an industrial complex by two and an arms factory by one.
The highest score wins and the lowest native state id breaks exact ties.

At schedule time the chain freezes Power, Scrap, Medicine, Cohesion, Recognition, the selected state id, the selected branch, and the registry generation.
Outcome grading combines the frozen Power, Scrap, Medicine, and Cohesion values with a one hundred point clamp.
Each policy has its own success and partial thresholds.
Result failure removes a small state population share through the Deaths contract at 0.03 percent of remaining population.
Callback failure uses 0.014 percent.

## Player and AI behavior

Human choices are visible only while the ordinary receipt, target state, country registry, owner, generation, and branch cost remain valid.
The hidden AI lane prefers the verified manual when Power is strong, then improvisation when Scrap is strong, foreign recruitment when Recognition is strong, and sealing when Cohesion is strong.
It falls back through affordable branches and uses the same delayed result, callback, memory, Event Log, and cleanup effects as a human choice.

The result and callback authenticate ticket, event token, branch, mode, generation, owner, country registry, and continued ownership of the selected state.
An invalid receipt is cancelled and frozen country values are released.
Cleanup releases the callback receipt first, then the result receipt, preserves the selected state's facility memory, and clears all transaction variables.

## Numerical surfaces

Success returns Power, Scrap, Medicine, Recognition, Cohesion, Stability, and War Support and adds a state production and research modifier.
Partial results return smaller resources while increasing exposure and leaving the facility fragile.
Failure reduces resources and political cohesion, raises exposure, damages one surviving facility building, applies an unsafe modifier, and routes population loss through Deaths.
The callback can renew the facility protocol, retain one limited service room, or abandon the site after a second contamination burden.

## Event Log and assets

History `9128` has twelve branch and outcome payloads plus three callback outcomes.
Detail localisation is provided by `GetFalloutEvent345EventLogDetail` and shared Event Log name and detail mappings.
The dedicated report image shows an ash-frosted technical station, safety lamps, an incomplete staff board, three workers, and a ring-bound maintenance manual.
The source, processed preview, DDS hash, and GFX handoff belong under `docs/assets/air_cleanliness_fallout/fallout_manual_nobody_read/`.

The state modifiers use reviewed existing icons.
`GFX_idea_generic_research_bonus` marks a verified or sealed protocol.
`GFX_idea_013_disaster_recovery_mobilization` marks a partial protocol.
`GFX_idea_country_without_breath` marks unsafe service.
The report sprite is `GFX_report_event_fallout_manual_nobody_read` in `interface/fallout_world_end.gfx` and points to `gfx/event_pictures/fallout/report_event_fallout_manual_nobody_read.dds`.

## Future expansion

Later reviewed candidates may turn a renewed technical facility into a regional power compact, a foreign engineer character, or a successor-state industrial identity.
Those consumers remain separate candidates with their own gates, memories, assets, and audits.
This chain does not silently activate them.
