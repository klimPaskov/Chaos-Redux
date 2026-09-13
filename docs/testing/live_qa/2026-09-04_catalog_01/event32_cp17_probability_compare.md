# Event 032 command-power alias postpatch probability compare

Date: 2026-09-05

Status: read-only postpatch comparison, partial native probability evidence, numeric threshold acceptance unresolved.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

## Source provenance

The audited surface is `events/032_missile_crisis.txt`, event `chaosx.nr32.60`, options `.a` through `.g`.

The parent applied the four requested `has_command_power` to `command_power` substitutions at lines 265, 271, 277, and 283 after the baseline hash guard matched `964423E2ED8A07B4D23B3EA463E01994AB58802FC2461698C8634454CDE2EAA2`.

The current source SHA-256 is `FEE0B45854C7ED3A55C826EBA4BBFB9E8AF254B9D716E2F5213EF7F030781041`.

The baseline snapshot remains [`pre_patch_event32_cp16/032_missile_crisis.txt`](pre_patch_event32_cp16/032_missile_crisis.txt) with SHA-256 `964423E2ED8A07B4D23B3EA463E01994AB58802FC2461698C8634454CDE2EAA2`.

No gameplay source, runtime, save, or launch file was written by this audit, and no game was launched.

## Matching scenario contract

The full candidate pool was reused: `chaosx.nr32.60.a`, `.b`, `.c`, `.d`, `.e`, `.f`, and `.g`.

The exact nine scenario IDs were reused: `E32_CP16_BELOW_LOW`, `E32_CP16_EQUAL_LOW`, `E32_CP16_ABOVE_LOW`, `E32_CP16_BELOW_STANDARD`, `E32_CP16_EQUAL_STANDARD`, `E32_CP16_ABOVE_STANDARD`, `E32_CP16_BELOW_HIGH`, `E32_CP16_EQUAL_HIGH`, and `E32_CP16_ABOVE_HIGH`.

The command-power values were `7`, `8`, `9`, `14`, `15`, `16`, `24`, `25`, and `26`, preserving the strict below/equal/above checks for low `8`, standard `15`, and high `25`.

The saved fixture declared `is_ai=true`, command-power and alias mirrors, `fuel=1000`, `support_equipment=1000`, `manpower=1000`, incident site present, payload absent, reserve absent, and `has_war=false`; `.f` was explicitly overridden false because the rogue launch target/reserve was absent.

The baseline evaluator scenario hash was `0cb8c7016d65ef88b090f947899ad5a0ee99ac1eda4f9219ad0adaf4b1c1a8b7`, and the successful compare returned the same hash.

## Mandatory postpatch inspect

The first postpatch call was `hoi4.probability_inspect` with adapter `event_option_ai_chance`, source `{identifier: "chaosx.nr32.60", path: "events/032_missile_crisis.txt"}`, `refresh=true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `PROBABILITY_SOURCE_INSPECTED` with a complete seven-candidate pool, nine required inputs, zero unresolved inspect items, and game verification `Operation Postern 1.19.2.0 (d245)`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c93fa009978b6493314d51b0f04d8158cabb6dc5310a79ec3da15f8f5d932c71/7a26eca890b8dc833cb4b12ce3ca8f7f420c36baee26682a8ead366c00f64435/probability-inspect-018671f981e7.json`.

Inspect source revision: `56e9c53d922bcb05132a1441d582c539de39e88625613a77089e38bee6778414`; MCP source hash: `018671f981e7f1dc6ee15bcc0bbadcdd3e5b8444dff7ddb53b8d3f93e899c1be`.

## Same-scenario probability compare

The compare used the baseline snapshot as an inline before source and the current file as the after source, with the same adapter, nine scenarios, complete candidate pool, one-day horizon, and JSON/comparison/ranking/matrix/waterfall/unresolved outputs.

