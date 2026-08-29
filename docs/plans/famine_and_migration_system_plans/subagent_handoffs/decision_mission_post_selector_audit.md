# Famine and Migration Post-Selector Decision/Mission Audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded audit complete in the shared worktree. Two local decision-surface fixes and one direct localisation fix were applied. The owner must resolve the semantic and weighted follow-up items below before the shared system can be treated as complete.

## Scope and evidence

The audit covered `common/decisions/famine_migration_decisions.txt`, the owner-added destination selector helpers and triggers, the mission constants and slot contracts, the ordinary category and its compact header scripted GUI, both state mapmodes, the 26-row decision map, and the eight famine/migration specification parts and supporting matrices.

The offline Paradox wiki decision, trigger, effect, modifier, localisation, scope, data-structure, on-action, event, interface, and scripted-GUI pages were read before source review.

Vanilla decision documentation and state-targeted/custom-cost precedents in `BOL`, `BEL`, `COG`, `CHI_decisions`, and `CHI_warlord_decisions` were used for comparison.

The current source has 32 top-level `fm_` blocks: 26 decisions and six non-selectable missions. The decision map CSV also has 26 rows, with no missing or unlisted source identifier.

## Required MCP evidence and blockers

The category registers `famine_migration_report_header_scripted_gui` at `common/decisions/categories/famine_migration_categories.txt:37`, and the scripted GUI owns `famine_migration_report_header_window` at `common/scripted_guis/famine_migration_report_header_scripted_gui.txt:11` and `interface/famine_migration_report_header.gui:14`.

The required read-only `hoi4.gui_inspect` call for `famine_migration_report_header_window` with the `default` scenario timed out after 180 seconds.

The required read-only `hoi4.gui_render` call for the same window, with normal, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720, also timed out after 180 seconds.

