# Reviewed global-survival event 47: The Weapons in the Nursery

## Scope

This event family covers a former child-care room in an occupied shelter that has been converted into a state armory during the first year after Fallout. The register marks the room vacant and no minors are present. The conflict is about custody, command, and the room's civic meaning, not radiation science. The family is Fallout-owned and remains dormant until the reviewed scheduler activation audit opens its candidate lane.

The candidate selects the lowest owned urban state with a produced current-generation Air Winter shelter receipt, valid identity and resource rows, surviving population, and enough shelter capacity for a custody dispute. It uses candidate `513`, transaction `710047`, route `7147`, and Event Log history `9152`. No zombie id, file, asset, audio, sprite, or path is reused.

## Opening choices

The human opening has four government-aware choices.

1. Democratic or communist governments can spend Power and Recognition to seal the cache in a central armory.
2. Democratic or neutrality governments can spend Scrap, Recognition, and Food to issue household receipts.
3. Neutrality, communist, or fascist governments can spend Power and Fuel to place the stock with a supervised militia.
4. Democratic, neutrality, or fascist governments can spend Medicine, Recognition, and Food to dismantle the cache and reopen the room as shelter.

The AI uses the same branch tokens. It prefers a central armory when Power is available and civic trust is low, a family register when trust is established, a militia when War Support is high, and disarmament as the final eligible branch.

## Numerical and engine contract

The result freezes Shelter, Power, Fuel, Scrap, Medicine, Food, Recognition, Cohesion, War Support, state Supply Access, exposure, reclamation, arms discipline, accident risk, and civic trust before the delayed transaction. Viability is a deterministic weighted sum with positive shelter, Power, Cohesion, Supply Access, civic trust, and arms-discipline components, reduced by exposure and accident risk. Each custody branch has explicit success, partial, and failure thresholds.

Success, partial, and failure update survival resources, Cohesion, Stability, War Support, state Supply Access, Air Winter shelter capacity, exposure, reclamation, arms discipline, accident risk, civic trust, and the nursery memory. Failure damages an arms factory or infrastructure surface and records a bounded civilian loss through the shared Deaths system. Callback failure uses a separate smaller Deaths request. Timed state or country modifiers expose supply, defense, attack, stability, and attrition consequences without a political-power store.

The delayed result and safety callback use the Fallout scheduler's authenticated ticket, generation, owner, target, branch, control mode, visible-budget cost, queue status, and cleanup token. Human reports are visible. AI reports are hidden. Cleanup releases the callback receipt, closes the memory, clears the frozen snapshot, and leaves the country ready for later family or militia arcs.

## Presentation and proof

The dedicated report picture is `GFX_report_event_fallout_weapons_in_nursery` and is documented under `docs/assets/air_cleanliness_fallout/fallout_weapons_in_nursery/`. Event Log history `9152` stores twelve branch outcomes and three callback outcomes through the shared Fallout Event Log routing.

The implementation proof is `docs/plans/air_cleanliness_fallout_plans/FALLOUT_WEAPONS_IN_NURSERY_CHAIN_PROOF.md`. Static checks cover ids, localisation references, constants, dynamic modifiers, trigger and effect braces, BOM encoding, and unique dedicated assets. HOI4 was not launched, so runtime scheduler activation, save recovery, multiplayer delivery, AI frequency, and full-screen Fallout presentation remain observation gates.

## Future depth

The nursery memory can later feed a named armourer, a professional army route, a militia council, a shelter education arc, or a successor government dispute over inherited weapons. Each expansion requires a separately reviewed chain and must not silently activate this dormant candidate.
