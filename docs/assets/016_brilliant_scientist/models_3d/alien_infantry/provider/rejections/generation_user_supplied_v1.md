# Rejected provider lineage: generation_user_supplied_v1

- Exact input SHA-256: `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`.
- Meshy 7 generation: `01a033ce-2052-7782-8c56-a3bb163fe4f1`, succeeded, 30 credits, GLB SHA-256 `8213328348BFA5F07EE0D38EC16063A79835DAE95B647F32417DCC65F8A4521E`, FBX SHA-256 `C1DA03CC7A79495EE970921F4DFF760E2E45E61CE1C748270A8603A955FED28B`.
- Meshy remesh: `01a033d8-2724-7127-8d6f-9794d65186e0`, succeeded, 5 credits, GLB SHA-256 `4ABF19833B3EC3BC6595470982F29FF368855D4FE3DD86D79B20BA05316F193F`, FBX SHA-256 `C577C7FB5B88FC4C2EAEECC6BFBDBACFF7590AB52A5884643C0582D0DB4E3DB1`.
- Meshy rig: `01a033e1-c9c3-799f-b824-3bf849429e19`, succeeded, 5 credits, GLB SHA-256 `40A9597CF58490CED3D737A9609892119C8F6F1BB1716F7CADC91BC12EC7AE12`, FBX SHA-256 `000D75BECE50DD5DE5D838E9B529BC7B84A7E95B8B6D0AC971EF8EEBF4C88E51`.
- Neutral rig gate passed after excluding only Meshy helper `Icosphere`; the supplied gun and both-hand low-ready contact were visually retained.
- Action 98 `Run_and_Shoot`: task `01a033f1-0c58-7ed4-a426-c7f66435b3fc`, succeeded, 3 credits, rejected at frame 0 for catastrophic fused-geometry arm/body stretching and loss of a usable gun silhouette.
- Action 690 `Walk_Forward_While_Shooting_inplace`: task `01a033fa-16c8-7a6c-b738-6b10f7b31e2b`, succeeded, 3 credits, rejected at frame 0 for the same catastrophic deformation.
- Verdict: entire generation/remesh/rig lineage rejected because distinct provider firing actions failed identically. No Blender-authored repair, weapon attachment, or replacement motion was attempted.
- Large provider models, Blender checkpoints, and rendered previews from this failed lineage were deleted before recovery generation; this note is the retained minimal evidence.
