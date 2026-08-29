# Industrial Boom specification, part 1: Core event and baseline lifecycle

## Catalog entry

- Event ID: `34`
- Event name: Industrial Boom
- Type: Minor Repeatable
- Status: To Be Reworked
- Chaos level: 1
- Cluster: Not assigned

## Event premise

A major country or player-controlled country experiences an abrupt industrial acceleration that exceeds the capacity suggested by its factories, labor force, infrastructure, and access to materials. Production lines fill, construction schedules shorten, new shifts appear, and firms accept orders that would normally take years to complete. The benefit begins immediately and remains large enough to alter the country's military and civilian plans.

The expansion is unstable. Every new order competes for labor, fuel, transport, machine time, credit, imports, and maintenance. These strains are gathered into one public value, `Overheating`. The country may use the boom as a short power window, convert it into lasting development, or push the system into Event 35 Great Depression 2.0.

The event should feel generous before it becomes urgent. The player must have time to exploit the initial opportunity, observe the first signs of strain, and choose a management philosophy. A target that receives only a brief bonus followed by an unavoidable punishment would fail the premise.

## Core player experience

The event creates five linked experiences.

1. **Immediate abundance**
   - The first day changes production and construction priorities.
   - Existing lines accelerate enough to matter in an active war.
   - New lines become viable because production efficiency grows rapidly.
   - Civilian construction and industrial expansion become attractive.

2. **Visible strain**
   - Overheating rises according to the country's decisions and material condition.
   - The player sees the current band, trend, and next threshold.
   - The game explains the strongest actionable causes without exposing a full formula.

3. **Competing uses of the boom**
   - Running the economy harder gives more short-term output.
   - Stabilization consumes logistics and civilian capacity.
   - Reserves sacrifice current performance for shock protection.
   - Regional investment can produce lasting gains if the landing succeeds.

4. **A landing problem**
   - The boom does not end because a hidden timer expires.
   - The country must become structurally ready to leave the extreme phase.
   - A controlled landing preserves part of the transformation.
   - A forced or failed landing can leave exhaustion or activate Event 35.

5. **Campaign memory**
   - Repeat firings remember earlier booms, protected regions, exhausted states, permanent gains, and previous crashes.
   - A country can benefit more than once, but repeated booms produce diminishing permanent returns and greater fragility.

## Target selection

Each normal firing selects one country from a valid target pool.

### Eligible countries

A country is eligible when all of the following are true:

- It exists.
- It is a major country or is controlled by a human player.
- It uses ordinary civilian and industrial systems.
- It controls at least one populated, valid state with civilian or military industrial capacity.
- It does not have an active Industrial Boom.
- It is not in the unresolved handoff between Event 34 collapse and Event 35 activation.

A player-controlled non-major remains eligible. The event should scale to that country's real economy and avoid costs or permanent rewards sized for a great power.

### Excluded countries

Special Chaos actors and actual nonhuman countries should not receive the event through ordinary selection. Their economies may not use normal labor, credit, consumption, logistics, or civilian production assumptions. A later owning event may create a specific adapter when a special actor genuinely needs the mechanic.

A country with Event 35 already active remains eligible only when the Industrial Boom design can coexist with that depression. The default rule is exclusion. An independent boom should not erase an active depression or create contradictory modifiers. A later Event 35 specification may define a rare recovery-boom interaction, but Event 34 does not assume it.

### Target weighting

Every valid country needs a nonzero path to selection. Weighting should produce variety without making the same largest major dominate.

Weight can rise with:

- Substantial existing civilian and military industry.
- High infrastructure and a connected rail network.
- Strong production efficiency and stable trade access.
- High stability.
- A major war that creates strong industrial demand.
- A human player who has not recently received the event.

Weight can fall with:

- A recent Industrial Boom firing in the same country.
- An earlier Event 34 crash.
- Severe infrastructure loss.
- A blockade or sustained convoy crisis.
- Very low stability.
- Loss of a large share of core industry.
- Another active event-owned economic crisis that would create a conflict.

The weighting should not preselect the easiest country. Weak logistics can still receive the event and face a dangerous version of the management problem. The weighting only prevents obviously invalid or repetitive outcomes.

### Impossible target pool

When no valid country exists, Event 34 contributes no live candidate to normal selection and should appear as unavailable in the event list. It should not queue against a dead or invalid tag and should not display a misleading zero weight as though it were merely unlikely.

## Opening sequence

### World event entry

The global Event 34 firing chooses the target and records the event once. The affected country then receives the player-facing opening and the active economic package. The target country becomes the actor shown in Event History.

The opening should communicate speed through concrete industrial evidence:

- Lines that had months of backlog begin clearing orders.
- Rail yards and ports operate at full capacity.
- Construction crews work multiple shifts.
- Factory owners, ministries, unions, military procurement offices, and local authorities compete for workers and materials.
- New industrial districts appear around existing centers.

