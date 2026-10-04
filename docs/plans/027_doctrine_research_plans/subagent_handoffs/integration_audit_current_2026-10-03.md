# Event027 current integration audit

Latest verification: the actual-recorder binder and row-specific failed-publication quarantine are corrected in current source.
The final repair verification supersedes both blockers from the earlier transaction snapshot and records no additional confirmed source defect in this bounded path.
The direct producer, History payload, cluster 9/member row, shared selectors, and four previews remain source-implemented, with MCP/runtime and AI probability evidence still unresolved.
The original source hashes and tool failures remain historical evidence for the earlier audit snapshot.

Date: 2026-10-03.
Role: read-only event completion auditor.
Disposition: partial source integration, blocked MCP completion evidence.
Acceptance basis: the parent's bounded 2026-10-03 request explicitly requires current registration, one actorless History row with an immutable batch-size payload, Event Details, four evolution catalog entries, and labels.
The Event027 specification package supplies the corresponding design requirements.
This report does not approve gameplay or mark the full event complete.

## Scope and current-source boundary

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
All 16 files in `docs\specs\027_doctrine_research_specs\` were consulted, including the acceptance criteria and implementation, achievement, asset, catalog, probability, and goal prompts.
Current `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning` guided the audit.
The improvement guidance was used to keep this an integration closure audit without adding mechanics.
The events skill supplied the separation between History, related logged evolutions, and the Event Details preview catalog.

Source inspection was restricted to the named shared files, Event027 files, exact selector consumers, default enable trigger, and Event027 documentation.
There was no full workspace scan, gameplay patch, launch, index operation, reversal of another agent's changes, staging, or commit.
The only authored file is this handoff.
Gameplay and achievement patches, final integration, and final validation remain parent-owned.

Concurrent edits occurred during the audit.
In the final inspected source, `chaosx_settings_effects.txt:4011-4014` calls `doctrine_research_prepare_random_event_fire`.
The helper at `027_doctrine_research_effects.txt:1999-2014` captures forced/debug origin only.
It does not prepare the firing size or History payload.
Earlier source observations lacking that new call are superseded by this final read.
Line numbers below identify the inspected snapshot and should be relocated by the named helper or selector after another edit.

## Completion by surface

| Surface | Status | Current file evidence |
| --- | --- | --- |
| Root identity and generic dispatch | Finished in source, runtime evidence blocked | `events\027_doctrine_research.txt:12-20` defines hidden triggered-only `chaosx.nr27.1`, calling `doctrine_research_fire_global_batch`. `common\scripted_effects\chaosx_settings_effects.txt:4459-4465` constructs `chaosx.nr[EVENT_ID].1` with `event_fire_record_id`. |
| Minor Repeatable registration | Finished in source | `common\scripted_effects\chaosx_logic_effects.txt:293` registers 27 in `global.repeatable_events`. |
| Event name and debug name | Finished in source | `localisation\english\chaosx_event_names_l_english.yml:29` defines Doctrine Research. The shared log name selectors match event 27 at lines 1389, 10707, and 12441. `common\scripted_localisation\chaosx_scripted_localisation_debug.txt:129-130` supplies the debug mapping. |
| Default enable state | Present, readiness disposition unresolved | `common\scripted_triggers\chaosx_settings_triggers.txt:25` includes 27. The spec requires full rework readiness before default enablement, while the current integration and MCP evidence are incomplete. This audit does not remove the entry. |
| Unavailable event display | Finished in source | `chaosx_logic_effects.txt:829-832` identifies no valid participant. The shared localisation at lines 13402 and 13583 maps the corresponding N/A reason. |
| One global History row | Present in source | `on_repeatable_event_fired` calls the shared recorder once at `chaosx_logic_effects.txt:1231`. No History recorder or fired-event handler was found in Event027 country-choice pages or its inspected owner effects. |
| History actor | Correct default in source | `chaosx_events_log_effects.txt:198-200` defaults actor and has-actor to zero. There is no Event027 actor branch. The dispatcher host must not become the actor of the global wave. |
| History immutable batch-size payload | Missing | `record_events_log_history_entry` initializes payload to zero at lines 685-692 and reads only an active payload override. No Event027 producer sets that override. The owner prepares the size only in the root fanout at `027_doctrine_research_effects.txt:2018`. |
| Event Details description | Missing selector wiring | `GetEventsLogEventDetailDescription`, shared localisation lines 5668-6776, has no Event027 branch and falls back to `chaosx.events_log.window.event_details.entry_placeholder.generic`. Event027's premise and History keys exist at its localisation lines 339-344. |
| Four evolution preview rows | Missing | `events_log_rebuild_open_event_details_view` clears the four aligned preview arrays at `chaosx_events_log_effects.txt:1961-1964`. Its event-specific preview section at lines 2265-2820 contains no Event027 branch. |
| Actual evolution recording | Present in source, lifecycle evidence blocked | `doctrine_research_record_new_evolutions`, owner effects lines 1960-1996, emits event ID 27, type 27, stages I-IV, and `events_log_evolution_has_actor = 0`. It does not emit country-choice evolution records. |
| Evolution labels and selected detail bodies | Missing selector wiring | All nine selectors in the mapping table below have zero Event027 branches. The owner localisation already defines the type, four titles, and four bodies at lines 338 and 345-352. |
| Documentation claims | Stale for this integration snapshot | `docs\events\027_doctrine_research\overview.md:150` claims the immutable payload exists, and line 184 claims broad log/details integration. The current shared sources contradict those claims. |
| Required event and probability evidence | Blocked | Current attempts and exact limitations are recorded below. Source inspection is not equivalent MCP or engine evidence. |

No additional event-specific dispatcher branch is needed merely to reach Event027.
The parent's finding that dispatch is generic is correct.
Do not restore a dated explicit `news_event` branch, add a second root dispatch, or record each country page as a random event.

## Owner patch instructions: History snapshot and context

The intended flow is one firing profile, one snapshot stored in the shared History payload, and one matching global fanout.
The profile helper is `doctrine_research_prepare_firing_profile` at owner effects lines 1948-1958.
It writes `global.doctrine_research_firing_stage`, `global.doctrine_research_firing_size`, and `global.doctrine_research_last_firing_size`.
The size is 1 at baseline, then the existing `constant:doctrine_research_event.evolution_i_batch_size` through `evolution_iv_batch_size`, which are 2, 3, 4, and 5.

Prepare and capture the firing profile in the dispatcher effect chain before the queued `country_event` and before its `on_repeatable_event_fired` History recorder.
The current Event027 prefire hook at `chaosx_settings_effects.txt:4011-4014` is the bounded owner integration point.
Extend its owner helper to prepare the profile and snapshot its size, preserving the existing debug-origin capture.
Do not rely on temporary variables set inside the root event surviving back into the dispatcher's effect chain.
Do not read a prior `global.doctrine_research_last_firing_size` without first preparing the current firing.

Immediately before the single shared History record, the Event027 branch must provide the following existing temporary inputs in the recorder's caller chain:

```text
events_log_history_payload_override_active = 1
events_log_history_payload_override = <this firing's captured batch size>
events_log_history_actor_override_active = 0
events_log_history_secondary_actor_override_active = 0
```

Use `set_temp_variable` for those inputs, with the payload copied from the prepared profile rather than a live stage recomputed when the UI is opened.
The generic dispatcher restores `event_id = event_fire_record_id` and calls `get_event_type` before the handler, so the owner branch must preserve that identity contract.
`record_events_log_history_entry` appends `events_log_entry_payload` to `global.events_log_history_payload_entries` at lines 720-724.
It resets the active override flags at lines 817-819, which should remain the common cleanup.
The default actor mapper already returns zero for Event027, so no country actor mapping is required.

The owner must also keep the root fanout's batch profile equal to the profile captured for this same firing.
The current root unconditionally calls `doctrine_research_prepare_firing_profile` again and clears its global scratch profile at lines 2025-2026.
If dispatch and root execution can be separated, the parent must carry and consume the per-firing profile safely, preserving independent overlapping firings.
A mutable global last-size value alone is not a per-firing delivery identity.
Do not call the fanout from the History helper, and do not add a second History row to compensate for a missing payload.
Runtime ordering and overlapping dispatch behavior remain validation requirements, not proven by this proposal.

History click routing already copies `global.events_log_view_payload_entries^events_log_history_index` into the viewer country's `events_log_history_selected_payload` at `common\scripted_guis\chaosx_scripted_gui_events_log.txt:342`.
`events_log_open_history_event_details_entry` sets `events_log_detail_use_history_context` at shared effects line 1727.
Opening ordinary catalog details clears that flag and resets selected payload to zero at lines 2834 and 2845.
No new History click path is needed for this simple numeric payload.

In `GetEventsLogEventDetailDescription`, add five History branches before the general Event027 premise branch.
Each History branch must require `event_id = constant:doctrine_research_event.id`, `has_country_flag = events_log_detail_use_history_context`, `events_log_history_selected_event_id = constant:doctrine_research_event.id`, a positive `events_log_history_selected_sequence`, and the selected payload matching the corresponding batch-size constant.
Map payloads 1-5 to `chaosx.events_log.window.event_details.doctrine_research.history.1` through `.5`.
Then map the ordinary Event027 branch to `chaosx.events_log.window.event_details.doctrine_research`.
Order matters because the general Event027 branch must not mask the specific History branches.
Rows already recorded with payload zero must retain an honest generic premise or explicit unknown-payload treatment.
Do not invent their size from the current global stage or the latest firing.

## Owner patch instructions: four evolution catalog entries

Add one `event_id = constant:doctrine_research_event.id` branch inside `events_log_rebuild_open_event_details_view`, beside the existing event-owned preview branches and before the final world-end rebuild at line 2822.
For each of the following four tuples, assign the existing temporary preview inputs and call `events_log_add_event_detail_evolution_preview = yes` once.

| Row | `events_log_event_detail_preview_type` | `events_log_event_detail_preview_tier` | `events_log_event_detail_preview_stage` | Choices described |
| --- | --- | --- | --- | ---: |
| I | `constant:doctrine_research_event.evolution_type` | `constant:doctrine_research_event.evolution_i_tier` | `constant:doctrine_research_event.evolution_i_stage` | 2 |
| II | same type constant | `constant:doctrine_research_event.evolution_ii_tier` | `constant:doctrine_research_event.evolution_ii_stage` | 3 |
| III | same type constant | `constant:doctrine_research_event.evolution_iii_tier` | `constant:doctrine_research_event.evolution_iii_stage` | 4 |
| IV | same type constant | `constant:doctrine_research_event.evolution_iv_tier` | `constant:doctrine_research_event.evolution_iv_stage` | 5 |

The existing constants declare type 27, tiers 1-4, and stages 1-4 at `common\script_constants\027_doctrine_research_constants.txt:14-26`.
The shared preview helper at lines 2913-2940 writes all four aligned arrays and computes enabled state through `has_disabled_current_evolution`.
Reuse it, including its zero-based row indexes, rather than populating one array independently or recording fake evolutions.
Do not add baseline as a fifth evolution, and do not gate catalog rows on an evolution having already fired.
Catalog rows have no History index, firing date, or actor.
The existing preview click helper at lines 2871-2883 already initializes selected evolution event/type/stage and sets actor, has-actor, date, and sequence to zero.
Generic stage formatting already covers I-IV, for example `GetEventsLogEventDetailEvolutionStageView:4401-4439`.

## Owner patch instructions: all nine shared selectors

All selectors below are in `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt`.
A bounded selector-by-selector source check found zero `doctrine_research` or exact event-27 branches in each.
The variable and index names must follow the corresponding surface.

| Selector and inspected line | Match input | Localisation output |
| --- | --- | --- |
| `GetEventsLogEvolutionTypeView:868` | `global.events_log_evolution_view_type_entries^events_log_evolution_index` | Type key |
| `GetEventsLogEvolutionNameView:2122` | Same view type, plus `global.events_log_evolution_view_stage_entries^events_log_evolution_index` | Four stage title keys |
| `GetEventsLogSelectedHistoryEvolutionTypeView:3027` | `global.events_log_history_detail_evolution_type_entries^events_log_history_detail_evolution_index` | Type key |
| `GetEventsLogSelectedHistoryEvolutionNameView:3257` | Same related-history type, plus `global.events_log_history_detail_evolution_stage_entries^events_log_history_detail_evolution_index` | Four stage title keys |
| `GetEventsLogEventDetailEvolutionTypeView:4150` | `global.events_log_event_detail_evolution_type_entries^events_log_event_detail_evolution_index` | Type key |
| `GetEventsLogEventDetailDescription:5668` | `event_id`, History flag, selected event ID/sequence/payload as described above | Premise or five immutable History size keys |
| `GetEventsLogEventDetailEvolutionTitle:6828` | Same catalog type, plus `global.events_log_event_detail_evolution_stage_entries^events_log_event_detail_evolution_index` | Four stage title keys |
| `GetEventsLogSelectedEvolutionTitle:7624` | `events_log_selected_evolution_type`, `events_log_selected_evolution_stage` | Four stage title keys |
| `GetEventsLogSelectedEvolutionBody:8420` | Same selected type and selected stage | Four stage body keys |

For evolution type comparisons, use `constant:doctrine_research_event.evolution_type`.
For stage comparisons, use the four existing `constant:doctrine_research_event.evolution_*_stage` constants.
The type key is `chaosx.events_log.evolution.type.doctrine_research`.
The four title keys are `chaosx.events_log.window.evolution_details.doctrine_research.title.stage_1` through `.stage_4`.
The body keys use the corresponding `.body.stage_1` through `.stage_4` suffixes.
Place these branches before their unconditional generic/unknown fallback.
Existing owner keys at localisation lines 338-352 provide the complete text set, so the missing work is selectors and preview data rather than absent English keys.
`chaosx_gui_l_english.yml:634`, `:638`, and `:751` consume the description, catalog title, and selected title selectors respectively.

## Accepted-plan disposition and documentation gaps

The source specs require the one global actorless row, four previews, no country-choice history, and accurate labels in `027_doctrine_research_spec_part_1_core.md`, Part 4's History/Event Details sections, the coding prompt's Event Logs section, and the acceptance criteria's Event Logs and Event Details section.
Those integration requirements remain partially implemented.
The current parent request is an explicit acceptance basis for completing this bounded wiring.
The missing pieces must remain unresolved implementation work until the owner patch and required evidence exist.

`docs\events\027_doctrine_research\overview.md:150` must be reconciled with the missing payload producer.
Its line 184 and `docs\plans\027_doctrine_research_plans\review_closure_refresh_2026-09-04.md:7` overstate current Event Details/log integration.
The latter's conclusion that remaining blockers are only evidence is stale for this source snapshot, which contains actual missing wiring.
`documentation_state.md` is dated September 4 and is provenance rather than current integration proof.
This handoff supplies current source findings without editing or promoting those documents.

The original specification's improvement closure remains a design recommendation to finish the existing doctrine flow.
This audit proposes no expansion addendum, country package, focus tree, decision category, custom window, animation, super-event, portrait, or 3D asset.
The shared Event Details framework is not an Event027-owned UI, so `chaosx_event_ui_worker` is not a completion requirement for this bounded shared-selector repair.
No Event027 visual-production audit was performed here, and dated asset audits are not being promoted into current proof.
The owner may reuse the already defined text keys without a new art handoff.

The workbook was outside this urgent sidecar scope and was not opened or changed.
After owner integration, the parent should align the authoritative `docs\spreadsheets\chaos_redux_events_catalog.xlsx` detail/evolution text with final in-game wording through the spreadsheet owner and regenerate exports if the workbook changes.
The spec catalog handoff's historical status suggestions do not override current `AGENTS.md` catalog vocabulary and approval requirements.

The 2026-10-03 `parent_queue_correction` and `parent_native_repairs` handoffs document owner-applied gameplay changes with validation pending.
They were read as current boundary evidence and are not substitutes for this shared integration review.
Their native mastery and receipt findings remain outside this audit's patch recommendations.

## Task-specific validation and MCP limits

Performed source checks: root-to-generic-dispatch crosswalk, repeatable handler-to-single-recorder flow, absence of country-choice History calls, no-actor default mapping, firing-size producer/consumer tracing, History click payload/context tracing, preview helper/array/click crosswalk, all nine selector coverage checks, existing localisation-key coverage, and stale documentation comparison.
No probability estimate, engine timing verdict, in-game outcome, visual acceptance, or passing source comparison is inferred from those checks.

The connected tools were exposed in this auditor's tool list even though the parent's earlier app list omitted them.
The connected `source_lookup` schema accepts `includeReferences`, `maxDefinitions`, `maxReferences`, and `maxLines`, with no `view`/`keyPath`.
The single connected narrow request used symbol `chaosx.nr27.1`, `includeReferences=false`, `maxDefinitions=1`, `maxReferences=0`, and `maxLines=20`.
It returned `tool call failed` with `timed out awaiting tools/call after 600s` and no source result.

A first direct production stdio connection failed initialization with MCP `-32001: Request timed out` at 10,000 ms, with empty stderr.
The bounded 60,000 ms direct connection subsequently initialized successfully and reported live server `hoi4-agent-tools` version `3.6.0`.
Its live `tools/list` verified the legacy `source_lookup` schema and `execution.taskSupport = forbidden` for that route.
The parent-requested narrow production source lookup used the same arguments above and failed at 60,000 ms with MCP `-32001: Request timed out`, with empty stderr.
There was no successful source revision, continuation URI, or artifact from either lookup.

Production stdio executable: `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\bin\stdio.js`.
Client: the package's `node_modules\@modelcontextprotocol\sdk\dist\esm\client` implementation.
No helper-expansion, task, or job route was assumed from package metadata, and no `script_validate` result is claimed.
The parent's live-engine version `1.19.2` and fixed index rejection `f9978e9` are supplied context, not facts revalidated by this audit.
No index recommendation follows from these timeouts.

Current event inspect/render/compare attempts and the specialized probability route are recorded in the final evidence addendum below.
The September revision is used only as historical comparison input, never as current validation.
Required source and visual evidence remain blocked unless an actual route result resolves them.

## Local reference evidence

| Source | Read lines | SHA-256 revision | Rule |
| --- | --- | --- | --- |
| Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2943-2966, 7820-7840 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Country event scope/delay fields, and copying a normal variable into a temporary variable. |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 180-214 | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` | Hidden/triggered events, immediate blocks, and event firing arguments. |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 435-446 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Temporary values are unscoped and do not carry into a separately fired event. |