The prior owner callback contains inherited, not-current-call, artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9410b7bf900fabf1baa9c56db70787eb3a4e36ffe9f8f7d9badde586efe0f54/b3cbc23f8b96415c4f0a732e65c312f69afe75f72384a5b9e55e153e705c3952/gui-inspect.c159fc5d62130b30.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f19a21bbec4ecdbb9717a41d0a34b45c1cc68bc2bd527f30e4aa725588d37/df9f59d4ecc363ba846230814ce41e9c3fc515eed4bdcb46add8cda63dca69a5/famine_migration_report_header_window-full.svg`.

The mandatory probability route was attempted for `decision_ai_will_do`, `mission_ai_will_do`, and `custom_weighted_pool` against the current decision/helper sources. The decision and custom-pool inspections returned `INTERNAL_ERROR` with zero artifacts, and the mission inspection timed out after 180 seconds.

No `chaosx_ai_probability_auditor` callable route was available in the tool registry, and no probability compare was run. The destination-selection weights are therefore source-reviewed only and remain an owner/probability-auditor follow-up, not engine evidence.

No `hoi4.gui_rewrite` was used because no GUI layout patch was required or authorized.

## Issue list sorted by severity

### High: external relief actions do not all execute external delivery

`fm_escorted_relief_convoy` is described as protected external delivery, but `common/decisions/famine_migration_decisions.txt:1170` calls `famine_migration_release_food_reserves`, which consumes the target state's local reserve.

`fm_emergency_airlift` is described as airlifted external delivery, but `common/decisions/famine_migration_decisions.txt:1265` also calls `famine_migration_release_food_reserves` and therefore consumes local reserves.

`fm_emergency_imports` calls `famine_migration_import_food_reserves` at `common/decisions/famine_migration_decisions.txt:1005`, which is a distinct import adapter but still credits the target reserve without selecting or proving a donor state or external route.

`fm_invite_relief` only subtracts a third of current food pressure at `common/decisions/famine_migration_decisions.txt:1350-1352`; it has no donor, relief-source, route, or delivery transaction.

This is a semantic and balance ownership issue, not a safe local tuning fix. The owner should route convoy and airlift through an explicit external delivery contract, require a proven donor/source for imports, and give invited relief a bounded source/route outcome before changing any weights or pressure fractions.

### High: corridor negotiation is a shallow request without a selected counterpart

`fm_negotiate_corridor` checks `any_other_country` for a valid non-hostile country at `common/decisions/famine_migration_decisions.txt:2026`, but it does not select or persist that country, prove a route, or bind the corridor to a counterpart.

Its completion opens the player's border at `common/decisions/famine_migration_decisions.txt:2059`, while its remove effect simply subtracts one quarter of trapped population at `common/decisions/famine_migration_decisions.txt:2063-2068` and starts the mission when the remaining local conditions permit it.

The localisation promises a valid counterpart and route, so the current surface overstates what the action proves. The owner should add a named counterpart/route contract or revise the design and text together; no broad corridor redesign was made here.

### High before patch, fixed: third-country resettlement checked neighbors at the wrong scope

`fm_third_country_resettlement` had `any_neighbor_state` outside its `FROM` state scope in its `available` block, so a state-targeted action could evaluate the acting country's scope rather than the selected origin state.

The neighbor predicate is now nested under `FROM` at `common/decisions/famine_migration_decisions.txt:2742-2753`, matching the state-targeted precedents and the destination helper's caller contract.

### Medium: airlift AI factor is inverted and remains untouched

`common/decisions/famine_migration_decisions.txt:1250` increases `fm_emergency_airlift` AI weight when `has_air_experience` is below the minimum requirement.

This probability-bearing modifier should be corrected by the decision owner only after a baseline probability audit and the required same-scenario `probability_compare`; it was deliberately not tuned in this audit.

### Medium before patch, fixed: airlift hid a fourth spendable cost

The airlift complete effect consumes political power, five transport aircraft, fuel, and air experience, while its old cost string displayed only political power, fuel, and air experience.

`famine_migration_cost_emergency_airlift` now displays the transport-aircraft icon through `GetFamineMigrationTransportPlanes5Cost`, and the requirement tooltip also uses `£GFX_unit_transport_plane_icon_small`.

### Medium before patch, fixed: worker evacuation hid a non-consumed prerequisite

`fm_evacuate_workers` required support equipment in `available` but did not consume it or explain it in a custom trigger tooltip.

The requirement is now exposed as `famine_migration_evacuate_workers_support_requirement_tt` with the support-equipment texticon at `common/decisions/famine_migration_decisions.txt:1658-1661` and `localisation/english/famine_migration_l_english.yml:92`.

### Medium: active-category cognitive load is above the requested action density

The active phase can expose the relief, movement, border, reception, and resolution-adjacent decisions together whenever their state predicates are true. The source has no explicit phase subcategory or action cap for the active category, so a live crisis can present substantially more than six primary actions.

The six mission rows are non-selectable, but they can be visible alongside the decision wall. The max-three mission contract limits simultaneous active missions, not visible primary decisions.

The compact header displays Food Security, Displacement Load, Reception Capacity, and Border Policy in `localisation/english/famine_migration_l_english.yml:3`. The load value is bound to `famine_migration_reception_load`, and none of these values shows a threshold marker, cause, consequence, or direct recommended response.

The owner should phase or collapse active actions and add concise threshold/action cues before completion. No broad category redesign was made here.

### Low: mission duration ladder is slightly compressed for emergency actions

The constants use 100 days for evacuation protection and 110 days for relief delivery, below the generic medium-mission guideline of 120 days. Their emergency context makes this a design warning rather than a confirmed defect, and no timing was changed.

## Decision map and destination-selector audit

All 26 accepted IDs are present and match the decision map exactly: `fm_release_reserves`, `fm_emergency_imports`, `fm_repair_relief_route`, `fm_escorted_relief_convoy`, `fm_emergency_airlift`, `fm_invite_relief`, `fm_famine_evacuation`, `fm_requisition_safer_state`, `fm_conceal_crisis`, `fm_maintain_extraction`, `fm_prepare_evacuation`, `fm_evacuate_vulnerable`, `fm_evacuate_workers`, `fm_open_departure_routes`, `fm_restrict_departure`, `fm_negotiate_corridor`, `fm_open_reception`, `fm_controlled_medical_reception`, `fm_distribute_arrivals`, `fm_transit_only`, `fm_close_border`, `fm_enforce_closure`, `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation`.

The seven former random-neighbor call sites now use the helpers at `common/decisions/famine_migration_decisions.txt:1423`, `1557`, `1687`, `1826`, `2271`, `2424`, and `2788`. There are no remaining `random_neighbor_state` calls in the decision or destination-selector files.

The helper set is bounded to `every_neighbor_state`, performs a total-weight pass and a draw pass, leaves the destination unbound on a zero total, and writes route, food-safety, reception, border, transport, safety, and actor proof for a selected non-donor destination.

The candidate trigger fails closed for invalid states, food-security danger stages, unsafe routes, persecution, bombing, trapped populations, active camps, chemical contamination, fallout, plague, hostile controllers, inadequate infrastructure, closed or forced-return borders, exhausted reception, and invalid owners.

The owner-added weighted surface is `famine_migration_destination_selection_calculate_candidate_weight`, `famine_migration_destination_selection_run_weighted_pool`, the five `famine_migration_select_*` wrappers, and `famine_migration_destination_selection_weight` in `common/script_constants/famine_migration_destination_selection_constants.txt`. These are probability-bearing changes and were not tuned or compared here.

Exactly two dedicated mapmodes exist: `famine_state_map_mode` at `common/map_modes/chaosx_state_map_modes.txt:390` and `migration_state_map_mode` at `common/map_modes/chaosx_state_map_modes.txt:487`. No third famine/migration mapmode was added.

## Mission lifecycle notes

| Mission | Owner, category, and subject | Requirement and duration | Success/failure and duplicate risk |
| --- | --- | --- | --- |
| `fm_mission_secure_relief_route` | ROOT country; route/relief; one owned and controlled route subject state. | Route subject, success proof, intact route, and deadline; 150 days from `repair_route_timeout`. | Stability on success; stability and war-support loss on timeout; all terminal paths clear subject/proof/deadline and route flag. The route family flag prevents duplicates. |
| `fm_mission_hold_humanitarian_corridor` | ROOT country; trapped-civilian corridor; one state/cohort with a hostile neighboring controller. | Corridor success proof, no remaining trapped population, safe route, hostile-neighbor condition, and 120-day timeout. | Stability and corridor achievement on success; stability and war-support loss on timeout; subject/cohort/flag cleanup is present. The corridor family flag prevents duplicates. |
| `fm_mission_protect_evacuation_transport` | ROOT country; evacuation transport; one state/cohort and deadline. | Evacuation success proof, safe route, and deadline; 100 days. | Stability on success; stability and war-support loss on timeout; subject/cohort/deadline/flag cleanup is present. The evacuation family flag prevents duplicates. |
| `fm_mission_deliver_relief_before_reserves_fail` | ROOT country; relief/reserve delivery; one food state and deadline. | Relief proof, reserve floor, food pressure below success threshold, and deadline; 110 days. | Stability on success; stability and war-support loss on timeout; subject/proof/deadline/flag cleanup is present. The relief family flag prevents duplicates. |
| `fm_mission_prevent_reception_collapse` | ROOT country; receiving state/cohort and observation context. | Reception proof, capacity/load headroom, no overload, no outbreak, and observation deadline; 150 days. | Stability and political power on success; breach/collapse failure records stability, war-support, and achievement failure. Cancel and timeout clean all reception proof and flag state. The reception family flag prevents duplicates. |
| `fm_mission_prepare_safe_return_route` | ROOT country; resolution return route; one return-context state and deadline. | Safe route, no active food-security danger, return context, and deadline; 180 days. | Stability on success; stability and war-support loss on timeout; subject/deadline/flag cleanup is present. The return family flag prevents duplicates. |

All six missions use `visible`, `activation`, `available`, `cancel_trigger`, `cancel_effect`, `days_mission_timeout`, `selectable_mission = no`, `fire_only_once = no`, `complete_effect`, and `timeout_effect`.

The six family flags are counted by `famine_migration_recount_active_mission_slots` in `common/scripted_effects/chaosx_famine_migration_effects.txt:64-71`, and the free-slot trigger compares the count against `constant:famine_migration_mission_contract.maximum_active_missions` at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:21-30`.

