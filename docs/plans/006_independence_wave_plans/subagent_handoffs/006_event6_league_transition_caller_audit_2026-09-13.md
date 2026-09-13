# Event 006 League transition-caller audit handoff — 2026-09-13

## Status and scope

Status: unresolved parent-owned design/integration gap; no gameplay patch applied in this tranche.

Owner: bounded Event 006 League lifecycle reachability audit, for parent `/root`.

Scope: the authored League state-machine effects and their current callers in `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_effects/006_independence_wave_decision_effects.txt`, `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`, `common/decisions/006_independence_wave_decisions.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_scenario_effects.txt`, and `common/scripted_triggers/006_independence_wave_triggers.txt`.

The accepted League state-machine diagram, League mechanics specification, decision/mission map, current lifecycle handoff, offline Paradox wiki pages, and the relevant vanilla effects/triggers/decision documentation were reviewed before this audit. No new decision, mission, event, phase, localisation, icon, AI weight, fallback, or generic content was added.

## Finding

The source contains named transition effects for the complete League state machine, but several normal-play transitions have no active caller in the current repository. The accepted decision matrix does not define a decision or mission row for those transitions, and the current localisation set has no player-facing contract for them.

The missing callers are:

- `independence_wave_proclaim_consultative_league`
- `independence_wave_upgrade_consultative_league`
- `independence_wave_mark_league_durable`
- `independence_wave_reform_league`
- `independence_wave_normalize_reformed_league`
- `independence_wave_reunify_rival_leagues`
- `independence_wave_dissolve_league_to_network`
- `independence_wave_restart_informal_network`

The durability branch has an additional concrete reachability hole: `can_independence_wave_mark_league_durable` requires the global flag `independence_wave_league_durability_mission_complete`, but the current source census found no setter for that flag. A caller added without an accepted completion contract would either be permanently locked or require inventing a new mission outcome.

## Existing valid callers

The following transitions are already connected to authored gameplay paths and were left unchanged:

| Transition | Current caller/owner |
| --- | --- |
| Regional conference, congress preparation, charter vote | DM45 founding-congress mission and the accepted focus/evolution preparation paths |
| Formal League proclamation | DM46 charter-pillar mission after the fifth accepted pillar |
| Leadership challenge | DM47 League mission and existing term-management effects |
| Crisis entry | League decision effects and the high-chaos reclamation path |
| Crisis to rival leagues | Rival-bloc activation effect after crisis handling |
| Rival-bloc internal return to formal/informal | `independence_wave_rival_bloc_dissolve_contract` |
| Scenario consultative/formal setup | `independence_wave_scenario_form_common_congress` |

The rival-bloc reunification helper remains defined and internally coherent, but it is not called by the current main League lifecycle. The rival dissolution contract performs its own formal/informal transition and is not evidence that the separate reunification effect has a player-facing caller.

## Why no source patch was applied

The accepted decision/mission map contains DM45–DM47 and DM60–DM62 for the League category, but no lifecycle rows for consultative upgrade, durability, reform, normalization, reunification, dissolution, or restart. Adding calls from an existing decision or value-change helper would silently change when the League changes phase and would create player-facing behavior without an accepted trigger, cost, duration, AI, tooltip, cancellation, cleanup, or balance contract.

Automatically calling every unused effect from `change_league_values` or another shared helper would be especially unsafe: it would invent transition timing, make authored crisis/reform branches fire without a defined player action, and bypass the missing durability completion receipt. It would also blur the fail-closed admission and no-pre-event UI constraints already accepted for Event 006.

The correct next step is a parent-owned design decision that supplies the missing lifecycle contracts (or explicitly rejects/deprecates the unused effect names), followed by a bounded implementation with localisation, AI, cost, cooldown, cleanup, and runtime evidence. This audit does not choose that design.

## Validation and evidence

The prior League mutation-boundary patch remains the only gameplay edit in the current tranche: the radical-charter transformation snapshots the live member array before removing low-standing members. Its focused allocator, country API, scenario matrix, flags, and GUI semantic validators passed.

The fresh Event MCP inspection of `chaosx.nr6.1` was `EVENT_INSPECTED_PARTIAL` (revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`) with artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a2f7d474fb2d41040392f4b88d663f220a5082183aa4e1f8c508eeea350283d/72efaf754e0403cde8400dbf9e1231dff90b04e998038adee85c6c66768717d1/event-lint-4bccb6ec7fe1.json`

The Event MCP result is partial/deferred engine evidence and is not a live lifecycle execution proof. The decision-specific MCP route is not exposed in this runtime. No HOI4 launch or save/load test was performed.

## Handoff boundary

This document records a design/integration gap, not a completed lifecycle implementation. The parent should not claim the full League state machine is reachable until accepted caller contracts exist and are wired with matching player-facing text, AI behavior, cleanup, and runtime evidence.

The existing dissolution/restart cleanup repair and the live-member snapshot repair remain separate implemented changes. This audit intentionally leaves all gameplay source files unchanged.

The repository currently contains a pre-existing zero-byte `.git/index.lock`; the handoff is therefore unstaged and uncommitted for parent review.
