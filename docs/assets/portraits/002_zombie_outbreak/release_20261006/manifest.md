# Event 002 portrait replacement manifest

Date: 2026-10-06  
Status: parent-approved fictional portrait package installed at the existing 12 runtime DDS paths; no GFX or character rewiring.  
Validation limit: source, crop, DDS roundtrip, and hash promotion are verified; live HOI4 validation remains user-owned.

## Approval and source mode

The parent explicitly authorized replacement of the 12 active Event002 leader and weaponized-profile portraits with original native ImageGen art on 2026-10-06. The parent reviewed and approved the first two weaponized candidates for art and category-picture derivatives, then reviewed and approved the remaining portraits, including corrected leader_1_v2, before runtime installation.

All 12 subjects are fictional. The four ZZZ leader stages are an explicitly parent-authorized staged three-member fictional collective; the same invented group identities continue from newly risen dead through early undead, decay, and demonic corruption. The eight weaponized profiles depict anonymous fictional types rather than named people. The Wendigo image is an original invented antlered creature and is not presented as an authentic cultural, religious, or ethnographic depiction.

Native ImageGen generated every selected source master. The built-in tool did not expose a model selector; this manifest records the actual tool route and makes no backend-model claim. Full prompts and tool-reported source paths are stored with each source and crop record. All portrait canvases are complete opaque paintings because the portrait consumer uses a full-canvas background.

## Reference and consumer evidence

The installed vanilla portrait examples inspected were interface/_leader_portraits.gfx:65-68 with gfx/leaders/USA/Portrait_USA_Generic_land_4.dds and interface/_leader_portraits.gfx:2771-2773 with gfx/leaders/SOV/portrait_SOV_supreme_soviet.dds. Both decode to 156x210; the first is a single-leader portrait and the second is a group/council composition at the same canvas.

The canonical role family .agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/contact_sheet.png and its eight 156x210 samples were inspected for painted face treatment, subdued palette, natural shading, and opaque painted backgrounds. References transferred style properties only; no reference face or artwork was copied.

All 12 selected sprites were already registered in interface/chaosx_characters.gfx, and the existing dynamic consumers already used their stable names. No GFX, character, gameplay, localisation, event, focus, decision, or GUI file was edited.

| Portrait slot | Existing consumer and intended image | Selected candidate | Source mode | Stable runtime sprite and DDS | Status |
| --- | --- | --- | --- | --- | --- |
| Leader tier 1 | ZZZ_leader; three-member group, newly risen corpses | leader_1_v2 | Native ImageGen; fictional staged collective | GFX_portrait_ZZZ_leader_1; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_1.dds | Approved and installed |
| Leader tier 2 | Dynamic leader refresh, tier 1; same group, early undead | leader_2_v1 | Native ImageGen; fictional staged collective | GFX_portrait_ZZZ_leader_2; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_2.dds | Approved and installed |
| Leader tier 3 | Dynamic leader refresh, tier 2; same group, decayed undead | leader_3_v1 | Native ImageGen; fictional staged collective | GFX_portrait_ZZZ_leader_3; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_3.dds | Approved and installed |
| Leader tier 4 | Dynamic leader refresh, tier 3; same group, demonic stage | leader_4_v1 | Native ImageGen; fictional staged collective | GFX_portrait_ZZZ_leader_4; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_4.dds | Approved and installed |
| Infected | Neurobiological pathogen; living with mind overridden | weaponized_infected_v1 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_infected; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_infected.dds | Approved and installed |
| Rabid | Rage-inducing degenerative agent; fast and aggressive | weaponized_rabid_v2 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_rabid; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_rabid.dds | Approved and installed |
| Parasitic | Parasitic symbiosis; transformed and directed behavior | weaponized_parasitic_v1 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_parasitic; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_parasitic.dds | Approved and installed |
| Mutant | Transformed neurobiological strain; semi-sapient cunning | weaponized_mutant_v2 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_mutant; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_mutant.dds | Approved and installed |
| Undead | Biologically dead canonical reanimation | weaponized_undead_v1 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_undead; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_undead.dds | Approved and installed |
| Necrotic | Dead necrotic siege; slow and durable | weaponized_necrotic_v1 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_necrotic; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_necrotic.dds | Approved and installed |
| Demonic | Extra-scientific corruption; controlled purifier profile | weaponized_demonic_v1 | Native ImageGen; fictional | GFX_portrait_ZZZ_weaponized_demonic; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_demonic.dds | Approved and installed |
| Wendigo | Fast predatory antlered fictional creature with mutations | weaponized_wendigo_v2 | Native ImageGen; fictional creature | GFX_portrait_ZZZ_weaponized_wendigo; gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_wendigo.dds | Approved and installed |

