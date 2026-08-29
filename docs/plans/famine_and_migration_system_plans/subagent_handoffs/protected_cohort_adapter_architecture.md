# Protected-cohort custody adapter architecture handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: shared receipt implementation added; owner integration remains incomplete. The protected-cohort internment and forced-labor disqualifiers remain blocked until an owner supplies the exact transaction described below.

## Implementation tranche

The package-owned shared layer now contains `famine_migration_record_cohort_custody_action_exact` in `common/scripted_effects/famine_migration_adapter_effects.txt`, the `famine_migration_custody_action` enum in `common/script_constants/famine_migration_custody_constants.txt`, and strict owner-scoped exact recorders in `common/scripted_effects/famine_migration_achievement_effects.txt`.

The receipt requires one explicit live ID, `internment` or `forced_labor`, a positive whole-row living amount, transaction/actor/site proof, aligned live/history ledgers, one ID match, current host equality, a valid persisted row owner, and a live migration status. It saves the row owner as a regular event target, appends separate idempotent evidence IDs for each action, sets the existing disqualifier flag only from exact proof, and clears one-shot request/proof fields.

No camp, Gulag, genocide, forced-labor, decision, localisation, or on-action owner file was changed. The helper is intentionally inert until an owner action supplies the missing exact cohort intake/retention/labor-assignment receipt.

## Parent disposition

No authoritative existing owner transaction exists in the repository that can prove that a specific famine/migration cohort entered internment or forced labor.

The current camp, genocide, Gulag, and forced-labor paths accept state, action, actor, site-type, quota, pressure, and death values, but no famine cohort ID, current host binding, and accepted living-person amount in one transaction.

The existing famine adapter is a post-owner state-death adapter. It cannot be promoted into a custody proof without creating false positives.

The recommended disposition is to keep the existing generic recorders API-only and add one narrow post-owner receipt operation, `famine_migration_record_cohort_custody_action_exact`, only after an owner action has accepted an explicit live famine cohort and an exact living amount. The parent should not wire the operation to site creation, state pressure, quotas, death bursts, same-state deaths, or a generic country-wide camp flag.

If no owner action can be changed to produce that receipt, the parent should leave the protected internment and protected forced-labor achievements blocked and report the blocker. A state/site/death approximation is not an acceptable fallback.

## Evidence and existing-system boundary

The aligned live cohort registry is the authoritative source for an active famine/migration cohort. Its rows are parallel arrays for ID, origin, host, destination, owner, amount, source, and status. Any row operation must preserve equal lengths and remove every array at the same index.

`famine_migration_transfer_civilians_exact` is an exact state-to-state movement operation. It can debit the origin, credit survivors, record route deaths once, update the cohort host and amount, and append a state visit. It does not mean that the cohort was interned or assigned to labor.

`famine_migration_bind_cohort_destination_forced` records forced movement/deportation into a destination. It is not an internment or labor assignment receipt.

The cohort history ledger proves ordered state visits and transfer cycles. A state visit is not a site intake, custody, retention, or labor assignment proof and must not be reused for this purpose.

`famine_migration_adapt_camp_state` consumes `camp_site_last_month_deaths`, `camp_state_site_type`, and `genocide_responsible_country` after the camp owner records state deaths. It applies famine pressure only; it has no cohort ID, accepted amount, custody state, or durable exact receipt.

`famine_migration_achievement_record_protected_internment` and `famine_migration_achievement_record_protected_forced_labor` are now strict compatibility wrappers around exact owner-scoped recorders. They still have no valid owner call site because generic camp activity cannot identify a protected cohort.

The bounded MCP event inspection for `soviet_gulag.1` returned `status=ok`, `code=EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and deferred large-workspace helper/lifecycle expansion. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46c8766990bab72d521bd5d4d7b871ad21551208c479f9554a696c408cc75564/066cced09310298730ddaa5d5a17dbfa5b3b7408c3addb7c5c04e4954baa4c73/event-lint-2ff7afa1197e.json`.

The broader multi-event state-flow inspection for `soviet_gulag.1` through `.5` exceeded the MCP response window and was terminated. That is recorded as a tooling limitation, not as evidence for a missing or present transaction. Source review is decisive for the owner-receipt gap.

## Exact owner contract

