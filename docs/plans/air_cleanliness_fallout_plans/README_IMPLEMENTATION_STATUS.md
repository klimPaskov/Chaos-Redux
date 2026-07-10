# Air Cleanliness and Fallout Repository Implementation Status

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Purpose

Air Cleanliness and Fallout are handled as an unnumbered system package. Fallout is a terminal world rewrite and manual scenario with its own event file, `chaosx.fallout` namespace, GUI, GFX, asset package, and optional audio package.

This package converts the accepted Air Cleanliness and Fallout design pack into a repository implementation plan. It does not replace the source specifications in `air_cleanliness_fallout_planning_package_expanded.zip`. It records the live repository state, resolves design ownership, orders implementation tranches, defines hard validation gates, and preserves the exact next starting point for a writable local checkout.

## Repository snapshot inspected

- Repository: `klimPaskov/Chaos-Redux`
- Branch inspected: `master`
- Commit inspected: `8044d232376fef3a1a3ca1ea3e0d487523924cc6`
- Access mode in this pass: read only through the GitHub connector
- Gameplay edits made: none
- Repository files created or changed: none

## Source design status

The accepted source design remains the expanded planning package with Part 1 through Part 12, three dedicated matrices, research notes, prompts, and the manual improvement-loop closure pass.

The source pack defines:

- a state-based Air Winter system
- a dedicated winter mapmode
- population, building, supply, and state-category consequences
- flavour events with real mechanical effects
- a reusable Fallout aftermath framework
- a black-screen cinematic transition instead of a normal super-event
- a total world rewrite with survivor governments, warlords, mutant fiction, and regional successor content
- a manual scenario that strikes every valid province, waits seven days, then starts the rewrite
- a three-layer focus design made from an archetype skeleton, regional overlay, and country memory overlay
- a candidate pool of 99 successor identities

The source pack remains design authority unless a later user decision changes it. This implementation plan does not shorten that design.

## Current implementation state

The live repository already contains several useful foundations:

- global Air Contamination in basis points
- a host-owned monthly contamination update
- nuclear fallout state intensity and daily population loss
- irreversible contamination and state-category degradation helpers
- a data-driven triggerable-scenario window
- two scripted state mapmodes
- runtime focus-tree assignment through `load_focus_tree`
- a large pool of custom successor tags from Soviet Collapse
- cosmetic-tag patterns and country transformation helpers

The live repository does not yet contain the accepted Fallout overhaul. A stale terminal Fallout block exists outside a dedicated Fallout event file and sets normal world-end and super-event state. Delete it and do not retain it as a wrapper. The current winter mechanic is a random-state modifier pulse and lacks a persistent state phase system.

## Hard implementation gates

Gameplay work must not begin until the following checks are completed in a writable local repository:

1. Read the local offline Paradox wiki pages required by `AGENTS.md`.
2. Read the official Hearts of Iron IV documentation under the local game installation.
3. Confirm the exact engine effect available for a thermonuclear strike on every valid province.
4. Inspect the actual selected and deselected mapmode strip textures and reconcile their frame count with the `.gfx` definition and documentation.
5. Scan the live manual scenario registry and allocate Fallout to the next integer after the highest assigned id.
6. Build a tag conflict ledger from vanilla tags, Chaos Redux tags, releasables, dynamic tags, and other feature-owned packages.
7. Confirm the supported full-screen scripted GUI parent and drawing order against local vanilla GUI files.
8. Create the dedicated Fallout event, script, GUI, GFX, asset, and optional audio ownership surfaces before migrating any caller.

A missing proof at any gate is a blocker. It must not be replaced with a smaller effect without explicit user approval.

## Accepted implementation order

1. Reconcile source-of-truth documents and live code facts.
2. Create `events/fallout_world_end_events.txt`, the `chaosx.fallout` namespace, and the dedicated Fallout asset surfaces.
3. Implement the Air Winter state model and mapmode.
4. Add winter population, building, supply, category, flavour, mitigation, AI, and treaty behavior.
5. Implement the reusable Fallout request coordinator and black-screen state machine.
6. Implement deterministic world-state grading and the world rewrite.
7. Add the manual Fallout scenario after exact province-strike feasibility is proven.
8. Implement a manually reviewed pilot batch of successor countries.
9. Expand successor and focus content in regional batches.
10. Complete assets, localisation, documentation, spreadsheet alignment, and audits.

## Implementation ownership

The parent implementation agent owns cross-system integration, final behavior, validation, and completion claims.

Recommended bounded subagent use:

- `chaosx_scripted_system_architect` for shared effects, triggers, constants, cleanup, and state-machine logic
- `chaosx_decision_mission_auditor` after the winter response and survival decision systems exist
- `chaosx_country_package_auditor` after each successor batch
- `chaosx_focus_tree_auditor` after each focus batch
- `chaosx_localisation_auditor` after broad visible text exists
- `chaosx_documentation_curator` after each major implementation tranche
- `chaosx_spreadsheet_doc_worker` only after in-game wording and implementation facts are stable
- `chaosx_event_completion_auditor` before any completion claim

All project custom subagents must use `fork_context=false` and must receive explicit paths, constraints, accepted design rules, and current implementation status.

## Current stopping point

Repository implementation planning is complete in this package. No gameplay code has been changed. The next pass begins in a writable local checkout with local official documentation available.

The first implementation action is Tranche 0 from `IMPLEMENTATION_TRANCHE_PLAN.md`, beginning with the three blocking proof tasks:

- mapmode texture frame verification
- next-free scenario id allocation
- exact province-wide thermonuclear effect validation
