# Event 006 BAX/BBX capital-scope guard — 2026-08-26

## Status

Completed a narrow source repair for the dormant IW-027 Thrace (`BAX`) and IW-028 Epirus (`BBX`) carriers. No live game, save/load, or in-engine country-release result is claimed.

## Finding

The pasted `capital_scope` diagnostics identify the pre-consolidation Epirus and Thrace trigger files. Those parser files no longer exist; their package checks are now in `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`, where the fixed anchors are state 184 for Thrace and state 185 for Epirus. The empty history shells in `history/countries/BAX - Thrace.txt` and `history/countries/BBX - Epirus.txt` have no valid capital before Event 006 transfers their reserved states, so a decision trigger must not evaluate `capital_scope` on those dormant shells.

## Source changes

- Added `has_independence_wave_current_capital_controlled_by_root` to `common/scripted_triggers/006_independence_wave_triggers.txt`. It checks for an owned state that is marked as the country's capital and is controlled by `ROOT`, so an empty dormant shell fails closed without constructing an invalid capital target.
- Replaced the `capital_scope` availability and cancellation forms in the IW-028 Epirus and IW-027 Thrace sections of `common/decisions/006_independence_wave_balkan_decisions.txt`. The replacement covers 11 positive and 11 negative trigger forms per section; decision effects, costs, missions, and package identifiers are unchanged.
- Active released countries still use their actual controlled capital through the shared helper semantics. No other Balkan package was changed.

## Invariants

The hidden `chaosx.nr6.1` event remains the only standalone transaction entry point, and the public `.2` report remains gated on a committed non-empty plan. The retired `.3` compatibility endpoint only clears stale flags and cannot create a wave, pressure, queue, decision category, or visible crisis indication. The patch does not restore any pre-event player-facing surface.

## Evidence

The focused checks passed after the patch:

- `python -B .tools/audit_event6_allocator.py` — allocator and pre-event-surface audit passed.
- `python -B .tools/audit_event6_country_api.py` — 242 broad tags, 191 resolved carriers, zero missing or duplicate API rows.
- `python -B .tools/audit_event6_flags.py --strict` — 102 complete flag families.
- `python -B .tools/audit_event6_form16.py` — FORM-16 contract passed.
- `python -B .tools/audit_event6_scenario_matrix.py` — 32 cells and 8 edge cases passed.

The prior valid Event 006 MCP inspect was partial with zero blocking diagnostics; it is source/lint evidence only and does not replace live transaction validation.

## File consolidation disposition

Earlier Event 006 registry merges already removed 132 small parser files and about 79 KB of committed source. No additional file was merged in this repair: the remaining small files are either already canonical registries or active/ownership-sensitive package surfaces, and moving them would add documentation and review risk without changing runtime behavior.

## Remaining risk

The user must verify the release transaction in a live session. If a current build still shows the old “Independence Wave Crisis” or the former long cost string, that text is not present in the current source tree and indicates a stale or different loaded mod copy rather than a source string covered by this patch.
