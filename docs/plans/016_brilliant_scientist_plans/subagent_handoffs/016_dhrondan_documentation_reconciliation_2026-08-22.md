# Event 016 Alien Infantry and D’Rhonda documentation reconciliation

## Scope

This handoff reconciles the Event 016 Alien Infantry and Empire of D’Rhonda specifications, system documentation, asset/model manifests, implementation handoffs, acceptance evidence, and catalog-facing wording after the source and audit tranches.

The context-free documentation-curator route was attempted twice but produced no handoff before stalling. The parent completed this bounded reconciliation directly without changing gameplay or workbook content during the reconciliation pass.

## Current sources of truth

- `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` owns the accepted design.
- `docs/events/016_brilliant_scientist/systems/alien_infantry.md` owns the reusable unit, equipment, landing, and contact API contract.
- `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md` owns the Kruger and Mengele contact lifecycle.
- `docs/events/016_brilliant_scientist/systems/dhrondan_country.md` owns the rebellion, state-transfer, and country lifecycle.
- `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md` owns the exact 88-focus structure and spirit lifecycle.
- `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md` owns the named acceptance scenarios.
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md` and `subagent_handoffs/alien_infantry_3d_model_handoff.md` own the rejected-model and recovery status.
- The final focus, decision/mission, country, localisation, event-completion, and AI-probability handoffs in this directory own bounded acceptance evidence.

## Reconciled facts

- All current documentation uses `alien_infantry`, `alien_laser_weapon_equipment`, and `KRG_arm_the_alien_cohorts`; retired unit-family runtime identifiers are absent from the scoped documentation and live consumers.
- Provider 508 now records exact one-request, deferred transaction, commit, rollback, cleanup, and deletion-identity behavior. The remaining limitation is architectural: the generic Event 019 registry does not yet publish reusable materialize/commit/rollback hooks for future providers.
- The reusable 2D Alien Infantry package, original counters, equipment and technology icons, tactics, decisions, event art, DHR flags, portraits, focus icons, achievement art, and country-interface assets are installed and registered.
- The rifle-bearing 3D package remains rejected and unwired. No fallback entity, animation, or sound binding is represented as complete.
- Event 016 remains a minor fire-once incident with exactly four logged evolutions, no cluster, no fifth D’Rhondan evolution, and no separate DHR super-event.
- The final probability audit proves the declared 10%, 20%, and 40% rebellion pools. Other dynamic weighted surfaces remain conditional where the installed MCP adapters timed out or could not execute the full helper chain.
- The catalog workbook wording and exported CSVs remain aligned with the implemented Event 016 chain; Evo V and Cluster ID remain blank.

## Files reconciled

- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_provider508_api_handoff_2026-08-21.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_unit_database_handoff_2026-08-21.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_final_event_completion_audit_2026-08-22.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_audit_handoff_2026-08-05.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_consumer_ledger.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/alien_infantry_3d_model_handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`

Obsolete unreferenced retired-family DDS files and generated intermediates were removed. No broad gameplay, spreadsheet, or unrelated documentation rewrite was performed during this pass.

## Unresolved boundaries

1. The rifle-bearing Meshy 7 recovery, seven genuine actions, Blender PDX export/reimport proof, exact action synchronization, and runtime entity/sound wiring require the requested failure-recovery authorization.
2. The accepted formula caps the initial DHR army at fifteen cohorts while separately requiring at least one cohort in every disconnected enclave. A revolt with more than fifteen disconnected landing components cannot satisfy both rules and needs an explicit precedence decision.
3. A future reusable Event 019 provider with deferred external resources should first receive a generic lifecycle-hook contract instead of copying provider-508 private branches.
4. Event, technology, map-state, and several weighted helper-chain MCP surfaces remain conditional where the installed service timed out, hit artifact storage limits, or lacked a compatible adapter.
5. In-game behavior and visual acceptance remain user-owned and are not claimed by this documentation reconciliation.
