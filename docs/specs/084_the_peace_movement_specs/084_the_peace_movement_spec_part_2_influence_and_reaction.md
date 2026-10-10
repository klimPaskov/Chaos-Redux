# 84 · The Peace Movement
## Part 2 · Influence, reaction, social effects, and demographic policy

### Influence bands

| Influence | Political condition | New possibilities |
|---|---|---|
| 0–19 | Scattered or dormant circles | Local organizing, protection, exposure, or containment |
| 20–39 | Public counterculture | Civic projects, regular cultural events, conscientious-objection demands, local patrons |
| 40–59 | Established movement | National negotiations, larger strikes, recurring character affiliations, foreign sponsorship |
| 60–79 | National contender | Coalition demands, elections or constitutional transfer, mass noncooperation, military loyalty disputes |
| 80–100 | Dominant social force | Movement-led institutions, broad civilian reorientation, mass voluntary organizing, final-route candidacy where government authority also exists |

The table shows whole-point display bands.
Internally use the half-open intervals 0≤Influence<20, 20≤Influence<40, 40≤Influence<60, 60≤Influence<80, and 80≤Influence≤100.
Retained fractions belong to the interval selected by those lower-bound thresholds.

Crossing a band changes the available political opportunities.
It does not automatically grant the government, create military units, change ideology, or qualify the country as movement-dominated for the world-end calculation.

### Reaction bands

| Reaction | Political condition | New possibilities |
|---|---|---|
| 0–24 | Limited organized opposition | Ordinary debate and legal opposition |
| 25–49 | Organized countercampaign | Public petitions, rival demonstrations, traditionalist officials, family-policy negotiations |
| 50–69 | National counter-movement | Coordinated strikes or boycotts, international contacts, cabinet pressure, security demands |
| 70–84 | Polarized institutions | Command splits and rupture incidents when Influence is also high |
| 85–100 | Immediate confrontation risk | Emergency conventions, leadership challenges, armed uprisings after a concrete trigger |

Reaction uses the corresponding internal thresholds below 25, below 50, below 70, below 85, and up to 100.
A value of 24.5 remains in the first band, even though the display rounds to whole points.
Gameplay uses the internal value, not the rounded label.

High Reaction can exist under either government.
Movement rule does not reset it.
A traditionalist takeover does not automatically reduce it, since the winning coalition may keep demanding further restrictions or mobilization.

### Change cadence and pressure buckets

Use a country-owned 30-day political review as the balance unit.
An urgent crisis can be checked every 10 days, with elapsed-time accounting, without applying a full monthly change three times.
Fractions may be retained internally so changing review cadence does not change total pressure.
The interface shows whole points, the expected net change, the three largest current causes, and the next consequential threshold; the full source table below stays internal.

The normal monthly net change is capped at minus 10 to plus 10 Influence and minus 10 to plus 15 Reaction.
Discrete incidents can exceed that monthly drift, but one incident never re-applies when a report is reopened.
Distinct incident families have cooldowns and factual causes.
The cap prevents ten overlapping cultural or military predicates from turning one country into a revolutionary state overnight.

| Influence source | Proposed monthly contribution | Meaning and limit |
|---|---:|---|
| A war lasting at least 180 days | +5 | Count the country's sustained war burden once, not each enemy |
| Severe recent military losses | +5 | Recorded losses in the last 30 days reach 5% of the country's prior deployed manpower, using a minimum denominator of 5,000 |
| War Support below 40 during an active war | +5 | A country at peace is not punished merely for low War Support |
| A recorded nuclear, chemical, or biological strike on the country's controlled states in the last 60 days, or the country's own condemnation at tier 3 (100) or higher | +5 | One contribution however many strikes or sanctions apply; it reads the CBRN and condemnation owners' records and never recreates their effects |
| Extensive Conscription or a harsher applicable law | +5 | A military-service grievance, removed by a genuine alternative-service settlement |
| Open organizing under toleration | +5 | Requires an active cell and public organization |
| Completed festival, exchange, or civic project | +5 for 60 days | One cultural-development contribution regardless of how many events were held |
| Active sympathetic official or institution | +5 | One aggregate contribution, not one per character |
| Maintained foreign network | +5 | One contribution across neighboring states, trade, media, and sponsors |
| A credible unresolved repression incident | +5 | Applies during its stated aftermath, not for fabricated deaths or generic policing |
| A fulfilled reform settlement after war ends | −5 | Reduces confrontational mobilization while preserving the reform |
| A quiet, satisfied country without active organizing | −5 | Attention fades toward a dormant cell, not compulsory social reversal |

