# Event 032 agent decisions — 2026-10-04

Authority: the user granted the implementing agent full authority to take the recommended, spec-consistent option and record it here.
Each entry is an agent decision with its acceptance basis; implementation evidence is linked where it exists.

## Lead decisions carried into this round

1. The stopped thread's uncommitted fixes for the seven routed lint defects are adopted rather than rewritten. Basis: they match the routed fixes, use the shared `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days` helpers with the output temporaries preset, and every `.tools/test_event32_*.py` test passes. Disposition: `implemented`.
2. Evolution pacing uses one bounded delayed job per track, armed when the track first becomes eligible, with a randomised delay derived from its base MTTH and shortened by pressure; firings remain a fallback. The architect's full pressure ledger, hostile-pair registry and hazard-clock worker from `subagent_handoffs/032_evolution_pacing_architecture_2026-10-03.md` are `rejected` for this round. Basis: spec part 4 allows bounded delayed evolution jobs created when a threshold is first met, and the larger design adds maintenance cost with no player-visible difference.
3. Saturation doctrine and retaliation posture are explicit country decisions, and an unlock grants access only. Basis: spec part 4 lets a country decline or delay adoption and requires posture adoption to carry requirements, costs and a cooldown.
4. Missing decision families reuse the existing localisation keys, cost keys and same-family decision icons. No new art and no scripted GUI. Basis: spec decision 4.
5. `rejected` optional scope: changing the participating site or increasing preparation effort for a prepared operation (part 5 says "where allowed"), and redirecting the retaliation target after new evidence (the decision prompt allows it only when the accepted spec and engine proof permit it).
6. The physical custody model stays: the aggregate reserve is authoritative with a greedy whole-missile projection onto sites. Only the equal-split operation allocation is fixed.
7. No native raid route or icon is added; the accepted conditional scripted route in spec part 8 stands.
8. Event 032 returns to the default-enabled list only after the priority 1 and 2 gameplay items land. The catalog status change is staged in `catalog_changes_pending.md`; the workbook and CSV exports are not edited.
9. HOI4 MCP is used only with narrow queries, and timeouts are recorded as exact blockers rather than retried.
10. The duplicate native id stays a live-only item, and the temporary allocation markers remain until a fresh log attributes the error.

## Implementation decisions taken during the round

- The stray `.tools/commit_event32_scn015_qa_message_temp.txt` commit-message scratch file from the SCN-015 repair is removed; it was never part of the mod.
- The untracked probability-matrix audit handoff and its evolution-gate scenario fixture from 2026-10-03 are adopted as finished read-only evidence. Their legacy-toggle findings were already repaired by `032_evolution_toggle_binding_repair_2026-10-03.md`; the handoff stays as dated evidence.
