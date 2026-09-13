# Event 42 special-equipment audit matrix

## Status vocabulary

- **Provisional allowlist** means current evidence supports inclusion after one named narrow compatibility change and full implementation testing.
- **Conditional** means the token exists but independent use, AI, or source isolation is not yet proven.
- **Excluded** means current owner contracts make safe Event 42 use too broad or impossible without redesign.
- **Defensive candidate** means the item may enter Evolution III as useful special equipment even when it is not a weapon, after consumer review.

No row becomes final merely because the CXT test country can add the token to stockpile.

## Current matrix

| Owner | Exact token or family | Physical stockpile proof | Current consumer | Independent-use finding | Minimum acceptable Event 42 receipt | Production rule | AI requirement | Forbidden side effects | Provisional status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shared clone system | `clone_equipment_1` | Explicit CXT grant and provider-neutral transfer docs | `clone_infantry`, clone reserve manpower | Raw stockpile gives reserve manpower to any holder. Fielding access is coupled with manufacture in the current public effect | Fielding-only clone access plus one bounded template, or owner split of fielding from manufacture | Remain unavailable unless normally earned | Cap division creation by stockpile, rifles, manpower, and supply. Audit weekly reserve-manpower scaling | Do not grant Kruger or Mengele refinement, clone production, projects, source events, or Aryan access | Provisional allowlist after fielding split and balance audit |
| Event 16 teleportation | `teleportation_equipment_1` | Explicit CXT grant | inactive `portal_raider` battalion | Stockpile alone cannot be fielded through normal designer | Fielding-only portal-raider access and one template | Keep Event 16 project and facility production gates | Use only with rifles, manpower, and supply. Finite stockpile | Do not set Kruger host, portal project stages, operational flags, terminal state, or facilities | Conditional |
| Event 16 robotics | `autonomous_robot_equipment_1` | Explicit CXT grant | inactive `autonomous_robot` battalion | Stockpile alone cannot be fielded through normal designer | Fielding-only robot battalion and one template | Keep robotics project and facility production gates | Require support equipment, fuel, and supply. Bound army share | Do not set Kruger host, robotics stages, assembly complex, or Event 16 threat state | Conditional |
| Event 16 paleogenetics | `paleogenetic_creature_equipment_1` | Explicit CXT grant | inactive paleogenetic battalion | Stockpile alone cannot be fielded | Fielding-only battalion and one template | Keep project, site, and production gates | Require support equipment and terrain-aware template use | Do not create reserves, hatcheries, Kruger state, or project completion | Conditional |
| Event 16 xenobiology | `xenobiological_assault_organism_equipment_1` | Explicit CXT grant | inactive xenobiological battalion | Stockpile alone cannot be fielded | Fielding-only battalion and one template with owner-approved control behavior | Keep project, control-method, site, and production gates | Require support equipment and conservative deployment | Do not choose a control method, create vats, set research, or start Event 16 | Conditional |
| Shared alien-contact system | `alien_laser_weapon_equipment_1` | Explicit CXT grant | provider-neutral alien infantry locked cohort | Contact API is provider-neutral, but ordinary fielding still needs owner access | Captured-alien-weapon fielding receipt that does not add contact sources | No production without normal contact | Field only through finite stockpile and owner-approved template | Do not create alien contact, Event 25 result, Event 16 host, projects, or source counts | Conditional |
| Event 16 temporal | `temporal_guard_equipment_1` | Explicit CXT grant | inactive temporal battalion | Stockpile alone cannot be fielded | Fielding-only battalion and one template | Keep temporal project and anchor production gates | Conservative finite fielding with rifles, support, manpower, and supply | Do not create temporal anchor, project state, time-travel events, or source host | Conditional |
| KMB and Event 19 golem provider | `coal_golem_equipment_1` | Explicit CXT grant | inactive `coal_golem` battalion | Stockpile alone cannot be fielded | Fielding-only golem battalion and one template | Keep KMB and validated derivative production gates | Bound army share, require supply, no production plan | Do not set KMB tag, Event 19 derivative flags, family ID, or provider proofs | Conditional |
| Event 012 strange formations | eight `africa_*_equipment_1` tokens | Explicit CXT grants | eight inactive Event 012 battalions | Stockpile alone cannot be fielded | Separate fielding-only receipt per family and one matching template | Keep global package-readiness and owner production gates | Family-specific template, terrain, fuel, and support rules | Do not set Africa package ready, fire Event 012, create countries, gods, routes, or super-events | Conditional |
| Event 012 elephants | `chaosx_elephant_equipment_1` | Explicit CXT grant | Event 012 elephant consumer | Requires owner consumer and setup review | Fielding-only consumer if source API supports isolation | Keep owner production gate | Terrain-aware finite deployment | Do not activate Event 012 country or route state | Conditional |
| Event 020 Black Plague | `plague_bomb_1` | Explicit CXT grant and equipment definition | Black Plague weaponization delivery | Delivery requires active system, projects or tech, completion flags, support resources, target, and cooldown | Provider-neutral captured-payload action that consumes one bomb and uses ordinary exposure and consequence logic | No production | Use only against valid enemy state under shared AI and CBRN policy | Do not activate Black Plague, complete weaponization, create Rat Nations, set world threat, or open terminal route | Excluded from first allowlist, conditional on owner API |
| Shared biological warfare | `anthrax_bomb_1`, `tularemia_bomb_1`, `smallpox_bomb_1`, `zombie_disease_bomb_1` | Explicit CXT grants and equipment definitions | biological strike or raid systems | Raw stockpile does not prove mission access | Owner-neutral captured-payload action per agent with full consequence routing | No production | Existing target, policy, delivery, and retaliation logic | Do not complete projects, activate outbreaks, unlock doctrine, or set source-event flags | Conditional |
| US chemical special raids | `malodor_bomb_1`, `aphrodisiac_bomb_1` | Explicit CXT grants and equipment definitions | raid-launched special chemical strikes | Raw stockpile does not prove raid access | Captured-payload raid action with normal target and consequence rules | No production | Existing raid AI or explicit exclusion from AI pool | Do not unlock USA weapon-test content, research, or unrelated raid families | Conditional |
| Shared CBRN offensive payloads | chemical agent lots, cylinders, shells, air payloads, Livens projectors | Explicit CXT grants | CBRN support units, operations, and raids | Depends on command, readiness, units, and delivery systems | Narrow captured-payload or captured-support receipt for exact family | No production | Existing CBRN AI, use policy, condemnation, and target rules | Do not establish Chaos Warfare, initialize every CBRN system, grant doctrine, or create facilities | Conditional |
| Shared CBRN protection | gas masks, instruments, decontamination equipment | Explicit CXT grants | protection and decontamination systems | May provide defensive stockpile value with smaller compatibility need | Owner-neutral defensive equipment recognition if current systems ignore stockpile without tech | No production | AI uses through existing protection and decontamination priorities | Do not grant doctrine, facilities, readiness cap, or offensive use policy | Defensive candidate |