All terminal mission paths clear the state subject and proof variables, clear the country family flag, and recount the active slots. The reception cancel path also records a breach before cleanup.

The source relies on the mission `activation` trigger and family flags rather than an explicit `activate_mission` effect. This matches the current source pattern, but runtime activation was not engine-verified because the MCP decision route and live game are unavailable.

## Cost, requirement, and localisation audit

All 26 decisions have a custom cost text and the current spendable designs remain at three or four types. The airlift is now explicitly four types: political power, transport aircraft, fuel, and air experience.

The four-cost escorted convoy and third-country resettlement entries use political power, convoys or trains, support or convoys, and fuel with no fifth hidden spendable cost.

Every displayed spendable cost uses a texticon after the patch. The former literal `Support Equipment:` labels were replaced by `£support_equipment_text_icon`, and transport aircraft now use the existing vanilla `GFX_unit_transport_plane_icon_small` texticon.

`fm_evacuate_workers` has a separate support-equipment prerequisite rather than a consumed cost, and the new custom trigger tooltip states that operational stock must be available to the transport authority.

The custom cost strings still use several fixed values in scripted localisation rather than shared constants. This is a maintainability warning, not a reason to change balance in this audit.

The category and generic effect tooltips remain concise but do not always expose the exact pressure threshold, route failure consequence, or donor/counterpart identity. External-relief and corridor follow-up should add dynamic target and blocked-reason text when their contracts are repaired.

