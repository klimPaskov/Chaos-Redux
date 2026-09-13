# Event 067 Probability Scenario Matrix

## Purpose

This matrix defines the named scenarios required for every Event 067 weighted surface. It gives expected ordering and safety conditions. It does not prescribe exact percentages where the full candidate pool or engine state is not yet known.

`chaosx_ai_probability_auditor` must inspect each weighted surface before evaluation. The auditor remains read-only. The parent or owning implementation agent sets the intended balance and applies changes.

## Required workflow

1. Use `hoi4.probability_inspect` on the exact source surface.
2. Confirm the complete candidate pool and all external factors used by the named scenario.
3. Use `hoi4.probability_evaluate` for complete option and target pools.
4. Use `hoi4.probability_sweep` across Influence, stability, war direction, command authority, and removal preparation.
5. Use `hoi4.probability_render` for matrices and sensitivity views that improve review.
6. Use `hoi4.probability_simulate` only when the candidate pool and repeated cadence are complete.
7. Use `hoi4.probability_sequence` only when the full demand cadence, cooldown, removal, and terminal-state contract is declared.
8. After a patch, use `hoi4.probability_compare` with the same scenario IDs.

## Target selection scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-T01` | One valid player is losing a major war. Four valid peaceful majors exist. | The player has the highest individual target weight. Peaceful majors remain possible. |
| `G67-T02` | One valid peaceful player and one valid major at war. | The class bias and war factors remain visible. Neither valid country is forced to zero. |
| `G67-T03` | Two valid players and eight valid majors. | The configured player-class share is distributed among players. One Generalissimo is selected worldwide. |
| `G67-T04` | No valid player. Five valid majors. | Selection normalizes across majors only. |
| `G67-T05` | One valid major is the only valid target. | Exact normalized probability is 100 percent. |
| `G67-T06` | A major is an actual nonhuman country. | Exact target weight is zero. |
| `G67-T07` | A major is in an active civil war. | Exact target weight is zero. |
| `G67-T08` | A player controls one state and cannot sustain two sides. | Normal Event 067 target weight is zero. Scenario non-war types can remain available if supported. |
| `G67-T09` | A major is capitulated but still exists. | Exact target weight is zero. |
| `G67-T10` | Event 067 already fired or SCN-015 launched. | Every target receives zero because the event is unique. |

## Evolution pacing scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-E01` | Chaos 199, Generalissimo active. | Evolution I cannot enter. |
| `G67-E02` | Chaos 200, low service record, peace, Advisory Reserve. | Evolution I is eligible but slower than the base pacing target. |
| `G67-E03` | Chaos 200, high service record, active losing war, National Field Command. | Evolution I enters faster than `G67-E02`. |
| `G67-E04` | Chaos 400, Influence 25, weak network. | Evolution II remains slow or ineligible according to the accepted threshold. |
| `G67-E05` | Chaos 400, Influence 60, Supreme Command, accepted concessions. | Evolution II enters faster than `G67-E04`. |
| `G67-E06` | Chaos 600, Influence 70, strong counterweights. | Evolution III remains slower than a comparable unprepared government. |
| `G67-E07` | Chaos 600, Influence 95, strong network, Supreme Command. | Evolution III enters quickly, followed by a short visible ultimatum interval. |
| `G67-E08` | Evolution disabled in settings. | Exact entry probability is zero and no recorded flag is set. |

## Demand selection scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-D01` | Evolution I, Theater Command, active major war. | National Field Command or operational authority outranks peacetime propaganda demands. |
| `G67-D02` | Evolution I, Supreme Command already granted. | Supreme Command demand receives zero. Appointment, budget, and officer-protection demands remain possible. |
| `G67-D03` | Evolution II, no military factories under host control. | Armament-board demand receives zero or uses a valid alternative institution. |
| `G67-D04` | Evolution II, no intelligence DLC. | Internal-security demand remains valid through the no-DLC route. DLC-only actions receive zero. |
| `G67-D05` | A demand was accepted recently. | Demand cadence is delayed by cooldown. No immediate second demand. |
| `G67-D06` | A demand is already active. | Every other demand receives zero until resolution. |
| `G67-D07` | Peace, high stability, low Influence. | Public promotion or appointments can appear. Emergency powers remain low weight. |
| `G67-D08` | Losing war, low stability, high Influence. | Emergency powers, armament control, or Supreme Command outrank minor prestige demands. |

