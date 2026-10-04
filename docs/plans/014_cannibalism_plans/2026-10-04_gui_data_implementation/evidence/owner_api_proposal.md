# Event014 GUI data owner API proposal

Disposition: accepted requirements and proposed source implementation, awaiting parent application and review.
Acceptance basis is the parent's explicit 2026-10-04 instruction accepting target-specific observations, actual report/result hooks, secrecy, unknown confidence, and generation-safe extension of the existing record owner.
This proposal does not authorize new costs, weights, decision eligibility, raid design, assets, or shared GUI infrastructure.
CAP architect `01a10386` remains plan-only and AI baseline `01a10385` remains frozen.
The parent owns application, English review, AI/balance, actual targeted raid work, GUI worker synchronization, and shared commit.

Proposed eventual authoritative document: `docs/events/014_cannibalism/gui_data_contract.md`.
Proposed dynamic API index row in `common/scripted_effects/chaosx_dynamic_effects.md`, under `owner_owned_apis`:

| capability | authoritative_source | reference |
| --- | --- | --- |
| `event014_gui_observation_and_identity` | `014_cannibalism_effects.txt`, `014_cannibalism_triggers.txt`, and `014_cannibalism_scripted_localisation.txt` | `../../docs/events/014_cannibalism/gui_data_contract.md`, typed observer snapshots, public identity, immutable integrated history, real target receipts, epoch invalidation, and caller-owned trigger-local outputs |

No implementation is added to the shared dynamic effects file and no router or wrapper skill is proposed.
No icons or art are added by this API package.
The existing three windows and their installed sprites remain UI-worker consumers, including all 56 regional portrait finals and the four protected Hannibal assets.

## Scope, identity, and fields

COUNTRY observations are stored on their subject with `_@OBSERVER` targeting, implemented as `_@PREV` in writers and `_@ROOT` in native row readers.
STATE observations use the identical observer key with state flags.
Only one tag suffix appears in any flag.
Record kinds are country actor, state node, inbound warning, and own subject fact.
Own subject facts describe current domestic or command subjects and never imply that a hidden node was discovered.
Foreign hidden cells require actual observed records even when their country's diplomatic identity is public.

Each subject record stores `cannibalism_ui_observer_epoch_@ROOT`, `cannibalism_ui_record_kind_@ROOT`, and the identity appropriate to that kind.
COUNTRY actor: `cannibalism_ui_subject_generation_@ROOT` equals its positive `cannibalism_actor_generation`.
STATE node: `cannibalism_ui_subject_node_id_@ROOT` and `cannibalism_ui_subject_generation_@ROOT` equal its positive node ID and generation.
Warning: `cannibalism_ui_subject_spread_id_@ROOT` equals the validated positive spread ID and never substitutes for node identity.
Node and warning records also capture `cannibalism_ui_source_country_@ROOT` and `cannibalism_ui_source_generation_@ROOT` from their exact current source snapshot.
Source validity requires an actual COUNTRY object with `exists = yes` and matching positive actor generation.
No source name is thereby authorized for display.
An own-state fact instead rechecks owner/controller and viewer epoch and does not depend on a nonexistent node source.

Subject flags: `cannibalism_ui_identity_observed`, `cannibalism_ui_type_observed`, `cannibalism_ui_strength_observed`, `cannibalism_ui_route_observed`, `cannibalism_ui_incident_observed`, and `cannibalism_ui_counteraction_selected`, each with the observer suffix.
Flags represent presence, so a genuinely observed zero strength does not equal unknown.
Values: `cannibalism_ui_observed_node_type`, `cannibalism_ui_observed_strength_band`, `cannibalism_ui_observed_route`, `cannibalism_ui_last_incident`, `cannibalism_ui_counteraction`, and `cannibalism_ui_counteraction_status`, each observer-targeted.
Dates: `cannibalism_ui_strength_observed_date`, `cannibalism_ui_route_observed_date`, `cannibalism_ui_last_incident_date`, and `cannibalism_ui_counteraction_date`, each observer-targeted and using existing `global.date` integer encoding.
Never compute date arithmetic by treating this encoding as a number of elapsed days.