These sections were read locally after the MCP route gaps.
The installed documentation does not establish the exact queued root/handler timing or the owner's final per-firing bridge.
Those are still task-specific validation limits.

## Inspected source identities

| File, relative to workspace | SHA-256 at final source inspection |
| --- | --- |
| `common\scripted_effects\chaosx_settings_effects.txt` | `2bd05e61083f9563a8881eb118387ad84b15ffdb11a2f345ffef2a01c8b4f978` |
| `common\scripted_effects\chaosx_logic_effects.txt` | `433362223952ae687fa98f87176167d7931b7eb4d930236eab3a8a4247a4c644` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `debac43a3bb604526ee2c4bb3c8de5806dfc8c4f40fef97bb3948b5ff780fcc9` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `a185e11c2587fc6ca1150d62a1e90a952231c70969dc86ca45aa628e900d928f` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `4a6ad8aec0733be61251735ab94e941e11cf9a7f5ad3941168957a95a752826a` |
| `common\script_constants\027_doctrine_research_constants.txt` | `d24ba6d1c77f76880be4297f01cd848859466ac806643b29b41561376861d87a` |
| `localisation\english\027_doctrine_research_l_english.yml` | `0dfb4b32c313f23fb629e87828a7d028681a8f737b7ae45e6ccc6e21653ff5cf` |

