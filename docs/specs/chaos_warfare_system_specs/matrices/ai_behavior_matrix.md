# AI Behavior Matrix

## Strategic posture selection

| AI situation | Defensive preparation | Retaliatory arsenal | Battlefield chemical army | Strategic CBRN power | Desperate release |
| --- | ---: | ---: | ---: | ---: | ---: |
| enemy has no CBRN capability | medium for exposed majors | low | very low | zero | zero |
| enemy researches or stockpiles chemicals | high | medium | low | very low | zero |
| enemy confirmed first use | maximum | high | medium | low to medium | low |
| doctrine already adopted | high | high | high based on route | medium | route dependent |
| severe equipment deficit | medium protection only | low | zero | zero | low near capitulation |
| high industrial surplus | high | medium | medium | medium after projects | route dependent |
| high import dependence and condemnation | high | low | low | very low | low unless collapse |
| radical or high-chaos route | medium | medium | high | high | medium to high |
| near capitulation | medium if stock remains | medium | medium | low | high with route |

## Research decisions

| Condition | AI response |
| --- | --- |
| military protective coverage below 50% | prioritize masks and filter technologies |
| enemy has blister agents | prioritize protective clothing and decontamination |
| enemy has nerve agent | prioritize advanced masks, antidotes, medical HQ |
| own artillery posture | research chemical shell logistics before air delivery |
| own air posture and air superiority potential | research chemical air interdiction after mask reserve is adequate |
| own armor posture | research sealed crews before armored delivery |
| completed biological project | research containment and surveillance before mass payload production |
| high stockpile accident risk | prioritize safety or reduce production |
| Condemnation 100+ and import vulnerable | pause offensive tech unless victory pressure is severe |

## Production decisions

| Trigger | Action | Stop condition |
| --- | --- | --- |
| military mask coverage below target | assign 4 to 10% military IC to masks | coverage and reserve target reached |
| civilian priority state unprotected after threat | maintain 2 to 5% mask IC | priority states at target coverage |
| selected CBRN HQ lacks instruments | instruments and support equipment priority | two HQ reserve sets available |
| contaminated front lacks cleanup | decon and trucks priority | one mobile column per active theater |
| prepared chemical operation planned | build payload and delivery lots | 125% reserved requirement reached |
| payload reserve above 200% target | reduce offensive line | reserve falls or new operation planned |
| stockpile risk Dangerous or Critical | stop biological payload line | safety restored or explicit desperate route |

## Operation authorization

| Factor | Weight for use | Weight against use |
| --- | ---: | ---: |
| fortified target | +30 | 0 |
| important supply hub | +25 | 0 |
| stalled front | +20 | 0 |
| target masks below 50% | +30 | 0 |
| favorable forecast | +25 | 0 |
| retaliation status | +40 | 0 |
| own order protection 90%+ | +30 | 0 |
| own order protection below 50% | 0 | +100 |
| payload ratio below 75% | 0 | +40 |
| friendly or allied state | 0 | +200 |
| neutral target | radical profile +20 | ordinary profile +200 against |
| target near capitulation | +5 | +25 waste penalty |
| Condemnation tier 3+ | radical +10 | import-dependent +50 |
| expected blowback high | desperate +10 | ordinary +80 |
| enemy protection 90%+ | +5 persistent role | +50 for choking use |

Final weights belong in constants and country AI strategies.

## Agent selection

| Situation | Preferred agent |
| --- | --- |
| early unprotected front | chlorine or phosgene |
| fortified and static route | mustard or lewisite |
| rapid high-value breakthrough | nerve agent after project |
| target has masks but weak decon | blister agent |
| target has advanced protection | avoid choking, use conventional or persistent combined operation |
| low desired deaths | incapacitant or malodor profile |
| occupation high resistance | nerve suppression only under route and policy |
| high sanction vulnerability | no use or retaliation-only local use |

## Target selection

| Target type | Chemical artillery | Chemical air raid | Biological operation | Nerve suppression |
| --- | ---: | ---: | ---: | ---: |
| fortified frontline state | very high | medium | low | not applicable |
| capital | medium | very high under extreme policy | high | only if occupied and route permits |
| supply hub | very high | high | medium | not applicable |
| port | high | high | medium to high | not applicable |
| airbase | medium | high | low to medium | not applicable |
| low-population empty state | low | low | very low | low |
| occupied high-resistance state | low | low | low | high under policy |
| own core contaminated state | cleanup only | never | containment only | never |
| allied state | never offensive | never offensive | never offensive | never |

## Defensive reaction

| Event | Immediate AI action | Follow-up |
| --- | --- | --- |
| enemy capability detected | start mask production, protect key divisions | civil-defence reserve and HQ |
| probable chemical raid | emergency distribute masks in target | air defence and forensic evidence |
| confirmed chemical use | activate protective posture | retaliation or sanction policy |
| Serious contamination | deploy decon and reroute supply | cleanup mission |
| biological seed suspected | surveillance and movement control | quarantine if confirmed |
| severe outbreak | hospitals, quarantine, aid request | vaccination or antibiotics |
| facility capture | send biosecurity formation if available | preserve evidence or destroy safely |

## Sanction response

| Country profile | Preferred response at high Condemnation |
| --- | --- |
| democratic and import dependent | inspections, stockpile reduction, humanitarian response |
| authoritarian industrial major | denial, partial compliance, autarky |
| radical high-chaos | defiance, black market, faction shielding |
| desperate near victory | continue operations until stock or war goal exhausted |
| losing near capitulation | doomsday only if explicit route, otherwise destroy or relocate stock |

## Template refresh

AI template updates should occur after:

- doctrine adoption
- enemy confirmed CBRN use
- relevant mastery unlock
- equipment reserve threshold
- major theater assignment

Do not rebuild every template on a broad daily or weekly loop.

## AI fail-safes

- no operation without a valid target state
- no use against ally, subject, or own state unless explicit doomsday logic
- no chemical air contamination from idle aircraft
- no biological operation with domestic containment below minimum unless desperate route
- no nerve suppression in a state likely to be lost within a short horizon
- no offensive support in templates if payload production is zero
- no research of locked special-project technology
- no black-market or sanction action against dead or invalid countries
