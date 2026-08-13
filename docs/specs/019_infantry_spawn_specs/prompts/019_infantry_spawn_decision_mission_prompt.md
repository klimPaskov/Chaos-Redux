# Decision and Mission Implementation Prompt for Event 19 Infantry Spawn

## Task

Implement the phased Event 19 decision, mission, and scripted GUI system from the accepted specification.

Read:

- `AGENTS.md`
- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-frame-animation` for the three animated UI packages
- all Event 19 specification parts
- `matrices/019_decision_mission_map.md`
- `matrices/019_ai_strategy_matrix.md`
- `matrices/019_evolution_entry_cleanup_matrix.md`
- the final shared helper architecture

Inspect the offline Paradox wiki, vanilla documentation, vanilla decisions, existing Chaos Redux categories, selected-target patterns, scripted GUI patterns, and current event-owned file conventions before editing.

## Category phases

Implement a category that changes with event state.

- Baseline: audit, territorial roles, standardization, emergency integration, supervised demobilization.
- Evolution I: muster districts, integration staff, equipment ledgers, specialist preservation.
- Evolution II: rail and depot missions, advanced-lot handling, on-demand formation requests.
- Evolution III: Muster Board, fully random requests, selected-lot management, claimant demands and revolt preparation.
- Evolution IV: Anomalous Registry, family sustainment, containment, trainable versus spawn-only actions, breach response.

Hide obsolete and irrelevant actions. Do not show all future decisions at game start.

## Selected-lot model

Use one selected formation lot for human-facing targeted actions.

Required behavior:

- compact lot list in the scripted GUI
- selected lot stored safely
- activate only relevant lot decisions
- clear target when the lot resolves, country transforms, target becomes invalid, or UI cleanup runs
- AI evaluates all lots without human selection

Do not create one permanently visible decision per division.

## Costs

Use dynamic costs that express the action.

Possible resources:

- army experience
- command power within the project cap
- infantry, support, artillery, truck, train, fuel, and special equipment
- manpower or labor burden
- construction and factory capacity
- supply and rail opportunity cost
- stability, war support, legitimacy, and local support
- time, unit commitment, and mission failure risk

Political power can support genuinely political actions. It must not become the default cost.

Show icon-first costs. When a button has many requirements, show a short status line and full custom tooltip.

## Mission quality

Implement the mapped mission families with real objectives, dynamic duration, success, failure, cleanup, and partial success where designed.

Do not replace them with passive stockpile checks or repeated political-power purchases.

Important missions:

- Formation Roll Call
- Standardization Cycle
- Clear the Rail Network
- Establish Command Districts
- Prototype Maintenance Trial
- Meet the Claimant Deadline
- Break the Claimant Network
- Restore Civil Command
- Contain Anomalous Saturation
- derivative survival and integration missions

## Formation requests

All request costs are paid before result generation.

Implement:

- field reinforcement
- mobile reserve
- territorial defenders
- specialist firepower
- unrestricted random draw
- anomalous draw

Scale cost and cooldown by country size, current lots, event divisions, prior requests, congestion, control, war need, claimant influence, and saturation.

Prevent cancel-and-reroll behavior.

## Claimant decisions

Implement demand-specific actions rather than one generic response.

Required families:

- formal command
- equipment share
- autonomous district
- additional formation
- political seat
- emergency powers
- counter-command
- reassignment
- negotiated retirement
- arrest
- military takeover

Refusal tooltips should communicate broad visible risk without exposing exact hidden revolt rolls.

## Anomalous decisions

Read family behavior from the Chaos unit registry.

- base zombie training is available only after its unlock chain
- advanced zombie variants remain blocked
- ghosts and golems use spawn effects, not training decisions
- future families use registry mode
- containment, sustainment, and derivative risk use family-specific helpers

## Muster Board

Implement a movable scripted GUI with:

- Overview
- Formation Lots
- Command when a claimant exists
- Anomalous Registry at Evolution IV
- optional compact local generation history only if UI space and performance justify it

Every interactive button must call the same shared trigger, cost, effect, cooldown, and cleanup logic as the decision system. Give AI an equivalent non-GUI path.

## Animated presentation

Wire:

- 8-frame Muster seal pulse
- 8-frame critical command border
- 10-frame anomalous registry emblem

Use static fallbacks and verified local frame-sheet precedent. Do not use GIF files as game assets.

## AI

Implement the national profiles and lot evaluation from the AI matrix. AI must compare strategic value and burden before requesting or preserving a lot.

Block invalid actions involving dead claimants, missing states, unavailable families, spawn-only training, impossible civil wars, or closed routes.

## Cleanup and exploits

Required protections:

- delayed partial salvage
- audit lock and safe unlock
- no template conversion equipment farming
- no free request rerolls
- no duplicate unit transfer during revolt
- no stale selected lot, claimant, family, or mission target
- one-state takeover handling
- country transformation migration
- scenario bypass cleanup

## Localisation

Write final in-world text from the specification direction. Do not copy working labels blindly. Keep costs, requirements, target states, deadlines, and visible consequences clear. Do not expose achievements or hidden revolt formulas.

## Audit

After implementation, run `chaosx_decision_mission_auditor` with `fork_context=false` and pass the complete Event 19 scope. Resolve or explicitly disposition every finding before completion.
