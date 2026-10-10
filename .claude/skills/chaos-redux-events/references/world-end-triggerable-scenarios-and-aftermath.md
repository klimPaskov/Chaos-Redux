# World-end branches, triggerable scenarios, and defeat aftermath

## World-end scenarios

A world-end scenario is a terminal branch that changes the campaign into a resolved or end-state condition, not just a large disaster or strong major event. It is chosen based on the world state and can only be triggered when the chaos value is over 1000.

### World-end scenario implementation

The normal contract is:

1. guard the branch with `NOT = { has_global_flag = world_end }`
2. set `world_end`
3. set a scenario-specific global flag
4. set the matching `super_event_visible`
5. update the matching super-event text, image, and audio wiring
6. stop or gate incompatible future systems and branches
7. document the end-state in the event doc, and spreadsheet

Classify every terminal branch as public or hidden/easter-egg before wiring Event Details.

For every public terminal branch, complete the Event Details contract in the same implementation pass:

1. Give the branch a stable scenario registry entry and the owning event ID.
2. Create one row per branch. If one event has several public terminal branches, do not collapse them into one event-level row.
3. Give each row its own default-enabled persistent toggle state. Rebuilding or reopening Event Details must not reset it, and toggling one branch must not change sibling branches or the parent event.
4. Add player-facing title and details text that explains the premise and terminal state without listing raw effects, hidden variables, secret conditions, or implementation state.
5. Wire the row, selection, toggle, and detail-panel clicks through the shared Event Details behavior. Add availability or status text when it helps the player understand why a public branch cannot currently be selected, without exposing hidden logic.
6. Make automatic world-end selection read the branch toggle. A disabled branch is skipped as a candidate without disabling its owning event, suppressing enabled sibling branches, bypassing the 1000+ Chaos gate, or changing the normal world-state selection rules.
7. Keep the scenario-specific global flag and matching super-event visibility, text, image, and audio linkage distinct for that branch.
8. Align the public event doc and spreadsheet-facing world-end fields with the same title, premise, terminal state, and branch count.

Hidden or easter-egg world-end scenarios may retain a stable internal registry identity with hidden visibility, but they must stay out of the projected public Event Details rows, title/detail selectors, toggles, status controls, public docs, and spreadsheet-facing public fields. Their terminal flagging, chaos gate, selection logic, and super-event wiring still follow the normal world-end contract.

## Triggerable scenarios

Triggerable scenarios are manual sandbox or challenge setups launched from the Chaos Redux settings UI. They are separate from the normal random-event timer, chaos-tier eligibility, evolution pacing, and automatic source-event prerequisites.

Core rule: a triggerable scenario is always directly fireable from the scenario UI unless the launch would be impossible or conflict with an active terminal state. It creates instant chaos from setup controls, not from live Chaos Meter progression. After launch, ordinary event behavior resumes.

Use this contract when adding a scenario for an event:

1. Register a stable scenario ID and sort value in `triggerable_scenarios_initialize_registry`.
2. Add tuning constants in `common/script_constants/chaosx_triggerable_scenarios_constants.txt` for scenario IDs, sort values, intensity stops, scenario type IDs, and scale values.
3. Add or update launch, registry, sorting, intensity, and type effects in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`.
4. Add launch eligibility in `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`.
5. Add scripted GUI click handling, dynamic list support, slider stops, and visibility checks in `common/scripted_guis/chaosx_scripted_gui_settings.txt`.
6. Add scenario name, sort text, detail text, type labels, and intensity impact text in `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`.
7. Add or update player-facing labels, tooltips, confirmation text, and scenario event text in `localisation/english/chaosx_gui_l_english.yml`.
8. Update `interface/chaosx.gui` only when the existing scenario window cannot present the new controls cleanly.
9. Document the scenario in the relevant event doc or scenario doc, for example in `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/systems/event_system/triggerable_scenarios.md`.

The scenario window is data-driven. It should use `global.triggerable_scenario_view_ids` for the sortable list, log-style entries for scenario rows, and a detail panel that updates from the selected entry. Do not hardcode one button per scenario when the registry and dynamic list can handle it.

The scenario button should open a confirmation window. Confirming must read the selected scenario, type, and intensity at launch time. Do not bake these values into the first click.

Intensity uses the existing four-stop scenario slider:

- Low
- Medium
- High
- Maximum

The selected intensity should be stored in `triggerable_scenarios_intensity`. The knob position, impact text, and launch effects must all read the same stored value. If a scenario deliberately ignores intensity, state that in its detail text and keep the slider harmless.

Scenario type controls are scenario-specific. If a scenario has types, define type constants, cycle buttons, labels, detail text, and launch branches.

Launch gates are not normal event prerequisites. They should only block impossible or conflicting launches, such as a required source country not existing, a required target scope being impossible to build. Do not block a triggerable scenario because chaos value, chaos tier, prior event state, evolution unlocks, date gates, route prerequisites, or super-event history flags are missing.

When a triggerable scenario needs to force a path that is normally gated, use an explicit scenario launch flag or variable. Scope the bypass tightly to the launch effect and clear it when the scenario setup is finished so automatic event behavior remains governed by normal event state.

Triggerable scenarios may call source-event helpers, unit-spawn helpers, release helpers, super-event helpers, or world-end helpers, but the scenario wrapper owns manual setup choices, intensity scaling, scenario type routing, confirmation flow, and bypass cleanup. Shared helpers must stay idempotent when the scenario and normal event chain can both call them.

The scenario UI normally reuses existing Chaos Redux and vanilla UI assets. Do not request dedicated scenario art, report images, icons, or animated UI unless the user asks for them or the existing scenario window cannot communicate the mechanic. If the UI requires a sprite entry for technical reasons, register a stable placeholder path and report that it is a placeholder.

Completion for a scenario-backed event requires:

- scenario ID and sort registration
- launch effect and confirmation flow
- launch eligibility using the same gate for click enablement and button state
- intensity and type controls wired
- scripted localisation and GUI localisation
- bypass flags scoped and cleaned up
- no normal chaos, evolution, date, route, or super-event-history prerequisite blocking manual launch
- documentation updated without listing stale or implementation-only debug details

## Major-event defeat aftermath

Some major events should also have a structured aftermath when the threat is beaten.

Use a defeat aftermath package when all of these are true:

- the defeated threat was global or near-global in reach
- the campaign lasted long enough to feel like a world crisis
- the cost in casualties, destruction, or political disruption was high enough that the world should not simply snap back to normal

Typical aftermath content:

- a defeat super-event or defeat-stage super-event effect
- postwar treaties, compacts, or new world orders
- recurring remembrance, reconstruction, or vigilance events
- lasting ideas, tech-sharing groups, or diplomatic rules that exist because the world learned from the crisis

Do not add a treaty/new world order after every contained or short-lived disaster. Those only make sense when the event genuinely reshaped the campaign.