## Remaining blockers and bounded next actions

1. Parent wires the current-firing History size snapshot, its safe fanout profile consumption, and the six description branches.
2. Parent adds four aligned preview rows and the eight evolution label/title/body selectors listed above.
3. Parent reconciles the exact stale documentation claims and retains the default-enable readiness question as an explicit disposition.
4. Owner validation must cover payloads 1-5, an earlier one-choice row opened after a later five-choice firing, ordinary catalog details with no History context, zero-payload historical rows, four previews before any firing, independent evolution toggles, no actor flags, one global row, and no extra rows after country choices.
5. For actual evolved History rows, exercise both the main Evolutions list and the selected History related-evolution list, then click their selected title/body details.
6. Obtain current event inspect/render and real baseline comparison evidence, with helper/lifecycle coverage limits retained, and complete the specialized weighted registration audit.

The source gaps are implementation omissions, not asset-production or broad design gaps.
The missing MCP outputs are validation blockers.
No simplification or fallback was implemented by this auditor, and none of the missing requirements is declared complete.

## Final event MCP evidence addendum

The production direct client initialized successfully as v3.6.0 and read the live schemas for all three event routes before calling them.
All domain requests were read-only, selected only `chaosx.nr27.1`, and used `refresh=false`.
The connected and direct requests used matching event arguments.

