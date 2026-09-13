# Event 049 Doomsday Specification

## Part 2: Simulation Model

## Simulation purpose

The event should feel globally connected without asking the player to manage a world spreadsheet.

The simulation uses hidden country and movement state to create local variation, then summarizes the world through Doomsday Conviction and the countdown. Each hidden value must feed a visible consequence, an AI choice, an event condition, or a recovery result.

## Public and hidden state

| State | Visibility | Function |
| --- | --- | --- |
| Doomsday Conviction | Persistent public value | Summarizes global belief and action. |
| Time Until the End | Persistent public value | Shows the predicted date and countdown. |
| Country local conviction | Hidden numeric state | Determines national pressure and contribution to the global value. |
| Society organization | Hidden numeric state | Measures the capacity to mobilize, distribute aid, resist suppression, and capture institutions. |
| Society current shares | Hidden composition | Determines the character of local demands and government takeover. |
| Government posture | Public qualitative state | Shows the chosen policy without adding a third meter. |
| Suppression backlash | Hidden numeric state | Stores resentment, martyr effects, underground growth, and future revolutionary risk. |
| Institutional continuity | Hidden numeric state | Measures how well education, logistics, records, administration, finance, and command survive. |
| Peace pressure | Hidden war-linked state | Drives truce demands, refusal, mutiny, and demobilization. |
| Terminal readiness | Hidden global and country state | Determines whether one of the Final Vigil paths has matured. |
| Public trust trend | Hidden input with qualitative tooltip output | Helps resolve denial, reassurance, and failed-date legitimacy. |

No additional persistent number should be placed in another category, tooltip, national spirit, focus inlay, or Event Details panel.

## Country local conviction

Every eligible country has a hidden local conviction state.

Local conviction represents the share and intensity of social belief inside that country. It should not be a direct copy of global Conviction.

Local conviction rises through:

- Severe casualties, prolonged war, and repeated mobilization failures.
- Famine, mass displacement, occupation, disaster, contamination, or social collapse that movements can interpret as confirmation.
- Trusted local religious, communal, pacifist, or prophetic networks.
- Visible government admissions or Last Days policies.
- Successful society relief, organization, prisoner support, and settlement building.
- Public violence against peaceful groups when it creates martyrs.
- Institutional abandonment that makes the prediction appear self-fulfilling.
- Neighboring country takeovers and major-power demobilization.

Local conviction falls through:

- Credible public evidence and open access to records.
- Successful continuity missions that keep schools, railways, hospitals, administration, and military rolls functioning.
- Movement fraud, corruption, leadership scandal, or failed local predictions.
- Peaceful public debate that prevents underground mythmaking.
- Improved security and recovery from the crises that movements used as proof.
- The predicted date passing without an obvious catastrophe.

Local conviction should move gradually during ordinary months and sharply after major incidents. A country should not jump from low belief to government collapse because one small report fired.

## Global Conviction aggregation

Global Conviction is a weighted aggregate of eligible country local conviction, global confirmation shocks, international movement coordination, and major political milestones.

Country weights should be bounded.

Population and major-power status can increase a country’s influence, but no single populous state should control most of the global meter. A coalition of small and medium countries must be able to alter world belief when they adopt the same policy or produce a visible international movement.

A useful design shape is:

- Every eligible country contributes a base share.
- Population tier increases its share within a cap.
- Major powers receive a limited additional share.
- Countries with no functional government or no normal civilian system contribute through special event rules or are excluded.
- Global shocks are capped and decay after their effect has entered country conviction.

The final implementation should be tested against cases where one major remains skeptical while many smaller countries convert, and where one very populous major converts while most of the world remains skeptical.

## Cross-feed between local and global belief

The relationship works in both directions.

A high global value raises local pressure because the prediction appears internationally confirmed. Strong local movement success raises the global value because foreign societies cite it as evidence.

The cross-feed must be damped. It cannot create an uncontrolled daily feedback loop.

Recommended behavior:

- Local conviction contributes to the global aggregate on a bounded monthly or scheduled cadence.
- Global Conviction applies a smaller monthly pressure to local conviction.
- Major global incidents create one-shot changes with per-source guards.
- Threshold crossing events can create additional one-time movement organization.
- The same incident cannot add global Conviction directly, add every country local conviction, and then be counted again as a fresh global confirmation without a cap.

## Conviction trend

The public display should show a qualitative recent trend, such as falling, stable, rising, or surging.

This qualitative trend derives from recent changes in Doomsday Conviction and does not count as a third value.

