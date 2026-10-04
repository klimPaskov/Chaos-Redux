# Event014 Larder logistics

Status: implemented. Parent review settled the capital-capture fallback and the constructor completion boundary on 2026-10-04, and the auditor's same-fixture probability comparison is recorded in the plans folder.
Acceptance basis: the parent authorized source application on 2026-10-04 after auditor 01a10385 captured ten baseline source files and eight named fixtures.
The accepted capacity constants are 1200/100/50 with the existing 5000 ceiling and unchanged 2000 ordinary cap.
The development input is the existing full logistics and administrative contract index, not physical buildings, completed storage projects or a node count.
No AI weight, cost, population, equipment, technology package, GUI layout, observation writer, model, portrait or workbook is added.

## Capacity and lifecycle

An ordinary country has capacity 2000.
A unified or transformed Wendigo country has capacity min(5000, 1200 + 100 times its actual controlled-state count + 50 times its refreshed existing cannibalism_unified_larder_capacity).
Each existing flag in the map below adds five index points, so it contributes 250 capacity before the ceiling.
The existing category stages 50/80/110 and their underlying fifty-flag score are unchanged.

A one-controlled-state, zero-index host has capacity 1300.
That permits the existing inclusive 800 + 400 reserve and the strict Larder > 1200 bonus without a weight or threshold retune.
A zero-state, zero-index host remains capped at 1200.
All other manpower, equipment, target, mission, war and route requirements remain applicable.

The derived country field cannibalism_larder_effective_capacity is initialized by the existing incarnation, warlord setup and external-spread activation owners.
It refreshes at operational-profile calculation, every store finalization and the existing bounded actor pulse.
A control loss therefore lowers the store at the next existing pulse or relevant operation boundary, with surplus discarded.
It does not create an extra daily or whole-world loop.
The existing incarnation reset, integration release, local victory and final cleanup clear the derived field.
Final cleanup uses the existing actor registry only, before that registry is emptied.

## Transfer accounting and exact distance

The route fraction retains the existing 1.00 opening factor, .85 retained-command submission, .65 surrendered-warband submission and .20 autonomy tribute, plus their existing preparation/relief modifiers.
Dispatch is the donor store multiplied by that route fraction.
The received amount is dispatch times (1 - min(.60, distance / 10000)).
The donor loses dispatch once, the recipient gains received once and the difference is transit loss.
A hoarder or an autonomy bargain conceals part of the dispatch in a cache at its own captured capital before it travels; the received amount is then (dispatch - concealed) times the retention, and [Hidden hoards](hidden_hoards.md) documents the cache, the host's review and the recovery actions.
Capacity overflow is discarded only at the completed recipient transaction boundary.
The existing route fraction is bounded to 0–1 and a negative donor store cannot produce a transfer.
Distance units are the engine map metric, with no unsupported physical unit label.

The consuming owner allocates quote outputs before nested helpers or country scopes.
The source and destination countries are explicit regular targets, and their actual capital-state targets are frozen before tag changes or annexation.
Native capital-scope capture sets two caller-owned transient proofs.
The meta effect evaluates the regular state targets' GetID namespaces and injects literal state IDs into the documented state distance expression.
For states 123 and 124 the resulting read is 123 = { set_temp_variable = { cannibalism_transfer_distance = distance_to@124 } }.
The distance output starts at -1. When either capital cannot be captured or the distance stays unwritten or negative, the quote uses the maximum route loss of .60 (constant `cannibalism_larder_logistics.distance_loss_maximum`) instead of blocking the transaction.
A real same-state zero result is valid.
No ROOT capital assumption, composite variable target argument or zero-distance fallback is used. Only an invalid country or generation context rejects the quote.

