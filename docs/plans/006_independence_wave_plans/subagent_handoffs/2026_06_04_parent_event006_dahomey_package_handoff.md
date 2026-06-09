# Event 006 Dahomey Package Handoff

## Scope

Implemented the narrow `iw_pkg_dahomey` tranche as a high-chaos historical-return package.

The package uses vanilla `DAH` and state `776` only. Vanilla Dahomey tag data, country history, state core, localisation, advisor characters, and all ideology flag files exist. Vanilla `common/characters/DAH.txt` does not provide a clear country-leader role, so this tranche represents authority through Event 006 package state, spirit, focus nodes, decisions, and event-log entries instead of adding a bespoke leader or portrait.

## Behavior Added

- Added high-chaos DAH candidate gating through `can_independence_wave_seed_dahomey_package`.
- Added DAH to the special candidate exclusion path so it only enters the pool through the verified package gate.
- Added state `776` as the reduced-release anchor for DAH.
- Added DAH package classification through `independence_wave_package_dahomey`, `constant:independence_wave_package.dahomey`, historical-return tracking, and `constant:independence_wave_decision.formation_family_palace_council`.
- Added startup spirit `independence_wave_dahomey_palace_council_spirit`.
- Added focus overlay nodes:
  - `independence_wave_dahomey_palace_council`
  - `independence_wave_bight_customs_charter`
- Added Formation Ledger decisions and mission:
  - `independence_wave_open_dahomey_palace_council`
  - `independence_wave_register_bight_customs_charter`
  - `independence_wave_proclaim_dahomey_palace_council`
  - `independence_wave_integrate_dahomey_palace_council`
- Added event-log types:
  - `dahomey_palace_formation_type = 42`
  - `dahomey_palace_package_type = 43`
- Added event-log writer effects, package label scripted localisation, GUI log type localisation, and player-facing localisation.
- Added Dahomey to old-name AI restraint routing.
- Updated Event 006 docs and country-package spec.

## Vanilla Evidence

- `DAH = "countries/Dahomey.txt"` exists in vanilla `common/country_tags/00_countries.txt`.
- Vanilla `history/countries/DAH - Dahomey.txt` sets capital `776`, politics, technology, convoys, and recruits DAH advisor characters.
- Vanilla `history/states/776-Dahomey.txt` has `add_core_of = DAH`, owner `FRA`, victory point `10919`, and a naval base.
- Vanilla DAH ideology flags exist in large, medium, and small flag folders.
- Vanilla country localisation exists for `DAH`.

## Validation

- `git diff --check` passed on touched files.
- `rg -n '<=|>='` returned no matches on touched files.
- Brace counts were balanced on all touched script files:
  - constants: `20/20`
  - triggers: `628/628`
  - effects: `1600/1600`
  - ideas: `62/62`
  - focus: `626/626`
  - decisions: `931/931`
  - AI strategy: `135/135`
  - Event 006 scripted localisation: `44/44`
  - event-log scripted localisation: `2916/2916`
- Localisation BOM checks returned `efbbbf` for:
  - `localisation/english/006_independence_wave_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
- `rg -n ':0\s*"'` returned no matches on the touched localisation files.
- Focus count is now `68`.
- `git status --short -- gfx/flags common/country_tags common/countries history/countries history/states` returned no changed files.

## Assets and Flags

No new flags or art assets were created. Dahomey reuses vanilla `DAH` flags and existing Event 006 old-state/archival sprites:

- `GFX_decision_independence_wave_archive_claim`
- `GFX_focus_independence_wave_old_name_council`
- `GFX_focus_independence_wave_archive_identity`
- `GFX_idea_independence_wave_sokoto_emirate_federation`

## Remaining Risks

- DAH has vanilla advisors but no verified vanilla country-leader role. This tranche deliberately avoids leader creation to avoid inventing a portrait or leader identity inside a package pass.
- The full Event 006 source-spec pack remains incomplete; this handoff covers only the Dahomey package tranche.
