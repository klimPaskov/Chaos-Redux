# Event 097 Collaboration: Part 4, Decisions and Responses

## Design limit

The brief rules out a Collaboration currency and a large event-specific management system. The decision layer respects that. It adds no meter and no new resource. Every action either changes the native collaboration value, changes how strongly the evolutions read it, or spends ordinary resources to protect the state. Two small categories cover the whole event, each with a handful of phased actions.

| Category | Working label | Who sees it | Purpose |
| --- | --- | --- | --- |
| Host category | Divided Loyalties | A participant at war with another participant, after Event 097 has added networks inside it | Defend the state apparatus against the enemy networks inside it |
| Installer category | Prepared Governments | A participant while Collaboration Governments is active, when it has a valid target or holds a government installed through this route | Install and sustain prepared governments |

Neither category exists at peace for a country with no active installed government. Peace is when the opening report's stance choice is the country's tool.

## Presentation choice

### Divided Loyalties

This category is a simple category: a short description, one compact status block, and an ordinary list of decisions. It passes the picture eligibility gate and receives a static category picture. A full scripted GUI would add nothing, because the player manages no list of targets and no value beyond the two qualitative readings and the Fifth Column band, all of which fit in the category text.

The category header shows, in this order:

- Foreign networks among us, as the qualitative band from Part 1
- the Fifth Column band and the country with the strongest network inside us, only while the Fifth Column is active
- the active protective measure and its remaining days, only while one is active

The header must read as intentional game text. It must not use pipes, divider rows, or raw variable names.

Picture direction: a period scene of a ministry corridor or district office at night, where a few officials work by lamplight while one figure at the end of the corridor waits by a door. The picture should suggest divided loyalty through posture and light, not through paperwork as the main subject, and it must not paint any buttons, meters, or text. It follows the decision-category picture reference family named in the asset prompt.

### Prepared Governments

This category is an ordinary category with its icon and a concise description. It holds at most two visible decisions per target. It does not receive a picture because its content is a short targeted list.

## Divided Loyalties decisions

The category shows at most four actions at once. Actions appear in phases so that a country at war only sees what fits its situation.

| Action | Working label | Phase | Visible when | Effect | Costs | Duration and cooldown |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Loyalty Commissions | Wartime | Always while the category is visible | Upgrades or starts the vetting spirit to its wartime form. While active, seats against us gain half as much compliance, the Fifth Column counts one band lower, Open Gates timers run at half speed, and at our capitulation every occupier's capitulation compliance is reduced by a quarter of its collaboration inside us | Political power, stability and consumer goods through the spirit | 180 days, then a 90-day cooldown |
| A2 | Arrest the Prepared Officials | Wartime, Administrations in Waiting active | A participant enemy currently holds at least one seated state of ours | Reduces that enemy's collaboration inside us by 15 points, never below zero | Manpower for police and gendarmerie, infantry equipment, political power | 120-day cooldown per enemy |
| A3 | Evacuate the Ministries | Fifth Column active on us | The Fifth Column spirit is active | The Fifth Column counts one band lower and Open Gates cannot happen for 120 days | Trains or trucks for moving departments, a temporary factory output penalty through a timed modifier, political power | 120 days, then a 180-day cooldown |
| A4 | Commissars in the Ministries | Fifth Column active on us | The Fifth Column spirit is at Defecting or Collapsing | Removes the factory output and recruitment penalties of the Fifth Column for 90 days and suspends Open Gates for the same period | Command power, army experience, stability through a timed modifier | 90 days, then a 180-day cooldown |
| A5 | Charter a Government in Exile | Exile, Collaboration Governments active | We are past 40 percent surrender progress, or an enemy with a Strong network occupies part of our territory | Raises the installation threshold against us by 10 for this war, and raises the starting restoration pressure of any government installed over us anyway | Political power, convoys carrying ministers, archives, and reserves abroad | Once per war |

Effects must be strong enough to change the outcome of a war on the margin. A1 and A3 together can drop a Collapsing host to Wavering, which is the difference between capitulating this month and holding out for a season. A4 keeps the factories running at the moment the host most needs them.

A1 and A3 do not stack band reductions beyond one band in total, because both represent removing collaborators from contact with the enemy. A3 and A4 stack because they address different parts of the column.

The A2 reduction requires `add_collaboration` to accept a negative value or an equivalent relative reduction. If the engine cannot reduce collaboration relatively, the implementation reports a blocker. It must not replace the action with an absolute set, because that would erase collaboration from other sources.

### Dynamic costs

Costs scale with the country and the situation. A large country pays more manpower and equipment for A2 because it has more offices to purge, and a country already at Collapsing pays less political power for A3 because its ministries are already half empty. The ordinary anchors are kept in one constant group:

| Action | Minor country anchor | Major country anchor | Situation factor |
| --- | --- | --- | --- |
| A1 | 25 political power, 10 percent stability, 10 percent consumer goods | 50 political power, same spirit values | Stability cost rises to 15 percent while the Fifth Column is at Collapsing |
| A2 | 5,000 manpower, 500 infantry equipment, 25 political power | 15,000 manpower, 1,500 infantry equipment, 50 political power | Manpower falls by a third when the enemy holds a Total network, because the officials are easy to find |
| A3 | 10 trains or 300 trucks, 15 percent factory output for 120 days, 25 political power | 20 trains or 600 trucks, same output penalty, 50 political power | Political power cost falls by 10 at Collapsing |
| A4 | 25 command power, 25 army experience, 10 percent stability for 90 days | 40 command power, 50 army experience, same stability | Command power cost never exceeds 60 |
| A5 | 50 political power, 5 convoys | 100 political power, 15 convoys | none |

No action uses more than four distinct spendable cost types. Every displayed cost uses its correct texticon, and the inline cost row shows at most three values.

