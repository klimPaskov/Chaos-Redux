# Event 20 remaining launch errors patch handoff

## Scope and issues

- High: five mission `allowed` blocks expanded scripted predicates containing unsupported `exists = yes`, producing load errors at shared-response lines 806, 837, 867, and 889 and Rat King line 893.
- High: `gulag_labor_camp_network` was dynamically allocated but absent from the synchronized-token registry, risking multiplayer OOS allocation.

## Changed files and identifiers

- `common/decisions/020_black_plague_shared_response_decisions.txt`: `black_plague_shared_strike_the_crown_mission`, `black_plague_shared_seal_royal_burrows_mission`, `black_plague_shared_last_response_hold_mission`, and `black_plague_shared_last_response_refuge_mission`.
- `common/decisions/020_black_plague_rat_decisions.txt`: `black_plague_rat_king_crown_the_continent_mission`.
- `common/synchronized_dynamic_tokens/chaosx_tokens.txt`: `gulag_labor_camp_network`.

## Before and after

Each affected mission previously used a scripted role predicate in `allowed`; those predicates begin with `exists = yes`, which the mission `allowed` parser rejects.
The five blocks now use `allowed = { always = yes }`.
Their intended lifecycle gate is unchanged: each appears only when its existing owner-only activation flag is set by its matching start flow, and existing availability, cancellation, completion, timeout, and cleanup effects remain untouched.
The Gulag labor-network token is registered next to the other synchronized dynamic lookup tokens.

## Decision and mission notes

The affected surface is activation-driven rather than a passive decision store.
The four human missions are activated by their matching human response start path, while the Rat King mission is activated by the continent-crown decision after it charges the existing royal-meter costs.
No costs, requirements, timers, AI weights, localisation, scripted GUI surface, success/failure outcome, or route lock was changed.
No new exploit or stale-cleanup path was introduced because activation, cancellation, and resolution logic is unchanged.

## Validation

- Confirmed all five reported line locations now use the parser-safe `allowed = { always = yes }` form and retain their original activation flags.
- Confirmed the synchronized-token file contains exactly one `gulag_labor_camp_network` entry.
- Ran a scoped diff check on the three gameplay files.

## Skipped validation and remaining issues

No game launch or live mission execution was run; that belongs to the parent/user validation flow.
No unresolved issue remains within this three-file patch scope.
The unrelated warnings and errors in the supplied log remain outside this handoff's ownership.
