# Event 042 change ownership

First source-repair commit: `09958b40d78e2544b69dcc2aa5f307577e189797`.
Manual-guard follow-up commit: `2e1115177a1a29ce2c4cf02035afbf9e5a501125`.
The follow-up changes only manual-delivery guards, their source tests, eligibility wording and documentation.
Shared integration hunks owned by other agents remain uncommitted; only one caller-initialization line in `chaosx_settings_effects.txt` belongs to the first commit.

## First commit paths

| Change | Path |
| --- | --- |
| A | `.tools/test_event042_recovery.py` |
| A | `common/ai_strategy/042_equipment_from_heavens.txt` |
| A | `common/dynamic_modifiers/042_equipment_from_heavens_state_modifiers.txt` |
| A | `common/ideas/042_equipment_from_heavens_cxt_ideas.txt` |
| A | `common/on_actions/042_equipment_from_heavens_cxt_on_actions.txt` |
| A | `common/on_actions/042_equipment_from_heavens_on_actions.txt` |
| A | `common/script_constants/042_equipment_from_heavens_constants.txt` |
| A | `common/scripted_effects/042_equipment_from_heavens_achievement_effects.txt` |
| A | `common/scripted_effects/042_equipment_from_heavens_cxt_effects.txt` |
| A | `common/scripted_effects/042_equipment_from_heavens_effects.txt` |
| A | `common/scripted_effects/042_equipment_from_heavens_registry_effects.txt` |
| A | `common/scripted_effects/042_equipment_from_heavens_special_effects.txt` |
| M | `common/scripted_effects/chaosx_settings_effects.txt` |
| A | `common/scripted_localisation/042_equipment_from_heavens_scripted_localisation.txt` |
| A | `common/scripted_triggers/042_equipment_from_heavens_triggers.txt` |
| A | `common/technologies/042_equipment_from_heavens_fielding_technologies.txt` |
| A | `docs/events/042_equipment_from_heavens/overview.md` |
| A | `docs/events/042_equipment_from_heavens/systems/assets.md` |
| A | `docs/events/042_equipment_from_heavens/systems/special_equipment_registry.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/agent_decisions_2026-10-05.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/catalog_changes_pending.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/assets_contact.png` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/ai_strategy/042_equipment_from_heavens.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/script_constants/042_equipment_from_heavens_constants.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/scripted_effects/042_equipment_from_heavens_achievement_effects.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/scripted_effects/042_equipment_from_heavens_effects.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/scripted_effects/042_equipment_from_heavens_registry_effects.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/common/scripted_effects/042_equipment_from_heavens_special_effects.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/before/events/042_equipment_from_heavens.txt` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/mcp_final.json` |
| A | `docs/plans/042_equipment_from_heavens_plans/evidence/mcp_parent.json` |
| A | `docs/plans/042_equipment_from_heavens_plans/release_review_2026-10-05.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/subagent_handoffs/completion_2026-10-05.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/subagent_handoffs/localisation_2026-10-05.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/subagent_handoffs/probability_2026-10-05.md` |
| A | `docs/plans/042_equipment_from_heavens_plans/subagent_handoffs/skill_note_2026-10-05.md` |
| M | `docs/specs/042_equipment_from_heavens_specs/specs/042_equipment_from_heavens_spec_part_4_ai_presentation_and_acceptance.md` |
| D | `events/042_equipment_from_heaven.txt` |
| A | `events/042_equipment_from_heavens.txt` |
| A | `gfx/achievements/042_equipment_from_heavens_borrowed_nightmare.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_borrowed_nightmare_grey.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_borrowed_nightmare_not_eligible.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_nuclear_lottery.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_nuclear_lottery_grey.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_nuclear_lottery_not_eligible.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_tiny_arsenal_state.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_tiny_arsenal_state_grey.dds` |
| A | `gfx/achievements/042_equipment_from_heavens_tiny_arsenal_state_not_eligible.dds` |
| D | `gfx/event_pictures/042_equipment_from_heaven/news_equipment_heavens.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_aircraft_field.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_atomic_cache.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_chaos_cargo.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_crate_fields.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_overwhelmed_depot.dds` |
| A | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_vehicle_descent.dds` |
| A | `interface/042_equipment_from_heavens.gfx` |
| D | `localisation/english/042_equipment_from_heaven_l_english.yml` |
| M | `localisation/english/042_equipment_from_heavens_l_english.yml` |

## Manual-guard follow-up paths

- `.tools/test_event042_recovery.py`
- `common/scripted_effects/042_equipment_from_heavens_effects.txt`
- `common/scripted_effects/042_equipment_from_heavens_achievement_effects.txt`
- `localisation/english/042_equipment_from_heavens_l_english.yml`
- `docs/events/042_equipment_from_heavens/overview.md`
- `docs/plans/042_equipment_from_heavens_plans/agent_decisions_2026-10-05.md`
- `docs/plans/042_equipment_from_heavens_plans/release_review_2026-10-05.md`
- `docs/plans/042_equipment_from_heavens_plans/subagent_handoffs/completion_2026-10-05.md`
- `docs/plans/042_equipment_from_heavens_plans/files_changed_2026-10-05.md`

A documentation-only correction clarifies that an AI recipient can acknowledge its discovery before the orchestrator switches tags. Complete popup acceptance uses the direct fresh-USA fixture.