The quote/commit context also binds the donor's captured positive actor generation and requires it to match the current source.
Post-reveal recipients require a positive expected global host generation and exact equality to their current actor generation.
The constructor context is transient and only permits the selected, generation-validated donor with the exact planned CBL or selected Wendigo recipient.
An opening CBL quote uses the selected donor's actual capital for both endpoints because current construction explicitly installs that same state as CBL's capital.
The planned CBL country object is referenced explicitly before the existing capital owner/controller transfer creates the country.

## Transaction boundaries

Opening CBL and Wendigo constructors repeat the reveal dispatcher's spread-queue preflight before committing their reveal paths.
The preflight only fails on a corrupt queue, which already blocks the reveal at the dispatcher. Rows whose source or target country has died still validate and are invalidated when due.
They calculate distance before country/identity/annex work.
Once the public reveal flag is set, each constructor always completes its reveal: the opening CBL assignment, donor annex, roster rebuild and result follow runtime migration without depending on its result, and an unmigrated spread row is invalidated when it falls due.
The opening assignment substitutes the received quote into the existing inherited snapshot and preserves the original 300 bootstrap and managed/mobile route bonuses.
It does not invoke the later-donor credit path.
All non-Larder route knowledge, ledger, commander, troop, equipment and technology logic remains with the existing owners.

CBL finalizes after the actual donor annex returns and after publishing its own host pointer and expected generation.
Later absorption quotes before migration, requires migration success, consumes the quote before either store mutation, then admits the existing gifts/annex continuation only after actual credit success.
Because a missing capital quotes at the maximum loss instead of failing, a pending warlord is never stranded by a capital it cannot capture.
It finalizes after the actual donor annex, using the recipient's current territory.
Autonomy quotes and pays before clearing response flags, creates the subject through the explicit source country target, then finalizes using only the recipient's own territory.
It never credits autonomous donor land.

Initial transformed Wendigo publishes its own expected host generation after its existing identity preparation and before primary-donor integration.
The primary donor uses the existing explicit migration targets and requires a valid quote and host context.
It assigns the opening Larder only after migration succeeds and finalizes after primary annex.
The two-human branch retains the existing zero inherited donor Larder and disabled absorption.
It skips the donor quote/debit/credit, applies only the existing zero-snapshot opening assignment and route/bootstrap additions, then finalizes against the transformed country's own land.
A donor that is not absorbed, in the two-human branch or after a failed quote or migration, keeps its own stores, is not annexed and receives the normal response event through the rebuilt roster.
The transformed country then receives the zero-snapshot opening assignment, and the reveal tail (evolution record, super-event, anchors, focus overlay, roster, report and news) always runs once the public flag is set.

The five remaining immediate global mutation sites, mixed actor-pulse clamp and shared foreign-seed debit all call the country-aware finalizer.
Ordinary consumption and warlord-only operation clamps retain the local bound.
No standalone identity helper clamps or publishes stores before a territory transfer finishes.
Operational profile refresh calls the calculation-only capacity API, whose contract-score rebuild never calls back into operational-profile refresh.

## Private helper contracts

