# Event 012 Action Annex and Scramble Settlement Reconciliation

Date: 2026-08-02

Status: implemented in the current Event 012 source; live acceptance remains open.

## Scope

This handoff closes two deterministic lifecycle gaps without creating tags, models, duplicate action stores, or new recurring world scans.

## Implemented changes

- `common/scripted_effects/012_africa_action_effects.txt` now defines `africa_cleanup_annexed_action_target` for the `FROM` victim scope of `on_annex`.
- A current action/host generation uses the normal `africa_cancel_action` owner, including mission removal, host reservation refund, active-count decrement, state unlock, and record cleanup.
- A stale or hostless record performs target-local teardown, unregisters any current relationship state, asks the surviving host to reconcile relationship counts, and clears state-project locks only when both the action and host generations match the victim record.
- `common/on_actions/012_africa_world_order_on_actions.txt` invokes that helper before priority-package teardown so achievement and package owners read their immutable proof before the victim record disappears.
- `common/scripted_triggers/012_africa_world_order_triggers.txt` now tests only coalition members carrying `africa_scramble_intervention_war_actor` when deciding whether an intervention war remains active.
- `common/scripted_effects/012_africa_world_order_effects.txt` defines `africa_scramble_reconcile_intervention_war`, which marks a defensive victory, clears the intervention global, and opens aftermath only after every flagged expedition actor is out of war with the host.
- Capitulation, ordinary peace, and peace-conference settlement hooks clear only the actor that actually settled and call the host reconciliation owner; the previous first-actor global-war clear is removed.
- The expedition loop no longer carries the unused `africa_scramble_expedition_loop_break` variable or break hook, so every eligible frozen planner is evaluated under the cap.

## Validation evidence

Static source assertions confirm one annex cleanup callsite, one action-annex helper, one Scramble reconciliation helper, coalition-member actor filtering, and no remaining `africa_scramble_expedition_loop_break` references. The Event 012 event inspector remains workspace-partial and no live Hearts of Iron IV executable or save was launched.

## Remaining risks

Live acceptance is still required for a target annexed during each duration band, a stale host-generation record, simultaneous expedition actors settling in different orders, and the aftermath mission opening after the final actor leaves the war. The six external continent packages, W5 certification, final super-event package, and all previously documented asset/model gates remain unchanged.