The exact selected-source inventory, source hashes, prompt paths, crop boxes, processed PNG hashes, DDS hashes, legacy backups, and runtime promotion hashes are recorded in notes/asset_inventory.json. Each candidate has a co-located crop/provenance JSON record in crop_records/.

## Source, crop, and DDS processing

Every selected source master is retained under source_imagegen/, with the exact submitted prompt under prompts/. Each selected crop uses a uniform portrait-aspect fit and Lanczos downsample to 156x210; no face was repainted or retouched. The selected native PNGs are under processed_png/, and their corresponding 624x840 nearest-neighbour review enlargements are under review/.

All twelve processed PNGs are 156x210 RGBA with alpha extrema 255-255. All twelve selected candidate DDS files are uncompressed BGRA, one mip, and decode pixel-identically to their selected PNG masters. The complete equality and hash evidence is notes/dds_roundtrip_report.json.

The parent reviewed the first two weaponized portraits at source, native, and 4x sizes on 2026-10-06. The first Rabid output was retained as rejected because its style reference caused excessive reuse of the Infected face; the selected Rabid v2 was generated from text only. Mutant v1 was retained as rejected because its mutation was not clear at native size. Wendigo v1 was retained as rejected because its antler tips approached the portrait edges. Leader_1 v1 was retained as rejected because the faces appeared healthy despite the outbreak depicting risen dead; the selected leader_1_v2 adds fresh-death pallor, cloudy eyes, and stiff expressions without changing identity, uniforms, or composition. The initial leader_1 crop attempt is retained separately as a rejected processing attempt; its crop box slightly exceeded the source height, so the same unchanged source was reprocessed with a valid centered crop. Selected versions are explicitly listed in the inventory; no rejected alternative was installed.

The review sheets are contact_sheets/early_weaponized_candidates_native.png, contact_sheets/early_weaponized_candidates_4x.png, contact_sheets/remaining_leader_tiers_native.png, contact_sheets/remaining_leader_tiers_4x.png, contact_sheets/remaining_weaponized_native.png, contact_sheets/remaining_weaponized_4x.png, contact_sheets/corrected_leader_1_stage_comparison_native.png, and contact_sheets/corrected_leader_1_stage_comparison_4x.png. Rejected-version contact sheets are retained separately with rejected in their filenames.

## Legacy versions and installation evidence

Before installation, all twelve prior runtime DDS files were copied byte-for-byte to legacy_unverified_dds/ because their original source provenance was unresolved. They are preserved as previous versions, not as source masters or approvals.

| Prior runtime file | Archived prior path | Prior SHA-256 |
| --- | --- | --- |
| portrait_ZZZ_leader_1.dds | legacy_unverified_dds/portrait_ZZZ_leader_1.dds | 9bd169b7874569ceeb88d35452b9cc8564ca84fcb8971e2b8c2100912cd0ff00 |
| portrait_ZZZ_leader_2.dds | legacy_unverified_dds/portrait_ZZZ_leader_2.dds | 623f294dc648ac800e937bb826587d0f063f8aa3fe30eed44927431cf82194af |
| portrait_ZZZ_leader_3.dds | legacy_unverified_dds/portrait_ZZZ_leader_3.dds | ec7eeb42ca62947a098459e9d686db45e2ef0aa060137bde796c6483e2c3e326 |
| portrait_ZZZ_leader_4.dds | legacy_unverified_dds/portrait_ZZZ_leader_4.dds | c8b155e8ea64ea1a0fe99f43655d76034710c2f7e3fd9967210ada9cba3a077b |
| portrait_ZZZ_weaponized_infected.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_infected.dds | 68e57696a4e03cf0a20f79a26487ae99098cc792d3351839069ad8193835c1c1 |
| portrait_ZZZ_weaponized_rabid.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_rabid.dds | 4a19288a4d504120038397963aa90a50abdcbab68c5b5b0fcf23d706c30f30f3 |
| portrait_ZZZ_weaponized_parasitic.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_parasitic.dds | 7d0e8e445f04d75fb56e3199ec7a57a9d8277befa13a2882313e19e684f12ec1 |
| portrait_ZZZ_weaponized_mutant.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_mutant.dds | 61b68b18325cb0d527e222f7b3a973eb14e071a97e134a2b1968c2e6cabd20d1 |
| portrait_ZZZ_weaponized_undead.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_undead.dds | 2da58149f4f2cb36124bb32654b8be3e0a094bb5c706d774196c5f79b46acd3f |
| portrait_ZZZ_weaponized_necrotic.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_necrotic.dds | 30b87a629e6da43a14d6f33a038775cfb0708ad01db81854da56fd25cb231d76 |
| portrait_ZZZ_weaponized_demonic.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_demonic.dds | 9c318ea12eb7209da081f67378d10b16e70fbe6827a56572bdcb70122b0a72d0 |
| portrait_ZZZ_weaponized_wendigo.dds | legacy_unverified_dds/portrait_ZZZ_weaponized_wendigo.dds | 1468c7998f98cca7cf79d916a5db177aaf2bf93b6568a977ea901a22b9fd4fdc |

