# Contamination, Deaths, and Condemnation Balance Matrix

## Chemical contamination

| Severity class | State value | Typical duration | Unit effects | State effects | Global Air Cleanliness event |
| --- | ---: | ---: | --- | --- | --- |
| Trace | 1 to 9 | 1 to 14 days | small recovery and mask use | no persistent major modifier | none or smallest class contribution |
| Local | 10 to 24 | 7 to 30 days | attrition, movement, recovery | small supply and output pressure | add first class contribution |
| Serious | 25 to 49 | 30 to 120 days | strong movement and org burden | construction, supply, civilian deaths | add serious class contribution |
| Severe | 50 to 74 | 90 to 240 days | high attrition and supply | medical saturation, migration pressure | add severe contribution |
| Catastrophic | 75 to 100 | 180 to 720 days | extreme without full protection | state crisis, high deaths and evidence | add catastrophic contribution |

## Chemical immediate death rates

Rates apply to exposed population.

| Use | Low | Typical | Catastrophic | Episode cap as state population |
| --- | ---: | ---: | ---: | ---: |
| choking tactical | 0.001% | 0.004% | 0.015% | 0.15% |
| choking strategic | 0.003% | 0.012% | 0.040% | 0.75% |
| blister tactical | 0.0005% | 0.003% | 0.010% | 0.20% including continuing deaths |
| blister strategic | 0.002% | 0.008% | 0.025% | 0.75% |
| nerve tactical | 0.003% | 0.015% | 0.050% | 0.30% |
| nerve strategic | 0.010% | 0.040% | 0.120% | 1.50% |
| incapacitant | 0.00005% | 0.0003% | 0.0015% | 0.05% |

## Exposed share examples

| Operation | Exposed share of state population |
| --- | ---: |
| local combat release | 0.1 to 1% |
| prepared artillery sector | 0.5 to 4% |
| persistent state fire plan | 1 to 8% |
| air operation | 2 to 12% |
| strategic raid | 5 to 20% |
| nerve suppression | 2 to 10% |
| doomsday | scenario-specific 20 to 80% |

## Protection reduction

| Effective protection | Choking multiplier | Blister | Nerve |
| ---: | ---: | ---: | ---: |
| 0 to 24 | 1.00 | 1.00 | 1.00 |
| 25 to 49 | 0.75 | 0.92 | 0.88 |
| 50 to 74 | 0.45 | 0.80 | 0.70 |
| 75 to 89 | 0.25 | 0.60 | 0.48 |
| 90 to 100 | 0.12 | 0.42 | 0.32 |
| advanced plus medical and decon | floor 0.06 | floor 0.15 | floor 0.10 |

## Base Condemnation

| Action | Base gain | Repeat-use add | Civilian death scaling | Attribution floor |
| --- | ---: | ---: | --- | --- |
| local projector combat | 2 to 5 | +1 to 3 | low | suspected if visible |
| prepared battlefield barrage | 4 to 10 | +2 to 5 | medium | probable with captured shells |
| persistent state plan | 8 to 18 | +4 to 8 | high continuing | probable |
| nerve barrage | 12 to 25 | +5 to 12 | very high | probable to confirmed |
| strategic chemical raid | 20 to 50 | +10 to 25 | extreme | confirmed on successful visible raid |
| nerve suppression | 10 to 35 | +5 to 15 | extreme in occupied population | probable, confirmed on liberation |
| covert biological seed | 15 to 40 when confirmed | +10 to 20 | outbreak-driven | hidden to confirmed |
| strategic biological raid | 30 to 70 | +15 to 35 | extreme | probable or confirmed |
| stockpile accident | 2 to 25 | none | domestic deaths | public if major, not same as deliberate use |
| doomsday release | 150 to 500 | maximum | catastrophic | confirmed |

## Attribution multiplier

| State | Multiplier applied publicly | Latent record |
| --- | ---: | ---: |
| unknown | 0 to 0.10 | 90 to 100% retained |
| suspected | 0.25 | 75% retained |
| probable | 0.60 | 40% retained |
| confirmed | 1.00 | none unpaid |

## Context multipliers

| Context | Multiplier or add |
| --- | ---: |
| retaliation against confirmed first user, proportionate military target | 0.65 to 0.85 participant pressure, base responsibility remains |
| first use | 1.25 to 1.50 |
| neutral target | 1.75 to 2.50 |
| ally or subject target | 2.00 to 3.00 |
| occupied non-core civilian target | 1.25 to 1.75 plus atrocity context |
| capital or high population state | 1.15 to 1.50 |
| repeated use within 90 days | +25 to 75% |
| successful humanitarian response | -10 to 25% future participant pressure, not historical score |
| discovered coverup | +20 to 100% of original act in coverup bucket |

## Condemnation tiers

| Tier | Threshold | CBRN consequence |
| --- | ---: | --- |
| concern | 25 | monitoring and protection aid |
| censure | 50 | inspection demand and reduced support |
| arms embargo | 100 | military aid, licenses, volunteers, attachés restricted |
| strategic embargo | 175 | fuel, rubber, metals, instruments, and program supply restricted |
| total embargo | 300 | broad trade and research isolation |
| pariah | 500 | faction rupture, containment pressure, intelligence actions |

## Cleanup rates

| Resource | Trace or Local | Serious | Severe | Catastrophic |
| --- | ---: | ---: | ---: | ---: |
| no intervention | 1 to 5 points per month | 0.5 to 2 | 0.25 to 1 | minimal |
| local decon decision | +5 to 15 | +3 to 10 | +1 to 5 | +0.5 to 3 |
| Mobile Decon HQ | +5 to 10 per operation period | +5 to 10 | +3 to 8 | +1 to 5 |
| international mission | +5 to 15 | +5 to 15 | +5 to 12 | +2 to 8 |
| persistent-agent neutralization tech | ×1.25 to 1.50 | ×1.25 to 1.50 | ×1.20 | ×1.10 |

## Medical saturation

| Saturation | Effect |
| ---: | --- |
| 0 to 24 | normal response |
| 25 to 49 | continuing deaths +10%, recovery -5% |
| 50 to 74 | deaths +25%, recovery -15%, local output -5% |
| 75 to 100 | deaths +50%, recovery -30%, output -10 to 20%, foreign aid actions enabled |

## Nonduplication rules

- one operation record owns its deaths, contamination, and base Condemnation
- continuing deaths aggregate by state and source family
- Air Cleanliness changes on contamination class movement
- atrocity and coverup buckets add context, not a second full weapon-use score
- chaos comes from existing death and Air Cleanliness rules unless an explicit event adds more
