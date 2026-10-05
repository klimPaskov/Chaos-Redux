# Event 042 Evolution III Special-Equipment Registry

This registry decides which existing Chaos Redux equipment can fall from the sky during Evolution III. A family is allowed only when a recipient can field it through an ordinary battalion consumer without gaining production, owner technology, or any owner-event lifecycle state. The runtime rows live in `common/scripted_effects/042_equipment_from_heavens_special_effects.txt`, the ids in `equipment_from_heavens_special` in `common/script_constants/042_equipment_from_heavens_constants.txt`, and the receipts in `common/technologies/042_equipment_from_heavens_fielding_technologies.txt`.

Repository revision reviewed: working tree on 2026-09-25 above commit `50a97347a`.

## Receipt contract

Each allowlisted family gets one hidden technology with `allow = { always = no }`, `ai_will_do = { factor = 0 }`, no folder, and a single `enable_subunits` entry. It enables no equipment and adds no modifier. The precedent is `common/technologies/014_cannibalism_irregular_activation_technologies.txt`, which uses the same shape for inactive Event 014 battalions.

The receipt also adds one editable six-battalion template (four for the width-three creatures) named after the family. The receipt is idempotent: the technology and template are only added when missing.

Production stays closed because every allowlisted equipment family is enabled only by its owner technology and gated by owner `can_be_produced` conditions, and the receipt touches neither. Stockpiled equipment of an unresearched type can still equip a division, which is the ordinary captured-equipment rule.

The receipt never calls `chaosx_grant_custom_operational_technology`, because that API sets the `chaosx_custom_technology_<family>_operational` flags that the Event 016 equipment `can_be_produced` blocks read as a production unlock.

## Allowed families

| Id | Family | Token | Consumer and need per battalion | Receipt | Owner event | Quantity basis |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Clone cohorts | `clone_equipment_1` | `clone_infantry`, 90 infantry equipment and 1 cohort | `equipment_from_heavens_clone_fielding_tech`, template "Unmarked Cohort Brigade" | 16 | 50-150, 150-300, or 300-500 cohorts plus 90 rifles per cohort |
| 2 | Combat robots | `autonomous_robot_equipment_1` | `autonomous_robot`, 50 robots and 10 support equipment | `equipment_from_heavens_robot_fielding_tech`, "Unmarked Machine Column" | 16 | battalion band × 50 |
| 3 | Portal raider kits | `teleportation_equipment_1` | `portal_raider`, 100 infantry equipment and 10 kits | `equipment_from_heavens_portal_fielding_tech`, "Unmarked Gate Company" | 16 | battalion band × 10 |
| 4 | Paleogenetic creatures | `paleogenetic_creature_equipment_1` | `paleogenetic_creature`, 55 creatures and 15 support equipment | `equipment_from_heavens_paleogenetic_fielding_tech`, "Unmarked Beast Column" | 16 | battalion band × 55 |
| 5 | Xenobiological organisms | `xenobiological_assault_organism_equipment_1` | `xenobiological_assault_organism`, 50 organisms and 20 support equipment | `equipment_from_heavens_xenobiological_fielding_tech`, "Unmarked Organism Column" | 16 | battalion band × 50 |
| 6 | Temporal guard kits | `temporal_guard_equipment_1` | `temporal_guard`, 45 kits, 60 infantry and 15 support equipment | `equipment_from_heavens_temporal_fielding_tech`, "Unmarked Guard Detachment" | 16 | battalion band × 45 |
| 7 | Coal golems | `coal_golem_equipment_1` | `coal_golem`, 70 golems | `equipment_from_heavens_golem_fielding_tech`, "Unmarked Stoneworks Brigade" | 5 | battalion band × 70 |

Battalion bands are 10-40, 40-100, or 100-250 battalion-equivalents by magnitude.

### Per-family evidence

