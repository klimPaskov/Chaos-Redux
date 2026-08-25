# Event 016 country-scoped Alien Infantry landing registry handoff

## Scope

This tranche implements the severity-one ownership finding from `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md`. The reusable Alien Infantry API now stores committed landing state scopes in the caller country’s regular `alien_infantry_landing_state_registry`, rather than a global cross-provider array.

## Changes

- `common/scripted_effects/016_alien_infantry_api_effects.txt` writes the selected state scope only after successful ordinary or Event 019 deferred materialization, and writes it to the current country scope.
- `common/scripted_effects/016_dhrondan_country_effects.txt` counts, selects a capital from, transfers, and claims only the current pact host’s registry. It no longer scans every owned state for the historical marker or consumes another provider’s state records.
- `common/scripted_effects/016_alien_infantry_api_effects.md` and `common/scripted_effects/chaosx_dynamic_effects.md` now document the ownership boundary and the absence of a global cross-provider ledger.
- The earlier global-registry handoff is marked superseded while retaining its historical evidence.

## Causal guarantees

- A landing by country A cannot raise country B’s D’Rhondan revolt count or add country B’s state to DHR claims.
- A state scope remains in its provider country’s registry after ownership or controller changes, preserving the lost-state claim rule.
- Receipt revocation does not erase committed territorial history.
- No parallel DHR-only ledger and no world-wide `every_state` scan were introduced.

## Validation

The touched scripted-effect files remain brace-balanced. Repository precedent confirms regular country arrays support `add_to_array`, `is_in_array`, and `for_each_scope_loop`. A fresh `hoi4.event_inspect` state-flow pass for `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc3cd6c47c9f9412410975e6cc452487783d158c2f8098de9474377c3c042d99/7e0ecd2f9a291a10ff69e056a0a9259b89ef049b1156bf6e60d740a1b8236bdf/event-state_flow-f588a2607444.json`. The matching bounded lint pass returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9963b02624e1fdfb0f9bd4a10ec3db72b1b8db028c641f51e6fa8d6324948e6/5b6f397a1f7a568336c50e3e8c55fcfed407986978ce04e175a1dcd3cd9b1ba9/event-lint-f588a2607444.json`. Both reports defer workspace-wide helper projections because the workspace is large; no native map route is available for this bounded registry change.

## Remaining ownership work

Transient Portal beachhead/extraction marker cleanup still requires a named containment/spread owner. Five DHR support-route markers remain documented future hooks rather than being consumed by duplicate decisions. Alien Infantry runtime entity acceptance remains blocked by the model handoff’s muzzle-locator, action-role, synchronization, and entity-wiring gates.
