# Event 34 Industrial Boom AI and probability scenario matrix

## Evidence standard

The implementation audit should use the same scenario IDs before and after tuning. Results may be exact only when the complete candidate pool and external factors are known. Otherwise report score ordering, bounded chance, sampled result, or unresolved dependency.

## Country target selection scenarios

| ID | World state | Required candidate pool | Expected result |
| --- | --- | --- | --- |
| TGT-01 | 1936 majors plus one player non-major | Every valid major and the player country | Player non-major has meaningful weight, largest major does not dominate |
| TGT-02 | One country has active Event 34 | Full valid pool | Active boom country has zero eligibility |
| TGT-03 | Several recent Event 34 recipients | Full valid pool with history | Recent recipients rank below untouched comparable countries |
| TGT-04 | One prior crash, one prior successful landing | Comparable valid countries | Prior crash lowers weight during recovery, success memory does not create dominance |
| TGT-05 | Multiplayer with several player countries | Every valid player and major | No hidden preference for the current local player unless the event framework requires one |
| TGT-06 | One valid country remains | Complete pool | That country receives all live weight |
| TGT-07 | No valid country | Empty pool | Event is unavailable and no target is queued |
| TGT-08 | High Chaos, Evolutions I to III enabled | Full valid pool | Target choice remains country-valid, evolved opening does not distort country selection unfairly |

## Decision behavior scenarios

### AI-01: Peacetime industrial major

Inputs:

- Overheating 15 and stable.
- Strong rail, fuel, trade, and convoys.
- No equipment deficit.
- No reserves.
- One unprotected Industrial Region.
- Baseline evolution.

Expected ordering:

1. Build Industrial Reserves or Survey Lasting Capacity.
2. Protect Key Industrial Regions.
3. Designate a project after survey.
4. Run the Economy Hot remains possible but below structural actions.
5. Cool the Expansion has near-zero score without a landing plan.

Invalid behavior:

- Emergency action receives weight.
- Stabilize Supply Chains dominates despite no bottleneck.

### AI-02: Winning wartime major

Inputs:

- Overheating 20 and rising slowly.
- Strong supply.
- Moderate equipment deficit.
- Major offensive planned.
- Limited reserves.

Expected ordering:

1. Run the Economy Hot.
2. Production Practices or Factory Conversion project.
3. Build reserves after the push begins.
4. Stabilize Supply Chains when pressure rises.
5. Landing remains low until the military deadline passes.

Invalid behavior:

- AI cools immediately and wastes the production window.
- AI begins several overlapping aggressive pushes.

### AI-03: Losing wartime major

Inputs:

- Overheating 45 and rising.
- Severe equipment deficit.
- Threatened capital.
- Supply adequate for one short window.
- No completed project.

Expected ordering:

1. Desperate profile may run hot once if below the hard lock.
2. Protect the critical region.
3. Use supply stabilization.
4. Prepare rough or forced landing after the short military window.

Invalid behavior:

- Long civilian project with no chance to complete dominates.
- Unrestricted spread begins after Pre-crash.

### AI-04: Blockaded maritime major

Inputs:

- Overheating 40 and rising quickly.
- Convoy shortage.
- One key port damaged.
- Material imports essential.
- No reserves.

Expected ordering:

1. Stabilize Supply Chains with maritime costs.
2. Protect or repair the port Industrial Region.
3. Build reserves when affordable.
4. Cool the Expansion if access cannot be restored.
5. Run the Economy Hot ranks very low.

Invalid behavior:

- Train-only stabilization gives full relief.
- Convoy-specific action appears for a landlocked comparison country.

### AI-05: Bombed regional network

Inputs:

- Overheating 50.
- Two primary regions.
- One protected and one unprotected.
- Repeated bombing and infrastructure damage.

Expected ordering:

1. Protect or repair the unprotected region.
2. Stabilize supply.
3. Suspend fragile project in the damaged state.
4. Begin landing when one secured project exists.

Expected state selection:

- Unprotected high-value state ranks above already protected state.

Invalid behavior:

- AI keeps targeting the protected state because it has more factories while the other region is collapsing.

### AI-06: Small player-equivalent non-major

Inputs:

- Overheating 25.
- One region.
- Small stockpiles and civilian industry.
- Baseline evolution.

Expected behavior:

- Essential decisions remain affordable after scaling.
- One project path is viable.
- AI does not reserve more factories than the country owns.
- Landing begins after one project reaches integration.

Invalid behavior:

- Major-country fixed costs block every response.

### AI-07: Speculative Mania with live project

Inputs:

- Evolution I.
- Overheating 55 and rising.
- One speculative project near completion.
- Limited reserves.
- At peace.

Expected ordering:

1. Impose Credit Restraint or stabilize supply according to dominant cause.
2. Complete project only when integration can finish safely.
3. Liquidate if pressure approaches danger and completion remains distant.
4. Run the Economy Hot ranks near zero.

Invalid behavior:

- AI approves a second speculative project.
- Cooling has no weight because it reduces output.

### AI-08: Industrial Miracle with fragile region

Inputs:

- Evolution II.
- Overheating 65.
- Two Miracle Regions, one fragile and unprotected.
- Strong reserves.

Expected ordering:

1. Protect the fragile region.
2. Cool the Expansion.
3. Suspend the fragile project when protection is unaffordable.
4. Prepare landing after pressure falls.

