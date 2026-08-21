# Event 006 roster checkpoint release fix

## Scope

The Banat, Thrace, and Epirus package setup effects no longer depend on a hidden `country_event = { id = chaosx.nr6.350 }` receipt being available before the same setup transaction continues.

## Changed files

- `common/scripted_effects/006_independence_wave_banat_package_effects.txt`
- `common/scripted_effects/006_independence_wave_thrace_package_effects.txt`
- `common/scripted_effects/006_independence_wave_epirus_package_effects.txt`

Each setup now checks its package-specific command-roster trigger directly before setting `independence_wave_command_roster_ready`.

## Runtime intent

AXX, BAX, and BBX already carry their approved command characters in the fixed-tag history roster, so their release-time setup can validate the roster synchronously without a queued event callback.

The change does not restore the retired pre-event crisis category, pressure, queue, or decision surface, and it does not alter the compact Event 006 decision-cost localisation.

## Validation

The current package trigger files contain fixed anchor-state checks rather than `capital_scope`, and the supplied source tree has no Event 006 package trigger at the reported invalid `capital_scope` call sites.

The broader Event 006 allocator remains fail-closed for unattested packages; this handoff does not synthesize package content or bypass central content attestation.
