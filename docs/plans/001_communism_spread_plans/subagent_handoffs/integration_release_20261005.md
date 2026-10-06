# Event001 Shared Integration Release Audit

Audit date: 2026-10-06.
Disposition: partial, with actionable shared-source defects and incomplete probability/runtime evidence.
The parent task names user G6 release-QA authority for coherent repairs within the existing design.
That authority supports the repair requests below, but does not approve every historical source-spec claim.

## Completion by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Root, category and name wiring | Source-present | `chaosx.nr1.1` in `events/001_communism_spread.txt:21`, fire-once ID1 at `chaosx_logic_effects.txt:245`, English name in `chaosx_event_names_l_english.yml:3`, detail selector at `chaosx_scripted_localisation_events_log.txt:6588`. |
| Global actor/evolutions | Source-present | Event001 has no forced default actor, matching its global crisis and actor-free evolution recorders. `communism_spread_event_log.event_id=91` is the separate Revolution identity, not an incorrect Event001 ID. |
| Event001 to Event091 unlock | Source-present, weighted proof open | Stage3 records the Event001 evolution and calls `increase_world_revolution_weight_from_communist_whisper`, which updates ID91. Cleanup clears the unlock and resets ID91 weight. |
| Revolution territory handoff | Source-present, lifecycle unverified | `events/091_the_great_revolution.txt:111` consumes communist-controlled states and calls state-specific spawn logic. Delayed popup/cleanup ordering and REV creation are not proved by the focused MCP root view. |
| Revolution aftermath dispatch | Defective | Monthly REV callback dispatches Portugal–Galicia repeatedly, detailed below. |
| Revolution actor | Misattributed | Shared ID91 default is SOV, despite REV being the active Revolution country. |
| Achievements | Design gap | No Event001-prefixed achievement definition was found in the shared achievement file. A new suite requires an accepted design disposition, not an auditor patch. |
| Assets/catalog/full gameplay | Partial or outside this bounded pass | Artist/portrait, GUI, probability and workbook owners retain their evidence gates. |

## Minimal parent-owned repair requests

1. **Stop unrelated recurring Portugal popups.**
   In `common/on_actions/091_the_great_revolution_on_actions.txt:34`, `on_monthly_REV` loops `every_other_country` when all countries are communist and calls `chaosx.nr93.1`.
   The actual target in `events/093_portugal_galicia.txt:22–31` redirects to POR and `chaosx.nr93.2`.
   Old: repeated dispatch of Event093 once per other country every month.
   Recommended new: remove this unrelated dispatch block until an accepted Revolution aftermath callback exists.
   Do not guess an `nr91.X` replacement, because the current 091 namespace defines only .1, .2 and .3.
   The wrong call is a live source defect, while the missing intended Revolution aftermath is an unresolved design item.

2. **Attribute Revolution to its actual actor.**
   In `common/scripted_effects/chaosx_events_log_effects.txt:471–473`, the ID91 branch uses SOV.
   `events/091_the_great_revolution.txt:32–40` creates/loads REV, which receives territory and rebel armies.
   Old: an unconditional SOV default actor.
   Recommended new: a guarded REV actor, or the parent's exact prefire Revolution actor receipt.
   Retain no actor when the actor cannot yet be established, rather than inventing a Soviet firing actor.
   Event001 global-crisis actor behavior should remain governed by its own source identity.

These requests were sent to the parent before waiting for comparison results.
The auditor applied no gameplay patch.

## Accepted-plan disposition, assets and documentation

- `agent_decisions_2026-10-05.md` records parent-authorized root wording, bounded per-type reports and lifecycle repairs as implemented in source.
  Their meaningful source evidence is in `subagent_handoffs/release_qa_20261005.md`.
  This audit does not re-audit the independent gameplay owner's intervention/timer changes.
- The capped priority conversion budget versus spec 40/80/100% state-level chances, and the 0.90 state-drift cap versus uncapped spec formula, remain unresolved acceptance conflicts.
  They are openly recorded in the overview and decision log, so neither is silently approved here.
