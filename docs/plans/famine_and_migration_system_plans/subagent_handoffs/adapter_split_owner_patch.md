# Famine and migration adapter-definition split handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25.

Owner scope: public adapter-definition split only. This pass edits the adapter-definition files and the required adapter handoff; it does not edit core definitions, callers, external hazard owners, decisions, helper subsystems, UI, localisation, assets, achievements, specs, or the event workbook.

Verdict: the former combined adapter surface is physically split into famine-owned, migration-owned, and narrowly neutral humanitarian files. No compatibility alias was added. Existing transitional callers remain blocked until the parent rewires them to the new names and supplies the exact proof fields described below.

## Files changed

### Added

- `common/scripted_effects/famine_adapter_effects.txt`
- `common/scripted_effects/famine_adapter_effects.md`
- `common/scripted_effects/migration_adapter_effects.txt`
- `common/scripted_effects/migration_adapter_effects.md`
- `common/script_constants/famine_adapter_constants.txt`
- `common/script_constants/migration_adapter_constants.txt`
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/adapter_split_owner_patch.md`

### Removed

- `common/scripted_effects/famine_migration_adapter_effects.txt`
- `common/scripted_effects/famine_migration_adapter_effects.md`
- `common/script_constants/famine_migration_adapter_constants.txt`

The removed paths are not compatibility shims. The new public definitions contain no combined `famine_migration_*` identifier.

## Helper map

### Famine-owned helpers

| New helper | Scope | Inputs | Outputs | Side effects | Intended call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_validate_state_local_food_receipt_exact` | State | Valid state; positive amount; state, food, environment, transport, policy, actor, cause, source, generation, revision, and request proofs; valid `famine_adapter_actor` target. | Temporary `famine_adapter_contract_valid`. | Validation only; no state discovery, population, Deaths, movement, or food write. | All famine aftermath adapters. |
| `famine_adapt_air_winter_state` | State | Positive owner-applied Air Winter loss plus the validator contract. | Temporary `famine_adapter_result`. | Calls one food-only Fallout or Air Cleanliness request. Never sets flight. | `fallout_consolidated_effects.txt:air_winter_apply_state_population_loss`; parent must rewire the current transitional caller. |
| `famine_adapt_camp_state` | State | Positive `camp_site_last_month_deaths`, site type, responsible owner, plus the validator contract. | Temporary `famine_adapter_result`. | Calls one famine camp, Gulag, or forced-labor pressure request. Never repeats Deaths. | `camp_repression_rework_effects.txt:camp_rework_record_latest_state_deaths`; parent must supply missing proof. |
| `famine_adapt_chemical_state` | State | Positive accepted chemical loss plus the validator contract. | Temporary `famine_adapter_result`. | Calls chemical-aftershock food pressure only. | `cbrn_occupation_effects.txt:cbrn_occupation_apply_accepted_operation_state`; parent must supply missing proof. |
| `famine_adapt_black_plague_state` | State | Established human plague, positive exact loss, non-rat provenance, plus the validator contract. | Temporary `famine_adapter_result`. | Calls outbreak food pressure only. | `020_black_plague_effects.txt:black_plague_apply_current_state_mortality_once`; parent must supply missing proof. |
| `famine_adapt_natural_disaster_state` | State | Positive Event 013 loss plus the validator contract. | Temporary `famine_adapter_result`. | Calls natural-disaster food pressure only. | `013_natural_disasters_effects.txt:natural_disaster_apply_population_loss`; parent must supply missing proof. |
| `famine_validate_condemnation_receipt_exact` | Country with explicit state and actor targets | Exact famine state, food, environment, transport, policy, actor, cause, people amount, generation, revision, and request identity proof. | Temporary `famine_condemnation_valid`. | Validation only. | Famine condemnation wrappers. |
| `famine_condemn_deliberate_starvation` | Country | Valid famine condemnation receipt. | Temporary `famine_condemnation_result`. | Existing Condemnation source only. | Former deliberate-starvation decision callers after parent rewiring. |
| `famine_condemn_relief_obstruction` | Country | Valid famine condemnation receipt. | Temporary `famine_condemnation_result`. | Existing Condemnation source only. | Future exact relief-obstruction owner. |
| `famine_condemn_concealment` | Country | Valid hidden famine mortality/concealment receipt. | Temporary `famine_condemnation_result`. | Existing hidden Condemnation source and durable famine concealment flag. | Former concealment decision caller after parent rewiring. |

