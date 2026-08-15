# Event 010 Death shared dashboard scripted GUI blocker handoff

Date: 2026-08-15

Event: `010`, slug `death`

Status: Blocked before implementation by the mandatory `hoi4.gui_rewrite` recovery gate.

## Event ownership and accepted surface

The inspected UI belongs exclusively to Event 010. The accepted source specification defines both `The Black Atlas` and DTH-only `The Black Ledger` in `docs/specs/010_death_specs/specs/010_death_decisions_ui_ai.md`. The existing Event 010 category file attaches `death_black_atlas_scripted_gui` to `death_country_containment_category`, and the existing scripted GUI owns window `death_black_atlas_container` in `interface/010_death_black_atlas.gui`. The intended recovery would attach the same Event 010 scripted GUI to `death_black_ledger_category`, following the installed vanilla `INS_revolution_scripted_gui` precedent in which one decision-category scripted GUI is reused by multiple categories.

No shared event log, event-details framework, settings UI, super-event framework, registry, unrelated GUI, gameplay effect, cost, AI weight, event, asset, spreadsheet, or binary file was edited.

## Required references inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, including the scripted-GUI action-integrity, text, value, action, background-first, and interactive-design contracts
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- Offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- Required core offline wiki pages named by `AGENTS.md`
- Installed vanilla documentation, including `documentation/script_concept_documentation.md` and `documentation/triggers_documentation.md`
- Vanilla precedent: `common/decisions/categories/INS_decision_categories.txt` and `common/scripted_guis/INS_revolution_scripted_gui.txt`
- Exact Event 010 GUI, scripted GUI, category, scripted localisation, localisation, GFX registrations, and relevant source specification sections

## Pre-change MCP evidence

- Route: `hoi4.gui_inspect`
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Window selector: `death_black_atlas_container`
- Status: `ok`
- Code: `GUI_INSPECTED`
- Shared revision: `3e68c189fd08a879a6826f2a3f33c91ea4ffaa909830e2c7b23fa1e8f079176f`
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f91e24ebed185d48dbdf525147f4cacbfe60e2c02d5e4385cc164a67747a7d9/e8030e1740299dba151314301fe5156404aa5b01dabeede90bf4f280c33069c0/gui-inspect.3e68c189fd08a879.json`
- The inspection resolved the existing 520 by 236 container and its eight elements. It linked the Event 010 layout, scripted GUI, localisation, sprites, animation, decision context, hierarchy, and scenario fidelity data.
- The inspect result also contained repository-wide graph truncation and unrelated collision diagnostics. Those were not treated as evidence against this bounded Event 010 surface.

## Mandatory rewrite attempts and exact blocker

Target source before and after all attempts:

- File: `interface/010_death_black_atlas.gui`
- SHA-256: `db33c8f417752b965531f88f10e330601d7bee4015dbfb533fc9f3cdca4740e3`
- Window: `death_black_atlas_container`
- Mode: exact `patches`
- Intended scalar change: `text = "death_black_atlas_gui_header"` to `text = "death_dashboard_gui_header"`
- Exact scalar byte/character range in the unchanged UTF-8 source: start `587`, end `624`

Attempt record:

1. A token-only range at start `595`, end `623` returned `GUI_UNSAFE_PATCH_RANGE`. The tool required the complete known scalar assignment rather than only the localisation token. This was a patch-shape validation result, not a source change.
2. The corrected complete-scalar request on the same source hash remained active until the tool transport timed out after 180 seconds. The source file remained unchanged.
3. The final complete-scalar exact-patch request on the same unchanged hash returned `status = error`, `code = REWRITE_STRUCTURE_LIMIT`, with blocker message `Rewrite could not be completed`.

Exact blocked route and selector:

- Route: `hoi4.gui_rewrite`
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Window selector: `death_black_atlas_container`
- Relative path: `interface/010_death_black_atlas.gui`
- Mode: `patches`
- Error: `REWRITE_STRUCTURE_LIMIT`

The parent prompt required work to stop if this exact patch returned `REWRITE_STRUCTURE_LIMIT`. No manual GUI, category, scripted-GUI, scripted-localisation, or localisation patch was applied after the blocker.

## Files changed

No runtime or player-facing source file changed.

This blocker handoff is the only file added:

- `docs/plans/010_death_plans/subagent_handoffs/2026_08_15_death_shared_dashboard_scripted_gui_handoff.md`

## Unimplemented accepted design

The following work remains pending and was not simplified:

- Preserve the living Black Atlas while adding DTH visibility to `death_black_atlas_scripted_gui`.
- Attach `death_black_ledger_category` to `death_black_atlas_scripted_gui`.
- Add context-specific visibility triggers for all current Atlas elements and all planned `death_black_ledger_*` elements.
- Keep the shared background and animated header, with a context-sensitive title.
- Add the four-value DTH hierarchy: available Soul Power, Spread Pressure, Consumed States, and Consumed Population.
- Add three informational, non-clickable route/status modules: Island Spread, Mainland Route, and Ghost Hosts, using the approved existing Event 010 animated/static sprite families.
- Move generated/spent soul detail, island/mainland subcounts, watch-network values and surcharge, cost ladder, source formula, and host counts into concise hover/tooltips.
- Reduce `death_black_ledger_category_desc` to a one-to-three-line in-world introduction.
- Preserve all living Atlas localisation and behavior.
- Run post-change `hoi4.gui_inspect` and the required living/DTH `hoi4.gui_render` scenario matrix at 1920 by 1080, 1600 by 900, and 1366 by 768 with UI scale 1.0, including normal, warning, minimum, maximum, long-text, hierarchy, click-region, resolution, and comparison evidence.

## Planned layout and budgets pending implementation

The accepted plan remains:

- Background coverage: shared 520 by 236 map board and header remain visible. The header carries the context title. The upper/middle map anchors carry one primary value block and three compact status modules. Supporting values occupy compact aligned readouts. Lower map space preserves the existing footer/negative-space rhythm without fake controls.
- Visible value budget: one primary value plus three supporting values, four total and at the hard ceiling.
- Action budget: zero GUI actions and zero GUI missions. Normal decisions remain below the category.
- Cost-count audit: no spendable cost is displayed as a GUI action. Exact decision costs remain in decision surfaces and informational tooltips.
- Texticon coverage: no new GUI spend action was planned. The blocked implementation never introduced a literal resource-name cost fallback.
- State matrix pending render: living Atlas with forbidden values hidden/shown, DTH low/locked, island-ready, mainland-ready, watch-network blocked, weak hosts, hollow hosts, Last Shores/world-end, maximum numeric, and long text.

## Skipped meaningful validation

Post-change inspect, render, hierarchy, click-region, state, resolution, and before/after comparison validation could not be run because the mandatory rewrite gate failed before any source change. Live consumer and in-game validation remain parent-owned and were not attempted.

## Remaining risk and parent follow-up

The Event 010 Black Ledger remains the existing dense category description. The accepted shared-container implementation is not present. This is a tooling blocker, not an approved fallback or feature simplification.

Parent follow-up should resolve or update the `hoi4.gui_rewrite` structural-limit behavior for exact scalar patches on `interface/010_death_black_atlas.gui`, then reroute the unchanged accepted implementation with the same bounded identifiers and files. Do not manually bypass the mandatory MCP rewrite requirement without explicit user direction.
