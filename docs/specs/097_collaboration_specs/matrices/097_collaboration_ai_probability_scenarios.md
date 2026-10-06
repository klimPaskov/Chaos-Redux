# Event 097 Collaboration: AI and Probability Scenarios

Every weighted surface in Event 097 must be audited by `chaosx_ai_probability_auditor` with the HOI4 MCP probability workflow. The audit begins with `hoi4.probability_inspect` on each surface, evaluates the named scenarios below with `hoi4.probability_evaluate`, sweeps the listed thresholds with `hoi4.probability_sweep`, and compares implemented source against the pre-edit source with `hoi4.probability_compare`. `hoi4.probability_render` is used where a ranking, timing, or comparison view makes the result easier to review. Decision and mission `ai_will_do` results are willingness scores and must not be reported as click probabilities. Option shares are conditional on the event having fired.

The expectations below are orderings, timing bands, and dominance or starvation limits. They are not exact probabilities, because candidate pools and campaign state vary.

## Weighted surfaces

| Surface | Kind | Candidate pool |
| --- | --- | --- |
| S1 Event 097 selection weight | Shared repeatable event weight, cap reduction, and recovery | Shared random-event pool |
| S2 Opening report stance | Event option `ai_chance` | Accept, Cultivate, Screen |
| S3 Prepared Government offer | Event option `ai_chance` | Install, Keep direct occupation |
| S4 Collaborators Unmasked | Event option `ai_chance` | Purge, Amnesty |
| S5 Divided Loyalties actions | Decision `ai_will_do` | A1 to A5 |
| S6 Prepared Governments actions | Decision `ai_will_do` | B1, B2 |
| S7 Evolution activation | MTTH timing | Evolutions I to IV |
| S8 Open Gates | MTTH timing | One incident per eligible host |
| S9 Turned Regime | MTTH timing | One incident per eligible government |
| S10 Installer choice | Deterministic selector with a random final tie-break | Qualifying enemies at capitulation |
| S11 Intelligence cluster roll | Shared cluster selection that reuses Event 097's weight | Cluster members 39, 52, 97 |
| S12 Open Gates state | Deterministic selector with a random final tie-break | Qualifying host core states |
| S13 Turned Regime rival | Deterministic selector with a random final tie-break | Qualifying rivals |
| S14 AI targets for A2 and B1 | Target ordering inside the decision weight | Enemies holding seated states, valid B1 targets |

## Named scenarios

| Id | Scenario | Key inputs |
| --- | --- | --- |
| P1 | Calm 1936 world, first firing | No wars, Chaos 50, no evolutions |
| P2 | Expanding fascist major at war in 1939 | At war with a neighbor, surrender progress 0, ruling party fascist |
| P3 | Threatened minor neighbor | Borders P2 country, claim on it, stability 55 percent |
| P4 | Threatened minor with low stability | As P3, stability 25 percent |
| P5 | Democracy at peace near an expanding power | Democratic, no war, fascist neighbor expanding |
| P6 | Installed government, Contested | Installer at 45 percent surrender progress |
| P7 | Host at Wavering against a Strong network | Surrender progress 30 percent |
| P8 | Host at Collapsing against a Total network | Surrender progress 65 percent, command power 40, manpower short |
| P9 | Installer offered a government while fighting on two fronts | Controls 80 percent of host cores, own surrender progress 10 percent |
| P10 | Installer offered a government while losing | Own surrender progress 45 percent |
| P11 | Democratic installer offered a government | As P9 with a democratic ruling party |
| P12 | Installer holding three governments, target on another continent | As P9 |
| P13 | Long world war, Chaos 850, all evolutions eligible | Many wars, several capitulations per year |
| P14 | Owner retakes a seated state from a Strong network | At war, stability 50 percent |
| P15 | Owner retakes a seated state with stability at 20 percent | As P14 |
| P16 | Expanding power at war at 25 percent own surrender progress | Cultivate reversal past 20 percent |
| P17 | Country in civil war | Screen blocked, Accept largest, a valid option remains |
| P18 | Installed government in Imposed and in Entrenched at peace | Baseline for P6 and for B2 starvation |
| P19 | Democracy at peace bordering an expanding power with a claim on it | Group precedence |
| P20 | Installer holding three governments, target on its own continent | Positive counterpart of P12 |
| P21 | Installer at 15 percent surrender progress with a peace conference near | Keep direct occupation case |
| P22 | Host at war at 15 percent surrender progress with Deep or Pervasive incoming networks | A1 taken before the Fifth Column |
| P23 | Host at Collapsing with Evolutions II, III, and IV active, allies at war, ideology different from the likely installer | A5 visibility, the four-action cap, and the A5 rule |
| P24 | Two enemies hold seated states, one Ordinary and one Strong | A2 target ordering |
| P25 | Expanding power with its own Fifth Column at Wavering | A1 for an expanding power |
| P26 | Fallout transition begun, Event 097 disabled, and one evolution disabled | Gate behavior on every surface |
| P27 | Long campaign from 1936 to 1946 under three declared Chaos paths and two pool sizes | Firing count, installation rate, and the Event 097 Chaos sum |

