# Event 016 raid lifecycle MCP capture — 2026-09-02

## Scope and status

Read-only capture for `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` and `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`.
Only this handoff is authored.
No gameplay, tool code, configuration, or source scenario design was changed.
Concurrent parent edits were preserved.
No game launch or log collection occurred.

Status: the supported selector syntax and the cause of helper omission are established.
A full structural baseline was captured and sent to the parent.
The completed narrow trace/lint/render requests did not inspect the requested helper bodies.
Full, source-linked lifecycle diagnostics remain blocked/pending after the parent paused further MCP requests to avoid contention with the probability baseline.
No lifecycle pass or gameplay completion is claimed.

## Exact selector syntax, verified against installed implementation

Installed server: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.7/node_modules/hoi4-agent-tools/dist/hoi4_agent_tools/`.

`schemas/event.js:40` defines selector kinds `event`, `namespace`, `file`, `source`, `node`, and `manifest`.
There is no `kind: "helper"` selector.
The direct node form is:

```json
{
  "kind": "node",
  "nodeId": "helper:brilliant_scientist_portal_register_beachhead"
}
```

The `helper:` prefix is not a guess.
`event/source-analysis.js:644` constructs `ownerId = helper:${name}` and adds a node whose kind is `helper`, label is the scripted-effect name, sourcePath is the source file, and location is the top-level assignment.
`event/queries.js:99` compares the supplied node ID to the actual node ID.
Thus the empty trace described below is a catalog-coverage problem, not an incorrectly guessed node-ID prefix.

Other supported forms:

```json
{
  "kind": "file",
  "sourcePath": "mod:common/scripted_effects/016_brilliant_scientist_raid_effects.txt"
}
```

```json
{
  "kind": "source",
  "sourcePath": "mod:common/scripted_effects/016_brilliant_scientist_raid_effects.txt",
  "line": 78
}
```

```json
{
  "kind": "manifest",
  "manifest": {
    "id": "event016_raid_lifecycle",
    "sourcePaths": [
      "mod:common/scripted_effects/016_brilliant_scientist_raid_effects.txt",
      "mod:common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt"
    ]
  }
}
```

Observed schema rejections were `kind: "helper"` (invalid discriminator) and file `path` (unrecognized key, missing `sourcePath`).
Both were corrected using the schema.
No further selector variants were brute-forced.

## Why the accepted narrow selectors omitted the helpers

The installed `event/service.js:750` selects focused analysis for all `trace` and `explain_path` requests and for `scan`, `roots`, or `lint` when any selector is present.
`event/service.js:154` limits focused source discovery to `events/**/*.txt` and `common/on_actions/**/*.txt`.
It does not discover scripted-effect files.
`event/service.js:717` and 735 additionally force helper projection off for focused analysis.
Consequently `expandHelpers: true` does not make a fresh focused graph include either target file.

The full-graph cache can sometimes satisfy a focused request, which explains the earlier lifecycle audit's change from helperless to helper-bearing responses.
However `service.js:719–727` returns a valid cached focused graph before testing for a full sibling.
Do not assume that creating one full graph automatically upgrades an already cached narrow request.

For a source-frozen, genuinely full narrow query, the implementation-supported route is `mode: "state_flow"` with the same node/file/source/manifest selector.
This mode is excluded from the focused predicate.
`service.js:835` also places selector-filtered lint issues containing `STATE`, `FLAG`, `VARIABLE`, `ARRAY`, `TARGET`, or `SCOPE` in `report.issues`.
Its `report.flow` comes from `inspectEventStateFlow(graph, selector, stateSubject)`.
A specific state subject keeps the returned state-flow evidence focused on the receipt being checked.

Reusable invocation for the parent's source-frozen pass, sourced from the implementation but not claimed as a successful result in this handoff:

```json
{
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0",
  "mode": "state_flow",
  "selector": {
    "kind": "node",
    "nodeId": "helper:brilliant_scientist_portal_register_beachhead"
  },
  "stateSubject": {
    "kind": "state_flag",
    "name": "brilliant_scientist_portal_beachhead_active"
  },
  "expandHelpers": true,
  "maxDepth": 2,
  "maxNodes": 40
}
```

The same exact node-ID construction applies to `brilliant_scientist_portal_cleanup_beachhead`, `brilliant_scientist_portal_reconcile_country_beachheads`, `brilliant_scientist_portal_cleanup_country_beachheads`, `brilliant_scientist_begin_biological_deployment`, `brilliant_scientist_refund_biological_deployment`, and `brilliant_scientist_resolve_biological_deployment`.
This names existing source surfaces, not new scenarios.

## Captured revisions and source hashes

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

### Full structural baseline

Revision: `f9b65b464e4880b782f3f153b251bdc285b68d8628454aaf3fdf1d2ada499baa`.
Graph hash: `625dc86a9b5c65ba403cc0bbf4cef763856e5762a0b9f7c705788af308e4e219`.
Captured by `hoi4.event_inspect`, `mode: "scan"`, no selector.
The baseline was sent to the parent before requesting the later full state-flow pass.

Artifact: [full scan summary](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2764568bd1dacc6198490d6e74fce37c19c8acc59762d6d821878323b96ca71c/cbb44ac924d33608d170800b71b9a44ad79024eb47ae6428c6a0d19db7a2ea98/event-scan-f9b65b464e48.json).
Artifact SHA-256: `2764568bd1dacc6198490d6e74fce37c19c8acc59762d6d821878323b96ca71c`.

The report is a `large-scan-summary`, not a serialized full graph.
Its source inventory contains 3,921 paths with digest `fc6d8de8ab400de29833ae3e4d76f110f0cbcddb4be3a2307dd6bf7876c1213f` using `sha256-length-prefixed-path-digest-v1`.
Only 256 individual source hashes are retained.
Neither target scripted-effect file's individual hash is exposed in the retained subset.
Do not silently substitute an observed disk hash for an authenticated individual graph-source hash.
The full graph itself reported 18,841 helpers, but that count is not a scoped diagnostic result.

### Completed focused requests

Revision: `c9e9ac572a640a5ffaf82e4cd3c6b88ce5293ff4ded2a168fb5fb0beb1576d9c`.
Graph hash: `3b58bf4742ed67a19507df014d16b03e31f695e9e863102f7fd3721ac93d2467`.
Both target scripted-effect paths are absent from this graph's complete 368-path source-hash map.
The graph contains zero helper nodes.

Disk SHA-256 observations, explicitly not individual hashes authenticated by the full baseline artifact:

| File | Earlier observation | Later observation |
| --- | --- | --- |
| `016_brilliant_scientist_raid_effects.txt` | `e95269f750ab934bf2bf3eb1d2725a10e50dbb8f243406c82df8204cc8f040e3` | Same |
| `016_brilliant_scientist_biological_operations_effects.txt` | `6fc8a53d899404d5cc9a088103780871c9c9d50473b7dacb3f48d28f46a333a1` | `3eab89d21a13af8d252686e7d6ae21cfb8e2c57e3d85bf0e1f2b6ea1c0659a2e` |

The biological file changed during the capture window, consistent with the parent warning that nonweighted edits would continue.
The later hash remained stable in the final local observation.
A post-change claim must use a graph exposing the exact target-file source hashes.

## Actual source-linked artifact inspection

The completed artifacts were opened locally from the server's generated artifact store under `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/`.
Only generated evidence was read.
Local reads avoided further MCP requests after the parent pause.

| Request | Artifact | Actual scoped result |
| --- | --- | --- |
| Node trace, portal register helper | [trace JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b5d22990bf7047432a4a710b24a89f380b1ffcff1380aa15b3c150b8cc68b0b/a73ef6f4d655f44e9c7d8cc8dbb386de163bab36bb38920b34c2d24ba3cac13c/event-trace-c9e9ac572a64.json) | `report.trace.startNodeIds = []`; zero trace nodes. Correct node ID, omitted helper catalog. |
| File lint, raid effects | [lint JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7f051a995c812fd97d1b29398ee7393c6427c41b1ed3b81d6efc2be1aad7a07/20e920fc21155eff648d33af65d5b345c7d288b7dfdd0ac516861f5b9dc59e00/event-lint-c9e9ac572a64.json) | Zero `report.issues`, but the selected file has no indexed nodes and no source hash. This is zero coverage, not a clean lint pass. |
| Same helper, state render | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da4e9cd0bffd947c890ec07f672ed3f447f5920e04dcef335d4ac95e99f8f4f9/f21805198140e0baf4f7b14fcdb0d7f0bd1191276d9c397df43e25b78276c5c4/event-state-c9e9ac572a64.json) | 40 selected nodes, zero requested helper nodes, zero nodes from either target source file. |
| Same helper, state render | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac22865475802220b64a386f8393db07e1900796125471cc5a655dac21c8177b/494145f891eb74b423e93915a50774cf6987b5409abf76f86d8f3b063a57ebd9/event-state-c9e9ac572a64-manifest.json) | Preserved with the JSON; not treated as a raid lifecycle rendering. |
| File scan with `refresh: true` | [focused scan summary](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9251e5ae794411955d61361d55d964a8288ddf9f16c4fe202af1005fd570cbb/b1026ec6a230dc7d8fba3c230b5083f4a1d0740f189d8230033f07eb6bbbaa0b/event-scan-c9e9ac572a64.json) | Still focused, zero helper nodes; refresh does not change the route-selection rule. |
| Selector-free full scan | [full scan summary](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2764568bd1dacc6198490d6e74fce37c19c8acc59762d6d821878323b96ca71c/cbb44ac924d33608d170800b71b9a44ad79024eb47ae6428c6a0d19db7a2ea98/event-scan-f9b65b464e48.json) | Target-file issue and diagnostic samples are absent; summary truncation prevents a source-local conclusion. |

The fallback render's first selected node was `entry_00fb47fe795e360e179d702d` from `game:common/on_actions/00_on_actions.txt`.
Other first nodes came from `mod:common/on_actions/cbrn_achievement_on_actions.txt`, `mod:common/on_actions/002_zombie_outbreak_on_actions.txt`, and vanilla on-actions.
This verifies that the rendered picture was unrelated fallback content, rather than merely reporting a workspace-wide diagnostic count.

No concrete defect inside either target helper body can responsibly be attributed to these completed MCP artifacts.
The source helpers are present at raid lines 78, 109, 165, and 234 and biological lines 161, 211, and 346.
An omitted body cannot be classified as missing gameplay.

## Paused full-state-flow request and comparison limit

A full `state_flow` request using the two-file manifest was submitted.
Its execution had already bundled subsequent lint/render calls for that manifest.
The parent then requested no further MCP work after the pending call to avoid contention with the probability auditor.
The residual execution was terminated and no usable structured full-state-flow/lint/render result or new artifact was retained from that batch.
No fresh MCP request was issued afterward.
Therefore current full source-linked diagnostics for these helpers remain pending; the full scan summary cannot stand in for them.

One comparison attempt used `before: {revision: "c9e9ac572a640a5ffaf82e4cd3c6b88ce5293ff4ded2a168fb5fb0beb1576d9c"}`, omitted `after` (current), and `render: false`.
It returned `EVENT_REVISION_NOT_CACHED`, “Requested event graph revision is not cached.”
Focused graphs are not remembered by the full-revision cache: `event/service.js:744` calls `rememberGraph` only for full analysis.
No post-change comparison is claimed.

The previously established report-wrapper incompatibility is recorded once here and was not repeatedly retested: `event-analysis.v1` reports and `event-render.v1` render JSON are not accepted as full-graph `before.artifactUri` inputs and return `EVENT_GRAPH_ARTIFACT_INVALID`.
The preserved full revision is the usable baseline reference while retained in the server cache.
The summary artifact is durable evidence of that revision, not itself a compare-compatible full graph.

## Reference checks and handoff

Offline Data structures and Scopes references were revisited for saved targets and state/country scope boundaries.
The previously consulted core offline wiki pages and repository event-audit skills remain the reference basis.
No raid-specific offline wiki page was located.
Installed vanilla `common/raids/_documentation.md` explicitly documents raid-instance `actor_effects` and `victim_effects`, `var:actor_country`, `var:victim_country`, `var:target_state`, and `var:target_province`.
Its outcome example uses `var:ROOT.actor_country` and `var:ROOT.target_province` inside changed scopes.
Those constructs in the portal source must not be rejected merely because the event graph cannot infer raid-instance scope.

The biological resolve helper's weighted selection remains under the parent's existing probability audit.
This task did not alter weights, start a duplicate probability audit, or add scenario design.

Parent next action, after source freeze: use the verified full `state_flow` selector route, read `report.issues` and exact target-file `sourceHashes`, and verify that a subsequent render actually contains the requested helper IDs before accepting it as evidence.
Retain `f9b65b464e4880b782f3f153b251bdc285b68d8628454aaf3fdf1d2ada499baa` for comparison if still cached.
Current blockers are omitted source bodies in focused analysis, the paused full helper pass, truncated individual hashes in the durable full-scan summary, and absence of a completed post-change comparison.

## Raid-unit conservation capability check — 2026-09-02

Finding: no documented installed scripting mechanism was found that relocates exactly the raid-selected division while retaining its complete state, or serializes and reconstructs that division's exact carried manpower, equipment inventory, damage, and experience.
The portal reconstruction remains an unresolved conservation blocker; conserving formation count does not prove conservation of division state.
This is a limitation of the exposed, documented scripting API, not a claim about inaccessible engine internals.

Evidence from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`:

