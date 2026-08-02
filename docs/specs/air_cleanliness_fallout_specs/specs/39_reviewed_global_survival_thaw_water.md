
# Thaw Water

## Event identity

Thaw Water is a reviewed Fallout ordinary-event chain in `chaosx.fallout`. It is a regional recovery incident that only opens after the Air Winter visual state reaches an eligible thaw. The candidate selects the lowest valid native state owned by the current Fallout country and remains dormant until the Fallout scheduler proves activation.

The gate requires current survival identity and durable resource rows, produced Air Winter data, surviving population, exposure in the accepted band, existing reclamation, and a water-security and disease-pressure combination that still needs intervention. It refuses a state that already carries the chain registry receipt.

## Opening conflict

Ice breaks along a settlement watercourse while cold rain turns ash-packed ground into brown runoff. The clinic needs clean water, the road crews need a stable bank, and the council must decide whether to drain the settlement, move families uphill, rebuild the channels, or put the meltwater fields into production.

## Policy branches

- Drain the settlement. Crews cut a controlled outlet and trade food, medicine, recognition, and cohesion for lower flood pressure and an immediate safety decision.
- Evacuate low ground. The government moves households to higher ground, protecting water safety while accepting supply and manpower strain.
- Rebuild the channels. Engineers reinforce the old watercourse and create a durable channel station with infrastructure and supply benefits.
- Use the floodwater fields. Farmers accept monitored runoff and turn the thaw into a food and recognition gamble with a higher disease burden if controls fail.

Each branch has its own resource cost, ledgers, thresholds, dynamic state modifier, and memory flag. The text names the watercourse, clinic, berms, and thaw work rather than using a generic apocalypse label.

## Deterministic delayed resolution

The result is scheduled for 60 days through the shared Fallout request coordinator. It freezes Food, Medicine, Recognition, Cohesion, flood pressure, water safety, channel trust, disease control, and thaw memory before calculating viability. The grade combines the five water ledgers with Food, Recognition, and Cohesion, then applies branch-specific success, partial, and failure thresholds.

Success and partial outcomes write the selected policy into state memory, update Air Winter water security and disease pressure, alter adaptation, reclamation, supply access, exposure, stability, war support, and manpower, and apply a branch-specific dynamic modifier. Failure uses the Deaths system for exact state civilian population loss, damages a state building, worsens supply and exposure, and records the failed water policy rather than ending as a harmless narrative result.

The 480-day callback rechecks the same owner, generation, state, and transaction receipts. It advances or erodes flood pressure, water safety, channel trust, disease control, thaw memory, Air Winter recovery, supply access, and exposure. Callback failure again uses Deaths and building damage. The cleanup event releases both delayed tickets, closes the memory receipt before clearing the chain registry, and removes frozen ledgers and temporary flags.

## AI and memory

The hidden AI lane uses the same coordinator and deterministic ledgers. Democratic governments with durable channel trust rebuild channels. Security governments with low water safety drain the settlement. Neutral governments with a strong thaw memory use the floodwater fields. Other governments evacuate low ground. AI results use the same callback and cleanup paths as human results.

## Air Winter relationship

This chain is part of the normal-map winter route. It uses the existing `air_winter_visual_thaw_is_eligible` trigger and updates the existing state values `air_winter_water_security` and `air_winter_disease_pressure`. It does not substitute a universal snow overlay or a mapmode-only visual for the normal map state.

## Assets

`GFX_report_event_fallout_thaw_water` is a dedicated generated report image registered in `interface/fallout_consolidated.gfx`. The source, processed PNG, DDS, prompt, manifest, and handoff are under `docs/assets/air_cleanliness_fallout/fallout_thaw_water/`.

## Review boundary

This spec does not claim live scheduler activation, host authority, save recovery, multiplayer delivery, full-screen blackout behavior, native state-population relocation, native character creation, native wildlife simulation, dynamic successor tags, or mutant-country creation. Those engine surfaces remain separate proofs. No HOI4 runtime was launched for this tranche.
