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

## Follow-up scope-preservation correction

The first country-scoped implementation still relied on `ROOT` and `THIS` while entering `var:dhrondan_landing_state_id`. That scope transition was ambiguous in nested provider callbacks: the array mutation could be evaluated from the selected STATE rather than the invoking COUNTRY. `alien_infantry_register_landing_state` now saves the invoking COUNTRY and selected STATE as short-lived regular event targets, then performs `is_in_array` and `add_to_array` from the saved country scope. This makes the ownership boundary explicit for ordinary landings and the Event 019 provider-508 deferred commit without introducing a global ledger or a second DHR registry.

## Validation

The touched scripted-effect files remain brace-balanced. Repository precedent confirms regular country arrays support `add_to_array`, `is_in_array`, and `for_each_scope_loop`. A fresh post-correction `hoi4.event_inspect` state-flow pass for `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`. The matching bounded lint pass returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/678bfabc6eb84fdbff224e0d7fae1f62e48aee85d4d7780a78e2c8043c716038/5afba29c4a86076360b6e191bb05a6ed5a52ef004fef10ceccdc53cd956ad19b/event-lint-f588a2607444.json`. The matching read-only render produced state-flow PNG/SVG/JSON artifacts under manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd81c30903ef30ef048a6478c0c9c6795e0e6371e82631f253c3e17581525cda/ca626de89826dfcdd32e35b58609f9f2491151a02727e318add020b45e91049e/event-state-f588a2607444-manifest.json`. Both reports defer workspace-wide helper projections because the workspace is large.

The weighted rebellion source was inspected with `hoi4.probability_inspect` using `custom_weighted_pool` and `direct_random`; the first route returned `PROBABILITY_SOURCE_INSPECTED` with zero declared custom-pool candidates, while the second discovered the supported `random_list` adapter and the two revolt/no-revolt branches. A bounded `hoi4.probability_evaluate` run with named LOW, MEDIUM, and HIGH scenarios returned `PROBABILITY_ANALYZED`, zero unresolved inputs, and the expected 10/20/40 versus 90/80/60 branch arithmetic. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e6b12c1c58d429149c8cfd862db1eb27fa2828abe9b019d28f7742f5b3bc5d5/4f8da02cda90ddb1005a32456c01c0b3f80491073478574d0c2381ef2d085338/probability-ce533f32be4dd0efbce3f9f8.json`; the MCP emitted a nonblocking dominance warning because the 90% no-revolt outcome is intentionally dominant in the low tier.

The required read-only `hoi4.map_inspect` route also completed with `MAP_INSPECTED` and a complete searchable state catalog. The workspace has pre-existing map-position and floating-harbor diagnostics in `map/buildings.txt` (2,654 omitted errors after truncation); no Event 016 state definition was changed by this tranche, and those unrelated map errors remain a validation blocker for a clean map-wide result.

## Remaining ownership work

Transient Portal beachhead/extraction marker cleanup still requires a named containment/spread owner. Five DHR support-route markers remain documented future hooks rather than being consumed by duplicate decisions. Alien Infantry runtime entity acceptance remains blocked by the model handoff’s muzzle-locator, action-role, synchronization, and entity-wiring gates.
