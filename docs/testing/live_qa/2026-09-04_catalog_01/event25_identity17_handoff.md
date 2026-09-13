# Event 025 identity trigger repair handoff

Status: implemented and source-ready for parent launch17 parser validation.

No launch or commit was performed by this worker.

## Finding

The fresh evidence at `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_16/logs/error.log` reports unsupported `is_same_country` triggers in `events/025_alien_technology_in_antarctica.txt` at source lines 446, 468, 490, 512, and 534.

The five sites are the trigger gates for `chaosx.nr25.100`, `chaosx.nr25.130`, `chaosx.nr25.160`, `chaosx.nr25.190`, and `chaosx.nr25.220`.

## Exact bounded patch

Each site was changed from `is_same_country = ROOT` to `tag = ROOT` inside its existing scheduler event-target block.

| Source line | Event | Event target | Replacement |
| ---: | --- | --- | --- |
| 446 | `chaosx.nr25.100` | `chaosx_nr25_evolution_active_signal_scheduler` | `is_same_country = ROOT` to `tag = ROOT` |
| 468 | `chaosx.nr25.130` | `chaosx_nr25_evolution_something_survived_scheduler` | `is_same_country = ROOT` to `tag = ROOT` |
| 490 | `chaosx.nr25.160` | `chaosx_nr25_evolution_militarised_antarctica_scheduler` | `is_same_country = ROOT` to `tag = ROOT` |
| 512 | `chaosx.nr25.190` | `chaosx_nr25_evolution_wreck_breaking_apart_scheduler` | `is_same_country = ROOT` to `tag = ROOT` |
| 534 | `chaosx.nr25.220` | `chaosx_nr25_evolution_technology_changes_users_scheduler` | `is_same_country = ROOT` to `tag = ROOT` |

The only gameplay source file changed is `events/025_alien_technology_in_antarctica.txt`.

No event IDs, titles, descriptions, pictures, pending flags, global flags, country flags, event-target names, options, effects, `ai_chance` values, or option costs were changed.

## Scope and identity semantics

Each affected block is a `country_event` trigger evaluated in the event's country scope, so `ROOT` is the country receiving and evaluating that event.

The nested `event_target:<scheduler>` block changes the current scope to the saved scheduler country, and `tag = ROOT` compares that country's actual current tag with the event ROOT country.

The offline Triggers reference and vanilla trigger documentation define `tag` as a country trigger accepting a scope target and checking the actual tag, while excluding dynamic countries that merely share an original tag.

The offline Scopes and event references define ROOT as the root node of the current block and document event-target scopes; these semantics make `tag = ROOT` the supported exact-current-country comparison here.

`original_tag = ROOT` was deliberately not used because it would include dynamic countries originating from the same tag and would broaden the existing identity gate.

None of the five predicates uses `FROM`, so no FROM substitution or scope reinterpretation was introduced.

The result preserves the existing gate: each evolution event is eligible only when its saved scheduler target is the same current country as the event ROOT country.

## Backup and source drift guard

The complete pre-patch event file was copied immediately to `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event25_identity17/events/025_alien_technology_in_antarctica.txt`.

The source remained stable during the copy, and the backup matched the source byte-for-byte before patching.

The pre-patch source and backup were 19,759 bytes with SHA-256 `E756E3DAC491E7FCE57DC9B1D62CF63365BE5986A613EDBECB0A56B77910633F`.

The post-patch source is 19,699 bytes with SHA-256 `92BF463D734C634AFECCAE58DE516F8DCAF2FFC8C765292ADE7244C9A7866EE0`.

## Source validation

The post-patch file contains zero `is_same_country` occurrences and exactly five `tag = ROOT` replacements at the assigned source lines.

Reconstructing the pre-patch text by replacing the five new `tag = ROOT` predicates with `is_same_country = ROOT` produced an exact text match to the backup, demonstrating that the edit is limited to the five requested aliases.

## Narrow Event MCP evidence

Read-only Event MCP inspection and unresolved rendering were run for all five affected event IDs.

The pre-patch inspection and render were captured for `chaosx.nr25.100` with status `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, revision `17b3aac359b767085af37746c2ad9e7a1bc9437f4d9712ff9ce7e3d72ba43614`, and graph hash `6b4402c3520bc5cdc2b4f108f49e88e9c0a8aec417e2b2b72722d9fcdc91e7c5`.

The pre-patch inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81bfc9b9497bebc8072979e46473cde3c13ca7cfea696d5458e4ce3c27eededd/b3d624d3f176f4e2c85017c1d80c006984fc26a410fc0667d351b8f100ddbe2b/event-lint-17b3aac359b7.json`.

The pre-patch render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69e1569b9eb5938c98979dc7ee9af456e8460e598a512a278f738f6e9c349625/b5f2d4b65413256c83b972966f7f413e9e1a937467feb48e9cbca1590befca85/event-unresolved-17b3aac359b7-manifest.json`.

The post-patch inspection and render for `chaosx.nr25.100` returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, revision `1e7516fb00135d5559a8dfcc786dbeaeac9e3850d4f17dad626bbe811df96bc0`, and graph hash `7a39b49e488ea4f2b2e4549cb4640a598037d2bf0fb6587b1a9e3ea496a3c587`.

The post-patch inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af6548ff6273cc52c96079079d0444f36de4561c7848292c478477dc58943100/dff19c28cfc00734da1fb0a9a6d25d84f429d7a8da62b3de42362a338f5355ac/event-lint-1e7516fb0013.json`.

The post-patch render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71585920ec42535553d89f51f5ab9164dc9e1735ce33d7d0a5b27d324632dcf4/3da4f08b17d56240be2459cbbd350ebf361f666f6fe155225620d24655c1fbb2/event-unresolved-1e7516fb0013-manifest.json`.

The other four event IDs returned the same post-patch partial status and graph revision/hash during their focused inspect and render calls.

Both MCP results report that workspace-wide helper projections and lifecycle passes were deferred, with zero helper nodes and `MCP_INLINE_FILES_TRUNCATED` inventory diagnostics.

The before/after event comparison was attempted with the lint artifacts and returned `EVENT_GRAPH_ARTIFACT_INVALID` because the event graph artifact used an unsupported schema version.

A revision-based comparison retry returned `EVENT_REVISION_NOT_CACHED` because the requested event graph revision was not cached.

These MCP results provide event linkage and render evidence only; no helper parser, helper registration, or helper lifecycle pass is claimed.

## Weighted surface assessment

The five changes are trigger eligibility repairs only.

Existing options retain their `ai_chance = { base = 100 }` blocks, and no AI weight, event probability, MTTH, random-list weight, strategy factor, or option cost changed.

A probability-auditor baseline and probability comparison were therefore not required for this alias-only repair.

## Remaining limits and parent validation

The worker did not launch Hearts of Iron IV, so native parser confirmation and campaign behavior remain parent-owned.

Parent launch17 should confirm that the five Event 025 `is_same_country` diagnostics are absent while preserving the scheduler-target gate behavior.

Other invalid triggers in other event files remain outside this exact Event 025 scope and were not changed here.

No simplification or fallback was used, and no unrelated source files were edited.

Skills applied were `chaos-redux-subagents` and `chaos-redux-events`.
