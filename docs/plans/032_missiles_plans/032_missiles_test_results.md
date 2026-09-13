# Event 32 — Missiles test and validation record

Status: partial/blocked. The source implementation and evidence reconciliation are substantial, but the independent completion audit records unresolved MCP, probability, asset-consumer, and planner evidence gaps. This record is the evidence ledger for the Event 032 acceptance and test matrices; it is not a substitute for live Hearts of Iron IV consumer validation.

## Source and static coverage

- All files under `docs/specs/032_missiles_specs/` were read before implementation, including the acceptance criteria, coding and decision prompts, asset and achievement prompts, requirement traceability, source review, probability scenario matrix, test matrix, and improvement-loop closure.
- The entry remains `chaosx.nr32.1`, with namespace `chaosx.nr32`; the implementation has one hidden entry event and no Event 032 world-end branch.
- The only explicit Event 032 `every_country` recipient enumeration is inside `missiles_global_firing_transaction` in `common/scripted_effects/032_missiles_effects.txt`. No Event 032 daily, weekly, or monthly whole-world scan was added.
- The transaction freezes `global.missiles_frozen_recipients` before recipient mutation, processes each frozen scope once by receipt id, and stores one accepted-recipient count for pacing, repeatable state, history, and first-news behavior.
- Event 032 has one ordinary decision category, one static category picture, phased visibility, ten timed mission definitions, five evolution tracks, five target profiles, four strike profiles, and the SCN-015 five-profile scenario wrapper.
- The Event 16 reaction helper remains the only shared Event 16 bridge; Event 23 and Event 76 ownership is not absorbed into Event 032.
- Achievement receipts are wired at operation, warning, capture/control, repair, war-start, war-resolution, and delayed-timer boundaries. Evolution-gated receipt adapters fail closed when the relevant track is disabled.
- Empty the Silos freezes opening-site IDs at war start, validates player conventional credit against that manifest, and records ally capture/destruction only through the bounded state-control and operation-impact hooks. No recurring world scan was introduced.
- The current workbook was reopened read-only after export and still contains Event 32 at `Events!A33` with title `Missiles`, blank world-end and cluster fields, and `SCN-015` at `Scenarios!A15`; current workbook hash and exporter hashes are recorded in the catalog handoff.

## Asset evidence

- Runtime asset count: 82 final DDS files, consisting of 58 non-achievement assets and 24 achievement-state assets.
- Every runtime DDS decoded successfully with Pillow and was opened individually at its decoded resolution and in labelled family contact sheets.
- The current dimensions are: report `210x176`, news `397x153`, category picture `114x101`, category button `52x40`, 27 decision icons and seven mission icons `34x33`, five guidance icons/four posture icons/five state modifiers `32x32`, three ideas `60x68`, three status texticons `24x24`, and 24 achievement icons `64x64`.
- The first global-news draft was rejected during visual review because it contained only one launch column. The current DDS is the replacement scene with multiple launch/smoke columns and a separate transporter; its runtime round-trip was reopened and passed.
- The full per-file audit table, consumer mapping, hashes, omitted families, and the exact native-raid icon blocker are in `docs/events/032_missiles/asset_audit.md`.
- No portrait, flag, focus, super-event, custom 3D, skeletal animation, frame animation, scenario-specific picture, or dedicated scripted-GUI asset was introduced.

## Static invariants checked

- No direct recursive `country_event` launch call exists in the Event 032 operation effects. Automatic retaliation schedules a later response event and uses the bounded warning/operation receipt path.
- Automatic-retaliation constants define generation, participant, linked-incident, queue, and automatic-missile limits; warning receipts are keyed by root incident and country.
- Special payload preparation checks existing technology, policy, stockpile, missile stage, reserve, and state custody before the payload is integrated or consumed.
- Operation cleanup clears prepared targets, sites, arrays, operation flags, reserved reserve, payload-debit receipt, and stale state allocation references.
- Site capture, scuttle, release, annexation, and state-control hooks are wired through Event 032 lifecycle helpers.
- The natural-disaster bridge now validates current controller custody, settles the percentage reserve receipt before mutation, fails closed on invalid scope/custody, recovers capacity loss during repair, retires scuttled capacity, and clears bridge receipts on accepted and rejected exits.
- The repository static `rg` checks found no Event 032 decision or mission reference to `GFX_decision_brilliant_scientist` or `GFX_mission_brilliant_scientist`.

