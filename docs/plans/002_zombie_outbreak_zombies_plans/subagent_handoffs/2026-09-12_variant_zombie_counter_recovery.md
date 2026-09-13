# Variant zombie counter recovery handoff

Disposition: `implemented` for bounded artifact production and `needs_user_review` for parent visual acceptance.

This handoff covers only the four requested bespoke counter packages: `parasitic_zombies`, `mutant_zombies`, `necrotic_zombies`, and `demonic_zombies`.

The owned files are each exact `docs/assets/002_zombie_outbreak/models_3d/<unit>/counters/` folder and this handoff file.

No runtime GFX or DDS file, model file, gameplay file, localisation file, sound file, dependency lock, or parent package manifest was edited.

## Reference gate

The installed vanilla definition was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` before production.

The exact installed references were read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

The canonical contact sheets were inspected before the individual reference PNGs at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.

The canonical individual review PNGs were `.../units/land/counters_large/unit_infantry_icon.png` and `.../units/land/map_counters/onmap_infantry.png` under that same canonical reference root.

The large reference is a 152x42 RGBA two-frame strip with 76x42 frames, and the small reference is a 60x12 RGBA two-frame strip with 30x12 frames.

Frame order follows the installed consumer: frame 0 is the normal state and frame 1 is the pale sparse schematic state.

The installed normal large palette contains the required exact `#496a49` RGB anchor, and the corrected palette mapper selects from that native palette without arbitrary color injection.

All produced visible RGB values are sampled from the corresponding installed reference frame palette; no arbitrary green, renamed vanilla art, copied existing counter, or resized unrelated icon was used.

## Production method

All sixteen selected source frames were generated with native ImageGen calls requesting genuine transparency in the initial call, a single centered subject, and no frame, text, terrain, checkerboard, or opaque background.

The unmodified native outputs are retained as `source/imagegen_large_frame0.png`, `source/imagegen_large_frame1.png`, `source/imagegen_small_frame0.png`, and `source/imagegen_small_frame1.png` in every unit package.

Exact native ImageGen origin paths are recorded in each package's `source/native_imagegen_origins.md`, and source-copy hashes are recorded in both that origin record and `validation.json`.

The existing model visibility references supplied anatomy guidance only and were never used as runtime source pixels.

## Compact small-counter silhouette refresh

Parent visual review rejected the prior full-body small normal and alternate states because the native 30x12 map-counter render reduced several identities to a thin vertical streak or otherwise lost the inspected vanilla head and helmet silhouette family. The prior selected small source frames, processed frames, sheets, DDS files, decoded round-trips, and review previews remain preserved under each package's `source/rejected_silhouette_imagegen_small_frame*.png`, `source/candidates/rejected_small_frame*_silhouette_legibility.png`, and `previews/rejected_small_silhouette_legibility*` paths and are recorded as excluded evidence in `validation.json` and `candidate_lineage.json`.

The refreshed small states are original transparent compact head and upper-shoulder emblems generated with native ImageGen calls and then mapped through the existing inspected vanilla palette and alpha workflow. Parasitic retains a bulbous one-sided parasite growth and one curled tendril beside a broad skull; mutant retains a broad helmet-like skull, thick snarling jaw, and massive neck; necrotic retains a gaunt exposed skull and ragged upper neck with torn bony shoulders; demonic retains swept horns and bold bat-wing edge silhouettes. No runtime or shared files were edited.

The refreshed source origins and prompts are recorded in each package's `source/native_imagegen_origins.md` and `prompts/generation_prompts.md`. The compact source origin inventory is:

