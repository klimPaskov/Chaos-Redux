# Audio, icon, and portrait restoration evidence

This report covers A3 audio, A4, A5, A6, A7, and the Inhumane scientist trait icon from the owner's restore plan.
A3 audio, A4, A6, A7, and the Inhumane icon are restored or verified original.
A5's 935-file restoration and recoverable wiring fixes are implemented, but its missing-art and family/size outputs remain incomplete as listed below.
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

## A5 bulk icons — restores implemented; family and missing-art outputs incomplete

935 existing DDS files were restored, covering focus, idea, decision, mission, category, counter, template, trait, ability, MIO, raid, faction-miniature, and equipment-designer artwork.
Fourteen non-cylinder research/equipment files already matched the original `38ae4996e^` bytes and were left unchanged.
The source matrix is `.tmp/restore_assets_audio/icons/a5_final_source_hash_handoff.json`; it contains each path, offending commit, exact parent, historical LFS OID, current SHA, and evidence source.
The parent independently compared 945 currently consumed files against their earliest modifying parents in the frozen pre-task history, with no byte mismatches; four reinstated deleted idea files have separate before-deletion source evidence.
That check includes the fourteen unchanged originals, giving 949 audited DDS paths in total.
Twenty-five files initially restored only to later repaint parents were traced back again and corrected to their earlier original parents.
The existing forest and stone large counters were likewise corrected to `6d3dc8283^`.
The two A7-owned paleogenetic/temporal small counters correctly remain at `bc3a45d86^`; the separate xenobiological small counter first changed in `414313038` and correctly uses that parent.

171 picture-field prefix corrections in fourteen idea files restore resolution to existing idea-family sprites, committed in `7a9cfcbf7`.
Black Death, Mass Panic, and Alien Spacecraft original idea DDS/aliases were reinstated, and three Black Plague state modifiers again use the original idea icon instead of decision artwork.
Two Holy Realm decisions referencing a nonexistent `generic_army` decision alias use the existing vanilla `generic_military` decision alias.
The original Holy Realm category binding is preserved; a proposed repoint to unbound artwork was reverted in `c9ff9d16a`.
The Black Plague response-state selector's category-icon regression in `3deac2d4d` was restored from that commit's parent in `a3bf9361a`, returning to `GFX_decision_black_plague_quarantine` and its native 33×32 decision DDS.
Its gameplay conditions and effects were preserved.

| First replacement/deletion | Exact restore source | DDS paths |
| --- | --- | ---: |
| `003d051dc8` | `abcff0ca31` | 1 |
| `02514e8d01` | `8190ed8cda` | 19 |
| `08ed41a37c` | `d3c613a2c5` | 27 |
| `154adc58e5` | `2dfa31e31c` | 1 |
| `1af5699b3b` | `fe0025208e` | 1 |
| `1cb4d061fb` | `b6bc6b4210` | 6 |
| `2936e79631` | `bc4a774cc3` | 11 |
| `2fd2f9258d` | `248dd887e7` | 3 |
| `3098ed9d2b` | `2e44610483` | 3 |
| `33b6946dd9` | `4efc01fc87` | 1 |
| `34559caed6` | `569e22ca6f` | 1 |
| `34ebd842c2` | `f8fa547326` | 50 |
| `35142b2c41` | `8ae1289b0b` | 4 |
| `37da905a3a` | `003d051dc8` | 1 |
| `399f054fb5` | `9a695313b1` | 45 |
| `3d7e3306e8` | `5f916facc4` | 1 |
| `414313038b` | `7634a39be1` | 18 |
| `5b44f0d3f5` | `1dccf6f733` | 1 |
| `5b6ed2ce58` | `c041810a8b` | 10 |
| `6288ccfebe` | `2782e3b12f` | 5 |
| `6d3dc8283f` | `e0a8a9fda5` | 2 |
| `77bbd81e1e` | `233ecf899a` | 567 |
| `77cdab8e09` | `8afb9f3d0a` | 2 |
| `7bf1ebd4ee` | `79a62a4c50` | 6 |
| `8172a80ba5` | `7353ab5b85` | 1 |
| `8450deaf87` | `9225f02da2` | 4 |
| `a89a5e086a` | `74ce713384` | 2 |
| `b0dcc9f5b9` | `8fc8e5af84` | 14 |
| `bbe5309cbe` | `657c0616a3` | 6 |
| `bc4a774cc3` | `04c5858729` | 1 |
| `c606f8d415` | `92ce42facc` | 8 |
| `cc5f0e876c` | `afd107c826` | 5 |
| `d6280f69c0` | `da083fc7e0` | 6 |
| `e77e647d06` | `390cbbac4d` | 61 |
| `ec17eb5367` | `e9390b86dd` | 1 |
| `f5f0c7c4c2` | `d604ace80d` | 32 |
| `f6ee19d9c6` | `f08e286d67` | 1 |
| `f7a08ab4fb` | `b0d53742ec` | 2 |
| `fbd3887dd1` | `a5a2e2d633` | 5 |

