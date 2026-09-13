# Event 33 mission cleanup repair handoff

Status: implemented and parser-accepted in launch 16, with campaign migration behavior still untested.

Acceptance basis: the parent authorized the initial two keyword repair and then authorized deletion of the two stale references after launch 15 showed that the supported effect still resolves the absent mission IDs and emits native errors.

## Scope and changed files

The only gameplay source changed by this repair is `common/scripted_effects/033_acid_rain_effects.txt`.

The affected helper is `acid_rain_migrate_legacy_runtime` at lines 351-390.

The affected legacy identifiers are `chaosx_acid_rain_timeout` and `chaosx_acid_clouds_timeout`.

The initial source contained two unsupported `cancel_mission` calls at lines 381-382.

The first bounded edit changed those two keywords to the documented `remove_mission` effect, and the second bounded edit removed the two stale calls after native validation proved that the absent IDs were not accepted as a no-op.

No decision, mission definition, event, GUI, localisation, AI weight, cost, or unrelated source file was changed.

No replacement mission definitions or compatibility stubs were added.

## Before and after behavior

Launch 14 reported `Invalid effect 'cancel_mission'` for both calls at lines 381-382 and then reported the corresponding unknown effect type at line 387 in `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_14/logs/error.log` lines 1040-1043.

The documented keyword repair removed those parser errors, but launch 15 reported `Invalid Decision ID for activate_mission chaosx_acid_rain_timeout` and `Invalid Decision ID for activate_mission chaosx_acid_clouds_timeout` at `effectimplementation.cpp:14462` in `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_15/logs/error.log` lines 1273-1274.

The same two missing-decision diagnostics were repeated later in the launch 15 log, confirming that the supported cleanup effect resolves the mission identifier through the mission database even when the ID is absent from the current definitions.

The final source removes both stale calls.

The surrounding one-time migration guard, migration receipt and lock, prototype modifier removal, legacy flag removal, legacy variable cleanup, and legacy array cleanup remain unchanged.

The current Event 33 runtime therefore reaches the existing cleanup that is backed by current data without attempting to resolve obsolete mission IDs.

## Scope and lifecycle proof

`events/033_acid_rain.txt:7` defines the root event `chaosx.nr33.1`.

`events/033_acid_rain.txt:12` invokes `acid_rain_start_runtime` directly in the country event's immediate block.

`common/scripted_effects/033_acid_rain_effects.txt:1022` defines `acid_rain_start_runtime`.

`common/scripted_effects/033_acid_rain_effects.txt:1027` invokes `acid_rain_migrate_legacy_runtime` from that country-scoped helper without an intervening state or country-target switch.

The migration helper's two obsolete mission calls were after the nested `every_state` block, so deleting them does not alter the state-scope traversal or any state-level modifier cleanup.

The helper is guarded by the legacy-state predicate and `NOT = { has_global_flag = acid_rain_migration_receipt }`, so it remains a one-time migration path.

The Event 33 migration specification calls the two IDs old prototype missions and lists their removal after new receipts exist in `docs/specs/033_acid_rain_specs/specs/033_acid_rain_spec_part_11_integrations_migration_and_save_safety.md` lines 176-193 and the old-save migration step 9.

The current runtime has no definition or activation path for either ID.

An exact search across `common`, `events`, `decisions`, `on_actions`, `interface`, and the active Event 33 source finds no current definition, `activate_mission`, `has_active_mission`, or other runtime reference after the deletion.

The exact IDs remain only in the historical recovered candidate under `docs/plans/033_acid_rain_plans/recovery/033_acid_rain_effects_recovered_candidate.txt`, the migration specification, and the localisation audit's record of removed obsolete rows.

The recovered candidate is documentation under `docs/plans` and is not a loaded game source file.

## Absent-ID assessment

The offline Effects wiki documents `remove_mission` as a country-scoped effect that removes a specified mission.

The installed vanilla `documentation/effects_documentation.md` at lines 6083-6090 documents the same country scope and states that removal skips complete and timeout effects.

The offline Decision modding page explains that mission IDs are decision definitions and that mission activation resolves a mission name from the decision database.

The current `common/decisions` tree contains no definitions for `chaosx_acid_rain_timeout` or `chaosx_acid_clouds_timeout`.

Launch 15 is direct engine evidence that an absent ID is not a supported no-op in this source state because the `remove_mission` references produced `Invalid Decision ID for activate_mission` diagnostics.

The final deletion is therefore the safe bounded repair for the current runtime.

The old-save specification still describes removal of the obsolete missions, but the current engine cannot resolve those removed definitions and no replacement migration mechanism was authorized in this task.

That old-save mission-removal substep is the only intentional omission from the original prototype migration contract; all current Event 33 runtime cleanup remains in place.

## Backup and hash guard

The exact source before the first keyword repair is archived at `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\testing\live_qa\2026-09-04_catalog_01\pre_patch_event33_mission15\common\scripted_effects\033_acid_rain_effects.txt`.

