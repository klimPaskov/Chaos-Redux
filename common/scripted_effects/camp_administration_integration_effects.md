# Camp administration integration

Acceptance: the parent-assigned implementation of `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/accepted_implementation.md`.
This adapter owns integration with the existing camp registry and preserves the shared accounting, migration, and event frameworks as read-only dependencies.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `camp_admin_integration_initialize_country` | Eligible country; no parameters | Idempotent foundation, institution/civil and regional-ledger defaults; cancels retired generic routine work | `camp_rework_initialize_eligible_country_variables`, monthly adapter |
| `camp_admin_integration_monthly_country` | Current registered country; ROOT may be the host | Fires hidden recipient event `camp_administration_country.1`, rebasing ROOT to the actual actor | Existing bounded `camp_rework_monthly_global_pulse`; compatibility `camp_rework_apply_monthly_state_effects` |
| `camp_admin_integration_monthly_country_recipient` | Actual country ROOT; no parameters | Calendar guard, quiet cancellation, country preparation, foundation maintenance/economy/mortality, regional records, funded country work, legacy pressure projection | Hidden `camp_administration_country.1` immediate effect only |
| `camp_admin_integration_seed_japan_labor_host` | Japan ROOT after the accepted start date; eligible Liaotung state 716 | One-time registration of the existing industrial host under Japan or its Manchukuo subject; no population or building grant | Guarded recipient before country preparation |
| `camp_admin_integration_cancel_routine_projects` | Country; optional legacy project target/reserve | Removes generic labor/reform missions without success or timeout payout, clears legacy labor target/reserve, uses the existing generation-qualified migration owner cleanup | Initialize, monthly and terminal-country adapters |
| `camp_admin_integration_close_country` | Country before registry teardown | Closes registered finite cohorts in place, halts programs, cancels civil work and regional campaigns, preserves cumulative records | Annexation and special-country exclusion |
| `camp_admin_integration_close_site` / `camp_admin_integration_reform_site` | State; existing immutable authority | One closure/liberation history entry before first closure; voluntary reform delegates finite civilian replacement target capture to foundation | Legacy resolve/unregister/annexation and voluntary/enemy dismantlement paths |
| `camp_admin_integration_record_site_history = yes` | State; required temporary history-kind input | Writes material state history on the original responsible country | Evidence resolution/destruction and lifecycle wrappers |
| `camp_admin_integration_record_completed_project` | Country; foundation completion flag, state and type | Consumes completion once; writes economic-project or civilian-conversion history | Immediately after foundation monthly callback |
| `camp_admin_register_cxt_content` / `chaosx_cxt_extension_camp_administration_apply` | Startup registration country / initialized CXT | Registers modifier-free carrier, initializes existing camp ledgers once, publishes fixture readiness | Existing startup and additive tag-only daily repair |
| `camp_admin_integration_has_continuing_work` | Country trigger | Retains registered civilian replacement, regional records, civil policy/review/claims, institutional/economic work and archive/oversight work | Inactive-country registry cleanup and category visibility |
| `camp_admin_legacy_generic_action_is_retired` | Country trigger; temporary `camp_rework_action_id` | Tests six retired generic command identifiers; no mutation | Public generic dispatcher |
| `camp_admin_generic_reform_visible` / `camp_admin_generic_reform_available` | Generic country ROOT outside bespoke civil kits | Visibility checks reform authority and remaining active sites; availability validates every site's current control, initialization, open status and original responsibility, incompatible closure work, and inclusive live PP affordability | Native `generic_dismantle_detention_network`, parent-owned GUI action 2, guarded reform effect |
| `camp_admin_generic_reform_quote` | Country trigger; existing active-site count | Always succeeds after setting temporary `camp_admin_reform_quote_pp` from centralized command constants; no payment | Shared availability and quote refresh |
| `camp_admin_generic_reform_refresh_quote` | Country effect; no parameters | Publishes current quote as persistent `camp_admin_generic_reform_pp`; no payment | Parent-owned `camp_admin_refresh_interface` |
| `camp_admin_generic_reform` | Actual country ROOT; no parameters | Revalidates, pays PP once, snapshots active states, records closures, ends regional campaign, releases survivors and retains paid civilian replacement, unregisters closed sites, clears snapshot, marks completed reform and refreshes ideas/display | Native decision, public generic dispatcher, parent-owned GUI action 2 |

No adapter adds population, directly records deaths, creates a global event target, or owns a new whole-world recurring hook.
`camp_admin_integration_month` stores the foundation's year-and-calendar-month key.
`camp_admin_japan_liaotung_registered` marks the one-time accepted industrial-host registration.
`camp_admin_generic_reform_pp` is a display cache; affordability and payment always compute the temporary quote afresh.
`camp_admin_generic_reform_states` is a bounded synchronous snapshot cleared before collection and after teardown, so unregistering does not mutate the array being iterated.
The guard wraps every module callback, so multiple legacy state calls cannot repeat maintenance, payments, awards or pressure in the same calendar month.
The existing host-only monthly hook still enters the duplicate-safe active-country array.

## Registration and terminal order

