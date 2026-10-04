# Event 014 required GUI fields: data API plan

Disposition: accepted display requirements, proposed implementation, no gameplay patch.
Acceptance basis: the parent's 2026-10-03 read-only assignment preserves part 6's Network fields and command identity cards, and explicitly excludes new mechanics, costs, AI, balance algorithms, shared UI, commits, and workbook changes.
Parent owns data effects, scripted localisation, English text, integration, and implementation review.
UI worker `01a10256-c8c7-7741-a65d-834aa547216c` owns bounded layout/bindings for `cannibalism_network_window`, `cannibalism_warlord_command_window`, and `cannibalism_revealed_command_window`.
No worker message was sent.
The storage architect's helper preallocation hunks remain exclusively theirs, with parent Larder work following that commit.

Evidence: [source excerpts and SHA-256 revisions](2026-10-03_gui_required_fields_data_api_source_evidence.json) and [MCP requests/results](2026-10-03_gui_required_fields_data_api_mcp_evidence.json).
Line references below identify the inspected revision, not guaranteed positions after concurrent edits.
`E` means `common/scripted_effects/014_cannibalism_effects.txt`, `T` means `common/scripted_triggers/014_cannibalism_triggers.txt`, `SL` means `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`, and `D` means `common/decisions/014_cannibalism_decisions.txt`.

MCP outcome: Network `hoi4.gui_inspect` timed out after 600 seconds.
Warlord command inspection returned `GUI_INSPECTED`, shared revision `1bc3ab65a37c5cba0c4113f09476e2dd9ce2ef7a8b71425e2b15a7fc1638908c`, scenario `E014_DATA_API_WARLORD_20261003`, and 17 inspected elements.
Its [complete artifact](2026-10-03_gui_required_fields_data_api_warlord_mcp_inspect.json) was retrieved in bounded byte ranges and verified against SHA-256 `672db1565cca563505de83240bffd3bc39197fb018a1ebe83008f473aec5dc02`.
The identifier-only scenario leaves nine dynamic/visibility facts unresolved and three animation shader fields unsupported.
It establishes source linkage, not gameplay or visual acceptance.
Revealed-command inspection, the narrow event trace, decision inventory, and reference search returned no observed result before client observation ended, with server outcomes unresolved.
Reference context/read returned successfully, including installed GUI documentation lines 78–107 and its revision.
`hoi4.source_lookup` returned `INTERNAL_ERROR` / `Unexpected internal error` for the exact integrated helper.
Direct cited source reads cover the plan's syntax and data mapping, with the missing domain evidence left open.

## Findings that constrain implementation

E014-FINAL-02/03 remain real display gaps [audit lines 49–81](2026-10-03_event014_final_current_completion_audit.md).
The existing Network selections are actual viewer-country variables, set from native row indices at E:7108–7121, not decision targets.
The current filters at T:704–765 read the global actor/node registries without a viewer observation gate.
Global registration alone must not become foreign intelligence permission.

The inspected integration helper at E:12325–12334 retains per-slot disposition only.
Its commander/servant constructors briefly set name/origin/region/slot/personality on the recipient and clear them at E:12371–12375 and 12413–12417.
No integrated identity receipt arrays or integrated generation fields were found in the inspected Event 014 source, although the assignment describes an existing integrated receipt mechanism.
The global slot-generation table does exist, and generations are allocated globally at E:5173–5175.
**Parent synchronization gap:** re-read the integration ledger after the storage commit before adding fields.
If newer receipt arrays exist, bind to and extend those exact arrays rather than introducing the proposed array names below as a second registry.
The names below describe a narrow extension of `cannibalism_record_integrated_warlord_slot` only if this inspected revision remains current.

`cannibalism_march_raid_supply_depot` is non-targeted at D:2569–2587.
`cannibalism_begin_march_supply_raid_operation` pays for a country modifier at E:17109–17120 and never selects a depot/state/country.
An actual raid target cannot be recovered from that mechanic.
The required raid card must expose this absence honestly, with a separate explicitly selected view subject if the parent implements an information-only selector.
Changing the operation into a targeted raid would require separate design authority.

## Scope and native binding contract

