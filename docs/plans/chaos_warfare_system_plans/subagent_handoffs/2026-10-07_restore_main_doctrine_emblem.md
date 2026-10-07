# Main Chaos Warfare Doctrine Icon Restoration

Status: complete for the assigned runtime asset and evidence scope; parent review remains.

## Result

Restored the exact pre-change DDS bytes at gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds from the verified local Git LFS object referenced by commit 4efc01fc87f1137e98c864f928dd5603e6b7d2f1.

The active consumer remains chaos_warfare in common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt, using GFX_doctrine_chaos_warfare_medium from interface/cbrn_doctrine.gfx.

The sprite-to-texture binding is unchanged in pre-change parent 4efc01fc87f1137e98c864f928dd5603e6b7d2f1, checkout HEAD 63f0799041f303d5d051dbdf22f8cd0bca5f7a48, and the current working tree: gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds.

No GFX, doctrine, gameplay, localisation, index, or other asset file was changed.

## Why the icon changed

Git history shows the DDS was first added in commit 5740285289001f6361b1426b3acf0422ac9d98da on 2026-02-12, and the pre-change LFS object remained in commit 4efc01fc87f1137e98c864f928dd5603e6b7d2f1 on 2026-09-22.

Commit 33b6946dd923b9fc90fbf29bc5798dce3c76a76f replaced the texture on 2026-09-22 at 18:58:15 +03:00; its subject is “Update” and its commit body is empty.

Git does not record the reason for that replacement, so its cause is unknown.

The parent commit 4efc01fc87f1137e98c864f928dd5603e6b7d2f1 is titled “Add shared chaos focus icon family”, but it did not change this DDS; no causal link is evidenced.

The same 33b6946 integration commit added docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-20_cbrn_icon_finish_handoff.md, whose final enlargement section says the main doctrine icon was not changed in that specific track-icon revision.

That handoff does not explain the separate DDS replacement recorded by 33b6946, so its cause remains undocumented.

## Byte and image evidence

| Revision | SHA-256 | Bytes | Decoded dimensions | DDS mip levels | Alpha range |
| --- | --- | ---: | --- | ---: | --- |
| Pre-change / restored | af90fd785c56719867f84ddb7f011bd05811f1c0e2a8fddaabc43aa0dd7908ad | 21,972 | 64x64, one decoded image | 7 | 0–255 |
| Replaced version | 11d41b4ab1de30410458cd52f0352c421c76383f03f59654a2e8e026512653d9 | 16,512 | 64x64, one decoded image | 0 | 0–255 |

The restored runtime file SHA-256 equals the pre-change LFS OID and its decoded RGBA output matches the pre-change image exactly.

All 4,096 decoded RGBA pixel tuples differ between the restored icon and the replacement icon.

The previous runtime texture decoded to the same pixels as docs/assets/chaos_warfare_cbrn/icon_package/processed_png/doctrine_chaos_warfare.png; that processed PNG and its source currently describe the replaced icon.

The historical DDS has seven mip levels, which were preserved as part of the exact byte restoration; no converter or image-generation tool was used.

The existing docs/assets/chaos_warfare_cbrn/icon_package/previous_runtime/doctrine_chaos_warfare.dds copy has the same SHA-256 and size as the historical LFS object; it corroborates the selection, but the restoration source was the Git LFS object from the pre-change revision.

## Review evidence

- docs/testing/2026-10-07_main_doctrine_emblem/before_current_runtime.png is the decoded pre-restoration runtime texture.
- docs/testing/2026-10-07_main_doctrine_emblem/after_restored_runtime.png is a fresh decode of the restored runtime texture.
- docs/testing/2026-10-07_main_doctrine_emblem/before_after_contact_sheet.png shows both versions at native size and enlarged on transparency-review backgrounds.
- docs/testing/2026-10-07_main_doctrine_emblem/evidence.json records Git revisions, LFS OIDs, DDS properties, decoded image hashes, pixel comparison, and the unchanged consumer binding.

## Parent follow-up

The 2026-10-03 reused-doctrine visual audit at docs/plans/027_doctrine_research_plans/subagent_handoffs/reused_doctrine_icon_visual_audit_2026-10-03.md records the replaced runtime hash and its current source and processed PNG lineage.

The parent should reconcile that audit and any related manifest or contact-sheet claims with the restored historical DDS. Those files were outside this assignment.

No standalone UI or in-game validation claim is made.
