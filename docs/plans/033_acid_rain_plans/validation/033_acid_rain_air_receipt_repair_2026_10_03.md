# Acid Rain authoritative Air receipt repair

Disposition: source repair implemented and source/model checks passed; executed acceptance remains unresolved.
Acceptance basis: the user requires gains no larger than the request, 1500 bp lifetime additions, a 5000 bp global ceiling, and one actual applied receipt for every addition.

## Source defect and repair

The Event 033 gateway read `air_contamination_source_applied_delta_bp` after calling the central mutation.
The central mutation writes that source-registration scratch, then calls `air_contamination_refresh_values`, which reuses and zeroes it while synchronizing other source rows.
It is therefore not a stable returned addition, even if the caller declares storage for it.
The source ledger can record a positive addition while Event 033's mirror remains stale.
Using that stale mirror to calculate a remaining lifetime allowance can permit a request larger than the source row's true remainder.
This is a source-confirmed contract weakness, not a claimed observed live cap violation.

The gateway now synchronizes its lifetime mirror from the authoritative Acid Rain source row before any eligibility/clamp work, including blocked requests.
Its lifetime remainder therefore comes from the actual persistent source ledger across reloads and generations.
After the mutation it uses the existing caller-owned `air_contamination_delta_bp`, which the central effect replaces with the actual clamped global change.
Event 033 adds that positive result once to its generation total and current contribution, and reads its lifetime mirror from the source row that already recorded the addition once.
It does not add a second lifetime source receipt.
No shared Air mutation helper or numeric cap was changed.

The gateway's non-formation minimum is zero, so it cannot raise an incoming zero or negative request into a positive gain.
The host's existing authored weekly request calculation retains its normal minimum/maximum pressure range.
Formation, weekly work, and all evolution contributions still use one gateway.
Disabled Air, irreversible contamination, permanent Fallout pressure, exhausted lifetime, and global-ceiling gates remain intact.

## Review and checks

The parent read `air_contamination_apply_delta_bp`, source registration, and source refresh directly, including the overwrite of source scratch.
Source regression assertions check pre-clamp lifetime synchronization, stable actual-return selection, no minimum request increase, and one central mutation call.
`033_acid_rain_air_receipt_final_checkpoint_2026_10_03.json` passes those assertions and the existing synthetic suite.
Its Air model covers 701213 requests in 10000 seeded sequences with zero modeled cap violations.
Explicit cases cover zero/negative requests, 1499/1500 lifetime, 4999/5000/above-ceiling global contamination, and stale Event 033 mirrors while the authoritative source has 1499 or 1500 bp.
The stale-mirror fixtures require one bp at 1499 and zero at 1500; blocked requests still publish the correct lifetime mirror.
These fixtures model the accepted arithmetic and do not execute the Clausewitz helper or prove live temporary-output persistence.

The checkpoint's Event 033 runtime source hash is `4c2290eaa8d4a65fe603de3405ed269a1d1d63703042fc1b17d54b4d8fa4dc13`.
That hash also includes separately owned uncommitted achievement/census integration, which is excluded from this repair's commit scope.
The shared central source was reviewed at its current local revision; its mutation and refresh ordering are the dependency contract, not an invented new API.
Offline Data structures lines 437–442 and installed temporary-variable documentation support the caller-owned input/output lifetime rule.
The task's reference routes and bounded event/probability inspections have returned documented 600-second timeouts; no engine or MCP certificate is inferred from local source review.

## Scope and remaining gates

Owned changes are the three Air-gateway hunks in `033_acid_rain_effects.txt`, Air-only validator cases/assertions, the Event 033 mutation paragraph in `docs/systems/air_cleanliness/contamination_source_ledger.md`, and this report.
Mortality-helper, achievement, census, aftermath, GUI, decision, and unrelated shared changes remain separate tranches.
Native formation/weekly/evolution execution, actual source/global/event deltas, disabled settings, interruption, reload, multiplayer determinism, and a second generation remain required.
No loss of existing contamination, duplicate shared Chaos, or substitute source is authorized.
This is not a full Event 033 completion or clean-error-log claim.
