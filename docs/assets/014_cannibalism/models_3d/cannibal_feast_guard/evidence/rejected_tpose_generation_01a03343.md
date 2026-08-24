# Rejected Meshy 7 T-pose generation `01a03343`

Status: remeshed and pre-remesh geometry both rejected before rigging.

- Task: `01a03343-a1a4-7c70-9fcd-daec6a513b35`.
- Input: immutable `refs/original/meshy_input.png`, SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`.
- Settings: exact `meshy-7`, standard, T-pose, PBR, triangle topology, 100,000 target polygons, provider remesh enabled, pre-remesh GLB preserved, 4K base texture, image enhancement and lighting removal enabled, bottom origin, GLB and FBX.
- Credits consumed: 30.
- Remeshed GLB SHA-256: `B5E6157F77A8D4B94D6A27E922998C86968589B777781787DBFAA865C6C87A6E`.
- FBX SHA-256: `A828F3521BED1006F20C96DDBF247AB757B5519D07AAB443ABCD87620CF564B2`.
- Pre-remesh GLB SHA-256: `974E3392EAC7472F5FDF38B9F88A18B72EFC9EAB603800421424C026DB76F6DF`.

The protected remeshed-source previews show a stable, broadly faithful T-pose body but no cleavers or other weapons. The preserved pre-remesh geometry was independently imported and inspected; its silhouette also contains no cleavers. The weapon loss therefore occurred during generation's pose transformation before the provider remesh stage. Neither geometry stage is eligible for rigging.

Evidence includes the `cannibal_feast_guard_tpose_recovery_raw_01a03343_*` remeshed previews, the `cannibal_feast_guard_tpose_recovery_pre_remesh_01a03343_*` previews, and their protected provider-source blends under `blender/source/`.

No rig or animation credits were spent on this rejected generation.