The tooltip should name a small number of major current causes. It should prefer actionable causes, such as war losses, failed continuity missions, successful public evidence, international takeovers, or major disaster confirmation.

It should not expose a full component ledger.

## Movement organization

Organization measures whether local societies can turn belief into durable action.

A country can have high conviction and low organization. In that case, panic and withdrawal are common, but the movement cannot easily administer food, coordinate strikes, negotiate a truce, or replace government.

A country can have moderate conviction and high organization. In that case, a disciplined pacifist, religious, communal, or survivalist network can exert more political pressure than raw belief suggests.

Organization rises through:

- Open meetings and legal recognition.
- Relief distribution and shelter management.
- Prisoner support and legal defense.
- Clerical, labor, communal, veteran, or municipal networks.
- Shared calendars, congresses, pilgrimages, and international communication.
- Government partnership that delegates practical duties.
- Suppression that fails to destroy decentralized networks.

Organization falls through:

- Exposed financial fraud or violent internal conflict.
- Arrest of genuinely central leaders when the movement is highly centralized.
- Loss of supplies, routes, meeting places, and trusted institutions.
- Failed missions and public disorder.
- The passing of the predicted date when no coherent reinterpretation remains.

Organization is internal. The player sees its effects through decision availability, movement status, event outcomes, and takeover risk.

## Society current composition

Every country’s movement has hidden shares among several currents. Intermediate calculations can normalize these shares before selecting stable dominant and secondary currents.

The core current set is:

- Pacifist
- Prophetic and calendar-centered
- Devotional and penitential
- Survivalist
- Communal
- Ascetic
- Hedonist
- Apocalyptic state-loyalist
- Revolutionary and avenging
- Skeptical continuity networks

The dominant current affects decisions, incidents, AI pressure, government-capture form, Final Assembly representation, and failed-date response.

Secondary currents create mixed outcomes. A pacifist movement with strong communal support behaves differently from a pacifist movement dominated by hedonist withdrawal or revolutionary anger.

The current model must avoid equating a religion, ideology, country, or culture with one fixed current. Current weights come from campaign conditions and institutions.

## Government posture state

Each country selects one main posture. The posture is a qualitative policy state and does not count as a persistent mechanic value.

Postures affect local conviction, organization, institutional continuity, peace pressure, available decisions, and AI strategy.

The posture should have a minimum commitment period, with one expensive emergency change after a major shock and no monthly oscillation.

The working posture labels are defined in Part 3.

## Suppression backlash

Suppression backlash stores the difference between visible control and underlying resistance.

A crackdown can lower open organization and reduce visible gatherings. It can also increase hidden conviction, create prisoners and martyrs, move networks underground, worsen Condemnation when atrocities occur, and strengthen revolutionary currents.

Backlash should be strongest when:

- The movement was peaceful and publicly respected.
- State violence causes real deaths.
- Religious, municipal, veteran, or labor institutions are attacked.
- Authorities destroy food, shelters, records, or relief routes.
- The state repeatedly claims success while the movement continues.
- Foreign governments or international organizations publicize the repression.

Backlash should be weaker when:

- The target is a proven violent cell.
- The state uses bounded legal action and public evidence.
- Authorities preserve relief networks and religious observance.
- Courts remain credible.
- The movement is already divided by exposed fraud.

Backlash feeds Evolution II revolutionary takeovers and the Avenging Witnesses current inside the Final Assembly.

## Institutional continuity

Institutional continuity measures whether the country preserves the capacity to function after the date.

It combines hidden state from:

- Schools, universities, technical institutes, and research establishments.
- Civil-service records, courts, archives, tax systems, and local administration.
- Railways, ports, supply depots, food distribution, and communications.
- Military rolls, officer schools, maintenance units, and command legitimacy.
- Financial records, savings, debt administration, insurance, and contracts.
- Hospitals, sanitation, shelters, and emergency reserves.

Continuity rises through missions that keep these systems staffed and supplied. It falls through closure, abandonment, seizure, destruction, corruption, and unplanned demobilization.

The player should not see a continuity number. The decision category can show a short country status such as functioning, strained, fragmented, or hollowed out. Tooltips should connect the status to current missions and consequences.

Continuity determines:

- How severe the countdown penalties become.
- Whether a country can resist government capture.
- The quality of a voluntary Doomsday administration.
- The speed and cost of failed-date reconstruction.
- Whether shelters and reserves remain useful after the crisis.
- Whether military and research institutions can be recalled.

## Peace pressure

