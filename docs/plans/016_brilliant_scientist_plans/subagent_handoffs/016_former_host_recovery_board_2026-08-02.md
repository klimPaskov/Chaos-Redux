# Event 016 former-host recovery board

Date: 2026-08-02

Status: implemented as a bounded gameplay continuation owned by the parent agent.

## Contract

The former host is eligible only after `brilliant_scientist_former_host` and `brilliant_scientist_kruger_departed` are both present, the country is viable, the capital is controlled, and at least one former Event 016 laboratory state remains. The board is unavailable to the current host, the Kruger State, a terminal world-end state, or a country whose recovery board has closed.

The category implements exactly four one-time actions from Phase H of the host specification:

1. `brilliant_scientist_reconstruct_independent_research` requires the surviving research-cohort route, support equipment, manpower, political authority, and civilian factory time. Success raises Independent Capacity, lowers Grievance, and records a research receipt; cancellation records a permanent failure.
2. `brilliant_scientist_secure_abandoned_archive` is a state-target operation. The selected former laboratory state must remain owned, controlled, supplied through a supply node, and carry an Event 016 facility receipt for the full hold window. Success marks the state and country archive receipts, raises Independent Capacity, lowers Exposure, and records recovery; loss of control records archive destruction pressure and a permanent failure.
3. `brilliant_scientist_offer_amnesty_to_assistants` requires a surviving assistant route, support equipment, manpower, political authority, and civilian factory time. Success raises Independent Capacity, lowers Grievance, and records infiltration risk plus recovery; cancellation records a permanent failure.
4. `brilliant_scientist_request_international_inspection` requires foreign access through an observer, protection, joint-laboratory, or faction channel, plus support equipment, trucks, political authority, and civilian factory time. Success lowers Exposure, records a treaty receipt, and adds recovery; cancellation records a permanent failure.

Three successful receipts are required to set `brilliant_scientist_former_host_recovery_complete`. That flag closes the category and makes the existing lifecycle refresh stop re-adding `brilliant_scientist_scientific_vacuum`. If all four actions reach either success or failure without three successes, the category closes while the vacuum remains. Each receipt is one-time and no action creates units, project stages, Kruger transfers, models, or a new evolution.

## Changed files

- `common/script_constants/016_brilliant_scientist_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_recovery_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_recovery_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/decisions/categories/016_brilliant_scientist_recovery_categories.txt`
- `common/decisions/016_brilliant_scientist_former_host_recovery_decisions.txt`
- `localisation/english/016_brilliant_scientist_recovery_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/idea_lifecycle.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

The recovery category reuses `GFX_decision_category_brilliant_scientist_aftermath_reconstruction`, which is already registered in `interface/016_brilliant_scientist_aftermath_decisions.gfx`; no new art or model dependency was introduced. The KRG route-staff continuation also centralizes mutually exclusive command-idea cleanup before reactivating a selected institutional office, so repeated focus or terminal calls cannot leave stacked command ideas.

## Validation boundary

Static checks still required before commit are brace/reference checks, localisation BOM verification, decision/category/id coverage, and a focused `hoi4.probability_inspect` or decision inspector pass. The recovery decision probability adapter currently reports `PROBABILITY_SURFACE_EMPTY` because it does not discover these target-gated timed decision blocks; this is recorded as an analyzer limitation, not a normalized AI claim. A rerun of focused hidden roster event `chaosx.brilliant_scientist_krg.90` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06ba289ae164a8cddace18a243f605732cb074456cbab63d56324ceacb5916d6/eeb931e92bdee8b826079495c8662ab0582a64cc45ad8617fce9e2b1cb96aad1/event-lint-139c181b58b5.json`, while deferring workspace-wide helper projections. No HOI4 process was launched and no live former-host scenario is claimed. The board's actual supply interruption, archive sabotage, and late recovery timing remain user-owned in-game acceptance work.
