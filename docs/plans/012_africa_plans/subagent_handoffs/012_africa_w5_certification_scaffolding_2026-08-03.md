# Event 012 W5 certification scaffolding handoff

Date: 2026-08-03

Status: Source scaffold implemented and accepted after the 2026-08-03 six-package asset, localisation, AI, focus, identity, and documentation tranche. Runtime certification remains political-roster-gated, but the reviewed post-freeze callsite is wired.

## Scope

This tranche closes the missing helper surface without creating a tag, installing a package, setting a route, transferring territory, or opening terminal presentation. The six external package surfaces are now accepted source content; the runtime call still waits for a complete frozen six-entry candidate roster.

## Gameplay source

- `common/scripted_triggers/012_africa_world_order_triggers.txt` now defines `africa_world_all_package_runtime_surfaces_are_certified`.
- `common/scripted_effects/012_africa_world_order_effects.txt` now defines `africa_world_certify_all_package_runtime_surfaces`.
- The roster-proof trigger requires the Event 12 host, a six-entry pending roster, zero absent and resolved entries, six exact continent slots, live sovereign candidates, controlled non-African capitals, and no successor, exile, breakup, terminal, installed, or high-chaos substitution state.
- The source-tranche writer records seven named receipts (`route`, `focus`, `decision`, `idea`, `AI`, `identity`, and `localisation`) before the separate review-writer effect records `africa_world_package_runtime_surfaces_reviewed`. The certification setter then requires all seven receipts plus the review receipt, rechecks the roster proof, iterates only the frozen `africa_world_package_candidates` array, sets `africa_world_package_implementation_ready` for all six candidates, and records `africa_world_package_runtime_surfaces_certified`. A second call is a no-op.
- The reviewed post-freeze callsite invokes the review writer and then the setter only after the exact six-entry roster has been frozen. The setter remains separate from Action 85 installation and the successor continuity writer.

## Validation

- Focused `hoi4.event_inspect` lint for `chaosx.nr12.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Workspace-wide helper analysis was deferred by the MCP.
- Scoped source inspection confirms the initial readiness writer is now the W5 setter and the existing successor writer remains the only continuity writer.
- Scoped Event 012 scripts contain no unsupported `<=` or `>=` operators.
- `git diff --check` remains clean for the tranche.

## Remaining acceptance

Models remain outside this tranche by user instruction. Actions 85-92 and terminal presentation remain closed until their ordinary political and lifecycle triggers succeed; they are no longer blocked by missing package identity assets or an absent W5 callsite.
