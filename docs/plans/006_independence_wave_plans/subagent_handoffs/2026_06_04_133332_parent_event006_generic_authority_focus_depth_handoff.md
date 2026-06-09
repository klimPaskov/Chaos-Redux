# Event 006 Generic Authority Focus Depth Handoff

Date: 2026-06-04

## Scope

Added a bounded second-layer focus tranche for existing Event 006 generic infrastructure and protectorate package lanes. No flags, country tags, country history, state history, portraits, or new visual assets were created or changed.

## Gameplay Changes

- Added six package-gated focus nodes to `common/national_focus/006_independence_wave_focus.txt`:
  - `independence_wave_railway_dispatch_ministry`
  - `independence_wave_free_port_harbor_courts`
  - `independence_wave_municipal_service_patrols`
  - `independence_wave_protectorate_observer_ministry`
  - `independence_wave_oil_field_guard_offices`
  - `independence_wave_canal_pilot_offices`
- Added corresponding scripted effects to `common/scripted_effects/006_independence_wave_effects.txt`:
  - `independence_wave_focus_railway_dispatch_ministry`
  - `independence_wave_focus_free_port_harbor_courts`
  - `independence_wave_focus_municipal_service_patrols`
  - `independence_wave_focus_protectorate_observer_ministry`
  - `independence_wave_focus_oil_field_guard_offices`
  - `independence_wave_focus_canal_pilot_offices`
- Added shared tuning constants to `common/script_constants/006_independence_wave_constants.txt`:
  - `package_route_legitimacy_gain`
  - `package_route_cohesion_gain`
  - `package_route_foreign_attention_gain`
  - `package_route_patron_relief`
  - `package_route_militia_gain`
  - `package_route_claim_ambition_gain`
  - `package_route_stability_gain`
  - `package_route_convoy_gain`
  - `package_route_train_gain`
  - `package_route_fuel_gain`
  - `package_route_building_level`

## Localisation And Docs

- Added focus names and descriptions to `localisation/english/006_independence_wave_l_english.yml`.
- Updated `docs/events/006_independence_wave.md` to describe the second-layer route-state focuses and current 109-focus tree count.
- Updated package and focus-tree specs:
  - `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`

## Validation

- Brace balance passed for touched script/localisation/docs files: all `balance=0 min=0`.
- Unsupported comparison-operator scan passed on touched script/localisation/doc files.
- Localisation encoding check passed: `006_independence_wave_l_english.yml` has UTF-8 BOM and no `:0` keys.
- Focus count/doc alignment passed: current focus tree has 109 focus blocks and the event doc says 109 focuses.
- New focus coordinate scan passed: no overlaps among the six new focus nodes.
- New focus/effect/localisation presence check passed for all six focus IDs and effects.
- Targeted Event005/PRA/Soviet scan inside the six new focus blocks and six new effect blocks returned zero matches.
- Local vanilla/repo precedent check found existing usage for `convoy_1`, `naval_base`, `rail_way`, `add_resource`, and `add_building_construction`.
- `chaosx_focus_tree_auditor` subagent `019e92cd-b6b4-7851-9bfa-2f94aa4593d7` initially found stale doc count and uncentralized new building reward levels; both were fixed. Final bounded re-check returned PASS.

## Residual Risks

- The new focuses gate on package identity and use later decisions for stricter control requirements, matching the existing package overlay pattern. If design later requires the focuses themselves to disappear after state loss, add control triggers to `available`.
- `level = constant:independence_wave_focus.package_route_building_level` is used only in the new route-depth reward effects. Existing older integration rewards remain unchanged at `level = 1`.
- Final visual support for these routes remains incomplete; no new focus icons, seals, animated category art, or flags were produced in this tranche.

## Simplifications, Omissions, And Blockers

- No new country package, tag, flag, leader, or asset work was done.
- This tranche deepens generic authority/protectorate/railway overlays only; it does not complete final route-family finishers or visual assets for Event 006.
