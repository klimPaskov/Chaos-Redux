# Event 014 Middle East Portrait Install Handoff

Disposition: The eight parent-approved Middle East portrait DDS files are installed; cross-region review and global matrix acceptance remain pending.

## Changed files

All tranche-owned art and evidence is under `docs/assets/014_cannibalism/portrait_finals_2026-10-03/middle_east/`: eight exact prompts plus the CBA safety-retry lineage; eight copied original native ImageGen source PNGs; eight lossless source crops and crop JSON receipts; eight processed `156x210` PNGs; eight approved BGRA32 DDS candidates; byte-identical backups of only the eight previous Middle East runtime DDS files; three review sheets; and complete pre/post snapshots and an install receipt.

This handoff is the only changed file under `docs/plans/014_cannibalism_plans/subagent_handoffs/` for this tranche. No other regional source packages or handoffs were opened or edited; other regional DDS files were hashed read-only as part of the authorized all-60 snapshot.

The only runtime files written by this tranche are the eight existing `gfx/leaders/014_cannibalism/leader_CB[A-H]_warlord_middle_east.dds` paths. No GFX registry or character file was written.

## Exact runtime crosswalk and preserved state

| Slot | Registered sprite | Existing runtime path | Pre-install SHA-256 | Installed and approved DDS SHA-256 |
| --- | --- | --- | --- | --- |
| CBA | `GFX_portrait_CBA_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_middle_east.dds` | `C6C8B35972FD90C40A87B3260064094E429C8C3AA4F6A8D8EC807B7F3098F5FB` | `835F24D1445647A0CC92FC5654679C3CD51128BC4B2C50724113FDEAC5168194` |
| CBB | `GFX_portrait_CBB_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_middle_east.dds` | `B7D084DCDAC9F75CE9B85B751D238A170D7A4D0E18837C89C5A83DFBC967D795` | `0D66C33F8F04B3ECE37CD76F19A4C13AEB56F1575A9D1D25168B59C9CDF529CE` |
| CBC | `GFX_portrait_CBC_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_middle_east.dds` | `E51EEF272A0A011193253A3E01DCB6F1A5A601BF33AA08ECB94733D704520FBE` | `3B5787E8300299F2D88E991710B00D0CED0C9C31F3D58C368B9E41163C072D5F` |
| CBD | `GFX_portrait_CBD_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_middle_east.dds` | `B7C6E580959AB5083A1804924817C85A44D62974D17A489C54D0540C253F326C` | `CC854B20DC946E13285927C7AA2AD13D9A46D80EE33C7BC99A1115B869E44E1B` |
| CBE | `GFX_portrait_CBE_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_middle_east.dds` | `4C33FA4B69F1962222955995FAE58CA82CD822CA72C4757049D8E2A421C78E3D` | `C6A8311A1A7B16AB8F381F0D62076FD431A99BB92B05916CAD444085E2B33341` |
| CBF | `GFX_portrait_CBF_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_middle_east.dds` | `D08E161C5C16D99E19BD63DD777F5CF128CBB7DF9CBA5CBCF400D45C9FE2B402` | `DF6E9DCDB5090B713442BA078A829AE64805C5ED5E1A0CD7E38192A5DDD37207` |
| CBG | `GFX_portrait_CBG_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_middle_east.dds` | `AEB5F56FF0BE8C0297EE5F83C6C336E68761BC15F26FC5488BF511C9CE6E9EE9` | `C06BB23C1411DCD6D364F7E020AE6154009C282F3CAEFC47C40E7195551F9D30` |
| CBH | `GFX_portrait_CBH_warlord_middle_east` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_middle_east.dds` | `BE91C31DC3BA8342A26187CE2D4E17DEB4433F8C6C64A1DC251EB2FB0BCF521C` | `89511E902E0670E0CF94BF7DACA6544BE9B0A5178816C3DE6F9E954789B9C016` |

Sprite names and paths were parsed from the existing `interface/014_cannibalism.gfx` registrations; they were not inferred or renamed. Baseline and final hashes for that GFX file, each existing runtime DDS, the Hannibal static portrait textures, and the protected animated sheets are retained in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/middle_east/evidence/runtime_and_protected_baseline.json`.

## Native ImageGen evidence and source review

The fictional route is parent-accepted within the user's full 56-final instruction. Eight separate built-in native ImageGen source calls succeeded, one per slot, and CBA had one additional failed first request followed by one narrow retry. The first CBA call was rejected at output moderation (`violence`, `self-harm`, request id `7b20e084-a411-4a53-b033-50bdf241eb29`); the retry kept the exact service-whistle action and made the staining non-graphic. All prompts, revisions, returned paths, prompt hashes, source hashes, and outcome details are in `middle_east/evidence/imagegen_call_log.json` and `middle_east/prompts/`.

The reference review used the vanilla leader contact sheet plus the Afghanistan and Ethiopia `156x210` examples and the accepted Europe candidate sheet. These informed painterly finish, framing, palette, and broad set coherence only. No reference was attached to a generation call, copied, or archived as a shipping asset. All eight masters are RGB and opaque; source copies match the native ImageGen output bytes.

The parent reviewed all eight full-resolution sources and the native/decoded DDS contact sheets, approving the bounded set's painted human portraits, framing, unique faces, backgrounds, and assigned gestures, including CBG's tooth-to-helmet contact at `156x210`. The approval receipt is `docs/plans/014_cannibalism_plans/evidence/2026-10-03_middle_east_portrait_parent_review.json` and is limited to these eight assets within the full 56-portrait goal. Cross-region distinctness still requires review of the other regional portraits.

## Processing and checks

Source masters are `1080x1456` or `1081x1455`; exact centered aspect crops and hashes are in `middle_east/crops/` and `middle_east/evidence/processing_log.json`. Each processed PNG is opaque RGB `156x210`, produced by LANCZOS resizing without repaint, filtering, or synthetic background fill. All eight candidate DDS files were made with the required `convert_to_dds.py` tool and are 32-bit BGRA, `156x210`, single-level, `131168` bytes each. Decoding each DDS confirms exact RGB equality with its PNG and opaque alpha; evidence is `middle_east/evidence/dds_verification.json`, and the decoded native contact sheet is `middle_east/review/middle_east_dds_decoded_native_4x2_contact_sheet.png`.

## Replacement state, remaining queue, and blockers

The parent-approved DDS candidates are installed byte-for-byte at the eight pre-existing Middle East runtime paths. The old eight DDS files are backed up and hash-verified in the tranche evidence. All 60 DDS files, the Event 014 `.gfx` registry, and the Event 014 character definition were snapshotted immediately before installation and again afterward. Forty-four of the 52 nonowned DDS files remained unchanged; eight Africa paths changed concurrently and are listed with before/after hashes in the receipt. The protected Hannibal DDS/portrait sheets, GFX registry, and character file remained unchanged. No region or registry changes were reverted.

Previously installed Europe and Asia DDS paths were included in the snapshots and remained unchanged. The eight Middle East runtime replacements are parent-approved for this tranche. Cross-region uniqueness review and global 56-portrait/Event 014 completion remain pending with the other regional owners; no full-goal or live-game acceptance is claimed. No commit was created.

The existing `.gitignore` rule at line 80 ignores the `docs/assets/` tree, including this source/evidence package. The runtime DDS replacements and this handoff are visible in the shared workspace. I did not force-add the ignored art or modify `.gitignore`.

Skills used: `chaos-redux-event-assets`, its portrait-production reference, and the official built-in `imagegen` skill.
