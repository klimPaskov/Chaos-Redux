# Industrial Boom specification, part 2: Overheating

## The public value

Overheating is the only number the player manages during Industrial Boom.
It answers one question: how close is the boom to losing control?
It runs from 0 to 100, where 100 means the boom has failed and the Event 35 handoff begins.
The runtime variable is `industrial_boom_overheating`, already read by the implemented Event 35 supplier adapter and collapse snapshot.

The category shows exactly four things about it:

- the current value as an integer and its band name;
- the trend: rising, steady or falling;
- the next threshold and what changes there;
- the single leading cause, as a short phrase such as "rail network overloaded" or "speculative projects multiplying".

Everything else stays internal.
Reserve and protection state are shown as plain words in the header and region tooltips (parts 3 and 4), not as extra meters.

## Bands

Final values may move after balance testing, but the four-band structure stays.

| Range | Band | What changes | Main player response |
| ---: | --- | --- | --- |
| 0 to 39 | Sustainable | Full package, best project progress, only light incidents | Exploit output or build structure |
| 40 to 69 | Strained | One third of the output share of the package erodes, serious incidents enter the pool, Run the Economy Hot costs more | Stabilize, build a reserve, plan the landing |
| 70 to 89 | Dangerous | Two thirds of the output share erodes, Run the Economy Hot and new projects lock, Emergency Production Halt opens | Cool down or land early |
| 90 to 99 | Critical | Prevent the Crash starts automatically, only relief and emergency actions remain | Avoid the final threshold |
| 100 | Collapse | The boom ends and Event 35 inherits the frozen snapshot | Manage the depression |

Erosion reduces the output portion of the package (factory output and efficiency growth) and leaves construction speed until the Dangerous band, so the player still has a reason to finish projects while hot.

Leaving a band downward requires falling five points below its lower edge.
This stops one-day crossings from churning modifiers or farming threshold reports.
Each upward band entry sends one short report describing what physically changed; a band can report again only after the country has left it for at least 30 days.

## Starting value

| Opening | Typical start | Fragile start |
| --- | ---: | ---: |
| Baseline | 10 to 20 | 20 to 30 |
| Evolution I | 20 to 30 | 30 to 40 |
| Evolution II | 25 to 35 | 35 to 45 |
| Evolution III | 35 to 45 | 45 to 55 |

The start is derived from the target's condition, not rolled.
It rises with concentrated industry, blockade or convoy shortage, damaged infrastructure, low stability, lost industrial cores, and each earlier Event 34 crash.

The implemented entry seeds Overheating as 35 plus two per civilian factory, capped at 100, so a large economy can start in the Critical band.
That seed only feeds the Event 35 snapshot today and must be replaced by this table when the live Overheating model lands.

## Drift model

Overheating changes through a periodic evaluation of active boom countries only, plus immediate changes from actions, incidents and shocks.
The evaluation runs from the event-owned schedule of each active boom; it never scans every country.

The hidden model uses four drivers.
The largest current contributor becomes the visible leading cause.

| Driver | Raised by | Lowered by |
| --- | --- | --- |
| Output intensity | Run the Economy Hot, large construction queues, wartime demand, labor drawn into mobilization, Evolution III spread | Cooling, controlled landing, project abandonment |
| Supply and materials | Fuel deficit, train or convoy shortage, resource deficit, blockade, embargo, lost trade | Stabilize Supply Chains, restored trade, Rail and Supply projects |
| Regional strain | Low infrastructure in regions, damage or loss of a region, too many active projects, fragile Miracle Regions | Protection, completed integration, repair of damaged regions |
| Finance and maintenance | Long time in Strained or worse, speculative projects, repeated hot running, earlier crashes | Cooling, held reserve, landing preparation |

Strong logistics slow drift without removing it.
A self-sufficient land economy and an import-dependent maritime economy overheat for different reasons and pay different stabilization costs.

Intended pacing before player action:

- a baseline target with sound logistics reaches Strained after several months, not weeks;
- a baseline target with severe supply problems can reach Dangerous within one season;
- Evolution I needs active management within a few months;
- an ignored Evolution III boom reaches Critical within one production campaign.

## Shocks

External shocks change Overheating immediately, scaled by exposure:

- loss or occupation of an Industrial Region;
- heavy bombing, disaster or infrastructure damage in a region;
- blockade, convoy losses, fuel collapse or sudden trade loss;
- an accepted shock request from another event owner (part 7).

A destroyed port matters more to an import-dependent country, and loss of a state matters more when it holds a large share of national industry.

A held Industrial Reserve absorbs most of the next severe shock and is then spent (part 3).
A protected region absorbs most of its own local shock and loses its protection (part 4).
Neither makes a country immune to conquest or collapse.

## Incidents

Incidents connect the value to the world.
At most one incident fires per 60 days, tuned through a constant, and each closes after its response.
Each offers two or three responses that change Overheating, a region's project, output or stability.

Baseline pool:

| Incident | Minimum band | Typical responses |
| --- | --- | --- |
| Rail Congestion | Sustainable | Pay trains or trucks for relief, or accept slower projects |
| Material Shortfall | Strained | Pay for emergency imports with convoys or fuel, or let a project stall |
| Plant Accident | Strained | Repair and compensate, or keep the line running and raise Overheating |
| Labor Dispute | Strained | Concede with a temporary output loss, or force continued work at a stability cost |
| Maintenance Failure | Dangerous | Shut the plant for repairs, or run it and accept a severe shock later |

Evolution incidents are listed in part 5.

Selection follows the leading cause, the band, the active evolution, region protection and recent incidents.
An incident with no valid state target cannot fire, a landlocked country never receives a convoy branch, and the same state cannot receive an incident while its previous one is unresolved.
A protected region has a much lower chance of a damaging incident.

## Feedback

Every action that changes Overheating states its immediate direction, main cost, duration or cooldown, and output or project tradeoff.
When relief depends on conditions, the tooltip names the condition, for example that relief scales with the current supply problem.

## Tests

The mechanic passes when the value rises for understandable reasons, strong logistics slow it, aggressive output is worthwhile in some wars, cooling has a real opportunity cost, shocks matter in proportion to exposure, the value can recover from danger through timely action, and poor preparation can still fail.

It fails when Overheating behaves as a timer, one cheap action resets it repeatedly, the strongest output route is always correct, the safe route keeps the same reward as the risky route, random incidents decide the result regardless of preparation, or high pressure leaves the full package untouched.
