# Event 023 reactor entitlement and construction architecture handoff

Historical status notice: The implementation status below predates the 2026-09-19 country-to-state scope repair in `sov_nuclear_bombs_verify_pending_reactor_construction`. The repair is present in current source, but native queue identity/cancellation and entitlement behavior remain unresolved as recorded in `023_documentation_curator_final_2026-09-19.md`.

Status: implemented and reconciled by the parent. The parent added the dedicated event-driven completion entry point and integrated the bounded native reactor queue contract. Live construction completion and save/reload remain user-owned validation surfaces.

## Scope and decision

This handoff covers only the reactor entitlement, state placement, pending construction, and verified completion boundary for Event 023 SOV nuclear bombs.

The parent subsequently changed the Event 023 event, decision, trigger, effect, runtime, constants, on-action, localisation, and asset-wiring surfaces. This handoff records the architecture and the engine limitation that still applies; it is no longer a design-only blocker.

The implementation keeps the existing ledger and native stockpile path separate from reactor entitlement. State flags plus one global event target mark the pending construction state, while verified `nuclear_reactor > 0` completion is the only boundary that increments the event-owned reactor count.

The parent added hidden event `chaosx.nr23.181`, bounded rechecks at the named completion interval, pending-state invalidation on control loss, and cleanup on actor teardown. The installed vanilla documentation exposes no effect that cancels an ordinary pending building-construction job, so cancellation is implemented as fail-closed Event 23 marker cleanup; the native queue itself is not falsely reported as removed.

## Evidence inspected

The following Event 023 sources were inspected in their current worktree state.

- common/script_constants/023_sov_nuclear_bombs_constants.txt
- events/023_soviet_nukes.txt
- common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt
- common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt
- common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt
- common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt
- common/scripted_effects/005_soviet_collapse_effects.txt
- common/on_actions/005_soviet_collapse_on_actions.txt
- common/scripted_effects/032_missiles_operations_effects.txt
- common/decisions/023_sov_nuclear_bombs_decisions.txt
- common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md
- docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_2_arsenal_command_and_production.md
- docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_5_evolutions_and_exchange.md

The required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and building modding.

The relevant vanilla documentation was consulted in C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation, including effects_documentation.md, triggers_documentation.md, dynamic_variables_documentation.md, script_concept_documentation.md, and common/script_constants/documentation.md.

The vanilla building precedent in C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/buildings/00_buildings.txt defines nuclear_reactor with level_cap state_max = 1.

The vanilla effect documentation confirms that add_building_construction is a STATE effect with type, level, and instant_build fields, but exposes no construction-job identity or completion callback.

The vanilla trigger documentation confirms building_count_trigger for nuclear_reactor, can_construct_building in STATE scope, free_building_slots in STATE scope, and dynamic building_level@nuclear_reactor values.

The Event 005 custody pattern was compared with the planned inheritance flow in common/scripted_effects/032_missiles_operations_effects.txt, especially the prepare, exact post-transfer verification, finalize, and explicit unresolved cleanup phases.

## MCP inspection evidence

The read-only HOI4 event inspection and rendering routes were used before designing this boundary.

- Workspace: mod_chaos_redux_ea3b2d67c2c0.
- Event scan and trace revision: 3d4d1503eea170d5726ebd4bc8d78f7284ec53439d7e518957fff586d3ed1741.
- Event state render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9b9b98bd3a2adaa94f4c01603b86fe1a83b03dd8c817b175c069cc45f4f1725/7763dbb13f72387343d21b6d2ba147b23cba5416837df83c566c15b55c41f0f2/event-state-649693da253f.json.
- Event target render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1d57083ff77d149a182106ba887f5fcbb7c0dffdaeeeeecc8ef2eeced62eb68/1273a058ee95901593413c8b3721a18299d4fee344ed54bac4216d2f8992ce54/event-targets-649693da253f.json.
- Event source lint artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/681d7d135c23a634b9bcbc129a28553ed8b91a1f4c8f7f7bc7423ce575d14789/b278280f1dccf5337da604fd9a0610b2fc2cbc72d19a48fb4eef1d17d3e16657/event-lint-3d4d1503eea1.json.
- Event trace artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1c6d7b28ea3583c43be7c62a1dc24f7dc9c9028979ea37f15a2633ec8e6e2cf/4f3a897142aafbb41169dcdbffbfd9c57285fad3f3e7e0c8db5e05d36b582615/event-trace-3d4d1503eea1.json.

