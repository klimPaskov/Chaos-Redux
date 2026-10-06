# Event 002 portrait replacement handoff

Date: 2026-10-06  
Disposition: implemented and installed for the 12 parent-approved active portraits; live-game review remains user-owned.

## What changed

This handoff covers only the 12 active portrait DDS files named below and the Event002 source archive. The parent approved original fictional ImageGen art for all 12 and reviewed the corrected three-member leader_1 stage before installation. The generated family now uses one coherent muted olive/khaki HOI4-painted treatment and stable 156x210 portraits.

The source archive is docs/assets/portraits/002_zombie_outbreak/release_20261006/. The 12 legacy DDS binaries are preserved byte-for-byte under legacy_unverified_dds/; each selected source master, prompt, crop JSON, processed PNG, 4x preview, candidate DDS, and review status is stored beside it.

The installed runtime paths are the pre-existing stable files in gfx/leaders/002_zombie_outbreak/: leader_1 through leader_4 and weaponized infected, rabid, parasitic, mutant, undead, necrotic, demonic, and wendigo. The already-wired GFX_portrait_* names and dynamic consumers remain unchanged. No character identity, gameplay, localisation, event, focus, decision, GUI, or GFX file was edited.

## Parent decisions carried into this package

The original task explicitly authorized four collective leader-stage portraits showing the same three fictional members as newly risen dead, early undead, decayed undead, and demonic-stage corruption.

The parent authorized eight distinct fictional weaponized profiles based on the existing special-project outcomes, including an original fictional antlered Wendigo creature with no claim to authentic Indigenous, religious, or ethnographic depiction.

The parent approved the first two weaponized portraits as art and as category-picture source PNGs, then approved the remaining portrait set after reviewing native and 4x contacts. The parent accepted the targeted leader_1_v2 edit for the risen-dead opening and approved the full 12-portrait set for installation.

## Validation evidence

All selected processed PNGs are opaque RGBA at 156x210. All selected candidate DDS files use one-level uncompressed BGRA and decode pixel-identically to their source PNGs. The post-install report confirms each runtime file hash matches its selected candidate DDS and each runtime decode still matches its PNG.

The before-install snapshot confirms all 12 legacy archive files matched the then-current runtime bytes and records the unchanged consumer/GFX source hashes. The post-install report confirms the registered but unused leader_5 texture is byte-identical to its pre-install hash. It also confirms the protected Event014 Hannibal static DDS was unchanged.

Read-only source review confirmed the leader-tier consumer in common/characters/ZZZ.txt and common/scripted_effects/002_zombie_outbreak_effects.txt, plus the eight profile refresh consumers in common/scripted_effects/zombie_special_project_effects.txt. Vanilla references included a single-leader portrait and the Soviet Supreme Soviet group portrait at 156x210, along with the local leader portrait reference-family contact sheet.

No HOI4 session or desktop window was opened, and no RunPod operation was performed. The user retains live-game validation.

## Separate Hannibal reveal portrait

The complete Event002 chain has a later reveal that uses ZZZ_hannibal_wendigo, the fictional Hannibal Lecter character owned by Event014. common/characters/014_cannibalism_characters.txt:19-25 defines the character; common/scripted_effects/zombie_special_project_effects.txt:2708-2712 assigns it after the reveal. The leader character sprite GFX_portrait_ZZZ_hannibal_wendigo in interface/014_cannibalism.gfx:565 points to the protected static gfx/leaders/014_cannibalism/hannibal_wendigo.dds, not to one of the 12 Event002 replacement textures. That static texture is 156x210, 174608 bytes, opaque, eight mipmaps, and SHA-256 26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717. The separate GFX_cannibalism_wendigo_portrait_animated presentation sprite at interface/014_cannibalism.gfx:567 uses gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds, 2496x210, 16 frames, 12 fps, SHA-256 f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b.

The 2026-10-03 receipt records the static file as protected user-supplied but does not retain its original source, crop, licensing basis, or independent static-art acceptance. The earlier Event014 audit also records missing original/source crop/provenance contract/static review. The late Event014 regeneration handoff describes a generated transformed Hannibal master and animation but says the archival static was preserved; its named Wendigo package path is absent from the current asset archive. This audit classifies the character as fictional and does not infer actor likeness from the pixels.

This file and its animation remain untouched and are not covered by the 12-portrait approval. Their provenance/approval gap needs a separate parent follow-up if the scope is expanded. Do not claim that the 12-texture package covers the full reveal chain.

## Exact parent force-add scope

The complete ignored source/evidence archive is owned at docs/assets/portraits/002_zombie_outbreak/release_20261006/. The durable documentation owned by this handoff is:

- docs/assets/portraits/002_zombie_outbreak/release_20261006/manifest.md
- docs/plans/002_zombie_outbreak_plans/portrait_source_decisions_20261006.md
- docs/plans/002_zombie_outbreak_plans/subagent_handoffs/portrait_replacement_20261006.md
- docs/plans/002_zombie_outbreak_plans/subagent_handoffs/portraits_audit_20261006.md, retained as the read-only pre-production baseline

The earlier read-only audit at docs/plans/002_zombie_outbreak_plans/subagent_handoffs/portraits_audit_20261006.md records the pre-production state and is superseded for the 12 active portrait slots by this handoff and its source/promotion evidence. Its leader_5 and Hannibal findings remain open as separate scope items.

Do not include unrelated Event014 portrait files, the unused leader_5 texture, or another worker's category-picture files when force-adding. No files were staged or committed; the parent owns shared-tree staging and commit.
