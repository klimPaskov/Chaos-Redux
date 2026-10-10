# Consultation Decision Matrix

[Part 3](../specs/030_time_traveler_spec_part_3_consultations_and_intelligence_war.md) owns the consultation rules.
Exact costs are tuning anchors and scale from country capacity.

| Family | Target selection | Example costs | Objective | Strong success | Failure consequence |
| --- | --- | --- | --- | --- | --- |
| Military forecast | current enemy, border, capital approach, supply route, sea or air region | army XP, command power, support equipment, fuel | hold, deploy, supply, protect, or delay in named places | planning window, Event 027 doctrine result, exposed enemy weakness | credibility loss, missed opportunity, forged-advice investigation |
| Industrial bottleneck | rail, port, hub, factory state, resource route, stockpile | civilian factory burden, trains, trucks, convoys, fuel | repair, construct, shift production, or maintain stockpile | map improvement, efficiency retention, spirit upgrade | shortage, sabotage exposure, delayed production |
| Scientific shortcut | active research family, valid project, secure research state | research opportunity, XP, support equipment, civilian capacity | pursue one viable method and secure requirements | research bonus, project progress, custom tech API result | wasted capacity, unsafe prototype, divergence warning |
| Diplomatic forecast | ally, rival, vulnerable neutral, faction member, or a remembered war variant | political power, convoys, civilian capacity, intelligence exposure | reach relation, secure agreement, expose rival offer, avert the remembered war | actual agreement, recognition, corridor, or faction resilience | betrayal, opinion loss, foreign fragment gain |
| Counterintelligence map | interested country, staff network, records site | command power, agency capacity, support equipment, time | identify, protect, or turn one network | expose attacker, lower Exposure, cheaper next sting | note theft, forged advice, staff compromise |
| Domestic threat assessment | real faction, region, official, or instability source | political power, command power, unit commitment, stability risk | lawful inquiry, security operation, political settlement, or named-state defense | plot prevented, government stabilized, route unlocked | radicalization, coup momentum, condemnation, public scandal |

## Cooldown and concurrency

- one active consultation mission
- default shared cooldown near 90 days
- profile specialty shortens its matching family
- Indispensable Credibility unlocks the advanced variant
- the Divergence band sets forecast precision
- the arrangement limits which families appear
- active war and national emergencies may shorten one relevant family but do not remove cost
