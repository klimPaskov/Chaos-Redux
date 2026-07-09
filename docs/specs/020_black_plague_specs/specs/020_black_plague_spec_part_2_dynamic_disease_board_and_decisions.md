# 020 Black Plague spec Part 2 - Dynamic disease board and decisions

## Shared disease category rule

Black Plague must use the shared biological warfare and disease-containment decision ecosystem. It should not create a duplicate Black Plague decision category that copies prevention buttons. The shared category should become a dynamic crisis board that changes depending on each country’s exposure.

The player should see one disease system that can handle Black Death, ordinary outbreaks, weaponized diseases, accident outbreaks, and future disease events. The Black Death can add unique state conditions, response modifiers, cure tracks, and special project hooks, but the main player surface remains shared.

## Disease board layout

The shared board should have these player-facing regions:

| Board region | Purpose |
| --- | --- |
| Current disease summary | Shows active diseases affecting the country and the most dangerous state. |
| State list | Shows infected, threatened, contained, recovering, cured, weaponized, and rat-held states. |
| Response lane | Shows decisions available for the selected disease status. |
| Cure lane | Shows treatment, countermeasure, and research progress. |
| Border and port lane | Shows outside exposure and cross-border controls. |
| Military containment lane | Shows army cordons, supply strain, and state defense tasks. |
| Biowarfare lane | Shows research and weaponization only for eligible countries. |
| Recovery lane | Shows cleanup, reopening, infrastructure repair, and population recovery support. |

The board can be a decision category with scripted localisation and targeted decisions. If the existing UI supports a richer scripted GUI, the board should open or attach to it. Static text is acceptable for the first implementation only if it remains readable and dynamic. The next implementation pass should evaluate a scripted GUI because this event has many state statuses and living values.

## Dynamic visibility by state status

The same category should expose different decisions depending on the current state.

| State status | Visible decision families |
| --- | --- |
| Clean | Surveillance, stockpiles, medical drills, and port hygiene. |
| Prepared | Maintain readiness, expand labs, train field hospitals, and reserve supplies. |
| Threatened | Border checks, port inspections, troop-route restrictions, refugee screening, and local medical buildup. |
| Infected | Quarantine, lockdown, field hospitals, army cordon, treatment push, corpse handling, vector control, and local cleanup. |
| Contained | Maintain cordon, controlled reopening, local aid, relapse monitoring, and supply restoration. |
| Recovering | Final cleanup, hospital drawdown, local recovery grants, and population recovery support. |
| Cured | Preparedness maintenance, memorial or recovery choice, and return to normal administration. |
| Weaponized | Emergency containment, evidence control, condemnation response, retaliation preparation, and sample security. |
| Rat-held | Military border seal, burn out warrens, evacuation, fortify nearby states, and anti-rat offensive preparation. |

The category should hide obsolete decisions. It should not show all possible responses at once.

## Prevention decisions

Prevention should matter before infection arrives. A country that prepares early should reduce spread and deaths. The opportunity cost should be real.

Prevention families:

| Family | Cost direction | Effect direction |
| --- | --- | --- |
| Disease surveillance | Political attention, small civilian burden, medical supply | Detects threatened states earlier and lowers surprise spread. |
| Medical stockpiles | civilian industry, support equipment, trucks, possibly convoys | Improves emergency treatment and reduces early deaths. |
| Port hygiene | convoys, trade friction, dockyard or civilian burden | Reduces port jumps and overseas spread after Evolution II. |
| Border health checks | stability, relations, trade, supply throughput | Reduces cross-border spread from threatened neighbors. |
| Field hospital reserve | support equipment, manpower, trucks | Raises medical capacity for infected states. |
| Public health law | stability or political cost, consumer goods burden | Creates lasting disease protection and underreaction resistance. |
| Railway sanitation | trains, infrastructure burden, supply throughput | Reduces troop-route and refugee-route spread. |

Prevention should have diminishing returns. A small country can prepare deeply, but a large empire should need to choose which regions and ports matter most.

## Threatened-state decisions

Threatened states are where the crisis becomes strategic. They are not infected yet, so harsh measures are optional.

Decision families:

- Border inspection posts in specific border states.
- Port screening in specific port states.
- Troop route restrictions through exposed states.
- Refugee screening and camp sanitation.
- Local medical buildup.
- Temporary school, market, and rail restrictions where the state has urban population.
- Early vector control with care, because bad rodent policy can increase flea-host movement.

Threatened-state decisions should reduce spread chance and increase preparedness. They should also damage local economy, supply, relations, or stability when severe.

## Infected-state decisions

Infected states need hard choices. Every useful response should have a cost.