Peace pressure is stored by belligerent and linked to each relevant war.

It is calculated from:

- Global and local Conviction.
- Time remaining.
- War duration and recent casualties.
- Current War Support.
- Mobilization strain and desertion.
- Territorial direction and perceived chance of survival.
- War type and public interpretation.
- Government posture.
- Pacifist organization.
- Enemy willingness to negotiate.

The player sees peace pressure through missions, incidents, unit refusal, public demands, and negotiation availability. It should not become a third public meter.

## Terminal readiness

Terminal readiness is a hidden event-owned state.

It records whether enough political, social, military, and international proof exists for The Final Vigil, independently from global Conviction.

Readiness can mature through several paths:

- A broad voluntary transfer of government authority.
- Sustained overwhelming Conviction.
- Major-power demobilization and Final Assembly membership.
- International pacifist capture of military authority.
- Suppression-driven cascading revolution.

Each path has its own proof and sustained period. The Final Vigil can use the first completed path or a combination of partial paths.

## Confirmation and disconfirmation shocks

The event can interpret other campaign events as confirmation or disconfirmation.

Examples include:

- A major asteroid warning, strange astronomical event, or catastrophic impact.
- A global plague, zombie crisis, Death expansion, or other visible existential threat.
- Severe natural-disaster seasons.
- High Air Contamination or nuclear winter.
- A Holy Realm or utopian movement that adopts or rejects the date.
- A respected scientific institution exposing a fabricated sign.
- A public prediction by one society failing before the Last Day.

Every source family must use a one-shot or bounded guard. A repeated event cannot farm Conviction indefinitely.

The event should react to visible campaign state. It should not claim that every disaster is secretly caused by the prophecy.

## Time pressure bands

The countdown changes hidden rates and available content.

| Remaining time | Main pressure |
| --- | --- |
| More than two years | The main struggle concerns credibility, organization, and long projects. |
| One to two years | Settlement growth, investment withdrawal, recruitment resistance, and shelters become more important. |
| Six to twelve months | Peace pressure and institutional closure accelerate. Final-year missions replace early actions. |
| One to six months | Governments face direct demands to release prisoners, distribute reserves, forgive debts, or demobilize. |
| Eight to thirty days | Mass vigils, closures, family movement, and local authority transfer dominate. |
| Seven days or less | Final-week presentation and emergency preservation actions replace ordinary policy work. |

## Update cadence

The simulation should avoid broad daily world scanning.

Use bounded registered country sets, event-owned scheduled pulses, existing on-action hooks, or country-local processing. The planning requirement is behavioral, not a command to use a specific script structure.

Recommended cadence:

- The countdown display derives from the persistent target date.
- Country local conviction and organization update on a bounded monthly or scheduled pulse.
- Major incidents create immediate one-shot changes.
- Peace pressure updates less often than daily unless a war incident requires immediate response.
- Final-month and final-week sequences use scheduled events and add no new global daily loop.

## Save, reload, and tag-switch behavior

The following state must persist:

- The predicted date.
- Global Conviction.
- Country local conviction.
- Country posture and commitment cooldown.
- Movement organization and dominant currents.
- Institutional continuity.
- Suppression backlash.
- Active country and war missions.
- Evolution state and enable state.
- Terminal path progress.
- Final Assembly membership and dominant current.
- Failed-date aftermath state.

The player’s event category must rebuild correctly after tag switching. Country-specific actions must use the new player country’s state without changing the global date or rerolling the event.

## Cleanup

Cleanup depends on outcome.

After an ordinary failed date, temporary countdown decisions, final-week missions, acute Conviction modifiers, and terminal readiness should be removed or converted into aftermath state. Residual movements, scars, shelters, debt effects, and institutional recovery may persist.

After The Final Vigil, incompatible ordinary event firing stops under the shared world-end contract. Event-owned consolidation content remains allowed until the terminal state is established.

If a country becomes invalid, annexed, nonhuman, or otherwise unable to use normal civilian systems, its ordinary country response state should be removed or frozen safely without corrupting the global aggregate.

## Debug and audit visibility

The normal player should not see hidden ledgers.

Debug or audit tools should be able to inspect:

- Local conviction.
- Country weight in the global aggregate.
- Movement organization.
- Dominant and secondary current.
- Posture and posture lock.
- Backlash.
- Institutional continuity.
- Peace pressure by war.
- Terminal readiness path progress.
- One-shot confirmation guards.

This evidence is needed for balancing and probability audits. It should not become ordinary localisation.
