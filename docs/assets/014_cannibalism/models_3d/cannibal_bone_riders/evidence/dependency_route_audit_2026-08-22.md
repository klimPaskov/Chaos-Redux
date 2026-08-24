# Bone Riders dependency-route audit, 2026-08-22

Status: route verified; production blocked by source selection, not adapter capability.

The MESHY_API_KEY gate passed before repository/job intake; no secret value was recorded. No Meshy route was invoked.

- dependency lock SHA-256: `39BEC68E5B356D6BB0BD0B7463C9FF761F8572E0453405DB929AAAC4292289F2`
- Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`
- adapter config SHA-256: `C8CF20F9C177D32AB0593BF9CA128BB369E9E24640BB436E310EE42EB9698F29`
- Meshy MCP `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK `1.29.0`, exact model `meshy-7`
- Blender `5.1.2`, build `ec6e62d40fa9`
- adapter `chaosx_blender_hoi4` `1.8.1`
- io_pdx_mesh `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`
- bridge `127.0.0.1:9876` listening
- health request `e283a4d0a4b24a98a87171854bdf4301` passed

The repository wrapper/client exposed 25 tools, including all lock-required creature operations. The earlier 1.8.0/callable-declaration mismatch is superseded. Vanilla horse/frame adapter measurements passed and are recorded in the measurement reports.

Provider task IDs and response IDs: none. Credits consumed: 0. Future Meshy activity requires both an eligible sourced artwork input and an explicit serialized parent lease naming the exact task/cost.