The art/wiring commits are `539006cd86`, `c9ff9d16a5`, `6344893ec7`, `2aa9a2b531`, `325bd35762`, `2f100da79a`, `25f0fbd38f`, `99efdc907f`, `6ba18c584`, `6a07b3b661`, `91073d05ed`, `f2a56c615d`, `079a3a6c0b`, `fa54ab5c5b`, `97666705a6`, `163ad74e4c`, `f2be4e603d`, `d7dd251166`, `d27ab9d082`, `7bdaf62ef8`, `8d283d598a`, `57759c7485`, `7a9cfcbf79`, `f6012031f3`, and `a3bf9361ae`.
`f6012031f3` commits the Great Depression public-works pilot restore that remained uncommitted after the first asset batch.
`6ba18c584` is the ability/MIO/designer restore; `6a07b3b661` is the Event 039 counter restore.

### Family audit and unfinished outputs

The final source matrix covers 1,993 ideas, 4,296 decision icons, 388 category icons, and 84 category pictures.
No idea consumer resolves to decision-family artwork, and no decision consumer resolves to idea-family artwork.
265 hidden carrier ideas intentionally have no icon.
The current source snapshot is `a3bf9361ae`; the corrected Black Plague decision binding was rechecked after its restoration.

The following requested A5 outputs remain incomplete, without a substituted image or resized original:

- 36 visible Event 016 ideas have no historical own-id sprite or corresponding original asset: 24 in `common/ideas/016_brilliant_scientist_aftermath_ideas.txt` and 12 in `common/ideas/016_brilliant_scientist_focus_ideas.txt`.
- `mysterious_people_select_hotspot` and `mysterious_people_close_hotspot` use the original 52×40 category sprite; their new-mechanic history supplies no previous decision-family binding to restore.
- `THR_begin_concentration_sequence`, `THR_hold_intention`, `THR_hold_energy`, `THR_hold_mind`, and `THR_hold_investigation` reference the restored original 12-frame animated Dhyana seal; each frame remains 96×96, so the native-size warning persists without an authorized resize or substitution.
- `doomsday` references the original vanilla `GFX_idea_FRA_matignon_agreements` alias, but its DDS is absent from the examined installed loose files and local DLC archive, and no original mod binary exists to restore.

The exact missing idea IDs and their history are retained in `.tmp/restore_assets_audio/icons/historical_missing_idea_icon_audit.json` and the consolidated handoff.
Original Event 014 idea files at 68×68 and native vanilla size variants remain byte-exact; an unusual size is recorded separately from a wrong asset family.
The new unwired alternatives, genuinely new mechanic artwork, and new art replacing vanilla placeholders remain intact.
A5 is not marked fully complete because its missing-art and decision-family/size outputs are unfinished.

### A5-only resumed check — 12 October 2026

The resumed work was explicitly limited to these unfinished A5 outputs; the completed A3/A4/A6/A7 work and the original 935-file restoration were not repeated.
Commit `e5a528fc7df3bd789fced175c62a29f95d7ddda1` had changed the five Holy Realm decision icon fields from `GFX_decision_holy_realm_dhyana_seal_animated` to the static seal.
Commit `f501fbddf4d60efb96febacc99c49d926fc128e9` restores those exact five values from its parent `b25b185892761d98980bad32b5300a101fdd7d14`.
No other decision field, cost, trigger, effect, or AI weight changed.
The existing animation DDS equals that source parent's LFS OID `9f28334cf717a293085ee4dea9fae524606768d3d8f9f15daf9703f606e8cd37`; its unchanged 1152×96 sheet contains twelve 96×96 frames at the original eight frames per second.
The existing sprite registration matches the source parent exactly, and all twelve native frames were inspected from a review-only decode without altering runtime art.
Its recovered binding resolves the missed historical reroute but does not convert the inherited animation into a decision-sized texture.

