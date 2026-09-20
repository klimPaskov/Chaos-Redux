# IW-179 FSM visibility phase gate

Date: 2026-09-20.

Status: implemented as a bounded presentation and pacing repair; Event 006 remains HOLD / PARTIAL.

## Finding

The FSM category exposed four mutually exclusive government-route decisions before the Inter-Island Authority ledger reached its stable threshold. Their availability blocks already required `has_stable_independence_wave_fsm_inter_island_authority`, so the pre-stability surface showed blocked route rows while the package was still in its core-survival phase. The autonomous federation mandate likewise exposed before its existing stable-authority and recognition requirements were met.

This contradicted the accepted package contract that the four government settlements condense only after the ledger reaches 60 and the shared Event 006 phase model in which provisional play keeps major ambitions blocked.

## Change

The four FSM route decisions now require `has_stable_independence_wave_fsm_inter_island_authority = yes` in `visible`. Their existing availability, cost, duration, cancellation, route-lock, and AI logic is unchanged.

The autonomous federation mandate now requires both the same stable-authority trigger and `is_independence_wave_recognized_or_later = yes` in `visible`, matching its pre-existing availability block. Its strategic cost and delegation effect are unchanged.

This keeps the founding mission and the three core FSM projects available during the survival phase, then exposes the route settlement choices only after stabilization. It does not add a new flag, variable, category, route, reward, or admission path.

## Validation

The source diff is limited to the five IW-179 `visible` blocks in `common/decisions/006_independence_wave_pacific_decisions.txt`. The existing package trigger `has_stable_independence_wave_fsm_inter_island_authority` is the shared threshold predicate used by the route availability helper, so no new helper or tuning value was introduced.

The focused Event MCP inspect/render should be refreshed against the committed source. Native decision-row rendering, quantitative AI comparison, live execution, and save/load behavior remain unverified.

## Scope limits

This repair addresses FSM category density and phase presentation only. It does not admit IW-179, publish the withdrawn portrait or identity, change FORM-48 reachability, alter the shared allocator, change costs, or close the whole-event HOLD / PARTIAL gates.
