# Event 025 event UI worker prompt

Spawn `chaosx_event_ui_worker` with `fork_turns="none"` only after the parent has implemented or stubbed the accepted Event 025 state and action helpers.

Event owner:

- ID `25`
- slug `alien_technology_in_antarctica`

Accepted GUI:

- independent Event 025 Expedition Board
- participant-country context
- header with phase and urgent state
- left column with Expedition Progress, Logistics Readiness, and Exposure Risk or Alien Dependence
- central six-sector Antarctic operations panel
- right bounded rival-card list
- bottom phase action tray
- target confirmation and hostile confirmation states
- full background with safe text regions
- multiplayer-private exact values

Expected owning files after live inspection:

- `interface/025_alien_technology_in_antarctica.gui`
- `interface/025_alien_technology_in_antarctica.gfx`
- `common/scripted_guis/025_alien_technology_in_antarctica_scripted_guis.txt`
- Event 025 GUI localisation

Allowed patch scope is the event-owned GUI, event-owned presentation-only scripted GUI wiring, event-owned GFX, and event-owned GUI localisation. Do not patch shared Event Logs, Event Details, Settings, Chaos Meter, Super Event framework, costs, gameplay effects, AI, balance, or reusable logic.

Mandatory workflow:

Follow [the GUI owner skill](../../../../.agents/skills/chaos-redux-scripted-gui/SKILL.md).

1. Create or inspect the intended reference before layout implementation and record its acceptance basis.
2. Run `hoi4.gui_inspect` and retain pre-change full-window, crop, state, hierarchy, click-region, and resolution renders.
3. Apply the authorized reviewed edit directly or optionally through `hoi4.gui_rewrite`.
4. Retain post-change inspection and matching comparison renders.

Review at `1920x1080`, `2560x1440`, and the current project low-resolution target. Verify scrolling, clipping, sector hitboxes, action hitboxes, decorative transparency, selected target, disabled reasons, warning states, and resolved states.

Write the handoff to:

`docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_event_ui_worker_handoff.md`

Missing MCP GUI routes block the UI task.
