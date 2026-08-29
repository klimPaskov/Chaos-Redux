# Famine and Migration Decision/Mission Final Audit

> **Superseded historical snapshot (2026-08-25):** This standalone audit records the pre-split decision census and phase-repair tranche and is retained as historical evidence only. Its `fm_*` block counts, combined category paths, and implementation claims are not current instructions. Use [source_of_truth_map.md](../source_of_truth_map.md) and [completion_report.md](../completion_report.md) for the current split source, incomplete audit status, and remaining blockers.

Status: reopened decision-phase repair tranche complete in the shared worktree. This handoff records the source census, phase and role visibility gates, six-mission audit, exact response priority, non-canceling primary timers, MCP evidence, and unresolved owner-level blockers.

## Scope and changed files

The earlier density tranche changed `common/decisions/famine_migration_decisions.txt` and added this handoff. The reopened phase-repair tranche additionally changed `common/decisions/categories/famine_migration_categories.txt`, added `common/scripted_effects/famine_migration_decision_phase_effects.txt` with its matching `common/scripted_effects/famine_migration_decision_phase_effects.md`, and added one call site in `common/scripted_effects/chaosx_famine_migration_effects.txt`. The final priority repair changed only the 21 existing primary `cancel_if_not_visible` settings in `common/decisions/famine_migration_decisions.txt` from `yes` to `no`; response cancellation and all decision effects remain unchanged.

The reopened tranche changed no mapmode, scripted GUI, event, AI weight, cost, decision effect, mission timing, probability target, or localisation file. Concurrent work already present in the shared files was preserved.

The source currently contains 34 top-level `fm_` blocks: 26 primary decision-map IDs, the accepted corridor contract responses `fm_accept_corridor_offer` and `fm_reject_corridor_offer`, and six non-selectable missions. The two corridor response IDs are retained because they are counterpart contract responses, not extra action-map rows.

## Reopened decision-phase repair tranche

The phase contract now has one sparse country-scope refresh, `famine_migration_refresh_decision_phase_from_country`, called only from `famine_migration_process_registered_displacement_country` after country cohort selection, displacement-load refresh, achievement reconciliation, and the sparse corridor pulse.

Active to resolution requires an exact current country cohort row with positive amount, active or destination-bound status, this country as persisted owner, and valid origin and host states; positive country reception load; no owned active food-security crisis; and no unresolved non-reception origin, trapped, or flight crisis. A state marked `famine_migration_reception_context_active`, or carrying positive state reception load, does not block the transition through its displacement, flight, or trapped context. The helper has no timer and does not scan the world.

The transition sets `famine_migration_decision_resolution` and clears active, emerging, and dormant flags. If a food or non-reception origin/trapped/flight crisis reappears while resolution is set, the helper returns the country to active and clears resolution, emerging, and dormant. Existing terminal completion and cleanup effects remain unchanged.

The four durable decisions now use resolution plus `NOT = { has_country_flag = famine_migration_decision_active }` as their phase gate: `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation`. Their state, cohort, load, capacity, safety, AI, cost, effect, cooldown, and terminal cleanup predicates were preserved; the final priority repair intentionally makes their primary timers non-canceling along with the other primary rows.

The category has a separate valid-offer branch for a dormant or otherwise clean counterpart. It requires both `famine_migration_corridor_offer_pending` and the unchanged exact `famine_migration_corridor_offer_is_valid = yes` contract. Every one of the 26 primary decisions has an exact `NOT = { has_country_flag = famine_migration_corridor_offer_pending }` visibility guard. The response pair retains its own pending flag and exact validity checks, so a valid pending offer exposes exactly `fm_accept_corridor_offer` and `fm_reject_corridor_offer` among selectable ordinary decisions; the six missions remain non-selectable and are not part of the primary-action cap. The 21 primaries that previously opted into visibility cancellation now use `cancel_if_not_visible = no`, so a pending offer hides new starts without ending a paid timer before its existing terminal `remove_effect`; the two response decisions retain `cancel_if_not_visible = yes` for stale-offer cleanup.

