# Murder Mystery Specification Part 16: Achievements

## Achievement design rules

Event 39 needs achievements for ordinary-government investigation, original-host survival, international containment, Assassin State routes, and terminal victory or resistance. Each achievement must require deliberate play, use durable tracking, prevent setup or scenario abuse where relevant, and have a distinct icon concept.

Final achievement IDs should remain stable once implementation begins. The working IDs below follow the required event-owned naming pattern.

## Achievement 1: No Second Victim

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_no_second_victim` |
| Title direction | Capture the original murderer before another successful Event 39 killing |
| Eligible country | Original host in a natural Event 39 run |
| Unlock condition | Full capture and permanent baseline resolution after the opening leader murder, with zero later successful named or generic Event 39 murders |
| Disqualifiers | Assassin Network scenario, force-trigger bypass that skips investigation, failed or partial capture, any later successful Event 39 casualty |
| Difficulty | Hard |
| Visibility | Visible after Event 39 begins, hidden before the event if project convention supports it |
| Why it is not trivial | Requires fast evidence, protection, and a correct final operation before the next incident |
| Tracking | opening casualty recorded separately, later successful casualty count, natural-run flag, full-resolution flag |
| Icon direction | sealed evidence file beside one empty chair, no blood or text |

Attempted attacks do not disqualify the achievement if no target dies. Deaths caused by war or unrelated events do not count.

## Achievement 2: The Empty Chair Holds

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_empty_chair_holds` |
| Title direction | Preserve constitutional or institutional continuity through the crisis |
| Eligible country | Original host |
| Unlock condition | Resolve Event 39 before Evolution III, maintain the verified succession, finish with high stability, preserve the capital, and avoid the emergency repression response profile |
| Disqualifiers | Assassin State created, capital lost during active investigation beyond the accepted short interruption, successor replaced through Event 39 collapse, emergency repression profile |
| Difficulty | Medium to hard |
| Visibility | Visible |
| Why it is not trivial | Rewards continuity and evidence quality through a slower protective strategy |
| Tracking | opening posture, successor identity, capital-control mission state, stability threshold, resolution stage |
| Icon direction | empty official chair guarded by a sealed constitutional folder or institutional emblem |

The final stability threshold should be audited against country scale and difficulty. It should be demanding without excluding countries that began the event under ordinary wartime pressure.

## Achievement 3: A Net Without Knives

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_net_without_knives` |
| Title direction | Dismantle the international network before any foreign territorial revolt |
| Eligible country | Original host or a country that becomes the recognized intelligence coordinator |
| Unlock condition | Event reached Evolution II, at least five foreign cells became active, every mature cell and the original core were dismantled, and no foreign Assassin derivative was created |
| Disqualifiers | Assassin Network Maximum setup, any foreign territorial revolt, unresolved mature cell, movement inheritance after the final operation |
| Difficulty | Hard |
| Visibility | Visible after Evolution II |
| Why it is not trivial | Requires international evidence sharing, target selection, and cell cleanup across several countries |
| Tracking | unique active-cell countries, maximum simultaneous cells, derivative creation count, mature-cell cleanup, global resolution |
| Icon direction | several connected dossiers closed by one unbroken net, no weapon as central symbol |

## Achievement 4: The Knife Breaks

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_the_knife_breaks` |
| Title direction | As the original host, defeat the Assassin State and eliminate every surviving mature cell |
| Eligible country | Original host controlled by the player at the time of the split |
| Unlock condition | Assassin State formed naturally, player remained with original host, central country or heir defeated, all derivatives resolved, and no stage 3 or 4 cells remain |
| Disqualifiers | player switched to Assassin State, foreign ally dealt the final central defeat without the host meeting a contribution floor, active movement heir, scenario setup if project achievements exclude it |
| Difficulty | Very hard |
| Visibility | Visible after Evolution III |
| Why it is not trivial | Combines civil war survival, counterintelligence, foreign cleanup, and movement-inheritance prevention |
| Tracking | original player side, war contribution or objective completion, central defeat, derivative registry, cell stages, inheritance count |
| Icon direction | broken Event 39 blade emblem across restored state papers |

The contribution floor should use campaign objectives or share of decisive actions. Raw war participation alone may be unreliable.

