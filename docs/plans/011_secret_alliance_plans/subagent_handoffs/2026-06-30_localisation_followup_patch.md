# Event 011 localisation follow-up patch

## Scope

Audited Event 011 Secret Alliance localisation, scripted localisation, Event Details wording, achievement localisation, music labels, super-event text, duplicate keys, key coverage, and BOM state against the current implementation and `docs/specs/011_secret_alliance_specs/`.

`AGENTS.md` was deleted in the working tree, so I read the repository instructions from `git show HEAD:AGENTS.md` without restoring or changing the file.

## Changed files

- `localisation/english/011_anti_player_pact_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

## Changed keys

- `chaosx_super_event.28.q`
- `chaosx.events_log.window.event_details.secret_alliance`
- `chaosx.events_log.window.evolution_details.secret_alliance.title.stage_4`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.stage_4`
- `chaosx_super_event_28_0_5`
- `chaosx_super_event_28_1_0`
- `chaosx_super_event_28_1_5`
- `chaosx_super_event_28_2_0`
- `chaosx_super_event_28_2_5`
- `chaosx_super_event_28_3_0`
- `secret_alliance_open_file_DESC`
- `secret_alliance_open_file_tooltip`
- `secret_alliance_empty_chairs_DESC`
- `secret_alliance_empty_chairs_tooltip`
- `secret_alliance_no_one_came_tooltip`
- `secret_alliance_border_knife_DESC`
- `secret_alliance_border_knife_tooltip`
- `secret_alliance_counter_pact_DESC`
- `secret_alliance_counter_pact_tooltip`
- `secret_alliance_alone_against_room_DESC`
- `secret_alliance_alone_against_room_tooltip`
- `secret_alliance_last_signature_DESC`
- `secret_alliance_last_signature_tooltip`
- `secret_alliance_clean_reveal_tooltip`
- `secret_alliance_war_case_DESC`
- `secret_alliance_war_case_tooltip`

## Before and after

- Super-event quote: previously used only the second sentence of the researched Thucydides excerpt. Now uses the researched full excerpt and attribution from `docs/super_events/011_secret_alliance_super_event_research.md`.
- Event Details and evolution details: previously named hidden-member war or war-caused reveal triggers directly. Now describe the same public collapse in in-world terms without exposing trigger phrasing.
- Music labels: previously showed the working label `Secret Alliance Reveal`. The parent integration later moved Event 011 from the conflicting super-event slot `11` to slot `28`; Event 011 now shows the sourced track title `La Puerta Del Vino` across all slot `28` volume variants.
- Achievement localisation: several descriptions and tooltips were much weaker than the actual predicates in `common/achievements/chaos_redux_achievements.txt`. They now describe founding-member exposure, founding-member removal, low-turnout war reveal, border reprisal before exposure, friendly-government rally plus survival, minor target victory against a patron-backed pact, founding-member cleanup, clean evidence reveal, and war-case victory with no core-state loss.

## Missing key list

No missing Event 011 localisation references were found across the named Event 011 scripts and scripted localisation files after the patch.

## Duplicate key list

No duplicate keys were found in the named localisation files:

- `localisation/english/011_anti_player_pact_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

## Scripted localisation issues

No broken Event 011 scripted localisation selector was found in:

- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`

Event 011 selectors for super-event image, title, quote, remark, description, event name, event details, and evolution details are present.

## Dynamic text opportunities

- Decision custom cost text uses static localisation keys such as `secret_alliance_trace_pouches_cost_text`. The matching `_blocked` keys exist but are not referenced directly by `common/decisions/011_secret_alliance_decisions.txt`. If `custom_cost_trigger` does not color the displayed `custom_cost_text` in-game, blocked cost lines will not use the red variants. I did not change this because it may need a decision-owner pass to confirm the intended UI pattern.
- Dossier Board value localisation already uses integer formatting for core values through `|0`.
- Public pact and live super-event title use dynamic target scope through `[secret_alliance_target.GetName]`. Event Details wording uses generic target-country language so the catalogue remains stable after cleanup clears the target scope.

## Cross-surface mismatch notes

- Achievement UI was the main mismatch. It now aligns more closely with the implementation predicates in `common/achievements/chaos_redux_achievements.txt`.
- Music UI now aligns with the sourced audio research note instead of the working role label.
- Super-event quote now aligns with the researched text package.
- Event Details and the stage 4 evolution detail no longer expose the hidden-member war trigger as directly.

## File encoding concerns

The four named localisation files have UTF-8 BOM after the patch. The three named scripted localisation `.txt` files are mixed, with Event 011's file carrying BOM and the two shared scripted localisation files not carrying BOM. The user only required BOM for localisation files, so I did not alter shared scripted localisation encoding.

## Validation performed

Ran a task-specific PowerShell audit over the primary Event 011 files for:

- UTF-8 BOM state on named localisation files.
- Em dash count.
- Semicolon count.
- `:0` localisation key format.
- Duplicate keys in named localisation files.
- Event 011 localisation references from primary scripts and scripted localisation.
- Remaining working-label hits for `Secret Alliance Reveal`, `Evolution II`, `war-caused`, and `post-reveal deadline` in patched files.

Results after patch:

- No missing Event 011 localisation references found.
- No duplicate keys found in named localisation files.
- No `:0` keys found.
- No em dashes or semicolons found in the primary Event 011 prose files checked.
- Patched localisation files kept UTF-8 BOM.
- No remaining hits for the checked working-label phrases in patched files.

## Skipped validation

I did not run the game or validate HOI4 UI rendering. This was a localisation audit and small text patch, and the meaningful checks available in this scope were static key, encoding, and cross-surface wording checks.

## Remaining risks

- The decision cost red/blocked display should be verified by the decision owner if the UI does not automatically color `custom_cost_text` through `custom_cost_trigger`.
- Event 011's final audio documentation now records slot `28`, the `chaosx_super_event_28_*` track family, and the `music/chaosx_music_track_list.html` row.
- I did not alter broad achievement mechanics. This patch only aligns the player-facing achievement wording with the current predicates.

## Plan handoff path

No new design plan was written. This handoff is the patch record.
