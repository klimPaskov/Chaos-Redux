# Audio, icon, and portrait restoration evidence

This report covers A3 audio, A4, A5, A6, A7, and the Inhumane scientist trait icon from the owner's restore plan.
The user authorized exact historical restores on 12 October 2026, retaining genuine new mechanics and vanilla-placeholder replacements.
No new artwork is produced for this task.

## A3 audio — restored

Offending commit `ad5678a09d9399c2ba4bc7244495b7cbe2c36d98` replaced nine existing recordings on 1 September 2026.
Restore commit `10292700c22304f1181b96733b797d2faf681a25` restores their exact bytes and corresponding catalogue rows from its parent `5e33b96da00a0fa3a5fe153808c368a798838fc0`.
The restored cues are zombie outbreak 1, defeat 5, Wendigo 6, Holy Realm 9 and 12, Soviet Collapse 15, 17 and 18, and Rat King 102.
The new Event 039 cue remains.
The routing review covered interface sound registrations, sound assets, music, and super-event scripted effects since 1 September 2026.
Existing cue IDs and paths had not been reassigned; later registrations were additions for new events.
Every restored WAV was hydrated with `git lfs smudge` and its SHA-256 matched the historical LFS OID.
The historical catalogue marks some source/license metadata unverified; this exact restore preserves that limitation.
Detailed source diffs and per-file hashes are retained in `.tmp/restore_assets_audio/audio/audio_restore_evidence.md`.

## A4 cylinders — originals already present, independently verified

Offenders `38ae4996e662ba98451bdd5774045d811dadfec6` and `308324b3d3f00f0ef0ec556d1e83d6599fbe0bb9` replaced the seven research DDS files.
Existing restore commits `eb54b2c8eab7c47ff25dab4020f5f26e8c4e9536` and `75fcd313b1acf70a0f15903fa236197957c337dc` put the originals back.
All seven current files were compared byte-for-byte with hydrated `38ae4996e^` blobs and matched.
`interface/chaosx_techtree.gfx` still maps chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman research sprites to those exact original paths.
The comparison and SHA-256 values are retained in `.tmp/restore_assets_audio/parent/original_audit.json` and `originals_comparison.png`.
No speculative replacement was made to already restored files.
Offender `d3c613a2c5c445a4eb4c1bad5a9e5b8d83176bd0` also repointed 21 established cylinder equipment sprite aliases to newly named wide paintings.
Those 21 texture fields in `interface/chaosx_equipment.gfx` were restored from `d3c613a2c^` to the same original seven research DDS files.
The wide DDS alternatives remain on disk with no deletion or repaint, and tank-shell icons that replaced vanilla flamethrower placeholders are retained.
Per-alias paths and restored target hashes are retained in `.tmp/restore_assets_audio/parent/cylinder_aliases_restore.json`.

## Inhumane scientist trait — original already present, independently verified

Offender `8450deaf874cfe98f8a9e9586ed1de5b8a79c007` replaced `gfx/interface/traits/scientist_traits/scientist_trait_inhumane.dds`.
Existing restore commit `8b8f2135428997b41cdad39bedbe98e0f8574ac6` restored it.
The current file equals the hydrated `8450deaf8^` blob byte-for-byte, with SHA-256 `f6f1dcfd27f81d9363f798847b09fb908e287fbea99d31d214ea7ff3e71c2654`.
`interface/chaosx_traits.gfx` maps `GFX_scientist_trait_inhumane` to that file.

## A7 truck — unchanged original vanilla bytes

`5c873230be691d43b76af60ee336ba7440740172` added the local motorized equipment texticon; history contains no later modification to its DDS.
Its current bytes equal both the original Git blob and installed vanilla `gfx/texticons/unit_motorized_icon_small.dds`, with SHA-256 `5edd42b0810ab5ab86c59219331dc4686c9c7ac3a070b2acd354968f6c899ff9` and canvas 60×12.
The only mod sprite definition points to this file, with two frames and `legacy_lazy_load = no`.
No alternate truck was invented.

## A6 portraits — historical restore batches

