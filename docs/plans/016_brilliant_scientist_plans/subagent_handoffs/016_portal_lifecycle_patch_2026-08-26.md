# Event 016 Portal Warfare lifecycle audit

Date: 2026-08-26

Scope: `common/raids/016_brilliant_scientist_portal_raids.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`, the Portal Warfare category and localisation, and the accepted Event 016 plans and handoffs.

## Disposition

No gameplay cleanup or expiry patch is justified by the accepted plan at this point.

A small adjacent localisation correction was safe and was applied to the two existing Portal cost tooltips so their spendable values use the registered texticons.

The accepted native-raid architecture makes the HOI4 raid engine the owner of preparation, equipment reservation, cancellation, expiry, outcome selection, collection, and native raid history, while the Event 016 effects resolve the post-outcome landing, extraction, damage, and persistent bookkeeping.

The open state-marker lifecycle is explicitly deferred to a later Portal beachhead, spread, or containment owner in the existing Event 016 audits.

Adding a generic timer or immediate cleanup here would choose an unaccepted mechanic and could erase state evidence before the later owner consumes it.

## Issue list sorted by severity

### P0/P1: no current critical or high-severity lifecycle defect found

Successful and critical outcomes use `division_effects = { destroy_unit = yes }` before the fixed-template reconstruction in `brilliant_scientist_portal_raid_establish_beachhead`.

Extraction removes the selected source building before transferring one level to an eligible destination, so the audited path does not create a repeatable free-unit, free-equipment, or duplicate-installation loop.

### P2: post-outcome state markers have no assigned cleanup consumer

`brilliant_scientist_portal_beachhead_active`, `brilliant_scientist_portal_raid_breach_recorded`, and `brilliant_scientist_portal_raid_targeted` are written by `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` and have no consumer that clears or transitions them.

`brilliant_scientist_portal_facility_extracted` and `brilliant_scientist_portal_factory_extracted` are also written as state markers without a defined expiry or terminal-state policy.

This is a real ownership gap, but it is not an immediate duplication exploit and the accepted 2026-08-10 and 2026-08-25 audits explicitly leave the cleanup decision to later containment or spread work.

### P3: known design decisions remain open and are outside this narrow patch

The unit requirement is `portal_raider = { min = 6 }`, while the locked reconstruction template contains six battalions; the accepted audit leaves the policy for larger custom formations open.

The exact-facility raid requires an eligible owned destination with all four special-facility families below one, which is conservative but intentional in the current source and not a lifecycle fix.

The full replacement-factor balance and live native raid outcome distribution still require parent review and engine evidence.

The explicit Portal cost prose was a low-risk presentation defect and is resolved in `localisation/english/chaosx_raids_l_english.yml` without changing the native cost fields.

## Accepted-plan and source evidence

`docs/events/016_brilliant_scientist/systems/portal_raider_api.md` states that native raids own preparation, reservation, cancellation, expiry, outcome selection, and raid history, and that success consumes the assigned formation before reconstructing the standard six-battalion formation in the captured province.

`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_raid_decision_mission_audit_2026-08-10.md` records the free-unit fix and identifies the persistent beachhead, breach, targeted, and extraction flags as an unresolved later-lifecycle issue.

`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_plague_completion_audit_2026-08-10.md` recommends that the later containment or spread owner define explicit clearing if persistence is not intentional and says that no broad cleanup system was accepted.

`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_decision_audit_2026-08-25.md` repeats that the flags have no bounded cleanup consumer, that this is not an immediate duplication exploit, and that no broad cleanup system was added.

`docs/plans/016_brilliant_scientist_plans/016_krg_hazardous_mission_pressure_accepted_plan.md` defines `brilliant_scientist_krg_transit_breach_closure_mission` as a separate KRG objective whose success requires an operational route and controlled terminal; it does not authorize clearing the native raid state markers.

## Decision category lifecycle notes

The category is `brilliant_scientist_raids` in `common/raids/categories/chaosx_raid_categories.txt`.

The category is visible behind `brilliant_scientist_portal_warfare_weaponization_tech`, uses free targeting, and exposes two primary native raid types: `brilliant_scientist_portal_facility_raid` and `brilliant_scientist_portal_special_project_facility_raid`.

Both types use seven preparation days, a thirty-day same-type target re-enable timer, ten Command Power, and sixty `teleportation_equipment` as the reserved essential equipment.

Both types have a `cancel_trigger` that rechecks actor readiness and target validity while the raid is preparing.

That native cancellation path is not a valid post-outcome cleanup hook because the state flags are written only after a success or critical success has resolved.

