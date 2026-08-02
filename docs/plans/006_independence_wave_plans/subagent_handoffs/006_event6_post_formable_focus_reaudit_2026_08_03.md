# Event 006 post-formable and focus-reflow completion re-audit

Date: 2026-08-03.

Scope: read-only completion re-audit after commits `ca42ad22e`, `e86b3c183`, `0ea6a3ff0`, `e802923e8`, and `b4e883285`, with the later documentation-only reconciliations visible at audit time. This handoff does not edit gameplay, localisation, assets, the workbook, or existing authority documents.

## Verdict

Event 006 remains **HOLD / PARTIAL** as a whole.

The prior P0 clean-checkout formable-mirror defect is **CLOSED**. The prior P5 focus-layout diagnostic is also **CLOSED** as a geometry defect. The focus reflow introduces a narrower design and validation gap: 35 visible prerequisite blocks were converted to hidden `available` gates. This preserves focus eligibility but changes player-facing dependency presentation and removes the engine's documented implicit AI preference boost for focuses whose direct prerequisite was just completed.

## Completion status by surface

| Surface | Status | Current evidence |
| --- | --- | --- |
| Vanilla CHU/ASY formable guard ownership | **PASS / CLOSED** | The full vanilla mirror is tracked at `common/decisions/formable_nation_decisions.txt`; the deleted narrow compatibility adapter is no longer the clean-checkout owner. |
| Vanilla mirror fidelity | **PASS / CLOSED** | After removing the three Event 006 guard lines and ignoring blank-line placement, all 16,119 nonblank lines match the installed vanilla file in exact sequence. |
| Event 006 guard predicates | **PASS / CLOSED** | CHU is guarded once and ASY twice. The scripted guards resolve to the exact IW-043 or IW-058 package, original-tag, Event 006 origin/state, and Soviet Collapse exclusion predicates. |
| Generic focus geometry | **PASS / CLOSED** | Fresh inspect/render: 184 nodes, 186 visible connectors, zero crossings, zero node intersections, zero long connectors, and zero too-close same-row pairs. |
| Focus eligibility after reflow | **BOUNDED PASS** | Removed direct prerequisites are represented by hidden `available = { has_completed_focus = ... }` gates, including capstone OR paths. This preserves completion eligibility under the documented engine distinction. |
| Focus player presentation | **PARTIAL / DESIGN GAP** | Thirty-five visible prerequisite blocks are now hidden availability gates. Their connector lines and prerequisite-group tooltip presentation are absent by design. Two route-choice focuses consequently remain renderer-isolated. |
| Focus AI equivalence | **PARTIAL / VALIDATION GAP** | The source `ai_will_do` blocks remain, but converting direct prerequisites to availability gates removes the documented 1.5 generated-AI-value multiplier that applies when a focus's prerequisite was just completed. No compensating factor or explicit acceptance is recorded. |
| Package capacity and admission | **HOLD** | Fourteen packages are attested; 179 non-overlay registry rows remain unattested and 55 selectable rows remain unbound. No accepted synchronized disjoint witness closes the 14- or 20-country modes. |
| Formable availability | **HOLD** | The compatibility source is fixed, but only 11 of 48 registry formable families are readiness-allowlisted. Package, identity, member-adapter, and source-proof gates still block multiple families. |
| Super-event 6001 | **BLOCKED** | Art exists, but no complete runtime dispatch/localisation/audio/WAV/wrapper/firing package is accepted. Audio remains rights-blocked. |
| Super-event 6002 | **PARTIAL** | Runtime wiring exists, but its hidden-formable and 20-country paths inherit unresolved formable and capacity blockers. |
| AI and balance | **PARTIAL** | Probability discovery is bounded, generic `ai_strategy_factor` evidence remains unresolved, no final whole-event balance acceptance exists, and the reflow adds the AI-weighting gap above. |
| Assets and source proof | **PARTIAL / BLOCKED** | Unattested packages and named formable families retain source, identity, flag, portrait, or member-adapter blockers. The accepted zero-advisor-icon boundary is not itself a blocker. |
| Catalog and current documentation | **PARTIAL / STALE** | Workbook/export statuses remain partial/playable rather than complete. Current routing documents were updated for the clean focus geometry, but historical/current-authority rows still preserve pre-reflow figures and none disclose the 35-gate presentation/AI consequence. |

