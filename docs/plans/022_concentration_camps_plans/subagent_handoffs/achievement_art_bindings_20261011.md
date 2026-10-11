# Event 022 achievement art bindings

Disposition: implemented within the user request to wire all named asset requirements.

Seven currently registered achievement IDs resolve their completed, grey and ineligible icons through exact root-level DDS filenames.
All 21 destinations were absent before promotion, and the accepted generated triplets were copied byte-for-byte without replacing any existing artwork.

The requirement and consumer IDs are in `common/achievements/chaos_redux_achievements.txt`, beginning at line 4816 at the reviewed source revision.
The owning achievement-file SHA-256 is 2500535f762f968a0e4b81acc5050b25cd263373e3f508e837779e0b92c89c09.
The engine lookup uses `gfx/achievements/<achievement_id>{,_grey,_not_eligible}.dds`, as documented by the asset skill and the existing `interface/chaosx_achievements.gfx` header.
No extra sprite alias or gameplay/text changes are needed for that lookup.

The independent reviewer sampled the close-every-gate subject and native state triplet.
All 33 existing candidate state files passed strict DDS, original-receipt hash, deterministic grey/cross and template-source pixel equality checks.
Only 21 files for the seven implemented IDs were promoted, and every promoted hash was compared against its source.
This is source and pixel evidence, without a live engine claim.

Source receipt: `docs/assets/022_concentration_camps/icon_run_2026-10-10/evidence/achievement_triplets.json`.
Independent sample review: `docs/assets/shard_5_review_20261011/current_review.json`, batch `batch022_achievements`.
The producer and independent reviewer are separate workers.

