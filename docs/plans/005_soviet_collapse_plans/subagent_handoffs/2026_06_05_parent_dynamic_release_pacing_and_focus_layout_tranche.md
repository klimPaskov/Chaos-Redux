# Event 005 Parent Handoff: Dynamic Release Pacing And Focus Layout Tranche

## Scope

This tranche tightened Soviet Collapse follow-on release pacing so non-base republics and custom pressure successors do not appear just because the chaos tier is high. Higher chaos now opens broader pools and increases burst size, while actual releases require dynamic crisis pressure.

No flag assets were touched.

## Changed Files

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - Added `is_soviet_collapse_nonbase_release_tier_open`.
  - Added `has_soviet_collapse_dynamic_follow_on_release_pressure`.
  - Added `is_soviet_collapse_pressure_successor_release_tier_open`.
  - Added `has_soviet_collapse_pressure_successor_follow_on_release_pressure`.
  - Internal/dynamic union candidates now require the non-calm tier gate plus real non-base pressure.
  - Custom pressure successors now require chaos-tier availability plus severe/real crisis pressure.
- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Follow-on burst counts now use the same dynamic gates as candidate selection.
  - Pressure-successor bursts are zeroed unless the severe/real pressure gate is open.
  - Dynamic follow-on backlog no longer fires from tier alone.
- `docs/events/005_soviet_collapse.md`
  - Updated release-system documentation to state that Gathering Storm and higher tiers open pools, while union threat, progressive pressure, failed objectives, regional cascades, war pressure, or severe components drive actual non-base releases.
- `common/national_focus/005_soviet_collapse_republics.txt`
  - Coordinate-only fixes for Ukraine, internal republics, Central Asia, and Kazakhstan branches.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Coordinate-only fixes for CFR construction/security and coercive-city branches.

## Validation

- Brace balance checked on touched script/focus/doc files: all depth `0`.
- `git diff --check` passed for touched files.
- Focus coordinate/prerequisite audit passed:
  - duplicate coordinates: `0`
  - same-row/upward prerequisite line risks: `0`
- Visible generic focus helper-stack scan: `flagged_visible_generic_focuses 0`.
- Unsupported operator scan on touched Event 005 files found no `<=` or `>=`.

## Remaining Risks

- This is not a full completion pass for the broader Soviet Collapse overhaul. Focus-tree depth, country-specific branch identity, evolution spreadsheet parity, and remaining decision/influence polish still need their own tranches.