The war sources share a plus 10 bucket ceiling.
Cultural, official, and foreign-network sources share a plus 10 bucket ceiling.
Apply those bucket ceilings before the final monthly net cap.
A government cannot manufacture unlimited Influence by repeatedly changing the same conscription law.

| Reaction source | Proposed contribution | Meaning and limit |
|---|---:|---|
| Influence rose by at least 15 within 60 days | +5 monthly while that rapid change is current | A rapid-change response, not a tax on all lasting movement support |
| A contested social reform without an agreement | +5 for 60 days | One reform bundle contribution, reduced by a negotiated accommodation |
| Mass draft refusal disrupts a current mobilization | +5 for 60 days | Requires an actual service crisis |
| A verified production stoppage in an active war | +5 for 60 days | Mere lower military output from a peaceful economy does not count |
| A real attack on a religious or national institution | +10 once, then +5 for 60 days | Targeted incident with investigation and de-escalation options |
| Government institutions are seized outside an accepted transfer | +15 once | Separate from an ordinary election or lawful coalition |
| Armed movement formations operate outside civilian command | +5 monthly | Ends when the command agreement is fulfilled or the formations are disarmed |
| Coercive foreign interference is exposed | +10 once | Applies to either bloc and is not triggered by ordinary cultural exchange |
| A credible pluralist settlement is maintained | −5 monthly | Requires actual protection of assembly and public institutions |
| Reconstruction and demobilization milestones are completed | −10 once per distinct milestone | Limited by the aftermath plan, not infinitely repeatable |

Religious identity, sexuality, gender, and family status are not pressure predicates on their own.
Political organizations and actual policies supply the conditions.

### Baseline national effects

The following are total Event 84 contributions at each Influence band before Reaction and route changes.
They replace the previous band rather than stacking on top of it.
A percentage point change to War Support or Stability is distinguished from a relative modifier to speed, output, demand, or recruitment.

| Influence | War Support | Military output | Training time | Recruitable population factor | Consumer-goods factor | Stability | Civilian construction speed |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0–19 | 0 pp | 0% | 0% | 0% | 0% | 0 pp | 0% |
| 20–39 | −10 pp | −5% | +5% | −5% | +5% | +5 pp | +5% |
| 40–59 | −20 pp | −10% | +10% | −10% | +10% | +10 pp | +10% |
| 60–79 | −30 pp | −20% | +20% | −20% | +15% | +15 pp | +15% |
| 80–100 | −40 pp | −30% | +30% | −30% | +20% | +20 pp | +20% |

The brief lists lower mobilization speed among possible effects; it is deliberately left out because War Support, recruitable population, and training time already carry the same burden in ways the player feels.

The consumer-goods column is a relative factor, not an extra 20 percentage points of factories assigned to consumers.
Its actual factory burden must be previewed against the installed game's economy rules.
Recruitment penalties represent refusal, demobilization, and reduced participation.
They do not remove people or count as deaths.
Civilian construction bonuses do not accelerate military factories, bunkers, dockyards, or special military projects unless a later explicit route changes a particular project.

A negotiated civic-service program can turn the recruitment and training penalties into a managed tradeoff.
Civilian service workers remain unavailable for ordinary military recruitment while serving.
Completing reconstruction objectives can improve the civilian payoff and reduce disruption, but it does not create both free soldiers and free civilian workers from the same people.