Famine helpers call only `famine_request_*` food endpoints. They do not set or consume any `apply_food`/`apply_flight` switch and cannot create movement.

### Migration-owned helpers

| New helper | Scope | Inputs | Outputs | Side effects | Intended call sites |
| --- | --- | --- | --- | --- | --- |
| `migration_record_current_state_cohort_custody_exact` | State | Explicit cohort ID equal to the unambiguous current cohort; aligned migration ledgers; internment/forced-labor action; route, actor, site, transaction, generation, revision, and request proof; actor target. | Temporary `migration_current_state_custody_result`. | Resolves one explicit row and forwards its fresh whole-row amount. No movement, food, population, or Deaths mutation. | Camp owner after exact custody assignment; current call is blocked pending proof and parent rewiring. |
| `migration_record_cohort_custody_action_exact` | State | Explicit ID, action, whole-row living amount, route/actor/site/transaction proof, aligned arrays, current host, live status, generation, revision, and request identity. | Temporary `migration_cohort_custody_result`, resolved row fields, duplicate/result markers. | Saves short-lived `migration_cohort_custody_owner`; calls a migration-owned exact achievement recorder; clears one-shot request/proof fields. Never edits the cohort row. | Exact internment or labor-assignment owner only; no complete current source transaction exists. |
| `migration_validate_condemnation_receipt_exact` | Country with explicit state and actor targets | Positive cohort ID and people amount plus exact state, route, actor, cause, generation, revision, and request proof. | Temporary `migration_condemnation_valid`. | Validation only. | Migration condemnation wrappers. |
| `migration_condemn_deportation` | Country | Valid exact cohort/route condemnation receipt. | Temporary `migration_condemnation_result`. | Existing Condemnation source only. | Forced-transfer owner after parent supplies the split proof bundle. |
| `migration_condemn_forced_return` | Country | Valid exact cohort/route condemnation receipt. | Temporary `migration_condemnation_result`. | Existing Condemnation source only. | Explicit return owner only; generic peace callback remains blocked. |
| `migration_condemn_violent_pushback` | Country | Valid exact cohort/route condemnation receipt. | Temporary `migration_condemnation_result`. | Existing Condemnation source only; no second Deaths debit. | Corridor/return owner after parent supplies the split proof bundle. |

No generic migration flight adapter was invented. The exact transfer operation remains a core migration owner API and is not duplicated here.

### Direct-death helpers classified by owner

| Helper | Scope | Inputs | Outputs | Side effects | Ownership boundary |
| --- | --- | --- | --- | --- | --- |
| `famine_apply_related_state_deaths_exact` | State | Complete famine proof bundle plus positive not-yet-applied occupation-repression or forced-labor amount. | Temporary `famine_related_deaths_applied`. | One exact state population loss and Deaths receipt; clears one-shot request fields. | Famine-owned only when the upstream owner proves the famine-side causal receipt. |
| `famine_apply_occupation_repression_deaths_exact` | State | Famine-owned exact death request. | Delegated applied amount. | Occupation-repression reason only. | Famine-owned. |
| `famine_apply_forced_labor_deaths_exact` | State | Famine-owned exact death request. | Delegated applied amount. | Forced-labor reason only. | Famine-owned. |
| `migration_apply_related_state_deaths_exact` | State | Positive not-yet-applied forced-displacement amount, explicit cohort ID, route proof, actor proof/target, generation, revision, and request identity. | Temporary `migration_related_deaths_applied`. | One exact state population loss and Deaths receipt; route deaths are rejected. | Migration-owned direct physical-death receipt only; exact transfer remains the route owner. |
| `migration_apply_forced_displacement_deaths_exact` | State | Migration-owned exact displacement-death request. | Delegated applied amount. | Forced-displacement reason only; no route transfer or food pressure. | Migration-owned. |

