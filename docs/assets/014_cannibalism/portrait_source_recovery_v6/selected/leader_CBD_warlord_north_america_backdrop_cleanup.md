# Entry 06 backdrop cleanup evidence

Entry 06 is the approved UmGra Champion source. Parent visual review accepted the crop and requested only removal of its stark white source backdrop so it matches the neutral dark treatment of the other fifteen portraits.

The immutable source crop remains unchanged at 468x630 with SHA256 463032afa339e0600a3fc3ba3a14a24833bf7aadd861bee0ae0313141f4e46b1. The cleanup used OpenCV connected components on border-connected near-neutral white pixels (minimum channel above 235 and channel spread below 35), replaced 114181 detected background pixels with RGB [0, 0, 0], applied a 3x3 Gaussian alpha feather only at the detected silhouette edge, and resized the unchanged 26:35 crop to 156x210 with Pillow LANCZOS.

This was bounded 2D compositing only. No generative model, ImageGen, Meshy, Blender, repaint, redesign, or source replacement was used. The character, skull/bone kit, paint, bloodied weapons, and silhouette remain the source-preserving identity input.

The refreshed processed PNG is leader_CBD_warlord_north_america_156x210.png with SHA256 c8fdd37f5ba7d7dcec9b8f72412870fcbcc8ed325eed5357ef430acc726cf692. The source crop JSON records the cleanup parameters and the co-located provenance contract records the operation. The corresponding runtime DDS was regenerated from this PNG using convert_to_dds.py.
