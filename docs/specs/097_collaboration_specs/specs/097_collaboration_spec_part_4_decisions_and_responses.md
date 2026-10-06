# Event 097 Collaboration: Part 4, Decisions and Responses

## Design limit

The brief rules out a Collaboration currency and a large event-specific management system. The decision layer respects that. It adds no meter and no new resource. Every action either changes the native collaboration value, changes how strongly the evolutions read it, or spends ordinary resources to protect the state. Two small categories cover the whole event, each with a handful of phased actions.

| Category | Working label | Who sees it | Purpose |
| --- | --- | --- | --- |
| Host category | Divided Loyalties | A participant at war with another participant, with Event 097 networks inside it, while at least one of its actions is visible or one of its measures is running | Defend the state apparatus against the enemy networks inside it |
| Installer category | Prepared Governments | A participant while Collaboration Governments is active, when it has a valid target or holds a government installed through this route | Install and sustain prepared governments |

Neither category exists at peace for a country with no active installed government. Peace is when the opening report's stance choice is the country's tool.

Category visibility and decision targets come from markers and lists that the event's own hooks update at the moment something changes: a capture, a seat, a capitulation, an exile, an installation, or a war ending. No category or decision searches every country to decide whether to show itself.

Both categories hide while the Fallout transition is running or Fallout is active.

## Presentation choice

### Divided Loyalties

This category is a simple category: a short description, one compact status block written as category text, and an ordinary list of decisions. It passes the picture eligibility gate and receives a static category picture. A full scripted GUI would add nothing, because the player manages no list of targets and no value beyond the qualitative readings and the Fifth Column band.

The category text shows, in this order:

- Foreign networks among us, as the qualitative band from Part 1
- the Fifth Column band and the country with the strongest network inside us, only while the Fifth Column is active, with a short note when our measures are holding the band down
- the names of the measures currently running, on one short line, only while at least one runs

Remaining days are not repeated in the text, because the running spirit and decision rows already show their own timers. The text must read as intentional game text, without pipes, divider rows, or raw variable names.

Picture direction: a period scene of a ministry corridor or district office at night, where a few officials work by lamplight while one figure at the end of the corridor waits by a door. The picture should suggest divided loyalty through posture and light, not through paperwork as the main subject, and it must not paint any buttons, meters, or text. It follows the decision-category picture reference family named in the asset prompt.

### Prepared Governments

This category is an ordinary category with its icon and a concise description. It does not receive a picture because its content is a short targeted list. It never shows more than six rows: B2 rows appear only for governments where B2 can be taken now, and if valid B1 targets and B2 rows would still pass six, the rows for the targets with the fewest controlled cores are hidden first.

## Divided Loyalties decisions

### Actions

| Action | Working label | Visible when | Effect | Costs | Duration and cooldown |
| --- | --- | --- | --- | --- | --- |
| A1 | Loyalty Commissions | At war, and Administrations in Waiting or The Fifth Column is active, or a participant enemy controls one of our cores. Hidden while the Fifth Column is at Defecting or Collapsing. | Starts the wartime form of the vetting spirit. While it runs, our surrender limit rises a little, seats against us gain half as much compliance, the Fifth Column counts one band lower, Open Gates timers started during it run twice as long, and if we capitulate, every occupier's compliance in our cores is reduced (below). The surrender limit change has an anchor of 5 percent, sized after the engine's collaboration surrender define is verified, so that A1 matters in wars before Administrations in Waiting and The Fifth Column. | Political power, and stability and consumer goods through the spirit | Runs 180 days. Available again 90 days after it ends. |
| A2 | Arrest the Prepared Officials | Administrations in Waiting is active and a participant enemy holds at least one seated state of ours | Subtracts 15 points from that enemy's collaboration inside us, never below zero. Targets the seating enemy with the strongest network, then the one holding the most seated states, then a random one among equals. The tooltip names that enemy and its band. | Manpower for police and gendarmerie, infantry equipment, political power | Available again 120 days after use |
| A3 | Evacuate the Ministries | The Fifth Column is at Defecting or Collapsing | The Fifth Column counts one band lower and Open Gates cannot happen for 120 days | Trains, or trucks when the country lacks the trains, plus a timed factory output penalty and political power | Runs 120 days. Available again 180 days after it ends. |
| A4 | Commissars in the Ministries | The Fifth Column is at Defecting or Collapsing | Removes the factory output and recruitment penalties of the Fifth Column for 90 days and suspends Open Gates for the same period | Command power, army experience, and a timed stability penalty | Runs 90 days. Available again 180 days after it ends. |
| A5 | Charter a Government in Exile | Collaboration Governments is active, we have not capitulated, we are not a subject or an installed government, and we are past 40 percent surrender progress or a participant enemy with at least a Widespread network controls our cores | Raises the installation threshold against us by 10 until the war ends, and raises the starting restoration pressure of any government installed over us anyway. The tooltip says in plain words that a foreign power will need a deeper network here to install a government over us. | Political power, plus convoys for a country with a coastline or trucks overland for a landlocked country | Once per war |

