# Documentation README management — 2026-08-22

## Scope

This pass inventoried every filesystem `README.md` under `docs/`, including ignored active asset and provenance workspaces that Git-only file enumeration omits.

The pass updated durable documentation navigation and verified local Markdown targets without rewriting historical findings, deleting provenance, changing gameplay, editing spreadsheets, touching asset payloads, or changing GUI layout.

Event 021+ event-specific README content remained out of scope.

The shared `docs/specs/README.md` navigation may point to preserved Event 021+ design packages, but it explicitly treats those links as design/provenance navigation rather than current implementation status.

## README inventory

The pre-change filesystem inventory contained 71 `README.md` files under `docs/`.

Three durable documentation roots received new indexes, bringing the post-change inventory to 74:

- `docs/formables/README.md`
- `docs/spreadsheets/README.md`
- `docs/testing/README.md`

The inventory combined direct filesystem enumeration with Git tracking checks so ignored but active workspaces were not mistaken for absent documentation.

## Files changed

- `docs/README.md` now routes CBRN documentation to `docs/systems/cbrn_warfare/`, removes two nonexistent top-level warfare-directory claims, and links the durable formables, spreadsheets, and testing indexes.
- `docs/plans/README.md` now indexes current Event 001–020 plan roots, shared-system plan groups, and reusable workflow/model packages without requiring boilerplate READMEs in every working folder.
- `docs/specs/README.md` now indexes the Event 001–020 accepted-design roots, labels Event 021+ entries as preserved design/provenance navigation only, indexes shared specification packages, and recognises an equivalent named package index where a root README is not used.
- `docs/systems/README.md` now links the major shared subsystem documents and directories rather than leaving unresolvable prose-only names.
- `docs/super_events/README.md` now includes the Event 005 research package and links the shared source/processed audio directories.
- `docs/specs/condemnation_system_specs/README.md` now points to the current nested CBRN condemnation document.
- `docs/specs/006_independence_wave_specs/README.md` and `docs/specs/019_infantry_spawn_specs/README.md` had accidental mid-sentence hard wrapping removed without changing their status claims.

## New files

`docs/formables/README.md` documents shared formable-state ownership, the registry index, consumer manifests, and generated evidence boundaries.

`docs/spreadsheets/README.md` records the workbook-as-source rule, export-only CSV rule, exporter command, and separation of the doctrine workbook.

`docs/testing/README.md` distinguishes reusable test-country guidance and dated live-QA evidence from current design and implementation authority.

## Stale links and status text corrected

The only missing local Markdown target found across the original 71 READMEs was `docs/specs/condemnation_system_specs/README.md` pointing to the former `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` path.

It now points to `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md`.

The top-level docs index no longer claims that nonexistent `docs/biological_warfare/` and `docs/chemical_warfare/` directories own those subsystems.

The shared specification index distinguishes accepted Event 001–020 package roots from preserved Event 021+ navigation and does not claim current implementation completion for obsolete event-specific packages.

## Missing README candidates rejected

No central `docs/assets/README.md` was created because asset workspaces carry package-specific provenance and several are ignored, active, blocked, or recent; a central index would risk becoming a false completion ledger.

No README was added to every event folder because `docs/events/README.md` defines `overview.md` as the canonical event implementation summary.

No README was added to every plan or handoff directory because these are working and historical evidence areas indexed by `docs/plans/README.md` and package-specific source-of-truth maps.

No README was added to the empty `docs/content_dump/` directory.

No Event 021+ event-specific README was created, rewritten, or deleted.

## Event 021+ shared-navigation references touched

Only `docs/specs/README.md` was changed for Event 021+ navigation.

Its Event 021+ table preserves discoverability of existing design packages while explicitly withholding current implementation-status claims.

## Additional documentation maintenance

The historical `docs/plans/repo_cleanup/interface_audit_2026-07-22.md` retained its findings while accidental mid-sentence hard wrapping was removed.

`docs/plans/repo_cleanup/chaos_redux_repo_cleanup_goal_prompt.md` now points to the actual `chaos_redux_repo_cleanup_master_prompt.md` filename.

## Validation

A post-change filesystem inventory found 74 `README.md` files under `docs/`.

A local-link resolution pass across all 74 READMEs found zero missing local targets.

The validation included ignored existing README files, not only paths returned by `git ls-files` or default ignore-aware `rg --files` scans.

No gameplay, localisation, spreadsheet, asset payload, interface, GUI, `.codex`, or `.qoder` file was changed by this documentation tranche.

## Remaining uncertainty

Local target existence does not prove that every historical document describes current runtime behavior.

Historical audits, handoffs, and provenance were therefore preserved and routed through source-of-truth indexes or supersession notes instead of being deleted or silently rewritten.
