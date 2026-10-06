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
| S10 Installer choice | Deterministic selector | Qualifying enemies at capitulation |

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

## Expected orderings and limits

### S1 selection weight

- The weight follows the shared repeatable rules with no event-owned factor.
- The audit records the expected number of natural firings over a long campaign and compares it with the assumption in Part 1 of two to five firings.
- The event shows zero weight with a reason while an application pass runs or fewer than two participants exist.

### S2 stance

- P1: Accept is the largest share. Cultivate and Screen each remain clearly above zero.
- P2: Cultivate is the largest share. Accept remains above zero.
- P3: Screen is the largest share.
- P4: Screen is blocked or near zero because of the stability requirement, and Accept becomes the largest share. The blocked state must not leave the event with no valid option.
- P5: Accept is the largest share, Screen second.
- P6: Screen rises above its P1 share.
- Across a P13 world, no single stance should take more than about two thirds of all AI choices in one firing.

### S3 Prepared Government offer

- P9: Install is the largest share.
- P10: Keep direct occupation is the largest share.
- P11: Install remains possible but lower than in P9.
- P12: Keep direct occupation is the largest share.

### S4 Collaborators Unmasked

- P14: Purge is the largest share.
- P15: Amnesty is the largest share, because the stability penalty is costly at that point.

### S5 Divided Loyalties

- P7: A1 ranks first. A3 and A4 are not visible.
- P8: A3 ranks first, A4 second when command power allows, A1 third. With manpower short, A2 ranks below A1.
- A5 ranks above A1 only for a country with allies still at war and a different ideology from the likely installer.
- No action has positive willingness when its effect is unavailable. A2 must be zero when no enemy holds a seated state.

### S6 Prepared Governments

- B1 ranks above zero only when the installer is below 40 percent surrender progress.
- B1 is zero for targets on another continent once the installer holds three governments.
- B2 ranks highest for a government that is Contested or has an enemy on its territory.

### S7 evolution timing

| Evolution | Ordinary window after eligibility | Fast case | Slow case |
| --- | --- | --- | --- |
| I | roughly 60 to 120 days | two prior firings, three wars | no prior firing |
| II | roughly 60 to 120 days | Deep Networks active, recent capitulation | no war |
| III | roughly 60 to 120 days | Administrations in Waiting active, a host past 40 percent | no war |
| IV | roughly 90 to 150 days | II and III active, recent capitulation | no war |

The audit must provide survival curves for the ordinary and extreme cases and confirm that no evolution activates in under 30 days.

### S8 Open Gates

- At Defecting, the expected time to the first incident is about 60 days. At Collapsing, about 30 days.
- With A3 or A4 active, the incident is suspended. With A1 active, the expected time doubles.
- Over a 365-day war at Collapsing, the cap of three per host must bind before the MTTH would produce more.

### S9 Turned Regime

- Expected time about 120 days while conditions hold.
- In P13, fewer than one Turned Regime per year across the world is the target band. More than two per year is a failure.

### S10 installer selector

- The selector is deterministic: highest network band, then most host cores controlled, then the capitulation recipient.
- The audit must confirm that the first valid candidate is accepted even when no score exceeds a numeric sentinel.

## Evidence requirements

- Each surface names its source file and identifier.
- Each scenario records whether the candidate pool and external factors were complete.
- Each result is classified as exact, bounded, sampled, score-only, or unresolved.
- Before any weight change, an immutable copy of the pre-edit source and the scenario fixture is preserved with a SHA-256 hash, and `hoi4.probability_compare` uses the same scenarios after the change.
- If the probability route is unavailable, the affected conclusions remain unresolved and are reported as blockers.
