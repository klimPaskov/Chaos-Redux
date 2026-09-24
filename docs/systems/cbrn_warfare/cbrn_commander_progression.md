# CBRN commander progression

CBRN commander traits record service by a named officer during completed Headquarters orders or protected field command.
The Chemical Operations Commander, Biological Operations Veteran, and Hazard Warfare Veteran occupy appended earned-trait rows; Protected Assault Expert is an assignable general trait, and Theatre Containment Organizer is an assignable field marshal trait.
The additions leave vanilla rows unchanged.

After the final successful paid upkeep tick of a bounded CBRN Headquarters order, the exact commander receives one service receipt.
Decontamination Corridor counts as chemical service; Mass Antidote Response and Seal Infection Corridor count as biological service; Decontamination Corridor, Seal Operational Area, and Seal Infection Corridor count as containment service.
Two chemical receipts earn Chemical Operations Commander, two biological receipts earn Biological Operations Veteran, and a commander with both earns Hazard Warfare Veteran.
Preparations, canceled orders, and failed upkeep do not count.
One completed order is credited at most once, and later completed orders can count after the next valid commitment clears the receipt guard.

Two won combats while the general commands a fielded protected CBRN detachment satisfy Protected Assault Expert's service prerequisite; the player still assigns that general trait through the native trait menu.
Two completed containment orders plus Hazard Warfare Veteran satisfy Theatre Containment Organizer's field marshal trait prerequisite.
The battle callback proves that the named commander won combat and had a protected detachment under command; it does not identify which division participated in that battle.
Protected Assault Expert reduces the commanded army's out-of-supply penalty by five percent; Theatre Containment Organizer adds one army-group command slot.

The native Chemical Operations Commander trait also offers a native High Command officer role with specialist, expert, and genius ranks.
Its planning-speed values are one, three, and four percent, respectively; the former generic CBRN Operations Director office is retired.
Civil Defence Coordinator, Chemical Logistics Inspector, and Biological Security Director remain distinct institutional High Command options.
The native officer role uses that commander's existing portrait.

Native raid outcomes expose `actor_effects` and `victim_effects` in raid-instance scope and `division_effects` in the participating division's scope.
The installed raid documentation exposes only actor country, victim country, target state, and target province as raid-instance pointers, and documents no division-to-army-leader scope switch for outcome effects.
Character scope is available to raid success-chance modifiers, but that read-only selection formula does not expose a persistent participating leader to an outcome callback.
Native raids therefore do not award personal commander service from an arbitrary country roster.

The progression definitions are `common/unit_leader/chaosx_traits.txt`, `common/scripted_effects/cbrn_commander_progression_effects.txt`, `common/scripted_triggers/cbrn_commander_progression_triggers.txt`, `common/on_actions/cbrn_commander_progression_on_actions.txt`, and `common/script_constants/cbrn_commander_progression_constants.txt`.
The exact Headquarters completion caller lives in `events/cbrn_hq_events.txt`.

## Icons

The four new trait DDS files belong at `gfx/interface/traits/cbrn/trait_biological_operations_veteran.dds`, `trait_hazard_warfare_veteran.dds`, `trait_protected_assault_expert.dds`, and `trait_theatre_containment_organizer.dds`.
`interface/chaosx_traits.gfx` registers `GFX_trait_biological_operations_veteran`, `GFX_trait_hazard_warfare_veteran`, `GFX_trait_protected_assault_expert`, and `GFX_trait_theatre_containment_organizer`.
Chemical Operations Commander continues to use `GFX_trait_chemical_operations_commander`.

## Future plans

If a future raid API exposes the participating leader or a verified raid-to-HQ command link, completed ground raids can credit that precise officer through a separate service receipt.
