# Reviewed global-survival Old Weather Station contract

Status: implemented as dormant candidate `373`. It is not release-floor credit until the Fallout scheduler caller, authority, save-recovery, multiplayer, Event Log delivery, and final audits are proven.

## Identity

The Old Weather Station owns candidate `373`, transaction `710027`, route `7127`, event ids `373` through `379`, and Event Log history `9132`.
It is a Fallout-owned climate and recovery incident for the consolidation phase and later second-world contact.
The chain uses a native state with a surviving radar station. It does not reuse the Air Winter weather chain, Zombie assets, or reactor identifiers.

## State gate and deterministic selection

The producer accepts only a current-generation Air Winter state with surviving population, produced snapshot provenance, exposure from `12` through `67`, a non-damaged radar station, and an ownership condition showing reclamation below `70` or supply access below `88`.
The state must also retain either infrastructure or industrial capacity and be one of the accepted Fallout state grades.
The candidate score is radar-station level multiplied by `4`, plus infrastructure and industrial capacity. The highest score wins and the lowest native state id breaks an exact tie.

## Branch contract

The opening presents four authored policies.

1. Fund the observers spends Power, Fuel, Medicine, and Recognition to return the station to public shelter planning.
2. Militarize the forecast spends Power, Fuel, and Cohesion to put the radio watch under guarded command.
3. Share the records spends Power, Medicine, and Recognition to copy the climate notebooks and open interregional exchange.
4. Abandon the tower spends a small Fuel, Power, and Recognition reserve to leave a sealed archive for a later expedition.

Every branch freezes the country resource row, Cohesion, Recognition, target state, transition generation, and climate ledgers before a 42-day delayed result.
Success, partial success, and failure have distinct text, state memory, dynamic modifiers, forecast, contact, intelligence, supply, exposure, Stability, War Support, and Deaths-backed failure effects.
Failure damages the radar station first, then infrastructure, then an industrial complex when the earlier targets are exhausted.

The result schedules a 300-day station review callback.
The callback changes the same durable ledgers, applies a branch-aware climate modifier on success, records a partial or unsafe outcome, and closes through authenticated delayed cleanup.
Human and hidden-AI paths use the same transaction, target, branch, result, callback, Event Log, and cleanup receipts.

## Localisation, Event Log, and asset surfaces

Concrete station, observer, military warning, radio exchange, and archive language is in `localisation/english/fallout_world_end_old_weather_station_l_english.yml`.
History `9132` has fifteen branch and callback payloads.
The dedicated report picture is `GFX_report_event_fallout_old_weather_station` and its manifest and GFX handoff live under `docs/assets/air_cleanliness_fallout/fallout_old_weather_station/`.

## Proof boundary

The chain remains dormant and contributes zero of the 660 release-floor blocks.
The bounded event inspector is expected to hit the fixed issue ceiling already observed on adjacent chains because the shared workspace graph is unresolved.
No HOI4 runtime was launched for this tranche.

## Future depth

Future reviewed work can consume the station memories with a climate monitoring charter, a polar contact chain, a false-spring crisis, or a named weather observer character.
Those consumers remain queued and are not implied by candidate `373`.
