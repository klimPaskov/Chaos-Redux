# Event 046 range and distribution matrix

The ranges below are design anchors.

Implementation centralizes exact bands after current engine limits and probability evidence are available.

No profile uses the scope's old amount as its center.

| Family | Frozen scale source | Baseline profile | Later profile direction | Hard legality rule |
| --- | --- | --- | --- | --- |
| Stability | Legal percentage range | Broad center with visible low and high tails | Stronger two-tail, full legal band at Evolution V | Remain inside engine percentage bounds |
| War Support | Legal percentage range | Broad center | Independent stronger tails | Remain inside engine percentage bounds |
| Political Power | Current legal cap | Broad center above zero | Flat legal or two-tail | Negative balance excluded unless proven supported |
| Command Power | Country's frozen current cap | Broad center | Low-skew, high-skew, or two-tail | Never exceed frozen cap |
| Army, Navy, Air Experience | Current legal cap for each store | Broad center | Full tails | Never exceed cap |
| Reserve manpower | Frozen world population, valid-country count, era, and country civilian population ceiling | Wide absolute bands with moderate center | Stronger low and high bands | Keep a legal national reserve and reconcile state effects |
| Fuel | Frozen country capacity | Broad share of capacity | Two-tail and scarcity or abundance moods | Between zero and capacity |
| Convoys | Era and frozen world production scale | Broad absolute bands | Scarcity, abundance, or two-tail | Practical object ceiling |
| Trains | Era and frozen world production scale | Broad absolute bands | Scarcity, abundance, or two-tail | Practical object ceiling |
| Equipment family | Era, family scale, loaded token set, and frozen world production anchor | Broad quantities by equipment class | Stronger zero, scarcity, and huge-stockpile tails | Only valid concrete tokens and practical quantity ceiling |
| State population | Frozen mean population per valid state and protected floor | Near-empty, sparse, ordinary, dense, and megastate bands | More near-empty and megastate results | Absolute legal population, no Deaths registration |
| Shared factories | Planned legal shared capacity | Independent civilian and military counts inside capacity | More empty and maximum-capacity states | Sum remains legal, dockyards coastal |
| Infrastructure and level buildings | Current legal building maximum | Broad legal level | Flat legal or two-tail | Legal integer level and feature loaded |
| Resources | Resource-specific world anchor and legal token | Broad resource bands including zero | Scarcity, abundance, or split-tail | Token valid and owner-protected deposits excluded |
| Party popularity | Loaded ideology set | Normalized shares with broad center | Stronger dominant and fragmented distributions | Shares reconcile to exact legal total |
| Ruling ideology | Approved loaded candidate set | Categorical compatible | Wider candidate eligibility | One legal ruling ideology and owner reconciliation |
| Law category | Approved category tokens | Categorical compatible with moderate extremes | Extreme tokens more common | Exactly one token in category |
| Active research progress | Current active project and legal progress cap | Broad center below completion | Low-skew, high-skew, or two-tail | Same project identity and no accidental completion unless accepted |
| Doctrine progress | Current selected doctrine and legal progress cap | Broad center | Stronger tails | Completed graph unchanged |
| Production efficiency | Current line cap | Broad center | Full legal tails | Same line and item identity |
| Stored production progress | Current line and supported progress range | Broad center | Low or high skew | Same line identity and legal value |
| Unit experience | Unit-domain legal range | Broad center | Full tails | Same unit identity |
| Unit planning | Current legal planning cap | Broad center | Full tails | Same unit and valid order state |
| Commander experience | Current commander range | Broad center | Full tails | Same commander identity and traits |
| Owner numeric value | Owner-supplied frozen floor and cap | Owner profile | Owner-approved stronger tails | Owner validation and reconciliation |
| Owner categorical value | Owner-supplied candidate set | Categorical compatible | Owner-approved rare categories | Stable object and one legal token |
| Claims | Valid country-state pair pool | Not available | Structural pair profile at Evolution V | Cores protected and pairs deduplicated |
| Ownership | Valid country-state bundle | Not available | Structural profile only after full proof | Country survival, capital, war, supply, unit, and occupation legality |
| Diplomatic pair | Valid pair and relationship contract | Not available | Structural pair profile | Symmetry, duration, and war legality |
| Unit location | Valid owned or controlled province pool | Not available | Structural location profile | Domain-specific base and pathing legality |

## Family world moods

A selected family can roll one mood for the whole transaction.

`balanced` uses its standard profile.

`scarcity` uses a low-skew profile.

`abundance` uses a high-skew profile.

`split` uses a two-tail profile.

The mood changes the distribution for every valid scope in that family.

It does not conserve a global total and does not pair one winner with one loser.

The family mood is fresh on every firing.
