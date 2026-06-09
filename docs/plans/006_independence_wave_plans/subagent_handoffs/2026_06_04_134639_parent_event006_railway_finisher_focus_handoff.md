# Event 006 Railway Finisher Focus Handoff

Timestamp: 2026-06-04 13:46 UTC

Parent tranche: bounded railway route-family finisher for Event 006 Independence Wave.

## Scope

Added a final railway focus for the existing Timetable Authority path. This tranche did not touch flags, country files, history files, Event 005 files, or asset files.

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`

## Implementation

- Added focus `independence_wave_railway_league`.
  - Position: `x = 8`, `y = 11`.
  - Prerequisite: `independence_wave_railway_dispatch_ministry`.
  - Available only for Event 006 railway packages with `independence_wave_timetable_authority_proclaimed`.
  - Bypasses on `independence_wave_focus_railway_league`.
  - Uses existing sprite `GFX_focus_independence_wave_railway_yard`.
- Added effect `independence_wave_focus_railway_league`.
  - Sets `independence_wave_focus_railway_league`.
  - Adds railway-league cohesion and legitimacy.
  - Adds train stock.
  - Improves a controlled core rail/high-infrastructure state with a rail construction level.
- Added constants:
  - `constant:independence_wave_focus.railway_league_cohesion_gain`
  - `constant:independence_wave_focus.railway_league_legitimacy_gain`
  - `constant:independence_wave_focus.railway_league_train_gain`
  - `constant:independence_wave_focus.railway_league_building_level`
- Added localisation:
  - `independence_wave_railway_league`
  - `independence_wave_railway_league_desc`
- Updated docs to describe the railway finisher and current `110`-focus count.

## Validation

- Brace balance passed on touched script, localisation, and docs files: all `balance=0 min=0`.
- Unsupported operator scan over touched files found no `<=` or `>=`.
- Localisation check passed:
  - UTF-8 BOM present.
  - No `:0` keys in `localisation/english/006_independence_wave_l_english.yml`.
  - All focus ids in `common/national_focus/006_independence_wave_focus.txt` have name and description localisation.
- Focus count check:
  - Actual `focus = {` blocks: `110`.
  - `docs/events/006_independence_wave.md` now says `110 focuses`.
- Coordinate check:
  - `independence_wave_railway_league` is at `(8,11)`.
  - The initial `(10,11)` collision with `independence_wave_send_permanent_delegation` was fixed before handoff.
  - Remaining duplicate coordinates are pre-existing overlay-family overlaps outside this tranche.
- Event 005/PRA/Soviet scan:
  - New focus and effect blocks have no Event 005, PRA, Soviet, or collapse references.
- Asset reference check:
  - Reused sprite `GFX_focus_independence_wave_railway_yard` is registered in `interface/006_independence_wave_icons.gfx`.

## Subagent audit

Bounded focus-tree audit passed:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_134446_event006_railway_finisher_focus_audit.md`

The auditor confirmed reachability, existing railway proof, centralized constants, valid reward effects, localisation/doc alignment, current 110-focus count, unique new focus coordinate, and no Event 005/PRA/Soviet runtime coupling.

## Simplifications, omissions, and blockers

- No flags or new assets were created.
- No new animation or bespoke railway art was added; final visual/animated railway route support remains a separate Event 006 asset blocker.
- This tranche closes the railway focus-route finisher gap only. Generic Free Port, Canal, Protected Mandate, Oil Protectorate, and Municipal Authority families still need broader non-railway route-family finishers.
- HOI4 was not launched from this environment.
