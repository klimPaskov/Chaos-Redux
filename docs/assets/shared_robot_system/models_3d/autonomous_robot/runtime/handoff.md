# Runtime staging handoff

The package is installed at the mod root. Staged evidence copies remain under `runtime/gfx/models/units/autonomous_robot/` for immutable hash comparison with the installed runtime files.

- Mesh identifier: `autonomous_robot_mesh`.
- Entity identifier: `autonomous_robot_entity`.
- Entity scale: `0.8`, applied exactly once.
- Source height: `7.3518247604`; effective runtime height: `5.8814598083`.
- Axes and origin: forward `-Y`, up `+Z`, feet at `Z=0`.
- Mesh: `autonomous_robot.mesh`.
- Actions: `autonomous_robot_{idle,move,attack,defend,support_attack,retreat,training,death}.anim`.
- Textures: `autonomous_robot_{diffuse,normal,specular}.dds`.

All mesh and animation exports were reimported through io_pdx_mesh. The death action received an allowlisted root-only per-frame grounding correction after its first reimport exposed late airborne contact; the final reimport remains within approximately `1.2e-5` of the ground plane.

No `.asset`, entity, GFX, sound definition, gameplay, or localisation wiring was edited. Live consumer validation remains parent/user-owned.
