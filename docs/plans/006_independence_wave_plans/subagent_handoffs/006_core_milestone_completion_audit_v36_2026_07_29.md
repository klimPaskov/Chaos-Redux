# Event 006 Core Milestone Completion Audit v36

Date: 2026-07-29

Audit mode: read-only source/static completion audit.

## Bounded verdict

The Event 006 core milestone is source-complete within the three surfaces authorized for this audit.

No blocker was found inside surfaces A–C.

This verdict covers the synchronized allocator/core loop, the shared dynamic systems, and the 206-row registry/API.

It does not claim that Event 006 is complete as a whole, that every registered country has a playable package, or that excluded country, asset, focus, super-event, achievement, catalog, and presentation surfaces are complete.

Live-game, save-load, and player-consumer evidence was explicitly excluded from the acceptance standard for this audit.

## Completion status by surface

| Surface | Status | Audit finding |
| --- | --- | --- |
| A. Synchronized allocator and core loop | Finished within milestone | The current source implements crisis and automatic candidate planning, host-survival selection, mandatory unique anchors, optional territory trimming, bounded rejection/reroll, lock-before-release, Event 005/Event 006 joint reservations, collision handling, cleanup, and the 6/8/10/14/20 automatic ladder. |
| B. Shared dynamic systems | Finished within milestone | The current source provides centralized tuning, initialization, readers, writers, clamping/recomputation, cleanup, visible decisions/missions, and AI hooks for country, host, patron, Network, League, and rival-bloc values. |
| C. Registry and reusable country API | Finished within milestone | The current source and audits account for all 206 registry rows, publish the reusable `chaosx_country` projections and bindings, keep unbound/inert rows fail-closed, and enforce the explicitly narrowed Event 006/Soviet collision boundary while preserving REV, ZIN, and ZZZ. |

## Surface A evidence

The package allocator in `common\scripted_effects\006_independence_wave_package_allocator_effects.txt` recomputes regional weights per draw, chooses a region and package through the published collections, uses a bounded attempt loop, and rejects an allocation that does not satisfy the exact requested count or aligned-array contract.

The candidate gates in `common\scripted_triggers\006_independence_wave_package_triggers.txt` require a usable anchor, an absent and unreserved target country, no conflicting Event 006/Soviet/Event 012 origin, compatible reservation-group use, and the required force/content mappings.

The shared reservation logic in `common\scripted_effects\chaosx_liberation_release_effects.txt` chooses a surviving host in the documented priority order, reserves the host before the target country, protects anchors, records owner and target snapshots, and prevents duplicate plan, package, anchor, country, and reservation-group use.

The only documented shared reservation-group exception is the intentional IW008/IW010 Rhine-Saar capacity pair.

The package planner in `common\scripted_effects\006_independence_wave_package_planner_effects.txt` reserves all mandatory anchors before compact territory and compact territory before extended territory.

Compact and extended territory failures are recorded as optional trims rather than invalidating a package whose anchor remains viable.

Failed packages are rolled back and rejected before bounded reroll, and the completed contribution is locked before release execution begins.

The execution path in `common\scripted_effects\006_independence_wave_execution_effects.txt` validates the locked plan, aligned reservations, live target scopes, adapters, force mappings, sponsorship metadata, and ownership transfers before commit.

Pre-mutation failures restore the prepared plan, post-mutation failures use the compensating rollback path, and finalization failure remains an explicit failed state rather than being reported as success.

The corrected positive existence gates are present for the ordinary reserved country, the sponsorship country, and the Event 005 joint reserved country.

The joint dispatcher in `common\scripted_effects\005_006_liberations_collision_effects.txt` orders Event 005 anchors before Event 006 anchors, then optional territory, then the shared lock.

The automatic tuning source publishes exact targets of 6, 8, 10, 14, and 20, with World Collapse also resolving to 20.

The pre-wave crisis request uses the same planner and reservation contract as the automatic wave, including queued requester-loss recovery, retry cleanup, and shared-barrier routing.

## Surface B evidence

The shared country-value system defines and initializes legitimacy, recognition, capacity, security, and instability through centralized constants and scripted effects.

The implementation includes gameplay writers, player-visible readers, clamping and recomputation, reset and cleanup behavior, decision and mission consumers, and AI weighting.

Host values and relations have explicit initialization, mutation, decay or recomputation, consumer, and cleanup paths.

The patron ledger has centralized writers, pruning and cleanup, bounded value handling, and patron-selection consumers.

Network and League values have initialization, membership and score writers, visible consumers, cleanup, and AI participation.

Rival-bloc state has its own constants, effects, triggers, decisions, cleanup, and AI behavior.

The payment predicate `can_pay_independence_wave_security_standard_cost` now matches the actual payment and player-facing cost contract and no longer imposes an undisclosed Command Power requirement.

The v35 dynamic-system crosswalk identifies the tuning source, initializer, gameplay and visible readers, writers, clamp or recomputation path, cleanup path, and AI hook for every dynamic subsystem in this milestone.

## Surface C evidence

The registry contains 206 rows composed of 102 custom X-tag rows, 91 reusable-tag rows, and 13 overlay rows.

The reusable-tag rows resolve to 89 unique tags because CHU and BIA are deliberately shared.