Typed cleanup indexes: subject COUNTRY/STATE `cannibalism_ui_observer_countries` contains unique COUNTRY pointers.
Observer COUNTRY `cannibalism_ui_observed_country_entries` contains unique COUNTRY subjects and `cannibalism_ui_observed_state_entries` contains unique STATE subjects.
These indexes enumerate only recorded pairs and never replace the gameplay actor, node, or spread registries.
Maintain both directions together on first publication and on retirement.
Use native membership to avoid duplicate rows and scope iterators for cleanup.
Do not enumerate all countries daily.

## Helper map

| Proposed helper | Scope, inputs | Outputs and side effects | Direct consumers |
| --- | --- | --- | --- |
| `cannibalism_ui_ensure_viewer_epoch` | observer COUNTRY | initializes only a missing normal epoch to one, no temp output | every report/result writer and command setup |
| `cannibalism_ui_prepare_country_observation` | subject COUNTRY with PREV observer, exact expected actor generation | validates existing subject, clears mismatched old observer record, publishes identity and cleanup indexes | country report/result adapters |
| `cannibalism_ui_prepare_node_observation` | subject STATE with PREV observer, expected node ID/generation/source | validates complete node snapshot and publishes only that identity | investigation and other genuinely observed state results |
| `cannibalism_ui_prepare_warning_observation` | subject STATE with PREV observer, exact warning ID/source/route snapshot | warning-kind receipt and membership, no strength or node type | `.60` successful immediate guard and paid warning screening |
| `cannibalism_ui_prepare_investigation_observation` | actual mission target STATE with PREV actor | node receipt when captured identity matches, otherwise own-subject order receipt with no fabricated node | investigation start and results |
| `cannibalism_ui_clear_country_observation` / `cannibalism_ui_clear_state_observation` | typed subject with PREV observer | clears six flags, all identity/value/date variables above for this pair, removes reciprocal index membership | observer reset, subject retirement, stale replacement |
| `cannibalism_ui_retire_current_subject_observations` | typed retiring subject | iterates its observer index, clears exact pairs before gameplay identity is erased | actor unregister, node retirement, slot release, warning identity retirement |
| `cannibalism_ui_reset_current_viewer` | viewer COUNTRY | clears indexed pairs and view state, increments existing epoch, no intelligence inheritance by default | incarnation reset before gameplay reset |
| `cannibalism_ui_transfer_current_human_observations` | explicit source and destination COUNTRY targets | transfers only the human viewer's validated indexed pairs to destination epoch with rewritten observer suffix and reciprocal indexes, then clears source | actual `change_tag_from` branches, before annex/reset |
| `cannibalism_ui_country_observation_valid`, `cannibalism_ui_node_observation_valid`, `cannibalism_ui_warning_observation_valid`, `cannibalism_ui_own_subject_fact_valid` | typed row THIS, ROOT viewer | pure Boolean, object and exact identity/epoch checks | row filters, card getters, selection guards |
| `cannibalism_ui_load_state_route` and per-field typed loaders | typed subject, ROOT viewer | trigger-local output only when matching receipt exists | corresponding `defined_text.text.trigger` |
| `cannibalism_gui_validate_selected_network_target` | viewer COUNTRY, stored typed pointer and captured identity/epoch | Boolean only, no display refresh from hidden state | selected-card getters and visibility |
| `cannibalism_gui_rebuild_command_view` | owner COUNTRY | native controlled-state array, live warlord and aligned generation arrays, dirty increment | setup, information refresh, owned state/host transfer handlers |
| `cannibalism_ui_live_warlord_row_valid` | native COUNTRY row, ROOT host and native index | exists, actor/slot generation equality, actual classification and relationship | live loyalty identity/portrait/disposition readers |
| existing `cannibalism_record_integrated_warlord_slot` extended | destination COUNTRY, existing integration inputs plus donor generation and origin STATE captured immediately from the explicit donor | appends nine aligned immutable arrays, positive globally allocated donor generation key, idempotent membership, new staging inputs cleared before and after each call | all three existing record calls in history hunks |
| `cannibalism_ui_integrated_arrays_aligned`, `cannibalism_ui_integrated_row_valid`, `cannibalism_ui_load_integrated_warlord_row` | host COUNTRY, native numeric generation and row index | Boolean validity and ten temp outputs, no persistent identity mutation | historical loyalty fields |
| `cannibalism_ui_clear_integrated_history` | recipient COUNTRY | clears exactly nine history arrays only at recipient reset | reset after any replacement-host transfer |
| `cannibalism_ui_record_continental_target` | command COUNTRY, validated actual decision target | last committed target pointer, captured target identity, observer epoch, date and operation kind | committed campaign operation |
| `cannibalism_ui_clear_command_view` | owner COUNTRY | view arrays, typed selection pointers, identities and dirty/open state | GUI close, branch hide, incarnation/terminal cleanup |

