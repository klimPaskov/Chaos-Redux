# Event 016 native-provider dispatch review

Date: 2026-09-02

Audit owner: `/root/timer_and_transaction_audit`

Mode: bounded, read-only source audit. No gameplay, localisation, configuration, save, log, or unrelated Event 026 files were changed, and no commit or game launch was performed.

## Executive disposition

The current source has a deterministic P1 completion-loss defect in `brilliant_scientist_record_new_project_prototype`. The wrapper selects the Mengele bridge from the broad `is_mengele_clone_directorate_country` identity test, but the bridge accepts only `brilliant_scientist_mengele_project_provider_is_valid`; that provider gate rejects `brilliant_scientist_current_host`. A country carrying both identities therefore enters the bridge, applies no prototype result, and never reaches the native Kruger stage callback.

Minimal owner remediation: change the wrapper branch selector to `brilliant_scientist_mengele_project_provider_is_valid = yes`, leaving the native `else` path and the bridge family effects unchanged. This preserves pure Mengele dispatch, routes a dual-identity active host through the existing native completion helper, and fails closed for an invalid Mengele provider without inventing project history. No gameplay patch was applied in this audit.

## Source evidence and callback reachability

- `common/special_projects/projects/016_brilliant_scientist_projects.txt:76-101` defines `sp_brilliant_scientist_computational_engine` with an OR of Kruger and Mengele visibility/availability gates, then calls `brilliant_scientist_record_new_project_prototype` from `project_output.country_effects` after setting the exact family temporary at lines 97-102.
- The same project-output pattern is present for advanced materials at lines 145-172, biomedical acceleration at lines 215-242, quantum transit at lines 285-312, cloning at lines 355-381, autonomous cognition at lines 424-451, paleogenetics at lines 494-521, xenobiological synthesis at lines 564-591, alien arms at lines 634-661, and temporal mechanics at lines 704-731.
- The native Kruger research triggers require `brilliant_scientist_is_current_host`, a valid primary facility, no active project incident, Theory stage, and prototype capacity; computation is shown at `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:1752-1766`, with the same gate shape for the other families through line 1911.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1279-1294` currently branches on `is_mengele_clone_directorate_country` at lines 1280-1283 and calls the native path only in `else` at lines 1284-1293.
- `common/scripted_effects/016_mengele_project_bridge_effects.txt:11-117` initializes `brilliant_scientist_mengele_project_result_applied` to zero, guards every Mengele family result with `brilliant_scientist_mengele_project_provider_is_valid`, applies no Event 016 stage arrays or capacity, and resets `brilliant_scientist_project_family` to the `none` constant at line 116.
- `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:9-13` defines the provider gate as Mengele identity, NOT `brilliant_scientist_current_host`, and NOT `brilliant_scientist_project_incident_active`.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1239-1276` is not a fallback for these custom Event 016 prototype IDs. Its four conditions recognize only reused native projects (`sp_air_radar`, flying-bomb/jet projects, `sp_nuclear_reactor`, and the three native biological bombs), not the ten `sp_brilliant_scientist_*` prototype IDs listed above.
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt:12-22` calls that reused-native synchronizer only from `on_project_completion` when the completing country is the current host. It does not re-run the custom project-output wrapper for the custom Event 016 prototype IDs.
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt:90-93` defines current-host status as the independent country flag plus the Kruger character. `common/scripted_triggers/germany_mengele_triggers.txt:87-96` defines Mengele identity as `exists = yes` plus one of several independent flags or cosmetic tags. Neither predicate clears or negates the other, and `common/scripted_effects/016_brilliant_scientist_effects.txt:462-466` sets current-host state without a Mengele-identity exclusion.

Together these paths make the collision source-reachable: the custom special project can be visible to both routes, its one completion output calls the wrapper, the broad identity branch prevents the native `else`, and the reused-native synchronizer cannot recover it.

## Four-case dispatch matrix

