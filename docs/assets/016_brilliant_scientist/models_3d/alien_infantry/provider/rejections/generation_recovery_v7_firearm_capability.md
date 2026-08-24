# Recovery V7 firearm-animation capability rejection

Status: **rejected at the mandatory firing gate; neutral geometry and rig retained as diagnostic evidence only**.

The exact approved Meshy input remained `refs/original/meshy_input.png`, SHA-256 `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`. Meshy received exactly that one image.

## V7 lineage

- Meshy 7 image-to-3D task `01a03499-135b-7a19-b5f3-eef4fc9d1515`, 30 credits. GLB SHA-256 `5CF528C917701DEC9634A268EF4B8E6754D11EEC13693B0562A756638CD81757`; FBX SHA-256 `50A626F366DE44D3C05364248E48556411A2410E9999AED47AE9C8F922580EA8`. Multi-angle review passed the generic alien identity, integrated rifle, readable muzzle, two-hand low-ready hold, grounded boots, and absence of forbidden insignia or extra weapons.
- Remesh task `01a0349e-d89f-76b4-baca-da8a190aafe5`, 5 credits. GLB SHA-256 `E0EF4D0A7DEC36A2879BAEA4C22E55DFDCED32A000BA168048930C907A396392`; FBX SHA-256 `442C395D7C9F67DEF73F9C65D817153B5EB4F4372E082B099B6867EA671B4465`.
- Rig task `01a034a4-700b-7a32-b9a8-ed95969a139a`, 5 credits. GLB SHA-256 `89ABD8EE5114AB5BA79DFF4C7B409202CE0037B168D18DA1EFC018FB267D212B`; FBX SHA-256 `484A267C779E704B84C0C0BF61494767B62580A9CAAC5FBC782B89C7677FB295`. Neutral 24-bone review passed geometry retention, but this did not validate animated weapon weighting.

## Mandatory firing tests

| Meshy action | Task | Credits | Artifact hashes | Full-phase evidence | Result |
|---|---|---:|---|---|---|
| 690 `Walk_Forward_While_Shooting_inplace` | `01a034a6-9666-79b9-8929-cc3598191272` | 3 | GLB `1FB70AF3A367838583817B3C5C724FF7541D9E9184F219C35BEFE891628116DE`; 24 FPS FBX `09DB46A597D3C4FC7FDDD07620412A0CEA7A5CD9838C8D90D9DEBAABA2B20E61` | frames 0/20/40/60/80 | Catastrophic upper-body and arm stretching, rifle loss, no stable muzzle or coherent two-hand hold. |
| 104 `Side_Shot` | `01a034ab-1c04-7c5a-ab0d-00687510cedf` | 3 | GLB `596E4D2AD09ABDC42CCA885967F6D5B28DD64DC49F783647800CE16048DAB4E8`; 24 FPS FBX `1D40AA025844AB73450481BE726EF3FA34C4FCC52D05EC48520EF8CFE2237124` | frames 0/16/32/48/64/80/97 | Stationary lateral-shot clip still smeared the arms, rifle, and torso together and destroyed trigger/support contact. |
| 232 `Cowboy_Quick_Draw_Shooting` | `01a034b5-7230-7789-831b-e2ad3faae058` | 3 | GLB `F05F1C685603AB0FE6B9EEA038C3DFE927159B27B87FD24D0B479FD19E540F3C`; 24 FPS FBX `F6DB5C2E8464523A5C58EA8F5E48880ACFEA7A2931889A3936CB242DDABE3DE6` | frames 0/22/44/66/88/110/132/154/176 | Draw/aim/fire/recover clip produced the same severe elastic deformation, unstable gun silhouette, and unusable muzzle. |

Actions 104 and 232 were selected from the official Meshy animation library because they are materially different from action 690 and from each other: 104 is a stationary side shot with reduced locomotion, while 232 is a long quick-draw, aim, fire, and recovery sequence. Neither had previously been tested on this lineage. Their failure rules out locomotion amplitude as the sole cause.

## Decision

The firing gate is failed. V3, V4, V5, V6, and V7 independent generations/rigs exhibit the same failure class, and V7 fails three materially distinct official firearm actions. Meshy cannot presently supply an acceptable armed-character firing clip for this integrated-rifle topology. No Blender weapon attachment, parenting, constraints, weight repair, weapon bone, manual motion, procedural motion, or semantic alias was attempted. The six remaining semantic actions were not purchased because the strongest mandatory firing role did not pass.

Live balance was 559 before action 104, 466 before action 232, and 433 after the audit; the account was being used concurrently. This audit itself consumed exactly 6 credits after the previously recorded V7 action 690. After this record, task hashes, reports, and the named frame evidence were preserved, the failed provider downloads and Blender sources/checkpoints were deleted through a path-verified package-local cleanup.
