# Missile region lookup contract

This document covers `missiles_assign_site_strategic_region` in `032_missiles_effects.txt`.
The operation and succession contracts remain in [missile operations](032_missiles_operations_effects.md).

## `missiles_assign_site_strategic_region`

Purpose: cache a site's strategic region using the existing bounded selector probe.
Scope: STATE with a live actual controller, reached through a country-to-state call whose program country controls that state.
Inputs: the current state and its native `controller`, with the unchanged `missiles_map.first_strategic_region` and `missiles_map.maximum_strategic_region` constants defining the existing search range.
Outputs: normal STATE variable `missiles_site_strategic_region`, assigned the discovered region or the existing zero result if the selector does not match within the configured range.
Defaults: an existing region cache bypasses all probe work, including event-target capture and country scratch mutation.
No new parameter or caller-owned temporary output is required.

The helper saves its input state as regular `missiles_region_probe_state`, records its actual controller as regular `missiles_region_probe_country`, then enters that exact country before the nested `any_state_in` STATE query.
Country scratch consists of `missiles_region_probe_states`, `missiles_region_probe_found` and `missiles_region_probe_found_id`.
The query's membership test and the final state result read use the named country target rather than event ROOT or an assumed PREV nesting.
The loop index `missiles_region_probe_id` and break value `missiles_region_probe_break` are unscoped temporaries consumed within this helper.
No native state, owner, controller, province or strategic-region membership is changed.

Side effects and cleanup: on an uncached state, the controller's scratch array is initialized for that exact state and emptied afterwards, and both normal scratch scalars are removed before return.
The two regular targets expire with the originating chain and are rebound on each uncached invocation.
No global target or persistent country pointer is created.
As before, these scratch names are private to this synchronous helper and must not contain caller-owned data on its actual controller.

## Direct caller contract

`missiles_score_site_candidate` reaches the probe from `missiles_select_best_site` over the program's owned states restricted to those controlled by the program ROOT.
`missiles_register_site` proves both ownership and control by its program ROOT before probing the registration state.
`missiles_recalculate_network` runs in the actual program COUNTRY and probes only its native `every_controlled_state` members, including occupied sites whose legal owner differs from the program and excluding foreign-controlled stale registry entries.
For all three callers, the actual controller recorded by the probe is therefore the proven program country.
This binds a claimant program correctly when the originating event ROOT is the reviewing government, and also binds the program country under foreign-root lifecycle callbacks such as `on_war_relation_added` on FROM.
The other ROOT-dependent scoring and site-registration commands retain their existing owner contracts and are outside this lookup repair.

Example: call `missiles_recalculate_network = yes` inside the recorded claimant COUNTRY while the government remains ROOT.
For every eligible uncached controlled site, the probe uses the site's current claimant controller, caches the region on that state, and leaves the government's missile records untouched.
A stored historical controller pointer or the site's legal owner is not substituted for actual native control.

## Validation and limits

The claimant fixture `.tools/test_event021_claimant_missile_scope.py` executes the probe source, its meta-trigger replacement, the bounded loop and region membership test, with explicit fixture memberships as the native map-query boundary.
It retains distinct scoped normal storage and conservative helper-return temporary cleanup, tests uncached claimant sites under government ROOT, foreign ownership, foreign-controlled entries, cached bypass and child/donor settlement.
The probe range, loop, first-match behavior, zero result, and all missile constants remain unchanged.
This is actual-source accounting evidence and does not establish native strategic-region query behavior or engine conservation.
Current references, hashes and unresolved no-child split recovery are recorded in the [Event021 handoff](../../docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_claimant_missile_scope_repair_2026-10-07.md).
