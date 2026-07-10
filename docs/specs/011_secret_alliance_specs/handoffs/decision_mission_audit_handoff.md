# Decision and mission planning audit handoff

## Status by design surface

| Surface | Planning status | Main evidence |
| --- | --- | --- |
| Category lifecycle | Complete | Phase table in the decision matrix |
| Investigation | Complete | Eight mapped actions with evidence classes and risks |
| Counterintelligence missions | Complete | Seven timed or goal missions with full, partial, and failure outcomes |
| Protection | Complete | Eight maintained projects with concrete costs and opportunity costs |
| Diplomacy | Complete | Seven suspect and ally actions tied to motive and confidence |
| Deception and offensive counter-network | Complete | Eight actions including false plans, turning, conference disruption, and depot sabotage |
| Border system | Complete | Five-step limited conflict ladder with escalation boundary |
| Public exposure | Complete | Five actions with stronger Evidence thresholds |
| Evolution III emergency | Complete | Seven emergency actions |
| Revealed-war fracture | Complete | Seven actions tied to Resolve and motive |
| AI equivalence | Complete at design level | AI matrix and prompt |
| Cleanup | Complete at design level | Category and target lifecycle rules |
| Localisation | Direction complete, final copy pending implementation | Localisation handoff |
| Assets | Fully registered for planning | Asset register |

## Strengths

- Costs use equipment, XP, fuel, trains, convoys, factories, units, stability, credibility, and access.
- Major missions require action in named states or regions.
- Full, partial, and failure outcomes change later play.
- Evidence uses independent classes and corroboration.
- Suspects use confidence bands.
- False accusations have recoverable first mistakes and escalating consequences.
- The category uses active caps and selected-target flow.
- Border action remains distinct from normal war until escalation.
- Revealed-war decisions use prewar knowledge and motive instead of generic war bonuses.

## Implementation risks to audit

1. Political power becoming the only coded cost despite the mapped resource model.
2. Missions auto-completing from passive conditions present at activation.
3. Duplicate investigation decisions with different names but identical effects.
4. Selected-target flags remaining on invalid countries.
5. AI seeing only the human-selected suspect.
6. Evidence being farmed from repeated low-quality clues.
7. Preparedness becoming a permanent uncapped stack.
8. Public accusation granting cheap war goals.
9. Border conflict accidentally satisfying the normal-war reveal condition.
10. Turned-channel success being reduced to an immediate modifier with no later consequence.
11. Severe sabotage repeating without recovery windows.
12. Decision category showing every possible region and country at once.

## Required implementation audit scenarios

- confirm one full, partial, and failed courier mission
- confirm one innocent suspect path and credibility recovery
- confirm repeated false accusation escalates consequences
- confirm a turned member survives to reveal and changes the war opening
- confirm a selected suspect dies or changes faction and cleans up
- confirm an island target receives maritime actions instead of invalid border actions
- confirm a border conflict does not reveal until normal war begins
- confirm an AI target can use all critical actions without GUI clicks
- confirm category conversion at reveal preserves relevant missions and closes obsolete ones
- confirm postwar cleanup removes target and member decisions

## Verdict

The decision and mission design is deep enough for implementation. Broad expansion is not recommended before a first implementation pass. Auditors should focus on fidelity, dynamic costs, mission quality, cleanup, and AI rather than adding another decision family.
