# Event 006 overlay-category visibility repair

## Status

Bounded source repair complete. The thirteen minor overlay decision categories now require the shared `is_independence_wave_overlay_runtime_unlocked` predicate in their own `visible` blocks, so category registration cannot expose an overlay before the root Event 006 transaction publishes its committed result. No pressure values, missions, decisions, costs, ideas, overlay refresh behavior, package admission, AI weights, or country identities were changed.

## Evidence reviewed

The offline Paradox wiki `Data structures`, `Triggers`, `Effects`, `Decision modding`, and `Localisation` pages were used alongside the vanilla decision-category structure. The existing Event 006 trigger registry defines `is_independence_wave_overlay_runtime_unlocked` as the post-event global marker, and every overlay route-active predicate plus normal refresh initializer already uses that gate. The category audit identified the remaining direct UI registration surface because its thirteen category blocks previously relied only on their local `*_overlay_active` predicates.

## Changed file

- `common/decisions/categories/006_independence_wave_categories.txt`
  - Added `is_independence_wave_overlay_runtime_unlocked = yes` to IW-005, IW-022, IW-025, IW-035, IW-059, IW-085, IW-101, IW-102, IW-105, IW-156, IW-196, IW-197, and IW-204 category visibility blocks.

## Validation

The Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 scenario-matrix audits pass. A focused source assertion confirms all thirteen category blocks contain the explicit unlock gate. Fresh `hoi4.event_inspect` and `hoi4.event_render` calls for `chaosx.nr6.1` remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with `artifactCount:0`, so no MCP or live-runtime claim is made.

## Remaining boundary

The whole Event 006 package remains HOLD / PARTIAL at the existing 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. The absolute no-pre-event surface is preserved. Unattested package identities, rights-cleared assets, typed probability evidence, and the MCP artifact-manifest repair remain outside this bounded change.

No staging or commit was performed by this handoff.
