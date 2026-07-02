# Event 17 decision and mission map

| Working id | Holder | Type | Available when | Costs and requirements | Success or result direction | Failure or risk direction | AI use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `random_faction_stabilize_alignment` | selected minor | clickable decision | joined through Event 17 and alignment shock active | political power, stability strain, support equipment scaled by size | shortens shock and improves faction relations | can increase polarization if country is unstable | high if safe |
| `random_faction_request_liaison` | selected minor | targetable decision | faction leader valid and liaison not active | army XP or command power, paired leader support cost | temporary coordination and faction influence | dependency pressure rises | medium |
| `random_faction_quiet_opposition` | selected minor | risky decision | opposition pressure active | stability, political power, possible war support | reduces shock quickly | backlash event chance | cautious |
| `random_faction_convene_neutrality_council` | pressured neutral | clickable decision | under pressure and not in faction | political power, stability, command consultation | raises neutrality resilience | delays action only, does not remove all pressure | high for stable neutral AI |
| `random_faction_reinforce_border_posts` | pressured neutral | timed mission | borders faction member or rival region | supplied divisions in named states, infantry equipment reserve | raises resilience and lowers selection weight | lowers resilience and raises future pressure | high if threatened |
| `random_faction_invite_observers` | pressured neutral | targetable decision | faction leader valid and observer path available | relations, political power, support equipment or convoy access | increases one faction pull | rival reaction risk | ideology and threat dependent |
| `random_faction_publish_neutrality` | pressured neutral | cooldown decision | pressure active and resilience not broken | political power, stability or war support cost | temporary all-faction resistance | another nearby neutral may become target | high for democracies |
| `random_faction_offer_staff_mission` | faction leader | targetable decision | target pressured or newly aligned | support equipment, command power, trucks or convoys | increases pull and stabilizes target | dependency and rival backlash | high for nearby targets |
| `random_faction_radio_networks` | faction leader | regional decision | region under bloc race | political power, civilian burden, exposure risk | increases faction pull | polarization and rival propaganda | medium |
| `random_faction_guarantee_corridor` | faction leader | targetable decision | target can be reached or has strategic value | convoys or trains, strength check | defensive credibility and pull | war danger if border enemy exists | strategic |
| `random_faction_demand_commitment` | faction leader | risky decision | Evolution II or III and target pressured | political power, command power, relation risk | triggers public commitment event | target may refuse and lean rival | aggressive AI only |

## Mission quality rules

Missions should be active objectives. Border posts require divisions in named states. Corridor guarantees require route access or supply plausibility. Neutrality resilience should be affected by actions, not passive stockpile checks.

## Clutter control

Only show decisions relevant to the current holder. Faction leaders should not see every eligible minor at once unless AI evaluation needs hidden decisions. Human-facing target management should use selector patterns if the target count is large.
