# Vanilla cavalry entity architecture

The installed vanilla precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_cavalry.asset`.

An exact archival copy is `evidence/vanilla/units_cavalry.asset`, 145,005 bytes, SHA-256 `5AC30F2E98F29A95A56675AE19E51C3C4FAD7B2F1B6453F6AA0C7D6415696AE6`.

Relevant installed lines:

- Lines 41-63 define `infantry_rider_entity` with its own infantry mesh, mounted idle/move/combat/training actions, weapon attachments, and rider scale `0.8`.
- Lines 92-110 define the outer `cavalry_entity` frame, its state surface, and its separate `infantry`, `cavalry`, and `horse` attachments.
- Lines 112-126 define `generic_cavalry_rifle_combined_entity` on the horse mesh and attach `infantry_rider_entity` at the horse mesh node `Saddle_Node`; the combined horse entity scale is `0.65`.
- Lines 128-163 repeat the architecture for the cavalry MG variant and again attach a distinct rider entity at `Saddle_Node`.
- The frame propagates runtime state into its attached children, while the horse and rider remain separate meshes and animation consumers.

## Bone Riders implementation consequence

The Bone Riders package should use three parent-owned runtime entities rather than merge horse and rider actions into one armature:

1. A custom frame entity that exposes all eight runtime roles and propagates each state to the attached horse and rider children.
2. A bespoke living bone-barded horse entity with the retargeted CC0 Mesh2Motion horse actions.
3. A bespoke painted skull-masked sling rider entity attached at an audited `Saddle_Node`, with eight distinct Meshy rider actions.

The horse mesh must contain a measured `Saddle_Node` whose local position and orientation reproduce the accepted mounted geometry exactly.
The rider entity scale and saddle attachment transform must be audited once and applied once; neither may compensate for a mismatched mesh calibration.

Attack and support-attack must preserve the loaded sling and pouch and display two distinct sling-stone volleys.
Death must keep horse collapse, rider collapse, frame state propagation, and any saddle detach/settle behavior synchronized without merging or aliasing actions.

Runtime `.asset`/entity wiring remains parent-owned and is not implemented in this model package.
