# Camp historical startup scope repair

Disposition: implemented narrow source repair; MCP comparison blocked; runtime outcome unverified.
Acceptance basis: parent task authorizes fixing the supplied new-game camp scope error while preserving initial behavior; parent explicitly accepted the call move and helper documentation clarification.
No staging or commit was performed, as instructed by the parent.

## Supplied fault and cause

The supplied attachment `C:/Users/klimp/.codex/attachments/151b5975-ba7b-4d6a-a9dd-63f1f4518271/pasted-text.txt` reports one `camp_occ_historical_setup` invalid-scope error at `common/on_actions/genocide_crisis_on_actions.txt:35`, dated `1936.01.01.12`, with provided scope `None`.
`on_startup` has default scope `none`; the scripted effect invocation requires a concrete scope, even though the helper body does not depend on its caller's ROOT.
The helper was invoked immediately after the existing `random_country` block had ended, returning execution to `None`.

## Files and exact patches

Runtime source changed: `common/on_actions/genocide_crisis_on_actions.txt`.
Existing helper documentation changed: `common/scripted_effects/camp_administration_occupation_effects.md`.
The existing occupation scripted effect and triggers were read without modification.

```diff
@@ -31,8 +31,8 @@
 				limit = { exists = yes }
 				camp_rework_run_versioned_migration = yes
 				camp_admin_register_cxt_content = yes
+				camp_occ_historical_setup = yes
 			}
-			camp_occ_historical_setup = yes
```

```diff
-| `camp_occ_historical_setup` | Existing startup chain, no ROOT dependency | Once-only explicit country origin snapshots and GER/JAP controlled-state registration | Existing package startup, integration owner |
+| `camp_occ_historical_setup` | Country invocation in existing startup chain; no ROOT dependency | Once-only explicit country origin snapshots and GER/JAP controlled-state registration | Existing package startup, integration owner |
```

The historical setup runs inside the existing single existing-country selection, after migration and CXT registration, with no additional country selection or iteration.
No recurring hooks, probability weights, selection pool, balance values, GUI, map files, event definitions, localisation, assets, or spreadsheet content changed.

## Backups and byte identity

Original bytes were copied before editing to `docs/testing/live_qa/20260913_campaign_start_repairs/baseline/camp/`, retaining each relative source path.
The tracked-file diff was inspected before editing; the startup file already contained user draft CXT registration and occupation setup additions, which were retained.
The baseline-to-result diff was reviewed after editing to isolate this repair from those drafts.

| File | Baseline SHA256 | Result SHA256 |
|---|---|---|
| `common/on_actions/genocide_crisis_on_actions.txt` | `535f1ff655a813e1b6e86f6a10f01399255eadc64138536b8d73300a09bfd805` | `0f9116a5c1db735b9ea5ce577ca4de2fba582cae72debb474ef70e129e9ee32c` |
| `common/scripted_effects/camp_administration_occupation_effects.md` | `63ddb89fa5a4b529d23b7144a762f0671deca2e07bd22ded76432d0d9f61fcfb` | `08a327f333918bdb245600b728d5ae92841538d2e9b62107b7b5adce512a7368` |

## Preserved helper contract

| Helper | Scope and inputs | Outputs and side effects | Call sites |
|---|---|---|---|
| `camp_occ_historical_setup` | Concrete country invocation; no caller ROOT/PREV/FROM dependency; no required inputs | Global `camp_occ_historical_seeded` guard; invokes 21 explicit historical origins, then GER/JAP controlled-state registration | Sole production invocation in existing camp `on_startup` |
| `camp_occ_seed_origin` | Explicit historical country and temporary `camp_occ_origin_ceiling_input_k` | Once-only European owned-state snapshots, origin ceiling allocation, unassigned residual, country/state guards | The 21 explicit country blocks inside historical setup |
| `camp_occ_track_controlled_state` | Explicit controlled state | Controller-owned eligible-state registry and conditional cohort registration | GER/JAP setup scans and existing state-control callback |

Origin tags remain POL, SOV, ROM, LAT, LIT, EST, GER, HUN, CZE, AUS, ENG, FRA, HOL, BEL, DEN, NOR, GRE, YUG, ITA, BUL, and ALB.
The source allocation's `PREV` remains the explicit origin country because it is used inside that country's `every_owned_state` block.
The eligible registry's `PREV` remains the actual state because it is used inside that state's `CONTROLLER` block.
Neither depends on the arbitrary existing country used to enter the startup helper.
At the reported January 1936 date, unchanged campaign chronology gates disallow Japanese campaign enrollment before July 1937 and German campaign enrollment before June 1941; origin snapshots and eligible-state tracking remain the intended initial work.
No loss/death effect was added.

