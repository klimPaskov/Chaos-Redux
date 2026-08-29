# Event 35 reusable crisis API contract

## Purpose

Event 35 needs one public country-scope entry point that starts a new Great Depression 2.0 crisis or deepens an existing crisis. This prevents Event 34, contagion, Evolution III, and future approved callers from copying Event 35 internals.

Working effect name:

`great_depression_start_or_deepen`

The final implementation may adjust the identifier to fit established file naming. The public contract must remain stable and documented in `chaosx_dynamic_effects.md` or the current reusable-effects registry.

## Scope

Country.

The current country is the exact crisis target.

## Authorized caller classes

Working caller enum:

- `independent_event_35`
- `industrial_boom_collapse`
- `financial_contagion_conversion`
- `worldwide_depression_conversion`
- `post_recovery_relapse`
- `debug_or_test`

Unknown caller types reject the request.

## Required public inputs

### Identity

- `great_depression_call_caller_type`
- `great_depression_call_source_event_id`
- `great_depression_call_source_episode_id`
- `great_depression_call_receipt_id`
- `great_depression_call_contract_supplied = 1`

### Pacing and logging

- `great_depression_call_pacing_mode`
- `great_depression_call_history_mode`
- `great_depression_call_report_policy`
- `great_depression_call_news_policy`

Working pacing modes:

- `normal_event`
- `consequence_no_pacing`
- `conversion_no_pacing`
- `debug_no_pacing`

### Evolution

- `great_depression_call_evolution_floor`
- `great_depression_call_evolution_proof`

The floor supports baseline, I, II, or III. Lower evolutions are activated automatically when a higher floor is valid.

### Severity

One of these must be supplied:

- `great_depression_call_starting_severity`
- `great_depression_call_deepen_amount`
- `great_depression_call_severity_profile`

The caller also supplies proof flags identifying which input mode is intended. Conflicting modes reject.

### Opening shock

- `great_depression_call_opening_shock_profile`

Working profiles:

- independent severe shock
- Event 34 baseline collapse
- Event 34 speculative collapse
- Event 34 miracle collapse
- Event 34 runaway collapse
- contagion conversion
- worldwide conversion
- active-crisis deepening

## Optional target and source context

- Source country target and proof.
- Source state target and proof.
- Secondary source country and proof.
- Event 34 snapshot supplied proof.
- Contagion link supplied proof.
- Worldwide episode supplied proof.
- Cluster call supplied proof.

Regular event targets are preferred for one effect chain. Persistent source relationships belong in Event 35-owned arrays or country variables after the transaction commits.

## Event 34 snapshot inputs

When the caller is `industrial_boom_collapse`, the call requires the frozen Event 34 snapshot contract.

Required:

- Event 34 episode identity.
- Collapse receipt.
- Final Overheating.
- Peak Overheating.
- Evolution floor.
- Target-country proof.
- One-shot snapshot proof.

Optional validated inputs:

- Dangerous-band duration.
- Recent shocks.
- Hot-running history.
- Cooling or landing state.
- Reserve state.
- Landing failure reason.
- Speculative exposure.
- Primary region count.
- Region registration callbacks.
- Secondary corridor count.
- Repeat crash history.

The main call should allocate the Event 35 episode before region registration begins. Event 34 then registers each proven state through a narrow companion call or aligned array contract.

## Event 34 region registration

Working companion effect:

`great_depression_register_inherited_region`

Scope:

- Country, with a supplied state target.

Required inputs:

- Event 35 episode ID.
- Event 34 episode ID.
- State ID or state target.
- Region role.
- Project profile.
- Project stage.
- Protection state.
- Fragility state.
- Control and damage state.
- Region receipt.
- Contract proof.

Outputs:

- Accepted or rejected.
- Reject reason.
- Center created, hidden liability created, merged, or ignored.
- Registered center index when visible.

The effect is idempotent by Event 34 episode and region receipt.