Invalid behavior:

- New Miracle Region designation receives weight.

### AI-09: Runaway Industrialization with corridor choice

Inputs:

- Evolution III.
- Overheating 35.
- Strong supply and stability.
- One protected primary region.
- One valid neighboring state.

Expected ordering:

1. Controlled Industrial Corridor for cautious and balanced profiles.
2. Unrestricted Expansion only for desperate wartime profile.
3. Contain the Spread for fragile profile.

Invalid behavior:

- Unrestricted route dominates every profile because its output reward is larger.

### AI-10: Pre-crash with depleted reserves

Inputs:

- Overheating 88 and rising quickly.
- Depleted reserves.
- One critical transport shock.
- Several incomplete projects.

Expected ordering:

1. Emergency Logistics Command when affordable and relevant.
2. Prevent the Crash objective.
3. Suspend or abandon projects.
4. Emergency halt when relief cannot reach the threshold in time.

Invalid behavior:

- Any new expansion decision has nonzero score.
- Rebuild reserves is treated as instant full safety.

### AI-11: Controlled landing nearly complete

Inputs:

- Overheating 30 and falling.
- Strong reserves.
- Two secured projects.
- Landing mission has little time remaining.

Expected ordering:

1. Preserve landing conditions.
2. Stabilize only when needed.
3. Avoid every voluntary pressure action.

Invalid behavior:

- Evolution pacing interrupts the final landing window.
- AI cancels landing for a small temporary output increase.

### AI-12: Previous crash history

Inputs:

- Baseline new firing.
- One prior Event 34 to Event 35 collapse.
- Moderate logistics.
- Overheating 25.

Expected behavior:

- Higher weight for reserves and supply control.
- Lower weight for speculative or aggressive options.
- Still capable of a successful project and landing.

Invalid behavior:

- Prior failure permanently forces a passive route.

## Evolution timing scenarios

| ID | Active state | World state | Expected timing relation |
| --- | --- | --- | --- |
| EVO-01 | Baseline, low pressure, cautious | Rising Chaos just reached | Evolution I later than normal center |
| EVO-02 | Baseline, repeated hot running | Rising Chaos | Evolution I earlier than EVO-01 |
| EVO-03 | Baseline, high pressure, several projects | Rising Chaos | Evolution I earlier than normal center |
| EVO-04 | Landing mission final window | Rising Chaos | Evolution pacing paused or strongly suppressed |
| EVO-05 | Evolution I active | Below Chaos Tier | Evolution II impossible |
| EVO-06 | Evolution I active, high pressure | Chaos Tier crossed | Evolution II eligible with dynamic delay |
| EVO-07 | Evolution II active, controlled management | Totalen Chaos | Evolution III possible but slower |
| EVO-08 | Evolution II active, unrestricted pressure | Totalen Chaos | Evolution III earlier than EVO-07 |
| EVO-09 | Evolution disabled | Any threshold | Zero activation and zero record chance |
| EVO-10 | Pre-fire evolved opening | Stage already active | No duplicate active-evolution record at opening |

## Incident selection scenarios

| ID | Conditions | Expected dominant family | Families that must be zero |
| --- | --- | --- | --- |
| INC-01 | Overheating 20, baseline | Light congestion and opportunity | Critical crash incidents |
| INC-02 | Overheating 55, rail deficit | Transport and maintenance | Convoy incident in landlocked state |
| INC-03 | Evolution I, speculative pressure | Credit and project incidents | Miracle and spread incidents |
| INC-04 | Evolution II, valid Miracle Region | Miracle and region fragility | Spread incidents |
| INC-05 | Evolution III, valid corridor | Spread and network incidents | Invalid-state incidents |
| INC-06 | Protected region | Lower damaging weight | Duplicate protected-state accident while prior incident active |
| INC-07 | No valid state target | Country-level incident only | Every state-specific branch |
| INC-08 | Recent incident in same family | Other relevant families rise | Immediate repeat of the same incident |

## Landing outcome scenarios

| ID | Pressure and structure | Expected result ordering |
| --- | --- | --- |
| LAND-01 | Low pressure, Strong reserves, several secured projects | Exceptional most likely, controlled fallback |
| LAND-02 | Moderate pressure, Limited reserves, one integrated project | Controlled most likely |
| LAND-03 | High pressure, weak reserves, unfinished projects | Rough most likely, crash possible after shock |
| LAND-04 | Pre-crash, Strong reserves, emergency halt | Forced success possible, controlled impossible |
| LAND-05 | Terminal pressure, depleted reserves, lost region | Event 35 handoff dominant |
| LAND-06 | Evolution III, controlled corridor, full integration | Exceptional possible but harder than baseline |
| LAND-07 | Evolution III, unrestricted spread, fragile network | Crash or rough result dominates unless heavily stabilized |

## Probability comparison requirements

For each patched weighted surface, the completion evidence should record:

- Source revision before change.
- Named scenario IDs.
- Candidate pool completeness.
- External factors supplied.
- Evidence type: exact, bounded, sampled, score-only, or unresolved.
- Baseline ordering or timing.
- Intended ordering or timing.
- Post-change ordering or timing.
- Any scenario that remains unresolved.
- Rendered matrix or sensitivity view when useful.

The auditor remains read-only. The event owner chooses the balance target and applies the patch.
