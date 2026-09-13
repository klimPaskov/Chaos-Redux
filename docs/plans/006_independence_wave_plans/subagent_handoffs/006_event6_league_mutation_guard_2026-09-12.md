# Event 006 League live-member mutation guard

Date: 2026-09-12

Status: **IMPLEMENTED / SOURCE-STATIC VALIDATED / LIVE ENGINE EVIDENCE PENDING**

## Scope

This bounded repair covers the `independence_wave_transform_league_charter` decision in `common/decisions/006_independence_wave_decisions.txt`.

## Finding

The radical-charter completion effect iterated `global.independence_wave_league_member_country_entries` while `independence_wave_leave_league` removed departing members from that same live array. Array removal shifts later rows into the current cursor, so adjacent low-standing members could be skipped and incorrectly remain in the transformed League.

## Change

The completion effect now snapshots the current member scopes into the temporary array `independence_wave_radical_charter_member_entries` before evaluating departures. The departure loop consumes that snapshot, allowing `independence_wave_leave_league` to reconcile and mutate the live member registry without changing the iteration set. The temporary array is cleared after the transition.

No route, threshold, cost, member identity, charter rule, AI weight, localisation, asset, or admission gate changed.

## Evidence

- Installed vanilla effects documentation confirms `for_each_scope_loop` iterates each element of the referenced array and `remove_from_array` removes an element by value or index; no live-array mutation guarantee is documented. The snapshot removes that ambiguity.
- `python -B .tools/audit_event6_allocator.py --strict` passed: exact automatic ladder `3/4/5/7/10`, 32 attestations, 40 adapters, 29 reservation groups.
- `python -B .tools/audit_event6_country_api.py --strict` passed: 242 broad rows, 191 resolved carriers, no missing or duplicate consumers.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases; failed publication remains zero.
- `python -B .tools/audit_event6_flags.py --strict` passed all 102 registered tag ladders.
- `python -B .tools/audit_event6_gui_matrix.py` passed the five-tab semantic contract and 5/3/4/4 frame counts.
- `git diff --check` is clean for the touched decision file.
- Read-only `hoi4.event_inspect` refresh/lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, with 9,741 events, 15,167 options, 38,369 edges, 2,199 diagnostics, and zero projected helpers. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a2f7d474fb2d41040392f4b88d663f220a5082183aa4e1f8c508eeea350283d/72efaf754e0403cde8400dbf9e1231dff90b04e998038adee85c6c66768717d1/event-lint-4bccb6ec7fe1.json`.

## Limits and follow-up

The required HOI4 Event/decision MCP route does not provide a League execution receipt in this runtime, and no live save/load test is claimed. The queued League scenarios remain unresolved for engine evidence: `LEAGUE_3_LIVING_FAIL_CLOSED`, `LEAGUE_4_LIVING_3_WILLING`, `LEAGUE_CONGRESS_FAILURE`, `LEAGUE_FIVE_PILLARS_ADOPTED`, `LEAGUE_EACH_ROUTE`, `LEAGUE_LEADERSHIP_CHALLENGE`, `LEAGUE_MEMBER_EXPULSION`, `LEAGUE_WAR_MANDATE`, `LEAGUE_FAILED_RESCUE`, `LEAGUE_CRISIS_REFORM`, `LEAGUE_CRISIS_SPLIT`, `LEAGUE_RIVAL_REUNIFICATION`, `LEAGUE_DURABLE`, and `LEAGUE_GENERATION_CLEANUP`.

The repository contains a pre-existing zero-byte `.git/index.lock`, so no staging or commit was attempted.
