# Industrial Boom specification, part 8: AI, probability, and balance

Named scenarios for every weighted surface live in the [AI and probability matrix](034_industrial_boom_ai_probability_matrix.md); this part owns the rules they test.

## AI goal

AI countries treat the boom as an economic bet: short-term output, lasting development and crash avoidance are different goals.
A cautious peacetime major, a well-supplied wartime power, a blockaded maritime country and a losing country that needs equipment now should behave visibly differently.
The AI pays the same costs, uses the same decisions and missions, and gets no relief the player cannot get.

## Profiles

A profile is chosen from the country's situation at each evaluation and can change.
It is internal and never shown to the player.

| Profile | Situation | Behavior |
| --- | --- | --- |
| Cautious consolidator | Peace or limited war, adequate equipment, high stability | Reserve early, protect the best region, rarely run hot, land once a project is Secured, contain Evolution III |
| Balanced developer | Moderate demand, stable logistics | One early hot window, one or two projects, stabilize in Strained, normal controlled landing |
| Wartime exploiter | Major war, equipment deficit, secure fuel and supply | Run hot while output matters, favor Factory Conversion, delay landing while the war needs output, cool when supply worsens |
| Desperate gambler | Losing a major war, threatened capital or core industry | Accept high-risk actions below Dangerous, may Let It Run, accept rough or forced landing; rare, and never once the output can no longer be used |
| Fragile retrencher | Blockade, fuel shortage, heavy damage, low stability or an earlier crash | Stabilize first, build a reserve, avoid running hot, land early, refuse speculative and Miracle offers without supply |

## Band behavior

| Band | AI behavior |
| --- | --- |
| Sustainable | May run hot with wartime demand, build a reserve, designate projects, protect exposed regions; never cools without a reason |
| Strained | Stops routine hot running except the wartime and desperate profiles, stabilizes the leading cause, starts the landing mission when a project is Secured |
| Dangerous | Cools, stabilizes, abandons weak speculative projects, starts the landing mission if below 70 is reachable; uses the Emergency Production Halt only when its success condition holds |
| Critical | Uses only actions with a credible path below 80; halts when the halt succeeds and the relief path does not |

## Decision scoring

Every score combines the band and trend, the leading cause, the expected Overheating change, affordability, war demand, project value, reserve and protection state, region exposure, landing readiness and cooldowns.
Scores compare marginal value, so Stabilize Supply Chains scores low when supply is not the leading cause.
Weighted logic should be centralized through MTTH variables per the `chaos-redux-mtth` skill rather than repeated in each `ai_will_do`.

### Project choice

Regions rank by industrial share, infrastructure, ports or resources, control stability and exposure to bombing or invasion, with lower rank for states already holding a strong legacy.
Profiles follow the bottleneck: Production Practices for low efficiency, Rail and Supply Integration for weak logistics or import pressure, Factory Conversion for line-switching needs and wartime capacity.
The AI does not put every project in the capital when another state is safer.

### Landing choice

The AI keeps the boom while war demand, low Overheating, a held reserve and a nearly Secured project outweigh the risk, and lands when a project is Secured, Overheating is rising, supply is weak, regions are exposed, the military need has passed, or it crashed before.
Cautious and balanced profiles start the landing mission before Dangerous.

## Weighted surfaces

| Surface | Current state |
| --- | --- |
| Target selection | Implemented as unweighted `random_country`; weighting pending (part 1) |
| Region ranking | Implemented as a random pick of one state; ranking pending (part 4) |
| AI decision and mission scores | Pending |
| Incident selection | Pending |
| Evolution pacing (MTTH) | Pending |
| Event 35 supplier contract AI | Implemented on the Event 35 side through `industrial_boom_supplier_adapter_is_safe` and `_is_overheated` |

Fairness goals for target selection: a player non-major has a meaningful chance, the same largest major does not take most firings, an active boom has zero weight, recent recipients and recent crashes are strongly lowered for two years, and strong and fragile economies both remain possible.

Evolution pacing goals: Evolution I does not normally arrive right after the opening, long hot booms bring it forward, the landing mission pauses it, a short boom may never evolve, and an evolved opening records no duplicate stage.

Incident goals: light incidents dominate low bands, evolution incidents need their stage and a valid target, protection lowers damaging weight, and a recent incident lowers its own repeat weight.

Every patched surface follows the project probability workflow: inspect the surface, declare the candidate pool and external factors, evaluate the named scenarios before and after, and compare with `hoi4.probability_analyze` (`analysis = compare`) when supported, or with calculations from the actual script when the analyzer cannot handle it.
Exact chances are reported only for complete candidate pools.

## Balance targets

### Opening package

A representative major should see a clear rise in monthly equipment output, faster ramp-up of a new line, and a construction queue finishing materially earlier, roughly comparable to doubling practical productivity.
Power is spread across factory output, efficiency growth, a modest efficiency cap, construction speed and dockyard output, without maximum values on any single modifier.
The balance pass compares practical output with representative technologies, laws and national spirits.

### Evolutions

Each stage changes the source of power: Evolution I raises output with faster pressure, Evolution II raises regional development and legacy potential, Evolution III gives the strongest temporary output with severe volatility.

### Duration

| Style | Typical duration | Typical result |
| --- | --- | --- |
| Early wartime exploitation | Several months | Strong output, rough or controlled landing |
| Balanced management | Half a year to a year | One or two legacy projects |
| Patient consolidation | Over a year while conditions stay sound | Best legacy within the budgets |
| Ignored Evolution III | One production campaign | Likely crash into Event 35 |

### Costs

A small player country can take every essential action, a major cannot trivialize an action with one train or one factory, emergency relief costs more than early preparation, and a reserve is cheaper than a crash.
Reject one resource paying for everything, political power as the universal answer, negligible fuel costs, civilian commitments a small country cannot carry, and full debits on partial outcomes.

### Legacy

A controlled landing is clearly better than an unprepared rough one, the best Evolution III landing feels campaign-defining, a crash never keeps legacy, and a major landing several booms over a long campaign stays strong but bounded by the budgets in part 4.

### Event 35 risk

A baseline crash disrupts war plans and needs active recovery; an Evolution III crash approaches paralysis without deleting the country; a held reserve and secured projects measurably soften the depression.

## AI acceptance

The AI passes when it finishes the boom without player-only actions, never runs hot in Dangerous or Critical, chooses projects that match its bottleneck, protects exposed valuable regions, lands after securing value in normal conditions, can make a deliberate wartime gamble, changes course after blockade or region loss, respects disabled evolutions, and produces no decision spam or repeated failed missions.
It fails when every country follows one route, one action dominates every scenario, it spends what it cannot afford, or it starts projects after the landing mission begins.
