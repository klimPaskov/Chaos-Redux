# Event 009 White Peace Localisation Audit Handoff

## Parent Resolution

The parent implementation resolved the gameplay-text follow-ups that were outside the localisation auditor's edit scope:

- Visible report variants now use variant-specific option keys (`chaosx.nr9.2.a` through `chaosx.nr9.5.a`) while preserving a single acknowledgement option per popup.
- Peace cluster availability now exposes compact White Peace skip reasons for no active wars, no safe pair, recent settlement memory, major-stage lock, and protected/special conflicts.

## Scope

Audited Event 009 player-facing localisation and scripted-localisation selectors in:

- `localisation/english/009_white_peace_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `events/009_white_peace.txt`
- `common/achievements/chaos_redux_achievements.txt`
- Event 009 specs and docs named in the audit prompt

## Findings

### Missing Key List

- No missing keys found for the implemented visible report events:
  - `chaosx.nr9.2.t`
  - `chaosx.nr9.2.d`
  - `chaosx.nr9.3.t`
  - `chaosx.nr9.3.d`
  - `chaosx.nr9.4.t`
  - `chaosx.nr9.4.d`
  - `chaosx.nr9.5.t`
  - `chaosx.nr9.5.d`
  - `chaosx.nr9.2.a`
  - `chaosx.nr9.3.a`
  - `chaosx.nr9.4.a`
  - `chaosx.nr9.5.a`
  - `chaosx.nr9.2.tt`
  - `chaosx.nr9.3.tt`
  - `chaosx.nr9.4.tt`
  - `chaosx.nr9.5.tt`
- `chaosx.nr9.1` is a hidden dispatcher in `events/009_white_peace.txt`, so the spec draft's `chaosx.nr9.1.d` key is not required by the current event script.
- No missing keys found for the Event Details, evolution details, Peace cluster name/detail, or the five White Peace achievement localisation triplets.
- Event name exists as `chaosx.event_name.9`, matching the current repo namespace. The spec draft's `chaosx_event_name_9` / `chaosx_event_debug_name_9` names are not used by the current scripted-localisation selectors.

### Duplicate Key List

- No duplicate keys found among the three audited English localisation files:
  - `localisation/english/009_white_peace_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
  - `localisation/english/chaosx_achievements_l_english.yml`

### Scripted Localisation Issue List

- No broken Event 009 actor/partner localisation syntax found.
- `chaosx.nr9.2.d` uses `[white_peace_primary.GetName]` and `[white_peace_partner.GetName]`, correctly omitting the `event_target:` prefix for event-target localisation.
- Event 009 is present in:
  - `GetEventsLogHistoryEventName` with `value = 9` -> `chaosx.event_name.9`
  - `GetEventsLogClusterMemberEventName` with `value = 9` -> `chaosx.event_name.9`
  - `GetEventsLogEventDetailText` through `constant:white_peace_event_log.event_id`
  - White Peace evolution title/body selectors for history, main evolution view, selected evolution, and event-detail previews.
- Peace cluster name and description selectors are present in both settings and event-log scripted localisation.

### Dynamic Text Opportunities

- The base report already uses dynamic actor and partner names.
- Resolved by parent: the visible event script uses variant-specific option keys, `chaosx.nr9.2.a` through `chaosx.nr9.5.a`.
- Resolved by parent: Peace cluster availability uses Event 009-specific compact skip-reason text.
- Pair counts are not printed in the multi/broad report text. If the existing runtime context exposes a stable settled-pair count to localisation, `chaosx.nr9.3.d` or `chaosx.nr9.5.d` could show it later.

### Cross-Surface Mismatch Notes

