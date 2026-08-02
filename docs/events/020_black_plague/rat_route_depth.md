# Event 020 Rat Route Depth

The reusable `RTA` carrier now has a second route layer after capped pulses. It keeps the two-tag boundary intact while giving every brood four connected choices: mutation pressure, plague economy, military method, and proto-sentient rivalry. The carrier also exposes Brood Mass, Hunger, Coherence, and derived Disease Dominion as living registers in the shared Rat category.

Mutation pressure is a three-way choice between Mass Swarm, Giant Mutation, and Burrow Warfare. Mass Swarm and Giant Mutation raise the finite division cap; Burrow Warfare raises physical exposure on routes emitted from the carrier.

Plague economy is a two-way choice between Preserve the Herd and Consume the State. Preserve the Herd adds brood mass without extra exposure. Consume the State adds more pulse mass and exposure, turning captured territory into an aggressive engine.

Military method is a four-way choice between Flood the Front, Break Strongpoints, Hunt the Roads, and Hold the Nest. The choices alter capped force capacity or pulse mass and are reflected in the RTA AI strategy profile.

Rivalry is a convergent chain: Rivals Detected -> Challenge the Weaker Brood or Resist the Stronger Brood -> Absorb and Integrate -> Symbols and Maps -> Command Between Nests. The final focus records proto-sentience and marks the carrier as a Rat King candidate; the existing Prepare the Crown focus remains the visible handoff into Evolution IV selection. The three hierarchy roots remove the starting Fractured Instinct spirit and raise Coherence, while unresolved Hunger can trigger the player-facing Brood Is Hungry crisis with a rationing or destructive-feeding choice. The existing hierarchy report now uses route-specific descriptions for Distributed Instinct, Dominant Beast, and Emergent Cunning so the chosen pulse, command, or memory lane is visible at the moment of selection.

Runtime consumers are in `common/scripted_effects/020_black_plague_rat_effects.txt` and `common/scripted_effects/020_black_plague_spread_effects.txt`. Tuning is centralized in `common/script_constants/020_black_plague_rat_constants.txt` under `black_plague_rat_depth`. No new country tag, human manpower, ordinary equipment, or 3D model is introduced.

The shared `black_plague_rat_brood_category` now exposes four route operations when their corresponding capstone is complete: Citadel Stockpile, Migration Lanes, Tide Manifest, and Rail Breach Order. Each spends Brood Mass, grants a bounded cap or mass result, and raises only the matching city, refugee, port, or troop/transport exposure route for a timed interval. The overseas gate remains authoritative for dock operations.

The hierarchy layer adds three route-locked continuing actions. Distributed Instinct can distribute nest signals once the carrier controls more than one state, restoring Coherence and adding capped capacity behind a cooldown. Dominant Beast can seat an alpha command pattern when Coherence is stable, trading Brood Mass and time for Sentience and capacity while raising Hunger. Emergent Cunning can decode a selected human enemy logistics target beside rat-held ground, spending Brood Mass and applying a bounded internal-transport exposure through the canonical disease ledger. The target cooldown and existing exposure rules keep this action from becoming a free global spread button.

Each route operation now opens a short report through `chaosx.nr20.78`. The report distinguishes the citadel reserve, migration lanes, overseas tide, rail breach, distributed signal, alpha command, and route-memory actions, so the living carrier's choice is visible at the moment the operation completes rather than only in a hidden flag or later pulse.

The route focuses use the six dedicated Event 020 hierarchy goal sprites registered in `interface/020_black_plague_rat_identity.gfx`: `GFX_goal_black_plague_rat_four_mouths`, `GFX_goal_black_plague_rat_choose_a_voice`, `GFX_goal_black_plague_rat_read_the_marks`, `GFX_goal_black_plague_rat_many_nests_one_signal`, `GFX_goal_black_plague_rat_fang_above_the_warren`, and `GFX_goal_black_plague_rat_stolen_route_memory`. Their source, processed previews, final 94x86 DDS files, and contact sheet are recorded in `docs/assets/020_black_plague/manifests/event020_rat_hierarchy_icons_manifest.md`.

## Future extension

Further depth can add route-specific report text and crisis art without changing the decision contract. No bespoke rat unit models are required or planned for Event 020; the registered infantry entity remains the accepted visual consumer.