An action that is running or waiting to become available again is not shown as a button, and the category text names the running measures instead. A1 and A3 never stack beyond one band in total, because both represent removing collaborators from contact with the enemy. A3 and A4 stack because they address different parts of the column.

### Rows by situation

| Situation | Rows at most |
| --- | --- |
| At war, an enemy controls our cores or Administrations in Waiting is active, no Fifth Column | A1, A2, A5, so three |
| Fifth Column at Wavering | A1, A2, A5, so three |
| Fifth Column at Defecting or Collapsing | A2, A3, A4, A5, so four |

The category therefore never shows more than four actions.

### Strength

Effects must be strong enough to change the outcome of a war on the margin. A1 or A3 drops a Collapsing host to the Defecting band, and A4 then keeps the factories and recruitment offices running. Together they can be the difference between capitulating this month and holding out for a season.

When a measure lowers a Wavering host by one band, the Fifth Column spirit stays in place for records with no modifier values, and Open Gates cannot start.

### Raw and effective band

The Fifth Column has a raw band from surrender progress and an effective band after A1 or A3. Each consumer reads one of them:

| Reads the raw band | Reads the effective band |
| --- | --- |
| A3 and A4 visibility, A1 hiding, and the dynamic costs | The spirit's modifier values |
| The highest band recorded for the war | Open Gates eligibility and timing |
| The Evolution IV installation threshold | The larger seat compliance under an active Fifth Column |
| Achievements | The band shown in the category text, with the note that measures are holding it down |

### A1 at capitulation

If a country with Loyalty Commissions running capitulates, a hidden follow-up runs one day later, after the engine has converted collaboration into compliance. For each participant enemy that still controls our cores when the follow-up runs, it subtracts compliance from each of those states by that enemy's network band, never below zero: 5 for Established, 12 for Widespread, and 20 for Pervasive. States that changed hands during the delay are skipped. The one-day delay makes the result independent of the order in which the engine and the capitulation hooks run.

### How reductions work

A2 and the Purge option subtract a fixed number of points from the current native value, whatever produced it, and never go below zero. Event 097 never overwrites the native value with an absolute number that ignores its current level.

The implementation must verify that a negative collaboration change stops at zero. Purge depends on that behavior, because it runs after the state has changed hands and the enemy may no longer occupy any of our cores, so no value is left to read. If the engine does not stop at zero, the implementation reports a blocker for Purge and A2. Setting the value to the current reading minus the points, read in an occupation context, is a candidate route for A2 that needs the user's approval before use.

The Foreign networks among us reading describes every foreign power together, so it does not fall after A2 or Purge, which act on one enemy. The A2 tooltip names the targeted enemy's current band, read while it controls our cores. The Collaborators Unmasked text names the band recorded when its administration was seated, and says that the network has been cut back if Purge is chosen.

### Dynamic costs

