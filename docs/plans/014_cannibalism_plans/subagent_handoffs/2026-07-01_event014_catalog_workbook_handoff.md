# Event 014 Catalog Workbook Handoff

Date: 2026-07-01
Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
Sheet: `Events`
Target row: `15` (`Event ID 14`, `Cannibalism`)

## Scope

Updated the Event 014 catalog row to match the current in-game Event Log wording and the final implementation facts documented in `docs/events/014_cannibalism.md`.

No gameplay files, localisation files, or non-catalog spreadsheets were edited.

## Changed Cells

- `C15` `Details`
- `D15` `Evo I`
- `E15` `Evo II`
- `F15` `Evo III`
- `I15` `World-End Scenario`

## Readback

- `C15`: `A fire-once frontline cannibalism outbreak. The event begins as war-horror discipline and supply collapse in a country at war, can be defeated locally by early containment, and every spread country must fight its own outbreak through equipment, trains, convoys, fuel, Army XP, Command Power, manpower, stability, war support, supplied-division, state-control, naval-access, and deadline gates. Exploiting terror units is dangerous. If communes survive, the Cannibal Commune package opens with generated identity assets, starting and reinforcement forces, AI, a 36-focus tree, CBL decisions and missions, a Last Table formable route with its map gate, and cleanup.`
- `D15`: `Ritual Hunger: The outbreak becomes a ritual ideology inside armies, depots, prisons, and field hospitals. It is still fought country by country, but containment now requires breaking doctrine as well as supply collapse.`
- `E15`: `Silent Islands: Organized cults learn to hold isolated territory. Silent islands, barricaded communes, and possible Cannibal Commune declarations become the central risk.`
- `F15`: `The Table Without Borders: The tables begin operating as a global network. Hannibal or another accepted unifier can turn the network into a world-end route once chaos is high enough.`
- `I15`: `The World as Larder: Requires maximum chaos, a global table, enough cult nodes and communes, and Hannibal or an accepted unifier.`

## Validation

- Reopened the workbook after save and read back the edited cells.
- Confirmed the `Events` sheet still uses `freeze_panes = A2`.
- Confirmed touched cells kept wrapped-text formatting and existing style ids:
  - `C15` style `43`
  - `D15` style `50`
  - `E15` style `51`
  - `F15` style `52`
  - `I15` style `55`

## Blockers

None.
