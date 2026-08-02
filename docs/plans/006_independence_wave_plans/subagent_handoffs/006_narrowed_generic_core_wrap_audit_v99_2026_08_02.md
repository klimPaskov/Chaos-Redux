# Event 006 narrowed generic-tree and core-system wrap audit

Date: 2026-08-02

## Scope decision

The current user decision makes one `independence_wave_focus_tree` the shared tree for every admitted Event 006 release. Bespoke country focus trees and live/in-game testing are outside this pass. Meaningful vanilla trees remain untouched; the reviewed ICE carrier is the only additive overlay, and CAT/FSM use the documented minimal-tree/full-framework exceptions.

## Narrowed scope result: static PASS

### Generic focus framework

- `common/national_focus/006_independence_wave_focus.txt` contains 207 focus blocks: 184 regular and 23 shared.
- The tree covers survival/statehood, government, economy, military/security, diplomacy/host/patron, regional expansion, Network/League, formable/high-chaos, and gated package modules.
- Static focus review found no duplicate IDs, missing prerequisites, unresolved localisation, unresolved custom tooltips, missing icons, or invalid mutual-exclusion targets. All focus blocks expose AI weighting and a concrete completion reward.
- The common package barrier requires either the full generic tree contract or the reviewed additive-carrier contract before a release can commit. No package can silently claim a missing focus surface.
- Route rewards write the visible country, host, patron, Network, League, ambition, formable, and high-chaos ledgers through shared scripted effects. The framework does not create a political-power store, passive checklist mission, reward dust, or free-unit loop.

### Shared release core

- The allocator freezes a complete plan before release, reserves surviving host states first, prefers capital anchors, requires unique anchors, trims optional territory before dropping candidates, rerolls living/invalid/colliding tags, and locks the plan before execution.
- Joint Event 005/Event 006 incidents reserve Event 005 anchors first, then Event 006 anchors, then optional territory, and use one shared lock and rollback boundary.
- The current static allocator receipt reports 149 publishers, 126 automatic/high-chaos selectable bindings, 138 SCN-008 ranked bindings, 14 exact content attestations across 13 compatible reservation groups and 14 distinct anchors, and zero external Event 006/Soviet tag or identity-surface collisions. Random Events Mod `REV`, `ZIN`, and `ZZZ` are intentionally outside the scoped collision policy.
- The doubled automatic ladder is 6/8/10/14/20; World Collapse is 20 and scales force, instability, rarity, and ambition instead of replacing the count rule. The 14/20 bands remain fail-closed when the admitted package/capacity witness is insufficient.
- The pre-wave crisis path covers low stability and severe occupation pressure with a paid mission, queued release, requester-loss recovery, and bounded failure receipt.
- Country, former-host, patron, Network, League, rival-bloc, and evolution ledgers have centralized tuning, visible readers, bounded writers, and generation cleanup. The five evolution incident families and paid Armed Birth reserve follow-through are source-wired.

### SCN-008 acceptance and ledger repair

- The source receipt covers eight player-facing modes at four intensities (32 cells): Sovereign Scatter, Common Congress, Wars of Separation, Universal Belligerence with each of its three target rules, Patron Worlds, and Great Partition.
- The edge receipt covers eight cases: zero-ready, mixed readiness, anchor collision, protected-host remnant, Event 005 collision, repeated launch/reset, former-host target uniqueness, and alternative belligerence target/ledger alignment.
- `independence_wave_scenario_freeze_summary` publishes selected rows as released only after `independence_wave_scenario_committed`. Failed/rolled-back plans keep released count and host count at zero, preserve the rejected-row country prefix, append selected package IDs from the frozen plan, append matching selected country scopes from frozen row indices, then append the common failure reason. Unbound rows are appended only after those aligned arrays.
- `python -B .tools/audit_event6_scenario_matrix.py` and `python -B .tools/audit_event6_allocator.py` pass after the repair commits `d6a364040` and `1d9bdba96`.

## Remaining whole-event disposition: HOLD / PARTIAL

The generic-tree/core tranche is source-closed, but the original complete Event 006 objective is not complete. The current authority remains `006_event6_narrowed_generic_focus_completion_audit_v98_2026_08_02.md` and records these open surfaces:

- 179 of 193 non-overlay registry rows remain unattested; 55 selectable rows lack an accepted current-map binding and 17 reservations are inert. The admitted set cannot currently satisfy the 14/20 bands, so no package-capacity shortcut was made.
- Country-specific package readiness, grounded leader/portrait/flag/symbol research, force/technology/AI evidence, formable reachability, GUI/achievement runtime surfaces, and final asset manifests remain incomplete or fail-closed for their documented reasons.
- Super-event `6001` has art and sprite registration but no rights-cleared audio/WAV, runtime dispatch, localisation wrapper, or reachable firing package. `6002` remains partial. No fallback audio or artwork substitute was introduced.
- Focus/probability MCP inspection remains `SCAN_BYTE_LIMIT`; no live focus geometry or runtime consumer claim is made. Package AI and balance evidence remain source-level/partial where the authority says so.
- The catalog workbook/export mirror is aligned with the current wording, but Event 006/Cluster 2 remains `In progress` and SCN-008 remains `Needs Testing` pending the documented package-capacity/source evidence boundary.
- No Event 006 advisor icons were created or authorized.

## Simplifications and blockers

- Approved simplification: one shared generic focus tree, with no bespoke country focus trees and no live/in-game testing in this pass.
- No fallback, admission shortcut, generic portrait substitution, advisor-icon substitute, political-power store, passive checklist mission, reward dust, free-unit loop, or unsafe overwrite was used.
- The whole-event goal must not be marked complete while the package, asset, formable, super-event, GUI/achievement, AI/balance, focus-diagnostic, and catalog/source blockers above remain open.

## Evidence commands

- `python -B .tools/audit_event6_scenario_matrix.py`
- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`

These checks are source/static evidence only and do not claim a live game run.
