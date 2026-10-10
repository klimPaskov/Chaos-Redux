# Unit visual references

Read this reference for any unit visual: equipment and technology art, land, air, and naval counters, division-template emblems, and 3D model packages. The 2D icon and counter generation contract remains in the icon and UI families reference.

## Asset-family contracts

### Unit visual references

Treat every unit visual as a domain-and-surface-specific pipeline. Inspect the matching catalog entries, contact sheet, and owning vanilla definition before deciding what the task needs.

- `units/equipment/technology_art/` contains flat 2D equipment illustrations used by equipment and technology sprites. Native canvases vary; follow the owning `interface/*.gfx` sprite.
- `units/land/counters_large/` contains large frame-aware land-unit strips. Preserve the cataloged `noOfFrames`, frame order, per-frame footprint, and transparent bounds.
- `units/land/map_counters/` contains land map-counter art. It is not a large division-designer strip.
- `units/land/division_template_emblems/` contains division-template identity emblems. It is not equipment art or map-counter art.
- `units/air/map_counters/` and `units/naval/map_counters/` contain domain-specific map-counter art. Do not substitute land counters or resized equipment art.
- `units/models_3d/land_materials/`, `units/models_3d/air_materials/`, and `units/models_3d/naval_materials/` contain UV model materials paired with cataloged `.mesh`, `.asset`, and entity definitions. They are not 2D icons, finished renders, or concept sheets.

Classify the requested deliverable before creating art: equipment/technology illustration, large land counter, land/air/naval map counter, division-template emblem, or land/air/naval 3D model package. Give each class its own brief, source art, native canvas or UV layout, frame metadata, final path, and handoff. A 3D task must keep model geometry, materials, entity wiring, and any separately produced concept reference distinct. Do not derive one unit pipeline by resizing, relabeling, or recoloring another.

#### 3D model package handoff

Route model production to [chaos-redux-3d-model-pipeline](../../chaos-redux-3d-model-pipeline/SKILL.md) and `chaosx_3d_model_pipeline`; read its route selection, intake, and evidence/handoff requirements before briefing or accepting a model package. The 3D skill owns provider/dependency gates, source-image preparation, separate body/item generation, supported rig/action attempts, Blender assembly/fallback, geometry, materials, weights, contacts, and export/reimport. Do not duplicate those procedures in a 2D art brief.

The brief and returned package must identify the profile, requested operation, deterministic job root, source/provider lineage, exact vanilla mesh/entity precedent, source height, entity scale and effective runtime height, axes/origin/contact plane, required actions and root-motion policy, PDX channels and dimensions, `.mesh`/`.anim` outputs, reimport evidence, and exact runtime consumer. For humanoids, use measured installed vanilla infantry geometry and apply entity scale once, never an assumed real-world height. Require all components and real articulated motion; unavailable production capabilities prevent the affected output, while unavailable review tools limit the claims made about it.

For every firing state, require the action → discharge frame/time → verified muzzle/weapon locator → particle/beam/muzzle effect and applicable light → licensed weapon-matched soundeffect → source/license → entity consumer → evidence crosswalk. Attack, defend, support_attack, and other firing states are independent consumers. Silent or particleless firing and unrelated weapon-family substitutes are incomplete. A declared non-firing armed action receives no firing effects merely because it carries a weapon.

Model textures follow the 3D skill's shared `.tools/3d_pipeline/textures/` BC1/BC3 full-mip contract, active `.gfx` overrides, and hash-bound UV/material masks, not the uncompressed 2D DDS recipe in [DDS conversion](../SKILL.md#dds-conversion). Unit audio uses `.tools/3d_pipeline/audio/master.py` with source/derivative attribution and hashes. Decoded bytes or a geometry-only reimport do not establish rendered materials, deformation, audio playback, or live-game behavior.

The 3D worker owns sources, checkpoints, textures, previews, exports, manifests, model/audio evidence, and the mandatory bounded counter handoff to `chaosx_icon_artist`; this asset skill owns final counter art. Equipment illustrations, division emblems, and frame sheets remain separate surfaces. The parent owns final `.asset`, entity, `.gfx`, particles, sound definitions, unit/building/gameplay wiring, selected-source runtime synchronization, and final evidence review. The user performs live-game validation; do not request or await it to finish the package.
