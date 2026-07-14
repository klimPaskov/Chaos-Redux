# Event 006 Repository Explorer Handoff

## Scope

Read-only mapping of the current Event 006 implementation, shared event infrastructure, installed tags, current-map anchors, scenario IDs, super-event slots, and likely implementation surfaces. The explorer made no gameplay, documentation, asset, or workbook edits.

## Required references used

- All mandatory offline Paradox wiki pages from `paradox_wiki/`, plus the focus, country, achievement, interface, sound, and music pages relevant to this event.
- Relevant vanilla documentation in the installed game, including script concepts/constants, effects, triggers, on-actions, decisions, scripted GUI, factions, AI strategy, and AI templates.
- Vanilla release, focus-tree, decision, faction, achievement, and event-asset precedents.
- `chaos-redux-events` and `chaos-redux-subagents`.
- All seven accepted Event 006 specification parts and their registries.

## Current implementation findings

- `events/006_independence_wave.txt` is an inert placeholder: hidden, `fire_only_once = yes`, `always = no`, and an empty option.
- The dedicated localisation file contains placeholder text only.
- Event 006 is registered as repeatable but is absent from the default allowlist and is explicitly rejected during active-pool construction.
- Liberations cluster membership exists, but Event 006 has zero participation weight and no joint Event 005/Event 006 reservation pass.
- Generic event-name selectors exist. Event actor mapping, Event Details data, evolution history, and preview reconstruction do not.
- No Event 006 country, focus, decision, mission, idea, AI, network, league, formable, achievement, asset, super-event, or audio implementation exists.

## Registry and map findings

- Accepted registry size: 206 packages.
- Reused registered tags: 78; all are currently registered.
- Reserved new Event 006 tags: 128; every one ends in `X`, none duplicates another resolved tag, and none collides with the installed vanilla or Chaos Redux tag registries.
- Reservation groups: 111.
- Numeric state anchors present in the accepted data: 155 unique IDs; all exist in the installed map.
- Several accepted baseline bindings point at older broad states despite more precise current-map states. Production readiness therefore requires a current-map semantic rebind, not only an ID-existence check.
- Chaos Redux currently supplies no `history/states` overrides for these bindings.

## Shared-system findings

- The current Liberations cluster queues members and fires them independently after a delay. It has no shared preflight or frozen release plan.
- Event 006 needs a pre-dispatch planning hook rather than planning inside the visible entry event.
- Super-event display slots 57 and 58 appear unused; accepted audio IDs are 6001 and 6002. Both allocations still require final source-level verification when wired.
- Proposed scenario `SCN-008` collides with the unreworked `Africa Is One` placeholder. Because Event 006 explicitly owns the accepted `SCN-008` design and the existing scenario uses constants throughout, the parent is migrating the placeholder intact to `SCN-011` and reserving ID 8 for Every Flag.
- The dirty catalog workbook belongs to concurrent work and must not be overwritten until ownership is clear.

## Recommended implementation order

1. Freeze current-map package bindings and compile the readiness whitelist.
2. Prove fixed-tag exact-state release against installed documentation and vanilla structure.
3. Implement the shared Liberations transaction coordinator and origin model.
4. Refactor Event 005 to publish exact provisional reservations and prevent cross-origin adoption/tree replacement.
5. Implement Event 006 planning, lock validation, synchronous execution, and result presentation.
6. Build the complete package, mechanic, focus, decision, AI, network, league, formable, scenario, asset, achievement, documentation, and catalog surfaces.
7. Run the specified improvement and completion audits.

## Risks carried forward

- Fixed-tag release is broad by default because it consumes owned cores; the coordinator must enforce the locked footprint through a documented core-mask/release/restore transaction.
- Current Event 005 terminal logic can adopt living non-Soviet recipients and overwrite focus trees unless origin exclusions are added.
- Current-map semantic anchor rebinding must be completed before packages enter readiness.
- The workbook remains a shared dirty surface.

## Simplifications

None. This was a read-only evidence handoff.
