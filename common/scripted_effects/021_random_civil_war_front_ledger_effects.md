# Event 021 front ledger effects

The companion source owns exact precommit validation and transaction-owned front receipts.
It uses the existing global plan arrays and tuning constants; it introduces no per-crisis country, state, front, actor, or division ceiling.

## Contracts

`event021_parent_release_completed_front_plan` runs on the successful current opening host after its public wrapper's mutation executor returns.
It requires matching host/front/crisis IDs, current registration, durable opening-stage provenance, consumed host status, a matching proved primary except for same-tag contests, and no active planning/child callback.
Every row must be consumed or explicitly rejected.
It then releases only the serial template/readiness/markers and pending opening-stage scratch, without unregistering any live front.
Incomplete or mismatched frames remain available to resolution checks and are not cleared merely because the caller is active.
Example: invoke it directly after each ordinary, complete Event 006, or same-tag mutation executor returns.

`event021_parent_validate_front_ledger_spans` accepts ANY scope after the existing parallel-array and capacity checks.
It leaves `event021_planned_front_plan_valid` unchanged on success and sets it to zero on failure.
Missing pending identity or host pointers fail closed.
The identity helper requires the exact host and primary prefix, or the single same-tag control row, before indexed reads.
The member helper requires positive integer counts, contiguous exhaustive spans, unique positive front IDs, unique states, host ownership, complete ordinary host coverage, and an anchor within each row's span.
There is no live-map replacement for a missing row.
Side effects are temporary scratch only; the parent validator alone publishes readiness.
The member helper preinitializes `event021_ledger_count` before each row-span helper call, because it consumes that helper's count afterwards to accumulate the exact next offset.
The validity scalar `event021_planned_front_plan_valid` must already have caller-owned storage before entering the span-validation chain.
Example: call `event021_parent_validate_front_ledger_spans = yes` after alignment checks and before setting `random_civil_war_front_plan_ready`.

`event021_parent_validate_secondary_transfer_receipt` runs in the exact recorded secondary source country before `start_civil_war`.
While an Evolution I review holds `random_civil_war_active_front_commit_in_progress`, it delegates to `event021_parent_validate_active_secondary_transfer_receipt`, which applies the same exact-span, marker, remnant, and division checks to the reviewing government's own receipt row instead of the global opening template.
Inputs are the validated plan, pending child ID, source front ID, staged markers, current state control, and live division count.
It requires an exact marker/state count, every selected state owned and controlled by that source, a surviving controlled remnant, and a positive division request smaller than the live army.
The marker count covers all controlled states admitted by the engine filter, not only owned states.
The created secondary's copied count must also equal its total owned-state count, so additional transferred territory cannot pass a subset-only check.
The default output `event021_secondary_transfer_valid` is zero.
The secondary starter preinitializes this temporary output before each receipt-helper call so its success survives return and later revalidation cannot consume stale success.
On success it publishes the verified pending state count and recalculates the child army ratio from requested divisions divided by the current source army.
It changes no ownership, registry, or units.
Example: call it before the secondary starter's availability gate and again after loading parser-sensitive ratio inputs.
The second result gates the entire native mutation path, including missile split preflight and every government branch, with the final fallback inside the same guard.
Failure uses `event021_parent_reject_secondary_transfer` to preserve the initial rejection path's cleanup and never reaches `start_civil_war`.

`event021_parent_refresh_retained_front_receipt` runs on a registered country after all optional openings finish.
It rebuilds `random_civil_war_opening_core_states` from states in the immutable transaction ledger that remain owned by that exact country, including rejected child regions.
Only active registered actors with the current pending crisis ID may refresh; a stale actor list cannot rewrite another crisis's receipts.
It updates the count, measured force receipts, and the matching registry region count without adding a second registry row or changing capacity.
`random_civil_war_opening_provenance_states` preserves the historical opening separately.
Example: the host invokes the helper for its stable opposition-actor array and then for itself after optional activation.

## References and validation limits

Installed `documentation/effects_documentation.md` lines 2278-2292 document array appends; lines 4279-4335 document array indexes, scope iteration, and numeric loop arguments; lines 8030-8059 document the civil-war child effect scope.
The installed revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` lines 1069-1077 and 1210-1221 document scoped persistent arrays, unscoped temporary arrays, scope traversal, and the numeric loop ceiling.
Its revision is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` line 197 documents a maximum of five displayed decimals.
The ordinary and secondary engine ratio injections retain those five decimals; they do not promise exact integer division transfers or override engine fixed-point precision.
The installed annex effect is documented at lines 2495-2500, and the offline Effects page describes `transfer_troops = yes` at line 1504.
Installed `documentation/dynamic_variables_documentation.md` lines 670-676 document `num_owned_states` at revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`; offline Data structures line 1524 gives the same ownership definition.
A created child with an invalid exact receipt is not registered and is annexed back into its recorded immediate source with troops transferred.
The callback ordering and force rounding still require engine evidence.

No image, portrait, GUI, animation, super-event, or 3D asset is introduced.
Future consumers should retain explicit owners, immutable transaction membership, separate provenance, exact count checks, and array traversal rather than numeric traversal over variable-length ledgers.
