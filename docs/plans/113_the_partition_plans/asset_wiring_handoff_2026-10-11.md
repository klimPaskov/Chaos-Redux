# Event 113 decision icon delivery

The 15 accepted 32×32 decision icons are installed in the event-scoped interface folder and registered in the existing `interface/chaosx_decisions.gfx` owner.
The explicit current asset request authorized this delivery. The spec labels T/C/P are planning roles rather than live decision IDs; no game consumer was added or invented, so actual action-to-sprite consumption remains pending the Event 113 gameplay implementation.

The independent reviewer accepted D1 after inspecting the generated source, native-scale art, alpha edges and DDS round-trip against the canonical decision family. D2–D15 passed automatic dimensions, transparency, strict one-level BGRA header and decoded-pixel equality checks.
The producer retained exact prompts, source PNGs, processed PNGs, DDS candidates, hashes and the contact sheet under `docs/assets/113_the_partition/shard4_decision_icons/`; the independent review record is `.tmp/assets_shard_4_20261011/reviewer/113_decision_review.json`.

| Requirement | Sprite | Runtime DDS | Source SHA-256 | DDS SHA-256 |
| --- | --- | --- | --- | --- |
| D1 | `GFX_decision_113_partition_counteroffer` | `gfx/interface/decisions/113_the_partition/decision_113_partition_counteroffer.dds` | `2e38413dd2b51e2b5f5f3f79e97d4b82e716db0c5acbbc121576f40ddef49ed5` | `a725de9b035f8db2e071e7f696f449886b29cddd30b651019ebb948e582fadd1` |
| D2 | `GFX_decision_113_partition_protection` | `gfx/interface/decisions/113_the_partition/decision_113_partition_protection.dds` | `a498dfc82c09c81593b09c53fd6c7854fed208e8822e3473f39df726cb7561a4` | `d029e116f31e6730e3cae1407e99d1420b93c5309111db8ba3faf9904d9079e6` |
| D3 | `GFX_decision_113_partition_entrench` | `gfx/interface/decisions/113_the_partition/decision_113_partition_entrench.dds` | `697e8a41ed4adf8979323fdfa781a512a6548ecdee2264f726521c87a1c6838e` | `24f67af7bb16de77dfc2d6b5f3eeeee2b20261f7fda291010a2db9bd2bf956a3` |
| D4 | `GFX_decision_113_partition_transport` | `gfx/interface/decisions/113_the_partition/decision_113_partition_transport.dds` | `4d0b8f16a0aaffa571d39fb9be2d52e1b005efcd59f2f70834bf8e5ba1bed296` | `4dc50d459818026c6f7dd037939c3b5fcb6a2e6896a1756db71dcfda3238b932` |
| D5 | `GFX_decision_113_partition_ratify` | `gfx/interface/decisions/113_the_partition/decision_113_partition_ratify.dds` | `4abb9fe9010173bf2e2c4a51694a2e7b1467b51ff7a28c9e227aab7e40861491` | `6efb8c6ae30c7ca6d3de0a7b468f0b64d78e5496d757f7ab8204c9b231561312` |
| D6 | `GFX_decision_113_partition_refuse` | `gfx/interface/decisions/113_the_partition/decision_113_partition_refuse.dds` | `54ba648df3503c931121cc583e43370635588bbcc2241b65e3bb492122f2ee75` | `290c16ac751cf0e211722be724d49f5081e30294bf4207c9474fd1aff9b01b6b` |
| D7 | `GFX_decision_113_partition_withdraw` | `gfx/interface/decisions/113_the_partition/decision_113_partition_withdraw.dds` | `310398bf26992f7357a68bd5a16cd7120e7a54d8c3213bb64e84b0cfc4dcf9b9` | `8ab96986db49c28e7896f8773082ea8b67ac5437a2bc3702191fa6dcfa7a5f38` |
| D8 | `GFX_decision_113_partition_invite` | `gfx/interface/decisions/113_the_partition/decision_113_partition_invite.dds` | `5a679665d71ce494e53f1dfcefba3d3e45743973453d24d6476d7e40c90ae7d2` | `8fce8e0361694910804d4ef6b9f16e77b52f343dedef66bfc9794e3dcb62b3fd` |
| D9 | `GFX_decision_113_partition_enforce` | `gfx/interface/decisions/113_the_partition/decision_113_partition_enforce.dds` | `b99680fa6385afd08444fb4217b9fad36acb9c52ce77119277785bdd280cc7ba` | `4cd2c096cc6936586de4a571763d9ba68b42100bcf87b13823a202d1d62b5da8` |
| D10 | `GFX_decision_113_partition_dispute` | `gfx/interface/decisions/113_the_partition/decision_113_partition_dispute.dds` | `f7b6c7bb7305276c4e96223b9badc4360a92911e0673fd5a5241407f83ac1538` | `6023d033da77b4ab7ac72486805e94ba0871cb8a4f5623ed8bccbcb412e0a8e0` |
| D11 | `GFX_decision_113_partition_arms` | `gfx/interface/decisions/113_the_partition/decision_113_partition_arms.dds` | `bbdd5168df4dd9674807d37092dfcf15d7c2862c9878ca15c3f141502ba43902` | `e9c634c0b2df65cadd4ae1e24c1f29b3129df12b8fac3c41209fc57e408bd05c` |
| D12 | `GFX_decision_113_partition_mediate` | `gfx/interface/decisions/113_the_partition/decision_113_partition_mediate.dds` | `df0de81b38cd60e83d6c09c411172b66f057cb6f9c152b81682f49f910ba0de4` | `78f69aba52c330632b09c62a85879d1862fbe4d7d7b61069e8008ec6e3f643e9` |
| D13 | `GFX_decision_113_partition_intervene` | `gfx/interface/decisions/113_the_partition/decision_113_partition_intervene.dds` | `c3628ad81deec2231538075e619a54459f0254681292a8bf97b5941a1102c702` | `bb73ac43a141041fd8f5a36d1da4af0fa681818a38108ebd75cf6542babd1555` |
| D14 | `GFX_decision_113_partition_rebuild` | `gfx/interface/decisions/113_the_partition/decision_113_partition_rebuild.dds` | `39332ffd7e6703d4865b1c0b07e4af178d9d1cde8bb288be6d3f0aa21520e92f` | `840d56ee347f26121ad5628eaf00a9c1a43fa80ec318d427a0bd1cdd5c06d791` |
| D15 | `GFX_decision_113_partition_reconcile` | `gfx/interface/decisions/113_the_partition/decision_113_partition_reconcile.dds` | `78b1bd84f09608251d8fb6e3c0499ab951a834399511395583922a1101a7f23f` | `774fa95a275b4009d9f949c146d7aa76ed9a394a5118eb6ec2e63cb93eaca533` |

The decision sprite format was checked against the offline Graphical asset modding wiki’s `spriteType` section (lines 28–81) and installed `interface/decisions.gfx` (lines 1–36). The HOI4 MCP reference routes were unavailable; this source check does not claim a live-game render or consumer test.
No existing art, gameplay definitions or localisation were overwritten.
