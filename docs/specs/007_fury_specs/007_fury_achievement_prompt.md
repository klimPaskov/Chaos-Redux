# Achievement Prompt for Event 007 Fury

Implement and document achievements for Event 007, Fury.

Read:

- docs/specs/007_fury_specs/007_fury_spec.md
- docs/specs/007_fury_specs/007_fury_ai_matrix.md
- AGENTS.md
- chaos-redux-events
- chaos-redux-event-assets for icons

Rules:

- Players cannot become Fury.
- Achievements reward containment, observation, timing, and defeating Fury.
- Do not create achievements that unlock just because the event fired.
- Add tracking flags or variables where a final state cannot prove the route.
- Each achievement needs a 64x64 icon direction.

## Planned achievements

| ID | Title | Visibility | Difficulty | Requirement summary | Disqualifiers | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `achievement_fury_no_second_neighbor` | No Second Neighbor | visible | medium | Stop a Fury country after it defeats the first neighbor but before it declares on a second | Fury declares second scripted war | broken border arrow stopped by shield |
| `achievement_fury_before_the_headlines` | Before the Headlines | hidden | hard | Defeat or force Fury capitulation before first victory news fires | first victory news fires | newspaper press plate crossed out |
| `achievement_fury_sparkbreaker` | Sparkbreaker | visible | hard | Defeat a Fury country after it reaches major threshold | Fury world-end starts first | small flame crushed under boot or seal |
| `achievement_fury_three_extinguished` | Three Extinguished | hidden | very hard | During Evolution III, all three Fury countries are defeated before any becomes major | any Fury becomes major | three darkened campaign lamps |
| `achievement_fury_no_borderless_war` | No Borderless War | visible | very hard | Prevent Fury world-end after a Fury country reaches no-neighbor branch | world-end Fury flag set | world map with locked borders |
| `achievement_fury_pact_shattered` | Pact Shattered | visible | hard | Destroy the Fury Pact after Evolution II before it completes a shared objective | pact reaches major cooperation milestone | broken pact emblem |
| `achievement_fury_let_them_march` | secret | very hard | Let one Fury country conquer its local continent without joining its wars, then defeat it later | player directly wars Fury before no-neighbor branch | long marching column turning into a trap |
| `achievement_fury_containment_doctrine` | visible | hard | Keep every active Fury country below major threshold for a long high-chaos period | any Fury major super-event fires | doctrine folder and containment ring |

Need exact tracking during implementation:

- first victory fired per Fury country
- second scripted war started per Fury country
- Fury major threshold fired globally
- Fury world-end active
- Evolution III active with three Fury countries
- Fury Pact formed and defeated
- player was at war with Fury before no-neighbor branch for secret achievement disqualifier

Asset handoff:

- create completed icon direction first
- grey and not-eligible variants can follow the repo achievement pattern later
