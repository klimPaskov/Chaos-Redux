# Event 013 Natural Disasters Planning Package

This package contains the full source planning handoff for Chaos Redux Event 013 Natural Disasters.

## Contents

- `specs/013_natural_disasters_spec_part_1.md` — core event specification.
- `specs/013_natural_disasters_evolutions_and_variants.md` — evolution and variant design.
- `matrices/013_natural_disasters_decision_mission_map.md` — decision and mission design.
- `matrices/013_natural_disasters_ai_balance_and_validation.md` — AI, balance, helpers, validation.
- `matrices/013_natural_disasters_event_log_catalog_and_localisation_map.md` — event-log, details, catalog, localisation map.
- `prompts/013_natural_disasters_asset_prompt.md` — asset production prompt.
- `prompts/013_natural_disasters_super_event_prompt.md` — super-event research prompt.
- `prompts/013_natural_disasters_achievement_prompt.md` — achievements prompt.
- `prompts/013_natural_disasters_decision_mission_prompt.md` — decision/mission implementation prompt.
- `prompts/013_natural_disasters_coding_prompt.md` — full coding-agent prompt.
- `prompts/013_natural_disasters_goal_prompt.md` — copy-pasteable `/goal` prompt under 4000 characters.
- `prompts/013_natural_disasters_subagent_routing_prompt.md` — bounded subagent routing handoff.
- `research/013_natural_disasters_research_notes.md` — public research notes and URLs.
- `research/013_natural_disasters_source_reading_log.md` — supplied-source reading log.
- `subagent_handoffs/013_natural_disasters_planning_handoff.md` — planning disposition and implementation surfaces.

## Key design decisions

- Event 13 remains a Minor Repeatable event.
- The Natural Disasters cluster contains only Event 13 and keeps Low member severity.
- There is no world-end scenario.
- A manual triggerable scenario launches a compressed disaster barrage.
- Evolution IV absorbs Event 46 Earth Earthquake and turns it into an abnormal earthquake-wave variant inside Event 13.
- The event uses warnings, recovery decisions/missions, dynamic targets, family-specific aftermath, assets, achievements, and optional Evolution IV super-event research gates.