| Surface | Native list contract | Actual retrieval scope |
| --- | --- | --- |
| Network country/state rows | Retain `cannibalism_network_country_dynamic_list` / `cannibalism_network_state_dynamic_list`, existing viewer-owned arrays, values and indices, `change_scope = yes` | `ROOT` is the viewer, `THIS` is the row country/state. Observation getters read this target's record for ROOT. A selected-card getter first enters the stored pointer. |
| Controlled states | Proposed `cannibalism_controlled_state_dynamic_list`, array `cannibalism_command_gui_state_entries`, value `cannibalism_command_gui_state`, index `cannibalism_command_gui_state_index`, `change_scope = yes`, container `cannibalism_controlled_state_entry` | ROOT is the commanding country, THIS is an actually controlled state. Never use the global controlled-state count as a row. |
| Integrated loyalty history | Proposed `cannibalism_loyalty_integrated_dynamic_list`, array `cannibalism_integrated_warlord_generation_entries`, value `cannibalism_loyalty_generation`, index `cannibalism_loyalty_index`, `change_scope = no`, container `cannibalism_loyalty_integrated_entry` | THIS/ROOT remain the revealed host. Value is a historical generation integer, not a country scope. Fetch aligned identity fields by this exact index. |
| Surviving warlord loyalty | Proposed `cannibalism_loyalty_live_dynamic_list`, array `cannibalism_command_gui_warlord_entries`, value `cannibalism_loyalty_country`, index `cannibalism_loyalty_country_index`, `change_scope = yes`, container `cannibalism_loyalty_live_entry` | THIS is a live registered warlord, ROOT is the revealed host. Render real disposition/pending response and actual name/portrait. Two adjacent native lists can form the loyalty section without combining incompatible scope types. |
| Raid / continental selected card | Proposed `cannibalism_raid_target_identity`, `cannibalism_continental_target_identity` and their `.tt` text elements | Owner country getter validates and enters its saved view/operation pointer, then prints that subject's name. A view selection never launches gameplay. |

Installed GUI documentation lines 15, 78–105 establishes player scope for decision categories, native array values/indices/scope changes, and dirty refresh.
Offline Scripted GUI lines 148–157 and 249–283 agrees, but warns that temporary data structures can fail in `decision_category` context.
Use regular owner-country arrays for attached command lists.
Build controlled-state rows through COUNTRY-scoped `every_controlled_state` with only `ROOT = { add_to_array = { cannibalism_command_gui_state_entries = PREV } }` as the row write.
This native iterator has no numeric 1,000-state loop cutoff and changes no gameplay state.
Run the builder on an information-only `cannibalism_command_refresh_click`, initial event-owned command entry/setup, and existing owned control-transfer handlers.
Recheck `is_controlled_by = ROOT` on row visibility/read even before refresh, so stale cards disappear immediately.
Do not put regular-array writes in a GUI trigger, add a daily scan, or use an unverified built-in `controlled_states` array.

## Network: target-specific observations

All names in this subsection are **proposed** unless explicitly marked existing.
Store observations on the target country/state, keyed by observer country with one `_@ROOT` suffix.
Writers enter through an explicit regular `cannibalism_ui_observer` target and an explicit `cannibalism_ui_subject_country` or `cannibalism_ui_subject_state` target.
Enter the observer country first, then directly enter the subject, so PREV is the observer.
At that exact child scope writers use `_@PREV`, and read `PREV.cannibalism_ui_viewer_epoch`, while GUI readers use `_@ROOT` for the same observer's tag.
Entering a country does not rebind ROOT, so a pulse anchor or absorbing warlord's ROOT must never supply the writer's observer suffix.
Avoid an extra scope layer between observer and subject, or pass explicit observer inputs rather than guessing a PREV chain.
The parent must validate that exact adapter context before adding its call.

