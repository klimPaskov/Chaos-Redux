# Event 064 AI Probability Scenario Matrix

This matrix defines expected preference order and invalid-choice behavior. It does not claim exact probabilities before implementation tools inspect complete option blocks and external modifiers.

All labels are working labels, not final localisation.

## Audit scope

The implementation-stage `chaosx_ai_probability_auditor` pass must inspect:

- every report posture option
- every decision `ai_will_do` or equivalent block
- every target-state and target-country candidate pool
- cluster-context modifiers
- evolution enablement and maturity conditions
- affordability and reserve floors
- country-specific external AI strategies
- war plans and front status
- special actor contracts
- repeated-wave and active-project state

The audit must use `fork_context=false` and receive the complete source paths, scenario definitions, and required rankings.

## Posture scenarios

| Scenario ID | Country state | Required valid options | Expected ranking | Near-zero or invalid | Reason |
| --- | --- | --- | --- | --- | --- |
| AI-064-P01 | peace, normal land frontier, adequate supply, no planned war | Integrate, Logistics, Breach only if fortified target exists | Integrate slightly above Logistics, bounded variation | Breach near zero without target | default use of local gift without inventing an offensive plan |
| AI-064-P02 | defensive war, capital one state from hostile frontier, weaker than enemy | Integrate, Logistics, Breach when counteroffensive target exists | Integrate dominant | Breach low, Observation invalid | immediate survival should override speculative plans |
| AI-064-P03 | defensive war, front supplied poorly, capital secure, long line | Integrate, Logistics, Breach when target exists | Logistics first, Integrate close second | Breach low | supply is the main constraint |
| AI-064-P04 | offensive war against target with level five or higher forts, home secure | all valid | Breach dominant | Observation invalid | direct need for counterplay |
| AI-064-P05 | offensive plan exists but support equipment and fuel are critically low | Integrate or Logistics if local line exists, Breach remains technically valid only when project reserve floors are met | Logistics or Integrate | Breach near zero or invalid | AI must not choose a posture whose main action it cannot support |
| AI-064-P06 | land-borderless island, no planned continental war, no Fortress World redoubt | Observation | Observation only | all three active postures invalid | no local or foreign use exists |
| AI-064-P07 | land-borderless island, valid invasion plan against fortified continental target | Breach, Observation | Breach dominant | Integrate and Logistics invalid | offensive study remains meaningful |
| AI-064-P08 | island, Fortress World capital redoubt, naval invasion threat | Integrate, Logistics, Breach when target exists | Integrate first, Logistics second | Observation invalid | local redoubt gives defensive use |
| AI-064-P09 | one-state minor threatened by stronger neighbor, small stockpiles | Integrate, Logistics if network target exists, Breach if target exists | Integrate dominant | projects can still be skipped | posture effect should remain useful even when project is unaffordable |
| AI-064-P10 | large continental major, several long borders, no immediate war, poor rail network | Integrate, Logistics, Breach when target exists | Logistics dominant | Observation invalid | network integration is the main value |
| AI-064-P11 | large continental major, strong rail network, several fortified likely enemies | all valid | Breach or Integrate according to active strategy | Observation invalid | existing logistics reduces Logistics value |
| AI-064-P12 | subject country with local fortified border and no independent war plan | Integrate, Logistics, Breach only through overlord war context | Integrate or Logistics | independent speculative Breach low | subject behavior should follow actual strategic freedom |
| AI-064-P13 | overlord with several subject borders and one hostile external front | all valid when targets exist | posture based on external threat, not subject borders alone | no blanket invalidation | relations do not change physical line, but threat drives use |
| AI-064-P14 | civil-war participant with active front and threatened capital | Integrate, Logistics, Breach | Integrate dominant unless a decisive offensive window exists | Observation invalid | survival and short front matter |
| AI-064-P15 | special Chaos actor with normal buildings but no normal civilian or equipment economy | owner-defined supported posture or Observation | owner contract | unsupported postures invalid | do not charge resources the actor does not use |
| AI-064-P16 | current response posture active from prior wave and no active project | all currently valid new report options | choose from fresh conditions, remove old weight memory except bounded continuity | Observation only if all active postures invalid | repeat wave should permit adaptation |
| AI-064-P17 | active Event 064 project from prior wave | valid postures based on current conditions | avoid posture whose access implies a conflicting new project until old project ends | no second active project | one-project cap must affect option value |
| AI-064-P18 | all local frontier positions capped, no evolved support gap, fortified enemy exists | Breach, possible Observation | Breach dominant | Integrate and Logistics low or invalid without useful action | avoid defensive posture with no material use |
| AI-064-P19 | Military Preparation cluster context and hostile neighbor mobilizing | all valid | increase Integrate and Breach according to current strategy | Observation invalid | context should strengthen readiness behavior without forcing one route |
| AI-064-P20 | Sudden Abundance context with trains and trucks recently granted | all valid | increase Logistics when a real network gap exists | no forced Logistics when network is already strong | use the actual member outcome, since the cluster label alone is insufficient |

