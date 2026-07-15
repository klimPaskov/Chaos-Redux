# Event 014 Documentation Final Reconciliation Handoff

> Historical checkpoint. Current Event 014 documentation authority is the 2026-07-15 audit set. The preserved `Implemented` catalog wording below predates the repository-wide `Fully Functional` status vocabulary.

Date: 2026-07-12

Mode: documentation-only curation

## Outcome

The Event 014 canonical overview, twelve-part source specification, implementation matrices, package status, validation boundary, anti-spoiler audit, package README, asset authority map, accepted closure addenda, and historical-ledger disposition are reconciled to the current repository implementation.

No gameplay, localisation, GFX, audio, workbook, skill, or binary asset file was edited by this documentation pass. No commit was created.

This handoff closes the documentation reconciliation tranche and incorporates the completed final event audit and catalog promotion. It does not claim that an in-game runtime session was run.

## Current implementation record promoted into the source docs

| Surface | Current fact recorded |
|---|---|
| Focus trees | 72 local warlord focuses, 108 unified focuses, and 28 Wendigo overlay focuses |
| Shared target model | Two country scorers, two decision-weight MTTH entries, and six unified targeted-decision consumers |
| P3 AI boundary | The pre-lock scored strategy package is idempotent. It can add newly valid targets, but an existing target is not dynamically removed or re-banded. Post-lock scoring is a separate one-time escalation package |
| Wendigo Pack | The original ZZZ country is transformed in place. Normal queue recruitment for the locked 16-battalion Pack is disabled before the first overlay focus. Both Event 014 recruitment paths are paid scripted musters |
| Pack accounting | The ordinary two-Pack path and receipt-backed one-Pack path share the complete-batch capacity check. Enemy-death receipts use non-retroactive snapshots, bounded per-enemy epochs, re-war reset, and shutdown cleanup |
| Inherited systems | Three Pack support stages, four inherited origin-template stages, two inherited commander stages, and the paid inherited winter-cell operation are recorded |
| Terminal hunt | Four surfaces are live: launch, mission, press, and defender break |
| Missions and actions | Eight maintained mission families and seven added paid action families |
| Achievements | 18 real achievements plus an 18-entry staged read-only tracker |
| Scenario | `SCN-010` supports five launch types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence |
| Event Details | Two independent default-enabled post-reveal terminal rows and persistent toggles. Scenario 6 maps the ordinary world end to super-event 50. Scenario 7 maps the Wendigo world end to super-event 53 |
| Closure art | 21 registered closure textures, comprising 20 icons and one tracker panel. The package includes generated sources, processed finals, runtime DDS files, manifests, hashes, contact sheets, and a handoff |
| Portraits and animations | 56 regional warlord portraits. The revealed ordinary portrait uses 12 independently generated frames and the transformed portrait uses 16 independently generated frames |
| GFX closure | 816 Event 014 texture references across nine `.gfx` files, 598 unique paths, and zero missing runtime files |
| Action super-events | Four unique action images and audio roles: reveal 49, ordinary world end 50, global defeat 52, and Wendigo world end 53. ID 51 remains assigned elsewhere |
| Audio | Four unique 44.1 kHz OGG and WAV pairs with source and rights records |
| Reveal secrecy | Every public identity surface is gated by `cannibalism_reveal_complete`. Pre-reveal events, evolutions, focuses, decisions, GUI, Event Details, tracker rows, scenarios, reports, portraits, terminal rows, and audio presentation remain neutral |

## Source specifications promoted

Both accepted closure addenda are marked implemented and promoted:

- `2026-07-12_event014_post_implementation_closure_addendum.md` records the closed constituent technology union and 39 distinct unified decision-icon package.
- `2026-07-12_event014_focus_closure_addendum.md` records the implemented H-01, H-02, H-03, and M-01 tranche.

Accepted behavior is folded into source spec parts 4 through 12 where relevant. Parts 1 through 3 remain authoritative for the unchanged core, containment, evolution, and spread contracts.

The following current matrices were reconciled:

- focus route
- decisions and missions
- AI strategy
- asset inventory
- country package
- idea lifecycle
- hidden-identity surfaces
- super-events
- world reactions
- event map and state machine

## Documentation authority and supersession

Current implementation facts are read in this order:

1. Live gameplay, localisation, GFX, audio, and asset files.
2. The twelve Event 014 source specification parts and current matrices.
3. `docs/events/014_cannibalism.md`.
4. Current manifests under `docs/assets/014_cannibalism/`.
5. Final audits and remediation handoffs under `docs/plans/014_cannibalism_plans/subagent_handoffs/`.