notes/runtime_preinstall_snapshot.json records that each legacy backup matched its runtime file before replacement and captures the unchanged leader_5 and consumer/GFX source hashes. notes/runtime_promotion_report.json records that each post-install runtime DDS hash equals its selected candidate DDS hash, every runtime DDS decodes to the selected PNG pixels at 156x210, every portrait remains opaque, the existing sprite bindings resolve, leader_5 is unchanged, and the protected Hannibal texture is unchanged.

The unused registered GFX_portrait_ZZZ_leader_5 and portrait_ZZZ_leader_5.dds remain untouched; the texture was not part of the parent-approved 12-portrait scope.

## Late Wendigo reveal: separate protected portrait outside this package

The complete Event002 chain can reveal the separate fictional character Hannibal Lecter through Event014. This package does not cover that portrait.

common/characters/014_cannibalism_characters.txt:19-25 defines fictional character ZZZ_hannibal_wendigo, localized as Hannibal Lecter, with GFX_portrait_ZZZ_hannibal_wendigo. After the reveal, common/scripted_effects/zombie_special_project_effects.txt:2708-2712 assigns that sprite and name. interface/014_cannibalism.gfx:565 binds the sprite to gfx/leaders/014_cannibalism/hannibal_wendigo.dds; this static texture is 156x210, 174608 bytes, opaque, eight mipmaps, and SHA-256 26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717. The separate presentation alias GFX_cannibalism_wendigo_portrait_animated is registered at interface/014_cannibalism.gfx:567 and uses gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds, a 2496x210 16-frame sheet at 12 fps with SHA-256 f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b.

docs/assets/portraits/014_cannibalism/hannibal_static_receipt.md records the static DDS as a protected user-supplied runtime file based on prior Event014 completion records. The receipt was reconstructed from current bytes and retained handoffs and explicitly does not claim original source rights or artistic acceptance; no original source, crop, processing, license, or independent static review is retained. The earlier docs/plans/014_cannibalism_plans/subagent_handoffs/event014_portrait_handoff_audit_2026-08-25.md likewise records that the protected static has no retained original, source crop, provenance contract, or independent static review. docs/plans/014_cannibalism_plans/subagent_handoffs/portrait_regen_b_handoff.md describes a generated transformed Wendigo Hannibal master and animation frames, but says the archival hannibal_wendigo.dds was preserved, and the current character sprite remains bound to that protected file. The regeneration handoff’s named leader_portraits_refresh/wendigo_hannibal package is absent from the current asset archive. This audit treats Hannibal Lecter as a fictional character and does not infer actor likeness from the pixels.

This is a separate provenance and approval follow-up for the parent if they choose to expand the brief. No Event014 Hannibal texture, animation, source file, or GFX definition was modified by this package.

## Validation boundary

No HOI4 process, desktop UI, or live game was opened. No RunPod operation was performed. The package's crop and DDS pixels, dimensions, alpha, source/runtime hashes, existing sprite bindings, legacy backups, excluded leader_5 file, and protected Hannibal static hash were verified from local files. Live in-game portrait rendering remains user-owned.