The MCP routes returned EVENT_INSPECTED_PARTIAL and EVENT_RENDERED_PARTIAL because the large workspace analysis deferred workspace-wide helper and lifecycle projections and truncated the inline file inventory. The returned evidence still exposed the Event 023 state, target, and source-lint surfaces, but it is not a clean workspace-wide validation pass.

The probability inspection and AI probability auditor were intentionally not run because this design changes no AI weight, score, MTTH, random-list weight, or other probability-bearing surface.

## Current Event 023 findings

The current constants already use one reactor level per placement through sov_nuclear_bombs_tuning.reactor_levels_per_stage = 1 and sov_nuclear_bombs_tuning.production_reactor_level = 1.

The evolution constants correctly express the target ladder of 2, 4, 6, and 8 reactors, but the target must remain separate from verified completion.

sov_nuclear_bombs_initialize_event_state currently initializes sov_nuclear_bombs_reactor_count and then assigns it to the opening target before any building completion check.

sov_nuclear_bombs_record_opening_evolutions currently issues repeated capital-scope add_building_construction calls, including multiple calls against the same state when the opening stage reaches the higher tiers.

sov_nuclear_bombs_expand_reactor_program currently queues one nuclear_reactor level in the selected state and immediately increments reactor_count, marks entitlement consumed, and applies production completion effects without a later building check.

sov_nuclear_bombs_event_has_reactor_entitlement and sov_nuclear_bombs_event_no_active_project already refer to sov_nuclear_bombs_reactor_construction_pending, but the current reactor production path does not establish a per-state pending marker or a global pending-state target.

Event 023.180 is an evolution timing pulse that clears sov_nuclear_bombs_evolution_timing_active before calling sov_nuclear_bombs_try_evolution_progression. It should not also be used as the reactor completion callback unless the parent deliberately redesigns the timing state machine.

The Event 005 runtime bridge snapshots and reconciles the registered bomb-device ledger around ownership changes. It does not identify or reconcile Event 023 reactor construction jobs, and it must not be modified by this bounded change.

## Proposed helper map

The helpers should be added to the existing Event 023 event trigger and effect files when the parent is ready to integrate them. A separate helper file is unnecessary unless the parent chooses to isolate the reactor boundary and also supplies the required helper documentation.

| Identifier | Scope | Inputs | Outputs | Side effects | Intended call sites |
| --- | --- | --- | --- | --- | --- |
| sov_nuclear_bombs_event_state_is_valid_reactor_site | STATE | ROOT country and current state | true only for a safe one-level site | Reads ownership, control, state flags, building level, construction capacity, and construction eligibility | Decision target and availability integration, opening placement selector, production queue effect |
| sov_nuclear_bombs_event_has_pending_reactor_construction | COUNTRY | Event actor | true when the country-level pending marker exists | Read-only | Completion event trigger and existing no-active-project gates |
| sov_nuclear_bombs_state_has_pending_reactor_completion | STATE | Current state | true when the state marker exists and nuclear_reactor is completed | Read-only | Bounded completion scan and exact control-change integration |
| sov_nuclear_bombs_event_pending_reactor_completion_is_valid | COUNTRY | Global pending state target | true only when the selected production state still belongs to ROOT, retains its pending marker, and has nuclear_reactor above zero | Read-only | Dedicated completion event and production completion branch |
| sov_nuclear_bombs_mark_reactor_construction_pending | STATE | One eligible state and one entitlement unit | Queued one-level reactor construction | Sets state pending marker, sets country pending marker, and queues one non-instant reactor level | Production effect and opening queue effect |
| sov_nuclear_bombs_queue_opening_reactors | COUNTRY | reactor_entitlement_count and reactor_count | Queues at most the target minus verified completed placements | Selects distinct eligible states, sets per-state pending markers, and leaves unmet target represented by the entitlement gap | Event initialization and later retry after a failed or unavailable placement |
| sov_nuclear_bombs_register_completed_reactor | STATE | A state with the Event 023 pending marker and nuclear_reactor above zero | One verified event-owned completed placement | Increments reactor_count once if the target still permits it, sets provenance, clears the pending marker, and preserves the ledger and stockpile | Production completion and opening completion scan |
| sov_nuclear_bombs_verify_pending_reactor_construction | COUNTRY | Pending production target plus opening pending states | Verified completion, explicit wait, or explicit invalidation | Completes or clears markers, clears global target when resolved, and applies production completion effects only after verification | Dedicated hidden reactor completion event |