The before/after census for this tranche is: resolution had zero durable primary rows before the phase gate repair and now has one to four durable rows only when their exact target contexts are valid; normal lanes remain three to five primary rows; the hard primary maximum is six; and a valid pending offer has two selectable ordinary response rows and zero newly selectable primary matrix rows. Any already-running primary timer remains engine-active but is hidden from new selection and reaches its existing terminal `remove_effect`; it is not an additional selectable action. The source still contains 26 primary IDs, two response IDs, and six missions.

## Exact visibility edits

The source-only density fix uses phase, role, and exact state/contract subject predicates. It does not remove a response or change what a valid action costs or does.

The following primary decisions gained or retained the role/subject gates used by the census:

- `fm_close_border` is active only for a valid displacement subject when the acting country has no food-security state and no positive reception load; its emerging branch remains available for a valid displacement subject.
- `fm_release_reserves`, `fm_emergency_imports`, `fm_repair_relief_route`, `fm_escorted_relief_convoy`, `fm_emergency_airlift`, and `fm_invite_relief` are food-role actions. Release requires initialized reserves and positive pressure, delivery actions require an exact relief contract and route mode, and invitation is visible only when no relief contract is active and a valid donor candidate exists.
- `fm_famine_evacuation` is hidden after the state is prepared and while the country has positive reception load. `fm_evacuate_vulnerable` and `fm_evacuate_workers` require the prepared displacement subject and no positive reception load.
- `fm_requisition_safer_state` remains a food-only action and is hidden while the displacement-country role is active.
- `fm_conceal_crisis` and `fm_maintain_extraction` are mutually exclusive by the state extraction profile; both remain restricted to the food-only role.
- `fm_negotiate_corridor` is restricted to a valid origin/transit role with no food-security state and no positive reception load.
- `fm_open_reception`, `fm_controlled_medical_reception`, and `fm_distribute_arrivals` are reception-role actions. Initial reception opening is not shown over an active displacement origin; overload opening requires positive load above capacity, while medical reception requires positive load and its existing policy subject.
- `fm_transit_only` and `fm_enforce_closure` are no-positive-load origin/transit actions, so they do not form a second wall over reception decisions.
- `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation` are durable reception-load actions. Integration and voluntary return require stable load, resettlement requires overload, and forced return requires positive load.

The emerging actions `fm_prepare_evacuation`, `fm_open_departure_routes`, and `fm_restrict_departure` remain in the existing emerging phase. Their valid state and pressure subjects were not removed.

## Before and after action census

The previous source-level mixed active category could expose approximately 18 primary decision IDs at once across relief, movement, border, reception, and durable outcomes. After the gates, the worst source-level primary-action count is six.

| Phase and role | Simultaneously valid primary IDs in the worst source state | Maximum |
| --- | --- | ---: |
| Emerging displacement | `fm_prepare_evacuation`, `fm_open_departure_routes`, `fm_restrict_departure`, and the valid-subject emerging branch of `fm_close_border` | 4 |
| Active food-only | `fm_release_reserves`, exactly one of the route-contract delivery decisions or `fm_invite_relief`, `fm_repair_relief_route`, `fm_famine_evacuation`, `fm_requisition_safer_state`, and exactly one profile-valid conceal/extraction decision | 6 |
| Active food plus displacement | Relief actions remain available when their food subjects and contracts are valid, while displacement-country registration hides requisition and conceal/extraction; the country does not get the food-only wall plus the displacement wall | 4 primary action types before subject-specific movement rows |
| Active origin/transit without food or positive reception load | The prepared case can show `fm_evacuate_vulnerable`, `fm_evacuate_workers`, `fm_negotiate_corridor`, `fm_close_border`, `fm_transit_only`, and `fm_enforce_closure` | 6 |
| Active origin/transit without a prepared pair | `fm_famine_evacuation` plus corridor, border, transit, and closure actions | 5 |
| Reception overload | `fm_open_reception`, `fm_controlled_medical_reception` when its existing policy subject is valid, `fm_distribute_arrivals`, `fm_third_country_resettlement`, and `fm_forced_repatriation` | 5 |
| Reception stable | `fm_controlled_medical_reception` when its existing policy subject is valid, `fm_distribute_arrivals`, `fm_local_integration`, `fm_voluntary_return`, and `fm_forced_repatriation` | 5 |
| Resolution | The helper exposes `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation` only when their exact reception, cohort, capacity, route, safety, and policy subjects are valid; `fm_mission_prepare_safe_return_route` remains non-selectable | 1-4 durable primary actions |

