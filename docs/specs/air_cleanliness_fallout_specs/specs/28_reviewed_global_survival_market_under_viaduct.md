# Reviewed global-survival Market Under the Viaduct contract

Status: implemented as dormant candidate `380`. It is not release-floor credit until the Fallout scheduler caller, authority, save-recovery, multiplayer, Event Log delivery, and final audits are proven.

## Identity

The Market Under the Viaduct owns candidate `380`, transaction `710028`, route `7128`, event ids `380` through `386`, and Event Log history `9133`.
It is a Fallout-owned transport and food-security incident for the consolidation phase and later second-world contact.
The chain uses a native state with a surviving supply node and rail connection. It does not reuse Air Winter event assets, Zombie paths, reactor identifiers, or Old Weather Station art.

## State gate and deterministic selection

The producer accepts only a current-generation Air Winter state with surviving population, produced snapshot provenance, exposure from `18` through `73`, a non-damaged supply node, at least two levels of rail or usable infrastructure, and an ownership condition showing reclamation below `70` or supply access below `88`.
The state must also be one of the accepted Fallout state grades.
The candidate score is supply-node level multiplied by `4`, plus railway level multiplied by `2`, infrastructure, and industrial capacity. The highest score wins and the lowest native state id breaks an exact tie.

## Branch contract

The opening presents four authored policies.

1. License the market spends Food, Scrap, Medicine, and Recognition to establish stall licenses, a common price board, and a public ration mark.
2. Tax the stalls for public stores spends Food, Scrap, and Cohesion to collect a measured levy for depots.
3. Police the exchange spends Scrap, Medicine, and Recognition to put wardens at the scales and ration gate.
4. Tolerate barter spends a small Scrap, Food, and Recognition reserve to leave the arches open to informal trade.

Every branch freezes the country resource row, Cohesion, Recognition, target state, transition generation, and market ledgers before a 35-day delayed result.
Success, partial success, and failure have distinct text, state memory, dynamic modifiers, food, scrap, medicine, price, merchant, ration, supply, exposure, Stability, War Support, and Deaths-backed failure effects.
Failure damages the supply node first, then rail, infrastructure, and an industrial complex when the earlier targets are exhausted.

The result schedules a 270-day civic review callback.
The callback changes the same durable ledgers, applies a branch-aware market modifier on success, records a partial or unsafe outcome, and closes through authenticated delayed cleanup.
Human and hidden-AI paths use the same transaction, target, branch, result, callback, Event Log, and cleanup receipts.

## Localisation, Event Log, and asset surfaces

Concrete viaduct, ration-stall, rail-market, levy, warden, and barter language is in `localisation/english/fallout_consolidated_l_english.yml`.
History `9133` has fifteen branch and callback payloads.
The dedicated report picture is `GFX_report_event_fallout_market_under_viaduct` and its manifest and GFX handoff live under `docs/assets/air_cleanliness_fallout/fallout_market_under_viaduct/`.

## Proof boundary

The chain remains dormant and contributes zero of the 660 release-floor blocks.
The bounded event inspector is expected to hit the fixed issue ceiling already observed on adjacent chains because the shared workspace graph is unresolved.
No HOI4 runtime was launched for this tranche.

## Future depth

Future reviewed work can consume the market memories with a named caravan, a ration-price crisis, a rail customs dispute, or a successor-country trade charter.
Those consumers remain queued and are not implied by candidate `380`.
