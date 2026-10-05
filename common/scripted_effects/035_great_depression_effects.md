# Event 35 synchronous crisis gateway

## Owner and scope

`great_depression_start_or_deepen = yes` is the only national crisis gateway.
Its current country is the exact receiving country, independently of the sender's ROOT.
The implementation and caller enums are in `035_great_depression_effects.txt`, `../scripted_triggers/035_great_depression_triggers.txt`, and `../script_constants/035_great_depression_constants.txt`.
The accepted field contract is [the reusable crisis API spec](../../docs/specs/035_great_depression_specs/035_great_depression_reusable_crisis_api.md).

## Inputs, defaults, and outputs

Inputs are normal `great_depression_call_*` variables on the receiver, plus explicitly proven regular source targets.
Supply contract version, caller class, source event and episode, unique receipt, pacing/history/report/news policies, evolution floor and proof, one Severity mode and its proof, and a compatible opening-shock profile.
Optional source-country and worldwide-origin targets require their matching proof.
Inherited, contagion, worldwide, and relapse calls also supply their documented owner-specific evidence.
The public gateway does not guess missing required inputs or replace missing country/state scopes.

Every public output resets first.
The immediate receiver can read result, rejection reason, episode, started/deepened/no-op, active evolution, final Severity, opening-shock application, report/history, and pacing status after the synchronous return.
All public inputs and private captured scope fields clear on accepted and rejected returns.
Committed source context, receipts, output variables, and regional history remain.
Regular target names cannot be manually cleared, so proof fields and captured normal pointers define their permitted lifetime.

## Validation and transaction

New crises require a valid ordinary economy and at least one permitted owned, controlled, passable core industrial state.
Unknown callers, malformed profiles, missing source context, duplicate receipts, incompatible states, and absent owner evidence reject or no-op according to the existing result enums.
Event 34 evidence must match its exact frozen country, episode, receipt, evolution, Overheating and ancillary fields.
Contagion requires the exact aligned source-target rows, source episode, unresolved stage and elapsed exposure.
Worldwide calls require the current global episode, pressure row, receipt and proven origin.
Relapse requires a completed prior episode, scar/watch proof, its actual recovery window, and no active crisis.

Capture source and origin pointers on the receiving country before any nested conversion can overwrite regular target names.
New setup stages the requested local floor and registration state before projecting networks, installing evolution ideas, or logging evolution.
Required regional preflight runs before setup, and regional commit precedes the national source/history receipt.
Deepening preserves the current episode, adds bounded Severity, merges validated context, and never creates another national package.
Exact duplicate national receipts do not replay Severity, centers, history, Chaos, or pacing.
Only independent calls own normal pacing.

## Call examples

An independent receiver uses the owner wrapper, which builds the full input contract:

```txt
great_depression_prepare_independent_call = yes
great_depression_start_or_deepen = yes
```

An Event 34 landing freezes its owner fields and removes boom-only bonuses in `chaosx.nr34.3`, then calls `industrial_boom_deliver_collapse_snapshot = yes`.
That wrapper prepares the complete main/regional contracts and retains one receipt and snapshot across bounded retries.
Do not consume the snapshot outside its accepted national-and-regional result branch.

A proved contagion source calls `great_depression_apply_exposure = yes` with its exact target and relationship/stage fields.
Its conversion branch freezes source country, episode, pair receipt, outer indexes and depth on the recipient before calling this gateway.
After return it restores those indexes and revalidates source-row identity before attribution.

The worldwide lifecycle calls `great_depression_run_worldwide_conversion = yes` after its interval and stage gates.
That wrapper selects from the bounded pressure registry, supplies its episode/origin/receipt contract, and updates the original row only after acceptance.
These wrappers do not own additional normal pacing.

## Caller-owned temporary outputs

Internal callers initialize temporary result storage before each returning helper.
The independent target selector owns `great_depression_independent_target_weight`, initially zero.
The center selector owns `great_depression_center_candidate_score`, initially the configured invalid-score sentinel.
New-crisis setup owns `great_depression_center_registration_failed`, initially one so a missing result rejects setup.
Deepening owns `great_depression_deepening_value`, initially zero.
Their callees overwrite these values through the existing formulas and gates.
Private intermediate values remain helper-local.

