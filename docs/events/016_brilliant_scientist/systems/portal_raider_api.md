# Portal Raider reusable unit and raid API

`portal_raider` is a shared land-unit family, not a Kruger-owned identity. Event 016 unlocks it through Portal Warfare, Event 019 can request it through the generic infantry-spawn provider, and later event packages may reuse the same subunit, equipment, and counter contract without copying Event 016 state.
The user's explicit 2026-09-25 decision says the Portal Raider, alien, and autonomous robot units already have good models and must remain untouched, followed by “don't create any models.” The user's statement is the model-quality approval for those existing assets. The older Portal Raider recovery and export directions below are historical only, superseded as active work by the [final completion contract](../../../specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md). Do not create, inspect, modify, regenerate, rig, animate, export, or otherwise touch any 3D/model asset or unit package under this task. Related sound, counter, effect, wiring, and live-consumer status is separate from this model-quality approval and remains unresolved where the documentation says so; no new model inspection was performed.

## Unit contract

The base battalion mirrors ordinary infantry for combat width, manpower, organization, recovery, suppression, supply, training time, and base combat statistics. Each battalion consumes 100 Infantry Equipment and 10 `teleportation_equipment_1`. Its exceptional combat performance comes from the grant-only Portal Warfare technologies rather than inflated subunit base values.

The default Event 016 template is `Quantum Transit Raiders`, a six-battalion locked formation. The reusable Event 019 provider uses family id `509` and charges the exact manpower, Infantry Equipment, and Teleportation Equipment manifest before spawning the requested formation.

## Portal Warfare raid surfaces

Both native Portal Warfare raids require seven days of preparation, ten Command Power, sixty Teleportation Equipment, and an assigned formation containing at least six `portal_raider` battalions. The native raid framework owns preparation, reservation, cancellation, expiry, outcome selection, and raid history. On success or critical success, a new six-battalion `Quantum Transit Raiders` cadre is committed in the captured target province and raises one scope-less reconstruction receipt. The assigned formation is consumed at its origin only when that receipt exists, so a target-state race cannot destroy the source without creating its replacement and a successful raid cannot retain both formations.

`brilliant_scientist_portal_facility_raid` is the state-targeted surface for hostile states containing factories, reactors, or rocket sites. Its target type is a state rather than an exact building, and its success path calls `brilliant_scientist_portal_raid_extract_state_installation`. A normal success attempts to extract one eligible state installation after the beachhead is established; a critical success calls the state-installation extraction twice before applying the heavy target damage.

`brilliant_scientist_portal_special_project_facility_raid` is the exact facility-target surface. Its target type is `building = { tags = facility }`, and its success path calls `brilliant_scientist_portal_raid_extract_installation` for the selected provincial special-project facility. A critical success may additionally call `brilliant_scientist_portal_raid_extract_state_installation` once, so the exact facility raid can take its selected facility and one state installation.

Both surfaces establish a captured hostile province and rebuild the selected formation there. Facility or state extraction occurs only when a valid owned destination with a compatible free slot exists; factory transfers preserve the building type through the existing off-map industry path, while facility transfers preserve the selected facility family. Persistent country and state flags record successful landings and each transferred installation class.

The transaction conserves one deployed formation but not its carried strength: the documented engine surface exposes no selected-division relocation or carried-state copy effect, so the breach force is a paid new cadre. It arrives with transit losses from `brilliant_scientist_portal_lifecycle` (experience factor 0.50, equipment factor 0.60, manpower factor 0.70) and refills through ordinary reinforcement from the stockpile and manpower pool, so a damaged formation never returns at full strength for free. The native raid consumes its separate sixty-unit transit payload. The only documented relocation effect, `teleport_armies`, operates on an entire state with an owner filter and would move unrelated formations, so it is not used.

Every successful breach persists the exact province, attacking country, and original defending country on the target state. The state is entered into bounded attacker-owned and defender-owned active-beachhead registries, and a state with an active breach cannot receive another Portal raid. The registries are reconciled only through the affected state or the two participating countries; there is no recurring world scan.

After the original defender recaptures the exact saved province, `brilliant_scientist_seal_recaptured_portal_breach` becomes available on that state. Sealing takes 21 days and spends 25 Command Power. Losing the province cancels only the sealing attempt, leaving the breach active. Successful sealing, invalid participant state, the end of the war, Event 016 containment, and either terminal route use `brilliant_scientist_portal_cleanup_beachhead`, the single idempotent transient cleanup owner. Cleanup does not refund raid equipment, reverse transferred installations, recreate units, or erase permanent raid history.

HOI4 has no province scope: `var:target_province` and `brilliant_scientist_portal_breach_province` are integer province IDs, never scopes.
The facility raid's native `building = { tags = facility }` target already guarantees a facility in the selected province, so `brilliant_scientist_portal_facility_raid_target_is_valid` checks only the state, the war, and a compatible destination.
`brilliant_scientist_portal_raid_extract_installation_internal` copies the raid province into a temporary and pastes it into `any_province_building_level = { province = { id = ... } building = <facility> level > 0 }` through `meta_trigger`, so only a facility that exists in that exact province is removed and rebuilt, and no facility can be duplicated.
The breach is registered on its own state, so the runtime check needs no province-to-state test.
`brilliant_scientist_portal_breach_province_is_controlled_by_root` pastes the stored breach province into a country-scope `controls_province` check; the sealing decision's target trigger, its cancel trigger, and the sealing settlement all use it, so sealing can start and stay active only while the original defender controls the exact breach province.

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
- Runtime entity and preview animation: historical handoffs record package-specific status, but current acceptance is unresolved; this entry does not queue model work.

## Historical visual, sound, and counter evidence

Earlier handoffs located evidence at `docs/assets/shared_portal_raider_system/models_3d/portal_raider/`; this documentation pass did not inspect that package.
The earlier closure route proposed preserving the body, recovering the rig, attaching the retro firearm, and finishing actions and effects. That proposal is superseded as active production direction by the September 25 no-model decision. Prior export/reimport requirements remain historical acceptance criteria only and do not authorize work on the model.

- Earlier handoffs named `gfx/models/units/portal_raider/portal_raider.mesh`, material DDS maps, and skeletal actions as recovery outputs; their current status was not verified here.
- Earlier handoffs named `gfx/entities/portal_raider.gfx` and `gfx/entities/portal_raider.asset` as recovery outputs; their current registration was not verified here.
- Earlier handoffs named `sound/portal_raider_sound.asset` and synchronized licensed audio as recovery outputs; their current status was not verified here.
- `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds` are complete and wired through `interface/portal_raider_system.gfx`; these counters do not imply model/entity completion.
- The active subunit-icon GFX registry entries for both counter tokens are complete and wired.
- The already registered technology and equipment icon sprites used by the technology, equipment, production, and raid surfaces remain unchanged.

The historical design called for an identity-neutral unit with protective goggles, an insulated suit, a teleportation backpack, and a retro ray rifle. This description is retained as context and does not authorize model inspection or changes.

## Future extensions

Later events can grant the portal technology API, create Portal Raiders through Event 019, or define another raid using the shared unit, equipment, and counter contract. A new consumer should reuse the identifiers above, preserve the ten-equipment-per-battalion contract, and record its own event history rather than setting Event 016 host or Kruger flags. Every future Chaos Redux special project must be reviewed for inclusion in the reusable CBRN random and project registries before it is accepted as a new consumer.

Potential extensions include defensive emergency extraction, reinforcement of isolated bridgeheads, and project-facility evacuation. They should use the same exact equipment reservation and destination-slot checks instead of creating a parallel teleportation ledger.