The opening should not present the boom as a mysterious magical gift at baseline. The cause remains uncertain because no single policy explains the scale, but the visible mechanism is industrial mobilization and investment. Later evolutions can make the expansion physically impossible.

### Immediate package

On the first day, the target receives an extraordinary temporary country effect. Exact HOI4 values require implementation tuning. The functional target is more important than one literal modifier.

The opening package should:

- Raise effective military factory output sharply.
- Raise civilian construction speed sharply.
- Accelerate production-efficiency growth.
- Raise the useful production-efficiency ceiling when the engine behavior supports it cleanly.
- Improve repair and conversion capacity enough to support expansion.
- Improve dockyard output for countries with a meaningful naval industry, at a lower relative rate than land production unless the country is strongly maritime.
- Make new production lines and large construction queues immediately attractive.

The intended total effect should feel roughly comparable to doubling the country's practical industrial productivity after normal stacking and bottlenecks are considered. The implementation should not simply apply `+100%` to every industrial modifier. That would interact unpredictably with laws, spirits, technologies, and other events.

### Starting Overheating

The boom begins below the first dangerous threshold. Starting Overheating varies by the target's real condition.

Lower starting pressure is appropriate when the country has:

- Strong infrastructure and rail coverage.
- High stability.
- Fuel and convoy security.
- A broad industrial base spread across several states.
- Accessible resources and stable imports.
- No recent Event 34 history.

Higher starting pressure is appropriate when the country has:

- Concentrated industry in a few vulnerable states.
- A blockade or severe convoy shortage.
- Damaged infrastructure.
- Low stability.
- Lost industrial cores.
- A recent boom or depression history.
- An evolved opening.

A baseline opening should normally begin in the stable band. The target must receive a real period of benefit before normal drift alone creates danger.

### Initial Industrial Regions

The opening identifies a small number of existing industrial states as the first centers of the boom. These are not yet permanent Miracle Regions. They provide state-level anchors for reports, protection, incidents, and later projects.

Selection should prefer:

- Controlled core states.
- States with civilian or military factories.
- States with usable infrastructure.
- States connected to the capital or a supply network.
- States with enough population to support industrial activity.

Selection should avoid:

- Impassable or unpopulated states.
- States controlled by another country.
- Isolated holdings that cannot plausibly support the main economy.
- States already exhausted by a previous boom unless no better state exists.

The number of initial regions scales with the economy, from one for a small player country to a small capped group for a large major. The player should never need to manage a long list of industrial state counters.

## Baseline lifecycle

The baseline lifecycle has four ordinary phases. These phases are not evolutions and should not appear as evolution records.

### Phase 1: Ignition

The event has just fired. The full opening bonus is active. Overheating is low enough that ordinary management actions are optional.

Player priorities:

- Reorganize production.
- Begin high-value construction.
- Decide whether to push the boom harder.
- Inspect the first Industrial Regions.
- Begin reserves or protection before visible danger.

Available content:

- Run the Economy Hot.
- Stabilize Supply Chains.
- Build Industrial Reserves.
- Protect Key Industrial Regions.
- One early project or survey action that identifies where lasting development is possible.

The opening phase should last long enough for production changes to matter. It ends through accumulated pressure and structural progress, not a fixed day count.

### Phase 2: Expansion

The boom has become a national economic condition. The country is still receiving extreme benefits. More contracts, construction, migration, and regional pressure appear.

Player priorities:

- Choose which industrial centers deserve lasting investment.
- Balance output against infrastructure and transport.
- Build reserve capacity.
- Decide whether another short acceleration is worth the added pressure.

Available content:

- All core management actions.
- Region designation and protection.
- Project work that can later become permanent legacy.
- Supply and logistics objectives.
- Evolution-specific incidents when enabled.

The best path through this phase builds both structural progress and a safety margin. A player who only lowers Overheating without completing any structural work should land safely but retain little.

### Phase 3: Strain

Overheating has entered a dangerous band or the economy has suffered repeated shocks. The extraordinary bonus begins to lose some efficiency. Shortages, maintenance debt, labor exhaustion, and speculative pressure become visible.

Player priorities:

- Stop avoidable shocks.
- Protect or abandon fragile projects.
- Complete reserves.
- Prepare a controlled landing.
- Choose whether wartime need justifies a final period of maximum output.

Available content:

- Strong cooling action.
- Emergency supply stabilization.
- Speculative liquidation when Evolution I is active.
- Emergency protection or project suspension.
- Controlled Landing preparation once structural conditions are met.
- Forced Landing when the crisis is close to collapse.

The event should not remain a pure positive modifier in this phase. High pressure should reduce part of the output bonus, increase disruption, and make further pushing less efficient. This prevents a player from treating a near-crash economy as a free permanent maximum-output state.

### Phase 4: Landing or collapse

The boom resolves through one of four result bands.

#### Controlled landing