## Required MCP evidence

The installed `hoi4_agent_tools` service returned current bounded Event and technology artifacts after the source reconciliation.

- `hoi4.event_inspect` for `chaosx.nr32.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `17b3aac359b767085af37746c2ad9e7a1bc9437f4d9712ff9ce7e3d72ba43614`, graph hash `6b4402c3520bc5cdc2b4f108f49e88e9c0a8aec417e2b2b72722d9fcdc91e7c5`, 9,740 events, 15,167 options, 38,360 edges, 30,436 state accesses, 2,199 diagnostics, and one blocking diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc8cbc170fa076d60fcb3fd9f5042cc6d98c415bea9917ccd96c3dc4e8a58536/de1f263293396a5a53226d1284a180b2ec8647a88e91eda434c5d9ac6a97c1eb/event-lint-17b3aac359b7.json`.
- `hoi4.event_render` for the same entry returned `EVENT_RENDERED_PARTIAL`, status `ok`, using the same revision and graph hash. The unresolved render selected two nodes and produced JSON, SVG, PNG, and manifest artifacts, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de2dde0db07c97cc223bc4f481d3b0e2531ef5921a9e6630210547609319f33b/e1cbb11f877190fa40193c99d14458b558cba9771ae0199b60018e0a55fa6f3d/event-unresolved-17b3aac359b7.json`.
- A fresh completion-auditor run observed a later Event inspect revision beginning `410c82bea077…` and again reported `EVENT_INSPECTED_PARTIAL`, focused analysis, zero expanded helpers, 8,728 unresolved items, one blocking diagnostic, and validation false. The returned handoff did not include the full revision or artifact URI, so this observation is recorded as a current limitation rather than substituted for the reproducible parent artifact above.
- `hoi4.event_compare` was attempted with the current service and first returned the exact blocker `EVENT_COMPARISON_BASELINE_REQUIRED`: `Provide a cached revision, graph artifact, or proposed source overlay`. A second read-only attempt supplied the returned graph artifact and revision and returned `EVENT_GRAPH_ARTIFACT_INVALID`: `Event graph artifact uses an unsupported schema version`. No comparison claim is made.
- `hoi4.tech_inspect` for `improved_rocket_engines` returned `TECH_INSPECTED`, revision `ea3ccbfd2c623bb948f8777fe1da11b5f01145c3c399f26bff727f84f07fc6d6`, graph hash `a8b8831eea07befaaca51d7a53d29c7922ae1cf558af01d211212fd21e1cf3f2`, and three unresolved nodes. The scan reported 1,351 blocking workspace technology diagnostics; the full artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e5680720b2ff31c3a7882ca0a6ff002b0b46ec1b38cc6da65b5c14e05f5335f/23a0919f6e3b9214e084753400f11d7681df5d2b7b1343a9e170675d9231eac8/technology-lint-ea3ccbfd2c62.json`.
- `hoi4.tech_render` for `improved_rocket_engines` returned `TECH_RENDERED` with four source-linked artifacts, but `sourceAccurate=false` and validation remained false because of the workspace-wide diagnostics. The technology JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb29c3e7bd885c6ea59b566b840495b0062b6a6f9280f70bb54630465630502f/878483666479f6e0a1330f37c6a4d8904362b9c111d1fff913bc102fcd49949d/technology-technology-c80e714485e6.json`.
- `hoi4.tech_compare` was attempted against the inspected revision and first returned the exact blocker `TECH_REVISION_NOT_CACHED`: `Requested technology revision is not cached`. A second read-only attempt supplied the returned technology artifact and revision and returned `TECH_GRAPH_ARTIFACT_INVALID`: `Technology graph artifact has an invalid schema`. No before/after technology comparison claim is made.
- The installed package exposes no separate standalone Technology Tree Viewer route; this is recorded as a package gap, not replaced with a fabricated capability.
- The current Event and technology artifacts remain partial because the service defers workspace-wide helper/lifecycle analysis and reports unrelated workspace diagnostics. These are evidence limits, not source-parse passes.

## Probability evidence

The required `chaosx_ai_probability_auditor` route was dispatched with `fork_context=false` before the weighted repair. The owner-applied repair changed only the four invalid `has_command_power` aliases in `events/032_missile_crisis.txt` Event `.60` to `command_power`; weights and scenario definitions were unchanged.

The postpatch inspect returned `PROBABILITY_SOURCE_INSPECTED` with the complete seven-candidate `.60` pool, nine required inputs, and zero unresolved inspect items. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c93fa009978b6493314d51b0f04d8158cabb6dc5310a79ec3da15f8f5d932c71/7a26eca890b8dc833cb4b12ce3ca8f7f420c36baee26682a8ead366c00f64435/probability-inspect-018671f981e7.json`, with source revision `56e9c53d922bcb05132a1441d582c539de39e88625613a77089e38bee6778414`.

