# Event 027 engine-evidence retry

> **Superseded status notice (2026-09-01):** This dated engine-evidence retry is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its source receipt finding remains useful, while its dated MCP artifact references are no longer current.

Date: 2026-08-31

Auditor mode: read-only completion audit

Scope: `chaosx.nr27.1` downstream event evidence, one native doctrine folder, the custom `chaos_warfare` grand doctrine identifier, and the native `add_mastery` one-point contract.

## Completion classification

**Overall status: partial and acceptance-blocked.**

- **Source-playable:** yes, based on the current Event 027 source implementation and its fail-closed transaction guards.
- **Engine-certified:** no.
- **Partial engine evidence:** yes. Event lint, event overview render, doctrine folder discovery, and doctrine rendering returned resource-backed artifacts.
- **Blocked evidence:** event comparison, source-accurate doctrine rendering, focused custom-grand-doctrine tracing, and runtime proof of native one-point mastery behavior.

This retry does not justify a completion claim. The successful calls returned partial or validation-failing results, and no cached comparison baseline was available.

## Completion status by surface

| Surface | Status | Audit finding |
| --- | --- | --- |
| Event 027 source chain | Source-playable, partial engine evidence | The root resolves and renders, but helper expansion was deliberately disabled and the returned validation did not pass. |
| Event 027 comparison | Blocked | The returned revision was rejected by `event_compare` as not cached. No accepted before-and-after comparison exists. |
| Native doctrine folder | Partial engine evidence | The installed `land` folder and four native grand doctrines were discovered by the technology folder route. |
| Custom Chaos Warfare doctrine | Partial engine evidence | `chaos_warfare` was discovered as a `grand_doctrine` in `land`, with its four tracks and resolved icon. The technology trace schema cannot trace a grand-doctrine identifier as a technology. |
| Doctrine visual evidence | Partial, not source-accurate | Doctrine render succeeded and produced JSON, SVG, PNG, and manifest artifacts, but reported `sourceAccurate: false` and failed validation. |
| Exact native mastery transaction | Source-playable, runtime proof blocked | Source increments raw mastery one point at a time and accepts only an exact one-level readback. Native residual, threshold, banked-point, and Special Forces branch behavior remain unproven in a live consumer. |
| Weighted AI and probability | Existing acceptance gap, not rerun | No probability-bearing source was changed in this bounded retry. The accepted Event 027 probability scenarios still require their separate `chaosx_ai_probability_auditor` completion evidence before final promotion. |
| Assets, localisation, logs, details, catalog, and documentation | No new production scope, acceptance remains open | This audit changed none of these surfaces. Existing source wiring is not promoted by the partial MCP result, and consumer evidence remains subject to the Event 027 acceptance checklist. |

## Event MCP evidence

### Requested lint call

The first call used the requested selector body `{ eventId: "chaosx.nr27.1" }` with `mode: lint`, `direction: downstream`, `refresh: true`, `expandHelpers: false`, `maxNodes: 40`, `maxEdges: 120`, and `maxDepth: 5`.

- Tool status: error before inspection
- Code: JSON-RPC `-32602`
- Exact blocker: `Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`
- Revision and artifacts: none

The installed schema required the selector discriminator. The bounded retry added `kind: "event"` and preserved every requested limit.

### Schema-compatible lint retry

- Status: `ok`
- Code: `EVENT_INSPECTED_PARTIAL`
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Revision: `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`
- Graph hash: `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`
- Boundary: downstream, depth 5, 40 nodes, 120 edges, helpers disabled, refresh enabled
- Validation: failed
- Validation message: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`
- Structured blockers: none
- Diagnostic: `MCP_INLINE_FILES_TRUNCATED`, with 367 files represented and 64 inline
- Linked lint report direct issue list: empty

Artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8187a8cc6080f71081a05e309a35dc64bb649042f5096ad6729dd497c774e8c/d062433b5686f918f5699756b22370680bea91c589ff075abb08193b3aace5bc/event-lint-2725045f62d1.json`
  - SHA-256: `f8187a8cc6080f71081a05e309a35dc64bb649042f5096ad6729dd497c774e8c`
  - Size: 2,030,833 bytes

