# Event 009 White Peace Planning Package

This package contains the source design and implementation handoffs for Event ID `9`, **White Peace**.

## Package map

- `specs/009_white_peace_spec.md` — main event specification.
- `specs/009_white_peace_dynamic_weight_model.md` — dynamic weight, cap, recovery, and branch model.
- `specs/009_white_peace_event_text_log_cluster.md` — localisation, event detail, evolution detail, history, and cluster wording handoff.
- `matrices/009_white_peace_safety_ai_acceptance_matrix.md` — safety gates, AI handling, helper map, validation matrix.
- `research/009_white_peace_diplomatic_design_notes.md` — vocabulary and visual design notes.
- `prompts/009_white_peace_asset_prompt.md` — asset handoff.
- `prompts/009_white_peace_achievement_prompt.md` — achievement handoff.
- `prompts/009_white_peace_coding_prompt.md` — coding-agent implementation prompt.
- `prompts/009_white_peace_goal_prompt.md` — compact `/goal` prompt.
- `prompts/subagents/` — bounded prompts for relevant project subagents.

## Design summary

White Peace is a low-impact repeatable Peace-cluster event. It searches for safe wars and forces no-gain settlements. The base version settles one minor-country pair. Later stages can settle several minor pairs, rarely include a major country, or quiet broader war clutter when many conflicts are active.

The event uses a dynamic weight cap. The cap rises with active wars and safe minor-war candidates, is usually below default event prominence, never exceeds `1500`, and is multiplied down by stronger evolution stages and normal repeatable decay.

## Implementation warning

The source spec intentionally avoids broad focus trees, country packages, formables, scripted GUI windows, or high-spectacle presentation. Adding them would make this low-impact Peace-cluster member too heavy. Future Peace-cluster members can reuse the helper patterns planned here.
