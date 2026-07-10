# Biological Agent and Countermeasure Matrix

## Agent profiles

Ratings use 1 to 5.

| Agent | Local lethality | Spread | Incubation | Persistence | Military disruption | Treatment sensitivity | Vaccination value | Attribution difficulty |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Anthrax | 5 | 1 | 2 | 5 | 3 | 4 with antibiotics | 2 | 3 |
| Plague | 4 | 5 | 2 | 3 | 4 | 4 with antibiotics | 2 | 4 |
| Tularemia | 2 | 3 | 2 | 3 | 5 | 4 with antibiotics | 2 | 4 |
| Smallpox | 4 | 5 | 4 | 4 | 4 | 2 | 5 | 3 |
| Zombie pathogen | special | special | special | special | special | separate cure system | separate | separate |

## Delivery matrix

| Delivery | Anthrax | Plague | Tularemia | Smallpox | Preparation | Attribution risk | Friendly spread risk |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| strategic air raid | strong | strong | strong | strong late | 21 to 45 days | high | medium |
| operative outbreak | strong | strong | moderate | strong | 90 to 240 days | low to extreme on capture | medium to high |
| battlefield dissemination | moderate | weak | strong | limited | 14 to 30 days | high | high |
| food or water sabotage | moderate | strong | moderate | moderate | 120 to 300 days | low initially | medium |
| stockpile accident | strong local | strong spread | moderate | strong spread | none | public if severe | domestic high |
| doomsday release | catastrophic | catastrophic | severe | catastrophic | route gated | confirmed | maximum |

## Outbreak modifiers

| Factor | Intensity growth | Spread | Deaths | Detection |
| --- | ---: | ---: | ---: | ---: |
| surveillance 80+ | -25% | -15% | -10% | +50% speed |
| containment 80+ | -20% | -50% | -15% | +20% |
| medical capacity 80+ | -10% | -10% | -50% | +20% |
| war-damaged state | +20% | +25% | +25% | -20% |
| dense urban state | +20% | +30% | +10% | +10% |
| active quarantine | -15% | -50% | +5% short-term hardship unless supplied | +10% |
| border closure | no local change | -30% cross-border | no direct change | no direct change |
| high chaos | +5 to 25% | +5 to 25% | no automatic bonus | -5 to 15% |
| repeated deliberate seed | +10 to 30% | +10 to 20% | +10% | evidence +25% |

## Countermeasure matrix

| Countermeasure | Anthrax | Plague | Tularemia | Smallpox | Equipment or capacity | Tradeoff |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| surveillance network | high detection | high | high | high | instruments, medical administration | cost and false alarms |
| field hospitals | medium death reduction | medium | high military recovery | medium | support eq, trucks, medical | supply burden |
| antibiotics | high | high | high | low | medical stores and industry | diminishing emergency efficiency |
| vaccination | medium if prepared | low | low | very high | vaccine capacity, time | slow distribution |
| quarantine | medium | very high | medium | very high | manpower, equipment, local control | output and resistance penalty |
| border closure | low local, good external | high external | medium | high external | political and trade cost | supply and diplomacy |
| decontamination | very high site cleanup | medium | medium | low to medium | decon equipment | industrial and fuel burden |
| international aid | high if accepted | high | high | high | diplomacy and access | evidence transparency |

## Stockpile risk

| Risk band | Conditions | Monthly or event-driven accident expectation | Player response |
| --- | --- | --- | --- |
| Controlled | safety 70+, stock below program threshold | negligible ordinary risk | maintain program |
| Strained | safety 40 to 69 or high stock | rare contained incident | invest in containment |
| Dangerous | safety 20 to 39 and large stock | meaningful local accident risk | reduce stock or upgrade facility |
| Critical | safety below 20, war damage, sabotage, extreme stock | major outbreak possible | emergency disposal or relocation |

Exact chance uses event-driven checks after production milestones, bombing, sabotage, facility damage, or stockpile threshold crossing. Avoid an all-country daily roll.

## Biological death bands

| Agent | Low-intensity weekly exposed death | Serious | Catastrophic | Maximum episode cap |
| --- | ---: | ---: | ---: | ---: |
| Anthrax | 0.0005% | 0.004% | 0.015% | 1.5% state population |
| Plague | 0.0003% | 0.006% | 0.025% | 5% |
| Tularemia | 0.00005% | 0.0008% | 0.004% | 1% |
| Smallpox | 0.0002% | 0.005% | 0.020% | 8% |

The model applies these rates to an exposed share, not automatically to the whole state.

## Condemnation anchors

| Action | Base gain when confirmed | Additional pressure |
| --- | ---: | --- |
| covert failed seed with no outbreak | 5 to 15 | captured operative or samples |
| local deliberate outbreak | 15 to 40 | deaths and non-core target |
| strategic raid | 30 to 70 | target population and spread |
| repeated cross-border spread | +10 to 30 | repeat-use and coverup |
| experiment-site discovery | atrocity bucket 20 to 80 | deaths, evidence, coverup |
| doomsday release | 200 to 500 | immediate pariah and world-threat evaluation |
