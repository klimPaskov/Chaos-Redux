# Event 006/Event 021 adapter predicate narrowing

Date: 2026-09-01.

## Scope

This tranche narrows the shared Event 006 lifecycle and package-content predicates after the read-only Event 021 adapter audit in `006_event6_event021_content_predicate_audit_2026-09-01.md`.

Changed files:

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`

## Implementation

`is_independence_wave_active_country` is strict again: it requires the real Event 006 active-origin flag, the Event 006 liberation origin, and a non-ended origin.

The transient Event 021 adapter window is accepted only by `is_independence_wave_package_content_active`, and only when both adapter setup flags and `has_valid_independence_wave_setup_input` are true. This permits the existing country-scoped setup refresh and package dispatch to consume validated setup data without exposing the adapter as an active Event 006 country.

The proven origin-neutral adapter receipt branch remains unchanged and still requires all four receipt flags, a package id, and the active-origin/ended exclusions.

The Scotland package predicate now relies solely on the shared package-content helper; its duplicate preparing/completed adapter bypass was removed.

## Contract and safety

No Event 006 fired-count, active-country registry, evolution, network, league, UI, or history state is admitted by the transient branch. Event 005 origin separation and the existing Event 006 origin guards remain intact. No package ids, force profiles, costs, or country identities were changed.

The Event 021 registry entries `iw_070`–`iw_072` remain a separate fail-closed decision because their package predicates still require the Event 006 liberation origin; this tranche does not weaken those guards.

## Validation

The parent should rerun the focused Event 006 allocator, country API, flags, FORM-16, scenario-matrix, and GUI-matrix validators against the resulting working tree. Fresh live execution is not claimed; the available Event MCP route remains partial and defers workspace-wide helper/lifecycle projections.

## Ownership and remaining risk

No other Event 006 or Event 021 files were intentionally edited here. A stale adapter receipt after an interrupted transaction remains governed by the existing abort and absorbed-adapter cleanup paths and requires live evidence to close.