### Reaction and polarization effects

Reaction 25–49 adds a minus 5 percentage-point Stability contribution.
Reaction 50–69 adds minus 10.
Reaction 70–84 adds minus 20.
Reaction 85–100 adds minus 30.
These are totals for the band, not cumulative deductions.
When Influence is at least 60 and Reaction at least 70, add a further minus 10 percentage points of Stability and minus 10% political-power gain for unresolved polarization.

If violent street conflict is active, suspend the movement's civilian-construction bonus in the affected country until an order or reconciliation objective is completed.
Do not suspend legal equality or religious freedom as a mechanical requirement for restoring construction.
The social conflict, not the identity of its participants, causes the disruption.

When a credible settlement has been maintained for 180 days, the temporary polarization penalty ends even if strong peaceful political organizations remain.
Thereafter Reaction represents legal political opposition unless a new material rupture occurs.
The player is not forced to drive both values to zero.

### Three national-spirit families

Use at most three simultaneous Event 84 national spirits.
Their structural names below are working labels, not final localisation.

| Family | Carries | Lifecycle |
|---|---|---|
| Social settlement | Influence-band Stability, Reaction penalties, legal agreements, political-power effects | Local movement → organized movement → negotiated society, revolutionary society, or restoration settlement |
| Civilian economy | Civilian construction, consumer-goods factor, military production, demographic-policy effects | Counterculture economy → route-specific civilian program → rebuilt mixed or communal economy |
| Service and command | War Support, recruitment, training, military pledges, defense mandates | Draft dispute → civilian service or resistance → armed-defense compact or restored command |

New reform, festival, scandal, or foreign-aid effects update these families or remain local objectives.
They do not each add another national spirit.
A character's ordinary role trait is not turned into a fourth hidden national spirit to evade this budget.

### Demographic choices

The movement's voluntary-childlessness and anti-natalist currents become selectable policy after it gains governmental authority.
The first policy decision must distinguish personal freedom from state discouragement of parenthood.

| Policy, working label | Effect | Tradeoff and route |
|---|---|---|
| Family autonomy | No Event 84 population-growth penalty | Protects voluntary childlessness and varied families without rewarding or penalizing parenthood |
| Deferred parenthood program | −25% to positive natural population growth while maintained | Civilian-welfare budget and housing commitments are prioritized over population-growth campaigns |
| Anti-natalist program | −50% to positive natural population growth | Strongest voluntary-childlessness current, larger political dispute and a difficult future recruitment outlook |
| Inclusive family support | Removes Event 84 growth penalties after a 180-day civic program | Costs real civilian construction capacity and supports parents without withdrawing LGBTQ equality |

These are fictional gameplay magnitudes, not empirical demographic claims about LGBTQ people, communal living, religion, or nontraditional families.
They reduce additions to living population.
They never subtract existing people, fabricate deaths, or immediately convert forgone births into missing adult recruits during a short war.
A negative natural-growth state is not made more negative by this modifier.

The policy is chosen in the family-policy congress event (Part 4), not through a separate decision.
It can be changed only after 180 days, by reconvening that congress.
Turning it on and off does not refund resources or restore forgone growth retroactively.
The demographic policy is disclosed in its decision and in the civilian-economy spirit.
No separate fertility meter is added.

### Dormancy and return

A country at Influence 15 or lower, Reaction 20 or lower, with no armed organization, active repression case, foreign operation, or unfulfilled political promise can enter dormancy after 90 days.
The category collapses to a compact status.
A dormant local network can return after a new long war, a genuine broken settlement, fresh outside sponsorship, or a new repression incident.
Routine monthly drift cannot repeatedly awaken and settle the same country to farm rewards.

A country with a fulfilled permanent settlement retains its laws and any paid civilian investments.
Its previous settlement flag suppresses repeated first-time rewards.
A renewed crisis reopens only the disputed institutions and current military questions.
