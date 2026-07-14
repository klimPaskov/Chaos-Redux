# Event 015 Documentation Curator Interim

Date: `2026-07-14`

Role: `chaosx_documentation_curator`

Scope: documentation audit only. No gameplay, localisation, asset, spreadsheet, or runtime file was changed by this pass.

Status: interim. Event 015 implementation and corrective audits are active. Counts and runtime observations in this file are a dated inspection snapshot, not a completion claim.

## Executive Status

Event 015 has a substantial accepted design package and broad implementation evidence. Its documentation does not yet provide one dependable current-state entry point. The main problems are not missing prose. They are mixed authority levels, historical blockers presented as live blockers, implementation clarifications that were never promoted into the specs, and asset records that describe several different generations of the package without a clear precedence order.

The intended canonical mechanic document, `docs/events/015_utopia_manifesto.md`, is not safe to use as current truth. It describes an older ledger, older route identities, older visual gaps, and an older achievement count. It needs a full post-stabilisation rewrite against final gameplay and final localisation.

The eight spec parts and their matrices remain the accepted design authority. They are not runtime proof. Live source is the authority for what is implemented. Handoffs and audits are dated evidence. Prompts are execution templates. Historical catalog and research files are provenance.

No live gameplay file inspected in this pass contains `World Tension Subsides`, `world_tension_subsides`, `Event 015 Placeholder`, or `015_placeholder`. Those labels survive only in documentation. They should be retained where they record source provenance, but they must be marked as historical input rather than the current Event 15 identity.

## Source of Truth Order

Use this order until a final Event 015 resume packet replaces this interim file.

| Priority | Source family | Authority | Current disposition |
| --- | --- | --- | --- |
| 1 | Live gameplay, localisation, interface, music, sound, and asset files | Runtime truth | Authoritative for implemented identifiers and wiring. Still changing during this audit. |
| 2 | `docs/specs/015_utopia_manifesto_specs/specs/` and accepted matrices | Design truth | Authoritative for intended scope. Not proof that an item is implemented or balanced. |
| 3 | Final Event 015 super-event text and audio research | Quotation, attribution, route text, and audio provenance | Authoritative for the researched package. Integration status must come from live source or a later integration handoff. |
| 4 | Family-specific final asset manifests | Asset provenance and binary inventory | Authoritative within each frozen asset family. The root asset manifest is currently an incomplete index. |
| 5 | `docs/events/015_utopia_manifesto.md` | Intended canonical mechanic and event documentation | Stale. Do not use for current ledger, route, identity, event, achievement, or asset facts. |
| 6 | `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/` | Dated implementation and audit evidence | Snapshot evidence only. Later handoffs and live source supersede earlier status claims. |
| 7 | `docs/specs/015_utopia_manifesto_specs/prompts/` | Execution templates | Not current status and not runtime truth. |
| 8 | Catalog replacement and source-reading records | Historical input and provenance | Preserve. Add status notices where old Event 15 names could be mistaken for the current identity. |

### Design authority

