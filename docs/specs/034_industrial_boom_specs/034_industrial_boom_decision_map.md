# Event 34 Industrial Boom decision map

## Phase and action map

| Action or objective | Ignition | Expansion | Visible Strain | Dangerous Imbalance | Pre-crash | Landing |
| --- | --- | --- | --- | --- | --- | --- |
| Run the Economy Hot | Available | Available | Conditional | Hidden | Hidden | Hidden |
| Stabilize Supply Chains | Available | Available | Available | Available | Emergency version | Conditional |
| Build Industrial Reserves | Available | Available | Available | Rebuild only | Emergency use only | Hidden |
| Cool the Expansion | Conditional | Available | Available | Strong version | Emergency halt path | Active landing effect |
| Protect Key Industrial Regions | Available | Available | Available | Repair current regions | Emergency repair only | Complete current work |
| Survey Lasting Capacity | Available once | Hidden after completion | Hidden | Hidden | Hidden | Hidden |
| Designate an Industrial Project | Conditional | Available | Conditional | Hidden | Hidden | Hidden |
| Suspend a Fragile Project | Hidden | Conditional | Available | Available | Available | Conditional |
| Abandon a Project | Conditional | Available | Available | Available | Available | Conditional |
| Approve a Speculative Expansion | Evolution I | Evolution I | Conditional | Hidden | Hidden | Hidden |
| Impose Credit Restraint | Evolution I | Evolution I | Evolution I | Evolution I | Emergency version | Landing support |
| Liquidate Speculative Projects | Hidden | Conditional | Evolution I | Evolution I | Evolution I | Conditional |
| Designate a Miracle Region | Evolution II | Evolution II | Conditional | Hidden | Hidden | Hidden |
| Open a Controlled Industrial Corridor | Evolution III | Evolution III | Conditional | Hidden | Hidden | Hidden |
| Permit Unrestricted Expansion | Evolution III | Evolution III | Conditional | Hidden | Hidden | Hidden |
| Contain the Spread | Evolution III | Evolution III | Evolution III | Evolution III | Emergency form | Landing support |
| Secure the Material Flow | Conditional | Active objective | Active objective | Emergency replacement | Hidden | Hidden |
| Consolidate Industrial Capacity | Hidden | Active objective | Active objective | Conditional retry | Hidden | Hidden |
| Prepare a Controlled Landing | Hidden | Conditional | Available | Conditional | Hidden | Active objective |
| Prevent the Crash | Hidden | Hidden | Hidden | Conditional | Active objective | Hidden |
| Order an Emergency Production Halt | Hidden | Hidden | Hidden | Conditional | Available | Hidden |

## Normal baseline route

```text
Opening
  -> optional early push
  -> survey lasting capacity
  -> build reserves or supply support
  -> designate one or more region projects
  -> secure material flow
  -> consolidate project capacity
  -> prepare controlled landing
  -> exceptional or controlled result
```

## Wartime exploitation route

```text
Opening during major war
  -> Run the Economy Hot
  -> production window supports military deadline
  -> reserve or supply action while pressure rises
  -> choose one production or conversion project
  -> stop pushing near Visible Strain
  -> controlled landing when preparation is sufficient
     or rough landing when the military timetable is more important
```

## Late emergency route

```text
Dangerous Imbalance
  -> stop new projects
  -> stabilize strongest cause
  -> suspend or abandon fragile projects
  -> rebuild or consume reserves
  -> Prevent the Crash
     -> success returns to Strain with no-push recovery period
     -> failure hands off to Event 35
```

## Forced landing route

```text
Pre-crash or Terminal Instability
  -> Order an Emergency Production Halt
  -> remove aggressive output
  -> freeze projects
  -> evaluate reserves, region protection, trend, and shock state
     -> forced landing succeeds
        -> severe temporary exhaustion
        -> limited legacy
     -> forced landing fails
        -> Event 35 handoff
```

## Speculative Mania route

```text
Evolution I
  -> choose speculative project or credit restraint
  -> speculative project accelerates output and progress
  -> pressure and political resistance rise
  -> complete and integrate the project at low pressure
     or liquidate it before collapse
     or carry the exposure into Event 35
```

## Industrial Miracle route

```text
Evolution II
  -> designate one to three Miracle Regions
  -> choose project profiles that match bottlenecks
  -> invest in protection, supply, and integration
  -> complete first abnormal project
  -> record guarded Chaos milestone
  -> controlled landing converts bounded map and national legacy
     or crash transfers Fragile Miracle Regions to Event 35
```

## Runaway Industrialization route

```text
Evolution III
  -> choose controlled corridor, unrestricted spread, or containment
  -> primary region links to valid neighboring states
  -> secondary states expand, integrate, become fragile, or are abandoned
  -> guarded Chaos milestones follow concrete abnormal spread
  -> controlled integration and landing preserve major bounded legacy
     or network cascade and crash start Event 35 at Evolution III
```

## Decision cost families

| Action family | Primary cost types | Secondary consequence | Cost types hard cap |
| --- | --- | --- | ---: |
| Aggressive output | Overheating, maintenance pressure, possible stability | Higher short-term output | Not a stockpile purchase |
| Supply stabilization | Trains, trucks, fuel, convoys or civilian commitment | Lower output from committed capacity | 4 |
| Reserves | Output sacrifice, construction sacrifice, civilian commitment, equipment | Bounded shock protection | 4 |
| Cooling | Output and construction sacrifice, possible stability or war support | Large Overheating relief | 3 |
| Region protection | Civilian commitment, trains or trucks, support or infantry equipment, fuel | State-specific resilience | 4 |
| Project designation | Civilian commitment, logistics, time, possible equipment | Project pressure and opportunity cost | 4 |
| Emergency action | Larger logistics commitment, reserve consumption, output loss, stability | Short survival window | 4 |

## Visibility rules

- Show one selected state at a time for target-specific actions.
- Hide a project action when no valid state exists.
- Replace ordinary actions with emergency versions at high pressure.
- Hide obsolete decisions after a project, reserve step, or protection step is complete.
- Stop voluntary pressure actions during the final landing window.
- AI can evaluate all valid targets through its own target logic without using the player selector.

## Objective capacity

- One main economic objective at a time under normal conditions.
- One region or incident objective may coexist when it requires separate state work.
- Pre-crash replaces normal objectives with Prevent the Crash.
- Landing replaces all ordinary objectives with Prepare a Controlled Landing.

## Failure ownership

| Failure | Immediate result | Long-term owner |
| --- | --- | --- |
| Supply objective failure | Overheating and transport incident | Event 34 |
| Project failure | Lost progress, unfinished works, fragility | Event 34 until landing or crash |
| Controlled landing cancellation | Return to active phase | Event 34 |
| Prevent the Crash failure | Frozen collapse snapshot | Event 35 after handoff |
| Emergency halt failure | Frozen forced-landing snapshot | Event 35 after handoff |
| State loss | Project pause or cancellation, shock | Event 34, then Event 35 if crash follows |
