# Event 049 Doomsday Specification

## Part 1: Core Event Design

## Catalog identity

- Event ID: `49`
- Event name: Doomsday
- Replaces: Mass Panic
- Event type: Major
- Chaos level: 4
- Cluster: None
- Status before implementation: To Be Reworked
- Public world-end route: The Final Vigil

## Playable promise

Doomsday turns the expectation of an ending into a global political and social crisis.

The event does not ask the player to stop a comet, defeat an invading army, expose one fraud, or trust one expert. It asks whether a state can keep people working, learning, serving, investing, and governing when a large part of society has stopped believing that the future will arrive.

The predicted end may never occur. The consequences of believing in it are still real.

The player should feel pressure from three directions:

1. The world’s shared conviction keeps rising as unrelated signs, movements, disasters, wars, and public experiences are drawn into one explanation.
2. The predicted date keeps approaching, which changes the value of long projects and makes delay increasingly costly.
3. The country’s chosen response can preserve institutions, redirect society, intensify repression, end wars, or hand practical authority to the movements.

The event must remain playable for countries at peace, countries at war, democracies, dictatorships, colonial empires, occupied territories, small states, and major powers. Their pressures and available responses should differ.

## Opening incident

The entry event fires as a Major global event and immediately triggers a dedicated super-event.

The first public reports establish five facts:

- Prophecies and calculations from unrelated traditions increasingly point toward the same period.
- No single cause or source can explain the convergence.
- A leading predicted date has emerged two to four years in the future.
- The first Doomsday Societies are forming across the world.
- Governments are already losing control of long-term expectations.

The event must not reveal whether the prediction is true. It should not imply that the game has secretly selected a physical disaster. The crisis is driven by belief, organization, and institutional reaction.

The opening applies a global shock through country-scaled effects. It weakens confidence, recruitment, investment, research, education, and long-term construction. Countries with strong institutions, high stability, functioning education, and no severe war pressure absorb the shock better. Countries already damaged by war, famine, occupation, mass death, repeated disasters, or political collapse begin in a worse position.

## Predicted date

The event creates one campaign-specific predicted date between roughly two and four years after the entry event.

The date generation should favor the middle of that range. Extremely short or long results should be less common than dates around two years and nine months to three years and three months after firing.

The date becomes public immediately as the leading consensus. Early movements still dispute the calculation by weeks or months. Evolution I removes most of that ambiguity and turns the date into the accepted Last Day.

The date must persist through save and reload. It cannot reroll because the player reopens a window, changes tag, or triggers a report event.

The date creates natural pacing:

- The early period is dominated by interpretation, government posture, first organizations, and institutional reassurance.
- The middle period is dominated by movement consolidation, economic withdrawal, peace pressure, shelters, reserves, and public representation.
- The final year is dominated by cancelled futures, desertion, settlement growth, government capture, vigils, and emergency preservation of food and records.
- The final month and final week use dedicated report families and stronger decision replacement.

## Public mechanic values

The event exposes exactly two persistent values.

### Doomsday Conviction

Doomsday Conviction is a global value from 0 to 100.

It represents the share and intensity of world belief that the predicted date marks the end of ordinary history. It also reflects whether institutions, movements, soldiers, workers, families, and governments are acting on that belief.

Conviction should rise through public confirmation shocks, local movement success, government admissions, visible abandonment, prolonged war, disasters that fit the prediction, failed reassurance, violent suppression that creates martyrs, and growing international coordination.

Conviction should fall through credible disconfirmation, open evidence, successful institutional continuity, movement scandals, exposed fraud, failed prophecies inside the larger coalition, public recovery, and the arrival of the predicted day without an obvious catastrophe.

The player sees the current level, a short stage name, the recent trend, the next meaningful threshold, and concise causes that can be acted on. The player does not see the full hidden country ledger.

### Time Until the End

Time Until the End shows the exact predicted date and the remaining time.

The public display should use years and months during the early period, months and days during the final year, and days during the final month. The final week should show the exact day count and replace ordinary category text with a short final-week status.

The value is a countdown, not a score. It cannot be increased through routine decisions. The movements may issue revised calculations inside incidents, but the campaign date remains fixed until the failed-date aftermath. One bounded hardliner recalculation can appear later as an aftermath problem.

## Conviction stages

The following are working labels, not final localisation.

| Conviction | Working stage | Public meaning | Main gameplay change |
| ---: | --- | --- | --- |
| `0–14` | Fringe Convergence | The prediction survives mainly in small networks and rumor circles. | Most countries can preserve normal institutions with light intervention. |
| `15–29` | Public Unease | The date becomes common public knowledge and local societies grow. | First response decisions and limited incidents appear. |
| `30–49` | Mass Conviction | Large portions of society act as if ordinary long-term planning may be pointless. | Recruitment, education, investment, and war support face material pressure. |
| `50–69` | Last Days Movement | Doomsday Societies become organized national forces. | Peace pressure, settlement growth, institutional withdrawal, and representation demands intensify. |
| `70–84` | Institutional Withdrawal | Universities, parties, military units, factories, and local authorities lose people to the movement. | Emergency continuity missions and government-capture risks become central. |
| `85–100` | Global Surrender | Much of the world treats the future as politically irrelevant. | Evolution II takeover paths and terminal readiness become much more likely. |

The threshold names should be rewritten during localisation work. Their function is to define readable stages and decision phases.

## Opening Conviction by campaign state

The event should not always begin at the same value.

| Opening state | Suggested global opening band | Design purpose |
| --- | ---: | --- |
| Event fires at Chaos level 4 before either evolution is active | `25–35` | The crisis is established, but governments still have time to shape it. |
| The world is already at 800 or more Chaos and Evolution I is eligible or active before firing | `45–60` | The Last Calendar begins close to public acceptance. |
| The world is already at 1000 or more Chaos and Evolution II is eligible or active before firing | `60–75` | Societies begin organized and politically dangerous, but the terminal route still requires its own proof. |

