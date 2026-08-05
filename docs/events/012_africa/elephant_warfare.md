# Event 012 armoured elephant warfare

Event 012 opens the armoured elephant capability as a visible force consequence of the preserved host's protection-first charter. The host receives the custom `chaosx_elephant` technology bridge and a named Africa Charter Elephant Guard on owned, controlled territory. The bridge also grants vanilla `elephantry` for compatibility with the installed vanilla roster, but the Event 012 formations use the custom subunit and its custom equipment line.

The custom equipment archetype is `chaosx_elephant_equipment` with buildable variant `chaosx_elephant_equipment_1`. It is gated by `africa_elephant_warfare_unlocked`, consumes steel, chromium, rubber, and fuel, and provides the armour, hardness, piercing, breakthrough, defence, and attack values used by the subunit. The equipment icon is the approved 131x52 DDS at `gfx/interface/technologies/012_africa/chaosx_elephant_equipment.dds`; `interface/012_africa_elephant.gfx` registers the equipment and technology tokens.

The `chaosx_elephant` subunit is active only through `chaosx_africa_elephant_warfare_tech`. It is a mobile front-line armoured formation with a combat width of four, a real `armor_value`, and a need for `chaosx_elephant_equipment_1`. Every host and member division template explicitly overrides its entity to `chaosx_elephant_shared_base_entity`, so each spawned consumer uses the same oversized elephant with rider, six skeletal actions, licensed source audio, and bespoke two-frame counter package.

Action 102 member registration calls `africa_elephant_prepare_member_guard` before the existing package force initializer. The five structural templates—royal guard, river guard, mobile guard, highland guard, and coastal guard—each add one `chaosx_elephant` regiment while preserving their package-specific infantry, cavalry, support, names, readiness, and reserve logic. The helper is idempotent and gives each package one seed equipment stockpile; later reinforcement remains governed by the existing package force actions.

No recurring world scan was added. The host and member helpers only execute from the Event 012 opening and Action 102 package activation surfaces, respectively. The shared entity, sound, animation, counter, equipment, unit, technology, and localisation identifiers are all parent-wired in the same tranche.

## Future extensions

Additional elephant loadouts can reuse the body and counter bytes while changing only equipment variants or package-owned formation roles. Any such extension must retain the protection-first consent gates, avoid new country tags, and add its own documented runtime consumer before its ledger row is promoted.
