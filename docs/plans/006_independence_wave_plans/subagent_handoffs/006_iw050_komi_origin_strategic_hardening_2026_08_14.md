# IW-050 Komi origin and strategic-cost hardening

## Disposition

Implemented a package-local lifecycle and cost-display hardening pass for IW-050. Central adapter, content attestation, normal and SCN-008 preflight, deterministic Join, and workbook surfaces remain unchanged.

## Source changes

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` now excludes `independence_wave_origin_ended` from Komi project readiness, while the existing generation guard remains active.
- `common/decisions/006_independence_wave_komi_decisions.txt` adds the origin-ended cancellation guard to the founding mission and all ten timed projects.
- The former-host ledger project also cancels when `has_independence_wave_komi_unsettled_host = yes`.
- The former-host ledger and Northern Ural corridor projects use `independence_wave_komi_cost_strategic` and reserve the package civilian-factory burden with `civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE`.
- `localisation/english/006_independence_wave_komi_l_english.yml` defines the package-specific strategic cost label.

## Evidence boundary

The patch changes availability, cancellation, and player-facing cost presentation; it does not change AI score formulas. Existing Komi probability evidence remains `no_weighted_surfaces` / incomplete mission pool, so no quantitative selection, timing, or balance claim is made. Event and focus MCP evidence remains partial at workspace scope, with no new central admission claim.

## Remaining gates

IW-050 remains package-local and fail-closed pending portrait identity/rights, stable neutral flag provenance, typed probability fixtures, and parent-approved central attestation/preflight/Join promotion.
