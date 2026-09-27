# Chaos Assault Battalion model

The Chaos Assault Battalion uses a dedicated period chemical-assault infantry model rather than the generic infantry entity.
Its silhouette is a steel-helmeted trooper in a round-eyed gas mask with a breathing hose, a long protective overcoat, tan webbing and pouches, a green-cross satchel, gloves, tall boots, and a twin-cylinder reservoir on the back.
He carries a pistol-gripped spray lance, generated as its own model and fitted to the right hand.

## Runtime wiring

The public unit remains `chaos_battalion` in `common/units/cbrn_regimental_support.txt` with `sprite = chaos_battalion`.
The sprite resolves to `chaos_battalion_entity` in `gfx/entities/chaos_assault_battalion.asset`, which consumes `chaos_assault_battalion_mesh` from `gfx/entities/chaos_assault_battalion.gfx`.
The model files live under `gfx/models/units/chaos_assault_battalion/`: `chaos_assault_battalion.mesh` (five skinned streams sharing one `PdxMeshAdvanced` material), `chaos_assault_battalion_diffuse/specular/normal.dds` (one atlas holding the body and the lance), and one `.anim` per role registered in `animation_chaos_assault_battalion.asset`.

## Action map

Eight distinct skeletal actions, one per entity state:

| State | Action |
| --- | --- |
| idle | lowers the lance, looks around, raises it again |
| move | laden walk under the reservoir |
| retreat | backs away with the lance levelled |
| attack | braces and sweeps a spray across the ground |
| support_attack | kneels and fires two short bursts |
| defend | swaps the reservoir canister behind cover |
| training | kneeling canister-change drill |
| death | shot and falling slowly backward |

## Aerosol effect

The mesh carries a `lance_nozzle` locator on the right hand, oriented like the vanilla flame-tank `flamethrower` locator so the jet leaves along the lance.
The attack and support-attack states emit `chaosx_chem_spray_particle` (a pale yellow-green aerosol jet) and `chaosx_chem_spray_cloud_particle` (the lingering cloud) from that node.
Both particles are defined in `gfx/particles/chaosx_chem_spray.asset` and registered in `gfx/entities/chaosx_chem_spray_particles.gfx`; they adapt the vanilla flamethrower jet and smoke systems with soft alpha-blended cloud sprites.

## Calibration and validation

The model is normalized to the installed vanilla Western European infantry source height of `7.3518242835` source units and keeps entity scale `0.8`.
All eight actions are grounded to 4 mm contact and reimport-proven through the locked Blender and `io_pdx_mesh` route; provider tasks and credits are recorded in `docs/plans/system_unit_model_rework_plans/credit_ledger.json`.

## Counter preservation

The existing Chaos Battalion large and small counter icons remain untouched and continue to be consumed by `interface/chaosx_subuniticons.gfx`.

## Audio

The dedicated sound package uses only preserved CC0 source candidates and mechanically converted PCM WAVs.
The source pages, licenses, transformation command, checksums, and runtime identifiers are recorded in `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/source_manifest.md`.
Event times in the entity follow the measured spray, step, and landing frames of the rebuilt actions.

## Live validation boundary

The agent does not launch Hearts of Iron IV; live confirmation of the spray direction at the nozzle, particle density at map zoom, and sound timing belongs to the user.

## Future work

- A dedicated hiss-and-sputter spray loop would suit the aerosol better than the compressed-gas cue.
- The idle and move actions could hold the lance two-handed; the provider motions leave the off hand free.
