# Event 006 IW-093/IW-098 fixed political-power exception acceptance

Date: 2026-09-20.

## Disposition

**ACCEPTED DESIGN RECONCILIATION / NO GAMEPLAY CHANGE.** The six IW-093 Asante and IW-098 Sokoto route-opening conferences retain their current fixed 100 political-power commitment and 70-day duration as a narrow package-specific exception to the general Part 3 rule against flat political-power costs.

The user explicitly approved the pending Event 006 design dispositions on 2026-09-20 by stating, “i approve everything.” That approval is recorded here as the acceptance basis for reconciling the already implemented package contract with the generic guidance. No replacement spendable type, amount, payer, timing, AI weight, localisation cost row, admission gate, or runtime behavior was invented or changed.

## Exact accepted contract

- `independence_wave_iw093_royal_confederacy_conference`, `independence_wave_iw093_constitutional_cabinet_conference`, and `independence_wave_iw093_veterans_emergency_conference` use `constant:independence_wave_iw093.conference_political_power_cost`, currently 100, and `constant:independence_wave_iw093.conference_days`, currently 70.
- `independence_wave_iw098_sultanic_federal_compact`, `independence_wave_iw098_northern_constitution_compact`, and `independence_wave_iw098_frontier_command_compact` use `constant:independence_wave_iw098.conference_political_power_cost`, currently 100, and `constant:independence_wave_iw098.conference_days`, currently 70.
- The IW-093 veterans emergency route keeps its separate 50 command-power transaction ledger and does not generalize that custom spend to the other five route openings.
- Native political power is consumed once by the timed decision engine at selection, route closure remains no-refund, and the existing route-lock, cancellation, failure, cleanup, and package-gate behavior is unchanged.

## Authority and references

The generic rule is in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md` under Dynamic costs and durations. The package-specific contract is in `docs/events/006_independence_wave/systems/iw093_iw098_signature_packages.md` and `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`. The constants are in `common/script_constants/006_independence_wave_constants_registry.txt`.

The earlier bounded audits `subagent_handoffs/006_event6_decision_route_audit_2026-09-19.md` and `subagent_handoffs/006_event6_iw093_iw098_route_cost_contract_blocker_2026-09-13.md` correctly identified the conflict and prohibited guessing a replacement payment. This receipt supersedes only that design-conflict disposition; it does not close native decision-row rendering, typed probability, package identity, rights, admission, or whole-event completion gates.

## Validation and limits

The current source retains all six native political-power cost fields, all six 70-day timers, the veterans-only command-power ledger, and the existing no-refund terminal paths. The accepted documentation now states the exception in both the Part 3 specification and package system document.

No gameplay source, localisation, AI weight, probability fixture, workbook, asset, map, GUI, admission list, or exported CSV changed in this reconciliation. Native decision-row rendering remains unavailable, so visual cost fit and hover behavior are not claimed. Event 006 remains **HOLD / PARTIAL** under the current completion audit.
