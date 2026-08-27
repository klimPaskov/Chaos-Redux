# Event 006 IW-095 anchor rebinding reconciliation — 2026-08-27

## Scope

This handoff reconciles the accepted IW-095 Dahomey research identifiers with the current installed-map binding. It is documentation-only. No gameplay source, central admission gate, country history, state file, asset, localisation, or catalog row was changed.

## Finding

The accepted public 763-state research references intentionally retain baseline anchor identifiers `556` and `556 | 558` in:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`

The current installed-map binding is authoritative for execution. `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` records IW-095 as a fixed-anchor compact binding at state `776`, with the baseline reference `556`, and `rebound_to_current_split` (`776=FRA`). `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_binding_audit.md` confirms `556` is Bamako in the installed map while `776` is the Dahomey binding. The runtime publisher and candidate trigger already use `776`.

## Decision

Keep the public-baseline matrix values unchanged as research provenance. Use state `776` exclusively for current-map runtime anchoring, preflight, reservation, state transfer, capital assignment, and any future IW-095 package evidence. Do not treat this clarification as identity, force, portrait, flag, AI, probability, or content attestation evidence. IW-095 remains fail-closed and outside central admission until its complete package contract is independently proven.

## Validation evidence

- Runtime publisher: `common/scripted_effects/006_independence_wave_package_effects_registry.txt` (`independence_wave_load_package_iw_095`) uses state `776`.
- Package trigger registry: `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt` uses state `776` for the current anchor path.
- Installed binding: `package_bindings/006_current_installed_map_package_bindings.csv` preserves the baseline `556` only as a reference and binds runtime to `776`.
- No central IW-095 content attestation, normal preflight, SCN-008 preflight, or deterministic Join admission was changed.

## Remaining risk

IW-095 still lacks the identity, leadership, portrait-rights, period flag/symbol, forces, history/setup, politics/ideas/projects/settlements, focus, AI, localisation, cleanup, MCP, and typed-probability evidence required by the first-footprint addendum. This note resolves only the coordinate semantics and does not authorize admission.