| Route | Request bounds/input | Connected outcome | Production stdio outcome |
| --- | --- | --- | --- |
| `hoi4.event_inspect` | `mode=trace`, selector `{kind:event,eventId:chaosx.nr27.1}`, downstream, `expandHelpers=false`, depth 3, nodes 30, edges 40 | `timed out awaiting tools/call after 600s` | MCP `-32001: Request timed out` at 30,000 ms |
| `hoi4.event_render` | `view=overview`, same selector/direction/depth/nodes, `expandHelpers=false`, `includeHtml=false` | `timed out awaiting tools/call after 600s` | MCP `-32001: Request timed out` at 30,000 ms |
| `hoi4.event_compare` | Same selector, `before.revision=57d351df319dd5e7cdd1aa154584e6ac6e4bde5f1e6d0689ede14544ce2eb4cc`, `render=false`, chain/render nodes 30 | `timed out awaiting tools/call after 600s` | MCP `-32001: Request timed out` at 30,000 ms |

The comparison revision was taken from the existing September closure addendum as historical input.
No current cached revision, valid graph artifact, comparison delta, rendered image, unresolved-coverage inventory, or continuation URI was returned.
No cached-revision rejection is inferred from these timeouts.
Even a successful focused trace would not establish full helper/lifecycle coverage under the event skill's analysis-boundary contract.
The actual required engine and visual evidence remains blocked.

The seven source hashes above were rechecked after report drafting and remained identical.
The final bounded search still found no Event027 shared description/evolution selectors or preview rows, and no Event027 History payload override producer.

## Specialized probability handoff limit

The weighted registration pass was routed to `chaosx_ai_probability_auditor` with `fork_context=false` and an explicit read-only prompt restricted to Event027 shared registration/availability and any probabilistic evolution pacing.
The spawned agent ID was `01a10125-e634-7cc0-a7ab-91cf959a5248`.
It was instructed to start with `hoi4.probability_inspect`, return findings inline, avoid broad doctrine AI review, and perform no file writes or index work.
No completed handoff or probability result was delivered during the bounded sidecar audit.
Repeated status waits returned no final status, and closing the child reported its previous status as `running`, followed by a shutdown notification.
This is an unresolved specialized-audit delivery limit, not proof of an orchestration failure or a probability-tool timeout.
No inspect, evaluation, normalization, comparison, or probability artifact from that child is claimed.
The parent still needs the specialized registration probability evidence before claiming weighted-surface completion.
This audit has not patched a weight or changed a weighted candidate pool.

## Cluster follow-up and applied selector review

Acceptance basis: the parent's follow-up confirms that National Breakthroughs is missing, reserves registry implementation to the parent after checking workbook ID 9, and authorizes a bounded Event027-only runtime member row.
Future accepted members 54, 65, 67, 83, 85, and 89 remain absent from the runtime loader until their own reworks are implemented.
This is `accepted and queued` integration work pending the parent's workbook check and source patch.
No full post-cluster integration audit is claimed before that patch exists.

Confirmed omission: `common\script_constants\event_cluster_constants.txt:9-26` declares IDs 1-8, 11, and 12, with no 9 or `national_breakthroughs`.
`initialize_event_cluster_definitions:205-296` and `load_event_cluster_members:1135-1400` in `common\scripted_effects\chaosx_event_cluster_effects.txt` have no National Breakthroughs or Event027 row.
The owner constants `doctrine_research_event.cluster_id = 9` and `cluster_member_row_id = 9001` at `027_doctrine_research_constants.txt:25-26` do not register a cluster.
Existing English name and description keys likewise do not prove runtime wiring.

The current overview's cluster claims at lines 52, 73, 84, 210, and 244 are stale against this inspected registry.
Its workbook cluster claim at line 226 is not a substitute for a runtime registry.
The parent owns reconciling these claims after its patch and recording the partial member coverage honestly.

### Exact parent-owned cluster hooks

| Hook | Required bounded integration |
| --- | --- |
| `event_cluster_id`, constants lines 9-26 | Add `national_breakthroughs` only after the parent's workbook ID audit. Keep it consistent with the existing Event027 cluster constant 9. |
| `initialize_event_cluster_definitions`, effects line 205 | Append aligned entries to `global.event_clusters`, `global.event_cluster_type_entries`, and `global.event_cluster_unlock_tier_entries`. The type is `constant:event_cluster_type.repeatable`, and the accepted minimum is Calm World, `constant:chaos_meter_tier_id.tier_0`. |
| `initialize_event_cluster_system`, effects line 16 | Its definitions bootstrap runs only when the registry is absent at lines 20-26. Preserve that behavior. If the parent supports adding the definition to an already initialized registry, use a guarded aligned append like the existing append at lines 113-120, then retain `event_cluster_ensure_probability_state` at line 125. Do not clear history or rebuild existing probability identities. |
| `load_event_cluster_members`, effects line 1135 | Add one National Breakthroughs branch with exactly one Event027 logical member row, using the inputs below and `event_cluster_append_member_definition`. |
| `event_cluster_append_member_definition`, effects line 1118 | Reuse its eight aligned output arrays. Do not manually append only the event ID or an obsolete five-column member shape. |
| `event_get_cluster_candidates_for_event`, effects line 400, and `event_belongs_to_cluster`, line 447 | These already derive membership from the registry and loader. No explicit Event027 mapping branch is needed. Automatic selection uses the full candidate arrays, and the compatibility lookup returns their first entry. |
| `event_cluster_resolve_trigger_member_row`, effects line 1402 | The primary-trigger marker is required for automatic selection to recognize Event027 as the originating member. Preserve its stable row identity so the selected row is guaranteed once. |
| `fire_event_cluster_member_by_temp_id`, effects line 2672 | Its generic branch already sets `event_cluster_member_fire_context` and calls `fire_event_by_temp_id_no_cluster` at line 2730. Reuse it. Do not call `doctrine_research_fire_global_batch` directly from cluster setup. |
| `event_cluster_prepare_runtime_context`, effects line 3492 | The default readiness and generic pending-context initialization are sufficient for the global Event027 root. No country actor or extra fanout setup is needed merely to register this row. |
| `try_fire_event_cluster_for_selected_event`, effects line 4237 | The generic path consumes primary matching rows and the cluster candidates. No second Event027 dispatch branch is required. |
| Optional owner-defined cluster cooldown | If the parent selects a cluster cooldown, keep its constant and matching writes/reads synchronized in `mark_event_cluster_fired_state:3235`, `event_cluster_check_cluster_gates:1735`, and `evaluate_event_cluster_unavailability_reason:2048`. This auditor chooses no cooldown value or new probability target. |

