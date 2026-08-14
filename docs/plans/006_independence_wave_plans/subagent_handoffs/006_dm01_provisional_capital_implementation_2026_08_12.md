# Event 006 DM-01 provisional-capital implementation handoff — 2026-08-12

> The current source audit is `006_dm01_current_material_commitment_audit_2026_08_12.md`. This implementation handoff remains the initial material-commitment receipt; its pre-fallback branch detail and dated whole-event counts are historical traceability.

## Disposition

The accepted DM-01 contract is implemented as a country-scoped automatic mission with a paid material commitment, a dynamic 30-to-75-day founding window, explicit capital-loss failure, and an emergency relocation choice. This tranche does not claim whole-Event-006 completion.

## Runtime changes

- `common/script_constants/006_independence_wave_decision_constants.txt` adds the DM-01 duration adjustments and isolated-capital train/truck costs.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt` adds force-tier equipment gates, supply-node/transport gates, and the complete `can_pay_independence_wave_provisional_capital_cost` reservation predicate.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` pays infantry/support equipment plus either train or motorized equipment when the capital has no supply node, starts the mission once per country, and clears all DM-01 reservation/failure state during decision-layer cleanup.
- `common/decisions/006_independence_wave_decisions.txt` opens DM-01 only through the paid start effect, applies the accepted failure pressure, marks the successful capital administration state, and refreshes the idea lifecycle.
- `common/scripted_effects/006_independence_wave_effects.txt` retries the country-scoped start gate during normal state refresh and preserves the functioning-administration idea after DM-01 success.
- `events/006_independence_wave.txt` adds `chaosx.nr6.311`, which moves the capital only to an already owned and controlled non-capital state or records dispersed emergency offices.
- `localisation/english/006_independence_wave_decisions_l_english.yml` and `localisation/english/006_independence_wave_l_english.yml` disclose the material commitment, duration range, failure consequence, and relocation choices.
- `docs/events/006_independence_wave/dm01_provisional_capital.md` is the player-facing mechanic handoff and asset listing.

## Accepted values and behavior

Fragile force levels reserve the light infantry/support tier and run for 30 days; viable levels reserve the standard tier and run for 45 days; armed and high-chaos levels reserve the major tier and retain the 75-day ceiling. An isolated capital reserves 10 trains, or 100 motorized equipment when the train alternative is unavailable. The cost is sunk at mission start and is not refunded by cancellation.

The source uses explicit gate constants one unit below each displayed payment amount because the HOI4 `has_equipment` comparison is strict: the light, standard, and major infantry/support gates are 249/49, 499/99, and 999/199, while the isolated transport gates are 9 trains or 99 motorized equipment. This makes exact displayed stockpiles eligible without changing the paid amounts.

The mission can begin only when the package is active and complete, the capital is controlled, the force-tier garrison is present, and the equipment/transport gate is satisfied. The retry is country-scoped through `independence_wave_refresh_country_state`; no periodic world callback or global scan was introduced.

Loss of capital control or the required garrison records the failure flags, applies ledger pressure, refreshes collapsed-cabinet and warlord-command ideas, and opens the country event relocation choice. Successful timeout sets `independence_wave_dm01_capital_secured` and `independence_wave_dm01_capital_administration_ready`, so later refreshes keep the functioning-administration idea until a stronger regional-power lifecycle takes precedence.

## Evidence and limits

Static source review, focused block checks, and the existing Event 006 allocator/scenario audits were used for this tranche. Fresh `hoi4.probability_inspect`/event evidence is unavailable because the installed MCP workspace returns `ARTIFACT_MANIFEST_INVALID` (“Artifact provenance manifest is invalid”) before scanning. No live HOI4 run or save/load claim is made.

The wider Event 006 remains HOLD/PARTIAL: the dated snapshots cited by this implementation receipt are historical, while current routing is 32 content-attested packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters; eight adapter-only packages remain fail-closed, and several asset/rights and super-event gates are unresolved.
