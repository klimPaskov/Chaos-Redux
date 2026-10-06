# Event 002 portrait audit

Date: 2026-10-06  
Disposition: blocked for provenance and the unused tier-5 sprite; visual and texture audit completed.  
Authority: Parent assignment authorized a read-only portrait audit for Events 002 and 003. It did not authorize art generation, runtime changes, GFX edits, GUI work, or portrait acceptance.

## Verdict

All thirteen DDS files registered for the ZZZ leader and weaponized portrait family are present and decode as 156×210 portraits. Contact-sheet review found no blank placeholders, clipped-off faces, or exact duplicate images. The four used horde-tier portraits read as a collective, matching the generic Zombie Horde consumer; the eight weaponized portraits are individually readable, though their rendering and background treatments vary across the set. No unambiguous crop defect was found.

The consumers are fictional zombie hordes and fictional/folkloric weapon profiles rather than named real people. A future production pass should use the fictional-asset route if the parent decides to replace these legacy textures. The current DDS files have no recoverable portrait source receipts, native ImageGen prompt/output record, attribution record, or approved user-final evidence in the inspected archives, so their actual production route remains unknown and they cannot be called provenance-complete finals.

One registered texture, portrait_ZZZ_leader_5.dds, has no current character, scripted-effect, scripted-localisation, history, event, or decision consumer in the searched runtime source. Keep it unresolved until the parent decides whether a fifth tier is intended or whether the sprite and texture should be retired.

## Consumer map

| Sprite and texture | Current consumer |
| --- | --- |
| GFX_portrait_ZZZ_leader_1 / portrait_ZZZ_leader_1.dds | Initial portrait for character ZZZ_leader, named Zombie Horde, in common/characters/ZZZ.txt:2-10. |
| GFX_portrait_ZZZ_leader_2 / portrait_ZZZ_leader_2.dds | Tier 1 branch of refresh_dynamic_zombie_country_leader in common/scripted_effects/002_zombie_outbreak_effects.txt:2170-2201. |
| GFX_portrait_ZZZ_leader_3 / portrait_ZZZ_leader_3.dds | Tier 2 branch of refresh_dynamic_zombie_country_leader. |
| GFX_portrait_ZZZ_leader_4 / portrait_ZZZ_leader_4.dds | Tier 3 branch of refresh_dynamic_zombie_country_leader. |
| GFX_portrait_ZZZ_leader_5 / portrait_ZZZ_leader_5.dds | Registered at interface/chaosx_characters.gfx:115-116, but no other source use was found. |
| GFX_portrait_ZZZ_weaponized_infected, _rabid, _parasitic, _mutant, _undead, _necrotic, _demonic, and _wendigo | All eight have matching flag-gated leader-name and portrait assignments in weaponized_zombie_refresh_country_leader at common/scripted_effects/zombie_special_project_effects.txt:2628-2697. The wendigo profile is later replaced by the separate Hannibal Lecter portrait after the cannibalism reveal; the generic wendigo profile itself is not orphaned. |

The category-picture source archive is not portrait provenance. Its manifest states that the eight PNGs in docs/assets/002_zombie_outbreak/decision_category_pictures/source_png/ are lossless previews decoded from the existing portrait DDS files and that those portrait masters were left untouched. It only produces seven category-picture variants; the separate wendigo portrait remains a live special-project leader portrait.

## Visual and texture review

The native vanilla examples inspected were interface/_leader_portraits.gfx:65-68 with gfx/leaders/USA/Portrait_USA_Generic_land_4.dds, and interface/_leader_portraits.gfx:2771-2773 with gfx/leaders/SOV/portrait_SOV_supreme_soviet.dds. Both vanilla textures decode to 156×210. The first is a conventional single leader portrait and the second demonstrates a valid group/council portrait composition at the same canvas.

The mod family uses the expected 156×210 canvas and full-background treatment. The leader-tier sequence shows the same generic group progressing from living soldiers to undead and demonic forms. The weaponized profiles span several rendering styles and close portrait crops; each face or creature remains readable at native size. The group set is darker and more photographic/painterly than the selected vanilla examples, and the weaponized set varies more internally. This is a parent style-acceptance question, not a confirmed technical crop failure.