The member loader inputs are exactly:

```text
event_cluster_member_event_id = constant:doctrine_research_event.id
event_cluster_member_role = constant:event_cluster_member_role.optional
event_cluster_member_min_tier = constant:chaos_meter_tier_id.tier_0
event_cluster_member_severity = constant:event_cluster_member_danger.medium
event_cluster_member_row_id = constant:doctrine_research_event.cluster_member_row_id
event_cluster_member_primary_trigger = constant:event_cluster_member_primary_trigger.yes
```

Assign these with `set_temp_variable` and call `event_cluster_append_member_definition = yes` once.
The helper supplies `temp_event_cluster_member_event_id_entries`, `role_entries`, `chance_entries`, `min_tier_entries`, `danger_entries`, `row_id_entries`, `primary_trigger_entries`, and `severity_entries` under the shared `temp_event_cluster_member_` prefix.
The row remains optional when another implemented member eventually originates the cluster, while the generic selected-trigger path guarantees it when Event027 originates the cluster.
No placeholder rows for unreworked future members should enter the current runtime pool.
The one-member implementation must retain one cluster pacing update and one Event027 fanout, cap update, and actorless History row.

### Six missing cluster text mappings

The keys already exist in `localisation\english\chaosx_gui_l_english.yml`: `chaosx.event_cluster.national_breakthroughs.name` at line 901 and `chaosx.events_log.window.cluster_details.description.national_breakthroughs` at line 428.
The following selectors currently have no National Breakthroughs branch.
Match the new shared cluster constant in each appropriate context and return the existing name key, or the description key for the last description selector.

| File and selector | Context variable |
| --- | --- |
| Shared Event Log localisation, `GetEventsLogDetailClusterName:530` | `global.events_log_open_event_detail_cluster_id_entries^events_log_open_event_detail_index` |
| Shared Event Log localisation, `GetEventsLogHistoryClusterName:11634` | `global.events_log_view_cluster_id_entries^events_log_history_index` |
| Shared Event Log localisation, `GetEventsLogClusterNameView:11774` | `global.events_log_cluster_view_id_entries^events_log_cluster_index` |
| Shared Event Log localisation, `GetEventsLogSelectedClusterName:11876` | `events_log_selected_cluster_id` |
| Shared Event Log localisation, `GetEventsLogSelectedClusterDescription:12054` | `events_log_selected_cluster_id` |
| `common\scripted_localisation\chaosx_scripted_localisation_settings.txt`, `GetSettingsClusterName:409` | `settings_selected_cluster_id` |

Other cluster status, roll, count, and tooltip helpers use generic fallback behavior or special-case Random Stuff rather than an exhaustive per-cluster name registry.
Their lack of a National Breakthroughs-specific branch alone is not an omission.
The subsequent full integration check should inspect their actual outputs after the registry row exists.

### Selector and preview patch disposition

The earlier nine selector omissions are superseded by the owner-applied patch.
The source review found one Event027 type branch in each of the three type selectors, four title branches in each of the four title/name selectors, four selected body branches, and the five History payload branches followed by the Event027 premise in `GetEventsLogEventDetailDescription:5727-5778`.
The History branches require the History flag, matching selected event ID, positive selected sequence, and payload 1-5 before the general premise branch.
`chaosx_events_log_effects.txt:2822-2837` now adds exactly four previews through the shared helper, with matching type, tier, and stage constants.
These are implemented source dispositions with MCP rendering and comparison still blocked.

The History payload producer remains missing in this follow-up snapshot.
No `events_log_history_payload_override` producer was found in the current Event027 effects, shared logic effects, or settings effects.
The six description branches therefore do not establish immutable firing-size history until the parent wires the producer.

No long MCP request was repeated, per the parent's instruction.
The prior exact event/source timeouts and specialized probability delivery limit remain evidence blockers.
A new weighted cluster pool will still require its specialized probability audit and comparison when that route can produce evidence.
This source hook review provides no probability verdict and chooses no balance targets.

Follow-up SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| `common\script_constants\event_cluster_constants.txt` | `e74a71fa4612452f80dfb651d762b39eb5ad6dd7eb41a3d08fa1fa5e741d349f` |
| `common\scripted_effects\chaosx_event_cluster_effects.txt` | `d8211da66bb429a5c00d2c51eefdc462d36d8a210bde1bc3df2d66f8dc25bdc2` |
| `common\scripted_localisation\chaosx_scripted_localisation_settings.txt` | `0288d09f3a7854ae124356d6733a2949ace42de400289f480869c353e8e765e0` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `5f9f99be4aa88dfddb17eb1f7a171dfbf6d49283ca51a2ee54b60940d2a770ce` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `641a78580e2291c97c0f45ff8efc0397e26812cad39a25c9a6b759bf34dcdb8a` |

Parent-owned registry implementation and the full subsequent integration review remain pending.
Only this handoff was changed by the auditor.

## Current transaction and cluster integration review

Acceptance basis: the parent requested a read-only review of the direct Event027 transaction, captured recipients, immutable firing envelopes, one shared handler, actual History binding, hidden recipient wake, firing-ID migration/cleanup, and the bounded cluster 9 row.
This section records the current source, rather than relying on September implementation claims.
Disposition: substantially implemented source integration with two concrete source blockers and the existing unresolved MCP/runtime evidence.
The auditor made no gameplay, registry, localisation, workbook, or asset changes.

### Current blockers

**B1. The binder call is in the system recorder, not the recorder reached by this producer.**

`common\scripted_effects\chaosx_events_log_effects.txt:536-626` defines `record_events_log_system_history_entry`.
The new guarded call to `doctrine_research_bind_firing_history` is inside that function at lines 619-622.
The actual transaction calls `on_repeatable_event_fired` from `027_doctrine_research_effects.txt:2062`.
That handler calls `record_events_log_history_entry` at `chaosx_logic_effects.txt:1241`.
The latter recorder begins at shared log effects line 681 and has no Event027 binder call before its override cleanup at lines 821-823.

Consequently, the normal path records the correct numeric size payload and actorless row, but does not bind the envelope's History sequence, mark it released, consume its one-shot firing context, or schedule `.14` wakes through the intended binder.
The envelope remains `batches_committed` with History sequence zero on this path.
Later lifecycle reconciliation can independently start queued work, so the missing wake must not be described as proof that every batch remains permanently dormant.

