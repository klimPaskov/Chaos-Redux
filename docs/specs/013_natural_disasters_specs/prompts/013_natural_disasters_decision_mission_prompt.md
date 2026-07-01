# Decision and Mission Prompt for Event 013 Natural Disasters

Use `hoi4-decisions-missions` and audit the finished category with `chaosx_decision_mission_auditor` before completion. The goal is a real disaster response system, not a political power store.

## Required category

Working category id: `natural_disaster_response_category`.

Category purpose:

- Appears for countries with active disaster aftermath.
- Shows current highest-risk affected states and family types.
- Opens emergency, stabilization, and reconstruction actions.
- Cleans itself up when no active aftermath remains.

## Required decision families

- Emergency rescue operations.
- Evacuate threatened area.
- Clear rail and road corridors.
- Reopen ports and airfields.
- Restore supply hubs.
- Establish field hospitals and shelters.
- Import food and water.
- Stabilize slopes and levees.
- Firebreak and fire suppression.
- Ash and dust clearing.
- Rebuild local industry.
- Request or provide foreign disaster aid.
- Monitor follow-up hazard.

## Cost rules

Every major decision family needs at least one meaningful non-political cost or requirement. Use support equipment, infantry equipment, trucks, trains, convoys, fuel, manpower, command power, army XP, civilian factory burden, construction capacity, port access, rail control, state control, supplied divisions, stability tradeoffs, war support tradeoffs, or foreign route access.

Use political power only when the action is administrative, diplomatic, or public-order focused. Command power must stay conservative.

## Mission rules

Timed missions should require action. Good objectives include keeping a port open, holding a supply hub, placing supplied divisions in affected states, clearing a rail corridor, protecting a threatened storm path, completing evacuation before a tsunami, or keeping food distribution stable.

Avoid passive stockpile checks.

## Clutter control

When many states are affected, show only the most relevant decisions or use a selected-target flow. AI can use hidden or broad decisions without relying on a human GUI selector.

## Cleanup rules

The category must clear temporary flags, selected targets, missions, and invalid state references when recovery ends, when a target state changes owner, when a country is annexed, or when the disaster sequence expires.