The 36 Event 016 ideas were rechecked at source snapshot `f501fbddf4d60efb96febacc99c49d926fc128e9`.
The 24 aftermath definitions first appear in `5ca199ffbb6c836459ec27b423de7196be9e6554`, and the twelve focus definitions first appear in `008fc6000f914e0e9c1a6b3f67297973e217dff9`.
Their introduction and current blocks have no picture field; no verified former-name link, historical own-id sprite, exact original DDS path, or matching local source artifact was found.
The scoped definitions and registrations have no later changes since the earlier audit, and same-folder alternatives lack an original binding or provenance for these slots.
Per-ID introduction commits, definition hashes, examined paths, and exclusions are retained in `.tmp/restore_assets_audio/resume_a5/ideas/idea_history_provenance.json`.

The two Event 037 hotspot decisions first appear with the category icon in `afad1de2b842a11fa108a451a84386f7dd94a082`; the decision and GFX files do not exist in its parent.
No older decision-family binding exists to restore for either selector.
The vanilla `FRA_matignon_agreements` binding is already present in the initial legacy idea history and is unchanged by the July event-file split `5f00dbea7a44080a981f47d71eec9e52245fc36d`.
Case-insensitive all-history texture-path searches and the installed game, mod, and local asset-cache scans found no recoverable original DDS.
The only local matches are previous inventories and audit references, not original artwork.
Generated 34×34 Holy Realm alternatives under `docs/assets/gfx_fix_holy_resume` remain unbound and untouched because they are replacement candidates rather than the original pre-change artwork.

Current evidence is grouped under `.tmp/restore_assets_audio/resume_a5/`, including the offending binding diff, original sheet hash/header, original native-frame review, and the remaining-family source snapshot.
The resume used the connected MCP decision-icon section at offline `Decision modding - Hearts of Iron 4 Wiki.md`, lines 111–127, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, graphical `frameAnimatedSpriteType` section, lines 101–140, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, and installed decision documentation, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
MCP source lookup confirms the unchanged animated registration at `interface/003_holy_realm.gfx`, lines 277–286, source revision `53ebe7d933ccbd3d4b8ad0e58a02209d0f0af8ae8afec271af242642b72ca747`; reference coverage was not complete and was supplemented by direct consumer reads.
Installed vanilla `interface/alerts.gfx`, lines 3–13, supplies the matching frame-animation structure.
No new artwork, resizing, substitution, game launch, or push was used on resume.

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
The complete history review restores 165 unique currently consumed portrait DDS paths across 23 first replacement commits.
The parent independently hashed all 165 installed files against the final manifest's historical LFS OIDs, with no mismatches.
The final crosswalk is `.tmp/restore_assets_audio/portraits/final_manifest.json`, including paths, parent OIDs, current hashes, dimensions, consumers, and the six same-path replacement chains.
Nineteen genuinely added portrait paths and 52 deleted/unwired or retired paths are excluded from replacement restoration, with individual dispositions in that manifest.
Two inherited DXGI 91 DDS files required FFmpeg for review-only PNG decoding; their runtime bytes were preserved unchanged.

