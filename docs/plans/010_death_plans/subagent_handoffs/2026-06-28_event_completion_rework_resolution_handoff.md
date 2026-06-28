# Event 010 Death Rework Completion Resolution

Date: 2026-06-28

Parent task: revisit Death evolutions and simplify SCN-006 into one Instant Outbreak scenario.

## Audit Findings Addressed

| Finding | Resolution |
| --- | --- |
| SCN-006 launch consumption still reached the shared Death deaths ledger and could raise Chaos during setup. | `death_consume_current_state` now skips `death_register_consumed_population_deaths` while `death_triggerable_scenario_started` is set, using direct population removal for launch setup only. Natural Death consumption after cleanup still uses the shared deaths ledger. |
| Pre-world-end ghost hosts needed clearer passive behavior. | `death_public_death` no longer pushes aggressive focus behavior, and `common/ai_strategy/010_death.txt` gives DTH careful non-executing front control on active wastelands before world-end. World-end switches the same target filter to rush execution. |
| SCN-006 could launch during another active world-end state. | `triggerable_scenario_can_launch_selected` now blocks Death scenario launch while the global `world_end` flag is present. |
| The scenario catalog needed to reflect the one-type scenario. | The workbook and triggerable scenario docs now describe Death as Instant Outbreak only, with intensity controlling starting footprint and ghost hosts. |
| Early Death evolution names duplicated Chaos Meter tier names. | Player-facing evolution names now use Death-specific milestones: Second Shore and Mainland Hunger. |
| Mainland reveal set Death as a world threat source too early. | `world_threat_source_death` now waits until Death has consumed a continent. Public mainland reveal still handles reveal, war, containment, and pressure behavior. |

## Current Implementation Shape

- Baseline Death consumes one remote island, records the event, schedules subtle delayed local reports, and waits.
- Second Shore records the first real evolution and unlocks slow island spread through Death focus choices.
- Mainland Hunger records the second evolution and unlocks the mainland reveal focus path.
- First Hosts records around the 600 tier and unlocks weak passive custom ghost hosts.
- Hollow Hosts records around the 800 tier and unlocks stronger but still inferior ghost hosts.
- World End records only after the terminal Death branch starts, then enables infantry-scale aggressive hosts.
- SCN-006 has only Instant Outbreak. It consumes an origin, intensity-scaled extra islands, at least one mainland reveal state, and intensity-scaled starting hosts without setting Chaos, shortcutting natural evolution records, or starting world-end.

## Validation Notes

- Focus audit patched the public reveal and first host gates.
- Localisation audit patched SCN-006 text and verified no Death scenario or evolution key blockers.
- Completion audit blockers above were patched in parent work.
- Static checks covered touched script brace balance, unsupported comparison operators, diff whitespace, localisation BOM preservation, stale old Death scenario-type strings, and workbook zip integrity.

## Remaining Risk

No known simplifications remain for this rework. The changes have not been live-loaded in Hearts of Iron IV.