Bounded owner correction: put the guarded binder call inside `record_events_log_history_entry`, after the complete row has been appended and before override cleanup and downstream view refreshes.
This preserves the real `global.events_log_history_sequence` and executes before `random_stuff_cluster_try_after_minor_event` in the shared handler.
Remove or explicitly justify the system-recorder copy so an unrelated later system row cannot consume a surviving Event027 context.
Keep one shared History row and one shared fired handler.
Do not compensate by recording another owner History row or firing `.14` from a country choice page.

**B2. Blocked publication does not prevent partial country rows from activating, and Settings still declares dispatch success.**

The recipient snapshot at owner effects lines 2041-2044 uses `doctrine_research_country_has_valid_action`.
That trigger at `027_doctrine_research_triggers.txt:1371-1383` checks live country and doctrine availability, but does not reject an existing `doctrine_research_state_corrupt` flag.
The append helper at owner effects lines 2108-2140 initializes the ledger and appends only if the country is live and not corrupt.
If any captured recipient rejects publication, the count comparison fails, and lines 2066-2069 mark the envelope blocked without calling the shared handler.
Rows already appended for other recipients remain in `queued` status.

`doctrine_research_start_next_batch:2143-2181` selects the first queued country row at lines 2151-2153 without reading `doctrine_research_batch_firing_ids` or checking the matching envelope status.
`doctrine_research_reconcile_country_lifecycle:2691-2719` reaches this starter at line 2717.
The event-owned on-actions call reconciliation for state-control, government, subject, and other lifecycle transitions.
Thus a valid country's partial row from a blocked firing can reach AI resolution or the human opening later, even though that firing was never released and received no shared History/pacing commit.

The direct Settings branch at `chaosx_settings_effects.txt:4340-4344` also sets `event_fire_dispatched = 1` unconditionally after the producer returns.
For the publication-failure path, this is a false success receipt that cluster dispatch can treat as fired.

Source-derived counterexample: country A has a valid ledger and doctrine action, while country B has a valid doctrine action and a corrupt ledger.
Both enter the recipient snapshot, only A appends, the envelope becomes blocked, and A's later lifecycle reconciliation can start its queued row.
This counterexample is derived from the source branches and has not been executed in the game or MCP.

Bounded owner correction: enforce the release contract for new nonzero firing IDs at every queue activation route, or quarantine the exact newly published rows when publication fails.
Keep migrated firing ID zero explicitly unknown rather than fabricating a released envelope for legacy rows.
Make the dispatch success receipt reflect publication/commit failure while preserving the rule that the producer performs no owner work after the shared handler returns.
The parent owns the exact repair and failure disposition.

### Source requirements that are implemented

| Surface | Current source finding |
| --- | --- |
| Settings dispatch | `chaosx_settings_effects.txt:4340-4346` calls the producer directly for 27. The generic enqueue and generic fired handlers are inside the sibling `else`, so this branch does not enqueue `.1` or invoke a second shared handler. |
| Root and wake IDs | The event file contains 32 unique Event027 definitions, including exactly one hidden triggered-only `.14` at lines 25-30. `.1` is the console bridge and marks forced achievement setup before calling the producer. |
| Participant snapshot | The producer has one `every_country` eligibility snapshot at lines 2041-2044. It then iterates that captured temporary scope array to append rows. No AI resolver or human page is invoked by the capture or append helper. |
| Immutable envelopes | Lines 2030-2037 append separate ID, stage, size, date, History-sequence, and status columns. Country rows at lines 2114-2120 copy the matching firing ID and envelope values, rather than recalculating the live stage. |
| History payload and actor | The producer sets the existing payload override from the captured envelope size at lines 2057-2058 and clears actor/secondary-actor override activation at lines 2059-2060. The actual shared recorder consumes that payload at lines 692-696 and appends it at lines 724-728. Its default actor mapper starts with actor/has-actor zero and has no Event027 actor branch. |
| One ordinary pacing/History commit | The committed producer has one `on_repeatable_event_fired` call at line 2062. The handler has one normal pacing path and one History recorder call. In cluster member context it skips individual global pacing, leaving the shared cluster pacing update authoritative. |
| Producer boundary after handler | There is no further Event027 producer operation on the successful branch after the shared handler. The blocked branch is the alternative branch, not post-handler cleanup. This preserves the intended boundary around a nested Random Stuff firing. |
| Binder body | When reached with the correct context, lines 2076-2098 verify firing ID/index and `batches_committed`, bind the real sequence, mark released, consume the temporary ID/index, coalesce wakes through `doctrine_research_batch_wake_scheduled`, and schedule `.14`. B1 is the missing call-path integration, not an absent binder definition. |
| Country-local wake | `.14` calls `doctrine_research_wake_country_batches`. That helper clears only its country wake flag and starts work only for a live country without an active batch. It adds no History or pacing call. |
| Firing-ID ledger | Country initialization clears the new column at line 221. Migration at lines 320-327 appends unknown zero for missing legacy positions without overwriting existing IDs. The alignment trigger at line 1440 checks its length against batch IDs. Annexation clears the column and wake flag at lines 2838-2841. |
| No additional country History rows | No History recorder or fired-handler call was found in `events\027_doctrine_research.txt`. The inspected owner effects contain only the producer's shared handler call. The wake, append, navigation, and country batch completion paths do not add random-event History rows. |
| Event Details and evolutions | The nine previously reviewed shared selectors and four preview rows remain wired. The five History size branches require selected-row History context and precede the ordinary premise branch. No fake preview History date/index or country actor was added. |

These are source findings, not observed engine behavior or passing visual evidence.
B1 prevents declaring the complete History-to-wake transaction wired, and B2 prevents declaring its failure path safe.

### Cluster registration and narrow tier exception

Cluster ID 9 now exists as `event_cluster_id.national_breakthroughs` at shared constants line 23.
Its tuning block at lines 285-288 declares unlock tier zero.
The registry appends its ID, repeatable type, and unlock tier at `chaosx_event_cluster_effects.txt:278-280`.
The loader branch at lines 1393-1404 contains exactly one member: Event027, optional role, Medium severity, declared tier zero, primary trigger yes, and stable row 9001 through the owner constant.
The other accepted rough members remain absent from this branch, consistent with the parent's explicit partial implementation scope.

The generic Medium severity floor remains one at `event_cluster_constants.txt:166`.
`event_cluster_get_member_effective_min_tier:729-752` computes the generic maximum, then overrides only the simultaneous cluster 9 / event 27 / row 9001 match to tier zero at lines 744-750.
Other Medium rows retain their ordinary floor.
This is a narrow eligibility exception, not a reclassification of the row to Low.
It changes the weighted eligible pool, so the required specialized probability baseline/comparison remains unresolved under the already recorded route limitations.

