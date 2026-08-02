# Event 012 RSA rejected-roster cleanup

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

The fire-once prefire pass freezes three to five contact governments before validating the selected host.

When the selected host failed the final generic-or-RSA readiness check, the pass left `africa_prefire_contacts_frozen`, `africa_frozen_first_contact_count`, the frozen target array, and contact-role flags on the selected governments.

For original SAF, that stale roster could make a later attempt fail the bounded exile-patron gate even after a new contact set would have been valid.

## Change

`common/scripted_effects/012_africa_effects.txt` now calls the existing `africa_clear_frozen_first_contact_context` helper when `africa_prepare_random_event_fire` has a selected prefire host but the final readiness check fails.

The cleanup is scoped to the rejected selected host and does not select a fallback, create a new tag, or reopen a world scan.

## Expected behavior

- A valid prefire host still sets `africa_prefire_ready` and proceeds to the existing dispatcher.
- A rejected host has its frozen roster and contact-role flags cleared before the effect chain returns.
- A later explicit attempt can rebuild a fresh bounded roster.
- Generic and RSA host eligibility predicates remain unchanged; the RSA patron-pool filter and final post-freeze gate remain authoritative.

## Validation boundary

Static source inspection confirmed the cleanup helper clears the regular roster array, count variable, frozen flag, and all three contact-role flags on each frozen government.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so repeated prefire attempts and patron-selection outcomes remain open acceptance work.
