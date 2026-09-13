# Administration integration handoff

Continuation: `integration_finish_handoff.md` supersedes this handoff's generic national dismantlement payment/target description and monthly execution description.
The current generic command performs immediate finite release through one shared national reform helper, and the monthly adapter uses hidden `camp_administration_country.1` to establish the actual country ROOT.

Disposition: implemented integration source, with final cross-module acceptance and MCP comparisons pending parent review.
Acceptance basis: explicit parent delegation within the user-approved complete administration plan recorded in `accepted_implementation.md`.
No commit was created, as requested by the parent.

## Files and identifiers

Changed existing files:

- `common/scripted_effects/camp_repression_rework_effects.txt`: eligible-country initialization, active-site initialization/reopening, terminal cleanup, bounded monthly dispatcher, generic instant policy outcomes, selected dismantlement, ledger refresh, legacy GUI purchase guards.
- `common/scripted_effects/genocide_crisis_effects.txt`: no building-count recruits on liberation, no old instant percentage debit in abstract policy payloads, regional state-control callback.
- `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`: preserved public generic dispatcher and legacy body; new priority-only adapters for construction/extraction; fail-before-payment retired commands.
- `common/on_actions/genocide_crisis_on_actions.txt`: one-time regional historical setup after existing versioned migration, startup CXT carrier registration, and additive tag-only CXT daily repair; no new whole-world recurring hook.
- `common/decisions/camp_repression_generic_decisions.txt`: eight retired candidate eligibility gates.
- `common/decisions/genocide_crisis_decisions.txt`: six retired candidate eligibility gates.
- `common/ideas/camp_repression_rework_ideas.txt`: removed flat national construction benefits from the three generic network ideas; liabilities retained; modifier-free CXT extension carrier added.
- `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt`: removed old construction/resource benefits from concentration-network and forced-labor carriers; security/compliance liabilities retained.
- `common/scripted_triggers/camp_repression_rework_triggers.txt`: only the granted `has_camp_category_visible_action` predicate expanded to initialized administration, material records and continuing work.

New files:

- `common/scripted_effects/camp_administration_integration_effects.txt` and matching `.md` document country initialization, guarded monthly callbacks, routine cancellation and terminal cleanup.
- `common/scripted_triggers/camp_administration_integration_triggers.txt` contains registry-retention and retired-action predicates.

No new tuning constants, icons, assets, localisation keys, global event targets, whole-world recurring hooks, shared core files, GUI files, or runtime configuration were introduced by this worker.
All local helper contracts are documented in `common/scripted_effects/camp_administration_integration_effects.md`.

## Monthly and lifecycle contract

The existing bounded active-country dispatcher runs `camp_admin_integration_monthly_country` once per foundation calendar-month key.
Callback order is country prepare, foundation monthly administration, wider occupation monthly records, country monthly institutions/civil programs, then legacy political pressure projection.
Country workers own retirement of their old monthly bridges and their own mission cleanup.
The original global active-state percent-loss loop is removed.
Legacy monthly state public aliases call the same guarded country adapter rather than applying a second state debit.

Active-site registration initializes only after the responsible-country pointer is assigned and validated and site type is established.
It calls the foundation's same-authority reopening API without resetting finite cohorts, original responsibility or cumulative history.
Resolution/unregister/dismantlement/annexation close finite cohorts before pointers or registry membership can be erased.
Special-country exclusion closes the bounded active-state array before clearing it.
The migration owner prepare/clear lifecycle remains in place; quiet legacy project cancellation uses the same labor owner class and generation-qualified clearing contract.
Release adds neither civilian population nor recruitable manpower.
Material history records use the parent-owned `camp_admin_record_history` with original responsible authority and actual state ID.
Close/liberation records occur only before first closure; evidence resolution records only before first resolution, and evidence-destruction choices append their own material record.
The monthly adapter consumes the foundation's economic completion flag once and distinguishes a civilian conversion by its saved completed type.
Camp dismantlement still removes camp-specific buildings; existing civilian infrastructure remains.

The camp-owned CXT carrier `chaosx_cxt_extension_camp_administration` and its `_apply` helper follow the existing dynamic extension contract.
Startup registers it from the existing bounded random-country scope; `on_daily_CXT` repairs registration and requests synchronization only on a newly inserted carrier.
The fixture initializes existing finite camp ledgers and interface defaults once and exposes `camp_admin_cxt_fixture_ready`; it does not seed admissions, mutate population or supply resources.

The regional owner supplies `camp_occ_historical_setup`, `camp_occ_on_state_control_changed`, `camp_occ_monthly_country`, `camp_occ_close_country`, and `camp_occ_country_has_records`.
Historical setup is called in global on-startup scope after camp migration; state-control callback is called in actual FROM.FROM state scope.
Source membership, chronological campaign authority, and nonoverlap with custody/shared occupation deaths belong to the regional owner.