For each target/observer record persist `cannibalism_ui_observer_epoch_@ROOT`, and country `cannibalism_ui_subject_generation_@ROOT` or state `cannibalism_ui_subject_node_id_@ROOT` plus `cannibalism_ui_subject_generation_@ROOT`.
The viewer owns positive `cannibalism_ui_viewer_epoch`, incremented by its existing incarnation reset.
On its first observation only, initialize a missing viewer epoch to `constant:cannibalism_gui_value.one` before storing the record, so an ordinary recipient without a prior Event 014 reset has a valid epoch.
Never reset an existing epoch to one during refresh or report delivery.
A state observation of an inbound warning without an active node instead stores `cannibalism_ui_subject_spread_id_@ROOT`, copied from the validated warning snapshot.
Keep warning and node identity validity distinct, so a warning row cannot claim an active node or its strength.
Maintain `cannibalism_ui_observer_countries` on the subject and `cannibalism_ui_observed_country_entries` / `cannibalism_ui_observed_state_entries` on the observer only to enumerate cleanup, with unique scope membership.
These are observation indexes, not replacements for actor/node/spread gameplay registries.
Extend `cannibalism_gui_rebuild_network_view` to filter existing actor/node candidates by these receipts, then append valid observed warning subjects from the viewer's state index if absent from the active-node list.
That union is necessary because a delivered inbound warning can precede node registration.
Recheck tab predicates separately from discovery and never enumerate undiscovered foreign subjects into the visible board.
For newest-first display, use native scope iteration with `add_to_array` front insertion (`index = 0`) instead of the existing numeric reverse loops at E:7038–7059, so a large node list cannot silently truncate at 1,000.
Keep ordering and uniqueness deterministic, with the same unknown/identity guards in both sort directions.

| Required field / reader | Actual existing data and scope | Proposed persisted observation / writer hook | Default and reset |
| --- | --- | --- | --- |
| Identity: `GetCannibalismUiNetworkIdentity` | Row THIS.GetName, state node ID/generation at E:1663–1664, actor generation, existing selected pointers | `cannibalism_ui_identity_observed_@ROOT` flag, plus identity/observer keys above. Set only for the report recipient, explicit inspected decision subject, or own known command subject. Filter rows by this receipt. | No row for undiscovered foreign subjects. Invalid generation returns `cannibalism_ui_identity_unavailable`, never a reused tag's identity. |
| Type: `GetCannibalismUiNetworkNodeType` | State `cannibalism_node_type`, existing SL:467–475 keys. Country stage at SL:456–463 is a stage, not a node type. | `cannibalism_ui_type_observed_@ROOT` flag + `cannibalism_ui_observed_node_type_@ROOT`. Snapshot only a directly inspected state. For country cards snapshot a specific observed node type only when the caller supplies that state, otherwise leave type unknown. | `cannibalism_ui_type_unknown`. Clear on record identity retirement. No arbitrary country-to-node type inference. |
| Strength band: `GetCannibalismUiNetworkStrengthBand` | State `cannibalism_node_strength`, country `cannibalism_cell_strength`, recorded at E:1666 / 10231 and maintained by existing effects | `cannibalism_ui_strength_observed_@ROOT` flag + `cannibalism_ui_observed_strength_band_@ROOT` and `cannibalism_ui_strength_observed_date_@ROOT`. Snapshot at a report/valid investigation result that actually reveals strength, or own command inspection. | `cannibalism_ui_strength_unknown`. Foreign pulse growth does not refresh the observer's band. The card labels a last observed band. |
| KNOWNROUTE: `GetCannibalismUiNetworkKnownRoute` | State `cannibalism_external_route_type` E:10319–10320, `cannibalism_inbound_spread_route`, country `cannibalism_external_infection_route` E:10240–10241 / 10271–10272. Existing spread-route IDs are 1–8. | `cannibalism_ui_route_observed_@ROOT` flag + `cannibalism_ui_observed_route_@ROOT` and observation date. Copy the exact state/route at delivered `.60` warning or `.61/.62` arrival report, after current warning ID/target checks. Never copy pending-route globals on opening the board. | `cannibalism_ui_route_unknown`. No route inferred from port/rail node type, inbound aggregate count, or warlord alignment route. Clear old incarnation route. |
| LASTINCIDENT: `GetCannibalismUiNetworkLastIncident` | Current report events `.2`, `.20`, `.21`, `.30`, `.60`, `.61`, `.62`, and exact decision/mission results. No target-specific latest incident field exists. | `cannibalism_ui_incident_observed_@ROOT` flag + `cannibalism_ui_last_incident_@ROOT` enum and `cannibalism_ui_last_incident_date_@ROOT`. Write at report `immediate` after its trigger passes, or a committed exact-target result. Record own-country event at country level. A state record needs an explicit state pointer. | `cannibalism_ui_incident_unknown`, meaning no incident observed. No claim that no incident occurred. Ignore stale callbacks. |
| SELECTEDCOUNTERACTION: `GetCannibalismUiNetworkCounteraction` | Real mission selections: investigation target state/node identity E:7665–7689, prison target E:7727 onward, reach-island country/generation E:7774–7776, break-network country/generation E:7825–7827, stop-unification E:7870–7872. Screening has exact state/spread ID E:10933–11034. Existing GUI selection merely chooses a view subject. | `cannibalism_ui_counteraction_selected_@ROOT` flag + `cannibalism_ui_counteraction_@ROOT` enum and `cannibalism_ui_counteraction_status_@ROOT`. Write only after mission start or successful payment/result, on that actual subject. Status is ordered/active/resolved/partial/failed/cancelled as supported by that action. | `cannibalism_ui_counteraction_none`, meaning no recorded order by this observer. Reset on incarnation/target invalidation. Mission clear ends active status, preserving last order and recorded result until superseded. No automatic action selected from card/tab or unrelated mission summary. |
| UNCERTAINTYLEVEL: `GetCannibalismUiNetworkUncertainty` | Report delivery and exact target checks. Country evidence is an aggregate, not per-node confidence. | `cannibalism_ui_identity_observed_@ROOT` and field-specific flags govern deterministic labels `unobserved`, `partial`, `observed`, `stale`. Partial means at least one required evidence field is unknown. Stale means identity/observer mismatch, not an invented age timer. Date belongs in the tooltip. | `cannibalism_ui_uncertainty_unobserved`. Never derive certainty from global reach or a generic stage label. An observed counteraction outcome does not confirm all intelligence fields. |

