# Event 012 elephant model

`elephantry_entity` renders a custom African elephant with tusks, an articulated trunk, ears and tail, a reinforced woven-wood howdah with rigid cloth and straps, and an attached installed vanilla infantry rider.
Vanilla elephantry and Event 012 `chaosx_elephant` share this consumer through the unchanged `sprite = elephantry` binding.
The implementation and acceptance record is [the elephant model handoff](../../plans/unit_fix_2026-10/models_1018_elephant_handoff.md).

## Runtime and actions

- `gfx/models/units/012_africa_elephant/` contains the mesh, six DDS maps, eight animations and animation registry.
- `gfx/entities/chaosx_africa_elephant.gfx` binds decoded mesh objects `Mesh_0.002` and `Cube`, stream index 0, to their body/howdah maps and `PdxMeshAdvanced` shader.
- `gfx/entities/chaosx_africa_elephant.asset` defines the sole `elephantry_entity` and an elephant-specific rider wrapper that copies the mesh, states, attachments and scale of installed `infantry_rider_entity`. It is not a `clone`: entity files load in file-name order, so this file cannot clone an entity from vanilla `units_cavalry.asset`.
- `gfx/entities/chaosx_vanilla_entity_aliases.asset` no longer contains the horse replacement for elephantry.
- `sound/chaosx_elephants_sound.asset` and `sound/012_africa/elephant/` provide attributed recorded vocal, footfall, impact and wooden creak sounds.

The 20,000-triangle elephant body is one connected closed surface; the 8,788-triangle howdah consists of closed rigid construction pieces attached to its back.
The 39-bone skeleton drives eight separate 30 FPS actions: breathing idle, four-beat walk, faster retreat amble, forward charge/tusk/trunk strike, rear/stamp defense, braced raised-trunk support attack, drill movement and a supported side collapse.
Idle, move and retreat loop; combat and training finish their recovery and repeat through their matching next state; death settles without a next state.
The model stays in place in XY.

`Saddle_Node`, parented to `Howdah`, carries the installed native rider and inherited rifle entities.
Seated roles use `elephantry_idle` or `elephantry_move`; attack/defend use the native standing attack and support attack uses the native support clip.
The seated native Hip scale 1.75 is compensated by constant attachment scale 1/1.75, with scale 1 during combat, while the rider and elephant entity factors remain 0.8.
The wrapper explicitly propagates native rifle states for combat, retaining native muzzle particles, discharge and cartridge sounds.
No native mesh, animation or texture is redistributed.

The effective seated assembly measures 6.59831 by 12.94037 by 11.77656 runtime units, compared with the cavalry horse's 1.92919 by 5.94834 by 4.57647 after both its 0.45 mesh factor and 0.65 entity factor.
The accepted 55-degree comparison and actual-byte multi-view action sheets are retained in `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/`.
Audio event times follow measured reimported sole plants, head/flank collapse contact and reviewed trumpet poses, with recorded waveform peak offsets included.

## Gameplay and icons

`common/units/012_africa_elephant_forces.txt` retains `sprite = elephantry`, equipment, armour and combat values.
Host and Action 102 member templates leave `override_model` unset so mixed divisions retain their regiment visuals.
The existing elephantry counters and texticons remain in use; this model repair needs no new icon registration.
The elephant achievement remains separately governed by its movement, supply, destruction and war-purpose witnesses.
Model acceptance does not establish those gameplay proofs.

## Evidence and limits

The job manifest and current handoff record the single 30-credit Meshy 7 body task, live manual howdah/rig/action work, final hashes, runtime copy receipt, audio licences and workspace cleanup.
All eight exported animations passed animation-sign and delivery checks and were reimported with the final DDS maps for map/front/side review.
The rider composites use the final elephant bytes and installed native reference assets.
No in-game validation is claimed.
Selection voices remain country-routed; entity idle calls are not represented as per-subunit selection sounds.
The supplied trumpet is catalogued as Asian elephant and is retained under the user's instruction to use the existing licensed recordings.
There are no omitted requested model components or actions.

## Future work

Additional independently recorded elephant calls could expand vocal variety while preserving these action contacts.
Per-subunit selection audio would require a separately verified engine consumer before implementation.
These are optional extensions, not missing parts of this model repair.