| First replacement | Exact restore source | Unique current portraits |
| --- | --- | ---: |
| `3098ed9d2b` | `2e44610483` | 5 |
| `97e51769f1` | `72783cb918` | 8 |
| `a5da081507` | `8fc6276c7f` | 8 |
| `e5ff42fed4` | `dffc390094` | 8 |
| `8f3279492e` | `e5ff42fed4` | 8 |
| `0f351f989e` | `f3f6727575` | 8 |
| `3485c371e1` | `c211f605b1` | 8 |
| `42be14e65a` | `3485c371e1` | 8 |
| `a7e384f6bb` | `1942c10660` | 5 |
| `bab17a7847` | `446ffb4ca2` | 1 |
| `250b9f1f06` | `3c09c71744` | 1 |
| `79a669512a` | `b85220482c` | 2 |
| `d92a67c4a8` | `79a669512a` | 12 |
| `36b6585eda` | `affec7c4e5` | 12 |
| `7dfaa32292` | `36cbc48ae3` | 1 |
| `a7227b7487` | `e5a528fc7d` | 16 |
| `7a30b87c0b` | `6c50c964ee` | 6 |
| `1cb4d061fb` | `b6bc6b4210` | 4 |
| `34559caed6` | `569e22ca6f` | 4 |
| `e8a307393a` | `29b582d0d6` | 11 |
| `9aaeb596a0` | `e8a307393a` | 11 |
| `2f506bc816` | `9aaeb596a0` | 11 |
| `ad741f951f` | `2f506bc816` | 7 |

The eleven portrait restore commits are `59267b7c8c`, `85594b9971`, `dc9d31e380`, `75bb1f633a`, `ebcc55bfd5`, `c888f80392`, `b456340082`, `2eec6523f2`, `bfe0bf648f`, `a376c644a7`, and `12b431f69f`.

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
Commit `753397bb5b9212931eed16b63a8236cc892174d3` restores 23 of those existing textures from the first replacement parents since 1 September 2026.
The offending commits are `6d3dc8283`, `f0f2ea3aa`, `cf6e7a637`, `ba4dc3e98`, `37e369007`, `001014065`, `bc3a45d86`, `d6280f69c`, and `65b1bb762`; every source is that commit's parent.
The source/byte reviewer verified all 23 historical LFS hashes and the 28 unchanged aliases consuming those files, each with two frames on a 60×12 DDS.
The parent reviewed the complete commit diff and the before/original contact sheet.
The full source and hash matrix is `.tmp/restore_assets_audio/parent/counter_texticon_manifest.json`; the offending pointer diffs are retained in `counter_texticon_offending_diffs.patch`.
The aliases and genuinely new textures remain.

## Reference evidence and scope

The connected MCP reference routes were exposed and used.
Offline wiki `Localisation - Hearts of Iron 4 Wiki.md`, lines 221–243, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was read for texticon names and frame handling.
Offline wiki `Graphical asset modding - Hearts of Iron 4 Wiki.md`, lines 30–100, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, was read for sprite texture and frame definitions.
Installed `common/scripted_guis/_documentation.md`, lines 30–69, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, was read for icon/image properties.
The installed documentation search contains no `texturefile` section; the actual installed `interface/texticons.gfx` and motorized DDS provide the vanilla precedent.
MCP source lookup confirmed the sole mod motorized sprite at `interface/chaosx_texticons.gfx`, lines 95–100, source revision `a2301aa9219ccce460b5efd3994c88604804c3e4b1ab9c84df46fc0e988ed20c`.
This evidence establishes source routing and binary identity; Hearts of Iron IV was not launched.
The late MCP idea-picture reference search returned `Transport closed` once.
No retry was useful for that transport failure; the relevant offline wiki `Idea modding - Hearts of Iron 4 Wiki.md`, lines 93–98, SHA-256 `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac`, and installed `common/ideas/italy.txt` picture fields were read directly for prefix and idea-id sprite precedence.
This current selection record supersedes runtime-selection claims in the historical repaint handoffs for the restored paths; their historical sources and review results are retained unchanged.
The Black Plague binding repair used offline `Decision modding - Hearts of Iron 4 Wiki.md`, lines 111–125, SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, installed `common/decisions/_documentation.md`, lines 1–45, SHA-256 `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, and the vanilla decision sprite precedent in `interface/decisions.gfx`, lines 1102–1105.
Its exact prior binding is in `3deac2d4d^:common/decisions/biowarfare_disease_containment_decisions.txt`; no gameplay body was changed.

Skills used: `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-decisions-missions`, `chaos-redux-frame-animation`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`, with specialist system skills used by the icon worker where consumers require them.
No skills were created or updated.
No restoration was simplified, and no replacement artwork was invented; the incomplete requested A5 outputs are explicitly listed above.
