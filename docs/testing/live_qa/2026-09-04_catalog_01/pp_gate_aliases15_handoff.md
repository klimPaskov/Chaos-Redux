# Launch 14 political power gate alias handoff

Status: the bounded five-location parser repair is complete. Gameplay source writes ended after the five exact trigger-key substitutions. No launch was performed and no commit was created.

## Scope and native error evidence

The source scope was limited to the five `political_power` trigger keys reported by the fresh log at `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_14/logs/error.log`.

The log SHA-256 is `E374A210E4CC10F974A83FC17713C5E3166AB4CD0CA43805A22FCF8392C75549`.

| Source | Invalid trigger rows | Unknown trigger rows | Reported source lines |
| --- | ---: | ---: | --- |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | 24 | 24 | 822, 873, 1003, with 8 repeated invalid and 8 repeated unknown rows per line |
| `common/scripted_effects/031_random_terror_effects.txt` | 8 | 8 | 3181, with 8 repeated invalid and 8 repeated unknown rows |
| `events/031_terrorist_attack.txt` | 1 | 1 | 314 |

The assigned total was 33 invalid rows and 33 paired unknown rows across five unique source locations. Repeated rows are repeated native diagnostics for the same source location.

## Source changes

`common/scripted_effects/021_random_civil_war_parent_effects.txt` changed the three gates in `event021_parent_prepare_route_evidence` at lines 822, 873, and 1003.

Each line changed from `political_power < constant:event021_parent_tuning.minimum_political_authority` to `has_political_power < constant:event021_parent_tuning.minimum_political_authority`.

`common/scripted_effects/031_random_terror_effects.txt` changed the country-scoped sponsor gate in `random_terror_commit_sponsor_request` at line 3181.

The line changed from `political_power > constant:random_terror_cost.partner_sponsor_political_power` to `has_political_power > constant:random_terror_cost.partner_sponsor_political_power` inside `event_target:random_terror_sponsor_target`.

`events/031_terrorist_attack.txt` changed the trigger for option `chaosx.nr31.42.a` in event `chaosx.nr31.42` at line 314.

The line changed from `political_power > constant:random_terror_cost.partner_sponsor_political_power` to `has_political_power > constant:random_terror_cost.partner_sponsor_political_power`.

All five edits preserve indentation, country or event-option scope, comparator direction, constant token, polarity, equipment gates, costs, effects, and AI chance blocks. No decision, mission, scripted GUI, or localisation identifiers changed. No `ai_will_do` or weighted modifier surface was edited, so no probability audit was required.

## Backups and hash guards

Immediate pre-edit copies are stored under `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_pp_gate_aliases15/` with the same relative paths as the source files.

| Source | Backup SHA-256 | Current SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `47EB91F8C3CC6E59D887CA9B3F88CFA3B1FD641C4D34815AEBE6B60DA3940EB8` | `2B3010670576F3C741684AAC2C8A2E590360670871F1AB62FD0BE99C76445D3E` |
| `common/scripted_effects/031_random_terror_effects.txt` | `2E096C1AB7AB6342D1647408E1852277467416A4F211FF315E05F4770F8D1BE2` | `830CBE5F7812DCADA0450CCC4AA86164F80975EDDCD14021C6D8E5BECD4A6149` |
| `events/031_terrorist_attack.txt` | `3D833B0B656531755A24C5A19D4C7EBE9F7C9C1CEDD19F32E7858C2982D288D2` | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` |

The inverse-transform validation compared each current file with its immediate backup. It found exactly three changed lines in the civil-war file, one changed line in the terror-effects file, and one changed line in the Event 31 file. It found no remaining trigger-key line matching `political_power <...` or `political_power >...` in those files. The full-file line counts were unchanged.

## Reference review

The offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` entry for `has_political_power` documents comparison use such as `has_political_power > 100`.

The installed vanilla documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` documents `has_political_power` as a COUNTRY-scope amount trigger.

Vanilla decision precedents in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/` use both strict `has_political_power < ...` and `has_political_power > ...` gates.

## Narrow Event 31 MCP evidence

