# Chaos Assault Battalion model

The Chaos Assault Battalion uses a dedicated period chemical-assault infantry model rather than the generic infantry entity. Its silhouette is a steel-helmeted infantryman in a hooded gas mask, sealed protective overgarment, gloves, boots, webbing, front pouches, respirator hose, rear reservoir, canisters, and field CBRN equipment.

## Runtime wiring

The public unit remains `chaos_battalion` in `common/units/cbrn_regimental_support.txt` with `sprite = chaos_battalion`. The sprite resolves to `chaos_battalion_entity` in `gfx/entities/chaos_assault_battalion.asset`, which consumes `chaos_assault_battalion_mesh` from `gfx/entities/chaos_assault_battalion.gfx`.

The model files live under `gfx/models/units/chaos_assault_battalion/`. The PdxMesh material uses `PdxMeshAdvanced` with `texture_0.dds`, `texture_specular.dds`, and `texture_normal.dds`.

## Action map

The model contains real skeletal `.anim` files for idle, movement, aerosol attack, and death. Entity state aliases use the real attack action for `support_attack`, the real movement action for `retreat`, and the real idle action for `training`. No static pose or generic-infantry animation is substituted.

The attack state is the chemical projector action and plays the sourced compressed-gas sound. Movement and retreat use the custom movement action and heavy equipment footsteps. The death action is a provider skeletal collapse; its body rises during the final collapse sample because the animation represents a falling body rather than a standing contact pose, which is recorded in the reimport evidence and is not used for movement.

## Calibration and validation

The candidate was normalized to the installed vanilla Western European infantry source height of `7.3518242835` source units and retains entity scale `0.8`, producing the effective runtime height `5.8814594268`. The calibrated rig has 24 bones and the exported mesh has 30,000 triangles. The mesh, all four actions, materials, and all DDS maps were reimported through the locked Blender and `io_pdx_mesh` route.

## Counter preservation

The existing Chaos Battalion large and small counter icons remain untouched and continue to be consumed by `interface/chaosx_subuniticons.gfx`. This model package does not overwrite or replace those existing Chaos Redux counter files.

## Audio

The dedicated sound package uses only preserved CC0 source candidates and mechanically converted PCM WAVs. The source pages, licenses, transformation command, checksums, synchronization points, and runtime identifiers are recorded in `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/source_manifest.md` and `runtime/sound_handoff.md`.

## Live validation boundary

The repository package is wired and structurally validated, but the agent does not launch Hearts of Iron IV. The remaining user-owned validation is live consumer confirmation that `sprite = chaos_battalion` resolves the entity and that state-entry sounds play at the expected map zoom.
