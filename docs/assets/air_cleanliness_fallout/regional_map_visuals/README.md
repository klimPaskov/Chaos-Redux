# Air Winter Regional Ordinary-Map Visual Asset Package

Status: final asset production, engine registration, and synchronized five-slot gameplay lifecycle are implemented. The full-screen grade window and static accessibility setting remain unwired. Placement, layering, animation, cleanup, multiplayer behavior, and performance have not been observed in the running game.

This package supplies Fallout-owned ordinary-map art for all nine `air_winter_presentation_class` values and all six active Air Winter phases. It contains:

- 54 regional phase ground plates
- 27 regional prop plates for dead vegetation, frozen water, and thaw/flood
- 4 particle families with 16 separately authored source frames
- 9 particle severities registered as PDX particle entities
- 4 static particle fallbacks registered both as mesh entities and GUI sprites
- 8 atmospheric grade plates covering phases 1-6, soot thinning, and ultraviolet-clear recovery
- 85 custom PDX meshes with diffuse, specular, and true normal-map bindings
- 181 final DDS files

All source imagery is fictional, generated specifically for Air Winter, and stored under `source_png/`. No vanilla weather texture, zombie texture, or unrelated Chaos Redux asset is used in the final package.

## Review surfaces

- `contact_sheets/regional_ground_phase_matrix.png` shows every class across phases 1-6.
- `contact_sheets/regional_prop_matrix.png` shows dead vegetation, frozen water, and thaw/flood by class.
- `contact_sheets/particle_authored_frames.png` shows the 16 authored particle source states.
- `contact_sheets/particle_static_fallbacks.png` shows the non-animated alternatives.
- `contact_sheets/phase_and_recovery_grades.png` composites every grade on one shared map texture for meaningful comparison.
- `previews/normal_mapped_entity_material_proof.png` is an offline Blender material/geometry proof.
- `previews/*_authored_frames.gif` previews the authored particle frame order. These GIFs are review artifacts, not runtime files.

## Source of truth

- `manifest.md` records ownership, paths, counts, identifiers, conversion provenance, and the evidence boundary.
- `handoff.md` gives the exact class/phase/entity matrix and integration contract.
- `frame_brief.md` and `frame_plan.md` record the animation design and source-frame proof.
- `prompts/regional_visual_generation_prompts.md` records the image-generation briefs.
- `build_report.json` records source SHA-256 values and final DDS dimensions.
- `mesh_export_report.json` records mesh hashes, shaders, material bindings, and geometry counts.

## Rebuild boundary

`_tooling/process_regional_visuals.py` deterministically extracts the generated source plates, derives material channels, builds contact sheets and GIF previews, and converts final textures. It deliberately requires an explicit `TEXCONV_PATH`. It does not permit the repository converter to choose an unapproved secondary converter.

`_tooling/build_regional_meshes.py` runs through Blender 5.1 with the installed PDX mesh exporter. It exports the engine meshes, text-form mesh proofs, the `.blend` source, the mesh report, and the offline render.

The package should not be rebuilt casually: generated source plates are the approved visual inputs, and a rebuild changes binary mesh hashes even when the visible design is unchanged.