Use country flags for country observations and state flags for state observations.
The offline flags section documents country-tag targeting generically, but an exact installed state-flag `_@ROOT` precedent was not established in this pass.
Parent must validate that state-flag form before applying it, or use a reviewed meta-expanded flag name for the same observer contract.
This is an unresolved syntax validation item, not an implemented fallback.

Existing `GetCannibalismSpreadRouteLabel` at SL:256–328 reads live inbound/external country fields.
Add `GetCannibalismUiObservedRouteLabel` over the recorded route ID while reusing the existing eight route localisation values.
Do not call the live getter against an unrelated viewer scope.
Reuse SL's node type labels only after the observation flag/identity guard.
No hidden actor name, Hannibal portrait, personality, future route, or lore appears in pre-reveal Network records.

### Exact writer placement

`chaosx.nr14.60.immediate` already stores `cannibalism_warning_expected_spread_id` at events:270–283.
Append its observation adapter after that successful guard, using `ROOT` recipient and `event_target:cannibalism_spread_target_state`, and the exact inbound route.
It records an inbound warning, not successful spread or containment.
At `.61/.62`, record arrival against the existing recipient and state target once the report actually executes.
`.2/.20/.21` record country-level discovery/ritual/network incidents only, with state details only when a validated primary state is genuinely supplied.
`.30` can observe the named public warlord and origin identity through `cannibalism_warlord_new_country`, but does not reveal foreign numerical strength or secret strategy.

At E:10972–11034, write humane/hard screening order only in the payment-success block, before the caller closes its warning snapshot.
At investigation success/partial/failure E:7991–8027 and prison/island/network counterparts, write result before their existing `clear_*_mission` removes the pointer.
Reuse the matching target-validity triggers at T:1049–1107.
Forensic outcomes E:6197–6234 are country-scoped and only later call `cannibalism_record_investigation_operation`.
Keep their result country-level unless a validated mission state was already available in that transaction.
Do not retroactively assign a country result to whichever state is selected in the UI.
Observation hooks do not modify result pools, weights, mission progress, costs, timers, or eligibility.

## Command identities and selected targets