`camp_rework_register_active_site` assigns and validates the responsible authority, establishes the legacy site type, calls `camp_admin_initialize_site`, then calls `camp_admin_reopen_site` before recording the country registry entry.
Initialization starts an empty cohort and stores the immutable responsible authority.
Reopening is a foundation-owned same-authority check; it preserves finite history and never restores released or dead detainees.
Different-authority reuse requires a separate phase ledger and remains unsupported rather than silently rewriting responsibility.

Closure precedes teardown in site-evidence resolution, inactive-site unregister, dismantlement start/completion, and annexed-country site handling.
Voluntary dismantlement uses `camp_admin_reform_site` to preserve a finite civilian replacement target before release; enemy liberation uses closure without assigning a new government's labor project.
The generation-qualified migration preparation and clearing calls remain in their existing lifecycle positions after finite-cohort closure.
Release never adds population or manpower; liberation no longer converts building levels into recruits.
Ordinary built civilian infrastructure is not removed by these adapters.
Legacy dismantlement still removes camp buildings and camp-only modifiers.

Regional setup uses the occupation owner's one-time `camp_occ_historical_setup` from existing `on_startup` after versioned camp migration.
The existing state-control callback invokes `camp_occ_on_state_control_changed` in the actual changed state scope.
The regional module owns its source proof and exclusions from shared occupation mortality.

## Public action compatibility

`camp_rework_dispatch_generic_action` remains the public identifier.
For initialized administration, old construction and extraction action identifiers request only `camp_admin_priority.works` or `.extraction` through `camp_admin_set_priority`.
The command revalidates its current quote and pays once through the parent-owned control API; it does not perform the old material purchase or start a routine mission.
Old guard, quota, expansion and radicalization purchases fail closed before payment.
The prior dispatcher body remains `camp_rework_dispatch_generic_action_legacy`, reached only for a nonretired action or a pre-administration country.
Exact generic activation, inspections and evidence preserve their existing action/target/quote contracts.
The generic national dismantlement command uses the shared national reform adapter; selected voluntary site closure remains separately owned.
The protected exact-custody receipt is not copied into a second detainee ledger without a proven depletion reconciliation contract.

## Tuning and presentation

No new balance constants are introduced.
Calendar keys and priority enums use foundation constants; retained inspection/evidence/dismantlement quotes use the existing site-cost subsystem.
National generic reform uses `clamp(policy_pp + camp_active_site_count * policy_pp_per_site, policy_pp, policy_pp_max) * mandate_pp_multiplier` from `camp_admin_command`.
Current tuning yields 15 to 60 political power; the native decision's fixed `ai_hint_pp_cost = 60` is an engine hint, not another debit.
It consumes no manpower, equipment or per-site legacy purchase at authorization.
The foundation releases the finite survivor stock immediately and captures its replacement target before release; shortages affect subsequent funded employment projects only.
No building removal is called by this national path.
After closure, `camp_rework_reformed_legacy` activates the existing idempotent reform idea projection while expansion remains frozen by `camp_admin_begin_reform`.
The existing reform idea grants stability and political-power factors only; no flat construction, industrial-output or extraction benefit is introduced.
Finite economics replace the three generic national flat construction bonuses and the two old state construction/resource bonus carriers; their security, compliance and evidence liabilities remain.
Old generic and genocide-crisis policy payloads do not perform instant percentage population debits.
The standalone burst helper and unrelated CBRN method implementations remain outside this change.
Both ledger opening and legacy display rebuild refresh the parent-owned administration interface without introducing a second payment path.
No new icons or assets are required by the integration layer.
The CXT carrier is `chaosx_cxt_extension_camp_administration`, with no modifiers and no direct idea grant.
It registers through the existing dynamic extension bus in the existing bounded startup country scope.
The additive `on_daily_CXT` fallback synchronizes only when the carrier is newly registered; core CXT hooks retain recurring synchronization ownership.
The one-time `camp_admin_cxt_fixture_ready` fixture initializes already registered camp locations and the interface, without inventing admissions, resources or deaths.
Retirement of the old monthly pulse also retires its separate restricted-method upkeep call; the parent explicitly accepted this consolidation and the excluded method implementations remain unchanged.

## Validation and remaining work

Task-specific evidence and final source limitations are recorded in `../../docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/integration_handoff.md`, with the continuation in `../../docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/integration_finish_handoff.md`.
The event inspector call timed out after 180 seconds; this source review is not equivalent to engine evidence.
Decision eligibility changes require the probability owner's same-scenario final comparison against the preserved pre-edit bytes.
The parent owns final GUI evidence, localisation reconciliation, historical intake calibration and package completion.

## History input contract

Initialize temporary `camp_admin_history_kind_input` with the exact `constant:camp_admin_history_kind.<kind>` immediately before `camp_admin_integration_record_site_history = yes`.
The state helper copies that input into `camp_admin_record_kind` only after proving the immutable responsible-country pointer, then records history on that country.
Its six callers supply evidence, liberation or closure exactly as their lifecycle path requires.
No target, population change, payment, default kind or cleanup is introduced.