| Unit | Small frame 0 native origin | SHA256 | Small frame 1 native origin | SHA256 |
| --- | --- | --- | --- | --- |
| parasitic_zombies | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-0ec2e001-3a68-4278-9c5a-c3379a0e83da.png` | `299480b50e78a939597bd79656d65f6d8b65db87a124c7afa1a31447cc70d5ea` | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-226c52d2-3270-4cb2-b164-8ade4e81e5e4.png` | `7a53f507862d90737370fdea0c3b7b69c7ad009abb18282f2ab9506efc255ae7` |
| mutant_zombies | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-d40f96df-7fc4-4edc-a387-200cc6731a4f.png` | `754ba076df783c4e458b04773b1859fb551cf0fbf006535929d34f4c6a7c3795` | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-4d0b6516-40e6-47df-bf46-4a995a05b7a7.png` | `81f37a3047c516c7013384e8948c208678a83e4f95739af5b9efe2d4e0d07392` |
| necrotic_zombies | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-705e03e3-bc13-40bc-a39b-f7f2ce995e75.png` | `bb3eec36e598dc0f19a5d61a93913e6f149b345b4446c664899944b2dfe89518` | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-5ec5489c-2ec4-4bc1-855e-f9dbe35782b7.png` | `427858a96bcbdd8c5732b44572a72157fc8bc2086ad658487b0dea05001fa9f5` |
| demonic_zombies | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-21e7b297-6abf-4a9a-9e61-82297b67b636.png` | `6e05a46538ed08b7ea6fc92bfcfc8d0c0be78ae471ee3d53d5a1a6bb5b51c365` | `C:/Users/klimp/.codex/generated_images/01a0962c-4404-7d32-a4b8-79ffdcc1365c/exec-75385faf-13f2-4a0a-a97f-aeac01c15791.png` | `46826aa6e6029af1904ac9544890ab8fc9c34d93cdafb6cb596838d2fdc1bc42` |

The standard selected small source names contain the same bytes as the explicit compact copies under each package. All four new small sources were initially requested with genuine transparency; no chroma key, painted canvas, or halo was introduced.

The refreshed small evidence output inventory is:

| Unit | Processed 60x12 small sheet SHA256 | Evidence small DDS SHA256 | Pixel-equal decoded round-trip SHA256 | Same-dark-backing compare SHA256 |
| --- | --- | --- | --- | --- |
| parasitic_zombies | `a2e876ce86a4fae362a1f24515ddcedac32797915dab1d6f78dcaed15b58bb2e` | `e81b9437b453df301798deb869efa30fa6e4ea4fab62327bb73b178858e7b610` | `a2e876ce86a4fae362a1f24515ddcedac32797915dab1d6f78dcaed15b58bb2e` | `0ea030e429e694f6bdec3fb89a7591136e0e9ce7678d9d447adfb11731a9320a` |
| mutant_zombies | `cd78fa7a8ae0c4570e87a25ca3c20f18c9601c413d8c6716247f42491e7f56fb` | `fd1a34d9ed67c698c55e34737fdec38cd1f87b4852d60376d9afc95ad702d15e` | `cd78fa7a8ae0c4570e87a25ca3c20f18c9601c413d8c6716247f42491e7f56fb` | `bb908a26f898c2b2caf3a989e1c4cc919cb5fffcfe9aa190b89bc3af6755085e` |
| necrotic_zombies | `e917c0b3390ad671e1faa45ea638b55a5d7b87fcf68690081879ad0a5612a6d9` | `608ab29861f13a8822107c9a07e9ecaf8b6915097471faad948cf20c412923a9` | `e917c0b3390ad671e1faa45ea638b55a5d7b87fcf68690081879ad0a5612a6d9` | `fe41d537428f6744a1f9f3cef8431d5417a44ef0b09b3ef81df240f9a3407079` |
| demonic_zombies | `a823aa7aef760b7f4ab7b53c58d1148c7d8d204e86bbda43f0f8120ea2ddd9a2` | `74309a6526b39906d31659e4b91dc8c4e0531848727145e2947b16312d7e3116` | `a823aa7aef760b7f4ab7b53c58d1148c7d8d204e86bbda43f0f8120ea2ddd9a2` | `4bb45843b6c66d5bf0fd7ab275a94b47887d50012582eed1d9684392445ee5ea` |

The exact paths for the first four columns are respectively `processed/small_onmap_unit_<unit>_icon.png`, `small/onmap_unit_<unit>_icon.dds`, and `decoded/small_<unit>_icon_roundtrip.png` under each unit package. The compare path is `previews/small_normal_vs_vanilla_review.png` under each unit package. The combined all-unit review is `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/previews/small_compact_four_unit_vs_vanilla_review.png` with SHA256 `8fecd2478e0525046df3c0633b5376aea50b07f1d36d1eea9e8204e211901471`.

The new normal small frames have opaque/partial pixel counts and opaque luma ranges of 94/37 and 94/190/236 for parasitic, 79/40 and 94/192/236 for mutant, 74/45 and 109/189.5/236 for necrotic, and 80/47 and 94/192/236 for demonic. These remain within the installed opaque pale frame-0 value distribution, and all four package validations remain `needs_user_review` pending parent visual acceptance.

Parasitic art uses the measured neutral front reference and preserves the bulbous one-sided parasitic shoulder/head growth, dominant claw, and hanging tendrils.

Mutant art uses the recovered neutral front reference and preserves the heavy asymmetric body, long oversized arms, and dragging hands.

Necrotic art uses the recovered neutral front reference and preserves the thin decayed humanoid, narrow shoulders, sagging torso, and bone-like gaps.

Demonic art uses both resume neutral front and neutral right references and preserves the bat wings, hooked claws, angular horns, digitigrade legs, and clawed feet.

Several native sources contained low-alpha halo values, so the verified Pillow 11.1.0 fallback cleared only source alpha values 1..31 before premultiplied resize; untouched sources remain preserved and RGB was never used as a chroma key.

The corrected mapper uses float luminance arithmetic and the full sampled value distribution; `validation.json` records exact `#496a49` presence when the source luminance naturally selects that native palette entry.