## P0 closure evidence: vanilla formable mirror

The current tracked mirror contains exactly three Event 006 additions:

- `can_access_vanilla_chu_formable_shortcuts = yes` at mirror line 13,965;
- `can_access_vanilla_asy_formable_shortcuts = yes` at mirror lines 17,495 and 17,701.

The Event 006 trigger owner is `common/scripted_triggers/006_independence_wave_vanilla_formable_compatibility_triggers.txt`. Its CHU and ASY guards exclude only the exact Event 006 IW-043 and IW-058 package countries. The package predicates in `006_independence_wave_iw043_iw058_package_triggers.txt` require the expected original tag, active Event 006 package identifier and package flag, Event 006 liberation origin, and exclusion of the Soviet Collapse origin.

The installed vanilla file has 18,573 physical lines and the mod mirror has 18,574. Removing the three guards and normalizing trailing whitespace leaves only two blank-line placement differences; removing blank lines yields exact equality across all 16,119 nonblank lines. This independently substantiates `006_vanilla_formable_compatibility_reconciliation_2026_08_02.md`.

Disposition: `ca42ad22e`, `e86b3c183`, and `0ea6a3ff0` fully promote the accepted guard-ownership repair. The former P0 is not a remaining clean-checkout blocker.

## P5 closure evidence: generic focus geometry

Fresh `hoi4.focus_inspect` and `hoi4.focus_render` evidence against the current `independence_wave_focus_tree` reports:

