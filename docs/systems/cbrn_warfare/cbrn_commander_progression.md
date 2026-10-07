# CBRN commander progression

CBRN commander traits record service by a named officer during completed Headquarters orders or protected field command.
The Chemical Operations Commander, Biological Operations Veteran, and Hazard Warfare Veteran occupy appended earned-trait rows; Protected Assault Expert is an assignable general trait, and Theatre Containment Organizer is an assignable field marshal trait.
The additions leave vanilla rows unchanged.

After the final successful paid upkeep tick of a bounded CBRN Headquarters order, the exact commander receives one service receipt.
Decontamination Corridor counts as chemical service; Mass Antidote Response and Seal Infection Corridor count as biological service; Decontamination Corridor, Seal Operational Area, and Seal Infection Corridor count as containment service.
Two chemical receipts earn Chemical Operations Commander, two biological receipts earn Biological Operations Veteran, and a commander with both earns Hazard Warfare Veteran.
Preparations, canceled orders, and failed upkeep do not count.
One completed order is credited at most once, and later completed orders can count after the next valid commitment clears the receipt guard.

The [HQ helper-output contract](cbrn_hq_command.md#temporary-output-contract) preserves actual package and preparation values through payment and scheduling.
Its source regression exercises final paid and failed upkeep, one-time receipts and planned cleanup; it does not prove native event timing or raid-to-commander attribution.

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
Citation: installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md`, the outcome-effect block at lines 246-281 and the raid-instance variable list at lines 549-556, which names exactly `var:actor_country`, `var:victim_country`, `var:target_state` and `var:target_province`; `division_effects` is documented only with a divisional-experience example and no unit-leader scope.
Character scope is available to raid success-chance modifiers, but that read-only selection formula does not expose a persistent participating leader to an outcome callback.
Native raids therefore do not award personal commander service from an arbitrary country roster.

The progression definitions are `common/unit_leader/chaosx_traits.txt`, `common/scripted_effects/cbrn_commander_progression_effects.txt`, `common/scripted_triggers/cbrn_commander_progression_triggers.txt`, `common/on_actions/cbrn_commander_progression_on_actions.txt`, and `common/script_constants/cbrn_commander_progression_constants.txt`.
The exact Headquarters completion caller lives in `events/cbrn_hq_events.txt`.

## Icons

The four new trait DDS files belong at `gfx/interface/traits/cbrn/trait_biological_operations_veteran.dds`, `trait_hazard_warfare_veteran.dds`, `trait_protected_assault_expert.dds`, and `trait_theatre_containment_organizer.dds`.
`interface/chaosx_traits.gfx` registers `GFX_trait_biological_operations_veteran`, `GFX_trait_hazard_warfare_veteran`, `GFX_trait_protected_assault_expert`, and `GFX_trait_theatre_containment_organizer`.
Chemical Operations Commander continues to use `GFX_trait_chemical_operations_commander`.

## What the player is told

Because no raid names a commander and no headquarters is bound to a raid, the earned-trait and achievement text states only what the source actually measures.

Chemical Operations Commander and Biological Operations Veteran are credited when the named general has seen the qualifying order through to its final paid day while commanding an army; preparations, cancelled orders, and orders that finish under a different commander are excluded, and the tooltips say so. The earlier wording also named a "Combined CBRN Overmatch" headquarters order, which is not one of the five operation codes in `common/script_constants/cbrn_hq_constants.txt`; that phrase is gone.

Protected Assault Expert names the Gas Mask and Decontamination Detachment that `cbrn_commander_commands_protected_formation` actually checks. Theatre Containment Organizer names the three containment orders that `cbrn_commander_record_completed_hq_operation` counts.

The Prepared Army achievement text now separates its country-level conditions from the three per-commander headquarters commitments and states plainly that no single headquarters is credited with a raid. The raid condition is a confirmed chemical land raid carried out while at least one of the country's armies has an Operations Section in the field, which is what `cbrn_country_has_deployed_chemical_hq_section` tests.

## Future plans

If a future raid API exposes the participating leader or a verified raid-to-HQ command link, completed ground raids can credit that precise officer through a separate service receipt.
