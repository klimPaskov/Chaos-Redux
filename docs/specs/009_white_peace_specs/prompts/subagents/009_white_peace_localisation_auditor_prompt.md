# Subagent Prompt — chaosx_localisation_auditor — Event 009 White Peace

Spawn with `fork_context=false`.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- relevant localisation wiki pages
- `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md`
- `docs/specs/009_white_peace_specs/specs/009_white_peace_event_text_log_cluster.md`

Audit or patch only Event 009 localisation surfaces:

- event name/debug name;
- popup titles/descriptions/options;
- event detail text;
- evolution detail text;
- history row text;
- Peace cluster detail/member/skip reasons;
- dynamic actor/partner text;
- achievement text if implemented.

Check for missing keys, duplicate keys, raw trigger exposure, wrong encoding, dynamic localisation leaks, update-history wording, and mismatch between event text and catalog/detail wording.

If patching, write a handoff under `docs/plans/009_white_peace_plans/subagent_handoffs/` with changed files and keys.
