# Event 006 DM-49 and DM-50 cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented a bounded selector-only repair for two accepted border decisions. Both decisions already reserve the major civilian-factory tier and use the strategic payment helper; their visible cards now select the matching major strategic cost triplet.

## Changes

- `common/decisions/006_independence_wave_decisions.txt:3065` — DM-49 `independence_wave_sponsor_plebiscite` now selects `independence_wave_cost_strategic_major`.
- `common/decisions/006_independence_wave_decisions.txt:3147` — DM-50 `independence_wave_negotiate_transfer` now selects `independence_wave_cost_strategic_major`.

The existing `independence_wave_cost_strategic_major`, `_tooltip`, and `_blocked` localisation triplet displays `civilian_factory_major`, matching the existing `CIVILIAN_FACTORY_MAJOR` reservations and the accepted matrix's three-factory burden.

## Boundary

No trigger, payment effect, AI score, target gate, duration, cancellation, cleanup, admission, Join, package, or catalog behavior changed. DM-49 and DM-50 retain their existing border-operation and generation guards.

The remaining scan findings are intentionally queued for their owning surfaces: dedicated border/integration/breakaway triplets, FORM-03 light-factory disclosures, and admitted package/formable callers with separate ownership or admission boundaries. Shared generic keys were not modified.

## Validation

The scoped decision diff contains only the two DM-49/DM-50 selector changes alongside the separately documented DM-10/DM-36 repair. Allocator and SCN-008 matrix audits remain passing at 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder. The source changes do not alter a weighted or eligibility surface, so no probability compare is meaningful for this text-only repair.