The exact opening result should consider recent world deaths, active major wars, severe contamination, repeated disasters, existing religious or utopian movements, and institutional collapse. Generic Chaos sources must not be counted again as fresh event-owned Chaos.

## Immediate global consequences

The opening shock should be strong enough to alter national priorities without making ordinary play impossible.

The first package should include:

- A country-scaled reduction in stability and War Support.
- A reduction in recruitable population access or recruitment efficiency that represents refusal, desertion, and delayed mobilization.
- A penalty to research speed or effective research capacity that represents staff and student departure.
- A penalty to construction and long-term industrial investment.
- A penalty to military training and deployment reliability where appropriate.
- A reduction in consumer saving and financial confidence, paired with temporary consumption pressure in some countries.
- A visible national spirit or dynamic modifier that updates by local conditions and global Conviction.
- First-response decisions for every ordinary human country.

The opening must respect playability floors. Research, construction, factory output, and recruitment cannot reach an unavoidable permanent zero before a terminal route is committed.

## Baseline event stages

The baseline uses ordinary progression stages. These stages are not evolution log entries.

### Stage A: Convergence

The date becomes public. Governments choose a posture. Local societies emerge. First incidents focus on rumors, calendars, gatherings, school withdrawal, draft refusal, and speculative spending.

### Stage B: Organization

Movements build relief networks, communes, pilgrimages, prisoner-support organizations, survival settlements, and political committees. Countries begin sustained missions around institutions, reserves, roads, railways, schools, and military rolls.

### Stage C: Society Abandons the Future

Long projects lose labor and finance. Young people leave professional training. Families spend savings. Strategic industries lose workers. Pacifist movements challenge mobilization. Governments decide whether to negotiate, repress, cooperate, or accept the movements as political partners.

### Stage D: Final-Year Crisis

The remaining time becomes the main public horizon. Ordinary decisions are replaced by stronger final-year actions. The most affected countries face local or national government capture. Wars can end, harden, or disintegrate.

### Stage E: Final Month

Mass vigils, temporary closures, final observances, debt jubilees, prisoner releases, demobilization demands, and settlement migration accelerate. Institutions that remain open require active protection and supplies.

### Stage F: The Last Day or The Final Vigil

If the terminal route has activated, the event follows The Final Vigil consolidation.

If the terminal route has not activated, the predicted date arrives, nothing clearly supernatural occurs, and the failed-date aftermath begins.

## Primary gameplay surface

The core response system should use an ordinary decision category with:

- A strong category picture that changes by broad Conviction stage.
- A compact header that shows Doomsday Conviction, trend, exact predicted date, remaining time, and the country’s qualitative posture.
- Three to five primary visible decisions in a normal phase.
- A hard maximum of six primary visible decisions in any one phase.
- One to three active missions.
- Replaced decisions as the date approaches, instead of a growing permanent list.

A full scripted mechanic window is not planned. The two values, one posture, and phased action set can be communicated more clearly through the decision category.

## Country eligibility

Ordinary human countries use the response system.

Countries classified by `uses_normal_civilian_systems` should be the default eligible set. Actual nonhuman actors and special system countries that cannot meaningfully experience civilian belief, education, family savings, or religious and political organization should not receive the ordinary package.

Doomsday administrations remain human countries. They do not become special Chaos countries or actual nonhuman countries.

## Player agency

The player cannot prove or disprove the prediction through one button.

The player can shape:

- How much open organization the societies retain.
- Whether state institutions cooperate with or confront trusted religious and civic networks.
- Whether armies are kept together through legitimacy, coercion, concessions, or demobilization.
- Whether wars are ended, continued, or accelerated.
- Whether reserves, shelters, records, education, and logistics survive the countdown.
- Whether the country remains a normal government, becomes a custodial Doomsday administration, or joins the Final Assembly.
- How severe the failed-date reconstruction becomes.

No route should be universally optimal. Repression gives short-term control and long-term backlash. Cooperation preserves order but shares legitimacy. Denial can sustain institutions when credible and collapse badly when contradicted. Preparation can protect the population but can also validate the belief. Pacifist concessions can end ruinous wars and leave a country vulnerable to aggressive holdouts.

## AI experience

AI countries must make posture and action choices based on campaign state.

The main factors are:

- Stability and War Support.
- War status, war direction, casualties, and enemy pressure.
- Government ideology and coercive capacity.
- Religious and civic institutional strength.
- Local movement composition.
- Industrial and educational resilience.
- Existing famine, migration, disaster, contamination, or occupation pressure.
- Remaining time.
- Global and local Conviction.

The AI should change posture only when a major shock or threshold makes the old posture untenable. It should not oscillate monthly between denial, cooperation, and repression.

## Core non-negotiables

- The event remains a Major event at Chaos level 4.
- The event exposes only two persistent public values.
- The predicted date is dynamic, public, persistent, and usually two to four years away.
- No physical apocalypse is secretly guaranteed by the event.
- The Last Day and The Final Vigil are separate outcomes.
- The Final Vigil requires 1000 or more Chaos and event-owned readiness.
- The event does not automatically white-peace every war.
- The event does not create dozens of new country tags.
- Doomsday administrations remain human countries.
- The event uses no custom unit or 3D model package.
- The event has no event-owned full scripted mechanic window.
- Evolution activation itself gives zero Chaos.
- Generic war, peace, death, contamination, famine, migration, annexation, and nuclear Chaos sources are not counted twice.
- The failed date receives a full aftermath and reconstruction loop.
