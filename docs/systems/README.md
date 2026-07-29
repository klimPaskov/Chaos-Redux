# Shared systems documentation

This directory contains mechanics shared by multiple events or owned by the mod as a whole. Event-owned system contracts belong under `docs/events/<event_id>_<slug>/systems/`.

Major shared groups include:

- Air Cleanliness and Air Winter in [`air_cleanliness/`](air_cleanliness/)
- CBRN Warfare in [`cbrn_warfare/`](cbrn_warfare/)
- The 3D model pipeline in [`3d_model_pipeline/`](3d_model_pipeline/)
- Chaos Meter and deaths accounting
- Event Logs, event clusters, and triggerable scenarios
- Shared country release, unit-family, world-threat, and startup compatibility systems
- Shared UI, settings, map-mode, and achievement infrastructure

Do not place a mechanic here only because it is implemented across several gameplay files. If one event owns its lifecycle and documentation, keep it with that event.

