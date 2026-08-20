# Event 006 empty-shell release validation fix — 2026-08-20

## Disposition

Implemented a bounded shared-release validation repair for Event 006 dormant carrier shells. Empty AXX, BAX, and BBX country shells are instantiated at startup so their characters can be parsed, but they own no states and have no capital before release. The validator previously rejected every existing target as a living country, preventing the frozen plan from reaching execution even after the invalid fixed-state `capital_scope` calls were removed.

## Source change

- `common/scripted_effects/chaosx_liberation_release_effects.txt`: `liberation_release_validate_country_rows` now permits an existing target only when it is an Event 006 row and satisfies `is_independence_wave_dormant_country_scope`. Event 005 rows and any active or non-dormant existing country still fail with `living_tag`; absent tags remain valid for the existing release path.

## Boundary

This does not create a pre-event category, pressure, mission, queue, or decision surface. It does not widen Event 006 content attestation, adapters, scenario preflight, or Join order. It only lets an already-selected dormant Event 006 shell survive the shared frozen-plan validation that precedes release.

## Validation

- The source block keeps the existing reserved-country, anchor, host, and package identity checks unchanged.
- The prior Event 006 allocator audit remains the governing static receipt: 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and no pre-event crisis surface.
- Fresh MCP Event 006 inspection/render remains partial with zero selected blockers; workspace-wide helper/lifecycle projection is deferred by the installed server.
- Post-change focused Event 006 lint/render again returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL` at revision `56319cc12de881e50904384f7991f675b88c92bf9c05828ec8c86ff0efb828fa`, with zero selected blockers and the same deferred workspace-wide validation boundary.

## Remaining limits

Whole Event 006 completion remains HOLD/PARTIAL. This repair addresses the concrete empty-shell rejection behind the “no countries appear” path; it is not a claim that every unattested package is executable.