The exact corridor response pair is counted separately from the table. `fm_accept_corridor_offer` and `fm_reject_corridor_offer` require `famine_migration_corridor_offer_pending` plus `famine_migration_corridor_offer_is_valid`, have no state target or map action, have no spendable cost, and complete only the exact accept or reject contract. They are therefore response priority rows for one pending counterpart offer rather than additional primary action types. Both are preserved for AI and player access when the offer is valid.

The six-action edge cases are intentional accepted-corridor/subject combinations. Normal lanes are otherwise three to five primary action types, and no source-valid phase exceeds six primary IDs after the gates.

## Decision category lifecycle

`chaosx_famine_migration_category` remains an ordinary category with `visible_when_empty = no`, the existing hidden start state, the sustained emerging flag, active and resolution visibility, the compact report-header scripted GUI, and the existing priority. The category still exposes one primary Displacement Load plus supporting Reception Capacity and Border Policy values through existing localisation. Exactly two dedicated mapmodes remain: `famine_state_map_mode` and `migration_state_map_mode`.

While a counterpart carries a valid pending corridor offer, the category visibility branch is independent of domestic phase, so a dormant or clean counterpart can see the response pair. Primary matrix rows are fail-closed on the pending flag until the exact response contract is accepted or rejected.

The gates apply to both the player and AI because they are in the decision `visible` blocks. The existing `available`, `target_trigger`, `ai_will_do`, cooldown, and decision effects remain in each decision unless an earlier concurrent owner patch already changed them. Primary timers are explicitly non-canceling so phase or pending-offer visibility changes cannot discard a paid action before its terminal `remove_effect`; the response pair retains visibility cancellation for stale exact offers. This does not create a parallel category or a GUI tab.

## Cognitive-load notes

The action surface now presents one lane at a time: food security, origin/transit displacement, or reception and durable outcomes. Exact state and cohort subjects keep map-targeted rows tied to a visible problem instead of showing all registered states as interchangeable buttons.

The category header still has one primary Displacement Load and supporting Reception Capacity and Border Policy. No raw ledger, additional tab, full scripted GUI, or third mapmode was added. Existing map cues and target tooltips carry the detailed state selection.

The remaining presentation gap is that the compact header does not itself show a threshold marker, cause, or direct recommended response for every value. This is a GUI/localisation follow-up and was outside the authorized patch surface.

## Six mission quality notes

All six missions are non-selectable, use the existing activation proof and family flag, have a timeout, terminal success and failure paths, and recount the shared mission slots. The central contract is `constant:famine_migration_mission_contract.maximum_active_missions = 3`.

| Mission | Owner, category, region, and subject | Requirement and duration | Success, failure, and duplicate risk |
| --- | --- | --- | --- |
| `fm_mission_secure_relief_route` | ROOT country; relief route; one owned and controlled route subject state | Route subject, success proof, intact route, and deadline; `repair_route_timeout = 150` days | Stability on success; stability and war-support loss on timeout; subject, proof, deadline, and family flag are cleared on terminal paths. The route family flag prevents duplicates. |
| `fm_mission_hold_humanitarian_corridor` | Displacement country; humanitarian corridor; one controlled front/state subject and cohort | Valid corridor mission operation and exact corridor subject; `secure_corridor_timeout = 120` days | Corridor finalisation and stability/achievement on success; corridor expiry plus stability and war-support loss on timeout. The corridor family flag and exact origin/front subject prevent duplicate contracts. |
| `fm_mission_protect_evacuation_transport` | Displacement country; evacuation transport; one owned and controlled state/cohort | Evacuation subject, success proof, safe route, and deadline; `protect_evacuation_timeout = 100` days | Stability on success; stability and war-support loss on timeout; subject, cohort, deadline, proof, and family flag are cleared. The evacuation family flag prevents duplicates. |
| `fm_mission_deliver_relief_before_reserves_fail` | ROOT country; relief delivery; one owned food-security state | Relief proof, reserve floor, food-pressure success threshold, and deadline; `deliver_relief_timeout = 110` days | Stability on success; stability and war-support loss on timeout; subject, proof, deadline, and family flag are cleared. The relief family flag prevents duplicates. |
| `fm_mission_prevent_reception_collapse` | Receiving country; reception observation; one owned receiving state/cohort | Pending observation, reception context, capacity headroom, no overload/breach/outbreak, and deadline; `prevent_reception_timeout = 150` days | Stability and political power on success; breach/collapse failure records penalties and achievement failure. Cancel and timeout clear subject, proof, cohort, deadline, and family flag. The reception family flag prevents duplicates. |
| `fm_mission_prepare_safe_return_route` | ROOT country in resolution; return preparation; one owned return-context state/cohort | Return context, safe route, no active food-security danger, and deadline; `prepare_return_timeout = 180` days | Stability on success; stability and war-support loss on timeout; subject, deadline, and family flag are cleared. The return family flag prevents duplicates. |