Missing inputs cause no publication and remain a failed contract needing parent review.
They do not cause a known zero, an arbitrary selected target, or a fake successful observation.
None of these helpers pays costs, changes timers, modifies outcomes, alters weights, or changes underlying eligibility.
Typed loaders never call scripted effects.
Installed `set_temp_variable` is explicitly legal in trigger context.
Every caller initializes the temporary outputs it consumes before a returning loader, including each localisation field and each nested forwarding boundary.
The native numeric history row's generation and index are inputs and are never zeroed by a loader.
No temporary variable is scoped with ROOT or PREV.
Literal YML keys contain numeric formatting, while `localization_key` names the key itself.

## Required real hooks

| Transaction or current helper | Typed subject and observation | Insertion and restrictions |
| --- | --- | --- |
| `.2`, `.20`, `.21` | actual recipient COUNTRY, delivered discovery/ritual/network incident | immediate after valid delivery, state details only if a validated actual state pointer exists |
| `.30` | `cannibalism_warlord_new_country` public COUNTRY | preserve public name and origin, no foreign secret strength or strategy receipt |
| `.60` | `cannibalism_spread_target_state` STATE | inside successful immediate warning guard after expected ID capture, warning route and incident only |
| `.61`, `.62` | actual report recipient and `cannibalism_spread_target_state` | add immediate adapter after exact arrival identity validation, distinct arrival/reinfection incident, do not use live pending globals |
| `cannibalism_start_investigation_mission` | `cannibalism_investigation_target_state`, optional captured node ID/generation | after mission activation in accepted start transaction |
| `cannibalism_start_hold_prison_mission` | captured prison target STATE and its exact identity | successful activation only |
| `cannibalism_start_reach_island_mission` | existing island target COUNTRY and generation | successful activation only |
| `cannibalism_start_break_network_mission` | existing network target COUNTRY and generation | successful activation only |
| `cannibalism_start_stop_unification_mission` | existing unification target COUNTRY and generation | successful activation only |
| `cannibalism_start_stop_transformation_mission` | existing transformation target COUNTRY and generation | successful activation only, retain existing reveal secrecy |
| complete/partial/fail/resolve cancellation for these six families | same stored actual target with its original identity | before corresponding `clear_*_mission`, publish the real status and observed incident, skip stale callback |
| `cannibalism_try_pay_humane_route_screening_cost`, `cannibalism_try_pay_hard_route_screening_cost` | `cannibalism_screening_state`, requested positive spread ID | successful payment block at E:10972–11034, before warning close |
| forensic outcomes at E:6197–6234 | acting COUNTRY unless actual mission STATE remains validated | country-level incident only when no specific state provenance exists |
| `cannibalism_unified_execute_campaign_operation` | `cannibalism_unified_decision_target`, real targeted decision FROM | after actual commitment and before target-chain end |
| actual targeted raid commit and completion | decision owner's real selected STATE and captured target identity | unresolved until targeted raid exists, no hook to unrelated UI selection |

Results may disclose type/strength only when the accepted mechanic actually observes that subject.
An order or failed result does not disclose all secret fields.
The earlier handoff supplies current target variable definitions and the parent must reread each exact start/result/clear block before applying all adapters.
The source hunks intentionally show representative transactions rather than mechanically generating unreviewed clones across every family.
All mapped adapters remain required application work, with their source-level contracts tested through real selectors and result paths.

## Public rows, sorting, selectors, and bindings

Keep native Network arrays and country/state dynamic-list identifiers.
Apply existing tab predicates plus visibility authorization: own known subject facts, public warlord COUNTRY identity, or valid observed secret subject.
Public identity does not confer strength, route, incident, or personality knowledge.
Retain diplomacy-known warlord rows in Foreign Links and Warlord States as appropriate to current filters.
No report flag becomes a decision `available` or `target_trigger` condition.

Replace only the Network reverse numeric loops with native scope traversal and front insertion at index zero for newest-first.
Use the same authorization and duplicate checks in both orders.
Append valid warning-only states from the viewer's typed state index if absent from the node list.
An unobserved warning or undiscovered foreign node must never enter a list simply because it is globally registered.