## Constants and tuning table

`common/script_constants/famine_adapter_constants.txt` owns `famine_condemnation_gain.deliberate_starvation = 25`, `relief_obstruction = 18`, `concealment = 12`, and `famine_adapter_pressure.nuclear_strike_population_fraction = 0.05`.

`common/script_constants/migration_adapter_constants.txt` owns `migration_condemnation_gain.deportation = 20`, `forced_return = 16`, and `violent_pushback = 22`.

No probability, AI weight, MTTH, random-list weight, or balance target was added. The numeric values are the existing condemnation gains and nuclear estimate moved into owner-specific categories.

There is no neutral adapter constant category. Shared validation uses existing neutral runtime/population/result constants; no new combined category was introduced.

The existing nuclear callback still references the transitional constant name in `common/on_actions/chaosx_famine_migration_on_actions.txt`. That caller is outside this subtask and is explicitly blocked until the parent rewires it to `famine_adapter_pressure.nuclear_strike_population_fraction`.

## Event-target and cleanup plan

Famine proof calls require the owner to provide the short-lived `famine_adapter_actor` event target. Famine condemnation requires `famine_condemnation_state` and `famine_condemnation_actor` targets. These targets are validation inputs only; the adapters do not create global targets.

Migration custody creates only the short-lived regular target `migration_cohort_custody_owner` after resolving the persisted row owner. It also saves `migration_cohort_custody_state` for the immediate state comparison. Neither target may become global.

Migration custody clears ID, action, amount, route, actor, site, transaction, generation, revision, request, receipt, and owner proof fields on accepted and rejected attempts. Durable migration achievement evidence remains outside adapter cleanup.

Famine adapters clear only temporary local amount/result fields. Owner systems must clear their normal proof variables at the transaction boundary; a stale owner proof must never be reused as a new generation/revision/request identity.

No daily, weekly, monthly, country-wide, or world-wide scan was added. Adapter calls remain sparse and owner-driven.

## Exhaustive mapping from the former combined file

| Former transitional helper | New owner | Migration action required |
| --- | --- | --- |
| `humanitarian_record_current_state_cohort_custody_exact` | `migration_record_current_state_cohort_custody_exact` | Rewire Camp owner and rename migration request/ledger fields; no alias retained. |
| `humanitarian_record_cohort_custody_action_exact` | `migration_record_cohort_custody_action_exact` | Rename the exact achievement call path and provide route/actor/generation/revision/request proof. |
| `humanitarian_apply_related_state_deaths_exact` | `famine_apply_related_state_deaths_exact` or `migration_apply_related_state_deaths_exact` | Classified by the accepted causal owner; no neutral adapter alias retained. |
| `humanitarian_apply_occupation_repression_deaths_exact` | `famine_apply_occupation_repression_deaths_exact` | Rewire only an unapplied exact famine-side owner request. |
| `humanitarian_apply_forced_labor_deaths_exact` | `famine_apply_forced_labor_deaths_exact` | Rewire only an unapplied exact famine-side owner request. |
| `humanitarian_apply_forced_displacement_deaths_exact` | `migration_apply_forced_displacement_deaths_exact` | Rewire only a separate direct displacement death; route deaths remain outside this helper. |
| `humanitarian_adapt_air_winter_state` | `famine_adapt_air_winter_state` | Rewire Fallout/Air Winter and supply the famine proof bundle. |
| `humanitarian_adapt_camp_state` | `famine_adapt_camp_state` | Rewire Camp Deaths bridge and supply food/environment/transport/policy/replay proof. |
| `humanitarian_adapt_chemical_state` | `famine_adapt_chemical_state` | Rewire CBRN operation bridge and supply famine proof fields. |
| `humanitarian_adapt_black_plague_state` | `famine_adapt_black_plague_state` | Rewire Black Plague mortality bridge and supply famine proof fields. |
| `humanitarian_adapt_natural_disaster_state` | `famine_adapt_natural_disaster_state` | Rewire Event 013 aftermath and supply famine proof fields. |
| `humanitarian_condemn_deliberate_starvation` | `famine_condemn_deliberate_starvation` | Rewire starvation caller with exact state/food/policy/actor receipt. |
| `humanitarian_condemn_relief_obstruction` | `famine_condemn_relief_obstruction` | Future owner only until exact relief proof exists. |
| `humanitarian_condemn_concealment` | `famine_condemn_concealment` | Rewire concealment caller with hidden mortality state and proof. |
| `humanitarian_condemn_deportation` | `migration_condemn_deportation` | Rewire forced transfer after exact cohort/route proof. |
| `humanitarian_condemn_forced_return` | `migration_condemn_forced_return` | Rewire explicit return owner after exact route proof. |
| `humanitarian_condemn_violent_pushback` | `migration_condemn_violent_pushback` | Rewire corridor/return owner after exact route/death proof. |

