# IW-050 KOM strategic payment alignment handoff

Date: 2026-08-15

## Disposition

Implemented a narrow package-local cost-payment correction in `common/decisions/006_independence_wave_komi_decisions.txt`.

IW-050 remains package-local and fail-closed, outside central adapter, content attestation, normal/scenario preflight, dispatcher, deterministic Join, and workbook authority.

## Source defect and correction

`independence_wave_komi_settle_former_host_ledgers` used the KOM strategic affordability trigger and cost text but completed with only `independence_wave_decision_pay_diplomatic_standard`.

`independence_wave_komi_open_northern_ural_corridor` had the same strategic-cost and diplomatic-only-payment mismatch.

Both completion effects now call `independence_wave_decision_pay_strategic`, which includes the shared stability and war-support payment before the shared diplomatic-standard payment.

The Pacific custom strategic-cost decisions were not changed because they already call their dedicated `independence_wave_pacific_pay_island_strategic_cost` effect.

No trigger, duration, AI factor, ledger delta, route gate, asset, identity, central adapter, attestation, preflight, or Join surface changed.

## Validation

- KOM decision source braces remain balanced at 235 opening and 235 closing braces.
- Both corrected decision blocks contain `can_pay_independence_wave_komi_strategic_cost`, `independence_wave_komi_cost_strategic`, and `independence_wave_decision_pay_strategic`, with no diplomatic-only payment remaining.
- The Event 006 allocator, SCN-008 scenario matrix, flag-family, and country API audits remain passing at 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and 161 unattested rows.

## Limits

The installed MCP exposes no decision-card inspect/render route, and no live-game validation was performed.

The correction is package-local source alignment only and does not justify IW-050 admission or any quantitative balance claim.
