# Manual Fallout population reconciliation handoff

## Outcome

The dormant manual scenario now has a generation-authenticated per-state
prestrike baseline and first-week after-population/loss receipt. During a manual
Fallout request, the later population rewrite calculates only the additional
loss required to reach the unchanged 90-95% grade target from the original
baseline, using the frozen post-first-week snapshot for deterministic replay.
One all-state preflight replays both unit conversion and first-week arithmetic
before any population mutation. Missing, stale, corrupt, or overshot provenance
fails closed with terminal
`fallout_transition_error_code.manual_population_contract_unproven`.

## Files changed

- `common/script_constants/fallout_manual_scenario_constants.txt`
  - advanced `fallout_manual_schema.version` from 2 to 4 for the new per-state
    receipt fields.
- `common/scripted_effects/fallout_manual_scenario_effects.txt`
  - reset and capture of `fallout_manual_prestrike_population_k` and generation;
  - first-week after-population, observed-loss, and reconciled-total provenance recorder;
  - manual additional-loss intent helper and sole all-state replay preflight.
- `common/scripted_triggers/fallout_manual_scenario_triggers.txt`
  - manual-source, O(1) baseline-ledger, full-provenance, and preflight receipt triggers.
- `common/script_constants/fallout_world_end_constants.txt`
  - terminal `manual_population_contract_unproven` error identity.
- `common/scripted_triggers/fallout_world_end_triggers.txt`
  - finalized population rows bind to the current manual preflight request.
- `common/scripted_effects/fallout_world_end_effects.txt`
  - two narrow intent call-site branches and the terminal pre-iteration gate;
  - existing strategic-singularity hunks were preserved.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MANUAL_POPULATION_RECONCILIATION_PROOF.md`
  - source-of-truth formula, helper map, Deaths contract, and validation proof.

## Helper and call-site identifiers

- `fallout_manual_capture_population_baselines`
- `fallout_manual_record_state_population_loss_provenance`
- `fallout_manual_calculate_population_loss_intent`
- `fallout_manual_population_reconciliation_is_required`
- `fallout_manual_prestrike_population_baseline_is_current`
- `fallout_manual_prestrike_population_baselines_are_current`
- `fallout_manual_population_baseline_is_current`
- `fallout_manual_population_baselines_are_current`
- `fallout_manual_preflight_population_contract`
- `fallout_manual_population_contract_preflight_row_is_current`
- `fallout_manual_population_contract_preflight_is_current`
- `fallout_apply_state_population_loss`
- `fallout_reconcile_population_loss_receipt`
- `fallout_apply_transition_phase_population_loss`

## Validation

- Read the required offline wiki pages and installed vanilla documentation for
  variables, scopes, effects, triggers, script constants, state population, and
  rounding before editing.
- Inspected the existing Deaths and exact state-population helpers to keep the
  first-week aggregate row and later observed-delta receipt paths unchanged.
- Ran static formula cases for empty, one-person, two-person, exact-90%, and
  exact-95% populations. No Hearts of Iron IV run was performed, per the
  dormant/manual release boundary.

## Risks and limitations

- The manual scenario remains unregistered and inactive; native sweep runtime
  acceptance is still a parent-owned blocker.
- The generation token follows the existing manual runtime token (`global.date`)
  and is cleared/rebuilt with every sweep reset.
- A state already below the computed target receives no compensating population.
  The terminal preflight rejects the transaction before any population row mutates.
- The pretransition population snapshot is used for both intent passes so replay
  after the one mutation cannot recompute a different request from live state.
- Baseline capture and the population-contract preflight each traverse all states
  once. Scheduled callbacks and the active validator use the counted O(1) baseline
  receipt, but runtime cost remains unproven.
- Existing strategic-singularity edits in world-end effects/triggers/constants
  were not reviewed or changed as part of this handoff.
