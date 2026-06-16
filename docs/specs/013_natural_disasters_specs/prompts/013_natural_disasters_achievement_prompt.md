# Achievement Prompt — Event 013 Natural Disasters

Implement these achievements only after the Natural Disasters mechanic exists. Each achievement needs tracking, localisation, completed icon, grey/not-eligible variants if the achievement system requires them, and docs. Do not award achievements merely because Event 13 fired.

## Achievement list

| ID | Title | Visibility | Difficulty | Eligible country | Unlock conditions | Disqualifiers | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ACH_ND_RING_THE_BELL` | Ring the Bell Before the Water | Visible | Medium | Any player | Receive at least 5 disaster warnings and complete a mitigation decision before impact for each; at least one must be flood/storm/tsunami. | Any warned disaster in the sequence has no mitigation decision taken. | warning bell/siren over wave and rail bridge |
| `ACH_ND_ENGINEERS_OF_THE_RUBBLE` | Engineers of the Rubble | Visible | Medium | Any player | Fully recover 10 earthquake/landslide/industrial-collapse aftermaths without letting recovery missions fail. | Using manual maximum scenario for all 10 recoveries. | cracked factory repaired by engineer tools |
| `ACH_ND_THE_TRAINS_ARRIVED` | The Trains Arrived | Visible | Medium | Any player controlling rail-connected land | Use relief train or railway repair responses in 8 different affected states and keep each state connected to supply. | Failing a rail recovery mission. | relief train crossing floodwater |
| `ACH_ND_NO_PORT_LEFT_BEHIND` | No Port Left Behind | Visible | Hard | Any coastal/island player | Survive 4 storm-surge/tsunami/port-disaster incidents while restoring every affected port before its mission expires. | Losing control of any affected port before recovery. | harbour crane and rescue boat |
| `ACH_ND_GRAIN_AGAINST_THE_DUST` | Grain Against the Dust | Visible | Hard | Any player | Prevent a drought chain from becoming famine in at least 3 different regions through rationing/import/relief missions. | Any drought famine chain succeeds in the same campaign after first drought warning. | grain sack and cracked field crossed by rail line |
| `ACH_ND_ASH_ON_THE_RUNWAY` | Ash on the Runway | Hidden | Hard | Any player with airbases | Clear 3 volcanic ash or meteor dust airfield aftermaths while keeping at least one airbase operational in each affected region. | Losing all airbase functionality in a targeted region during the recovery window. | ash cloud over a cleared airstrip |
| `ACH_ND_SKY_ARTILLERY_SURVIVOR` | Sky Artillery Survivor | Hidden | Very hard | Any player | Survive an Evolution IV meteor shower that hits at least 3 states, recover every affected state, and keep the capital undamaged by meteor aftermath. | Capital receives `meteor_scars` or equivalent during that shower. | meteor crater with intact capital silhouette |
| `ACH_ND_THE_SEA_WALKED_BACK` | The Sea Walked Back | Hidden | Very hard | Any coastal player | Receive an earthquake or volcanic warning, then survive the delayed tsunami follow-up with all affected ports recovered and civilian loss below the high threshold. | No warning/mitigation before tsunami; any affected port remains in aftermath at mission end. | receding sea and siren tower |
| `ACH_ND_NOT_ONE_MORE_AFTERSHOCK` | Not One More Aftershock | Visible | Hard | Any player | In a campaign with Evolution III active, complete 5 chained aftermath recoveries before their follow-up events trigger. | Any chained aftermath in the set escalates. | cracked seismograph needle calmed by engineer hand |
| `ACH_ND_DISASTER_LEDGER_CLOSED` | Disaster Ledger Closed | Hidden | Very hard | Any player | During the manual scenario at High or Maximum intensity, finish with every active disaster aftermath recovered or reduced to light recovery within the allowed window. | Any disaster aftermath remains severe at the end; scenario launched at Low/Medium. | closed emergency ledger with storm/quake/meteor marks, no text |
| `ACH_ND_NO_WORLD_END_REQUIRED` | No World End Required | Hidden | Extreme | Any player | Experience an Evolution IV abnormal disaster burst, avoid triggering any world-end scenario, and recover all affected core states while chaos remains below the next terminal threshold. | Any world-end scenario starts before recoveries finish. | globe with repair scaffold under meteor-streaked sky |
| `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS` | Still Standing in Four Seasons | Visible | Hard | Any player | In one campaign, successfully recover from one earthquake, one flood/storm, one drought/wildfire, and one volcanic/meteor/ash incident. | Manual scenario cannot count for more than one family. | four-panel disaster shield, no text |

## Tracking notes

- Track warning mitigations separately from impact recoveries.
- Track disaster family completion per state/region.
- Manual scenario achievements should be clearly flagged so ordinary achievements cannot be farmed entirely from the scenario unless intended.
- For hidden achievements, do not spoil Evolution IV exact content in visible descriptions.
- Ensure each achievement has an icon direction in the asset prompt.

## Acceptance criteria

- No achievement unlocks merely for firing Event 13.
- Every achievement has disqualifiers or nontrivial conditions.
- At least one achievement rewards warning use, one rewards recovery, one rewards regional chains, one rewards Evolution IV, and one rewards the manual scenario.
- All tracking flags/variables are cleaned up safely on campaign reset and do not leak across tags.