### Declared fixtures

- Group precedence for every scenario follows Part 6.
- P13 and P27 declare how many countries fall into each actor group, so the world-wide stance distribution can be computed.
- P27 declares the enabled pool at release, the Chaos path, and the player's event settings, because these decide the firing count.
- Every sweep below declares its step and range.

## Expected orderings and limits

### S1 selection weight

- The weight follows the shared repeatable rules with no event-owned factor. Recovery runs after every pacing update, major or minor, and continues while the event shows N/A.
- P27 records the number of natural firings and compares it with the ranges in Part 1.
- The event shows N/A with a reason while an application pass runs or fewer than two participants exist.

### S2 stance

- P1: Accept is the largest share. Cultivate and Screen each remain clearly above zero.
- P2: Cultivate is the largest share. Accept remains above zero.
- P3: Screen is the largest share.
- P4: Screen is blocked because stability is below the 30 percent requirement, and Accept becomes the largest share. The blocked state never leaves the event without a valid option.
- P5: Accept is the largest share, Screen second.
- P6: Screen is the largest share.
- P16: Cultivate falls below its P2 share, and Screen rises.
- P17: Screen is blocked and Accept is the largest share.
- P19: Screen is the largest share, through group precedence.
- Floors: Accept never below 10 percent, Cultivate and Screen never below 5 percent while available.
- Across a P13 world, no single stance should take more than about two thirds of all AI choices in one firing.

### S3 Prepared Government offer

- P9: Install is the largest share.
- P10: Keep direct occupation is the largest share.
- P11: Install remains possible but lower than in P9.
- P12: Install has zero weight.
- P20: Install is the largest share.
- P21: Keep direct occupation is the largest share.

### S4 Collaborators Unmasked

- P14: Purge is the largest share.
- P15: Amnesty is the largest share, because the stability penalty is costly at that point.

### S5 Divided Loyalties

- P7: A1 ranks first. A3 and A4 are not visible.
- P8: A3 ranks first, A4 second when command power allows, A2 third when manpower is at least twice its cost. A1 is hidden at Collapsing.
- A5 has positive weight for a country with allies still at war or with a ruling ideology different from the likely installer, and zero for a country with neither. A democracy weighs it higher. P23 checks both conditions together and that the category never shows more than four actions.
- P22: A1 ranks first.
- P24: A2 targets the Strong enemy.
- P25: A1 has positive weight only once the expanding power's own Fifth Column appears.
- At Defecting and Collapsing, A5 ranks between A3 and A4 when its rule is met.
- No action has positive willingness when its effect is unavailable. A2 must be zero when no enemy holds a seated state.

### S6 Prepared Governments

