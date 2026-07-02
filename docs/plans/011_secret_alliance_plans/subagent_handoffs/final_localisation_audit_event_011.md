# Event 011 Secret Alliance Final Localisation Audit

Status: PASS

## Scope

Audited the requested Event 011 localisation and scripted-localisation surfaces:

- `localisation/english/011_secret_alliance_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `events/011_secret_alliance.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/ideas/011_secret_alliance_ideas.txt`
- `common/factions/templates/011_secret_alliance_pact.txt`
- `interface/011_secret_alliance_dossier.gui`
- `common/achievements/chaos_redux_achievements.txt`

I also checked the Event 011 super-event music ids in `music/chaosx_super_event_music.asset` and `music/chaosx_super_event_music.txt` so the music localisation coverage could be validated.

## Changed Files

- `localisation/english/011_secret_alliance_l_english.yml`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/final_localisation_audit_event_011.md`

No gameplay decisions, effects, triggers, ideas, events, faction templates, achievements, or GUI script files were edited.

## Changed Keys

- `secret_alliance_dossier_gui_actions`
- `secret_alliance_recommended_war`
- `secret_alliance_recommended_after`

## Before And After

- `secret_alliance_dossier_gui_actions`
  - Before: described the UI as "targeted decisions".
  - After: describes the same country-card action family in player-facing terms: registry sweeps, backchannels, dossier releases, and fracture operations.
- `secret_alliance_recommended_war`
  - Before: used the more mechanical phrase "targeted fracture".
  - After: keeps the same advice but reads as an action against exposed signatories.
- `secret_alliance_recommended_after`
  - Before: mentioned achievements and aftermath cleanup in player-facing text.
  - After: replaces implementation/achievement wording with in-world claim, exit, and post-crisis accounting language.

## Missing Key List

None found.

The audit checked 260 Event 011-related references from events, decisions, custom cost text, idea ids, faction template names/goals/rules, scripted GUI text references, achievements, Event Log scripted localisation, super-event 111 scripted localisation, and super-event 111 music ids. All resolved to existing localisation keys.

## Duplicate Key List

None found for Event 011 key namespaces:

- `secret_alliance*`
- `011_secret_alliance*`
- `chaosx.nr11*`
- `chaosx_super_event.111*`
- `chaosx.event_name.11`
- Event Log Secret Alliance keys
- Secret Alliance faction goal/rule keys
- Secret Alliance achievement tooltip keys

## Scripted Localisation Issues

None blocking.

- `GetSecretAllianceStageName`, `GetSecretAllianceMemberStatus`, `GetSecretAllianceMemberActivity`, `GetSecretAllianceIncidentLineOne`, `GetSecretAllianceIncidentLineTwo`, `GetSecretAllianceIncidentLineThree`, and `GetSecretAllianceRecommendedAction` are defined and every Event 011 localisation call to those scripted localisation helpers resolves.
- Every `localization_key` used by `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` resolves to an existing key.
- Event Log selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` cover Event 011 name, event details, and evolution stages.
- Super-event slot 111 selectors in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` cover title, quote, remark, description, and image.

## Dynamic Text Opportunities

No required dynamic localisation patch remains.

Non-blocking notes for parent review:

- Dossier card text directly uses global event targets such as `[secret_alliance_founder_convener.GetName]`. The scripted GUI visibility gates require the matching event target and known-member state, so this is not currently a blocker.
- `secret_alliance_dossier_gui_values_left` and `secret_alliance_dossier_gui_values_right` are present but the current dossier GUI uses `secret_alliance_dossier_gui_top_meters` instead. This is harmless unused text unless the parent intends to expose separate left/right value panels later.

## Cross-Surface Mismatch Notes

None found.

- `chaosx.event_name.11` is present as "Secret Alliance".
- Super-event 111 title, description, quote, and button text are present.
- Super-event 111 music labels are present for `0_5`, `1_0`, `1_5`, `2_0`, `2_5`, and `3_0`, matching the music asset references found for the slot.
- Event popup ids `chaosx.nr11.1`, `.11`, `.21`, `.31`, `.40`, `.50`, and `.90` have the expected visible keys for their scripted usage.
- Achievement ids and custom achievement tooltips in `common/achievements/chaos_redux_achievements.txt` are covered.

## File Encoding Concerns

None found.

The four scoped `.yml` files are UTF-8 with BOM:

- `localisation/english/011_secret_alliance_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

The same pass found no `:0` keys and no leading-space localisation keys in the scoped `.yml` files.

## Recommended Fixes

Completed in this audit:

- Removed player-facing "targeted decisions" wording from `secret_alliance_dossier_gui_actions`.
- Removed achievement and cleanup wording from `secret_alliance_recommended_after`.
- Smoothed the war recommendation wording for `secret_alliance_recommended_war`.

No remaining required localisation fix is recommended before parent review.

## Validation

Meaningful checks run:

- BOM check on all four scoped `.yml` files.
- `:0` and leading-space key scan on all four scoped `.yml` files.
- Event 011 duplicate-key scan across English localisation files.
- Event 011 reference-resolution audit across the scoped event, decision, idea, faction template, GUI, achievement, scripted localisation, Event Log, super-event, and music-label surfaces.
- Custom cost triad coverage check for every Event 011 `custom_cost_text`.
- Scripted localisation call check for every `GetSecretAlliance*` call present in Event 011 localisation.
- Targeted read of the scripted GUI visibility gates for dossier country cards.

Results after patch:

- Missing referenced keys: 0
- Duplicate Event 011 keys: 0
- Undefined `GetSecretAlliance*` scripted localisation calls: 0
- Event 011 custom cost triads missing keys: 0
- `:0` keys in scoped `.yml` files: 0
- Scoped `.yml` BOM failures: 0

Skipped validation:

- I did not run the game or edit gameplay scripts. This audit was scoped to localisation/scripted-localisation integrity and small text patches only.

## Remaining Risks

- The Event 011 localisation file is currently untracked in the workspace, so this patch sits on top of parent-owned untracked Event 011 work. I did not create a git commit to avoid committing the parent-owned untracked package and unrelated Event 014 changes.
- Quote/source and audio-license verification were not re-researched in this localisation audit. Super-event 111 localisation and music label coverage are present, but source-documentation judgement remains with the parent super-event/audio handoff.

## Simplifications, Omissions, And Blockers

No simplifications were made to Event 011 localisation coverage.

No blockers remain from the localisation/scripted-localisation scope.
