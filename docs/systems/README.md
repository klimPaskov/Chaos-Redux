# Shared systems documentation

This directory contains mechanics shared by multiple events or owned by the mod as a whole. Event-owned system contracts belong under `docs/events/<event_id>_<slug>/systems/`.

## Subsystem index

| Area | Ownership |
| --- | --- |
| [`3d_model_pipeline/`](3d_model_pipeline/README.md) | Shared 3D runtime contracts, model-package records, and unit sound handoffs. |
| [`air_cleanliness/`](air_cleanliness/README.md) | Air contamination, natural sources, winter, treaty behavior, and fallout-facing integration. |
| [`cbrn_warfare/`](cbrn_warfare/README.md) | Shared chemical, biological, condemnation, genocide, doctrine, and CBRN operations systems. |
| [`chaos_meter/`](chaos_meter/README.md) | Chaos accumulation, deaths accounting, war declarations, nuclear use, and the meter window contract. |
| [`chaosx_settings/`](chaosx_settings/README.md) | Settings controls, help, export, logging, miscellaneous options, and numeric input behavior. |
| [`event_system/`](event_system/README.md) | Random-event eligibility, weighting, clusters, crisis rescue, triggerable scenarios, Event Logs, evolutions, and world-end scenario catalog behavior. |
| [`comfyui_portrait_pipeline/`](comfyui_portrait_pipeline/README.md) | Sourced portrait placeholder and user-supplied final workflow. |

## Independent shared contracts

- [`custom_achievements.md`](custom_achievements.md) documents the root-only achievement registry and shared achievement conventions.
- [`hoi4_agent_tools_mcp_integration.md`](hoi4_agent_tools_mcp_integration.md) documents the repository's HOI4 agent-tools integration.
- [`liberation_release_coordinator.md`](liberation_release_coordinator.md) and [`startup_history_compatibility.md`](startup_history_compatibility.md) document shared country release and additive startup compatibility.
- [`main_menu_redesign.md`](main_menu_redesign.md) and [`state_map_modes.md`](state_map_modes.md) document shared interface contracts outside the settings and Event Logs subsystems.
- [`shared_autonomous_robot_system.md`](shared_autonomous_robot_system.md) documents the provider-neutral autonomous robot family shared by multiple events.
- [`world_threat_mechanic.md`](world_threat_mechanic.md) documents the cross-event world-threat aggregator and its source contract.

## Placement rules

- Put a document in the narrowest shared subsystem that owns its lifecycle and source files.
- Keep accepted design specifications in `docs/specs/` and working prompts, audits, handoffs, and migration notes in `docs/plans/`.
- Keep event-owned mechanics with the event even when their implementation spans several gameplay folders.
- Use each existing subsystem README as its navigation index. Keep the detailed mechanic contract in the named document rather than duplicating it in the index.
