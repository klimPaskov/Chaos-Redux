# Event 006 FORM-01 authorization cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented a dedicated diplomatic-standard/standard-factory cost triplet for `independence_wave_form0124_authorize_full_integration`. The decision already reserves two civilian factories but previously selected the generic diplomatic card, which disclosed no factory burden.

## Changes

- The decision now selects `independence_wave_cost_diplomatic_standard_factory_standard`.
- Added the matching base, `_tooltip`, and `_blocked` localisation keys showing the existing diplomatic command-power/convoy values plus `civilian_factory_standard`.

## Boundary

No invitation-family gate, compact-control requirement, affordability trigger, payment effect, AI score, duration, cancellation, cleanup, formable membership, admission, Join, or catalog behavior changed. The existing standard factory modifier remains authoritative.

Existing concurrent constant-token and invitation-cancellation edits in the same FORM-01/02/04 decision file were preserved and are outside this handoff.

## Validation

The three new localisation keys occur once with the UTF-8 BOM intact. The authorization block resolves to the new selector beside its standard factory modifier. This text-only selector repair changes no weighted or eligibility surface, so no probability compare is meaningful; allocator and SCN-008 matrix audits remain passing at 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder.