- Patched: Event Details previously exposed a full eligibility checklist and "strict checks" wording. It now matches the spec/catalog direction: player-facing premise, evolution summary, and rarity framing.
- Patched: evolution titles previously used shorter labels (`Minor Tables`, `Quiet Giant`, `Circular Settlement`) that did not match the spec's public names. They now use `Repeated Minor Settlements`, `Major-Country Settlement`, and `Broad Diplomatic Settlement`.
- Patched: Peace cluster detail previously listed safety gates. It now matches the cluster wording direction and names White Peace as the low-impact member.
- Patched: White Peace option tooltips previously mentioned settlement checks and memory. They now describe visible settlement results.
- Patched by parent: `achievement_white_peace_the_circular_tooltip` now describes the implemented broad-branch unlock as at least three separate safe conflicts or five safe pairs.
- Resolved by parent: report variants now display variant-specific option text.

### File Encoding Concerns

- `localisation/english/009_white_peace_l_english.yml` is UTF-8 with BOM after edits.
- `localisation/english/chaosx_gui_l_english.yml` is UTF-8 with BOM after edits.
- `localisation/english/chaosx_achievements_l_english.yml` is UTF-8 with BOM after edits.

## Patches Made

### Changed Files

- `localisation/english/009_white_peace_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/plans/009_white_peace_plans/subagent_handoffs/localisation_audit.md`

### Changed Keys

- `chaosx.nr9.2.tt`
- `chaosx.nr9.3.tt`
- `chaosx.nr9.4.tt`
- `chaosx.nr9.5.tt`
- `chaosx.events_log.window.cluster_details.description.peace`
- `chaosx.events_log.window.event_details.white_peace`
- `chaosx.events_log.window.evolution_details.white_peace.title.stage_1`
- `chaosx.events_log.window.evolution_details.white_peace.title.stage_2`
- `chaosx.events_log.window.evolution_details.white_peace.title.stage_3`
- `chaosx.events_log.window.evolution_details.white_peace.body.event_detail`
- `chaosx.events_log.window.evolution_details.white_peace.body.stage_1`
- `chaosx.events_log.window.evolution_details.white_peace.body.stage_2`
- `chaosx.events_log.window.evolution_details.white_peace.body.stage_3`
- `achievement_white_peace_the_circular_tooltip`

### Dynamic Localisation Added or Fixed

- No new scripted-localisation branches were added.
- Existing event-target dynamic localisation for `[white_peace_primary.GetName]` and `[white_peace_partner.GetName]` was audited and left intact.

### Display Before and After

- Before: Event Details exposed internal safety checks.
- After: Event Details describes the player-facing premise, evolution behavior, and rarity pressure.
- Before: option tooltips used implementation terms such as settlement checks and memory.
- After: option tooltips describe what the settlement visibly does.
- Before: evolution detail names did not match the spec/catalog wording.
- After: evolution detail names match the spec's public names.
- Before: the broad achievement tooltip used "safe conflicts."
- After: it uses "three separate safe conflicts or five safe pairs," matching the event documentation.

## Validation Performed

- Confirmed edited localisation files remain UTF-8 with BOM.
- Checked Event 009 popup, tooltip, Event Details, evolution, Peace cluster, and achievement keys are present after edits.
- Checked no duplicate keys among the three audited Event 009-related localisation files.
- Checked no `event_target:` prefix is used in Event 009 localisation strings; `[white_peace_primary.GetName]` and `[white_peace_partner.GetName]` use the correct localisation namespace syntax.
- Checked scripted localisation has Event ID `9` branches for history event names and cluster member event names.
- Checked the patched Event 009-facing localisation no longer contains the audited update-history wording or the removed raw implementation phrases (`settlement checks`, `strict checks`, explicit eligibility checklist, settlement memory).

## Skipped Meaningful Validation

- Did not run the game or inspect runtime UI rendering. This was a localisation/scripted-localisation audit with no gameplay logic edits.
- Parent follow-up edited `events/009_white_peace.txt` to add variant-specific option keys after the localisation-only audit finished.

## Remaining Risks and Blockers

- Parent follow-up added Event 009-specific compact skip-reason text to the Peace cluster availability surfaces.
- The multi/broad report variants do not show dynamic pair counts. This is only worth adding if runtime exposes a stable display variable at report time.
- The worktree had pre-existing modifications in all audited Event 009 files before this audit. I did not revert or normalize unrelated changes.
