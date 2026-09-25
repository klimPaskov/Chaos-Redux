# Event 016 Mengele Singularity native incident integration

Disposition: implemented as a source tranche under the accepted `016_final_mengele_portfolio_closure_plan_2026-09-02.md`; Event 016 completion remains unresolved.

## Source integration

The six existing Singularity component projects keep their IDs, icons, weights, costs, cautious options, and Kruger risky paths.
Each risky option now selects a strict Mengele provider branch before the Kruger branch, binds the private Prototype selector, calls `brilliant_scientist_mengele_dispatch_singularity_incident`, then clears the selector.
The shared native project visibility gate admits the provider only with registry access, private Theory, three currently controlled qualifying facilities, the enabled scenario, and no active private incident.
The exact component output still goes through `brilliant_scientist_register_singularity_component` into the private deduplicated array.

The private dispatcher derives a conditional incident weight of 10 from the existing Prototype capacity and stage accident factor, and sets the complementary safe weight to 90.
The private incident applies the same command power and stability penalty values as the existing Singularity incident without reading or writing Kruger Exposure, Capacity, incident, stage, or terminal state.
Its paid recovery decision reserves two civilian factories for 60 days and receipts 35 Political Power, 300 Support Equipment, and 500 fuel as direct payments.
Cancellation refunds an exact unsettled receipt once; expiry consumes the receipt and clears the penalty; provider cleanup settles the direct receipt before removing the active decision and transient penalty.
The installed vanilla `remove_decision` documentation confirms that forced removal does not call `remove_effect`, so cleanup calls the refund helper explicitly first.

## Files

- `common/scripted_effects/016_mengele_singularity_incident_effects.txt` and `.md`: private weighted dispatcher, incident, recovery, cleanup, and API documentation.
- `common/scripted_triggers/016_mengele_singularity_incident_triggers.txt`: strict provider, Prototype, admission, affordability, and receipt predicates.
- `common/dynamic_modifiers/016_mengele_singularity_incident_modifiers.txt`: private penalty.
- `common/decisions/016_mengele_singularity_incident_decisions.txt`: paid native recovery timer and AI priority.
- `localisation/english/016_mengele_singularity_incident_l_english.yml`: decision, cost, tooltip, and penalty text.
- `common/special_projects/projects/016_brilliant_scientist_projects.txt`: six provider versus Kruger risky callbacks.
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`: provider component research admission.
- `common/scripted_effects/016_mengele_project_stage_effects.txt`: provider cleanup call.
- `docs/events/016_brilliant_scientist/systems/mengele_singularity_component_incident.md`: player-facing mechanic flow, interactions, icons, and future extension.

## Validation and balance

A source check found six provider risky branches, six preserved Kruger risky branches, six native visibility gates, and localisation for all new recovery decision keys.
The read-only probability baseline used named low, medium, and high exposure scenarios with declared host conditional incident chances of 20%, 70%, and 100%.
The mandatory `hoi4.probability_compare` reused those scenario IDs and returned `PROBABILITY_ANALYZED`, three scenarios, six scenario-candidates, zero unresolved findings, and no reported regressions; the provider formula gives a 10% conditional incident chance in each scenario.
The safe outcome at 90% is dominant under the analyzer threshold; this is an explicit private-risk balance choice derived from the existing stage constants rather than an inference about full-campaign incident frequency.
The adapter did not execute the surrounding Clausewitz effects or prove native project visibility, callback scope, recovery timing, or repeated-incident behavior.
The [baseline](016_mengele_singularity_accident_probability_baseline_2026-09-25.md) and [comparison](016_mengele_singularity_probability_compare_2026-09-25.md) handoffs retain source revisions, scenario hashes, diagnostics, and artifact URIs.
The deterministic core worker's two `hoi4.event_inspect` attempts timed out after 180 seconds without event artifacts; event-route MCP evidence remains a recorded blocker for completion claims.
The local adapter audit passed 3,072 Singularity assertions over all 64 native-component completion combinations, three provider states, and repeated adoption; this is source-only evidence with explicit stubs.
The [incident recovery AI audit](016_mengele_singularity_incident_decision_ai_audit_2026-09-25.md) found the timed decision under `mission_ai_will_do`, but its evaluator returned `INTERNAL_ERROR` and an absent-before comparison returned `PROBABILITY_SURFACE_EMPTY`.
The user owns live-game acceptance; no game process was launched.

## Remaining Event 016 work

Physical command/power site receipts, terminal decision, Fallout lock/retry adapter, shared world-end presentation, CXT fixtures, accepted AI decision-weight evidence, catalog alignment, and final completion audits remain separate open tranches.
The current source tranche introduces no substitute project, no Kruger-state reuse, no asset placeholder, and no 3D geometry change.
