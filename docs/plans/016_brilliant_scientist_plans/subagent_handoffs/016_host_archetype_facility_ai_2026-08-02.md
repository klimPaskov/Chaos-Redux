# Event 016 host-archetype facility AI handoff

## Scope

This bounded continuation applies the existing host-archetype AI tuning to the six ordinary Directorate facility decisions. It does not create a new decision, mission, meter, route, event, reward, asset, or model.

## Changed files

- `common/decisions/016_brilliant_scientist_directorate_facilities.txt`
- `docs/events/016_brilliant_scientist/systems/directorate.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

## Decision coverage

| Existing decision | Archetype preference |
| --- | --- |
| `brilliant_scientist_formalize_primary_research_campus` | university, industrial |
| `brilliant_scientist_expand_primary_prototype_works` | industrial, militarized |
| `brilliant_scientist_establish_secondary_laboratory` | university, refugee |
| `brilliant_scientist_relocate_primary_laboratory` | threatened, refugee |
| `brilliant_scientist_harden_primary_laboratory` | militarized, threatened |
| `brilliant_scientist_mobilize_primary_laboratory_repairs` | industrial, colonial |

The modifiers reuse `brilliant_scientist_host_flavor_ai` and the mutually exclusive host flags already assigned at appointment or transfer. Human availability, map targets, equipment and fuel gates, political costs, construction burdens, timers, effects, facility flags, and cleanup remain unchanged.

## Validation

- Confirmed all six facility decisions retain their original `ai_will_do` base and existing war, capacity, exposure, and control modifiers.
- Confirmed all six archetype multiplier keys and all six host-archetype flags already exist in `common/script_constants/016_brilliant_scientist_host_flavor_constants.txt` and the appointment/transfer effects.
- Confirmed no new localisation key, event id, decision id, map target, scripted effect, asset, entity, or model reference was introduced.
- Confirmed the equipment-gate drift in the shared worktree was normalized back to the authoritative helper-gated equipment file before this tranche; that unrelated correction is not part of this handoff.

## Simplifications and remaining blockers

This is a preference layer, not six bespoke country-specific facility chains. Quantitative AI ranking, live decision rendering, broader country flavour, live consumer acceptance, seven reusable 3D packages, and external redistribution rights for the copied stage-0 portrait remain outside this tranche.
