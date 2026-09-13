# Event 027 Doctrine Research

## Current verification refresh (2026-09-04)

This refresh supersedes the dated MCP artifact values in the sections below and is the current status of the Event 027 implementation.

The source is playable in the source-level sense: Event 027 is registered as a Minor Repeatable event, its default reworked-event enable path is active, manual and National Breakthroughs dispatch reach the country-owned batch flow, humans receive the chained pages, and AI countries resolve through the same validity pool.

The parent has also initialized the adapter registry during normal startup and added a dedicated fail-closed Event Log N/A reason for the impossible state in which no live country has a valid doctrine action.

The fresh focused `hoi4.event_inspect` lint returned `EVENT_INSPECTED_PARTIAL` at revision `57d351df319dd5e7cdd1aa154584e6ac6e4bde5f1e6d0689ede14544ce2eb4cc`, with 31 Event 027 IDs represented in the current source, zero direct Event 027 blocking diagnostics, and partial validation because the large workspace defers helper and lifecycle projections.

The current Event Viewer options render returned `EVENT_RENDERED_PARTIAL` at revision `00d629f508b7c159079ad7d6f7eb13641489097d593b4c360ba2f464b7eb960f`, with layout hash `805b63c9307c8b209975af2767e8e7fe5111f7f746138061fd4f769fc276ff92`, 180 selected nodes, 42,308 omitted nodes, and zero direct Event 027 blocking diagnostics. Its PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7bc62a327a0a03d022f33110d945983b5b6a4ecc14b314bb2c21bf285a2c9774/df26072c7cd36514b1190ef778126d342c9e0436bb490fc7af336fe2a73d7c01/event-options-00d629f508b7.png`. This is a source-linked partial render rather than a one-to-one in-game popup capture and therefore does not close pagination, clipping, Event Log, or Event Details presentation acceptance.

The Event Viewer comparison route was retried against the earlier focused revision and returned `EVENT_REVISION_NOT_CACHED`; no before/after Event 027 comparison is claimed until a comparison-compatible graph baseline is retained.

The current technology/doctrine evidence resolves Land/Chaos Warfare, Naval, Air, and Special Forces, but the aggregate technology index remains validation-failing with 1,408 blocking diagnostics and the focused renders report `sourceAccurate: false`; the same-revision comparison is only a zero-delta route control because Event 027 does not modify doctrine definitions.

The named probability pass covers all 37 DR-A01 through DR-G03 scenarios, but the current analyzer result is partial with 5,291 candidate rows, 144 unresolved inputs, withheld normalization, and no genuine before/after source delta; unresolved rows are not treated as zero probability.

The visual-asset audit found no missing final runtime asset, bad sprite path, duplicate identifier, orphan, or accidental cross-event asset, and the report image plus all three achievement triplets pass DDS round-trip checks. Production HOI4 consumer captures for the popup, Event Log, Event Details, and achievement states remain open evidence items.

Live engine traces are still required for native/banked mastery, empty-track assignment, Chaos Warfare and Special Forces identity, receipt recovery, overlapping queues, lifecycle transitions, achievements, and the complete named probability states, so this remains an implementation handoff rather than a completion claim.

## Status

Event 027 is a global Minor Repeatable event in the National Breakthroughs cluster.

The canonical root is the actorless `chaosx.nr27.1` event, and one root firing creates one append-only country-owned batch for every live country with at least one valid adapter action.

The source-of-truth design package is `docs/specs/027_doctrine_research_specs/`.

The runtime covers ordinary Army, Navy, Air, conditionally verified Special Forces, and Chaos Warfare through explicit native doctrine adapters. Active-track mastery uses one-point `add_mastery` increments with a native level readback after every point, while empty tracks use native `set_sub_doctrine` before the same transaction. Future custom rows remain disabled until they provide an equivalent adapter contract, and the remaining MCP and live-session evidence is tracked in the implementation plan.

Event 027 is included in the default reworked-event enable list. Manual settings dispatch and National Breakthroughs cluster dispatch remain wired for controlled validation and gameplay.

## Firing and queue contract

`doctrine_research_fire_global_batch` prepares one immutable global stage and batch size, increments the global batch sequence once, and performs one bounded `every_country` fanout.

The fanout snapshots only countries that exist, are not capitulated unless they are a government in exile, and pass `doctrine_research_country_has_valid_action` through the fail-closed adapter registry.

The baseline creates one choice, Evolution I creates two, Evolution II creates three, Evolution III creates four, and Evolution IV creates five.

The stage and size are written to the batch arrays at creation and are never recalculated while the batch is queued or active.

Each firing appends a new batch row even when another batch is active or queued, so later firings cannot overwrite, merge, or silently resize earlier work.

Countries created after a firing do not receive a retroactive row.

An active batch is resolved first, then the oldest queued row is promoted without changing its stored stage or size.

## Choice transaction

The human chain first selects a domain, then either selects an eligible Grand Doctrine or selects a track and one eligible subdoctrine.

When the selected domain has no active Grand Doctrine, the confirmation applies exactly one eligible native Grand Doctrine for free and consumes the choice without advancing a subdoctrine.

When the selected domain has an active Grand Doctrine, confirmation revalidates the current owner, domain, Grand Doctrine, track, subdoctrine, completion state, native gates, and receipt state before applying one native mastery increment. The static built-in adapter gate rejects unknown custom domains before any native mutation is attempted.

The source-level mastery adapter snapshots the current observable native level, applies one point, rereads the native level, and succeeds only when the observed level is exactly the expected level.

Preservation of fractional or banked native mastery, exact attribution at low, middle, and final levels, and recovery after an interrupted native mutation still require local engine evidence and are not claimed here.

The transaction finalizes the receipt and consumes the choice only after the native effect succeeds.

If native banked mastery completes a branch while an empty track is being assigned, the receipt is stored as `native_adoption` with the observed post-assignment level. It does not consume the choice or count as an Event 027 mastery step; human control returns to the selected domain's track list, and AI control clears the selection before recalculating the same valid pool.

Prepared and effect-applied receipts fail closed and expose an ambiguous result instead of guessing after a partial failure. Receipt recovery is keyed by batch and choice, restores the recorded target only while the pending receipt marker is present, rereads every effect-applied mastery result, and finalizes only when the stored and current levels both equal the recorded pre-level plus exactly one native increment. Adoption recovery requires the recorded Grand Doctrine to remain active; any mismatch quarantines the batch. Native-adoption receipts are terminal no-choice results, so they cannot be reused when the country makes a later selection with the same stored choice number. Invalid, ambiguous, abandoned, and consumed receipts remain one-time terminal records.

The separate batch and receipt ledgers now validate both parallel-array alignment and receipt-to-batch parent links, but save/reload recovery of an interrupted prepared or effect-applied native transaction remains unproven.

The Event 027 path never replaces an active Grand Doctrine, grants generic military experience, dumps mastery points across multiple levels, or uses technology helpers. The shared global-host coordinator persists the current host as an event target so a tag switch can reconcile the former controller without adding a recurring Event 027 world fanout.

Empty-track adoption calls native `set_sub_doctrine`, re-reads the selected branch, and then applies the first mastery step through the same one-point/readback transaction. The action is available only for the statically declared built-in domains and their explicit track/subdoctrine wrappers.

## Adapter registry

The registry is numeric, versioned, and fail-closed. Valid-pool, adoption, empty-track, and mastery checks require the initialized registry flag before any ordinary adapter can participate.

Ordinary domains have explicit static dispatch rows, native folder IDs, one-step capability, owner gates, AI selectors, and cleanup selectors.

Track emptiness is resolved by folder-owned adapters for Army, Navy, Air, and Chaos Warfare because the native `has_subdoctrine_in_track` trigger checks any instance of a track across the relevant doctrine scope. This keeps an Army or Chaos Warfare track from being hidden by a same-named track in the other land-domain system. Special Forces retains the native dual-track check because its subdoctrine identities are intentionally reusable between the two Special Forces tracks.

| Domain | Native folder | Tracks | Owner gate |
| --- | --- | --- | --- |
| Army | `land` | Infantry, Combat Support, Armor, Operations | Native Army Grand Doctrine adoption and track availability |
| Navy | `naval` | Submarines, Screens, Carriers, Capital Ships | Native Navy Grand Doctrine adoption and track availability |
| Air | `air` | Fighter Aircraft, Strike Aircraft, Medium Aircraft, Heavy Aircraft | Native Air Grand Doctrine adoption and track availability |
| Special Forces | `special_forces` | Special Forces First, Special Forces Second | Native adoption and mastery while the selected branch-to-track identity is unambiguous; both occupied tracks fail closed |
| Chaos Warfare | `land` | Infantry, Combat Support, Armor, Operations | `cbrn_chaos_warfare_adoption_capable` plus establishment stock, fielded operations HQ, fielded protected formation, and native Chaos AI state |
| Future Custom | disabled | none | No executable adapter until a complete contract is registered |

Chaos Warfare uses its owning `chaos_warfare` Grand Doctrine, four native track identities, the owning pre-adoption establishment package, native downstream requirements, native milestone transitions, and `cbrn_chaos_warfare_ai_has_viable_program` in its AI scoring.

Special Forces adoption checks the exact native `special_forces_quantity` and `special_forces_quality` identities instead of relying on a folder-wide probe, while preserving the installed DLC and special-forces technology gates.

A disabled or malformed custom row contributes no valid action and cannot remove valid ordinary rows.

Special Forces uses a stricter rule because vanilla permits each of its eight subdoctrine tokens in either native track while exposing only track occupancy and subdoctrine-wide mastery readback. Empty-track selection remains exact through the native folder index, and active mastery remains available when exactly one Special Forces track is occupied. When both tracks are occupied, Event 027 omits Special Forces mastery because the script API cannot prove which occupied track owns a reused token; other valid domains remain available.

The native one-step capability is implemented as a static adapter boundary: every built-in branch has an explicit native folder, track identity, subdoctrine identity, and postcondition reader. The event never dispatches a dynamic folder or callback for a future custom row. Live-session validation of the full receipt/save/reload sequence remains a separate acceptance item.

## Human presentation

The visible flow is implemented in `events/027_doctrine_research.txt`.

The `.2` opening explains the batch, `.3` selects a domain, `.4` selects a Grand Doctrine for adoption, `.5` selects a track, `.6` routes to one of eighteen track-specific subdoctrine pages, `.7` confirms the transaction, `.8` reports the result, `.9` continues a remaining batch, `.10` summarizes a completed batch, `.11` handles no-option states, `.12` reports an ambiguous receipt, and `.13` reports native banked completion without consuming the choice before returning to the track list.

The hidden `.6` router opens one of the visible `.60` through `.77` track pages. Ordinary candidate lists remain track-specific, and the Special Forces adapter suppresses an occupied two-track state before an ambiguous token can reach a page or transaction.

Every opening, selection, confirmation, navigation, continuation, summary, invalidation, and no-option page has a localized title, description, option text, trigger, and effect tooltip.

Track pages and confirmation now expose the selected or active branch's current mastery level, next mastery level, native maximum level, branch completion state, and Grand Doctrine Milestone state through country-scoped display values. Peoples' War uses its verified four-level native reward structure; other supported branches use their verified five-level structure.

Every active opening, domain, Grand Doctrine, track, subdoctrine, and confirmation page displays the current batch's remaining choices. Confirmation text is action-specific, so Grand Doctrine adoption does not show irrelevant mastery fields and mastery confirmation retains the full domain, Grand Doctrine, track, branch, level, completion, and Milestone context.

The actorless History row stores the immutable firing batch size as its payload. History details therefore report the exact one-, two-, three-, four-, or five-choice curriculum that fired, while the ordinary Event Details page presents the one-to-five progression range.

The largest candidate lists use deterministic two-page navigation in native doctrine-graph order. Page navigation is free, preserves the current choice, and rebuilds the same track page; the MCP event render still does not prove in-game overflow behavior.

## AI resolution

AI countries use the same domain, Grand Doctrine, track, and subdoctrine validity predicates as the human pages.

The AI scorer evaluates live forces, production, war, geography, theater, strategy flags, completion value, continuity, and owner-system readiness at each selection layer.

Navy owner-readiness weight requires a coastal state, naval production, a native fleet, or an active naval doctrine, while Air owner-readiness weight requires an air force, military production, or an active air doctrine; the valid human action pool remains unchanged.

It scores every eligible Grand Doctrine, all valid track identities, and all registered candidate subdoctrines before selecting from positive-weight candidates with bounded random choice.

After every successful adoption or mastery receipt, the resolver clears the previous selection and recalculates the pool before resolving the next choice.

Chaos Warfare receives additional readiness from its CBRN AI state and establishment requirements, while a failed custom adapter remains zero-weight.

If no valid doctrine action remains before an AI batch spends every stored choice, the resolver closes the exhausted batch normally. Quarantine is reserved for a batch that still has a valid action after the bounded resolution guard or a failed transaction.

## Persistence and lifecycle

All batch, receipt, choice, stage, size, result, and achievement values are country-owned variables and aligned parallel arrays, so save/reload, tag changes, subject changes, and controller changes do not transfer or overwrite the ledger.

The documented lifecycle callbacks reconcile the exact affected country after state control, puppet, release, subject-autonomy, government, exile, reinstatement, and civil-war transitions.

Those callbacks also reconcile controller changes: an AI-controlled active batch resolves silently, while a newly human-controlled active batch opens its next page once through the country-owned prompt flag. The shared global-host tag-switch branch reconciles the former host before clearing its marker and reconciles the new human country after setting it, without moving either country's ledger.

Annexation clears the annexed country's unused batches, active row, receipts, and transient Event 027 state without transferring it to the controller, including subject annexation.

No recurring whole-world on-action was added for Event 027.

## Integration and presentation assets

Event 027 is registered in the event settings, the National Breakthroughs cluster membership, firing history, event log, event details, evolution registry, debug names, and catalog workbook.

The report image is `GFX_report_event_027_doctrine_research` from `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`, registered by `interface/027_doctrine_research.gfx`.

Doctrine pages reuse the verified native doctrine-owned icons from the active doctrine definitions, including `GFX_doctrine_chaos_warfare_medium`, `GFX_doctrine_extermination_columns_medium`, `GFX_doctrine_contaminant_firebases_medium`, `GFX_doctrine_chemical_suppression_medium`, and `GFX_doctrine_integrated_chemical_operations_medium` for Chaos Warfare.

The three achievements are `027_doctrine_research_first_lesson`, `027_doctrine_research_single_school`, and `027_doctrine_research_joint_curriculum`.

Each achievement has an active, grey, and not-eligible 64 by 64 DDS icon registered in `interface/chaosx_achievements.gfx` and stored under `gfx/achievements/`.

The achievement effects use Event 027 receipt rows rather than transient UI state, require human-controlled completion, and distinguish Grand Doctrine adoption from later Event 027 mastery. First Lesson additionally requires the matching domain to have been empty in the immutable batch-start snapshot.

## Catalog and acceptance map

The editable source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; its Event 027 row is Minor Repeatable, cluster 9, Medium severity, and Needs Testing until live acceptance is supplied.

The export-only CSV files are regenerated with `.tools/export_event_catalog_csv.py` after workbook changes.

The implementation was checked against each file in the specification package: `README.md`, `027_doctrine_research_acceptance_criteria.md`, `027_doctrine_research_achievement_prompt.md`, `027_doctrine_research_asset_prompt.md`, `027_doctrine_research_catalog_cluster_handoff.md`, `027_doctrine_research_coding_prompt.md`, `027_doctrine_research_doctrine_registry_matrix.md`, `027_doctrine_research_goal_prompt.md`, `027_doctrine_research_probability_scenarios.md`, `027_doctrine_research_research_notes.md`, `027_doctrine_research_review_and_closure.md`, `027_doctrine_research_source_review.md`, `027_doctrine_research_spec_part_1_core.md`, `027_doctrine_research_spec_part_2_choice_flow.md`, `027_doctrine_research_spec_part_3_evolutions_balance_ai.md`, and `027_doctrine_research_spec_part_4_presentation_assets_achievements.md`.

## Future plans and suggestions

The next safe extension is to add a custom domain only after its adapter supplies a native folder, valid Grand Doctrine and track identities, one-step mastery proof, downstream requirements, AI selector, cleanup selector, localization, and MCP evidence.

Future custom adapters should be promoted only after a local engine trace demonstrates that native subdoctrine adoption and one mastery increment are atomic and observable through the receipt transaction.

The AI can later receive owner-provided strategy flags for country-specific doctrine preferences without changing the shared validity or receipt contract.

The named probability scenarios still need a completed baseline/final `hoi4.probability_compare` pass. Current MCP inspection discovered the weighted source but could not resolve country state candidates for the required scenario set.

## Current blockers and deviations

The completion audit identified the following unresolved acceptance items: live save/reload recovery of prepared or effect-applied receipts, pure tag-switch validation, rendered pagination/overflow evidence, complete named-scenario probability comparisons, and native proof for the Special Forces branch-to-track identity. The native mastery route, dynamic mastery-state presentation, lifecycle-backed controller reconciliation, and three achievement predicates are wired; their live evidence remains open until the owning validation pass is complete. Both occupied Special Forces tracks are an explicit fail-closed limitation rather than a substitute reward. Event 027 remains in the default reworked-event allowlist while the remaining acceptance evidence is collected; manual settings dispatch and cluster dispatch remain available.

The evolution clock now advances one enabled stage after the centralized 90-day interval from the existing global-host daily coordinator and records the stage when it promotes. This is a bounded global scheduler and performs no country fanout, but it still needs live and MCP timing evidence.

Because those items are unresolved, this document is an implementation handoff rather than a completion claim. No commit should be created until the blockers are closed and the final audit is rerun.

The current local Event Viewer runner is v3.0.6. Its file-scoped lint for `chaosx.nr27.1` returned `EVENT_INSPECTED_PARTIAL` at revision `d56afb96621c5db5d4ea7fdf4f8524e99aeab1b51652ab8d0c60f7750cc8a6b5` with no direct Event 027 blocker, while helper and lifecycle projections remain deferred. The matching options render returned `EVENT_RENDERED_PARTIAL` at the same revision with no direct Event 027 blocker. The current artifacts are recorded in `docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_mcp_refresh_2026-09-01.md`, and the older full-workspace scan remains historical because no accepted before-and-after comparison result exists.

The current technology/doctrine folder route resolves the supported Land, Naval, Air, and Special Forces folders and the Chaos Warfare Grand Doctrine at revision `7080c50bf1467579a159640153bbb2d43902b0b7a42a6c35daa41609a5124ed9` with graph hash `3a8197353f9acbc3271a5bbd54995b9887f067674e8d69285cb83dff0b574c68`. The aggregate index reports 1,421 blocking technology diagnostics and three unresolved index entries, so this result is evidence of source resolution rather than final engine-certified presentation.

The required probability audit submitted all 37 named scenarios under the current source set and discovered 143 available weighted candidates across the four random-list layers. The current typed fixture resolves DR-A01 through DR-A06 at the domain layer and DR-B01 at the Grand Doctrine layer, while the bounded Navy score sweep produces a score-only Army-to-Navy rank reversal; these are analyzer fixtures rather than native country-state proof. Native country, doctrine, batch, DLC, invalid-adapter, sequence, and baseline-to-final comparison evidence remain open. The native `add_mastery` route remains supported by source-level one-point increments and postcondition readback. The report and achievement asset provenance is recorded in `docs/assets/027_doctrine_research/manifest.md` and `gfx_handoff.md`.