Country selector captures positive actor generation, or a validated public subject epoch when there is no active actor.
State selector captures record kind, node ID/generation or warning ID, source identity and viewer epoch.
Validate native index range and row eligibility before pointer assignment.
Clear the mutually exclusive other selection and all of its identity fields.
Selected-card readers enter only a validated pointer and use identical secret-field receipts as row readers.

Command native lists:

| List ID | Array, value, index, scope change |
| --- | --- |
| `cannibalism_controlled_state_dynamic_list` | `cannibalism_command_gui_state_entries`, `cannibalism_command_gui_state`, `cannibalism_command_gui_state_index`, yes |
| `cannibalism_loyalty_integrated_dynamic_list` | `cannibalism_integrated_warlord_generation_entries`, `cannibalism_loyalty_generation`, `cannibalism_loyalty_index`, no |
| `cannibalism_loyalty_live_dynamic_list` | `cannibalism_command_gui_warlord_entries`, `cannibalism_loyalty_country`, `cannibalism_loyalty_country_index`, yes |

Live loyalty aligned auxiliary arrays are `cannibalism_command_gui_warlord_actor_generation_entries` and `cannibalism_command_gui_warlord_slot_generation_entries`.
Their index is native `cannibalism_loyalty_country_index`, and equality is required before printing a reused slot's current country identity.
Live rows read current `cannibalism_warlord_disposition` and pending absorption, with actual autonomy/resistance/challenge labels.
History rows read only captured numeric identity fields and captured STATE origin pointer.
Historical portrait getters use the existing slot/region sprite vocabulary without writing the host's canonical identity variables.
Reuse regional name/origin localisation vocabulary in dedicated historical getters, not by impersonating the donor with mutable host aliases.

Getters: `GetCannibalismUiNetworkIdentity`, `GetCannibalismUiNetworkNodeType`, `GetCannibalismUiNetworkStrengthBand`, `GetCannibalismUiNetworkKnownRoute`, `GetCannibalismUiNetworkLastIncident`, `GetCannibalismUiNetworkCounteraction`, `GetCannibalismUiNetworkUncertainty`, `GetCannibalismUiControlledStateCard`, `GetCannibalismUiRaidTarget`, `GetCannibalismUiContinentalTarget`, `GetCannibalismUiIntegratedWarlordName`, `GetCannibalismUiIntegratedWarlordOrigin`, `GetCannibalismUiIntegratedWarlordDisposition`, `GetCannibalismUiIntegratedWarlordPortrait`, and `GetCannibalismUiLiveWarlordDisposition`.
Each getter has a typed row or validated owner selection contract, and each field has a literal unknown/unavailable key when its specific provenance is absent.
Parent English review owns the final labels and text.
No aggregate integrated count substitutes for history rows, and no unrelated selected state substitutes for an active raid.

## Constants and tuning

Reuse existing `cannibalism_gui_value`, `cannibalism_meter`, `cannibalism_node_type`, `cannibalism_spread_route`, and `cannibalism_warlord_disposition` categories.
Existing spread-route values are `retreat=1`, `prisoner_transfer=2`, `convoy=3`, `volunteer_return=4`, `occupation_turnover=5`, `deliberate_seed=6`, `conquest=7`, and `survivor=8`.
Add integer enum categories with `schema = { any_key = yes data = int }` to the existing owner constants file.

| Category | Proposed stable values |
| --- | --- |
| `cannibalism_ui_record_kind` | unknown 0, country_actor 1, state_node 2, warning 3, own_subject 4 |
| `cannibalism_ui_strength_band` | unknown 0, quiet 1, active 2, severe 3 |
| `cannibalism_ui_uncertainty` | unobserved 0, partial 1, observed 2, stale 3 |
| `cannibalism_ui_action_status` | none 0, active 1, resolved 2, partial 3, failed 4, cancelled 5 |
| `cannibalism_ui_counteraction` | none 0, investigation 1, prison 2, island 3, break_network 4, stop_unification 5, humane_screening 6, hard_screening 7, stop_transformation 8 |
| `cannibalism_ui_incident` | unknown 0, discovery 1, ritual 2, network 3, emergence 4, inbound_warning 5, arrival 6, reinfection 7, investigation 8, screening 9, prison 10, island 11, network_result 12, unification_result 13, transformation_result 14 |

