# Chaos Redux sourced portrait workflow

For each sourced or grounded portrait:

1. Save the attributed source under `docs/assets/portraits/<event_id>_<event_slug>/` using the runtime portrait basename.
2. Crop and convert the source to a `156x210` DDS and wire it as the source placeholder.
3. Leave all ComfyUI and RunPod work to the user. Agents never operate RunPod.
4. When the user supplies the HOI4-style final, validate it, convert it to DDS, and replace the placeholder without changing its runtime path or wiring.

Keep the sourced portrait archive after replacement. Non-sourced fictional or impossible portraits use parent-owned native ImageGen.