The read-only Event MCP selector was `{ kind = event, eventId = chaosx.nr31.42 }` in workspace `mod_chaos_redux_ea3b2d67c2c0` with `direction = both`, `expandHelpers = false`, `maxDepth = 2`, and `maxNodes = 80`.

Before the edit, `hoi4.event_inspect` returned status `ok`, code `EVENT_INSPECTED_PARTIAL`, revision `94c858964b40bbc800c3b1257959c1f255c4f0b3d793261b508a3135a0b5f9cc`, and graph hash `cd1c8b663f31f3f65c1161e5793833a89c7bac3bcf77da7fa0188c074c412d5c`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbbc34e89096f2f5880ccac014a6c02e87a2c7a719b401e4efbbb9fea7a1092e/8e6975e942b91b914277b5f6ccb670e320061aecd3ee635065ee619287893969/event-lint-94c858964b40.json`.

Before the edit, `hoi4.event_render` with `view = options` returned status `ok`, code `EVENT_RENDERED_PARTIAL`, revision `94c858964b40bbc800c3b1257959c1f255c4f0b3d793261b508a3135a0b5f9cc`, graph hash `cd1c8b663f31f3f65c1161e5793833a89c7bac3bcf77da7fa0188c074c412d5c`, and layout hash `ae2d4d0116fd5be7c8dce4f504b30f121dd1617174b4c1c30c8edaed084dc356`.

After the edit, `hoi4.event_inspect` returned status `ok`, code `EVENT_INSPECTED_PARTIAL`, revision `86077b1d5f2fc155ad9a17fff30027ac88a6ac544a8a3c242b19b79f1d6b0260`, and graph hash `78e4b81f75f2e5856ae6ecdf7c53d94f0d4a1ce5f0dd24e5edc408c4eb844ad3`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4b2956e026f2aa8570702ff0175efd31cb1aadc45e850ef58e4bb85ad619a61/79eab8f8e04632488e80ddc1d4baae3f7979806cd1a261d4f6e7390518cbd4b0/event-lint-86077b1d5f2f.json`.

After the edit, `hoi4.event_render` with `view = options` returned status `ok`, code `EVENT_RENDERED_PARTIAL`, revision `86077b1d5f2fc155ad9a17fff30027ac88a6ac544a8a3c242b19b79f1d6b0260`, graph hash `78e4b81f75f2e5856ae6ecdf7c53d94f0d4a1ce5f0dd24e5edc408c4eb844ad3`, and layout hash `50d9c6169871529b18950db57014fc0a5b4e97b352d989ec49c35c8f1d8d476f`. Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54c0f8b74a300a87414ecdac0adced89d9ebcf6fa24402e3bd83b2f27a451978/f7e0a9b9b3454ad9ed914454c03515a3cf9751b328e1138ed40356dcb3ea7aec/event-options-86077b1d5f2f-manifest.json`.

Both inspect and render calls reported the expected focused-analysis notice, with status `ok`, no tool blockers, and stable selected event counts. The focused MCP pass does not perform a full workspace helper or lifecycle analysis.

The required `hoi4.event_compare` route was attempted with the cached pre and post revisions and returned blocker `EVENT_REVISION_NOT_CACHED`. A second attempt with the inspect artifact URIs returned blocker `EVENT_GRAPH_ARTIFACT_INVALID` because those lint artifacts use an unsupported graph schema. These exact compare blockers are recorded rather than treated as a source-only comparison.

## Remaining scope and skipped validation

The parent agent owns the subsequent native launch validation. Remaining invalid aliases elsewhere in the launch log, including unrelated scripted-trigger and protected or parent-owned surfaces, were outside this five-location tranche and were left unchanged.

No HOI4 launch was performed by this subagent. No probability auditor was run because no weighted AI surface changed. No broad global replacement or broad parser rewrite was attempted.

No plan handoff was needed.

Parent native launch 15 observed zero Invalid trigger political_power records across the full fresh log, with all three assigned files unchanged during launch.
This is parser acceptance only; campaign option eligibility and actual sponsorship payment remain untested.
