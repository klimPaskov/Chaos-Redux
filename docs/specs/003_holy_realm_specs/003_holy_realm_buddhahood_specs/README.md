# Holy Realm Buddhahood Planning Package

This package contains the source spec and implementation prompts for the Holy Realm Buddhahood and Final Silence rework.

Use [the current release reconciliation](../../../plans/003_holy_realm_plans/release_qa_completion_20261006.md) before resuming production.
It records acceptance for bounded repairs and leaves broad nested-spec acceptance and legacy terminal differences unresolved.
These prompts are reusable task briefs whose scope must be bound to the recorded acceptance and current implementation state.
The top-level [legacy specification](../003_holy_realm_spec.md) is historical provenance.

Workflow ownership is defined by [chaos-redux-subagents](../../../../.agents/skills/chaos-redux-subagents/SKILL.md), [chaos-redux-event-assets](../../../../.agents/skills/chaos-redux-event-assets/SKILL.md), and [chaos-redux-scripted-gui](../../../../.agents/skills/chaos-redux-scripted-gui/SKILL.md).
Every character portrait belongs to `chaosx_portrait_creator`.
The dedicated mandala window belongs to `chaosx_event_ui_worker` when its accepted bounded brief supplies the required reference and MCP evidence contract.

Main files:

- `specs/holy_realm_buddhahood_spec_part_1.md`.
- `specs/holy_realm_buddhahood_mechanics_and_gui.md`.
- `specs/holy_realm_buddhahood_focus_tree.md`.
- `specs/holy_realm_buddhahood_decisions_missions.md`.
- `specs/holy_realm_buddhahood_country_package_ai.md`.
- `specs/holy_realm_buddhahood_asset_animation_spec.md`.
- `specs/holy_realm_buddhahood_super_events.md`.
- `specs/holy_realm_buddhahood_achievements.md`.
- `prompts/holy_realm_buddhahood_coding_prompt.md`.
- `prompts/holy_realm_buddhahood_goal_prompt.md`.

The event id is `003`; implementation uses the existing `chaosx.nr3.*` Holy Realm namespace.