The country completes the landing objective with Overheating under control and enough structural preparation. The extraordinary bonus ends in stages. Completed projects convert into lasting or long-duration gains. Reserve strength reduces disruption during the transition.

#### Rough landing

The country exits before terminal collapse, but pressure remains high or structural preparation is weak. Most temporary benefits disappear. The country receives temporary exhaustion, keeps only limited legacy, and may begin with a mild risk of later Event 35 activation if a new shock occurs during the recovery period.

#### Forced landing

The player or AI uses an emergency shutdown near the terminal threshold. The action prevents immediate full collapse at a heavy price. Projects may be cancelled, temporary output falls sharply, stability is strained, and a long exhaustion period follows. Event 35 is avoided only when the forced-landing calculation succeeds.

#### Economic crash

Overheating reaches the terminal threshold or a late catastrophic shock exceeds the remaining safety margin. All boom-only benefits end. Event 34 freezes its result snapshot and hands the same country into Event 35. Evolution inheritance follows the active Event 34 level.

## Outcome quality

The landing outcome should derive from several factors. One final Overheating reading cannot decide it.

Positive factors:

- Low or falling Overheating.
- Completed industrial projects.
- Strong reserve status.
- Protected regions that remain controlled.
- Stable supply and trade access.
- High infrastructure in the main Industrial Regions.
- A sustained period below the danger band.
- No recent major boom accident.

Negative factors:

- High or sharply rising Overheating.
- Cancelled or unfinished projects.
- Lost Industrial Regions.
- Repeated use of Run the Economy Hot near the danger threshold.
- A blockade or fuel crisis.
- Recent industrial accidents.
- A previous Event 34 crash.
- Evolution II or III fragility that was not consolidated.

The final outcome should be readable before commitment. The player should see a qualitative landing forecast such as strong, uncertain, or dangerous. Exact hidden probability components need not be shown.

## Repeatability

Event 34 remains Minor Repeatable. Repeatability changes the strategic context across firings and prevents an identical reward loop.

### Country memory

The event remembers:

- Number of prior Industrial Booms.
- Number of controlled landings.
- Number of rough or forced landings.
- Number of crashes into Event 35.
- Highest evolution previously reached.
- Permanent industrial legacy already retained.
- States that received legacy projects.
- States marked as exhausted by a failed boom.

### Later openings

A later firing may:

- Start with slightly higher Overheating.
- Offer fewer untouched states for permanent development.
- Make reserve construction more expensive.
- Make experienced regions easier to reactivate but less rewarding permanently.
- Unlock reports that acknowledge institutional memory.
- Let a country with a strong previous landing begin structural preparation faster.
- Give a country with a previous crash stronger political resistance to aggressive expansion.

Repeat history creates advantages and liabilities. A successful country learns how to manage a boom. Its easiest permanent gains have already been taken. A failed country recognizes the danger but carries fragile institutions and exhausted regions.

### Permanent reward ceiling

Repeat firings cannot create an uncapped factory and building-slot engine. Permanent legacy is bounded at country and state level.

- Each state has a campaign limit on permanent Event 34 legacy packages.
- Each country has a cumulative Event 34 legacy budget that scales with its original and current economy.
- Later projects increasingly favor timed efficiency, infrastructure, rail, repair, conversion, or resource-use improvements over additional factories and slots.
- A crash can damage unprotected earlier legacy and can consume part of the remaining country budget.

The event should still feel worth receiving again. The reward shifts from raw expansion toward faster mobilization, stronger logistics, better conversion, and safer use of an existing industrial base.

## Event flow map

```text
Normal event selection
  -> choose valid major or player country
  -> apply evolved opening when already unlocked and enabled
  -> opening report and extreme temporary boom
  -> initialize Overheating and Industrial Regions
  -> Ignition
       -> exploit output
       -> prepare supply, reserves, protection
  -> Expansion
       -> designate projects
       -> convert temporary growth into structural progress
       -> possible active-event evolution
  -> Strain when pressure rises or shocks accumulate
       -> stabilize and prepare landing
       -> force an early landing
       -> continue pushing for wartime gain
  -> resolution
       -> controlled landing
       -> rough landing
       -> forced landing
       -> crash into Event 35
  -> clean active Event 34 state
  -> retain bounded country and state memory
  -> restore repeatable eligibility after resolution cooldown
```

## Success standard

A successful Event 34 firing should leave the player able to answer four questions without reading hidden formulas:

- How hot is the economy now?
- Is pressure rising or falling?
- What is the next threshold?
- Which action best addresses the current cause or strategic goal?

The event succeeds as design when a player may rationally choose any of the following:

- Exploit a short wartime production window and accept a rough landing.
- Sacrifice current output to preserve a large permanent legacy.
- Use reserves and protection to survive external shocks.
- End the boom early because the country's strategic situation changed.
- Push too far and knowingly risk Event 35.

No one route should dominate every country and war state.
