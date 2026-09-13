# Event 046 report priority matrix

| Report domain | Candidate rows | Normal display cap | Importance inputs | Special threshold examples |
| --- | --- | ---: | --- | --- |
| Global | Capability, committed families, rejected families, countries, states, units, adapters | One compact block | Scope counts and highest committed domain | Evolution V maximum coverage |
| Core politics | Stability, War Support, Political Power, ruling ideology, laws, party support | Three | Range-normalized delta and categorical severity | Stability or War Support at extreme low, ruling support below one fifth |
| Military stores | Manpower, fuel, equipment families, convoys, trains, military experience | Three | Capacity share, normalized stockpile value, operational threshold | Fuel reaches zero, equipment fulfillment collapses, huge reserve gain |
| State population | Largest owned or controlled population changes | Two | Change relative to family range and world ranking | State enters near-empty or megastate band |
| State industry | Largest factory, building, or resource changes | Two | Capacity share, resource band, strategic building threshold | State becomes top industry decile, loses every factory, gains major resource deposit |
| Research and production | Active progress, doctrine progress, line efficiency and progress | Two | Range-normalized delta and completion proximity | Active project nearly erased or brought near completion |
| Units and commanders | Experience, planning, approved readiness, commander experience | Two | Unit importance and normalized change | Largest army becomes untrained, key formation reaches elite band |
| Owner mechanics | Owner-approved public values | Two per broad domain, normally three total | Owner threshold score and normalized delta | Crisis stage crossed, legitimacy collapses, cohesion peaks |
| Structural | Claims, ownership, capital, diplomacy, location | Three | Owner-declared structural severity | Capital moved, state changed owner, major force relocated |
| Rejected selected families | Public domain name only | One summary line | Relevance to player's country and selected capability | Mandatory Evolution V family rejected |

## Tie breaking

Ties are resolved by greater threshold severity, then greater normalized change, then stable family and scope order.

The tie breaker is deterministic for every player viewing the same country.

## Omitted rows

The report states how many additional material changes were omitted when the cap hides valid rows.

It does not open a second ledger or custom window.

Debug evidence retains the full transaction summary outside player-facing text.
