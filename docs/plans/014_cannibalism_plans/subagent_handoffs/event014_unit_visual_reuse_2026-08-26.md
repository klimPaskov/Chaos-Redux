# Event 014 unit visual reuse decision

The unit gameplay profiles remain distinct, but the two formerly pending custom model packages are intentionally not part of the runtime surface.

| Sub-unit | Gameplay profile | Runtime sprite | Model decision |
|---|---|---|---|
| `cannibal_bone_riders` | Custom fast cavalry profile with `cavalry = yes` | `cavalry` | Reuse the installed vanilla cavalry entity and animation family. No Event 014 mesh or skeletal action package is required. |
| `cannibal_network_cadre` | Custom fast irregular-infantry profile | `infantry` | Reuse the installed vanilla infantry entity and animation family. No Event 014 mesh or skeletal action package is required. |

The mapping is implemented in `common/units/014_cannibalism_irregular_infantry.txt`. Event 014 remains responsible for each profile's statistics, equipment, activation, templates, counters, and scripted behavior; visual reuse does not merge the gameplay profiles or remove their unit identities.

The removed Bone Riders and Network Cadre 3D evidence workspaces are historical archive material after this decision. Their former provider, Blender, and generated-model paths must not be treated as runtime inputs or as evidence of a required remaining model task. The parent cleanup pass removed those two workspaces and retains this decision as the durable audit record.

The seven dedicated Event 014 model packages remain unchanged. Parent-owned entity/GFX wiring continues to cover only those seven dedicated sprite tokens; the two vanilla-reuse sprites intentionally have no Event 014 entity registration.
