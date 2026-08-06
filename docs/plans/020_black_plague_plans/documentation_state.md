# Event 020 documentation state

Date: 2026-08-06

This ledger is the current documentation source map for Event 020 after the shared rat model handoff and the national-focus MCP inspections. It reconciles documentation only and does not claim gameplay, sound, counter, GUI, or live in-game completion.

## Accepted current invariants

- Runtime country identity is exactly two tags: reusable Rat Nation `RTA` and separate Rat King `RTX`; internal broods remain state markers, basin values, infestation, mass, and army-pulse state inside `RTA`.
- `RTA` currently has 52 focus blocks and `RTX` has 71 focus blocks in the live source files, confirmed by the 2026-08-05 national focus MCP inspections.
- The shared rat model package registers `black_plague_rat_mesh` and `black_plague_rat_entity` and is consumed by six RTA/RTX subunits and five locked division templates; it intentionally does not provide per-subtype or separate Rat King models.
- The model worker package is production-complete at its worker/evidence boundary, while parent-owned sound definitions, sound-source acceptance, counter visual review, final runtime wiring review, and live in-game model playback remain open.
- The model handoff records 29,999 triangles, 15,012 vertices, 17 bones, five skeletal actions, PdxMeshAdvanced 1024-pixel maps, reimport evidence, runtime hashes, and one shared entity scale of 1.35; these facts are evidence from the handoff, not a replacement for live validation.
- `SCN-012` remains the accepted triggerable scenario and its repeat behavior is reconciliation-only and idempotent; the source and handoffs do not prove complete journaled rollback after downstream mutation failure.
- The Diseases cluster remains `8`, the public Event 020 world-end row remains registered, and workbook/CSV ownership remains with the spreadsheet worker and parent agent; this curator did not inspect or edit the workbook.
- The Event 020 layout audit records 52 RTA focuses, 71 RTX focuses, and authored local geometry without Event 020-owned focus collisions; generic vanilla palette diagnostics remain outside the Event 020 package.
- The shared disease GUI header has a bounded MCP inspection artifact with seven inspected elements, but global diagnostics, inline-source truncation, and missing/unsupported scripted context prevent a GUI completion claim.
- Event MCP inspection was attempted twice for `chaosx.nr20.1` and timed out after 180 seconds each time; source-only review is not equivalent to event MCP evidence.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted design | `docs/specs/020_black_plague_specs/` and the 2026-07-29 two-tag correction | Accepted source specification; old planning alternatives remain historical. |
| Runtime summary | `docs/events/020_black_plague/overview.md` | Updated to 52/71 and the shared model/entity runtime handoff; live validation remains open. |
| Asset requirements | `docs/specs/020_black_plague_specs/matrices/asset_inventory.md` | Updated with the shared model package, six subunit consumers, five locked templates, and review-gated status. |
| Focus layout | `docs/plans/020_black_plague_plans/2026-08-05_focus_gui_mcp_layout_audit.md` | Current layout evidence; this pass does not modify its bounded GUI or focus geometry. |
| Rat route behavior | `docs/events/020_black_plague/rat_route_depth.md` and `docs/systems/black_plague_rat_route_modules.md` | Updated to consume the shared model package without adding route-specific models. |
| Rat King route | `docs/events/020_black_plague/rat_king_depth.md` | Updated to reuse the shared model package and preserve the no-separate-King-model boundary. |
| Model production | `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-05_event020_rat_shared_3d_model_handoff.md` and `docs/plans/020_black_plague_plans/rat_ground_unit_shared_3d_model_brief.md` | Promoted worker/runtime evidence; parent-owned sound, counter, and live validation remain open. |
| Scenario behavior | `docs/plans/020_black_plague_plans/2026-08-02_event20_scenario_content_handoff.md` and Part 9 | Accepted two-tag/idempotent contract; no rollback completion claim. |
| Package review | `docs/specs/020_black_plague_specs/review/` | Updated count/model facts and explicit live-validation limits. |
| Catalog | `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md` plus the authoritative workbook | No workbook change in this pass; parent/spreadsheet worker owns any row update and export. |

## Plan and handoff disposition

