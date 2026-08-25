# Event 016 sparse Alien landing-state registry handoff

> Superseded by the country-scoped ownership fix documented in `016_alien_dhrondan_country_scoped_registry_2026-08-26.md`. The original global-array design below is retained as historical evidence only; current runtime code uses a regular country-scoped `alien_infantry_landing_state_registry`.

## Scope

The accepted D’Rhondan revolt path previously counted and claimed marked landing states with two one-time `every_state` scans. The original tranche introduced a sparse global array of state scopes, but that design was superseded because it allowed independent Alien Infantry providers to contaminate one another’s revolt inputs.

## Implementation

- Added the internal `alien_infantry_register_landing_state` effect beside the public landing API.
- The superseded implementation inserted every successful ordinary landing and Event 019 deferred commit into `global.alien_infantry_landing_state_registry`; the current implementation instead inserts the state into the caller country’s `alien_infantry_landing_state_registry` only after a successful commit.
- Replaced the superseded global loops in `dhrondan_capture_revolt_inputs` and `dhrondan_release_and_transfer_landing_states` with loops over the pact host’s country-scoped registry.
- Updated the public API reference to make the registry API-owned and prohibit parallel landing ledgers.

## Validation boundary

The touched Clausewitz files remain brace-balanced and contain no recurring world iterator. The registry is populated by the current landing API and is idempotent per state. No automatic migration scan was added for legacy saves whose state flags predate this registry; those saves need a controlled migration decision before being treated as equivalent to a fresh post-change save. Full engine execution of the registry loops remains a required MCP/live-consumer validation step and is not claimed here.
