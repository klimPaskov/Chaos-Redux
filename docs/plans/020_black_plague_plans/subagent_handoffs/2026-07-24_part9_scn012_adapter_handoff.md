# Event 20 Part 9 SCN-012 Adapter Handoff

## Outcome

The shared Triggerable Scenarios window now reserves collision-free live identity `SCN-012` for Black Plague Unbound and renders its fixed profile, four intensity outcomes, status text, and list entry in every supported sort view.

The scenario is deliberately non-launchable.

Its availability bridge is fail-closed until the Rat Nation package, Rat King package, and atomic Event 20 scenario commit provider each declare readiness.

No disease-only, natural-outbreak, event, or placeholder launch path was introduced.

This is a bounded adapter and audit handoff, not completion of Part 9.

## Changed files and identifiers

- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`: `triggerable_scenario_id.black_plague = 12` and `triggerable_scenario_sort_value.black_plague_name = 0.25`.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`: registry plus name ascending, name descending, ID ascending, and ID descending view entries for `triggerable_scenario_id.black_plague`.
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`: `triggerable_scenario_can_launch_selected` delegates SCN-012 eligibility to the Black Plague bridge.
- `common/scripted_triggers/020_black_plague_scenario_triggers.txt`: `black_plague_scenario_rat_country_package_is_ready`, `black_plague_scenario_rat_king_package_is_ready`, `black_plague_scenario_commit_provider_is_ready`, and `black_plague_scenario_can_launch_from_triggerable_scenarios`.
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`: SCN-012 selected name, row name, row ID, description, fixed type, intensity impact, and launch-status branches.
- `localisation/english/chaosx_gui_l_english.yml`: `chaosx.scenarios.entry.id.black_plague`, `chaosx.scenarios.black_plague.*`, `chaosx.scenarios.type.black_plague.instant_plague_kingdoms`, and `chaosx.scenarios.launch_status.black_plague.*`.
- `docs/systems/triggerable_scenarios.md`: SCN-012 adapter status.
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_9_triggerable_scenario.md` and `docs/specs/020_black_plague_specs/matrices/triggerable_scenario_matrix.md`: corrected the stale planning identity to `SCN-012`.

## Before and after

Before this change, Event 20 had no live scenario identity in the shared registry, no selectable list entry, no SCN-012 display text, and no Scenario-window availability boundary.

After this change, SCN-012 sorts between Africa Is One and Coalition Unmasked in name order, appears between SCN-011 and SCN-013 in numeric order, uses the existing confirmation UI, and refuses confirmation until the three required readiness providers exist.

The generic dispatcher intentionally has no SCN-012 branch because there is no safe transaction to call.

The future transaction implementation must add that dispatch branch and the readiness writer in the same change, never independently set `black_plague_scenario_commit_provider_ready`.

## Severity-sorted issues

### P0: Rat country package does not exist

The current repository contains no country tags, histories, country tag registration, localisation, flags, focus trees, ideas, AI, unit templates, or valid recruitment package for the Rat Nations or the Rat King required by Part 9.

The untracked rat-runtime effect file references Rat Nation tags and a Rat King tag, but the referenced country packages are absent.

No scenario can safely create actors until those packages are complete and their state-transfer, capital, army, portrait, flag, focus, AI, and cleanup behavior are verified.

### P0: No atomic SCN-012 commit transaction exists

There is no Event 20 scenario effect that captures the current intensity, validates eligible continents and basin capacity, initializes or upgrades disease state, sets and clears bootstrap state, seeds states, records Evolutions I through IV once, creates only missing Rat Nations and the Rat King, restores live pulses, refreshes mapmode and the disease board, records event history, and presents the report.

The natural Black Plague outbreak is not an acceptable substitute because it does not satisfy the scenario bootstrap contract.

### P1: Current rat runtime conflicts with the separate Royal Basin requirement

The current rat runtime's Evolution IV route consolidates Rat Nations into the Rat King.

Part 9 instead requires a separately created Rat King and independent Rat Nations that coexist through a grace period.

The scenario must not reuse that consolidating route as its launch path.

### P1: Evolution I and II scenario activation and history ownership are missing

The rat runtime supplies eligibility checks but not complete scenario activation and single-record behavior for Evolutions I and II.

The launch transaction must use one authoritative evolution record for each of I through IV and select the correct Rat Nation or Rat King actor for III and IV.

### P1: No scenario presentation, event-log, or ongoing pulse handoff exists

There is no SCN-012 launch report, Rat King coronation presentation integration, or verified weekly runtime hook for rat growth, dominance, and disease reconciliation after bootstrap.

### P2: Scenario-specific achievement and shortcut cleanup are not implemented

The eventual successful transaction needs a permanent ordinary-achievement shortcut disqualifier, but it must set the successful-launch flag only after the transaction is valid and must clean bootstrap flags, temporary arrays, tag reservations, target scopes, and scenario bypass state on every completion path.

## Decision category lifecycle notes

The existing `chaosx_disease_containment_category` is the correct owner for generic and Black Plague response decisions.

No dedicated scenario category is required.

The eventual transaction must initialize disease and response registries before exposing the existing targeted actions, then batch-refresh their visibility after state registration and mapmode rebuild.

No scenario-owned mission is currently available, so no mission lifecycle is implemented by this adapter.

## Cost and requirement clarity notes

Existing Black Plague responses already use a mix of state-targeted requirements, political power, equipment, and local state conditions rather than a flat scenario cost.

SCN-012 itself has no cost because it is a global sandbox launch controlled by the shared confirmation UI.

Its only current requirement is the fail-closed package and transaction readiness bridge, so it cannot expose a misleading launch button.

## AI validity and route-lock notes

No SCN-012-specific AI route is active while the scenario is disabled.

The required future package must provide valid human and rat AI behavior, country-target checks, alive and capital checks, safe territory selection, and a Rat King grace period that blocks immediate all-brood absorption.

The future launch gate must test at least two eligible inhabited continents, enough seed states for the Low package, one free Rat Nation tag, one free Rat King tag, and a valid royal-capital transfer before setting any permanent scenario state.

## Localisation and tooltip gaps

The adapter covers the row ID, name, description, fixed type, intensity impact, confirmation status, and shared confirmation wording through the existing dynamic UI.

It does not have dynamic post-launch actual-result text because no launch transaction or result arrays exist.

The eventual report must state the actual scaled continent, state, brood, king, army, and Chaos results when an altered map cannot meet optional targets.

## Cleanup and exploit-risk notes

The adapter writes no launch, disease, Chaos, evolution, country, map, or world-end state.

The future transaction must make `black_plague_triggerable_scenario_launched` idempotent only after it can fully commit, set and clear `black_plague_triggerable_scenario_bootstrap` around the bounded setup pass, prevent duplicate evolution and event-history rows, and release every temporary tag or target reservation.

It must never set Evolution V or `world_end` during SCN-012 launch.

## GUI evidence

`hoi4.gui_inspect` inspected `chaosx_scenarios_window` for `SCN-012` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

`hoi4.gui_render` produced locked, maximum-value, and long-text artifacts at 1920 by 1080 and 1280 by 720, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87c442b021239fcf29faa740041329e7a3b4bc3dad98373f3b51beaaa097e981/3374492553bd9ae790d3c5d49b2d141d8a32751752f6bcae8a0197f7c1c0c04e/chaosx_scenarios_window-full.png`.

