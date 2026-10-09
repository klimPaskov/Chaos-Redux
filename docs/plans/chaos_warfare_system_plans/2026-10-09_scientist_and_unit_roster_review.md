# Scientist chronology and retained unit roster

Disposition: the two accepted conduct-trait dates are implemented in source, and the inactive Livens definitions have an explicit documentation disposition.
Native recruitment, trait delivery and menu behavior remain unproved.
The wider CBRN goal remains incomplete.

The original overhaul requires individual review of all 67 scientists, date-appropriate availability, separate scientific competence and offensive authorization, and distinct retained unit roles.
The parent accepted the two narrow recommendations in the [residual scientist review](subagent_handoffs/2026-10-09_scientist_residual_review.md).
The [accepted correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-09_scientist_conduct_trait_dates.md) records the primary sources and the interpretation of each date.
Rascher's trait begins on 15 May 1941, the date of the documented request rather than a claimed first experiment.
Mengele's begins on 30 May 1943, the documented Auschwitz assignment.
Their existing scientist access remains January 1941 and January 1943 respectively.

## Implementation and preservation

`common/characters/cbrn_historical_scientists.txt` removes only their two static `scientist_trait_inhumane` entries.
`common/scripted_effects/chaosx_startup_history_effects.txt` adds two dated, character-present, one-time award blocks inside the existing German helper.
No character identity, portrait, skill, recruitment date, CSH ownership path, authorization rule or other dated trait award changes.
The historical scientist guide, accepted amendment and requirement ledger link the current date contract.
Event 016 and the separate Germany-Mengele route use their own flags and portrait reuse, with no direct gate on these two historical scientist IDs or their conduct trait in the reviewed consumers.

The [unit follow-up](subagent_handoffs/2026-10-09_remaining_source_gaps.md) traces the seven `livens_projector_support*` definitions through research, AI, templates, native raids and both static and registered CXT paths.
They have `active = no`, no current normal or CXT unlock path in the reviewed source, and no distinct gameplay role from the consolidated battery.
The Event 019 owner inventory labels them inactive legacy entries.
The twelve active CBRN support roles and the Chaos Battalion remain the thirteen-role consolidated package, with provider 521 and the parent-owned support boundary unchanged.
No unit definition, token, registry, template, AI or mastery list was changed by this documentation clarification.

## Evidence and limits

`python docs/testing/2026-10-09_scientist_conduct_traits/source_tests.py` passes 22 source assertions.
The checks preserve byte-exact original snapshots, all 67 IDs, character blocks outside the two removed trait lines, and the entire startup effects source outside the two award blocks after checkout newline normalization.
Date-boundary, already-awarded and absent-character cases retain the intended guards, and the existing callers remain German startup and `on_daily_GER`.
These are source assertions rather than a native character-lifecycle simulation.
The parent reran all 22 assertions in the isolated commit candidate with LF checkout text and byte-preserved before snapshots.

The installed command validator returns `valid = true` for syntax, command kinds and declared scopes of the two additions.
It does not check parameter semantics or execute the awards.
The event inspections and renders remain focused and partial, with helper bodies omitted, so they do not establish runtime event compatibility.
The [event receipt](../../testing/2026-10-09_scientist_conduct_traits/event_route_evidence.json), [command receipt](../../testing/2026-10-09_scientist_conduct_traits/script_validation_evidence.json) and [source results](../../testing/2026-10-09_scientist_conduct_traits/source_test_results.json) retain those boundaries.
No event text, catalog detail, asset, research weight or random-choice weight changed.
No workbook update or CSV export is required.

No gameplay simplification or replacement portrait was introduced.
Native holder transfer, dated trait delivery, exact menu visibility and the broader historical setup remain open acceptance items.
Unused legacy Livens tokens, force-fit reads and helpers remain cleanup candidates, without being treated as extra playable mastery roles.
Skills used: `chaos-redux-subagents`, `chaos-redux-events` and the shared-tree commit workflow.
