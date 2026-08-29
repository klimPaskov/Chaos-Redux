# AI probability scenario contract

## Required evidence fields

Every scenario result records:

- scenario ID
- analyzed source surface
- source revision or hash
- candidate pool completeness
- external-state completeness
- exact, bounded, sampled, score-only, or unresolved result type
- effective score or probability ordering
- timing result when applicable
- diagnostics
- intended ordering
- pass, fail, or unresolved verdict

## Participation scenarios

| ID | Actor state | Expected ordering |
| --- | --- | --- |
| P01 | Peaceful maritime major, strong reserves, missing tech | Highest ordinary participation band |
| P02 | Major at total war, convoy and fuel pressure | Lower than P01 |
| P03 | Human landlocked minor | Offered entry without probability roll |
| P04 | AI minor with perfect southern access | Ineligible under ordinary roster |
| P05 | Valid Kruger State | Eligible exception, below an otherwise stronger ordinary major when resources differ sharply |
| P06 | All base techs owned, upgrades missing | Still meaningful candidate |
| P07 | Full external pool owned | Lower reward need but not forced zero |
| P14 | Seven human entrants | AI roster reduced, humans preserved |

## Action scenarios

| ID | State | Expected dominant family |
| --- | --- | --- |
| A01 | Mobilization, readiness below departure threshold | Logistics and route preparation |
| A02 | Survey, readiness stable, no sector probable | Survey actions |
| A03 | Survey, rival leads, actor has intelligence capacity | Intelligence or targeted defense |
| A04 | Critical readiness, high progress | Resupply, not final recovery |
| A05 | Final sector confirmed, safe readiness | Final recovery preparation |
| A06 | Final sector confirmed, desperate losing war | Riskier final recovery may become valid |
| A07 | Evolution IV, actor trails badly | Fragment recovery |
| A08 | Evolution IV, actor leads | Core recovery or stabilization |
| A09 | Evolution V, stable high-capacity country | Containment or controlled integration |
| A10 | Evolution V, collapsing country | Emergency transfer, containment, or risky integration according to capacity |

## Rival-target scenarios

| ID | Candidate set | Expected target |
| --- | --- | --- |
| R01 | One leader, two weak laggards | Leader |
| R02 | Leader heavily defended, second place exposed | Second place may dominate when action value is higher |
| R03 | Previous attacker and unrelated leader | Retaliation factor matters without overriding race relevance automatically |
| R04 | Human and AI tied in state | No player-status factor |
| R05 | Selected target withdrawn | Weight zero and target cleared |
| R06 | Same sabotage on cooldown | Weight zero |

## Timing scenarios

| ID | Conditions | Design expectation |
| --- | --- | --- |
| T01 | Prepared nearby power, low chaos, no evolutions | Lower completion band, still several phases |
| T02 | Distant major, ordinary hazards | Longer than T01 |
| T03 | Several hostile actions | Delay without indefinite stall |
| T04 | All evolutions disabled | Full race still resolves |
| T05 | Evolution I direct tracking | Faster search, higher failure variance |
| T06 | Evolution III heavy militarisation | Longer route and outpost phases |
| T07 | Evolution IV fragmentation | More partial rewards, core still claimable |
| T08 | All participants resource constrained | Withdrawal or no-winner closure becomes plausible |

## Audit sequence

```text
probability_inspect
  -> confirm complete candidate pool
  -> evaluate named scenarios
  -> sweep sensitive factors
  -> simulate only when exact resolution is not available and sampling is justified
  -> render ordering, timing, or sensitivity evidence
  -> owner applies patch
  -> probability_compare with same scenario IDs
```

## Hard failures

- human participation receives a random weight
- invalid AI minor enters ordinary roster
- critical-readiness AI launches ordinary final recovery
- one sabotage action retains weight during cooldown
- weakest irrelevant rival dominates every hostile target pool
- full technology ownership produces a zero-value winner reward
- disabled evolution still changes AI weights
- candidate pool is incomplete but result is reported as exact
