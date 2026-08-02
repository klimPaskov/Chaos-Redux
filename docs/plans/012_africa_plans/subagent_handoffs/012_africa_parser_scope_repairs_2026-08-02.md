# Event 012 Africa parser and scope repair handoff

Date: 2026-08-02.

## Scope

This tranche freezes the Event 012 source repairs that were present in the shared worktree after the decision, GUI, and world-order audits. The changes are syntax/scope corrections only; they do not add country tags, characters, models, new action concepts, or substitute world-order packages.

## Changed surfaces

- `common/scripted_effects/012_africa_achievement_effects.txt`: moved filters and nested checks inside `if` blocks within `for_each_scope_loop`, preserving achievement counters and array refresh semantics.
- `common/scripted_effects/012_africa_ai_profile_effects.txt`: moved the state-candidate filter into a supported nested `if` block.
- `common/scripted_effects/012_africa_diaspora_effects.txt`: promoted the request host/target pointers to global event targets because the consent event resumes after the originating chain; matching cleanup now clears global targets.
- `common/scripted_effects/012_africa_effects.txt`: moved the continental peace-exemption filter into a supported nested `if` block so only owned, controlled African states are recorded.
- `common/scripted_effects/012_africa_focus_route_effects.txt`: moved action-target filters into nested `if` blocks while retaining the route-specific target flags.
- `common/scripted_effects/012_africa_world_order_effects.txt`: corrected the host-ideology comparison scope and guarded constituent breakup cleanup inside the array loop.
- `common/scripted_effects/012_africa_world_union_war_effects.txt`: guarded array-loop effects, preserved ballot/call dispatch, and made successor pointers global for the multi-event terminal protocol with matching cleanup.
- `common/scripted_guis/012_africa_charter_scripted_gui.txt`: addressed array-selected state scope through explicit `var:` references in click handlers.
- `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt`: addressed selected-country array scope through explicit `var:` references in relationship, protection, clause, and departure text.
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt`: used the supported `has_army_size = { size > ... }` form for Scramble expedition material readiness.

## Validation

The focused Event 012 event inspection returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics for the entry state-flow query after these repairs. The default-scenario GUI inspection returned `GUI_INSPECTED` for `africa_charter_window`; its workspace-global layout/context diagnostics remain separately documented in `012_africa_gui_inspect_default_2026-08-02.md`. The focused diff has no whitespace errors. No live game was launched.

## Remaining risks

These repairs do not close the acceptance ledger. The focus renderer still reports branch-template overlaps for mutually exclusive regional overlays, and the Event 012 completion audit still blocks W5 certification, external continent packages, terminal audio/presentation, model-gated packages, priority-carrier acceptance, achievement proof, AI scenario proof, and live GUI click/resolution acceptance. Those gaps remain intentionally visible rather than being masked by parser changes.