| Case | Wrapper branch under current source | Result under current source | Result after the minimal selector fix |
| --- | --- | --- | --- |
| Pure Kruger: current host, not Mengele, no incident, valid Theory/capacity | Native `else` | `brilliant_scientist_complete_native_prototype_stage` can pass its exact context/family/Theory/capacity guard and advance the stage | Unchanged native completion |
| Pure Mengele: Mengele identity, not current host, no incident | Mengele bridge | Provider gate passes and the family-specific directorate flag/modifier or custom technology is applied; Kruger arrays remain untouched | Unchanged Mengele bridge |
| Mengele identity plus active Kruger host, no incident, valid native Theory/capacity | Mengele bridge because the broad identity test wins | Provider gate fails on current host; every bridge family branch is skipped, `brilliant_scientist_project_family` is reset to `none`, and native Kruger stage/history/capacity output is suppressed | Provider gate passes only when the country is a real Mengele provider, so this case takes native completion |
| Invalid, absent/dead, or incident provider | Broad branch may be false for an absent scope, or true then fail the provider gate for an incident Mengele scope | Absent/dead scopes fail the identity/context checks and do not fabricate history; an incident-active Mengele scope enters the bridge but all result branches skip and the family temporary is reset | The exact-provider selector routes invalid Mengele scopes to native `else`; `brilliant_scientist_project_context_is_valid` still fails without an existing current host/facility, so no native history is fabricated. An existing-but-capitulated country is not explicitly tested by either current provider predicate, so that runtime state is an evidence limit rather than a certified case. |

## Native completion and cleanup checks

- `brilliant_scientist_complete_native_prototype_stage` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:166-192` sets the requested stage to Prototype, loads the family index, and only calls `brilliant_scientist_advance_project_to_requested_stage` when `brilliant_scientist_project_context_is_valid`, `brilliant_scientist_project_family_input_is_valid`, the selected entry is Theory, and capacity is at least the prototype threshold.
- `brilliant_scientist_project_context_is_valid` at `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:57-65` requires an existing country, current host, valid primary facility, and no terminal/world-end flags. This is the relevant fail-closed guard for a dead or invalid native callback.
- The advancing effect records the stage only after the requested stage is valid and greater than the current array entry at `common/scripted_effects/016_brilliant_scientist_effects.txt:1122-1144`; it then calls `brilliant_scientist_record_project_stage_on_kruger` and refreshes counts. A failed context or stage/capacity guard does not write stage history.
- The Mengele bridge's explicit final reset at `common/scripted_effects/016_mengele_project_bridge_effects.txt:115-117` prevents its temporary family from leaking into later effects. The native helper does not reset the caller's temporary family when its context guard fails, matching the canonical reused-native synchronizer path; this is effect-chain hygiene and an engine-behavior limit, not evidence of fabricated history.
- `brilliant_scientist_finalize_owned_project_stage` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:60-66` clears the active native receipt variables and refreshes gross capacity only for the timed integration lifecycle. It is not called by the special-project output wrapper, so the wrapper selector fix must not add a finalize call or alter native special-project payment/history ownership.
- The contract requires native prototype integration to preserve one native reward and one Capacity charge and forbids invalid-host/facility/terminal callbacks from producing a stage reward at `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:141-150`. The recommended selector fix aligns the dispatch with that contract without changing reward, cost, stage, or AI formulas.

## Severity-ranked findings

### P1 — dual-identity active host loses native prototype completion

Affected identifier: `brilliant_scientist_record_new_project_prototype`.

Evidence: `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1279-1294`; `common/scripted_effects/016_mengele_project_bridge_effects.txt:11-117`; `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:9-13`; custom project outputs at `common/special_projects/projects/016_brilliant_scientist_projects.txt:76-731`.

Remediation: select the Mengele bridge with `brilliant_scientist_mengele_project_provider_is_valid = yes` rather than the broad identity trigger. Keep the native `else` and existing `brilliant_scientist_complete_native_prototype_stage` guards intact.

### P2 — capitulated-but-existing provider semantics are not source-proven

`is_mengele_clone_directorate_country` checks `exists = yes` and identity flags/tags but does not test `is_capitulated`; the bridge provider predicate likewise has no explicit capitulation/death condition. A deleted country is covered by `exists = yes` failure, while a surviving but capitulated scope is not distinguishable from an active Mengele provider in the source. No concrete callback path was added or changed for this state in this audit, so this remains an engine/runtime evidence limit and must not be folded into the P1 selector fix without an accepted lifecycle requirement.

### No additional completion or history defect found

Invalid family, non-Theory stage, insufficient capacity, missing host, missing facility, terminal, and world-end native callbacks are guarded before stage advancement. The bridge never writes Kruger history or capacity and resets its family temporary after all branches. No duplicate native fallback exists for these custom project IDs.

