# Reviewed Global Survival Chain: Shelter Marriage Law

Status: implemented as dormant candidate `303`. It is not scheduler activation
approval and does not count toward the 660-block release floor.

## Purpose

After the Empty Ward closes, households in a surviving shelter need a usable
rule for partners, guardians, ration inheritance, and citizenship. This chain
turns that pressure into a country-level Fallout memory rather than a generic
political-power purchase.

## Eligibility and grading

The candidate requires the current Fallout country row and durable survival
resources, the closed Empty Ward memory, generation count at least two, campaign
day 720 through 1500, Cohesion at least 35, Food at least 20, Shelter at least
35, Recognition at least 20, and one affordable policy. Candidate severity is
recorded civilian Deaths multiplied by 0.00025 and clamped to the scheduler
range. The mechanic-pressure field is zero. Cohesion supplies the country state
value and Food supplies the required resource field.

The delayed result freezes Cohesion, Food, Shelter, Recognition, generation
count, and durable legitimacy, integration, fertility, and exposure ledgers.
Viability weights are Cohesion 30, Food 25, Shelter 25, and Recognition 20.
Each law has separate success and partial thresholds. Failure is deterministic
and cannot be selected by a random or MTTH branch.

## Authored laws

1. Civil marriage writes one public household code for every shelter.
2. Communal contracts let neighborhood councils witness guardianship and
   ration inheritance close to the families involved.
3. Religious authority lets recognized congregations keep the marriage books
   while the state protects the resulting identity.
4. No state role protects a narrow register and leaves private custom outside
   government control.

Every law has success, partial, and failure text. Results update Food, Medicine,
Power, Recognition, Cohesion, stability, war support, manpower, durable
legitimacy, integration, fertility, exposure, policy memory, timed modifiers,
and the Event Log. Failure routes population loss through the shared Deaths
contract at 0.08 percent of each owned state's population. The callback uses
0.04 percent on failure and closes the family-law memory.

## Cleanup and boundaries

The result and callback use exact issued ticket wrappers. Callback cleanup
prepares result cleanup only after its own ticket is released. Cleanup retains
the selected policy, legitimacy, integration, fertility, exposure, and memory
flags while clearing registry, frozen ledgers, branch, result, callback, and
transient flags. It does not activate the Fallout scheduler, host authority,
save recovery, or multiplayer behavior.

## Assets and localisation

The dedicated generated report image uses the repository 210 by 176 report-card
workflow. Runtime sprite registration is `GFX_report_event_fallout_shelter_marriage_law`
in `interface/fallout_world_end.gfx`, with source, processed preview, DDS,
manifest, and handoff under `docs/assets/air_cleanliness_fallout/fallout_shelter_marriage_law/`.
The player-facing text is concrete to shelter registries, ration inheritance,
guardianship, and cross-shelter identity. It does not use working labels.
