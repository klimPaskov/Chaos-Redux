# Air Winter Normal-Map Proof Gate

Status: the ordinary-map entity route is statically supported and the dedicated regional lifecycle is wired. HOI4 was not launched, and no live observation claim is made.

## Legacy proof

The first bounded proof used state 64, literal entity id `8600064`, the package entity `air_winter_normal_map_proof_entity`, and a temporary vanilla light-snow particle. It established these script surfaces before final asset production:

- state-centered `create_entity`
- replacement by a stable literal id
- explicit `destroy_entity` cleanup
- `min_zoom = 1100`, matching the approved Kaiserreich ambient-object precedent
- reconstruction from the existing monthly coordinator pulse

The monthly proof-entity creation call has been removed. Visual schema migration and global reset retain explicit destruction of its literal id. The proof asset is not part of the regional presentation.

## Promoted regional route

The dedicated route now supplies:

- all nine reviewed presentation classes
- phases 1 through 6, with phase 0 clearing every active slot
- two simultaneous weather channels for snow or rain plus ash
- regional ground dimming, frost, cold wetness, soot, and desaturation
- dead vegetation linked to phase and food damage
- class-specific frozen water
- peak-memory recovery thaw and runoff
- deterministic state ids, schema migration, save reconstruction, state reset, and deferred global cleanup
- one synchronized call inside the existing monthly state pass

The detailed engine, collision, post-wire resolver, hash, DDS, and contact-sheet evidence is in `AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`. Asset ownership, matrices, counts, source frames, and final paths are in `docs/assets/air_cleanliness_fallout/regional_map_visuals/`.

The post-asset static re-audit is recorded in `subagent_handoffs/air_winter_normal_map_static_reaudit_2026-07-22.md`. It independently rechecks the ordinary-map call chain, exact 1,081-state class cover, regional weather matrix, five-slot cleanup, entity and particle registries, source-file resolution, and Zombie separation. Its verdict is a source-level pass without a live observation claim.

## User validation handoff

The user may later inspect:

1. all nine classes at phases 1, 4, and 6 on ordinary political and terrain maps
2. absence of universal snow in desert, tropical, equatorial, and ordinary oceanic states
3. state centering, z order, scale, borders, counters, icons, and province selection
4. primary and secondary particle combinations at near, medium, and far zoom
5. phase escalation, downward recovery, thaw, phase 0, disable, state reset, and global reset
6. save-load reconstruction without duplicate entities
7. multiplayer synchronization and late-join presentation
8. world-scale entity and particle performance
9. particle atlas playback, density, culling, and absence of unwanted audio

## Removed unowned registrations

The unused full-screen grade plates and static accessibility sprite registrations were removed from `interface/air_cleanliness_winter_regional_visuals.gfx`. The ordinary-map entity and particle route does not depend on those sprites. This leaves no registered grade or accessibility surface without an owning GUI or player setting.

Regional phase materials already carry the dim-light cue, so the ordinary map does not depend on the unproven full-screen grade.