- Clone cohorts. `clone_infantry` in `common/units/clone_infantry.txt` is `active = no`. The owner access technology `clone_infantry_access_tech` enables both equipment and subunit, so Event 42 uses its own subunit-only receipt instead. Clone maturation requires the Kruger cloning focus and owner growth-site state flags, so a recipient cannot start production. The shared weekly clone reserve pays ten manpower per stockpiled cohort to any holder (`clone_refresh_reserve_manpower`). The Event 42 band is reduced from the spec starting values to keep that reserve at most 5,000 weekly manpower, and the reserve shrinks as cohorts are fielded or lost.
- Combat robots. The shared robot system (`docs/systems/shared_autonomous_robot_system.md`) is provider-neutral. Production requires `chaosx_custom_technology_robot_operational` or the Event 016 robotics project stage plus host state. The receipt does not unlock the Event 016 stat technology, so Event 42 robots use base statistics.
- Portal raiders, paleogenetic creatures, xenobiological organisms, temporal guards. Each battalion in `common/units/016_brilliant_scientist_project_forces.txt` is `active = no`, and each equipment `can_be_produced` requires owner operational flags or Event 016 project deployment plus host or Kruger state. The only script that reads these battalions on divisions is the Event 016 achievement snapshot, which uses `any_country_division` in the Kruger country's own scope, so an Event 42 recipient's divisions never enter it.
- Coal golems. `coal_golem` is `active = no` and had no enabling technology. KMB fields it through script-built templates. Equipment production is limited to KMB and validated Event 019 golem derivatives. The Event 42 receipt is the first design-screen exposure of this battalion, and it grants no KMB, derivative, or provider identity.

## Isolation checks

`equipment_from_heavens_grant_special_family` reads whether the owner event is in `global.fired_events` before and after the grant and records `efh_special_isolation_receipt_intact` when the value is unchanged. Every receipt is also logged in `global.efh_special_receipt_country_entries`, `_family_entries`, and `_owner_fired_entries`. The receipt writes no owner fired count, weight, cap, evolution flag, log record, country, host marker, world-threat flag, focus or decision unlock, project or facility state, super-event flag, or terminal-route flag.

If the owner event fires later it keeps full authority. Its own technologies add production and bonuses on top of the Event 42 receipt, and its template creation uses its own template names, so the neutral Event 42 template never collides. Event 42 never removes owner stockpile or templates.

## AI plan

The receipt template is available to the AI's ordinary recruitment logic. The stockpile bounds how many battalions can ever be equipped, the AI still pays manpower, training, and supply, and no free divisions are created. The assessment flag `efh_ai_special_windfall` records the delivery. There is no Event 42 production of special equipment, so fielded formations shrink as losses mount.

## Cleanup

Receipts, templates, and stockpile persist after the landing chain closes, as for conventional equipment. Disabling Evolution III stops future special slots and leaves existing receipts in place.

## Excluded families

| Family | Reason |
| --- | --- |
| Alien laser weapons (`alien_laser_weapon_equipment_1`) | `alien_infantry` is permanently inactive in the division designer and exists only in API-locked landing cohorts that require an alien-contact receipt. There is no fielding path without owner identity. |
| Event 012 strange formations (eight `africa_*_equipment_1` tokens) and elephants (`chaosx_elephant_equipment_1`) | Their consumers belong to the Event 012 package, whose global package-ready flag also guards model and presentation readiness. Fielding them before the owner package is ready risks broken presentation, so they stay excluded until the owner exposes a readiness-independent fielding receipt. |
| Every weapon payload family (biological, chemical, and special bombs, cylinders, shells, agent lots, and projectors) | Their consumers are raids whose visibility requires owner technologies or special projects. A usable payload would require granting research or activating owner systems, which the registry forbids. They remain excluded. |
| Protective and decontamination equipment | These are ordinary research-tree items rather than Chaos special capabilities and do not fit the Evolution III identity. |

## Queued work

Additional families can join when their owners expose a fielding-only split or an owner-neutral consumer. Each new row needs the columns above, a receipt, a template, an owner event id, a quantity basis, and the isolation check.
