/goal Implement Event 009 White Peace to the fullest extent from `docs/specs/009_white_peace_specs/`. Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and relevant HOI4 wiki/vanilla docs before editing.

Use `prompts/009_white_peace_coding_prompt.md`, `prompts/009_white_peace_asset_prompt.md`, and `prompts/009_white_peace_achievement_prompt.md` as implementation handoffs.

Non-negotiables: Event 9 is a repeatable Peace cluster ID 4 member; unavailable if no active war or no safe settlement pair; forced one-option settlement; base branch settles one safe minor-vs-minor pair; later stages can settle multiple minor pairs, rarely involve majors, and later quiet broader safe war clutter. Avoid civil conflicts, protected scripted wars, near-capitulation cases, recent pair repeats, unsafe subject/faction states, and special/nonhuman threat actors.

Dynamic weight is required: usually below default 1000, rises with active wars and safe minor-war candidates, environment cap never above 1500, higher evolution stages reduce likelihood, and normal repeatable recovery/decay still applies.

Implement event logs, event details, evolution details, Peace cluster detail, localisation, docs, catalog alignment, report-image/achievement icon handoffs, achievements where supported, and helper documentation. Use `chaosx_scripted_system_architect` for reusable helpers, `chaosx_localisation_auditor` before completion, `chaosx_event_completion_auditor` before claiming done, and `chaosx_spreadsheet_doc_worker` after final wording exists.

Keep iterating until the implementation satisfies the spec. Do not claim completion with fallbacks, placeholder logic, missing dynamic weights, missing safety gates, missing localisation, missing docs, missing achievements/assets, or unreported simplifications. Provide a concrete completion report with files changed, helpers, constants, variables/flags, validation scenarios, assets, achievements, and blockers.