The design authority consists of these files as a coordinated package:

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_1_core.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_2_commonwealth_ledger.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_focus_tree_architecture.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_decisions_and_missions.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_5_country_identity_and_formable.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_6_evolutions_events_and_reactions.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_7_ai_balance_and_compatibility.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_8_assets_localisation_and_acceptance.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/`
- `docs/specs/015_utopia_manifesto_specs/focus_graphs/`

`README.md` and `PACKAGE_MANIFEST.md` index this package. They do not override the numbered specs. Statements in the README about an unmounted repository, unavailable wiki, unavailable workbook, or unavailable project subagents describe the planning environment in which the package was drafted. They are not current implementation blockers.

### Asset authority

Use the following family-specific records:

- Non-icon event art: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/manifest.md`
- Route identity art: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/manifest.md`
- Icon and authored-frame inventory: `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`, but only after it is regenerated against the frozen decision source
- Super-event audio package: `docs/super_events/super_event_audio_packages.md`

`docs/assets/015_utopia_manifesto/manifest.md` should become the current index for those records. It is not currently reliable as that index.

## Read-Only Runtime Snapshot

This snapshot records identifiers observed during this curation pass. Other agents were actively working on Event 15, so final documentation must re-read live source rather than copy these counts.

| Surface | Observed state |
| --- | --- |
| Event identity | Event ID `15`, entry event `chaosx.nr15.1`, catalog name key `chaosx.event_name.15`, current English name `Utopia Manifesto` |
| Automatic entry | Registered through `global.fire_once_events` with `constant:utopia_manifesto_event.id` and covered by Event 15 settings and availability logic |
| Event Details | `chaosx.events_log.window.event_details.utopia_manifesto` |
| Central ledger values | `utopia_need`, `utopia_plenty`, `utopia_concord`, `utopia_assignment` |
| Route enum | `consent_of_households = 1`, `common_table = 2`, `guardians_of_measure = 3`, `closed_island = 4`, `joke_understood = 5` |
| Evolution enum | `glosses_in_the_margin = 1`, `necessary_shores = 2`, `cities_of_one_measure = 3`, `nowhere_made_law = 4`, `perfect_island = 5` |
| External case types | `port_access`, `defensive_corridor`, `essential_resource`, `settlement_and_housing`, `island_or_capital_refuge`, `reconstruction_zone` |
| Current route identities | `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH`, `UTOPIA_MANIFESTO_COUNCIL_UNION`, `UTOPIA_MANIFESTO_PLANNED_UTOPIA`, `UTOPIA_MANIFESTO_CLOSED_ISLAND`, `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` |
| Focus source | `122` focus blocks in `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| Decision source | `9` category definitions and, at the inspection point, `99` decision blocks plus `35` mission blocks |
| Event source | `85` Event 15 definitions by a one-tab `id = chaosx.nr15.*` scan at the inspection point |
| Achievements | `14` current `utopia_manifesto_*` achievements are documented and have exact asset triplets |
| Super-event package | Display slots `96` through `100`, playback audio ID `57`, title `UTOPIA HAS NEIGHBORS` |
| Non-icon art | `14` report images, `3` news images, and `5` current route super-event images in the final non-icon manifest |
| Route identity art | `39` runtime flag TGAs, `4` institutional portraits, `16` advisor portraits, and `5` league emblems, for `64` validated runtime outputs |

The observed decision and event counts differ from several handoffs and from an earlier point in this same implementation run. This is direct evidence that all inventory documents must be regenerated only after the gameplay owner freezes the source set.

### Observed open runtime and documentation gaps

- The Event 15 decision category did not contain `scripted_gui = utopia_manifesto_ledger_scripted_gui` when inspected. The route-identity wiring handoff also records this as an open parent integration item. Documentation must not say that the Ledger is player-accessible through the category until the attachment exists and is audited.
- `decision_utopia_offer_settlement_agreement` and `mission_utopia_fulfil_settlement_agreement` existed in live decision source but were absent from `decision_icon_mapping.csv` at inspection time.
- Those two settlement-agreement identifiers had no exact localisation entries at inspection time.
- The settlement-agreement decision and mission reuse `GFX_decision_utopia_settlement_charter`, so their mapping gap does not by itself prove that a new binary asset is required.
- The root asset manifest still reports `98` decisions and `32` missions and says gameplay has zero icon assignments. These claims do not match the inspected source.

## Staleness Audit

### Canonical event document

`docs/events/015_utopia_manifesto.md` requires a full rewrite after implementation stabilises.

Current conflicts include:

- The document title uses `Utopian Manifesto`, while the current catalog identity is `Utopia Manifesto` and the entry popup is `The Utopia Manifesto`.
- The overview describes replacement of an old world-tension event. That is implementation-history language, not a current mechanic description.
- The ledger is described as Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion, and League Confidence. The implemented central kernel uses Need, Plenty, Concord, and Choice or Assignment.
- Route and focus descriptions belong to an older architecture and do not document the accepted five-route, `122`-focus implementation.
- Late identities use the old `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_marked_bounds_state`, and `utopia_league_of_need` families rather than the five current cosmetic tags.
- The asset section says there are `12` achievements and missing route super-event visuals. The current package has `14` achievements and five complete route images.
- The document presents the Ledger scripted GUI as available without recording the missing category attachment found in the current source.
- It does not provide a dependable event-chain, decision-family, mission-family, idea-lifecycle, route-identity, super-event, or asset map for the implemented package.

Do not patch this file piecemeal while gameplay is moving. Rebuild it from the final source, final English localisation, accepted specs, and final audit handoffs.

### Legacy `World Tension Subsides` and placeholder text

