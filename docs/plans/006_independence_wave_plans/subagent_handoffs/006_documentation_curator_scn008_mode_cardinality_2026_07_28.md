# Event 006 SCN-008 mode-cardinality reconciliation

Date: 2026-07-28

Scope: current Event 006 / SCN-008 documentation surfaces for the source-driven mode cardinality. This pass did not edit gameplay, localisation, scripted localisation, GFX, binary assets, the spreadsheet workbook, export CSVs, or historical audit bodies.

## Exact authority decision

The current SCN-008 runtime acceptance matrix is **eight player-facing selectable modes by four intensities, or 32 cells**.

The implementation retains six numeric scenario families: Sovereign Scatter, Common Congress, Wars of Separation, Universal Belligerence, Patron Worlds, and Great Partition.

Universal Belligerence contributes three independently selectable rules: Former Hosts, Neighboring Releases, and Nearby Nonleague States. The selector walks those three rules before advancing to the next numeric family, and localisation and catalog mirrors expose each rule as its own mode.

This is a source-driven acceptance clarification. It adds no scenario family and no intensity. The historical six-by-four or 24-cell shorthand remains preserved inside older audit snapshots but is not the current runtime matrix.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted scenario design | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md` | Patched with the six-family/eight-mode/32-cell clarification and separate Universal Belligerence rules. |
| Acceptance criteria | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` | Patched to require all 32 mode/intensity cells and separate Universal Belligerence result rows. |
| Current gameplay-facing event map | `docs/events/006_independence_wave/overview.md` | Patched to record the eight-mode/32-cell authority while retaining the whole-event HOLD boundary. |
| Current scenario system docs | `docs/systems/triggerable_scenarios.md` and `docs/events/006_independence_wave/systems/triggerable_scenario.md` | Patched to distinguish six numeric families from eight selectable modes and to retain the existing 32-cell validation target. |
| Catalog mirror design note | `docs/specs/006_independence_wave_specs/quality/catalog_alignment_handoff.md` | Patched from an unqualified six-family list to the numeric-family plus eight-player-mode crosswalk. Its old catalog status remains a planning snapshot. |
| Current routing ledger | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Patched with the current cardinality row, v27 handoff disposition, catalog mirror evidence, and historical-shorthand contradiction note. |
| Current resume packet | `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Patched with the 32-cell acceptance boundary and this handoff path. Existing portrait-shelf sections were left unchanged. |
| Source evidence | `common/script_constants/006_independence_wave_constants.txt:127-153`, `common/script_constants/006_independence_wave_scenario_constants.txt:9-20`, `common/scripted_effects/006_independence_wave_scenario_effects.txt:25-90`, `common/scripted_triggers/006_independence_wave_scenario_triggers.txt:9-55` | Read-only evidence. No gameplay file was changed. |
| Player-facing mode evidence | `localisation/english/006_independence_wave_scenario_l_english.yml:5-12` and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv:15-21` | Read-only evidence. Eight mode labels and four intensity paragraphs are present. |
| Workbook mirror evidence | `subagent_handoffs/006_catalog_audit_v27_2026_07_27.md:9-21` | The audit records a direct `Scenarios!A9:F9` workbook/localisation comparison with all eight type names and four intensity paragraphs. The workbook and CSV were left unchanged. |

## Unresolved plan and handoff dispositions

| Artifact or family | Disposition |
| --- | --- |
| v27 improvement-loop handoff `006_improvement_loop_audit_v27_2026_07_27.md` | Current bounded planning evidence. Its C1-C3 addendum already states the 32-cell authority and remains queued for runtime execution evidence. It was preserved unchanged. |
| v27 catalog audit `006_catalog_audit_v27_2026_07_27.md` | Current catalog mirror evidence. It remains PASS for mirror alignment, with SCN-008 still `Needs Testing` and no workbook/export change. It was preserved unchanged. |
| v23 and v27 completion audits, v21 and earlier audits, and v10 improvement closure | Historical or whole-event status snapshots. Their six-by-four or 24-cell wording remains for traceability and was not rewritten. Use this handoff, the current source map, and the resume packet for matrix cardinality. |
| v28 broad documentation-curator reconciliation | Historical broad cleanup handoff. It remains useful for portrait, package, and whole-event dispositions. This dated handoff supersedes it only for SCN-008 mode cardinality. |
| Runtime acceptance plan | Queued. SCN-008 remains `Needs Testing` until all 32 cells and bounded sweeps are dispositioned. |

## Contradictions and resolution

1. Historical completion audits call the source contract six types by four intensities and request a 24-cell runtime matrix. The current source selector, localisation, catalog mirror audit, and v27 improvement addendum show three independently selectable Universal Belligerence rules. Current docs now state eight modes by four intensities, or 32 cells. Historical audit bodies remain unchanged.
2. The source constants/effects expose `bound_package_count = 138` and `disabled_unbound_package_count = 55`, while current scenario system/localisation documentation still describes 149 bound rows and 57 disabled identities. This package-count contradiction is outside the mode-cardinality decision and remains unresolved. No count was invented or rewritten in this pass.
3. The accepted spec and catalog-alignment handoff retain working-label language such as `Every Flag`, while live localisation uses `Every Banner Rises`. This is an accepted design-label versus implementation-localisation distinction, not a mode-cardinality conflict, and was left intact.

