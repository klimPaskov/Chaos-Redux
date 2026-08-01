# Event 020 Rat Route Depth

The reusable `RTA` carrier now has a second route layer after capped pulses. It keeps the two-tag boundary intact while giving every brood four connected choices: mutation pressure, plague economy, military method, and proto-sentient rivalry. The carrier also exposes Brood Mass, Hunger, Coherence, and derived Disease Dominion as living registers in the shared Rat category.

Mutation pressure is a three-way choice between Mass Swarm, Giant Mutation, and Burrow Warfare. Mass Swarm and Giant Mutation raise the finite division cap; Burrow Warfare raises physical exposure on routes emitted from the carrier.

Plague economy is a two-way choice between Preserve the Herd and Consume the State. Preserve the Herd adds brood mass without extra exposure. Consume the State adds more pulse mass and exposure, turning captured territory into an aggressive engine.

Military method is a four-way choice between Flood the Front, Break Strongpoints, Hunt the Roads, and Hold the Nest. The choices alter capped force capacity or pulse mass and are reflected in the RTA AI strategy profile.

Rivalry is a convergent chain: Rivals Detected -> Challenge the Weaker Brood or Resist the Stronger Brood -> Absorb and Integrate -> Symbols and Maps -> Command Between Nests. The final focus records proto-sentience and marks the carrier as a Rat King candidate; the existing Prepare the Crown focus remains the visible handoff into Evolution IV selection. The three hierarchy roots remove the starting Fractured Instinct spirit and raise Coherence, while unresolved Hunger can trigger the player-facing Brood Is Hungry crisis with a rationing or destructive-feeding choice.

Runtime consumers are in `common/scripted_effects/020_black_plague_rat_effects.txt` and `common/scripted_effects/020_black_plague_spread_effects.txt`. Tuning is centralized in `common/script_constants/020_black_plague_rat_constants.txt` under `black_plague_rat_depth`. No new country tag, human manpower, ordinary equipment, or 3D model is introduced.

The shared `black_plague_rat_brood_category` now exposes four route operations when their corresponding capstone is complete: Citadel Stockpile, Migration Lanes, Tide Manifest, and Rail Breach Order. Each spends Brood Mass, grants a bounded cap or mass result, and raises only the matching city, refugee, port, or troop/transport exposure route for a timed interval. The overseas gate remains authoritative for dock operations.

The route focuses reuse the existing Event 020 rat goal sprites registered in `interface/020_black_plague_rat_identity.gfx`. No additional icon file is required for this tranche. Future presentation work can replace reused sprites with route-specific art after the gameplay route has live visual evidence.

## Future extension

Further depth can add route-specific report text and crisis art without changing the decision contract. Bespoke rat unit models remain explicitly outside the current goal and should only be produced if a later asset plan requests them.
