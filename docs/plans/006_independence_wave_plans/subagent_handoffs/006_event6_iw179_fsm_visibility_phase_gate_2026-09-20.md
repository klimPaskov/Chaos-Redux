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

The focused read-only `hoi4.event_inspect` lint for the committed source returned `EVENT_INSPECTED_PARTIAL` with source revision `7bc390e9516d5b5dfe63dbd72b96eddd673953d1ad2177f259c603cef9509573`, zero blocking diagnostics, and zero skipped sources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54befee10e95c8b545d3961742548756a955cb307a1dfadc60f19ff7685c94ab/1e11ea1736cca9ab08de2e9a287f2c2ddc8faed48c0d6b57b2646ce0c932ebc0/event-lint-7bc390e9516d.json`.

The matching read-only options render returned `EVENT_RENDERED_PARTIAL` at the same cached revision with layout hash `dc7c6b2fdb9a3143f5ed65837542c0750cbf4453a8736f2c704ed2e8aa231e38`, 24 selected nodes, and 42,772 omitted nodes. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8953b35e83462d4790877ab4fd073808307a89b1859fe1aa92042144605cd10/44c58f98394f27326bc7795b5c25bbd16ef599c42a970a78cc0b99a8ac367cd5/event-options-7bc390e9516d-manifest.json`.

The refresh did not produce a new graph revision for the decision source: this focused Event route indexes the event/on-action projection, while the changed common decision file is outside the returned graph revision. The receipt therefore confirms no blocking Event MCP diagnostics but does not claim decision-row semantic diff coverage. Native decision-row rendering, quantitative AI comparison, live execution, and save/load behavior remain unverified.

## Scope limits

This repair addresses FSM category density and phase presentation only. It does not admit IW-179, publish the withdrawn portrait or identity, change FORM-48 reachability, alter the shared allocator, change costs, or close the whole-event HOLD / PARTIAL gates.