The required same-scenario `hoi4.probability_compare` reused all nine command-power boundary scenarios (`E32_CP16_BELOW/EQUAL/ABOVE_{LOW,STANDARD,HIGH}`), the full `.a` through `.g` pool, and scenario hash `0cb8c7016d65ef88b090f947899ad5a0ee99ac1eda4f9219ad0adaf4b1c1a8b7`. It returned `PROBABILITY_ANALYZED_PARTIAL`, 63 candidate rows, 24 unresolved items, five diagnostics, `comparisonChanges=0`, no regressions, and no scenario changes. Compare artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e20a2c8b696296070be4fd7433cd4cff91f609137867733a1a438fd53ed5d883/b70be47bbbb8954460e6f377bf8a535203c19045cde51f9b9dd9dcd255676820/probability-92eae05745394e3de60a897e.json`.

The native evaluator cannot bind `command_power`, `has_fuel`, `has_manpower`, `has_variable`, compound `has_equipment`, or the scoped payload helper in the fixture. Therefore no numeric probability, strict threshold, rank, dominance, starvation, or repetition conclusion is valid. The result is retained as required partial evidence, not probability proof. The full current handoff is `docs/testing/live_qa/2026-09-04_catalog_01/event32_cp17_probability_compare.md`.

The required named scenario matrix still includes additional target-selection, payload, guidance, evolution, incident, retaliation, maintenance/posture, and SCN-015 profiles that the installed probability adapter cannot bind as a single complete engine fixture. Any score-only, incomplete-pool, unresolved, or adapter-blocked output remains explicitly non-proof.

## Bridge disposition

The earlier natural-disaster bridge audit findings are implemented in `common/scripted_effects/032_missiles_operations_effects.txt` and `common/scripted_triggers/032_missiles_operations_triggers.txt`. The parent reviewed the current-controller reserve settlement, fail-closed controller/program gate, capacity-loss recovery, scuttle cleanup, and unconditional receipt cleanup. The original audit remains retained as historical evidence with its stale recommendations to be reconciled in its handoff.

## Live-validation boundary

No Hearts of Iron IV process or autonomous desktop test was launched. Live save, GUI, native raid consumer, decision rendering, event rendering, achievement unlock, and in-game consequence validation remain user-run surfaces. This boundary is intentional and does not convert source review or a missing MCP comparison baseline into engine evidence.

## Improvement-loop and final completion gate

The existing accepted closure in `docs/specs/032_missiles_specs/032_missiles_improvement_loop_closure.md` rejects broad expansion families and finds no missing accepted design family. A final `chaosx_improvement_loop_planner` worker was dispatched with `fork_context=false`, but returned no handoff after bounded waits and was shut down; its blocked disposition is recorded in `docs/plans/032_missiles_plans/subagent_handoffs/032_improvement_loop_planner_handoff_2026-09-05.md` and is not presented as independent planner evidence. The completion-auditor review is recorded in `docs/plans/032_missiles_plans/subagent_handoffs/032_event_completion_auditor_handoff_2026-09-05.md`.

This record remains partial/blocked until the recorded MCP, probability, native-raid-consumer, and independent-planner gaps are resolved or explicitly accepted by the user; no completion claim is made.