The small normal mapper is separately calibrated by rank-mapping source core luminance to the installed map-counter frame 0 opaque palette at alpha >=254, whose measured luma range is 94/189/236 minimum/median/maximum, then reinforcing only resized interior alpha values 128..254 to 255 while preserving edge alpha values 0..127.

The refreshed compact small normal outputs have opaque/partial pixel counts and opaque luma ranges of 94/37 and 94/190/236 for parasitic, 79/40 and 94/192/236 for mutant, 74/45 and 109/189.5/236 for necrotic, and 80/47 and 94/192/236 for demonic. The installed pale frame-0 range remains 94/189/236 minimum/median/maximum, and the refreshed output keeps transparent edges without a painted backing.

The repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced the evidence DDS files, and every decoded DDS round-trip is pixel-equal to its processed PNG sheet.

## Runtime identifiers and parent boundary

Each package records the exact large token `GFX_unit_<unit>_icon_medium`, small token `GFX_unit_<unit>_icon_medium_white`, large destination `gfx/interface/counters/divisions_large/unit_<unit>_icon.dds`, small destination `gfx/interface/counters/divisions_small/onmap_unit_<unit>_icon.dds`, owning definition `interface/chaosx_subuniticons.gfx`, unit consumer `common/units/zombies.txt`, and sprite consumer `chaosx_<unit>`.

The existing runtime destinations were preserved for parent review and are not claimed as updated.

All eight current runtime DDS files exist at 152x42 or 60x12 but have different SHA256 bytes from the new evidence DDS files, so the current runtime/evidence discrepancy is intentional and recorded below.

`armored_necrotic_zombies` and `armored_demonic_zombies` resolve shared sprites in `common/units/zombies.txt` but armored counters are outside this bounded task.

## Artifact inventory and hashes

The following hashes are SHA256 of the exact files in the workspace at handoff time.