The following files are retained as historical production snapshots and are explicitly superseded for current missing-file status:

- `014_live_asset_gap_map.md`
- `014_remaining_static_asset_ledger.md`
- `014_repo_exploration_map.md`

The following frozen ledgers remain useful as contract records, with their outputs accounted for by the current manifests:

- `014_flag_asset_frozen_ledger.md`
- `014_gui_dimension_ledger.md`

Historical subagent handoffs were not rewritten. Their checkpoint-era pending and missing statements are superseded by the source-of-truth order above and this reconciliation handoff.

## Disposition ledger

### Promoted and closed

- constituent technology union through the shared dynamic helper and all three recipient paths
- 39 distinct unified decision icons
- H-01 shared scoring and AI consumers
- H-02 paid terminal-hunt loop
- H-03 authored-value normalization and exception contract
- M-01 deeper paid Wendigo progression on the existing 28-focus overlay
- 21-texture closure art package
- staged achievement visibility tracker
- two Event Details terminal rows and toggles
- immediate paid-only Pack recruitment boundary

### Queued and unaccepted

Optional ideas A through C in the post-implementation closure addendum remain queued. They are not part of the implemented Event 014 contract and require explicit promotion before work begins.

### Rejected or superseded

- reused or fallback decision art
- generic or fixed-tag replacement for the original ZZZ Wendigo country
- ordinary queue recruitment for the transformed Pack
- transform-only leader portrait animation
- an additional route, country package, focus branch, currency, faction, evolution, super-event, or scripted GUI for this closure tranche
- old claims that registered Event 014 assets are still absent
- old pre-implementation statements that Event 014 is unregistered or undispatchable

### Completion disposition

- `event014_final_completion_audit_2026-07-13.md` reports completion-ready status with P0/P1/P2 zero and one accepted non-blocking P3.
- `Events!M15` and `Scenarios!F10` are promoted to `Implemented`, and the spreadsheet update helper matches both values.
- No completion blocker or pending catalog promotion remains.
- Any separately gathered in-game runtime evidence remains outside this definition-level documentation record.

No documentation fallback or simplification was used in this reconciliation.

## Audit evidence incorporated

- `event014_country_package_final_reaudit_2026-07-12.md` reports P0, P1, P2, and P3 all at zero. It confirms the immediate paid-only Pack boundary and preservation of the original ZZZ package.
- `event014_focus_tree_postclosure_reaudit_2026-07-12.md` reports no P0 or P1. Its documentation P2 is closed by this pass. Its bounded P3 is recorded explicitly in the AI source docs.
- `event014_decision_achievement_integration_reaudit_2026-07-12.md` reports no remaining High or Medium integration finding. Its tracker-only Low finding was patched before this reconciliation.
- `event014_localisation_final_reaudit_2026-07-12.md` reports completion-ready localisation and secrecy with P0/P1/P2/P3 all zero, zero missing reference families or constant tokens, zero Event 014 cross-file duplicates, and BOM across all 137 English YML files.
- The final closure-asset handoff reports all 21 required textures with no asset-production blocker.
- `event014_asset_final_remediation_2026-07-12.md` and the dated recheck in `event014_asset_final_reaudit_2026-07-12.md` report completion-ready assets and audio with P0/P1/P2/P3 all zero. The recheck covers 816 GFX references, 598 unique paths and hashes, 18 exact overlay composites, 54 matching achievement triplet files, 14 animations with 142 source and 142 processed frames, and zero stale manifest claims.
- `event014_final_completion_audit_2026-07-13.md` reports completion-ready status at P0 zero, P1 zero, P2 zero, and P3 one. The P3 is the accepted first-assignment pre-lock AI score band, followed by a separate post-lock rescore, and is not a completion blocker.
- `spreadsheet_audit/event014_catalog_final_reaudit_2026-07-12.md` records the completed promotion of `Events!M15` and `Scenarios!F10` to `Implemented` and confirms that the update helper matches.

The package validation record is deliberately definition-level, filesystem-level, manifest-level, and audit-level. It does not convert those checks into an in-game runtime claim.

## Files reconciled

- `docs/events/014_cannibalism.md`
- `docs/specs/014_cannibalism_specs/README.md`
- `docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md`
- source spec parts 4 through 12
- all ten current matrices
- `quality/package_status.md`
- `quality/package_validation.md`
- `quality/anti_spoiler_audit.md`
- `quality/manual_improvement_loop_review.md`
- `docs/assets/014_cannibalism/manifest.md`
- the two accepted improvement addenda
- the five historical asset, GUI, flag, and exploration ledgers named above

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `chaos-redux-event-assets`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`

No skill was created or updated.