The owner must expose a single post-transaction call point after it has accepted or retained a living cohort in a concrete camp/labor site or an exact labor assignment. The owner call must be in the state scope that owns the site or assignment.

The call must carry all of the following explicit request inputs.

| Input | Required contract |
| --- | --- |
| `famine_migration_cohort_custody_id_request` | Positive ID from the live aligned cohort registry. No state, country, current-host, or actor fallback is allowed. |
| `famine_migration_cohort_custody_action_request` | An explicit action enum with only `internment` or `forced_labor`. The enum must be added to the shared famine/migration constants. |
| `famine_migration_cohort_custody_amount_request` | Positive number of living cohort members accepted by this owner transaction. It is not deaths, pressure, a quota, building level, or a disruption value. |
| `famine_migration_cohort_custody_transaction_proven` | Positive proof token set by the owner only after its exact intake, retention, or labor-assignment operation succeeds. |
| `famine_migration_cohort_custody_actor_proven` | Positive proof token identifying the actor/owner operation that accepted the cohort. A generic country scope is not sufficient. |
| `famine_migration_cohort_custody_site_proven` | Positive proof token for the concrete camp or labor assignment. `camp_state_site_type` alone is not proof. |

The narrow first implementation should require a whole-row custody action: the requested amount must equal the current live row amount. A partial amount must fail closed because the current aligned registry has no split operation. The parent must not mark an entire cohort as interned or forced labor when an owner only accepted an untracked subset.

For cross-state custody, the owner must first complete the existing exact transfer and update the live row host to the destination state. The destination owner then calls the custody receipt in that host state. The helper must reject a call where the live row host is not the current state.

The helper must validate, in this order, before setting achievement evidence:

1. The current scope is a valid state.
2. The live cohort/history ledgers are aligned, using the existing aligned-ledger trigger or a narrower equivalent that includes every array touched by the helper.
3. The explicit requested ID appears exactly once in the global live ID array.
4. The row status is one of the currently live migration statuses (`active`, `destination_bound`, or `destination_bound_unsafe`) and the row amount is positive.
5. The persisted row owner is valid and is the country that owns achievement evidence.
6. The row host equals the current state.
7. The action enum is exactly `internment` or `forced_labor`.
8. All owner proof tokens are positive.
9. The accepted living amount equals the current row amount.
10. The request has not already been recorded for this exact cohort/action pair in the persisted owner evidence arrays.

The helper must fail closed on a missing ID, ambiguous ID, invalid alignment, stale row, wrong host, invalid action, missing owner proof, or amount mismatch. It must never resolve a cohort from state or country context.

## Proposed helper map

### `famine_migration_record_cohort_custody_action_exact`

Scope: current state, called only by an owner immediately after a successful exact living-cohort custody transaction.

Inputs: the six explicit request/proof values in the contract above.

Outputs: temporary result values for `valid`, `invalid_reason`, `resolved_cohort_id`, `resolved_action`, `resolved_amount`, `resolved_row_index`, `already_recorded`, and `achievement_recorded`.

Side effects: resolve the exact live row; save a regular event target named `famine_migration_cohort_custody_owner` from the persisted row owner; invoke the corresponding achievement recorder in that owner scope; clear one-shot request/proof variables after the attempt. The helper must not alter state population, deaths, route deaths, cohort amount, destination, host, migration status, or the camp death adapter.

Call sites: owner-local exact internment or forced-labor acceptance/retention functions only. Existing site activation and death-recording functions are not valid call sites.

### `famine_migration_achievement_record_protected_internment_exact`

Scope: persisted cohort owner country, reached through `famine_migration_cohort_custody_owner`.

Inputs: exact resolved cohort ID, exact resolved amount, and the validated custody action token. The public helper may keep the current generic flag setter as a compatibility wrapper, but the exact path must not accept a country-only call.

Outputs: temporary `valid`, `already_recorded`, and `recorded` values.

Side effects: append the exact ID once to `famine_migration_achievement_protected_internment_cohort_ids`; set the existing disqualifier flag; add the exact protected amount to the achievement ledger only on the first ID/action receipt.

Call sites: only `famine_migration_record_cohort_custody_action_exact` after all row and owner checks succeed.

### `famine_migration_achievement_record_protected_forced_labor_exact`

Scope: persisted cohort owner country, reached through `famine_migration_cohort_custody_owner`.

