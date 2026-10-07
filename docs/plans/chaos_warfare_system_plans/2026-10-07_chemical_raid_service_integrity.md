# Chemical raid action-record integrity

Disposition: bounded caller-storage source implementation reviewed; committed dependency integration and native outcomes remain incomplete.
Acceptance basis: the approved CBRN overhaul requires one reliable native raid execution path, exact resource accounting and no duplicate outcomes.
The parent authorized the [chemical caller-storage patch](subagent_handoffs/2026-10-07_chemical_raid_lifetime_patch.md) from the reviewed action-record audit and insertion map.

## Source behavior

Six runtime files contain 206 scalar declarations and one temporary-array initializer in nine insertion blocks.
The changed files are `common/scripted_effects/cbrn_chemical_land_raid_effects.txt`, `cbrn_chemical_raid_effects.txt`, `cbrn_chemical_doomsday_effects.txt`, `cbrn_protection_effects.txt`, `cbrn_consequence_effects.txt` in that directory, and `events/cbrn_doomsday_raid_bridge.txt`.
The native land, air and exact-state doomsday owners retain the complete existing 60-field action packet across returning reset, classification, preparation and dispatch helpers.
Air owns the returned result and native reservation/release proofs, while its failed-attempt path owns consequence and attribution outputs.
Protection owns its six class weights before the producing helper returns.
The accepted consequence branch owns context, evidence-floor and civilian-death outputs before using them.
The doomsday release owns its exact target count/array, captured arsenal, condemnation total/share and bridge release status.

Only fresh operation owners initialize dispatch proof.
The actual dispatcher keeps its accepted, paid, bound-target and not-yet-dispatched checks and sets proof before applying consequences.
No missing weather, target density, forecast, protection, payload or release input is converted into a supplied proof.
Every original statement and its order is preserved when the exact inserted spans are removed.
No price, payment/refund, target, policy, profile formula, random draw, native callback order, asset or player-facing choice is changed.
Native essential-equipment collection remains engine-owned; the exceptional doomsday remaining-stock debit retains its existing separate contract.

## Meaningful regression evidence

The parent reran `node docs/testing/2026-10-07_chemical_raid_lifetime_source_tests.js` and reviewed the [independent handoff](subagent_handoffs/2026-10-07_chemical_raid_lifetime_source_checks.md).
All 18 bounded cases pass.
They reconstruct all eight captured before sources byte-for-byte after removing the insertions, preserve their ASTs, and compare current sources against the after archives allowing only newline conversion.
The archived raw bytes are protected by local Git attributes.

The three complete-record owners retain all 60 fields instead of losing their returned packet.
Actual Chlorine classification, cylinder severity and 40-unit payload getters retain their results; the successful air reservation chain retains its returned receipt and consumption record.
Four protection-class probes retain all six actual weight outputs.
Within one prepared caller frame, two dispatcher calls produce one captured history application after the repair; the baseline loses proof and applies two.
Rejected, unpaid and unbound source records reach no consequence sink.
The failed-attempt probe retains 20 evidence points, a 35-point floor and eight Condemnation points, advances its fixture evidence from 50 to 70 and retains probable attribution; it records one attempt rather than two.
Doomsday probes retain exact target count/array, remaining-stock debit accounting and condemnation/share outputs, and the event bridge retains the result needed by its conditional news branch.

These are source-semantic observations, not proof of native payment, deaths or callback uniqueness.
Full-record probes execute owner prefixes; actor/target eligibility, selected context and several consequence/history sinks are explicit fixtures.
The death sink returns a declared fixture value, so the suite does not certify actual casualty arithmetic or full damage/protection balance.
Doomsday targets are supplied exact-state fixtures, and its four already-native-reserved units are assumed rather than collected by an engine.
Full multi-state remainder allocation is not executed.
Air outcome RNG, native cancellation, target loss, war termination and final engine equipment disposition remain unverified.

## Shared-tree dependencies and remaining consumers

The working baseline already contained eighteen exposure-profile allocations, six generic protection-output allocations and two payload-authorization metadata allocations.
Those 26 declarations are preserved and not attributed to this patch.
The exposure file and the untracked `common/scripted_effects/cbrn_payload_reservation_effects.txt` are byte-unchanged.
Only the six new weight declarations belong to this patch in the already dirty protection file.
The tests include those current working dependencies; they do not prove that a committed checkout contains the untracked reservation source or the other owners' dirty changes.
The isolated commit must retain only this patch's hunks and leave those dependencies for their owners to integrate and validate.
The current [chemical reservation contract](../../systems/cbrn_warfare/chemical_payload_reservations.md) and [Event 032 receipt review](../032_missiles_plans/subagent_handoffs/032_chemical_receipt_review_2026-10-07.md) identify that integration surface; the manual receipt review does not replace executable or native stock evidence.

`missiles_dispatch_chemical_payload`, `missiles_check_chemical_payload_stock` in `common/scripted_effects/032_missiles_operations_effects.txt`, and `camp_rework_apply_chemical_escalation_in_action_state` in `common/scripted_effects/camp_repression_rework_effects.txt` remain queued caller contracts.
Their current source must be reconciled against the [insertion map](subagent_handoffs/2026-10-07_chemical_action_lifetime_insertion_map.json), preserving the missile owner's durable receipt work.
They were not patched or validated by these eighteen cases.
The proof tested here prevents repeated dispatch within the same prepared source frame; it is not a persistent replay identifier for distinct native callbacks.

## MCP and native acceptance

Offline Data structures lines 435-443 and installed `set_temp_variable` documentation lines 7820-7827 establish the caller-ownership contract; source revisions are recorded by the patch handoff.
Installed raid documentation remains the payment, callback-scope and exact actor/target authority.
The earlier bounded land-bridge trace was partial and its complete artifact was not read.
The attempted trace-revision comparison returned `EVENT_REVISION_NOT_CACHED`.
The [MCP route review](subagent_handoffs/2026-10-07_mcp_event_comparison_route_review.md) identifies the cause: graph references require a scan graph, and a trace is only a report.
A future canonical comparison must retain the scan's `event-graph-<revision>.json` artifact; an archived-source overlay can provide only an explicitly reversed comparison against current source.
Current domain comparison/render coverage and native execution remain open.
The [chemical probability audit](subagent_handoffs/2026-10-07_chemical_raid_lifetime_probability.md) submitted the five existing RNG getter locations to the direct-random adapter; all returned no candidate and no required inputs.
The unchanged getter segment and bounds have identical before/after/current normalized hashes, but no numeric distribution or native outcome chance is claimed.
The separate incubation archived-source overlay comparison timed out after 600 seconds without a backend task handle; a second full graph overlay for chemical source was not started while its backend completion remained unknown.
No gameplay simplification or substitute mechanic is introduced.
The broader CBRN goal remains incomplete.
Skills used: events, native raids, subagents and shared Git commit.
