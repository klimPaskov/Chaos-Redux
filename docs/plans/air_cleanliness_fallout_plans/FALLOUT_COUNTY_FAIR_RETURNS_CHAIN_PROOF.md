# Fallout County Fair Returns chain proof

Date: 2026-07-26

Status: implementation tranche complete at source level, dormant by scheduler contract, and not release-floor credit.

## Ownership and source files

The chain owns `chaosx.fallout.572` through `.578`, candidate `572`, transaction `710054`, route `7154`, and Event Log history `9159`.

Gameplay source is split across `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_consolidated_triggers.txt`, `common/scripted_effects/fallout_consolidated_effects.txt`, the County Fair script constants, the County Fair dynamic modifiers, and the County Fair candidate producer block.

Presentation source is `localisation/english/fallout_consolidated_l_english.yml`, the dedicated Event Log scripted localisation, the shared Event Log actor and history mappings, `interface/fallout_consolidated.gfx`, and the dedicated report DDS.

## Static proof

The candidate producer counts all eligible current-generation native rural states owned and controlled by the country and records the lowest native state id as `fallout_event_572_candidate_state_id`.

The candidate is appended only when the country is in the North American region, meets the recovery thresholds, has at least three eligible states, and can afford at least one branch.

The candidate block does not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

The opening has four visible options with distinct Food, Fuel, Scrap, Equipment, Medicine, and Recognition costs.

The hidden AI opening uses the same branch scheduler and cost effects rather than a second result implementation.

The result uses the issued branch, authenticated registry, named deterministic thresholds, local state effects, branch ledgers, dynamic modifiers, and the Deaths contract.

The result schedules a callback exactly 365 days after the 35-day result transaction.

The callback reauthenticates generation, country, target state, owner, controller, branch, result, and callback receipt before preserving annual, partial, or interrupted memories.

The opening, result, and callback record history `9159` with the country as primary actor and the host state as secondary actor.

Cleanup releases both delayed receipts before clearing transient reservation and frozen ledgers, while durable fair memories remain.

The report asset has a source image, processed PNG, prompt, hashes, manifest, handoff, and runtime DDS at `gfx/event_pictures/fallout/report_event_fallout_county_fair_returns.dds`.

## Engine-sensitive boundary

No HOI4 runtime was launched for this tranche.

The native event dispatch, hidden-AI probability, delayed queue execution, save recovery, multiplayer behavior, and host-authority presentation still require a user-owned live session.

The candidate and all event blocks remain dormant until a later reviewed setter opens the Fallout scheduler activation gates.

The chain does not claim exact runtime delivery or countable release-floor credit on static source evidence alone.