The pre-keyword-repair archive SHA-256 is `80EE86FCF91DC0938A04E9ED13F0EC5E8B05C8678BFBDE80B4C4D17CD2F4F919`.

The exact intermediate source containing only the two supported `remove_mission` calls is archived at `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\testing\live_qa\2026-09-04_catalog_01\pre_patch_event33_mission15_remove\common\scripted_effects\033_acid_rain_effects.txt`.

The pre-deletion archive SHA-256 is `23810ED05885E7E5FB5B469162750D692317E6D695C3822C530613A70A5EF53D`.

The final working source SHA-256 is `B3274CAFF6F80424349FB57101144A8CCC4D81DA805C0AD21647A0A66081BFF5`.

The normalized diff against the intermediate archive contains exactly two deleted lines and no other gameplay changes.

## MCP evidence

The mandatory narrow Event 033 trace was run before the keyword repair with selector `{kind:event,eventId:chaosx.nr33.1}`, direction `both`, `maxDepth=2`, `maxNodes=30`, `maxEdges=60`, and helper expansion enabled.

The pre-keyword trace returned `EVENT_INSPECTED_PARTIAL` with artifact SHA-256 `51405A30BF73E8E9E54DA8A9E3D56D6F5F25B7B992152D2779A2C451B43795BB`, revision `94c858964b40bbc800c3b1257959c1f255c4f0b3d793261b508a3135a0b5f9cc`, graph hash `cd1c8b663f31f3f65c1161e5793833a89c7bac3bcf77da7fa0188c074c412d5c`, and `helpers=0`.

The post-keyword trace returned `EVENT_INSPECTED_PARTIAL` with artifact SHA-256 `7FA065423CF4D11ACE22DF8615D8AB538B944E031375B756EE991E9713C86732`, revision `a900b9ddbec87f6e514327c97653bcb663a4e1c1fa6ec77da212255823afb05c`, graph hash `de1f0da52ce5d16a06255dda02e8fb0d48471049a3a83d5ae28fe8daf176f851`, and `helpers=0`.

The trace route reported `MCP_INLINE_FILES_TRUNCATED` and deferred workspace-wide helper and lifecycle projections, so it is linkage evidence rather than parser acceptance.

The read-only trace issued after deletion returned the same cached post-keyword artifact and revision, so MCP did not provide a distinct final-source artifact for the deletion.

A single accepted-shape read-only `hoi4.event_compare` request used the recorded pre-deletion revision `a900b9ddbec87f6e514327c97653bcb663a4e1c1fa6ec77da212255823afb05c` for both the before and after graph inputs with `refresh=true`, `render=false`, and `maxRenderNodes=5`.

That compare returned status `error`, code `EVENT_REVISION_NOT_CACHED`, zero artifacts, and blocker `Requested event graph revision is not cached`.

No MCP comparison result is claimed because the recorded graph revision was unavailable to the compare route.

The native launch 15 result and the source-level exact-ID search were the decisive evidence for the deletion.

Launch 16 completed frontend startup in 58391 ms against the final source hash and reduced the two Event 33 legacy mission diagnostics from 10 occurrences to zero.

The launch 16 error log contains no `chaosx_acid_rain_timeout` or `chaosx_acid_clouds_timeout` diagnostics, and no new diagnostic family attributable to this deletion was observed beyond an aggregate error count line.

This is parser and startup acceptance for the stale-reference repair; the parent has not yet exercised an old-save migration or confirmed the legacy cleanup behavior in a campaign.

## Validation and skipped validation

The source snippet was inspected before each edit.

The first backup was hash-verified before the keyword repair.

The second backup was hash-verified immediately before deleting the two calls.

The normalized before-and-after diff against the second backup contains only the two intended deletions.

The final source search reports zero occurrences of either legacy ID in active runtime source.

The offline Effects and Decision modding wiki pages and the installed vanilla effects and triggers documentation were consulted before the edits.

No probability audit was run because this repair changes no weighted decision, mission, event, MTTH, or AI surface.

No GUI inspect or render was run because no decision-owned or mission-owned GUI surface is changed.

No additional HOI4 launch was run by this subagent because live engine validation belongs to the parent QA workflow; the parent ran launch 16 against the reviewed deletion.

The required narrow `hoi4.event_compare` route was attempted once with the recorded pre-deletion revision and returned the exact `EVENT_REVISION_NOT_CACHED` blocker above.

## Remaining issues

Launch 16 native parser acceptance is verified: the two legacy mission diagnostics decreased from 10 to zero, and no new diagnostic family attributable to this deletion was observed.

Other Event 33 and unrelated startup diagnostics recorded by launch 15 remain outside this bounded repair.

Old-save migration behavior remains untested because no supported live obsolete mission definition or activation path exists in the current package.

The current specification retains the historical old-save instruction to remove these obsolete missions, but no substitute mission or compatibility stub was added because the current engine rejects those absent IDs.

No plan handoff was written.

No commit was created, per the parent instruction.

No other simplification was made inside the assigned two-reference parser repair.
