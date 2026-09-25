# Event 016 Mengele provider-family decision source audit

Audit date: 2026-09-25. Scope: Teleportation, Robotics, Paleogenetics, Xenobiological Synthesis, Materials, and Biomedical; focused Cloning review; blocker-only Alien Arms and Temporal review. This is a read-only source audit. I made no gameplay edits, staging, commits, or game launch.

Repository HEAD observed with the final source-hash snapshot: `5f6523c4052106bbd668a30b3de603cbe88322a3`. The listed hashes are local SHA-256 values for the working-tree sources at that snapshot; parent edits may move independently.

## Findings, sorted by severity

### P2 — Required AI before/after comparison is unresolved for Teleportation and Robotics

No decision-source defect was found in either slice, but the mandatory probability comparison for their AI changes has no successful result. The Teleportation auditor handoff records `hoi4.probability_compare` rejecting the supplied baseline evaluation because required `beforeManifest` fields were absent and analysis-result fields were unrecognized; no comparison artifact was created. See `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_mengele_teleportation_ai_audit_2026-09-25.md:46` (local decision SHA-256 `0D992F3D5BBB0A58D414090F12AF6D8C15A8A9C34E3A0905A528FED4974C0989`).

The Robotics handoff records the compare route rejecting `sourceHash` and `sourceRevision` as unsupported fields; it also produced no comparison artifact. See `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_mengele_robotics_ai_audit_2026-09-25.md:113` (local decision SHA-256 `8B974AC810C6A74E068146C91168DDEE988ED600E46C45DD166D4569BC9D2BD5`). The existing handoffs include partial inspect/evaluate evidence, but do not prove the required before/after delta. This is an AI evidence gate, not a source defect; I did not repeat the probability auditor’s work.

No matching probability-audit handoffs for Materials, Biomedical, Paleogenetics, or Xenobiological Synthesis were found in the scoped Event 016 handoff directory. Their AI source wiring was reviewed statically only; this audit makes no numeric weight or balance claim for them.

### P2 — Native decision visuals have no supported HOI4 MCP inspect/render route

All reviewed actions are ordinary decisions in `mengele_clone_army_category`, including `mengele_event016_teleportation_theory` at `common\decisions\016_mengele_teleportation_stage_decisions.txt:16`. The exposed GUI inspect/render routes target scripted GUI windows; no decision-category inspect or render route is exposed. No in-game visual evidence is therefore available for native row alignment, clipping, text fit, icon display, or click regions. This is an exact route limitation, not a visual pass. No scripted GUI is introduced by these slices.

### P2 — Broad adapter contract check stops outside this scope

The read-only `node .tools/audit_mengele_project_adapter_contract.mjs` check stopped at `.tools/audit_mengele_project_adapter_contract.mjs:122` with `AssertionError: electronics_deployment native needed without DLC`. That assertion concerns the out-of-scope Electronics family. The check did not complete, so it supplies no completion evidence for these slices; no source was changed to work around it.

### Source defects

No gameplay-source blocker was found in the six primary families. The formerly shared Xenobiological cautious cutoff is stage-specific in the audited snapshot: the four wrappers call their matching no-spare-factory predicates, and those predicates compare against each stage’s own quote in `common\decisions\016_mengele_xenobiological_synthesis_stage_decisions.txt:55` and `common\scripted_triggers\016_mengele_xenobiological_synthesis_stage_decision_triggers.txt:113`. The earlier provider handoff described the previous family-wide cutoff; the current source hashes below identify the audited replacement.

No source blocker was found in the supplemental Cloning review or the blocker-only Alien Arms and Temporal reviews.

## Six-family audit

### IDs, receipts, and stage lifecycle

| Family | Family ID / receipt index | Audited stage IDs |
| --- | --- | --- |
| Teleportation | 7 / 6 | `mengele_event016_teleportation_{theory,prototype,deployment,weaponization}` |
| Robotics | 9 / 8 | `mengele_event016_robotics_{theory,prototype,deployment,weaponization}` |
| Paleogenetics | 10 / 9 | `mengele_event016_paleogenetics_{theory,prototype,deployment,weaponization}` |
| Xenobiological Synthesis | 11 / 10 | `mengele_event016_xenobiological_synthesis_{theory,prototype,deployment,weaponization}` |
| Materials | 3 / 2 | `mengele_event016_materials_prototype`; Theory, Deployment, and Weaponization remain in the conventional file |
| Biomedical | 6 / 5 | `mengele_event016_biomedical_prototype`; the other three stages remain in the conventional file |

