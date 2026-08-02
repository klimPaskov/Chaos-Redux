# Event 016 localisation integrity pass

Date: 2026-08-02

Scope: Event 016 localisation files, Event 016 scripted-localisation consumers, and directly referenced event-log, super-event, focus, decision, idea, special-project, and Directorate GUI keys. This pass used `chaos-redux-events` and `chaos-redux-subagents`, the required offline Paradox wiki pages, and the relevant vanilla localisation/script documentation.

## Changed files and keys

- `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`
  - `brilliant_scientist_directorate_gui_animation_tt` now says “animated Directorate presentation” and “still display” instead of exposing “frame-by-frame” and “static fallbacks”.
  - `brilliant_scientist_directorate_gui_animation_static` changed from “static fallbacks” to “still presentation”.
  - `brilliant_scientist_directorate_gui_animation_live` changed from “frame animation” to “animated presentation”.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
  - `chaosx.nr16.6.robotics.d` now says “staged demonstration” instead of “scripted demonstration”, avoiding implementation-sounding wording in the player-facing report.

Before these changes the mechanics and keys were already valid; the edits only clarify the same visible states and report meaning.

## Missing key list

- No missing non-GFX localisation keys were found in Event 016 scripted localisation.
- The Event 016 source scan found 575 candidate title, description, name, tooltip, and localisation-key references across 91 files with zero missing player-facing keys.
- All 101 Kruger State focus IDs have their focus and `_desc` keys; the focus-tree container name has no standalone localisation key and is expected to remain that way.
- Event 016 decision/category IDs, ideas, and 15 special-project IDs all have matching display and description keys.
- All `$KRG_...$` cosmetic-name references resolve.

## Duplicate key list

- No exact duplicate content keys were found after excluding the normal repeated `l_english` header.
- One case-only pair is intentional and must remain distinct: `KRG_XENOBIOLOGICAL_ASCENDANCY` in `016_brilliant_scientist_country_l_english.yml:68` is the cosmetic country tag, while `KRG_xenobiological_ascendancy` in `016_brilliant_scientist_focus_l_english.yml:87` is the focus ID and focus localisation.

## Scripted localisation issue list

- No unresolved Event 016 custom `defined_text` helper references were found.
- The six `common/scripted_localisation/016_*.txt` files contain 517 `localization_key` references (339 unique); all non-GFX keys resolve against English localisation.
- 87 unresolved `GFX_...` tokens are intentional texture/sprite return values from scripted localisation and are not YAML keys. They should not be added to localisation.
- Shared event-log selectors resolve: `brilliant_scientist.evolution.type`, `.summary`, `.1` through `.4` title/description pairs, and `chaosx.events_log.window.event_details.brilliant_scientist` are all present in `016_brilliant_scientist_evolutions_l_english.yml`.

## Dynamic text opportunities

- Several decision and operation descriptions show fixed durations while the script uses constants: `brilliant_scientist_krg_begin_singularity_disarmament_hold_desc` (six months/180 days), `brilliant_scientist_krg_begin_singularity_arming_desc` (one year/365 days), `brilliant_scientist_krg_begin_controlled_singularity_disarmament_desc` (eight months/240 days), `brilliant_scientist_krg_complete_laboratory_world_desc` (eight months/240 days), foreign operation effect tooltips (30/45/60/75/90/120 days), and `brilliant_scientist_convene_cross_domain_review_effect_tt` (120 days). Current text matches current constants, so no dynamic helper was added in this narrow pass; revisit if those constants become player-tunable.
- Resource and stat effect tooltips are intentionally static summaries of the current scripted effects and do not expose raw trigger syntax.

## Cross-surface mismatch notes

- Global event-log name `chaosx.event_name.16` remains “Brilliant Scientist” in `chaosx_event_names_l_english.yml`, matching the Event 016 detail and evolution surfaces.
- Super-event IDs 90–95 are all wired by shared scripted localisation and have title, quote, button, and description keys in `016_brilliant_scientist_super_events_l_english.yml`.
- The focus, decisions, ideas, special projects, GUI text, event reports, aftermath, and event-log surfaces use consistent Brilliant Scientist/Kruger Directorate terminology after the wording cleanup.
- No hidden-route text, raw trigger text, or missing requirement/effect tooltip keys were found in the audited Event 016 localisation surfaces.

## File encoding concerns

- All 16 `localisation/english/016_*.yml` files are UTF-8 with BOM and retain that encoding after the patch.
- No malformed localisation key lines or duplicate content keys were detected.

## Validation and remaining risks

- Ran repository PowerShell key-set scans, scripted-localisation reference scans, focus/decision/idea/project key coverage scans, BOM checks, and targeted `rg` checks for raw trigger or implementation wording.
- No in-game or live GUI validation was run because agents must not launch Hearts of Iron IV; visual layout and consumer validation remain with the parent/user.
- No spreadsheet update was needed because no event meaning, event-log wording, evolution wording, or event detail text changed.
- No gameplay mechanic, fallback route, asset, or script was changed. The only unresolved design choice is whether future timing-constant changes should gain dynamic duration localisation.

