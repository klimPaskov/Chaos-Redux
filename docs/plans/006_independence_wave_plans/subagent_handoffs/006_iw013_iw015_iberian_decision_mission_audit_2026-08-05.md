# Event 006 IW-013 / IW-015 Iberian Decision and Mission Audit

## Scope and status

This is a current-state audit of the NAV and GLC decision maps only.

The audit inspected the Iberian decision, package effect, package trigger, constants, AI, localisation, shared decision-cost, shared route-selection, and package-dispatch files.

The offline Paradox wiki decision reference, vanilla decision/effect/trigger documentation, and a vanilla timed-mission precedent were consulted before the audit.

Two narrow source defects were patched.

No obsolete audit log was used, no advisor icon was added, and no scripted GUI surface belongs to this decision map.

## Changed files

- `common/decisions/006_independence_wave_iberian_decisions.txt`
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_iberian_decision_mission_audit_2026-08-05.md`

## Issue list, sorted by severity

### Critical — resolved: all ten government-route projects were dead

The five NAV choices and five GLC choices tested an already selected shared government route in both `visible` and the installer helper limit.

No Iberian focus selects the shared route before these projects, so the choices were not visible at package setup and could not install a government even if surfaced externally.

The affected decision identifiers are `independence_wave_nav_ratify_fueros_charter`, `independence_wave_nav_convene_workers_board`, `independence_wave_nav_confirm_municipal_compact`, `independence_wave_nav_establish_pyrenean_command`, `independence_wave_nav_accept_protected_customs_mandate`, `independence_wave_glc_ratify_atlantic_charter`, `independence_wave_glc_convene_workers_port_council`, `independence_wave_glc_confirm_municipal_covenant`, `independence_wave_glc_establish_coastal_command`, and `independence_wave_glc_accept_protected_customs_mandate`.

The corresponding installer identifiers are `independence_wave_install_nav_constitutional_government`, `independence_wave_install_nav_workers_government`, `independence_wave_install_nav_municipal_government`, `independence_wave_install_nav_emergency_government`, `independence_wave_install_nav_patron_government`, `independence_wave_install_glc_constitutional_government`, `independence_wave_install_glc_workers_government`, `independence_wave_install_glc_municipal_government`, `independence_wave_install_glc_emergency_government`, and `independence_wave_install_glc_patron_government`.

Before the patch, each project required `has_independence_wave_*_route = yes`, while selecting that route was inside the same installer.

After the patch, each path requires its matching `independence_wave_route_*_available` flag, sets its route input, and calls the existing `independence_wave_select_government_route` helper.

The package-local government predicate remains the completion guard, preventing a second route after selection.

### High — resolved: founding missions could re-arm after success or timeout

`independence_wave_nav_hold_fueros_together` and `independence_wave_glc_hold_council_together` set a resolved or failed terminal flag but their activation blocks did not exclude either flag.

Consequently, a settled mission or a timed-out mission could activate again on the next evaluation and repeat a failure penalty or return a cleared mission.

The activation blocks now exclude both terminal flags, and `independence_wave_cleanup_iw_013_basque` plus `independence_wave_cleanup_iw_015_galicia` clear those flags when the package lifecycle ends.

### Low — remaining: four package duration constants are unused

`independence_wave_iberian_duration.regional_project`, `route_project`, `host_project`, and `sovereignty_project` have no current Iberian call site.

The map uses the shared short, standard, and long decision durations, while only `founding_crisis` uses the Iberian duration table.

This is not a runtime fault, but these stale tuning entries could mislead future balance work.

Recommendation: either bind the intended Iberian projects to those constants in a separately approved balance pass or delete the unused entries after confirming they are not reserved by the parent design.

### Low — remaining: the local compact crisis does not participate in the shared founding-mission concurrency list

`has_independence_wave_active_founding_mission` lists shared generic missions only, not `independence_wave_nav_hold_fueros_together` or `independence_wave_glc_hold_council_together`.

NAV and GLC can therefore run the generic founding mission alongside their local compact crisis.

The local crisis is a distinct package objective and every paid local project is serialized by its carrier-specific project gate, so this is not an exploit or duplicate local project loop.

Recommendation: retain this as intentional parallel pressure unless the event design requires a single global founding-mission cap, in which case change the shared trigger in a parent-owned cross-package pass.

## Decision category lifecycle notes

Both categories follow setup complete, local compact crisis, serialized paid projects, one government-route project, durable sovereignty, and optional Iberian Network integration.

NAV tracks fueros legitimacy and industrial capacity from 46 and 34, while GLC tracks council legitimacy and port capacity from 43 and 36.

Both ledgers are clamped through the package helper and require both values to reach the shared stable threshold of 60 to cancel the crisis successfully.

The route projects now use the availability flags established by the focus contract, then commit the shared government route and a matching local government idea and flag.

The local active-project predicates list all eleven paid or immediate project actions per carrier, so route selection, sovereignty, former-host work, and Network work cannot overlap another local project.

## Mission quality notes

| Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NAV | `independence_wave_nav_iberian_category` | Iberia, state 792 | IW-013 setup; both compact ledgers reach 60; capital held | 420 days | Cancels as resolved | Capital loss or timeout sets failed and applies project failure | Resolved: terminal activation guards prevent re-arm |
| GLC | `independence_wave_glc_iberian_category` | Iberia, state 171 | IW-015 setup; both compact ledgers reach 60; capital held | 420 days | Cancels as resolved | Capital loss or timeout sets failed and applies project failure | Resolved: terminal activation guards prevent re-arm |

The missions are not passive stores: completion depends on several paid projects with distinct military, administration, diplomatic, and strategic pressures.

## Cost and requirement clarity notes

The map contains no political-power exchange store, unit-creation loop, equipment reward, or unbounded resource reward.

Security projects pay manpower, Army Experience, infantry equipment, and support equipment through the shared security cost helper.

Administration projects pay Command Power, manpower, and a temporary civilian-factory-use modifier.

Diplomatic projects pay Command Power plus a convoy or train resource, and the strategic sovereignty action has a shared strategic cost and a spare-civilian-factory requirement.

Every paid action has a matching custom-cost trigger and custom-cost text key, and all six cost keys used by this map resolve in shared localisation.

The strategic sovereignty action checks spare civilian factories but does not reserve a factory modifier because it completes immediately; this is a shared-cost-model clarity point, not a free-resource or PP exploit in this Iberian surface.

## AI validity and route-lock notes

The NAV and GLC AI strategy profiles are correctly restricted by original tag, active package, completed setup, and profile flag.

The decision AI priorities distinguish standard, high, and urgent work, with the emergency-command routes receiving an at-war multiplier.

Former-host projects require a living former host and refuse to run while at war with it.

All corrected route decisions are hidden when their focus-contract availability flag is absent and disappear after the package-local route government is installed.

## Localisation and tooltip notes

The Iberian category descriptions display their respective dynamic ledger variables.

Project, failure, host, route, patron-route, and Network completion tooltips are present for the current decision identifiers.

The Iberian localisation file is UTF-8 with BOM, and all direct decision identifiers resolve there.

No new localisation was required for the two logic-only patches.

## Cleanup and exploit-risk notes

Both package cleanup helpers remove their mission and every local decision, remove local ideas, clear ledger variables, and clear lifecycle, government, progress, Network, and now crisis-terminal flags.

No global event target is introduced by this decision map.

No free-unit, equipment-farming, political-power, core-spam, war-goal-spam, or local cooldown-bypass loop was found in scope.

## Meaningful validation

Static route-contract validation confirmed ten route availability gates, ten matching government-selection calls, and zero remaining already-selected shared-route predicates in the Iberian decision and installer files.

Static mission-lifecycle validation confirmed both founding missions exclude both terminal flags and the two package cleanup helpers clear all four terminal flags.

Static localisation validation confirmed all direct decision IDs and all six custom-cost text keys resolve, while the Iberian localisation file retains its UTF-8 BOM.

The source scan found zero `add_political_power`, `create_unit`, or `add_equipment_to_stockpile` tokens in the Iberian decision and package-effect surfaces.

No scripted GUI inspection or rendering was applicable because this scope has no decision-owned GUI surface.

Live game validation and full AI scenario execution were not run because they are user-owned and outside this subagent audit.

## Simplifications, omissions, and blockers

No unapproved fallback or simplification was used.

The two low-severity design follow-ups above remain intentionally unpatched because they affect shared duration/balance interpretation or cross-package founding-mission policy beyond this narrow Iberian repair.

## Skills used

`hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` guided the audit, lifecycle checks, current-state evidence, and handoff format.