## Achievement 5: No Masters Above Us

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_no_masters_above_us` |
| Title direction | Complete the decentralized movement route and prove it can survive without central rule |
| Eligible country | Central Assassin State |
| Unlock condition | Lock Cells Without Masters, defeat or force surrender of the original host, control its former capital, maintain at least three viable autonomous foreign derivatives, and complete the decentralized campaign-council capstone |
| Disqualifiers | Hidden Hand or Necessary Mask route, all derivatives set to the strict central subject form, terminal victory before decentralized settlement is complete |
| Difficulty | Hard |
| Visibility | Visible after the political fork |
| Why it is not trivial | Requires military success while preserving autonomous cells and managing lower central coordination |
| Tracking | route lock, former capital control, derivative autonomy state, viable derivative count, capstone completion |
| Icon direction | several independent cell emblems around an empty center, clear at achievement size |

## Achievement 6: Necessary Hypocrisy

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_necessary_hypocrisy` |
| Title direction | Build an effective conventional state while claiming it is temporary |
| Eligible country | Central Assassin State |
| Unlock condition | Lock The Necessary Mask, replace all three starting spirits with mature pragmatic outcomes, field a viable Mechanized Assassin formation, lead a Veiled Compact with at least four surviving derivatives, and maintain high Brotherhood Cohesion |
| Disqualifiers | route switch, free scenario-only elite grants without normal production proof, derivatives that exist only as setup rows with no viable package |
| Difficulty | Very hard |
| Visibility | Visible after route lock |
| Why it is not trivial | Requires industry, fuel, technology, subjects, Cohesion, and a mixed military. One focus completion is insufficient |
| Tracking | route, spirit lifecycle, mechanized template fielded and supplied, derivative viability, Cohesion threshold |
| Icon direction | formal government seal worn over the movement's broken-command symbol |

## Achievement 7: Every Chair Empty

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_every_chair_empty` |
| Title direction | Complete World of Anarchy |
| Eligible country | Central Assassin State or valid movement heir controlled by the player |
| Unlock condition | Activate World of Anarchy through normal terminal preparation and reach terminal victory with no eligible ordinary independent government left outside a valid administration or exemption |
| Disqualifiers | debug victory, invalid registry repair that directly marks targets complete, dedicated future terminal scenario unless explicitly made eligible |
| Difficulty | Extreme |
| Visibility | Hidden until Evolution V or visible as a spoiler according to project convention |
| Why it is not trivial | Requires reaching World Collapse, surviving internal contradiction, winning a global terminal war, and resolving every ordinary government safely |
| Tracking | terminal activation, target registry completion, central or inherited player actor, victory transaction |
| Icon direction | a row of empty government chairs linked to one concealed command knot |

## Achievement 8: The Last Safe Cabinet

| Field | Specification |
| --- | --- |
| Working ID | `039_murder_mystery_last_safe_cabinet` |
| Title direction | Remain an ordinary independent government through the terminal war and help defeat the movement |
| Eligible country | Player-controlled ordinary country that is not an Assassin country or special Chaos country |
| Unlock condition | World of Anarchy activates, country remains independent and not dismantled, preserves its current national leader and a minimum safe command and cabinet set from activation to movement defeat, completes at least one major sector or intelligence objective, and survives the final defeat transaction |
| Disqualifiers | becoming an Assassin derivative, entering protected special-country status after activation, losing required protected offices, no meaningful contribution, movement victory |
| Difficulty | Extreme |
| Visibility | Hidden until World of Anarchy activates |
| Why it is not trivial | Requires leadership protection, war survival, counterintelligence, and real coalition contribution during the terminal system |
| Tracking | ordinary-country status at activation, leadership and office disposition snapshot, independence, terminal objective completion, movement defeat |
| Icon direction | one guarded cabinet room illuminated while surrounding office windows are dark |

## Scenario eligibility policy

Achievements should normally distinguish natural Event 39 progression from triggerable scenario setup. The investigation achievements `No Second Victim`, `The Empty Chair Holds`, and `A Net Without Knives` should require a natural run because scenario intensities alter their opening state.

Assassin State route achievements may allow High or Maximum scenario runs only if the scenario does not grant the achievement conditions directly and the implementation can prove normal production, route, subject, and Cohesion requirements. The final achievement audit must make this policy explicit for each row.

World of Anarchy victory and resistance achievements should exclude future terminal-only debug or scenario shortcuts unless a separate achievement rule is accepted.

## Tracking safety

Achievement tracking should use one-shot flags, stable actor references, registry outcomes, and explicit disqualifiers. It should not infer a condition from a current value that can be regained after failure.

Examples:

- once a later Event 39 victim dies, No Second Victim remains disqualified
- once a foreign derivative forms, A Net Without Knives remains disqualified
- once the original player switches sides, The Knife Breaks remains disqualified
- once a required terminal office is lost, The Last Safe Cabinet remains disqualified

## Icon package

Every final achievement ID requires normal, grey, and not-eligible DDS files in `gfx/achievements/`. Filenames must match the full achievement ID. The icon worker should inspect the achievement reference shelf, preserve the correct frame and alpha behavior, and use the project overlay workflow for the not-eligible variant.

## Acceptance standard

The achievement set is complete only when every condition, disqualifier, country scope, scenario policy, difficulty, visibility rule, tracking flag, tooltip direction, icon triplet, and live test path is implemented. Easy focus-click unlocks, ambiguous contribution, current-state-only checks, and missing scenario disqualifiers are not accepted.
