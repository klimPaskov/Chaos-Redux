# Reviewed global-survival event 48: The Captain Refuses

## Scope

This event family covers a winter military operation whose captain refuses an unsafe route through an exposed state. The dispute is about command responsibility, casualty rules, field autonomy, and the survival of a real platoon. It is Fallout-owned and remains dormant until the reviewed scheduler activation audit opens its candidate lane.

The candidate selects the lowest owned state with a produced current-generation Air Winter receipt, surviving population, exposed phase, state Supply Access, and a valid urban or rural settlement category. The country must carry a low durable captain-loyalty ledger, enough command power and military experience, and the reviewed survival resources. It uses candidate `520`, transaction `710048`, route `7148`, and Event Log history `9153`. No zombie id, file, asset, audio, sprite, or path is reused.

## Opening choices

The human opening has four government-aware choices.

1. Democratic or neutrality governments can spend Food, Fuel, and Recognition to give the operation a negotiated civilian mandate.
2. Communist or fascist governments can spend Scrap and Equipment to replace the refusing captain before departure.
3. Communist, fascist, or neutrality governments can spend Fuel and Equipment to arrest the captain and force the march.
4. Democratic, neutrality, or fascist governments can spend Food and Scrap to grant the field command a bounded local route and withdrawal rule.

The AI uses the same branch tokens. It prefers compromise when the mission mandate is strong, replacement when loyalty has collapsed, arrest when War Support is high, and field autonomy as its final eligible response.

## Numerical and engine contract

The result freezes Food, Water, Fuel, Equipment, Scrap, Recognition, Cohesion, War Support, Command Power, captain loyalty, mission mandate, field autonomy, state Supply Access, exposure, and reclamation before the delayed transaction. Viability is a deterministic weighted sum with positive state Supply Access, Cohesion, War Support, Command Power, and loyalty components, reduced by exposure and field autonomy pressure. Each command branch has explicit success, partial, and failure thresholds.

Success, partial, and failure update survival resources, Cohesion, Stability, War Support, Command Power, Army Experience, bounded manpower, state Supply Access, Air Winter exposure and reclamation, captain loyalty, mission mandate, field autonomy, and refusal memory. Failure damages one repairable infrastructure or arms-factory surface and records a bounded civilian loss through the shared Deaths system. Callback failure uses a separate smaller Deaths request. Timed modifiers expose military attack, defence, organization, local supply, stability, and attrition consequences without creating a political-power store.

The delayed result and command review callback use the Fallout scheduler's authenticated ticket, generation, owner, target, branch, control mode, visible-budget cost, queue status, and cleanup token. Human reports are visible. AI reports are hidden. Cleanup releases both receipts, closes the memory, clears the frozen snapshot, and leaves the durable command ledgers for later character or successor work.

Native character replacement is not claimed. The chain records replacement, arrest, compromise, and autonomy in country and state memory until the separate character installation surface is proven.

## Presentation and proof

The dedicated report picture is `GFX_report_event_fallout_captain_refuses` and is documented under `docs/assets/air_cleanliness_fallout/fallout_captain_refuses/`. Event Log history `9153` stores twelve branch outcomes and three callback outcomes through the shared Fallout Event Log routing.

The implementation proof is `docs/plans/air_cleanliness_fallout_plans/FALLOUT_CAPTAIN_REFUSES_CHAIN_PROOF.md`. Static checks cover ids, localisation references, constants, dynamic modifiers, trigger and effect braces, BOM encoding, and unique dedicated assets. HOI4 was not launched, so runtime scheduler activation, save recovery, multiplayer delivery, AI frequency, and full-screen Fallout presentation remain observation gates.

## Future depth

The command memory can later feed a named officer, a professional army focus, a militia council, a successor government's officer corps, or a regional military compact. Each expansion requires a separately reviewed chain and must not silently activate this dormant candidate.