## Duplicate or superseded document list

- `docs/systems/triggerable_scenarios.md` and `docs/events/006_independence_wave/systems/triggerable_scenario.md` intentionally overlap. The former is the cross-scenario index, and the latter is the SCN-008 implementation contract. Both were retained and clarified.
- The v27 improvement handoff and this handoff both record 32 cells. The v27 file is the bounded closure plan, while this file is the documentation authority and patch ledger. Neither replaces the other.
- The v27 catalog audit remains the workbook/localisation evidence record. This handoff records the no-workbook-change disposition and the current doc crosswalk.
- v23/v27 completion snapshots and older six-by-four plans remain historical evidence. No file was deleted or rewritten to hide the old shorthand.

## Stale prompt or instruction list

- `docs/specs/006_independence_wave_specs/quality/catalog_alignment_handoff.md` carried an unqualified six-family list and was patched with the eight-mode crosswalk.
- Historical v10/v21/v23/v27 completion and improvement handoffs still contain six-type or 24-cell wording. They are intentionally preserved snapshots and must not be used as current matrix instructions.
- No other current scoped spec, event doc, system doc, source map, resume packet, or catalog-mirror note retains the unqualified six-by-four runtime acceptance instruction after this patch.

## Remaining runtime evidence gates

The matrix clarification does not establish gameplay completion. Parent-owned evidence is still required for all 32 cells, including requested mode and intensity, committed numeric family and Universal Belligerence rule, candidate/accepted/blocked counts, per-package rejection reasons, protected hosts and remnants, transferred territory, force and institutional tuning, league setup, patron setup, host-war or bounded-belligerence results, partition setup, war declarations and targets, summary text, achievement eligibility/disqualification, retry, rollback, and save/load results.

Universal Belligerence requires three separate target-selection result columns. One rule cannot proxy for the other two.

The bounded sweeps still include Event 005 collisions, living or already released origins, unsafe or exhausted hosts, unique-anchor conflicts, invalid current-map bindings, insufficient pools, repeated execution, selector wrap in both directions, save/load between selection and execution, save/load after a committed summary, and representative deterministic seeds where weighted target choice exists.

The current package-count mismatch between source constants and scenario docs also needs an explicit parent/source decision before any package-count or catalog wording is promoted.

## Patch handoff

Files changed:

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`
- `docs/specs/006_independence_wave_specs/quality/catalog_alignment_handoff.md`
- `docs/events/006_independence_wave/overview.md`
- `docs/systems/triggerable_scenarios.md`
- `docs/events/006_independence_wave/systems/triggerable_scenario.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- this handoff

Docs promoted or clarified: the accepted specs, current event/system docs, source map, and resume packet now use the eight-mode/32-cell authority. The catalog-alignment handoff now records the numeric-family/player-mode crosswalk. No plan was marked gameplay-complete.

Docs queued: the 32-cell runtime matrix, bounded collision/selector/rollback/persistence sweeps, balance evidence, and package-count authority decision remain queued.

Docs left unchanged: v27 improvement/catalog audits, v23/v27/v21/v10 historical or completion snapshots, the workbook, the three export CSVs, gameplay source, localisation source, and portrait-shelf sections in the resume packet/source map.

## Meaningful validation run

- Targeted source reads confirmed six numeric `independence_wave_scenario_type` values, three `independence_wave_scenario_belligerence_rule` values, nested selector stepping, and four intensity values.
- Targeted localisation and CSV reads confirmed eight SCN-008 type labels and four intensity paragraphs. The v27 catalog audit was used as the direct workbook mirror evidence; no workbook was modified or exported.
- Targeted `rg` checks after patching found no unqualified six-by-four or 24-cell runtime instruction in the current scoped specs, event docs, system docs, source map, resume packet, or catalog-alignment handoff. Historical audit snapshots intentionally retain those terms.
- Targeted path checks confirmed all changed docs and this handoff exist.

Skipped meaningful validation:

- No Hearts of Iron IV launch, engine load, MCP runtime witness, live save/load test, workbook inspection/edit, CSV export, binary asset inspection, or gameplay-source edit was performed. Those checks are outside this documentation-only scope and remain parent/runtime or spreadsheet-worker gates.

## Remaining risks

- SCN-008 remains `Needs Testing`; the 32-cell matrix and all bounded sweeps have no live evidence in this pass.
- The source/doc package-count mismatch remains open and may affect future summary wording, but it does not change the accepted 8-by-4 mode cardinality.
- Historical audit snapshots intentionally preserve obsolete six-by-four shorthand, so readers must use the current source map, resume packet, current event/system docs, and this dated handoff.
- The parent is concurrently flattening the Event 006 portrait shelf. This pass did not alter shelf sections, but the parent may need a later docs-only reconciliation after that change.
- No Git commit was created, as requested. The worktree contains unrelated concurrent changes.
