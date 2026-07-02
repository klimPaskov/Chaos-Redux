# Event 17 AI matrix

## AI selection priorities

| Actor | Ordinary priority | High chaos priority | Avoid |
| --- | --- | --- | --- |
| selected neutral minor | choose faction by ideology, proximity, threat, relations, and military strength | accept riskier faction choices if neutrality resilience is low | direct enemy factions and dead leaders |
| selected wartime minor | join faction fighting its enemies or protecting its front | join stronger patron even with heavy war danger | factions that cannot reach it or are losing nearby fronts unless desperate |
| pressured neutral neighbor | resist if stable, copy if ideologically close, counter-align if encircled | counter-align or accept public commitment more often | endless neutrality declarations without cost |
| faction leader at peace | use staff missions and propaganda in nearby or ideological regions | demand commitments if rivals are gaining ground | spending scarce equipment on unreachable targets |
| faction leader at war | pressure border countries and corridor states | pressure aggressively when a new front helps | inviting countries that open useless fronts or supply traps |
| democratic AI | prefer neutrality council, guarantees, and defensive commitments | accept faction pressure if threatened or encircled | aggressive demand decisions without threat |
| fascist AI | favor ideological alignments, demands, and military pressure | use commitments and border missions aggressively | supporting ideological enemies unless strategic fear is high |
| communist AI | favor ideological alignments, party networks, and staff missions | pressure worker-friendly or unstable neighbors | overinvesting in distant regions with no faction presence |
| neutral AI | resist pressure if stable and safe | seek protection if surrounded or weak | joining faraway factions with no plausible protection |

## Option scoring inputs

| Input | Baseline | Evolution I | Evolution II | Evolution III |
| --- | ---: | ---: | ---: | ---: |
| ideology match | high | high | high | medium high |
| faction proximity | high | very high | very high | very high |
| common enemy | medium | medium | high | high |
| faction military strength | medium | medium | high | high |
| active war assistance | low | medium | very high | very high |
| neutrality resilience | reduces all pressure | strong reducer | medium reducer | weak but still relevant |
| recent same-region alignment | low | high | high | very high |
| rival encirclement fear | low | high | high | very high |
| relation with faction leader | medium | medium | medium | medium |

## AI route notes

AI must revalidate every target before acting. If a saved faction option becomes invalid, the AI should reroll from remaining valid options. If no options remain, the event should cancel cleanly.

AI should not be forced into all extreme choices by chaos alone. High chaos makes risky diplomacy more likely, but ideology, threat, war state, and geography remain meaningful.