| Required record | Binding / proposed reader | Source, narrow persistence, writer and cleanup |
| --- | --- | --- |
| Controlled-state identity | `cannibalism.gui.controlled_state_entry` → `GetCannibalismUiControlledStateCard` | Native THIS.GetName, current owner/controller, existing `cannibalism_state_stage`, node type where present, and existing exhaustion/recovery flags. Rebuild owner view array with `every_controlled_state`, retain recruitment capacity as its separate existing display. Read population/recruitment eligibility through existing commands only if approved layout needs it. No invented per-state closure value. Lost control hides row and refresh removes it. |
| Raid view selection | `cannibalism.gui.raid_target` → `GetCannibalismUiRaidTarget` | There is no operation target in the inspected raid. Proposed owner vars `cannibalism_command_gui_selected_raid_state` and optional selected country + captured actor generation, mutually exclusive, set by an information-only row select using the actual native row value. Controlled-state selections show that named state. An existing targeted decision can supply its exact FROM if relevant to the card, labelled as that decision's subject. Never relabel recruitment/consumption target as a raided depot. Reset clears view selection. The no-target operation displays `cannibalism_ui_raid_target_unassigned`. This remains an explicit acceptance/implementation gap for a true raid target. |
| Continental selected target | `cannibalism.gui.continental_target` → `GetCannibalismUiContinentalTarget` | Targeted campaign uses actual FROM saved as `cannibalism_unified_decision_target` at D:2007, consumed at E:15223–15248. Proposed owner vars `cannibalism_command_gui_continental_target_country`, `cannibalism_command_gui_continental_target_operation`, `cannibalism_command_gui_continental_target_date`, and generation when it is an Event 014 actor. Capture the exact target after a committed campaign operation, before its regular event target ends. Show “Last prepared campaign” with name and date. No stable pre-click decision highlight exists in source. A separate view-only selection may show “Selected country” and must remain distinct from that operation receipt. No target defaults to `cannibalism_ui_continental_target_none`. |
| Continental target context | `GetCannibalismUiContinentalTargetContext` | A country may span continents. Show its actual capital state/continent only as capital location, rather than assigning the whole country to a guessed continent. Inactive/annexed ordinary country fails `country_exists` and clears live selection. Do not introduce an actor generation on ordinary human countries just for the UI. Event 014 reusable actors require their positive captured generation to match. |

Targets chosen by paid effects belong to those effects, not to GUI refresh or scorer order.
`cannibalism_get_unified_scored_targets` E:11683–11691 creates temporary AI-ranking arrays, not a player's selected country or a durable campaign record.
Do not call it to fabricate a continental target or alter target scoring.
The existing decision owner retains all target/cost checks.
For an optional view-only continental selection, add `cannibalism_command_gui_selected_continental_country` plus its captured Event 014 generation and `cannibalism_gui_select_continental_country_entry`.
Its input is a real displayed native country-row value, validated against that owner view's membership and object existence.
The information-only `cannibalism_continental_target_entry_select_click` sets that pointer and dirty value only.
The getter identifies this as a selection, while `cannibalism_ui_record_continental_target` retains the separate committed campaign receipt.
If no actual target row/selection exists in the worker layout, show the last committed campaign or the explicit empty selection, without inventing a pre-click target.

## Revealed loyalty list and historical identity

Reuse the existing `cannibalism_record_integrated_warlord_slot` owner and integration constructors.
If no newer integrated receipt ledger is available, extend that same record helper to append aligned country-owned arrays named:

- `cannibalism_integrated_warlord_generation_entries` and `cannibalism_integrated_warlord_slot_entries`.
- `cannibalism_integrated_warlord_name_entries`, `cannibalism_integrated_warlord_origin_entries`, `cannibalism_integrated_warlord_region_entries`, `cannibalism_integrated_warlord_personality_entries`.
- `cannibalism_integrated_warlord_origin_state_entries`, `cannibalism_integrated_warlord_disposition_entries`, `cannibalism_integrated_warlord_date_entries`.

All row values are integer IDs/enums except date, which uses the existing `global.date` representation.
The key is positive globally allocated donor `cannibalism_warlord_slot_generation`, with slot stored separately.
Repeated recording for the same generation is idempotent and cannot append a duplicate.
Use native `is_in_array` against the generation array for this membership check, avoiding an unbounded numeric history loop.
Never use slot alone as the historical key or replace an older row after a new CBA incarnation.
Validate equal array lengths and every row's positive generation before exposing rows.
No numerical loop over arbitrary history is needed to render: the native numeric dynamic list supplies the direct aligned index.
An invariant failure hides malformed rows and returns a truthful identity-unavailable value, without reconstructing lost identity from the live tag.

