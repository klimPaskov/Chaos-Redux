# undead_zombies runtime handoff

Status: `ready_for_user_live_validation`.

The selected Meshy 7 geometry package is complete through PDX mesh/material export, action export, and per-action reimport proof. Its runtime package is promoted under `gfx/models/units/chaosx_undead_zombies/`, with the entity and mesh registrations below.

- Mesh: `gfx/models/units/chaosx_undead_zombies/chaosx_undead_zombies.mesh`
- Actions: `chaosx_undead_zombies_idle`, `chaosx_undead_zombies_move`, `chaosx_undead_zombies_attack`, and `chaosx_undead_zombies_death`
- Entity: `chaosx_undead_zombies_entity`
- PDX mesh: `chaosx_undead_zombies_mesh`
- Unit consumer: `common/units/zombies.txt#undead_zombies`

Action-state audio uses the zombie soundeffects in `sound/chaosx_zombies_sound.asset`. Selection audio is the exact tag/original-tag consumer `ZZZ_infantry_idle` in the `Voices` category; it is intentionally tag-wide because HOI4 infantry selection voices are not sprite-specific. The seven specialized unit entities therefore receive zombie selection and action audio under the ZZZ identity.

Bespoke large and small counter DDS files were visually reviewed against their contact sheets and promoted to the paths already registered in `interface/chaosx_subuniticons.gfx`. The base `zombies` sprite and all armored zombie sprites remain unchanged. Live in-game playback and visual validation remain user-owned.
