# CBRN unit and project-equipment package

The fielded CBRN roster uses three headquarters sections, a combined protection company, a combined field medical company, reconnaissance, chemical projectors, ammunition logistics, biological security assault, the Chaos battalion, and one armored-delivery role across the light, medium, and heavy flame chassis. Agent selection and exact payload reservation belong to native operations, not the standing divisional equipment bill.

The Operations and Intelligence section retains the sealing command ability, while offensive preparation and combined overmatch are native operation paths without separate paid HQ abilities or dedicated active-order traits.

## Fielded units and compatibility

| Fielded ID | Role and retained output | Inactive compatibility ID absorbed |
| --- | --- | --- |
| `cbrn_hq_operations_section` | Operations plans, weather intelligence, reconnaissance, and command orders | `cbrn_hq_intelligence_weather_cell` |
| `cbrn_hq_protective_logistics_section` | Protective issue, corridor opening, and mobile decontamination | `cbrn_hq_mobile_decontamination_column` |
| `cbrn_hq_medical_countermeasure_directorate` | Countermeasures, outbreak control, and biological security | `cbrn_hq_biological_security_section` |
| `cbrn_gas_mask_decon_detachment` | Mask issue, decontamination, and later hazard-pioneer training | `cbrn_hazard_pioneer_detachment` |
| `cbrn_medical_countermeasure_detachment` | Field hospitals, epidemiology, and quarantine | `cbrn_field_epidemiology_detachment` |
| Nerve-delivery certification | Operation-only upgrade; it does not field a standing suppression company | `cbrn_nerve_suppression_detachment` (retired compatibility reference) |

The 18 agent-specific chemical tank companies and the six agent-specific Livens projector companies remain inactive definitions for compatibility. They are absent from CXT playable templates and AI formations. Existing surviving IDs remain stable so technology, counter sprites, and save-facing references have one canonical consumer.

## Research and AI formation flow

The Theater CBRN Headquarters marker unlocks the three HQ sections together. Hazard Pioneer Training is a doctrine-granted Protection Company upgrade after mask and field-decontamination research, with no visible research node. Field Epidemiology Teams unlocks the Field Medical Company at the normal 75-day support-tech band; Mobile CBRN Hospitals improves its casualty retention at the advanced 100-day band. Doctrine and project markers have no visible tree folder and no positive AI research factor. AI templates use actual standing unit bills, and chemical artillery or armored assaults require a country-level CBRN programme or war state, real strategic-agent stock, and the complete role-specific standing bill before adoption. Native operations still require an exact selected target receipt before release.

Armored delivery is exposed as three separate standing formation variants: light, medium, and heavy. Each variant checks its own generic and flame chassis stock thresholds, so the AI cannot satisfy a medium bill with light or heavy equipment. The native operation layer remains responsible for selecting and validating the payload target.

The AI formation trigger for a coercive security garrison requires an occupied, non-core state with sufficient resistance, the relevant security authorization, protection and biological-security research, and the full standing equipment bill. It does not use the retired nerve detachment or treat stock of a generic payload as proof of a selected operation.

## Static stat and production checks

The projector battery starts with soft attack 12, hard attack 4, defense 4, and breakthrough 10. Each Livens progression technology adds multiplicative sub-unit fractions of 0.025 soft attack, 0.13 hard attack, 0.05 defense, and 0.075 breakthrough. Even treating every legal doctrine, technology, and army-wide source as independently multiplicative, the package contributes at most +32.8602% soft attack, +32.8455% hard attack, +34.0096% defense, and +33.7780% breakthrough. The Chaos battalion starts at breakthrough 18 and organization 40; its 1942 upgrade adds 0.15 breakthrough and a flat 11 organization (+27.5% of base), with a strict independent-source organization upper bound of +33.3404% after the country-wide bonuses.

At representative 1939 production costs, the chemical-assault AI template needs 1,110 infantry weapons, 449 gas masks, 200 decontamination kits, 88 instruments, 310 support kits, 110 trucks, and 24 projector chassis. Using installed vanilla infantry IC 0.58, support IC 4, truck IC 2.5, and the 1936 CBRN mask IC 0.27, decontamination IC 7.5, and instrument IC 5, the bill is at least 4,220.03 IC before projector construction. A conventional nine-infantry formation needs 900 infantry weapons or 522 IC under the same infantry model, so eight such formations cost 4,176 IC. The CBRN formation carries only nine combat battalions at that near-equal cost and is a costly specialized offensive package.

