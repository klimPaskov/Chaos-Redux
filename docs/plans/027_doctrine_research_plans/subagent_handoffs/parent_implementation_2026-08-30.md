# Event 027 parent implementation handoff

> **Superseded status notice (2026-09-01):** This dated implementation handoff is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its intentional-exclusion claim for the default allowlist is contradicted by the current source.

## Scope completed in source

The parent replaced the stale Event 027 source with the global `chaosx.nr27.1` fanout and the country-owned append-only batch/receipt ledger.

The source covers Army, Navy, Air, verified Special Forces, Chaos Warfare, and a disabled future-custom adapter through explicit numeric registry rows. All mastery-track actions are additionally fail-closed behind `doctrine_research_mastery_transaction_verified`; the separate empty-track proof is required on top of that flag.

The human chain includes opening, domain, Grand Doctrine, track, track-specific subdoctrine routing, confirmation, result, continuation, summary, invalid, ambiguous, and no-option events.

The AI uses the shared validity predicates and scored domain, Grand Doctrine, track, and subdoctrine selectors, recalculating after successful choices.

The parent removed the live AI first-subdoctrine fallback so an unresolved scored pool now fails closed instead of selecting an unscored candidate.

The source adds receipt states, parent-link validation, post-effect finalization, annex cleanup, lifecycle reconciliation, achievement receipts, Event Details and evolution mappings, cluster registration, controlled manual dispatch, National Breakthroughs integration, localization, final DDS assets, and workbook/export alignment. Event 027 is intentionally excluded from the default reworked-event enable list until the unsafe/unproven mastery path is accepted.

The source adds a centralized 90-day one-stage evolution clock to the existing global-host daily coordinator without adding a recurring country fanout.

## Files owned by this handoff

Gameplay and registry files include `events/027_doctrine_research.txt`, `common/script_constants/027_doctrine_research_constants.txt`, `common/scripted_effects/027_doctrine_research_effects.txt`, `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`, `common/scripted_effects/027_doctrine_research_ai_effects.txt`, `common/scripted_triggers/027_doctrine_research_triggers.txt`, and `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`.

Integration files include the Event 027 settings, cluster, event-log, event-details, synchronized-token, on-action, achievement, CXT, GFX, and shared localization files touched by the implementation.

Documentation files include `docs/events/027_doctrine_research/overview.md`, this handoff, the MCP evidence handoff, and the existing specification-package handoffs.

Asset files include the Event 027 report image, nine achievement DDS files, their source/processed asset handoff files, and `interface/027_doctrine_research.gfx`.

The editable catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; its export-only CSVs were regenerated after the update.

## Evidence reviewed

All files in `docs/specs/027_doctrine_research_specs/` were read as acceptance criteria before editing.

Required offline Paradox wiki pages, vanilla documentation, vanilla doctrine definitions, Chaos Warfare definitions and gates, Event Log and cluster registries, achievements, assets, AI source, and the catalog workbook were inspected before and during implementation.

The localization auditor and completion auditor were run as isolated project subagents with `fork_context=false`, and their handoffs are retained in this directory.

The required final probability comparison was attempted against all 37 named scenarios and is retained in the MCP evidence handoff.

## Unresolved acceptance items

The active-track and empty-track mastery routes are intentionally fail-closed because local engine evidence has not proven that native one-level assignment, banked-progress preservation, and the empty-track subdoctrine selection transaction are safe and atomic.

The current exact-mastery source is a bounded one-point/readback adapter, but the local engine has not proven preservation of fractional banked mastery, low/middle/final level behavior, or separate Event 027 attribution.

Receipt state handling prevents guessing after an ambiguous result, but save/reload recovery of prepared and effect-applied native transactions has not been proven.

The subdoctrine pages now have explicit stable two-page candidate routing, but no accepted in-game overflow/pagination evidence.

The global evolution clock is source-level and uses the existing host coordinator, but its timing and history behavior still need live and MCP evidence.

The Event Viewer comparison baseline and complete four-domain technology comparison are blocked by the installed MCP artifact/cache and scan-byte limits.

The probability comparison exposes an incomplete candidate state rather than producing accepted scenario orderings.

The worktree is therefore incomplete for the user's acceptance standard and must not be committed as a finished Event 027 change.
