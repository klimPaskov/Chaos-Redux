# Parent handoff: folder-owned Event 027 track guards

> **Superseded status notice (2026-09-01):** This dated track-guard handoff is preserved as historical source evidence and is superseded as a current MCP status authority by ../documentation_state.md. Its dated transport statement is stale after the fresh bounded Event 027 calls.

## Scope

The parent implementation audited the human Event 027 subdoctrine pages after the scripted adapter audit found that the native `has_subdoctrine_in_track` trigger checks any instance of a named track rather than a folder-owned track identity.

Army and Chaos Warfare both use the native `land` folder and share `infantry`, `combat_support`, `armor`, and `operations` track names. A global emptiness check could therefore hide a valid Army choice when Chaos Warfare occupied the same-named track, or hide a valid Chaos Warfare choice when Army occupied it.

## Changes

- Added explicit folder-owned emptiness adapters for every Army, Navy, Air, and Chaos Warfare Event 027 track in `common/scripted_triggers/027_doctrine_research_triggers.txt`.
- Updated ordinary-domain valid-pool, selected-track, selected-subdoctrine, and empty-track guards to use those adapters.
- Updated every ordinary-domain human subdoctrine page in `events/027_doctrine_research.txt` so its empty-track option branch uses the matching folder-owned adapter.
- Retained native Special Forces occupancy checks because vanilla permits each Special Forces subdoctrine token in either of its two tracks and the script API does not expose a documented identity-at-track trigger.
- Documented the contract in `docs/events/027_doctrine_research/overview.md` and `docs/plans/027_doctrine_research_plans/mcp_evidence.md`.

## Evidence

The current Event 027 source has 107 track-qualified mastery wrappers and 107 exact native adoption wrappers. The event file contains only the 16 intentional Special Forces negative `has_subdoctrine_in_track` guards; ordinary-domain negative guards now call the folder-owned adapters. The Event 027 event and trigger files remain brace-balanced after the change.

The source uses native `add_mastery` one-point increments with level readback, native `set_sub_doctrine` for empty-track assignment, and receipt postconditions. The HOI4 MCP retry for current-source Event 027 inspection still returns `Transport closed`, so this handoff does not claim engine render, doctrine inspect, save/reload, or live cross-domain proof.

## Residual risk

Special Forces remains fail-closed when both native tracks are occupied because an active token cannot be attributed to a specific track through the documented trigger surface. A live engine trace is still required for that identity case and for all persistence and banked-mastery acceptance scenarios.