Proposed display ladder: quiet includes measured values from zero through `cannibalism_meter.quiet` (20), active is above quiet and below `cannibalism_meter.severe` (70), and severe includes values from severe through the existing maximum (100).
Use documented inclusive `check_variable.compare` variants only at the two inclusive boundaries.
Parent reviews this presentation mapping before application, and a missing strength receipt always selects unknown rather than quiet.
No balance target, numerical loyalty, weight, probability, TTL, new cost, or dynamic gameplay multiplier is proposed.
Enums are identities rather than gameplay tuning.
The AI baseline specialist remains owner of any later probability-bearing patch and its mandatory comparison.

## Cleanup and migration order

1. State node retirement E:1676–1694 clears node-kind observation pairs before node IDs/source fields are erased.
Warning-only records remain distinct and retire only for their exact warning ID.
New node registration E:1649–1673 starts clean and cannot inherit an old warning's secret fields.
2. Actor unregister E:1631–1646 and slot release E:5600 onward retire subject observations and stale live selectors before actor/slot generations are cleared.
Public diplomatic identity rows may survive as public rows only when that country's current public classification remains valid.
3. Warning close `cannibalism_close_spread_warning_instance` ends only the expected spread record's active order or warning identity.
Queue removal/rebuild hooks at E:9985 onward clear observations for removed IDs before replacing inbound fields, preserving unrelated later warnings.
4. Viewer reset at E:3354 invokes indexed viewer cleanup before existing mission/policy reset, increments the persistent UI epoch, clears view selections and command arrays, and clears recipient history only after any accepted replacement transfer.
No reset restores epoch one over an existing epoch.
5. Actual `change_tag_from` branches E:12524–12532, E:12737–12748, and the original-ZZZ merge branches copy only the moving human viewer's validated receipts.
Re-key subject fields to the destination tag and its epoch, add destination membership, and remove source membership.
If two humans already occupy source and destination, never overwrite the destination human's private records or merge their intelligence implicitly.
The parent must use the actual surviving human/tag policy, retaining the storage commit's two-human behavior and reporting an unresolved policy if no unambiguous recipient exists.
6. Runtime reference migration E:12275 changes scheduling and gameplay pointers through its existing contract.
Observation provenance is neither silently reassigned to the unified host nor copied to other observers by this migration.
Source identity retirement makes former source snapshots stale, even if the scheduling host is rehomed.
7. Recipient command-host replacement copies all nine history arrays to the actual validated replacement before resetting the old recipient.
Donor annex/reset never clears the recipient's captured history.
No new history row is synthesized from a current reusable tag.
8. Network close at E:7088 clears selections and view arrays, retaining valid observations.
Command hide on ordinary/Wendigo replacement clears view state under existing gates and leaves historical retention to the recipient ownership rule.
Global cleanup E:2493 calls the UI owner cleanup from its existing bounded country-owner traversal, adding no world daily loop.

Implement pair cleanup while iterating an immutable transaction-local copy of the typed index, or defer membership removals until traversal finishes.
Never mutate an array being traversed in a way that skips adjacent records.
That copy's temporary outputs must be initialized by the caller before a helper returns them.
No numeric `for_loop_effect` over histories, countries, nodes, or states is proposed.

## Validation and remaining limits

Required application cases: two human observers with different secret knowledge of the same public country, observed zero strength versus unknown, warning without node, stale warning and recreated node, observer/source tag reuse, controlled-state loss before refresh, current CBA A integrated then reused CBA B, absorbed donor annexed, duplicate generation append, malformed nine-array alignment, actual autonomy/resistance/pending response, human tag transfer with an occupied destination, real campaign FROM distinct from view selection, and actual targeted raid commitment.
Use actual production helper paths with conservative temporary call-frame cleanup rather than mocked record writes.
Parent runs matching source scenarios and UI worker's source/scenario-matched MCP render/compare after application.

Current prep validates source contracts and installed syntax precedents, not executed proposed helpers.
GUI inspect summaries are source-linkage evidence, not populated visual or gameplay acceptance.
The connected tool list does not expose `hoi4.script_validate`.
Advanced jobs/helper expansion remain unused because live health/version/task negotiation was not verified.
Foreign report disclosure masks need review against the exact accepted outcome wording.
The march raid has no actual target in the current source and remains a decision-owner dependency.
External non-Event014 country incarnation detection for persistent campaign pointers remains unresolved.
The proposal contains no fallback or gameplay simplification, and none of E014-FINAL-02/03 is marked implemented by this prep.