- `portrait_source_20261005.md` supplies the canonical portrait-creator handoff, attributed durable 1918 institutional source, installed source-placeholder DDS and exact checksum.
  The user's styled final remains pending.
- `asset_provenance_20261005.md` documents stock image reuse and the earlier bespoke-scene gaps.
  The parent separately reports a 15-image production task in progress.
  A new artist handoff and parent-selected final DDS evidence must supersede the relevant old gap before claiming art completion.
- `catalog_changes_pending.md` is accepted/queued for the workbook owner because this audit forbids XLSX/CSV writes.
  The workbook and exports were not inspected or changed here.
- The probability pass is assigned to `/root/probability001_release`, with intended handoff `subagent_handoffs/probability_release_20261005.md`.
  No normalized AI or same-scenario probability comparison is claimed by this integration audit.

## Meaningful source validation

The runtime Event001 namespace has 34 top-level definitions, with no duplicate Event001 IDs.
Direct targets in Event001, Event091 and the Revolution on-actions resolve to actual top-level event definitions.
This check deliberately does not equate an existing target with a correct target, which is why the Event093 error remains a defect.
Entry category and player-visible name/detail mappings were read from their current shared definitions.

## MCP evidence and limits

The live tool list exposed event inspect/render/compare and reference/source lookup routes.
No connected server-version/health or native-task-negotiation endpoint was exposed, so no helper-expansion or job route was used.
The selectors were corrected from the schema-hidden object to `{kind: "event", eventId: "chaosx.nr1.1"}` after validation returned the required discriminator and field names.

- Inspect: `mode=trace`, downstream, depth 2, 25 nodes, 60 edges, helpers disabled, no refresh.
  Result: `EVENT_INSPECTED_PARTIAL`, `analysisMode=focused`, revision `0f7411e7faa6030bd9a0b378146a88fb89cbe631cbcce8ad6524a093cca570e7`, helpers 0, one blocking diagnostic, validation false.
- Render: `view=neighborhood`, same root/depth/node limits.
  Result: `EVENT_RENDERED_PARTIAL`, 12 selected nodes, `complete=false` in the retrieved manifest, 5 unresolved helper occurrences.
- [Inspect report](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e23cbbb01eea3f5cc80be03e2d62742c332436de81815d40bfa85275448173b/fbed0dfa33a4c3e1e13eebdbd984e11a1d22ee1bc71e54a1cc2a6ebe63f6326c/event-trace-0f7411e7faa6.json).
- [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/936beb3ca895120c8ee62107f8b154fad5476bbac987be4fd7aa4b36b1d32083/8c9b0bcae36cb6e22d946be19c141a4236e914962a4a3f8b1b73c71451782ed7/event-neighborhood-0f7411e7faa6-manifest.json).
- [Render PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efd1650c90d49d647e1333af68fc4ddfb4a66846b2109c977d40633b96efbf9d/16d6dd3f976d7345c21e367850b5ae81e150989d6f7196211854c9c8c418a056/event-neighborhood-0f7411e7faa6.png).

The full manifest was retrieved in bounded base64 byte ranges after the one-shot resource response truncated its JSON.
The reconstructed byte count matches the declared 48845 bytes.
Its source inventory covers events and on-actions, excluding scripted effects, localisation, achievements and GUI.
The unresolved helper labels are the focused-analysis boundary, not proof that these existing source definitions are missing.
The inspect/render results therefore do not establish helper lifecycle, gameplay correctness, costs, AI balance or live behavior.

A compare without a supplied baseline returned `EVENT_COMPARISON_BASELINE_REQUIRED`, with the explicit message “Provide a cached revision, graph artifact, or proposed source overlay”.
A second comparison supplies the event-file baseline snapshot as a `proposedSources` overlay with `relativePath` and `source`, selecting the same root and 25-node limits.
That valid overlay request returned `timed out awaiting tools/call after 600s`, with no comparison graph, source revision or changed-node evidence.
The direction is current indexed source to historical overlay, so any returned changes must be read in reverse for old-to-current review.
It was bounded to the event file and could not have proved shared-helper integration even if it had returned.

