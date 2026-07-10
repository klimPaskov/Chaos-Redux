# Gas-Mask Starting Stockpile Matrix

## Equipment unit

One unit is one protective-equipment crate. It represents about one thousand civilian respirators or about one hundred military full-issue sets with filters, training, spares, and carrying equipment.

## Calculation

`starting crates = civilian reserve + field army reserve + mobilization and training reserve`

### Civilian reserve

`core population / 1,000 × target civilian coverage`

### Field army reserve

`fielded military manpower / 100 × target issue multiplier`

The military conversion already reflects a military set using more material than a civilian respirator.

### Training reserve

Add 5 to 25 percent according to First World War experience, civil-defence institutions, industry, and doctrine.

## Country targets

Exact values require current 1936 core population and OOB data. Bands below are acceptance ranges.

| Country or profile | Civilian coverage target | Military issue target | Starting crates target | Starting tech | Program identity | Confidence |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Britain | 65 to 85% | 150% of fielded need | 35,000 to 50,000 | basic and improved where compatible | mass civilian distribution, strong registration | high relative, medium exact |
| France | 35 to 55% | 140% | 18,000 to 30,000 | basic and improved | fortified-front and urban reserve | medium |
| Germany | 35 to 55% | 150% | 20,000 to 32,000 | basic and improved | military and urban reserve | medium |
| Soviet Union | 15 to 30% | 140% | 18,000 to 30,000 | basic | huge military reserve, uneven civilian issue | medium-low exact |
| United States | 8 to 18% | 120% | 10,000 to 18,000 | basic | industrial reserve and rapid expansion | medium-low exact |
| Italy | 10 to 25% | 110% | 7,000 to 13,000 | basic | military and priority cities | low exact |
| Japan | 8 to 20% | 120% | 8,000 to 15,000 | basic | military-first, limited civilian issue | low exact |
| Poland | 20 to 35% | 130% | 6,000 to 10,000 | basic | exposed frontier and urban reserve | low exact |
| Czechoslovakia | 25 to 40% | 130% | 4,000 to 7,000 | basic | strong industry and preparedness | low exact |
| Belgium | 20 to 35% | 120% | 2,500 to 4,500 | basic | First World War legacy | low exact |
| Netherlands | 15 to 30% | 110% | 2,500 to 5,000 | basic | urban civil defence | low exact |
| Canada | 10 to 25% | 120% | 2,000 to 4,500 | basic | Commonwealth defensive reserve | low exact |
| Australia | 8 to 20% | 120% | 1,500 to 3,500 | basic | Commonwealth military reserve | low exact |
| New Zealand | 8 to 20% | 120% | 400 to 1,000 | basic | Commonwealth reserve | low exact |
| South Africa | 5 to 15% | 100% | 800 to 2,000 | basic | military reserve | low exact |
| Romania | 5 to 15% | 100% | 1,000 to 3,000 | basic or research progress | military reserve | low exact |
| Yugoslavia | 5 to 15% | 100% | 1,000 to 3,000 | basic or research progress | uneven reserve | low exact |
| Turkey | 5 to 15% | 100% | 1,000 to 3,000 | basic or research progress | military reserve | low exact |
| Spain | 2 to 10% | 80% | 500 to 2,000 | variable by civil war setup | disrupted reserve | low exact |
| China | 1 to 5% | 50 to 80% priority units | 1,000 to 5,000 | limited | enormous population, scarce industry | low exact |
| industrial minor with WWI experience | 5 to 15% | 80 to 110% | population formula, usually 500 to 2,500 | basic possible | defensive reserve | profile only |
| small minor | 0 to 5% | 0 to 70% | 0 to 500 | none or researchable | emergency procurement | profile only |

## Distribution state

Starting crates do not mean all civilians are protected. Country history can begin with:

- crates in national reserve
- selected states already distributed
- registered population bonus
- military issue reserve

Britain should begin with the largest distributed share. Other countries can begin with reserve that requires decisions to issue.

## Production target after alert

| Coverage gap | Suggested AI production priority |
| ---: | --- |
| military below 50% | emergency, 6 to 10% of military IC if possible |
| military 50 to 80% | high, 4 to 7% |
| military 80%+ and civilians below target | medium, 2 to 5% |
| reserve above target | maintenance, 0.5 to 2% |

## State decision cost

`base crates = state population / 1,000`

| Modifier | Multiplier |
| --- | ---: |
| capital or dense urban | 1.15 to 1.30 |
| active bombing | 1.20 |
| active frontline | 1.30 to 1.50 |
| infrastructure below 5 | 1.15 to 1.40 |
| occupied non-core | 1.25 to 1.75 |
| civil-defence registration | 0.85 |
| mass-distribution institutions | 0.75 to 0.90 |
| improvised emergency issue | 0.60 cost, only 35 to 55% effective coverage |

## Replacement consumption

| Condition | Reserve consumption |
| --- | ---: |
| peacetime storage and training | event-driven 0.5 to 2% yearly for basic models |
| theater protective posture | 0.5 to 2% of covered military stock per week |
| actual chemical exposure | 2 to 8% of covered stock per episode |
| Severe contaminated state | 1 to 3% weekly for units remaining in state |
| civilian chemical raid | 5 to 20% of distributed state stock damaged or filters consumed |
| Catastrophic state exposure | 15 to 35% |

Improved technology reduces consumption.

## Validation

- Calculate against actual 1936 populations and OOBs.
- Compare starting crates with production cost and annual output.
- Ensure Britain can protect most civilians without consuming years of production.
- Ensure the Soviet Union and China cannot obtain near-total coverage from a modest stock.
- Ensure small countries can protect a few divisions and a capital.
