# Event 006 Kuban Cossack Rada Package Handoff

## Superseded Status

Superseded by the 2026-06-05 user correction. This handoff is retained as historical tranche documentation only and must not be used as current Event 006 source-of-truth scope. Kuban (`KUB`) is not a currently requested Event 006 package expansion, focus overlay, formable overlay, or asset lane unless the user explicitly reopens it later.

Historical parent implementation tranche was recorded on 2026-06-04, before the 2026-06-05 correction superseded this direction.

## Superseded Historical Scope

This now-superseded handoff previously described an Event 006 Kuban Cossack Rada historical-return package using vanilla `KUB` support.

- Release seed: Krasnodar state `234`.
- Temporary release masking: Sochi `233` and Stavropol `235` KUB cores are masked during release selection and restored afterward as proof/claim territory.
- Package identity: `independence_wave_package_kuban`.
- Package label id: `kuban_cossack_host`.
- Formation family: `formation_family_kuban_cossack_rada`.
- Focuses: `independence_wave_kuban_black_sea_records`, `independence_wave_kuban_petition_map`.
- Decisions and mission: open Black Sea records, map Kuban petitions, proclaim the Kuban Cossack Rada, integrate or discredit the Rada.
- Spirit: `independence_wave_kuban_cossack_rada_spirit`.
- Historical Event Log row claim: Kuban Black Sea Records package and Kuban Cossack Rada formation. This is superseded as current Event 006 scope.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## References

- Offline wiki pages refreshed before edits: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Country creation, and Graphical asset modding.
- Vanilla documentation refreshed before edits: effects, triggers, script concepts, script constants, decisions, AI strategy, modifiers, localisation objects, and characters.
- Vanilla KUB support inspected:
  - `~/projects/Hearts of Iron IV/history/countries/KUB - Kuban Republic.txt`
  - `~/projects/Hearts of Iron IV/common/countries/Kuban Republic.txt`
  - `~/projects/Hearts of Iron IV/common/characters/KUB.txt`
  - `~/projects/Hearts of Iron IV/gfx/flags/KUB.tga`
  - `~/projects/Hearts of Iron IV/gfx/flags/medium/KUB.tga`
  - `~/projects/Hearts of Iron IV/gfx/flags/small/KUB.tga`

## Validation

- Brace balance across touched Event 006 script files: all `0`.
- Unsupported operator scan for `<=` and `>=`: no matches.
- Focus count: `119` `focus = {` blocks.
- Kuban focus IDs present: `independence_wave_kuban_black_sea_records`, `independence_wave_kuban_petition_map`.
- Localisation BOM preserved for:
  - `localisation/english/006_independence_wave_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
- Localisation `:0` count: `0`.
- Kuban decision, focus, spirit, package label, tooltip, and Event Log localisation keys present.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` zip test: ok.
- Source workbook XML: `119-focus` count `2`, `117-focus` count `0`, `115-focus` count `0`, formula-error strings `0`.
- LibreOffice round-trip output `/tmp/chaosx_catalog_validate_event006_119/chaos_redux_events_catalog.xlsx`: zip test ok, `119-focus` count `2`, `117-focus` count `0`, `115-focus` count `0`, formula-error strings `0`.
- `git diff --check` on touched tranche files: clean.
- Audit subagent `019e9318-5b39-70f3-9b97-4dd0c12ca94e` returned no KUB tranche issues.

## Flags

No KUB flag assets were edited or created in the mod. Vanilla KUB large, medium, and small flags exist and are reused.

## Residual Risks

- No game parser or live-session validation was run by the parent.
- The wider Event 006 goal remains incomplete; this handoff only covers the bounded Kuban package tranche.