## Reference evidence and audit scope

The installed `documentation/effects_documentation.md` `country_event` section was read through `hoi4.reference_read` at lines 2943–2967, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` event-creation section was read at lines 37–40, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
The context result also listed omitted event-target, scope, trigger, on-action and localisation sources.
This narrow review does not claim those omitted rules were covered.
The installed vanilla `events/NewsEvents.txt` lines 8–34 was read as the triggered, major-news precedent.
No Paradox web request, HOI4 launch, desktop control, spreadsheet write, index operation or commit was performed.

Skills read/applied: AGENTS.md, chaos-redux-events, chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-event-assets and the shared-surface boundaries in chaos-redux-scripted-gui.
Only this handoff file is owned by this auditor.
Gameplay, shared localisation, shared GUI and assets remain with their assigned owners.

## Parent review and Event091 bootstrap follow-up

The parent accepted removal of the whole unrelated `on_monthly_REV` dispatch block, with no invented replacement.
The parent also accepted guarded REV actor mapping rather than SOV.
These are accepted and queued repair requests at this audit snapshot, not auditor-applied gameplay edits.

The root bootstrap at `events/091_the_great_revolution.txt:29–44` chooses an unrestricted global state, stores that state's owner in a temporary variable, transfers the state to REV, loads the OOB/templates/faction, then returns **every** REV-owned state to the one sampled owner.
The all-REV restoration is directly source-backed.
It can consume legitimate existing REV territory and erase occupation control because `transfer_state_to` changes owner and controller.
No claim is made that lack of caller preinitialization alone proves a temporary-variable failure.
The repair should use a bounded state/owner receipt rather than any stale cross-scope assumption.

Replace only the existing bootstrap block with the following parent-reviewed candidate and retain the existing claims, annexation, fan-out and cleanup continuation inside a `world_revolution_bootstrap_ready > 0` guard.
This leaves a no-seed case without mutation, introduces no invented terminal fallback and does not replace the Revolution's first mechanics.

```hoi4
set_temp_variable = { world_revolution_bootstrap_ready = 0 }
if = {
	limit = { REV = { exists = yes } }
	set_temp_variable = { world_revolution_bootstrap_ready = 1 }
}
else = {
	random_state = {
		limit = {
			impassable = no
			is_capital = no
			owner = {
				exists = yes
				uses_normal_civilian_systems = yes
				num_of_owned_states > 1
				controls_state = PREV
			}
		}
		save_event_target_as = world_revolution_seed_state
		owner = { save_event_target_as = world_revolution_seed_owner }
		transfer_state_to = REV
		REV = {
			load_oob = "REV_1936"
			create_communist_rebel_templates = yes
			create_faction = revolution_front
		}
		event_target:world_revolution_seed_state = {
			transfer_state_to = event_target:world_revolution_seed_owner
		}
		set_temp_variable = { world_revolution_bootstrap_ready = 1 }
	}
}
```

An existing REV bypasses the bootstrap and retains its OOB, faction and owned territory.
A fresh REV samples globally by eligible state, preserving the prior state-selection weighting model while excluding impassable, capital, occupied and last-state donor cases.
The donor owner controls the selected state and retains another owned state.
Only the selected seed is restored to its captured owner.
The parent must review fresh bootstrap, existing REV, one-state donors, occupied donors and no-eligible-seed cases against actual engine behavior.
The focused event graph cannot prove whether a landless REV remains usable through the immediate annexation continuation.
The current ordering is preserved here rather than silently claiming that runtime question resolved.

Exact guarded actor branch:

```hoi4
else_if = {
	limit = {
		check_variable = { event_id = constant:communism_spread_event_log.event_id }
		REV = { exists = yes }
	}
	REV = { ROOT = { set_temp_variable = { events_log_default_actor = PREV } } }
	set_temp_variable = { events_log_default_has_actor = 1 }
}
```

Additional references read: installed effects `random_owned_controlled_state` lines 5512–5520, `random_state` lines 5574–5584, `save_event_target_as` lines 6496–6504 and `transfer_state_to` lines 8332–8347 at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The event-target and transfer sections were also read through MCP.
Offline Data structures regular event targets lines 303–328, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, establishes receipt lifetime.
Installed trigger docs `controls_state` lines 2329–2336 supports PREV.
Installed `events/AAT_Finland.txt:3761` and the existing Event006 package trigger at `common/scripted_triggers/006_independence_wave_package_triggers.txt:9–13` provide owner/control precedents.
No new random weight is selected by the auditor.
The probability owner was notified of the Event091 eligibility implications.

A narrow `hoi4.script_validate` request used `kind=effect`, `scope=country`, installed documentation, limit 25 and explicit state/country bindings for the two receipt targets.
It produced no result before this bounded handoff was delivered, and its orchestration cell was terminated while awaiting the read-only request.
The candidate is not marked validated.
A narrow Event091 request used `event_inspect` trace and `event_render` neighborhood with `{kind:event,eventId:chaosx.nr91.1}`, depth 2, 20 nodes, helpers disabled and no refresh.
Those requests also produced no result before handoff, and their orchestration cell was terminated while awaiting the tools.
This is an outstanding Event091 inspect/render evidence gate, not a claim that the routes are absent, a completed MCP job cancellation, or equivalent engine proof from source.


## Current source snapshot

Snapshot UTC: 2026-10-05T21:21:18+00:00.
Other agents are editing this shared tree, so the hashes bind this source review to these exact bytes and do not certify later revisions.
The focused MCP graph revision can remain older than current owner edits, so current-source conclusions and MCP coverage are reported separately.

| Source path | SHA-256 |
| --- | --- |
| `events\001_communism_spread.txt` | `077282727c803a58f112b7d34a31c38a210204cafac4bc38d6ec078a33f233ee` |
| `events\091_the_great_revolution.txt` | `9d271643d8d4402ccc8b038c9359810517c8d5ba2deaaff651dd6b29b79a1e87` |
| `common\on_actions\091_the_great_revolution_on_actions.txt` | `13e2add1ac63a0e093e8aa58c8512d8a7d8fe75e932917519545bd0ddb943da9` |
| `common\scripted_effects\001_communism_spread_effects.txt` | `e524489010882292d30917a5efa558fde119ae0f282655aba5b5a63fea2abdb6` |
| `common\script_constants\001_communism_spread_constants.txt` | `afeecde85b9dc698b7ac68c24d191bd70a7320573ce77b3f08554893b928da37` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `60cc08d2f9c04d6a017a415cd61aedcd4b1d920ade0de0e4716d249071660403` |
| `common\scripted_effects\chaosx_logic_effects.txt` | `7d4ae19f327aeba7a62c98bda9236369a319be528752e80a9b5c6c734a5f2b81` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `144173ab4bf2c344775670a7b05b06e5de3f309d871d396754985baa702e6e1d` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `56f6dbf4db7e709cd8269a8b54a6734b5e868e076f15ae6dc3a6e23f55449c4d` |
| `localisation\english\chaosx_event_names_l_english.yml` | `c081593fd0270ca58983b568bf208ff698ca5109b0f609fc14fa853c8b8ee64b` |
| `localisation\english\chaosx_gui_l_english.yml` | `a3f75b2d406573d2b11e977c9dad9a80a40167772cf26f134f99f9fc0ab9367c` |
| `common\achievements\chaos_redux_achievements.txt` | `0c25cf1e5db6de4197fcb0190f084525d561e3e3f5a2437deff09186005b5b3a` |
