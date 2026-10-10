# Event 027: Doctrine Research

## Part 3: Evolutions, AI, balance, and cluster behaviour

## Evolution model

Event 027 has one linear evolution track.
Each stage adds one choice to every curriculum and never strengthens a single choice.
The batch sizes are the user's explicit brief; the tier mapping is the accepted design.

| Stage | Player-facing curriculum name | Chaos tier that makes it eligible | Choices per curriculum |
| --- | --- | --- | --- |
| Baseline | Foundational | Calm World | 1 |
| Evolution I | Expanded | Gathering Storm | 2 |
| Evolution II | Advanced | Rising Chaos | 3 |
| Evolution III | Joint-Service | Chaos Tier | 4 |
| Evolution IV | Comprehensive | Totalen Chaos | 5 |

All rules in this section are **implemented** (overview, Evolutions).

### Entry and promotion

The first firing opens at the highest stage the Chaos Meter has already made eligible, so a late first firing arrives with an evolved curriculum and no baseline curriculum first.
After the first firing, a daily global pulse promotes a newly eligible stage about 90 days after it became eligible, one stage per interval.
An evolution never grants an immediate curriculum; it changes the size of the next firing.

### Enabled states

Every stage checks its own Event Details setting.
A disabled stage is skipped and records nothing, and it never blocks a higher enabled stage.
Each firing sizes its curricula from the highest reached stage whose setting is still enabled, so switching Evolution IV off after it was reached makes the next firing use the highest lower enabled stage.
While Event 027 itself is disabled, the pulse promotes and records nothing and resumes from its stored clock once the event is enabled again.

### Evolution memory

The reached stage affects the next firing's size, the Event Details preview, the evolution History rows, achievement eligibility that depends on curriculum size, and the AI's multi-choice allocation.
It never affects the strength of one step, doctrine eligibility, participation, repeatable weight recovery, or the Chaos Meter.

Five choices is the last stage.
Most native branches have five levels and every Chaos Warfare subdoctrine has five, so Evolution IV already allows one fresh branch to be completed in one curriculum, and a sixth choice would add quantity without a new decision.

## AI design

The AI must spend its choices well enough that global symmetry does not hand human players a systematic advantage.
It uses the human validity pool, recalculates after every choice, stacks when one branch clearly leads, diversifies when several are close, and keeps a bounded amount of variation so countries do not converge on one pattern.

The scoring model below is **implemented**; exact weights live in the `doctrine_research_ai_weight`, `doctrine_research_ai_ratio`, and `doctrine_research_ai_native_*` script constant categories, and the overview's AI section is the reference for every term.
Real-campaign AI mixes are a **live check**.

### Domain scores

Domain scores read capability that belongs to each domain, so country-wide signals separate domains and never separate candidates inside one domain.

| Domain | Raised by | Zero or low when |
| --- | --- | --- |
| Army | divisions, land templates, military factories, war with divisions, a land front, alliance membership, the industry focus term unless dockyards or aircraft lead | every Army track is complete |
| Navy | warships, dockyards, convoys, naval doctrine, a coastal capital, a war without a land front, dockyard-led industry, a maritime plan | no coast, ships, dockyards, convoys, naval doctrine, or maritime plan |
| Air | deployed air wings, military factories, war or alliance with air wings, air-led industry (which also takes the land-front term) | no deployed air wings |
| Special Forces | templates fielding Special Forces battalions, with coast or mountains as a geography term | no Special Forces templates |
| Chaos Warfare | a viable CBRN programme, divisions, plains or mountains, a land front | the owning establishment gate fails |

A landlocked country has a maritime plan when it holds a core or claim on a coastal state it does not control, or has or is justifying a war goal against a country that owns one.
Completion value and strategy signals add weight in every domain.
If no domain scores, every valid domain falls back to the base weight, so a choice is never wasted.

### Grand Doctrine scores

A Grand Doctrine scores the formations it serves: Mobile Warfare motorised, mechanised, and armoured forces; Superior Firepower line and support artillery, anti-tank, and anti-air; Grand Battleplan a defensive war, forests, or mountains; Mass Assault infantry without mobile templates, militia, or irregulars; and every naval, air, Special Forces, and Chaos Warfare Grand Doctrine its own ships, planes, battalions, or CBRN programme.
The score is multiplied by the vanilla `ai_will_do` factors for that doctrine, so country identity and minor or major status shape the result as they do natively.
Event 027 never builds a strategy table that ignores those native preferences, and AI scoring can never bypass Chaos Warfare eligibility.

### Track and subdoctrine scores