Costs are quoted through the shared universal cost framework, so cost-changing effects from other events, such as Event 026 sales, apply to them as they do elsewhere. Costs scale with the country and the situation. The minor anchor applies to a country with few core states and the major anchor to a country with many, with a linear scale between two core-state counts kept in the constant group. All anchors live in one constant group.

| Action | Small country anchor | Large country anchor | Situation factor |
| --- | --- | --- | --- |
| A1 | 25 political power, 10 percent stability, 10 percent consumer goods | 50 political power, same spirit values | none, because A1 is hidden at Collapsing |
| A2 | 5,000 manpower, 500 infantry equipment, 25 political power | 15,000 manpower, 1,500 infantry equipment, 50 political power | Manpower falls by a third when the enemy holds a Pervasive network, because the officials are easy to find |
| A3 | 10 trains or 300 trucks, 15 percent factory output for 120 days, 25 political power | 20 trains or 600 trucks, same output penalty, 50 political power | Political power cost falls by 10 at Collapsing |
| A4 | 25 command power, 25 army experience, 10 percent stability for 90 days | 40 command power, 50 army experience, same stability | Command power cost never exceeds 60 |
| A5 | 50 political power, 5 convoys or 100 trucks | 100 political power, 15 convoys or 300 trucks | none |

Every action stays within four spendable cost types, and every displayed cost uses its correct texticon with at most three inline values. A3 shows only the transport it will actually take: trains when the country holds enough, otherwise trucks. The A3 factory output penalty has no texticon of its own, so it appears as the decision's timed modifier in the effect tooltip and still counts as a cost type. A5 shows only convoys for a country with a coastline and only trucks for a landlocked country.

The timed penalties of A3 and A4 always run their full duration, even if the Fifth Column ends earlier. Their protective effects end with the Fifth Column. A host close to peace therefore cannot take A3 for its protection and lose its price.

### Stability floor

A1 and A4 share one stability requirement of at least 20 percent, a tuning anchor that applies to human and AI countries alike. The blocked tooltip names it. It is lower than the 30 percent Screen requirement on purpose: Screen is a choice made in calmer times for a campaign of four to six months, while A1 and A4 are wartime emergency measures that must stay usable when the state is already shaken. The Purge penalty is one timed spirit that is refreshed, not stacked, when another Purge happens during it.

### Vetting spirit lifecycle

The Screen stance in the opening report and the A1 decision share one spirit family, so the host never carries two vetting spirits.

| Form | Source | Effects | Next form |
| --- | --- | --- | --- |
| Vetting Campaign | Screen stance | Stability and consumer goods costs from Part 1, incoming layer halved for the current firing | Upgraded to Loyalty Commissions by A1, or expires |
| Loyalty Commissions | A1 | Wartime effects in the table above with their costs | Expires after 180 days, or falls back to Vetting Campaign (below) |

Taking A1 while a Vetting Campaign runs replaces it with Loyalty Commissions and restarts the duration. Choosing Screen while Loyalty Commissions runs keeps the commissions and extends the spirit so that at least the full Vetting Campaign duration remains. When the commissions end, the remaining time continues as a Vetting Campaign. Screen therefore always costs its full price.

### Collaborators Unmasked

This is an event choice rather than a decision. It appears when Administrations in Waiting is active and the owner or an ally retakes a state where an enemy administration had been seated. It appears at most once per war for each owner and enemy pair, and never during or after the Fallout transition.

| Option | Working label | Effect | Cost |
| --- | --- | --- | --- |
| Purge | Make examples of them | Subtracts 10 points from that enemy's collaboration inside us, never below zero | A timed 10 percent stability penalty for 90 days |
| Amnesty | Keep the offices working | The enemy's network stays in place, and the retaken state receives a 90-day state modifier that raises its local factory output and recruitable population, because the experienced officials stay at their desks | None |

Option direction: the purge option is the voice of a returning government that wants visible punishment. Its grim irony can point at the speed with which the same officials now denounce each other. The amnesty option is cold pragmatism: the trains must run and there is nobody else who knows how. Neither option may make light of reprisals against civilians.

