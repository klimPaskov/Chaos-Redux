# Event 006 core scripted-system audit v97

Date: 2026-08-02

Scope: shared Event 006 allocation, reservation, execution, crisis, scenario, registry, ledger, on-action, and generic-focus validation surfaces. Country-package admission, bespoke package focus content, assets, and live or in-game testing remain outside this audit.

## Verdict

The shared Event 006 core is source-closed for the accepted v97 contracts and has no clearly safe local gameplay patch from this audit. The whole event remains **HOLD / PARTIAL** because package admission, capacity, focus diagnostics, formables, assets, AI, balance, super-event, and runtime evidence remain open under the current whole-event authority.

The newly accepted single-tree contract is compatible with the release transaction. `common/national_focus/006_independence_wave_focus.txt` defines the one `independence_wave_focus_tree`; full assignments load it, reviewed carrier overlays avoid `load_focus_tree`, and `independence_wave_dispatch_package_final_validation` fails closed when neither `has_independence_wave_generic_focus_contract` branch is true. The standalone four-pass finalizer and the Event 005-first joint finalizer run that barrier after activation and before durable origin history or shared-plan commit. Post-formation overlay assignment preserves the full-framework flag, so the contract remains true through the existing generic tree rather than admitting an unowned overlay.

No fallback, new package, tag admission, or bespoke focus tree was added.

## Existing helper map

The following helpers already provide the reusable core. No new helper is proposed.

| Helper | Scope and inputs | Outputs and side effects | Current call sites |
| --- | --- | --- | --- |
| `independence_wave_capture_wave_tuning` | Country/coordinator scope; current chaos tier and mode | Publishes automatic target count, territory tier, force level, and chaos band from shared constants | Standalone execution and `liberations_joint_prepare_and_execute_incident` |
| `independence_wave_begin_plan_contribution` / `independence_wave_begin_package_reservation` | Global coordinator plus frozen candidate targets | Clears pending arrays, captures target/chaos metadata, reserves host/country/anchor only after exact attestation and survival checks | Automatic allocator, scenario allocator, and joint Event 005/Event 006 planner |
| `independence_wave_allocate_automatic_packages` | Frozen target and allocator phase | Selects exact-count packages in anchor-first order and records aligned package, region, host, territory, force, and rejection arrays | Standalone automatic execution and the Event 005-first joint transaction |
| `independence_wave_expand_selected_optional_territory` | Frozen selected package arrays | Applies compact territory to all selected packages, then extended territory only when no optional failure is present; fail-closes exact-count alignment | Standalone and joint allocation paths |
| `independence_wave_execute_standalone_frozen_plan` and the four-pass execution helpers | Locked frozen plan with Event 006 ownership | Prepares origins, activates registries, dispatches package setup, applies the generic-focus final validation barrier, commits only after every package validates, and compensates post-mutation failures | `chaosx.nr6.1`, `chaosx.nr6.3`, and scenario trigger paths |
| `liberations_joint_prepare_and_execute_incident` | Shared coordinator with Event 005 and Event 006 contributions | Reserves Event 005 anchors first, then Event 006 anchors, expands optional territory, takes one lock, executes both contributions, and commits or rolls back as one transaction | Event 005/Event 006 joint presentation branch |
| `independence_wave_scenario_attempt_ranked_packages` / `independence_wave_allocate_scenario_packages` | SCN-008 mode/intensity and all 138 current-map-bound rows | Rerolls invalid or living tags, attempts every viable ranked candidate, records rejections, and finalizes selected-count metadata without fallback | Scenario trigger and report flow |
| `independence_wave_scenario_apply_type` plus host-war, patron, League, and partition helpers | Committed scenario type and selected country/host ledgers | Applies scatter, congress, host wars, universal former-host belligerence, patrons, or partition while preserving bounded targets and cleanup | `independence_wave_trigger_scenario` |
| `independence_wave_pay_crisis_cost`, `independence_wave_queue_crisis_release`, `independence_wave_resolve_pre_wave_crisis`, and requester-loss recovery | Host country crisis mission and pressure flags | Charges concrete cost, queues one bounded retry chain, records success/failure/cancellation history, and cleans orphaned requester queues on annexation | Crisis decision, `chaosx.nr6.3`, and `006_independence_wave_crisis_on_actions.txt` |
| `independence_wave_registry_record_event6_origin` / `independence_wave_registry_clear_event6_origin` and `chaosx_country_*` collections | Country lifecycle and static registry projections | Records/clears generation-scoped origin state; exposes reusable all, Event 006, bound/unbound, overlay, regional, and active collection views | Shared origin setup/cleanup and downstream consumers |
| Host, patron, Network, and League ledger APIs in `006_independence_wave_effects.txt` | Country scope with aligned global arrays | Initialize, clamp, mirror, register, recompute, remove, and generation-clean all dynamic ledgers; living patrons and active members are checked before writes | Origin activation, scenario type effects, focuses, decisions, and evolution incidents |
| `has_independence_wave_generic_focus_contract` and `independence_wave_dispatch_package_final_validation` | Active prepared country after package setup and registry activation | Requires the one generic tree for full assignments or a reviewed living carrier for additive overlays; converts adapter success to failure otherwise | `independence_wave_validate_frozen_country_packages`, the single-country compatibility wrapper, and the joint finalizer |