- B1 ranks above zero only when the installer is below 40 percent surrender progress.
- B1 is zero for targets on another continent once the installer holds three governments.
- B2 ranks highest for a government that is Contested or has an enemy on its territory, and stays low but above zero in P18.
- In P13, installations stay within about one to four per year worldwide. More than six in a year is a failure.

### S7 evolution timing

| Evolution | Ordinary window after eligibility | Fast case | Slow case |
| --- | --- | --- | --- |
| I | roughly 60 to 120 days | two prior firings, three wars | no prior firing |
| II | roughly 60 to 120 days | Deep Networks active, a capitulation since the first firing | no war |
| III | roughly 60 to 120 days | Administrations in Waiting active, a host past 40 percent | no war |
| IV | roughly 90 to 150 days | II and III active, recent capitulation | no war |

Every timed surface follows the timing model in Part 2: the MTTH entry is evaluated once when the countdown starts, clamped, and scheduled with an even spread of up to a third of the delay in either direction. Each scenario therefore gives an exact delay range rather than a curve. The audit reports that range for the ordinary and extreme cases, separately for the pre-fire and active entries, and confirms that the minimum clamp keeps every evolution at 30 days or more. Scheduled state changes during a countdown, such as a war starting, Chaos falling, or the evolution being disabled, must leave the countdown unchanged and be handled at the check.

### S8 Open Gates

- At Defecting, the first incident comes after about 60 days. At Collapsing, about 30 days. The 90-day spacing sets the pace after that.
- A check during A3 or A4 does nothing and starts a new timer. A timer started during A1 runs twice as long.
- Over a 365-day war at Collapsing, the cap of three per host binds. At Defecting it may not bind within a year, which is intended.

### S9 Turned Regime

- The delay is about 120 days while conditions hold, clamped between 60 and 365 days.
- The world spacing of 365 days allows at most one per year. In P13 the target is fewer than one per year across the world.

### S10 installer selector

- The selector is ordered: highest network band, then most host cores controlled, then the capitulation recipient, then a random choice among equals.
- The audit must confirm that the first valid candidate is accepted even when no score exceeds a numeric sentinel.

### S11 to S14

- S11: the cluster roll is audited with the shared cluster rules once the Intelligence cluster exists. Event 097 must not gain more than one extra firing per cluster activation.
- S12 and S13 follow the orderings in Part 3. The audit confirms that every tie-break ends in a choice.
- S14 follows the target orderings in Part 4.

### P26 gate expectations

- During the Fallout transition: S2 to S9 produce no new choices or timers that write collaboration, both categories are hidden, Collaborators Unmasked does not fire, and the event shows N/A.
- With Event 097 disabled: S1 is zero and no firing happens. Behaviors of evolutions that already activated continue.
- With one evolution disabled: that evolution's surfaces stop as Part 4 describes, and every other surface behaves as in its own scenarios.

## Sweeps

Each threshold below gets a sweep across its edge so rank reversals are visible:

- own surrender progress across 20 percent for the Cultivate decline
- stability across the 30 percent Screen requirement and the Purge stability penalty
- installer surrender progress across 40 percent for the offer and B1
- host surrender progress across the Fifth Column floors of 20, 40, and 60, rising and falling, to show the 5-point hysteresis
- command power across the A4 costs and the cap
- available manpower across twice the A2 manpower cost
- network value across the band edges of 15, 40, and 70
- the installation threshold across its modifiers and its limits of 25 and 60
- governments held from two to three for the continent rule

## Evidence requirements

- Each surface names its source file and identifier.
- Each scenario records whether the candidate pool and external factors were complete.
- Each result is classified as exact, bounded, sampled, score-only, or unresolved.
- Before any weight change, an immutable copy of the pre-edit source and the scenario fixture is preserved with a SHA-256 hash, and `hoi4.probability_compare` uses the same scenarios after the change.
- If the probability route is unavailable, the affected conclusions remain unresolved and are reported as blockers.