An initial request using the inspect MCP hash as `after.expectedSourceHash` returned the exact blocker `PROBABILITY_SOURCE_STALE`: expected `018671f981e7f1dc6ee15bcc0bbadcdd3e5b8444dff7ddb53b8d3f93e899c1be`, actual file hash `fee0b45854c7ed3a55c826eba4bbfb9e8af254b9d716e2f5213ef7f030781041`.

The schema rejected an uppercase actual hash with `Invalid string: must match pattern /^[a-f0-9]{64}$/u`; the retry used the same actual hash in lowercase and succeeded.

The successful call returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-92eae05745394e3de60a897e`, nine scenarios, 63 candidate rows, 24 unresolved items, five diagnostics, and `comparisonChanges=0`.

Compare artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e20a2c8b696296070be4fd7433cd4cff91f609137867733a1a438fd53ed5d883/b70be47bbbb8954460e6f377bf8a535203c19045cde51f9b9dd9dcd255676820/probability-92eae05745394e3de60a897e.json`.

Compare source revision: `56e9c53d922bcb05132a1441d582c539de39e88625613a77089e38bee6778414`; MCP after-source hash: `018671f981e7f1dc6ee15bcc0bbadcdd3e5b8444dff7ddb53b8d3f93e899c1be`.

The comparison record contains `beforeAnalysisId=probability-775a2db39764ce904cb93be1` and `afterAnalysisId=probability-17c46fabc6767f0aafa74837`, with `adapterChanged=false`, `assumptionsChanged=false`, `regressions=[]`, and `scenarioChanges=[]`.

Comparison visualization: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/4a8e04c96c1bfefd0c96ff19108f42858777a4f5cb710ee0798554b39f68ac47/probability-probability-92eae05745394e3de60a897e-comparison.svg`.

The comparison also emitted ranking, matrix, waterfall, and unresolved visual resources; their URIs and hashes are retained in the authoritative compare artifact response.

## Postpatch result and remaining limits

The canonical `command_power` token appears in all four repaired triggers, but the native evaluator still reports `TRIGGER_UNRESOLVED` because `command_power` cannot compare the declared scenario value in this adapter fixture.

Option `.b` additionally remains unresolved on `has_fuel`; option `.d` remains unresolved on `has_manpower`; option `.c` remains unresolved on `has_variable`, compound `has_equipment`, and the payload helper’s `has_variable` plus `var:missiles_incident_site`; option `.e` remains unresolved on `has_variable`, `has_manpower`, and the same payload helper scope paths.

Across all nine scenarios, `.a` is false for the AI actor, `.f` is false by the declared override, `.g` is true with raw score `1`, and the source-local score traces remain `.b=10`, `.c=10` before its unresolved modifier, `.d=12` after the `6 x 2.00` restraint factor, and `.e=3` before its unresolved modifier.

The comparison therefore produced no resolved score, eligibility, rank, or probability delta attributable to the four-token patch; `comparisonChanges=0` reflects the unresolved fixture, not proof that the engine repair has no effect.

No normalized probability, strict boundary result, rank reversal, dominance, starvation, or repetition conclusion is valid from this compare because the affected candidate eligibility remains unresolved.

The native diagnostics remain `EVENT_OPTION_FALLBACK_NOT_PROVEN`, `.a` never eligible across the supplied AI scenarios, `.f` never eligible under the explicit override, and inactive verification/escalation modifiers in this fixture.

## Owner handoff

The source repair is preserved as the exact four-token parser correction requested by the parent, with the current file hash recorded above.

The owner may retain the patch without a numeric probability acceptance gate because the compare confirms no unrelated score or modifier change and the adapter cannot bind the required numeric and scoped inputs.

Do not claim a numeric probability or strict threshold acceptance from this compare.

If the probability route is revisited, it must support country-resource and nested scope fixtures for `command_power`, `has_fuel`, `has_manpower`, `has_variable`, `has_equipment`, and `missiles_rogue_incident_site_has_payload`, then rerun the same nine IDs and pool.

No additional scenario expansion, simulation, sequence analysis, or source tuning was performed.
