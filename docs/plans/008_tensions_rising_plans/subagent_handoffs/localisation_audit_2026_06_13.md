# Event 008 Localisation Audit Handoff

## Scope

Audited and patched Event 008 `Tensions Rising` localisation/scripted localisation surfaces named by the parent prompt.

## Files Changed

- `localisation/english/008_world_tension_rises_l_english.yml`

## Keys Changed

- `chaosx.events_log.window.event_details.tensions_rising`
- `super_event.62.q`
- `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_1`
- `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_2`
- `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_3`

## Before And After

Before:

- Event detail text used implementation-flavored wording: `short-lived timer pressure`, `AI readiness pressure`.
- Stage I evolution detail exposed `temporary capped pulse`.
- Stage II detail said `AI countries receive broader readiness pressure`.
- Stage III detail said `timer pressure lasts longer`.
- The super-event quote used a close Hobbes excerpt with lower-case sentence start and `actuall`.

After:

- Event detail now says later incidents gain `fresh momentum` and countries enter `wider military readiness`.
- Stage I says later incidents can briefly gather pace.
- Stage II says governments adopt broader readiness postures.
- Stage III says diplomatic aftershocks linger longer.
- The super-event quote uses a cleaner sourced Hobbes excerpt with sentence-case start and `actual`.
- Quote source checked: Hanover College's `Leviathan` excerpt from Thomas Hobbes, Chapter 13.

Gameplay meaning is unchanged. The patch only removes implementation/cap/timer/AI phrasing from player-facing detail text.

## Dynamic Localisation

No dynamic localisation was added or changed. Existing dynamic branches remain:

- `GetTensionsRisingMainDesc`
- `GetTensionsRisingOption`
- `GetTensionsRisingEffectText`
- Event-log Tensions Rising evolution title/body selectors
- Super-event slot 62 title/quote/remark/description/image selectors

## Audit Results

Missing key list: none found in the audited Event 008 references.

Duplicate key list: none found for Event 008 keys across the audited localisation files.

Scripted localisation issues: no branch-coverage break found. Popup desc/option/effect selectors cover baseline plus stages I-IV, event-log title/body selectors cover stages I-IV on list/history/detail surfaces, and super-event slot 62 maps title/quote/button/desc/image.

Dynamic text opportunities: no required dynamic values were missing from the audited Event 008 text. Achievement thresholds are explicit by design; popup text does not expose relation-pair math.

Cross-surface mismatch notes:

- `chaosx_music_l_english.yml` still contains old `chaosx_super_event_8_*` labels for `The Final Silence`, while the implemented Tensions Rising super-event uses slot 62 and has `chaosx_super_event_62_*` labels. I did not patch slot 8 because it appears to belong to an older separate super-event mapping, not this Event 008 slot.

File encoding concerns: audited `.yml` files retain UTF-8 BOM.

## Validation

Ran task-specific mechanical checks for:

- Event 008 referenced localisation keys from the audited event, achievement, scripted localisation, settings, chaos meter, and super-event files.
- Duplicate Event 008 keys across the audited localisation files.
- UTF-8 BOM on the audited `.yml` files after patching.
- Direct line check for the five changed keys after patching.

Skipped full game parse/load validation because this was a localisation-only patch inside an already dirty multi-file Event 008 worktree.

## Remaining Risks

- Super-event quote wording was checked against online Leviathan excerpt/search sources and tightened, but no dedicated super-event text researcher was spawned for alternate quote candidates.
- The worktree already contained broad Event 008 changes before this audit, so `git diff` for the changed localisation file includes parent implementation changes in addition to this small wording patch.
