# Event 023 scripted-system architect handoff

Disposition: **blocked** for native detonation delivery and callback confirmation.
The bounded fail-closed repair and delivery preflight are implemented.
Acceptance basis is the parent assignment's explicit instruction to fail closed when an exact callback design cannot be proven.
This is not a completion claim for Event 23.

## Engine blocker and resulting behavior

Installed `documentation/effects_documentation.md`, `launch_nuke`, documents state/province, controller, use_nuke, and nuke_type arguments.
It provides no scripted success return, request identifier, cancellation operation, or caller nonce argument.
The offline `On actions` page documents `on_nuke_drop` with ROOT as launcher and FROM as struck state.
Neither that contract nor the installed vanilla callback exposes the originating request nonce or action type.
A copied country/state nonce proves the stored request's identity but cannot distinguish its callback from another native or scripted launch by the same country at the same state.
There is also no documented synchronous-callback guarantee that would make a flag around `launch_nuke` an authenticated receipt.

Consequently, `sov_nuclear_bombs_execute_shared_action` rejects test, demonstration, combat strike, and accident before issuing `launch_nuke`.
It returns rejection reason `confirmation_unavailable = 11`, releases the unlaunched reservation once, and never sets an accepted receipt or expended ledger entry.
The former native invocation has been removed from the executable path, rather than retaining a launch that cannot safely be accounted.
No replacement delivery route or direct consequence call was introduced.
This blocks actual limited Evolution II use as well as Evolution IV use, despite preserving both authorization predicates.
That omission follows the explicit fail-closed instruction and remains an engine blocker.

Non-detonating demolition remains executable through the same reservation/commit contract.
Acceptance is stamped only after its reservation is committed.
Its receipt requires the committed nonce and cannot be recorded twice.
The existing native on_nuke_drop hook remains the only detonation-consequence entry point and was not edited.
It continues observing foreign strikes, but does not authenticate Event 23 outbound delivery.

## Exact files changed

- `common/script_constants/023_sov_nuclear_bombs_constants.txt`
- `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`
- `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`
- `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`
- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`
- This handoff.

No events, decisions, localisation, shared consequence files, Event 5 source, assets, workbook, or other documentation were edited.
No commit was created because native delivery remains blocked and these runtime files already contained parallel work.

## Helper map and call sites

| Helper | Scope and input | Output and side effects | Call sites |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_event_has_delivery_route` | Country, current technologies, deployed bombers, fuel, owned controlled states | Boolean preflight and temporary numeric inputs for meta_trigger | Existing route consumers and local capability wrapper |
| `sov_nuclear_bombs_event_state_has_delivery_access` | Exact target state, PREV must be launcher country | Boolean endpoint/range/access result, temporary range input, no persistent target mutation | Targeted selection wrapper and runtime delivery validator |
| `sov_nuclear_bombs_event_has_targeted_delivery_route` | Country, selected-state event target | Calls exact-state preflight | Existing limited/major target predicates |
| `sov_nuclear_bombs_event_has_local_delivery_capability` | Country | Reuses generic delivery preflight | Existing breakaway delivery consumers |
| `sov_nuclear_bombs_action_delivery_route_is_valid` | Country, action state/target/type/detonation fields | Exact endpoint preflight for detonation, non-detonating validation for demolition | Runtime action context |
| `sov_nuclear_bombs_action_can_commit` | Country, valid action context and active reservation | True only for non-pending, non-detonating demolition | Shared execute and commit helpers |
| `sov_nuclear_bombs_action_receipt_is_valid` | Country, accepted committed nonce/type and recorded nonce | Boolean one-shot demolition receipt gate | Event-owned receipt recorder |

Changed effects are `sov_nuclear_bombs_stage_action_context`, `sov_nuclear_bombs_record_action_receipt`, `sov_nuclear_bombs_reserve_device_for_action`, `sov_nuclear_bombs_release_reserved_device`, `sov_nuclear_bombs_commit_reserved_device`, `sov_nuclear_bombs_execute_shared_action`, `sov_nuclear_bombs_clear_action_context`, and the action-pointer cleanup in `sov_nuclear_bombs_cleanup_annexed_actor`.
The action context and no-active-action triggers also reject an unresolved native-pending marker.

