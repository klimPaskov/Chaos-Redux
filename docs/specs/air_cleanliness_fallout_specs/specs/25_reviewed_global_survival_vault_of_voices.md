# Reviewed Global Survival Event: The Vault of Voices

## Contract

The Vault of Voices is the twenty-fifth reviewed Fallout global-survival candidate.
It follows The Working Machine memory and selects one owned native state with a surviving archive, radio, or data facility surface.
The scheduler owns candidate `359`, transaction `710025`, route `7125`, and Event Log history `9130`.
The row stores one deterministic native state id and a weighted voice-archive score before delivery.

The opening presents four authored policies.

1. Preserve the archive without editing its recordings with Power, Medicine, and Recognition.
2. Curate a civic archive for the surviving settlements with Shelter, Medicine, and Cohesion.
3. Weaponize the archive as a controlled public narrative with Power, Scrap, and Recognition.
4. Trade verified copies with foreign partners with Scrap, Power, and Recognition.

Every policy has a human report, a hidden AI lane, a forty-two-day delayed result, a two-hundred-seventy-day archive callback, branch-specific result grades, memory, Event Log payloads, and authenticated cleanup.
The chain remains dormant while scheduler activation, host authority, save recovery, multiplayer delivery, and the full-screen Fallout blackout remain unproven.

## Gates and deterministic grading

The candidate requires the current Fallout registry, durable survival resources, a closed Working Machine memory, campaign day 1200 through 2999, Power at 18 or more, Scrap at 10 or more, Medicine at 6 or more, Recognition at 12 or more, Cohesion at 30 or more, exposure from 10 through 65, a surviving state population, and one affordable policy.
The selected state must be controlled by the owner, have a current produced Air Winter snapshot, and contain a non-damaged radar station or at least two levels of non-damaged infrastructure, with an industrial complex also accepted as a supporting archive site.
The voice score weights radar stations by three, infrastructure by one, and industrial complexes by one.
The highest score wins and the lowest native state id breaks exact ties.

At schedule time the chain freezes Power, Scrap, Medicine, Cohesion, Recognition, the selected state id, the selected branch, and the registry generation.
Outcome grading combines the frozen Power, Scrap, Medicine, Cohesion, and Recognition values with a one hundred point clamp.
Each policy has its own success and partial thresholds.
Result failure removes a small state population share through the Deaths contract at 0.022 percent of remaining population.
Callback failure uses 0.011 percent.

## Player and AI behavior

Human choices are visible only while the ordinary receipt, target state, country registry, owner, generation, and branch cost remain valid.
The hidden AI lane prefers preservation when Recognition is strong, curation when Cohesion is strong, weaponization when Power is strong, and trading when Scrap is strong.
It falls back through affordable branches and uses the same delayed result, callback, memory, Event Log, and cleanup effects as a human choice.

The result and callback authenticate ticket, event token, branch, mode, generation, owner, country registry, and continued ownership of the selected state.
An invalid receipt is cancelled and frozen country values are released.
Cleanup releases the callback receipt first, then the result receipt, preserves the selected state's archive memory, and clears all transaction variables.

## Numerical surfaces

Success returns Power, Scrap, Medicine, Recognition, Cohesion, Stability, and War Support and adds a branch-specific state research, local supply, resource, or legitimacy modifier.
Partial results return smaller resources while increasing exposure and leaving the archive politically contested.
Failure reduces resources and political cohesion, raises exposure, damages one surviving archive facility, applies an unsafe modifier, and routes population loss through Deaths.
The callback can renew a public archive, preserve a disputed copy, or close the vault after a second trust and contamination burden.

## Event Log and assets

History `9130` has twelve branch and outcome payloads plus three callback outcomes.
Detail localisation is provided by `GetFalloutEvent359EventLogDetail` and shared Event Log name and detail mappings.
The dedicated report image shows a frost and ash covered archive room with radio reels, a relay console, paper labels, and three workers listening beside a dim transmitter.
The source, processed preview, DDS hash, and GFX handoff belong under `docs/assets/air_cleanliness_fallout/fallout_vault_of_voices/`.

The state modifiers use reviewed existing icons.
`GFX_idea_generic_research_bonus` marks preserved or weaponized records.
`GFX_idea_013_disaster_recovery_mobilization` marks curated, traded, or partial archive service.
`GFX_idea_country_without_breath` marks unsafe service.
The report sprite is `GFX_report_event_fallout_vault_of_voices` in `interface/fallout_world_end.gfx` and points to `gfx/event_pictures/fallout_world_end/report_event_fallout_vault_of_voices.dds`.

## Future expansion

Later reviewed candidates may turn a preserved archive into an old-world trial, a cultural revival, a disinformation crisis, a foreign truth commission, or a character chain for the surviving radio crew.
Those consumers remain separate candidates with their own gates, memories, assets, and audits.
This chain does not silently activate them.
