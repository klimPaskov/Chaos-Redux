# Chaos Redux sourced portrait workflow

Keep the portrait workflow deliberately small.

## Required flow

1. Find an attributed source portrait for each grounded character.
2. Save the source under `docs/assets/portraits/<event_id>_<event_slug>/` using the runtime portrait basename.
3. Crop and convert the source to a `156x210` DDS and wire it as `source_placeholder` and `replacement_pending`.
4. The user alone creates the HOI4-style portrait externally. Agents never operate RunPod or generate the styled replacement.
5. When the user supplies the final portrait, validate identity, framing, dimensions, and provenance; convert it to DDS and replace the placeholder without changing the runtime path or wiring.

Do not create provider configuration, provider-selection skills, workflow locks, API instructions, or browser-operation instructions for Chaos Redux.

`chaosx_asset_source_researcher` owns source research and provenance. `chaosx_portrait_creator` validates and converts the user-supplied final. The parent owns character, `.gfx`, localisation, gameplay, and runtime wiring.

Non-sourced fictional or impossible portraits use parent-owned native ImageGen and do not use this workflow.
