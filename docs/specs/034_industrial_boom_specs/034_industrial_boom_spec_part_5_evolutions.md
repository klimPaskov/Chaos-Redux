# Industrial Boom specification, part 5: Evolutions

No evolution is implemented yet.
The implemented entry always records evolution 0, so every current collapse enters Event 35 at baseline.

## Structure

| Stage | Name | Unlocks at | Core change |
| ---: | --- | --- | --- |
| I | Speculative Mania | Rising Chaos | Credit and confidence make the boom stronger and harder to restrain |
| II | The Industrial Miracle | Chaos Tier | Chosen regions develop faster than material limits allow |
| III | Runaway Industrialization | Totalen Chaos | Industry spreads into neighboring states and becomes volatile |

The stage number is stored in `industrial_boom_evolution` on the same 0 to 3 scale as Event 35's `great_depression_evolution` constants, because the collapse request passes it unchanged as the Event 35 evolution floor (part 6).

The world threshold makes a stage possible; it does not apply it.
Each stage is independently controlled by the shared evolution enable system, and a higher stage requires the lower stages.
A stage disabled during an active boom stays in effect for that boom if already applied and cannot newly apply.
Evolution activation gives no Chaos (part 7).

## Two entry paths

**Active entry.** An active boom in the Running state evolves through MTTH pacing centered on 90 days.
Pacing speeds up with long time in Strained or worse, repeated hot running, several active projects, wartime equipment demand, and global Chaos well above the threshold.
It slows when Overheating is low, cooling is active or the boom fired recently.
It pauses entirely while Prepare a Controlled Landing is active.
Active entry sends one evolution report, records the stage in the shared evolution log with the target as actor, and never resets Overheating or the lifecycle.

**Evolved opening.** A new firing after a stage is unlocked and enabled starts at that stage, with the higher starting Overheating from part 2 and the stage's opening content.
It records no new evolution log row, because the stage was already active before the firing.

## Evolution I: Speculative Mania

Firms announce projects before materials exist, banks treat future capacity as present wealth, and everyone resists anything that slows orders.
It stays grounded in recognizable economic behavior.

On entry:

- the package's output share grows by about a quarter;
- speculation becomes a large part of the Finance and maintenance driver;
- Cool the Expansion becomes Impose Credit Restraint, with a stability cost (part 3);
- the first speculative offer arrives within 30 days.

**Approve a Speculative Expansion** offers one named project in a named region, matched to the country: a factory district, a port and yard expansion for a coastal region, or a rail and depot network for a continental one.
Approving it starts a project in that region directly at the Integrating stage, with a legacy one step stronger than its profile normally gives, and adds a large Finance contribution until it is Secured or abandoned.
Abandoning a speculative project gives large relief (part 3).
Only one speculative project can exist at a time, and a new offer arrives at most every 120 days.

Incidents:

| Incident | Choice |
| --- | --- |
| Order-Book Frenzy | Force priorities and lose output, or let delays pile up and raise Overheating |
| The Profitable Shell | Expose a speculative project and lose its progress, or keep backing it and add pressure that will surface later |
| Restraint Backlash | Hold credit restraint at a stability cost, or weaken it and keep less relief |

A Speculative Mania crash enters Event 35 at Financial Contagion and passes higher shock evidence for each live speculative project.

## Evolution II: The Industrial Miracle

Railways, plants and districts appear faster than engineers can explain.
The miracle stays tied to named regions and player choices.

On entry, every region with a project can be declared a Miracle Region, and the first evolution report shows one physically abnormal result in a named state.

**Declare a Miracle Region** upgrades an existing project:

| Base profile | Miracle form | Raised legacy ceiling |
| --- | --- | --- |
| Production Practices | Automated Production Control | Stronger and longer national efficiency legacy, lower drift in later booms |
| Rail and Supply Integration | National Rail Spine | Railway and infrastructure in the region and one adjacent state |
| Factory Conversion | Machine-City | Larger factory or slot reward, still inside the country budget |

A Miracle project progresses about twice as fast and doubles its Regional strain contribution.
When Overheating is 70 or above, a Miracle Region is Fragile: an unabsorbed shock there sends the project back a stage.
A player may refuse every declaration and land an evolved boom conventionally with smaller rewards.

Incidents:

| Incident | Choice |
| --- | --- |
| The Railway Completed Overnight | Inspect it before use and slow the project, or put it into service and accept fragility |
| Materials That Should Not Exist | Use the unaccounted components for progress, or quarantine them and lose time |
| The Impossible Schedule | Exploit the output and raise Overheating, or restrict the region to its rated capacity |

The first Miracle project to reach Secured is the stage's concrete abnormal outcome and can add guarded Chaos (part 7).

A crash with live Miracle Regions enters Event 35 at Social Collapse and marks those regions as fragile depression centers through the region contract (part 6).

## Evolution III: Runaway Industrialization

Industry spreads from existing centers into neighboring states faster than administration can follow.

On entry the evolution event asks for the spread policy:

| Option | Effect |
| --- | --- |
| Direct the Spread | One adjacent state per region may expand; moderate pressure; spread states can integrate and receive legacy |
| Let It Run | Every valid adjacent state expands; strongest output; large Output intensity and Regional strain; spread states cannot receive permanent legacy |
| Contain It | No spread; temporary output loss and stability cost; best landing forecast |

**Contain the Spread** remains available afterwards to switch from either spreading policy to containment once.
Containment cannot be reversed for that boom.

A valid spread state is owned, controlled, core, passable, populated, adjacent to its region, not on an active front unless Let It Run is chosen, and not under a severe disaster or contamination condition.
Each spread state shows one of two statuses, expanding or integrated, through a state modifier.
Spread states contribute to their region's project and never create new project slots or legacy receipts of their own.

Incidents:

| Incident | Choice |
| --- | --- |
| The Unplanned Works | Recognize the new works and add pressure, or dismantle them and lose output |
| The Railway That Keeps Growing | Integrate the line for a logistics gain, or leave it and raise Regional strain |
| Network Cascade | Spend a held reserve to contain it, or let it pass and take a severe shock across connected states |

Exceptional Evolution III landings, with directed spread, integrated spread states and low final Overheating, are the strongest legacy the event can give, and still sit inside the budgets of part 4.

A Runaway crash enters Event 35 at The Second Great Depression with the inherited-worldwide severity profile, and its spread states are passed as regional corridor inputs where the region contract allows them (part 6).

## AI

- Cautious and fragile profiles cool or contain, and refuse speculative and Miracle offers without secure supply.
- Balanced profiles accept one speculative project at low Overheating, declare Miracle Regions only with a held reserve, and choose Direct the Spread.
- Wartime and desperate profiles may choose Let It Run below the Dangerous band.
- No AI approves a second speculative project or keeps spreading in the Critical band.

## Text direction

- **Speculative Mania**: official confidence, announcements ahead of inputs, resistance to restraint; mild irony in small incidents, none in failures.
- **The Industrial Miracle**: engineers and inspectors facing finished work that should have taken years and missing material records; technical wonder with unease; no religious or supernatural explanation.
- **Runaway Industrialization**: local authorities and planners chasing works beyond the approved plan; concrete and administrative under pressure; the industry is never described as alive.

## Acceptance

- Each stage changes decisions, incidents, regional behavior, AI and the Event 35 floor, not only modifier size.
- Active booms evolve without a new firing, and evolved openings record no duplicate log row.
- Disabled stages leak no state and never block baseline resolution.
- Evolution II and III can be landed without collapse.
- The safest route gives less maximum legacy than the risky route.