| Unit | Role | Workspace path | SHA256 |
| --- | --- | --- | --- |
| parasitic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_large_frame0.png` | `377475e911a970c36fd8b1d8eaa9c53767dfb3b9f8804b2eeabe5e46dab1c8c8` |
| parasitic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_large_frame1.png` | `3a5a013d3c8311c81b230b13d752f2d46d2a0ef678579f5ac7f79b51e1bbd19f` |
| parasitic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_small_frame0.png` | `299480b50e78a939597bd79656d65f6d8b65db87a124c7afa1a31447cc70d5ea` |
| parasitic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_small_frame1.png` | `7a53f507862d90737370fdea0c3b7b69c7ad009abb18282f2ab9506efc255ae7` |
| parasitic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/processed/large_unit_parasitic_zombies_icon.png` | `b72f4f3a49454a35e8cad72f84444fbc7bf2c5d29017585cb151282b6dd304e4` |
| parasitic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/processed/small_onmap_unit_parasitic_zombies_icon.png` | `a2e876ce86a4fae362a1f24515ddcedac32797915dab1d6f78dcaed15b58bb2e` |
| parasitic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/large/unit_parasitic_zombies_icon.dds` | `c5f830fd94f874e31343071e3d3b905f06939e0e2fdd86664fe4a5829c52f07c` |
| parasitic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/small/onmap_unit_parasitic_zombies_icon.dds` | `e81b9437b453df301798deb869efa30fa6e4ea4fab62327bb73b178858e7b610` |
| parasitic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/decoded/large_parasitic_zombies_icon_roundtrip.png` | `b72f4f3a49454a35e8cad72f84444fbc7bf2c5d29017585cb151282b6dd304e4` |
| parasitic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/decoded/small_parasitic_zombies_icon_roundtrip.png` | `a2e876ce86a4fae362a1f24515ddcedac32797915dab1d6f78dcaed15b58bb2e` |
| mutant_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_large_frame0.png` | `9bcd174ae7b1fb11062381ba5e2454273fe1840e72494d89951a59cd9be0ce61` |
| mutant_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_large_frame1.png` | `7acb8755544f6f7d402c0ddfc3199ccd8f5590baf3514e206b29aa3a72b2ef72` |
| mutant_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_small_frame0.png` | `754ba076df783c4e458b04773b1859fb551cf0fbf006535929d34f4c6a7c3795` |
| mutant_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_small_frame1.png` | `81f37a3047c516c7013384e8948c208678a83e4f95739af5b9efe2d4e0d07392` |
| mutant_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/processed/large_unit_mutant_zombies_icon.png` | `8a9569526fc18f4c3933a2c131a15010e8e0ffb06bd81040a1d9ec59517e93c4` |
| mutant_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/processed/small_onmap_unit_mutant_zombies_icon.png` | `cd78fa7a8ae0c4570e87a25ca3c20f18c9601c413d8c6716247f42491e7f56fb` |
| mutant_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/large/unit_mutant_zombies_icon.dds` | `556371d5321dd354b2d66edbe3e58ee92cbde85539cb0ff30975e1b40b9b464b` |
| mutant_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/small/onmap_unit_mutant_zombies_icon.dds` | `fd1a34d9ed67c698c55e34737fdec38cd1f87b4852d60376d9afc95da702d15e` |
| mutant_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/decoded/large_mutant_zombies_icon_roundtrip.png` | `8a9569526fc18f4c3933a2c131a15010e8e0ffb06bd81040a1d9ec59517e93c4` |
| mutant_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/decoded/small_mutant_zombies_icon_roundtrip.png` | `cd78fa7a8ae0c4570e87a25ca3c20f18c9601c413d8c6716247f42491e7f56fb` |
| necrotic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_large_frame0.png` | `3b7ae85867576d9f0c8e85eaddd44bbb3cf8c102ea48b9095024892cbe6a91bc` |
| necrotic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_large_frame1.png` | `35c1c269f6821cbf549b113f802f2ba81130d6638f1d4db8e04e57b9c69a9696` |
| necrotic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_small_frame0.png` | `bb3eec36e598dc0f19a5d61a93913e6f149b345b4446c664899944b2dfe89518` |
| necrotic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_small_frame1.png` | `427858a96bcbdd8c5732b44572a72157fc8bc2086ad658487b0dea05001fa9f5` |
| necrotic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/processed/large_unit_necrotic_zombies_icon.png` | `2a62c7495a7339ff146b2a3a653e8898671c7ddcf33c1e711cb2144da7081c21` |
| necrotic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/processed/small_onmap_unit_necrotic_zombies_icon.png` | `e917c0b3390ad671e1faa45ea638b55a5d7b87fcf68690081879ad0a5612a6d9` |
| necrotic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/large/unit_necrotic_zombies_icon.dds` | `3e8a06e6eb8355e6e2732afa5670730f936cffd79465201b86a6a5bef5077756` |
| necrotic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/small/onmap_unit_necrotic_zombies_icon.dds` | `608ab29861f13a8822107c9a07e9ecaf8b6915097471faad948cf20c412923a9` |
| necrotic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/decoded/large_necrotic_zombies_icon_roundtrip.png` | `2a62c7495a7339ff146b2a3a653e8898671c7ddcf33c1e711cb2144da7081c21` |
| necrotic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/decoded/small_necrotic_zombies_icon_roundtrip.png` | `e917c0b3390ad671e1faa45ea638b55a5d7b87fcf68690081879ad0a5612a6d9` |
| demonic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_large_frame0.png` | `39c67e646fe227621bc74d22d1f783e4b91a4c0a2bf40472079872f21c6ad340` |
| demonic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_large_frame1.png` | `257656174e9d3c8631f2f3f7ee7986e51ae46a7c4b664fb19b74861ce70ef63d` |
| demonic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_small_frame0.png` | `6e05a46538ed08b7ea6fc92bfcfc8d0c0be78ae471ee3d53d5a1a6bb5b51c365` |
| demonic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_small_frame1.png` | `46826aa6e6029af1904ac9544890ab8fc9c34d93cdafb6cb596838d2fdc1bc42` |
| demonic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/processed/large_unit_demonic_zombies_icon.png` | `06618f6fb5bb94bc54211abcf7a5e29d24b96fb4d332097247c0f2381348fa19` |
| demonic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/processed/small_onmap_unit_demonic_zombies_icon.png` | `a823aa7aef760b7f4ab7b53c58d1148c7d8d204e86bbda43f0f8120ea2ddd9a2` |
| demonic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/large/unit_demonic_zombies_icon.dds` | `fcccd9a15b7ef4286c0aae3b0cd1a90aba1d543c4060e0147bf34575937dda08` |
| demonic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/small/onmap_unit_demonic_zombies_icon.dds` | `74309a6526b39906d31659e4b91dc8c4e0531848727145e2947b16312d7e3116` |
| demonic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/decoded/large_demonic_zombies_icon_roundtrip.png` | `06618f6fb5bb94bc54211abcf7a5e29d24b96fb4d332097247c0f2381348fa19` |
| demonic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/decoded/small_demonic_zombies_icon_roundtrip.png` | `a823aa7aef760b7f4ab7b53c58d1148c7d8d204e86bbda43f0f8120ea2ddd9a2` |

