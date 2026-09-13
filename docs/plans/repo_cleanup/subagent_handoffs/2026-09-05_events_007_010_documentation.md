# Events 007 to 010 documentation review

Date: 2026-09-05.
Disposition: implemented for the four overview repairs, with the acceptance and validation limits below.
The [central cleanup record](../documentation_state.md) owns the broader task.

## Reading and ownership

Curator `events_007_010_docs_c03` fully read the four originals before any edits and returned a read-only closeout without writing files.
The parent independently fully read all four, reviewed the source discrepancies, applied the repairs, and wrote this handoff.
The curator reports full prerequisite reads of the request, AGENTS.md, subagent and event skills, eleven required offline wiki pages, and eleven vanilla documentation files.
It also reports full reads under `docs/specs/007_fury_specs/`, `008_tensions_rising_specs/`, `009_white_peace_specs/`, `010_death_specs/`, and `docs/plans/007_fury_plans/`, `008_tensions_rising_plans/`, `009_white_peace_plans/`, `010_death_ghost_hosts_plans/`, and `010_death_plans/`.
Those dependency reads do not constitute reconciliation or current implementation acceptance for every interior document.

| Fully read original | Bytes | SHA-256 | Disposition |
| --- | ---: | --- | --- |
| `docs/events/007_fury/overview.md` | 19462 | `a5c6d7393550feb868f42541af27b6ac796ea8fd1037b0741e47026885f30494` | Implemented overview repair |
| `docs/events/008_tensions_rising/overview.md` | 9362 | `839e719245713ff10e6a6f4b6781bfabd5763e7b000765dcb5caf03e4387edef` | Implemented overview repair |
| `docs/events/009_white_peace/overview.md` | 10076 | `01df00f04114bb51c03906306f89cc0278cfcdfbfceb652cbbd88ca897b98924` | Implemented overview repair |
| `docs/events/010_death/overview.md` | 22426 | `01ca80bd7208da6241224f93734fa57c8926958978e689502174fdba4b04c670` | Implemented overview repair |

## Repairs and retained evidence

- Fury: removed only literal duplicate WAV and recommended-asset entries, retaining both audio IDs, every unique asset path, every consumer, and the historical lighter 5% modifier value.
- Tensions Rising: retained the canonical Diplomacy identity and historical Diplomatic Panic aliases without promoting old naming as a new design decision.
- White Peace: corrected the helper index and opening description to distinguish report dispatch from option-applied settlement. Narrow reads show `chaosx.nr9.1` calling `fire_white_peace_report_event`, report options `.2` through `.5` calling `apply_white_peace_current_context`, and the latter owning settlement. The original presentation sentence is preserved below.
- Death: clarified that the text-value Atlas source includes its background and animated header. Kept the absence of a separate close control and decorative status icons distinct from that header. Kept the existing living-country Atlas separate from the shared Atlas and Black Ledger extension recorded as blocked in its historical handoff.
- All four: repaired sentence punctuation, linked this evidence boundary, retained gameplay quantities and stable identifiers, and labelled future proposals as unresolved rather than implicitly authorized.

Original White Peace presentation statement:

> The event is intentionally quiet: the popup has one acknowledgement option, and the settlement has already been signed.

The inspected implementation executes settlement from the acknowledgement option.
This source observation does not settle whether the original presentation intent requires a separate gameplay change.

## Archive checks

`docs/assets/007_fury/achievement_icons/manifest.md`, `docs/assets/008_tensions_rising/`, and `docs/assets/009_white_peace/` are absent.
Git records their deletion in `87d441ac758d515e1abca34167fcd45b51acf028`.
The absent `docs/assets/010_death/generated_art_manifest.md` was deleted in `487670dee3722238dadc218a30d84c59aa27594a`.
The overviews retain each original path and distinguish historical source material from runtime registration.
No replacement source archive was verified and no asset was recreated or removed.

## Source and MCP evidence

