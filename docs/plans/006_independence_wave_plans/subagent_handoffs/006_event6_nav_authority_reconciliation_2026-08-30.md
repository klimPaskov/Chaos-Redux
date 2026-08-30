# Event 006 IW-013 NAV authority reconciliation

Date: 2026-08-30

Owner: Event 006 parent documentation authority

## Scope

This handoff reconciles the IW-013 Basque Country state wording in the candidate and research matrices. It does not change gameplay, package admission, reservation groups, flags, portraits, localisation, assets, Join, or live-runtime behavior.

## Authority decision

The installed-map runtime authority is state 792, País Vasco. Vanilla `NAV - Navarra.txt` sets the NAV capital to 792, and the installed binding, package triggers, reservation loader, formable registry, and shared `basque_anchor_state` constant already use 792 as the compact release anchor.

States 172 (Navarre) and 806 (French Basque) remain optional extension objectives. The numeric `172` retained in the two specification rows is historical baseline traceability, not the runtime compact anchor, and the row wording now says so explicitly. The existing reservation-group identifier `RG-172` remains unchanged because it names the accepted package collision group rather than asserting the compact state ID.

## Files changed

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`: clarified the IW-013 baseline-anchor name field.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`: clarified the IW-013 baseline-anchor name, compact release rule, and optional extension states.

No gameplay or asset file was changed. IW-013 remains absent from central content attestation and deterministic Join.

## Remaining blockers

NAV still requires independent flag and route-identity review, final Aguirre portrait-rights disposition, central content attestation, deterministic Join admission, typed probability evidence, and separate FORM-07 readiness. No fallback identity or unapproved source was introduced.

## Validation

- CSV header and row-field counts were checked after the wording-only edits.
- The IW-013 rows were searched for residual wording that calls 172 the runtime compact anchor.
- `python -B .tools/audit_event6_allocator.py` remains the next allocator check; this documentation-only change does not alter its package arithmetic.

No live HOI4 or save/load evidence is claimed.