The thirty-day `days_re_enable` value is a native raid target cooldown and must not be treated as an expiry policy for a captured beachhead or historical extraction marker.

No scripted mission owns Portal Warfare; the two operations are native raids with native preparation, cancellation, expiry, and history behavior.

## Cognitive-load notes

There are two visible primary actions in the category, below the six-action limit.

There are no scripted active missions in this Portal Warfare surface, so there is no simultaneous-mission overload to resolve here.

The category tooltip communicates the seven-day preparation, six-battalion minimum, sixty-equipment reservation, ten Command Power cost, and six-battalion reconstruction.

The two raid descriptions communicate the target class, beachhead behavior, one-installation success, and additional critical extraction.

The persistent state markers are hidden script state rather than raw player-facing numeric rows, and there is no decision-owned custom GUI in this scope.

Every currently displayed mechanic value has a stated consequence or response in the category and raid tooltips; adding a cleanup timer to the tooltip without an accepted lifecycle would be misleading.

## Mission quality notes

Portal Warfare is a native raid surface rather than a scripted mission surface.

| Raid | Owner and category | Target and region | Requirement | Duration and cooldown | Outcomes | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `brilliant_scientist_portal_facility_raid` | Attacking country in `brilliant_scientist_raids` | Hostile controlled state with an eligible factory, dockyard, reactor, or rocket installation | Portal Warfare weaponization technology, a formation with at least six `portal_raider` battalions, sixty `teleportation_equipment`, ten Command Power, and a valid supply-node start | Seven preparation days and thirty-day target re-enable | Failure, limited success, success, and critical success are resolved by native raid success levels | The selected division is destroyed on success or critical success before one fixed-template beachhead reconstruction |
| `brilliant_scientist_portal_special_project_facility_raid` | Attacking country in `brilliant_scientist_raids` | Hostile controlled province containing a tagged special-project facility and an eligible owned destination | The same technology, formation, equipment, Command Power, and supply-node requirements, plus exact facility and destination checks | Seven preparation days and thirty-day target re-enable | Failure, limited success, success, and critical success are resolved by native raid success levels | Exact source removal and one-level destination transfer prevent repeated extraction of the same building |

The native raid engine owns preparation, timeout or expiry, cancellation, and success-history behavior; the Event 016 effects own only the post-outcome consequences listed above.

## Cost and requirement clarity

Each Portal raid has two distinct spendable cost types: ten Command Power and sixty Teleportation Equipment.

The source uses `command_power = @CR_SC_PORTAL_RAID_COMMAND_POWER` and `essential_equipment = { teleportation_equipment = @CR_SC_PORTAL_RAID_EQUIPMENT_RESERVATION }`.

The category and preparation tooltip now use `£command_power` and `£teleportation_equipment_1_text_icon` for the two spendable values, while the native raid UI owns the actual cost rendering and reservation presentation.

No custom cost string introduces a third, fourth, or hidden fifth spendable type, and the two existing explanatory cost strings no longer spell out spendable resource names without icons.

Non-consumed requirements are separated into technology, formation, target, war, and supply-node checks rather than being mixed into a cost block.

## AI validity and route-lock notes

`brilliant_scientist_portal_raid_actor_is_ready` requires the Portal Warfare weaponization technology and the locked `Quantum Transit Raiders` template.

The state-target trigger requires an existing actor, a war with the target, target ownership and control by the defender, and at least one eligible state installation.

The exact-facility trigger requires the same war and control relationship, a tagged facility in the selected province, and a controlled owned destination with capacity for the special-facility transfer.

The native `available`, `launchable`, and `cancel_trigger` blocks call those readiness and target triggers, so invalid countries, closed routes, dead targets, and impossible borders are rejected at the source level audited here.

The AI uses the Portal base constant and factors for Kruger state, Kruger presence, major target, capital target, and strategic-facility target, with a zero factor for invalid readiness or target conditions.

The required `chaosx_ai_probability_auditor` route is not present in the callable tool inventory, and the direct probability inspection attempt against `common/raids/016_brilliant_scientist_portal_raids.txt` returned an `INTERNAL_ERROR` with `Unexpected internal error` and `artifactCount: 0`.

