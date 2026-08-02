# IW-179 FSM source-gate correction

Status: **HOLD / fail-closed**.

## Scope

The IW-179 Micronesia setup trigger now requires
`independence_wave_fsm_sourced_identity_ready` before any package setup can
promote `FSM_independence_wave_inter_island_congress_chair` or expose its
portrait consumer. The flag is intentionally unset while the real-country
portrait source remains unresolved.

## Reason

FSM is a real-world country. Its previous package path could be reached by a
direct setup call even though the only available chair was the fictional
Elias Kihleng portrait and the package was already documented as outside
runtime attestation. That violated the real-country sourced-leader gate.

## Changed surfaces

- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`
  adds the explicit source-admission flag to
  `can_initialize_independence_wave_iw_179_package`.
- `docs/events/006_independence_wave/pacific_country_packages.md` records the
  gate and the no-promotion behavior.

## Validation

`python -B .tools/audit_event6_allocator.py` passes with the accepted ladder,
joint reservation order, scenario matrix, and current attestation boundary.
No portrait, advisor, character, GFX, DDS, or runtime asset was promoted.

## Remaining gate

An attributable adult male Micronesian/Pohnpeian/Carolinian source must clear
identity, era, role/community, and rights review before a parent-owned asset
handoff can set the admission flag and perform the normal source-crop,
identity-preserving HOI4 repaint, independent audit, DDS, and runtime wiring.