Inputs, outputs, side effects, and call-site restrictions match the internment helper, using `famine_migration_achievement_protected_forced_labor_cohort_ids` and the forced-labor disqualifier flag.

The two evidence arrays are intentionally separate. A cohort may be recorded once for internment and once for forced labor if both exact transactions occur. Repeating the same action for the same ID is a no-op and must not increment protected people twice.

## Achievement evidence persistence

Initialize the two per-country exact evidence arrays in `famine_migration_achievement_initialize_country`:

* `famine_migration_achievement_protected_internment_cohort_ids`
* `famine_migration_achievement_protected_forced_labor_cohort_ids`

The arrays are campaign-persistent achievement evidence. Do not clear them when a live cohort row is cleaned up, when the cohort is released, when the source state is annexed, or when the live row reaches zero. Live-row cleanup must remove the eight aligned migration arrays and visit history only; it must not erase an already proven achievement disqualifier.

The existing generic flags may remain as fast trigger gates, but they are valid only when set by their corresponding exact recorder. They must not be set by a generic camp callback. If the parent changes the achievement triggers to membership checks, the membership check must be scoped to the current achievement owner and exact evidence array.

No global custody ledger is recommended for the first implementation. The exact ID and amount are validated in the owner transaction and the durable achievement arrays retain only the evidence needed by the achievement triggers. A global custody ledger would introduce another aligned registry, global initialization, duplicate cleanup, and stale-owner handling without adding proof for the achievement.

## Constants and tuning table

Add a small action enum category to `common/script_constants/famine_migration_constants.txt`:

| Constant | Value/meaning |
| --- | --- |
| `famine_migration_custody_action.internment` | Stable token for exact internment evidence. |
| `famine_migration_custody_action.forced_labor` | Stable token for exact forced-labor evidence. |

Do not add death percentages, pressure multipliers, quota tiers, or duration tuning to this adapter. Custody evidence is binary per exact cohort/action receipt; balance belongs to the owner transaction that accepts the living people. Do not use file-local `@` constants across files for the action enum.

If the parent later adds partial-cohort support, the split operation needs its own documented constants and conservation checks. It must not be hidden inside the receipt helper.

## Event target and cleanup lifecycle

Use a regular event target, `famine_migration_cohort_custody_owner`, only for the immediate owner-country callback. It should be saved from the aligned row owner immediately before leaving the state scope and consumed in the same effect chain. A global event target is unnecessary and would create stale cross-chain ownership risk.

The helper must clear the temporary request/proof variables on both success and rejection so a later owner action cannot accidentally reuse an old ID or amount. If the repository’s normal temporary-variable cleanup convention is used, the implementation must still ensure that the request values cannot leak into an unrelated action chain.

The exact evidence ID arrays and disqualifier flags are not cleanup targets. They represent irreversible campaign evidence for the achievement contract. The existing live registry cleanup continues to remove every parallel row array at the same index and visit history through the existing exact cleanup helpers.

No `on_daily`, `on_weekly`, `on_monthly`, country-wide callback, or whole-world scan may be added. The owner transaction is the only producer of this evidence, so its call is sparse and event-driven.

If a terminal owner action removes the live row after custody, the custody receipt must run first. Cleanup itself is never evidence of internment or forced labor.

## No-double-counting rules

The receipt helper must not call `famine_migration_transfer_civilians_exact`, `famine_migration_apply_related_state_deaths_exact`, `camp_rework_record_latest_state_deaths`, or any population/death effect.

The owner’s existing death path remains the sole owner of same-state camp deaths and famine-pressure adaptation. `camp_site_last_month_deaths`, `genocide_last_state_deaths`, `chaos_deaths_change`, forced-labor quotas, building levels, camp population-loss pressure, and relocation disruption are never accepted as custody amounts.

The exact ID/action evidence arrays provide idempotence. Before appending, the recorder must search only the persisted owner’s array for that exact ID and treat a duplicate as `already_recorded` without adding protected people again or firing another achievement side effect.

The live row amount must be read from the aligned registry after ID resolution, not trusted from an arbitrary caller variable. The caller amount is compared to that resolved value and is not used to debit or credit population.

The owner country for achievement evidence must come from the persisted live row owner. The current state owner, action actor, responsible country, and site owner can differ and must not replace the row owner.

## Migration from current duplicated/API-only logic

