# Death ghost host rebuild (2026-09-27)

Disposition: `implemented` — the shared ghost host model, eight actions, textures, mesh registration, and timed entity are installed; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27 and asked that every remaining model be finished thoroughly, using renders of the current models as references.

## Why it was replaced

The shipped model had five actions, so `defend`, `support_attack`, and `training` played other roles, and its greatcoat mesh had torn-through holes that showed the background.

## Route

The reference `docs/assets/010_death/models_3d/ghost_hosts/refs/original/meshy_input_v3.png` keeps the legacy identity (skull face under a steel helmet, cold blue eye-light, torn greatcoat, belt and canteen, clawed grey-blue hands) with a closed, intact coat, drawn from a render of the legacy model in `refs/legacy_model/`.
Meshy 7 body, one rig, six presets (Idle 3, Unsteady Walk, Walk Backward, Head Hold in Pain, Electrocuted Fall, Mage Spell Cast), and two prime text-to-motion actions (a gliding double claw rake; a life-draining reach) — 79 credits, recorded in the credit ledger.
The ghost holds nothing, so there is no item step.

## Runtime

`gfx/models/units/death_ghost_hosts/` holds the mesh (four streams), eight `.anim` files, and three maps; `gfx/entities/010_death_ghost_hosts.gfx` keeps the mesh name `death_ghost_hosts_mesh`, and `gfx/entities/010_death_ghost_hosts.asset` keeps `death_ghost_entity` with eight distinct states timed from the phase review, using the existing ghost sound effects.
All eight actions are grounded to 4 mm and reimport-proven.

## Remaining limits

- The idle includes a raised-arm stretch; it reads as a wail on this character but is a provider motion, not authored for a ghost.
- Counter art was not changed.