Exact legacy labels occur in these documentation files:

- `docs/specs/015_utopia_manifesto_specs/catalog/event_15_catalog_replacement_plan.md`
- `docs/specs/015_utopia_manifesto_specs/handoffs/implementation_sequence.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/prompts/subagents/01_repo_explorer_prompt.md`
- `docs/specs/015_utopia_manifesto_specs/prompts/subagents/09_documentation_curator_prompt.md`
- `docs/specs/015_utopia_manifesto_specs/prompts/subagents/10_spreadsheet_worker_prompt.md`
- `docs/specs/015_utopia_manifesto_specs/prompts/utopia_manifesto_coding_prompt.md`
- `docs/specs/015_utopia_manifesto_specs/prompts/utopia_manifesto_goal_prompt.md`
- `docs/specs/015_utopia_manifesto_specs/README.md`
- `docs/specs/015_utopia_manifesto_specs/research/source_reading_and_limitations.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_1_core.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_8_assets_localisation_and_acceptance.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/repo_explorer_handoff.md`

Disposition rules:

- Preserve the catalog plan and source-reading record as historical evidence.
- Preserve completed prompts as execution templates.
- Preserve the repository explorer handoff as an initial-state snapshot.
- Add a package-level status notice that the old title is provenance only and that no live Event 15 script uses it.
- Remove old-title framing from the future canonical mechanic document and from any matrix row intended to state current completion.
- Do not rewrite historical snapshot sentences to pretend that the initial state never existed.

### Spec and plan boundary

The numbered specs and accepted matrices belong under `docs/specs/`. Dated audits, implementation snapshots, improvement addenda, blocker ledgers, and resume packets belong under `docs/plans/`.

Three current package files blur that boundary:

- `docs/specs/015_utopia_manifesto_specs/handoffs/unresolved_verification_blockers.md` is a planning-time blocker ledger inside the spec package. It still reports missing mounts, unavailable agents, an unavailable workbook, and missing route images. Several claims are no longer true.
- `docs/specs/015_utopia_manifesto_specs/handoffs/implementation_sequence.md` is an execution plan without final dispositions.
- `docs/specs/015_utopia_manifesto_specs/handoffs/subagent_orchestration.md` is a routing plan without final dispositions.

Keep these as package provenance if desired, but add a clear historical-status banner. The final active blocker ledger and resume packet should live in `docs/plans/015_utopia_manifesto_plans/`.

### Implementation-backed clarifications not folded into specs

`scripted_system_architect_case_review.md` contains the most important unpromoted architecture review. Several recommendations have direct implementation evidence:

- `utopia_manifesto_clear_case_response_state`
- distinct `utopia_manifesto_case_ultimatum_refused` state
- `utopia_manifesto_remove_active_stewardship_missions`
- dedicated `utopia_manifesto_necessary_ground_take_state` wargoal
- stage-aware case-validity triggers
- six external `utopia_manifesto_case_type` values
- `utopia_manifesto_domestic_review_family`
- `utopia_manifesto_case_trade_attempted`
- `utopia_manifesto_recognized_compacts`
- stewardship status consumers
- revolt target arrays
- `utopia_manifesto_invalidate_active_need_case`

After the gameplay owner confirms final state, promote the implemented invariants into:

- Part 2 for the case type model, case stages, integrity rules, and persistent state
- Part 4 for methods, response reset, settlement agreement, stewardship, and terminal outcomes
- Part 7 for reconciliation, ownership cleanup, AI constraints, and local-support handling
- `matrices/decision_mission_matrix.md` for exact decision, mission, cancellation, and outcome coverage

Do not automatically promote every recommendation. The review also names unresolved design decisions that require an explicit disposition:

- reversible cleanup for market-access outcomes
- successor or disposition policy when a stewardship target disappears
- durations, renewal, and exit rules for contracts, leases, and joint administration
- policy for integrated-state benefits after a later owner change

The older `scripted_system_architect_handoff.md` is a historical recovery architecture based on an earlier commit. It must not override the later case review or final live source.

### Super-event research not promoted into design authority

The final text and audio research is substantially more specific than Part 8. The following accepted and wired facts should be summarised in Part 8 after the final integration audit:

- Title: `UTOPIA HAS NEIGHBORS`
- Remark: `Nowhere has a timetable.`
- Thomas More quotation source through Gilbert Burnet
- five route-specific descriptions
- display slots `96`, `97`, `98`, `99`, and `100`
- playback audio ID `57`
- Brahms, Symphony No. 3, third movement, `Poco allegretto`
- Musopen Symphony Orchestra recording with CC0 provenance

Keep the full research and attribution in:

- `docs/super_events/015_utopia_manifesto_super_event_text_research.md`
- `docs/super_events/015_utopia_manifesto_super_event_audio_research.md`
- `docs/super_events/super_event_audio_packages.md`

The audio research file and its handoff still describe missing route visuals. That blocker is superseded by the final non-icon manifest and current route sprite registration.

### Asset manifests and stale asset handoffs

The final non-icon and route-identity manifests provide strong family-level evidence. The root manifest still combines current facts with superseded instructions.

Stale root-manifest claims include:

- the other `13` report and `3` news sprite blocks remain for parent wiring
- decision mapping covers `98` decisions and `32` missions
- gameplay has zero decision icon assignments
- cosmetic flags are the old four identity families
- parent integration still needs `16` report and news blocks
- no indexed current summary of `route_identity_2026_07_14/manifest.md`

The following records also need status correction after the final source freeze:

- `docs/assets/015_utopia_manifesto/gfx_handoff.md` still presents completed non-icon registration as pending.
- `docs/assets/015_utopia_manifesto/generated_event_art_handoff.md` records prompt-only route images and is superseded for current image coverage.
- `docs/assets/015_utopia_manifesto/icon_animation_handoff.md` carries the old missing-route-image blocker.
- `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv` does not cover the inspected source set.
- `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json` reports a passing `98` decision and `32` mission inventory that is no longer current.
- `generated_event_art_final_handoff.md` remains useful for asset provenance, but its pending registration step is superseded by `non_icon_asset_wiring_handoff.md`.
- `route_identity_asset_handoff.md` remains useful for asset provenance, but its pending sprite-wiring step is superseded by `route_identity_asset_wiring_handoff.md`.

The current family authorities already show:

- `22` final non-icon assets with no fallback visual source
- five complete and registered route super-event images
- `64` validated route-identity runtime outputs
- `14` exact achievement triplets

These facts must not be diluted by older handoff language in the final index.

## Handoff Disposition Ledger

Every entry below remains useful evidence. None is a substitute for final live-source review.

| Handoff | Disposition | Required follow-up |
| --- | --- | --- |
| `repo_explorer_handoff.md` | Superseded as a live-state map. Retain as the initial recovery snapshot. | Add an archival-status banner. Do not update its historical findings in place. |
| `scripted_system_architect_handoff.md` | Historical recovery architecture. Superseded by implementation, the case review, and current source. | Retain for rationale. Link forward to the case review and final architecture summary. |
| `scripted_system_implementation_handoff.md` | Implemented snapshot, not final integration proof. | Reconcile its identifiers and counts with the frozen source. |
| `scripted_system_architect_case_review.md` | Partially implemented and partially unresolved. It is the main unpromoted architecture addendum. | Fold confirmed invariants into Parts 2, 4, and 7. Record explicit dispositions for its four design questions. |
| `focus_implementation_handoff.md` | Implemented snapshot. Later audits and current source govern status. | Link to the final focus audit. |
| `focus_tree_audit.md` | Superseded by `focus_tree_reaudit.md`. | Retain as audit history. |
| `focus_tree_reaudit.md` | Latest stored broad focus audit at this inspection point. It records failure. Its layout finding is superseded by the layout repair. | Replace current-status use with the active fresh audit. Keep lifecycle and route-AI findings open until that audit closes them. |
| `focus_tree_layout_repair.md` | Implemented and passing for coordinate repair only. | Do not treat it as lifecycle, reward, balance, or AI proof. |
| `decision_implementation_handoff.md` | Implemented snapshot. Superseded for counts by source drift and the later audit. | Link to a fresh decision and mission audit after source freeze. |
| `decision_mission_audit.md` | Latest stored decision audit and a failure record, but its inventory is stale. | Re-run after settlement-agreement localisation, icon mapping, and source stabilisation. |
| `country_package_implementation_handoff.md` | Implemented snapshot. | Reconcile against the final country audit and five current route identities. |
| `country_package_audit.md` | Latest stored audit at inspection time. Several visual findings are superseded by route-identity assets and wiring. Other gameplay, AI, and lifecycle findings remain open. | Replace current-status use with the active fresh country-package audit. |
| `localisation_implementation_handoff.md` | Partial implementation snapshot. It reported broad non-decision coverage, while decision coverage remained incomplete. | Regenerate the exact missing-key inventory after all gameplay identifiers freeze. |
| `asset_source_research_handoff.md` | Accepted provenance research. Its five-image blocker is superseded. | Add a status note linking to the final non-icon manifest. |
| `generated_event_art_final_handoff.md` | Final asset-production handoff for its package. Pending registration status is superseded. | Link to `non_icon_asset_wiring_handoff.md` and preserve the provenance record. |
| `non_icon_asset_wiring_handoff.md` | Implemented wiring snapshot for its bounded report and news scope. | Verify against final event picture references, then cite it from the root asset index. |
| `icon_frame_asset_handoff.md` | Final package snapshot for its then-current source. Its decision inventory and missing-route-image note are stale. | Regenerate the mapping and audit against final decisions and missions. |
| `route_identity_asset_handoff.md` | Complete route-identity asset-production record. Pending wiring language is superseded. | Link to the route-identity wiring handoff. |
| `route_identity_asset_wiring_handoff.md` | Implemented sprite, advisor, and emblem wiring snapshot. It records the open Ledger category attachment. | Keep the Ledger attachment open until source and UI audit prove access. |
| `super_event_text_researcher_handoff.md` | Accepted research and text integration snapshot. | Keep the full research document as quotation and route-text authority. Recheck live localisation before final completion. |
| `super_event_audio_researcher_handoff.md` | Accepted audio package and integration snapshot. Its visual blocker is superseded. | Link to the final non-icon manifest and audio package index. |
| `documentation_curator_interim.md` | This source-of-truth and staleness map. It is intentionally interim. | Supersede with a final resume packet after fresh audits and final documentation reconciliation. |