The registry resolves 191 unique nonblank carriers, publishes 14 regions and 111 groups, and separates row identity from current package readiness.

The current projections expose 138 bound selectable rows, 55 unbound selectable rows, and 13 overlays.

The status projections additionally identify 85 researched definitions and 17 inert reservations.

The public `chaosx_country` API publishes row, tag, group, region, status, binding, unbound, and overlay collections through reusable lifecycle effects.

Unbound and inert rows remain registered but are deliberately excluded from automatic selection until an explicit package binding and required identity facts exist.

This is fail-closed registry behavior, not a fallback carrier or silent substitution.

The Event 006/Soviet collision audit protects 136 scoped tags and reports no external country-definition collision and no external identity-surface collision.

The narrowed scan intentionally leaves REV, ZIN, and ZZZ available to their existing consumers.

## Accepted-plan and handoff disposition

| Reviewed source | Disposition |
| --- | --- |
| `docs\specs\006_independence_wave_specs\diagrams\006_release_planner_flow.md` | Implemented by the current anchor-first, optional-trim, reroll, lock, release, verification, and rollback sequence. |
| `docs\specs\006_independence_wave_specs\specs\006_independence_wave_spec_part_1_core.md` | Implemented for the audited allocator, host-survival, collision, ladder, and registry surfaces. |
| `docs\specs\006_independence_wave_specs\specs\006_independence_wave_spec_part_3_mechanics.md` | Implemented for the audited country, host, patron, Network, League, rival-bloc, crisis, decision, mission, and AI surfaces. |
| `006_package_allocator_integration_handoff.md` | Implemented in structure; its older allocation counts and registry split are superseded by the doubled ladder and current 138-bound/55-unbound projections. |
| `006_event5_collision_handoff.md` | Implemented and superseded by the shared joint-reservation and lock sequence. |
| `006_country_registry_api_handoff.md` | Implemented and extended by the v35 status, binding, unbound, and overlay projections. |
| `006_pre_wave_crisis_and_doubled_ladder_2026_07_28.md` | Its earlier crisis receipt, requester-loss, retry, and disclosure holds are resolved in the audited source paths. |
| Broad all-Chaos tag-collision findings | Not a completion gate for this audit because the authorized policy is the narrower Event 006/Soviet scan and expressly preserves REV, ZIN, and ZZZ. |

## Meaningful validation

`python .tools\audit_event6_allocator.py` passed against the current worktree.

The audit found 149 package publishers, 126 automatic/high-chaos selectable package bindings, 138 SCN-008-ranked rows, 12 content-attested packages across 11 compatible groups, the documented Rhine-Saar exception, exact targets of 6/8/10/14/20, anchor-before-compact-before-extended ordering, Event 005-before-Event 006 joint ordering, positive target-existence guards, host-survival sourcing, reservation alignment, and lock-before-execution behavior.

`python .tools\audit_chaosx_country_tags.py --surface-scan` passed against the current worktree.

The collision audit reported 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one intentionally skipped random-event root.

The v35 event inspection completed as a partial static scan with zero blocking diagnostics.

Its evidence artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20a65ca26ac069a9a4e5df10507001c95f8bbbe025eace5a2a9b230a325a9ab7/64f77aab950abcc6f8bc3b78eb2a4a8d58f6ec6a6d37b7efcc990d4ea636fff7/event-scan-867986734b88.json`.

The event inspector also reported 7,347 unresolved helper references and 2,020 global dangling-reference warnings across the broad repository scan.

Those warnings were non-blocking and not localized as failures of the audited A–C surfaces, so they are recorded as a tool limitation rather than silently treated as proof of correctness.

Probability inspection could not fully evaluate every decision scenario because some scenario inputs were undeclared to the inspection tool.

The source still contains the required AI weights and value consumers, so this remains a static-validation limitation rather than an identified milestone defect.

No live-game, save-load, or player-consumer test was required or performed.

## Simplifications, omissions, and blockers

No undisclosed simplification or internal blocker was found within surfaces A–C.

The 55 unbound selectable rows and 17 inert reservations are explicit fail-closed registry states.

They are not replaced by generic carriers and do not prevent completion of the registry/API milestone.

Only 12 packages are currently content-attested by the allocator audit.

That content-admission count does not establish that excluded package content can currently satisfy every 14- or 20-package live wave.

The ladder targets, exact-count contract, and fail-closed response are complete in the core source, while expanding playable package admission is explicitly outside this audit.

Country-specific gameplay packages, portrait and flag production, focus-tree customization, super-events, achievements, catalog alignment, and broader full-event completion were not audited and are not claimed complete.

No visual asset was required by the audited core, dynamic-system, or registry/API surfaces.

Asset gaps belonging to excluded country packages or presentation consumers remain outside this verdict.

Historical handoffs that contain older allocation counts or registry splits should be read as superseded implementation history, not current authority.

## Remaining external dependencies and recommended next actions

1. Treat this report as the completion handoff for the bounded A–C source milestone only.
2. Continue package-content admission separately if the live automatic consumer must satisfy the 14- and 20-package tiers rather than fail closed on insufficient attested content.
3. Audit country packages, visual assets, focus customization, super-events, achievements, catalog surfaces, and whole-event player experience under their own acceptance criteria.
4. Obtain live consumer evidence only when a later milestone explicitly adopts live-game or save-load validation.