Staging preserves an existing reservation instead of rewriting its state, source, holder, type, and nonce.
Fresh staging clears stale action_state and requires an explicit selected endpoint instead of substituting the capital.
Target controller/owner and country ID are captured in their actual state/country scope before assigning the root actor's variables.
Reservation activation now requires a source bucket to have actually supplied the device.
Runtime availability accepts exactly one remaining device and recognizes a remote transferred-device holder's reserved bucket.

## Delivery thresholds and documented references

New category `sov_nuclear_bombs_delivery` contains `deployed_bomber_floor = 0`, `airbase_level_floor = 0`, `minimum_fuel = 1000`, and `maximum_state_distance = 1000`.
Bomber and airbase checks are strict greater-than comparisons, fuel is inclusive at 1000, and distance is strictly below 1000.
The radius is an Event 23 preflight ceiling, grounded in the installed inter-war large airframe's base `air_range = 1000`, not a measurement of the active wing's modified range.
No receipt timing constants were added because no safe timeout can prove that a native request failed.

The route requires atomic_research and nukes, strategic_bomber1 or the existing By Blood Alone iw_large_airframe branch, deployed strategic_bomber aircraft, and an owned and controlled state with an airbase.
That airbase must satisfy `distance_to = { target = PREV.PREV value < ... }` against the exact endpoint.
Only the launcher's owned and controlled states are enumerated.
Numeric constants are loaded into temporary variables and injected with documented meta_trigger syntax because direct constant-token support in these static numeric fields is not documented.

Installed vanilla root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

- `documentation/triggers_documentation.md`: distance_to at 2596, has_deployed_air_force_size at 3720, has_fuel at 3957, has_tech at 4882, meta_trigger at 6404, and num_of_nukes at 6813.
- `documentation/effects_documentation.md`: launch_nuke at 4745, event-target save/clear documentation at 6496/6505/2733.
- `documentation/script_concept_documentation.md`: Script Constants at 216 and Formatted Localization at 161.
- `common/script_constants/documentation.md`: schema and scoped constant access.
- `common/scripted_effects/SOV_scripted_effects.txt`: distance_to precedent at 9833.
- `common/technologies/electronic_mechanical_engineering.txt`: installed nukes technology at 1832.
- `common/special_projects/projects/nuclear_projects.txt`: sp_nuclear_bomb output grants nukes at 487.
- `common/technologies/air_techs.txt` and `bba_air_techs.txt`: strategic_bomber1 and iw_large_airframe.
- `common/units/equipment/plane_airframes.txt`: large_plane_airframe_0 base range at 2567.
- Offline wiki: Data structures event targets, Triggers distance_to/deployed aircraft/meta triggers, Effects launch_nuke, Scopes, Localisation, and On actions on_nuke_drop.

The required core wiki pages, current Event 23 targeting/evolution/shared-contract/technology specs, existing dynamic-effect registry, and runtime-effect Markdown were consulted.
No technologies, aircraft, missiles, thermonuclear capability, fuel, map data, or world loops were added.

## Pending envelope, cleanup, and migration

The requested future envelope would need launcher, exact state, nonce, type, weapon, reservation source/holder, and a native request identity echoed by the callback.
The final field has no documented implementation, so no pretend envelope, timer, or callback confirmation was added.
A stored nonce must never be presented as native correlation proof.

An existing `sov_nuclear_bombs_native_delivery_pending` marker is preserved.
Staging, execution, commit, refund, and action-context cleanup cannot overwrite or release it.
Execution reports `delivery_unresolved = 12`.
No automatic timeout or native-bomb refund is inferred.
Such a marker requires parent investigation and an evidence-backed recovery disposition, including any state-custody changes, rather than a guessed refund.
The patched path creates no new pending delivery, so rejected requests do not leave reservations behind.

The existing selected-state event targets remain selection UI pointers.
Persistent action variables preserve the staged request independently.
`sov_nuclear_bombs_recorded_action_nonce` is durable receipt history and must not be cleared with transient action context.

Migration is local: existing callers keep their public effect names, selected-state and runtime checks converge on one endpoint helper, premature native commit is removed, and event receipt creation uses the committed one-shot gate.
The major first-use severe gate, runtime major-first-use guard, and limited-strike predicate are structurally unchanged from the captured task baseline.

