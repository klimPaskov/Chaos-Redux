# Event 012 SCN-008 Spreadsheet Alignment Handoff

Date: 2026-06-21

Scope: spreadsheet/catalog alignment only. This is not an Event 012 completion claim and does not replace live scenario validation.

## Workbook

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Sheet: `Main Sheet`
- Row: `13`

## Cells Updated

- `I13` distinguishes the ordinary World Is One route prerequisite chain from the prepared `SCN-008` World Is One manual scenario context.
- `W13` changes the manual scenario id from stale `SCN-012` wording to `SCN-008`.
- `Y13` replaces retired route-variant details with the current two-type behavior: `Africa Is One` forms strong Africa and starts continental wars; `World Is One` starts from that opening, prepares external continent-unifier actors, applies the Congress of Continents identity, starts terminal wars, and sets the Africa World Is One terminal state.
- `Z13` now lists only `Africa Is One; World Is One`.
- `AA13` now matches the current intensity behavior: Low through Maximum scale opening logistics, regional authority seeding, colonial pressure, Totalen Chaos readiness, and World Is One external actor support.
- `AB13` remains `Implemented` for the manual scenario coding surface, while `M13` remains `Needs Testing` for the broader event row.

## Source Alignment

The wording was aligned against:

- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `docs/systems/triggerable_scenarios.md`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`

## Validation

- Re-read row `13` from the workbook after editing.
- Confirmed workbook ZIP integrity after save.

## Remaining Blockers

- Main Event 012 status remains `Needs Testing`.
- Live SCN-008 launch validation remains open.
- Live GUI/animation render proof, AI/balance/exploit proof, deeper route-specific country-package consequences, and final World Is One gate proof remain broader Event 012 blockers.