## AI concession and counterweight scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-A01` | Constitutional government, peace, high stability, Influence 30. | Oversight, rotation, or reserve action outranks major concession. |
| `G67-A02` | Constitutional government losing a major war, Influence 30. | Command expansion can outrank oversight during immediate danger. |
| `G67-A03` | Militarist government at war, Influence 45. | Appointment and command concessions receive high weight. |
| `G67-A04` | Personalist ruler, Influence 45, strong intelligence. | Removal preparation outranks public promotion. |
| `G67-A05` | Weak fragmented government, Influence 70, no loyal reserve. | Concessions or submission preparation outrank coercive removal. |
| `G67-A06` | Defensive isolated government, Influence 55. | Managed coexistence and Fortress-oriented counterweights outrank aggressive purge. |
| `G67-A07` | Country cannot pay equipment cost for loyal reserve. | Loyal reserve decision receives zero. |
| `G67-A08` | Country cannot pay a command-power cost. | Decision receives zero and blocked text agrees. |

## Removal chance scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-R01` | Influence 15, Advisory Reserve, strong civilian command. | Retirement is deterministic or near-certain. Dismissal is favorable. |
| `G67-R02` | Influence 35, Theater Command, moderate preparation. | Dismissal and arrest are viable. Capture and assassination remain method-dependent. |
| `G67-R03` | Influence 60, National Field Command, no loyal reserve. | Every coercive method is worse than `G67-R02`. |
| `G67-R04` | Influence 60, loyal reserve, separated intelligence, dispersed guard. | Arrest and capture improve materially over `G67-R03`. |
| `G67-R05` | Influence 80, Supreme Command, protected officers, internal-security control. | Unprepared coercive methods are very poor. |
| `G67-R06` | Same as `G67-R05`, with full government preparation. | Success remains risky but is materially higher than the unprepared case. |
| `G67-R07` | Event 039 support active and valid. | Assassination improves without becoming guaranteed. |
| `G67-R08` | Failed ordinary dismissal before Evolution III. | No immediate revolt. Safe dismissal locks and Influence rises. |
| `G67-R09` | Failed arrest at any crisis stage. | Immediate revolt probability is exactly 100 percent. |
| `G67-R10` | Failed final removal during ultimatum. | Immediate revolt probability is exactly 100 percent. |

## Final ultimatum AI scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-U01` | Influence 95, weak government army, losing external war, military regime. | Submit is the dominant AI option. |
| `G67-U02` | Influence 85, strong loyal reserve, secure capital, strong allies. | Refuse can outrank submit. |
| `G67-U03` | Influence 90, removal chance high after full preparation. | Final removal can outrank both alternatives. |
| `G67-U04` | Influence 100, removal chance near zero, government militarily weak. | Final removal receives very low weight. |
| `G67-U05` | Democratic government with high legitimacy and moderate civil-war strength. | Refuse outranks peaceful submission unless removal is favorable. |

## Civil-war setup scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-C01` | Influence 20, weak network. | Junta division share falls near the lowest accepted band. One compact nucleus. |
| `G67-C02` | Influence 45, average network. | Junta division share and territory exceed `G67-C01`. |
| `G67-C03` | Influence 70, strong officer and regional support. | Junta receives a majority-capable army share and more territory. |
| `G67-C04` | Influence 95, failed assassination, full institutional control. | Junta approaches the maximum safe army band and gains strong coordination. |
| `G67-C05` | Influence 70, government created loyal reserve and moved arsenals. | Division and stockpile shares are lower than `G67-C03`. |
| `G67-C06` | High officer loyalty but low military-industry reach. | Division share can be high while stockpile share remains lower. |
| `G67-C07` | Strong naval host with Maritime Command support. | Navy split is meaningful and ordered by support. |
| `G67-C08` | Landlocked host. | Naval candidate pool is empty and no naval setup runs. |
| `G67-C09` | Archipelagic host. | Junta territory prioritizes viable ports and avoids unsupported inland pockets. |
| `G67-C10` | Invalid one-state host. | Normal target and immediate-war scenario type remain blocked. |

