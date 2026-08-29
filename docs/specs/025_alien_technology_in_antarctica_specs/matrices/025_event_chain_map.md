# Event 025 chain map

## Global flow

```text
Major event selected
  -> initialize race and hidden crash state
  -> opening super-event
  -> invite every current human-controlled country
  -> select bounded AI major roster
  -> close entry window
  -> Phase 1 Mobilization
  -> Phase 2 Crossing and Outpost
  -> Phase 3 Survey and Triangulation
  -> Phase 4 Final Recovery
  -> declare one winner
  -> apply winner and losing rewards
  -> Phase 5 Analysis and Settlement
  -> close active race state
  -> retain alien-recovery and aftermath ledgers
```

## Baseline participant flow

```text
Invited
  -> Declines
       -> Observer
       -> Public reports only

  -> Enters
       -> Select entry secrecy
       -> Commit initial resources
       -> Choose gateway and route
       -> Organize expedition mission
       -> Reach gateway mission
       -> Cross south
       -> Establish outpost mission
       -> Survey sectors
       -> Confirm primary sector
       -> Build final recovery readiness
       -> Launch final recovery mission
            -> Success first
                 -> Winner
                 -> Main technology reward
                 -> Aftermath policy
            -> Success after winner
                 -> Losing fragment tier
            -> Partial success
                 -> Progress or fragment result
                 -> May try again after recovery
            -> Failure
                 -> Setback, losses, or withdrawal decision
```

## Evolution insertion points

```text
Evolution I Active Signal
  -> may be present at initialization
  -> or enter during any active phase after eligibility
  -> adds signal actions and incidents
  -> does not change phase ownership

Evolution II Something Survived
  -> may be present at initialization
  -> or enter after outpost or survey activity
  -> adds contact and escort actions
  -> final recovery remains possible

Evolution III Militarised Antarctica
  -> may be present at initialization
  -> or enter after hostile pressure and tier gate
  -> adds blockade, seizure, patrol, and demilitarisation
  -> no automatic war

Evolution IV Wreck Breaking Apart
  -> may be present at initialization
  -> or enter after site confirmation or wreck instability
  -> creates fragment sites and wreck integrity
  -> main core remains winner condition

Evolution V Technology Changes Its Users
  -> can alter first opening only as a high-chaos latent property
  -> normally activates after usable technology exists
  -> changes winner and fragment-holder aftermath
  -> does not reopen the race
```

## Global reports

| Threshold | Surface | Repeat rule |
| --- | --- | --- |
| Major event begins | Super-event | Once |
| First functioning outpost or first verified fragment | News or report | One global milestone, choose the first relevant threshold |
| First attributed armed clash | News | Once, only when it occurs |
| Main core secured | News | Once |
| Public Evolution V crisis | News | Once per major public exposure, tightly bounded |

## Participant reports

| Family | Typical trigger | Audience |
| --- | --- | --- |
| Departure | Route and commitment locked | Participant |
| Route setback | Convoy, access, weather, or sabotage incident | Affected participant |
| Outpost | Camp established, damaged, seized, restored, or abandoned | Affected participant |
| Survey | Major certainty gain, false lead, exposed theft | Affected participant |
| Fragment | New category recovered or lost | Holder and relevant rival |
| Rescue | Rescue completed or refused | Involved countries |
| Final recovery | Mission begins, partially succeeds, or fails | Participant |
| Aftermath | Technology field and policy change | Holder |

## Resolution guards

- `primary_core_claimed` is set once.
- Winner reward uses one-shot proof.
- Losing reward uses one-shot proof per participant.
- Final missions cancel after winner selection.
- Same-day finalists pass deterministic comparison.
- Cleanup can be called repeatedly without changing final ownership.