1. Keep `famine_migration_adapt_camp_state` and its reason-specific wrappers unchanged as the state-death pressure bridge.
2. Add the action enum and exact achievement evidence arrays during achievement initialization.
3. Implement the exact receipt and exact achievement recorders with fail-closed validation and one-shot input cleanup.
4. Add one explicit accepted-cohort receipt to each owner action that truly performs internment or forced-labor intake/retention. The owner must pass the cohort ID and accepted living amount from the same transaction, not reconstruct them afterward.
5. Remove any temptation to call the generic recorders from site activation, quota, death, pressure, or country-flag paths. Those paths remain non-producers of protected-cohort evidence.
6. Leave the existing achievement trigger flags as disqualifiers if the exact recorders set them. If trigger membership is added, make it an exact owner-scoped check and keep the flags as a compatibility/readability layer.
7. Add owner-specific validation for duplicate receipts, wrong owner, stale ID, wrong host, partial amount, and broken alignment before considering the achievement closure complete.

The current eight-array live registry should not gain `interned` or `forced_labor` statuses. Those are custody facts, not migration lifecycle states, and changing the migration status would risk breaking release, integration, return, or resolution logic. If an owner needs a release lifecycle, it should own that state locally and never use release/cleanup as retrospective proof.

## Required owner call-site changes

The following are the complete gameplay surfaces that the parent may need to edit. Files are conditional where the owner action currently lacks the required exact cohort transaction.

### Shared adapter and achievement files

* `common/scripted_effects/famine_migration_adapter_effects.txt` — add the exact custody receipt helper.
* `common/scripted_effects/famine_migration_adapter_effects.md` — document scope, explicit inputs, outputs, rejection cases, side effects, and an owner call example.
* `common/scripted_effects/famine_migration_achievement_effects.txt` — initialize exact evidence arrays and add exact ID/action recorders.
* `common/script_constants/famine_migration_constants.txt` — add the two custody action enum values.
* `common/scripted_triggers/famine_migration_achievement_triggers.txt` — edit only if the trigger implementation changes from the existing exact-recorder flags to explicit evidence-array membership.
* `common/scripted_effects/chaosx_famine_migration_effects.txt` — edit only if the parent adds a shared initialization/cleanup hook for new global arrays. The recommended design adds no new global custody arrays, so this file need not change for the narrow version.
* `common/scripted_triggers/famine_migration_cohort_history_triggers.txt` — edit only if a narrower aligned-ledger predicate is introduced. Reusing the existing aligned-ledger trigger is acceptable if it has no side effects.
* `common/scripted_effects/chaosx_dynamic_effects.md` — update only if the repository’s public helper index requires the new adapter helper to be listed there; the adapter-specific markdown remains mandatory.

### Owner gameplay files

* `common/scripted_effects/camp_repression_rework_effects.txt` — add the receipt at the post-success point of an exact detention/internment or labor-assignment operation, not in site profile refresh or state-death recording.
* `common/scripted_effects/genocide_crisis_effects.txt` — add a receipt only after a Soviet/Gulag owner function has an explicit cohort ID and accepted living amount. The current `genocide_soviet_forced_labor_quotas_in_from_accepted` function is not a valid producer because it only applies a quota, pressure, and state death burst.
* `common/scripted_effects/camp_repression_major_country_effects.txt` — update Soviet industrial-camp or German prisoner-transfer owners only if they are changed to accept an exact living famine cohort. Current prisoner-transfer paths have no such receipt.
* `common/scripted_effects/camp_repression_colonial_country_effects.txt` — update USA detainee labor, French internment, or UK/Italy/Belgium detention/labor owners only if they gain an exact living cohort intake/assignment transaction.
* `common/scripted_effects/camp_repression_action_dispatcher_effects.txt` — update only if the dispatcher must carry the explicit cohort ID, action enum, and accepted amount into an owner function. Do not wire the dispatcher by state/action ID alone.
* `common/decisions/camp_repression_generic_decisions.txt` — conditional, only if a decision becomes an exact cohort-selection producer.
* `common/decisions/camp_repression_major_country_decisions.txt` — conditional, only if a decision becomes an exact cohort-selection producer.
* `common/decisions/camp_repression_colonial_country_decisions.txt` — conditional, only if a decision becomes an exact cohort-selection producer.
* `common/decisions/genocide_crisis_decisions.txt` — conditional, only if `sov_raise_forced_labor_quotas` or another decision is redesigned to submit an explicit cohort ID and accepted amount. Its current state/quota action is not proof.