A track scores its base weight, its force fit, one investment point per level earned, an empty-track bonus when an empty track fits, completion value when one step from completion and fitting, and continuity with the previous choice in the curriculum.
A subdoctrine candidate for an empty track scores its base weight, its earned or banked levels, completion value one level below its maximum, continuity, and its own unit fit.
Both sums are squared before they enter the weighted random list, which lets a clearly better candidate win most choices, keeps close candidates close, and keeps every valid candidate possible.
A near-complete branch the country has no formations for keeps only its investment value, so completion never overpowers a severe strategic mismatch.

Chaos Warfare track fit reads each track's own fielded CBRN battalions: the battalions its subdoctrine earns mastery from and the companies its bonuses serve.

### Multi-choice allocation

Because the AI rescores after every successful choice, a strong lead produces stacking, a completed branch drops out and forces a fresh target, an adoption immediately opens the new doctrine's tracks, and the fifth choice of Evolution IV receives its own score pass.

### Delegated human choices (pending R5)

Revision R5 in part 2 lets a human hand the remaining choices to the same resolver.
It needs no new weights and must not change the AI pool.

## Balance intent

### Global symmetry

Every participant receives the same number of choices from one firing, and majors and minors are treated alike.
Symmetry is not equal value, because doctrine states and native branch rewards differ, so strong AI selection is part of balance.

### Direct power

One baseline choice can establish a doctrine or complete a nearly finished track, but never a whole doctrine portfolio.
Evolution IV is a late-chaos capstone where five steps can complete a fresh five-level branch; this is intended and arrives only at Totalen Chaos.

### Repeatable diminishing returns

Event 027 uses the shared repeatable contract: its weight resets on firing, its maximum cap halves, and weight recovers on the event-system pacing pulses.
That makes repeated global curricula progressively rarer without an event-specific cooldown.
A recurrence or starvation claim against other events needs the complete automatic-selection pool, which selects across all registered events rather than only repeatable ones; that sequence evidence is still missing (scenario group F).

### Chaos and compensation

Doctrine Research never changes the Chaos Meter directly and never compensates an exhausted country.

## Exploit controls

| Exploit | Control (all implemented) |
| --- | --- |
| Resetting a poor doctrine for free | The event never replaces a Grand Doctrine or a selected subdoctrine. |
| Refunding earlier experience | Only the event's own action is free; nothing is refunded. |
| Double consumption | One-time receipts survive double clicks, duplicate pages, save, reload, and delayed continuations. |
| Farming banked mastery | Banked mastery is preserved and only explicit event steps are attributed. |
| Overwriting a queued curriculum | Every firing appends a distinct curriculum. |
| Cluster double fanout | One cluster firing calls the Event 027 fanout once. |
| Tag switching | A curriculum stays with its country. |
| Annexation or re-release farming | Unused choices disappear with the country, and released countries get no retroactive curriculum. |
| Achievement farming | Only consumed receipts of the active or closing curriculum count; debug, console, cluster-forced, and test-country setups are excluded. |

## National Breakthroughs cluster role

National Breakthroughs groups small positive developments in military knowledge, research, leadership, and institutions.
Event 027 is a Medium member because it is global and reaches five direct steps at Evolution IV.

| Attribute | Value (implemented) |
| --- | --- |
| Cluster ID | `9`, reserved in the runtime registry and the workbook |
| Runtime member row | `9001`, Event 027 |
| Member role | Optional when another member is selected; guaranteed as the originally selected event |
| Minimum tier | Calm World |
| Severity | Medium |
| Cooldown | Shared cluster cooldown of 120 days |
| Effect when included | One normal fanout at the current stage, no extra choices, no extra pacing |

The other catalogued members (54, 65, 67, 83, 85, 89) join the runtime cluster only when their own reworks are implemented, and participation chances are tuned with the full member pool at that time.
A cluster should normally produce two or three members, not every eligible member.
Until a second member exists, the optional-member case cannot be exercised, and the cluster stays Partially Available in the catalog.

When Event 027 and Event 085 fire in one cluster, Event 027 grants doctrine actions and Event 085 grants its own experience reward; neither scales the other.

## Expansion scope

The doctrine curriculum, its stacking choices, adapters, AI, evolutions, achievements, and cluster role fully serve the event's promise.
A pressure meter, doctrine currency, decision category, focus branch, faction mechanic, custom window, or crisis chain would duplicate the native doctrine system and turn a small positive breakthrough into a burden.
Further work belongs to usability (revisions R1 to R7), live engine evidence, the recurrence audit, and new National Breakthroughs members.