## Caller census and exact blockers

The following census was taken from the current working tree before deleting the combined definition file. No caller was edited in this pass.

| Current caller | Former call | Intended new call | Exact facts currently missing or unsupported |
| --- | --- | --- | --- |
| `common/scripted_effects/fallout_consolidated_effects.txt:4034`, `air_winter_apply_state_population_loss` | `humanitarian_adapt_air_winter_state` | `famine_adapt_air_winter_state` | Exact state and applied loss exist; explicit food, environment, transport, policy, actor target, generation, revision, and request identity fields are not supplied at this call. |
| `common/scripted_effects/camp_repression_rework_effects.txt:1962`, `camp_rework_record_latest_state_deaths` | `humanitarian_adapt_camp_state` | `famine_adapt_camp_state` | Exact applied site deaths and responsible country exist; a food receipt, environmental/transport/policy proof, actor target, generation, revision, and replay request identity are absent. Site type is not a complete food receipt. |
| `common/scripted_effects/camp_repression_rework_effects.txt:5104`, `camp_rework_commit_exact_cohort_custody` | `humanitarian_record_current_state_cohort_custody_exact` | `migration_record_current_state_cohort_custody_exact` | Explicit ID, action, amount, actor token, site token, and current host are partially available; exact route proof, actor target, generation, revision, request identity, and migration-renamed aligned ledgers are absent. Partial rows remain unsupported. |
| `common/scripted_effects/cbrn_occupation_effects.txt:516`, `cbrn_occupation_apply_accepted_operation_state` | `humanitarian_adapt_chemical_state` | `famine_adapt_chemical_state` | Exact state, actor-related variables, delivery route, contamination, and applied deaths exist; the famine-specific food/environment/transport/policy proof envelope and one-shot generation/revision/request identity are not supplied to the adapter. |
| `common/scripted_effects/020_black_plague_effects.txt:1432`, `black_plague_apply_current_state_mortality_once` | `humanitarian_adapt_black_plague_state` | `famine_adapt_black_plague_state` | Exact human outbreak and applied loss exist; no explicit famine food, environment, transport, policy, actor target, generation, revision, or request identity receipt exists. Rat provenance remains rejected. |
| `common/scripted_effects/013_natural_disasters_effects.txt:5344`, `natural_disaster_apply_population_loss` | `humanitarian_adapt_natural_disaster_state` | `famine_adapt_natural_disaster_state` | Exact state and Event 013 death amount exist; current owner does not expose the full famine food/environment/transport/policy/actor/replay bundle. |
| `common/decisions/famine_migration_decisions.txt:1340` | `humanitarian_condemn_concealment` | `famine_condemn_concealment` | Caller sets a concealment flag/pressure context but does not provide explicit state target, actor target, food/environment/transport/policy/cause proof, people amount, generation, revision, or request ID. |
| `common/decisions/famine_migration_decisions.txt:1415` | `humanitarian_condemn_deliberate_starvation` | `famine_condemn_deliberate_starvation` | Caller identifies a famine stage but not an exact state-local people receipt and independent food/environment/transport/policy/actor proof bundle. |
| `common/decisions/famine_migration_decisions.txt:3262` | `humanitarian_condemn_violent_pushback` | `migration_condemn_violent_pushback` | Route-death/finalize values exist in the decision path, but no explicit migration state/cohort/people/route/actor targets, generation, revision, or request identity is supplied to the new wrapper. |
| `common/decisions/famine_migration_decisions.txt:3900` | `humanitarian_condemn_forced_return` | `migration_condemn_forced_return` | Return finalize values exist, but the wrapper needs explicit cohort/people/route/actor/state targets and replay identity. Generic peace remains invalid. |
| `common/scripted_effects/famine_migration_forced_movement_effects.txt:240` | `humanitarian_condemn_deportation` | `migration_condemn_deportation` | The owner has exact transfer transaction, cohort, survivor, origin, destination, and actor context, but the new wrapper requires migration-named state/actor targets, positive people amount, route proof, generation, revision, and request identity; parent must add them at the valid-positive branch. |

