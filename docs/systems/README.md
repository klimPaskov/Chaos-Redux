# Shared systems documentation

This directory contains mechanics shared by multiple events or owned by the mod as a whole. Event-owned system contracts belong under `docs/events/<event_id>_<slug>/systems/`.

Major shared groups include:

- Air Cleanliness and Air Winter in [`air_cleanliness/`](air_cleanliness/)
- CBRN Warfare in [`cbrn_warfare/`](cbrn_warfare/)
- The 3D model pipeline in [`3d_model_pipeline/`](3d_model_pipeline/)
- Chaos Meter and deaths accounting in [`chaos_meter/`](chaos_meter/)
- Event Logs and evolutions in [`events_log_evolutions_and_clusters.md`](events_log_evolutions_and_clusters.md), event clusters in [`event_clusters.md`](event_clusters.md), and triggerable scenarios in [`triggerable_scenarios.md`](triggerable_scenarios.md)
- Shared country release in [`liberation_release_coordinator.md`](liberation_release_coordinator.md), startup compatibility in [`startup_history_compatibility.md`](startup_history_compatibility.md), and world-threat handling in [`world_threat_mechanic.md`](world_threat_mechanic.md)
- Shared settings in [`chaosx_settings/`](chaosx_settings/), map modes in [`state_map_modes.md`](state_map_modes.md), and achievements in [`custom_achievements.md`](custom_achievements.md)
- The ComfyUI portrait workflow in [`comfyui_portrait_pipeline/`](comfyui_portrait_pipeline/)

Do not place a mechanic here only because it is implemented across several gameplay files. If one event owns its lifecycle and documentation, keep it with that event.