The state-site trigger should use the documented dynamic building level and centralized state cap, together with the normal construction guards.

~~~text
sov_nuclear_bombs_event_state_is_valid_reactor_site = {
	exists = yes
	impassable = no
	is_owned_by = ROOT
	is_controlled_by = ROOT
	NOT = {
		has_state_flag = sov_nuclear_bombs_site_missing
	}
	NOT = {
		has_state_flag = sov_nuclear_bombs_reactor_site_pending
	}
	check_variable = {
		var = building_level@nuclear_reactor
		value = constant:sov_nuclear_bombs_tuning.reactor_state_max
		compare = less_than
	}
	can_construct_building = nuclear_reactor
	free_building_slots = {
		building = nuclear_reactor
		size > 0
		include_locked = no
	}
}
~~~

The parent should retain the direct nuclear_reactor building-count guard as a second fail-closed check if the current parser or MCP lint treats the dynamic building level differently in a scripted trigger. The documented direct form is nuclear_reactor < 1, and the literal one represents the vanilla state cap rather than a balance value.

The queue effect must run in STATE scope and must never use instant_build for this path.

The completion registration effect must be idempotent by requiring sov_nuclear_bombs_reactor_site_pending and nuclear_reactor above zero before changing reactor_count.

## Variable, flag, and event-target contract

| Name | Kind | Meaning | Lifecycle |
| --- | --- | --- | --- |
| sov_nuclear_bombs_reactor_count | Country variable | Verified completed Event 023-owned placements only | Initialize to zero, increment only from register_completed_reactor, and never increment when construction is queued |
| sov_nuclear_bombs_reactor_entitlement_count | Country variable | Target number of Event 023 reactor placements requested by the opening or evolution ladder | Set to 0, 2, 4, 6, or 8; it is not proof of a completed building |
| sov_nuclear_bombs_reactor_construction_pending | Country flag | At least one Event 023 construction or unresolved reactor placement still needs a completion check | Set when a construction is queued or an unmet target is intentionally retained; clear only after bounded verification confirms no pending state and no unresolved target |
| sov_nuclear_bombs_reactor_site_pending | State flag | This state has one Event 023 reactor placement awaiting verification | Set before the queue effect, which prevents a second queue in the same state; clear on verified completion or explicit invalidation |
| sov_nuclear_bombs_reactor_event_owned | State flag | This completed reactor placement belongs to the Event 023 package for accounting purposes | Set only after nuclear_reactor above zero is verified together with the pending marker |
| sov_nuclear_bombs_pending_reactor_state | Global event target | The one selected production state whose queued construction must be checked later | Save when production queues; clear on verified completion, invalidation, actor teardown, or terminal cleanup |
| sov_nuclear_bombs_reactor_production_completion_pending | Country flag | Optional discriminator for applying production completion rewards once | Set with the production target and clear only in the verified completion or invalidation branch |

The existing sov_nuclear_bombs_reactor_entitlement_consumed flag must not be used as the queue marker. It should be set only after the selected production state passes the later completion check.

The selected production state must be copied to sov_nuclear_bombs_pending_reactor_state before any cleanup clears sov_nuclear_bombs_selected_state.

Global target cleanup is mandatory on verified completion, state loss before completion, actor annexation or terminal collapse, and any explicit cancellation path. A missing target must never be treated as a completed reactor.

## Opening ladder algorithm

Initialization must set reactor_count to zero and set reactor_entitlement_count from the opening stage target.

The opening effect must not assign reactor_count to the target and must not use repeated capital-scope construction calls.

sov_nuclear_bombs_queue_opening_reactors should compute the outstanding target from reactor_entitlement_count minus reactor_count, then run a bounded loop whose body selects one random owned and controlled eligible state.

