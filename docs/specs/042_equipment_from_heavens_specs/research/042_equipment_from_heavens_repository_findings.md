# Event 42 repository findings

## Purpose

This note records repository facts that materially shaped the Event 42 specification. It is not a full implementation audit. The local repository, installed vanilla game, offline wiki, and HOI4 MCP remain the authoritative implementation evidence surfaces.

## Current catalog state

The current event export lists Event 42 as:

- name: Equipment from heavens
- type: Minor Repeatable
- Chaos level: 1
- status: To Be Reworked
- cluster: blank
- member severity: blank

The accepted design uses the title Equipment from Heavens and assigns the event to Various Anomalies as a Low member.

The current cluster export has an unavailable Various Anomalies row with no numeric ID, no details, no members, type Minor Fire-Once, and Chaos level 4. Implementation must reconcile this in the workbook and live registry. The specification does not invent a cluster ID.

## Shared country classifiers

The supplied `chaosx_dynamic_triggers.md` defines the shared roles of:

- `is_special_chaos_country`
- `is_actual_nonhuman_country`
- `uses_normal_civilian_systems`

Event 42 should use these shared contracts as part of its ordinary-recipient validation. It should not create a second local definition of special or nonhuman countries.

## Shared dynamic effects

The supplied `chaosx_dynamic_effects.md` confirms that the central dynamic registry is reserved for neutral helpers with callers across several systems. Event 42-specific manifest generation, target selection, report orchestration, compatibility receipts, and lifecycle cleanup belong in Event 42-owned files unless another event also needs the exact contract.

The same document confirms existing neutral stockpile-debit helpers and owner-owned APIs for clone systems, alien infantry, project bridges, unit-family registration, and CBRN-related systems. Event 42 should call owner APIs rather than copying owner state.

## CXT concrete stockpile inventory

`common/scripted_effects/chaosx_test_country_stockpile_effects.txt` contains an explicit list of concrete equipment tokens that can be added through `add_equipment_to_stockpile`. Relevant existing tokens include:

- `clone_equipment_1`
- `alien_laser_weapon_equipment_1`
- `autonomous_robot_equipment_1`
- `teleportation_equipment_1`
- `paleogenetic_creature_equipment_1`
- `xenobiological_assault_organism_equipment_1`
- `temporal_guard_equipment_1`
- `coal_golem_equipment_1`
- `plague_bomb_1`
- `anthrax_bomb_1`
- `tularemia_bomb_1`
- `smallpox_bomb_1`
- `zombie_disease_bomb_1`
- `malodor_bomb_1`
- `aphrodisiac_bomb_1`
- chemical payload cylinders, shells, air payloads, and agent lots
- eight Event 012 strange-formation equipment tokens
- `chaosx_elephant_equipment_1`
- CBRN protective and decontamination equipment

This inventory proves a concrete grant token exists. It does not prove independent fielding, mission access, AI use, or source-event isolation.

## Clone equipment

`common/units/equipment/clone_equipment.txt` defines `clone_equipment_1` under a provider-neutral clone archetype.

`docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md` states:

- one stockpiled unit represents one viable standardized clone cohort
- every full stockpiled unit contributes ten weekly manpower through the clone reserve modifier
- captured, transferred, or lend-leased clone equipment benefits its current holder even when the holder cannot manufacture clones
- the `clone_infantry` battalion consumes one clone-equipment unit per battalion
- `clone_grant_infantry_access` enables manufacture and recruitment and creates a template

This is the clearest existing provider-neutral cross-event equipment family. Raw stockpile has a real effect, but fielding access is currently coupled with manufacturing access. Event 42 needs a fielding-only clone receipt or an owner-approved split of the existing API.

## Event 16 project-force equipment

`common/units/equipment/016_brilliant_scientist_project_force_equipment.txt` defines six concrete families:

- teleportation equipment
- autonomous robot equipment
- paleogenetic equipment
- xenobiological equipment
- alien laser equipment
- temporal equipment

Their production rules depend on Event 16 project stages, Kruger host and character state, specialized facilities, or provider-neutral alien contact.

