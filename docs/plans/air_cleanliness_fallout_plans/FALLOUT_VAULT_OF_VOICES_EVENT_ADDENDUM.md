# Fallout The Vault of Voices Event Addendum

## Accepted design

The Vault of Voices is the reviewed global-survival tranche after The Working Machine.
It is candidate `359`, transaction `710025`, route `7125`, history `9130`, and events `359` through `365`.
It remains dormant until the Fallout scheduler activation contract is proven.

The four branches are Preserve the Archive, Curate a Civic Record, Weaponize the Broadcast, and Trade Verified Copies.
They use distinct resource costs and produce distinct Power, Scrap, Medicine, Recognition, Cohesion, Stability, War Support, reclamation, supply, exposure, building, diplomacy, and state-memory outcomes.
Result failure and callback failure use the Deaths system in the selected native state.
The result delay is forty-two days and the callback delay is two hundred seventy days.

## Implementation handoff

- Constants live in `common/script_constants/fallout_world_end_vault_of_voices_constants.txt`.
- The candidate row is appended in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Triggers, effects, modifiers, Event Log payload localisation, events, and player-facing localisation are Fallout-owned surfaces.
- The report image has a dedicated generated source, processed preview, DDS, manifest, and GFX handoff.
- It does not reuse Zombie paths, Air Winter report images, The Working Machine art, or another Fallout chain's source.
- The workbook row is `FALLOUT-359`, with CSV export regenerated after implementation facts are recorded.

## Review boundary

The bounded read-only event inspector is required for `chaosx.fallout.359`.
If it returns the known fixed issue ceiling without an artifact, the chain remains dormant and the exact engine-side receipt, host, save recovery, multiplayer, and target delivery surfaces remain unproven.
No HOI4 runtime is required for this tranche.
