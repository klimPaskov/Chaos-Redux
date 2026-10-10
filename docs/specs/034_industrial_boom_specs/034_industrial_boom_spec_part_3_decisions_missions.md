# Industrial Boom specification, part 3: Decisions and missions

None of this layer is implemented yet; the implemented stub has no decision category (README, implementation status).

## Category role

Industrial Boom uses one decision category for the affected country, from the opening until cleanup.
It is a management surface, not a shop.
Its presentation (header lines, picture and texticons) is defined in part 9.

The national list shows at most five rows: the core actions valid in the current band, one evolution action, the active mission and the Emergency Production Halt when it applies.
Each Industrial Region adds at most one row, its single most relevant action: Designate an Industrial Project when it has no project, Protect an Industrial Region when it has a project and no protection, and Abandon a Project only when the project is threatened or the band is Dangerous or worse.
With the three-region cap the category therefore stays at eight rows or fewer, and normally shows five or six.
Actions that are invalid for the current band, lifecycle state or evolution are hidden rather than shown disabled, except Run the Economy Hot, which stays visible with its lock in the Dangerous band so the player learns the rule.

The phase-by-phase visibility table lives in the [decision map](034_industrial_boom_decision_map.md).

## Costs

Costs scale with the country's civilian and military factory count and the current band, so a small player country can afford every essential action and a major feels the commitment.
Each action uses at most three spendable cost types.
Costs favor trains, trucks, convoys, fuel, support equipment, temporary civilian-factory commitments and temporary output sacrifice.
Political power appears only on actions that represent coercion, such as forcing continued work during an incident.
Stabilize Supply Chains picks its transport cost from the country's real profile: a landlocked country never pays convoys, and an import-dependent maritime country cannot stabilize with trains alone.
Costs are validated before payment, and a rejected target or failed transaction refunds what was paid.
Every displayed cost uses the matching texticon.

## Core actions

### Run the Economy Hot

Firms, ministries and procurement offices accept every order and defer maintenance.

- Available in the Sustainable and Strained bands; locked from Dangerous upward and during the Landing state.
- 60-day active period, cannot overlap itself or Cool the Expansion, 30-day cooldown after it ends.
- Gives a strong temporary boost to factory output, efficiency growth and project progress.
- Adds Overheating at once and raises Output intensity drift for the period; in the Strained band the immediate cost is higher and the project boost is lower.
- Under Evolution I the immediate cost is lower and the drift higher, because confidence feeds itself.

Its real price is risk, not equipment.
Early use is efficient and late repeated use is reckless.

### Stabilize Supply Chains

Transport and procurement authorities commit scarce movement capacity to the worst links.

- Available in every band before collapse, with a 45-day cooldown.
- Pays trains or trucks, fuel, and convoys only when the country depends on sea routes.
- Relief scales with the Supply and materials driver: large when that driver leads, small when it does not.
- In the Dangerous and Critical bands the same decision costs more, gives more relief, and protects against the next supply shock for 30 days. This replaces a separate emergency logistics decision.
- Partial relief is explained: a blockaded country sees that relief is reduced while the blockade lasts. Full costs are never paid for silent nothing.

### Build an Industrial Reserve

The country deliberately leaves machine time, spare parts and repair stores unused.

- Available in the Sustainable and Strained bands when no reserve is held.
- Costs a 90-day output reduction and a civilian-factory commitment for the same period.
- Lowers Overheating slightly at once and gives the country one held reserve when the period ends.
- A held reserve absorbs most of the next severe shock, improves landing legacy, and is passed to Event 35 as reserve units.
- When the reserve absorbs a shock it is spent, and a new one can be built after a 90-day cooldown.

The header shows the reserve as one word: none, building, held or spent.

### Cool the Expansion

The government restrains credit, delays contracts and reduces shifts.

- Available in the Running state; in the Opening state only if Overheating started at 40 or above.
- 60-day active period, cannot overlap Run the Economy Hot.
- Suppresses most of the package's output share for the period and slows projects.
- Gives a large immediate reduction and lowers drift for the period.
- Under Evolution I it becomes Impose Credit Restraint: the same mechanics plus a stability cost, and it also clears the speculative contribution to the Finance driver.

Cooling is the safest large relief and has the highest opportunity cost.

## Region actions

These rows target one Industrial Region at a time (part 4).
The player sees only current regions, never every controlled state.

### Designate an Industrial Project

Choose one region without a project and one profile: Production Practices, Rail and Supply Integration or Factory Conversion (part 4).

- Locked from Dangerous upward and during the Landing state.
- Costs a civilian-factory commitment for the project's Building stage plus trains or support equipment by profile.
- Adds a small amount of Regional strain while the project is active.
- Does not grant buildings or slots by itself; it opens a path to legacy at landing.

### Protect an Industrial Region

Harden one region with repair stores, alternative transport and civil defence.

- One protection per region at a time; renewable 90 days after it is spent.
- Costs a civilian-factory commitment, support equipment and trains or trucks.
- A protected region absorbs most of its next local shock and keeps its project progress, then loses its protection.
- Protection does not survive the state leaving the country's control.

### Abandon a Project

Cancel a project that can no longer be supported.

- Removes its pressure and gives immediate relief; a speculative project gives larger relief (this replaces a separate liquidation decision).
- Loses the project's progress and leaves an unfinished-works state modifier for one year.
- A project cancelled after state loss is removed automatically without this decision.

## Evolution actions

Each evolution adds at most one decision row.

- Evolution I: Approve a Speculative Expansion (part 5).
- Evolution II: Declare a Miracle Region (part 5).
- Evolution III: Contain the Spread (part 5); the spread policy itself is chosen in the evolution event.

## Missions

### Prepare a Controlled Landing

The main resolution objective, started by decision.

- Requires the Running state and Overheating below 70.
- Lasts 120 days, shortened by 30 for a country with an earlier controlled landing and lengthened by 30 under Evolution III.
- While active, Run the Economy Hot and new projects close, and evolution pacing pauses.
- The category lists the checklist: stay below 70, keep the project regions controlled, finish or abandon active projects.
- Success resolves the outcome from part 1: controlled below 40 with a secured project, otherwise rough.
- Rising to 70 or losing every project region cancels the mission, returns the country to Running, and starts a 60-day cooldown.

### Prevent the Crash

An emergency objective that starts automatically on entering the Critical band.

- 60 days to fall below 80.
- Success returns the country to Running and blocks Run the Economy Hot for 90 days.
- Failure is a crash into Event 35.

## Emergency Production Halt

The last-resort forced landing, available in the Dangerous and Critical bands.

- Ends the package and every active action at once, cancels all projects without legacy, and applies a long exhaustion modifier.
- Succeeds when the country holds a reserve, or when Overheating is below 90 and at least one region is protected.
- Otherwise it fails and the country crashes into Event 35, with the failed landing recorded in the snapshot.
- The decision tooltip states which of those conditions currently holds, so the outcome is known before the click.

## AI

The AI uses the same decisions, missions, costs and outcomes, scored by the profiles in part 8.
No action depends on a human-only path, and the AI receives no relief the player cannot get.

## Cleanup

When the boom ends:

- every Event 34 decision, mission and target marker closes;
- temporary commitments are released and timed action modifiers end;
- the reserve converts to landing value, or to Event 35 reserve units after a crash;
- the frozen snapshot is delivered to Event 35 before active state clears (part 6);
- only the country and state memory listed in parts 1 and 4 remains.
