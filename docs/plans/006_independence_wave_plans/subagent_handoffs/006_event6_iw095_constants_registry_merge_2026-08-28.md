# Event 006 IW-095 constants registry merge handoff (2026-08-28)

## Scope

The 1.8 KB IW-095 Dahomey constants parser file was consolidated into the existing Event 006 script-constants registry to reduce parser-file fragmentation without changing any constant name, value, schema, or consumer.

## Changed source surfaces

- `common/script_constants/006_independence_wave_constants_registry.txt` now owns the `# [source: 006_independence_wave_iw095_constants.txt]` section with the four `independence_wave_dahomey_*` definitions.
- `common/script_constants/006_independence_wave_iw095_constants.txt` was removed after its definitions were copied source-equivalently.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` now point to the canonical constants section.

## Preserved behavior

The pressure, cost, politics, and duration schemas retain their original keys and values, including the state-776 civilian-factory serialization note.

No package admission, reservation group, readiness gate, decision cost, AI weight, trigger, effect, country shell, asset, or pre-event visibility surface was changed.

## Evidence

The Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 validators remain green at the established 32 content-attested package / 29 compatible group / 40 adapter / 161 unattested-row boundary.

The canonical registry was checked for duplicate `independence_wave_dahomey_*` definition names before removal of the package-local file.

The required Event 006 MCP inspect/render route remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero scanned files and artifacts, so this tranche makes no engine, probability, live-session, or save-load claim.

## Remaining risks

IW-095 remains package-local and fail-closed pending its DAH identity and rights package, country shell, flag/emblem, approved portrait roster, central adapter/publisher/preflight/Join wiring, typed probability evidence, and repaired MCP artifact manifest.
