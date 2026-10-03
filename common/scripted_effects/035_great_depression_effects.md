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

The exact regional companion is documented in [035_great_depression_region_effects.md](035_great_depression_region_effects.md).
State cleanup checks the registered state's current episode against the closing receiver before removing physical/project flags.
Invalid sparse-registry actors retire without recovery rewards or pacing.
No recurring whole-world scan is introduced.

Source models and named before/after fixtures are in `docs/plans/035_great_depression_plans/subagent_handoffs/`.
Current domain MCP timeouts prevent native transaction, lifecycle, and probability-comparison certification.
The full Event 35 goal remains incomplete while mapped acceptance or upstream-source dependencies are unresolved.