## Project start scenarios

| Scenario ID | Posture or tier | Candidate state | Resources | Expected action | Required guard |
| --- | --- | --- | --- | --- | --- |
| AI-064-D01 | Integrate | capital-front state below fort cap | adequate | start Reinforce with high priority | one active-project cap |
| AI-064-D02 | Integrate | remote allied border state below cap, active enemy front elsewhere | adequate | choose enemy-front state instead | strategic target ranking |
| AI-064-D03 | Integrate | only candidate already at cap | adequate | skip project | physical-result validation |
| AI-064-D04 | Integrate | valid target | infantry equipment deficit | skip or use scaled minimum only if reserve survives | stockpile floor |
| AI-064-D05 | Logistics | key border state with damaged network | adequate trains and trucks | start Connect | network gap validation |
| AI-064-D06 | Logistics | network already at cap | adequate | skip | no false supply reward |
| AI-064-D07 | Logistics | valid gap | critical train shortage | skip | train reserve floor |
| AI-064-D08 | Breach | current enemy with high forts and active offensive | adequate | start Breach Exercises | target fort threshold and war-plan check |
| AI-064-D09 | Breach | current enemy with no meaningful forts | adequate | skip | no general-bonus farming |
| AI-064-D10 | Breach | high-fort target | low fuel and support equipment | skip | reserve floor and expected-use check |
| AI-064-D11 | Evolution II | industrial Fortress State under bombing | adequate | start air branch | threat and state-role check |
| AI-064-D12 | Evolution II | major border port under naval threat | adequate | start coastal branch | coast, port, and threat check |
| AI-064-D13 | Evolution II | inland state without air role | adequate | do not choose coastal or air action | role validity |
| AI-064-D14 | Evolution III | capital directly threatened | adequate | start National Redoubt | one-per-wave cap |
| AI-064-D15 | Evolution III | secure capital and exposed supply junction | adequate | choose supply redoubt when score clearly higher | target ranking with bounded variation |
| AI-064-D16 | Any | active project exists | adequate | start nothing else | global Event 064 project cap |
| AI-064-D17 | Any | target likely lost before duration ends | adequate | skip or choose safer target | control-risk forecast |
| AI-064-D18 | Any | target changes control after start | already committed | fail and clean up | no transfer or duplicate reward |

## Target ranking scenarios