Capture generation and origin-state pointer directly from the donor while it still exists, before `cannibalism_prepare_current_warlord_slot_for_unification` or annex/reset.
For the opening host use `event_target:cannibalism_unification_host` before E:12560.
For later submissions use `event_target:cannibalism_absorbed_warlord` before E:12750.
Extend the destination's existing record call at E:12544 / 12711 with these two explicit donor inputs, avoiding edits to the storage architect's sixteen-output snapshot contract.
Existing transferred name/origin/region/slot/personality/disposition values are copied once into the row before constructors clear their working fields.

`GetCannibalismUiIntegratedWarlordName`, `GetCannibalismUiIntegratedWarlordOrigin`, `GetCannibalismUiIntegratedWarlordDisposition`, and `GetCannibalismUiIntegratedWarlordPortrait` read only the aligned historical row.
Reuse existing regional name keys and the portrait slot/region token vocabulary from SL:332–443.
Do not call current CBA.GetName/GetLeader/GetFlag or write temporary aliases into the host's persistent canonical identity variables.
The row's captured origin-state name and origin label identify its old territory without consulting the reset tag's map identity.
Portrait selection is the existing `GFX_portrait_<slot>_warlord_<region>` pairing from E:12350–12351.
All 56 regional finals and four protected Hannibal assets are supplied as installed by the parent, with no new portrait request or asset write.

For live loyalty, build `cannibalism_command_gui_warlord_entries` from `global.cannibalism_actor_countries`, filtered by `exists = yes`, active warlord classification, and positive current actor/slot generations.
Use live `cannibalism_warlord_disposition` for autonomous governor, resistant rival, or challenger, and `cannibalism_pending_absorption` for awaiting response.
Autonomy/resistance writers exist at E:12779–12836.
Do not infer loyal percentage from alignment, or force these surviving countries into an integrated-history row.
`GetCannibalismUiLiveWarlordDisposition` returns the actual discrete relationship.
The list is gated by the existing revealed ordinary-host visibility, including exclusion of the Wendigo route.
Historical integrated rows survive donor annex/slot release. Current autonomy/resistance rows disappear when the actor disappears or changes generation.

## Proposed helper map and output lifetime

| Helper / location | Scope and inputs | Outputs, defaults and side effects / call sites |
| --- | --- | --- |
| `cannibalism_ui_record_country_observation` / `cannibalism_ui_record_state_observation`, E | Explicit observer + typed subject regular event targets, caller-supplied observation kind/field values, expected generation or warning ID | Persistent observed flags/fields and cleanup membership on exact subject/observer only. Missing input skips writing, not unknown-to-known promotion. Call from delivered report/committed result adapters above. No temp return is required. |
| `cannibalism_ui_clear_country_observation` / `cannibalism_ui_clear_state_observation`, E | Subject + explicit observer | Clears all this observer's flags/fields and membership. No gameplay cleanup. Invoked by retirement and viewer reset through existing recorded observation scope indexes. |
| `cannibalism_gui_validate_selected_network_target`, T | ROOT viewer, existing selected country/state plus proposed `cannibalism_network_gui_selected_generation` and state `cannibalism_network_gui_selected_node_id` or selected warning ID | Boolean trigger only. Check pointer presence, country existence where applicable, exact positive identity and observation epoch. No `scope_exists` on variables. Use in selected-card visibility/getters and before selector reads. |
| `cannibalism_ui_load_network_observation`, T | THIS target, ROOT viewer | Temporary `cannibalism_ui_row_valid`, `type`, `strength_band`, `route`, `incident`, `incident_date`, `counteraction`, `counteraction_status`, `uncertainty` prefixed `cannibalism_ui_row_`. Each caller initializes **all** consumed outputs inline to zero/unknown before invoking it. Missing flags remain unknown. No regular writes from triggers. |
| `cannibalism_gui_rebuild_command_view`, E | Owner COUNTRY, current controlled states and registered warlord array | Rebuilds regular command view arrays and bumps `cannibalism_command_gui_dirty`. Clears invalid live selections. Call on command setup, view refresh, existing owner transfer/operation adapters. No gameplay outputs. |
| `cannibalism_gui_select_raid_state_entry`, E | GUI ROOT owner, native `cannibalism_command_gui_state_index` | Validate index and state control, set `cannibalism_command_gui_selected_raid_state` from the actual array element, clear the mutually exclusive country choice. Information-only click `cannibalism_controlled_state_entry_select_click`. No operation launch. |
| `cannibalism_ui_record_continental_target`, E | Commanding country + validated existing `cannibalism_unified_decision_target`, committed operation kind | Persistent last campaign subject/date/operation plus Event 014 generation when needed. Call after E:15223 campaign commit. Does not alter payment or target flags. |
| Extend `cannibalism_record_integrated_warlord_slot`, E | Destination COUNTRY, existing integration fields + explicit donor generation/origin-state inputs | Idempotent aligned historical receipt in existing owner. No gameplay changes, no temp return. Record before donor release. Prefer any newer parent's actual integrated ledger names over proposed aliases. |
| `cannibalism_ui_load_integrated_warlord_row`, T | Revealed host, native `cannibalism_loyalty_index` and `cannibalism_loyalty_generation` | Temporary `cannibalism_ui_loyalty_valid`, `generation`, `slot`, `name`, `origin`, `region`, `personality`, `origin_state`, `disposition`, `date`, all prefixed `cannibalism_ui_loyalty_`. Caller initializes each output inline before call. Validate lengths/index/value. No country-scope change for numeric rows. |
| `cannibalism_ui_clear_command_view`, E | Owner COUNTRY | Clears view arrays, raid/continental live selections, dirty/open view flags. Incarnation reset, revealed branch replacement, terminal hide/cleanup. Integrated history cleared only when its recipient incarnation is reset, or copied to an accepted replacement recipient before clearing. |

