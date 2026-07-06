# Event 014 Cannibalism decision and mission matrix

All names are working labels and not final localisation.

## Decision pacing

| Phase | Visible decisions | Hidden or queued content | Category clutter rule |
| --- | --- | --- | --- |
| Baseline first report | kitchens, unit rotation, ration convoy, hospital audit | prisoner route checks, first leak chance | show four to six decisions |
| Baseline confirmed outbreak | military police, prison freeze, rail mission, public posture | first affected state expansion, spread chance | show active region plus two response families |
| Evolution I | suppression, deprogramming, chaplain or political officer, secrecy, exploitation if allowed | cult cell events, courier routes, hidden-leader seed strength | show posture-specific decisions first |
| Evolution II | island inspection, evacuation, commune raid, port inspection, prison road audit | cannibal country formation, silent ship events | show target state or selected island first |
| Evolution III | global courier hunt, allied warnings, terror unit dismantling, world-threat response | hidden-leader unification, Wendigo fusion checks, world-end preparation | hide ordinary low-impact decisions |
| Aftermath | veteran screening, evidence handover, archive review, local cleanup | leak, survivor cell, tribunal event | close category when cleanup is complete |

## Cost palette

| Action type | Preferred costs | Avoid |
| --- | --- | --- |
| Logistics | trains, convoys, fuel, support equipment, civilian factory burden, state supply | political power only |
| Military justice | command power, infantry equipment, army XP, stability, war support, unit presence | repeated command power only |
| Medical and audit | support equipment, army XP, medical tech, supplied target state | passive stockpile checks |
| Prison and POW controls | infantry equipment, command power, trains or convoys, diplomatic cost with allies | free decisions |
| Island response | convoys, fuel, naval access, air access, port control, time | flat global cost |
| Exploitation | stability, war support, condemnation, cult pressure, hidden-leader resonance, future defection or unification backlash | safe bonuses |
| Cannibal country reinforcement | population loss, hunting-ground deaths, captured equipment, raid success | free manpower timers |

## Mission table

| Mission | Owner | Requirement | Duration | Success | Failure | AI use |
| --- | --- | --- | --- | --- | --- | --- |
| Guard the ration rail | outbreak country | hold named rail route and supplied divisions | 100 to 140 days | lowers hunger and opens safer logistics | state disappearances | AI uses if target state is home or front-critical |
| Audit field hospitals | outbreak country | support equipment, supplied state, active hospital risk | 90 to 120 days | reveals or removes cell | public fear and cult pressure | AI uses if stability is moderate or high |
| Seal prison kitchens | outbreak country | control target state, equipment, command power | 90 to 130 days | lowers spread | riot or courier escape | AI uses if spread pressure is high |
| Inspect silent island | owner or overlord | naval access, convoy, fuel | 120 to 180 days | reveals or clears island | missing ships and Evolution II pressure | naval-capable AI uses if island has port |
| Evacuate garrison | owner or ally | convoy or rail route, manpower, control | 90 to 160 days | clears state risk | exposure at evacuation port | AI uses if losing state or low supply |
| Break ritual cell | outbreak country | divisions in state, equipment, command power | 90 to 130 days | lowers cult and raises containment | organized cell | AI uses if cult pressure is revealed |
| Retake commune | owner or neighbor | nearby port or state control, units committed | 120 to 180 days | blocks country formation | cannibal country spawns | AI uses if strength ratio is favorable |
| Stop mainland copying | exposed country | inspect ports, hospitals, prison transfers | 120 to 180 days | delays Evolution III | mainland state modifier | AI uses if public fear is high |
| Dismantle terror units | exploit country | remove or convert units, stability cost | 90 to 150 days | lowers hidden-leader resonance | units defect | AI uses only if not on exploitation path |

## Exploit prevention

- every repeatable decision needs cooldown or target-state limit
- no manpower gain without population loss, death log, or state damage
- no terror unit can be duplicated by switching postures
- cannibal country reinforcement cannot fire if state population is already exhausted
- defeated countries clear active decisions and missions
- target flags and event targets must be cleaned when state owner changes
- AI should never take exploit decisions only because they are available

## Strength floor

Decision effects that help cannibal countries, hidden-leader unification, or the Wendigo fusion branch should be strong enough to matter. Do not implement these branches as small modifier buttons. Use major state conversion, unit unlocks, absorbed armies, strong raiding tools, severe enemy attrition, meaningful combat shifts, and terminal fusion effects where the spec calls for them.