Each selected state must pass sov_nuclear_bombs_event_state_is_valid_reactor_site, receive one level of non-instant nuclear_reactor construction, and receive sov_nuclear_bombs_reactor_site_pending before the next loop iteration.

The pending flag makes a state ineligible for the next iteration, so the opening ladder cannot queue a second level in the same state even while the first construction is unfinished.

If enough distinct states exist, targets 2, 4, 6, and 8 produce one queued level per state.

If fewer eligible states exist, the helper stops after the available states are marked and leaves reactor_entitlement_count above reactor_count. That gap is the represented pending entitlement and must not be converted into completed reactors, factories, readiness, or production capacity.

The dedicated completion event may retry the outstanding entitlement with the same bounded state selection when a later state becomes eligible, but it must use an event delay and must not become an on_daily, on_weekly, or on_monthly whole-world loop.

Evolution stage flags and target metadata may still advance according to the existing Event 023 design, but any text or effect that claims completed reactor capacity must use the verified reactor_count boundary.

## Production migration sequence

The parent should change the production path in this order without changing the ledger or stockpile effects.

1. The decision target and availability filters must use the same one-level site trigger and reject states carrying sov_nuclear_bombs_reactor_site_pending.
2. The production effect must verify the selected state in STATE scope immediately before queuing.
3. The effect must save the selected state as sov_nuclear_bombs_pending_reactor_state.
4. The effect must set sov_nuclear_bombs_reactor_site_pending and sov_nuclear_bombs_reactor_construction_pending.
5. The effect must queue exactly production_reactor_level, which is currently one, without instant_build.
6. The effect must not increment reactor_count, set entitlement consumed, or apply completion readiness and integrity rewards at queue time.
7. The effect must schedule the dedicated hidden completion event through a bounded event chain.
8. The completion event must leave the marker and target intact while the state remains valid but nuclear_reactor is still zero.
9. The completion event must call sov_nuclear_bombs_register_completed_reactor only after the state has nuclear_reactor above zero and still has the Event 023 pending marker.
10. Only the verified production branch may clear sov_nuclear_bombs_reactor_production_completion_pending, set entitlement consumed, apply production-complete rewards, and clear sov_nuclear_bombs_pending_reactor_state.
11. If the state is lost, invalidated, or the target disappears before completion, the event must clear the state marker, country pending marker when no other work remains, and global target while leaving the entitlement target unchanged and applying no completion reward.

The existing stockpile and runtime device registration effects remain outside this migration. They must be called exactly as they are today after the reactor completion boundary where applicable.

## Required parent event integration

Add a dedicated hidden event such as chaosx.nr23.181 in events/023_soviet_nukes.txt.

The event should be actor-scoped and is_triggered_only, require the valid Event 023 actor and the pending reactor marker or unresolved entitlement gap, call sov_nuclear_bombs_verify_pending_reactor_construction, and schedule itself again after a named verification interval only when unresolved work remains.

The parent should not reuse chaosx.nr23.180 while sov_nuclear_bombs_evolution_timing_active can be set, because the two systems would then share one event pulse and could clear or consume each other's timing state.

Add a named duration constant such as sov_nuclear_bombs_duration.reactor_completion_check_days = 30, or explicitly reuse the existing verification duration if the parent confirms that both meanings are intentionally identical.

The existing decision file needs the parent-owned target and available integration described above. This handoff does not patch it.

## Event 005 custody and cleanup integration

The Event 005 snapshot and reconciliation bridge must remain unchanged for the bomb-device ledger.

The reactor state marker should follow the same prepare, exact verification, and explicit cleanup discipline used by missiles_prepare_planned_inheritance and missiles_finalize_planned_inheritance.

When a pending reactor state changes control before completion, the exact state callback should invalidate the pending construction marker and global target, preserve the entitlement target, and avoid changing reactor_count.

When a completed Event 023 reactor state changes hands, the parent must resolve whether reactor_count is historical completed placement count or current SOV-controlled capacity.

The safest accounting contract for this task is that reactor_count means verified completed Event 023-owned placements and is never increased by entitlement alone.