Runtime activation of the mission contract remains an MCP/live-game blocker because the fresh event-inspect route was partial rather than decision-specific and this agent cannot launch the game.

## Costs, requirements, and localisation

The 26 primary decisions retain their existing custom cost strings. The reviewed localisation uses icon-first scripted cost helpers, and no primary decision displays more than four spendable cost types. The four-cost escorted convoy, airlift, and third-country entries remain within the cap. The airlift transport-plane cost and worker support-equipment prerequisite were already documented by the earlier audit and were not changed here.

No localisation key was added or renamed. Existing trigger tooltips cover the non-consumed support-equipment and airlift-plane requirements, while the existing route, target, and blocked-reason tooltips remain in place. New visibility predicates do not expose raw implementation variables to the player.

## AI validity and route-lock notes

All 26 primary IDs retain an `ai_will_do` block. The patch changes no AI weight or probability-bearing factor, so it does not claim a balance result. The mandatory probability inspection for `common/decisions/famine_migration_decisions.txt` using the `decision_ai_will_do` adapter timed out after 180 seconds, and no probability comparison was run in this tranche. The current airlift access gate is legal above 10 air experience and its positive factor applies above 50 air experience; the remaining uncertainty is numeric scenario impact, not an inverted factor.

Relief delivery rows now stay behind the exact relief contract and route mode. Invitation requires a valid donor candidate and no active relief contract. Island delivery retains blockade proof and the sea/air route mode. Movement rows retain exact state, cohort, corridor, destination, border, safety, and transport predicates from the existing transfer contracts. The accepted corridor response pair remains behind the exact pending offer contract.

The current source preserves exact route ownership contracts: emergency imports, escorted convoy, and airlift call `famine_migration_relief_deliver_contract`; invitation uses the exact donor-contract lifecycle; and corridor negotiation prepares and submits the exact counterpart/front offer contract. No broad-country or local-reserve fallback claim remains in this tranche. These existing contracts were retained and not silently redesigned here. A separate route-producer gap remains: `famine_migration_retire_recovered_state` currently registers only `famine_migration_relief_land_route_proven_input`, while no other caller sets the sea/air endpoint and route proof inputs. The sea/air decision predicates and contract validators are exact and fail closed, but the escorted-convoy and airlift rows are therefore structurally unreachable until an owner supplies those exact producers; this was not patched because it is outside the bounded decision-phase files.

## Cleanup and exploit-risk notes

The six mission families clear their subject flags, proof flags, deadlines, country family flags, and shared slot count on success, timeout, and cancellation. Exact civilian transfer calls debit the origin once, credit only surviving arrivals, and record route deaths separately. Existing route-request cleanup, cohort cleanup, return/integration/resettlement cleanup, and accepted-corridor expiry remain in the source.

The phase helper clears stale active, emerging, and dormant phase flags on active-to-resolution and resolution-to-active transitions. The existing durable terminal effects continue to clear the selected cohort and retain their established cleanup and achievement calls. Pending-offer priority is fail-closed on the pending flag, so it does not duplicate accept/reject effects or create a response loop. Primary timers now remain active through the pending visibility window and reach their original terminal `remove_effect`; no paid relief, movement, or contract action is canceled by the incoming response.

The exact relief and corridor contracts retain one-debit/one-credit ownership and response cleanup, and the current source audit found no repeated-reserve or broad-counterpart fallback in these decision paths. The source does have the separate sea/air proof-producer gap recorded above; fail-closed validators prevent a fabricated delivery, but those two rows cannot start until exact endpoint inputs are produced. No free-unit loop, population creation loop, duplicate mission slot loop, or global periodic scan was introduced by this patch.

