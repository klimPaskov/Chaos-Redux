# Entry 06 recrop v7 backdrop cleanup evidence

Entry 06 is the approved UmGra Champion source. The v7 corrective pass tightened the source-preserving crop to make the skull mask, face, shoulders, and chest readable in the 156x210 leader texture while retaining the approved identity.

The immutable source crop is 312x420 with SHA256 `f4ce6506eee50d5a29b397a7adf5307380f9c510f286c5a7822ccb19f527ed35`. The source crop remains an exact decoded-pixel rectangle from the archived original. Only the processed candidate receives bounded background treatment.

The cleanup keyed 31,229 border-connected near-neutral white pixels using a minimum channel value of 235 and a channel spread of 35 or less, replaced them with RGB `[0, 0, 0]`, applied a Gaussian alpha feather with radius `0.65`, composited onto neutral black, and resized the unchanged 26:35 crop to 156x210 with Pillow LANCZOS. No generative model, ImageGen, Meshy, Blender, repaint, redesign, or source replacement was used.

The processed PNG is `leader_CBD_warlord_north_america_156x210.png` with SHA256 `61f39495612b55b662990cb4a7350e3289db8e49e9e88e7ff7e7c4391b3f2dc6`. The corresponding runtime DDS was regenerated from this processed PNG with `convert_to_dds.py` and is recorded in the v7 runtime hash evidence.