| Decision family | Strong effect | Cost or risk |
| --- | --- | --- |
| Emergency quarantine | Strongly lowers spread from the state | Stability loss, compliance damage, resistance risk, supply damage. |
| Full lockdown | Lowers deaths and spread more than quarantine | Heavy consumer goods, local industry loss, war support damage. |
| Army cordon | Lowers movement spread and refugee spread | Ties down manpower and equipment, hurts fronts, risks attrition. |
| Field hospitals | Reduces deaths and supports cure progress | Support equipment, trucks, manpower, civilian industry. |
| Treatment surge | Reduces death pressure and cure time | Medical supply cost, political attention, limited repeat use. |
| Controlled burials | Reduces panic and local disease load | Manpower, stability pressure, religious or local unrest risk in some countries. |
| Vector control | Lowers rodent pressure | Requires timing and may backfire if done badly. |
| Local cleanup crews | Moves infected to contained or recovering | Equipment, manpower, safety risk, low success if disease load is still high. |

The strongest containment should be expensive enough that a country at war may hesitate. The weak response should be cheaper but visibly risky.

## Contained and recovery decisions

Contained states should still demand attention. The cure should not erase the problem instantly.

Contained-state decisions:

- Maintain containment.
- Reopen slowly.
- Continue treatment.
- Rotate army cordon units.
- Inspect rail and port traffic.
- Hunt remaining rodent reservoirs.
- Monitor relapse risk.

Recovery decisions:

- Remove remaining disease load.
- Rebuild local infrastructure and supply.
- Restore workforce and manpower recovery.
- Fund survivors and orphan care through a stability and civilian burden tradeoff.
- Lift restrictions too early for faster economy and higher relapse chance.

## Underreaction and overreaction

The player should be able to choose a bad response on purpose.

Underreaction traits:

- Lower immediate economic loss.
- Lower political cost.
- Higher disease load growth.
- Higher death pressure.
- Higher spread pressure.
- Higher chance of later panic, riots, military cordon failure, and rat warren pressure.

Overreaction traits:

- Lower disease load growth.
- Lower spread and deaths.
- Higher stability damage.
- Higher war support damage.
- Higher resistance and compliance damage in occupied states.
- Higher relations damage from border closure.
- Higher supply and trade disruption.

The best play should depend on war, geography, population, and state value. Overreaction in a low-population frontier may be wasteful. Underreaction in a crowded industrial state should be dangerous.

## Mapmode and black fog presentation

The existing disease mapmode must update every time a state becomes infected, threatened, contained, cured, weaponized, rat-held, or cleared. The player should never need to read hidden variables to know where the disease is active.

Mapmode color and marker direction:

| Status | Visual direction |
| --- | --- |
| Clean | Normal mapmode neutral. |
| Prepared | Subtle cool outline or shield marker. |
| Threatened | Yellow or sickly border glow. |
| Infected | Dark red, black-red, or deep sickly highlight. |
| Contained | Dark red with containment ring or cordon mark. |
| Recovering | Faded sickly tone with recovery marker. |
| Cured | Temporary pale recovery marker, then clears. |
| Weaponized | Harsh warning mark with stronger black overlay. |
| Rat-held | Black fog with rat insignia or warren marker. |

The user requested black fog for sick states if possible. The visual plan should try to create a fog-like state overlay through the strongest supported project pattern. If the engine cannot support true fog on state map surfaces, implementation must report that limitation and provide the closest approved visual path only after review. Silent fallback is not allowed.

Potential visual layers:

- disease mapmode tint for infected states
- state modifier icon and tooltip
- animated black fog or smoke marker for the selected state panel or disease board
- fog-like UI overlay in the disease board when an infected state is selected
- rat-held state marker after Evolution III

## UI animation planning

This event benefits from animated presentation because the state board is a living crisis. The asset prompt should request animation planning for:

| Animated asset | State logic | Target surface |
| --- | --- | --- |
| Black fog disease status | Active when selected state is infected or weaponized | disease board or state detail overlay |
| Critical infection pulse | Active when death pressure crosses a high threshold | disease board warning frame |
| Containment ring pulse | Active when contained state is near relapse | disease board state card |
| Rat warren marker | Active when rat warren pressure is high or rat-held | map marker or disease board card |
| King of Rats portrait aura | Active after Evolution IV | leader portrait or event-owned GUI card |

Animations must use real source frames, frame sheets, static fallbacks, and manifest entries. They must not be final GIFs or transform-only local effects.

## Decision text direction

Decision names and descriptions should describe the public action. They should not reveal hidden future rat outcomes. Black Plague decisions can mention infected streets, closed roads, port checks, field hospitals, missing workers, military cordons, and treatment shortages. They should not spoil the King of Rats route before it appears.