| Scenario ID | Candidate set | Expected top band | Expected lower band | Invalid candidates |
| --- | --- | --- | --- | --- |
| AI-064-T01 | three border states, one protects capital, one industrial, one remote | capital approach and active hostile front | industrial then remote | state not controlled |
| AI-064-T02 | long border across several regions | one high-value candidate per region before second target in same region | repeated low-value state in already represented region | capped or invalid state |
| AI-064-T03 | coastal and inland Fortress States | threatened port and industrial air-defense state according to current threat | quiet low-value coast | strait-only state without land frontier |
| AI-064-T04 | several foreign fortified targets | current enemy and active war-goal target | neutral country without plan | ally, invalid tag, no forts |
| AI-064-T05 | capital, major VP, supply hub, and industry for redoubt | threatened capital first, then exposed supply hub or major VP | secure minor industry | invalid building site or already capped position |
| AI-064-T06 | fragmented colonial empire | high-value home target plus one distinct remote region when quota permits | several targets in one low-threat region | off-map and impassable sites |
| AI-064-T07 | civil war and foreign border candidates | active civil-war capital front | peaceful allied edge | same-controller boundary |
| AI-064-T08 | Event 23 or Event 32 strategic site states | threatened strategic site with valid border or redoubt role | unrelated empty border state | site marker without valid physical position |

## Expected ranking bands

Exact percentages remain implementation evidence. Use these acceptance bands after full calculation.

| Condition | Required result |
| --- | --- |
| dominant survival condition | preferred posture or target should receive at least a strong majority of final probability after all options and external factors |
| clear strategic advantage without emergency | preferred choice should lead by a meaningful margin but leave bounded variation |
| two close valid choices | neither should collapse to a token chance unless an external AI strategy resolves the tie |
| invalid choice | exact zero probability or hidden option |
| unaffordable project | exact zero start probability |
| project with no physical or target-bound result | exact zero start probability |
| observation when a meaningful active posture exists | near zero or unavailable according to report design |
| unsupported special actor action | exact zero probability |

The probability auditor should translate these qualitative bands into explicit numeric ranges after inspecting the full implementation.

## External factors to inspect

The audit cannot stop at local `factor` blocks. It must inspect:

- base option weight
- normalization across all report options
- generic AI aggressiveness
- ideology or country strategy plans
- war strategy and front status
- current national spirits
- difficulty settings
- current stockpiles and reserve logic
- cluster source modifiers
- evolution availability
- active decision and mission state
- target pool size
- invalid target filtering
- random-list normalization
- any shared country-specific override

## Sequence probability checks

Event 064 contains multi-step weighted behavior:

1. Event 064 is selected from the repeatable pool.
2. Zero, one, or two cluster memberships are eligible.
3. One cluster context or standalone route is selected.
4. The global transaction selects evolved candidates through weighted ranking and bounded random variation.
5. AI selects a posture.
6. AI decides whether to start a project.
7. AI selects a target.

The probability audit must inspect the full sequence and every local decision.

Questions to answer:

- Can Event 064's additional cluster membership occur at a meaningful rate?
- Can cluster arbitration accidentally double fire the event?
- Do high-value strategic candidates remain reachable after quota and dedupe rules?
- Does a minor defensive emergency produce the intended posture after project affordability is included?
- Does Breach remain chosen when its target pool is smaller than local defensive pools?
- Does bounded variation preserve replay without overriding urgent survival?
- Do repeated waves create target-memory bias that prevents new frontiers from being selected?

## Required tool evidence

When the configured probability MCP tools are available, the auditor should provide:

- inspected option and decision blocks
- final effective weights for each scenario
- normalized probabilities
- invalid-choice proof
- target-pool composition
- sweeps across key variables such as threat, fort level, supply, and stockpile reserves
- comparisons before and after tuning
- rendered tables or charts for posture and project choice where useful
- Monte Carlo or sequence simulation for cluster arbitration and target variety
- saved evidence paths

If the toolchain remains unavailable, the implementation report must state the blocker and withhold probability completion. Source inspection alone is not equivalent.

## AI acceptance failures

Fail the AI plan when any of these occurs:

- a capital emergency regularly selects Observation
- a supply crisis regularly selects Breach without a real offensive plan
- island countries select local defensive postures with no local line or redoubt
- AI starts projects with no valid physical result
- AI spends below required train, truck, convoy, equipment, or fuel reserves
- active-project cap is ignored
- target loss transfers a mission to the new controller
- allies or invalid tags remain in breach target pools
- one cluster membership is effectively unreachable
- random variation can override an urgent survival condition too often
- fixed exact probabilities are claimed without complete external-factor evidence