No current caller invokes the direct-death aliases. They remain API-only until an owner proves that population has not already been debited and supplies the accepted owner-specific proof bundle.

## Exact public APIs still blocked by absent source facts

The following APIs are not fabricated or aliased by this split.

### Famine APIs

- `famine_request_occupation_pressure`: no exact law-change callback with state-local people amount and actor.
- `famine_request_bombing_pressure`: bombing recency and Air Winter deaths do not prove a bomber actor plus a separate food-route amount.
- `famine_request_war_pressure`: `on_war_relation_added` is country-level reassessment only; no front/siege state receipt exists.
- `famine_request_peace_pressure`: peace callbacks contain countries, not state-local food loss.
- `famine_request_event_pressure`: Event 5, 6, 14, 15, 21, 33, 50, and 95 roots expose no accepted ordinary famine receipt at the inspected owner points; Event 14 cannibalism deaths remain Event 14-owned.
- `famine_request_cluster_pressure`: cluster queues carry IDs and delays, not state-local food facts.
- `famine_request_scenario_pressure`: generic scenario intensity and country scope are not an applied food amount.
- `famine_request_blockade_pressure`: embargo/route flags without island, dependence, shortage, relief-exemption, and state amount proof remain insufficient.
- `famine_request_biological_warfare_pressure`: ordinary biological lifecycle has exact deaths but no current food-aftershock caller with complete actor and famine proof.

### Migration APIs

- Exact migration movement, organized evacuation, internal displacement, cross-border flight, deportation flow, reception, return, integration, and resettlement APIs remain core-owner responsibilities and are not duplicated in the adapter files.
- Event 5 lacks an exact deportation or collapse cohort transaction with origin, destination, people amount, actor, route, transport, safety, and replay proof.
- Event 6 release/control transfer lacks a refugee cohort, exact amount, route, and reception transaction.
- Event 14 spread queues and prisoner feeding do not prove central civilian cohorts; cannibalism deaths remain Event 14-owned.
- Event 15 territorial settlement and stewardship do not prove a cohort or exact return transaction.
- Event 21 `start_civil_war` supplies ideology and size, not state-local displaced people or route proof.
- Event 28 is already covered by the nuclear callback and must not gain a second movement call.
- Event 33 modifiers and random continent/state selection do not prove evacuation cohorts, shelter destinations, or safe return.
- Event 50 country embargo registration has no migration facts.
- Event 95 state control transfer is not a population transfer.
- Generic war/front, peace, cluster, and scenario dispatchers lack exact cohort/route/actor receipts.
- Protected internment and forced-labor evidence remain blocked unless an owner supplies the exact living cohort transaction required by the migration custody API.

### Owner-specific direct-death APIs

- `famine_apply_related_state_deaths_exact`, `famine_apply_occupation_repression_deaths_exact`, and `famine_apply_forced_labor_deaths_exact` remain blocked because current famine-like callers have already applied their physical loss or lack the complete famine proof bundle.
- `migration_apply_related_state_deaths_exact` and `migration_apply_forced_displacement_deaths_exact` remain blocked because route owners already own route deaths or no separate direct displacement transaction exposes the required cohort/route/actor proof.
- Movement is not death. No route-death amount may be passed to the neutral direct-death receipt.

