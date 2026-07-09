# Event 020 Black Plague source notes

These notes are safe design references. They are not real-world operational guidance. The gameplay design should stay at a high abstraction level and must not include lab protocols, growth methods, delivery engineering, or real instructions for biological harm.

## Plague biology anchors for design

- The disease behind plague is `Yersinia pestis`, and modern plague can be treated with antibiotics when diagnosis and treatment happen quickly. This supports the cure-progress model, where treatment reduces deaths and spread before it allows cleanup.
- Plague can spread through infected fleas, contact with infected animals or tissues, and pneumonic droplets under close contact. This supports several in-game spread vectors: crowded states, poor public health, rodent pressure, troops, ports, and infected neighboring states.
- Pneumonic plague can develop quickly and is the most virulent form. This supports an evolved form that has shorter escalation windows and punishes delayed response.
- WHO outbreak guidance emphasizes finding the source, vector control before rodent control, isolation of pneumonic cases, monitoring contacts, protective measures for workers, treatment supply, and disinfection. This supports a dynamic decision board with source tracing, vector control, quarantine, medical stockpiles, inspections, and cleanup.

Sources consulted:

- WHO fact sheet on plague: https://www.who.int/news-room/fact-sheets/detail/plague
- CDC about plague: https://www.cdc.gov/plague/about/index.html
- CDC how plague spreads: https://www.cdc.gov/plague/causes/index.html
- WHO plague management guidance page: https://www.who.int/publications/i/item/9789240015579

## Historical scale anchors for design

The Black Death is used as scale inspiration, not as a literal historical recreation. Oxford History notes that long-accepted estimates put western European mortality around 25 to 33 percent, while later research argues for far higher regional impact. The spec uses this only to justify that ignored Black Death states can lose a very large share of population over time.

Source consulted:

- Oxford Faculty of History, Black Death and European Expansion: https://www.history.ox.ac.uk/black-death-and-european-expansion

## Rat king inspiration

The King of Rats route is fictional and high-chaos. The real phrase rat king refers to rare groups of rats with entangled tails, and Estonian research records the phrase and some finds. The event should use the term as folklore-shaped inspiration for a sentient nonhuman unifier, not as a realistic natural history claim.

Source consulted:

- Andrei Miljutin, Rat kings in Estonia, 2007: https://www.researchgate.net/publication/240640974_Rat_kings_in_Estonia

## Safe design boundary for weaponization

The weaponization path must be written as Hearts of Iron IV special-project abstraction. It can include samples, containment safety, delivery readiness, stockpile accident risk, condemnation, and deployment hooks inside existing Chaos Redux biowarfare systems. It must not include real laboratory steps, real procedures, real equipment recipes, or real optimization instructions.