Reader outputs are unscoped temporary values.
Never prefix them with ROOT/PREV, initialize them first inside their returning helper, or assume an outer caller inherits a nested getter's allocations.
In `defined_text.text.trigger`, allocate the temporary fields in that trigger before calling the loader, then select a literal `.yml` key.
Formatting and composite text live in `.yml` values, not inline dynamic `localization_key` strings.
For numeric lists, fetch each row inside its own localisation/property evaluation, so one card cannot reuse another row's temporary values.
Do not create persistent globals solely for display formatting.

## Binding-friendly localisation and constants

Parent adds these presentation keys, with field readers above supplying their values:

`cannibalism.gui.network.country_entry`, `.state_entry`, `.selected_target`, `.selected_target.tt` retain their identifiers and receive the full records.
Add `cannibalism.gui.network.node_identity`, `.node_type`, `.strength_band`, `.known_route`, `.last_incident`, `.counteraction`, `.uncertainty` for separate worker text bindings.
Add `cannibalism.gui.controlled_state_entry`, `.controlled_state_entry.tt`, `.raid_target`, `.raid_target.tt`, `.loyalty_integrated_entry`, `.loyalty_live_entry`, `.loyalty_entry.tt`, `.continental_target` and `.continental_target.tt`.
Existing `.continental_target` is rewritten around actual selected/last campaign identity, retaining the key.
`cannibalism.gui.warlord.capacity` remains recruitment capacity, and `.warlord_loyalty` becomes a section heading rather than an aggregate substitute.

Unknown keys: `cannibalism_ui_identity_unavailable`, `cannibalism_ui_type_unknown`, `cannibalism_ui_strength_unknown`, `cannibalism_ui_route_unknown`, `cannibalism_ui_incident_unknown`, `cannibalism_ui_counteraction_none`, `cannibalism_ui_raid_target_unassigned`, `cannibalism_ui_continental_target_none`.
These describe missing observations/selections explicitly and must not masquerade as successful implemented records.
Add literal enum labels under `cannibalism_ui_strength_*`, `cannibalism_ui_uncertainty_*`, `cannibalism_ui_incident_*`, `cannibalism_ui_counteraction_*`, `cannibalism_ui_action_status_*` and `cannibalism_ui_loyalty_*`.
Incident enum labels describe the delivered discovery/ritual/network/emergence/inbound-warning/arrival/reinfection/investigation/screening result, without revealing an actor behind it.

In existing `common/script_constants/014_cannibalism_constants.txt`, reuse `cannibalism_spread_route`, `cannibalism_node_type`, `cannibalism_warlord_disposition`, `cannibalism_gui_value`, and `cannibalism_meter` thresholds.
Proposed display categories `cannibalism_ui_strength_band`, `cannibalism_ui_uncertainty`, `cannibalism_ui_incident`, `cannibalism_ui_counteraction`, `cannibalism_ui_action_status` contain integer enums only.
Suggested strength presentation uses existing quiet/active/severe boundaries, with mutually exclusive intervals and unknown separate from a genuine zero strength.
This is a proposed presentation mapping, not new tuning or a balance change.
No weights, probabilities, TTL, freshness duration, numerical loyalty meter, or closure field is added.