Constants and tuning: no change; existing `camp_occ_origin_k`, profile, and chronology gates are retained.
Event targets and cleanup: no change; no event target is created by the setup helper, and its existing global/per-origin/state guards retain once-only behavior.
Migration plan: this is a call-site scope correction; the existing migration still precedes setup, with no extraction or replacement of the helper.

## References consulted

- `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Required offline core pages in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, General on actions/on_startup: default scope is `none`, and manual scoping is necessary; its file example uses explicit countries inside startup.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, Scripted effects, and `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, scope switching and PREV.
- Installed vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`: on_startup registration.
- Installed vanilla `common/on_actions/02_dod_on_actions.txt:3`: startup enters YUG before invoking a scoped effect; `common/on_actions/00_on_actions.txt:2` enters actual states before startup building effects.
- Installed vanilla `documentation/effects_documentation.md`, `set_global_flag` and country iteration entries; `documentation/triggers_documentation.md`, `has_global_flag`; `documentation/script_concept_documentation.md`, Script Constants; `common/script_constants/documentation.md`.
- Existing `common/scripted_effects/chaosx_dynamic_effects.txt` and matching markdown were checked before choosing to retain the owning helper.
- Existing occupation helper documentation, `camp_occ_seed_origin`, `camp_occ_track_controlled_state`, `camp_occ_try_register_current_state`, the versioned migration and CXT registration helpers, and occupation chronology triggers were reviewed.

## Meaningful validation

An in-memory byte contract check passed: result startup bytes equal baseline bytes with only the shown call move; exactly one invocation remains.
The unchanged setup body has no ROOT, PREV, or FROM references, contains exactly 21 explicit origin calls and exactly two controlled-state scans, and retains the global seeded guard.
The origin helper retains its country seeded guard and explicit origin-to-owned-state scope relationships.
Baseline-to-result diffs confirm the existing country selection and order migration -> CXT registration -> historical setup, with no changed recurring callback or tuning values.
These are source contract checks rather than a simulation of HOI4 execution.

## MCP evidence and limitations

Read-only `hoi4.event_inspect` scan and trace were attempted for `selector = { kind = file, sourcePath = common/on_actions/genocide_crisis_on_actions.txt }` with bounded depth/nodes/edges and helper expansion.
Both returned `EVENT_INSPECTED_PARTIAL`, `status = ok`, revision `89a41bf795f9f785d9608f46b13e5441301ef973736cdeae2e4c6ff3dcc7b70a`, graph hash `0a92f87d2a53dafd458e0ad408df9590537e4a8ff760008e089e51fc592bafcb`.
Validation was false: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
The returned helper count was zero, so this evidence does not establish the corrected helper's runtime scope.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68c59eaf366c4ce7f6790734452977d7f3a126ec78133edf30aacb44339d7c52/d2703c1f153ca517ce49a42d24fd3f0ee7eed8961d42e8884a8dcb94dd1cef9e/event-trace-89a41bf795f9.json`.
One bounded artifact read at offset 0, length 12000 returned a stringified JSON transport envelope with application/json MIME and base64 byte-range payload; it was not fully reconstructed or used for graph conclusions.

Read-only scope renders with bare and `mod:` source paths returned `EVENT_RENDERED_PARTIAL`, zero selected nodes, and the same deferred-helper validation limitation.
Bare-path scope manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/648fc96d38ceafe837da4977f402397bb9b13eef423800038c1b1a87737c0814/1c4312f5a28037b94899df58477136c1d83d37419cbe852ab5c681c5f39e0aef/event-scope-89a41bf795f9-manifest.json`.
These empty selected-node renders do not validate the startup scope correction.

Read-only `hoi4.event_compare` with `before.artifactUri` pointing at the trace artifact and `refresh = true` returned `status = error`, `code = EVENT_GRAPH_ARTIFACT_INVALID`, blocker `Event graph artifact uses an unsupported schema version`.
No comparison artifact or completed after graph was returned.
Earlier unsupported selector and comparison-key attempts produced only input-validation errors and no writes.
MCP did not mutate source.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was introduced.
Runtime outcome is unverified; HOI4 was not launched or controlled.
MCP helper projections were deferred, file renders selected zero nodes, and the graph comparison rejected its input artifact's schema as described above.
No AI/probability helper was designed or changed; the existing selection, pool, weights, and number of selections remain identical, and no further subagent was spawned under the parent's restriction.
The parent must review the narrow patch and carry these evidence limits into the integrated report.
This handoff makes no all-campaign completion claim.
