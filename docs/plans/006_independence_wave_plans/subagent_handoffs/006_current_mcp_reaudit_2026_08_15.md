# Event 006 current MCP re-audit

Date: 2026-08-15.

Disposition: HOLD / PARTIAL. This is a read-only evidence receipt; it does not widen central attestation, normal or SCN-008 preflight, deterministic Join, package identity, asset rights, or formable ownership.

## Current authority

The allocator and static acceptance boundary remains 149 publishers, 40 runtime adapters, 32 content-attested selectable packages, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

The active automatic ladder remains 3/4/5/7/10, with World Collapse also targeting 10.

The adapter-only fail-closed IDs remain IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179.

IW-047 MEL, IW-048 UDM, IW-050 KOM, IW-051 YAK, IW-052 BYA, IW-053 ALT, IW-054 KHA, and IW-060 KUR remain outside central admission and Join under their current identity, map, asset, or typed-probability gates.

## Event MCP receipt

A fresh `hoi4.event_inspect` scan targeted `events/006_independence_wave.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The result was `EVENT_INSPECTED_PARTIAL` with revision `76e767e6fb64a0bcdbe93bac59bc931d6b7bbc158ab0a9a65a65ffb9dc8fcd5b` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c274b33244b44a53737393e2f4520bfcb21286e9124081b5c2359965b092a89/3a3faa69caf26c9e439ba26b8bc2b4644023d9fc98019e292682f2b24ab0ef8a/event-scan-76e767e6fb64.json`.

The focused scan reported 9,499 events, 14,688 options, 1,060 entries, 37,069 edges, 2,127 diagnostics, and zero selected blocking diagnostics.

The engine deferred workspace-wide helper projections and lifecycle passes, so this is not a whole-event completion receipt.

A focused `state_flow` pass for `chaosx.nr6.350` returned the same revision and partial boundary with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8dda0fba1ea57dc695cd403186d5d0aab6f8b4dbfd7ce8902980fd042a4fdcc5/fcc4704d30b4bd0dfdfbb846d8528287e27b74ae61c0df890c0beaaed2c184fb/event-state_flow-76e767e6fb64.json`.

The state-flow report found zero selected blocking diagnostics, but the same deferred workspace-wide helper and lifecycle projections prevent a whole-event pass claim.

## Focus MCP receipt

A fresh `hoi4.focus_inspect` national-tree inspection targeted `independence_wave_focus_tree` in the same workspace.

The result was `FOCUS_INSPECTED` with revision `dfc8e312e53c649e090c782f7f87013558b357c230018775d234affba9dcb89`, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08bd58d8ad369827046fe7cdb77aaecc675d4cbecca36f5cc32243a4ecafaa44/07560d21cc4337789e9033d0dd6f8ef76c679cb70da9f390db8220988f1772eb/focus-inspect.dfc8e312e53c649e.json`.

The tree contains 184 focuses and 196 connectors with zero crossings, zero node intersections, and two long connectors.

The validation remains false because the workspace reports 15 blocking diagnostics, including an unrelated vanilla `TSR_lingguang_incident_joint_branch.txt` unexpected closing brace and repeated focus-tree-not-found warnings from non-tree source files.

No authored Event 006 focus layout defect was established by this receipt.

## Probability MCP receipt

A fresh `hoi4.probability_inspect` request targeted `common/decisions/006_independence_wave_kuban_decisions.txt` with adapter `mission_ai_will_do`.

The inspect returned `PROBABILITY_SOURCE_INSPECTED`, source revision `2093bbc850cae5cb98838a55a5050fcd2065bbd92b57937291a08ff74ccb1127`, source hash `87ba7c79b4c87b980b378f0a6c08cd27051363bea3b9b44eaec4a7ee49a4f25c`, 11 discovered candidates, zero available candidates, 15 required inputs, zero unresolved inputs, `poolComplete=false`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/276cf104086ace0cd8d72b9709328e77a8bd3db59462fb28b88af1c38d2c76d1/f646cf1fe80bb11b05d3918c2e4527a08ace868154b82aed027bb2a779722b52/probability-inspect-87ba7c79b4c8.json`.

The attempted six-scenario empty-fixture evaluation returned `PROBABILITY_SURFACE_EMPTY` rather than a balance result, so no ranking, probability, timing, dominance, starvation, or live AI claim is made.

## Remaining safe boundary

No central source patch is justified by these receipts.

The next admissible progress requires typed campaign fixtures for the admitted KUB/TAT mission surfaces, family-isolated formable GUI evidence, or independent identity/flag/portrait decisions for package-local rows.

Until those inputs exist, preserve the 40/32/29/161 authority boundary and keep the fail-closed admission gates unchanged.