The IDs and zero-based receipt indexes match `common\script_constants\016_brilliant_scientist_constants.txt:330`. Duplicate decision IDs and duplicate localization keys were not found in the scanned Event 016 prefix. The four full families gate stages on the prior completion flag, an empty family receipt, and a valid Mengele provider. Materials and Biomedical Prototypes follow their existing Theory stages and unlock the existing Deployment stages through the shared completion flag. No target family reads or writes Kruger capacity, receipts, or history.

### DLC boundary, costs, and requirements

Every paid Prototype fallback is visible only without `Gotterdammerung`, after Theory, before its private Prototype completion, and while the matching native special project is incomplete. The exact native project IDs are `sp_brilliant_scientist_quantum_transit`, `sp_brilliant_scientist_autonomous_cognition`, `sp_brilliant_scientist_paleogenetics`, `sp_brilliant_scientist_xenobiological_synthesis`, `sp_brilliant_scientist_advanced_materials`, and `sp_brilliant_scientist_biomedical_acceleration`. Each ID exists in the Event 016 special-project definition file. Materials and Biomedical wrappers therefore fill the no-DLC Prototype gap without replacing the three existing conventional stages.

The fallback quotes displayed, checked, and loaded by the shared stage core agree. Each has four committed axes at most: reserved civilian factories plus Political Power, Support Equipment, and Fuel. Directly consumed types are at most three; Theory has no Fuel charge. Inline spendable costs use `£pol_power`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon` as applicable. The separate cost tooltip explains the factory reservation and all spendable amounts with icons; no literal resource labels or hidden fifth cost were found.

| Fallback Prototype | Factories reserved | Political Power | Support Equipment | Fuel |
| --- | ---: | ---: | ---: | ---: |
| Teleportation | 3 | 90 | 300 | 600 |
| Robotics | 3 | 83 | 375 | 400 |
| Paleogenetics | 2 | 98 | 325 | 300 |
| Xenobiological Synthesis | 2 | 105 | 350 | 250 |
| Materials | 2 | 68 | 200 | 200 |
| Biomedical | 2 | 90 | 300 | 100 |

Each wrapper calls the same family/stage affordability trigger from `available` and `custom_cost_trigger`; the begin effect reloads the shared quote and debits once. Factory counts are mirrored only for the native timed-decision reservation modifier and `ai_hint_pp_cost`; payment and localization use shared constants. Threshold checks are inclusive against the quoted amount. Requirements are separate from costs.

### Category density, values, and mission quality

These are timed decisions, not mission objects. The owner is the currently valid Mengele provider country; the category is `mengele_clone_army_category`; the scope is country-wide with no state or region target. Stages are sequential, one active receipt per family. The reviewed slice can expose up to six current actions at once across its six families; the total shared category also contains out-of-scope rows and is not certified by this bounded audit.

Durations are centralized: Teleportation 240/360/540/720 days; Robotics 180/300/450/600; Paleogenetics 210/330/480/660; Xenobiological Synthesis 240/390/570/750; Materials Prototype 240; Biomedical Prototype 240. Titles identify the stage, requirement tooltips name the predecessor or provider state, cost tooltips name the full commitment, and completion tooltips state the result. No wall-of-text description or unexplained player-facing value was found. Native row fit and visual density remain unverified because the MCP route cannot render this surface.

### AI, output, cleanup, and exploit checks

Teleportation and Robotics use the expected stage bases and wartime preference with stage-quote factory-margin predicates. Paleogenetics and Xenobiological use stage-matched no-spare-factory predicates in the current source. The Xenobiological current source is now stage-specific at thresholds 1/2/5/7; the older stage handoff documents the prior family-wide maximum and is stale for these two source files. Materials and Biomedical Prototype wrappers have AI weights and a stage-specific factory caution trigger. No invalid country target or closed-route target is present; provider validity is checked by the shared provider trigger.

Start, cancel, finish, and failure settlement use the shared private receipt core. `cancel_if_not_visible = no` preserves a running timed row if its visible trigger later changes; the explicit cancel trigger instead checks provider authority and the exact receipt. Cancellation refunds the recorded direct costs and releases the timed factory modifier. Finish records history/output only for the matching receipt and refunds direct costs when output is rejected. Successful custom operational packages pass through the existing idempotent technology API. No duplicate-stage path, free equipment loop, refund farming path, war-goal spam, or repeated grant path was found by source review.

## Supplemental source review

### Cloning

The four wrappers in `common\decisions\016_mengele_cloning_stage_decisions.txt` map to family ID 8 / receipt index 7 and use the shared stage cost, timer, cancel, and finish flow. The no-DLC Prototype requires Theory, an incomplete native cloning project, successful private finish/output, and the private Prototype completion flag before calling `germany_mengele_complete_cloning_project`; that dedicated effect is guarded by its completion flag. It then grants the existing neutral Clone operational package and selects the Aryan refinement only when the master-race claim exists and its technology is absent. The native bridge at `common\scripted_effects\016_mengele_project_bridge_effects.txt:16` requires valid provider, private Theory and Prototype history, and exact native project completion; it clears selectors and invokes the dedicated clone effect and guarded Aryan refinement after a successful idempotent API grant. Localization keys resolve, and all four sprite definitions and DDS files exist. No source blocker found.

### Alien Arms and Temporal

Blocker-only review found family ID/index 13/12 for Alien Arms and 14/13 for Temporal, exact predecessor/receipt gates, no-DLC Prototype guards for their matching native special projects, and four wrapper AI/cancel/finish call sites per family. Decision icons resolve to existing sprite definitions and DDS files; localization keys resolve. No source blocker found. No probability or native visual evidence is claimed for these two supplemental families.

## Localization, assets, and validation

The bounded prefix scan found no duplicate decision IDs or localization keys. A focused lookup of 190 decision tooltip, cost, and effect keys found no missing English localization. All 30 sprite references across the six primary and three supplemental families have a matching `.gfx` definition and existing DDS file. Shared dynamic cost localization uses the same quote constants as affordability and payment.

No separate decision-category inspect/render artifact exists because the installed HOI4 MCP tool inventory exposes no native decision inspect/render route. Existing Teleportation and Robotics probability handoffs are the only MCP artifacts used for their weighted logic; their compare blockers are listed above. The broad adapter contract script failure is listed above. No game was launched.

## Source snapshot hashes

All hashes below are local SHA-256 values captured at repository HEAD `5f6523c4052106bbd668a30b3de603cbe88322a3`.

| Family | Decision file SHA-256 | Trigger file SHA-256 | English localization SHA-256 |
| --- | --- | --- | --- |
| Teleportation | `0D992F3D5BBB0A58D414090F12AF6D8C15A8A9C34E3A0905A528FED4974C0989` | `73703DC378DE6F1BF9735CAEF49E97B6362C6674C2F855ADDCE591266B45ECBD` | `DC6EF88AB24A753D3B9420DAD0CF91F114F283DAFE55C6CA9DEFEDF37CFA4331` |
| Robotics | `8B974AC810C6A74E068146C91168DDEE988ED600E46C45DD166D4569BC9D2BD5` | `064CC387D3E89830C6B5A3926F542226A052EDE2881B5CF3460DDD6136149B69` | `D376DC810CD7EB00E8E70655647F8B754C1F2D0085C15A466E1BEB51175761E0` |
| Paleogenetics | `DD5B6DB1BD72A2A170CCE58FB88F8C9C7A926EA34A45844FB4908FAB1D4A378D` | `A457BD6F889EA2EF163EA4F0D536AAB8213377737DDE496A63F2F35A8D8BCF0A` | `4EB97520295D11050C7AD7184E7C6E02D9164C85DA0685E9396BF922BC1CBD9F` |
| Xenobiological Synthesis | `38D5232F6099985BF1710EE372554E7A79648A333974F613D6C90D65B8EF899B` | `5FC76BEC30F2A2FCACF80A5643083725FD1EE7322D8F1D5A8AFFCCC84384C1E3` | `4E7A438BF3E4B4D129FA5F4EB1D64DA3E9A2B886E81E74D416EB33043341F722` |
| Materials | `A75D59F2153BBE9A7D4BDCB02105BCAA604FDC73A4E85F0A8EA82CD43F566048` | `104B387CAC3BE952A865FCDCDC0E3B5A1A208CDA0E202BDD3C0BA21E294D6BFB` | `35EC3C79DB5D7713A474848C1E7E1A0FBA42141B6DCF03C85CA86396B0250952` |
| Biomedical | `529EB153259BB5993DEC34A3DE6D8036D72508759148474D5BE54773D023B00C` | `040620D13A3B89AD5EAAC4C1C2D70A589A4FD65CC3963C2E97A1F81D51BC7163` | `581D2A47424498663472850841D72773D2017D827A12531EAFCE1E484D8ED5A7` |
| Conventional baseline | `48CD2DD6A7414320EDD8C173B8FFAFA24D9A488C7B3E4FC24A3CFD65AA8A4303` | `1E361C5F85585C4EB51AA0EA7BB2345CC21287A2EA0C7858CE93263F737B2A38` | `CD2E25EE929440258E00D3A719001528478B87F80E11C71F2DEA1EF78CE12087` |
| Cloning | `1792B55DD88B7F08042CAB28ECD9AA5FFCC7A2DBFDDD260927CA42C71477F37E` | `7318FF6926BBE23321DF66658355E19E88998954C0918861A33B994A45369A8D` | `8356BE9FCF587DB4BEF7DF8B4C38E8E133B7862BAD6404C866F9C0007CBB39EA` |
| Alien Arms | `BCA4A3C2E723D44506E71A874068E2472C172D5858F57929E8A345727F1041B2` | `EF7E5C23940B5AC3768092553E444708202BA9337BDF61876D898BFC4E7E7B52` | `680C6ECA414AB64D7ADC2AB9434FD080C0B92329F4E7BA4A30DC5024B445DD23` |
| Temporal | `5CF8B6B87CC079EF27C33333B29FD51A1A328350F77E328EDD74F27FC311AFF8` | `A46DDA28A3D915E280396C372607F66BA06F81BEBEE8F0CFAA7809D6B73EF980` | `18AE619910355C2C8E61B43CE6D85DB53578F3BB4655F814D11D1B0B41F87E42` |

Supporting source hashes: `common\scripted_effects\016_mengele_project_bridge_effects.txt` `3F444A410451C37DD9E2BE2387ADB40E5DEB36D8D022926FA17B5ECB9E6F5C2D`; `common\scripted_effects\016_mengele_project_stage_effects.txt` `5AC6A807101B489AC23944FDB7A8572A67BC87A76A47CAC5B7718844785690C4`; `common\script_constants\016_brilliant_scientist_constants.txt` `ADFEE7FE6093933C394C34C8A6A162795D4BDB4575512C476B417C1173B6E4A6`; `common\script_constants\016_brilliant_scientist_project_constants.txt` `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131`; `common\scripted_localisation\016_mengele_conventional_stage_costs.txt` `BF9DF537920BAA5F84959A1F39BDBDE827E2E297CFC203BEBD80AF6E929FE3B9`; `interface\016_brilliant_scientist_project_icons.gfx` `B039D16B4415929899EF336BE33C99F5633DDCD7BFB55E6E2B452AC842D135F4`.

## Handoff

### Parent reconciliation after the audit snapshot

The Electronics no-DLC requirement is intentional in the accepted conventional Prototype route. The parent updated `.tools/audit_mengele_project_adapter_contract.mjs` to test that route and the guarded Cloning completion bridge, then ran `node .tools/audit_mengele_project_adapter_contract.mjs` successfully. The source-only harness reported 221 adapter, 308 grant, 60 adoption, 3,072 Singularity, and 630 finish assertions. Its provider validity, native callbacks, and neutral API outcomes use stubs, so this resolves the stale harness assertion but does not establish engine behavior or the MCP probability comparisons listed above.

Changed by this auditor: only this report. No gameplay source was edited, staged, or committed. Parent action: resolve or explicitly accept the Teleportation/Robotics probability comparison gap before treating AI validation as complete; record the unavailable native-decision visual route; and arrange the separate probability evidence for the other weighted family slices without duplicating this source audit.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. `chaos-redux-scripted-gui` was not applied because these are native decision rows, not a scripted GUI surface.