The Event 35 humanitarian adapter similarly initializes famine and migration request acknowledgements and occupation proof to zero before the owner call.
It marks its one-shot source receipt only after the returned owner acknowledgement succeeds.
No owner definitions or request amounts are duplicated.

## Companion, cleanup, and evidence limits

### Center project identity

A state has one current paid project authorization and keeps its last spent completion/failure IDs separately from historical completion flags.
`great_depression_authorize_center_project` increments the state serial only for a current registered target with an open country project slot and a valid pending project.
It binds the new authorization to the current episode and resets work timing, not prior completed rewards.
Completion requires current ownership/control, matching registration and authorization episode, unspent authorization, and the configured work duration.
Failure spends the same authorization once.
An idle center may receive a distinct mapped follow-on or reopening project after a new collapse.

`great_depression_write_center_project_ledger` runs in STATE scope with the acting country as ROOT.
It reads the state's current registry index, project type, stage, start, stage, due, and pause dates and updates the corresponding existing aligned country columns.
It returns no temporary output, creates no registry, and grants no reward.
For example, the project-stage helper calls it after changing `great_depression_center_project_stage`.
State authorization and spent IDs survive transfer; accepted adoption binds continuing work to the receiving episode without replaying prior completion.

Reopening counts once per state and episode.
Lasting Capacity and reconstruction construction use distinct one-shot receipts that treatment changes cannot clear.
Physical transitions retain the center episode, while matching registered terminal cleanup clears the live episode and project fields.
The immutable authorization serial and last spent IDs remain compact state history.
The inherited-liability consumer is implemented in `035_great_depression_inherited_liability_effects.txt` and is documented in its companion Markdown file.
Secured-value salvage and exact corridor outcomes remain blocked on missing Event 034 producer facts, as recorded in D4 of `docs/plans/035_great_depression_plans/agent_decisions_2026-10-04.md`.

The exact regional companion is documented in [035_great_depression_region_effects.md](035_great_depression_region_effects.md).
State cleanup checks the registered state's current episode against the closing receiver before removing physical/project flags.
Invalid sparse-registry actors retire without recovery rewards or pacing.
No recurring whole-world scan is introduced.

Source models and named before/after fixtures are in `docs/plans/035_great_depression_plans/subagent_handoffs/`.
Current domain MCP timeouts prevent native transaction, lifecycle, and probability-comparison certification.
The full Event 35 goal remains incomplete while mapped acceptance or upstream-source dependencies are unresolved.

## Report-chain helpers

`great_depression_initialize_report_chain` runs in COUNTRY scope after a new national episode is allocated.
It reads the caller type and frozen source-country pointer and writes the regular `great_depression_report_chain_episode` value.
Financial descendants inherit that value, worldwide conversions use the unique global episode value, and other national starts use their own episode value.
It creates no temporary output, changes no Severity, and initializes the per-country spread announcement guard.

`great_depression_queue_exposed_partner_report` runs in the source country with `great_depression_exposure_target` bound to the receiver.
It stores a targeted numeric episode value on the receiver to prevent repeats from the same spreading chain, then appends a bounded pending origin and relationship.
`great_depression_open_exposed_partner_report` freezes the first origin, relationship and number of other origins in regular receiver variables, then consumes the pending batch immediately.
The close helper clears only the pending arrays and flag, leaving the report's display values and episode-targeted history intact.
These helpers have no public temporary outputs.

`great_depression_reset_clearing_bloc_announcement_if_small` may run in any scope.
It reads the global clearing member count and formation threshold and clears the global formation-announced flag only when the group falls below formation size.
Membership exits and expiry pruning call it, while global retirement preserves surviving clearing agreements and their announcement guard.
It grants no economic benefit and returns no temporary output.

`great_depression_prepare_action_tooltip_values` runs in COUNTRY scope and publishes 37 regular, display-only `great_depression_tt_*` fields on that country.
All values come from the existing constants, including the compound freight relief calculation, and no gameplay calculation consumes the cache.
`great_depression_refresh_costs` initializes the cache before the first hover, and decision callbacks refresh it before emitting their tooltips.
The constant-display localisation reads the acting ROOT country, while unrelated callback-local temporary values remain unscoped.
The helper has no public temporary output and must not be called on a state.
