# Reviewed archetype chain 80: Health Without Borders

## Status

This is a reviewed, dormant implementation row for the Quarantine state archetype. It follows a completed Open the Sealed City memory and turns a surviving clinic network into a regional health authority. The chain is a Fallout survivor consequence, not an ordinary event or super-event, and it does not create a country tag.

## State and timing contract

The candidate producer selects the lowest valid owned city or large-city state id. The state must remain controlled by the current country, retain current identity, survival, supply, and Air Winter rows, carry `fallout_event_740_memory_closed`, and keep bounded Exposure and Disease values. It must retain population, shelter, reclamation, supply access, and one repairable infrastructure level. The country must remain a current Quarantine government with durable Food, Medicine, Power, Recognition, Cohesion, and registry rows.

The chain is eligible from campaign day `1825` through day `9125`. Candidate `747` stores the state subject, transaction `710078`, route `7188`, and an explicit target state id. The opening freezes the country resources and state Shelter, Supply Access, Reclamation, infrastructure, Exposure, Disease, and population. Registry, delayed result, callback, and cleanup gates recheck owner, generation, state id, candidate id, and the committed reservation.

## Branches and outcomes

The human and hidden AI lanes share four authored branches.

1. Shared health compact funds one medicine register for the Ash Ward, North Gate, and outer clinics with Food, Scrap, and Recognition.
2. Client inspections license partner-clinic inspections with Food, Power, Scrap, and Recognition while preserving local stores.
3. Isolation doctrine funds named corridors and narrow closures with Food, Fuel, Support Equipment, and Command Power.
4. Humanitarian service sends mobile care teams beyond the North Gate with Food, Medicine, Fuel, and Recognition.

Each branch schedules a deterministic 45-day result. Grading combines the frozen state and country ledgers, branch-specific readiness, disease and exposure pressure, and the selected policy. Results change the regional health ledgers, Food, Recognition, Cohesion, Stability, War Support where isolation succeeds, Supply Access, Shelter, Reclamation, Exposure, and Disease. Failed results route bounded state population loss through the Deaths system and apply a dedicated health-authority modifier.

A 365-day callback regrades the selected policy against updated regional trust, clinic capacity, country ledgers, state Shelter, Supply Access, Exposure, Disease, and Cohesion. Success, partial, and failure callbacks have distinct ledger changes, state effects, dedicated modifiers, Event Log payloads, and bounded Deaths loss for failure. The chain never removes the country, creates a replacement tag, or stores its work in a political-power loop.

## Scheduler and Event Log wiring

Event ids are `chaosx.fallout.747` through `chaosx.fallout.753` under `add_namespace = chaosx.fallout`. Human events `.747`, `.749`, and `.751` are visible. Hidden AI events `.748`, `.750`, and `.752` resolve the same branch and delayed contracts. Cleanup `.753` authenticates the delayed cleanup ticket, clears state reservations and temporary ledgers, writes a state memory flag, and closes the chain idempotently.

The survivor Event Log history is `9184`. Choice, result, callback, and cancellation payloads use dedicated scripted localisation and concrete Ash Ward, North Gate, clinic, council, and medicine-register wording. Fallout itself remains outside ordinary Event Log and evolution registration.

## Asset and review surface

The dedicated report image is `GFX_report_event_fallout_health_without_borders`, registered in `interface/fallout_world_end.gfx`. Source, processed PNG, runtime DDS, manifest, and GFX handoff live under `docs/assets/747_health_without_borders/`.

The authoritative workbook row is `FALLOUT-747` with `Needs Testing` status. The chain remains dormant and contributes zero release-floor blocks until the shared scheduler activation gates are deliberately promoted.
