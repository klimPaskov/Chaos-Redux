# Chemical raid action-record integrity

Disposition: bounded raid caller-storage source implementation reviewed; shared dependencies committed; remaining Camp/missile declarations implemented and parent-reviewed; native outcomes remain incomplete.
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

The historical working baseline contained eighteen exposure-profile allocations, six generic protection-output allocations and two payload-authorization metadata allocations outside this patch's ownership.
At that capture the reservation API was untracked and neighboring dependencies were dirty; those facts remain baseline provenance, rather than current integration blockers.
Peer commit `5793df4345a413dcf7cadf5aeae99597a859020a` and follow-up `0dc5df3f11da5639e79752591cf78781b7da4d43` are ancestors of the reconciled HEAD and publish the exposure outputs, generic protection outputs and `cbrn_payload_reservation_effects.txt` API.
Current HEAD retains the six private protection weights from `611cbb63`.
The [missile follow-up](subagent_handoffs/2026-10-07_missile_cbrn_caller_followup.md) records this dependency coverage without attributing peer custody work to the raid patch or certifying its complete transactions.
The [chemical reservation contract](../../systems/cbrn_warfare/chemical_payload_reservations.md) and [Event 032 receipt review](../032_missiles_plans/subagent_handoffs/032_chemical_receipt_review_2026-10-07.md) remain receipt evidence rather than native stock proof.

The [remaining-caller report](2026-10-08_remaining_chemical_callers.md) records 66 Camp declarations inside its existing eligible branch and one missile retaliation-status declaration before reset, with 46 independently reviewed passing source-model cases.
The two insertions are implemented in source and parent-reviewed; every original statement, cost, gate and order is preserved.
The missile owner retains its justified partial packet; the removed `missiles_check_chemical_payload_stock` entry in the old insertion map is superseded and must not be applied.
These callers were outside the original eighteen-case suite; the separate source checks retain actual getter, exact-model fixture debit, returned-death and none/authorized strategic missile history boundaries.
The proof tested here prevents repeated dispatch within the same prepared source frame; it is not a persistent replay identifier for distinct native callbacks.
A fresh Camp invocation prepares a separate record and may pay again.

The 2026-10-09 receipt-scope review does not establish an additional safe persistent native-raid guard.
Installed `documentation/effects_documentation.md:7888–7895` labels `set_variable` as any-scope, while the offline `Data structures` scoping section at lines 445–452 describes regular storage only on countries, states, characters and global scope.
Installed `common/raids/_documentation.md:247–301,548–558` establishes RAID_INSTANCE outcome scope and four built-in actor/victim/target variables, but documents neither custom persistent storage on that instance nor an instance identifier suitable for a country-side receipt.
The installed raid precedents inspected use country flags for one-time national achievements, which cannot distinguish concurrent or repeated legitimate raids.
These sources therefore do not prove that an instance-local custom variable would survive or be writable; a generic any-scope command check would not settle that storage question.
No native callback replay was observed in this review, and no speculative raid variable, country-wide pending scalar, refund or extra payment is added.
Native callback uniqueness remains the same unresolved acceptance item, separate from the repaired within-frame dispatch proof.

| Receipt-scope reference | Source SHA-256 |
| --- | --- |
| Installed `documentation/effects_documentation.md`, lines 7888–7895 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 445–452 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Installed `common/raids/_documentation.md`, lines 247–301 and 548–558 | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` |

## MCP and native acceptance

Offline Data structures lines 435-443 and installed `set_temp_variable` documentation lines 7820-7827 establish the caller-ownership contract; source revisions are recorded by the patch handoff.
Installed raid documentation remains the payment, callback-scope and exact actor/target authority.
The earlier bounded land-bridge trace was partial and its complete artifact was not read.
The attempted trace-revision comparison returned `EVENT_REVISION_NOT_CACHED`.
The [MCP route review](subagent_handoffs/2026-10-07_mcp_event_comparison_route_review.md) identifies the cause: graph references require a scan graph, and a trace is only a report.
A future canonical comparison must retain the scan's `event-graph-<revision>.json` artifact; an archived-source overlay can provide only an explicitly reversed comparison against current source.
The parent subsequently captured a bounded Camp scan at revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5` with a 96,333,999-byte graph, zero expanded helpers and deferred lifecycle projections.
The correctly shaped artifact-backed comparison returned `ARTIFACT_NOT_FOUND` because the artifact provenance manifest is unavailable; this is a genuine artifact-access failure distinct from the earlier trace/report-as-graph mistake.
The [remaining-caller report](2026-10-08_remaining_chemical_callers.md) retains the stable graph URI and [parent MCP receipt](../../testing/2026-10-07_camp_chemical_lifetime/recorded_mcp_attempts.json), with the original structured-store loss and recorded-output reconstruction explicit.
No complete graph body read or successful comparison/render is established; current domain comparison/render coverage and native execution remain open.
The separate reconciliation attempt returns `EVENT_GRAPH_ARTIFACT_LIMIT` because that snapshot exceeds the fixed 67,108,864-byte comparison ceiling; it does not replace the parent's provenance-manifest failure.
The [chemical probability audit](subagent_handoffs/2026-10-07_chemical_raid_lifetime_probability.md) submitted the five existing RNG getter locations to the direct-random adapter; all returned no candidate and no required inputs.
The unchanged getter segment and bounds have identical before/after/current normalized hashes, but no numeric distribution or native outcome chance is claimed.
The separate incubation archived-source overlay comparison timed out after 600 seconds without a backend task handle; a second full graph overlay for chemical source was not started while its backend completion remained unknown.
No gameplay simplification or substitute mechanic is introduced.
The broader CBRN goal remains incomplete.
Skills used: events, native raids, subagents and shared Git commit.
