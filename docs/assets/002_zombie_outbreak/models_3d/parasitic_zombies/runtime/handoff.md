# parasitic_zombies runtime handoff

Status: `ready_for_user_live_validation`.

The selected Meshy 7 geometry package is complete through PDX mesh/material export, action export, and per-action reimport proof. Its runtime package is promoted under `gfx/models/units/chaosx_parasitic_zombies/`, with the entity and mesh registrations below.

- Mesh: `gfx/models/units/chaosx_parasitic_zombies/chaosx_parasitic_zombies.mesh`
- Actions: `chaosx_parasitic_zombies_idle`, `chaosx_parasitic_zombies_move`, `chaosx_parasitic_zombies_attack`, and `chaosx_parasitic_zombies_death`
- Entity: `chaosx_parasitic_zombies_entity`
- PDX mesh: `chaosx_parasitic_zombies_mesh`
- Unit consumer: `common/units/zombies.txt#parasitic_zombies`

Action-state audio uses the zombie soundeffects in `sound/chaosx_zombies_sound.asset`. Selection audio is the exact tag/original-tag consumer `ZZZ_infantry_idle` in the `Voices` category; it is intentionally tag-wide because HOI4 infantry selection voices are not sprite-specific. The seven specialized unit entities therefore receive zombie selection and action audio under the ZZZ identity.

Bespoke large and small counter DDS files were visually reviewed against their contact sheets and promoted to the paths already registered in `interface/chaosx_subuniticons.gfx`. The base `zombies` sprite remains unchanged; armored undead, necrotic, and demonic variants reuse their corresponding specialized parent sprites. Live in-game playback and visual validation remain user-owned.
