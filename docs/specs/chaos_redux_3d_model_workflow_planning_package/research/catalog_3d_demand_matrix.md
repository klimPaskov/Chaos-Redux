# Catalog 3D Demand Matrix

The full event, cluster, and scenario catalogs were parsed before this matrix was written. The matrix identifies likely reusable workflow consumers. It does not assert that every row already requires a new model, and it does not change catalog status.

| Event or scenario | Name | Likely 3D need | Workflow profile |
| --- | --- | --- | --- |
| 2 | Zombie Outbreak | Humanoid and variant zombie unit models, attack, move, idle | `humanoid_biped plus creature variants` |
| 10 | Death | Death host model family, passive host variants, reveal presentation | `creature or humanoid custom` |
| 19 | Infantry Spawn | Conventional and specialist spawned unit identity models | `humanoid_biped and vehicle` |
| 25 | Alien Technology | Alien equipment, machines, structures, and animated devices | `vehicle, prop, building` |
| 36 | Alien Spacecraft | Spacecraft, landing craft, and animated alien machinery | `aircraft and vehicle` |
| 38 | Malta Crusaders | Crusader infantry, cavalry, banners, and siege identity | `humanoid_biped and cavalry` |
| 56 | Navy | Naval model variants and unusual vessel identities | `naval` |
| 57 | Radar | Radar buildings and animated dishes when justified | `building and mechanical rig` |
| 68 | ZIN | Custom armed forces and route-specific state models | `humanoid_biped and vehicle` |
| 73 | Mongols | Cavalry and mounted unit family | `cavalry custom rig` |
| 80 | Airship | Strategic airship model and moving control surfaces | `aircraft and mechanical rig` |
| 90 | Suicide Craft | Specialized explosive craft and attack animation | `vehicle` |
| 118 | Plague of Locust | Locust swarm representation or host marker models | `creature swarm` |
| 139 | Mysterious Creature | Unknown creature model family and custom locomotion | `creature custom rig` |
| 140 | Dracula | Vampiric leader or unit variants and transformation assets | `humanoid_biped plus creature` |
| 142 | Partisans | Partisan infantry variants and irregular equipment | `humanoid_biped` |
| 158 | Tomorrow's Girls | Clone or altered soldier unit family | `humanoid_biped` |
| 160 | Shark-infested Waters | Shark or sea-creature representation and maritime hazards | `creature or naval` |
| unassigned | Super Soldiers | Enhanced soldier models and action variants | `humanoid_biped` |
| unassigned | Crazy Scientist | Scientist, laboratory machines, and facility props | `humanoid_biped, prop, building` |
| unassigned | Facilities | Research, containment, military, and anomalous buildings | `building` |
| SCN-002 | Army of Clones | Clone army model family and stronger variant | `humanoid_biped` |
| SCN-006 | Death | Death outbreak host and passive host variants | `creature or humanoid custom` |
| SCN-013 | The Unbidden Muster | Zombie, ghost, golem, specialist vehicle, and claimant formations | `mixed profiles` |

## Production implications

- A humanoid-only pipeline would fail a large part of the catalog. Creature, cavalry, vehicle, naval, aircraft, prop, and building profiles are mandatory.
- Reusable skeleton families should be created only after at least two assets prove the same body plan and animation set.
- Large scenario families need asset inheritance and variation rules so they do not produce hundreds of unrelated rigs.
- Event ownership, asset IDs, final runtime consumers, and source provenance must be recorded in each model manifest.
- The event catalog workbook remains the only editable catalog source. This planning package does not edit CSV exports.
