# Event 014 GUI and Focus Improvement-Loop Audit

Date: 2026-07-22

Status: plan-only audit. No gameplay or interface files were edited.

## Scope and references

This pass is limited to the direct Event 014 presentation contract:

- `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- `interface/014_cannibalism_frontline_hunger.gui`
- the three focus trees in `common/national_focus/014_cannibalism_focus.txt`
- the Event 014 decision categories that host the five scripted GUI windows
- `docs/reports/interface_visual_quality_audit.md`

The offline Paradox wiki snapshot was consulted for Data structures, Triggers,
Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision
modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, and
National focus modding. Official vanilla documentation was checked for script
concepts and script constants, effects, triggers, modifiers, and dynamic
variables. The relevant vanilla contracts are:

- a scripted GUI needs a valid context, visible and clickable element triggers,
  effect handlers, dirty updates when state is cached, and explicit AI wiring
  when the AI must use the GUI;
- a decision category may host a `decision_category` scripted GUI, while
  decision availability and AI selection remain in the decision definitions;
- a focus tree needs unique IDs, visible prerequisite and mutual-exclusion
  structure, completion rewards, AI weights, localisation, icons, and a clear
  route payoff;
- event targets must not be used in scripted GUIs. Event 014 uses country
  variables, country flags, arrays, and scripted effects for GUI state instead.

## Current implementation evidence

### GUI surface

The live package has five direct windows: early containment, the Evolution II
network view, Warlord command, revealed unified command, and Wendigo command.
The network view is the only large stateful window. It uses country-owned
variables and arrays, a dirty variable, dynamic list entries, tab selection,
sorting, refresh, close, animation toggles, and selected country or state
cards. The other four windows expose live meters, stage or mission summaries,
warning frames, portraits or seals, and animation toggles.

All 16 authored GUI buttons have matching click handlers. Every handler is a
view or presentation action. No handler pays population, Larder, command
power, equipment, manpower, or fuel. No handler starts a mission, declares a
war, creates a unit, changes a terminal lock, or writes a Deaths record. Those
actions remain in the decision and mission surfaces, so the AI uses the same
cost and cleanup contracts as the player.

The five GUI blocks are explicitly human-facing with `is_ai = no` and
`ai_enabled = { always = no }`. This is intentional. The GUI does not own an
action economy. Adding AI clicks would duplicate the already audited decision
AI and create two cost or cleanup paths for every operation. The scripted GUI
file contains no event-target scope. Animated and static siblings are gated by
the animation preference, and the network window updates through its dirty
variable instead of an unconditional large-window refresh.

The existing visual audit records five bounded windows, 54 registered Event
014 GUI sprites, 24 animated sheets with static fallbacks, 16 handler pairs,
31 text keys, and 38 tooltip keys. The remaining tooling note is a fresh
post-patch MCP rerender after the prior transport shutdown. This is a proof
task, not a reason to add another window or mechanic.

### Focus surface

The current file contains three independent roots:

| Tree | Focuses | Route contract |
| --- | ---: | --- |
| Unified CBL | 108 | opening convergence, warlord disposition, hierarchy, four Larder methods, army, navy, air, cells, expansion, counterwar, ordinary terminal |
| Regional warlord | 68 | survival, three hierarchy routes, three Larder methods, military doctrine, Island, Siege, and March origin overlays, regional predation, infiltration, and Evolution II end routes |
| Wendigo overlay | 28 | merge, winter hunger, recruitment, inherited cannibal routes, transformation anchors, countdown, and alternate terminal |

The consolidated focus audit reports 204 unique IDs, 204 rewards, 204 AI
blocks, 204 icons, 204 localisation contracts, zero dangling prerequisite or
mutual-exclusion references, zero duplicate coordinates, and zero unresolved
route or terminal gates. Every non-root node has an ancestry path. Focus reward
helpers feed decisions, missions, ideas, dynamic modifiers, map contracts,
terminal readiness, and achievement hooks. Unified family lifecycle logic
keeps the focus-created spirit count at three or fewer. The ordinary and
Wendigo terminal routes retain strict chaos-above-1000 checks and their
operational prerequisites.

Focus and decision systems are connected. Unified focuses open command,
Larder, war-machine, global campaign, counterwar, and terminal decision
families. Warlord overlays open origin and regional actions. Wendigo focuses
feed the Pack, inherited-cell, receipt, scored-target, and terminal-hunt
contracts. These are route effects and decision gates, not decorative focus
bonuses. The source focus audit also records that the pre-lock Wendigo score
band is assigned once per target and rescored by a separate post-lock package.
That bounded engine limitation is documented and does not require a new focus
branch or GUI control.

## Improvement-loop verdict

No further GUI or focus expansion is justified in the accepted Event 014
scope. The current surfaces already answer the player-facing questions that a
custom presentation layer should answer, while decisions and missions own
all paid actions. The focus trees already provide staged opening choices,
distinct route families, branch locks, cross-branch utility, concrete
decision and mechanic hooks, AI behavior, and terminal payoffs.

Adding another GUI meter, a target-map layer, direct GUI action buttons, or a
fourth route family would duplicate existing state, split cost logic, or add
small rewards without a new strategic decision. Adding more focuses would
repeat the existing route and idea lifecycle patterns. The anti-bloat stop
condition therefore remains active.

The following are closure checks only. They do not authorize gameplay or
interface edits:

1. When MCP transport is available, rerender the five GUI windows at the
   existing resolution and UI-scale matrix. Confirm bounds, text height,
   animation/static fallback selection, and intentional overlap counts.
2. Re-run the read-only focus graph inspection for all three roots and preserve
   the 108, 68, and 28 focus counts, connector metrics, and zero-dangling
   result in the final completion audit.
3. Keep GUI state ownership in country variables, flags, arrays, and scripted
   effects. Do not introduce event targets into scripted GUI context.
4. Keep action ownership in the existing decision and mission categories. Any
   future action proposal needs a new accepted specification before it can
   touch the GUI or focus tree.

## Queued ideas and blockers

No new GUI or focus idea is accepted by this pass. The earlier improvement-loop
addendum still records cross-origin joint operations, route-aware recovery
case files, and inspection-access compacts as queued and unaccepted. They are
not blockers and are not presentation work items here.

The only open evidence item inside this scope is the fresh MCP rerender noted
above. It cannot be completed while the artifact transport is unavailable.
There are no gameplay, interface, localisation, AI, route, asset, or terminal
simplifications in this audit.

## Handoff

This addendum is documentation-only. The parent completion audit should cite
this verdict alongside the consolidated focus audit and the existing interface
visual-quality audit. No gameplay or interface patch is requested from this
pass.

