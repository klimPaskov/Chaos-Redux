# Pre-wave crisis history copy fix — 2026-08-15

## Scope

Updated the player-facing Event Log history title and blocked outcome for the pre-wave pressure request.

## Changes

`independence_wave.history.crisis.outcome.title` now reads `Pre-Wave Request Result` instead of `Independence Wave Crisis Result`.

`independence_wave.history.crisis.outcome.blocked` now describes persistent pre-wave pressure instead of implying that an event-fired crisis was already open.

The scripted history keys, resolution enum, event log routing, and internal crisis variables are unchanged. This is a copy-only correction; no gameplay timing, queue, ownership, or cost behavior changed.

## Remaining wording

The internal localisation key family retains `crisis` for stable scripted-localisation and history compatibility. Player-facing category, mission, cost, and result copy now consistently describe the surface as pre-wave pressure or a synchronized request.

