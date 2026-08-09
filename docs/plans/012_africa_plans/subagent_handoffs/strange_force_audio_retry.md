# Event 012 strange-force unit audio retry handoff

Date: 2026-08-06.

## Outcome

Source-only sound-design packages are complete for `gorilla_heavy_infantry`, `pan_sappers`, `stone_cohorts`, `forest_giants`, `oracle_recon`, `riverborn`, `disaster_wardens`, and `plague_carriers`.

The package contains 17 job-local immutable source copies representing 13 distinct licensed or public-domain recordings, 49 mechanically derived WAV cues, eight source-research evidence records, eight manifests, and eight runtime handoffs. Shared originals retain identical SHA-256 hashes across job roots.

## Legal and technical status

All selected sources are public domain, CC0 1.0, CC BY 4.0, or CC BY-SA 4.0. Attribution, source page, direct-download URL, permission terms, source checksum, excerpt interval, transformations, and final checksum are recorded in each job package. CC BY-SA-derived files must retain attribution, a change notice, and ShareAlike treatment when redistributed.

Every runtime candidate is mono 44,100 Hz PCM 32-bit float. FFprobe verified codec, sample format, sample rate, and channel count across all 49 WAVs. No generated, synthesized, recorded, placeholder, or unlicensed audio was used.

## Runtime ownership

No gameplay, GFX, entity, `.asset`, `sound.asset`, or `soundeffects.asset` file was edited. Each per-unit handoff supplies exact proposed sound IDs, soundeffect wrapper IDs, runtime paths, animation actions, and synchronization frames. The parent still owns copying selected WAVs into the runtime sound tree, defining sound and soundeffect entries, binding UI/entity consumers, selecting runtime volume/distance/instance limits, and validating the live consumer in game.

## Costs and dependencies

No Meshy/provider call was made and no credits were estimated or consumed. The dependency locks were inspected but the audio-only work required no paid route and no Blender mutation. Wikimedia download throttling was resolved by using the same approved direct media URLs over IPv4; no source fallback was introduced.

## Package roots

- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/audio/`
- `docs/assets/012_africa/models_3d/pan_sappers/audio/`
- `docs/assets/012_africa/models_3d/stone_cohorts/audio/`
- `docs/assets/012_africa/models_3d/forest_giants/audio/`
- `docs/assets/012_africa/models_3d/oracle_recon/audio/`
- `docs/assets/012_africa/models_3d/riverborn/audio/`
- `docs/assets/012_africa/models_3d/disaster_wardens/audio/`
- `docs/assets/012_africa/models_3d/plague_carriers/audio/`

## Simplifications, omissions, and blockers

There are no source, licensing, role-coverage, conversion, checksum, or handoff omissions in this bounded audio task. Final runtime wiring and in-game consumer validation are intentionally not claimed because they remain parent-owned.

## Parent integration receipt

The parent copied all 49 derived WAV files into `sound/012_africa/units/<slug>/`, registered 49 source sounds and 49 soundeffect wrappers in `sound/012_africa_strange_forces_sound.asset`, and bound every wrapper. Forty action roles are bound to map-entity animation states. Eight selection roles play once when their exact formation is successfully created. The plague-carrier impact role plays for the affected country after the native disease lifecycle accepts the seed. A source-to-consumer audit reports 49 defined soundeffect IDs and zero unused IDs.