## Focus route scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-F01` | High aggression, high Cohesion, strong army, few rivals. | Personal Command receives the highest political route weight. |
| `G67-F02` | Many skilled commanders, meaningful navy and air, medium Cohesion. | Officer Directorate receives the highest political route weight. |
| `G67-F03` | Damaged economy, high resistance, need for recognition. | National Emergency Council receives the highest political route weight. |
| `G67-F04` | Fuel-rich, armor-capable offensive state. | Decisive Command outranks other military strategies. |
| `G67-F05` | Manpower-rich, equipment-moderate state. | Army of the Nation outranks other strategies. |
| `G67-F06` | Threatened resource-poor defensive state. | Fortress Command outranks other strategies. |
| `G67-F07` | Landlocked state with no navy. | Every naval focus route weight and visibility condition resolves to zero or hidden. |
| `G67-F08` | Several friendly military governments and no faction conflict. | Officer Solidarity route gains weight. |
| `G67-F09` | No valid expansion targets and weak logistics. | Supreme Strategic Sphere receives low or zero weight. |

## World-end country response scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-W01` | Stable civilian major, strong loyal command reforms, no losing war. | Civilian Defiance is the dominant outcome. |
| `G67-W02` | Low-stability military-heavy state with one dominant commander. | Peaceful Officer Coup is the dominant outcome. |
| `G67-W03` | Divided officer corps, several viable regions, medium military dominance. | Split Command Civil War has high weight. |
| `G67-W04` | One-state country. | Split Command Civil War receives zero. Peaceful coup, emergency government, or defiance remain. |
| `G67-W05` | Existing military government friendly to original Generalissimo. | Alignment with International Command is possible. Redundant coup receives zero. |
| `G67-W06` | Existing strong military major with regional ambition. | Rival military bloc can outrank submission to original Generalissimo. |
| `G67-W07` | Actual nonhuman or incompatible special Chaos country. | Every Event 067 world-end response weight is zero. |
| `G67-W08` | Country already in civil war. | Immediate second civil war receives zero. Delayed or side-alignment handling applies. |

## Bloc membership scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-B01` | Original Generalissimo plus one friendly junta. | International Command cannot form. |
| `G67-B02` | Original Generalissimo plus three independent compatible juntas. | International Command becomes available. |
| `G67-B03` | Five juntas, two at war with each other. | Founding pool excludes incompatible belligerents. |
| `G67-B04` | Three civilian governments with no major or regional power. | Civil Authority Compact remains unavailable if the major-power gate is required. |
| `G67-B05` | Three civilian governments including one major. | Civil Authority Compact becomes available when diplomacy is compatible. |
| `G67-B06` | Strong rival military major and two partners. | Rival bloc formation becomes possible. |

## Manual scenario scaling scenarios

| Scenario ID | Setup | Expected result |
| --- | --- | --- |
| `G67-S01` | Favored Commander, Low to Maximum. | Influence and network rise monotonically. No immediate revolt. |
| `G67-S02` | State Within the State, Low to Maximum. | Institutional control and removal danger rise monotonically. |
| `G67-S03` | The Ultimatum, Low to Maximum. | Preparation window shortens and starting Influence rises monotonically. |
| `G67-S04` | Generalissimo's War, Low to Maximum. | Army, stockpile, commander, and territorial shares rise monotonically within safe caps. |
| `G67-S05` | Current player valid. | Current player is selected at every intensity. |
| `G67-S06` | Current player invalid, one valid major. | Valid major is selected or launch is blocked according to the selected type. |
| `G67-S07` | World-end already active. | Launch probability and button availability are zero. |
| `G67-S08` | Scenario already launched. | Repeat launch probability and button availability are zero. |

## Sequence audit scenarios

Use `hoi4.probability_sequence` only after the complete cadence is declared.

| Scenario ID | Sequence | Expected property |
| --- | --- | --- |
| `G67-Q01` | Ten years of peace, Advisory Reserve, strong oversight | Influence should trend downward or remain contained. Ultimatum should not be inevitable. |
| `G67-Q02` | Major war, repeated command concessions, several victories | Influence should rise into the high bands and accelerate Evolution II and III. |
| `G67-Q03` | Alternating authority expansion and restriction | Cooldowns and memory prevent bonus or Influence farming. |
| `G67-Q04` | Repeated demand acceptance | Demand cooldown prevents immediate chains and major institutional milestone Chaos fires once. |
| `G67-Q05` | Government prepares removal over several phases | Removal chance improves in a measurable ordered way. |

## Required comparison report

The final probability report should list:

- source surface
- scenario ID
- candidate pool completeness
- external factors supplied
- result type, such as exact, bounded, sampled, score-only, or unresolved
- baseline revision
- patched revision
- `hoi4.probability_compare` result
- whether expected ordering passed
- remaining balance decision