## Validation and output

An in-memory source-driven Clausewitz subset model parsed the five runtime files and evaluated 15 adversarial fixtures, with output `15 passed, 0 failed`.
Fixtures cover valid endpoint, fuel 999/1000, missing deployed bomber, missing bomber technology, lost airbase control, distance 999/1000, missing atomic capability, all four detonating action types rejecting with reservation conservation and no native spend, last-device demolition committing once, duplicate receipt rejection, unresolved-pending preservation, and absent global backing producing no phantom reservation.
Initialization and reconciliation effects were treated as fixture setup/no-ops, distance and deployed-unit data were explicit fixtures, and this model is not the HOI4 engine.
Three baseline-versus-final AST comparisons confirmed unchanged severe-first-use, limited-strike, and runtime major-first-use predicates.

MCP evidence:

- Focused event trace revision `a755267db440a679119926da6b160e610a2ba4573a57f5f2aad4cabc18143b21`, artifact `event-trace-a755267db440.json`, SHA256 `63f7a2ff9c1947b895206700c17cc384b29474f343080f5bc13b42ab8e7d9e81`.
- State render `event-state-a755267db440.json`, SHA256 `03b79bc316a624d01afb6b53fbedf3df78c75d6a02385c4ecc1197c68c3ba60a`, and companion SVG/PNG were returned.
- Full state_flow revision `c85b7ba8f6e49bdb3d3c97625f5406ad6d0479b36a43b3eb0eb8ed4aae270520`, artifact `event-state_flow-c85b7ba8f6e4.json`, SHA256 `56bb778c6089a26f02b95dfbec11d8bad8ec2e3c5e98ab7de413551cfa134fda`.
- Full inspection indexed 19,086 helpers over 3,942 sources but returned 3,928 blocking event-chain diagnostics, so it is not a clean lifecycle validation.
- Post-change event_compare with the full baseline revision returned `EVENT_REVISION_NOT_CACHED`, message `Requested event graph revision is not cached`, with no comparison artifact.
- Initial probability_inspect found the three receipt-pool candidates after reporting identifier_not_found for the effect name, artifact `probability-inspect-f61e7be135de.json`, SHA256 `2c358741e0fdfd4531cfa5c498b446856e5ae022746a98256a3b543ba608475f`.

Focused trace/render disable helper lifecycle analysis and do not validate the runtime helpers.
The read-only `chaosx_ai_probability_auditor` returned inspection artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18e13d756ebfa916642051ec2b5e609ebaf494fac73881963999289c2680d79b/510158a8fee6e3e1219448d13821bf3d2bb6b39e063f46b7ac72771b68e259cc/probability-inspect-f61e7be135de.json`.
Its source revision was `8dada14529cbf68d1a7e7f0403e4c66b18fec48652ffdb98638a4c31cb168a1d`, which differed from the supplied earlier baseline revision.
It confirmed the conditional receipt-pool weights remain 70/20/10, but returned no successful probability_compare artifact.
The required same-scenario probability comparison is therefore incomplete, not a passed audit or a proven probability-service outage.
The named delivery scenarios remain unresolved at the outer trigger/callback layer.
No clean MCP comparison, live-game proof, mission-basing proof, interception proof, or actual aircraft-range proof is claimed.
HOI4 was not launched.

## Remaining work and documentation ownership

The engine exposes no documented generic actual-air-superiority trigger or generic strategic-bomber mission/basing query in the inspected current trigger documentation.
Fuel, owned controlled airbase access, and bounded state distance therefore remain documented preflight checks with explicitly limited reach.
Country-wide deployed bomber presence does not prove that those aircraft are stationed at the qualifying airbase.

The parent must reconcile unavailable detonation actions and their costs/tooltips in its separately owned decision, event, and localisation surfaces.
The matching `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` still describes launch invocation as the commit point and needs parent correction.
It was intentionally not edited because the assignment permits only the five runtime text files and this handoff.
This handoff documents the changed helper contracts pending that integration.

Skills used: chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents.
No skills were created or updated.
The remaining blocked functionality and validation gaps above are explicit, with no silent simplification or substitute consequence route.