### Vetting spirit lifecycle

The Screen stance in the opening report and the A1 decision share one spirit family, so the host never carries two vetting spirits.

| Form | Source | Effects | Next form |
| --- | --- | --- | --- |
| Vetting Campaign | Screen stance | Stability and consumer goods costs from Part 1, incoming layer halved for the current firing | Upgraded to Loyalty Commissions by A1, or expires |
| Loyalty Commissions | A1 | Wartime effects in the table above with their costs | Expires after 180 days |

Taking A1 while a Vetting Campaign runs replaces it with Loyalty Commissions and restarts the duration. A later Screen stance during Loyalty Commissions applies only the incoming multiplier and does not shorten the commissions.

### Collaborators Unmasked

This is an event choice rather than a decision. It appears when Administrations in Waiting is active and the owner or an ally retakes a state where an enemy administration had been seated. It appears at most once per war for each owner and enemy pair.

| Option | Working label | Effect | Cost |
| --- | --- | --- | --- |
| Purge | Make examples of them | Reduces that enemy's collaboration inside us by 10 points, never below zero | A timed 10 percent stability penalty for 90 days |
| Amnesty | Keep the offices working | Collaboration stays in place | None |

Option direction: the purge option is the voice of a returning government that wants visible punishment. Its grim irony can point at the speed with which the same officials now denounce each other. The amnesty option is cold pragmatism: the trains must run and there is nobody else who knows how. Neither option may make light of reprisals against civilians.

## Prepared Governments decisions

The category appears only while Collaboration Governments is active.

| Action | Working label | Target | Visible when | Effect | Costs |
| --- | --- | --- | --- | --- | --- |
| B1 | Seat the Prepared Government in a target country | A capitulated participant, or one whose government is in exile | We control at least one of its core states, no living government installed through this route exists for its original tag, our network inside it meets the installation threshold, and average compliance in its cores we control is at least the reduced compliance threshold | Installs a prepared government through the Part 3 route | Political power, infantry equipment and manpower for the auxiliaries |
| B2 | Arm the Installed Administration | One of our living governments installed through this route | The government exists and is our subject | The government raises two more auxiliary divisions and moves 90 days closer to the Entrenched stage | Infantry equipment, manpower, political power |

### Reduced compliance threshold

The vanilla collaboration-government route needs 80 percent average compliance. B1 needs less when the network is deep: the threshold is 80 minus half of our collaboration inside the target, and never below 50. A Total network of 70 points therefore needs 45, which rises to the floor of 50. An Ordinary network of 20 points needs 70.

### Dynamic costs

| Action | Anchor | Scaling |
| --- | --- | --- |
| B1 | 50 political power, 500 infantry equipment and 2,000 manpower for each auxiliary division the government will receive | Political power rises by 25 for each living government we already hold through this route, which stops one power from installing governments everywhere at no growing price |
| B2 | 1,000 infantry equipment, 4,000 manpower, 25 political power | Usable once every 180 days per government and at most three times per government |

### Limits

- B1 has a 180-day cooldown per installer.
- One living government installed through this route per original tag at any time, regardless of installer.
- B1 and the Part 3 capitulation offer share the same installation helper and the same registry, so neither route can bypass the other's limits.

## AI behavior for the decisions

Weights belong to the probability matrix and must be audited. The intended ordering is below.

### Divided Loyalties

- A country at Collapsing takes A3 first, then A4 when it still has command power, then A1.
- A country at war whose foreign networks are Deep or Pervasive takes A1 early in the war, before the Fifth Column appears.
- A2 is taken when the seating enemy holds a Strong or Total network and the country can spare the manpower. A country short on manpower skips it.
- A5 is taken by a country that expects to fight on from exile: one with allies still at war, or one whose ideology differs from the enemy that would install a government. A country whose government is already sympathetic to the likely installer skips it.
- An AI never takes A1 while its stability is so low that the spirit would push it into civil-war risk. The blocked tooltip names the stability requirement.

### Prepared Governments

- An AI takes B1 when it is not itself past 40 percent surrender progress and the target's cores would otherwise need large garrisons.
- An AI prefers B1 over direct occupation when it is fighting on several fronts and needs its garrisons elsewhere.
- An AI that already holds three governments through this route takes B1 only for targets on its own continent.
- An AI takes B2 when one of its installed governments is Contested or faces an enemy on its territory.
- A democratic AI uses the same logic at reduced weight, reflecting political reluctance rather than an ideology lock.

## Decision cleanup

- Divided Loyalties hides when the country is at peace with every participant enemy. Active timed spirits run to their end.
- A2 targets clear when the targeted enemy no longer holds a seated state of ours.
- A3 and A4 hide when the Fifth Column ends.
- A5 resets at the end of each war.
- Prepared Governments hides when Collaboration Governments is disabled. B2 targets clear when a government stops existing, becomes independent, or turns to a rival.

## Exploit checks

| Risk | Guard |
| --- | --- |
| Farming compliance by recapturing the same state | 180-day seat guard per state and controller |
| Repeating Collaborators Unmasked | Once per war per owner and enemy pair |
| Stacking band reductions | A1 and A3 together reduce at most one band |
| Chain-installing governments everywhere | Growing political power cost, 180-day cooldown, one government per original tag |
| Using B2 as a free unit loop | Equipment and manpower are transferred, not created, with a cap of three uses per government |
| Screen stance as a free shield | The vetting spirit costs stability and consumer goods for months |
| Cultivate as a free advantage | Incoming layer rises by a quarter, which makes the cultivator easier to defeat in its own wars |
| Clicking A2 against an enemy with no meaningful network | Visible only while that enemy holds a seated state of ours, so the action always targets an exposed network |