All six previously missing cluster text mappings now exist: five shared Event Log mappings and `GetSettingsClusterName`, returning the existing National Breakthroughs name and description keys.
The generic candidate/member dispatch remains sufficient, and the Event027 direct branch is reached through that same shared member dispatcher.
No extra owner fanout or placeholder future member was introduced.

### Validation and documentation disposition

Performed: current direct-dispatch branch inspection, producer/append/binder/wake call-path crosswalk, actual recorder and shared handler inspection, 32-ID uniqueness/count check, country History-call check, firing-ID migration/alignment/annex cleanup crosswalk, one-row cluster inspection, exact three-key tier exception review, and all six cluster name/description mappings.
The failed-publication counterexample was traced through current lifecycle and queue-selection source.
No gameplay file was changed, and no engine model, probability normalization, live save, visual render, or source comparison result is claimed.
No long MCP request was repeated, as instructed by the parent.
The previously recorded event/source route timeouts and missing specialized probability evidence remain blockers.

The earlier missing History payload producer and missing cluster registry/member findings are superseded by current implementation.
The actorless numeric History row is now source-wired, while the envelope-sequence/wake binding and failed-publication handling remain incomplete.
`docs\events\027_doctrine_research\overview.md:75-90` still describes the prior root/fanout arrangement and temporary working profile.
The parent should align it with direct normal dispatch, console-only root behavior, immutable envelopes, the hidden local wake, and the two current limits.
The dated statement of 31 nodes in its historical MCP result at line 57 is old artifact coverage, not current source inventory, and should remain clearly historical rather than being presented as 32-node validation.
No asset or workbook evidence was promoted by this review.

### Source identities for this review