## AI validity and route-lock notes

All 26 decisions have an `ai_will_do` block and use the decision AI constants. No decision was left without AI access by the selector replacement.

Movement decisions call the exact transfer contract once and consume the returned actual origin debit, survivor credit, and separately logged route deaths. The calls include general evacuation, internal distribution, foreign transit, and third-country resettlement.

`fm_requisition_safer_state` uses the safe-food donor selector and the requisition transfer contract, so it has a distinct donor path rather than pretending a local release is external aid.

Closed borders retain trapped-population state, and forced return uses its separate forced-return contract with unsafe-route deaths and condemnation consequences rather than silently deleting the cohort.

The destination helper validates owner/controller, route, reception, border, and hazard conditions before binding an event target. A zero candidate total has no fallback destination, which is the correct fail-closed behavior for the exact-transfer contract.

The airlift low-air-experience AI modifier is an invalid-target/score interaction because the decision is unavailable below that threshold while its factor rises there. It requires owner-side probability evidence and a separate compare after correction.

## Cleanup and exploit-risk notes

The six mission families have explicit stale-subject cleanup on cancel, timeout, and completion, and country cleanup clears all six active flags at `common/scripted_effects/chaosx_famine_migration_effects.txt:2161-2166`.

Exact movement debits the origin once, credits only surviving arrivals, records route deaths separately, rebinds the cohort destination, and clears terminal cohort records. No free-unit or population-creation loop was found in the reviewed decision call sites.

The primary remaining exploit/semantic risk is repeated local-reserve relief through actions described as external convoy or airlift delivery, combined with pressure reduction that is not tied to a donor or route transaction. The secondary risk is corridor population reduction without a named counterpart or route proof.

Regular event targets are used by the selector wrappers and are chain-scoped, while the existing route cleanup clears request variables. No confirmed stale-target leak was found, but the owner should include zero-total and repeated-call scenarios in the next engine pass.

## Changes made in this audit

`common/decisions/famine_migration_decisions.txt` was changed in `fm_third_country_resettlement` to nest the neighboring-state availability predicate under `FROM`, and in `fm_evacuate_workers` to expose its support-equipment prerequisite through a custom trigger tooltip.

`common/scripted_localisation/famine_migration_scripted_localisation.txt` gained `GetFamineMigrationTransportPlanes5Cost` with ready and blocked branches.

`localisation/english/famine_migration_l_english.yml` now uses the transport-plane icon in the airlift requirement and cost, uses support-equipment icons in all support cost entries, and adds `famine_migration_evacuate_workers_support_requirement_tt`, `famine_migration_cost_transport_planes_5_ready`, and `famine_migration_cost_transport_planes_5_blocked`.

Before the changes, third-country resettlement could test neighbors at the wrong scope, airlift hid a consumed aircraft cost, and worker evacuation hid a support prerequisite. After the changes, the target scope matches the state-targeted helper contract, the airlift displays all four spendable types, and the worker prerequisite has an icon-first requirement tooltip.

No probability-bearing weight, AI factor, pressure fraction, mission duration, route rule, or mapmode was tuned.

## Validation performed

The source contains 26 decision blocks and six mission blocks, and the source decision IDs compare exactly with the 26-row decision map CSV.

The seven selector call sites are present, no `random_neighbor_state` call remains in the decision or selector files, and exactly two dedicated mapmode IDs are present.

The three touched decision/script/localisation sources have balanced Clausewitz braces, and the localisation file remains UTF-8 with BOM.

The required GUI inspect/render and probability inspect routes were attempted and their exact timeout or `INTERNAL_ERROR` blockers are recorded above.

Live game validation was skipped because repository policy reserves in-game testing for the user.

## Recommended owner follow-up

1. Define and wire an external relief delivery contract for escorted convoy and airlift, including donor/source, route, capacity, survivor/food accounting, failure, and cleanup proof.

2. Give emergency imports a proven donor or external source identity, and give invited relief a bounded route/source result instead of direct pressure subtraction.

3. Select and persist a corridor counterpart and route, or rewrite the corridor tooltip and decision to describe the actual local action.

4. Correct the airlift AI modifier only after `chaosx_ai_probability_auditor` can run the named baseline scenarios and `hoi4.probability_compare` uses the same scenario set.

5. Rerun GUI inspect/render for `famine_migration_report_header_window` and render the two mapmodes when the MCP timeout is cleared.

6. Reduce active-category visible action density and add threshold/response cues for the header's load, capacity, and border values.

No separate broad implementation plan was written; the unresolved items require owner/system design decisions rather than a safe local patch.
