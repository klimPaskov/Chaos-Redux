# Event 006 IW-095 decision registry merge handoff (2026-08-28)

## Scope

The 20 KB IW-095 Dahomey decision parser file was consolidated into the existing Event 006 decision registry to reduce parser-file fragmentation without changing decision identifiers, mission timing, costs, gates, callbacks, or package admission.

## Changed source surfaces

- `common/decisions/006_independence_wave_decisions.txt` now owns the `# [source: common/decisions/006_independence_wave_first_footprint_decisions.txt]` section, its file-scoped civilian-factory constant, and the IW-095 first-footprint category with one founding mission and nine paid decisions.
- `common/decisions/006_independence_wave_first_footprint_decisions.txt` was removed after its definitions were copied source-equivalently.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` now point to the canonical decision registry section.

## Preserved behavior

The category and all nine decisions retain their original DAH package, setup, identity-rights, force, route, capital, former-host, network, and lifecycle gates.

The founding mission retains its cancellation and timeout behavior, and every paid project retains the serialized factory modifier, material-cost trigger, callback, failure cleanup, cooldown, and AI score.

No admission list, reservation group, publisher, adapter, readiness gate, decision cost, AI target, country shell, asset, or pre-event visibility surface was changed.

## Evidence

The moved category and decision identifiers were checked against the destination registry for duplicate names, and the registry tail was reviewed for balanced enclosing blocks.

The Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 validators remain green at the established 32 content-attested package / 29 compatible group / 40 adapter / 161 unattested-row boundary.

The required Event 006 MCP inspect/render route remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero scanned files and artifacts, so this tranche makes no engine, UI, probability, live-session, or save-load claim.

## Remaining risks

IW-095 remains package-local and fail-closed pending its DAH identity and rights package, country shell, flag/emblem, approved portrait roster, central adapter/publisher/preflight/Join wiring, typed probability evidence, and repaired MCP artifact manifest.