## Prepared Governments decisions

The category appears only while Collaboration Governments is active and enabled.

| Action | Working label | Target | Visible when | Available when | Effect | Costs |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Seat the Prepared Government | A participant that has capitulated or whose government is in exile | We are not a subject and not an installed government. We can use the installation route resolved in Part 3. We are at war with the target, or the target's government is in exile while we control its cores. We control at least one of its cores. No living collaboration government exists for its original tag, whether installed through Event 097 or through vanilla. The original tag is not under its reinstallation cooldown. | Our network inside the target meets the Part 3 installation threshold, average compliance in its cores we control meets the ladder below, and our installation cooldown has passed | Installs a prepared government through the Part 3 route | Political power, plus infantry equipment and manpower for the auxiliaries |
| B2 | Arm the Installed Administration | One of our living governments installed through this route | The government is our subject, has uses left, is past its waiting time, and is Imposed or Contested or has an enemy on its territory | Costs are payable | The government raises two more auxiliary divisions. In the Imposed stage it also moves 90 days closer to the Entrenched stage. In other stages it only raises the divisions. | Infantry equipment and manpower for two divisions, political power |

The B1 tooltip names the current average compliance in the target's cores we control, the compliance required, and whether our network is deep enough, as a band word. These are requirements the player acts on, so they are shown. The ladder and threshold formulas stay out of the text.

### Compliance ladder

The vanilla collaboration-government route needs 80 percent average compliance. B1 needs less when the network is deep. The ladder is kept in the constant group:

| Our network inside the target | Average compliance required |
| --- | --- |
| 60 points or more | above 50 percent |
| 50 to 59 points | above 55 percent |
| 40 to 49 points | above 60 percent |
| 25 to 39 points | above 67 percent |

A network below 25 points never meets the installation threshold, so it never reaches the ladder. Collaboration is stored by the engine on a 0 to 1 scale, and the points in this file are that value times 100. Compliance is read on its 0 to 100 scale in the target cores we control. While the war against the target runs, the threshold uses that war's Collapsing and charter modifiers from Part 3. Against a government in exile after the war has ended, the ordinary threshold applies.

### Auxiliary costs

The price of every auxiliary division equals what one division of the auxiliary template from Part 3 needs, in infantry equipment and manpower, read from constants that mirror that template. The installer pays for what the division holds. The implementation verifies how spawned divisions are equipped. If they spawn without equipment, the paid equipment is sent to the government's stockpile instead.

| Action | Anchor | Scaling |
| --- | --- | --- |
| B1 | 50 political power, plus the template's equipment and manpower for each auxiliary division the government will receive | Political power rises by 25 for each government this installer has installed through this route in the last three years, living or not, so annexing a government does not reset the price. The paid manpower leaves the installer's pool. If spawned divisions draw on the government's own manpower, the paid manpower is added to the government's pool first. |
| B2 | 25 political power, plus the template's equipment and manpower for two divisions | Usable once every 180 days per government and at most three times per government |

### Limits

- B1 has a 180-day cooldown per installer, stored on the installer.
- One living collaboration government per original tag at any time, regardless of installer or route.
- An original tag whose installed government ended cannot receive a new one through B1 or the capitulation offer for 365 days.
- B1 and the Part 3 capitulation offer share the same installation helper and the same registry, so neither route can bypass the other's limits.
- B2 uses are counted on the registry row and cleared when the row retires.

## AI behavior for the decisions

Weights belong to the probability matrix and must be audited. Decision weights use MTTH-backed entries, one per action, so the inputs below stay in one tuning place. Collaborators Unmasked follows matrix surface S4.

### Divided Loyalties