## Required MCP evidence and blockers

The fresh read-only `hoi4.gui_inspect` route for the decision surface returned `GUI_INSPECTED` with status `ok`, but the source does not expose a full dedicated decision GUI. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/917b4c2cca6f21dcba8b04139b87732ba05ab211717ac0c874bfd7b945f2a6e4/07adee513c78646fec1ff57d7d65b2087a5c4b7511409ffac9c7a594299d8b10/gui-inspect.b2aa2cbd2ef811a.json`. Its fidelity reported zero modelled elements, one approximated element, and one missing element, with unrelated global `INDEX_SYMBOL_COLLISION` and `GUI_SCRIPTED_CONTEXT_INVALID` diagnostics.

The matching fresh `hoi4.gui_render` route for normal, active, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720 timed out after 180 seconds.

The fresh `hoi4.probability_inspect` route for the decision AI surface timed out after 180 seconds. No `chaosx_ai_probability_auditor` callable route was available, so no probability balance authority was duplicated here.

An earlier `hoi4.event_inspect` lint route against `common/decisions/famine_migration_decisions.txt` timed out after 180 seconds. For the reopened tranche, the single required fresh `hoi4.event_inspect` lint attempt returned `EVENT_INSPECTED_PARTIAL` with status `ok` and no blocking diagnostics, but its focused event analysis did not model the decision source. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/141063897062d3668c0724921fbbde880417d0dcabba8d1659072fe692e9fe56/73cb7869814ca07f2e581174cba9680edbce1885e4318e675a90dcb62893e692/event-lint-9028d4903907.json`. The report carries `MCP_INLINE_FILES_TRUNCATED` as an informational diagnostic and `validation.passed = false` because workspace-wide helper projections were deferred. This is not an event-owned surface, and no event route was changed; no repeat MCP attempt was made.

## Validation performed

The current source comparison reports 26 CSV primary IDs, 26 source primary IDs, no missing IDs, and no extra primary IDs. The two corridor response IDs are the only ordinary source extras and are documented above. The source has six mission IDs, balanced decision braces with 1,828 opens and 1,828 closes, balanced category braces with 14 opens and 14 closes, balanced phase-helper braces with 78 opens and 78 closes, and balanced existing-effect braces with 3,348 opens and 3,348 closes. It retains exactly two dedicated mapmode IDs and a shared mission cap of 3.

The source-level visibility census was re-read after the reopened patch. The highest primary-action rows in each valid phase are four emerging, six active food/origin edge cases, five reception rows, and one to four resolution durable rows under their exact target contexts. Normal lanes remain three to five primary rows and no source-valid phase exceeds six. The accepted response pair is not included in the primary-action cap because its exact pending-offer contract owns the response surface; while pending, it is the only selectable ordinary pair. The 26 primary visibility guards remain present, and the 21 primary `cancel_if_not_visible` settings are now non-canceling; the two response settings remain canceling.

Live game validation was skipped because repository policy reserves gameplay validation for the user. No new GUI, mapmode, or event was added, and no probability target was changed; the category received only the narrow valid-offer visibility branch documented above.

## Remaining issues and simplifications

No response, primary decision ID, mission ID, cost, effect, AI weight, GUI, mapmode, event, or probability target was removed or redesigned for this bounded patch. The category received only a narrow valid-offer visibility branch. The primary timer cancellation setting was deliberately changed to non-canceling to prevent a pending offer from discarding paid work before terminal delivery; existing effects and terminal cleanup were not rewritten. The simplification is intentional phase and response visibility gating using existing flags, variables, route contracts, and subjects.

The unresolved GUI-render, probability scenario-impact, partial event-lint, live-runtime, and sea/air route-proof producer blockers remain for the parent/system owners. The sea/air blocker is source-evidenced by the single land-only registration producer and the absence of any other sea/air input caller; its exact validators remain fail-closed. The primary non-canceling contract also means the old visibility-derived `cancel_effect` blocks are no longer reached by ordinary visibility loss; terminal `remove_effect` remains the paid-action cleanup path. If future state-loss cancellation is required, it needs an explicit `cancel_trigger` that excludes a pending offer, which is outside this bounded patch. Parent review is still required before treating the full famine and migration system as complete.