Restore commit `59267b7c8` restores 49 existing DDS files from the exact parents of five repaint commits.
The 45 Event 031 portraits comprise 12 clandestine/criminal portraits from `e8a307393a^`, 14 jihadist/military portraits from `9aaeb596a0^`, 12 millenarian/revolutionary portraits from `2f506bc816^`, and seven council/entity portraits from `ad741f951f^`.
The remaining four portraits are Hannibal Wendigo and its sheet, Ilyr Ren, and Kruger stage 0, restored from `34559caed6^`.
The exact source parents are `29b582d0d6`, `e8a307393a`, `9aaeb596a0`, `2f506bc816`, and `569e22ca6f`, respectively.
Existing portrait sprite paths and character references remain bound to these original filenames.
At the first batch, the parent rechecked all 49 file hashes against the historical LFS OIDs, with no mismatches, and reviewed the restored contact sheet.
The row-level paths, source pointers, repaint pointers, dimensions, and hashes are retained in `.tmp/restore_assets_audio/portraits/restore_evidence.json`.
Follow-up commit `85594b997` restores five Random Terror files changed earlier in `3098ed9d2`, using `3098ed9d2^` rather than their later October parents.
Four of these files overlap the first batch; jihadist 08 is the fifth.
The wider currently consumed portrait history is being completed before A6 is marked finished.

## A7 other texticons — restored

Restore commit `b23e41257f78895546fcbb2843756610ba2875f2` restores 42 DDS files and 32 earlier texture/frame bindings in `interface/chaosx_texticons.gfx`.
The restored families are support equipment, CBRN instruments, chemical support/category artwork, the Chaos Battalion, Livens projectors, nine Cannibalism unit glyphs, the Independence Wave reserve glyph, famine/migration/medical resource glyphs, zombie variants, Death Ghost, and Murder Mystery operations kits.
The offending redraw chains are `1a4af3a4d`, `37e369007`, `1cb4d061f`, `07e229d3d`, `b0dcc9f5b`/`1e42516fe`, and `baaf0c041`.
Each binary comes from the parent of its first unwanted redraw; the later Murder Mystery and famine/migration redraws do not become the restore baseline.
The 23 CBRN bindings repointed by `f7fa11b52` return to their exact earlier custom aliases from its parent.
The nine support-equipment, armored-category, and agent-specific Livens binding/frame changes return to `1a4af3a4d^`.
Eleven deleted original DDS targets required by those aliases were reinstated from the cited pre-change versions; the corresponding retired gameplay units were not reinstated.
Genuine new resource glyphs remain, and the replacement files under new names remain on disk when unbound.
An independent read-only reviewer checked all 42 hashes against the historical LFS OIDs, all 32 aliases against their historical bindings, target existence, and frame declarations, and found no concrete defect.
The parent reviewed the before/original contact sheet and the complete intended diff.
The row-level binary sources, hashes, and alias sources are retained in `.tmp/restore_assets_audio/parent/texticon_restore_manifest.json` and `texticon_wiring.json`.
The additional inline unit aliases in `interface/chaosx_missing_unit_texticons.gfx` reference small counter textures directly.
Their changed existing texture history is being restored separately; the aliases and genuinely new textures remain.

## Reference evidence and scope

The connected MCP reference routes were exposed and used.
Offline wiki `Localisation - Hearts of Iron 4 Wiki.md`, lines 221–243, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was read for texticon names and frame handling.
Offline wiki `Graphical asset modding - Hearts of Iron 4 Wiki.md`, lines 30–100, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, was read for sprite texture and frame definitions.
Installed `common/scripted_guis/_documentation.md`, lines 30–69, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, was read for icon/image properties.
The installed documentation search contains no `texturefile` section; the actual installed `interface/texticons.gfx` and motorized DDS provide the vanilla precedent.
MCP source lookup confirmed the sole mod motorized sprite at `interface/chaosx_texticons.gfx`, lines 95–100, source revision `a2301aa9219ccce460b5efd3994c88604804c3e4b1ab9c84df46fc0e988ed20c`.
This evidence establishes source routing and binary identity; Hearts of Iron IV was not launched.

Skills used: `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`, with specialist system skills used by the icon worker where consumers require them.
No skills were created or updated.
