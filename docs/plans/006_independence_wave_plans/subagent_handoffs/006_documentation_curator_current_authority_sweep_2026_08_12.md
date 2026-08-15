# Event 006 documentation curator handoff — current authority sweep (2026-08-12)

## Scope and outcome

This was a documentation-only reconciliation of Event 006 current authority, package-count wording, deterministic Join order, automatic ladder claims, dated snapshots, prompts, and handoff references.

The authority at the time of this dated sweep was 29 content-attested selectable packages across 26 compatible reservation groups, 164 unattested selectable rows out of 193 non-overlay rows, and 37 runtime package adapters. The later IW-040 promotion supersedes those counts for current routing.

The dated pre-IW-040 Join order placed IW-038 immediately before IW-033: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184. The current order additionally inserts IW-040 after IW-038.

The active automatic ladder is 3/4/5/7/10, with World Collapse also targeting 10.

The whole-event disposition remains HOLD / PARTIAL; this handoff makes no gameplay completion claim.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Event-wide package counts, admitted IDs, ladder, and IW-038 promotion | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` top override and 2026-08-10 continuation | Current source of truth |
| Event implementation-facing overview | `docs/events/006_independence_wave/overview.md` current package authority and package-admission override | Current, aligned |
| Resume state | `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` 2026-08-10 authority override | Current, aligned |
| Deterministic Join order and settled retry evidence | `docs/events/006_independence_wave/join_wave.md` and `subagent_handoffs/006_join_wave_settled_filesystem_audit_2026_08_09.md` | Current, with live execution still unclaimed |
| Accepted design | `docs/specs/006_independence_wave_specs/` | Accepted source specification; not edited |
| Regional package details | `docs/events/006_independence_wave/*.md` | Current package mechanics retained; dated arithmetic explicitly marked below where needed |

## Files changed

- `docs/events/006_independence_wave/karelia_crimea_packages.md`
- `docs/events/006_independence_wave/banat_package.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- This handoff file.

No gameplay, localisation, spreadsheet, asset, accepted-specification, or prompt file was changed.

## Patches and dispositions

The Karelia/Crimea regional document now carries a 2026-08-12 supersession note, labels its 2026-08-06 source section historical, describes its 24/22/169 and 23/22/170 arithmetic as dated evidence, and pointed routing at that time to the 29/26/164/37 IW-038 authority.

The Banat package document now labels its 24/22/169 package audit dated and pointed the dated whole-event routing to the 29/26/164/37 authority and 3/4/5/7/10 ladder.

The source-of-truth map's 2026-08-06 IW-029 amendment is now explicitly historical and superseded by the 2026-08-10 IW-038 promotion; its 23/22/170 and 32-adapter values remain unchanged as dated evidence.

The accepted specifications, resume packet, overview, Join document, and current prompts were already aligned and were left unchanged.

| Plan or handoff class | Disposition | Evidence |
| --- | --- | --- |
| IW-038 Ruthenia promotion | Current and implemented at source level; whole-event completion remains open | Current source-map, overview, resume, and IW-038 audit references |
| Join retry and deterministic order | Current source-patched evidence; live runtime/save-load validation unclaimed | `006_join_wave_settled_filesystem_audit_2026_08_09.md` and revision `53a767c5012bf86517e556e90f78047efea681342277a5d2813f07ffef0c5f15` |
| Older 2026-08-06 and earlier package-count amendments | Historical evidence retained and superseded for routing | Explicit historical headings in source map, overview, resume, and regional docs |
| Accepted specs and prompts | Left unchanged; no stale active package count or ladder claim found | `docs/specs/006_independence_wave_specs/` and prompt subdirectory |
| Unresolved handoffs | Retained as evidence, not promoted to completion | Probability, live runtime, audio, formable reachability, and asset caveat handoffs |

## Contradictions resolved

The unmarked “current” 24/22/169 and 23/22/170 claims in `karelia_crimea_packages.md` were converted to dated/historical wording.

The unmarked “current” 24/22/169 claim in `banat_package.md` was converted to dated wording with an explicit current-authority pointer.

The unmarked “Current package-admission amendment” heading and current-tense 23/22/170 claim in the source-map IW-029 tail were converted to a historical amendment superseded by IW-038.

No contradiction remained in the top-level authority sections inspected at this dated pass: they used 29/26/164/37, IW-038 immediately before IW-033, and 3/4/5/7/10 with World Collapse 10. The later IW-040 promotion supersedes those counts and inserts IW-040 after IW-038.

## Remaining historical contradictions and stale-looking evidence

The overview, resume packet, source map, accepted quality notes, and older handoffs intentionally retain 6/8/10/14/20 ladder snapshots, 28/25/165, 24/22/169, 23/22/170, 21/20/172, and earlier adapter counts for dated traceability.

Those values are not current contradictions where the surrounding heading or paragraph says historical, superseded, dated, or snapshot; they must remain unchanged unless the parent wants an archival rewrite.

The accepted package specification still contains historical amendments alongside the current 2026-08-10 override; it was intentionally not edited because accepted specs are outside this sweep's patch authority.

The scenario registry documents 149 publishers, 138 bound rows, 55 unbound rows, and 13 overlays, while the country API documents carrier collections; these are different registry surfaces and must not be normalized to package-admission counts.

## Duplicate and superseded document assessment

The source map, overview, and resume packet are complementary rather than duplicates: the source map records authority and evidence precedence, the overview maps implementation surfaces, and the resume packet preserves continuation state.

Older package-specific handoffs remain useful evidence for mechanics and limitations and were not deleted.

The dated IW-029 tail in the source map and dated regional arithmetic are now explicitly superseded rather than removed.

## Prompt and instruction audit

No active prompt under `docs/specs/006_independence_wave_specs/prompts/` asserted the stale 23/22/170 or 24/22/169 package boundary.

The goal and coding prompts already state the active 3/4/5/7/10 ladder and World Collapse 10.

The routing prompt's older package wording is framed as a historical work-item note and was left unchanged.

## Markdown hard-wrap audit

The touched files retain one-line prose paragraphs after the patches.

Broader Event 006 documentation still contains historical mid-sentence physical wraps, notably `docs/events/006_independence_wave/evolutions.md`, `docs/events/006_independence_wave/form05_mediterranean_island_league.md`, `docs/events/006_independence_wave/generic_ai.md`, `docs/events/006_independence_wave/mediterranean_island_packages.md`, and `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`.

Those broad reflows were not patched in this bounded authority sweep because they span concurrent work and deliberate historical/table structure; a follow-up documentation-only pass can normalize them after the parent freezes the worktree.

## MCP artifact-manifest limitations

The current Join MCP evidence is recorded as a partial workspace projection at revision `53a767c5012bf86517e556e90f78047efea681342277a5d2813f07ffef0c5f15`; it is not a live-game transaction, save/load, or runtime artifact receipt.

The grouped GUI inspection is an external `hoi4-agent://` artifact URI with aggregate overlap and unresolved-context diagnostics, so family-isolated visual acceptance remains bounded.

The documented probability routes report `PROBABILITY_SURFACE_EMPTY` for BOS, AXX, and MAC strategy surfaces, an internal error for the BAX decision adapter, and missing typed KAR/CRI scenario/compare evidence; no quantitative AI-balance claim is promoted.

The repository does not expose a durable local artifact manifest enumerating every MCP event, GUI, probability, and runtime receipt. A fresh read-only `hoi4.event_inspect` scan for workspace `mod_chaos_redux_ea3b2d67c2c0` returned `ARTIFACT_MANIFEST_INVALID` with no artifacts or files scanned, so no new MCP artifact receipt could be generated during this sweep. Parent review must preserve the external artifact URIs and their limitations rather than treating source-map references as live engine proof.

## Recommended parent decisions

For the dated pre-IW-040 pass, keep the 29/26/164/37 and 3/4/5/7/10 wording as historical traceability; the later IW-040 30/27/163/38 authority is also superseded, and current routing uses the IW-044 31/28/162/39 authority.

Leave dated 6/8/10/14/20 ladder and earlier package arithmetic snapshots intact for provenance, with their explicit historical labels.

Decide separately whether to run a later hard-wrap cleanup after concurrent documentation edits settle.

Do not claim whole-event completion until live transaction, save/load, typed probability, formable reachability, and super-event 23 audio/firing evidence are independently closed.

## Validation performed

Targeted `rg` checks confirmed that the touched regional docs and source-map tail now use explicit historical wording and point current routing to the IW-038 authority.

Targeted reads confirmed current counts, Join ordering, ladder values, accepted-spec overrides, and prompt wording before patching.

No gameplay or spreadsheet validation was run because this handoff changed documentation only. The required read-only Event 006 MCP route was attempted and blocked by the exact `ARTIFACT_MANIFEST_INVALID` result above.
