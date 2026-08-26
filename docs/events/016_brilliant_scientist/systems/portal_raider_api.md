# Portal Raider reusable unit and raid API

`portal_raider` is a shared land-unit family, not a Kruger-owned identity. Event 016 unlocks it through Portal Warfare, Event 019 can request it through the generic infantry-spawn provider, and later event packages may reuse the same subunit, equipment, and counter contract without copying Event 016 state. The reusable model/entity contract remains pending because the current Portal Raider model task was rejected at the semantic generation gate and no accepted recovery package exists.

## Unit contract

The base battalion mirrors ordinary infantry for combat width, manpower, organization, recovery, suppression, supply, training time, and base combat statistics. Each battalion consumes 100 Infantry Equipment and 10 `teleportation_equipment_1`. Its exceptional combat performance comes from the grant-only Portal Warfare technologies rather than inflated subunit base values.

The default Event 016 template is `Quantum Transit Raiders`, a six-battalion locked formation. The reusable Event 019 provider uses family id `509` and charges the exact manpower, Infantry Equipment, and Teleportation Equipment manifest before spawning the requested formation.

## Portal Warfare raid surfaces

Both native Portal Warfare raids require seven days of preparation, ten Command Power, sixty Teleportation Equipment, and an assigned formation containing at least six `portal_raider` battalions. The native raid framework owns preparation, reservation, cancellation, expiry, outcome selection, and raid history. On success or critical success, the selected formation is consumed at its origin and reconstructed as the standard fully supplied six-battalion `Quantum Transit Raiders` formation in the captured target province; this prevents a repeatable free-unit loop while allowing the landing force to attack immediately.

`brilliant_scientist_portal_facility_raid` is the state-targeted surface for hostile states containing factories, reactors, or rocket sites. Its target type is a state rather than an exact building, and its success path calls `brilliant_scientist_portal_raid_extract_state_installation`. A normal success attempts to extract one eligible state installation after the beachhead is established; a critical success calls the state-installation extraction twice before applying the heavy target damage.

`brilliant_scientist_portal_special_project_facility_raid` is the exact facility-target surface. Its target type is `building = { tags = facility }`, and its success path calls `brilliant_scientist_portal_raid_extract_installation` for the selected provincial special-project facility. A critical success may additionally call `brilliant_scientist_portal_raid_extract_state_installation` once, so the exact facility raid can take its selected facility and one state installation.

Both surfaces establish a captured hostile province and rebuild the selected formation there. Facility or state extraction occurs only when a valid owned destination with a compatible free slot exists; factory transfers preserve the building type through the existing off-map industry path, while facility transfers preserve the selected facility family. Persistent country and state flags record successful landings and each transferred installation class.

The raid does not require Warren Kruger. His active authority raises AI interest through the existing raid weighting surface, while launch, equipment, target, template, and preparation requirements remain the same for every consumer.

## Runtime identifiers

- Subunit: `portal_raider`
- Equipment archetype: `teleportation_equipment`
- Equipment variant: `teleportation_equipment_1`
- Operational technology: `brilliant_scientist_portal_warfare_tech`
- Weaponization technology: `brilliant_scientist_portal_warfare_weaponization_tech`
- State-targeted raid: `brilliant_scientist_portal_facility_raid`
- Exact facility-target raid: `brilliant_scientist_portal_special_project_facility_raid`
- State installation effect: `brilliant_scientist_portal_raid_extract_state_installation`
- Exact facility effect: `brilliant_scientist_portal_raid_extract_installation`
- Runtime entity and preview animation: no entity or arrival-animation hook is registered in either native raid while the model package is rejected; accepted 3D production remains pending.

## Required visual, sound, and counter assets

The evidence package is rooted at `docs/assets/shared_portal_raider_system/models_3d/portal_raider/`, but it is rejected for runtime use because the legacy provider task omitted the mandatory ray rifle and no accepted recovery package exists. The package therefore does not hand accepted model, entity, animation, or sound files to runtime consumers. Any recovery generation must use Meshy 7 and the current balance and provider-capability gates.

- `gfx/models/units/portal_raider/portal_raider.mesh`, material DDS maps, and real skeletal action files remain future recovery outputs rather than accepted runtime files.
- `gfx/entities/portal_raider.gfx` and `gfx/entities/portal_raider.asset` remain future recovery outputs; no runtime entity or preview hook is registered until an accepted model package exists.
- `sound/portal_raider_sound.asset` and synchronized licensed audio remain future recovery outputs.
- `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds` are complete and wired through `interface/portal_raider_system.gfx`; these counters do not imply model/entity completion.
- The active subunit-icon GFX registry entries for both counter tokens are complete and wired.
- The already registered technology and equipment icon sprites used by the technology, equipment, production, and raid surfaces remain unchanged.

The unit model must remain identity-neutral: protective goggles, an insulated period-compatible military-laboratory suit, a compact coil-and-cable teleportation backpack, and a retro ray rifle without country, ideology, event, Kruger, or organization insignia. Runtime animation cannot use transform-only substitutes.

## Future extensions

Later events can grant the portal technology API, create Portal Raiders through Event 019, or define another raid using the shared unit, equipment, and counter contract. A new consumer should reuse the identifiers above, preserve the ten-equipment-per-battalion contract, and record its own event history rather than setting Event 016 host or Kruger flags. Every future Chaos Redux special project must be reviewed for inclusion in the reusable CBRN random and project registries before it is accepted as a new consumer.

Potential extensions include defensive emergency extraction, reinforcement of isolated bridgeheads, and project-facility evacuation. They should use the same exact equipment reservation and destination-slot checks instead of creating a parallel teleportation ledger.
