# Event 016 Event 019 portal and temporal provider extension

> **Superseded provider-inventory notice (2026-08-09):** This handoff closes the historical portal and temporal extension to providers `504-510`. Provider 522 and the expanded owner-adapter census were added later; use `016_core_runtime_handoff_map.md`, `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`, and `.tmp/event19_docs_curator_current.md` for current provider facts.

## Scope

This tranche closes the missing shared-infantry-spawn coverage for the two Event 016 project-force families that were still native-only: Portal Raider and Temporal Guard. It does not create models, entities, animations, or a presentation fallback.

## Runtime changes

- `common/script_constants/016_brilliant_scientist_project_force_constants.txt` adds provider kinds `portal = 6` and `temporal = 7`, plus family/provider rows 509 and 510 with centralized derivative, sustainment, containment, AI, neutral-visual, cleanup, isolation, spawn-weight, template, manpower, training, and sustainment values.
- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt` adds active-package and exact-history gates for `brilliant_scientist_event19_portal_provider_unlocked` and `brilliant_scientist_event19_temporal_provider_unlocked`, with derivative identity checks.
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` registers providers 509/510 when the matching Event 016 project is active and supplies callback parity for eligibility, locked templates, native battalion spawning, manpower obligations, management affordability, payment, refund, sustainment, derivative setup, public-package receipts, removal, and cleanup.
- `common/ideas/016_brilliant_scientist_project_force_ideas.txt` adds hidden, cleanup-auditable host receipts for the two provider families.
- `localisation/english/019_infrantry_spawn_l_english.yml` localizes both hidden receipt ideas.

Portal provider 509 consumes `kruger_portal_raider` and `kruger_portal_equipment_1`. Temporal provider 510 consumes `kruger_temporal_guard` and `kruger_temporal_equipment_1`. Both use the existing Event 019 generic provider dispatch and do not restore the Event 016 parent identity.

## Documentation changes

`docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md` now records that all seven families are exposed through providers 504-510 while keeping all seven bespoke 3D packages deferred. `016_core_runtime_handoff_map.md` records the new provider count and the same live-validation boundary.

## Validation evidence

- Provider IDs 509 and 510 are above the registry minimum and do not collide with the existing 501-508 rows.
- Each provider has registration, eligibility, template, spawn, sustainment, management-evaluation, payment, refund, derivative-setup, public-removal, and cleanup callback identifiers.
- The portal and temporal native battalion and equipment tokens resolve in the existing Event 016 units/equipment/technology sources.
- The two provider unlock triggers require current Event 016 runtime state and exact deployment history, and derivative branches require matching family/provider IDs.
- No HOI4 runtime was launched. Event 019 derivative, affordability, defeat, and final-cleanup scenarios remain user-owned validation.
- A focused read-only Event Inspector lint for `chaosx.nr19.918` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, but workspace-wide helper/lifecycle validation was deferred by the analyzer; this is evidence of inspection, not a clean whole-workspace pass.

## Remaining risks

The generic Event 019 provider analyzer and live game still need to exercise provider 509/510 through Anomalous Rising, management, transfer/derivative isolation, defeat, and final cleanup. No model or entity wiring was added; the seven-family 3D backlog remains deferred by the current instruction.
