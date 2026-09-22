# Event 016 biological raids

Event 016 attacks use the existing `biological_raids` category and the native raid preparation, equipment reservation, Command Power, cancellation, and history system.
The equipment stockpile remains authoritative.
Each raid names its agent and method, so the player chooses the payload in the raid panel without maintaining a selected arsenal, a staging directive, or a separate attack decision.
The unrelated Event 016 Portal facility raids retain their own category.

## Unlocks and equipment

Anthrax, Plague, Tularemia, and Smallpox accept either their completed special project or delivery technology.
Weaponized Zombies accepts its completed project, completion flag, or delivery technology.
Engineered Black Plague requires its weaponization receipt or explicit Kruger authorization and spends Plague Bomb equipment because the accepted Event 020 program uses the same physical delivery stock.
The five concrete equipment models are buildable through their delivery technologies, and the common biological AI production strategies cover them, including Zombie Disease Bombs.
An AI country with the offensive Event 020 Black Plague program maintains a two-bomb Plague reserve under safe stockpile conditions, even without a generic strategic CBRN production posture; generic safe, desperate, and Japan campaign Plague demand takes precedence when active.
CXT's debug stockpile includes all five models; its player-triggered refill action is deliberately repeatable.

| Agent | Concrete stock | Battlefield and Portal quantity | Covert quantity |
| --- | --- | ---: | ---: |
| Anthrax | `anthrax_bomb_1` | 200 | 400 |
| Plague | `plague_bomb_1` | 100 | 200 |
| Tularemia | `tularemia_bomb_1` | 100 | 200 |
| Smallpox | `smallpox_bomb_1` | 50 | 100 |
| Weaponized Zombies | `zombie_disease_bomb_1` | 125 | 250 |
| Engineered Black Plague | `plague_bomb_1` | 1 | 2 |

## Raid sequence and outcomes

The battlefield variant targets an enemy-held frontline or operational military state, prepares for seven days, and reserves 25 Command Power plus one agent lot.
The Portal battlefield variant reaches an enemy-held rear state when the actor has operational portals, with the same seven-day preparation and 25 Command Power plus ten `teleportation_equipment_1` items.
The covert variant targets an enemy core state containing industry or a strategic installation, prepares for fourteen days, and reserves 50 Command Power plus two agent lots.
All three use a qualifying land formation, a supply-node starting point, and the native raid instance.
The native outcome callback performs no equipment or Command Power debit and never makes a refund.

The legacy battlefield outcome weights were 70 percent delivery, 25 percent failed delivery, and 5 percent home accident.
The covert weights were 55 percent delivery, 30 percent failed delivery, and 15 percent home accident.
The raid formulas use those success and disaster bases, with native failure mapped to the home accident, limited success to failed delivery, and success or critical success to delivery.
The native engine controls the final calculation, so those bases are source-level parity rather than a claim that the engine's final probabilities are identical under every raid circumstance.

Successful ordinary pathogens call `bio_lifecycle_dispatch_seed` with actor, victim, route, payload amount, and deliberate-use proof.
That dispatcher owns disease progression, attribution, condemnation, and confirmed-use history.
The Event 016 callback sets `bio_native_raid_dispatch_in_progress` only during a deliberate lifecycle dispatch so the shared lifecycle does not apply an extra Command Power recovery to an engine-paid raid.
Weaponized Zombies uses its outbreak creator and deliberate strike consequences.
Engineered Black Plague uses the ordinary plague seed plus `black_plague_apply_weaponized_exposure_runtime`, preserving its stronger exposure and accepted Event 020 provenance.
A home accident releases the chosen agent near the actor's capital and records the accident and exposure.
A failed delivery consumes the reserved cargo and records the failed attempt.
Each settled raid records the last agent, route, attempt count, and relevant Portal history once.

The raid outcome starts in `RAID_INSTANCE` scope, while the inherited disease, Zombie, and Black Plague effects require the actor country as `ROOT`.
Each of the seventy-two native result callbacks therefore saves its exact actor, selected state, and victim as chain-local event targets and fires one hidden immediate country event for that agent, method, and result.
The hidden event reconstructs temporary inputs from its own ID, validates the live actor and original hostile state, and dispatches the consequence with actor-country `ROOT`.
The event targets are private to the effect chain, so concurrent raids never share a pending country or global variable slot; a missing or invalid target leaves the paid raid in its native history without a second debit or a scripted refund.

The native `cancel_trigger` aborts preparation if the target, war, release authority, or actor validity disappears.
There is no scripted refund or second debit; the engine owns the reservation and cancellation accounting.
The former Event 016 decision receipt, capitulation refund, annexation seizure, selected-agent variable, production decisions, and staging readiness are retired.
Ordinary military production replaces the former Event 016 thirty-day and sixty-day payload decisions, which had spent 80 or 240 Support Equipment, 250 or 750 manpower, and two or four civilian factories.

## Presentation and files

The eighteen raid IDs live in `common/raids/016_brilliant_scientist_biological_raids.txt`.
Their hidden country-scope outcome bridges live in `events/016_brilliant_scientist_biological_raid_events.txt`.
Their agent names and methods are localized in `localisation/english/016_brilliant_scientist_biological_raids_l_english.yml`.
The actor and exact-state predicates live in `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt`, and the guarded outcome dispatcher lives in `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`.
The four ordinary agent map sprites and the Weaponized Zombie sprite reuse `interface/chaosx_raids.gfx` and its DDS files under `gfx/interface/military_raids/map_icons/`.
Engineered Black Plague uses `GFX_raid_type_icon_brilliant_scientist_black_plague` in `interface/016_brilliant_scientist_biological_raids.gfx`, currently wired to the existing Event 020 weapon-delivery image at `gfx/interface/decisions/020_black_plague/decision_weapon_delivery.dds`.
Equipment icons reuse the five definitions in `interface/chaosx_equipment.gfx`.
No new category artwork or scripted GUI is required.

## Validation limit and future plans

The native land path solver's behavior for a distant or disconnected Portal rear target remains an engine evidence gap; source inspection proves the target predicate and ten-equipment reservation but cannot prove every engine path.
A future distinct Black Plague raid-map DDS may replace the reused Event 020 image without changing the sprite key.
Further agent variants should provide one named raid and its equipment, unlock, AI, lifecycle, localisation, and CXT proof without creating a second attack transaction.
