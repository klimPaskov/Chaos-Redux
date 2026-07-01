# Event 015 Localisation Audit Handoff

Subagent: localisation
Scope: Event 015 `utopia_manifesto` localisation and scripted localisation only.

## Files inspected

- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/ideas/015_utopia_manifesto_ideas.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `common/countries/cosmetic.txt`
- `docs/super_events/super_event_quote_sources.md`
- `docs/super_events/super_event_audio_packages.md`
- `docs/events/015_utopia_manifesto.md`

## Patch summary

Changed files:

- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

Changed keys:

- `utopia_manifesto_tree`
- `utopia_open_stores_cost_text`
- `utopia_open_stores_cost_text_blocked`
- `chaosx.events_log.window.event_details.utopia_manifesto`

Behavior/display before and after:

- `utopia_manifesto_tree` displayed as `Tree`. It now displays as `Utopian Manifesto`.
- `utopia_open_stores_cost_text` and blocked variant used `requires stable Surplus` inline. They now use shorter icon-first requirement wording: `Stable Surplus`.
- `chaosx.events_log.window.event_details.utopia_manifesto` described selection pools, AI acceptance, focus tree replacement, and other implementation behavior. It now describes the manuscript, public ledgers, councils, Needful Land proof, and integration work in-world.

Dynamic localisation added or fixed:

- No new scripted or dynamic localisation was added.
- Existing dynamic ledger values in `utopia_manifesto_ledger_gui_values_left`, `utopia_manifesto_ledger_gui_values_right`, and `utopia_manifesto_ledger_gui_footer` already use integer formatting.

## Audit results

Missing key list:

- None found for the audited Event 015 surfaces.
- Focus key coverage checked all 106 focus ids for `id` and `id_desc`.
- Idea key coverage checked all 19 idea ids for `id` and `id_desc`.
- Achievement key coverage checked all 12 Event 015 achievements for `_NAME` and `_DESC`.
- Direct tooltip and name references from the listed Event 015 focus, decision, idea, achievement, and cosmetic files resolved in the inspected localisation files.

Duplicate key list:

- No duplicate keys found inside the four inspected localisation files.
- No duplicate keys found across the four inspected localisation files.

Scripted localisation issue list:

- No broken Event 015 event-name selector found. Event id `15` maps to `chaosx.event_name.15`.
- No broken Event Details selector found. Event id `15` maps to `chaosx.events_log.window.event_details.utopia_manifesto`.
- No broken super-event selector found for Event 015. Slots `151` and `152` are wired for image, title, quote, remark, and description.
- No Event 015 references to `World Tension Subsides`, `015_world_tension_falls`, or `world_tension_falls` were found in the audited files.

Dynamic text opportunities:

- Event 015 cost strings are static while the decision costs are defined through script constants and local file constants. If the parent expects costs to change often, the decision layer should expose current cost values through variables or scripted localisation so the text cannot drift from tuning. This requires gameplay/script support and was not patched by this localisation-only pass.
- The targeted decision descriptions name action types clearly, but some target-specific state names remain in scripted requirements rather than printed in descriptions. This is acceptable for the current narrow pass because custom target tooltips exist.

Cross-surface mismatch notes:

- Achievement `_NAME` and `_DESC` convention is correct for all 12 Event 015 achievements.
- Cosmetic tags `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state` have base, `_DEF`, `_ADJ`, and ideology-specific name coverage in the inspected localisation.
- Event Log name text uses `Utopian Manifesto`, matching the event popup title direction after the old Event 015 replacement.
- Super-event quote and audio documentation for slots `151` and `152` exists in the inspected docs. This audit did not re-research quote wording or audio licensing.

File encoding concerns:

- `015_utopia_manifesto_l_english.yml`, `chaosx_achievements_l_english.yml`, `chaosx_event_names_l_english.yml`, and `chaosx_gui_l_english.yml` all retained UTF-8 BOM after the patch.
- Git reports existing line-ending normalization warnings for `chaosx_gui_l_english.yml`; this audit did not rewrite the file globally.

Recommended fixes:

- Already patched `utopia_manifesto_tree`, `utopia_open_stores_cost_text`, `utopia_open_stores_cost_text_blocked`, and `chaosx.events_log.window.event_details.utopia_manifesto`.
- Parent should consider a later scripted-cost localisation pass if Event 015 tuning is still moving.

## Validation

Meaningful validation run:

- Rechecked UTF-8 BOM on the four inspected localisation files.
- Rechecked duplicate keys inside and across the four inspected localisation files.
- Rechecked focus, idea, and achievement key coverage after the patch.
- Rechecked Event 015 scripted localisation selectors for Event Log and super-event slots.
- Searched the audited Event 015 files for old World Tension strings.

Skipped meaningful validation and why:

- Did not run the game or inspect live UI. This was a localisation/scripted-localisation audit pass.
- Did not validate audio files, sprites, or GUI layout because the prompt limited patch authority to localisation and scripted localisation.

Unresolved wording decisions:

- None requiring parent decision. The remaining dynamic-cost opportunity needs script support if the parent wants it.

Plan handoff path:

- This audit handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_localisation_audit.md`
- No separate improvement plan was written.
