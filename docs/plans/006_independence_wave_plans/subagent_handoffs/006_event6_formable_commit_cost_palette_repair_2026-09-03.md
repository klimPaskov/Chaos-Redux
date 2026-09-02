# Event 006 formable commit-cost palette repair — 2026-09-03

## Scope

This tranche repairs the DM-55 `independence_wave_proclaim_military_union` cost surface. The previous revolutionary, military, and hidden high-chaos branches debited the strategic package and a security package, exposing seven distinct spendable resource families while the decision could not present a compact, honest cost row.

## Accepted palette

- Negotiated, dynastic, and league formable methods retain the existing civic palette: stability, command power, transport, and manpower. The civilian-factory availability check remains a non-consumed project-capacity requirement.
- Revolutionary union uses the existing standard security package: manpower, army experience, infantry equipment, and support equipment.
- Military settlement and hidden high-chaos proclamation use the existing major security package: manpower, army experience, infantry equipment, and support equipment.

The revolutionary, military, and hidden high-chaos branches no longer pay the strategic package. This is an intentional balance change, not a localisation-only shortening, and keeps every player-facing formable commit action within the four-distinct-spendable-cost limit.

## Files and identifiers

- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` — `independence_wave_formable_pay_selected_commit_cost` now invokes the strategic package only for civic/dynastic/league methods.
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` — `can_pay_independence_wave_selected_formable_commit_cost` now gates revolutionary/military/high-chaos methods only through their matching security package.
- `localisation/english/006_independence_wave_formable_registry_l_english.yml` — revolutionary and military cost rows reuse the canonical four-resource security strings; the civic row remains compact and icon-first.

## Validation and remaining evidence

The parent reruns the focused Event 006 allocator, scenario, flags, country-API, GUI-matrix, and FORM-16 validators after this change. A same-scenario probability baseline/compare is required for the availability change; typed formable scenarios remain dependent on the MCP schema and the named probability-auditor route.

No package admission, generic fallback, portrait, flag, audio, GUI, or runtime claim is changed by this tranche.