Decoded-pixel hashes were distinct across all thirteen textures. Alpha was opaque for the five leader-tier textures and the infected, rabid, parasitic, mutant, undead, demonic, and wendigo textures except for the small antialiased extrema below; no transparency-dependent crop was apparent. FFmpeg decoded leader tier 2 successfully as 156×210 BGRA sRGB from a DX10 DDS header; Pillow's DDS decoder did not support that format, so the format difference is recorded without claiming the game rejects it.

| DDS path | Bytes | Dimensions | Alpha extrema | Raw DDS SHA-256 |
| --- | ---: | --- | --- | --- |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_1.dds | 16664 | 156×210 | 255–255 | 9bd169b7874569ceeb88d35452b9cc8564ca84fcb8971e2b8c2100912cd0ff00 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_2.dds | 131188 | 156×210 | 255–255 | 623f294dc648ac800e937bb826587d0f063f8aa3fe30eed44927431cf82194af |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_3.dds | 16664 | 156×210 | 255–255 | ec7eeb42ca62947a098459e9d686db45e2ef0aa060137bde796c6483e2c3e326 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_4.dds | 16664 | 156×210 | 255–255 | c8b155e8ea64ea1a0fe99f43655d76034710c2f7e3fd9967210ada9cba3a077b |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_5.dds | 16664 | 156×210 | 255–255 | 959018ce48f01aba417cadddfb420364e3276b88bb7c4cc2d4a6f08712d80d9c |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_demonic.dds | 174608 | 156×210 | 255–255 | 9c318ea12eb7209da081f67378d10b16e70fbe6827a56572bdcb70122b0a72d0 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_infected.dds | 174608 | 156×210 | 255–255 | 68e57696a4e03cf0a20f79a26487ae99098cc792d3351839069ad8193835c1c1 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_mutant.dds | 174608 | 156×210 | 255–255 | 61b68b18325cb0d527e222f7b3a973eb14e071a97e134a2b1968c2e6cabd20d1 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_necrotic.dds | 174608 | 156×210 | 254–255 | 30b87a629e6da43a14d6f33a038775cfb0708ad01db81854da56fd25cb231d76 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_parasitic.dds | 174608 | 156×210 | 238–255 | 7d0e8e445f04d75fb56e3199ec7a57a9d8277befa13a2882313e19e684f12ec1 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_rabid.dds | 174608 | 156×210 | 228–255 | 4a19288a4d504120038397963aa90a50abdcbab68c5b5b0fcf23d706c30f30f3 |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_undead.dds | 174608 | 156×210 | 238–255 | 2da58149f4f2cb36124bb32654b8be3e0a094bb5c706d774196c5f79b46acd3f |
| gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_wendigo.dds | 174608 | 156×210 | 255–255 | 1468c7998f98cca7cf79d916a5db177aaf2bf93b6568a977ea901a22b9fd4fdc |

## Archive and provenance findings

The direct ignored-path check found docs/assets/portraits/002_zombie_outbreak/ absent. The inspected docs/assets/002_zombie_outbreak/ tree has 7,265 files, but the only files matching the portrait texture stems are the eight decoded category-picture previews described above; no original portrait masters, source receipts, prompt/output records, rights notes, or user-final approval were found. Git reports docs/assets/ ignored by .gitignore:80, so this check explicitly enumerated the ignored files instead of relying on the default tracked-file search.

The 2026-10-05 Event002 release-QA handoff also recorded portrait provenance as unresolved and said no portrait-creator handoff was located. Its wording describes a seven-item weaponized portrait family, while the current source maps all eight registered weaponized textures, including wendigo, to the special-project leader refresh. The current consumer trace takes precedence for this audit.

## Bounded follow-up

1. Parent decision required for portrait_ZZZ_leader_5.dds: either identify and accept its intended fifth-tier consumer or retire the unused sprite/texture in a separately reviewed patch.
2. Provenance is blocked for all thirteen current DDS files. If replacement production is authorized, create a portrait-specific archive with the actual native ImageGen evidence, source/output lineage, processed 156×210 PNG previews, DDS hashes, and a reviewed manifest; keep the current DDS as legacy baselines until review.
3. Parent review should decide whether the family’s mixed weaponized rendering style is acceptable. No image was re-cropped or replaced during this audit.
4. Live-game rendering and consumer validation were not performed; no HOI4 session was opened. Only read-only source inspection, DDS decoding, local image review, and vanilla texture comparison were performed.

Review contact sheet: C:\Users\klimp\AppData\Local\Temp\portrait_audit_002_003_20261006\002_zombie_outbreak_portraits_contact.png. No runtime or GFX file was changed.