If production capacity must fall when a completed site leaves SOV control, the parent should either introduce a separately reconciled operational reactor count or add an exact state-control reconciliation that removes the completed-site contribution. It must not silently decrement reactor_count from a broad world scan.

Any control-change integration must be bounded to the changed state through an existing state-control callback or an explicitly parent-owned event path. Do not add a whole-world daily, weekly, or monthly scan.

Annexation, terminal collapse, and actor teardown must clear sov_nuclear_bombs_pending_reactor_state and all unresolved reactor construction markers belonging to the actor.

## Constants and tuning plan

Keep sov_nuclear_bombs_tuning.reactor_levels_per_stage at one and sov_nuclear_bombs_tuning.production_reactor_level at one.

Add sov_nuclear_bombs_tuning.reactor_state_max = 1 if the dynamic building-level trigger is retained. This mirrors the vanilla state cap and is a guard, not a second building-definition limit.

Keep sov_nuclear_bombs_tuning.reactor_building_limit = 8 as the Event 023 national target ceiling only if a call site uses it. Otherwise the parent should remove or document its intended use rather than leaving an unused tuning value.

Keep the existing evolution target constants for 2, 4, 6, and 8.

Add a named reactor completion verification duration rather than embedding a new timing literal in an event.

No AI, MTTH, random weight, or score tuning changes are proposed.

## Migration plan

First add the state eligibility trigger and the idempotent completion registration helper to the existing Event 023 helper files.

Then replace the initialization assignment that treats the opening target as completed count with zero-count initialization plus entitlement target initialization.

Then replace repeated capital construction with the distinct-state opening queue helper.

Then convert production from immediate completion to pending state target plus one-level non-instant construction.

Then add the dedicated hidden completion event and call the verifier until it resolves or explicitly invalidates the target.

Then update the parent-owned decision filters and any production/readiness consumer that currently assumes reactor_count is immediately available.

Finally add exact state-control and actor-teardown cleanup integration and run the Event 023 MCP inspection again after all parent-owned files are wired.

## Risks and unsupported analysis

Vanilla documentation exposes no construction-job identity, so a later check can prove that the selected state has nuclear_reactor above zero but cannot prove that the completed building came from the specific queued job if the player cancels it and builds a reactor manually in the same state.

The state pending flag is therefore the best available Event 023 ownership marker and must be cleared on every success and invalidation path.

can_construct_building alone does not prove that the state has no existing reactor or no Event 023 construction already queued, so the building-level guard and per-state pending flag are both required.

nuclear_reactor shares construction slots and is state-only, so add_building_construction must remain in STATE scope.

The current Event 005 on_state_control_changed path only recognizes event5 snapshot markers and has no reactor-specific callback. Full exact reactor custody reconciliation therefore requires a parent-owned integration outside this bounded handoff.

The MCP inspection was partial at workspace scale, so helper projection and lifecycle diagnostics were not available as a complete engine-backed proof.

No game launch or live consumer test was performed, as live HOI4 validation belongs to the user.

## Validation performed

The Event 023 read-only MCP event scan, downstream trace, state render, target render, and source lint routes were run before this design was written.

The available MCP result was partial rather than a clean pass because the workspace-wide analysis deferred helper and lifecycle projections and truncated inline files.

The vanilla documentation and the existing Event 005 and missile custody patterns were inspected for the construction, state-cap, event-target, and cleanup assumptions used here.

No helper syntax validation is claimed because no helper source was added.

## Files changed

- docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_reactor_architect.md

No gameplay file, helper file, shared runtime file, decision file, event file, localisation file, GFX file, workbook, generated agent file, or shared on_action file was changed.

## Parent integration checklist

- Keep nuclear_reactor state_max at one in the vanilla-compatible building definition.
- Keep one queued level per state and reject a state with an existing level or pending Event 023 marker.
- Treat reactor_entitlement_count as a target and reactor_count as verified completed placements.
- Do not credit reactor_count, entitlement consumption, production capacity, readiness, or completion rewards at queue time.
- Add the dedicated event-driven completion check and bounded retry path.
- Preserve the runtime ledger and native stockpile registration exactly.
- Reconcile pending and completed reactor markers on exact state-control changes and actor teardown.
- Re-run the Event 023 MCP inspection after parent integration and carry forward any partial or unsupported result.
