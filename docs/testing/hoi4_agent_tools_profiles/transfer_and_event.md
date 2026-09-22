# Civilian transfer and event integration profile

Verify the connected server version, health, live schemas, and client task negotiation before using `hoi4.mechanic_test`, `hoi4.package_check`, `hoi4.scenario_test`, `hoi4.event_inspect`, or `hoi4.event_render`. Run only confirmed read-only routes. `transfer_and_event_suite.json` checks source declarations, one invalid preflight, and the Event 001 chain. An unresolved mechanic result is not a pass.

## Civilian transfer

The state-scope primitive in `common/scripted_effects/civilian_transfer_effects.txt` uses `civilian_transfer_preflight`, `civilian_transfer_civilians_exact`, `civilian_transfer_finalize`, `civilian_transfer_rollback_transaction`, and `civilian_transfer_cleanup_request`. `common/scripted_triggers/civilian_transfer_triggers.txt` defines `civilian_transfer_finalize_request_is_valid`. `common/scripted_effects/migration_core_effects.txt` consumes finalization through `migration_record_transfer_projection` and `migration_update_cohort_host_after_transfer`; `common/decisions/migration_decisions.txt` checks the finalization result at its call sites.

Use explicit origin, destination, actor, route, cohort, reception, and obligation state in each `hoi4.mechanic_test` scenario. The source interpreter only advances declared effects and days; it does not run campaign hooks or the game. Retain applied, skipped, and unresolved trace steps and source revision. The cases to establish are:

| Case | Required assertions |
| --- | --- |
| Valid exact transfer | `civilian_transfer_actual_origin_debit > 0`; debit equals `civilian_transfer_route_deaths + civilian_transfer_survivor_credit`; `civilian_transfer_conservation_ledger = 0`; destination actual credit and reception applied equal survivor credit. |
| All deaths | Survivor credit and destination credit are zero; route deaths equal measured origin debit; conservation ledger is zero. |
| Under-credit | The residual is restored to origin before finalization; the final ledger is zero and the projection uses the measured debit. |
| Invalid proof | Invalid route, host, actor, border, transport, safety, cohort, or reception proof leaves population, cohort, reception, and projection state unchanged. |
| Cohort alignment | Cohort id, amount, status, and host arrays retain equal lengths; the surviving row moves to the exact destination. |

The suite includes an invalid preflight with a missing cohort id and asserts that origin population does not change. Valid transfer, all-death, under-credit, and cohort-alignment cases require a finite scenario with the exact route and state scope bindings from the owning system; do not mark them passed from source text or substitute invented state. Keep these cases unresolved until the complete named inputs and tool traces are retained.

## Event integration

`events/001_communism_spread.txt` defines the `chaosx.nr1.1` entry event and its options. `common/on_actions/001_communism_spread_on_actions.txt`, `common/decisions/001_communism_spread_decisions.txt`, `common/scripted_effects/001_communism_spread_effects.txt`, `common/scripted_triggers/001_communism_spread_triggers.txt`, `common/dynamic_modifiers/001_communism_spread_dynamic_modifiers.txt`, and `common/ideas/001_communist_insurgency_ideas.txt` are related sources. Use `hoi4.event_inspect` with the exact event selector and a bounded trace, then `hoi4.event_render` for options and nearby flow. Check registration, both root options, downstream event links, state access, terminal paths, localisation and icon references, and unresolved findings. Compare matching source revisions if any of those files change.

Event 031 insurgency is a separate decision and state surface in `common/scripted_effects/031_random_terror_effects.txt` and `common/decisions/categories/031_random_terror_categories.txt`. Inspect `random_terror_state_stage` and `random_terror_state_armed_insurgency` as state facts; no dedicated Event 031 GUI source was found. The Event 001 dashboard and state mapicon are covered by the scripted GUI profile.

The user owns live-game validation. Source and MCP results establish only their declared coverage and remain separate from in-game behavior.
