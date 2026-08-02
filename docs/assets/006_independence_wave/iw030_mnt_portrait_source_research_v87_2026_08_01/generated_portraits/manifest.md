# IW-030 Mitar Martinovic portrait asset manifest

Status: `needs_user_review_v7`.

| Asset | Path | Dimensions | SHA-256 | Role |
| --- | --- | ---: | --- | --- |
| Source-locked HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw.png` | 1098x1432 | `8d69a2d39f99cd0d69a7dfddc4da1943af1b176a0eab07e06dc132c7797619d7` | Raw ImageGen result; evidence only until independent audit. |
| Native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210.png` | 156x210 | `57c6f654d1f8bb6aa4e8407bb256f7529d645d4ffb9e0d87c9efc047b95c65d8` | Deterministic candidate; no DDS conversion before audit PASS. |
| Processing record | `portrait_MNT_mitar_martinovic_processing.json` | — | — | Center crop `[17, 0, 1081, 1432]`, then Pillow LANCZOS to 156x210; no padding or recolour. |

The immutable archival source, exact crop, crop equality JSON, source URLs, and role research remain in the parent v87 source-research workspace. The durable ComfyUI pair is `docs/assets/portraits/006_independence_wave/portrait_MNT_mitar_martinovic.png` and `portrait_MNT_mitar_martinovic.txt`; it is not a runtime path.

No advisor, high-command, operative, dossier, small portrait, or generated replacement for another historical person is included.

## Revision candidates

| Asset | Path | Dimensions | SHA-256 | Role |
| --- | --- | ---: | --- | --- |
| v2 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v2.png` | 1115x1410 | `c58c3f0a2a43d86b24a0c9700aaa8ec60c699428505f032fdbf5d7030e3aa111` | Evidence-only repaint. Independent audit HOLD. |
| v2 native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v2.png` | 156x210 | `ffbb69d1998f154a84f230b595b6dbdfecc1e037c0d7fb794feb9cd3a6f972e8` | Deterministic evidence candidate. No DDS conversion. |
| v3 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v3.png` | 1114x1411 | `2d1edd076b3b57e7debbe2225d134cb036786405b962272d16d8fee9fc3eda1c` | Evidence-only repaint. Independent audit HOLD. |
| v3 invalid native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v3.png` | 1058x1411 | `f842d2f9abc10be1bfa7b9730283c0c2db30b447ff0732f9e217ed3169ea3d27` | Processing defect recorded by audit. Not a native asset. |
| v4 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v4.png` | 1115x1410 | `aadd994e42f2592f7a4479b0af66c9743ad7258c48f1b3d61da0f656166bd842` | Evidence-only repaint. Independent audit HOLD. |
| v4 native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v4.png` | 156x210 | `18810f98092b9b0a88fa93da69d31383151280cb2261ebb7e6c3eea11c36c9f2` | Deterministic evidence candidate. No DDS conversion. |
| v5 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v5.png` | 1114x1412 | `4ff2aba90318de05fe3ec00be7bfb6ee272663e2c2bce83b2ddfc335b2c407d3` | Final constrained attempt pending independent audit. |
| v5 native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v5.png` | 156x210 | `7f4186eb160ffbb9e44c3e297ea6b28d6470ff7c5c27ce50d2302ffe5a18ecf4` | Deterministic candidate pending independent audit. No DDS conversion. |
| v6 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v6.png` | 1114x1412 | `b9f1c5e0e28f0a1e12ebce80b14b935cfe31c32232a784c249bfe15c3073b80a` | New identity-preserving ImageGen repaint; evidence-only pending independent audit. |
| v6 native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v6.png` | 156x210 | `4165007d39d70f45780e3615e5e000ea2d12296141d8d79710fcaedf59e9fac7` | Deterministic 156x210 candidate; no DDS conversion before independent audit PASS. |
| v6 processing record | `portrait_MNT_mitar_martinovic_processing_v6.json` | — | — | Center crop `[27,0,1086,1412]`, then Pillow LANCZOS to 156x210; no padding or recolour. |
| v7 HOI4 repaint | `portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v7.png` | 1080x1456 | `d30891ac10f58dd080b2eeb85081efec9314d6e7e849ab91f8d01f9c05733b6d` | Style-only light-background refinement of v6; evidence-only pending independent audit. |
| v7 native candidate | `portrait_MNT_mitar_martinovic_hoi4_156x210_v7.png` | 156x210 | `6b14b6cb8ef48b9c2b256bc331026448450e6dfbd409f4a9d19da6a8c6254501` | Deterministic full-width 156x210 candidate; no padding, DDS, or runtime wiring. |
| v7 processing record | `portrait_MNT_mitar_martinovic_processing_v7.json` | — | — | Full-width crop `[0,0,1080,1456]` because the ImageGen canvas was already narrower than the 3:4 crop; Pillow LANCZOS to 156x210. |
