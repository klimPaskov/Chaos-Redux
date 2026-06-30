# Event 011 Secret Alliance Localisation Audit Handoff

## Files Changed

- `localisation/english/011_anti_player_pact_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `docs/events/011_secret_alliance.md`

## Changed Keys And Helpers

- `secret_alliance_plants_cost_text`
- `secret_alliance_plants_cost_text_blocked`
- `secret_alliance_pass_cost_text`
- `secret_alliance_pass_cost_text_blocked`
- `secret_alliance_board_values_left`
- `secret_alliance_board_values_right`
- `chaosx.events_log.window.event_details.secret_alliance`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.event_detail`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.stage_1`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.stage_2`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.stage_3`
- `chaosx.events_log.window.evolution_details.secret_alliance.body.stage_4`
- `secret_alliance_alone_against_room_tooltip`
- `GetSecretAllianceStageText`
- `GetSecretAllianceKnownMembersText`
- `GetSecretAllianceLastIncidentText`

## Behavior Before And After

- Before: Event 011 scripted localisation used the British spelling for the key field, which does not match the HOI4 wiki or the repo's standard scripted-localisation spelling.
- After: Event 011 scripted localisation uses `localization_key` consistently for stage, known-member, and incident text.
- Before: Dossier Board values used `.0` formatting and the right column said `Latest name`.
- After: Dossier Board values use integer formatting with `|0`, and the right column says `Latest member`.
- Before: Two decision cost strings referenced `£GFX_unit_motorized_icon_small`, which I did not find as a valid texticon in the repo.
- After: They use the existing `£GFX_motorized_equipment_text_icon` texticon.
- Before: Event Details and evolution bodies listed hidden mechanic behavior and decision surfaces directly.
- After: They describe the visible diplomatic pattern, public pact, patron escalation, and war reveal in-world.
- Before: `secret_alliance_alone_against_room_tooltip` used a literal working-style pact phrase.
- After: It refers to the public Secret Alliance pact forming against the player without exposing a raw internal key.
- Before: `docs/events/011_secret_alliance.md` listed an older compact report sprite key, while the event and GFX registry use `GFX_report_event_secret_alliance_meeting`.
- After: The doc asset list matches the implemented sprite.

## Validation

- Checked 226 Event 011 localisation references from event, decision, category, idea, faction, Dossier Board GUI, achievement, super-event, and scripted-localisation surfaces. Result: no missing keys.
- Checked Event 011 key namespace duplicates across `localisation/english`. Result: no Event 011 duplicate keys.
- Checked BOM status for the named Event 011 localisation files. Result: `011_anti_player_pact_l_english.yml`, `chaosx_achievements_l_english.yml`, `chaosx_event_names_l_english.yml`, and `chaosx_music_l_english.yml` are UTF-8 with BOM.
- Checked named localisation files for odd unescaped quote counts. Result: no odd quote counts found.
- Checked Event 011 scripted localisation and named dependent scripted-localisation files for brace balance. Result: balanced.
- Searched Event 011 touched text for stale internal labels, the stale compact sprite, the wrong scripted-localisation spelling, `.0` variable formatting, the stale motorized icon, update-history wording, em dashes, and semicolons. Result: no matches after patch.

## Skipped Validation

- I did not launch HOI4 or inspect in-game UI rendering. This pass was limited to static localisation, scripted-localisation, and key-reference validation.

## Remaining Issues And Risks

- Several Event 011 cost text strings are static numbers. They match the current constants, but future tuning changes will require localisation updates unless a broader scripted cost-display helper is added.
- The Event Details text still includes `Anti-[secret_alliance_target.GetName] Pact`. This matches the requested dynamic public pact naming, but if the Event Details catalog can render before `secret_alliance_target` exists, a generic fallback helper would be safer.
- Existing git status shows `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` and `docs/events/011_secret_alliance.md` as untracked in this checkout. I worked with the files named in the task and did not change unrelated repository state.