| Helper | Scope | Inputs/defaults | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| cannibalism_refresh_larder_effective_capacity | Existing country | Current country identity, native controlled states and existing recomputed contract flags | Regular country effective capacity, default ordinary 2000 | Rebuilds existing contract scores for a unified/Wendigo country. Changes no store or global mirror. |
| cannibalism_clamp_and_publish_current_larder | Country at a completed transaction boundary | Current stores, derived capacity calculation | Bounded stores and legitimate current host mirror | Calculates fresh capacity, discards excess and publishes only through the valid expected-generation host. |
| cannibalism_capture_current_larder_transfer_capitals | Donor country | Explicit regular destination country target, native current capitals | Caller-owned source generation and two native capture proofs, regular source/capital targets | Pointer capture only. No grant or debit. Failed scope entry retains zero proof allocated by caller. |
| cannibalism_prepare_larder_transfer_quote | Actual donor country | Two regular country targets, frozen capital targets, captured source generation, two proofs, existing route fraction, transient constructor context when applicable | Caller-owned distance, dispatch, received amount, loss fraction, retention and result | Read-only quote. Consumes capture proofs, route input and constructor context. Invalid context returns zero result and amounts. Missing capture or negative/unwritten distance quotes at the maximum route loss. |
| cannibalism_add_current_warlord_larder_to_unified_host | Donor country | Successful quote and still-valid country/generation context | Caller-owned transfer_committed | Consumes quote success before one dispatch debit and one received credit. Does not clamp the recipient. Rejects reused/invalid quotes. |
| cannibalism_apply_initial_larder_inheritance | Recipient after migration | Caller-owned inherited snapshot with distance-adjusted store | Existing opening Larder assignment | Preserves bootstrap/managed/mobile additions. No clamp, publication or second donor credit. |
| cannibalism_larder_transfer_context_is_valid | Donor-country trigger | Explicit regular countries, captured positive source generation and selected/current host context | Boolean | No mutation. |
| cannibalism_runtime_migration_source_is_valid | Runtime source context | Existing live source, or exact one-shot validated CBL opening provenance | Boolean | Source validity only, with unchanged live-source behavior and no later bypass. |
| cannibalism_has_valid_unification_destination | Existing trigger scope | Existing host pointer and positive expected generation | Boolean | Preserves original identity/reveal/existence predicates and requires current actor-generation equality. |

Scope pointers are regular effect-chain targets, with no new global target.
All quote/proof/commit outputs are allocated inline by the four owners before helpers/scopes.
The absorption and autonomy owners also own the hidden share `cannibalism_transfer_concealment_share` before `cannibalism_prepare_current_warlord_concealment_share` and the cache amount `cannibalism_transfer_hoard_amount` before the quote (`helper_output_ownership.md`).
The source generation, route input and constructor context are temporary.
Private scratch fields used only inside capacity/quote calculation need no caller allocation.
Regular targets clear with their effect chain, and fresh zero capture proofs prevent stale target reuse within a chain.

Use the calculation API for a country value consumer without mutating stores:
~~~txt
cannibalism_refresh_larder_effective_capacity = yes
~~~

Use the finalizer after a completed store mutation or native territorial transaction:
~~~txt
cannibalism_clamp_and_publish_current_larder = yes
~~~

The constructors, absorption and autonomy owners show the full inline output-allocation and quote/commit usage.
The prior lifetime repair remains intact.
Its 67 source projections and archived repair checker outputs remain historical evidence and were not relabelled as validation of this change.

## Fifty-flag administrative development map

Every flag below is set by a completed focus-owned effect, rather than by a completed physical storage payment.
Each contribution remains five points in the existing category score and contributes 250 proposed storage capacity through the accepted administrative index.
Multiple flags describe distinct contracts in one completed institution/method, so this is a contract index rather than a count of focuses.

The two risk flags, escort burden, harvest-cap requirement and pending package were flagged to the parent before source application.
The risk flags represent the completed method's live tradeoff configuration and currently alter hostility gains.
Escort burden represents the completed transport method's current support-equipment requirement.
Harvest-cap requirement represents the installed receipt-limit rule used by current harvest validation.
The legacy pending-package flag is set by the completed supply-ceiling focus and currently extends Larder mission duration by 60 days.
It has no storage-payment/completion writer or clear-on-payment transition in the inspected source.
Its index contribution represents that enacted long-horizon administrative contract, with no claim or grant of an unpaid storage building.
No flags are excluded or silently converted to a new category score.