Each package also contains `manifest.md`, `prompts/generation_prompts.md`, `source/native_imagegen_origins.md`, `candidate_lineage.json`, `validation.json`, `previews/contact_sheet.png`, `previews/alpha_contrast_review.png`, `previews/small_normal_vs_vanilla_review.png`, and `sha256sums_artifacts.txt`.

## Existing runtime discrepancy

These are the current preserved runtime hashes, compared with the newly produced evidence hashes above.

| Unit | Runtime path | Current runtime SHA256 | Evidence SHA256 | Match |
| --- | --- | --- | --- | --- |
| parasitic_zombies | `gfx/interface/counters/divisions_large/unit_parasitic_zombies_icon.dds` | `d41ebb36df5d11c43a853646e111a2f38215c9845695e9b5b65c5a78738e35a1` | `c5f830fd94f874e31343071e3d3b905f06939e0e2fdd86664fe4a5829c52f07c` | no |
| parasitic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_parasitic_zombies_icon.dds` | `ee0973f34cedca5593f4bfd4d84efecfab80731ef7c0e6e470c55effce79abe9` | `e81b9437b453df301798deb869efa30fa6e4ea4fab62327bb73b178858e7b610` | no |
| mutant_zombies | `gfx/interface/counters/divisions_large/unit_mutant_zombies_icon.dds` | `41a03a4fcff3fe7409dbb68e5dde7a56747f06ce1c39152792abdb56569a597a` | `556371d5321dd354b2d66edbe3e58ee92cbde85539cb0ff30975e1b40b9b464b` | no |
| mutant_zombies | `gfx/interface/counters/divisions_small/onmap_unit_mutant_zombies_icon.dds` | `4f3f3d2080a6a66390eae72004645494c17bb142bf67a04ca7e4c2af7271b08a` | `fd1a34d9ed67c698c55e34737fdec38cd1f87b4852d60376d9afc95da702d15e` | no |
| necrotic_zombies | `gfx/interface/counters/divisions_large/unit_necrotic_zombies_icon.dds` | `f6497cb84905cc10a70c82590d8e952e5a1b2e4d07f5c6805ef35ffc07843b01` | `3e8a06e6eb8355e6e2732afa5670730f936cffd79465201b86a6a5bef5077756` | no |
| necrotic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_necrotic_zombies_icon.dds` | `48a931b536feac9c315ace0c9b057268bf65cb81648de3e176cf7a21341262a3` | `608ab29861f13a8822107c9a07e9ecaf8b6915097471faad948cf20c412923a9` | no |
| demonic_zombies | `gfx/interface/counters/divisions_large/unit_demonic_zombies_icon.dds` | `dd657c7eba183cffc7346896b95378ffb965397dd033c57646ccb0fc75274e9f` | `fcccd9a15b7ef4286c0aae3b0cd1a90aba1d543c4060e0147bf34575937dda08` | no |
| demonic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_demonic_zombies_icon.dds` | `a6f63d46e73ba827cb378b98391ebac7c7042f5af23ceab80ec5b4aeeebfa92e` | `74309a6526b39906d31659e4b91dc8c4e0531848727145e2947b16312d7e3116` | no |

## Review evidence and limits

The four `previews/contact_sheet.png` files show native-size sheets enlarged for review beside decoded DDS round-trips, and the `previews/alpha_contrast_review.png` files show dark/light backing checks.

The four `previews/small_normal_vs_vanilla_review.png` files place the installed vanilla map-counter frame 0 beside the refreshed compact candidate at native-size labels enlarged 10x on the same dark backing for direct contrast and anatomy review. The combined four-unit comparison is `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/previews/small_compact_four_unit_vs_vanilla_review.png` and places the installed frame beside all four refreshed normal states on the same backing.

The four `previews/rejected_palette_overflow_*` sets retain the earlier processor outputs as rejected comparison evidence after an int16 reference-luminance overflow was found and corrected.

The four `previews/rejected_small_normal_contrast*` sets retain the pre-calibration small normal outputs after opaque map-counter luminance and coverage review found insufficient contrast; their paths and hashes are recorded in each `validation.json` and `candidate_lineage.json`.

The four `previews/rejected_small_silhouette_legibility*` sets retain the pre-refresh full-body small outputs after same-background native-size review found insufficient head and upper-shoulder identity; the prior selected source copies are retained under each package `source/` folder and their paths and hashes are recorded in each `validation.json` and `candidate_lineage.json`.

The `validation.json` files confirm exact dimensions, two-frame order, sampled palette-subset checks, source alpha evidence, corrected value distribution, DDS header structure, and pixel-equal DDS decoding.

The packages are ready for parent visual review and promotion review; no in-game acceptance claim is made. Per the parent coordination constraint, this compact refresh is intentionally left unstaged and uncommitted for review.

The only deliberate simplification is that native ImageGen source detail is reduced to the exact vanilla counter footprints and sampled palettes required by the consumer; the source PNGs and processing evidence remain available for review.
