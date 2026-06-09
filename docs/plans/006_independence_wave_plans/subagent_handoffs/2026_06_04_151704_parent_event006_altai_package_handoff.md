# Event 006 Altai-Oyrot Kurultai Package Handoff

## Superseded Status

Superseded by the 2026-06-05 user correction. This handoff is retained as historical tranche documentation only and must not be used as current Event 006 source-of-truth scope. Altai (`ALT`) is not a currently requested Event 006 package expansion, focus overlay, formable overlay, or asset lane unless the user explicitly reopens it later.

Historical parent implementation tranche was recorded on 2026-06-04, before the 2026-06-05 correction superseded this direction.

## Superseded Historical Scope

This now-superseded handoff previously described a bounded Event 006 country package for vanilla `ALT` as the Altai-Oyrot Kurultai.

This package is explicitly not an Idel-Ural fallback. Idel-Ural remains blocked until a real accepted carrier exists.

## Vanilla Evidence

- Vanilla tag: `ALT = "countries/Altay.txt"` in `/home/klim/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Vanilla country history: `/home/klim/projects/Hearts of Iron IV/history/countries/ALT - Altai Republic.txt`.
- Vanilla state support:
  - `40` Altai Krai / Barnaul has an `ALT` core.
  - `654` Oyrot Region / Oyrot-Tura has an `ALT` core and is the vanilla capital.
- Vanilla characters and portraits:
  - `/home/klim/projects/Hearts of Iron IV/common/characters/ALT.txt`
  - `GFX_portrait_Grigory_Gurkin`
  - `GFX_portrait_Samuil_Yufit`
- Vanilla flags exist for all ideology variants in normal, medium, and small folders.

## Superseded Historical Implementation Claims

- Added `ALT` candidate gate and package use gate.
- Added state `40` as the reduced-release anchor.
- Temporarily masks state `654` during release selection, then restores it as later proof/claim territory.
- Historical claim only: added an explicit `KUB` anchor selector for Krasnodar `234`, matching the then-current Kuban package documentation and core-mask path. This is superseded as current Event 006 scope.
- Added package identity:
  - `independence_wave_package_altai`
  - package id `altai_oyrot_kurultai`
  - formation family `formation_family_altai_kurultai`
- Added focus mini-overlay:
  - `independence_wave_altai_oyrot_records`
  - `independence_wave_altai_petition_map`
- Added decisions and mission:
  - `independence_wave_open_altai_oyrot_records`
  - `independence_wave_map_altai_petitions`
  - `independence_wave_proclaim_altai_kurultai`
  - `independence_wave_integrate_altai_kurultai`
- Added package spirit:
  - `independence_wave_altai_kurultai_spirit`
- Added AI old-name package restraint for package and records-opened state.
- Added scripted package label and Event Log title routing for list, history detail, event detail, and selected-detail views.
- Updated docs/specs/catalog focus count from `119-focus` to `121-focus`.

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

## Assets and Flags

No mod-side flag, country, country-tag, country-history, or state-history files were changed.

No new flag art was needed because vanilla `ALT` ideology flags exist in normal, medium, and small flag folders. The package reuses existing Event 006 old-name focus/decision/idea icon families.

## Validation

- Focus count: `121` `focus = {` blocks.
- Brace-balance check across touched Event 006 script/localisation files: all `0`.
- Unsupported operator scan across touched files: no forbidden comparison tokens.
- Localisation encoding:
  - `localisation/english/006_independence_wave_l_english.yml`: UTF-8 BOM present, no `:0`.
  - `localisation/english/chaosx_gui_l_english.yml`: UTF-8 BOM present, no `:0`.
- Altai localisation key check: no missing decision/focus/spirit/Event Log keys.
- Focus localisation coverage check: no missing focus names or descriptions.
- Source workbook XML: `121-focus` count `2`, `119-focus` count `0`, `117-focus` count `0`, formula-error strings `0`.
- LibreOffice round-trip output `/tmp/chaosx_catalog_validate_event006_121/chaos_redux_events_catalog.xlsx`: zip test ok, `121-focus` count `2`, `119-focus` count `0`, `117-focus` count `0`, formula-error strings `0`.
- `git diff --check` on touched tranche files: clean.
- `git status --short -- gfx/flags common/country_tags common/countries history/countries history/states`: no output.

## Audit

Read-only subagent audit `019e9330-3dfe-7d50-a935-5a6780aea7bf` returned no issues and made no file changes.

The audit confirmed the high-chaos inactive-ALT gate, state `40` anchor, state `654` mask/restore behavior, Event 006 origin/package classification, decision/focus/spirit/AI/Event Log/doc alignment, no stale fallback framing, and no mod-side flag or country/history/state touches.

## Remaining Scope

This is one bounded package tranche. Event 006 remains incomplete overall because the source spec still tracks remaining dormant/custom-tag packages, deeper railway and strange package work, package-specific non-flag presentation assets, animated route assets, final balance scenarios, and final completion audits.

## Simplifications, Omissions, and Blockers

- Historical claim only: no fallback was used, and `ALT` was framed as Altai-Oyrot rather than Idel-Ural. This is superseded as current Event 006 scope.
- No new flags were created because vanilla `ALT` flags are present.
- No package-specific portrait, seal, or animated route art was created in this tranche; existing Event 006 icon families are reused.