`events/soviet_gulag.txt` should remain untouched unless an event option is explicitly redesigned to perform a real exact cohort intake/retention transaction. The inspected `soviet_gulag.1` through `.5` event family currently changes thresholds, famine relief, concealment, and administration; it does not prove custody.

Do not edit `common/on_actions/` for this feature. A recurring scan would violate the sparse registry and no-whole-world-iteration rules.

## Partial-cohort blocker

The narrow helper intentionally rejects an accepted amount that is smaller than the live row amount. The current aligned registry has no exact split operation, so accepting a subset and marking the whole row would be a false positive for the protected-cohort achievements.

If the design requires disqualification when any subset is interned or forced into labor, the parent must first add a separate `famine_migration_split_cohort_exact` operation. That operation would require an explicit parent ID and positive accepted amount less than the parent amount, debit the parent row, append a child row with a new monotonic ID and copied origin/owner/source/status, set the child host to the custody state, and preserve all aligned arrays and history rules. The owner would then receipt the child ID as a whole-row custody action. This is a larger design and is not part of the narrow recommended implementation.

## Unsupported fields and risks

The inspected owner code has no exact `camp_intake_population`, `detainee_cohort_id`, `labor_assignment_cohort_id`, or `custody_retention_amount` field. It exposes site flags/buildings, responsible country, action/state IDs, quotas, pressure, and death bursts instead.

There is no engine callback that automatically links a famine cohort to a camp or labor site. The link must therefore be authored by the owner at the exact transaction boundary.

`camp_state_site_type` identifies a state site classification, not a protected cohort. It remains useful for post-owner pressure adaptation only.

The existing generic achievement flags are safe only after exact recorders become their sole writers. Any old or future generic writer would reintroduce a false-positive path.

The regular event target is safe for the immediate owner callback, but it must not be converted into a global target unless a future cross-chain design explicitly adds clear-on-success, clear-on-failure, and stale-target recovery.

If an owner action accepts multiple cohorts in one transaction, it must invoke the receipt once per explicit cohort ID and amount. One state-level call for a batch is not sufficient evidence unless the batch itself carries an exact per-cohort receipt list, which is outside this narrow design.

## Validation requirements for the parent

Before wiring an owner, verify that the owner function has an explicit live cohort ID, accepted living amount, concrete site/assignment proof, and a post-success call point. Reject any path whose only new values are deaths, pressure, quotas, flags, building levels, or state/action IDs.

After implementation, run the relevant scripted-effect and trigger lint checks and inspect every new owner call site. Exercise at least these deterministic cases: valid whole-row internment; valid whole-row forced labor; duplicate same-action receipt; same cohort recorded once for each different action; wrong owner; wrong host state; stale or ambiguous ID; invalid action; missing proof; amount mismatch; broken aligned arrays; live-row cleanup after receipt; and a receipt followed by owner death recording.

Confirm that the receipt produces no population change, no death change, no second famine adapter call, and no migration-row mutation. Confirm that exact evidence survives live-row cleanup and is scoped to the persisted cohort owner.

The probability-inspection workflow is not applicable because this helper is deterministic and has no AI weight, MTTH, random list, or probability-bearing modifier. Focus, GUI, map, and technology MCP routes are not in scope. No in-game launch is part of this handoff.

## Tranche validation

The changed scripted files have balanced brace counts after comment removal, and `git diff --check` reports no whitespace errors. Identifier searches confirm one shared receipt, one custody enum category, and one exact recorder per action. The owner census finds no current owner input for the custody request fields, confirming that no owner call site was silently wired.

The new receipt body contains no population, death, transfer, pressure, or live-cohort-array mutation effect. The available HOI4 MCP route is event-focused and does not lint standalone scripted effects or script constants; no game launch was used as a substitute.

## Final recommendation

Parent should wire the implemented shared exact receipt to an owner gameplay change that supplies the missing cohort ID and accepted living amount. Until at least one owner action satisfies that contract, protected-cohort internment and forced-labor achievement closure is blocked by an exact missing transaction, and generic camp activity, same-state deaths, quotas, or broad scans must remain disqualified as evidence.