The parent fully read `interface/010_death_black_atlas.gui`, `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`, and `docs/plans/010_death_plans/subagent_handoffs/2026_08_15_death_shared_dashboard_scripted_gui_handoff.md`.
The White Peace event/effect checks and Death GFX declarations were narrow source excerpts, not complete file reads.
The old handoff's `REWRITE_STRUCTURE_LIMIT` concerns the proposed shared Atlas and Black Ledger extension.
It does not prove that the existing living-country Atlas is missing.
The user-supplied AGENTS.md on 2026-09-06 makes `gui_rewrite` optional and permits direct application of an authorized reviewed edit.
The historical transaction failure alone is therefore no longer a current implementation gate or a reason to request fallback approval.
The extension and its required inspect, render, and matching before-and-after evidence remain outside this documentation task.

Curator Event 007 trace: `EVENT_INSPECTED_PARTIAL`, focused analysis, graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e`.
Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19c749ffead2543396ba4418f5f901875c643aae5324e4da64bc6bb4331056a7/90cb42a9948a6f7e60af5a1f35b6ba7b7982f0654aaff3072a95edc318066bca/event-trace-1102e50fad94.json`

Parent Event 009 trace: selector `{kind: "event", eventId: "chaosx.nr9.1"}`, depth 2, maximum 12 nodes and 24 edges, helper expansion disabled.
The first request omitted `selector.kind` and was rejected by argument validation.
The corrected request returned `EVENT_INSPECTED_PARTIAL`, revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, with deferred workspace-wide helper and lifecycle projections and validation false.
Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd01db90176c7ac14ed5cdd748268ac1ed0811b9afd343eec0d972f1550bf7e3/9b98e5b9a3f0c6eae1a934d66f93dccf7ee7ab68cd6c3f6c31a61e4ba1cf33eb/event-trace-1102e50fad94.json`

Parent Black Atlas inspection: `death_black_atlas_container`, scenario `{id: "documentation_death_black_atlas_revealed", state: "normal"}`, generated scenarios disabled.
It returned `GUI_INSPECTED`, complete source graph, eight inspected elements, and no blocking source-graph diagnostics at revision `7e2c0520e78e924f209d3ad43cc0f9e4a7cc4c80b847afe3daa7f7afbf7dbacb`.
Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/502c86f7ae373e7729203276fa3bc89e138652de44e3a2378f6dc63b6e230b67/10363854efd7d091d81a174f5997af2c86d299f08cbcd0b53cf2f813498b5f80/gui-inspect.7e2c0520e78e924f.json`

The same result reports seven overlap findings, unresolved dynamic text, an unresolved static-fallback link for the header, missing source-manifest provenance, and footer text measuring 473 by 32 inside 478 by 22.
Fidelity counts are 85 modelled, three approximated, and four unresolved.
These findings remain owner follow-ups and are not dismissed as renderer discrepancies.
The parent reviewed the structured summary and diagnostics, not the complete linked bulk artifacts.
No matching render, full fixture matrix, before/after comparison, probability audit, GUI rewrite, or live-game validation was performed.
No current event-wide or GUI-wide completion claim follows.

## Remaining scope

Source archives remain missing, original presentation intent and future proposals remain unapproved here, and the documented GUI defects and shared-dashboard extension remain outside the authorized documentation edits.
No gameplay, localisation, asset, workbook, or protected configuration changed.
No design simplification or fallback was introduced.
Skills used: `chaos-redux-subagents`, `chaos-redux-events`, and the existing scripted-GUI evidence workflow for the read-only Atlas inspection.

## Commit isolation

The original Fury and Tensions Rising working copies contained uncommitted cluster-contract changes absent from tracked source.
The commit excludes Fury's added two-row cluster paragraph and Tensions Rising's new Diplomacy membership paragraph and related future-membership wording.
The working tree retains those inherited changes.
One punctuation repair inside the inherited Diplomacy paragraph stays with that uncommitted work.
The commit does not certify the older tracked cluster wording as the current accepted contract.

The reviewed changes are preserved on `codex/documentation-cleanup-review-20260906`.
Integration into the shared working branch remains pending because its Git index lock is owned outside this task.
See the central cleanup record for the selective manifests and integration boundary.
