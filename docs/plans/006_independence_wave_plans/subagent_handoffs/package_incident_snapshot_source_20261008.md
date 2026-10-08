# Event 006 package-incident shown-snapshot source review

Disposition: owner implementation reviewed at source; native lifecycle acceptance remains open.
The parent applies the existing generation-owned incident and popup-lifetime contract within the full user-authorized Event 006 goal.
No new package, incident, choice, price, reward, timing tier or AI coefficient is designed by this repair.

## Source change and invariants

The two schedulers register a known package's current appointment and its original due date even when an earlier shown slot blocks delivery.
Original 65 A and 65 B mappings are retained by two selector helpers with caller-created temporary numeric-ID output.
Queue helpers require a scheduled current generation, known package, stored due date, no delivery/resolution and a free shown slot.
They calculate remaining hours from the original date, clamp past dates to zero and inject static native ID/hours values through meta_effect.
They never recreate or move an appointment date.

All 130 immediate blocks capture the matching shown generation/package before publishing delivered.
Both reply predicates compare shown proof with the current origin/package, and origin cleanup retains outstanding shown locks and snapshots.
Every event's after closes only its own slot independently of reply authority and may dispatch an already-registered current appointment.
No current delivery/resolution flag, generation or due date is cleared by stale closure.
A valid answer still resolves once and retains the existing A-to-B scheduling step.

Changed gameplay files are common/scripted_effects/006_independence_wave_package_incident_effects.txt, common/scripted_triggers/006_independence_wave_package_incident_triggers.txt and events/006_independence_wave_package_incident_events.txt.
The existing package_incidents.md overview and the new systems/package_incident_lifecycle.md record the API, defaults, inputs/outputs, side effects and use.
The owner index in chaosx_dynamic_effects.md links that event-owned API.
No localisation, sprite, event-log, evolution, scenario, workbook or export delta is required because every event ID, picture and option body remains unchanged.

## Meaningful regression evidence

The canonical baseline is evidence_20261008/package_incident_snapshots/frozen_before/ with its three raw hashes and captured-before-owner-patch manifest.
The exact baseline path has a scoped -text attribute so Git preserves those raw bytes; the selected tree's three blobs are checked against the manifest before publication.
The separate before/ folder was copied after a pending client reference call and is explicitly noncanonical; it is excluded from this source plan.
The parent interpreter executes the actual snapshot/queue/cleanup/reply bodies under a declared active-origin fixture, conservative temporary call frames and the documented shared date converter.
It records queued native meta-event ID/hour values without running the game.
The retained source_cases.py and clausewitz_subset_parser.py make that bounded regression runnable from the mod root.

| Case | Result |
| --- | --- |
| All package selectors | All 130 original package/event mappings preserved; every initial A/B dispatch retains 45/150 days and repeats register no second appointment. |
| All public content | All 130 event IDs and 260 option bodies byte-identical, including prices, effects, AI bases/modifiers and requirement guards. |
| Baseline stale reply | Original current-country predicate becomes true after replacement delivery; preserved shown generation/package rejects that stale authority after the patch. |
| Cleanup with shown A/B | Live receipts clear, shown proof survives, and replacement display remains blocked until that slot closes. |
| Date preservation | Closing old A thirteen days into a replacement appointment queues 768 hours, retaining the original date; the independent symmetric B case queues 3288 hours. |
| Slot independence | Old B closure preserves current A; a valid current A answer schedules B at its original 3600-hour delay. |
| Once and unknown package | Duplicate delivery/reply/closure before reuse grants no second work; unknown package creates no appointment. |

The [independent architect audit](package_incident_snapshot_audit_20261008.md) checks both cleanup callers, all 130 mappings/options and the post-patch source cases without source edits.
It finds no source-critical regression within the initialized-origin/current-appointment contract.
Neither model simulates native economy, timeout/country-disappearance behavior, zero-delay event ordering or arbitrary replay of a closed handler after its slot has been reused.
The latter cannot be distinguished by country scalars alone and is not claimed as a public repeatable API guarantee.
The normal default thirteen-day timeout versus 45/150-day appointments constrains natural overlap; no native exploit is asserted observed.

## References and MCP evidence

Installed effects_documentation.md 2943-2967 and 4833-4852, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, describes country-event delay and meta construction.
Offline Effects 900 and 4637-4670, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c, documents variable hours and numeric .0 meta arguments.
Offline Event modding 180-191, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d, describes immediate, after and first-option timeout.
Installed triggers_documentation.md 2110-2135, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, documents comparing normal variables.
The shared date-unit constants and conversion helpers retain exact whole-hour scaling and caller-owned outputs; their source was read directly.
Vanilla bftb_turkey.134 in events/BFTB_Turkey.txt around 5820 has an after block following its options; the exact source and additional citations remain in the independent audit.

The event file script check reports SCRIPT_CHECKED, 3468 commands checked and no findings under aggregate documentation revision 9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b.
Its checksPerformed are syntax, command_kind, declared_scope, player_text and event_popups; 901 native argument blocks and parameter semantics remain unchecked.
Effect/trigger file checks are partial: 12/5 roots have unknown inferred scope, 305/7 native blocks are unchecked and no command findings were returned.
An explicit COUNTRY reply snippet validates the native command kinds/scopes but keeps its custom can_fire helper unresolved and its two variable argument blocks unchecked.
Source lookup separately finds that exact non-shadowed helper at mod:common/scripted_triggers/006_independence_wave_package_incident_triggers.txt:8-12, revision 866d856bf2215897197f50f2438dec13a117db522430b7bfc4f78b94b4593c46.
These results do not establish native lifecycle behavior.

The architect's full file state-flow request timed out after 600 seconds, followed by a narrower focused trace that returned EVENT_INSPECTED_PARTIAL.
The parent neighborhood render for event 101 returns EVENT_RENDERED_PARTIAL at revision 5b61a45d5836c19fd276ef8a5e51b000c91b28ce24b8158b45c373319843902d and graph hash 037eb2eda9cdca709c30b78d69779582bcdfbcd9f3bd290b924567efd5839078, selecting six nodes.
The focused boundary indexes zero helpers and defers whole-workspace lifecycle passes; source inventory is limited inline to 64 of 404 paths.
The initial JSON was read locally and hash-verified as 13701357f4e13f3ec0866d0910f373e76930adfc8459a09f9dbb7098ace7502e, before cache eviction prevented continued artifact/image access.
A repeated bounded render was retained immediately under evidence_20261008/package_incident_snapshots/mcp_render/ as manifest, JSON, SVG and PNG.
The retained JSON has complete = false, twelve unresolved entries and 46249 omitted nodes; its six nodes are event 101, two options and unresolved capture, country-delta and close helpers.
Its event source hash exactly matches the current raw file at 0cdfe730fa131af45af5d1e358c1a0587f41d5f39d4146b3f75de00f8fb26b35.
The PNG was visually inspected as that bounded chain diagram and does not show native popup or helper execution.
The metadata archive retains both render results and the command-check limits, without expanding their coverage.
The requested comparison before revision db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5 returns EVENT_REVISION_NOT_CACHED with zero comparison artifacts.
A focused trace or source equivalence is not substituted for that missing helper/lifecycle comparison.

No implementation simplification or fallback was introduced.
Native popup lifetime, timeout/after ordering, country disappearance and zero-delay delivery remain open alongside the full Event 006 goal's package, asset, GUI, balance, catalog and completion gates.
Skills used: events, subagents and the shared Git workflow, with the existing generic popup/temporary-lifetime guidance.
