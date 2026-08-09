# Universal state-registry skill handoff

## Scope

This maintenance pass updates only the reusable formable state-puzzle template guidance and this requested handoff. No gameplay files, registry JSON, generated assets, runtime tools, or `.agents/skills/hoi4-decisions-missions/SKILL.md` were edited.

## Changed files

- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md` is a new focused workflow covering the canonical geometry registry, ordered-root provenance, builder and consumer commands, consumer schema/template, candidate supersets, optional live visibility helpers, live qualification/control, runtime manifest discovery, no-cache/no-world-scan rules, finite runtime limits, map-changing mod regeneration, mandatory MCP map/GUI evidence, and DDS decode round-trip evidence.
- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/README.md` now links the focused workflow, identifies `state_manifest.*` as compatibility scaffolding rather than a second geometry source, points setup step 2 at the registry-backed consumer flow, and calls out the MCP/DDS evidence gates.
- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/validation_checklist.md` now includes registry/consumer provenance, complete-manifest discovery, candidate-superset, live-helper, regeneration, MCP map/GUI, and DDS round-trip checks.

## Verified source and route details

- Read `AGENTS.md`, the complete `chaos-redux-subagents` skill, and the complete `hoi4-decisions-missions` skill before editing.
- Read the required offline Paradox wiki pages and applicable vanilla documentation, including decision, interface, scripted-GUI, trigger, effect, localisation, scope, and dynamic-variable references.
- Inspected `.tools/build_formable_state_registry.py`, `.tools/build_formable_state_puzzle_consumer.py`, `docs/formables/state_registry/consumer_spec.schema.json`, `docs/formables/state_registry/consumer_spec.template.json`, `docs/formables/state_registry/README.md`, and `.tools/generate_formable_state_puzzle_runtime.mjs` to ground the guidance in current contracts.
- Verified the installed HOI4 MCP route names `mcp__hoi4_agent_tools__hoi4_map_inspect`, `mcp__hoi4_agent_tools__hoi4_map_render`, `mcp__hoi4_agent_tools__hoi4_gui_inspect`, and `mcp__hoi4_agent_tools__hoi4_gui_render` from the active tool surface.
- Confirmed that no dedicated DDS MCP route is installed; the guidance therefore names the repository `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` plus local decode and round-trip evidence as the required DDS check.

## Validation performed

- Confirmed the template folder was clean before editing; no unexpected pre-existing template changes were found.
- Ran `git diff --check` on the changed template files.
- Checked that the new workflow contains the requested registry, builder, consumer, schema/template, complete-manifest, visibility-helper, live qualification, no-cache/world-scan, finite-runtime, ordered-root, MCP, and DDS round-trip terms.
- Re-read the changed README, checklist, and new workflow for path and contract consistency.

## Not run and why

- No registry builder, consumer compiler, runtime generator, map MCP inspection/render, GUI MCP inspection/render, or DDS conversion was run because this pass changes reusable documentation only and does not create or modify a consumer, runtime manifest, GUI, map, or asset.
- No gameplay validation was attempted; the parent remains responsible for running the workflow and collecting consumer-specific evidence.

## Remaining risks

- The existing legacy `state_manifest.*` examples remain in the template for compatibility and still describe a pre-registry owner package. New consumers should follow the universal workflow and must not create parallel geometry sources.
- A future consumer must record any unavailable MCP route or unresolved engine scope as a blocker rather than treating source-only review as completion evidence.