The lean protected nine-infantry template costs 756.5 IC: 522 for infantry and 234.5 for its company bill of 100 masks, five decontamination kits, five instruments, 30 support kits, and ten trucks. At the same IC, a plain nine-infantry army can field 1.449 templates. The Protection Company contributes native defense 5, breakthrough 3, and supply consumption factor −0.20; Hazard Pioneer Training later adds fort attack +0.10, fort movement +0.05, and urban attack +0.05. The source does not establish that these bonuses beat 1.449 plain formations in general combat.

With the same installed 1939 infantry-equipment model on both sides, nine infantry battalions contribute approximately 81 equipment soft attack while 1.449 plain formations contribute approximately 117.4 before other division modifiers. The retired separate pioneer company had six native soft attack, but the combined Protection Company does not inherit that general attack stat: its pioneer progression is fort and urban specialization, preserving the clean-battle industry cost. This is a deliberate balance reduction of the old role, not an exposure-protection benefit.

The exposure comparison holds national military mask coverage equal between sides and uses the corrected multiplicative technology values above. Let `D` be an accepted action's unprotected organization-damage ratio (capped at 0.60) and `L` its unprotected strength-damage ratio (capped at 0.01). The dispatcher applies the same countrywide protection multipliers to every hostile division in the exact target state, regardless of its support-company composition.

| Condition | Equal-IC source result |
| --- | --- |
| Clean state | No exposure damage applies; one protected template retains its native support and terrain bonuses, with the corrected Livens and Chaos Battalion percentages bounded by the accepted +35% dedicated-stat cap, while the plain force fields 1.449 templates. |
| Unprotected exposure | With protection 0, both templates take `D` organization and `L` strength damage; the corrected unit technologies do not create a separate exposure reduction for the Protection Company. |
| Protected exposure | With full improved-mask coverage and no other layers, the respiratory score reaches 75, choking casualty multiplier is 0.25, and disruption multiplier is 0.4375. Both templates therefore take `0.4375D` organization and `0.25L` strength damage under the same country coverage; corrected unit-tech percentages change native stats only. |
| Equipment shortage | If this protected template has only 50 of its 100 improved masks and no other army or issued masks, its 9,320 manpower requires 93.2 mask crates; coverage becomes 53.65 and the respiratory score is capped there. Choking casualties use the 0.45 medium-band multiplier and disruption uses about 0.598, again shared by every division of that country. Missing essential equipment also weakens the company's native stats, while the AI formation gate refuses a new understocked template and a native chemical raid without its exact required payload cannot launch. |

The Company places real masks into the national deployed-equipment count, but the same masks can be issued through the national protection program. The current source therefore does not prove a distinct per-division exposure advantage at equal national coverage. The four conditions are source-based ratios, not a combat simulation; they omit division-stat aggregation, terrain, frontage, combat tactics, reinforcement, and equipment replacement. A future unit-specific mitigation requires a verified engine consumer that can target any equipped Protection Company division, not only an exact named template.

## Native vehicle and module consumers

Completing the vanilla flamethrower-tank project, Collective Protection Systems, and Sealed Tank Crews grants the hidden `cbrn_sealed_flamethrower_crew_integration` technology. It unlocks `cbrn_sealed_flamethrower_crew_module` in the vanilla flame chassis `tank_special_module` slots. The module adds defense and reliability at an IC and rubber cost, and requires tank-design XP.

Completing the vanilla military-engineering-vehicles project, Collective Protection Systems, and Mobile Wash Columns grants the hidden `cbrn_armored_engineer_decontamination_integration` technology. It unlocks the producible `cbrn_armored_support_vehicle_decontamination` model of the installed `armored_support_vehicle` archetype consumed by `armored_engineer`. Compared with the vanilla vehicle, the model costs more IC and rubber and has lower mechanical reliability; its protected wash gear adds a small defense benefit. CXT registers the concrete model through its package-owned hidden-idea carrier and stocks it only during player-triggered setup or refill.

## Visual assets

The surviving CBRN unit and HQ sprite IDs remain in `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`; their transparent counter DDS textures live under the existing CBRN counter path. The sealed-crew module sprite is `GFX_tank_module_cbrn_sealed_flamethrower_crew_module` in `interface/cbrn_project_equipment.gfx`, pointing to `gfx/interface/equipmentdesigner/tanks/modules/tank_module_cbrn_sealed_flamethrower_crew_module.dds`. The armored engineer model inherits the installed vanilla armored-support archetype picture.

## Future depth

The decontamination-configured vehicle could receive a distinct field recovery order or project specialization bonus after live evidence proves that the new model is built and consumed by vanilla armored engineer companies. The operation system could expose a bounded, exact-target AI receipt to narrow country-level formation adoption further if a supported AI/template target hook becomes available.