| Group | Exact flag | Completed owner writer | Rationale |
| --- | --- | --- | --- |
| Administration | `cannibalism_unified_central_accounting_open` | `cannibalism_unified_focus_central_accounting`, effects line 16081 | Installed central accounting procedure. |
| Administration | `cannibalism_unified_larder_audit_missions_open` | `cannibalism_unified_focus_central_accounting`, effects line 16082 | Operational store-audit mandate and mission contract. |
| Administration | `cannibalism_unified_state_classification_open` | `cannibalism_unified_focus_classify_the_consumption_states`, effects line 16086 | Installed state-classification ledger procedure. |
| Administration | `cannibalism_unified_consumption_stage_decisions_open` | `cannibalism_unified_focus_classify_the_consumption_states`, effects line 16087 | Authorized and configured stage-specific consumption contracts. |
| Administration | `cannibalism_unified_storage_projects_open` | `cannibalism_unified_focus_build_the_storage_network`, effects line 16091 | Storage-program administration opened by its completed focus. |
| Administration | `cannibalism_unified_larder_route_projects_open` | `cannibalism_unified_focus_build_the_storage_network`, effects line 16092 | Routing-program contract and controlled-route infrastructure policy. |
| Administration | `cannibalism_unified_captured_industry_projects_open` | `cannibalism_unified_focus_boards_of_captured_industry`, effects line 16097 | Completed captured-industry board administration. |
| Administration | `cannibalism_unified_workshop_conversion_open` | `cannibalism_unified_focus_boards_of_captured_industry`, effects line 16098 | Operational workshop-conversion authorization. |
| Administration | `cannibalism_unified_larder_method_routes_open` | `cannibalism_unified_focus_continental_larder_doctrine`, effects line 16103 | Completed continental method-selection doctrine. |
| Administration | `cannibalism_unified_larder_tradeoff_missions_open` | `cannibalism_unified_focus_continental_larder_doctrine`, effects line 16104 | Configured method tradeoff mission framework. |
| Rapid method | `cannibalism_unified_larder_method_rapid` | `cannibalism_unified_focus_burn_through_the_near_states`, effects line 16108 | Selected and installed rapid-consumption method. |
| Rapid method | `cannibalism_unified_rapid_consumption_decisions_open` | `cannibalism_unified_focus_burn_through_the_near_states`, effects line 16110 | Operational rapid-consumption authorization. |
| Rapid method | `cannibalism_unified_state_exhaustion_risk` | `cannibalism_unified_focus_burn_through_the_near_states`, effects line 16111 | Named risk marker of the completed rapid doctrine, with current hostility gain. |
| Rapid method | `cannibalism_unified_legion_surge_decisions_open` | `cannibalism_unified_focus_feed_the_legion_surge`, effects line 16117 | Installed surge-feeding operational contract. |
| Rapid method | `cannibalism_unified_rapid_recruitment_cost_scaling_open` | `cannibalism_unified_focus_feed_the_legion_surge`, effects line 16118 | Active rapid-recruitment cost-scaling policy. |
| Rapid method | `cannibalism_unified_frontier_exhaustion_missions_open` | `cannibalism_unified_focus_exhaust_the_frontier`, effects line 16124 | Operational frontier-exhaustion mission framework. |
| Rapid method | `cannibalism_unified_exhausted_state_abandonment_open` | `cannibalism_unified_focus_exhaust_the_frontier`, effects line 16125 | Installed exhausted-district disposition procedure. |
| Rapid method | `cannibalism_unified_rapid_larder_capstone` | `cannibalism_unified_focus_short_horizon_continent`, effects line 16131 | Completed rapid-method administrative capstone. |
| Rapid method | `cannibalism_unified_short_campaign_horizon` | `cannibalism_unified_focus_short_horizon_continent`, effects line 16133 | Installed short-horizon planning contract. |
| Managed method | `cannibalism_unified_larder_method_managed` | `cannibalism_unified_focus_preserve_the_working_herds`, effects line 16137 | Selected and installed managed-herd method. |
| Managed method | `cannibalism_unified_managed_herd_decisions_open` | `cannibalism_unified_focus_preserve_the_working_herds`, effects line 16139 | Operational managed-herd authorization. |
| Managed method | `cannibalism_unified_organized_resistance_risk` | `cannibalism_unified_focus_preserve_the_working_herds`, effects line 16140 | Named risk marker of the completed managed doctrine, with current hostility gain. |
| Managed method | `cannibalism_unified_feeding_rotation_decisions_open` | `cannibalism_unified_focus_rotate_the_feeding_districts`, effects line 16146 | Installed district feeding-rotation procedure. |
| Managed method | `cannibalism_unified_district_recovery_missions_open` | `cannibalism_unified_focus_rotate_the_feeding_districts`, effects line 16147 | Operational district-recovery mission framework. |
| Managed method | `cannibalism_unified_long_harvest_policing_open` | `cannibalism_unified_focus_police_the_long_harvest`, effects line 16151 | Completed long-harvest policing administration. |
| Managed method | `cannibalism_unified_herd_revolt_missions_open` | `cannibalism_unified_focus_police_the_long_harvest`, effects line 16152 | Operational herd-revolt response mandate. |
| Managed method | `cannibalism_unified_managed_larder_capstone` | `cannibalism_unified_focus_managed_continental_reserve`, effects line 16158 | Completed managed-method administrative capstone. |
| Managed method | `cannibalism_unified_long_campaign_horizon` | `cannibalism_unified_focus_managed_continental_reserve`, effects line 16160 | Installed long-horizon campaign planning contract. |
| Mobile method | `cannibalism_unified_larder_method_mobile` | `cannibalism_unified_focus_prisoner_trains`, effects line 16164 | Selected and installed mobile method. |
| Mobile method | `cannibalism_unified_prisoner_train_decisions_open` | `cannibalism_unified_focus_prisoner_trains`, effects line 16166 | Operational prisoner-train routing authorization. |
| Mobile method | `cannibalism_unified_transport_escort_burden` | `cannibalism_unified_focus_prisoner_trains`, effects line 16167 | Named burden marker of the completed transport method, setting current support cost. |
| Mobile method | `cannibalism_unified_larder_column_escort_open` | `cannibalism_unified_focus_escort_the_larder_columns`, effects line 16173 | Installed column-escort administration. |
| Mobile method | `cannibalism_unified_route_interdiction_missions_open` | `cannibalism_unified_focus_escort_the_larder_columns`, effects line 16174 | Operational route-interdiction response mandate. |
| Mobile method | `cannibalism_unified_oceanic_hulk_routes_open` | `cannibalism_unified_focus_oceanic_hulk_routes`, effects line 16178 | Completed oceanic route-planning administration. |
| Mobile method | `cannibalism_unified_prison_hulk_transport_open` | `cannibalism_unified_focus_oceanic_hulk_routes`, effects line 16179 | Installed prison-hulk transport authorization. |
| Mobile method | `cannibalism_unified_mobile_larder_capstone` | `cannibalism_unified_focus_the_larder_that_moves`, effects line 16184 | Completed mobile-method administrative capstone. |
| Mobile method | `cannibalism_unified_mobile_global_routes_open` | `cannibalism_unified_focus_the_larder_that_moves`, effects line 16186 | Installed global mobile-route administration. |
| Battlefield method | `cannibalism_unified_larder_method_battlefield` | `cannibalism_unified_focus_mark_the_battlefield_yields`, effects line 16190 | Selected and installed battlefield-yield method. |
| Battlefield method | `cannibalism_unified_battlefield_yield_decisions_open` | `cannibalism_unified_focus_mark_the_battlefield_yields`, effects line 16192 | Operational battlefield recovery authorization. |
| Battlefield method | `cannibalism_unified_battlefield_harvest_caps_required` | `cannibalism_unified_focus_mark_the_battlefield_yields`, effects line 16193 | Installed receipt-limit enforcement rule, used by current harvest validation. |
| Battlefield method | `cannibalism_unified_recovery_battalion_missions_open` | `cannibalism_unified_focus_recovery_battalions`, effects line 16199 | Operational recovery-battalion mission framework. |
| Battlefield method | `cannibalism_unified_major_victory_receipts_open` | `cannibalism_unified_focus_recovery_battalions`, effects line 16200 | Installed major-victory receipt procedure. |
| Battlefield method | `cannibalism_unified_captured_hospital_conversion_open` | `cannibalism_unified_focus_convert_the_captured_hospitals`, effects line 16204 | Completed hospital-conversion administration. |
| Battlefield method | `cannibalism_unified_battlefield_processing_projects_open` | `cannibalism_unified_focus_convert_the_captured_hospitals`, effects line 16205 | Operational field-processing project authorization. |
| Battlefield method | `cannibalism_unified_battlefield_larder_capstone` | `cannibalism_unified_focus_harvest_follows_victory`, effects line 16209 | Completed battlefield-method administrative capstone. |
| Battlefield method | `cannibalism_unified_victory_harvest_scaling_open` | `cannibalism_unified_focus_harvest_follows_victory`, effects line 16211 | Installed victory-yield scaling policy. |
| Continental network and terminal administration | `cannibalism_unified_continental_supply_regions_open` | `cannibalism_unified_focus_continents_as_supply_regions`, effects line 16215 | Completed continental supply-region administration. |
| Continental network and terminal administration | `cannibalism_unified_network_anchor_capitals_open` | `cannibalism_unified_focus_continents_as_supply_regions`, effects line 16216 | Installed network-capital routing contract. |
| Continental network and terminal administration | `cannibalism_unified_terminal_larder_gate` | `cannibalism_unified_focus_abolish_the_old_supply_ceiling`, effects line 16221 | Completed terminal logistics authorization and readiness gate. |
| Continental network and terminal administration | `cannibalism_unified_supply_ceiling_package_pending` | `cannibalism_unified_focus_abolish_the_old_supply_ceiling`, effects line 16222 | Disclosed legacy pending marker with a current 60-day mission-planning extension. |