## Contagion conversion inputs

When caller type is `financial_contagion_conversion`, require:

- Source country.
- Contagion link receipt.
- Exposure stage.
- Exposure duration or proof.
- Conversion gate proof.
- Source Event 35 episode.

The start API records the source and converts once. Multiple sources remain in the exposure ledger but cannot create duplicate national crises.

## Worldwide conversion inputs

When caller type is `worldwide_depression_conversion`, require:

- Active worldwide episode ID.
- Origin country when valid.
- Vulnerability profile.
- Worldwide pressure stage.
- Conversion receipt.

The call starts a national crisis while preserving the existing global pressure row. National and global penalties must not duplicate the same modifier family.


## Relapse inputs

When caller type is `post_recovery_relapse`, require:

- A completed prior Event 35 episode on the current country.
- The prior episode's relapse window or scar proof.
- A new one-shot relapse receipt.
- A relapse profile derived from the prior recovery doctrine, remaining scars, current shocks, and current external exposure.
- Proof that no active Event 35 crisis already exists.

A relapse starts a new Event 35 episode with inherited scars and safeguards. It does not reopen the old episode, replay old Chaos receipts, or recreate previously recovered Depression Centers without current state proof.

## Public outputs

- `great_depression_call_result`
- `great_depression_call_reject_reason`
- `great_depression_call_episode_id`
- `great_depression_call_started`
- `great_depression_call_deepened`
- `great_depression_call_no_op`
- `great_depression_call_active_evolution`
- `great_depression_call_final_severity`
- `great_depression_call_opening_shock_applied`
- `great_depression_call_report_queued`
- `great_depression_call_history_recorded`
- `great_depression_call_pacing_counted`

Every output resets before validation.

## Result enum

Working values:

- accepted new crisis
- accepted deepening
- accepted merge without Severity change
- rejected invalid country
- rejected invalid caller
- rejected missing contract
- rejected duplicate receipt
- rejected conflicting severity inputs
- rejected invalid evolution floor
- rejected missing source context
- rejected incompatible active state
- rejected invalid snapshot

Stable reject reasons help tests and external callers.

## Validation order

1. Reset outputs.
2. Validate one-shot contract proof.
3. Validate current country exists.
4. Validate ordinary civilian economy.
5. Validate caller enum.
6. Validate source event and episode.
7. Validate unique receipt.
8. Validate pacing and history modes.
9. Validate evolution floor and proof.
10. Validate one Severity input mode.
11. Validate caller-specific context.
12. Validate target has at least one viable economic state for a new crisis.
13. Determine start, deepen, or safe no-op.
14. Freeze rollback state.
15. Apply transaction.
16. Set outputs.
17. Clear all public inputs.

## New-crisis transaction

A valid new crisis should:

1. Allocate a unique Event 35 episode.
2. Store entry source and receipt.
3. Set the evolution floor.
4. Set starting Severity.
5. Apply the opening shock once.
6. Select or receive Depression Centers.
7. Initialize trend, phase, and doctrine choice.
8. Register active-country evaluation.
9. Queue the correct report or news surface.
10. Record history according to policy.
11. Count pacing only when `normal_event` was supplied.
12. Commit the source receipt.

## Deepening transaction

A valid deepening should:

1. Preserve the existing Event 35 episode.
2. Commit the new source receipt.
3. Raise the evolution floor when needed.
4. Add bounded Severity or raise to a minimum band.
5. Merge source and state context.
6. Apply only a valid stronger shock.
7. Recalculate phase and objectives.
8. Record deepening history.
9. Avoid a second category, idea, Severity variable, or pacing count.

## Fail-closed behavior

The call performs no partial work when required validation fails.

It must not:

- Guess a source country.
- Substitute a random state.
- Infer an evolution level from global Chaos alone.
- Create a crisis on a special or nonhuman country.
- Apply an opening shock without an active episode.
- Count consequence calls as random pacing events.
- Reuse an old receipt.
- Leave public inputs uncleared.

