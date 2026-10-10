# Asset prompt for Event 007 Fury

Read the [accepted release corrections](../specs/007_fury_release_corrections_2026-10-05.md) first; they set the presentation contract for reports and news.
Use [chaos-redux-event-assets](../../../../.claude/skills/chaos-redux-event-assets/SKILL.md) for provenance, alpha, processing, manifest, durable-record, and parent-wiring requirements, and `chaos-redux-frame-animation` for any animated asset.
Inspect the reference folders under `.claude/skills/chaos-redux-event-assets/assets/gfx_references/` that match the asset family before producing anything.

Event ID: `7`.
Event slug: `fury`.
Working asset folder: `docs/assets/007_fury/`.

## Source mode

Fury is a fictional dynamic war mechanic, so its visuals are generated or symbolic.
Do not create portraits of real people for this package.

## Installed assets

These are wired in `interface/007_fury.gfx`, `interface/chaosx_super_events.gfx`, and `interface/chaosx_achievements.gfx`; do not regenerate them.

| Family | Sprites |
| --- | --- |
| News and report | `GFX_news_event_fury_begins` (opening news, preserved mobilisation image), `GFX_news_event_fury_first_conquest` (battle scene), `GFX_report_event_fury_war_office` (event-owned report card) |
| Ideas | the seven Fury ideas and four anti-Fury ideas, `GFX_idea_fury_*` and `GFX_idea_anti_fury_*` |
| Decisions | `GFX_decision_category_fury_war_office`, `GFX_decision_category_anti_fury`, and the target, depots, settlement, coring, terminal reserves, terminal fronts, and anti-Fury response icons |
| Focus families | war office, target files, depots, occupation registers, pact, rivalry, all borders, and world end, each with a shine variant |
| Leader overlay | `GFX_fury_leader_flame_overlay_static` and `GFX_fury_leader_flame_overlay_animated` |
| Super-events | slot `59` `fury_becomes_a_state.dds` and slot `60` `super_event_world_in_fury.dds` |
| Achievements | ten `GFX_achievement_007_fury_*` triplets with grey and not-eligible variants |

The opening-news provenance is in `docs/assets/007_fury/opening_news_2026_10_05/manifest.md`.

## Open asset items

- Legacy provenance for the earlier report, news, idea, decision, focus, and super-event art is unresolved in the release review; record source and generation evidence rather than regenerating approved art.
- The portrait-overlay composition remains visually unaccepted in the GUI audit.
- No faction emblem sprite exists; the native faction uses the default emblem. A generated emblem of converging border arrows around a small central map, without readable text and legible at emblem size, is optional unless the README accepts it.
- An institutional War Directorate portrait (156x210, a table of officers in shadow with maps and files, no single real person) is needed only if the Internal Fury route is accepted; route it to `chaosx_portrait_creator`.
- An aftermath super-event image is needed only if the optional third super-event is accepted; see the super-event prompt.