## Retired candidates and compatibility

Generic candidates gated out after `camp_admin_initialized`: `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, `generic_labor_project_cycle`, `generic_reform_and_dismantlement`.
Genocide-crisis candidates gated out after initialization: `germany_intensify_extermination_policy`, `germany_transfer_prisoners_to_experiment_site`, `genocide_intensify_deportations`, `genocide_redirect_trains_and_supplies`, `japan_transfer_prisoners_to_experimental_facilities`, `sov_raise_forced_labor_quotas`.
Visibility, availability and applicable mission activation receive the gate; numerical `ai_will_do` clauses are unchanged.
The exact candidate list was sent to the probability owner for same-scenario final comparison.

Legacy public construction/extraction identifiers request only the new economic priority through `camp_admin_set_priority`, using the parent-owned quote, legality gate and single payment.
Other retired generic commands reject before legacy costs; existing legacy GUI labor/guard/quota entrypoints also reject before payment after initialization.
Generic exact activation, inspection, evidence and dismantlement retain their existing target and payment contracts.
The strict exact migration custody staging/commit helper bodies are preserved.
No second finite-cohort copy is inferred from a migration receipt without an approved reconciliation contract.

## Meaningful checks completed

`integration_validation.json` records 15 task-specific source checks and SHA-256 hashes for the eleven owned script files at handoff.
A source comparison against `C:/Users/klimp/AppData/Local/Temp/camp_administration_baseline_20260906` confirmed both `camp_rework_prepare_exact_cohort_custody` and `camp_rework_commit_exact_cohort_custody` remained identical after normalizing line endings.
Source traces verified closure precedes pointer clear or registry/building teardown in evidence resolution, unregister, dismantlement and annexation.
The old monthly state entry contains no percent debit, and the global monthly effect contains exactly one new country-driver call and no active-state monthly iteration.
Liberation contains no `add_manpower`; the legacy genocide policy file contains no direct percentage death call.
All `ai_will_do` blocks in both owned decision files match preserved baseline clauses after whitespace normalization.
Every new dependent helper named by the integration currently has a live definition in the new administration modules.
Selected voluntary closure invokes the finite replacement-preserving site-reform helper, economic completion history consumes its flag once, and the CXT fixture is guarded by its one-time readiness marker.
Integration contains no physical population or death transaction call.
These are source checks, not execution by the HOI4 engine.

The required initial `hoi4.event_inspect` call used mode `trace`, selector `{file: "events/genocide_crisis_events.txt"}`, maxDepth 2, maxNodes 40 and maxEdges 80.
It returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_inspect; Caused by: timed out awaiting tools/call after 180s`.
No event artifact/revision was produced.
The parent then requested no more worker MCP submissions while coordinating service capacity.
No source-only report is presented as equivalent engine evidence.

## Omissions, uncertainty and parent work

- Final event/helper lifecycle inspection and the probability owner's final same-scenario comparison remain required; baseline provenance and exact blocked probability call are in `ai_audit.md`.
- Full twelve-month economic/payment/mortality conservation and period calibration belong to the foundation, country and regional scenario owners; this worker verified integration call structure only.
- The protected exact migrant-custody receipt remains independent of foundation finite detainees until a proven reconciliation contract is supplied.
- Different-authority reuse of a previously closed site remains unsupported by the single immutable-authority ledger.
- Selected voluntary dismantlement is wired to `camp_admin_reform_site`; final foundation validation must confirm finite target capture and continued paid replacement after legacy active-array removal.
- Foundation owner accepted three source-review fixes raised here: replace unsupported direct `limit` entries under `for_each_scope_loop` with guarded effects, immediately refresh national output on site closure, and prevent a fully completed civilian registry from starving later economic project selection.
- National-reform callers must invoke `camp_occ_close_country` before `camp_admin_begin_reform`; the parent, major and civil owners were notified because foundation keeps this cross-module coupling caller-owned.
- Parent localisation review must reconcile `generic_detention_network_administration_desc`, `generic_expanded_labor_network_desc`, `generic_overextended_repression_network_desc`, and the liberation tooltip with removal of flat output/recruit grants.
- Parent owns GUI evidence, civil location activation/authority gates, quiet AI authorization of country policies, and the final completion claim.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-state-ledgers`, and `chaos-redux-subagents`.
No skill was created or changed.
The parent explicitly accepted retirement of the old separate restricted-method monthly upkeep with the legacy pulse; excluded one-time method implementations remain unchanged.
