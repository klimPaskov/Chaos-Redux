# Runtime validation and isolation record

## Production registrations

The pilot `.mesh`, `.anim`, texture, `.gfx`, `.asset`, building, unit, and
localisation files are present in the production repository paths. A direct
full Chaos Redux launch was attempted after the pilot wiring was added. It
exited before the main menu with errors including
`interface/fallout_world_end.gui`, `common/script_constants/014_cannibalism_constants.txt`,
and a `PHYSFS_swapULE64` access violation. The full launch produced no
pilot-specific entity or animation error after the state bindings were corrected
to use the local pdxmesh animation IDs.

## Exact isolation

The exact pilot files were temporarily removed to a bounded
`tmp/3d_pipeline/isolation_backup/` directory, the full Chaos Redux launch was
retried, and the same pre-menu crash occurred. Every pilot path was restored and
verified. This isolates the full-mod crash from the pilot package without
silently weakening the production runtime files.

## Minimal live showcase

The user-facing standalone `3d_pipeline` copy is the bounded test mod. It
copies the production runtime registrations and compiled artifacts, then adds
the Brandenburg building and Germany unit consumers needed to exercise both
pilots. The original history-only consumer did not appear in the user's run;
the active copy now applies both consumers through `on_startup` and the
Germany-only `on_daily_GER` repair hook. The unit/template effect remains
country-scoped for template creation, while the building and `create_unit`
effects run directly inside state 64. Final status still requires unobstructed
renderer screenshots from that showcase.

## Historical live-validation waiver

The user explicitly instructed on 2026-07-22 that HOI4 did not need to be run.
That waiver remains retained as historical evidence, but it is not a passing
renderer test and does not replace the current live verification after the
consumer repair.