## Constants and tuning table

Centralized constants are in `common/script_constants/006_independence_wave_constants.txt`, `006_independence_wave_mechanics_constants.txt`, `006_independence_wave_scenario_constants.txt`, and `006_independence_wave_crisis_constants.txt`.

| Contract | Current source values |
| --- | --- |
| Automatic ladder | Calm 6, Gathering 8, Rising 10, Chaos Tier 14, Totalen Chaos 20, World Collapse 20 |
| Intensity mapping | Low anchor/fragile; medium compact/viable; high extended/armed; maximum extended/high-chaos |
| Allocation order | All anchors, then compact, then extended, then lock; no fallback branch is used |
| Scenario registry | 138 current-map-bound ranked candidates from the 206-row registry; 14 package attestations across 13 compatible groups; 13 overlay-only rows excluded from selectable release |
| Scenario types | Sovereign scatter, common congress, wars of separation, universal belligerence, patron worlds, great partition |
| Crisis gate | Stability below 0.35 or severe occupation pressure above the documented resistance threshold; paid 120-day mission; one-day retry with 14-attempt bound and explicit blocked receipt |
| Crisis cost | 5,000 manpower, 20 Army XP, 20 Command Power, 500 infantry equipment, 100 support equipment, and 0.05 stability |
| Shared ledgers | Country legitimacy/recognition/capacity/security/instability; former-host relation; patron influence/aid; Network; League; and revisionist-pressure values are initialized, clamped, and cleaned through central helpers |

## Event-target and cleanup plan

Short-lived regular event targets carry the current candidate country, anchor, former host, patron, and first/next war actors through one effect chain and are overwritten before each new candidate or declaration. They are used for the frozen execution context and are not treated as persistent global state.

Persistent global targets are limited to the scenario actor and bounded war surfaces, including `independence_wave_latest_actor` and `independence_wave_first_former_host_war_actor`; they are cleared by the scenario completion, declaration-failure rollback, and belligerence-target cleanup helpers.

Crisis queue state uses country flags and requester variables rather than a broad periodic scan. `independence_wave_cancel_crisis_runtime`, `independence_wave_record_blocked_crisis_consequence`, `independence_wave_recover_crisis_requester_loss`, and the malformed-orphan branch of `chaosx.nr6.3` clear queue, retry, requester, barrier, and runtime flags while writing a bounded resolution row.

Generation cleanup clears focus assignment flags, package metadata, origin state, active/Network/League rows, host and patron rows, pending arrays, rejection arrays, and temporary event targets before a new generation can reserve the same footprint. Host-war target marks are cleared both on failed declarations and after a committed scenario.

## Migration plan

No migration is required. Existing allocator, execution, crisis, scenario, registry, focus-contract, and ledger call sites already route through shared helpers. Keep package-specific setup and final-validation adapters behind the common dispatcher, keep the generic focus contract as a final barrier, and do not duplicate allocator or ledger logic in package files.

If later runtime evidence finds a regression, patch the narrow owning helper and add a task-specific handoff rather than bypassing the final barrier or admitting a package through a fallback.

## Validation and evidence

`python -B .tools/audit_event6_allocator.py` passed after the generic-focus contract was present: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, 13 compatible reservation groups, RG-RHINE-SAAR pair capacity of two, the 6/8/10/14/20 ladder, crisis gates, all-anchors/compact/extended/lock order, and Event 005-first joint order.

A task-specific static focus-contract check passed: the single generic tree is referenced by the assignment effect, the final-validation dispatcher contains the fail-closed `has_independence_wave_generic_focus_contract` barrier, and both standalone and joint finalizers place validation before origin-history and shared-plan commit.

Read-only `hoi4_event_inspect` scan and state-flow artifacts were obtained for `events/006_independence_wave.txt` and `chaosx.nr6.1`. The MCP responses were partial because inline files were truncated and validation was deferred, so they are source-navigation evidence only and not runtime proof.

Offline Paradox wiki event-target, scope, trigger, and effect pages plus vanilla script-constant, effect, and trigger documentation were consulted. The required Chaos Redux events, subagent, and decisions/missions skills were read before the audit.

## Risks, unsupported analysis, and skipped validation

No in-game launch, save/load cycle, 32-cell SCN-008 execution sweep, focus geometry/render inspection, or live package allocation was run because the controlling scope keeps live testing out of this pass and the available MCP inspection is byte-limited. These remain parent-owned evidence gaps.

The MCP partial responses do not prove engine acceptance of helper lifecycle, dynamic scope resolution, or focus-tree rendering. Static source also cannot prove force materialization, host survival in a live save, or rollback after a mid-finalization engine failure.

The exact attestation set and package content remain unchanged. Unattested rows, overlay-only rows, missing assets, formable/source gates, and dormant super-event paths remain fail-closed. No simplification or fallback was used.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_core_system_audit_v97_2026_08_02.md`

No gameplay, constants, scripted-effect, scripted-trigger, event, on-action, package, focus, or localisation file was changed by this audit.