## Migration plan for the parent

1. Add/rename the famine-only core endpoints and request fields used by `famine_adapter_effects.txt`; they must not delegate through a combined apply-flag API.
2. Add/rename migration ledger validators, cohort resolvers, status enums, and exact achievement recorders used by `migration_adapter_effects.txt`.
3. Rewire each current hazard caller only after its owner supplies the complete proof fields in the census; do not infer missing facts from existing death variables or modifiers.
4. Rewire famine and migration condemnation decision/transfer callers separately, with distinct target scopes and request identities.
5. Keep all event-root and generic on-action surfaces API-only until the exact blockers above are resolved.
6. Run a repository-wide final identifier scan after parent integration and remove every remaining combined adapter name without adding aliases.

## Event-target lifecycle

The prior owner handoffs confirm that short-lived regular event targets are sufficient for owner-to-state and row-owner handoffs. No global adapter target is justified. The existing migration live-row cleanup must continue removing every aligned row array while preserving durable achievement evidence.

## Evidence and MCP status

The required offline wiki core pages and vanilla documentation for effects, triggers, scopes, event targets, state population, scripted effects, and script constants were reviewed before this split. Vanilla documentation confirms state-local population effects and explicit event-target scope handling; no engine field supplies the missing owner facts.

The linked event owner surfaces were already inspected read-only in the parent handoffs before this adapter design. Recorded artifacts include Event 005/006 state-flow inspections and renders, Event 014/015 inspections/renders, Event 021/033 state-flow/lint artifacts, and Event 043/050 artifacts. The recorded limitations are preserved: large-workspace inline source truncation, Event 033 render timeouts/internal errors on some retries, Event 051/095 inspection timeouts, and an invalid event-compare artifact schema/cache blocker. Since this pass changes no event source or event graph, no new event compare claim is made.

The exact prior artifacts remain in `event005_006_adapter_owner_patch.md`, `event014_015_adapter_owner_patch.md`, `event021_033_adapter_owner_patch.md`, `event043_050_051_095_adapter_owner_patch.md`, `event_adapter_owner_map.md`, and `adapter_wiring_closure.md`. These artifacts are evidence for owner-surface classification only and are not treated as fresh post-change engine validation.

No weighted helper or probability-bearing field changed. The required probability-inspect/auditor/compare route was not applicable; no weights were added or tuned.

## Validation run and limitations

Read-only validation performed for this patch:

- mapped every former adapter helper and constant category to exactly one new owner namespace or the narrow neutral causal file;
- censused every current source caller of the former transitional helper names;
- checked that famine source helpers set only famine request fields and never a flight field;
- checked that migration custody helpers contain no food pressure, population, Deaths, or transfer effect;
- checked that neutral direct-death helpers exclude route deaths;
- checked that no new recurring action, world scan, event, decision, GUI, map, localisation, asset, achievement, or workbook file was edited;
- checked that the old combined adapter files were removed rather than aliased.

Standalone adapter lint is not exposed by the installed HOI4 MCP route. No game launch or live-save validation was performed. Parent integration must run the source parser/lint after the core and caller renames because this split intentionally references the final famine/migration core names that are not yet present in the transitional working tree.

## Known limitations and follow-up

The working tree still contains transitional `humanitarian_*` callers and core definitions outside this subtask. They are expected integration blockers, not silently supported aliases. Neutral `humanitarian_*` adapter definitions were not retained.

The current Camp custody owner does not provide route proof, actor target, generation, revision, or request identity; protected-cohort evidence remains blocked.

The current hazard owners expose exact applied death amounts but not the complete famine proof envelope; the new famine adapters reject them until parent-owned proof fields exist.

No generic movement adapter was added because no current external hazard owner supplies exact cohort/people/route/actor facts at a valid call point. This is deliberate fail-closed behavior and not a fallback.

No commit was created, as requested. No weights were changed.
