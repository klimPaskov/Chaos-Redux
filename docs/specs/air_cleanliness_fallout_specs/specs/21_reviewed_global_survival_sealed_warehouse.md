# Reviewed Global Survival Event: The Sealed Warehouse

## Contract

The Sealed Warehouse is the twenty-first reviewed Fallout global-survival candidate.
It is a country-level routine salvage incident after the Working Elevator memory closes.
It does not claim a state, province, character, or bilateral partner.
The scheduler owns candidate `331`, transaction `710021`, route `7121`, and Event Log history `9126`.

The opening uses four authored policies.

1. Open the warehouse at once and accept immediate exposure for visible stores.
2. Inspect under quarantine and spend medicine, filters, and power to separate useful medical stock from sealed drums.
3. Sell the coordinates through a licensed carrier contract and turn salvage access into public law.
4. Leave the doors sealed behind a filtered watch and preserve a future claim.

Each policy has a human report, a hidden AI lane, a twenty-one-day delayed result, a one hundred eighty-day callback, a result memory, a callback memory, and exact cleanup.
The country stays the owner across every receipt.
The chain is dormant while scheduler activation, host authority, save recovery, multiplayer delivery, and the full-screen Fallout blackout remain unproven.

## Gates and deterministic grading

The candidate requires a current Fallout country registry row, a durable survival resource row, the closed Working Elevator memory, the generation counter, Scrap at 28 or more, Medicine at 22 or more, Reclamation at 20 or more, Cohesion at 25 or more, Recognition at 15 or more, and campaign day 900 through 2400.
At least one branch must be affordable.
The scheduler uses the lowest eligible owner and its existing cooldown and generation receipts.

At schedule time the chain freezes Scrap, Medicine, Reclamation, Cohesion, Recognition, and five country ledgers.

- `fallout_warehouse_331_access`
- `fallout_warehouse_331_salvage`
- `fallout_warehouse_331_contamination`
- `fallout_warehouse_331_legitimacy`
- `fallout_warehouse_331_scavenger_reputation`

The grade is deterministic.
Viability is a weighted value from Scrap, Medicine, Reclamation, and Cohesion.
The selected policy also requires its policy resource threshold.
Success, partial, and failure have separate resource, cohesion, stability, War Support, ledger, memory, and timed-modifier outcomes.
Failure applies the Deaths contract at 0.02 percent of remaining state population.
Callback failure applies 0.01 percent.

## Player and AI behavior

Human choices are visible only after the current ordinary receipt and the country registry match.
The hidden AI lane chooses quarantine inspection first when Medicine, Filters, and Power support it.
It then prefers immediate opening, licensed coordinates, and finally a sealed watch.
Affordability fallbacks use the same branch order and never create a transaction with an unpaid cost.

The result and callback compare the issued ticket, event token, branch, mode, generation, owner, and registry target before effects run.
An invalid receipt is cancelled and its frozen variables are released.
Cleanup releases the callback receipt first, then the result receipt, and clears all chain-owned flags and frozen variables while preserving durable warehouse ledgers and memory flags.

## Numerical surfaces

The result updates Medicine, Scrap, Power, Filters, Recognition, Cohesion, stability, and War Support.
It also updates access, salvage, contamination, legitimacy, and scavenger reputation.
Inspection success reduces contamination while opening or bad contracts can raise it.
The callback gives a smaller continuation result and repeats the Deaths path on failure.
Six dynamic modifiers provide distinct policy and maintenance identities.

## Event Log and assets

History `9126` has fifteen payloads covering four policy grades and three callback grades.
Detail localisation is provided by `GetFalloutEvent331EventLogDetail`.
The dedicated report image is the fictional sealed warehouse, not a Zombie asset and not a reused pilot image.
Source, processed preview, DDS hash, and GFX handoff belong under `docs/assets/air_cleanliness_fallout/fallout_sealed_warehouse/`.

The six dynamic modifiers reuse reviewed vanilla-style idea icons.
`GFX_idea_generic_research_bonus` is defined in existing idea GFX and is used for inspection and maintenance surfaces.
`GFX_idea_013_disaster_recovery_mobilization` is defined in `interface/013_natural_disasters.gfx` and is used for immediate opening and sealed-watch surfaces.
`GFX_idea_country_without_breath` is defined in `interface/chaosx_ideas.gfx` and is used for licensed coordinates and failure surfaces.
The report sprite is `GFX_report_event_fallout_sealed_warehouse` in `interface/fallout_world_end.gfx` and points to `gfx/event_pictures/fallout/report_event_fallout_sealed_warehouse.dds`.

## Future expansion

The next reviewed additions may connect a successful warehouse claim to the Dead City Permit, a scavenger character, or a cause-memory chain about unknown military material.
Those consumers remain separate candidates and must receive their own gates, ledgers, assets, and audits.
This chain does not silently activate them.