The render did not report a visible overlap on this window, but its source graph had 1,832 unrelated global diagnostics, so it is layout evidence only and does not validate gameplay or the repository's other scripted GUIs.

## Validation run

The shared registry was checked for all four sort views and the `SCN-012` numeric slot between existing IDs 11 and 13.

The dynamic localisation branches were checked against each new English key.

The SCN-012 gate was checked to confirm that no readiness flag currently has a writer, leaving confirmation disabled.

The GUI inspect and render evidence above confirms that the existing shared surface can display the new entry without a GUI source patch.

## Skipped meaningful validation

No launch, intensity, seeding, country creation, evolution, mapmode, decision, AI, or cleanup scenario was run because no safe launch provider or Rat Nation and Rat King package exists.

No Event 20 spreadsheet update was made because the scenario is incomplete and the workbook must not claim a playable system before the actual transaction is implemented.

No Git commit was created because this is an intentionally incomplete adapter in a heavily shared dirty worktree.

## Required next implementation tranche

Implement a single atomic `black_plague_scenario_commit_launch` effect and SCN-012 dispatch branch after the Rat Nation and Rat King packages are present.

The transaction must consume the current shared intensity selector, initialize or reconcile Event 20 state, force and record Evolutions I through IV once, seed eligible continents, preserve or create missing actors, create a separate Royal Basin, activate grace and AI, apply the capped Chaos floor, start valid pulses, rebuild the board and mapmode once, present the report, clear all temporary state, and then write the successful-launch flag.

Only that same completed tranche may write `black_plague_scenario_commit_provider_ready`.
# Supersession note

The fail-closed and unimplemented statements in this historical handoff are superseded by `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`. The live `SCN-012` adapter and atomic Event 20 transaction are implemented.