## Exact Post-Stabilisation Update Map

Perform these updates only after the gameplay owner declares the Event 15 source set stable enough for a documentation freeze.

### 1. Freeze and inventory live source

Re-read and record exact identifiers from:

- `events/015_utopia_manifesto.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/ideas/015_utopia_manifesto_ideas.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- Event 15 script constants, enums, on-actions, dynamic modifiers, AI strategies, cosmetic tags, characters, achievements, interface, music, sound, and localisation

The inventory must include exact event IDs, decision IDs, mission IDs, focus IDs, idea IDs, achievement IDs, cosmetic tags, route and evolution constants, super-event slots, sprites, pictures, localisation keys, and all current counts.

### 2. Collect final audit evidence

Require fresh final handoffs for:

- focus tree
- decisions and missions
- country package
- localisation
- event completion

Do not promote old failure findings to resolved unless a fresh audit or direct source review proves resolution. Do not discard still-valid findings merely because their counts are stale.

### 3. Rewrite the canonical mechanic document

Rewrite `docs/events/015_utopia_manifesto.md` from final source and final English localisation. It should cover:

- entry conditions and actor selection
- the four-value Ledger and how values change
- all five route commitments and route locks
- external need cases, methods, responses, settlement, stewardship, and cleanup
- decisions, missions, focus branches, ideas, country identities, AI behaviour, and achievements
- the event chain, reactions, evolutions, world-end branches, Event Details, event log, and super-event package
- player-facing UI access, including the actual Ledger entry point
- exact asset families and their authoritative manifests
- balance and lifecycle interactions
- future plans that remain genuinely unimplemented

Write it as if the feature has always existed. Do not retain replacement-history or tuning-history language.

### 4. Promote accepted architecture into the specs

Update:

- `spec_part_2_commonwealth_ledger.md`
- `spec_part_4_decisions_and_missions.md`
- `spec_part_7_ai_balance_and_compatibility.md`
- `matrices/decision_mission_matrix.md`
- `matrices/target_eligibility_matrix.md` if final case eligibility differs from the accepted matrix

Promote only implementation-backed or explicitly accepted clarifications from `scripted_system_architect_case_review.md`. Record rejected, queued, and unresolved recommendations with reasons.

### 5. Reconcile acceptance and coverage documents

Update:

- `spec_part_8_assets_localisation_and_acceptance.md`
- `matrices/completion_coverage_matrix.md`
- `matrices/asset_manifest_plan.md`
- `matrices/achievement_matrix.md`
- `matrices/country_package_matrix.md`
- `matrices/idea_lifecycle_matrix.md`
- `README.md`

Part 8 should summarise the final super-event text and audio decisions and point to the full research. Matrices should distinguish design requirement, implemented source, audit evidence, and unresolved status.

### 6. Rebuild the asset index and exact mapping

Update `docs/assets/015_utopia_manifesto/manifest.md` so its opening section is a current family index. It should link to the final non-icon, route-identity, icon-frame, and audio authorities. Move historical packages into clearly labelled history sections.

Then:

- regenerate `decision_icon_mapping.csv` against the frozen source
- regenerate `final_icon_frame_audit.json`
- update `gfx_handoff.md` to show completed registration
- mark `generated_event_art_handoff.md` as superseded for current route-image coverage
- correct stale image-blocker language in `icon_animation_handoff.md`
- add the route-identity manifest and wiring handoff to the root index
- reconcile every current event picture, decision icon, idea picture, achievement sprite, flag, portrait, emblem, and super-event sprite with live references

Do not delete historical assets or handoffs merely to simplify the index. Classify them.

### 7. Reconcile super-event research status

Update:

- `docs/super_events/015_utopia_manifesto_super_event_audio_research.md`
- `super_event_audio_researcher_handoff.md`
- `super_event_text_researcher_handoff.md` if final localisation changed

Remove only stale integration-risk statements. Preserve quotation, attribution, licensing, checksum, and source provenance.

### 8. Add status banners to archival records

Add concise status notices to the package README or affected historical files so readers can distinguish:

- accepted design
- execution template
- initial-state snapshot
- implementation snapshot
- superseded audit
- current audit
- unresolved addendum
- final asset provenance

The prompt directory needs one package-level notice. It does not require rewriting every completed prompt.

### 9. Create the final resume packet

Supersede this interim with a final Event 15 resume packet under `docs/plans/015_utopia_manifesto_plans/`. It should contain:

- final source-of-truth order
- final runtime inventory
- links to final audits
- accepted addendum dispositions
- closed and open blocker ledger
- asset and audio authority map
- spreadsheet alignment status
- exact list of remaining work, if any

### 10. Update spreadsheet-facing records last

Only after gameplay identifiers and English localisation are frozen, route the final implementation facts to `chaosx_spreadsheet_doc_worker`. Spreadsheet event details, evolution details, and cluster details must match in-game wording. This interim audit does not establish spreadsheet alignment.

## Required Evidence Before Final Curation

Final documentation reconciliation must wait for or explicitly report the absence of:

- the active fresh focus-tree audit
- the active fresh country-package audit
- a fresh decision and mission audit after current source drift
- a fresh localisation audit after all new decision, mission, event, focus, idea, and country keys are final
- a final event-completion audit
- an explicit disposition for the unresolved case-architecture decisions
- a decision on whether an improvement-loop addendum is accepted, queued, rejected, or unnecessary
- final spreadsheet alignment against final English localisation
- confirmation that the Ledger has a real player-access path or a clearly reported runtime blocker

## Documents Inspected

This curation pass inspected:

- all Event 15 numbered specs, matrices, focus graphs, research records, handoffs, prompts, README, and package manifest
- all handoffs in `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`
- `docs/events/015_utopia_manifesto.md`
- the Event 15 root asset manifest, final non-icon manifest, route-identity manifest, icon audit, decision mapping, asset handoffs, and prompt records
- Event 15 super-event text research, audio research, and the shared audio-package index
- current Event 15 gameplay, localisation, interface, asset registry, music, and sound identifiers on a read-only basis
- the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, and AI
- relevant vanilla documentation for script concepts, localisation formatting, decisions, on-actions, scripted GUI, script constants, effects, and triggers

## Simplifications, Omissions, and Blockers

This is an interim documentation map, not a final Event 15 completion report.

- No gameplay, localisation, assets, spreadsheets, or source specifications were changed.
- Historical files were not rewritten because their evidence value depends on preserving the state they recorded.
- The canonical event document was not rewritten because gameplay and audits were still active.
- Counts are inspection snapshots and must be regenerated after source freeze.
- This pass does not resolve the open Ledger access issue, settlement-agreement localisation gap, stale icon mapping, case-architecture design questions, or any audit finding.
- No final completion claim is made.
