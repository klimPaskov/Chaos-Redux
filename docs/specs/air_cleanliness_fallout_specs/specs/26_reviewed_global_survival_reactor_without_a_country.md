# Reviewed global-survival Reactor Without a Country contract

Status: implemented as dormant candidate `366`. It is not release-floor credit until the Fallout scheduler caller, authority, save-recovery, multiplayer, Event Log delivery, and final audits are proven.

## Identity

The Reactor Without a Country owns candidate `366`, transaction `710026`, route `7126`, event ids `366` through `372`, and Event Log history `9131`.
It is a Fallout-owned country-level routine crisis incident for the first year and later consolidation phases.
The chain uses a native state target. It does not reuse Air Winter reactor event ids or Zombie assets.

## State gate and deterministic selection

The producer scans owned states and accepts only a current-generation Air Winter state with a surviving population, produced snapshot provenance, exposure from `16` through `71`, a nuclear reactor level at least `1`, and an ownership condition showing reclamation below `58` or supply access below `82`.
The state must also have a repair route through non-damaged infrastructure or an industrial complex, and it must be one of the accepted Fallout state grades.
The candidate score is nuclear reactor level multiplied by `5`, plus infrastructure and industrial capacity.
The highest score wins and the lowest native state id breaks an exact tie.
The producer stores the selected state id, score, and exposure before appending the candidate row, then clears its working variables.

## Branch contract

The opening presents four authored policies.

1. Joint authority spends Power, Fuel, Medicine, and Recognition to create a civilian and technical board.
2. Military occupation spends Power, Fuel, and Cohesion to secure the plant with troops.
3. Engineer protectorate spends Power, Fuel, and Recognition to give the cooling crew protected authority.
4. Permanent shutdown spends Fuel, Power, and Recognition to drain and seal the core.

Every branch freezes the country resource row, Cohesion, Recognition, target state, transition generation, and branch token before a 35-day delayed result.
Success, partial success, and failure have distinct text, state memory, dynamic modifiers, power and fuel movement, reclamation, supply access, exposure, Stability, War Support, and Deaths-backed failure effects.
Failure damages the nuclear reactor first, then infrastructure, then an industrial complex when the earlier targets are exhausted.

The result schedules a 240-day inspection callback.
The callback changes the same durable ledgers, applies a branch-aware maintenance modifier on success, records a partial or unsafe outcome, and closes through authenticated delayed cleanup.
Human and hidden-AI paths use the same transaction, target, branch, result, callback, Event Log, and cleanup receipts.

## Localisation, Event Log, and asset surfaces

Concrete reactor, cooling, claimant, military, engineer, and shutdown language is in `localisation/english/fallout_consolidated_l_english.yml`.
History `9131` has fifteen branch and callback payloads.
The dedicated report picture is `GFX_report_event_fallout_reactor_without_a_country` and its manifest and GFX handoff live under `docs/assets/air_cleanliness_fallout/fallout_reactor_without_a_country/`.

## Proof boundary

The chain remains dormant and contributes zero of the 660 release-floor blocks.
The bounded event inspector is expected to hit the fixed issue ceiling already observed on adjacent chains because the shared workspace graph is unresolved.
No HOI4 runtime was launched for this tranche.

## Future depth

Future reviewed work can consume the state memories with a reactor war, a named engineer institution, a regional power compact, or a successor-country identity overlay.
Those consumers remain queued and are not implied by candidate `366`.
