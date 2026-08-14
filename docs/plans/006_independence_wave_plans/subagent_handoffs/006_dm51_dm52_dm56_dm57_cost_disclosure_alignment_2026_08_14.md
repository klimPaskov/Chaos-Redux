# Event 006 DM-51, DM-52, DM-56, and DM-57 cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented a bounded selector/localisation repair for four accepted decisions whose visible cost cards omitted or understated an existing civilian-factory reservation.

## Changes

- DM-51 `independence_wave_prepare_border_ultimatum` now selects `independence_wave_cost_border_ultimatum_major`, whose base, `_tooltip`, and `_blocked` keys disclose the existing major factory commitment.
- DM-52 `independence_wave_integrate_settled_district` now selects `independence_wave_cost_integration_major`.
- DM-56 `independence_wave_integrate_member_region` now selects the same dedicated integration-major triplet.
- DM-57 `independence_wave_sponsor_another_breakaway` now selects `independence_wave_cost_breakaway_sponsorship_standard_factory`, whose triplet discloses its existing standard factory reservation.

The selectors match the live `CIVILIAN_FACTORY_MAJOR` or `CIVILIAN_FACTORY_STANDARD` modifiers and the accepted decision-mission matrix. Shared standard-tier keys were not changed because they remain correct for their other callers.

## Boundary

No affordability trigger, payment effect, AI score, target gate, duration, cancellation, cleanup, admission, Join, package, or catalog behavior changed. DM-51/52/56/57 retain their existing border, integration, formable, high-chaos, generation, cooldown, and route guards.

Other cost-disclosure findings remain queued for their owning formable/package surfaces where dedicated keys or admission review are required. This tranche does not normalize unadmitted package callers or change shared generic cost semantics.

## Validation

The localisation file retains its UTF-8 BOM. The nine new localisation keys (three complete triplets) occur once each, and all four decision blocks resolve to the new selectors while retaining their existing factory modifiers. The scoped source diff is selector-only; no weighted or eligibility surface changed, so a probability compare is not meaningful for this repair.
