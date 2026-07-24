# Fallout Reactor Without a Country event addendum

## Accepted scope

Implement one dormant country-level candidate at `chaosx.fallout.366` through `.372`.
Use candidate `366`, transaction `710026`, route `7126`, and history `9131`.
The source matrix row describes joint authority, military occupation, engineer protectorate, and permanent shutdown.

## Reviewed implementation surfaces

- native nuclear-reactor state selection with a deterministic reactor, infrastructure, and industry score
- unstable-ownership gates based on reclamation and supply access
- Power, Fuel, Medicine, Cohesion, Recognition, reclamation, supply, exposure, Stability, and War Support ledgers
- four human options and a hidden-AI preference order
- 35-day delayed result and 240-day inspection callback
- Deaths route for result and callback failure
- nuclear-reactor, infrastructure, and industrial damage ladder
- branch-specific state memory and timed dynamic modifiers
- Event Log history `9131` with fifteen payloads
- dedicated generated report image, processed preview, runtime DDS, manifest, prompt, and GFX handoff

## Dormancy and review boundary

The producer never sets scheduler activation or authority flags.
The chain earns no release-floor credit while ordinary receipt production, host authority, save recovery, multiplayer behavior, blackout delivery, and runtime Event Log delivery remain unobserved.
No placeholder, generic event id, zombie asset, or ordinary super-event ownership is used.