The returned workspace totals include unrelated event content and must not be attributed to Event 027. They reported 9,722 events, 15,150 options, 38,320 edges, 2,206 diagnostics, and one blocking diagnostic across the analyzed workspace. The direct Event 027 report did not list a root-specific issue, but the call remained partial because workspace-wide helper and lifecycle projections were deferred.

### Event overview render

The render used the same event selector and workspace with `view: overview`, downstream direction, `maxNodes: 40`, helpers disabled, and no refresh.

- Status: `ok`
- Code: `EVENT_RENDERED_PARTIAL`
- Revision: `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`
- Graph hash: `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`
- Layout hash: `1729fe993aee0578ed8fd2b03d51b4155b6fda6c3d8b83e712401a363f89cc5c`
- Selected nodes: 2
- Omitted nodes: 42,454 across the loaded workspace graph
- Branch renders: 0
- Validation: failed with the same deferred helper and lifecycle message
- Structured blockers: none

Artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1456711090ee7d79e9462bdcf5ae4145fc6ca1cb480f09fccbf2836f76f0a37b/e324731cb4830acb12afc1a34b7d10431f68261f03f2b424e976fc0d18928b0b/event-overview-2725045f62d1-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f109ce6e66cb8e8e8e2528c33c45f550644431d81ce67b3185d6ea13260d1e0/f42fcb68e0c15dc175c8cd6a462cf5f5d3e7fc007397181f86ea1bbaf278dc96/event-overview-2725045f62d1.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bf1aa93d1847bbfbca72d8563e98dbbf8797d275b83c99386bf48c6463b5ad1/c2c34dde2366e6ad5c9ad181f266ce751f40a3d6f7bca70896b9c255c9cc0655/event-overview-2725045f62d1.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a54cd6d78871ea91c65c4691a6952610a847c85fc3212c3c56d9d4b6b9b159a9/9e8307f645c15587209018a569dd12cb154e5725de5133da9a085e19fb5c84ae/event-overview-2725045f62d1.png`

The respective artifact SHA-256 values are the first hash component after `artifact/`. Sizes were 42,722 bytes for the manifest, 42,930 bytes for JSON, 28,748 bytes for SVG, and 38,420 bytes for PNG.

### Event comparison

The first comparison request represented the returned revision as `{ kind: "revision", revision: ... }` and failed schema validation because `kind` is not accepted in the installed comparison schema.

- Tool status: error before comparison
- Code: JSON-RPC `-32602`
- Exact blocker: unrecognized key `kind` in `before` and `after`

The retry passed `{ revision: ... }` for both sides only to verify that the returned revision was cacheable. It did not claim a source delta.

- Status: `error`
- Code: `EVENT_REVISION_NOT_CACHED`
- Exact blocker: `Requested event graph revision is not cached`
- Artifacts: none

No event comparison evidence was accepted. The revision returned by inspect and render was not cacheable by the comparison route.

## Doctrine and technology MCP evidence

### Folder discovery

The bounded technology call used `mode: folders`, `maxNodes: 40`, no refresh, and the same workspace.

- Status: `ok`
- Code: `TECH_INSPECTED`
- Revision: `2cd542692fe8d08e6b476266374b531d1b69cb55faf0e7ffc40c3b84250da24f`
- Graph hash: `12fffcb622b11ad8625e02bb9a5c77255ab5fad25809ad863352de0747aa7aea`
- Validation: failed
- Validation message: `1421 blocking technology diagnostics; full evidence is linked`
- Structured blockers: none
- Reported counts: 679 technologies, 18 folders, 475 placements, 457 edges, 857 unlocks, 520,298 references, 1,302 issues, and 3 unresolved references

The validation message reports 1,421 blocking diagnostics while the structured count reports 1,302 issues. This audit preserves that server-side discrepancy and does not reconcile the numbers.

Artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a35cb6ed877a7acfd67de92bcf3f138e45a3db5802b40e19ccced6cafea566f/516f5ca567176be31bd601870919aea9c1864fc2d9b29a0110c6461c5a998ff9/technology-folders-2cd542692fe8.json`
  - SHA-256: `7a35cb6ed877a7acfd67de92bcf3f138e45a3db5802b40e19ccced6cafea566f`
  - Size: 371,146 bytes

