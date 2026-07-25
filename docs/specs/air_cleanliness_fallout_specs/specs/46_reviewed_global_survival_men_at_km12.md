# Reviewed global-survival event 46: The Men at Kilometer Twelve

## Scope

This event family covers an armed checkpoint on a trade or water route during the first season of Air Winter. It is Fallout-owned and remains dormant until the reviewed scheduler activation audit opens the candidate lane.

The candidate selects the lowest owned state with a produced Air Winter receipt, valid identity and resource rows, an exposed population, and a state grade that can support a corridor memory. The row uses candidate 506, transaction 710046, route 7146, and history 9151. No zombie event id, file, asset, audio, sprite, or path is reused.

## Opening choices

The human opening has four government-aware choices.

1. Democratic or neutrality governments can pay food, water, and recognition for a supervised passage.
2. Democratic, neutrality, or communist governments can negotiate a written water pass.
3. Communist or fascist governments can spend fuel and power to attack the checkpoint.
4. Democratic, neutrality, or fascist governments can hire a local guard band with food, scrap, and recognition.

The AI uses the same branch tokens. It prefers tribute when the route can pay, negotiation when checkpoint trust is established, an attack when war support and power support it, and a guard contract as the final eligible choice.

## Numerical and engine contract

The result freezes food, water, fuel, power, scrap, recognition, Cohesion, War Support, checkpoint trust, raider strength, state Supply Access, exposure, and reclamation before the delayed transaction. Viability is a deterministic weighted sum with explicit exposure and raider penalties. Each branch has success, partial, and failure thresholds.

Success, partial, and failure update survival resources, Cohesion, stability, War Support, state Supply Access, Air Winter exposure, reclamation, checkpoint trust, raider strength, and corridor memory. Failure damages one repairable infrastructure or arms-factory surface and records a bounded civilian loss through the shared Deaths system. Callback failure uses a separate smaller Deaths request. State modifiers show route supply and army readiness outcomes without a political-power store.

The delayed result and callback use the Fallout scheduler's authenticated ticket, generation, owner, target, branch, control mode, visible-budget cost, queue status, and cleanup token. Human results are visible. AI results are hidden. Cleanup reopens the result cleanup ticket when the callback releases first, then closes the country memory and clears the receipt variables.

## Presentation and proof

The dedicated report picture is registered as `GFX_report_event_fallout_men_at_km12` and is documented under `docs/assets/air_cleanliness_fallout/fallout_men_at_km12/`. Event Log history 9151 stores branch and callback outcomes through the shared Fallout Event Log routing.

The implementation proof is `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MEN_AT_KM12_CHAIN_PROOF.md`. Static checks cover ids, localisation references, constants, dynamic modifiers, trigger and effect braces, BOM encoding, and unique dedicated assets. HOI4 was not launched, so runtime scheduling, save recovery, multiplayer presentation, AI frequency, and map readback remain observation gates.

## Future depth

The checkpoint memory can later feed a named militia character, a bilateral corridor treaty, a warlord-client successor, or a recurring raider retaliation chain. Those expansions must add separately reviewed event blocks and must not silently activate this dormant candidate.