## Required audit columns before final allowlisting

Every final row must add:

- repository revision
- equipment definition path
- consumer definition path
- owner effect or trigger paths
- local vanilla or mod precedent used
- stockpile grant test
- fielding or payload test
- save and reload test
- AI test
- production denial test
- owner-event pre-state and post-state comparison
- source-event later-firing test
- cleanup test
- quantity formula and battalion-equivalent calculation
- achievement-use callback
- CXT setup and registry coverage when a new compatibility carrier is introduced
- final reviewer and date

## Fielding receipt design test

A fielding receipt passes only when:

1. The country can create or receive one valid template using the existing battalion.
2. The template consumes the delivered special equipment.
3. The country cannot manufacture replacement special equipment through the receipt.
4. The source event remains unfired and unchanged.
5. The template disappears or becomes harmless when its owner package is removed, while deployed divisions and stockpile follow an explicit cleanup rule.
6. AI can use the template without creating zero-cost or zero-equipment formations.
7. The receipt is idempotent and does not duplicate templates after save, reload, later delivery, or source-event firing.

## Captured-payload receipt design test

A captured-payload receipt passes only when:

1. A positive real payload is present.
2. Use consumes the payload once.
3. The target and delivery platform are valid.
4. Ordinary command, fuel, range, war, use-policy, and cooldown rules remain.
5. Deaths, contamination, attribution, Condemnation, retaliation, and Chaos route through the owner systems once.
6. The source event remains unfired and unchanged.
7. The action disappears when no payload remains.
8. AI has a valid bounded use rule or the family is excluded from AI deliveries and therefore from the shared random pool.

## Initial implementation recommendation

The first safe Evolution III implementation should start with clone equipment only after the fielding-only split is complete and the reserve-manpower scale is balanced. Additional families should enter one owner-reviewed row at a time.

This staged allowlist is an implementation order, not a reduction of the accepted final design. Evolution III is complete only when several distinct safe special families exist and the pool produces meaningful variety. If the repository cannot support that variety without owner redesign, report the stage as incomplete.
