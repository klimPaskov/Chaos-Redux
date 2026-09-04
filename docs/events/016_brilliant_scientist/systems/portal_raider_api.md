# Portal Raider reusable unit and raid API

`portal_raider` is a shared land-unit family, not a Kruger-owned identity. Event 016 unlocks it through Portal Warfare, Event 019 can request it through the generic infantry-spawn provider, and later event packages may reuse the same subunit, equipment, and counter contract without copying Event 016 state.
The runtime package remains pending the existing-geometry recovery and export gates in the final completion contract.
Model regeneration is forbidden; body geometry, the approved existing firearm, and recoverable rig/action work are the inputs for closure.

## Unit contract

The base battalion mirrors ordinary infantry for combat width, manpower, organization, recovery, suppression, supply, training time, and base combat statistics. Each battalion consumes 100 Infantry Equipment and 10 `teleportation_equipment_1`. Its exceptional combat performance comes from the grant-only Portal Warfare technologies rather than inflated subunit base values.

The default Event 016 template is `Quantum Transit Raiders`, a six-battalion locked formation. The reusable Event 019 provider uses family id `509` and charges the exact manpower, Infantry Equipment, and Teleportation Equipment manifest before spawning the requested formation.

## Portal Warfare raid surfaces

Both native Portal Warfare raids require seven days of preparation, ten Command Power, sixty Teleportation Equipment, and an assigned formation containing at least six `portal_raider` battalions. The native raid framework owns preparation, reservation, cancellation, expiry, outcome selection, and raid history. On success or critical success, the standard fully supplied six-battalion `Quantum Transit Raiders` formation is committed in the captured target province and raises one scope-less reconstruction receipt. The assigned formation is consumed at its origin only when that receipt exists, so a target-state race cannot destroy the source without creating its replacement and a successful raid cannot retain both formations.

`brilliant_scientist_portal_facility_raid` is the state-targeted surface for hostile states containing factories, reactors, or rocket sites. Its target type is a state rather than an exact building, and its success path calls `brilliant_scientist_portal_raid_extract_state_installation`. A normal success attempts to extract one eligible state installation after the beachhead is established; a critical success calls the state-installation extraction twice before applying the heavy target damage.

`brilliant_scientist_portal_special_project_facility_raid` is the exact facility-target surface. Its target type is `building = { tags = facility }`, and its success path calls `brilliant_scientist_portal_raid_extract_installation` for the selected provincial special-project facility. A critical success may additionally call `brilliant_scientist_portal_raid_extract_state_installation` once, so the exact facility raid can take its selected facility and one state installation.

Both surfaces establish a captured hostile province and rebuild the selected formation there. Facility or state extraction occurs only when a valid owned destination with a compatible free slot exists; factory transfers preserve the building type through the existing off-map industry path, while facility transfers preserve the selected facility family. Persistent country and state flags record successful landings and each transferred installation class.

The transaction conserves one deployed formation and the locked six-battalion baseline manpower and equipment budget. The native raid consumes its separate sixty-unit transit payload. Damage and experience are intentionally normalized to the breach-cadre profile because the documented engine surface exposes no selected-division relocation or carried-state copy effect. The only documented relocation effect, `teleport_armies`, operates on an entire state with an owner filter and would move unrelated formations, so it is not used.

Every successful breach persists the exact province, attacking country, and original defending country on the target state. The state is entered into bounded attacker-owned and defender-owned active-beachhead registries, and a state with an active breach cannot receive another Portal raid. The registries are reconciled only through the affected state or the two participating countries; there is no recurring world scan.

After the original defender recaptures the exact saved province, `brilliant_scientist_seal_recaptured_portal_breach` becomes available on that state. Sealing takes 21 days and spends 25 Command Power. Losing the province cancels only the sealing attempt, leaving the breach active. Successful sealing, invalid participant state, the end of the war, Event 016 containment, and either terminal route use `brilliant_scientist_portal_cleanup_beachhead`, the single idempotent transient cleanup owner. Cleanup does not refund raid equipment, reverse transferred installations, recreate units, or erase permanent raid history.

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
- Defender sealing decision: `brilliant_scientist_seal_recaptured_portal_breach`
- State cleanup effect: `brilliant_scientist_portal_cleanup_beachhead`
- Country registry cleanup effect: `brilliant_scientist_portal_cleanup_country_beachheads`
- Runtime entity and preview animation: pending the existing-model runtime tranche; gameplay and counter wiring alone do not establish model acceptance.

## Required visual, sound, and counter assets

The evidence package is rooted at `docs/assets/shared_portal_raider_system/models_3d/portal_raider/`.
The accepted closure route preserves the existing body and recovers its rig, attaches the approved existing retro firearm with two-hand contact, provides a stable muzzle attachment, and finishes distinct actions, particles, light, and synchronized sourced sound.
Final runtime promotion requires actual-byte export/reimport evidence and matching entity/action consumers; the historical generation failure does not authorize regeneration or replacement geometry.

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
