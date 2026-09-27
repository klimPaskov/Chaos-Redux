# SCN-008 static matrix audit — 2026-09-27

**Disposition:** Static source/matrix coverage recorded; SCN-008 and Event 006 remain **HOLD / PARTIAL**. This handoff records the parent-supplied successful result of `python .tools/audit_event6_scenario_matrix.py` against current source; the curator did not rerun the command.

The audit reported **32/32 unique cells**: `common_congress`, `great_partition`, `patron_worlds`, `sovereign_scatter`, `wars_of_separation`, and `universal_belligerence` with `former_hosts`, `nearby_nonleague`, and `neighboring_releases` rules, each at `low`, `medium`, `high`, and `maximum` intensity. It also reported all eight static edge-case IDs, `EDGE-SCN-001` through `EDGE-SCN-008`. The matrix sources are [the 32-cell acceptance matrix](006_scn008_32_cell_static_acceptance_2026_08_02.md) and [the current edge-case source matrix](../006_event6_scn008_edge_case_source_matrix_current_2026-09-25.md).

| Publication source witness | Count or order |
| --- | --- |
| Commit setter; ledger-visible setter; result-pending setter | One each |
| Result-pending clearers | Two |
| Scenario-result dispatch; scenario-log dispatch | One each |
| Success dispatch | `chaosx.nr6.2` -> `chaosx.triggerable_scenarios.80` |
| Failed-branch result dispatchers; failed-branch log dispatchers | Zero each |

These counts establish source and matrix coverage only. They do not execute any cell or edge case, establish host/DHC ordering or rollback behavior at runtime, prove map-wide candidate selection, validate delayed result delivery or save/load, or change package attestation, admission, design acceptance, or catalog status. The [focused Event MCP handoff](006_scn008_focused_mcp_refresh_2026-09-27.md) remains separate partial structural evidence; its helper/lifecycle and comparison limits remain open. Parent review and user-owned runtime observation remain outstanding.

**Documentation handoff:** Created this file and added concise links in `../006_source_of_truth_map.md` and `../006_independence_wave_resume_packet.md`. The 32-cell and edge matrices remain the static source witnesses; no document was merged, rejected, or superseded by this receipt. No gameplay, localisation, GUI, focus, workbook, CSV, or asset file was edited, and no commit was made. No additional test, HOI4 launch, or catalog export was run.

The same bounded reconciliation records IW-048 portrait clearance as blocked and IW-039 mission eligibility/probability as unresolved in both current ledgers; it clarifies the earlier DON fixture result without accepting a design or changing a plan disposition. The current repository-wide localisation finding was retained. The curator reviewed the three-file diff and link placements; no broader prompt, duplicate-document, or Markdown hard-wrap cleanup was in scope.
