# IW-048 UDM strategic payment alignment handoff

Date: 2026-08-15

## Disposition

Implemented a narrow package-local cost-payment correction in `common/decisions/006_independence_wave_udm_decisions.txt`.

IW-048 remains fail-closed and is still absent from central adapter, content attestation, normal/scenario preflight, dispatcher, deterministic Join, and workbook authority.

## Source defect and correction

`independence_wave_udm_settle_former_host_ledgers` used `can_pay_independence_wave_udm_strategic_cost`, `independence_wave_udm_cost_strategic`, and the UDM civilian-factory modifier, but its completion effect called only `independence_wave_decision_pay_diplomatic_standard`.

`independence_wave_udm_open_volga_ural_corridor` had the same mismatch between its strategic cost gate/text and diplomatic-only payment effect.

Both completion effects now call `independence_wave_decision_pay_strategic`, which includes the shared stability and war-support payment before the shared diplomatic-standard payment.

No trigger, duration, AI factor, ledger delta, route gate, asset, identity, central adapter, attestation, preflight, or Join surface changed.

## Validation

- UDM decision source braces remain balanced at 230 opening and 230 closing braces.
- Both corrected decision blocks contain the UDM strategic affordability trigger, strategic cost text, and strategic payment effect, with no diplomatic-only payment remaining.
- The Event 006 allocator audit remains at 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and adapter-only IDs IW013, IW015, IW043, IW058, IW093, IW098, IW177, and IW179.
- The SCN-008 scenario matrix, Event 006 flag-family audit, and country API audit remain passing at this authority boundary.

## Limits

The installed MCP exposes no decision-card inspect/render route, and no live-game validation was performed.

The correction is package-local source alignment only and does not justify an IW-048 admission or any quantitative balance claim.