## Decision, UI, AI, localisation, and cleanup boundary

This audit concerns special-project completion dispatch rather than a decision-owned GUI surface, ordinary decision category density, mission quality, or a probability-bearing AI block. No GUI inspect/render or probability audit is claimed, and no weight, cost, duration, tooltip, localisation, or decision surface was changed. The custom project `visible`/`available` OR gates and the native/Mengele route locks were source-reviewed only; live in-game availability and completion ordering remain unproven.

## Narrow Event MCP evidence

One focused read-only request was made against source line 1279 with `mode = trace`, `direction = downstream`, `selector = { kind = source, sourcePath = common/scripted_effects/016_brilliant_scientist_project_effects.txt, line = 1279 }`, `expandHelpers = yes`, `maxDepth = 4`, `maxNodes = 40`, `maxEdges = 80`, and `refresh = yes`.

The server returned `status = ok`, `code = EVENT_INSPECTED_PARTIAL`, `revision = 3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f`, and `graphHash = 33b3de6736a2f97d06a3ec40f40d528d1018bbec9b4a3064ed2874933698791a`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/427e6fdf404189288c0bbd97dbe5c926582775a1b09ca7b17771614eb66cbfa1/451c570a5becd4beaf7f4f9d33ef3a8e605491f8bf5f90713ad9ffea7f27d4e0/event-trace-3278b34c5334.json` with artifact SHA256 `427e6fdf404189288c0bbd97dbe5c926582775a1b09ca7b17771614eb66cbfa1`.

The result is not full lifecycle acceptance: the trace reported `helpers = 0`, `validation.passed = false`, and `event-analysis` said large-workspace helper projections and lifecycle passes were deferred. The boundary was `direction = downstream`, `maxDepth = 4`, `maxNodes = 40`, `maxEdges = 80`, with `refresh = true`; inline source inventory was truncated to 64 of 368 paths (`MCP_INLINE_FILES_TRUNCATED`). The artifact and source inspection therefore support the deterministic branch finding but do not prove engine callback ordering or live gameplay behavior.

## Current source hashes

These hashes were captured after the read-only review and before this handoff was written.

| File | SHA256 |
| --- | --- |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | `D058FF42828DF16E43083BE79076577121D663C6031FF0B27CBA6576A1CCD37F` |
| `common/scripted_effects/016_mengele_project_bridge_effects.txt` | `700BF3A191F61A395103B6FB29541DE6A1828D55C035DD05D5A2CCD9D874DF19` |
| `common/scripted_triggers/016_mengele_project_bridge_triggers.txt` | `02649BE801E1BDCD9A5054CAA4A9CF1299F541C4AD4A7C754287FA711CCC778B` |
| `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` | `5B82CB6B8A816DB6039F7EAB08637CA62C9FBE667487E140DDD11A89216A05E8` |
| `common/scripted_triggers/germany_mengele_triggers.txt` | `B55D74CBA83C3B03026526F6DF5668AEB93E50AF0CE3E6654101B0144BEAF949` |
| `common/scripted_triggers/016_brilliant_scientist_triggers.txt` | `EF9B7964617CB6B73CF5BC230FD31751081A0FFC21CCA999575DBB45F3853636` |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `E24D19FD70CF52C3374BAC1553B83444147F86546DB981601C42AE6E3DFBF0DC` |
| `common/on_actions/016_brilliant_scientist_project_on_actions.txt` | `D56934AC7016E8229A135B63B6240A2ECC70A37BCCE3DC3AEB836B60D08125D8` |
| `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` | `A9B0724B553708C7BB47430FB1D14945C876646F31F0042D5ABCA771F1939CAB` |

## Acceptance limits

The source review is not a whole-Event 016 completion certification. The P1 branch defect was deterministic in the prepatch source, and the owner selector correction and bounded postpatch recheck are recorded below. A successful source trace would still not replace user-owned live testing of pure Kruger, pure Mengele, dual-identity host, incident, and country-loss cases.

## Owner selector patch postreview

The owner applied the minimal one-line correction at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1281`: the wrapper now tests `brilliant_scientist_mengele_project_provider_is_valid = yes` before calling `brilliant_scientist_record_mengele_project_prototype`. The native `else` path, Mengele bridge family effects, stage guards, costs, durations, rewards, and AI values are unchanged by this correction.