## Cleanup, migration and parent validation

1. After the storage architect commit, refresh source evidence and reconcile the claimed newer integration receipt arrays with the inspected per-slot implementation.
Parent applies this plan only after that reconciliation.
2. Document event-owned helper contracts in `docs/events/014_cannibalism/gui_data_contract.md` and index them in `common/scripted_effects/chaosx_dynamic_effects.md`, following its existing owner-owned API section.
Do not add a central router or duplicate generic dynamic helper.
3. Attach report/result observation writers before their target pointers/working snapshots clear, preserving all existing decisions and outcomes.
Add exact selected identity fields at E:7108–7121 and their reset at close/reset.
4. Add command view builders and direct target capture, then bind the named native lists/getters with the UI worker's accepted layout through parent synchronization.
5. On state node retirement E:1676–1694, clear that node identity's observation flags/fields through its observer index before clearing IDs.
On new registration E:1649–1673, initialize empty observation membership and never carry old evidence into the new generation.
Inbound-warning-only records retire with the exact warning/spread ID, not with an unrelated later warning.
6. On actor unregister E:1631–1646 and reusable slot release E:5600–5698, retire live observations/selections before clearing generations.
On viewer incarnation reset E:3354 onward, clear its indexed country/state observations and command selections, and increment its epoch.
GUI close clears selections and view arrays, preserving still-valid observations.
7. On absorption/reference migration E:12275 onward, keep historical integrated identity immutable.
Invalidate the old live country observation rather than exposing the recipient through the old identity.
If the human viewer changes tag, copy only that viewer's observation records/indexes to the actual destination with its new epoch, clearing the source after transfer.
Do not transfer one country's private intelligence to every observer.
8. Pulse callback rehome E:1787–1850 moves scheduling responsibility only and must not move intelligence ownership.
An actual command-host replacement must explicitly copy the integrated receipt ledger to the validated replacement host before its old recipient reset.
Ordinary/Wendigo replacement hides these three windows under their existing gates and clears their view selections, retaining history only where the accepted owner lifecycle retains it.
Global victory/world end hides windows and invokes existing bounded owner cleanup, with no new world iteration.

Meaningful parent cases: two human viewers with different knowledge of the same foreign node, delivered warning with no active node, stale warning callback, node retirement/recreation at the same state, observer tag reuse, CBA generation A integrated then CBA generation B formed, absorbed donor removed, autonomy/resistance/pending response rows, malformed aligned receipt arrays, controlled-state loss before refresh, non-targeted raid with no fabricated target, exact campaign FROM surviving event-chain end, empty/crowded lists and long real regional identities.
Each case must prove displayed record provenance, not just a raw value assignment.
UI worker retains source/scenario-matched MCP inspect/render/click-region comparisons, while parent validates writer/read/reset contracts.
Do not claim focus, map, probability, engine runtime, or visual validation from this document.

Completed here: bounded source/reference review and an explicit ownership/lifecycle/binding plan.
Skipped: gameplay implementation, localisation changes, assets, workbook, commits, worker communication, game launch, runtime tests, balance changes, probability audits, and layout renders, by the read-only assignment and UI-worker ownership.
Blocked/unresolved: MCP inspection results as recorded in the evidence file, exact state-flag targeting validation, the claimed newer integrated receipt ledger, and a gameplay raid target absent from inspected source.
No gameplay simplification or fallback was applied.
This handoff does not mark E014-FINAL-02/03 implemented or Event 014 complete.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and relevant read-only context from `chaos-redux-scripted-gui`.
No skills were created or updated.
Files written are this handoff, its two cited evidence JSON files, and the verified warlord MCP inspection artifact in this same folder.
Task-specific review confirmed all required field groups have data/writer/reset/read contracts and the archived inspection bytes match the returned artifact hash.
All cited Event 014 source hashes still matched at the final read, with later shared-worktree changes requiring parent synchronization.

## Parent reconciliation, 2026-10-04

`superseded` for the Network fields by agent decision D5 and `docs/events/014_cannibalism/gui_data_contract.md`; the command-window data remains `accepted and queued`.
