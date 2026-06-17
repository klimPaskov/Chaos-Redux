# Event 012 Africa Localisation Slot Audit Handoff

Date: 2026-06-16

Subagent role: Chaos Redux localisation audit

## Scope

Audited Event 012 Africa localisation and scripted localisation after mission and super-event wiring.

Primary files inspected:

- `localisation/english/012_african_union_l_english.yml`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `events/012_african_union.txt`
- `docs/super_events/012_africa_super_event_research.md`
- `docs/events/012_africa_foundation.md`

Required context read:

- `AGENTS.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- relevant `effects_documentation.md` and `triggers_documentation.md` tooltip sections
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

## Missing Key List

Current state: no missing Event 012 keys found.

Validated references from Event 012 event titles/options, decision categories, decisions, custom trigger tooltips, custom effect tooltips, custom cost text, focus ids, scripted localisation `localization_key` entries, and super-event slots 68-72.

Note: an initial pass saw five mission availability keys as missing, but `localisation/english/012_african_union_l_english.yml` changed during the audit and the current file contains all five:

- `africa_liberation_front_deadline_available_tt`
- `africa_regional_integration_deadline_available_tt`
- `africa_archive_guard_deadline_available_tt`
- `africa_bestiary_containment_deadline_available_tt`
- `africa_rsa_pretoria_deadline_available_tt`

No patch was made to those keys by this subagent.

## Duplicate Key List

No duplicate keys found inside `012_african_union_l_english.yml`.

No duplicate definitions found elsewhere under `localisation/english/*_l_english.yml` for keys defined in `012_african_union_l_english.yml`.

## Scripted Localisation Issue List

No broken Event 012 scripted localisation references found in `common/scripted_localisation/012_africa_scripted_localisation.txt`.

`GetAfricaSelectedDossierName` maps every visible dossier key currently defined in Event 012 localisation and has a safe `africa_dossier.none` fallback.

`GetAfricaSelectedHighChaosPackageName` maps every visible high-chaos package key currently defined in Event 012 localisation and has a safe `africa_high_chaos_package.none` fallback.

Super-event slots 68-72 have title, quote, remark, and description selectors in `chaosx_scripted_localisation_super_events.txt`, and all referenced `super_event.68.*` through `super_event.72.*` keys exist.

Image selector note: slots 70 and 71 both map to `GFX_super_event_012_archive_bestiary`. This appears plausibly intentional because the generated-art manifest describes the asset as an Archive / Bestiary role with empty crowns and witnesses, and slot 71 is `Counterfeit Crowns`. If the parent wants unique slot imagery, add a dedicated `GFX_super_event_012_counterfeit_crowns` sprite and switch slot 71 to it.

## Dynamic Text Opportunities

Several cost and threshold strings remain static while the script values are centralized in constants:

- cost text keys such as `africa_send_league_aid_cost_tt`, `africa_prepare_liberation_operation_cost_tt`, `africa_raise_border_liberation_columns_cost_tt`, and similar
- category counters `Opened: .../24` and `Unlocked: .../6`
- mission availability text such as "Complete at least three living cores and seat at least two regional authorities."

Current text is correct for the current constants, but future tuning can desync visible text. Recommended follow-up: expose the relevant mission goals and cost values through variables or scripted localisation before another balance pass.

## Cross-Surface Mismatch Notes

Slot 69 naming is inconsistent outside the allowed localisation patch scope:

- `localisation/english/012_african_union_l_english.yml`: `super_event.69.t` is `The Second Scramble`
- `docs/super_events/012_africa_super_event_research.md`: final title candidate is `The Second Scramble`
- `docs/events/012_africa_foundation.md`: slot 69 is `The Second Scramble`
- `music/chaosx_super_event_music.txt` and `music/chaosx_music_track_list.html`: label the same slot as `The Scramble Answers`

Recommended parent fix: rename the slot 69 music comment/table display to `The Second Scramble`, unless the intended final title is being changed across localisation and docs.

The continent-sponsor role is consistently documented as blocked by missing unique final audio and is not assigned to slots 68-72. No localisation mismatch found there.

## File Encoding Concerns

`localisation/english/012_african_union_l_english.yml` is UTF-8 with BOM.

No malformed localisation lines, leading-space keys, or `:0` key syntax found in the Event 012 localisation file.

`common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` currently has mixed CRLF/LF line terminators. This is not a localisation YAML encoding issue, but the parent may want to normalize it in a dedicated formatting pass. I did not normalize it because that would create broad churn in a shared file.

## Recommended Fixes

No Event 012 localisation or scripted-localisation patch was required in the current file state.

Recommended follow-ups:

- `music/chaosx_super_event_music.txt`: align slot 69 comment with `The Second Scramble`.
- `music/chaosx_music_track_list.html`: align slot 69 table title with `The Second Scramble`.
- Future balance pass: make Event 012 cost and mission threshold text dynamic, or add a handoff note requiring text updates whenever the related constants change.
- Optional asset follow-up: create and wire `GFX_super_event_012_counterfeit_crowns` if slot 71 should not share the Archive / Bestiary image.

## Validation Run

Meaningful task-specific checks performed:

- Parsed all Event 012 localisation keys and checked duplicates in-file and across English localisation files.
- Compared Event 012 event, focus, decision, tooltip, custom-cost, scripted-localisation, and super-event slot references against the English localisation key set.
- Verified focus ids and decision/category ids have title and description localisation.
- Verified `super_event.68.*` through `super_event.72.*` are selected by scripted localisation and defined in Event 012 localisation.
- Verified `012_african_union_l_english.yml` has UTF-8 BOM and no malformed key lines.

## Skipped Meaningful Validation

No in-game localisation console validation was run. This pass was limited to repository-level key/reference/encoding checks.

No web quote verification was performed in this audit. Quote wording was checked only for consistency against the existing Event 012 super-event research document.

## Unresolved Wording Decisions

- Whether slot 71 should share the Archive / Bestiary super-event image or receive a dedicated Counterfeit Crowns image.
- Whether the parent wants to keep slot 69 as `The Second Scramble` everywhere or rename the localisation/docs to match the music label `The Scramble Answers`.

## Files Changed By This Subagent

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_localisation_slot_audit_handoff.md`