The four-case source matrix was re-evaluated against the patched selector.

- Pure Kruger (not Mengele, current host, valid Theory/capacity) fails the provider gate and takes native `else`; the existing native completion helper can advance the stage.
- Pure Mengele (Mengele identity, not current host, no incident) passes the provider gate and takes the Mengele bridge; its provider-owned result remains separate from Kruger stage history.
- Mengele identity plus active Kruger host fails the provider gate on `NOT = { has_country_flag = brilliant_scientist_current_host }` and now takes native `else`; the existing context, family, Theory, capacity, and stage-advance guards are the intended native completion path.
- Invalid, absent/dead, or incident Mengele provider fails the provider gate; an absent/dead scope also fails the native existence/current-host context, while a pure non-host incident provider fails native context and records no stage history. The previously recorded capitulated-but-existing provider uncertainty remains outside this one-line patch.

The original P1 is therefore resolved at source for the requested cases. The native helper still does not clear the caller's temporary family when its context guard fails, but this remains the canonical native-sync hygiene limit and no fabricated history is written. No additional source defect was found in this postpatch matrix.

## Postpatch MCP recheck and limits

The same bounded source-helper `hoi4.event_inspect` request was rerun with `mode = trace`, `direction = downstream`, `selector = { kind = source, sourcePath = common/scripted_effects/016_brilliant_scientist_project_effects.txt, line = 1279 }`, `expandHelpers = yes`, `maxDepth = 4`, `maxNodes = 40`, `maxEdges = 80`, and `refresh = yes`. The server returned `EVENT_INSPECTED_PARTIAL`, but it reused the prior revision `3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f`, graph hash `33b3de6736a2f97d06a3ec40f40d528d1018bbec9b4a3064ed2874933698791a`, and trace artifact `event-trace-3278b34c5334.json` with artifact SHA256 `427e6fdf404189288c0bbd97dbe5c926582775a1b09ca7b17771614eb66cbfa1`. The response again reported `helpers = 0`, `validation.passed = false`, and deferred workspace-wide helper/lifecycle analysis.

The matching bounded `hoi4.event_render` request used `view = scope` with the same source selector, downstream direction, helper expansion, depth 4, node limit 40, and `refresh = yes`. It returned `EVENT_RENDERED_PARTIAL` at that same old revision and graph hash, with `selectedNodes = 40`, `omittedNodes = 42436`, `helpers = 0`, `branchRenders = 0`, and validation false. The returned render hashes were manifest `be8e656f832f7566f9c324a1494d4d3cd6d6b866072bad7b3cd5e053857637a6`, JSON `28a3b5e1375fcecaee8def96824fb7902f2db758a30a6f62793f343792ab3891`, SVG `af6c9d24b220eaf63752b8eb239bcdc424f61e8ab0ae55d9fa0c1d35d0d688ab`, and PNG `5717eefa50756b392b6824c25e26223b6cc5a35cf2eda10c89d5e288f3273c82`.

A legal revision-cache comparison probe using `before = { revision = 3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f }` and the same explicit `after` revision returned `EVENT_REVISION_NOT_CACHED`, `artifactCount = 0`, and no diagnostics. No current postpatch event-graph revision was emitted, so no semantic before/after comparison is claimed. The repeated zero-helper focused projection is a tool-coverage/cache result, not engine evidence and not proof that the patched scripted effects were expanded or executed.

The MCP inline inventory remained truncated to 64 of 368 paths (`MCP_INLINE_FILES_TRUNCATED`), with the same boundary `direction = downstream`, `maxDepth = 4`, `maxNodes = 40`, `maxEdges = 80`, `expandHelpers = yes`, and `refresh = yes`. These postpatch artifacts do not supersede the source matrix or establish live callback ordering.

## Postpatch source hash

The patched `common/scripted_effects/016_brilliant_scientist_project_effects.txt` SHA256 is `6406E3E8087CD475193A6CA470A81F2976E889A6831098897B9AD334CBA349D1`.

The P1 source correction is accepted for this bounded dispatch review. The handoff still does not claim whole-Event 016 completion, capitulated-provider acceptance, engine callback-order proof, or user-owned live testing.
