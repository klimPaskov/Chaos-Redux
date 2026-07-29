# Event 016 project-icon prompt and provenance

This package uses the official built-in image-generation workflow required by the imagegen skill.

Source mode is generated symbolic fictional art because the Brilliant Scientist project families and their project-board symbols are fictional.

Each decision family was generated as a four-quadrant atlas with four distinct compositions for Theory, Prototype, Deployment, and Weaponization or Autonomy on a flat `#00ff00` chroma-key background.

Each special-project tranche was generated as a four-quadrant wide atlas with separately composed project illustrations and was processed independently from the decision atlases.

The atlas prompts required HOI4 1930s-1940s period-science visual language, worn steel and brass, muted teal, restrained amber or cyan highlights, generous padding, no readable text, no flags, no modern digital electronics, no atom-only motif, and no watermark.

The biological-weapons prompt was framed as hazardous biological defense research with sealed containment, quarantine, and fail-safe hardware so the generated art does not depict harm or gore while preserving the requested project-family identity.

The generated source atlases are retained under `source_atlas/` and `source_special_atlas/`. Individual raw quadrant crops are retained under their `crops/` subfolders as the source PNG for every runtime asset.

The local chroma-key processor was `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`.

Processed quadrant art was alpha-fitted to 32x32 decision icons or the verified 161x98 special-project footprint without reusing a decision icon for a special-project surface.

The special-project footprint was verified from the installed vanilla project icon files, including `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/special_project/project_icons/sp_air_axial_jet_engine.dds`, which declares 161x98 and a 63240-byte legacy BGRA DDS.

Reference contact sheets inspected before generation were the canonical decision, special-project, and technology sheets under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/`.

The generated-image source IDs are retained in the source-atlas file metadata and in the tool outputs for this production run. The selected source atlases are `computational_mathematics_atlas.png`, `electronics_guidance_atlas.png`, `advanced_materials_atlas.png`, `rocketry_propulsion_atlas.png`, `high_energy_physics_atlas.png`, `biomedical_acceleration_atlas.png`, `teleportation_atlas.png`, `cloning_atlas.png`, `robotics_ai_atlas.png`, `paleogenetics_atlas.png`, `xenobiological_synthesis_atlas.png`, `biological_weapons_atlas.png`, `alien_arms_atlas.png`, `temporal_mechanics_atlas.png`, `strategic_singularity_atlas.png`, and four `special_projects_*_atlas.png` files.

No sourced real-world material, real-person likeness, readable text, flag, or fallback placeholder is used in this package.
