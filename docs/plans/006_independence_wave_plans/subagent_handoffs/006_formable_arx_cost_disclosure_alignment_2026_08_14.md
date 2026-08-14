# Event 006 FORM-02, FORM-04, and IW-018/ARX cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented three selector-only repairs for admitted/formable decisions that reserve one civilian factory but selected the generic diplomatic card without a factory disclosure.

## Changes

- `independence_wave_form02_chart_convoy_routes` now selects `independence_wave_cost_diplomatic_standard_factory`.
- `independence_wave_form04_establish_public_peace_court` now selects `independence_wave_cost_diplomatic_standard_factory`.
- IW-018/ARX `independence_wave_arx_restore_cagliari_shipping_office` now selects the same existing factory-aware triplet.

All three decisions retain their existing diplomatic-standard affordability triggers, one-factory modifiers, payment effects, focus integration, target/route gates, durations, and cleanup. The reused triplet already displays the standard diplomatic resources plus the light factory reservation.

## Boundary

No shared generic localisation key, formable membership rule, package admission, Join, AI score, payment helper, timing, cancellation, or cleanup logic changed. Other formable callers with security or custom administrative/diplomatic costs remain queued for dedicated owner-reviewed triplets.

## Staging boundary

The three selector lines were staged selectively. Existing concurrent constant-token and formable cancellation edits in the same decision files remain unstaged and untouched by this handoff.

## Validation

The existing factory-aware triplet resolves in localisation, each selector sits beside a light factory reservation, and the staged diff contains exactly three selector replacements. Allocator and SCN-008 audits remain passing at 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder. This text-only repair changes no weighted or eligibility surface, so no probability compare is meaningful.