The artifact resolves the native `land` doctrine folder from `game:common/doctrines/folders/doctrine_folders.txt` and lists `grand_battleplan`, `mass_assault`, `new_mobile_warfare`, and `superior_firepower` as native grand doctrines.

The same artifact resolves `chaos_warfare` as a custom `grand_doctrine` in the `land` folder from `mod:common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`. Its tracks are `armor`, `combat_support`, `infantry`, and `operations`. It resolves `GFX_doctrine_chaos_warfare_medium` to `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`.

### Minimal trace attempts

- `mode: trace` with `folderId: land` failed schema validation with JSON-RPC `-32602` because trace requires `technologyId`.
- `mode: trace` with `technologyId: chaos_warfare` returned status `error`, code `TECHNOLOGY_NOT_FOUND`, and blocker `Technology chaos_warfare was not found`.

The second result is a schema and entity-kind limitation, not evidence that the custom doctrine is absent. Folder discovery identifies it as a grand doctrine rather than a classic technology.

### Doctrine render

The bounded render used `view: doctrine`, `folderId: land`, `maxNodes: 40`, no refresh, and the same workspace.

- Status: `ok`
- Code: `TECH_RENDERED`
- Revision: `2cd542692fe8d08e6b476266374b531d1b69cb55faf0e7ffc40c3b84250da24f`
- Graph hash: `12fffcb622b11ad8625e02bb9a5c77255ab5fad25809ad863352de0747aa7aea`
- Selected nodes: 6
- Omitted nodes: 0
- Focused renders: 0
- Source accurate: `false`
- Validation: failed with the same 1,421-blocking-diagnostics message
- Structured blockers: none

Artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee0958a0d7aebf837a25462f03ce5cfb5de9fbe7c4a499146ed24f1f9e7da77f/5d1913fe19c64d1406b379ca2dc014d6cdae7d37adccddca3a49ddb985bdc7f2/technology-doctrine-2cd542692fe8-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa299ad34357b979a39467fdb303e2ceab2eb818333760ea97e121507a5a6c14/7db7b0ff037792eeff381c9bf5d5847382e52f287b3ca3e7d0e2b5afa1611a41/technology-doctrine-2cd542692fe8.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e540771a6f987640a2ff1ef9b7fed620c48b9e4e4765fd85ee35e5593296ed04/2680c98a33cd2d6b35ad23663fc0042eede4aed4fb6c55226647996141d9be02/technology-doctrine-2cd542692fe8.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7945b2bc3acf4ccc0cace4f91640955341bd003fb622adb74d981c7ca89100c/4760f9e14db6c4579536b0cfd6f9c62777c0bba38b01e4ffd071cc7232255f4c/technology-doctrine-2cd542692fe8.png`

The respective artifact SHA-256 values are the first hash component after `artifact/`. Sizes were 3,149 bytes for the manifest, 2,720 bytes for JSON, 94,955 bytes for SVG, and 46,536 bytes for PNG.

No technology comparison was attempted. There was no changed technology revision or cacheable baseline in this bounded retry.

## Native `add_mastery` one-point source summary

The native effect documentation at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, beginning at line 1477, defines `add_mastery` for country scope. It accepts an amount plus optional `folder`, `grand_doctrine`, `sub_doctrine`, `track`, and `index` filters. Without filters it applies to every active track. The documented example uses `amount = 100` with explicit filters.

Native doctrine data also expresses reward thresholds as raw mastery values, including `mastery = 150` in the sub-doctrine documentation and `mastery = 60` in installed Special Forces reward definitions. Therefore `amount = 1` means one raw native mastery point. It does not mean one mastery reward level and is not documented as one percent.

Event 027 centralizes this amount as `mastery_point_increment = 1` in `common\script_constants\027_doctrine_research_constants.txt` at line 37. The exact adapter beginning at `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt` line 17139 demonstrates the contract. It repeatedly calls filtered `add_mastery` with that one-point amount until the observable mastery reward level reaches the expected next level or the 1,000-iteration guard stops the loop. It then accepts success only when the observed level equals the expected level.

This is a coherent source-level exact-one-level strategy. It is not native runtime proof. No installed vanilla call using `add_mastery` with `amount = 1` was found in the inspected precedents. The source review cannot certify how one-point increments interact with a partially filled threshold, banked mastery, residual mastery after a reward boundary, or Special Forces branch-to-track identity. Those cases require live consumer evidence.

The current receipt recovery source also rereads the native level and requires selected-doctrine activity, stored post-level equality, and observed current-level equality before finalization. That closes the earlier source-level stale-receipt defect. The MCP event calls in this retry disabled helper expansion, so they do not independently certify the helper body or its lifecycle behavior.

## Accepted-plan disposition

- The Event 027 exact native adoption and mastery implementation is present in source and remains classified as source-playable.
- The receipt-recovery reread correction is present in source.
- The prior improvement-loop disposition to stop broad feature expansion remains appropriate. This audit found no basis for another broad design addendum.
- The Event 027 acceptance plan remains open. It has not been promoted to complete because the required engine comparison, source-accurate doctrine proof, runtime mastery scenarios, full probability evidence, and consumer validation are still missing.
- Existing unresolved validation work must remain explicit work, not be hidden as future polish.

## Validation performed and limits

Meaningful validation performed:

- Fresh bounded event lint from `chaosx.nr27.1` with the requested downstream boundary and no helper expansion.
- Fresh bounded event overview render from the same graph revision.
- Cache verification through `event_compare` using the returned revision.
- Doctrine folder discovery covering installed native `land` doctrine data and the custom `chaos_warfare` grand doctrine.
- Doctrine render for the `land` folder.
- Source comparison of Event 027's one-point loop against installed native `add_mastery` documentation, native doctrine reward data, the current exact adapter, and the current recovery guard.

Missing or insufficient validation:

- No accepted event graph comparison because the revision was not cached.
- No helper-expanded Event 027 graph proof.
- No passing event validation result.
- No focused grand-doctrine trace for `chaos_warfare` because the technology trace route only accepts classic technology identifiers.
- No source-accurate or validation-passing doctrine render.
- No technology or doctrine comparison baseline.
- No live proof for low, middle, final, partially filled, banked, empty-track, Special Forces dual-track, Chaos Warfare, queue, tag-switch, or save-and-reload transaction scenarios.
- No fresh probability audit in this bounded engine retry. Existing Event 027 probability acceptance remains unresolved.

## Asset and documentation gaps

No visual asset, portrait, scripted GUI, custom 3D unit, unit audio, or counter production was in scope. No asset handoff was required by this retry. The doctrine artifact resolves the installed Chaos Warfare icon path, but the validation-failing and non-source-accurate render is not final consumer proof.

This handoff is the only file created by the audit. Gameplay, localisation, catalog, specification, and existing handoff files were left unchanged. Existing catalog and completion documentation should retain a needs-testing or partial state until the acceptance blockers close.

## Remaining blockers and recommended next actions

1. Repair or clarify event revision caching in `hoi4_agent_tools`, then rerun the same bounded lint and render and complete an artifact-backed `event_compare` against a real accepted baseline or changed revision.
2. Run a helper-expanded, still bounded Event 027 inspection after the comparison route is usable so transaction helpers and recovery lifecycle can be certified.
3. Add or use an MCP grand-doctrine trace selector for `chaos_warfare`, resolve the technology diagnostics affecting source accuracy, rerender the `land` doctrine view, and compare against an accepted doctrine baseline.
4. Obtain live consumer evidence for exact mastery at low, middle, final, fractional, banked, empty-track, Special Forces, Chaos Warfare, queue, tag-switch, and persistence boundaries.
5. Complete the named Event 027 weighted scenarios through `chaosx_ai_probability_auditor` before final promotion.
6. Reconcile the successful source wiring with event log, details, evolution, catalog, presentation, and acceptance documents only after the required engine and runtime evidence exists.

## Workspace handling

The workspace already contained concurrent changes. They were preserved. This audit did not edit gameplay or localisation and did not create a commit.
