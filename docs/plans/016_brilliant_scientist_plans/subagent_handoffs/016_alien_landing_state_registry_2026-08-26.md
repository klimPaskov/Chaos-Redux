# Event 016 sparse Alien landing-state registry handoff

## Scope

The accepted D’Rhondan revolt path previously counted and claimed marked landing states with two one-time `every_state` scans. The API now owns a sparse global array of state scopes so revolt setup can operate only on states that have actually received an Alien Infantry landing.

## Implementation

- Added the internal `alien_infantry_register_landing_state` effect beside the public landing API.
- Every successful ordinary landing and every Event 019 deferred commit inserts its selected state scope into `global.alien_infantry_landing_state_registry` only when that scope is not already present.
- Replaced `every_state` in `dhrondan_capture_revolt_inputs` with a `for_each_scope_loop` over the registry and returned the count to the host country through `ROOT`.
- Replaced `every_state` in `dhrondan_release_and_transfer_landing_states` with the same registry loop for DHR claims.
- Updated the public API reference to make the registry API-owned and prohibit parallel landing ledgers.

## Validation boundary

The touched Clausewitz files remain brace-balanced and contain no recurring world iterator. The registry is populated by the current landing API and is idempotent per state. No automatic migration scan was added for legacy saves whose state flags predate this registry; those saves need a controlled migration decision before being treated as equivalent to a fresh post-change save. Full engine execution of the registry loops remains a required MCP/live-consumer validation step and is not claimed here.