`common/units/016_brilliant_scientist_project_forces.txt` defines matching inactive battalions. The file states that six legacy families consume their owner project systems and that alien infantry uses a provider-neutral source-counted contact unit. Ordinary division-designer access is not available by default.

Physical grant is therefore proven, but independent field use is not. Event 42 must not set Event 16 project, host, facility, character, or contact-source state merely to activate a stockpile.

## Coal golems

`common/units/equipment/coal_golems.txt` defines `coal_golem_equipment_1`. Production is restricted to the Kuznetsk Mining Board and validated Event 19 golem derivatives.

`common/units/coal_golems.txt` defines an inactive `coal_golem` battalion that consumes seventy equipment units.

A fielding-only receipt could make the stockpile usable, but the recipient must not become KMB, an Event 19 derivative, or a producer.

## Event 012 strange formations

`common/units/equipment/012_africa_strange_force_equipment.txt` defines eight isolated equipment archetypes and variants. The file states that the global package gate controls production and that parent-owned effects seed stockpiles after model readiness.

The matching `common/units/012_africa_strange_forces.txt` file defines the consumers. These families need a separate owner-reviewed fielding receipt. Event 42 cannot set the global Event 012 package-ready flag because that flag belongs to the full source package.

## Biological payloads

`common/units/equipment/bioweapons.txt` defines physical anthrax, plague, tularemia, and smallpox bomb variants.

The current Black Plague weaponization triggers show that `plague_bomb_1` delivery also depends on:

- Black Plague system activation
- a completed project or delivery technology
- weaponization completion and delivery-ready flags
- support equipment, command power, and fuel
- a hostile valid target state
- cooldown and exposure lifecycle logic

Raw payload stockpile is insufficient. Event 42 should use these payloads only after an owner-neutral captured-payload contract exists.

The same standard applies to zombie-disease payloads and other biological bombs. Event 42 should not initialize the full biological warfare system or start an outbreak merely because a crate was opened.

## Chemical special bombs and payloads

`common/units/equipment/chemical_special_bombs.txt` defines malodor and aphrodisiac bomb variants as stockpiled payloads consumed by raid-launched special chemical strikes.

Other current equipment files define agent lots, cylinders, shells, aircraft payload lots, Livens projectors, protective equipment, and decontamination equipment.

These items belong to shared CBRN command and delivery systems. Protective and decontamination equipment may be easier to distribute safely than offensive payloads, but every family still needs a consumer and AI review. Event 42 cannot activate the complete Chaos Warfare or CBRN command package as a compatibility shortcut.

## Nuclear stockpile precedent

`common/scripted_effects/chaosx_test_country_effects.txt` uses `add_nuclear_bombs`, proving the physical stockpile effect is available.

The test-country setup also completes all technologies and facilities, so it does not prove that a normal country without nuclear research can launch received bombs. Event 42 must inspect vanilla and current mod launch conditions directly.

## Conventional designer equipment

The supplied repository evidence does not prove that every bare tank chassis or aircraft airframe is a usable finished item under every DLC configuration. Event 42 therefore needs a curated complete-variant registry and a non-DLC fallback path.

The event should never grant an empty chassis only because `add_equipment_to_stockpile` accepts its token.

## Event identity boundaries

The catalog contains nearby concepts that must remain distinct:

- Soldiers from Nowhere creates personnel or formations
- Eq aid uses a known major donor and minor ally recipient
- Arms for Everyone distributes infantry equipment globally
- Army Loses Equipment removes stockpile
- Missiles Giveaway concerns missile technology and missiles

Event 42 remains a recipient-neutral physical anomaly with no sender, no personnel, no diplomatic relationship, no global universal grant, and no technology award.

## Implementation consequences

The repository findings support these design decisions:

1. Conventional equipment uses a curated complete-token or complete-variant registry.
2. Clone equipment is the first provisional special-family candidate.
3. Every other named special family remains conditional until its actual consumer can be exposed without source production or lifecycle state.
4. Nuclear receipt is incomplete until launch-only behavior is proven.
5. Event 42 must use owner APIs and compatibility receipts instead of copying event flags.
6. CXT stockpile presence is evidence of grant syntax only.
7. The final allowlist belongs to the repository revision and must be re-audited when owner equipment systems change.
