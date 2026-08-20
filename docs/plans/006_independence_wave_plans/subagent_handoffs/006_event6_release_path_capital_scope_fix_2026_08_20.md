# Event 006 release-path and dormant-capital fix — 2026-08-20

## Disposition

Implemented a bounded runtime repair for manual `chaosx.nr6.1` execution. The pre-event crisis category, pressure surface, queue, and cost localisation remain retired; the first player-facing surface is still the post-commit `chaosx.nr6.2` report.

## Source changes

- `events/006_independence_wave.txt`: the public report now requires a positive committed presentation count instead of the calm-world target of three. A valid partial wave can therefore display after the allocator commits one or two source-complete packages.
- `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`: IW-024 now uses the loader's `standard` package depth in both initialization and prepared-setup gates. This removes the AXX/82 setup rejection caused by the former `regional` mismatch.
- `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt`: admitted IW-040/KUB uses its exact package identity gate rather than the retired generic `independence_wave_package_content_ready` flag.
- `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt`: admitted IW-044/TAT and IW-045/BSK use their exact package identity gates rather than the retired generic content flag.

## Capital-scope error boundary

The reported line-17 `capital_scope` calls are no longer present in the current Epirus, Thrace, or Banat package triggers. Their fixed anchor checks use numeric state scopes with `is_capital = yes`, which remain valid when the dormant carrier does not yet own a capital. The remaining dynamic `capital_scope` calls are limited to live, already-scoped package mechanics outside those three dormant-carrier gates.

## Evidence

- `python .tools/audit_event6_allocator.py`: passed with 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and no pre-event category/mission/cost/queue.
- Static release-path checks confirmed no fixed `capital_scope = { state = ... }` remains in Event 006 package triggers, IW-024 depth parity is restored, and the three admitted exact package gates resolve.
- Fresh Event MCP lint: `EVENT_INSPECTED_PARTIAL`, revision `56319cc12de881e50904384f7991f675b88c92bf9c05828ec8c86ff0efb828fa`, zero selected blocking diagnostics; workspace-wide helper/lifecycle validation remains deferred.
- Fresh Event MCP state render: `EVENT_RENDERED_PARTIAL`, same revision, zero selected blocking diagnostics; source-linked JSON/SVG/PNG/HTML artifacts were produced.

## Remaining limits

The whole Event 006 completion boundary remains HOLD/PARTIAL. Unattested package breadth and the MCP workspace-wide deferred-analysis limitation are unchanged. No central attestation, Join order, pre-event UI, or unrelated package was widened by this repair.