| File | SHA-256 |
| --- | --- |
| `events\027_doctrine_research.txt` | `777149623bf633fc07c04cf4f7f747a208024d2afee00d6e7120ae4bf9e01751` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `794ce5ae417b98807a3c8b7c35aac578c6c6e98b42398aeb341783807f7898d4` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt` | `9941284e3c4acf3549bc3e87972e6ad2e6e103289f927868776e8327f725fdf4` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `12090796f3234663ead13ad3b755db683947440c37592a910239115529c59a29` |
| `common\scripted_effects\chaosx_logic_effects.txt` | `c28ee6eab4a2ceea866c81cffd6488e04a0b9d9ed509f650cfddcc3f49b7548e` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `f8c48d9f273e5757a199cb7b23f42a935851b125a46e024934354abbed129d6b` |
| `common\script_constants\027_doctrine_research_constants.txt` | `a7b5af2152b80855571c18a3607916a6068f71924593604e4a5dedae809e8724` |
| `common\script_constants\event_cluster_constants.txt` | `c76988b9618e0d2eddbdda275ddf8a910613129061dca335eeecb59c457625f7` |
| `common\scripted_effects\chaosx_event_cluster_effects.txt` | `589d0af4e736b62c234b438fca3922893e48d3c520f3e93acb4c6fb3c895ef41` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `3c8bb0871e65be9a4d484d22b83d71541225b1a8925a21877031e435f58b6733` |
| `common\scripted_localisation\chaosx_scripted_localisation_settings.txt` | `320dec0cef72f51d6863d3a2cc2fa40a29cb27ea19f5714ac7c9651ef7ba1c31` |

Required next owner actions: correct the actual-recorder binder placement, make blocked publication rows and dispatch receipts safe, then review matching-size History linkage, overlapping independent firings, nested Random Stuff entry, coalesced `.14` wake delivery, and cluster one-pacing/one-fanout behavior with appropriate evidence.
There is no completion claim for the full event or its engine behavior.

## Achievement controller-edge contract review

Scope: the parent's source-only question about a human-started country batch that AI subsequently resolves, then a human later controls again.
Disposition: no accepted requirement was found for `HumanExecuted` per receipt or permanent disqualification on losing human control.
Do not classify the absence of that field as a confirmed implementation defect or add a new ban as an automatic fix.
This conclusion is limited to the written Event027 contract, not a runtime unlock verdict.

### Explicit design evidence

| Source | Lines | Explicit criterion |
| --- | --- | --- |
| `027_doctrine_research_spec_part_4_presentation_assets_achievements.md` | 221, 265, 312 | Every achievement requires the country to be human-controlled when the batch begins. The condition is not stated per choice or per receipt. |
| `027_doctrine_research_achievement_prompt.md` | 41, 72, 111 | Repeats the same human-at-batch-beginning condition for all three achievements. |
| Part 4, First Lesson | 228-230, 247 | The later mastery step must be Event027-attributed, in the same domain and batch. |
| Part 4, Single School | 272-284, 294 | Requires five same-branch Event027 mastery receipts and completion. Excludes external/native/debug progress, other targets, adoption, premature completion, and unused choices. It does not exclude AI-executed Event027 receipts. |
| Part 4, Joint Curriculum | 318-330, 340 | Requires four distinct tracks with Event027-attributed mastery in the same batch. Excludes other mastery sources, annexation, insufficient distinct tracks, and project save disqualification. |
| `027_doctrine_research_acceptance_criteria.md` | 220-224 | Requires the specific receipt patterns and excludes native, sharing, focus, decision, other-event, and debug progress. AI execution of the country's own Event027 receipt is not listed as an excluded source. |
| `027_doctrine_research_spec_part_1_core.md` | 228-230 | Controller changes preserve the country's batch, and AI resolves remaining choices through the same valid pool. Tag switching must not move another country's choices into the current player tag. |
| `027_doctrine_research_spec_part_2_choice_flow.md` | 391-393 | Human departure preserves the country batch and routes it to its current controller, including bounded AI resolution. |
| Achievement prompt, shared safety | 139-148, 152-161 | The required provenance fields cover batch/action/domain/doctrine/track/branch and Event027 attribution. The prohibited tag-switch case is one country's receipt being applied to another, not AI completing the original country's work. |

The literal written criteria support counting a valid same-country, same-batch Event027 receipt even when AI performed that event action after a human-started batch.
This is an interpretation of the explicit eligibility and attribution rules, not a separate quoted design decision about retrospective awards.
There is no explicit sentence promising automatic achievement reevaluation when a human returns, and that award-timing edge remains unspecified.
Neither that timing omission nor the stronger player-intent wording around Single School establishes a mandatory per-receipt human-execution flag.
Normal debug/forced-route, annexation, and project achievement disqualifiers still apply independently.

### Current source behavior

`doctrine_research_achievement_campaign_is_valid` at `common\scripted_triggers\027_doctrine_research_triggers.txt:188-196` requires current `is_ai = no`, valid aligned country state, and no forced/debug/CXT disqualification.
The three trackers scan retained country batch rows and require `doctrine_research_batch_human_started` at achievement-effects lines 25, 96, and 185.
They then check country-owned receipt identity, `choice_consumed`, action type, and the achievement-specific domain/branch/track conditions.
`doctrine_research_prepare_receipt`, runtime effects lines 2238-2259, records no controller-at-execution column.
Thus a later eligible achievement scan can consider AI-executed receipts from the same human-started country batch.
The review does not prove that returning human control alone immediately schedules such a scan.

The comment at achievement-effects lines 4-7 says AI transactions cannot satisfy an achievement **unless** the receipt ledger proves that the event choice performed the required work.
It is a provenance condition, not an unconditional AI-execution exclusion.
The current receipt checks express that provenance condition.

Parent disposition: retain the existing attribution rule unless a new accepted design decision explicitly requires human execution of each counted action or disqualifies controller departure.
Such a restriction would strengthen the achievement contract and require its own acceptance basis, receipt tracking semantics, and treatment of resumed or existing rows.
It should not be inferred from the conditional comment or implemented by guessing.
No gameplay or specification was changed by this review.

Source identities: achievement effects `809edbf5df1bc4cbeb7e0af8b908baca994678dab72a503149acdc4c1d0ba2fe`, runtime effects `794ce5ae417b98807a3c8b7c35aac578c6c6e98b42398aeb341783807f7898d4`, and triggers `9941284e3c4acf3549bc3e87972e6ad2e6e103289f927868776e8327f725fdf4`.
Spec Part 4 revision is `97ee91f8b30ffb0988fb1d969fdb4505083ef178c4d402d7076167f6668edd68`, the achievement prompt is `6d74f5cd92c27ce6bab15a869b959c777a78e27e915055d07e60f48b644bd70e`, and the acceptance criteria are `f72db5ab8d265128f7815e8ff2ef811244e77fbd09f879ba326fb515c29cc181`.

## Current repair verification and accepted controller policy

Acceptance basis: the parent explicitly accepted human-at-batch-start plus country-owned Event027 receipt attribution, rejected a new `HumanExecuted` field or tag-departure ban, and defined failed publication as one actorless payload-zero attempt with no wakes.
The current source was reread against those instructions.
No additional confirmed source defect was identified in the bounded dispatch, publication, quarantine, binding, or wake path.
This is not full event, engine, AI, probability, or presentation completion.

The prior B1 and B2 findings are superseded for this new source snapshot:

- The only `doctrine_research_bind_firing_history` call is at `chaosx_events_log_effects.txt:819`, inside `record_events_log_history_entry`, which starts at line 677.
There is no binder call in the system recorder, which starts at line 536.
The binding occurs after the actual History row and before override cleanup, view refreshes, and the handler's Random Stuff callback.
- Failed publication at owner effects lines 2066-2094 sets the envelope blocked, then visits the captured countries.
It checks aligned state and a nonempty batch ledger, selects only the last row, and quarantines it only when its firing ID equals the current envelope ID at lines 2074-2079.
An older queued or active row with another firing ID does not match and is not changed.
The partial rows are no longer eligible for the starter's queued-only selection.
- The failure path clears captured recipients before calling the shared handler, supplies payload zero and inactive actor overrides, and ends with that one handler call.
The blocked branch of the binder at lines 2122-2130 binds the real sequence and consumes the one-shot context while leaving the envelope blocked.
It schedules no wake.
- Under the parent's accepted attempted-firing semantics, Settings' dispatch receipt represents the committed attempt, including a recorded blocked attempt, rather than a claim that choices were granted.
The previous false-success finding does not carry forward unchanged after this explicit failure disposition and committed History path.

The following source cases were checked by tracing the current branches, without executing them:

| Case | Source result |
| --- | --- |
| All captured countries append | One shared handler and numeric size payload. The binder stores the actual sequence, marks released, consumes its context, and coalesces `.14` wakes. |
| One valid country appends and another rejects | The matching appended row is quarantined, captured recipients are cleared, and one payload-zero attempt is recorded. The blocked envelope gets its sequence and no wakes. |
| Captured country has only a prior active or queued row | Its last row's different firing ID prevents quarantine. The active flag, pointer, prior choices, and prior receipt rows are not modified by this rollback loop. |
| Captured country is unaligned | The quarantine loop makes no indexed mutation in that country. Existing corruption/alignment gates continue to prevent local queue activation. |
| Binder is invoked again without a new firing context | Its positive-ID guard prevents duplicate release or wake scheduling because the first accepted binding consumed the context. |
| A later lifecycle reconciliation follows failed publication | Newly quarantined rows are skipped by the queued-only starter. Prior valid queued work remains available under its own state. |

Both successful and blocked producer branches perform no further owner work after their shared handler call.
The ordinary Settings branch still invokes the owner transaction directly and excludes the generic `.1` enqueue and second handler.
The `.1` console bridge's deliberate global forced-setup flag at event lines 18-21 remains accepted behavior, not a new defect.
The owner prefire helper separately retains the existing manual/forced/CXT checks.
No tag-departure disqualification or per-receipt human-controller column was added to achievement tracking.
The source still contains 32 unique Event027 event definitions.

The public eligibility key at `localisation\english\027_doctrine_research_l_english.yml:359` says "Use this country's own curriculum" and does not impose completion of the whole batch as eligibility.
Its achievement registry consumers remain the shared `possible` tooltip wrappers for the three Event027 achievements.

Meaningful checks were limited to the current recorder boundary, mutually exclusive success/failure branches, firing-ID-specific quarantine, original-row preservation, queued-only activation, one-shot binding, wake scheduling, direct dispatch, and the accepted achievement wording/controller policy.
No source file was patched by the auditor.
Weak AI, complete normalized named scenarios, genuine baseline comparisons, exact native transactions, persistence/reentrancy, and visual acceptance remain the parent's acknowledged unresolved work.
No new MCP call or game launch was performed, and the previously recorded route blockers remain explicit.

| Current source | SHA-256 |
| --- | --- |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `b17677ad2809791243a6e2107331f43f2b9a62233dde1fbf01d500feed9e6dcd` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `7fde6b681e3bd62a38eb2c01a22ffab8fc262ad2b0e37e7d0fede43c028d9b81` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `577119da0c1f1a512fb79c597959bddfcfc21d3653ee6770df173ca1ec07ecea` |
| `events\027_doctrine_research.txt` | `777149623bf633fc07c04cf4f7f747a208024d2afee00d6e7120ae4bf9e01751` |
| `localisation\english\027_doctrine_research_l_english.yml` | `aab9117be89de76206de3691200d9d01d7397678b41663c00d473f7c4dacc1b4` |

These identities were rechecked before recording this verification.
The shared Settings file changed concurrently during the final check.
Its Event027 direct branch was reread at lines 4341-4347 and retains the same producer call, attempt-dispatch receipt, display refresh, and exclusion of the generic enqueue/handler sibling branch.
The table records the refreshed Settings hash rather than the earlier file identity.
Only this handoff was edited.