| Current achievement ID | Accepted source DDS | Runtime lookup DDS | SHA-256 |
|---|---|---|---|
| chaos_redux_022_close_every_gate | gfx/achievements/chaosx_achievement_022_close_every_gate.dds | gfx/achievements/chaos_redux_022_close_every_gate.dds | e8f4861daba6a4837f5cf83c9d087dd4a52f8116af91b2914acbca22d0b076a7 |
| chaos_redux_022_close_every_gate | gfx/achievements/chaosx_achievement_022_close_every_gate_grey.dds | gfx/achievements/chaos_redux_022_close_every_gate_grey.dds | 5af28d3abbb318d8b38c4016356a70e1b5f0ed8102d53da0903d347601b11394 |
| chaos_redux_022_close_every_gate | gfx/achievements/chaosx_achievement_022_close_every_gate_not_eligible.dds | gfx/achievements/chaos_redux_022_close_every_gate_not_eligible.dds | 18df603e07c7a7d133aa27371db8a3fe789342810d47db23e6fc1d90ec2a71cc |
| chaos_redux_022_the_machine_stopped | gfx/achievements/chaosx_achievement_022_machine_stopped.dds | gfx/achievements/chaos_redux_022_the_machine_stopped.dds | a02bbacd8268c10ef9a1ef0c282414d01f70843268ab216fd842c07a9648688e |
| chaos_redux_022_the_machine_stopped | gfx/achievements/chaosx_achievement_022_machine_stopped_grey.dds | gfx/achievements/chaos_redux_022_the_machine_stopped_grey.dds | 68ddd0611f53cda74cd8a82feb7b9f1bd5e78891b9696e0ac0fa7bd6c3314d98 |
| chaos_redux_022_the_machine_stopped | gfx/achievements/chaosx_achievement_022_machine_stopped_not_eligible.dds | gfx/achievements/chaos_redux_022_the_machine_stopped_not_eligible.dds | f48934610ba41f2d672df11c6c4d598e0016c7d56b4fa402ead36db0c1981784 |
| chaos_redux_022_the_evidence_survives | gfx/achievements/chaosx_achievement_022_evidence_survives.dds | gfx/achievements/chaos_redux_022_the_evidence_survives.dds | bf93c8f069e361035de27262523756b950a13272957d47d2b5dcb05cdfe10ab8 |
| chaos_redux_022_the_evidence_survives | gfx/achievements/chaosx_achievement_022_evidence_survives_grey.dds | gfx/achievements/chaos_redux_022_the_evidence_survives_grey.dds | 0b79b4160d0be776572ead8275c6e7c79a87bed99b64c831be4dd01380ff7d42 |
| chaos_redux_022_the_evidence_survives | gfx/achievements/chaosx_achievement_022_evidence_survives_not_eligible.dds | gfx/achievements/chaos_redux_022_the_evidence_survives_not_eligible.dds | 7bbf56084b667cbabbea6a823dd5c5fb6bcd237e56708c1634d17f5280970136 |
| chaos_redux_022_no_one_disappears_twice | gfx/achievements/chaosx_achievement_022_no_one_disappears_twice.dds | gfx/achievements/chaos_redux_022_no_one_disappears_twice.dds | 981c59a7587651e3b8c51d826dcc35a04d1c77c5231241bc55db7ae74491c39a |
| chaos_redux_022_no_one_disappears_twice | gfx/achievements/chaosx_achievement_022_no_one_disappears_twice_grey.dds | gfx/achievements/chaos_redux_022_no_one_disappears_twice_grey.dds | 9d30db2cd3842ab225f35e5086717c97802a05d9d7b78b5b21849a5e36a3cf6c |
| chaos_redux_022_no_one_disappears_twice | gfx/achievements/chaosx_achievement_022_no_one_disappears_twice_not_eligible.dds | gfx/achievements/chaos_redux_022_no_one_disappears_twice_not_eligible.dds | 30ec7a8a9afe78318d6d6bf0c448cdea00fcf92e8aee5383bb615c5ac5a81978 |
| chaos_redux_022_a_government_answers | gfx/achievements/chaosx_achievement_022_government_answers.dds | gfx/achievements/chaos_redux_022_a_government_answers.dds | 442a91932d7d1991d48931c432cbca9f881fbffdf058881cdcf6b69347fd1d95 |
| chaos_redux_022_a_government_answers | gfx/achievements/chaosx_achievement_022_government_answers_grey.dds | gfx/achievements/chaos_redux_022_a_government_answers_grey.dds | 3d9e5fde27200cdf61c54d27c523bab00c5d54eecc43b03332912b4748754823 |
| chaos_redux_022_a_government_answers | gfx/achievements/chaosx_achievement_022_government_answers_not_eligible.dds | gfx/achievements/chaos_redux_022_a_government_answers_not_eligible.dds | 9e88e4fd1e283d1ef22373846f33630730bc7b38c780ab5e56fc2b5c2a4b827d |
| chaos_redux_022_safe_harbor | gfx/achievements/chaosx_achievement_022_safe_harbor.dds | gfx/achievements/chaos_redux_022_safe_harbor.dds | 3ece08d590529ad84376603ae917157ef6c72621f88ddde322a47fc3400e949a |
| chaos_redux_022_safe_harbor | gfx/achievements/chaosx_achievement_022_safe_harbor_grey.dds | gfx/achievements/chaos_redux_022_safe_harbor_grey.dds | 8494c944975b2cc049aaf69eac2554018ae3201e0836eb2a8424d2e316ea8f88 |
| chaos_redux_022_safe_harbor | gfx/achievements/chaosx_achievement_022_safe_harbor_not_eligible.dds | gfx/achievements/chaos_redux_022_safe_harbor_not_eligible.dds | a09e39ca901d0a0bdbd3310bf04200a71ca913c9efb27f25c40f987c662c1381 |
| chaos_redux_022_against_the_order | gfx/achievements/chaosx_achievement_022_against_the_order.dds | gfx/achievements/chaos_redux_022_against_the_order.dds | 029cc47687ce371a7a5d5c75df491978b87e3cb0e100a5a731d6167e72f92d1a |
| chaos_redux_022_against_the_order | gfx/achievements/chaosx_achievement_022_against_the_order_grey.dds | gfx/achievements/chaos_redux_022_against_the_order_grey.dds | 07ce8839ae19c226f59ed89586e26eebf5327a59d7cb99d1a55dba56f8295741 |
| chaos_redux_022_against_the_order | gfx/achievements/chaosx_achievement_022_against_the_order_not_eligible.dds | gfx/achievements/chaos_redux_022_against_the_order_not_eligible.dds | b71af5ad38118f576a6cfa6943164935cfe64c08a4c30331ebf3c243af326828 |

Excluded current-scope subjects:

- chaosx_achievement_022_names_restored: dropped by accepted P-022-E
- chaosx_achievement_022_long_return: unimplemented; missing migration proof
- chaosx_achievement_022_from_camps_to_care: dropped by accepted P-022-E
- chaosx_achievement_022_no_second_operator: dropped by accepted P-022-E

The excluded assets and original source files remain untouched.
Skills used: chaos-redux-event-assets, chaos-redux-subagents, chaos-redux-shared-git-commit.