- workspace `mod_chaos_redux_ea3b2d67c2c0`;
- layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`;
- 184 regular nodes and 186 visible connectors;
- bounds `x = 1..121`, `y = 0..19`;
- minimum same-row spacing 2;
- maximum horizontal span 7, vertical span 3, and Manhattan span 9;
- zero crossings, node intersections, long connectors, and too-close same-row pairs.

The current render artifact hashes are:

- HTML: `179044a1f79cadc1604bb667cb61e699947d8f664b902ab6b367e34b765c4c15`;
- SVG: `77a0a7857e0e6191a01c76de96d7177deb808a07996bb75bc67a7a69362bc6c7`;
- JSON: `de3265bd27665de9f3e54b86916914f8b5b742575036f42110da1cae0205a9c9`;
- quarter-scale PNG: `fbd7d53d681772259013ff59e76ad10a60d64ce434691ec7dc89822268a2f0b7`, 5,356 by 610 pixels, 166,131 bytes.

The two remaining Event 006 warnings are intentional `FOCUS_ISOLATED` warnings for `independence_wave_standardize_with_league` and `independence_wave_preserve_independent_command`. Both are hidden-gated from `independence_wave_adopt_military_archetype_program`, mutually exclusive, and consumed by the capstone's hidden OR gate.

The tool's overall validation flag remains false because the installed vanilla continuous-focus palette contributes fourteen missing-icon errors and one localisation warning. Those diagnostics do not reference Event 006 assets or nodes and are not Event 006 blockers.

Disposition: `e802923e8` and `b4e883285` close the former crossing/intersection/connector-span diagnostic. `006_focus_geometry_reflow_parent_2026_08_02.md` is substantiated for raw layout metrics.

## New focus reflow design and validation gap

The reflow removes 35 visible `prerequisite = { ... }` blocks and replaces their dependency tests with hidden `available = { has_completed_focus = ... }` gates. No new visible prerequisite block replaces those 35 groups.

The offline National Focus modding reference documents that a completed-focus check in `available` can enforce the same eligibility condition as `prerequisite`, but the two forms differ in rendered prerequisite lines and tooltip grouping. The same reference documents a generated AI-value multiplier of 1.5 for a focus whose prerequisite has just been completed. The reflow therefore has two consequences beyond geometry:

1. Players no longer receive visible connector-line and prerequisite-group presentation for those 35 groups.
2. The former child focuses no longer receive the implicit 1.5 just-completed-prerequisite AI preference through those edges.

The existing handoff states that source AI hooks and route eligibility are preserved, but it does not record either consequence. This is not evidence that route availability broke; it is evidence that presentation and AI behavior are not equivalent to the pre-reflow contract.

Recommended disposition: accept the geometry closure while keeping focus completion **PARTIAL** until the parent either:

- explicitly accepts and documents the hidden-dependency presentation and AI-weight change; or
- restores a minimal visible prerequisite spine compatible with clean geometry and adds explicit AI weighting where hidden edges remain.

## Meaningful task-specific validation

The following current static audits pass:

- allocator audit: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages across 13 compatible groups, pair capacity 2 for RHI/IW-008 and AJX/IW-010, and ladder 6/8/10/14/20 with World Collapse at 20;
- SCN-008 scenario audit: all 32 matrix cells and eight edge cases;
- Statehood Ledger GUI audit: five tabs, five recognition frames, three dependency frames, four league frames, four formable frames, cleanup coverage, and four static/animated pairs;
- protected-tag surface scan: 136 protected tags, zero external country-definition collisions, and zero external identity-surface collisions, with the documented Random Events root skipped.

These are source/static receipts. They do not substitute for the missing package-capacity witness, package admission, formable readiness, asset/source proof, 6001 runtime/audio package, final AI/balance acceptance, or player-owned live observation where the controlling specs require it.

## Accepted-plan disposition

| Accepted item | Disposition |
| --- | --- |
| Track a single full vanilla formable mirror with three narrow guards | **Implemented and promoted.** Clean checkout now reproduces the intended CHU/ASY guard behavior. |
| Remove the separate narrow compatibility adapter | **Implemented and promoted.** No duplicate clean-checkout owner remains. |
| Coordinate a full generic focus geometry reflow | **Implemented for layout.** All former MCP geometry diagnostics are closed. |
| Preserve focus route semantics through hidden availability gates | **Implemented for eligibility; partial for presentation and AI equivalence.** Thirty-five visible groups moved to hidden gates and lost the implicit child-focus AI boost. |
| Close Event 006 as a whole | **Not accepted and not achieved.** Current package, formable, asset, super-event, catalog, AI, balance, and capacity blockers remain. |

## Remaining blockers and recommended next actions

1. Record a parent decision on the 35 hidden prerequisite groups: accept the presentation/AI change explicitly, or restore selected visible edges and compensate AI weighting.
2. Keep the 14- and 20-country modes fail-closed until an accepted synchronized, reservation-aware, host-compatible disjoint witness exists.
3. Continue package admission and source-proof work; do not infer readiness from registry membership.
4. Close formable families only after their package, identity, flag, member-adapter, and readiness conditions pass; the repaired vanilla mirror does not close those gates.
5. Keep 6001 blocked until rights-clear audio and the complete runtime firing/localisation/sound package exist.
6. Finish scenario-based AI and balance evaluation, including the focus-reflow weighting consequence, before any whole-event balance claim.
7. Reconcile current authority prose so pre-reflow 223-connector and fourteen-blocker paragraphs are unambiguously historical and the new 35-gate consequence is disclosed.
8. Align the workbook and exports only after implementation facts and completion dispositions are accepted.

## Simplifications, omissions, and blockers

The focus reflow uses hidden availability gates in place of 35 visible prerequisite groups. That is a material presentation and AI-behavior simplification and is not yet explicitly accepted. No other simplification was introduced by this read-only audit. The audit did not run Hearts of Iron IV, alter gameplay, validate live/save-load behavior, promote assets, modify the workbook, or resolve any remaining package, formable, super-event, asset, AI, balance, or catalog blocker.