The latest available historical audit artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7f74f4d0070ec15cb8d64f7f2502e73c739877ef99f163fc92e8afcb2fff7f4/b4df7143e0b7126b39fb8fe723c2922df18504c1181cb210d169ed3e3ffce0d4/probability-inspect-653eee865c1c.json`, which reported no weighted surfaces and no candidates; it is historical evidence, not a fresh compare for this audit.

## Localisation and tooltip gaps

The Portal category, both raid names and descriptions, the target labels, preparation and launch requirements, and all four result tooltips are present in `localisation/english/chaosx_raids_l_english.yml`.

The wording matches the current seven-day, sixty-equipment, ten-Command-Power, six-battalion, beachhead, extraction, and critical-outcome behavior, and the two spendable values use the existing texticons.

There is no accepted cleanup or containment timer to describe, so no lifecycle localisation was added.

## Cleanup and exploit-risk notes

Country history flags and counters such as `brilliant_scientist_portal_raid_success_ever`, `brilliant_scientist_portal_raid_critical_success_ever`, `brilliant_scientist_portal_beachhead_established_ever`, `brilliant_scientist_portal_installation_extraction_ever`, and their counters must remain persistent for later intelligence, achievements, rebellion, and aftermath consumers.

The state markers `brilliant_scientist_portal_beachhead_active`, `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` currently have no assigned clear, expiry, or transition consumer.

Clearing them immediately after the native outcome would remove the only active beachhead signal before later containment or spread code can react.

Giving them an arbitrary timed duration would create an unapproved balance rule and would not define what happens when the controller, actor, province, or surrounding state changes.

Clearing them from `cancel_trigger` would be incorrect because `cancel_trigger` applies to the in-flight native raid and does not run after a successful outcome.

No whole-world polling or broad state scan was added because no owner, terminal condition, target registry, or bounded cadence is accepted for that work.

## Recommended follow-up fixes

The future Portal beachhead or containment owner should first update the accepted Event 016 spec with the active-beachhead owner, expiry condition, controller-change behavior, and terminal cleanup event or decision.

That owner should distinguish the transient `brilliant_scientist_portal_beachhead_active` marker from permanent historical evidence such as `brilliant_scientist_portal_raid_breach_recorded` and the country `*_ever` flags.

After that policy is accepted, add a state-scoped cleanup trigger in `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt` and an idempotent cleanup effect in `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, then wire it only from the actual containment, spread, or terminal consumer.

The cleanup effect must not call `create_unit`, refund equipment, repeat extraction, or clear native raid history, and it must preserve the one-for-one formation reconstruction contract.

Do not use `days_re_enable` as the beachhead expiry and do not attach cleanup to native raid cancellation.

## Changed files and behavior

Changed files: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_lifecycle_patch_2026-08-26.md` and `localisation/english/chaosx_raids_l_english.yml`.

No gameplay source file, decision, mission, raid type, scripted GUI, localisation key identifier, AI weight, or native history behavior was changed.

Before and after gameplay behavior is identical: successful and critical Portal raids still destroy the selected formation, reconstruct one standard beachhead formation, transfer the accepted installation result, and retain native raid history and Event 016 persistent history.

Before the adjacent localisation correction, the category and preparation tooltips displayed `sixty Teleportation Equipment` and `ten Command Power` as literal prose; afterward they display the same values with `£teleportation_equipment_1_text_icon` and `£command_power`.

## Validation and blockers

I read the required offline wiki pages and the vanilla raid documentation, including the native land-infiltration precedent for state flags, `cancel_trigger`, `add_raid_history_entry`, and explicit `clr_state_flag` cleanup.

A repository-wide `rg` consumer scan found the five state-marker families only being written in `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` and not being cleared or consumed elsewhere.

Targeted source inspection confirmed both success paths use `destroy_unit = yes`, both raid types revalidate readiness and targets, and both use the two-cost native reservation contract.

The corrected localisation retains the UTF-8 BOM and resolves the existing `teleportation_equipment_1_text_icon` and `command_power` texticon keys.

The HOI4 MCP tool inventory has no raid-specific inspect or render route, and the direct probability inspection returned the exact internal-error blocker recorded above.

No GUI inspect or render was run because Portal Warfare is a native raid category with no decision-owned or custom scripted GUI in this scope.

No native game launch or live playtest was performed, per task constraints.

Skipped validation: native raid-engine inspection, probability compare through `chaosx_ai_probability_auditor`, and live outcome testing remain blocked by unavailable MCP routes and the no-game-launch constraint.

## Remaining risks

The state-marker lifecycle remains incomplete until a later accepted owner defines whether active beachheads expire, are closed by a mission or decision, or remain permanent evidence.

The larger-than-six formation policy, exact-facility destination restriction, full AI factor balance, and live native outcome distribution remain parent-review items from the prior audits.

No simplification or fallback was introduced; the unresolved cleanup system is intentionally left unimplemented pending an accepted lifecycle specification.

Plan handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_lifecycle_patch_2026-08-26.md`.