- A1 has zero weight unless a participant enemy controls our cores or our surrender progress is past 10 percent. Outside an active Fifth Column it is taken at most once per war.
- A country at war whose foreign networks reading is Widespread or Pervasive takes A1 early in the war, before the Fifth Column appears.
- A country at Defecting or Collapsing takes A3 first, then A5 when the A5 rule below is met, then A4 when it has the command power, then A2.
- A2 is taken when the seating enemy holds a Widespread or Pervasive network and the country's available manpower is at least twice the action's manpower cost.
- A5 is taken by a country with allies still at war, or by one whose ruling ideology differs from that of the likely installer. The likely installer is the participant enemy that controls our cores, holds the highest band, and can install through the resolved Part 3 route. A country that shares that enemy's ideology group and has no allies at war skips A5. A democracy weighs A5 higher than other ideologies.
- Installed governments use A1 to A4 like any other country. A5 is hidden for them.

### Prepared Governments

- An AI takes B1 when it is not itself past 40 percent surrender progress and it controls at least three cores of the target, which would otherwise need large garrisons, or all of the target's cores when the target has fewer than three. Rows hidden by the six-row limit are hidden for the AI too, and the limit hides the targets the AI values least. Among several valid targets, it prefers the one where it controls the most cores, then the one with the highest average compliance.
- An AI prefers B1 over direct occupation when it is fighting on several fronts and needs its garrisons elsewhere.
- An AI that already holds three governments through this route takes B1 only for targets on its own continent.
- An AI takes B2 when one of its installed governments is Contested or faces an enemy on its territory.
- A democratic AI uses the same logic at reduced weight, reflecting political reluctance rather than an ideology lock, if the resolved Part 3 route lets democracies install at all.

## Decision cleanup

- Divided Loyalties hides when the country is at peace with every participant enemy. Running spirits and timed modifiers run to their end.
- The A2 target clears when no enemy holds a seated state of ours.
- A3 and A4 hide when the Fifth Column falls below Defecting or ends. Their penalties finish their duration.
- A5 resets when the war ends, using the war-scoped guard rules in Part 3.
- Prepared Governments hides when Collaboration Governments is disabled. B2 targets clear when a government stops existing, becomes independent, or turns to a rival.
- During the Fallout transition and after it, both categories hide, A2 and Purge never write, Collaborators Unmasked does not fire, and B1 and B2 are unavailable. Running spirits and timed modifiers expire on their own timers.

### Evolution disabled after activation

| Evolution disabled | Result in this part |
| --- | --- |
| Administrations in Waiting | A2 hides, no new seats form, and Collaborators Unmasked stops. Existing seats keep their lowered resistance target until the state changes controller, because the administration already sits in place. |
| The Fifth Column | The spirit is removed at its next evaluation, A3 and A4 hide, A1 loses its band and Open Gates effects, and the band line leaves the category text |
| Collaboration Governments | A5 and the Prepared Governments category hide, and B2 counters stop changing |

Running spirits and timed modifiers from the disabled evolution expire on their own timers.

## Exploit checks

| Risk | Guard |
| --- | --- |
| Farming compliance by recapturing the same state | 180-day seat guard per state and controller |
| Repeating Collaborators Unmasked | Once per war per owner and enemy pair |
| Stacking band reductions | A1 and A3 together reduce at most one band |
| Chain-installing governments everywhere | Political power cost that counts installations over three years, 180-day installer cooldown, one government per original tag |
| Install, annex, and reinstall for the same country | 365-day reinstallation cooldown per original tag, installations counted for three years, and the installation Chaos row limited to once per original tag per war |
| Using B2 as a free unit loop | The price equals what the divisions hold, with a cap of three uses per government |
| Screen stance as a free shield | The vetting spirit costs stability and consumer goods for months, and Screen during Loyalty Commissions extends the spirit instead of costing nothing |
| Taking A3 near peace for free protection | A3 and A4 penalties always run their full duration |
| Stacking stability penalties into collapse | Shared stability floor for A1 and A4, and one refreshed Purge penalty |
| Cultivate as a free advantage | Incoming layer rises by a quarter, which makes the cultivator easier to defeat in its own wars |
| Clicking A2 against an enemy with no meaningful network | Visible only while an enemy holds a seated state of ours, so the action always targets an exposed network |