- `documentation/effects_documentation.md:8264`: `teleport_armies` is STATE-scoped; its `limit` evaluates the army owner's COUNTRY, not the selected division.
It cannot isolate one raid unit when unrelated units share that state, so it does not meet the requested contract.
The narrow relocation/movement search found no documented specific-division location setter.
- `common/raids/_documentation.md:278` exposes the selected division through `division_effects`, but the documented raid-instance variables at line 549 are only actor country, victim country, target state, and target province.
`raid_damage_units` and `raid_add_unit_experience` can modify the assigned unit (`effects_documentation.md:5216` and 5233); they do not export its existing state or relocate it.
- `documentation/dynamic_variables_documentation.md:9` lists country, state, unit-leader, and other supported dynamic-variable scopes, but no division/unit inventory-snapshot scope.
The unit-leader `num_equipment` entry is not a selected-division equipment manifest.
No documented getter was found for exact per-division manpower, per-type/variant carried equipment, or existing unit experience suitable for lossless reconstruction.
- `documentation/triggers_documentation.md:7685` and 7695 expose `unit_organization` and `unit_strength` comparisons only.
Those scalar checks cannot recover the missing equipment composition or manpower independently.
The raid's predefined experience/organisation/strength success modifiers (`common/raids/_documentation.md:329–349`) are outcome-scoring inputs, not documented snapshot variables.
- `create_unit` (`effects_documentation.md:3278`) creates an OOB-style new division with initial factors; it does not clone the selected division.
`set_unit_organization` at line 7879 multiplies current organization by a factor, while `add_divisional_commander_xp` at line 1135 adds commander XP; neither supplies the missing state serialization.
`delete_unit` with `disband = yes` at line 3476 returns resources to national pools, not an exact selected-unit reconstruction receipt, and does not preserve unit state.

No gameplay change, state-wide teleportation, full-readiness replacement, extra cost, or fallback is proposed or approved by this check.
An approved-mod search was not needed: no usable engine primitive emerged from the installed effect, dynamic-variable, trigger, and raid documentation.
Exact preservation cannot be certified with the presently documented API; this blocker must remain explicit unless a supported exact mechanism is established or the user approves a different design.
