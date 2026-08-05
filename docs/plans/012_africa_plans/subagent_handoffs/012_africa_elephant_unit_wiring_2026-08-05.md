# Event 012 armoured elephant unit wiring handoff — 2026-08-05

The parent runtime tranche consumes the approved shared model package as one custom `chaosx_elephant` subunit. No country tag, cosmetic tag, second body, or transform-only substitute was added.

## Runtime consumers

- Unit: `common/units/012_africa_elephant_forces.txt`.
- Equipment: `common/units/equipment/012_africa_elephant_equipment.txt`.
- Technology: `common/technologies/012_africa_elephant_technologies.txt`.
- Unlock and stockpile helpers: `common/scripted_effects/012_africa_elephant_effects.txt`.
- Event 012 host callsite: `common/scripted_effects/012_africa_effects.txt`.
- Action 102 member callsite and five package templates: `common/scripted_effects/012_africa_priority_member_effects.txt` and `common/scripted_effects/012_africa_priority_member_force_effects.txt`.

## Asset bindings

`chaosx_elephant` keeps its subunit sprite token, and every host/member division template explicitly sets `override_model = chaosx_elephant_shared_base_entity`. The six installed skeletal actions, sound package, and scale `0.8` therefore apply to every spawned consumer. The large and on-map counters reuse the inspected two-frame DDS package and are exposed under both the shared body and `chaosx_elephant` subunit icon tokens. The equipment/technology icon handoff is `012_africa_elephant_equipment_icon_2026-08-05.md` and the final runtime DDS is `gfx/interface/technologies/012_africa/chaosx_elephant_equipment.dds`.

## Mechanics

The unlock bridge grants vanilla `elephantry` and custom `chaosx_africa_elephant_warfare_tech`, then marks `africa_elephant_warfare_unlocked`. The preserved host receives two elephant regiments in Africa Charter Elephant Guard. Each promoted Action 102 member receives one elephant regiment in its package-specific guard template. Stockpile grants are idempotent and only run on the Event 012 opening or member activation path.

## Review status

Static source wiring and filesystem bindings are complete for this tranche. The achievement `africa_elephants_crossed_the_desert` remains runtime-evidence-gated until a live campaign proves movement, supply, destruction, and the required war-purpose witness. Further elephant loadouts must reuse this body and add a fresh documented consumer.
