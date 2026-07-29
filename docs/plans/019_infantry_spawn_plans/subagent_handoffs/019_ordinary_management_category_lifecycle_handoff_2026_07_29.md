# Event 019 ordinary management category lifecycle handoff

## Scope

This focused decision and mission patch removes the permanent Evolution III category state from ordinary Event 19 countries while preserving the Muster Board doorway during a live crisis.

## Changed files and identifiers

- `common/scripted_triggers/019_infantry_spawn_triggers.txt`: `infantry_spawn_ordinary_management_crisis_is_active` and `infantry_spawn_ordinary_management_category_is_relevant`; `infantry_spawn_management_is_available` now uses the shared category gate.
- `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt`: `infantry_spawn_muster_board_is_available` now uses the shared category gate.
- `common/decisions/categories/019_infantry_spawn_decision_categories.txt`: `infantry_spawn_formation_management_category` now uses the shared gate and sets `visible_when_empty = no`.
- `common/decisions/019_infantry_spawn_decisions.txt`: `infantry_spawn_open_muster_board` shares the lifecycle gate.
- `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt`: `infantry_spawn_muster_board_refresh_if_open` closes, rather than rebuilds, an invalid Board.
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`: `infantry_spawn_execute_selected_claimant_takeover` closes the Board after a completed takeover.
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`: the former-parent revolt marker and Board close are success-gated at the final exact-transfer or one-state takeover proof.
- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`: a proven direct-scenario dynamic breakaway closes the former parent's ordinary Board and terminal surface.
- `common/scripted_effects/019_infantry_spawn_pulse_effects.txt`: passive pulses refresh the Board gate before and after management so quiet closeout clears a stale Board-open flag.
- `docs/events/019_infantry_spawn/overview.md` and `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md`: lifecycle contract updated to match implementation.

## Before and after behavior

Before this patch, `infantry_spawn_has_evolution_iii` and `visible_when_empty = yes` kept the ordinary Formation Management category visible permanently, including after a player declined future draws or removed every Event 19 formation.

After this patch, the ordinary category and Board require a live unresolved generation, active or unaccounted Event 19 formation, active claimant, pending Evolution III opening, deferred action, running management mission, or request cooldown.

Persistent capability flags such as `infantry_spawn_claimant_system_active`, `infantry_spawn_anomalous_registry_active`, and `infantry_spawn_evolution_two_management_active` no longer qualify the ordinary UI on their own.

`infantry_spawn_claimant_takeover_complete`, the success-gated parent-side `infantry_spawn_achievement_revolt_history`, derivative classification, direct-scenario actor flags, and derivative creation lock exclude the ordinary surface.

The Evolution III Board remains available while the first bounded opening, a live formation, a claimant, or another live management state exists.

## Decision category lifecycle notes

The category is no longer a persistent feature unlock.

It becomes visible for live management work and closes after quiet closeout.

The completed claimant takeover and final-proven derivative revolt paths explicitly close an already open Board, while the country pulse also clears a stale Board flag after passive quiet closeout, so the scripted GUI cannot remain stranded after the category disappears.

## Mission quality notes

Owner: ordinary Event 19 country.

Category: Formation Management.

Region: country-scoped; selected-lot missions remain tied to the exact registered lot.

Requirement: each running audit, standardization, demobilization, training, district, officer search, specialist, prototype, rail, or request-cooldown mission retains category visibility until its existing completion or deferred replay path resolves.

Duration, success, failure, and cleanup remain owned by the existing mission effects and timeout handlers.

Duplicate risk: none added; this patch only folds every existing running mission flag into the category lifecycle gate.

## Cost and requirement clarity notes

No cost was changed.

The shared gate is applied to both the Board entry and the ordinary management availability trigger, so neither a player nor AI can use an otherwise hidden ordinary decision after a terminal takeover or revolt.

## AI validity and route-lock notes

The Board opener remains AI-disabled.

Ordinary decision AI continues to use its existing affordability and action gates, now additionally subject to the same live-category and terminal-outcome gate used by the player.

No target selection, border rule, formable, or focus route changed.

## Localisation and tooltip gaps

No player-facing gameplay string changed because the category and Board names remain correct.

The Event 19 implementation document and the source design specification now state the player-visible lifecycle.

## Cleanup and exploit-risk notes

The patch uses the existing completed-takeover and parent-side completed-revolt flags rather than adding a parallel historical marker.

No loop, timer, constant, resource transaction, or unit generation path was added.

Closing the Board on terminal outcomes prevents stale GUI interaction with an ordinary-country surface after its crisis has ended.

## Meaningful validation

Reviewed the official vanilla `common/decisions/_documentation.md` category and decision visibility semantics, including frame-refresh `visible` behavior.

Reviewed existing vanilla categories that use a flag-based `visible` gate and `visible_when_empty = no` for transient surfaces.

Traced the completed claimant takeover flag and the existing former-parent derivative revolt marker in source.

Ran `hoi4.event_inspect` state-flow analysis for `infantry_spawn_claimant_takeover_complete`; it produced the read-only artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f2466acfd9db1ad9aa0038b6fd432beaa19666dca9410355e7eb9c291fea0ae/9d8bf92cc9d7f3adfbc1909399b512ed04b5e9925832adeb3b863becc2715d56/event-state_flow-f5ca082883c7.json`.

## Skipped meaningful validation

No in-game validation was run because live session validation belongs to the user under repository rules.

No GUI layout render was needed because the `.gui` source and click regions are unchanged; only existing scripted visibility and close effects were adjusted.

## Remaining issues

The generic country pulse intentionally still treats `infantry_spawn_claimant_system_active` and `infantry_spawn_anomalous_registry_active` as pulse-entitlement signals; that broader entitlement remains separate from the category visibility gate.
