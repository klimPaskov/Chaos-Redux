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

`sound/chaos_assault_battalion_sound.asset` declares nine runtime WAVs under `sound/chaos_warfare/chaos_assault_battalion/` and groups them into the `idle`, `attack`, `move` and `death` sound effects the entity fires.

All nine runtime files were measured directly from their RIFF headers on 2026-10-04: WAVE_FORMAT_IEEE_FLOAT, mono, 44,100 Hz, 32-bit float, with durations of 6.254 s (idle breath), 2.000 s (attack), 0.247/0.247/0.263/0.247 s (the four steps) and 3.670/4.063/3.014 s (the three deaths). They entered the repository in commit `a48e000bf` on 2026-08-15 and have not changed since.

The separate 2026-09-12 recovery set under `audio/recovery_20260912/derived/` is a reviewed candidate set that was never installed. Its files are PCM signed 16-bit mono 44,100 Hz, and its own `derived_manifest.json` records `status: needs_user_review` with `runtime_wiring: parent-owned; not copied`. Comparing the two sets by header and duration, only the idle breath matches the runtime length exactly, at 6.2539 s in both; the other eight differ, for example 2.000 s against 0.320 s for the attack and 3.670 s against 0.766 s for the first death. No runtime file matches an archived file byte for byte.

The runtime audio keeps its existing timing.
The idle cue is independently traced to primbal's CC0 OpenGameArt recording: all 275,796 mono frames match the archived stereo source after float32 equal-power channel conversion, with zero residual.
The source, runtime hashes, recipe and live licence-page verification are in [`2026-10-06_audio_provenance.md`](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-06_audio_provenance.md) and its JSON crosswalk.
The other eight runtime cues remain blocked for exact source/attribution evidence.
The archived recovery candidates have their own attribution receipt, but no plain crop/gain waveform match establishes them as these eight shipped recordings.
Different cue lengths or similar Git LFS pointer boilerplate do not establish source lineage.
The earlier `audio/source_manifest.md` does not exist, and no arbitrary recovery-set replacement is authorized by this evidence.

Commit `802006bf5` rebuilt the model and retimed the entity's sound events to the new animation lengths in `gfx/entities/chaos_assault_battalion.asset`. It changed no WAV and did not touch the sound asset, so event times follow the measured spray, step and landing frames of the rebuilt actions while the nine recordings stay as they were.

### Selection audio is an engine limit

Vanilla exposes generic `select_army`, `select_vehicle` and `select_tank` effects in `sound/soundeffects.asset`, plus separate country/original-tag infantry voice groups in `integrated_dlc/dlc018_together_for_victory/sound/vo.asset`.
Those groups include `<TAG>_infantry_idle`, `move_out`, `neutral_combat`, `positive_combat` and `retreat` in the Voices category.
They are not subunit-specific bindings.
Because ordinary infantry and Chaos Assault Battalions can share a tag, assigning that tag a CBRN selection voice would also affect its other infantry.
This package therefore retains the native shared voice routing, with CBRN-only selection still blocked.
The active entity's sound events attach to animation states and cannot substitute for a selection callback.

The battalion's active idle, movement, attack and death cues retain their existing consumers and timing.
A distinct selection cue for one subunit requires an actual consumer that does not replace the tag's other infantry voices.

## Live validation boundary

The agent does not launch Hearts of Iron IV; live confirmation of the spray direction at the nozzle, particle density at map zoom, and sound timing belongs to the user.

## Future work

- A dedicated hiss-and-sputter spray loop would suit the aerosol better than the compressed-gas cue.
- The idle and move actions could hold the lance two-handed; the provider motions leave the off hand free.