## Idempotence

The source receipt is the transaction identity.

Calling the same receipt again returns a duplicate-receipt no-op. It does not:

- Reapply Severity.
- Reapply the opening shock.
- Recreate centers.
- Add history.
- Count pacing.
- Add Chaos.

## Rollback

Before applying a multi-step inherited or conversion transaction, preserve enough state to reverse:

- Active crisis existence.
- Severity.
- Evolution floor.
- Episode ID.
- Center count.
- Source row count.
- Report and history receipt state.

If a required state registration fails before commit, roll back the uncommitted Event 35 transaction and leave the caller snapshot intact for a bounded retry. After commit, the snapshot is consumed.

## Internal helpers

The public API should delegate to event-owned helpers such as:

- initialize new crisis
- deepen active crisis
- calculate inherited Severity
- apply opening shock
- select independent centers
- merge inherited centers
- raise evolution floor
- refresh national modifiers
- rebuild category state
- register active episode
- record entry history
- reconcile after load
- close and clean episode

These are internal Event 35 helpers and do not belong in the public registry unless another subsystem needs a stable contract.

## Contagion exposure adapter

Working public or cross-system helper:

`great_depression_apply_exposure`

Purpose:

- Add or modify one source-target Financial Contagion link without creating a full crisis immediately.

Required:

- Source country and episode.
- Target country.
- Exposure amount or profile.
- Relationship proof.
- Source receipt.
- Contract proof.

Outputs:

- Accepted or rejected.
- New exposure stage.
- Conversion requested or not.

It must be source-aware, idempotent, sparse, and bounded.

## Event 34 demand adapter

Event 35 should call an Event 34-owned adapter for extraordinary depressed-market demand.

Event 35 supplies:

- Source depression or worldwide episode.
- Supplier country.
- Demand profile.
- Duration.
- Receipt.

Event 34 returns:

- Accepted or rejected.
- Output opportunity applied.
- Overheating pressure applied.

Event 35 never writes Overheating directly.

## Pacing contract

Only an independent Event 35 random-pool firing counts as Event 35 pacing.

The following do not count another global pacing event:

- Event 34 collapse.
- Contagion conversion.
- Worldwide conversion.
- Post-recovery relapse.
- Deepening an active crisis.
- Evolution activation.
- Cluster members after the cluster has already counted its one pacing event.

## History contract

History mode distinguishes:

- Normal independent event row.
- Consequence row linked to Event 34.
- Contagion conversion row linked to a source country.
- Worldwide conversion row linked to a global episode.
- Relapse row linked to the prior completed Event 35 episode.
- Deepening row attached to an existing episode.

Evolution records use the shared evolution pipeline. Baseline phases do not.

## Cleanup contract

After every public call:

- Clear temporary input selectors.
- Clear proof flags.
- Clear temporary source targets where the engine permits it.
- Preserve only committed Event 35-owned source rows.
- Preserve outputs long enough for the immediate caller to read them, then allow the caller to clear or overwrite them.

## Documentation requirement

The implementation change that adds the public effect must document:

- Purpose.
- Scope.
- Inputs.
- Outputs.
- Defaults.
- Reject reasons.
- Side effects.
- Idempotence.
- Pacing behavior.
- Example calls for independent Event 35, Event 34, contagion, and worldwide conversion.

## Acceptance tests

- Valid independent call starts once and counts pacing once.
- Valid Event 34 call starts once and counts no Event 35 pacing.
- Event 34 call into active Event 35 deepens once.
- Duplicate receipt is a no-op.
- Missing target, source, proof, or evolution rejects without partial work.
- Contagion conversion records source and starts once.
- Worldwide conversion preserves the global row and starts once.
- Higher inherited evolution activates lower stages.
- Load reconciliation does not replay a committed call.
- Public inputs clear after success and rejection.