| Plan or handoff | Disposition | Reason or remaining work |
| --- | --- | --- |
| `rat_ground_unit_shared_3d_model_brief.md` | Promoted to the 2026-08-05 worker package | Shared model/entity design is accepted for six subunits and five locked templates; no per-subtype or Rat King model. |
| `2026-08-05_event020_rat_shared_3d_model_handoff.md` | Current implementation evidence | Worker package and static runtime registration are recorded; sound-definition wiring, counter review, and live model playback remain open. |
| `2026-08-05_focus_gui_mcp_layout_audit.md` | Current bounded layout evidence | RTA/RTX counts are current; GUI and generic MCP diagnostics remain unresolved. |
| `2026-08-02_event20_documentation_reconciliation_handoff.md` | Superseded for current counts and model status | Its 51/71 and no-model claims remain archive provenance only; this ledger and the 2026-08-06 handoff control current facts. |
| `2026-08-01_event20_content_tranche_handoff.md` | Historical gameplay tranche with current override | It did not modify the separately promoted model package; its old 51/70 and no-model body claims are superseded. |
| `2026-08-01_event20_consequence_and_aftermath_addendum.md` | Historical addendum with current override | Its two-tag/no-model boundary is replaced by the two-tag/shared-model boundary; route and live-validation findings remain useful. |
| `2026-07-29_event20_core_readiness_report.md` | Historical baseline with current override | Gameplay tranche evidence remains useful, but 52/71, shared model status, sound/counter review, and live validation now control. |
| Older subagent handoffs and prompts | Archive-only unless their notice points to current docs | They preserve earlier audit evidence and must not be used to revive multi-tag, 51-focus, or blanket no-model instructions. |
| Event catalog workbook and exports | Unchanged and parent-owned | This curator did not read or edit spreadsheet files; any catalog wording update belongs to `chaosx_spreadsheet_doc_worker`. |

## Contradictions resolved

- Active specs, event docs, reviews, prompts, and current plans now state 52 RTA focuses and 71 RTX focuses instead of the former 51/71 or 51/70 convention.
- Active docs now distinguish the promoted shared model/entity package from rejected per-subtype and separate Rat King models.
- Active docs now distinguish worker/static runtime evidence from parent-owned sound definitions, counter review, and live in-game proof.
- The 2026-08-05 layout audit is scoped to focus/GUI layout and no longer reads as evidence that the shared model package does not exist.

## Contradictions still open

- The event-scoped Event 020 source/provenance workspace has been restored from the repository for the report, decision-art, portrait, and source-frame records; the separate worker evidence directory `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/` is still not present, so provider-output retention remains unverified.
- Sound candidates remain `needs_user_review`; no accepted impact/contact source and no parent sound-definition wiring or live playback proof is recorded.
- Bespoke counters are installed according to the model handoff but remain review-gated; no live counter visual validation is claimed.
- `hoi4.event_inspect` timed out twice, so Event 020 event-level MCP evidence is unavailable for this pass.
- Focus MCP returned 14 generic vanilla continuous-focus palette diagnostics per tree, plus Event 020 layout-detour warnings; no Event 020-owned blocking reference or geometry issue was reported.
- GUI MCP returned a bounded header artifact but also inline-source truncation, missing/unsupported scripted-context diagnostics, and global overlaps outside the bounded header; full board rendering remains unavailable.

## Stale prompts and documents

- The active coding, goal, and decision/mission prompts now point to the shared model handoff and mark old no-model prose as historical.
- Historical handoffs that still contain blanket no-model or old-count statements are listed in the disposition table and remain archive-only; the parent should not use them as implementation instructions.
- The untracked 2026-08-06 completion-audit handoff from another audit pass is a pre-cleanup snapshot where it says active docs remain stale; this ledger and the dated cleanup handoff supersede that snapshot after the listed patches.

## Markdown hard-wrap audit

- Newly added and directly patched prose in this reconciliation uses one physical line per sentence and preserves headings, list items, tables, and code spans.
- Existing historical plan prose contains intentional or inherited mid-sentence wraps, especially in the core-readiness report and older handoffs; those archive bodies were not flattened because doing so would alter audit provenance. The parent may normalize them in a separate documentation-only pass.
- No hard-wrap correction was applied to gameplay, localisation, GUI, GFX, asset, or spreadsheet files.

## Parent decisions and resume actions

- Decide whether the absent temporary model evidence directory is intentionally archived elsewhere or should be restored from the retained handoff evidence; do not infer that its absence invalidates the installed runtime package.
- Complete parent-owned sound-definition wiring only after accepting the licensed candidates or recording a blocked role; do not synthesize or silently substitute sounds.
- Visually review the bespoke counter package and retain the review result in the durable model handoff before claiming counter completion.
- Run the user-owned live HOI4 model, counter, mission, scenario, event, and GUI validation passes; preserve the explicit MCP timeout and GUI diagnostics in the final report.
- Route any catalog wording update through the authoritative workbook and export tool after gameplay facts are final.
