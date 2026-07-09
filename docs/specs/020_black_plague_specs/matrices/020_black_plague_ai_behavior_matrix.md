# 020 Black Plague AI behavior matrix

| Actor group | Main priorities | Avoids | High-chaos changes | Required implementation notes |
| --- | --- | --- | --- | --- |
| Owner of first infected state | Contain if stable, underreact if at desperate war, seek cure if capacity exists. | Wasteful full lockdown in tiny low-risk states. | More likely to choose harsh measures or weaponize if radical. | AI weights must account for population, war, stability, industry, infected count, and cure progress. |
| Neighboring country | Prepare borders, inspect ports, aid or close borders depending on relations. | Ignoring infected borders with high population. | Can take severe border measures and form response blocs. | Needs decisions that appear before infection arrives. |
| Major powers | Send aid, fund research, exploit rival infections, condemn weaponizers. | Humanitarian aid to sworn enemies unless strategic logic supports it. | May weaponize if extremist or already using biowarfare. | Tie to ideology, condemnation, existing biowarfare tech, and faction goals. |
| Biowarfare-capable countries | Study samples, improve countermeasures, consider weaponization. | Weaponization without containment safety unless radical or desperate. | Rush projects and accept accident risk. | Must use special-project structure, not one-off decisions. |
| Countries with ports | Inspect ports and restrict travel when exposed. | Closing all ports when exposure is low and economy is fragile. | Severe port lockdowns become more likely. | Port logic matters after Evolution II. |
| Rat nations | Expand into infected or weak neighbors, grow units, absorb weaker rat nations. | Normal diplomacy, normal faction joining, waiting passively. | More aggressive and more likely to attack majors. | Register as special chaos and actual nonhuman countries. |
| King of Rats | Unite rat states, pursue continental conquest, unlock world-end path. | Normal human diplomacy and human economy routes. | Push world-end path when conditions are close. | Needs route-aware focus AI and state-control checks. |
| Coalition responders | Contain rat borders, send aid, retake plague states, prevent port jumps. | Uncoordinated single-state actions when rat threat is continental. | More likely to cooperate under world threat. | Should integrate with shared world-threat framework. |