## Meaningful validation and limits

The handoff and evidence retain before/after source hashes, direct call-site coverage, the unchanged fifty-flag score and constants, protected event-description equality, scoped structural-checker findings and source-derived transaction arithmetic.
The eight frozen fixture IDs are preserved for the parent's mandatory probability_compare through auditor 01a10385.
Source arithmetic is synthetic and does not execute the engine or establish normalized AI chances.
The auditor's baseline contains partial MCP coverage and unbound fixture inputs.
The parent must carry those into comparison and acceptance.

Opening CBL also has a one-shot validated-source provenance input.
The existing capital transfer may take the donor's last state before runtime migration.
The source predicate therefore retains its normal live-source branch and permits only that already validated opening donor when the captured source/recipient pointers match, the quoted positive source generation and quote success survive, the actual recipient is live CBL with a positive actor generation, and its installed owned/controlled capital is the frozen source capital.
The input is allocated and cleared in the CBL constructor.
It is never set by later absorption, autonomy or Wendigo and provides no later-donor or stale-generation bypass.

Installed docs and offline reference citations for GetID, meta_effect, static state distance, variable bounds, constants and regular target lifetimes remain in the owner acceptance evidence.
Connected pre-change probability inspection and event trace are retained with source revisions and artifact URIs.
Post-change exact helper inspection is retained separately.
The event workflow remains partial where its helper/lifecycle passes were deferred.
script_validate is not exposed, advanced helper jobs were not used without negotiation, and no game or log was accessed.

Icons/assets: no new icons, sprites or visual assets are required.
Existing Larder tooltips are reused, with only their authorized English capacity text updated.
GUI layout and observation-writer work remain proposals under their separate owners.

Future work: bind the auditor's declared missing fixture inputs, then confirm native GetID/distance and control-loss timing in a live session.
Any later replacement of the administrative index by physical storage or network counts needs a separate accepted design and must preserve category-score semantics.

